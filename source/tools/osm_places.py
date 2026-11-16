#!/usr/bin/env python3
"""Download the named settlements of one state (cities, towns, villages, hamlets) from the copy of OpenStreetMap
that Esri hosts, for tools/pockets.py, which uses them to tell an old town centre from any other pocket.

   python3 tools/osm_places.py ny        writes cache/osm/ny_places.json: [{n, lat, lon, p}]

A settlement's point in OpenStreetMap is placed at its centre: the green, the main crossroads, the old core.
Data is OpenStreetMap, © OpenStreetMap contributors, ODbL."""
import sys,os,json,time,urllib.request,urllib.parse
if len(sys.argv)<2: sys.exit(__doc__)
KEY=sys.argv[1]; RINGS=json.load(open('build/states.json'))[KEY]
xs=[r[i] for r in RINGS for i in range(0,len(r),2)]; ys=[r[i+1] for r in RINGS for i in range(0,len(r),2)]
W,E,S,N=min(xs)-0.02,max(xs)+0.02,min(ys)-0.02,max(ys)+0.02
U='https://services6.arcgis.com/Do88DoK2xjTUCXd1/arcgis/rest/services/OSM_NA_POIs/FeatureServer/0/query'; UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
def inring(r,x,y):
    ins=False; n=len(r)//2; j=n-1
    for i in range(n):
        xi,yi,xj,yj=r[2*i],r[2*i+1],r[2*j],r[2*j+1]
        if (yi>y)!=(yj>y) and x<(xj-xi)*(y-yi)/(yj-yi)+xi: ins=not ins
        j=i
    return ins
out={}
for c in range(4):
    w=W+(E-W)*c/4; e=W+(E-W)*(c+1)/4; off=0
    while True:
        p={'where':"place IN ('city','town','village','hamlet')",'geometry':f'{w},{S},{e},{N}','geometryType':'esriGeometryEnvelope','inSR':4326,'spatialRel':'esriSpatialRelIntersects','outFields':'OBJECTID,name,place','outSR':4326,'geometryPrecision':5,'orderByFields':'OBJECTID','resultOffset':off,'resultRecordCount':2000,'f':'geojson'}
        for k in range(5):
            try:
                j=json.loads(urllib.request.urlopen(urllib.request.Request(U,data=urllib.parse.urlencode(p).encode(),headers=UA),timeout=180).read())
                if 'error' in j: raise ValueError(str(j['error'])[:100])
                break
            except Exception as ex:
                if k==4: raise
                time.sleep(6*(k+1))
        fs=j.get('features',[])
        for f in fs:
            g=f.get('geometry'); a=f['properties']
            if not g or g['type']!='Point' or not a.get('name'): continue
            x,y=g['coordinates']
            if any(inring(r,x,y) for r in RINGS): out[a['OBJECTID']]={'n':a['name'],'lat':round(y,5),'lon':round(x,5),'p':a['place']}
        off+=len(fs)
        if len(fs)<2000: break
json.dump(list(out.values()),open(f'cache/osm/{KEY}_places.json','w'),separators=(',',':'),ensure_ascii=False)
from collections import Counter
print('wrote',f'cache/osm/{KEY}_places.json',len(out),dict(Counter(v['p'] for v in out.values())))
