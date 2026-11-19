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
FIRST=['ny','mo','ks','ct','ri','vt','nh','me','nj','pa']
# Since November 19, 2026 the rest of the country and the ten provinces, each from its own outline's box
# (python3 tools/osm_leads_box.py --skip-mines --state <key> ...). These follow rules the first states do not:
#   - No Native American sites. Outside the Northeast most of what OpenStreetMap calls an archaeological site is one
#     (mounds, pueblos, rock art, heiau; 1,395 of Colorado's 1,822 raw leads were in Mesa Verde). They are not the
#     Atlas's subject and a map of leads is no place for them. Left out: every historic=archaeological_site, every name
#     that says so (NATIVE below), every lead on reservation or trust land (cache/tribal.json, from tools/tribal.py),
#     any other lead within DISTRICT metres of three or more of the sites left out by tag or by name, and every ruin
#     in FOURCORNERS (Cedar Mesa, Hovenweep, Mesa Verde and the Mancos valley), where a mapped "ruin" is nearly always
#     an ancestral Puebloan one whatever it is called ("Jailhouse Ruin", "Fallen Roof Ruin"). The rules are not
#     complete: a session that finds a lead is such a site leaves it alone and says so in its note.
#   - No mapped mine entrances (--skip-mines): the mines layer has the USGS records for every state.
MORE=['tx','hi','md','la','ca','id','il','tn','wi','ar','dc','ms','nd','ne','oh','az','fl','ga','wy','al','co','de','ia','in','ky','mi','mn','mt',
      'nc','nm','nv','ok','or','sc','sd','ut','va','wa','wv','ak','nb','ns','pe','nl','qc','on','mb','sk','ab','bc']
STATE_KEYS=FIRST+MORE
NATIVE=re.compile(r"pueblo|kiva\b|petrogly|pictogra|rock art|cliff dwell|indian (ruin|mound|village|burial)|anasazi|hohokam|sinagua|\bsalado\b|mogollon|\bmounds?\b|midden|heiau|pit ?houses?\b|totem|archa?eolog|great house",re.I)
DISTRICT=1500
FOURCORNERS=(-110.7,36.9,-108.1,38.0)      # west, south, east, north
# A clump of unnamed ruins is one lead, not fifty: an unnamed lead within CLUMP metres of another unnamed lead of the same
# kind is left out (a ghost town, a burnt street, the 1,394 hut sites of the Aleutian war bases). Named leads are all kept.
CLUMP=150
OLDBOX=(-75.35,41.45,-72.55,44.15)
_ST=json.load(open('build/states.json'))
def _inring(r,x,y):
    ins=False; n=len(r)//2; j=n-1
    for i in range(n):
        xi,yi,xj,yj=r[2*i],r[2*i+1],r[2*j],r[2*j+1]
        if (yi>y)!=(yj>y) and x<(xj-xi)*(y-yi)/(yj-yi)+xi: ins=not ins
        j=i
    return ins
def hav(a,b,c,d2):
    R=6371000; p=math.pi/180
    h=math.sin((c-a)*p/2)**2+math.cos(a*p)*math.cos(c*p)*math.sin((d2-b)*p/2)**2
    return 2*R*math.asin(math.sqrt(h))
_seen={(e['type'],str(e['id'])) for e in els}
REBUILT=[]; _TRIB=None; _cand=[]; _left=[]; _out={'tag or name':0,'reservation land':0,'Four Corners':0,'beside left-out sites':0}
def _tribal(x,y):
    global _TRIB
    if _TRIB is None:
        if not os.path.exists('cache/tribal.json'): sys.exit('cache/tribal.json is missing: run  python3 tools/tribal.py  first (reservation outlines; a minute).')
        _TRIB={}
        for r in json.load(open('cache/tribal.json'))['r']:
            for gx in range(int(math.floor(r[0])),int(math.floor(r[2]))+1):
                for gy in range(int(math.floor(r[1])),int(math.floor(r[3]))+1): _TRIB.setdefault((gx,gy),[]).append(r)
    return any(r[0]<=x<=r[2] and r[1]<=y<=r[3] and _inring(r[4],x,y) for r in _TRIB.get((int(math.floor(x)),int(math.floor(y))),()))
for k in STATE_KEYS:
    f=f'cache/osm/{k}_leads.json'
    if not os.path.exists(f): continue
    n=0; REBUILT.append(k)
    for e in json.load(open(f))['elements']:
        c=e.get('center') or e
        if 'lat' not in c or (e['type'],str(e['id'])) in _seen: continue
        if OLDBOX[0]<=c['lon']<=OLDBOX[2] and OLDBOX[1]<=c['lat']<=OLDBOX[3]: continue
        if not any(_inring(r,c['lon'],c['lat']) for r in _ST[k]): continue
        _seen.add((e['type'],str(e['id'])))
        if k in FIRST: els.append(e); n+=1; continue
        t=e.get('tags',{})
        if t.get('historic')=='archaeological_site' or NATIVE.search(t.get('name') or ''): _left.append((c['lat'],c['lon'])); _out['tag or name']+=1; continue
        if _tribal(c['lon'],c['lat']): _out['reservation land']+=1; continue
        if FOURCORNERS[0]<=c['lon']<=FOURCORNERS[2] and FOURCORNERS[1]<=c['lat']<=FOURCORNERS[3]: _out['Four Corners']+=1; continue
        _cand.append((k,e))
    if k in FIRST: print(k,'layer leads added',n)
if _cand:
    _lg={}
    for la,lo in _left: _lg.setdefault((int(la/0.05),int(lo/0.05)),[]).append((la,lo))
    _n={}
    for k,e in _cand:
        c=e.get('center') or e; a,b=int(c['lat']/0.05),int(c['lon']/0.05)
        if sum(1 for i in (a-1,a,a+1) for j in (b-1,b,b+1) for q in _lg.get((i,j),()) if hav(c['lat'],c['lon'],q[0],q[1])<DISTRICT)>=3: _out['beside left-out sites']+=1; continue
        els.append(e); _n[k]=_n.get(k,0)+1
    print('layer leads added:',' '.join(f'{k} {v}' for k,v in _n.items()))
    print('left out as Native American sites or ground:',', '.join((f'{v} by {k}' if k in('tag or name','reservation land') else f'{v} in the {k} box' if k=='Four Corners' else f'{v} {k}') for k,v in _out.items()))
S=json.load(open('build/sites.json'))
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
types=[]; pts=[]; drop=0; clump=0
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
    if not t.get('name') and any(p[3]=='' and p[2]==types.index(k) and hav(lat,lon,p[0],p[1])<CLUMP for p in _near(_pg,lat,lon)): clump+=1; continue
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
print(len(pts),'leads;',drop,'already Atlas places;',clump,'unnamed ones left out of clumps;',Counter(types[p[2]] for p in pts),sum(1 for p in pts if p[3]),'named')
