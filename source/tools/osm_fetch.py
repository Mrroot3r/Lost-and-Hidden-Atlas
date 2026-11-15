import urllib.request,urllib.parse,json,sys,time
BB='41.55,-75.35,44.45,-73.05'
Q={
'rail_old':f'''[out:json][timeout:240];(
way["railway"~"^(abandoned|disused|razed|dismantled)$"]({BB});
way["abandoned:railway"]({BB});way["disused:railway"]({BB});way["razed:railway"]({BB});way["removed:railway"]({BB});way["historic:railway"]({BB});way["railway:historic"]({BB});
way["historic"="railway"]({BB});
);out tags geom;''',
'rail_now':f'''[out:json][timeout:240];(way["railway"="rail"]["service"!~"."]({BB});way["railway"~"^(preserved|narrow_gauge)$"]({BB}););out tags geom;''',
'canal':f'''[out:json][timeout:240];(
way["waterway"="canal"]({BB});way["disused:waterway"]({BB});way["abandoned:waterway"]({BB});way["razed:waterway"]({BB});way["historic:waterway"]({BB});way["waterway:historic"]({BB});
way["historic"~"^(canal|lock|aqueduct)$"]({BB});node["historic"~"^(canal|lock|aqueduct)$"]({BB});
way["waterway"="lock_gate"]({BB});way["lock"="yes"]({BB});way["waterway"="canal"]["disused"="yes"]({BB});
);out tags geom;''',
'stations':f'''[out:json][timeout:240];(
nwr["railway"="station"]({BB});nwr["disused:railway"~"station|halt"]({BB});nwr["abandoned:railway"~"station|halt"]({BB});nwr["historic:railway"~"station|halt"]({BB});nwr["building"="train_station"]({BB});nwr["historic"="railway_station"]({BB});
);out tags center;'''}
EP=['https://overpass-api.de/api/interpreter','https://overpass.kumi.systems/api/interpreter','https://overpass.private.coffee/api/interpreter']
for k,q in Q.items():
    for ep in EP:
        try:
            r=urllib.request.urlopen(urllib.request.Request(ep,data=urllib.parse.urlencode({'data':q}).encode(),headers={'User-Agent':'lost-hidden-atlas-research/1.0'}),timeout=300).read()
            j=json.loads(r); open(f'cache/osm/{k}.json','wb').write(r); print(k,len(j['elements']),len(r),ep); break
        except Exception as e: print(k,'fail',ep,str(e)[:80]); time.sleep(5)
    time.sleep(3)
