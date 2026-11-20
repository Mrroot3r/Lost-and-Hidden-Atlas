#!/usr/bin/env python3
"""Build the historic-pockets layer: old town centres first, then every other place where historical markers and
National Register listings bunch together.

   python3 tools/pockets.py            reads, for every key in KEYS, cache/hmdb/<key>.json (tools/hmdb_state.py),
                                       cache/nrhp/<key>.json (tools/nrhp_state.py) and cache/osm/<key>_places.json
                                       (tools/osm_places.py); writes build/pockets.json (every state's pockets, small)
                                       and build/pock/<key>.json (that state's markers, listings and district outlines).
                                       make.py copies both to data/.

Why: showing every plaque is clutter, and most plaques mark something that is gone. But where many sit close
together, with listed buildings among them, there is usually an old town centre worth walking.

How a pocket is made (GUIDE.md section 8 says the same in plain words):
 1. Listings come from the Park Service file, corrected and filled in from Wikidata (see listings() below).
    Markers closer than 30 m count as one spot. Spots and listings closer than LINK metres chain together.
 2. OLD TOWN CENTRES (type 'c'). A chain that comes within TOUCH metres of a mapped settlement point (an
    OpenStreetMap city, town, village or hamlet) belongs to that settlement, out to REACH metres from the point.
    A district named after the settlement ("Cobleskill Historic District") belongs to it even when the Register's
    coordinate for it is a kilometre off, which is common. Everything a settlement gathers this way is ONE pocket
    carrying the settlement's name, so a town appears once however long its main street is. It is kept as a town
    centre only with real evidence: a historic district, several listed buildings, or several plaques about things
    from before 1900.
 3. OTHER POCKETS (type 'p'). Whatever is left over: estates, battlefields, mill sites, campuses, cemeteries, city
    neighbourhoods away from the centre. A chain longer than SPLIT is cut into blocks of CELL metres.
 4. The score (see score()) ranks them. Buildings that still stand count most: the contributing buildings of a
    district, then individually listed buildings (a church, courthouse, bank, hotel, depot, store or hall counts
    double a house), then plaques weighted by the earliest year they name.

Like the lines and leads, this rebuilds only the states whose raw files are present and keeps the rest of an existing
build/pockets.json. Sources and their terms are in tools/hmdb_state.py and tools/nrhp_state.py."""
import json,os,math,re,hashlib
from collections import Counter,defaultdict
KEYS=['ny','ma','vt','ct','nh','nj','pa','ri','me','md','de','dc','va','oh','wv','tx','la','az','ca','il','mo','ks','hi','tn','nc','ga','fl']   # states to build when their raw files are present
LINK=220               # metres: two things closer than this belong to the same chain
MIN=5                  # a plain pocket needs at least this weight (a marker spot 1, a listed place 2, a district 3 to 30)
SPLIT=900              # metres: a leftover chain longer than this is cut into blocks of CELL metres
CELL=600
TOUCH={'hamlet':300,'village':400,'town':500,'city':600}    # metres: a chain with something this close to a settlement's point belongs to it
FAR={'hamlet':2500,'village':2500,'town':2500,'city':3500}  # metres: a district named after a settlement belongs to it within this distance
UNK=40                 # a district whose building count is unknown (it came from Wikidata only) is ranked as this many buildings
MOVE=250               # metres: when the Park Service and Wikidata place a listing further apart than this, Wikidata's position is used
REACH={'hamlet':500,'village':700,'town':800,'city':1100}   # metres: how far from its point a settlement's centre runs
PK={'hamlet':'h','village':'v','town':'t','city':'C'}
CIVIC=re.compile(r'\b(Church|Chapel|Meeting ?house|Synagogue|Cathedral|Court ?house|Post Office|Bank|Hotel|Inn|Tavern|Opera House|Theat(?:re|er)|Library|Town Hall|City Hall|Village Hall|Municipal|Depot|Station|Store|Block|Building|Academy|School(?:house)?|Armory|Fire(?:house| Station)|Engine House|Masonic|Lodge|Grange|Hall|Market|Mill|Factory|Company|Jail|Custom House|Parsonage|Rectory)\b',re.I)
CENTRE=re.compile(r'\b(Village|Downtown|Main Street|Commercial|Business|Central|Court ?house|Square|Green|Hamlet|Cent(?:er|re)|Core|Stockade|Market|Canal|Waterfront|Harbor|Corners|Common|Uptown|Broadway|Front Street|Water Street|State Street|Church Street|Old Town)\b',re.I)
STRICT=re.compile(r'\b(Central(?! Avenue| Park| Street)|Village|Downtown|Main Street|Commercial|Business|Hamlet|Town Cent(?:er|re))\b',re.I)   # a district that is a centre even with no mapped settlement point
def load(d,k,suffix=''):
    p=f'cache/{d}/{k}{suffix}.json'
    return json.load(open(p)) if os.path.exists(p) else None
def metres(a,b,c,d): return math.hypot((c-a)*111320,(d-b)*111320*math.cos(math.radians((a+c)/2)))
def base(nm): return re.sub(r'\s*\(Boundary (?:Increase|Decrease)[^)]*\)','',nm).replace('--',', ').strip()
def isd(e): return e['k']=='district' or (e.get('cb') or 0)>=8          # a district, or a listing that counts as one
def listings(key):
    """The Park Service file, put right from Wikidata (tools/wd_nrhp.py) where that is present:
      - a listing the two sources place more than MOVE metres apart takes Wikidata's position. Checked against town
        points for listings named after a town, Wikidata was the closer of the two about twice in three;
      - a listing the Park Service calls a single building but counts eight or more contributing buildings for is a
        district filed under one of its houses (Hudson's is 'Robert Jenkins House'); it takes Wikidata's name;
      - a listing the Park Service file lacks is added, without a building count ('cb' None)."""
    N=load('nrhp',key) or []; W={e['ref']:e for e in (load('nrhp',key,'_wd') or [])}
    moved=renamed=0
    for e in N:
        w=W.get(e['ref'])
        if not w: continue
        if metres(e['lat'],e['lon'],w['lat'],w['lon'])>MOVE: e['lat'],e['lon']=w['lat'],w['lon']; moved+=1
        if e['k']!='district' and (e.get('cb') or 0)>=8 and re.search(r'\bDistrict\b',w['n']): e['n']=w['n']; renamed+=1
    have={e['ref'] for e in N}; names=defaultdict(list)
    for e in N: names[base(e['n']).lower()].append(e)
    added=0
    for ref,w in W.items():
        if ref in have: continue
        if any(metres(w['lat'],w['lon'],e['lat'],e['lon'])<2500 for e in names.get(base(w['n']).lower(),())): continue   # the same place under a second number
        N.append({'ref':ref,'n':w['n'],'k':w['k'],'town':'','county':'','cb':None,'nhl':False,'y':'','lat':w['lat'],'lon':w['lon']}); added+=1
    if W: print(f'  {key}: Wikidata moved {moved} listings, renamed {renamed}, added {added}')
    return N
def weight(e):
    """How much one listing counts toward MIN. A district with many contributing buildings is a pocket by itself."""
    if isd(e): return 8 if e.get('cb') is None else max(3,min(30,e['cb']//4))
    return 2
def era_weight(y,wm):
    if y is None: return 0.4 if wm else 0.7
    return 1.5 if y<=1830 else 1.2 if y<=1900 else 0.6 if y<=1945 else 0.3
def inpoly(poly,la,lo):
    ins=False; j=len(poly)-1
    for i in range(len(poly)):
        yi,xi=poly[i][0],poly[i][1]; yj,xj=poly[j][0],poly[j][1]
        if (yi>la)!=(yj>la) and lo<(xj-xi)*(la-yi)/(yj-yi)+xi: ins=not ins
        j=i
    return ins
def named_after(dn,place):
    """Is a district named after this settlement? 'Hudson Historic District', 'Downtown Cohoes Historic District',
    'Kingston Stockade District', 'Athens Lower Village Historic District': yes. 'Union Street Historic District' for
    a hamlet called Union: no."""
    return re.match(r'(?:Downtown |Uptown |Central |Old |Lower |Upper |Village of |Hamlet of |Town of )?'+re.escape(place)+r',? (?:Lower |Upper |Old )?(?:Village|Hamlet|Town|Downtown|Commercial|Business|Central|Stockade|Cent(?:er|re)|Main Street|Historic|Multiple)\b',dn,re.I) is not None
def score(spots,rs):
    """spots: [(earliest year or None, war memorial?)], one per marker spot; rs: the listings.
    Returns (score, evidence) where evidence = (M, B, contributing buildings known, plaque spots about something
    before 1901, whether a district's name says it is a centre, whether there is a real district)."""
    M=sum(era_weight(y,wm) for y,wm in spots)
    blds=[e for e in rs if not isd(e)]; civic=sum(1 for e in blds if CIVIC.search(e['n']))
    B=2.0*civic+1.0*(len(blds)-civic)
    ds=[e for e in rs if isd(e)]; cb=sum(e.get('cb') or 0 for e in ds)
    named=any(CENTRE.search(base(e['n'])) for e in ds)
    C=4*math.log2(1+(cb+UNK*sum(1 for e in ds if e.get('cb') is None))/15)
    S=min(M,15)+min(B,15)+min(C,22)+(4 if named else 0)
    old=sum(1 for y,wm in spots if y is not None and y<=1900)
    real=any(e.get('cb') is None or e['cb']>=8 for e in ds)
    return round(S,1),(M,B,cb,old,named,real)
def is_centre(ev):
    M,B,cb,old,named,real=ev
    return real or B>=4 or (old>=3 and M+B>=5) or (named and M+B>=3)
def era_of(spots):
    """The decades most of the dated plaques here speak of: from the oldest fifth to a little past the middle."""
    ys=sorted(y for y,wm in spots if y is not None)
    if len(ys)<3: return ''
    a,b=ys[int(len(ys)*0.2)]//10*10,ys[min(len(ys)-1,int(len(ys)*0.6))]//10*10
    return f'{a}s' if a==b else f'{a}s–{b}s'
def build(key):
    M=load('hmdb',key) or []; N=listings(key); PL=load('osm',key,'_places') or []
    # A memorial walk can hold hundreds of plaques on one lawn. Markers in the same 30 m square are one spot.
    sp=defaultdict(list)
    for m in M: sp[(int(m['lat']*111320/30),int(m['lon']*111320*math.cos(math.radians(m['lat']))/30))].append(m)
    spots=[{'lat':v[0]['lat'],'lon':v[0]['lon'],'ms':v,'y':min([m['y'] for m in v if 'y' in m],default=None),'wm':all(m.get('wm') for m in v)} for v in sp.values()]
    # items: [lat, lon, weight, 's' spot | 'r' listing, the thing]
    items=[[s['lat'],s['lon'],1,'s',s] for s in spots]+[[e['lat'],e['lon'],weight(e),'r',e] for e in N]
    # settlement points on a coarse grid
    pg=defaultdict(list)
    for qi,q in enumerate(PL): pg[(int(q['lat']/0.02),int(q['lon']/0.02))].append(qi)
    def places_within(la,lo,d):
        a,b=int(la/0.02),int(lo/0.02); out=[]; k=int(d/1800)+1
        for i in range(a-k,a+k+1):
            for j in range(b-k-1,b+k+2):
                for qi in pg.get((i,j),()):
                    m=metres(la,lo,PL[qi]['lat'],PL[qi]['lon'])
                    if m<=d: out.append((m,qi))
        return out
    # 2a. a district named after a settlement belongs to it. When the settlement's point lies inside the district's
    #     outline, or within reach of its coordinate, the district is taken to sit ON the settlement point (the
    #     Register's coordinate for a district is the middle of a rough box and can be a kilometre off). Otherwise the
    #     district is somewhere else in town (Kingston's Stockade is uptown) and may become the town's anchor instead.
    own={}; anchor={qi:(q['lat'],q['lon']) for qi,q in enumerate(PL)}; far=defaultdict(list)
    for n,it in enumerate(items):
        e=it[4]
        if it[3]!='r' or not isd(e): continue
        c=[(m,qi) for m,qi in places_within(it[0],it[1],3500) if m<=FAR[PL[qi]['p']] and named_after(base(e['n']),PL[qi]['n'])]
        if not c: continue
        m,qi=min(c); q=PL[qi]
        if m<=REACH[q['p']] or (e.get('poly') and inpoly(e['poly'],q['lat'],q['lon'])): own[n]=qi; it[0],it[1]=q['lat'],q['lon']
        else: far[qi].append(n)
    for qi,ns in far.items():
        q=PL[qi]; n=max(ns,key=lambda n:items[n][2])
        def lump(la,lo): return sum(it[2] for it in items if abs(it[0]-la)<0.012 and metres(la,lo,it[0],it[1])<=REACH[q['p']])
        if lump(items[n][0],items[n][1])>lump(q['lat'],q['lon']):
            anchor[qi]=(items[n][0],items[n][1])
            for x in ns:
                if metres(items[x][0],items[x][1],anchor[qi][0],anchor[qi][1])<=REACH[q['p']]: own[x]=qi
    ag=defaultdict(list)
    for qi,(la,lo) in anchor.items(): ag[(int(la/0.02),int(lo/0.02))].append(qi)
    def anchors_within(la,lo,d):
        a,b=int(la/0.02),int(lo/0.02); out=[]
        for i in (a-1,a,a+1):
            for j in (b-1,b,b+1):
                for qi in ag.get((i,j),()):
                    m=metres(la,lo,anchor[qi][0],anchor[qi][1])
                    if m<=d: out.append((m,qi))
        return out
    # 1. chains
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
    chains=defaultdict(list)
    for n in range(len(items)): chains[find(n)].append(n)
    # 2b. which settlement each chain belongs to
    got=defaultdict(list); left=defaultdict(list)       # settlement index -> items ; chain root -> leftover items
    for root,g in chains.items():
        touched={own[n] for n in g if n in own}
        for n in g:
            for m,qi in anchors_within(items[n][0],items[n][1],600):
                if m<=TOUCH[PL[qi]['p']]: touched.add(qi)
        for n in g:
            it=items[n]; best=None
            if n in own: got[own[n]].append(n); continue
            for qi in touched:
                m=metres(it[0],it[1],anchor[qi][0],anchor[qi][1])
                if m<=REACH[PL[qi]['p']] and (best is None or m<best[0]): best=(m,qi)
            if best: got[best[1]].append(n)
            else: left[root].append(n)
    pk=[]
    def make(g,place=None):
        w=sum(items[n][2] for n in g)
        la=sum(items[n][0]*items[n][2] for n in g)/w; lo=sum(items[n][1]*items[n][2] for n in g)/w
        ss=[items[n][4] for n in g if items[n][3]=='s']; rs=[items[n][4] for n in g if items[n][3]=='r']
        ds=sorted([e for e in rs if isd(e)],key=lambda e:-(e.get('cb') or 0))
        dist=sorted(metres(la,lo,items[n][0],items[n][1]) for n in g)
        r=dist[min(len(dist)-1,int(len(dist)*0.85))]+60
        if ds and not place: r=max(r,min(ds[0].get('w',0)/2,700))
        r=int(max(120,min(REACH[place['p']] if place else 900,r)))
        yrs=[(s['y'],s['wm']) for s in ss]
        S,ev=score(yrs,rs)
        towns=Counter([m['town'] for s in ss for m in s['ms'] if m['town']]+[e['town'] for e in rs if e['town']])
        town=towns.most_common(1)[0][0] if towns else ''
        if place: name=place['n']
        else:
            lone=sorted([e for e in rs if not isd(e)],key=lambda e:(not e.get('nhl'),e['n']))
            name=base(ds[0]['n']) if ds else lone[0]['n'] if lone else ('Plaques near '+town if town else 'Unnamed pocket')
            if (ds or lone) and town and town.lower() not in name.lower(): name+=', '+town
        row=[round(la,5),round(lo,5),r,sum(len(s['ms']) for s in ss),sum(1 for e in rs if not isd(e)),len({base(e['n']) for e in ds}),ev[2],name[:70],key,len(ss),'p',S,era_of(yrs),PK[place['p']] if place else '']
        return {'row':row,'ev':ev,'ds':ds}
    for qi,g in got.items():
        p=make(g,PL[qi])
        if is_centre(p['ev']): p['row'][10]='c'; pk.append(p)
        else:
            for n in g: left[find(n)].append(n)          # not enough for a town centre: back into the leftovers
    # 3. the leftovers become plain pockets
    for g in left.values():
        las=[items[n][0] for n in g]; los=[items[n][1] for n in g]
        if metres(min(las),min(los),max(las),max(los))<=SPLIT: parts=[g]
        else:
            sub=defaultdict(list)
            for n in g: sub[(int(items[n][0]*111320/CELL),int(items[n][1]*111320*math.cos(math.radians(items[n][0]))/CELL))].append(n)
            parts=list(sub.values())
        for part in parts:
            if sum(items[n][2] for n in part)<MIN: continue
            p=make(part)
            # a district named as a village, downtown, main street or business district is a centre even where
            # OpenStreetMap has no settlement point for it (an old village long since swallowed by a city)
            if p['ds'] and STRICT.search(base(p['ds'][0]['n'])) and (p['ds'][0].get('cb') is None or p['ev'][2]>=10):
                p['row'][10]='c'; p['row'][7]=re.sub(r'\s+(Historic |Commercial |Business )+District\b','',p['row'][7])[:70]
            pk.append(p)
    rows=[p['row'] for p in pk]
    rows.sort(key=lambda p:(p[10]!='c',-p[11]))
    KIND={'building':'b','district':'d','site':'s','structure':'t','object':'o'}
    def thin(poly,cap=28):
        st=max(1,-(-len(poly)//cap)); q=poly[::st]
        return q if q[-1]==poly[-1] else q+[poly[-1]]
    # the detail file keeps every listing where its source put it (a district moved onto its town's point above is
    # written at its own coordinate here)
    pos={e['ref']:(e['lat'],e['lon']) for e in N}
    det={'m':[[m['lat'],m['lon'],m['id'],m['t'][:70]] for m in M],
         'r':[[pos[e['ref']][0],pos[e['ref']][1],e['ref'],e['n'][:70],'d' if isd(e) else KIND.get(e['k'],'b'),-1 if e.get('cb') is None else e['cb'],e.get('y','')] for e in N],
         'd':[[e['ref'],thin(e['poly'])] for e in N if e.get('poly') and e['k']=='district']}
    s=json.dumps(det,separators=(',',':'),ensure_ascii=False)
    os.makedirs('build/pock',exist_ok=True); open(f'build/pock/{key}.json','w',encoding='utf-8').write(s)
    nc=sum(1 for p in rows if p[10]=='c')
    info={'markers':len(M),'listings':len(N),'pockets':len(rows),'centres':nc,'h':hashlib.md5(s.encode()).hexdigest()[:8],'gaps':[c for c,n in (load('hmdb',key,'_gaps') or {}).get('short',[])]}
    print(key,len(M),'markers,',len(N),'register listings,',len(PL),'settlements ->',len(rows),'pockets, of which',nc,'old town centres;',f'detail {len(s)//1024} KB')
    print('  top centres:',[(p[7][:20],p[11]) for p in rows[:8]])
    return rows,info
if __name__=='__main__':
    old=json.load(open('build/pockets.json')) if os.path.exists('build/pockets.json') else None
    out={'v':3,'k':[],'s':{}}
    have=[k for k in KEYS if load('hmdb',k) is not None or load('nrhp',k) is not None]
    if old and old.get('v')==3:
        keep=[s for s in old.get('s',{}) if s not in have and os.path.exists(f'build/pock/{s}.json')]
        if keep:
            out['k']+=[x for x in old['k'] if x[8] in keep]
            for s in keep: out['s'][s]=old['s'][s]
            print('kept from the existing build/pockets.json:',' '.join(keep))
    for key in have:
        rows,info=build(key); out['k']+=rows; out['s'][key]=info
    out['k'].sort(key=lambda p:(p[10]!='c',-p[11]))
    s=json.dumps(out,separators=(',',':'),ensure_ascii=False); open('build/pockets.json','w',encoding='utf-8').write(s)
    print('wrote build/pockets.json',len(s)//1024,'KB;',len(out['k']),'pockets in',len(out['s']),'states; detail files in build/pock/')
