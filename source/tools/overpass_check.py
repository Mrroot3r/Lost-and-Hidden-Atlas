#!/usr/bin/env python3
"""Is Overpass (the full OpenStreetMap query service) reachable today?   python3 tools/overpass_check.py

It has been blocked or too slow from cloud machines since November 2026, so New York's old lines outside the
Capital Region were built from Esri's hosted copies instead (tools/osm_layers.py), which lose some detail.
GUIDE.md section 10 has a standing note to come back and re-download with Overpass when this check passes.
A mirror is usable when it answers the second test (every old-railway tag in a quarter-degree box near Buffalo)
in well under a minute."""
import urllib.request,urllib.parse,json,time
UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
MIRRORS=['https://overpass-api.de/api/interpreter','https://maps.mail.ru/osm/tools/overpass/api/interpreter','https://overpass.kumi.systems/api/interpreter','https://overpass.private.coffee/api/interpreter']
B='42.75,-79.0,43.0,-78.75'
TESTS=[('small',f'[out:json][timeout:25];way["railway"="abandoned"](42.88,-78.9,42.92,-78.85);out tags geom;',30),
       ('quarter-degree, all old-railway tags',f'[out:json][timeout:55];(way["railway"~"^(abandoned|disused|razed|dismantled)$"]({B});way["abandoned:railway"]({B});way["disused:railway"]({B});way["razed:railway"]({B});way["historic:railway"]({B}););out tags geom;',60)]
ok=[]
for m in MIRRORS:
    for name,q,t in TESTS:
        t0=time.time()
        try:
            r=urllib.request.urlopen(urllib.request.Request(m,data=urllib.parse.urlencode({'data':q}).encode(),headers=UA),timeout=t).read()
            n=len(json.loads(r)['elements']); dt=time.time()-t0; print(f'OK    {m}  {name}: {n} elements in {dt:.0f} s')
            if name!='small' and n>50 and dt<45: ok.append(m)
        except Exception as e:
            print(f'FAIL  {m}  {name}: {str(e)[:60]} after {time.time()-t0:.0f} s'); break
print('\nUsable mirrors:',ok or 'none. Keep using tools/osm_layers.py and try again another day.')
