#!/usr/bin/env python3
"""Download one state's National Register of Historic Places listings from the National Park Service, for the
historic-pockets layer (tools/pockets.py).

   python3 tools/nrhp_state.py "NEW YORK" ny        writes cache/nrhp/ny.json

The Park Service publishes two layers: points, and polygons for listings that have a mapped boundary (most historic
districts). Each listing is kept once, with its name, kind (building, district, site, structure, object), town,
the number of contributing buildings it counts, a centre point, and for districts a simplified outline.
The data is a work of the US government and in the public domain. The Park Service warns that positions are
approximate (many are a single coordinate from the nomination form) and that a listing may no longer stand."""
import sys,os,json,time,urllib.request,urllib.parse
if len(sys.argv)<3: sys.exit(__doc__)
STATE,KEY=sys.argv[1].upper(),sys.argv[2]
B='https://mapservices.nps.gov/arcgis/rest/services/cultural_resources/nrhp_locations/MapServer/'; UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
F='NRIS_Refnum,RESNAME,ResType,City,County,NumCBldg,Is_NHL,CertDate'
def pull(layer):
    out=[]; off=0
    while True:
        q=urllib.parse.urlencode({'where':f"State='{STATE}'",'outFields':F,'outSR':4326,'geometryPrecision':5,'orderByFields':'OBJECTID','resultOffset':off,'resultRecordCount':1000,'f':'json'})
        for k in range(5):
            try:
                j=json.loads(urllib.request.urlopen(urllib.request.Request(B+f'{layer}/query?'+q,headers=UA),timeout=180).read())
                if 'error' in j: raise ValueError(str(j['error'])[:100])
                break
            except Exception as e:
                if k==4: raise
                print('  retry',str(e)[:70],flush=True); time.sleep(8*(k+1))
        fs=j.get('features',[]); out+=fs; off+=len(fs); print('  layer',layer,off,flush=True)
        if len(fs)<1000: break
    return out
def simp(ring,tol=0.0002):
    """Thin a ring to points at least tol degrees apart (about 20 m); enough for an outline on a phone."""
    o=[ring[0]]
    for p in ring[1:]:
        if abs(p[0]-o[-1][0])>tol or abs(p[1]-o[-1][1])>tol: o.append(p)
    if o[-1]!=ring[-1]: o.append(ring[-1])
    return [[round(y,5),round(x,5)] for x,y in o]
L={}
for f in pull(0):
    a=f['attributes']; g=f.get('geometry')
    if not g or g.get('x') is None: continue
    L[a['NRIS_Refnum']]={'ref':a['NRIS_Refnum'],'n':(a['RESNAME'] or '').strip(),'k':(a['ResType'] or '').lower(),'town':a['City'] or '','county':a['County'] or '','cb':a['NumCBldg'] or 0,'nhl':bool(a['Is_NHL']),'y':(a['CertDate'] or '')[:4],'lat':round(g['y'],5),'lon':round(g['x'],5)}
for f in pull(1):
    a=f['attributes']; g=f.get('geometry')
    if not g or not g.get('rings'): continue
    ring=max(g['rings'],key=len); xs=[p[0] for p in ring]; ys=[p[1] for p in ring]
    e=L.get(a['NRIS_Refnum']) or {'ref':a['NRIS_Refnum'],'n':(a['RESNAME'] or '').strip(),'k':(a['ResType'] or '').lower(),'town':a['City'] or '','county':a['County'] or '','cb':a['NumCBldg'] or 0,'nhl':bool(a['Is_NHL']),'y':(a['CertDate'] or '')[:4]}
    e['lat']=round((min(ys)+max(ys))/2,5); e['lon']=round((min(xs)+max(xs))/2,5)
    e['w']=round(max(max(xs)-min(xs),(max(ys)-min(ys))*1.35)*82000)        # widest extent in metres, roughly
    if e['k']=='district' and len(ring)>3: e['poly']=simp(ring)
    L[a['NRIS_Refnum']]=e
os.makedirs('cache/nrhp',exist_ok=True)
json.dump(list(L.values()),open(f'cache/nrhp/{KEY}.json','w'),separators=(',',':'),ensure_ascii=False)
from collections import Counter
print('wrote',f'cache/nrhp/{KEY}.json',len(L),'listings',dict(Counter(e['k'] for e in L.values())),'districts with an outline',sum(1 for e in L.values() if e.get('poly')))
