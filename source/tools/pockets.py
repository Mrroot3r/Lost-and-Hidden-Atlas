#!/usr/bin/env python3
"""Build the historic-pockets layer: places where historical markers and National Register listings bunch together.

   python3 tools/pockets.py            reads cache/hmdb/<key>.json and cache/nrhp/<key>.json for every key in KEYS,
                                       writes build/pockets.json (copied to data/pockets.json by make.py)

Why: showing every plaque is clutter, and most plaques mark something that is gone. But where many of them sit
close together, with listed buildings among them, there is usually an old town centre worth walking. A pocket is a
group of markers and listings chained together by gaps of no more than LINK metres. Each one gets a centre, a
radius, counts, and a name (the historic district it sits in, or the town most of its markers name).
The single markers and listings are kept too; the app shows them only when zoomed well in.

Like the lines and leads, this rebuilds only the states whose raw files are present and keeps the rest of an
existing build/pockets.json. Sources and their terms are in tools/hmdb_state.py and tools/nrhp_state.py."""
import json,os,math,sys,re
from collections import Counter,defaultdict
KEYS=['ny']            # states with raw files from hmdb_state.py and nrhp_state.py
LINK=220               # metres: two things closer than this belong to the same pocket
MIN=5                  # a pocket needs at least this many things (a district counts as several, see weight())
SPLIT=900              # metres: a chain longer than this (a whole downtown) is cut into blocks of CELL metres
CELL=600
def load(d,k):
    p=f'cache/{d}/{k}.json'
    return json.load(open(p)) if os.path.exists(p) else None
def metres(a,b,c,d): return math.hypot((c-a)*111320,(d-b)*111320*math.cos(math.radians((a+c)/2)))
def weight(e):
    """How much one listing counts toward MIN. A district with many contributing buildings is a pocket by itself."""
    if e['k']=='district': return max(3,min(30,e.get('cb',0)//4))
    return 2
old=json.load(open('build/pockets.json')) if os.path.exists('build/pockets.json') else None
out={'v':1,'k':[],'m':[],'r':[],'d':[],'s':{}}
have=[k for k in KEYS if load('hmdb',k) is not None or load('nrhp',k) is not None]
if old:
    keep=[s for s in old.get('s',{}) if s not in have]
    if keep:
        for part in ('m','r','d'): out[part]+=[x for x in old[part] if x[-1] in keep]
        out['k']+=[x for x in old['k'] if x[8] in keep]
        for s in keep: out['s'][s]=old['s'][s]
        print('kept from the existing build/pockets.json:',' '.join(keep))
for key in have:
    M=load('hmdb',key) or []; N=load('nrhp',key) or []
    # every item: (lat, lon, weight, kind, index)
    # A memorial walk can hold hundreds of plaques on one lawn. Only the first marker in each 30 m square counts
    # toward a pocket's weight and rank; the rest are still shown and still counted in the number the reader sees.
    spot=set()
    def first(m):
        c=(int(m['lat']*111320/30),int(m['lon']*111320*math.cos(math.radians(m['lat']))/30))
        if c in spot: return 0
        spot.add(c); return 1
    items=[(m['lat'],m['lon'],first(m),'m',i) for i,m in enumerate(M)]+[(e['lat'],e['lon'],weight(e),'r',i) for i,e in enumerate(N)]
    cell=LINK/111320*1.05; grid=defaultdict(list)
    for n,it in enumerate(items): grid[(int(it[0]/cell),int(it[1]/(cell*1.4)))].append(n)
    parent=list(range(len(items)))
    def find(x):
        while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for (a,b),ns in grid.items():
        for i in (a-1,a,a+1):
            for j in (b-1,b,b+1):
                for q in grid.get((i,j),()):
                    for p in ns:
                        if p<q and metres(items[p][0],items[p][1],items[q][0],items[q][1])<=LINK:
                            rp,rq=find(p),find(q)
                            if rp!=rq: parent[rp]=rq
    groups=defaultdict(list)
    for n in range(len(items)): groups[find(n)].append(n)
    # a long chain is one pocket only on paper: cut it into blocks so that a city centre reads as several walks
    final=[]
    for g in groups.values():
        las=[items[n][0] for n in g]; los=[items[n][1] for n in g]
        if metres(min(las),min(los),max(las),max(los))<=SPLIT: final.append(g); continue
        sub=defaultdict(list)
        for n in g: sub[(int(items[n][0]*111320/CELL),int(items[n][1]*111320*math.cos(math.radians(items[n][0]))/CELL))].append(n)
        final+=list(sub.values())
    def base(nm): return re.sub(r'\s*\(Boundary (?:Increase|Decrease)[^)]*\)','',nm).replace('--',', ').strip()
    pk=[]
    for g in final:
        w=sum(items[n][2] for n in g)
        if w<MIN: continue
        la=sum(items[n][0]*max(items[n][2],0.01) for n in g)/(w+0.01*sum(1 for n in g if not items[n][2])); lo=sum(items[n][1]*max(items[n][2],0.01) for n in g)/(w+0.01*sum(1 for n in g if not items[n][2]))
        ms=[M[items[n][4]] for n in g if items[n][3]=='m']; rs=[N[items[n][4]] for n in g if items[n][3]=='r']
        r=max([metres(la,lo,items[n][0],items[n][1]) for n in g]+[e.get('w',0)/2 for e in rs if e['k']=='district'])
        r=int(max(120,min(900,r+60)))
        cb=sum(e.get('cb',0) for e in rs if e['k']=='district')
        ds=sorted([e for e in rs if e['k']=='district'],key=lambda e:-e.get('cb',0))
        towns=Counter([m['town'] for m in ms if m['town']]+[e['town'] for e in rs if e['town']])
        town=towns.most_common(1)[0][0] if towns else ''
        name=base(ds[0]['n']) if ds else (town or 'Unnamed pocket')
        if ds and town and town.lower() not in name.lower(): name+=', '+town
        nb=sum(1 for e in rs if e['k']!='district')
        spots=sum(items[n][2] for n in g if items[n][3]=='m')
        pk.append([round(la,5),round(lo,5),r,len(ms),nb,len({base(e['n']) for e in ds}),cb,name[:70],key,spots])
    pk.sort(key=lambda p:-(p[9]+2*p[4]+min(p[6],400)/8))
    out['k']+=pk
    out['m']+=[[m['lat'],m['lon'],m['id'],m['t'][:70],key] for m in M]
    KIND={'building':'b','district':'d','site':'s','structure':'t','object':'o'}
    out['r']+=[[e['lat'],e['lon'],e['ref'],e['n'][:70],KIND.get(e['k'],'b'),e.get('cb',0),e.get('y',''),key] for e in N]
    def thin(poly,cap=28):
        st=max(1,-(-len(poly)//cap)); q=poly[::st]
        return q if q[-1]==poly[-1] else q+[poly[-1]]
    out['d']+=[[e['ref'],thin(e['poly']),key] for e in N if e.get('poly') and e['k']=='district']
    out['s'][key]={'markers':len(M),'listings':len(N),'pockets':len(pk)}
    print(key,len(M),'markers,',len(N),'register listings ->',len(pk),'pockets; the largest:',[(p[7][:28],p[3],p[4],p[6]) for p in pk[:6]])
s=json.dumps(out,separators=(',',':'),ensure_ascii=False); open('build/pockets.json','w',encoding='utf-8').write(s)
print('wrote build/pockets.json',len(s)//1024,'KB;',len(out['k']),'pockets,',len(out['m']),'markers,',len(out['r']),'listings,',len(out['d']),'district outlines')
