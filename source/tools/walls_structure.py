"""Keep the wall pieces that are part of a built pattern, and drop the scatter the finder draws on a rough ground model.

Why: the wall finder (tools/lidar_walls.py) looks at ground one tile at a time. Where the ground model is rough or soft
(conifer plantations, the Adirondack fringe, parts of north-west Massachusetts) it draws short pieces at random angles:
Shaker Mountain Wild Forest came out with 100 km of "wall", nearly all of it noise. Real walls differ in one way that
needs no ground model to see: they are long and they join. So a piece is kept only if
  - it lies in a straight run of pieces at least RUN metres long (ends within GAP of each other, in line), or
  - it meets such a run at about a right angle (a field corner or a T), or
  - both its ends meet other pieces at about a right angle (a yard or small enclosure).
Then every box of about 500 m in which less than ROUGH of the drawn length passed is dropped whole: that is rough ground,
and the few "runs" left in it are chance.
The unit files in lidar/walls/ keep every piece the finder drew; only the map layer (tools/walls.py) is filtered, so the
rule can be changed without scanning again.   python3 tools/walls_structure.py     prints what each unit keeps"""
import math,json,glob,os,sys
RUN=45.0; GAP=14.0; LINE=3.5; TURN=12.0; JOIN=7.0; SQUARE=(60.0,120.0); MINP=10.0; ROUGH=0.35; ROUGHMIN=150.0; BOX=500
def _m(w,la0):
    k=1.1132*math.cos(math.radians(la0)); return (w[1]*k,w[0]*1.1132,w[3]*k,w[2]*1.1132)      # x0,y0,x1,y1 in metres
def _ang(p): return math.degrees(math.atan2(p[3]-p[1],p[2]-p[0]))%180.0
def _dang(a,b): d=abs(a-b)%180.0; return min(d,180.0-d)
def _pl(px,py,s):
    """distance from a point to the segment s, and to its endless line"""
    x0,y0,x1,y1=s; dx,dy=x1-x0,y1-y0; L2=dx*dx+dy*dy or 1e-9; t=((px-x0)*dx+(py-y0)*dy)/L2
    line=abs((px-x0)*dy-(py-y0)*dx)/math.sqrt(L2); tc=max(0.0,min(1.0,t)); return math.hypot(px-(x0+tc*dx),py-(y0+tc*dy)),line
def structured(W):
    """W: [[lat0,lon0,lat1,lon1] in 0.00001 degree]. Returns the list of booleans: keep this piece?"""
    n=len(W)
    if not n: return []
    la0=sum(w[0] for w in W)/n/1e5; P=[_m(w,la0) for w in W]; A=[_ang(p) for p in P]; Ln=[math.hypot(p[2]-p[0],p[3]-p[1]) for p in P]
    C=40.0; grid={}
    for i,p in enumerate(P):
        for gx in range(int(math.floor(min(p[0],p[2])/C))-1,int(math.floor(max(p[0],p[2])/C))+2):
            for gy in range(int(math.floor(min(p[1],p[3])/C))-1,int(math.floor(max(p[1],p[3])/C))+2): grid.setdefault((gx,gy),[]).append(i)
    def near(i):
        p=P[i]; s=set()
        for gx in range(int(math.floor(min(p[0],p[2])/C)),int(math.floor(max(p[0],p[2])/C))+1):
            for gy in range(int(math.floor(min(p[1],p[3])/C)),int(math.floor(max(p[1],p[3])/C))+1): s.update(grid.get((gx,gy),()))
        s.discard(i); return s
    par=list(range(n))
    def find(i):
        while par[i]!=i: par[i]=par[par[i]]; i=par[i]
        return i
    corner=[set() for _ in range(n)]            # which end (0 or 1) of piece i meets another piece squarely, and which piece
    for i in range(n):
        for j in near(i):
            if j<i: continue
            d=_dang(A[i],A[j])
            if d<=TURN:                         # in line: an end of one near an end of the other, and on its line
                ok=False
                for (ex,ey) in ((P[i][0],P[i][1]),(P[i][2],P[i][3])):
                    seg,line=_pl(ex,ey,P[j])
                    if seg<=GAP and line<=LINE: ok=True
                for (ex,ey) in ((P[j][0],P[j][1]),(P[j][2],P[j][3])):
                    seg,line=_pl(ex,ey,P[i])
                    if seg<=GAP and line<=LINE: ok=True
                if ok: par[find(i)]=find(j)
            elif SQUARE[0]<=d<=SQUARE[1] and Ln[i]>=MINP and Ln[j]>=MINP:
                for e,(ex,ey) in enumerate(((P[i][0],P[i][1]),(P[i][2],P[i][3]))):
                    if _pl(ex,ey,P[j])[0]<=JOIN: corner[i].add((e,j))
                for e,(ex,ey) in enumerate(((P[j][0],P[j][1]),(P[j][2],P[j][3]))):
                    if _pl(ex,ey,P[i])[0]<=JOIN: corner[j].add((e,i))
    run={}
    for i in range(n): run[find(i)]=run.get(find(i),0.0)+Ln[i]
    strong=[run[find(i)]>=RUN for i in range(n)]; keep=list(strong)
    for i in range(n):
        if keep[i]: continue
        if any(strong[j] for e,j in corner[i]): keep[i]=True                         # its end meets a long run squarely
        elif {e for e,j in corner[i]}=={0,1}: keep[i]=True                           # squared off at both ends: a yard
    for j in range(n):                                                               # the crossbar of a T: a long run ends squarely on it
        if strong[j]:
            for e,i in corner[j]: keep[i]=True
    for i in range(n):                                                               # the pieces that square off a kept yard side stay with it
        if not strong[i] and keep[i] and {e for e,j in corner[i]}=={0,1}:
            for e,j in corner[i]: keep[j]=True
    # Rough ground: a box of about 500 m where most of what the finder drew is scatter. Whatever "runs" are left there are
    # mostly chance, so the whole box is left out. (A box with little drawn in it is not judged.)
    box={}
    for i,w in enumerate(W):
        b=((w[0]+w[2])//2//BOX,(w[1]+w[3])//2//BOX); t=box.setdefault(b,[0.0,0.0]); t[0]+=Ln[i]; t[1]+=Ln[i] if keep[i] else 0.0
    for i,w in enumerate(W):
        t=box[((w[0]+w[2])//2//BOX,(w[1]+w[3])//2//BOX)]
        if t[0]>=ROUGHMIN and t[1]<ROUGH*t[0]: keep[i]=False
    return keep
if __name__=='__main__':
    rows=[]
    for f in sorted(glob.glob('lidar/walls/*.json')):
        d=json.load(open(f)); k=structured(d['w']); L=[math.hypot((w[2]-w[0])*1.1132,(w[3]-w[1])*1.1132*math.cos(math.radians(w[0]/1e5))) for w in d['w']]
        tot=sum(L) or 1; kept=sum(l for l,b in zip(L,k) if b); rows.append((kept/tot,kept/1000,tot/1000,d['name']))
    print('share kept | km kept | km drawn | unit')
    for r in sorted(rows): print('%.2f  %6.1f  %6.1f  %s'%r)
