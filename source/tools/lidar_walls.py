#!/usr/bin/env python3
"""Find stone walls on the LiDAR ground model (LIDAR.md, "Stone walls"). New York only, like the other LiDAR tools.

   from lidar_walls import walls              walls(a) -> [[r0,c0,r1,c1], ...] straight pieces, in cells of the 1 m grid `a`
   python3 tools/lidar_walls.py test          draws what it finds on the test chips in research/walls/

A field wall on a 1 m ground model is a low ridge one to three cells wide and only 0.05 to 0.2 m high after the ground
classifier has shaved it, on ground whose own roughness is as large. No single cell says "wall". What gives a wall away
is that it goes on, STRAIGHT, for tens of metres. So the method is a line filter:
  1. local relief: the lightly smoothed ground minus a 4 m smoothing of itself. Only narrow features are left.
  2. for each of 16 directions, the mean local relief along a 25 m line through every cell, minus the HIGHER of the means
     along the two parallel lines 3 m to either side. A wall scores its own height; rough ground averages to nothing; a
     raised roadbed is no higher in the middle than at its sides and scores nothing. Scoring against the average of
     the two sides was tried and let rough ground through everywhere. (The first attempt, in November 2026, tested
     single cells against a median and marked road banks and chip edges instead.)
  3. at least 60% of the cells along that line must themselves stand above their surroundings: one boulder or a mound
     cannot carry a line.
  4. the best direction's score is thinned to its crest, and a probabilistic Hough transform keeps straight runs of at
     least MINLEN metres with gaps of at most GAP.
  5. each piece is then measured again along its own length: its height, the ground on both sides (the spine between
     two gullies is not a wall), and the step across it (a road cut or a bank of a metre is not a wall). A wall standing on a
     field-edge terrace as high as itself is usually missed: its upper side is as high as its top. A piece under 38 m with no other piece near either end is dropped.
  6. nothing is reported on steep ground or where the ground model is flat facets (no ground points under conifers).
Everything returned is a CANDIDATE. Expect misses where a wall is low, tumbled or shorter than 20 m, and false lines
along straight ditch spoil, the berms of old roads and plough ridges. Give the caller's margin and it is dropped."""
import sys,os,math,numpy as np
from scipy import ndimage as ndi
SCORE=0.035; NOISE=0.9; FRAC=0.6; LEN=25; SIDE=3; MINLEN=18; GAP=5; NDIR=16; SIDELOW=0.09; STEP=0.45; WIDE=0.55; BOTH=0.03; ALONE=38; NEAR=10
def facets(a):
    """True where the ground model is interpolated flat triangles: the second derivative is almost exactly zero over an area."""
    g2=np.abs(ndi.laplace(a)); flat=(g2<0.004).astype('float32')
    return ndi.uniform_filter(flat,15)>0.72
_KF={}
def _kernels(shape):
    """Fourier transforms of the line kernels (centre line and the two side lines) for every direction, for one array shape."""
    if shape in _KF: return _KF[shape]
    H,W=shape; out=[]; half=LEN/2
    for i in range(NDIR):
        th=math.pi*i/NDIR; dx,dy=math.cos(th),math.sin(th); px,py=-dy,dx; ks=[]
        for off in (0,SIDE,-SIDE):
            k=np.zeros(shape,'float32'); n=0
            for t in np.arange(-half,half+0.01,0.5):
                x=t*dx+off*px; y=t*dy+off*py; k[int(round(y))%H,int(round(x))%W]+=1; n+=1
            ks.append(np.fft.rfft2(k/n))
        out.append((th,ks))
    _KF[shape]=out; return out
def relief(a):
    g=ndi.gaussian_filter(a.astype('float32'),0.8); lrm=g-ndi.gaussian_filter(a.astype('float32'),4.0)
    return np.clip(lrm,-0.3,0.4)              # one boulder or a pit rim must not carry a line
def score(lrm):
    """(best score, its direction index, fraction of the line standing proud) for every cell."""
    F=np.fft.rfft2(lrm); P=np.fft.rfft2((lrm>0.015).astype('float32')); sh=lrm.shape
    best=np.full(sh,-1,'float32'); bi=np.zeros(sh,'int8'); bf=np.zeros(sh,'float32')
    for i,(th,ks) in enumerate(_kernels(sh)):
        L=np.fft.irfft2(F*np.conj(ks[0]),s=sh); S=np.maximum(np.fft.irfft2(F*np.conj(ks[1]),s=sh),np.fft.irfft2(F*np.conj(ks[2]),s=sh))
        R=L-np.maximum(S,0); up=R>best
        if up.any(): fr=np.fft.irfft2(P*np.conj(ks[0]),s=sh); best[up]=R[up]; bi[up]=i; bf[up]=fr[up]
    return best,bi,bf
def crest(best,bi):
    """Keep a cell only if no cell within 2 m across its line scores higher."""
    keep=np.zeros(best.shape,bool); H,W=best.shape; rr,cc=np.mgrid[0:H,0:W]
    for i in range(NDIR):
        m=bi==i
        if not m.any(): continue
        th=math.pi*i/NDIR; px,py=-math.sin(th),math.cos(th); ok=m.copy()
        for d in (1,2,-1,-2):
            r2=np.clip(np.rint(rr+py*d).astype(int),0,H-1); c2=np.clip(np.rint(cc+px*d).astype(int),0,W-1); ok&=best>=best[r2,c2]
        keep|=ok
    return keep
def measure(lrm,seg,g=None):
    """Look at one straight piece again: (mean height along it above the higher side, fraction of it standing proud, the
    lower side's relief, and how much of a STEP the ground makes across it). The step is the height difference between
    the two sides 3 m out, less what the lie of the land 9 m out on each side accounts for. A wall on a slope has none;
    a road cut or a terrace edge has its whole height."""
    r0,c0,r1,c1=seg; n=int(max(2,math.hypot(r1-r0,c1-c0))); t=np.linspace(0,1,n); rr=r0+(r1-r0)*t; cc=c0+(c1-c0)*t
    L=math.hypot(r1-r0,c1-c0) or 1; pr=(c1-c0)/L; pc=-(r1-r0)/L                # unit vector across the piece (row, col)
    mid=ndi.map_coordinates(lrm,[rr,cc],order=1,mode='nearest')
    s1=ndi.map_coordinates(lrm,[rr+pr*SIDE,cc+pc*SIDE],order=1,mode='nearest').mean(); s2=ndi.map_coordinates(lrm,[rr-pr*SIDE,cc-pc*SIDE],order=1,mode='nearest').mean()
    step=0.0; proud=1.0
    if g is not None:
        z=lambda k: ndi.map_coordinates(g,[rr+pr*k,cc+pc*k],order=1,mode='nearest').mean()
        step=max(abs((z(SIDE)-z(-SIDE))-(z(3*SIDE)-z(-3*SIDE))/3.0),abs((z(2*SIDE)-z(-2*SIDE))-(z(6*SIDE)-z(-6*SIDE))/3.0))    # near and wider: the piece may sit on the shoulder, a few metres off the step itself
    if g is not None:
        # In real heights, with the lie of the land taken out: the crest must stand above the ground 3 m away on BOTH sides.
        # The shoulder of a roadbed or a bank stands above the outside only.
        tr=(z(3*SIDE)-z(-3*SIDE))/(6.0*SIDE); zc=z(0); proud=min(zc-(z(SIDE)-SIDE*tr),zc-(z(-SIDE)+SIDE*tr))
    n1=ndi.map_coordinates(lrm,[rr+pr*2,cc+pc*2],order=1,mode='nearest').mean(); n2=ndi.map_coordinates(lrm,[rr-pr*2,cc-pc*2],order=1,mode='nearest').mean()
    wide=0.5*(n1+n2)/max(float(mid.mean()),1e-3)             # a wall has fallen away 2 m to either side; a roadbed has not
    return float(mid.mean()-max(s1,s2,0)), float((mid>0.015).mean()), float(min(s1,s2)), float(step), float(wide), float(proud)
def walls(a,margin=0):
    """Straight wall pieces in grid cells: [[r0,c0,r1,c1],...]. Pieces whose middle lies in the margin are dropped."""
    from skimage.transform import probabilistic_hough_line
    lrm=relief(a); best,bi,bf=score(lrm); g1=ndi.gaussian_filter(a.astype('float32'),0.8)
    gy,gx=np.gradient(ndi.gaussian_filter(a.astype('float32'),3.0)); slope=np.hypot(gx,gy)
    rough=np.sqrt(ndi.uniform_filter(lrm*lrm,41))                    # how bumpy the ground is round about: a line must stand clear of that
    need=np.maximum(SCORE,NOISE*rough)
    flat=ndi.binary_dilation(facets(a),iterations=6)                 # facets, still water and a few metres round them (a shoreline is a step, not a wall)
    m=(best>need)&(bf>FRAC)&(slope<0.45)&(~flat)&crest(best,bi)
    out=[]; H,W=a.shape
    for d in range(NDIR):
        md=m&((bi==d)|(bi==(d+1)%NDIR)|(bi==(d-1)%NDIR))
        if md.sum()<MINLEN*0.6: continue
        md=ndi.binary_dilation(md,structure=np.ones((2,2)))          # the crest is one cell wide and steps sideways; the Hough needs it joined
        th=math.pi*d/NDIR-math.pi/2; thetas=th+np.linspace(-math.pi/NDIR,math.pi/NDIR,5)
        thetas=(thetas+math.pi/2)%math.pi-math.pi/2
        for (x0,y0),(x1,y1) in probabilistic_hough_line(md,threshold=10,line_length=MINLEN,line_gap=GAP,theta=np.sort(thetas),rng=1):
            my=(y0+y1)/2; mx=(x0+x1)/2
            if margin and not(margin<=my<H-margin and margin<=mx<W-margin): continue
            seg=[int(y0),int(x0),int(y1),int(x1)]; h,f,low,step,wide,proud=measure(lrm,seg,g1)
            # the ground on both sides must be ordinary ground: the spine between two gullies stands above two trenches, not above
            # a field; and it must not be a step: the shoulder of a bank looks like a ridge to the line filter
            if h>=max(SCORE,NOISE*float(rough[int(my),int(mx)])) and f>=FRAC and low>-SIDELOW and step<STEP: out.append(seg)
    return lonely(merge(out))
def lonely(segs):
    """Walls come in networks: a yard, a lane, a field corner. A short piece with no other piece near either end is
    far more often rough ground than a wall, so it is dropped. A long piece stands on its own."""
    L=lambda s:math.hypot(s[2]-s[0],s[3]-s[1]); keep=[]
    def dseg(p,k):
        vy,vx=k[2]-k[0],k[3]-k[1]; l2=vy*vy+vx*vx; t=max(0,min(1,((p[0]-k[0])*vy+(p[1]-k[1])*vx)/l2)) if l2 else 0
        return math.hypot(p[0]-(k[0]+t*vy),p[1]-(k[1]+t*vx))
    for i,s in enumerate(segs):
        if L(s)>=ALONE: keep.append(s); continue
        ends=((s[0],s[1]),(s[2],s[3]))
        if any(j!=i and min(dseg(e,k) for e in ends)<=NEAR for j,k in enumerate(segs)): keep.append(s)
    return keep
def merge(segs):
    """Pieces come from 16 direction bins and overlap. Longest first: a piece lying along one already kept is dropped,
    or cut back to the part that runs on beyond its end."""
    segs=sorted(([float(v) for v in s] for s in segs),key=lambda s:-math.hypot(s[2]-s[0],s[3]-s[1])); keep=[]
    for s in segs:
        alive=True
        for k in keep:
            vy,vx=k[2]-k[0],k[3]-k[1]; L2=vy*vy+vx*vx
            if not L2: continue
            Lk=math.sqrt(L2); ang=abs(math.atan2(s[2]-s[0],s[3]-s[1])-math.atan2(vy,vx))%math.pi; ang=min(ang,math.pi-ang)
            if ang>math.radians(12): continue
            t0=((s[0]-k[0])*vy+(s[1]-k[1])*vx)/L2; t1=((s[2]-k[0])*vy+(s[3]-k[1])*vx)/L2          # where the piece's ends fall along the kept one (0..1)
            d0=abs((s[0]-k[0])*vx-(s[1]-k[1])*vy)/Lk; d1=abs((s[2]-k[0])*vx-(s[3]-k[1])*vy)/Lk     # and how far to its side
            if max(d0,d1)>3.5 or max(t0,t1)<0 or min(t0,t1)>1: continue                              # not alongside, or wholly beyond an end
            lo,hi=min(t0,t1),max(t0,t1); p=lambda t:(s[0]+(s[2]-s[0])*(t-t0)/(t1-t0),s[1]+(s[3]-s[1])*(t-t0)/(t1-t0))
            before=(0-lo)*Lk if lo<0 else 0; after=(hi-1)*Lk if hi>1 else 0
            if max(before,after)<6: alive=False; break                                               # nothing worth keeping runs on past the kept piece
            if after>=before: a0=p(1.0); a1=p(hi)
            else: a0=p(lo); a1=p(0.0)
            s=[a0[0],a0[1],a1[0],a1[1]]
        if alive and math.hypot(s[2]-s[0],s[3]-s[1])>=6: keep.append(s)
    return [[int(round(v)) for v in k] for k in keep]
def clip(seg,lo,hi):
    """The part of a piece inside the square lo <= row, col < hi (Liang-Barsky), or None."""
    r0,c0,r1,c1=[float(v) for v in seg]; t0,t1=0.0,1.0; dr,dc=r1-r0,c1-c0
    for p,q in ((-dr,r0-lo),(dr,hi-r0),(-dc,c0-lo),(dc,hi-c0)):
        if p==0:
            if q<0: return None
        else:
            t=q/p
            if p<0: t0=max(t0,t)
            else: t1=min(t1,t)
    if t0>=t1: return None
    return [r0+t0*dr,c0+t0*dc,r0+t1*dr,c0+t1*dc]
def tile_walls(a,T,PAD,to_latlon):
    """Wall pieces of one scan tile as [lat0,lon0,lat1,lon1] in units of 0.00001 degree (about a metre). `a` is the tile with
    its margin of PAD cells; only what lies in the T x T middle is returned, cut at its edge, so neighbouring tiles
    never report the same stretch twice. to_latlon(row,col) -> (lat,lon)."""
    out=[]
    for seg in walls(a):
        c=clip(seg,PAD,T+PAD)
        if not c or math.hypot(c[2]-c[0],c[3]-c[1])<4: continue
        la0,lo0=to_latlon(c[0],c[1]); la1,lo1=to_latlon(c[2],c[3])
        out.append([round(la0*1e5),round(lo0*1e5),round(la1*1e5),round(lo1*1e5)])
    return out
if __name__=='__main__':
    sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
    from lidar_dem import shade
    from PIL import Image,ImageDraw
    import glob
    only=sys.argv[2:]; fs=[f for f in sorted(glob.glob('research/walls/*.npy')) if not only or os.path.basename(f)[:-4] in only]; cols=min(4,len(fs)); rows=(len(fs)+cols-1)//cols; S=400; Z=2 if len(fs)<=4 else 1
    o=Image.new('RGB',(cols*S*Z,rows*S*Z))
    for i,f in enumerate(fs):
        a=np.load(f); hs=shade(a,1.0,315,40,3.0).astype('float32')*0.6+shade(a,1.0,45,40,3.0).astype('float32')*0.4
        im=Image.fromarray(hs.astype('uint8')).convert('RGB').resize((S*Z,S*Z),Image.LANCZOS); d=ImageDraw.Draw(im); w=walls(a,margin=8); tot=0
        for r0,c0,r1,c1 in w: d.line((c0*Z,r0*Z,c1*Z,r1*Z),fill=(255,60,0),width=1); tot+=math.hypot(r1-r0,c1-c0)
        d.text((5,3),'%s  %d pieces, %d m'%(os.path.basename(f)[:-4],len(w),tot),fill=(255,255,0)); o.paste(im,((i%cols)*S*Z,(i//cols)*S*Z))
    o.save('research/walls/test.jpg',quality=88); print('wrote research/walls/test.jpg')
