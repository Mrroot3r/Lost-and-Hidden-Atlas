#!/usr/bin/env python3
"""Run the LiDAR farmstead search (GUIDE.md section 13, steps 2 to 4) over many units of public land in one go.

   python3 tools/lidar_sweep.py research/lidar/unit_A.json research/lidar/unit_B.json ...
        for each unit: scans it for pits (tools/lidar_scan.py), finds the oldest 1:62,500 survey sheets over it,
        downloads the ones not yet in cache/topo/, lists the buildings those sheets draw inside the unit with any pit
        within 90 m (tools/lidar_buildings.py), and adds what it finds to research/lidar/sweep.json.
        A unit already in sweep.json is skipped, so the command can be stopped and run again.
   python3 tools/lidar_sweep.py rank
        prints the candidates in order of promise: a deep, house-sized pit close to the old map's building comes first.

This only gathers candidates. A person still has to LOOK at each one (tools/lidar_sheet.py sheet ...) and check the
tax parcel (tools/parcel.py) before it is a find. Most candidates are not."""
import sys,os,json,re,subprocess,urllib.request,urllib.parse,time,math
OUT='research/lidar/sweep.json'; UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
def load(): return json.load(open(OUT)) if os.path.exists(OUT) else {'units':{},'cands':[]}
def pts(rings):
    for r in rings:
        for p in r: yield p
def sheets(lo,la):
    """Old survey sheets over a point that are detailed enough to place a building, oldest first: [(year, name, url, (w,s,e,n))].
    New York and Massachusetts: the 1:62,500 sheets, as always. A state whose first survey was at 1:125,000, too coarse to say which
    pit was a house (Missouri, Kansas), takes any sheet at 1:62,500 or larger up to the year the sweeper is told (LIDAR_OLDMAP)."""
    d=0.0005
    u='https://tnmaccess.nationalmap.gov/api/v1/products?'+urllib.parse.urlencode({'datasets':'Historical Topographic Maps','bbox':f'{lo-d},{la-d},{lo+d},{la+d}','prodFormats':'GeoTIFF','max':100})
    for k in range(4):
        try: j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60)); break
        except Exception as e:
            if k==3: return []
            time.sleep(6*(k+1))
    out=[]
    for it in j.get('items',[]):
        url=it.get('downloadURL') or ''; m=re.search(r'/([A-Z]{2}_[^/]*?_(\d{4})_(\d+)_geo\.tif)$',url)
        if not m or not lidar_oldmap.sheet_ok(0,int(m.group(3)),LASTYEAR,ANYSCALE): continue
        b=it.get('boundingBox') or {}
        out.append((int(m.group(2)),m.group(1),url,(b.get('minX'),b.get('minY'),b.get('maxX'),b.get('maxY'))))
    return sorted(out,key=lambda t:(t[0],int(re.search(r'_(\d+)_geo',t[1]).group(1)),t[1]))          # oldest first; of one year, the more detailed
# LIDAR_OLDMAP="<last year>,any": the latest year an old sheet may have, and whether scales larger than 1:62,500 count (tools/lidar.py sets it by state)
import lidar_oldmap
LASTYEAR,ANYSCALE=lidar_oldmap.rule(os.environ.get('LIDAR_OLDMAP'))
_INK={}
def ink(tif):
    """How dark a scanned sheet prints black: red+green+blue of its darkest ink. Under about 100 is a good scan; 250 is pale."""
    if tif not in _INK:
        try:
            import rasterio,numpy as np
            with rasterio.open(tif) as ds: a=ds.read(out_shape=(ds.count,ds.height//4,ds.width//4)).astype('int32')
            _INK[tif]=float(np.percentile(a[:3].sum(0),0.2))
        except Exception: _INK[tif]=0.0
    return _INK[tif]
def rank(c):
    """Higher is more promising. A cellar is 5 to 12 m across and at least 0.6 m deep, and sits where the map says."""
    w,h=c['size']; big=max(w,h); small=min(w,h)
    shape=1.0 if 5<=small and big<=13 else 0.5
    return round(min(c['depth'],1.5)*shape*(1.0 if c['dist']<=50 else 0.7),2)
if len(sys.argv)>1 and sys.argv[1]=='rank':
    S=load(); cs=sorted(S['cands'],key=lambda c:-rank(c))
    print(len(S['units']),'units,',sum(u['buildings'] for u in S['units'].values()),'map buildings,',len(cs),'pits beside one')
    for c in cs: print(f"{rank(c):4} {c['unit'][:28]:28} pit {c['plat']:.6f},{c['plon']:.6f} {c['depth']:.2f} m {c['size'][0]}x{c['size'][1]}  {c['dist']} m from the {c['year']} symbol at {c['lat']},{c['lon']}  {c['sheet']}")
    sys.exit()
S=load()
REDO='--redo' in sys.argv
DEADLINE=float(os.environ.get('LIDAR_DEADLINE') or 0)     # set by tools/lidar.py: stop cleanly at this time and say so (exit code 3)
for uf in [a for a in sys.argv[1:] if a!='--redo']:
    unit=json.load(open(uf)); name=unit.get('name') or os.path.basename(uf)
    if name in S['units'] and REDO:   # look for buildings again (new sheet rules): forget what was found for this unit
        S['units']=[u for u in S['units'] if u!=name] if isinstance(S['units'],list) else {k:v for k,v in S['units'].items() if k!=name}
        S['cands']=[c for c in S['cands'] if c.get('unit')!=name]
        import glob
        for f in glob.glob('research/lidar/sw_'+re.sub(r'[^a-z0-9]+','',name.lower())[:18]+'_b_*.txt'): os.remove(f)
    if name in S['units']: print('skip (done):',name); continue
    P=list(pts(unit['rings'])); xs=[p[0] for p in P]; ys=[p[1] for p in P]
    pre='research/lidar/sw_'+re.sub(r'[^a-z0-9]+','',name.lower())[:18]
    t0=time.time()
    if not os.path.exists(pre+'_cands.json'):   # a finished scan is kept: only the look for buildings is repeated
        r=subprocess.run([sys.executable,'tools/lidar_scan.py',uf,pre],capture_output=True,text=True)
        if not os.path.exists(pre+'_cands.json'): print('SCAN FAILED',name,(r.stdout+r.stderr)[-200:]); continue
    # The oldest sheet over every 15-minute square the unit's outline touches (old sheets are 15 minutes on a side).
    # The first version asked only at the four corners of the unit's box and its middle, which for a big unit made of
    # scattered pieces (a wild forest) can miss every piece: Taylor Pond Wild Forest came back with no buildings at all.
    cells={}; ALT={}
    for x,y in P: cells.setdefault((math.floor(x*4),math.floor(y*4)),[]).append((x,y))
    asks=[(sum(a for a,b in v)/len(v),sum(b for a,b in v)/len(v)) for k,v in sorted(cells.items(),key=lambda kv:-len(kv[1]))[:14]]
    want={}
    for lo,la in asks:
        ss=[s for s in sheets(lo,la) if s[0]<=LASTYEAR]
        if ss:
            quad=ss[0][1].split('_')[1]
            if quad not in want:
                want[quad]=ss[0]; ALT[quad]=[]; seen={ss[0][0]}
                for s in ss[1:]:                                    # later printings of the same sheet, one a year, in case the oldest is a poor scan
                    if s[1].split('_')[1]==quad and s[0] not in seen and len(ALT[quad])<4: ALT[quad].append(s); seen.add(s[0])
    nb=0; found=[]; MISSED=[]
    def have(fn,url):
        tif='cache/topo/'+urllib.parse.quote(fn) if os.path.exists('cache/topo/'+urllib.parse.quote(fn)) else 'cache/topo/'+fn
        if not os.path.exists(tif):
            g=subprocess.run([sys.executable,'tools/lidar_sheet.py','get',url],capture_output=True,text=True)
            tif=(g.stdout.strip().splitlines() or [''])[-1]
        return tif if os.path.exists(tif) else None
    for quad in list(want):
        year,fn,url,bb=want[quad]
        tif=have(fn,url)
        if not tif: print('  sheet download failed',fn); MISSED.append(fn); continue
        # A pale scan (its black ink is grey) gives far fewer buildings than a dark scan, and what it does give is mostly
        # road junctions. The first Massachusetts printings (1886) are like that: Hawley 1886 has ink near 330 and Greylock
        # 1886 near 150 to 200, where a good scan is near 100; the 1890s printings of the same sheets are sharp and add
        # the place names. So when the oldest sheet is paler than 140 and later printings from before 1916 exist, the
        # darkest of up to four is used, if it is clearly darker.
        k=ink(tif)
        if k>140 and not os.path.exists(pre+'_b_'+re.sub(r'[^A-Za-z0-9]+','',fn)[:60]+'.txt'):
            best=None
            for alt in ALT.get(quad,[]):
                t2=have(alt[1],alt[2])
                if t2 and ink(t2)<k-30 and (best is None or ink(t2)<ink(best[1])): best=(alt,t2)
            if best:
                print(f"  the {year} {quad} sheet is a pale scan; using the {best[0][0]} printing instead",flush=True)
                year,fn,url,bb=best[0]; tif=best[1]; want[quad]=best[0]
        bcf=lambda f: pre+'_b_'+re.sub(r'[^A-Za-z0-9]+','',f)[:60]+'.txt'
        bc=bcf(fn)                           # this sheet's buildings, kept so a run that is cut off need not repeat it
        if os.path.exists(bc): bout=open(bc).read()
        else:
            if DEADLINE and time.time()>DEADLINE:
                print(f"{name}: PARTIAL: time is up with {sum(1 for v in want.values() if not os.path.exists(bcf(v[1])))} of {len(want)} old sheets still to read. Run the same command again to carry on."); sys.exit(3)
            print(f"  reading the {year} {quad} sheet for buildings (this step cannot be split; it can take a minute or more)...",flush=True)
            b=subprocess.run([sys.executable,'tools/lidar_buildings.py',uf,pre,tif],capture_output=True,text=True)
            if b.returncode!=0: print('  buildings step failed on',fn,b.stderr[-200:]); sys.exit(5)
            bout=b.stdout; open(bc+'.part','w').write(bout); os.replace(bc+'.part',bc)
        for line in bout.splitlines():
            m=re.match(r'(-?\d+\.\d+) (-?\d+\.\d+) (\[.*\])$',line.strip())
            if not m: continue
            la,lo=float(m.group(1)),float(m.group(2))
            # a "building" outside the sheet's own bounds is lettering in the margin
            if None not in bb and not (bb[0]<=lo<=bb[2] and bb[1]<=la<=bb[3]): continue
            nb+=1
            for dist,pla,plo,dep,size in eval(m.group(3)):
                w,h=[int(x) for x in size.split('x')]
                found.append({'unit':name,'lat':la,'lon':lo,'plat':pla,'plon':plo,'dist':dist,'depth':dep,'size':[w,h],'sheet':fn,'year':year})
    if MISSED and not os.environ.get('LIDAR_ALLOW_GAPS'):       # a sheet that would not download is tried again by the next run
        print(f"{name}: PARTIAL: {len(MISSED)} old sheet(s) could not be downloaded. Run the same command again."); sys.exit(3)
    S['units'][name]={'file':uf,'buildings':nb,'pits':len(found),'sheets':[v[1] for v in want.values() if v[1] not in MISSED]}
    S['cands']+=found
    json.dump(S,open(OUT,'w'))
    print(f"{name}: {nb} map buildings, {len(found)} pits beside one, sheets {[v[1].split('_')[1]+' '+str(v[0]) for v in want.values()]}, {int(time.time()-t0)} s",flush=True)
