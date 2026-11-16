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
    """Historic 1:62,500 sheets over a point, oldest first: [(year, name, url, (w,s,e,n))]."""
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
        if not m or m.group(3)!='62500': continue
        b=it.get('boundingBox') or {}
        out.append((int(m.group(2)),m.group(1),url,(b.get('minX'),b.get('minY'),b.get('maxX'),b.get('maxY'))))
    return sorted(out)
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
for uf in sys.argv[1:]:
    unit=json.load(open(uf)); name=unit.get('name') or os.path.basename(uf)
    if name in S['units']: print('skip (done):',name); continue
    P=list(pts(unit['rings'])); xs=[p[0] for p in P]; ys=[p[1] for p in P]
    pre='research/lidar/sw_'+re.sub(r'[^a-z0-9]+','',name.lower())[:18]
    t0=time.time()
    r=subprocess.run([sys.executable,'tools/lidar_scan.py',uf,pre],capture_output=True,text=True)
    if not os.path.exists(pre+'_cands.json'): print('SCAN FAILED',name,(r.stdout+r.stderr)[-200:]); continue
    # the oldest sheet at each corner and the middle, so a unit across a sheet edge is covered
    want={}
    for lo,la in ((min(xs),min(ys)),(min(xs),max(ys)),(max(xs),min(ys)),(max(xs),max(ys)),(sum(xs)/len(xs),sum(ys)/len(ys))):
        ss=[s for s in sheets(lo,la) if s[0]<=1915]
        if ss:
            quad=ss[0][1].split('_')[1]
            want.setdefault(quad,ss[0])
    nb=0; found=[]
    for quad,(year,fn,url,bb) in want.items():
        tif='cache/topo/'+urllib.parse.quote(fn) if os.path.exists('cache/topo/'+urllib.parse.quote(fn)) else 'cache/topo/'+fn
        if not os.path.exists(tif):
            g=subprocess.run([sys.executable,'tools/lidar_sheet.py','get',url],capture_output=True,text=True)
            tif=(g.stdout.strip().splitlines() or [''])[-1]
            if not os.path.exists(tif): print('  sheet download failed',fn); continue
        b=subprocess.run([sys.executable,'tools/lidar_buildings.py',uf,pre,tif],capture_output=True,text=True)
        for line in b.stdout.splitlines():
            m=re.match(r'(-?\d+\.\d+) (-?\d+\.\d+) (\[.*\])$',line.strip())
            if not m: continue
            la,lo=float(m.group(1)),float(m.group(2))
            # a "building" outside the sheet's own bounds is lettering in the margin
            if None not in bb and not (bb[0]<=lo<=bb[2] and bb[1]<=la<=bb[3]): continue
            nb+=1
            for dist,pla,plo,dep,size in eval(m.group(3)):
                w,h=[int(x) for x in size.split('x')]
                found.append({'unit':name,'lat':la,'lon':lo,'plat':pla,'plon':plo,'dist':dist,'depth':dep,'size':[w,h],'sheet':fn,'year':year})
    S['units'][name]={'file':uf,'buildings':nb,'pits':len(found),'sheets':[v[1] for v in want.values()]}
    S['cands']+=found
    json.dump(S,open(OUT,'w'))
    print(f"{name}: {nb} map buildings, {len(found)} pits beside one, sheets {[v[1].split('_')[1]+' '+str(v[0]) for v in want.values()]}, {int(time.time()-t0)} s",flush=True)
