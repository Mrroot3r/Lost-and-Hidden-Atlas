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
im,b=crop(TIF,clat,clon,HW,PX); a=np.array(im.convert('RGB')).astype(int)
dark=(a.sum(2)<230)&(a.max(2)-a.min(2)<60)                      # black ink, not brown contours or blue water
core=ndi.binary_opening(dark,structure=np.ones((6,6)))           # removes road lines and most lettering
lab,n=ndi.label(core); out=[]
x0,y0=merc(clat,clon); k=1/math.cos(math.radians(clat))
for i,sl in enumerate(ndi.find_objects(lab),1):
    h=sl[0].stop-sl[0].start; w=sl[1].stop-sl[1].start; area=int((lab[sl]==i).sum())
    if not(6<=h<=20 and 6<=w<=20) or area/(h*w)<0.6: continue
    cy=(sl[0].start+sl[0].stop)/2; cx=(sl[1].start+sl[1].stop)/2
    la,lo=unmerc(x0+(cx-PX/2)*2.5*k, y0+(PX/2-cy)*2.5*k)
    if inside(lo,la): out.append({'lat':round(la,5),'lon':round(lo,5),'w':w,'h':h})
C=json.load(open(pre+'_cands.json'))
def dist(a,b): return math.hypot((a['lat']-b['lat'])*111320,(a['lon']-b['lon'])*111320*math.cos(math.radians(a['lat'])))
for o in out:
    near=sorted([(round(dist(o,c)),c['lat'],c['lon'],c['depth'],f"{c['w']}x{c['h']}") for c in C if dist(o,c)<90])
    o['pits']=near[:3]
json.dump(out,open(pre+'_buildings.json','w'))
print(len(out),'building symbols on the old map inside the unit;',sum(1 for o in out if o['pits']),'have a LiDAR pit within 90 m')
for o in out: print(o['lat'],o['lon'],o['pits'][:2])
