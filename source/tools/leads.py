import json,math,re
import os,sys
# The raw downloads are not in the repository. With the first Overpass download missing (a fresh workspace), the leads already
# in build/leads.json are kept and only the states whose layer file is present are rebuilt (see STATE_KEYS below).
HAVE_OLD=os.path.exists('cache/osm/leads.json')
if HAVE_OLD:
    d=json.load(open('cache/osm/leads.json')); els=d['elements'] if isinstance(d,dict) else d
else: els=[]
import os
if os.path.exists('cache/osm/leads_ma.json'):
    _seen={(e['type'],e['id']) for e in els}
    els=els+[e for e in json.load(open('cache/osm/leads_ma.json'))['elements'] if (e['type'],e['id']) not in _seen]
# Whole states downloaded with tools/osm_layers.py (cache/osm/<key>_leads.json). Inside New York the part covered by the
# first Overpass download (the box below) keeps that data; a state's layer data fills the rest of its outline.
STATE_KEYS=['ny','mo','ks','ct','ri','vt','nh','me','nj','pa']
OLDBOX=(-75.35,41.45,-72.55,44.15)
_ST=json.load(open('build/states.json'))
def _inring(r,x,y):
    ins=False; n=len(r)//2; j=n-1
    for i in range(n):
        xi,yi,xj,yj=r[2*i],r[2*i+1],r[2*j],r[2*j+1]
        if (yi>y)!=(yj>y) and x<(xj-xi)*(y-yi)/(yj-yi)+xi: ins=not ins
        j=i
    return ins
_seen={(e['type'],str(e['id'])) for e in els}
REBUILT=[]
for k in STATE_KEYS:
    f=f'cache/osm/{k}_leads.json'
    if not os.path.exists(f): continue
    n=0; REBUILT.append(k)
    for e in json.load(open(f))['elements']:
        c=e.get('center') or e
        if 'lat' not in c or (e['type'],str(e['id'])) in _seen: continue
        if OLDBOX[0]<=c['lon']<=OLDBOX[2] and OLDBOX[1]<=c['lat']<=OLDBOX[3]: continue
        if not any(_inring(r,c['lon'],c['lat']) for r in _ST[k]): continue
        _seen.add((e['type'],str(e['id']))); els.append(e); n+=1
    print(k,'layer leads added',n)
S=json.load(open('build/sites.json'))
def hav(a,b,c,d2):
    R=6371000; p=math.pi/180
    h=math.sin((c-a)*p/2)**2+math.cos(a*p)*math.cos(c*p)*math.sin((d2-b)*p/2)**2
    return 2*R*math.asin(math.sqrt(h))
def kind(t):
    h=t.get('historic',''); r=t.get('ruins',''); m=t.get('man_made','')
    if t.get('railway') in('abandoned','disused','razed') and not t.get('building') and h!='railway_station': return None
    if h in('mine','mine_shaft') or m in('mineshaft','adit') : return 'Old mine or shaft'
    if h=='quarry' or t.get('landuse')=='quarry' or 'quarry' in t.get('name','').lower(): return 'Old quarry'
    if h in('charcoal_pile',) or r=='charcoal_pit' or 'kiln' in (h+r+m+t.get('name','').lower()): return 'Kiln or charcoal pit'
    if h=='fort': return 'Fort site'
    if h=='archaeological_site': return 'Archaeological site'
    if h in('railway','railway_station') or r in('bridge','platform'): return 'Rail or bridge remains'
    if h=='farm' or r=='house': return 'Old farm or house'
    if h=='battlefield': return None
    if r in('ski_lift',): return 'Old ski area'
    if h=='ruins' or r or t.get('abandoned')=='yes' or t.get('disused')=='yes' or t.get('landuse')=='brownfield': return 'Mapped ruin'
    if h: return 'Mapped ruin'
    return None
types=[]; pts=[]; drop=0
from collections import defaultdict
_cell=lambda la,lo:(int(la/0.003),int(lo/0.003))
_sg=defaultdict(list)
for s_ in S: _sg[_cell(s_['lat'],s_['lon'])].append(s_)
_pg=defaultdict(list)
def _near(grid,la,lo):
    a,b=_cell(la,lo)
    for i in (a-1,a,a+1):
        for j in (b-1,b,b+1):
            for x in grid.get((i,j),()): yield x
for e in els:
    t=e.get('tags',{}); c=e.get('center') or e
    if 'lat' not in c: continue
    k=kind(t)
    if not k: continue
    lat,lon=c['lat'],c['lon']
    if any(abs(s['lat']-lat)<0.002 and hav(lat,lon,s['lat'],s['lon'])<150 for s in _near(_sg,lat,lon)): drop+=1; continue
    if any(abs(p[0]-lat)<0.0006 and hav(lat,lon,p[0],p[1])<40 and p[3]==(t.get('name') or '') for p in _near(_pg,lat,lon)): continue
    if k not in types: types.append(k)
    pts.append([round(lat,5),round(lon,5),types.index(k),(t.get('name') or '')[:60]]); _pg[_cell(lat,lon)].append(pts[-1])
if not HAVE_OLD:
    if not REBUILT: print('no raw OpenStreetMap download here; keeping the existing build/leads.json'); sys.exit(0)
    def _rebuilt(la,lo): return (not(OLDBOX[0]<=lo<=OLDBOX[2] and OLDBOX[1]<=la<=OLDBOX[3])) and any(_inring(r,lo,la) for k in REBUILT for r in _ST[k])
    old=json.load(open('build/leads.json')); kept=0
    for q in old['p']:
        if _rebuilt(q[0],q[1]): continue
        nm=old['t'][q[2]]
        if nm not in types: types.append(nm)
        pts.append([q[0],q[1],types.index(nm),q[3]]); kept+=1
    print('kept',kept,'leads from the existing build/leads.json outside',' '.join(REBUILT))
json.dump({'t':types,'p':pts},open('build/leads.json','w'),separators=(',',':'),ensure_ascii=False)
from collections import Counter
print(len(pts),'leads;',drop,'already Atlas places;',Counter(types[p[2]] for p in pts),sum(1 for p in pts if p[3]),'named')
