"""Raw LiDAR ground elevation as a float grid, and a shaded-relief renderer. Used by lidar_scan.py and lidar_sheet.py
(LIDAR.md; GUIDE.md section 13).   python3 tools/lidar_dem.py <lat> <lon>   writes research/lidar/test.png

Where the ground model comes from:
  ny     New York State's own "Latest_DEM" image service (1 m). Used for every point inside New York.
  3dep   the USGS 3DEP elevation service, the whole country. It gives 1 m LiDAR where a 1 m survey exists (all of
         Massachusetts) and silently falls back to a 10 m model where none does: coarse() tells the two apart.
  ma     MassGIS's own copy of the Massachusetts LiDAR. Several times faster than 3dep but rougher (survey striping
         shows through), which makes the wall finder draw more false walls. Only for when 3dep will not answer.
The source is LIDAR_SRC when that is set (tools/lidar.py sets it from the unit's state so a whole unit comes from one
source). Otherwise it goes by the point: inside New York's outline 'ny', anywhere else '3dep'. A New York answer that
is empty (the outline is coarse near the border) is asked for again from 3dep."""
import io,os,json,math,requests,numpy as np
from PIL import Image
SRC={'ny':('https://elevation.its.ny.gov/arcgis/rest/services/Latest_DEM/ImageServer/exportImage',{}),
     '3dep':('https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer/exportImage',{}),
     'ma':('https://arcgisserver.digital.mass.gov/arcgisserver/rest/services/LiDAR/DEM_lidar_2013to2021_32bitFloat/ImageServer/exportImage',{'bandIds':'0'})}
URL=SRC['ny'][0]
def merc(la,lo): return lo*20037508.34/180, math.log(math.tan((90+la)*math.pi/360))*20037508.34/math.pi
def unmerc(x,y): return math.degrees(2*math.atan(math.exp(y*math.pi/20037508.34))-math.pi/2), x*180/20037508.34
_OUT=None
def state_of(la,lo):
    """The state or province a point is in, as the Atlas's two-letter key ('ny', 'ma'), from the coarse outlines in
    build/states.json. None when the file is missing or the point is in none of them. Good to a kilometre or two at a border."""
    global _OUT
    if _OUT is None:
        _OUT={}
        for p in (os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','build','states.json'),'build/states.json'):
            if os.path.exists(p): _OUT=json.load(open(p)); break
    for k,rings in _OUT.items():
        c=False
        for r in rings:
            n=len(r)//2; j=n-1
            for i in range(n):
                xi,yi,xj,yj=r[2*i],r[2*i+1],r[2*j],r[2*j+1]
                if ((yi>la)!=(yj>la)) and lo<(xj-xi)*(la-yi)/(yj-yi)+xi: c=not c
                j=i
        if c: return k
    return None
def source(la,lo):
    s=os.environ.get('LIDAR_SRC','')
    if s in SRC: return s
    return 'ny' if state_of(la,lo)=='ny' else '3dep'
def empty(a): return a is None or not np.isfinite(a).any() or float(np.mean(~np.isfinite(a)|(a<-1000)))>0.9
def _get(src,x,y,h,px):
    url,extra=SRC[src]
    p={'bbox':f'{x-h},{y-h},{x+h},{y+h}','bboxSR':3857,'imageSR':3857,'size':f'{px},{px}','format':'tiff','pixelType':'F32','interpolation':'RSP_BilinearInterpolation','f':'image'}; p.update(extra)
    r=requests.get(url,params=p,timeout=120); r.raise_for_status()
    return np.array(Image.open(io.BytesIO(r.content)),dtype='float32')
def dem(la,lo,half_m,px):
    """square of 2*half_m ground metres centred on la,lo, px*px cells. Returns (grid, scale) where scale = ground metres per cell."""
    x,y=merc(la,lo); h=half_m/math.cos(math.radians(la)); src=source(la,lo)
    import time
    for k in range(5):
        try:
            a=_get(src,x,y,h,px)
            if src=='ny' and not os.environ.get('LIDAR_SRC') and empty(a): src='3dep'; a=_get(src,x,y,h,px)     # just over the state line
            break
        except Exception as e:
            if k==4: raise
            time.sleep(3+3*k)
    return a, 2*half_m/px
def coarse(a,scale=1.0):
    """True when a grid asked for at about 1 m a cell was really made from a much coarser model (3dep where no 1 m LiDAR
    exists): such ground is perfectly smooth at the scale of a cellar or a wall, so nothing can be found on it. Still
    water and dead-flat ground are not called coarse: they are smooth in a real survey too."""
    from scipy import ndimage as ndi
    a=np.where(np.isfinite(a),a,np.nan)
    if np.isnan(a).mean()>0.5 or scale>2.5: return False
    a=np.nan_to_num(a,nan=float(np.nanmean(a)))
    gy,gx=np.gradient(ndi.gaussian_filter(a,5.0/scale),scale); land=np.hypot(gx,gy)>0.02              # sloping ground only
    if land.mean()<0.1: return False
    d=np.abs(a-ndi.gaussian_filter(a,1.0/scale))
    # the middle value, not the average: a blown-up coarse grid has a few sharp creases where its own cells join.
    # Measured: real 1 m LiDAR 0.011 to 0.024 m; a 10 m model blown up 0.001 to 0.004; a 5 m one 0.003 to 0.007.
    return float(np.median(d[land]))<0.005
def shade(a,scale,az=315,alt=35,z=2.0):
    gy,gx=np.gradient(a*z,scale); slope=np.pi/2-np.arctan(np.hypot(gx,gy)); asp=np.arctan2(-gx,gy)
    azr=math.radians(360-az+90); altr=math.radians(alt)
    s=np.sin(altr)*np.sin(slope)+np.cos(altr)*np.cos(slope)*np.cos(azr-asp)
    return np.clip(s*255,0,255).astype('uint8')
if __name__=='__main__':
    import sys
    la,lo=float(sys.argv[1]),float(sys.argv[2]); a,sc=dem(la,lo,250,500)
    print('source:',source(la,lo),'| state:',state_of(la,lo),'|',a.shape,sc,float(np.nanmin(a)),float(np.nanmax(a)),a.dtype,'| coarse' if coarse(a,sc) else '| fine (1 m LiDAR)')
    os.makedirs('research/lidar',exist_ok=True); Image.fromarray(shade(a,sc)).save('research/lidar/test.png'); print('wrote research/lidar/test.png')
