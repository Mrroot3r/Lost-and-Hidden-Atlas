import rasterio, math, io, sys
from rasterio.warp import reproject, Resampling, transform_bounds
from rasterio.transform import from_bounds
import numpy as np
from PIL import Image
R=6378137.0
def merc(lat,lon): return (math.radians(lon)*R, math.log(math.tan(math.pi/4+math.radians(lat)/2))*R)
def unmerc(x,y): return (math.degrees(2*math.atan(math.exp(y/R))-math.pi/2), math.degrees(x/R))
def crop(tif,lat,lon,hw,size=600):
    x,y=merc(lat,lon); k=1/math.cos(math.radians(lat))
    b=(x-hw*k,y-hw*k,x+hw*k,y+hw*k)
    with rasterio.open(tif) as src:
        dst=np.zeros((src.count,size,size),dtype=np.uint8)
        tr=from_bounds(*b,size,size)
        for i in range(src.count):
            reproject(rasterio.band(src,i+1),dst[i],dst_transform=tr,dst_crs='EPSG:3857',resampling=Resampling.bilinear)
        if src.count==1:
            cm=None
            try: cm=src.colormap(1)
            except Exception: pass
            if cm:
                lut=np.array([cm.get(i,(0,0,0,255))[:3] for i in range(256)],dtype=np.uint8); arr=lut[dst[0]]
            else: arr=np.stack([dst[0]]*3,-1)
        else: arr=np.transpose(dst[:3],(1,2,0))
    s,w=unmerc(b[0],b[1]); n,e=unmerc(b[2],b[3])
    return Image.fromarray(arr),(s,w,n,e)
if __name__=='__main__':
    im,bb=crop(sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),int(sys.argv[6]) if len(sys.argv)>6 else 900)
    from PIL import ImageDraw
    d=ImageDraw.Draw(im); c=im.width//2; d.ellipse((c-8,c-8,c+8,c+8),outline=(255,0,255),width=2)
    im.save(sys.argv[5],quality=88); print(bb)
