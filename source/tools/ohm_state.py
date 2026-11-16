#!/usr/bin/env python3
"""Download OpenHistoricalMap's railways and canals for one state or province: python3 tools/ohm_state.py ny
OpenHistoricalMap holds lines with start and end dates that OpenStreetMap does not keep, and its own server has
answered reliably. Writes cache/osm/<key>_ohm_rail.json and cache/osm/<key>_ohm_canal.json for tools/lines.py."""
import sys,os,json,time,math,urllib.request,urllib.parse
KEY=sys.argv[1]; RINGS=json.load(open('build/states.json'))[KEY]
xs=[r[i] for r in RINGS for i in range(0,len(r),2)]; ys=[r[i+1] for r in RINGS for i in range(0,len(r),2)]
W,E,S,N=min(xs)-0.05,max(xs)+0.05,min(ys)-0.05,max(ys)+0.05
EP='https://overpass-api.openhistoricalmap.org/api/interpreter'; UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
def run(q):
    for k in range(4):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(EP,data=urllib.parse.urlencode({'data':q}).encode(),headers=UA),timeout=240).read())['elements']
        except Exception as e: print('retry',str(e)[:60],flush=True); time.sleep(10*(k+1))
    raise SystemExit('OpenHistoricalMap did not answer')
cols=max(1,math.ceil((E-W)/2.5)); out={'rail':{},'canal':{}}
for c in range(cols):
    w=W+(E-W)*c/cols; e=W+(E-W)*(c+1)/cols; b=f'{S},{w},{N},{e}'
    for k,q in (('rail',f'[out:json][timeout:200];way["railway"]({b});out tags geom;'),('canal',f'[out:json][timeout:200];(way["waterway"="canal"]({b});way["historic"="canal"]({b});way["waterway"="lock"]({b}););out tags geom;')):
        for el in run(q): out[k][el['id']]=el
        print(KEY,k,'strip',c+1,'of',cols,len(out[k]),flush=True); time.sleep(2)
for k in out:
    p=f'cache/osm/{KEY}_ohm_{k}.json'; json.dump({'elements':list(out[k].values())},open(p,'w'),separators=(',',':')); print('wrote',p,len(out[k]),os.path.getsize(p)//1024,'KB')
