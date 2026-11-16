"""Raw LiDAR ground elevation from the New York State "Latest_DEM" image service, as a float grid, and a shaded-relief
renderer. Used by lidar_scan.py and lidar_sheet.py (GUIDE.md section 13). New York only: other states need their own
elevation service here.   python3 tools/lidar_dem.py <lat> <lon>   writes research/lidar/test.png"""
import io,math,requests,numpy as np
from PIL import Image
URL='https://elevation.its.ny.gov/arcgis/rest/services/Latest_DEM/ImageServer/exportImage'
def merc(la,lo): return lo*20037508.34/180, math.log(math.tan((90+la)*math.pi/360))*20037508.34/math.pi
def unmerc(x,y): return math.degrees(2*math.atan(math.exp(y*math.pi/20037508.34))-math.pi/2), x*180/20037508.34
def dem(la,lo,half_m,px):
    """square of 2*half_m ground metres centred on la,lo, px*px cells. Returns (grid, scale) where scale = ground metres per cell."""
    x,y=merc(la,lo); k=1/math.cos(math.radians(la)); h=half_m*k
    import time
    for k in range(5):
        try:
            r=requests.get(URL,params={'bbox':f'{x-h},{y-h},{x+h},{y+h}','bboxSR':3857,'imageSR':3857,'size':f'{px},{px}','format':'tiff','pixelType':'F32','interpolation':'RSP_BilinearInterpolation','f':'image'},timeout=120)
            r.raise_for_status(); im=Image.open(io.BytesIO(r.content)); a=np.array(im,dtype='float32'); break
        except Exception as e:
            if k==4: raise
            time.sleep(3+3*k)
    return a, 2*half_m/px
def shade(a,scale,az=315,alt=35,z=2.0):
    gy,gx=np.gradient(a*z,scale); slope=np.pi/2-np.arctan(np.hypot(gx,gy)); asp=np.arctan2(-gx,gy)
    azr=math.radians(360-az+90); altr=math.radians(alt)
    s=np.sin(altr)*np.sin(slope)+np.cos(altr)*np.cos(slope)*np.cos(azr-asp)
    return np.clip(s*255,0,255).astype('uint8')
if __name__=='__main__':
    import sys
    a,sc=dem(float(sys.argv[1]),float(sys.argv[2]),250,500); print(a.shape,sc,float(np.nanmin(a)),float(np.nanmax(a)),a.dtype)
    import os; os.makedirs('research/lidar',exist_ok=True); Image.fromarray(shade(a,sc)).save('research/lidar/test.png'); print('wrote research/lidar/test.png')
