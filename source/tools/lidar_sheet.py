"""Evidence sheets for LiDAR finds (GUIDE.md section 13).
   python3 tools/lidar_sheet.py maps <lat> <lon>
        lists the historic USGS sheets covering a point and downloads none
   python3 tools/lidar_sheet.py get <downloadURL>
        downloads one sheet into cache/topo/ and prints its path
   python3 tools/lidar_sheet.py sheet out.jpg <half_m> <map.tif>[,<map.tif>] "label,lat,lon" ...
        one row per spot: LiDAR | leaf-off aerial (same frame) | each old map. Pink ticks mark the same point in every panel.
LOOK at the sheet. A find needs all of: a sharp pit or wall on LiDAR, a building on an old map at the spot, nothing
standing on the aerial, and a parcel check (tools/parcel.py)."""
import sys,os,io,re,math,json,requests,urllib.request,urllib.parse,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from PIL import Image,ImageDraw
UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
if sys.argv[1]=='maps':
    la,lo=float(sys.argv[2]),float(sys.argv[3]); d=0.0005
    u='https://tnmaccess.nationalmap.gov/api/v1/products?'+urllib.parse.urlencode({'datasets':'Historical Topographic Maps','bbox':f'{lo-d},{la-d},{lo+d},{la+d}','prodFormats':'GeoTIFF','max':100})
    its=[]
    for it in json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60)).get('items',[]):
        m=re.search(r'_(\d{4})_(\d+)_geo\.tif$',it['downloadURL'])
        if m and int(m.group(2))<=63360: its.append((int(m.group(1)),int(m.group(2)),it['downloadURL']))
    try:
        for y,s,u in sorted(its): print(y,'1:%d'%s,u)
    except BrokenPipeError: pass
    sys.exit()
if sys.argv[1]=='get':
    p='cache/topo/'+sys.argv[2].split('/')[-1]; os.makedirs('cache/topo',exist_ok=True)
    if not os.path.exists(p): open(p,'wb').write(urllib.request.urlopen(urllib.request.Request(sys.argv[2],headers=UA),timeout=600).read())
    print(p); sys.exit()
from lidar_dem import dem,shade,merc
from topocrop import crop
out=sys.argv[2]; HALF=int(sys.argv[3]); maps=[m for m in sys.argv[4].split(',') if m]; items=[a.split(',') for a in sys.argv[5:]]; P=500
def ortho(la,lo,half,px):
    x,y=merc(la,lo); h=half/math.cos(math.radians(la))
    for k in range(4):
        try:
            r=requests.get('https://orthos.its.ny.gov/arcgis/rest/services/wms/Latest/MapServer/export',params={'bbox':f'{x-h},{y-h},{x+h},{y+h}','bboxSR':3857,'imageSR':3857,'size':f'{px},{px}','format':'jpg','f':'image'},timeout=90)
            return Image.open(io.BytesIO(r.content)).convert('RGB')
        except Exception: pass
    return Image.new('RGB',(px,px),'#444')
def mark(im,txt):
    d=ImageDraw.Draw(im); c=P//2
    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)): d.line([c+dx*22,c+dy*22,c+dx*38,c+dy*38],fill='#ff2d95',width=2)
    d.rectangle([0,0,P,15],fill='#000'); d.text((4,2),txt,fill='#ff0'); return im
sheet=Image.new('RGB',((2+len(maps))*P,len(items)*P),'#222')
for r,(lab,la,lo) in enumerate(items):
    la=float(la); lo=float(lo); a,sc=dem(la,lo,HALF,P)
    hs=shade(a,sc,315,40,3.0).astype('float32')*0.6+shade(a,sc,45,40,3.0).astype('float32')*0.4
    cells=[mark(Image.fromarray(hs.astype('uint8')).convert('RGB'),f'{lab} LiDAR {2*HALF} m across  {la},{lo}'),mark(ortho(la,lo,HALF,P),'leaf-off aerial, same frame')]
    for m in maps:
        y=(re.search(r'_(\d{4})_(\d+)_geo',m) or [0,'?','24000']); hw=900 if int(y[2])>30000 else 350
        try: im=crop(m,la,lo,hw,P)[0].convert('RGB')
        except Exception as e: im=Image.new('RGB',(P,P),'#444'); ImageDraw.Draw(im).text((10,40),str(e)[:70],fill='#fff')
        cells.append(mark(im,f'{y[1]} USGS map, {2*hw} m across'))
    for c,im in enumerate(cells): sheet.paste(im,(c*P,r*P))
sheet.save(out,quality=88); print('wrote',out)
