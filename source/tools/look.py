#!/usr/bin/env python3
"""Aerial tiles for finding a structure by eye: python3 tools/look.py out.jpg label,lat,lon,half_m ...
Each tile is centred on lat,lon and is 2*half_m wide; grid lines are drawn every half_m/3, so an offset can be read off."""
import sys,io,math,requests
from PIL import Image,ImageDraw
ESRI='https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/export'
PX=560
def merc(la,lo): return lo*20037508.34/180, math.log(math.tan((90+la)*math.pi/360))*20037508.34/math.pi
tiles=[]; FAILED=[]
import time
for a in sys.argv[2:]:
    lab,la,lo,h=a.split(','); la=float(la); lo=float(lo); h=float(h)
    x,y=merc(la,lo); hh=h/math.cos(math.radians(la))
    im=None
    for k in range(3):
        try:
            r=requests.get(ESRI,params={'bbox':f'{x-hh},{y-hh},{x+hh},{y+hh}','bboxSR':3857,'imageSR':3857,'size':f'{PX},{PX}','format':'jpg','f':'image'},timeout=60)
            im=Image.open(io.BytesIO(r.content)).convert('RGB'); break
        except Exception: im=None; time.sleep(3+4*k)
    if im is None:
        im=Image.new('RGB',(PX,PX),'#7a1010'); FAILED.append(lab)
        ImageDraw.Draw(im).text((20,PX//2),'DOWNLOAD FAILED: this is not a picture of the ground. Run again.',fill='#fff')
    d=ImageDraw.Draw(im); c=PX//2; step=PX/6
    for k in range(1,6):
        col='#ff2d95' if k==3 else '#ffffff'
        d.line([k*step,0,k*step,PX],fill=col,width=1); d.line([0,k*step,PX,k*step],fill=col,width=1)
    d.rectangle([0,0,PX,16],fill='#000'); d.text((4,2),f'{lab} {la},{lo} grid {h/3:.0f} m',fill='#fff')
    tiles.append(im)
cols=min(3,len(tiles)); rows=math.ceil(len(tiles)/cols); sh=Image.new('RGB',(cols*PX,rows*PX),'#222')
for k,im in enumerate(tiles): sh.paste(im,((k%cols)*PX,(k//cols)*PX))
sh.save(sys.argv[1],quality=85); print('wrote',sys.argv[1])
for f in FAILED: print('WARNING: no aerial came back for',f,'(red tile). That is a failed download, NOT empty ground: run the command again.')
print('To turn a spot you can see into a coordinate: python3 tools/pix.py look <lat> <lon> <half_m> <x> <y>   (x,y = the pixel in this picture)')
