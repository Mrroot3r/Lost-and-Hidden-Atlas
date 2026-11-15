import urllib.request,urllib.parse,json,time
UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
def post(ep,q,t=240):
    return urllib.request.urlopen(urllib.request.Request(ep,data=urllib.parse.urlencode({'data':q}).encode(),headers=UA),timeout=t).read()
# OpenHistoricalMap
BB='41.55,-75.35,44.45,-73.05'
for k,q in {'ohm_rail':f'[out:json][timeout:180];way["railway"]({BB});out tags geom;','ohm_canal':f'[out:json][timeout:180];(way["waterway"="canal"]({BB});way["historic"="canal"]({BB});way["waterway"="lock"]({BB}););out tags geom;'}.items():
    try:
        r=post('https://overpass-api.openhistoricalmap.org/api/interpreter',q); j=json.loads(r); open(f'cache/osm/{k}.json','wb').write(r); print(k,len(j['elements']),len(r))
    except Exception as e: print(k,'fail',str(e)[:100])
# active rail, in 4 tiles
els=[]
for (s,w,n,e) in [(41.55,-75.35,43.0,-74.2),(41.55,-74.2,43.0,-73.05),(43.0,-75.35,44.45,-74.2),(43.0,-74.2,44.45,-73.05)]:
    q=f'[out:json][timeout:120];way["railway"="rail"]["service"!~"."]({s},{w},{n},{e});out tags geom;'
    ok=False
    for ep in ['https://overpass.kumi.systems/api/interpreter','https://overpass.private.coffee/api/interpreter','https://overpass-api.de/api/interpreter']:
        try:
            j=json.loads(post(ep,q,150)); els+=j['elements']; print('rail_now tile',len(j['elements']),ep); ok=True; break
        except Exception as ex: print('fail',ep,str(ex)[:60]); time.sleep(3)
json.dump({'elements':els},open('cache/osm/rail_now.json','w')); print('rail_now',len(els))
