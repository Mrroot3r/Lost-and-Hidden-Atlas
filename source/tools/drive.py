"""Drive times from start cities to every place, from the public OSRM server (needs network).
Each place gets times only from the start cities within RANGE miles in a straight line; beyond that the app
shows its own rough estimate (marked ~). That keeps the place list small now that start cities span the
continent. A pair with no road between them (an island, Hawaii from the mainland) is left out the same way."""
import json,urllib.request,time,math,os,hashlib
S=json.load(open('build/sites.json'))
from states import HUBS   # start cities live in tools/states.py
RANGE=450
# What the routing server said last time is kept in build/drive.json (in the repository as source/build/drive.json), so a
# build asks only about places it has not seen, and a build while the server is down still has every older place's
# times. A place it could not ask about goes without (the app then shows its own rough estimate, marked ~) and is asked
# about again by the next build. The whole file is thrown away when the list of start cities changes.
CF='build/drive.json'; SIG=hashlib.md5(json.dumps(HUBS).encode()).hexdigest()[:10]
try: C=json.load(open(CF)); C=C if C.get('hubs')==SIG else {'hubs':SIG,'t':{}}
except Exception: C={'hubs':SIG,'t':{}}
key=lambda s:'%.5f,%.5f'%tuple(dest(s))
def dest(s): return s.get('th') or [s['lat'],s['lon']]
def mi(a,b,c,d):
    p=math.pi/180; x=math.sin((c-a)*p/2)**2+math.cos(a*p)*math.cos(c*p)*math.sin((d-b)*p/2)**2
    return 3958.8*2*math.asin(math.sqrt(x))
def near(s): d=dest(s); return [hi for hi,h in enumerate(HUBS) if mi(d[0],d[1],h[2],h[3])<=RANGE]
for s in S:
    c=C['t'].get(key(s))
    if c: s['dt']=dict(c[0]); s['snap']=c[1]
    else: s['dt']={}; s['snap']=0
order=sorted([i for i in range(len(S)) if key(S[i]) not in C['t']],key=lambda i:(round(dest(S[i])[1]/4),dest(S[i])[0]))   # neighbours together, so a request needs few start cities
k=0; reqs=0; failed=0
while k<len(order):
    chunk=[]; hubs=[]
    while k<len(order) and len(chunk)<60:
        s=S[order[k]]; hs=sorted(set(hubs)|set(near(s)))
        if chunk and len(hs)+len(chunk)+1>98: break
        chunk.append(s); hubs=hs; k+=1
    if not hubs:
        for s in chunk: C['t'][key(s)]=[{},0]
        continue
    coords=';'.join(f"{HUBS[h][3]},{HUBS[h][2]}" for h in hubs)+';'+';'.join(f"{dest(s)[1]},{dest(s)[0]}" for s in chunk)
    src=';'.join(str(i) for i in range(len(hubs))); dst=';'.join(str(i+len(hubs)) for i in range(len(chunk)))
    u=f"https://router.project-osrm.org/table/v1/driving/{coords}?sources={src}&destinations={dst}&annotations=duration,distance"
    j=None
    for a in range(4):
        try:
            j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'lost-hidden-atlas-research/1.0'}),timeout=120))
            if j.get('code')=='Ok': break
            j=None
        except Exception as e: j=None
        time.sleep(5)
    if j is None: failed+=len(chunk); continue          # the server is down or refused: these places are asked about again next build
    for ci,s in enumerate(chunk):
        mine=set(near(s))
        for n,h in enumerate(hubs):
            du,di=j['durations'][n][ci],j['distances'][n][ci]
            if h in mine and du is not None and di is not None: s['dt'][HUBS[h][0]]=[round(du/60),round(di/1609.34,1)]
        s['snap']=round(j['destinations'][ci]['distance']); C['t'][key(s)]=[s['dt'],s['snap']]
    reqs+=1; time.sleep(1.2)
live={key(s) for s in S}; C['t']={k:v for k,v in sorted(C['t'].items()) if k in live}
json.dump(C,open(CF,'w'),separators=(',',':'))
if failed: print('WARNING:',failed,'places got no drive times because the routing server did not answer; the next build asks again')
json.dump(S,open('build/sites.json','w'),indent=1,ensure_ascii=False)
json.dump([dict(id=h[0],name=h[1],lat=h[2],lon=h[3],st=h[4]) for h in HUBS],open('build/hubs.json','w'))
far=sorted(S,key=lambda s:-s['snap'])[:12]
print(reqs,'requests;',sum(1 for s in S if not s['dt']),'places with no start city in range')
print([(s['id'],s['snap']) for s in far])
