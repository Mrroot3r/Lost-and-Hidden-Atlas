#!/usr/bin/env python3
"""The front door for finding cellar holes and farm sites on LiDAR. READ LIDAR.md FIRST: it is the whole method.

Run from the workspace root (the folder that holds tools/ and src/). Every command is safe to run again.

  python3 tools/lidar.py status                    where things stand, and what to do next
  python3 tools/lidar.py find "Wilcox Lake"        public-land units by name: acres, and whether already swept
  python3 tools/lidar.py near 43.30 -74.20 20      units within 20 miles of a point that have not been swept
  python3 tools/lidar.py sweep "Unit Name" ...     scan a unit and pair its pits with old-map buildings. It stops when
        [--minutes 1.6]                            its time is up and says so: run the same command again until DONE
  python3 tools/lidar.py walls "Unit Name" ...     map the stone walls of a unit swept before walls were looked for
        [--minutes 1.6]                            (a new sweep maps them in the same pass). Run again until DONE
  python3 tools/lidar.py next [36] [--unit text]   the next candidates nobody has looked at: one picture of LiDAR chips
  python3 tools/lidar.py sheet tpwf12 smwf3 ...    full comparison sheets: LiDAR | aerial | old map | 1940s map (three rows a picture)
  python3 tools/lidar.py mark tpwf12 no water      your verdict: no | maybe | yes, then a reason word, then any note
  python3 tools/lidar.py mark - <<'EOF'            many verdicts at once, one per line:  tpwf12 no water on a pond shore
  ...EOF
  python3 tools/lidar.py check smwf3 ...           who owns it: tax parcel, public-land record, town, nearest road
  python3 tools/lidar.py draft smwf3:mussey-road-cellar ...    write a place file with the measured facts filled in
  python3 tools/lidar.py show smwf3                everything recorded about one candidate
  python3 tools/lidar.py report                    what this session did, worded for the pull request

Reason words for "no": faint water road modern natural coarse nomap private noland dup other   (LIDAR.md explains each)

What is kept, and where:
  lidar/units/<unit>.json   one file for every unit swept: its candidates and the verdict on each. These are in the
                            repository (source/lidar/), so the next session starts where this one stopped. Do not edit
                            them by hand: use the commands.
  lidar/walls/<unit>.json   the stone walls found in a unit, as straight pieces. In the repository too; the site build
                            turns them into the "Stone walls" map layer (tools/walls.py).
  research/lidar/, cache/topo/   scans, pictures and downloaded maps. Not in the repository; made again when needed.
New York and Massachusetts. The ground model is New York's own elevation service in New York and the USGS 3DEP service
in Massachusetts (tools/lidar_dem.py); the tax parcels are each state's own file (tools/parcel.py); the leaf-off aerial
is each state's own (tools/ortho.py). STATES below says what a state needs; LIDAR.md, "Another state", says how to add one."""
import sys,os,json,re,math,time,glob,subprocess,datetime,urllib.request,urllib.parse
HERE=os.path.dirname(os.path.abspath(__file__)); PY=sys.executable
LDIR='lidar/units'; WDIR='lidar/walls'; WORK='research/lidar'; UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
PAD='https://services.arcgis.com/v01gqwM5QqNysAAi/arcgis/rest/services/PADUS_Public_Access/FeatureServer/0/query'
REASONS={'faint':'no clear shape on LiDAR','water':'on a pond, lake or stream edge','road':'beside a paved road, a ditch or a parking area',
 'modern':'a building, park facility or fresh logging is there now','natural':'rough or rocky ground; reads as natural','coarse':'the ground model is too coarse there to judge',
 'nomap':'the map "building" is lettering, a line or a survey mark','private':'the tax parcel is private','noland':'no public-land record at the point',
 'dup':'the same site as another candidate','other':'see the note'}
ORDER={'new':0,'no':1,'maybe':2,'yes':3,'published':4}
# The states this tool is set up for. box: west,south,east,north, generous (it takes in the edges of the neighbours).
# src: where the ground model comes from (tools/lidar_dem.py). A unit record carries its state as "st"; one without is New York.
STATES={'ny':{'name':'New York','box':'-79.8,40.45,-71.8,45.05','src':'ny'},
        'ma':{'name':'Massachusetts','box':'-73.52,41.2,-69.9,42.9','src':'3dep'},
        # 'oldmap': the first survey there was at 1:125,000, too coarse to place a building, so the sweep reads the earliest sheet at
        # 1:62,500 or larger from 1936 or before (the owner's line: a 1950s sheet does not prove a building is old).
        # Missouri and Kansas (November 23, 2026, for the Kansas City country): ground model from the USGS; no parcel file for the whole of
        # either state, so the ownership check rests on the federal public-land record, with Missouri's file of state-owned parcels as
        # a yes where it has one (tools/parcel.py). 'noparcel' is what the place's access line says about that.
        'mo':{'name':'Missouri','box':'-95.8,35.95,-89.05,40.65','src':'3dep','oldmap':'1936,any','walls':False,'noparcel':'Missouri has no tax-parcel file for the whole state, and the state-owned parcels it does publish have none under the pin'},
        'ks':{'name':'Kansas','box':'-102.1,36.95,-94.55,40.05','src':'3dep','oldmap':'1936,any','walls':False,'noparcel':'Kansas has no tax-parcel file for the whole state'}}
ALLBOX='-102.1,35.95,-69.9,45.05'          # every state's box together: used only to find a unit by its exact name
# county -> the Atlas region key (tools/states.py) a drafted place gets. A county that is split between two regions is left as
# a TODO naming the choices, so the writer decides from the town.
REGION={'ny':{'Albany':'albco','Rensselaer':'renss','Schenectady':'sch','Saratoga':'sar','Washington':'wash','Montgomery':'mohw','Schoharie':'scho','Otsego':'scho','Delaware':'scho',
 'Greene':'cat','Ulster':'cat','Sullivan':'cat','Columbia':'hud','Dutchess':'hud','Orange':'midh','Putnam':'midh','Rockland':'midh','Westchester':'midh',
 'St. Lawrence':'nny','Jefferson':'nny','Lewis':'nny','Oneida':'cny','Madison':'cny','Chenango':'cny','Onondaga':'cny','Oswego':'cny','Cortland':'cny','Broome':'cny','Tioga':'cny','Tompkins':'cny','Cayuga':'cny',
 'New York':'nyc','Kings':'nyc','Queens':'nyc','Bronx':'nyc','Richmond':'nyc','Nassau':'nyc','Suffolk':'nyc'},
 'ma':{'Berkshire':'berk','Essex':'nshore','Suffolk':'bos','Norfolk':'bos','Plymouth':'south','Bristol':'south','Barnstable':'south','Dukes':'south','Nantucket':'south',
 'Franklin':'TODO: region: pv (Pioneer Valley), or cmass for the Quabbin towns','Hampshire':'TODO: region: pv (Pioneer Valley), or cmass for the Quabbin towns','Hampden':'pv',
 'Worcester':'TODO: region: cmass (Quabbin and central) or worc (Worcester and Blackstone Valley)','Middlesex':'TODO: region: bos (Greater Boston and MetroWest) or nshore (Merrimack Valley)'}}
for _c in ('Warren','Essex','Hamilton','Franklin','Clinton','Fulton','Herkimer'): REGION['ny'][_c]='adk'
# Missouri has one Atlas region so far, the Kansas City country; a pit anywhere else in the state leaves a TODO. Kansas is one region ('*': every county).
REGION['mo']={c:'kcmo' for c in ('Jackson','Clay','Platte','Cass','Ray','Lafayette','Johnson','Clinton','Buchanan','Caldwell','Bates','Henry','Carroll','Saline','Pettis','DeKalb','Andrew')}
REGION['mo']['*']='TODO: region: Missouri has only kcmo (the Kansas City country) so far; tell the owner this county needs a region'
REGION['ks']={'*':'ks'}
def region_of(st,county):
    R=REGION.get(st,{}); return R.get(county or '') or R.get('*') or 'TODO: region key from tools/states.py'
def st_of(u): return (u or {}).get('st') or 'ny'
def unit_state(rings):
    """The state a unit lies in, as a key of STATES or another two-letter code, from the middle of its outline: the Census
    Bureau's answer when it gives one (exact), otherwise the Atlas's coarse state outlines."""
    xs=[p[0] for r in rings for p in r]; ys=[p[1] for r in rings for p in r]; lo=sum(xs)/len(xs); la=sum(ys)/len(ys)
    try:
        j=fetch('https://geocoding.geo.census.gov/geocoder/geographies/coordinates',{'x':lo,'y':la,'benchmark':'Public_AR_Current','vintage':'Current_Current','layers':'States','format':'json'},timeout=30,tries=2)
        return j['result']['geographies']['States'][0]['STUSAB'].lower()
    except Exception:
        sys.path.insert(0,HERE)
        from lidar_dem import state_of
        return state_of(la,lo)
TODAY=str(datetime.date.today())
def stamp():
    """When a verdict was given, to the second: two sessions, or one session twice, often judge the same candidate on one day, and
    a date alone cannot say which came later. Older verdicts carry the date only; a timed one of the same day counts as later."""
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def die(msg): print(msg); sys.exit(1)

# ---------- the ledger: one file per unit, one candidate per line (so two sessions' changes merge cleanly in git) ----------
def slug(name): return re.sub(r'[^a-z0-9]+','-',name.lower()).strip('-')
def read_dir(d):
    L={}
    for f in sorted(glob.glob(os.path.join(d,'*.json'))):
        u=json.load(open(f,encoding='utf-8')); u.setdefault('cands',[]); L[u['name']]=u
    return L
def load(): return read_dir(LDIR)
def save(u):
    os.makedirs(LDIR,exist_ok=True); f=os.path.join(LDIR,slug(u['name'])+'.json')
    head=json.dumps({k:v for k,v in u.items() if k!='cands'},ensure_ascii=False)
    body=',\n'.join(json.dumps(c,ensure_ascii=False,separators=(',',':')) for c in u.get('cands',[]))
    open(f+'.tmp','w',encoding='utf-8').write(head[:-1]+',\n"cands":[\n'+body+('\n' if body else '')+']}\n'); os.replace(f+'.tmp',f)
def code_for(name,L):
    """A short letter code for a unit, from its initials: Taylor Pond Wild Forest -> tpwf. Candidate ids are code + number."""
    base=''.join(w[0] for w in re.findall(r'[A-Za-z]+',name)).lower()[:5]
    if len(base)<2: base=(re.sub(r'[^a-z]','',name.lower())+'xx')[:3]
    used={u['code'] for u in L.values()}; ws=re.findall(r'[A-Za-z]+',name)
    if base in used and ws and len(ws[0])>1: base=(ws[0][:2]+''.join(w[0] for w in ws[1:])).lower()[:6]    # Bates State Forest -> basf when bsf is taken
    code=base; k=0
    while code in used: k+=1; code=base+'abcdefghijklmnopqrstuvwxyz'[k%26]+('' if k<26 else 'abcdefghijklmnopqrstuvwxyz'[k//26])
    return code
def allc(L):
    for u in L.values():
        for c in u['cands']: yield u,c
def get(L,cid):
    cid=cid.lower().strip()
    for u,c in allc(L):
        if c['id']==cid: return u,c
    die('No candidate "'+cid+'". Ids look like tpwf12 (unit letters and a number); "lidar.py next" lists them.')
def rank(c):
    """Higher is more promising. A cellar is 5 to 12 m across and at least 0.6 m deep, and sits where the map says."""
    w,h=c['size']; big=max(w,h); small=min(w,h)
    return round(min(c['depth'],1.5)*(1.0 if 5<=small and big<=13 else 0.5)*(1.0 if c['dist']<=50 else 0.7),2)
def prefix(name): return WORK+'/sw_'+re.sub(r'[^a-z0-9]+','',name.lower())[:18]
def fetch(url,params=None,timeout=60,tries=3):
    if params: url=url+('&' if '?' in url else '?')+urllib.parse.urlencode(params)
    for k in range(tries):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=timeout))
        except Exception:
            if k==tries-1: raise
            time.sleep(4*(k+1))
def run(args,**kw): return subprocess.run([PY]+args,capture_output=True,text=True,**kw)
def place_ids():
    ids=set()
    for f in glob.glob(os.path.join(HERE,'data_*.py')): ids|=set(re.findall(r"N\('([a-z0-9\-]+)'",open(f,encoding='utf-8').read()))
    return ids

def import_walls(u,pre):
    """Keep the wall pieces a finished scan found (research/lidar/<prefix>_walls.json) as lidar/walls/<unit>.json."""
    f=pre+'_walls.json'
    if not os.path.exists(f): return None
    w=json.load(open(f)); m=0.0
    for a,b,c,d in w: m+=math.hypot((c-a)*1.1132,(d-b)*1.1132*math.cos(math.radians(a/1e5)))
    os.makedirs(WDIR,exist_ok=True); g=os.path.join(WDIR,slug(u['name'])+'.json')
    json.dump({'name':u['name'],'code':u['code'],'n':len(w),'m':round(m),'w':w},open(g+'.tmp','w'),separators=(',',':')); os.replace(g+'.tmp',g)
    u['walls']=len(w); u['wall_m']=round(m); save(u); return len(w),round(m)
def sync(L):
    """Bring a unit that tools/lidar_sweep.py has finished (research/lidar/sweep.json) into the ledger. One row per pit:
    where a pit lies near several map buildings the nearest is kept. A unit already 'done' is never touched again, so
    candidate ids stay what they were."""
    f=WORK+'/sweep.json'
    if not os.path.exists(f): return 0
    S=json.load(open(f)); new=0
    for name,su in S['units'].items():
        u=L.get(name)
        if u and u.get('state')=='done': continue
        if not u: u=L[name]={'name':name,'code':code_for(name,L),'cands':[]}
        best={}
        for c in S['cands']:
            if c['unit']!=name: continue
            k=(c['plat'],c['plon'])
            if k not in best or c['dist']<best[k]['dist']: best[k]=c
        rows=[{'lat':c['plat'],'lon':c['plon'],'depth':c['depth'],'size':c['size'],'dist':c['dist'],'blat':c['lat'],'blon':c['lon'],'sheet':c['sheet'],'year':c['year'],'status':'new'} for c in best.values()]
        rows.sort(key=lambda c:(-rank(c),c['lat'],c['lon']))
        u['cands']=[dict({'id':u['code']+str(i+1)},**c) for i,c in enumerate(rows)]
        u.update({'state':'done','swept':u.get('swept') or TODAY,'buildings':su['buildings'],'sheets':su.get('sheets',[])})
        for k in ('done','total','tries'): u.pop(k,None)
        save(u); new+=len(rows)
    return new

def merge_from(d):
    """Fold another copy of the ledger (the repository's) into this one. For each candidate the later verdict wins; with
    no dates to go by, the one further along (new < no < maybe < yes < published) wins. Nothing is ever dropped."""
    mine=load(); theirs=read_dir(d); n=0
    for name,t in theirs.items():
        m=mine.get(name)
        if not m: save(t); n+=1; continue
        if m.get('state')!='done' and t.get('state')=='done': save(t); n+=1; continue
        if t.get('state')!='done': continue
        tc={c['id']:c for c in t['cands']}; changed=False
        for i,c in enumerate(m['cands']):
            o=tc.get(c['id'])
            if not o or o==c: continue
            a=(c.get('when',''),ORDER.get(c['status'],0)); b=(o.get('when',''),ORDER.get(o['status'],0))
            # stamped the very same (only the old date-only verdicts can be), the workspace's own verdict stands: it is the one being
            # worked on, and "further along" would turn a "no" given this afternoon back into this morning's "maybe"
            if a[0] and a[0]==b[0]: continue
            if b>a: m['cands'][i]=o; changed=True
        if changed: save(m); n+=1
    return n

# ---------- status ----------
def counts(cs):
    by={}
    for c in cs: by[c['status']]=by.get(c['status'],0)+1
    return by
def cmd_status(a):
    L=load(); sync(L); cs=[c for u,c in allc(L)]; by=counts(cs)
    done=[u for u in L.values() if u.get('state')=='done']; part=[u for u in L.values() if u.get('state') in ('scanning','pairing')]
    bs={}
    for u in done: bs[st_of(u)]=bs.get(st_of(u),0)+1
    print(f"{len(done)} units swept"+(' ('+', '.join('%s %d'%(STATES[k]['name'],n) for k,n in sorted(bs.items()))+')' if len(bs)>1 else '')+f"; {len(cs)} pits beside an old-map building.")
    print('  not looked at yet: %d   set aside: %d   maybe: %d   yes, not written up: %d   published: %d'%tuple(by.get(k,0) for k in ('new','no','maybe','yes','published')))
    for u in part: print(f"  NOT FINISHED: {u['name']}. Run:  python3 tools/lidar.py sweep \"{u['name']}\"")
    left={}
    for u,c in allc(L):
        if c['status']=='new': left.setdefault(u['name'],[]).append(rank(c))
    if left:
        print('Not looked at yet, by unit (count, best rank):')
        for n,r in sorted(left.items(),key=lambda kv:-max(kv[1]))[:16]: print('  %4d  %.2f  %s'%(len(r),max(r),n))
    ids=place_ids()
    for u,c in allc(L):
        if c['status']=='published' and c.get('place') and c['place'] not in ids:
            print(f"  WARNING: {c['id']} is recorded as published as {c['place']}, but no tools/data_*.py has that place. If the draft was thrown away run:  python3 tools/lidar.py mark {c['id']} yes")
    print('Next:')
    if part: print('  finish the unfinished unit above.')
    if by.get('yes'): print('  write up the "yes" ones:  python3 tools/lidar.py check '+' '.join(c['id'] for c in cs if c['status']=='yes')[:160]+'   then   lidar.py draft <id>:<short-name> ...')
    if by.get('maybe'): print('  settle the "maybe" ones on full sheets:  python3 tools/lidar.py sheet '+' '.join(c['id'] for c in cs if c['status']=='maybe')[:200])
    if by.get('new'): print('  look at the next batch:  python3 tools/lidar.py next')
    print('  sweep more ground:  python3 tools/lidar.py near <lat> <lon> <miles>   then   python3 tools/lidar.py sweep "<unit>"')
    now=[u['name'] for u in done if u.get('walls') is None]
    print('Stone walls are mapped in %d of %d swept units%s'%(len(done)-len(now),len(done),('. Not yet: '+'; '.join(now[:6])+(' and %d more'%(len(now)-6) if len(now)>6 else '')+'.  python3 tools/lidar.py walls "<unit>"') if now else '.'))

# ---------- finding units ----------
def pad_units(where,extra=None):
    p={'where':where,'outFields':'Unit_Nm,GIS_Acres,Pub_Access,MngNm_Desc','returnGeometry':'false','f':'json','resultRecordCount':2000}
    if extra: p.update(extra)
    out={}
    for f in fetch(PAD,p,timeout=120).get('features',[]):
        t=f['attributes']; nm=t.get('Unit_Nm') or ''
        if not nm: continue
        o=out.setdefault(nm,{'acres':0,'access':t.get('Pub_Access'),'mgr':t.get('MngNm_Desc') or '','n':0}); o['acres']+=t.get('GIS_Acres') or 0; o['n']+=1
    return out
def show_units(U,L,limit=30):
    if not U: print('Nothing found.'); return
    print('   acres  access  swept   unit (manager)')
    for nm,o in sorted(U.items(),key=lambda kv:-kv[1]['acres'])[:limit]:
        st=(L.get(nm) or {}).get('state')
        print('%8d  %-6s  %-6s  %s (%s)'%(o['acres'],o['access'] or '?','yes' if st=='done' else 'part' if st else '-',nm,o['mgr'][:40]))
    print('Access: OA open, RA restricted (permit or season), XA closed, UK unknown. Sweep only OA and RA.')
    print('A scan takes about a minute for every 2,000 acres. Give "sweep" the name exactly as printed, capitals included.')
    print('Best ground: hill farms the state bought and reforested (state forests, wildlife areas). Parks give more false alarms.')
def take_state(a):
    """Takes --state xx out of the arguments. Returns (the rest, the state key or None)."""
    st=None
    if '--state' in a:
        i=a.index('--state'); st=(a[i+1] if i+1<len(a) else '').lower(); a=a[:i]+a[i+2:]
        if st not in STATES: die('--state must be one of: '+', '.join('%s (%s)'%(k,v['name']) for k,v in STATES.items()))
    return a,st
def cmd_find(a):
    a,st=take_state(a)
    if not a: die('Usage: lidar.py find "part of a name" [--state ny|ma|mo|ks]')
    # the service's state field is not filled in for every unit, so a state is taken as a box (it takes in the edges of its neighbours)
    U={}
    for k in ([st] if st else list(STATES)):          # a state at a time: one box round all of them would take in every state between New York and Kansas
        for nm,o in pad_units("Unit_Nm LIKE '%"+a[0].replace("'","''")+"%'",{'geometry':STATES[k]['box'],'geometryType':'esriGeometryEnvelope','inSR':4326,'spatialRel':'esriSpatialRelIntersects'}).items(): U.setdefault(nm,o)
    show_units(U,load())
    if not st: print('Searched: '+' and '.join(v['name'] for v in STATES.values())+'. To search one only, add  --state '+' or --state '.join(STATES)+'.')
def cmd_near(a):
    if len(a)<3: die('Usage: lidar.py near <lat> <lon> <miles>')
    la,lo,mi=float(a[0]),float(a[1]),float(a[2]); dla=mi/69.0; dlo=mi/(69.0*math.cos(math.radians(la)))
    U=pad_units("GIS_Acres>=100 AND Pub_Access IN ('OA','RA')",{'geometry':f'{lo-dlo},{la-dla},{lo+dlo},{la+dla}','geometryType':'esriGeometryEnvelope','inSR':4326,'spatialRel':'esriSpatialRelIntersects'})
    L=load(); show_units({k:v for k,v in U.items() if v['acres']>=300 and (L.get(k) or {}).get('state')!='done'},L)
    print('Listed: units of 300 acres or more that touch the box and are not yet swept. Names such as "Memorial Park" or\n"Conservation Area" belong to many places at once: leave those alone.')

# ---------- sweeping ----------
def outline(name,st=None):
    """The file holding a unit's outline, fetched if it is not there: pieces of that exact name inside the state's box
    (or, with no state given, inside all the states this tool covers)."""
    f=WORK+'/unit_'+''.join(ch for ch in name if ch.isalnum())+'.json'
    if os.path.exists(f): return f
    r=run([os.path.join(HERE,'lidar_unit.py'),name,'save',STATES[st]['box'] if st else ALLBOX]); m=re.search(r'wrote (\S+\.json)',r.stdout)
    if not m and 'did not answer' in (r.stdout+r.stderr): print('  The public-land service did not answer. This is not "no such unit": run the same command again in a minute.',flush=True)
    return m.group(1) if m else None
def cmd_sweep(a):
    mins=1.6; wide=False
    if '--minutes' in a: i=a.index('--minutes'); mins=float(a[i+1]); a=a[:i]+a[i+2:]
    if '--wide' in a: wide=True; a.remove('--wide')
    a,want=take_state(a)
    if not a: die('Usage: lidar.py sweep "Unit Name" ["Another"] [--minutes 1.6] [--state ny|ma]')
    t0=time.time(); end=t0+mins*60; L=load(); os.makedirs(WORK,exist_ok=True)
    if mins<3: print(f'Working for {int(mins*60)} seconds, then stopping cleanly. To do more in one go: --minutes 9, with your command time limit set to 10 minutes.',flush=True)
    for name in a:
        u=L.get(name)
        if u and want and st_of(u)!=want: print(f'SKIPPED "{name}": the ledger already has a unit of this name in {STATES[st_of(u)]["name"]}. One name is one unit here; tell the owner.'); continue
        if (u or {}).get('state')=='done': print('already swept:',name); continue
        if end-time.time()<25: print(f'TIME IS UP before "{name}". Run the same command again.'); return
        uf=outline(name,want or (u and st_of(u)))
        if not uf: print(f'NO SUCH UNIT: "{name}". Use the exact name printed by "lidar.py find" or "lidar.py near".'); continue
        rings=json.load(open(uf))['rings']; xs=[p[0] for r in rings for p in r]; ys=[p[1] for r in rings for p in r]
        span=max((max(ys)-min(ys))*111,(max(xs)-min(xs))*111*math.cos(math.radians(sum(ys)/len(ys))))
        if span>90 and not wide:
            os.remove(uf)
            print(f'SKIPPED "{name}": pieces with this name lie {int(span)} km apart, so it is probably several places that share a name.\n  If the others are in another state, name the state:  --state '+' or --state '.join(STATES)+'.  If it really is one big unit, add --wide.'); continue
        if not u:
            st=want or unit_state(rings)
            if st not in STATES:
                os.remove(uf); print(f'SKIPPED "{name}": it lies in {(st or "no state this tool knows").upper()}. This tool is set up for '+' and '.join(v['name'] for v in STATES.values())+' (LIDAR.md, "Another state", says what a new one needs).'); continue
            u=L[name]={'name':name,'code':code_for(name,L),'st':st,'state':'scanning','cands':[]}; save(u)
        st=st_of(u); pre=prefix(name)
        if not os.path.exists(pre+'_cands.json'):
            env=dict(os.environ); env['LIDAR_WALLS']='1'               # pits and stone walls from one fetch of the ground model
            env.setdefault('LIDAR_SRC',STATES[st]['src'])             # the whole unit from one source
            if u.get('tries',0)>=2: env['LIDAR_ALLOW_GAPS']='1'       # the same tiles failed twice: go on without them
            print(f'{name} ({STATES[st]["name"]}): scanning the ground model for pits and walls...',flush=True)
            r=subprocess.run([PY,os.path.join(HERE,'lidar_scan.py'),uf,pre,str(max(10,int(end-time.time()-8)))],env=env)
            if r.returncode in (3,4):
                pj=json.load(open(pre+'_partial.json')); u.update({'state':'scanning','done':pj['done'],'total':pj['total']})
                if r.returncode==4 and pj['done']==0:
                    save(u); print(f'NO GROUND MODEL for "{name}": not one tile could be fetched. The elevation service for {STATES[st]["name"]} may be down: try again later (tools/lidar_dem.py names the services).'); continue
                if r.returncode==4: u['tries']=u.get('tries',0)+1
                save(u); left=max(1,round((pj['total']-pj['done'])*2.2/60))
                print(f'NOT FINISHED: {name}: {pj["done"]} of {pj["total"]} tiles scanned, about {left} more minute(s) of scanning. Run the same command again; it carries on from here.'); return
            if r.returncode!=0 or not os.path.exists(pre+'_cands.json'): print('SCAN FAILED for',name,'(exit code %d). Run the same command again; if it fails the same way twice, tell the owner.'%r.returncode); continue
        sj=json.load(open(pre+'_scan.json')) if os.path.exists(pre+'_scan.json') else {}
        u.update({'state':'pairing','tiles':sj.get('total')}); u.pop('done',None); u.pop('total',None)
        if sj.get('failed'): u['gaps']=sj['failed']
        if sj.get('coarse'):
            u['coarse']=sj['coarse']
            print(f'WARNING: {name}: {sj["coarse"]} of {sj.get("total")} tiles have no 1 m LiDAR (the national model is coarse there). Nothing can be found on those: "nothing here" is not a finding for that part of the unit.')
        save(u)
        if end-time.time()<20: print(f'NOT FINISHED: {name}: the scan is complete; the old maps are next. Run the same command again.'); return
        print(f'{name}: scan complete. Finding buildings on the old survey sheets (each sheet is a 10 to 20 MB download, once)...',flush=True)
        env=dict(os.environ); env['LIDAR_DEADLINE']=str(end)
        if STATES[st].get('oldmap'): env['LIDAR_OLDMAP']=STATES[st]['oldmap']
        if u.get('btries',0)>=3: env['LIDAR_ALLOW_GAPS']='1'
        r=subprocess.run([PY,os.path.join(HERE,'lidar_sweep.py'),uf],env=env)
        if r.returncode==3:
            u['btries']=u.get('btries',0)+1; save(u); print(f'NOT FINISHED: {name}. Run the same command again; it carries on from here.'); return
        if r.returncode!=0: print('THE OLD-MAP STEP FAILED for',name,'. Run the same command again; if it fails the same way twice, tell the owner.'); continue
        L=load(); new=sync(L); u=L[name]
        for k in ('btries','tries'): u.pop(k,None)
        save(u); wl=import_walls(u,pre) if STATES[st].get('walls',True) else None          # no stone-wall layer where the straight banks are fence rows and terraces
        if wl: print(f'{name}: {wl[0]} straight pieces of wall, {wl[1]/1000:.1f} km in all, kept for the "Stone walls" map layer.')
        print(f'DONE: {name}: {u.get("buildings",0)} buildings on the old sheets, {new} pits beside one.'+(f' See them:  python3 tools/lidar.py next --unit "{name[:24]}"' if new else ' Nothing to look at here.'))

def cmd_walls(a):
    a,end=budget(a,1.6)
    if not a: die('Usage: lidar.py walls "Unit Name" ["Another"] [--minutes 1.6]')
    L=load(); os.makedirs(WORK,exist_ok=True)
    for name in a:
        u=L.get(name)
        if not u or u.get('state')!='done': print(f'"{name}" has not been swept. Sweep it instead (that maps its walls too):  python3 tools/lidar.py sweep "{name}"'); continue
        if u.get('walls') is not None and os.path.exists(os.path.join(WDIR,slug(name)+'.json')): print('walls already mapped:',name,'-',u['walls'],'pieces'); continue
        if end-time.time()<25: print(f'TIME IS UP before "{name}". Run the same command again.'); return
        uf=outline(name,st_of(u))
        if not uf: print(f'NO SUCH UNIT: "{name}".'); continue
        pre=prefix(name); env=dict(os.environ); env['LIDAR_WALLS']='only'; env.setdefault('LIDAR_SRC',STATES[st_of(u)]['src'])
        if u.get('wtries',0)>=2: env['LIDAR_ALLOW_GAPS']='1'
        print(f'{name}: reading the ground model for walls...',flush=True)
        r=subprocess.run([PY,os.path.join(HERE,'lidar_scan.py'),uf,pre,str(max(10,int(end-time.time()-8)))],env=env)
        if r.returncode in (3,4):
            pj=json.load(open(pre+'_partial.json'))
            if r.returncode==4: u['wtries']=u.get('wtries',0)+1; save(u)
            print(f'NOT FINISHED: {name}: {pj["done"]} of {pj["total"]} tiles, about {max(1,round((pj["total"]-pj["done"])*4.5/60))} more minute(s). Run the same command again; it carries on from here.'); return
        if r.returncode!=0: print('FAILED for',name,'(exit code %d). Run the same command again; if it fails the same way twice, tell the owner.'%r.returncode); continue
        u.pop('wtries',None); wl=import_walls(u,pre)
        print(f'DONE: {name}: {wl[0]} straight pieces of wall, {wl[1]/1000:.1f} km in all.' if wl else f'DONE: {name}: no wall file was written.')

# ---------- looking ----------
def metres(a,b,c,d): return math.hypot((c-a)*111320,(d-b)*111320*math.cos(math.radians(a)))
def near_known(L,u,c):
    """The nearest thing already dealt with inside 100 m: a published place of any kind, or a candidate with a verdict."""
    best=None
    for o in u['cands']:
        if o is c or o['status']=='new': continue
        d=metres(c['lat'],c['lon'],o['lat'],o['lon'])
        if d<=100 and (best is None or d<best[0]): best=(d,'%s (%s)'%(o['id'],o.get('place') or o['status']+(' '+o['why'] if o.get('why') else '')))
    try:
        for p in json.load(open('build/sites.json')):
            d=metres(c['lat'],c['lon'],p['lat'],p['lon'])
            if d<=100 and (best is None or d<best[0]) and p['id']!=c.get('place'): best=(d,'the published place '+p['id'])
    except Exception: pass
    return ('%d m from %s'%best) if best else ''
def cmd_next(a):
    unit=None
    if '--unit' in a: i=a.index('--unit'); unit=a[i+1].lower(); a=a[:i]+a[i+2:]
    n=max(6,min(36,int(a[0]))) if a else 36
    L=load(); sync(L)
    cs=[(u,c) for u,c in allc(L) if c['status']=='new' and (unit is None or unit in u['name'].lower())]
    cs=sorted(cs,key=lambda uc:(-rank(uc[1]),uc[1]['id']))[:n]
    if not cs: die('Nothing left to look at'+(' in that unit' if unit else '')+'. Sweep more ground:  python3 tools/lidar.py near <lat> <lon> <miles>')
    os.makedirs(WORK,exist_ok=True); spots=WORK+'/next_spots.txt'; out=WORK+'/next_%s_%s.jpg'%(cs[0][1]['id'],cs[-1][1]['id'])
    open(spots,'w').write(''.join('%s %s %s\n'%(c['id'],c['lat'],c['lon']) for u,c in cs))
    r=run([os.path.join(HERE,'lidar_triage.py'),out,spots])
    if not os.path.exists(out): die('The picture could not be drawn: '+(r.stdout+r.stderr)[-300:])
    print('id       rank  depth   size    map building        unit')
    for u,c in cs:
        nk=near_known(L,u,c); print('%-8s %.2f  %.2f m  %2dx%-2d m  %3d m away (%d)  %s%s'%(c['id'],rank(c),c['depth'],c['size'][0],c['size'][1],c['dist'],c['year'],u['name'],('   <-- '+nk+': the same site?') if nk else ''))
    print(f'\nLOOK AT THIS PICTURE (open it with your image-reading tool): {out}')
    print('It is a grid, six to a row, in the order above, each chip labelled with its id. A chip is 140 m across, north up,\nlit from the north-west, with the pit between the four pink ticks. A dark red chip means the ground model did not load.')
    print('Give EVERY chip a verdict (LIDAR.md says how to judge). All at once, one line each:')
    print("  python3 tools/lidar.py mark - <<'EOF'\n  %s no faint\n  %s maybe ring with a straight bank beside it\n  EOF"%(cs[0][1]['id'],cs[-1][1]['id']))
    print('then make full sheets for the "maybe" ones:  python3 tools/lidar.py sheet <ids>')
def tnm(la,lo):
    """Old USGS sheets whose map area covers a point: [[year, scale, file name, url, [w,s,e,n]]]. The answer for each
    0.05-degree cell is remembered; the sheet's own bounds then decide, so a point beside a sheet edge gets the right sheet."""
    f=WORK+'/tnm_cells.json'; C=json.load(open(f)) if os.path.exists(f) else {}
    cx=math.floor(lo/0.05)*0.05; cy=math.floor(la/0.05)*0.05; k='%.2f,%.2f'%(cy,cx)
    if k not in C:
        j=fetch('https://tnmaccess.nationalmap.gov/api/v1/products',{'datasets':'Historical Topographic Maps','bbox':f'{cx},{cy},{cx+0.05},{cy+0.05}','prodFormats':'GeoTIFF','max':300},tries=4)
        out=[]
        for it in j.get('items',[]):
            url=it.get('downloadURL') or ''; m=re.search(r'/([A-Z]{2}_[^/]*?_(\d{4})_(\d+)_geo\.tif)$',url); bb=it.get('boundingBox') or {}
            if m and None not in [bb.get(x) for x in ('minX','minY','maxX','maxY')]: out.append([int(m.group(2)),int(m.group(3)),m.group(1),url,[bb['minX'],bb['minY'],bb['maxX'],bb['maxY']]])
        C[k]=sorted(out); os.makedirs(WORK,exist_ok=True); json.dump(C,open(f,'w'))
    return [i for i in C[k] if i[4][0]<=lo<=i[4][2] and i[4][1]<=la<=i[4][3]]
def tif_for(item):
    """Path of a sheet in cache/topo, downloading it if it is not there."""
    for p in ('cache/topo/'+item[2],'cache/topo/'+urllib.parse.quote(item[2]),'cache/topo/'+urllib.parse.unquote(item[2])):
        if os.path.exists(p): return p
    r=run([os.path.join(HERE,'lidar_sheet.py'),'get',item[3]]); p=(r.stdout.strip().splitlines() or [''])[-1]
    return p if p and os.path.exists(p) else None
def maps_for(c):
    """(old sheet, later sheet) for a candidate. The later one is the 1:24,000 or 1:31,680 sheet nearest 1945."""
    items=tnm(c['lat'],c['lon']); want=urllib.parse.unquote(c['sheet'])
    old=[i for i in items if urllib.parse.unquote(i[2])==want] or [i for i in items if i[1]==62500 and i[0]<=1915]
    late=sorted([i for i in items if 1925<=i[0]<=1965 and i[1]<=31680],key=lambda i:(abs(i[0]-1945),i[1]))
    return (old[0] if old else None),(late[0] if late else None)
def quad(fn):
    m=re.match(r'[A-Z]{2}_(.*?)_\d+_(\d{4})_\d+_geo\.tif$',urllib.parse.unquote(fn)); return m.group(1).replace('_',' ') if m else fn
def budget(a,default=1.4):
    """Takes --minutes N out of the arguments. Returns (the rest, the time to stop at)."""
    mins=default
    if '--minutes' in a: i=a.index('--minutes'); mins=float(a[i+1]); a=a[:i]+a[i+2:]
    return a,time.time()+mins*60
def cmd_sheet(a):
    a,end=budget(a)
    if not a: die('Usage: lidar.py sheet tpwf12 smwf3 ...')
    L=load(); groups={}; left=[]
    for cid in a:
        u,c=get(L,cid)
        if time.time()>end-30: left.append(c['id']); continue          # a new map can take half a minute to download
        try: o,l=maps_for(c)
        except Exception as e: print('  the map list could not be fetched for',c['id'],'- try again:',str(e)[:80]); continue
        to=tif_for(o) if o else None; tl=tif_for(l) if l else None
        if not to: print('  no old sheet could be fetched for',c['id'],'- skipped; try again'); continue
        c['late']=[l[0],l[2]] if (l and tl) else None
        groups.setdefault((to,tl or ''),[]).append((u,c))
    made=[]
    for (to,tl),ucs in groups.items():
        for k in range(0,len(ucs),3):
            part=ucs[k:k+3]
            if time.time()>end-15: left+=[c['id'] for u,c in part]; continue
            out=WORK+'/sheet_%s%s.jpg'%(part[0][1]['id'],('_'+part[-1][1]['id']) if len(part)>1 else '')
            if os.path.exists(out): os.remove(out)
            r=run([os.path.join(HERE,'lidar_sheet.py'),'sheet',out,'100',to+((','+tl) if tl else '')]+['%s,%s,%s'%(c['id'],c['lat'],c['lon']) for u,c in part])
            if not os.path.exists(out) or 'wrote' not in r.stdout:
                print('  the sheet could not be drawn for',' '.join(c['id'] for u,c in part),':',(r.stdout+r.stderr)[-200:]); continue
            try:
                from PIL import Image
                im=Image.open(out); im.thumbnail((1600,1600)); im.save(out,quality=82)
            except Exception: pass
            for u,c in part: c['seen']=TODAY; save(u)
            made.append((out,part,to,tl))
    for out,part,to,tl in made:
        print(f'LOOK AT THIS PICTURE: {out}')
        print('  rows, top to bottom: '+', '.join(c['id'] for u,c in part))
        for u,c in part:
            nk=near_known(L,u,c)
            if nk: print('  NOTE %s is %s: if it is the same site, mark it:  no dup'%(c['id'],nk))
        print('  columns, left to right: LiDAR | leaf-off aerial | %s %d map%s'%(quad(os.path.basename(to)),part[0][1]['year'],(' | %s %d map'%(quad(os.path.basename(tl)),part[0][1]['late'][0])) if tl else '  (no 1925-1965 large-scale sheet exists here)'))
    if made:
        print('LiDAR and aerial show the same 200 m square. The map panels are wider (each says how wide along its top): look for the\nsmall black square or dot of a building at the pink ticks. North is up; the ticks mark the pit in every panel.')
        print('For each row answer the four questions in LIDAR.md, then:  python3 tools/lidar.py mark <id> yes <what you saw>   or   mark <id> no <reason>')
    if left: print('NOT FINISHED (time was up). Look at the pictures above, then run:  python3 tools/lidar.py sheet '+' '.join(left))
def mark_one(L,a):
    """One verdict. Returns (ok, message)."""
    if len(a)<2 or a[1] not in ORDER or a[1]=='published': return False,'not understood: '+' '.join(a)+'   (want: <id> no|maybe|yes|new [reason word] [note])'
    cid=a[0].lower().strip(); hit=[(u,c) for u,c in allc(L) if c['id']==cid]
    if not hit: return False,'no candidate "'+cid+'"'
    u,c=hit[0]; st=a[1]; rest=a[2:]
    if c['status']=='published' and c.get('place') in place_ids(): return False,c['id']+' is published as '+c['place']+'. Leave it.'
    if st=='yes' and not c.get('seen'): return False,c['id']+': before "yes", look at the full comparison sheet:  python3 tools/lidar.py sheet '+c['id']
    if st=='no' and (not rest or rest[0] not in REASONS): return False,c['id']+': a "no" needs a reason word first: '+' '.join(REASONS)
    was=('   (it was: %s%s, %s)'%(c['status'],' '+c['why'] if c.get('why') else '',c.get('when','no date'))) if c['status'] in ('no','yes','published') else ''
    for k in ('why','place','batch','note'): c.pop(k,None)
    if st=='no': c['why']=rest[0]; rest=rest[1:]
    if rest: c['note']=' '.join(rest)
    c['status']=st; c['when']=stamp(); save(u); return True,'%s -> %s %s %s%s'%(c['id'],st,c.get('why',''),c.get('note',''),was)
def cmd_mark(a):
    L=load()
    if a and a[0]=='-':           # many at once: one verdict per line on standard input
        bad=0
        for line in sys.stdin:
            if not line.strip() or line.lstrip().startswith('#'): continue
            ok,msg=mark_one(L,line.split()); bad+=not ok; print(('   ' if ok else 'NOT RECORDED: ')+msg)
        if bad: print(bad,'line(s) were not recorded: fix them and send those lines again.')
        return
    ok,msg=mark_one(L,a)
    if not ok: die(msg+'\nUsage: lidar.py mark tpwf12 no|maybe|yes|new [reason word] [note...]   Reason words for "no": '+' '.join(REASONS))
    print(msg)
def cmd_show(a):
    L=load()
    for cid in a:
        u,c=get(L,cid); print(u['name']); print(json.dumps(c,indent=1)); print('rank',rank(c),'  https://www.google.com/maps?q=%s,%s'%(c['lat'],c['lon']))

# ---------- ownership ----------
def cmd_check(a):
    a,end=budget(a)
    if not a: die('Usage: lidar.py check smwf3 ...')
    L=load(); left=[]
    for cid in a:
        u,c=get(L,cid); la,lo=c['lat'],c['lon']; k={}
        if time.time()>end-10: left.append(c['id']); continue
        st=st_of(u); r=run([os.path.join(HERE,'parcel.py'),'--state',st,str(la),str(lo)]); line=(r.stdout.strip().splitlines() or [''])[-1]
        if 'lookup failed' in line: print(c['id'],': the parcel service did not answer. Run check again.'); continue
        if '->' in line:
            f=[x.strip() for x in line.split('->',1)[1].split('|')]
            k['parcel']={'kind':f[0],'class':f[1].replace('class','').strip() if len(f)>1 else '','acres':f[2].replace('acres','').strip() if len(f)>2 else '','muni':f[3] if len(f)>3 else '','addr':f[4] if len(f)>4 else ''}
        else: k['parcel']=None
        # the lots round about: a pit on public land can be 40 m from somebody's house lot, and the 200 m sheet does not show it
        ring=[]; kk=math.cos(math.radians(la))
        for nm,dx,dy in (('north',0,1),('north-east',.7,.7),('east',1,0),('south-east',.7,-.7),('south',0,-1),('south-west',-.7,-.7),('west',-1,0),('north-west',-.7,.7)):
            ring+=[nm,'%.6f'%(la+75*dy/111320),'%.6f'%(lo+75*dx/(111320*kk))]
        r=run([os.path.join(HERE,'parcel.py'),'--state',st]+[x for i,x in enumerate(ring) if i%3]); rl=r.stdout.strip().splitlines()
        k['near']=[ring[3*i] for i in range(8) if i<len(rl) and '-> PRIVATE' in rl[i]] if len(rl)==8 else None
        r=run([os.path.join(HERE,'pad.py'),'%s,%s,%s'%(c['id'],la,lo)])
        if 'ERROR' in r.stdout: print(c['id'],': the public-land service did not answer. Run check again.'); continue
        pu=re.findall(r"\('([^']*)', '([^']*)', '([^']*)'\)",r.stdout); pu=sorted(pu,key=lambda x:(x[2] not in ('OA','RA'),x[0]!=u['name']))
        k['padus']={'unit':pu[0][0],'manager':pu[0][1],'access':pu[0][2]} if pu else None
        try:
            j=fetch('https://geocoding.geo.census.gov/geocoder/geographies/coordinates',{'x':lo,'y':la,'benchmark':'Public_AR_Current','vintage':'Current_Current','layers':'County Subdivisions,Counties','format':'json'})
            g=j['result']['geographies']; k['town']=re.sub(r' (town|city|village)$','',(g.get('County Subdivisions') or [{}])[0].get('NAME','')); k['county']=re.sub(r' County$','',(g.get('Counties') or [{}])[0].get('NAME',''))
        except Exception: k['town']=k['county']=''
        try:
            j=fetch('https://nominatim.openstreetmap.org/reverse',{'format':'jsonv2','lat':la,'lon':lo,'zoom':17,'addressdetails':1}); k['road']=(j.get('address') or {}).get('road') or ''; time.sleep(1.1)
        except Exception: k['road']=''
        p=k['parcel']; pd=k['padus']
        if p and p['kind']=='PRIVATE': k['rule']='private'; say='DO NOT PUBLISH: the tax parcel is PRIVATE. Now run:  python3 tools/lidar.py mark %s no private'%c['id']
        elif p and (p['kind']=='STATE LAND' or p['kind'].startswith('public')): k['rule']='parcel'; say='MAY PUBLISH: the tax parcel is public land.'
        elif pd and pd['access'] in ('OA','RA'):
            k['rule']='padus'
            say=('MAY PUBLISH WITH A CAVEAT: the tax parcel is tax-exempt land that is not government-owned (a land trust or the like), and the federal public-land record names the unit as open. The draft writes the caveat; find the owner\'s own visiting rules for the access line.' if p and p['kind'].startswith('tax-exempt')
                 else 'MAY PUBLISH WITH A CAVEAT: no owner in the tax-parcel file here, but the federal public-land record names the unit. The draft writes the caveat for you.')
        else: k['rule']='none'; say='DO NOT PUBLISH: no public owner in the parcel file and no public-land record. Add a row to LEADS.md, then run:  python3 tools/lidar.py mark %s no noland'%c['id']
        c['check']=k; save(u)
        print(c['id'],'|',k.get('town') or '?','|',(k.get('county') or '?'),'County | nearest named road:',k.get('road') or 'none found')
        print('   tax parcel:',('%s, class %s, %s acres%s'%(p['kind'],p['class'],p['acres'],(', '+p['addr']) if p['addr'] and p['kind']!='PRIVATE' else '')) if p else ('no record (this county is not in the state file, or the point is on a road)' if st=='ny' else 'no record ('+STATES[st]['noparcel']+')' if STATES[st].get('noparcel') else 'no record (the point is on a road, a railway or water)'))
        print('   public-land record:',('%s (%s), access %s'%(pd['unit'],pd['manager'],pd['access'])) if pd else 'nothing at this point')
        if k.get('near'): print('   PRIVATE LAND within about 75 m, to the '+', '.join(k['near'])+'. Look at the aerial for a house there (tools/pincheck.py shows 300 m) and say in the access line which side is public.')
        elif k.get('near') is None: print('   the lots round about could not be read (the parcel service did not answer for all eight points)')
        print('  ',say)
    if left: print('NOT FINISHED (time was up). Run:  python3 tools/lidar.py check '+' '.join(left))

# ---------- writing up ----------
def cmd_draft(a):
    if not a or any(':' not in x for x in a): die('Usage: lidar.py draft <id>:<short-name> ...   e.g.  draft smwf3:mussey-road-crossroads tpwf1:rock-street-house-site\nThe short name is lower-case words joined by hyphens saying where and what; the place id becomes lidar-<short-name>.')
    L=load(); ids=place_ids(); todo=[]
    for x in a:
        cid,nm=x.split(':',1); u,c=get(L,cid); pid='lidar-'+re.sub(r'^lidar-','',nm.strip().lower())
        if not re.match(r'^lidar-[a-z0-9]+(-[a-z0-9]+)+$',pid): die('"%s" is not a usable short name: lower-case letters, digits and hyphens, at least two words.'%nm)
        if pid in ids or pid in [t[2] for t in todo]: die('The place id %s is taken. Choose another short name.'%pid)
        if c['status']!='yes': die('%s is "%s", not "yes". Look at its full sheet and mark it yes first.'%(c['id'],c['status']))
        if 'check' not in c: die('Run first:  python3 tools/lidar.py check '+c['id'])
        if c['check']['rule'] in ('private','none'): die('%s may not be published as public land. See what "check" printed for it.'%c['id'])
        todo.append((u,c,pid))
    key='lidar_%s_%s'%(datetime.date.today().strftime('%m%d'),todo[0][0]['code']); k=0
    while os.path.exists(os.path.join(HERE,'data_%s.py'%key)): k+=1; key='lidar_%s_%s%d'%(datetime.date.today().strftime('%m%d'),todo[0][0]['code'],k+1)
    f=os.path.join(HERE,'data_%s.py'%key); body=[]; notes=[]
    for u,c,pid in todo:
        k=c['check']; w,h=c['size']; q=quad(c['sheet']); late=c.get('late'); p=k.get('parcel'); pd=k.get('padus'); st=st_of(u)
        story="The %d USGS survey (%s sheet) draws a building about %d m from here. TODO: what is beside it on that map (a road, a stream, a crossroads)? %s"%(c['year'],q,c['dist'],
              ("TODO: what does the %d sheet (%s) show at this spot? Is the building still drawn?"%(late[0],quad(late[1]))) if late else "No later map was looked at, so when it went is not known.")
        look="On LiDAR: TODO: the shape you see (round or square, a rim, walls, banks or an old road beside it); the pit is about %d by %d m and %.1f m deep. The leaf-off aerial shows TODO: woods, brush or field, and nothing standing. Not checked on the ground."%(w,h,c['depth'])
        road=k.get('road') or ''
        if k['rule']=='parcel':
            acc="%s: the tax parcel under the pin is a %s-acre lot%s%s. %s TODO: the marked trail or parking place for this spot, or say that none was found."%('State land' if p['kind']=='STATE LAND' else 'Public or conservation land',p['acres'],' owned by the state' if p['kind']=='STATE LAND' else '',(', in '+pd['unit']) if pd else '',('The nearest road OpenStreetMap names is '+road+'.') if road else 'No named road is near.')
        else:
            if p and p['kind'].startswith('tax-exempt'): lead='The tax parcel under the pin is tax-exempt land that is not government-owned (a land trust, a charity or the like). TODO: who that is, and their own visiting rules, from their own page.'
            elif st=='ny': lead="No tax-parcel record could be checked: %s."%(("%s County is not in the state's public parcel file"%(k.get('county') or 'This')) if not p else "the county's parcel record does not give the owner")
            elif STATES.get(st,{}).get('noparcel'): lead="No tax-parcel record could be checked: %s."%STATES[st]['noparcel']
            else: lead="No tax-parcel record could be checked: %s."%('no parcel covers the pin (it may sit on an old road layout)' if not p else 'the parcel record does not give the owner')
            acc=lead+" The federal protected-areas database puts the spot inside %s, open to the public%s. Public land is a patchwork with private lots inside it, so confirm with the Owner? button or the state boundary signs before you leave the road."%(pd['unit'],(', and the nearest road OpenStreetMap names is '+road) if road else '. No named road is near')
        tail='+HUNT' if re.search(r'Forest|Wma|Wildlife|Wild Forest|Wilderness|Multiple Use',u['name']) else "+' TODO: the opening hours and any fee, from the managing body\\'s own page.'"
        years=('before %d'%c['year'])+(('–TODO: add "before %d" if the later sheet no longer draws it'%late[0]) if late else '')
        if k.get('near'): acc+=' Private land lies within about 75 m to the %s: TODO: say which side of the road or wall is public, and whether a house stands there (look at the pin check).'%', '.join(k['near'])
        body.append("# %s  rank %.2f  verdict note: %s\nN(%r,%r,%r,%r,'lidar','traces',%s,%s,%r,'public','hike','',%r,\n  %r,\n  %r,\n  %r,\n  %r%s,SRC,conf='lead',brick='?'),"%(c['id'],rank(c),c.get('note') or '(none)',pid,'TODO: a plain name, what it is and where',k.get('town') or 'TODO: town',region_of(st,k.get('county')),c['lat'],c['lon'],'exact' if c['dist']<=60 else 'site',years,story,look,'TODO: one short line, why it is worth the walk',acc,tail))
        notes.append(" %r:%r,"%(pid,"The pin is the pit on LiDAR. The building on the %d sheet is drawn about %d m away%s. Looked at on LiDAR and the leaf-off aerial; not seen on the ground."%(c['year'],c['dist'],'; sheets of that scale can be 50 to 100 m out' if c['dist']>30 else '')))
        for kk in ('why',): c.pop(kk,None)
        c.update({'status':'published','place':pid,'batch':key,'when':stamp()}); save(u)
    units=sorted({u['name'] for u,c,pid in todo})
    open(f,'w',encoding='utf-8').write('''# %s: LiDAR finds in %s, drafted by tools/lidar.py (method: LIDAR.md).
# Every entry is an unverified lead (conf='lead'): a pit on the LiDAR ground model beside a building on an old
# USGS sheet, nothing standing on the leaf-off aerial, on land the records show as public. Nothing was seen on the ground.
# FINISH EVERY "TODO" BEFORE BUILDING: tools/check.py refuses a place that still has one. Say only what you saw.
from data_b import N
from data_lidar3 import SRC,HUNT
BATCH={'key':%r,'label':'LiDAR finds: TODO: a few words saying where','added':%r}
PLACES=[
%s
]
PIN_NOTES={
%s
}
'''%(datetime.date.today().strftime('%B %d, %Y'),', '.join(units),key,datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M'),'\n'.join(body),'\n'.join(notes)))
    print('wrote',f,'with',len(todo),'place(s). Now:')
    print('  1. Open that file and replace every TODO with what you saw on the sheets. Change nothing you did not check.')
    print('  2. python3 tools/topo_all.py '+' '.join(pid for u,c,pid in todo))
    print('  3. python3 tools/pincheck.py --batch '+key+'      and LOOK at the picture it writes')
    print('  4. build and publish as LIDAR.md step 7 says')

def cmd_report(a):
    """What this session did: the ledger now against the copy taken when the workspace was set up (research/lidar/base).
    Without that copy, what carries today's date."""
    L=load(); base=read_dir(WORK+'/base') if os.path.isdir(WORK+'/base') else None
    if base is not None:
        old={c['id']:c for u in base.values() for c in u['cands']}
        sw=[u for u in L.values() if u.get('state')=='done' and (base.get(u['name']) or {}).get('state')!='done']
        mk=[(u,c) for u,c in allc(L) if c['status']!='new' and (c['id'] not in old or old[c['id']]['status']!=c['status'])]
        print('LiDAR work since this workspace was set up')
    else:
        sw=[u for u in L.values() if u.get('swept')==TODAY and u.get('state')=='done']; mk=[(u,c) for u,c in allc(L) if str(c.get('when','')).startswith(TODAY)]
        print('LiDAR work dated',TODAY)
    if sw: print('Units swept: '+'; '.join('%s (%d buildings on the old sheets, %d pits beside one)'%(u['name'],u.get('buildings',0),len(u['cands'])) for u in sw))
    no=[c for u,c in mk if c['status']=='no']; why={}
    for c in no: w=c.get('why','other'); why[w]=why.get(w,0)+1
    print('Candidates given a verdict: %d. Set aside: %d%s. Left as "maybe": %d. Marked yes, not yet written up: %d. Written up as places: %d.'%(len(mk),len(no),(' ('+'; '.join('%d: %s'%(n,REASONS[w]) for w,n in sorted(why.items(),key=lambda kv:-kv[1]))+')') if no else '',sum(1 for u,c in mk if c['status']=='maybe'),sum(1 for u,c in mk if c['status']=='yes'),sum(1 for u,c in mk if c['status']=='published')))
    for u,c in mk:
        if c['status']=='published': print('  %s | %s | %s,%s | ownership: %s'%(c.get('place'),u['name'],c['lat'],c['lon'],{'parcel':'the tax parcel is public land','padus':'public-land record only; no parcel could be checked'}.get((c.get('check') or {}).get('rule'),'not recorded')))
    by=counts([c for u,c in allc(L)]); print('Ledger now: %d units swept, %d candidates, %d not yet looked at.'%(sum(1 for u in L.values() if u.get('state')=='done'),sum(by.values()),by.get('new',0)))
    print('Not verified: nothing here has been seen on the ground. Every place is conf=lead.')
def cmd_pull(a):
    """Fold the repository's copy of the ledger into the workspace's. With --base (tools/setup.sh does this) also keep a
    copy of it as the starting point that "report" measures from."""
    base='--base' in a; a=[x for x in a if x!='--base']
    if not a or not os.path.isdir(a[0]): print('no ledger at',a[0] if a else '?','(nothing to bring in)'); return
    n=merge_from(a[0]); print('ledger: %d unit file(s) brought in from %s; %d units in all'%(n,a[0],len(load())))
    if base:
        import shutil
        shutil.rmtree(WORK+'/base',ignore_errors=True); os.makedirs(WORK,exist_ok=True); shutil.copytree(a[0],WORK+'/base')

CMDS={'status':cmd_status,'find':cmd_find,'near':cmd_near,'sweep':cmd_sweep,'walls':cmd_walls,'next':cmd_next,'sheet':cmd_sheet,'mark':cmd_mark,'show':cmd_show,'check':cmd_check,'draft':cmd_draft,'report':cmd_report,'pull':cmd_pull}
if __name__=='__main__':
    if len(sys.argv)<2 or sys.argv[1] not in CMDS: print(__doc__); sys.exit(0 if len(sys.argv)<2 else 1)
    if not os.path.isdir('tools') or not os.path.isdir('src'): die('Run this from the workspace root (the folder with tools/ and src/):  cd "$ATLAS" && python3 tools/lidar.py status')
    try: CMDS[sys.argv[1]](sys.argv[2:])
    except BrokenPipeError: pass          # the output was piped into head
