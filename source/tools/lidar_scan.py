# Scan a public-land unit's LiDAR ground model for small closed pits the size of a cellar hole (GUIDE.md section 13).
#   python3 tools/lidar_scan.py research/lidar/unit_X.json research/lidar/x      writes x_cands.json and caches tiles
# Method: depth = (grey closing of the ground with a 17 m window) - ground. A closing fills any hollow narrower than the
# window up to its rim, so depth is "how far below its own rim" each cell sits. Keep compact hollows 4-16 m across and
# at least 0.6 m deep on gentle ground, away from stream networks. Everything kept is only a candidate to look at.
import sys,json,math,os,time,numpy as np
from scipy import ndimage as ndi
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lidar_dem import dem,merc,unmerc
unit=json.load(open(sys.argv[1])); pre=sys.argv[2]; rings=unit['rings']
xs=[p[0] for r in rings for p in r]; ys=[p[1] for r in rings for p in r]; W,E,S,N=min(xs),max(xs),min(ys),max(ys)
def inside(lo,la):
    c=False
    for r in rings:
        j=len(r)-1
        for i in range(len(r)):
            if ((r[i][1]>la)!=(r[j][1]>la)) and lo<(r[j][0]-r[i][0])*(la-r[i][1])/(r[j][1]-r[i][1])+r[i][0]: c=not c
            j=i
    return c
T=1000; PAD=40; TD=os.path.join(os.path.dirname(pre) or '.','tiles'); os.makedirs(TD,exist_ok=True)
mlat=(S+N)/2; dlat=T/111320; dlon=T/(111320*math.cos(math.radians(mlat)))
cands=[]; la=S+dlat/2; n=0
while la<N+dlat/2:
    lo=W+dlon/2
    while lo<E+dlon/2:
        # skip tiles with no corner or centre inside the unit
        pts=[(lo,la)]+[(lo+dx*dlon/2,la+dy*dlat/2) for dx in(-1,1) for dy in(-1,1)]+[(lo+dx*dlon/4,la+dy*dlat/4) for dx in(-1,1) for dy in(-1,1)]
        if any(inside(x,y) for x,y in pts):
            f=f'{TD}/{os.path.basename(pre)}_{la:.5f}_{lo:.5f}.npy'
            if os.path.exists(f): a=np.load(f)
            else:
                for k in range(3):
                    try: a,_=dem(la,lo,T/2+PAD,T+2*PAD); break
                    except Exception as e: time.sleep(3); a=None
                if a is None: print('failed tile',la,lo); lo+=dlon; continue
                np.save(f,a)
            n+=1
            if np.nanmax(a)-np.nanmin(a)<0.5 or np.isnan(a).mean()>0.2 or (a<-1000).mean()>0.2: lo+=dlon; continue
            g=ndi.gaussian_filter(a,0.7); depth=ndi.grey_closing(g,size=(17,17))-g
            gy,gx=np.gradient(ndi.gaussian_filter(a,5.0)); slope=np.hypot(gx,gy)
            lab,k=ndi.label(depth>0.45)
            wide=ndi.uniform_filter((depth>0.45).astype('float32'),size=121)*121*121     # hollow cells within 60 m: high along streams
            for i,sl in enumerate(ndi.find_objects(lab),1):
                h=sl[0].stop-sl[0].start; w=sl[1].stop-sl[1].start
                if not(4<=h<=16 and 4<=w<=16): continue
                m=lab[sl]==i; area=int(m.sum())
                if area<14 or area>200 or max(h,w)/min(h,w)>2.2 or area/(h*w)<0.5: continue
                dmax=float(depth[sl][m].max())
                if dmax<0.6 or dmax>3.5: continue
                cy=(sl[0].start+sl[0].stop)/2; cx=(sl[1].start+sl[1].stop)/2
                if not(PAD<=cy<T+PAD and PAD<=cx<T+PAD): continue
                if slope[int(cy),int(cx)]>0.22 or wide[int(cy),int(cx)]-area>450: continue
                # edge sharpness: a dug cellar has steep sides all round; a natural hollow is a bowl
                rim=ndi.binary_dilation(m,iterations=2)&~m; steep=float(np.hypot(*np.gradient(g[sl[0].start-3:sl[0].stop+3,sl[1].start-3:sl[1].stop+3])).max()) if sl[0].start>3 and sl[1].start>3 else 0
                x0,y0=merc(la,lo); kk=1/math.cos(math.radians(la)); px=(cx-(T/2+PAD))*kk; py=((T/2+PAD)-cy)*kk
                clat,clon=unmerc(x0+px,y0+py)
                if not inside(clon,clat): continue
                cands.append({'lat':round(clat,6),'lon':round(clon,6),'depth':round(dmax,2),'w':w,'h':h,'area':area,'fill':round(area/(h*w),2),'steep':round(steep,2),'tile':f,'cy':cy,'cx':cx})
        lo+=dlon
    la+=dlat
json.dump(cands,open(pre+'_cands.json','w'))
print(pre,'tiles',n,'candidates',len(cands))
