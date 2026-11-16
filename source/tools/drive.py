import json,urllib.request,time
S=json.load(open('build/sites.json'))
HUBS=[('alb','Albany',42.6526,-73.7562),('sch','Schenectady',42.8142,-73.9396),('troy','Troy',42.7284,-73.6918),('sar','Saratoga Springs',43.0831,-73.7846),('wor','Worcester',42.2626,-71.8023),('prov','Providence',41.8242,-71.4126)]
def dest(s): return s.get('th') or [s['lat'],s['lon']]
out={}
for k in range(0,len(S),70):
    chunk=S[k:k+70]
    coords=';'.join(f"{h[3]},{h[2]}" for h in HUBS)+';'+';'.join(f"{dest(s)[1]},{dest(s)[0]}" for s in chunk)
    src=';'.join(str(i) for i in range(len(HUBS))); dst=';'.join(str(i+len(HUBS)) for i in range(len(chunk)))
    u=f"https://router.project-osrm.org/table/v1/driving/{coords}?sources={src}&destinations={dst}&annotations=duration,distance"
    j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'lost-hidden-atlas-research/1.0'}),timeout=90))
    assert j['code']=='Ok',j
    for ci,s in enumerate(chunk):
        s['dt']={HUBS[hi][0]:[round(j['durations'][hi][ci]/60), round(j['distances'][hi][ci]/1609.34,1)] for hi in range(len(HUBS))}
        s['snap']=round(j['destinations'][ci]['distance'])
    time.sleep(1.2)
json.dump(S,open('build/sites.json','w'),indent=1,ensure_ascii=False)
json.dump([dict(id=h[0],name=h[1],lat=h[2],lon=h[3]) for h in HUBS],open('build/hubs.json','w'))
far=sorted(S,key=lambda s:-s['snap'])[:12]
print([(s['id'],s['snap']) for s in far])
print([(s['id'],s['dt']) for s in S if s['id'] in ('luna-park','hotel-kaaterskill','adirondac','central-warehouse','grossingers')])
