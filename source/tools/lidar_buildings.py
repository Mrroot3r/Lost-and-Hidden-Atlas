# Find building symbols (small solid black squares) on an old USGS 15-minute sheet inside a public-land unit, then pair
# each with any LiDAR pit within 90 m. This is the step that finds real farmsteads; pits alone are mostly tree throws.
#   python3 tools/lidar_buildings.py research/lidar/unit_X.json research/lidar/x cache/topo/<sheet>_geo.tif
# Get the sheet name from the USGS list: python3 tools/lidar_sheet.py maps <lat> <lon>.  Tuned for 1:62,500 sheets.
import sys,json,math,os,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from scipy import ndimage as ndi
from topocrop import crop
from lidar_dem import merc,unmerc
unit=json.load(open(sys.argv[1])); pre=sys.argv[2]; TIF=sys.argv[3]; rings=unit['rings']
xs=[p[0] for r in rings for p in r]; ys=[p[1] for r in rings for p in r]
def inside(lo,la):
    c=False
    for r in rings:
        j=len(r)-1
        for i in range(len(r)):
            if ((r[i][1]>la)!=(r[j][1]>la)) and lo<(r[j][0]-r[i][0])*(la-r[i][1])/(r[j][1]-r[i][1])+r[i][0]: c=not c
            j=i
    return c
clat=(min(ys)+max(ys))/2; clon=(min(xs)+max(xs))/2; HW=max((max(ys)-min(ys))*111320,(max(xs)-min(xs))*111320*math.cos(math.radians(clat)))/2+300; PX=int(2*HW/2.5)
out=[]
def detect(clat,clon,HW,PX,keep=None):
    """Building symbols in one square of the old map, HW metres either side of clat,clon. keep(lo,la) limits them to a block."""
    im,b=crop(TIF,clat,clon,HW,PX); a=np.asarray(im.convert('RGB')).astype(np.int16)
    # Black ink, not brown contours or blue water. Most scans print black as black (red+green+blue under 230). Some old scans
    # are pale: their "black" is a dark grey-brown near 260-300, and the fixed rule finds nothing at all on them (the 1886
    # Hawley, Massachusetts sheet: 0 buildings where a darker scan of the same plate gives 300). So the level is taken
    # from the sheet itself when its ink is paler than the rule: a quarter of the way from its darkest ink to its paper.
    ssum=a.sum(2); K=float(np.percentile(ssum,0.2)); P=float(np.median(ssum)); T=max(230.0,K+0.25*(P-K))
    dark=(ssum<T)&(a.max(2)-a.min(2)<(60 if T<=230 else 90))
    core=ndi.binary_opening(dark,structure=np.ones((6,6)))           # removes road lines and most lettering
    lab,n=ndi.label(core)
    x0,y0=merc(clat,clon); k=1/math.cos(math.radians(clat))
    for i,sl in enumerate(ndi.find_objects(lab),1):
        h=sl[0].stop-sl[0].start; w=sl[1].stop-sl[1].start; area=int((lab[sl]==i).sum())
        if not(6<=h<=20 and 6<=w<=20) or area/(h*w)<0.6: continue
        cy=(sl[0].start+sl[0].stop)/2; cx=(sl[1].start+sl[1].stop)/2
        la,lo=unmerc(x0+(cx-PX/2)*2.5*k, y0+(PX/2-cy)*2.5*k)
        if (keep is None or keep(lo,la)) and inside(lo,la): out.append({'lat':round(la,5),'lon':round(lo,5),'w':w,'h':h})
if PX<=6000: detect(clat,clon,HW,PX)
else:
    # A big unit (a wild forest of scattered pieces can be 50 km across) cannot be read in one piece: at 2.5 m a cell
    # that is more than ten gigabytes, and the first version of this tool was killed for it without a word, so the
    # sweep reported "0 buildings". Read it in 6 km blocks instead, only where the sheet and the unit's pieces overlap.
    import rasterio
    from rasterio.warp import transform_bounds
    with rasterio.open(TIF) as ds: W,S,E,N=transform_bounds(ds.crs,'EPSG:4326',*ds.bounds)
    rb=[(min(p[0] for p in r),min(p[1] for p in r),max(p[0] for p in r),max(p[1] for p in r)) for r in rings]
    B=6000.0; dla=B/111320; dlo=B/(111320*math.cos(math.radians(clat)))
    la0=max(min(ys),S); lo0=max(min(xs),W); nblocks=0
    la=la0
    while la<min(max(ys),N):
        lo=lo0
        while lo<min(max(xs),E):
            box=(lo,la,lo+dlo,la+dla)
            if any(not(r[2]<box[0] or r[0]>box[2] or r[3]<box[1] or r[1]>box[3]) for r in rb):
                try: detect(la+dla/2,lo+dlo/2,B/2+150,int((B+300)/2.5),lambda x,y,box=box: box[0]<=x<box[2] and box[1]<=y<box[3]); nblocks+=1
                except Exception as e: print('  block failed',round(la,3),round(lo,3),str(e)[:80],file=sys.stderr)
            lo+=dlo
        la+=dla
    print('  read in',nblocks,'blocks',file=sys.stderr)
C=json.load(open(pre+'_cands.json'))
def dist(a,b): return math.hypot((a['lat']-b['lat'])*111320,(a['lon']-b['lon'])*111320*math.cos(math.radians(a['lat'])))
for o in out:
    near=sorted([(round(dist(o,c)),c['lat'],c['lon'],c['depth'],f"{c['w']}x{c['h']}") for c in C if dist(o,c)<90])
    o['pits']=near[:3]
json.dump(out,open(pre+'_buildings.json','w'))
print(len(out),'building symbols on the old map inside the unit;',sum(1 for o in out if o['pits']),'have a LiDAR pit within 90 m')
for o in out: print(o['lat'],o['lon'],o['pits'][:2])
