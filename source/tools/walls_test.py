#!/usr/bin/env python3
"""Offline test of the stone-wall finder (tools/lidar_walls.py) on made-up ground. No network.
   python3 tools/walls_test.py
The ground is a gentle slope with the roughness of real forest floor. On it: two walls 0.15 m high that meet in a corner,
a low wall 0.08 m high, a bank (a 1 m step), a wall on a slight field-edge terrace, a raised roadbed 6 m wide, a boulder field and a winding gully. The
finder must trace the walls and leave the rest alone. Run it after changing any number in lidar_walls.py."""
import sys,os,math,numpy as np
from scipy import ndimage as ndi
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import lidar_walls as W
rng=np.random.default_rng(7); N=420
rr,cc=np.mgrid[0:N,0:N].astype('float32')
a=100+0.04*rr+0.02*cc+ndi.gaussian_filter(rng.normal(0,1,(N,N)),1.2)*0.10+ndi.gaussian_filter(rng.normal(0,1,(N,N)),6)*0.8
def dist_seg(r0,c0,r1,c1):
    vy,vx=r1-r0,c1-c0; t=np.clip(((rr-r0)*vy+(cc-c0)*vx)/(vy*vy+vx*vx),0,1); return np.hypot(rr-(r0+t*vy),cc-(c0+t*vx))
WALLS=[(60,60,60,180,0.15),(60,180,150,180,0.15),(250,40,300,150,0.08),(150,40,150,130,0.15)]       # row0,col0,row1,col1,height
a+=0.08/(1+np.exp(np.clip(-(rr-150)/1.0,-50,50)))*(cc<150)                    # the last wall stands on a slight terrace edge: ground 0.08 m higher south of it
for r0,c0,r1,c1,h in WALLS: a+=h*np.exp(-(dist_seg(r0,c0,r1,c1)/0.9)**2)
a+=1.0/(1+np.exp(np.clip(-(cc-330)/1.2,-50,50)))*(rr<200)                                      # a bank: ground 1 m higher east of column 330, upper half
bed=dist_seg(380,20,330,400); a+=0.3*np.clip(1-np.clip(bed-3,0,None)/1.5,0,1)  # a raised roadbed 6 m wide
for _ in range(60):                                                            # boulders
    r,c=rng.integers(200,240),rng.integers(230,300); a+=0.3*np.exp(-((rr-r)**2+(cc-c)**2)/1.5)
gy=120+25*np.sin(cc/28.0); a-=0.5*np.exp(-((rr-gy-150)/2.5)**2)*(cc>210)*(rr>230) # a winding gully
segs=W.walls(a,margin=6)
def near(seg,line,tol):
    r0,c0,r1,c1=seg; n=int(max(2,math.hypot(r1-r0,c1-c0))); t=np.linspace(0,1,n); pr=r0+(r1-r0)*t; pc=c0+(c1-c0)*t
    L0,K0,L1,K1=line[:4]; vy,vx=L1-L0,K1-K0; u=np.clip(((pr-L0)*vy+(pc-K0)*vx)/(vy*vy+vx*vx),0,1); d=np.hypot(pr-(L0+u*vy),pc-(K0+u*vx)); return (d<=tol).mean()
ok=0
def t(name,cond,extra=''):
    global ok
    print(('ok   ' if cond else 'FAIL ')+name+('  ['+str(extra)+']' if extra!='' else ''))
    if not cond: sys.exit(1)
    ok+=1
def covered(line,tol=2.5):
    """Fraction of a true wall's length that some piece lies along."""
    L0,K0,L1,K1=line[:4]; n=int(math.hypot(L1-L0,K1-K0)); hit=np.zeros(n,bool)
    for s in segs:
        if near(s,line,tol)<0.8: continue
        for e in np.linspace(0,1,int(max(2,math.hypot(s[2]-s[0],s[3]-s[1])))):
            pr=s[0]+(s[2]-s[0])*e; pc=s[1]+(s[3]-s[1])*e; u=((pr-L0)*(L1-L0)+(pc-K0)*(K1-K0))/((L1-L0)**2+(K1-K0)**2)
            if 0<=u<=1: hit[min(n-1,int(u*n))]=True
    return hit.mean()
on_wall=lambda s:any(near(s,w,3)>=0.8 for w in WALLS)
cov=[round(covered(w),2) for w in WALLS]
t('the two 0.15 m walls are traced along most of their length',cov[0]>=0.8 and cov[1]>=0.8,cov)
t('the 0.08 m wall is traced too',cov[2]>=0.6,cov[2])
t('a wall on a slight field-edge terrace is still a wall',cov[3]>=0.6,cov[3])
stray=[s for s in segs if not on_wall(s)]; L=lambda s:math.hypot(s[2]-s[0],s[3]-s[1])
bank=[s for s in stray if near(s,(0,330,200,330),4)>=0.5]
t('a bank (a step in the ground) is not a wall',not bank,len(bank))
road=[s for s in stray if near(s,(380,20,330,400),7)>=0.5]
t('a raised roadbed and its edges are not walls',sum(L(s) for s in road)<25,'%d m'%sum(L(s) for s in road))
inb=lambda s:195<=(s[0]+s[2])/2<=245 and 220<=(s[1]+s[3])/2<=310
boul=[s for s in stray if s not in bank and s not in road and inb(s)]; other=[s for s in stray if s not in bank and s not in road and not inb(s)]
t('rough ground and a winding gully give nothing',not other,'%d pieces, %d m'%(len(other),sum(L(s) for s in other)))
# sixty boulders packed into 40 by 70 m do line up here and there, as a tumbled wall would. That is a known limit, kept small.
t('a dense boulder field gives a few short pieces at most',sum(L(s) for s in boul)<90,'%d pieces, %d m'%(len(boul),sum(L(s) for s in boul)))
c=W.clip([10,10,10,100],40,80); t('a piece is cut at the edge of its tile',c is None) ; c=W.clip([50,10,50,100],40,80); t('and kept where it is inside',c is not None and abs(c[1]-40)<1e-6 and abs(c[3]-80)<1e-6,c)
tw=W.tile_walls(a,N-80,40,lambda r,c:(42.0+(N-r)*1e-5,-74.0+c*1.3e-5)); t('tile pieces come out as whole numbers of 0.00001 degree',len(tw)>0 and all(isinstance(v,int) for w in tw for v in w),len(tw))
print('wall finder test:',ok,'checks passed;',len(segs),'pieces on the made-up ground')
