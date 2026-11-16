#!/usr/bin/env python3
"""Contact sheets for checking pins against an aerial photo. Run after build_sites.py.
   python3 tools/pincheck.py --batch ri            every place in a batch
   python3 tools/pincheck.py id1 id2 ...           named places
Each tile is a 300 m square centred on the pin, with a 30 m ring. Sheets go to research/pincheck_*.jpg.
LOOK at every tile: is the ring on the structure, the ruin or the documented footprint? If not, move the pin
only when you can see the right spot; otherwise keep it, set prec='area', and say what you saw in the pin note."""
import sys,json,io,math,os,requests
from PIL import Image,ImageDraw
S={s['id']:s for s in json.load(open('build/sites.json'))}
a=sys.argv[1:]
if a[:1]==['--batch']: ids=[i for i,s in S.items() if s.get('new')==a[1]]; tag=a[1]
else: ids=a; tag='picked'
if not ids: sys.exit('no places matched')
PX=420; HALF=150
ESRI='https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/export'
STATE=[('New York leaf-off',lambda la,lo:lo<-73.3 or (la<42.0 and lo<-73.48),'https://orthos.its.ny.gov/arcgis/rest/services/wms/Latest/MapServer/export'),
       ('Rhode Island March 2026',lambda la,lo:la<42.02 and -71.9<lo<-71.1,'https://maps.edc.uri.edu/rigis/rest/services/IMG/RI_202603_RGB_3in_web/ImageServer/exportImage')]
def merc(la,lo): return lo*20037508.34/180, math.log(math.tan((90+la)*math.pi/360))*20037508.34/math.pi
def grab(url,la,lo):
    x,y=merc(la,lo); h=HALF/math.cos(math.radians(la))
    r=requests.get(url,params={'bbox':f'{x-h},{y-h},{x+h},{y+h}','bboxSR':3857,'imageSR':3857,'size':f'{PX},{PX}','format':'jpg','f':'image'},timeout=60)
    im=Image.open(io.BytesIO(r.content)).convert('RGB')
    lo_,hi_=im.resize((8,8)).convert('L').getextrema()
    if hi_-lo_<12: raise ValueError('blank image')
    return im
tiles=[]
for i in ids:
    s=S.get(i)
    if not s: print('unknown id',i); continue
    src='Esri satellite (leaves may be on)'; im=None
    for name,test,url in STATE:
        if test(s['lat'],s['lon']):
            try: im=grab(url,s['lat'],s['lon']); src=name
            except Exception: im=None
            break
    if im is None:
        try: im=grab(ESRI,s['lat'],s['lon'])
        except Exception as e: im=Image.new('RGB',(PX,PX),'#444'); src='no image: '+str(e)[:30]
    d=ImageDraw.Draw(im); c=PX//2; r=30/(2*HALF)*PX
    d.ellipse([c-r,c-r,c+r,c+r],outline='#ff2d95',width=3); d.line([c-8,c,c+8,c],fill='#ff2d95',width=2); d.line([c,c-8,c,c+8],fill='#ff2d95',width=2)
    d.rectangle([0,0,PX,34],fill='#000000'); d.text((5,3),f"{i}  [{s['prec']}/{s['st']}]",fill='#ffffff'); d.text((5,18),f"{s['lat']},{s['lon']}  {src}",fill='#bbbbbb')
    tiles.append(im); print(i,src)
os.makedirs('research',exist_ok=True); PER=12
for n in range(0,len(tiles),PER):
    part=tiles[n:n+PER]; cols=4; rows=math.ceil(len(part)/cols); sh=Image.new('RGB',(cols*PX,rows*PX),'#222')
    for k,im in enumerate(part): sh.paste(im,((k%cols)*PX,(k//cols)*PX))
    p=f'research/pincheck_{tag}_{n//PER+1}.jpg'; sh.save(p,quality=82); print('wrote',p)
