import json,math,re
d=json.load(open('cache/osm/leads.json')); els=d['elements'] if isinstance(d,dict) else d
import os
if os.path.exists('cache/osm/leads_ma.json'):
    _seen={(e['type'],e['id']) for e in els}
    els=els+[e for e in json.load(open('cache/osm/leads_ma.json'))['elements'] if (e['type'],e['id']) not in _seen]
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
for e in els:
    t=e.get('tags',{}); c=e.get('center') or e
    if 'lat' not in c: continue
    k=kind(t)
    if not k: continue
    lat,lon=c['lat'],c['lon']
    if any(abs(s['lat']-lat)<0.002 and hav(lat,lon,s['lat'],s['lon'])<150 for s in S): drop+=1; continue
    if any(abs(p[0]-lat)<0.0006 and hav(lat,lon,p[0],p[1])<40 and p[3]==(t.get('name') or '') for p in pts): continue
    if k not in types: types.append(k)
    pts.append([round(lat,5),round(lon,5),types.index(k),(t.get('name') or '')[:60]])
json.dump({'t':types,'p':pts},open('build/leads.json','w'),separators=(',',':'),ensure_ascii=False)
from collections import Counter
print(len(pts),'leads;',drop,'already Atlas places;',Counter(types[p[2]] for p in pts),sum(1 for p in pts if p[3]),'named')
