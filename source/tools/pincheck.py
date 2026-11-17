#!/usr/bin/env python3
"""Contact sheets for checking pins against an aerial photo. Run after build_sites.py.
   python3 tools/pincheck.py --batch ri            every place in a batch
   python3 tools/pincheck.py id1 id2 ...           named places
   add --lidar to either for a second sheet of the same squares as bare-ground LiDAR shading (research/pincheck_*_lidar_*.jpg).
   Use it for anything in woods: a cellar, a race or a wall shows there when the aerial shows only trees.
Each tile is a 300 m square centred on the pin, with a 30 m ring. A place with a parking or trailhead point (th=) gets a second
tile for that point, titled TRAILHEAD in blue: check it is a lot or a road shoulder and not somebody's house or yard. Sheets go to research/pincheck_*.jpg.
LOOK at every tile: is the ring on the structure, the ruin or the documented footprint? If not, move the pin
only when you can see the right spot; otherwise keep it, set prec='area', and say what you saw in the pin note."""
import sys,json,io,math,os,requests
from PIL import Image,ImageDraw
S={s['id']:s for s in json.load(open('build/sites.json'))}
a=sys.argv[1:]
LIDAR='--lidar' in a; a=[x for x in a if x!='--lidar']
if a[:1]==['--batch']: ids=[i for i,s in S.items() if s.get('new')==a[1]]; tag=a[1]
else: ids=a; tag='picked'
if not ids: sys.exit('no places matched')
PX=420; HALF=150
ESRI='https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/export'
STATE=[('New York leaf-off',lambda la,lo:la>40.4 and -80.0<lo and (lo<-73.3 or (la<42.0 and lo<-73.48)),'https://orthos.its.ny.gov/arcgis/rest/services/wms/Latest/MapServer/export'),
       ('Rhode Island March 2026',lambda la,lo:la<42.02 and -71.9<lo<-71.1,'https://maps.edc.uri.edu/rigis/rest/services/IMG/RI_202603_RGB_3in_web/ImageServer/exportImage')]
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from ortho import ortho
from lidar_dem import state_of
MA_TEST=lambda la,lo: state_of(la,lo)=='ma'
def merc(la,lo): return lo*20037508.34/180, math.log(math.tan((90+la)*math.pi/360))*20037508.34/math.pi
def grab(url,la,lo):
    x,y=merc(la,lo); h=HALF/math.cos(math.radians(la))
    r=requests.get(url,params={'bbox':f'{x-h},{y-h},{x+h},{y+h}','bboxSR':3857,'imageSR':3857,'size':f'{PX},{PX}','format':'jpg','f':'image'},timeout=60)
    im=Image.open(io.BytesIO(r.content)).convert('RGB')
    lo_,hi_=im.resize((8,8)).convert('L').getextrema()
    if hi_-lo_<12: raise ValueError('blank image')
    return im
PADQ='https://services.arcgis.com/v01gqwM5QqNysAAi/arcgis/rest/services/PADUS_Public_Access/FeatureServer/0/query'
def land(s):
    """The public-land unit under a pin, from the place itself if the build looked it up, else asked for now."""
    if s.get('pl'): return '%s (%s)'%(s['pl'][0],s['pl'][2])
    try:
        fs=requests.get(PADQ,params={'geometry':'%s,%s'%(s['lon'],s['lat']),'geometryType':'esriGeometryPoint','inSR':4326,'spatialRel':'esriSpatialRelIntersects','outFields':'Unit_Nm,Pub_Access','returnGeometry':'false','f':'json'},timeout=40).json().get('features',[])
        fs=sorted(fs,key=lambda f:f['attributes'].get('Pub_Access') not in ('OA','RA'))
        return '%s (%s)'%(fs[0]['attributes']['Unit_Nm'],fs[0]['attributes']['Pub_Access']) if fs else None
    except Exception: return 'land lookup failed'
WARN=[]
tiles=[]; ltiles=[]
def lidar_tile(s,i):
    """The same 300 m square as shaded bare ground, from the elevation service lidar_dem picks for the spot."""
    from lidar_dem import dem,shade,coarse,empty
    import numpy as np
    note='LiDAR bare ground'
    try:
        g,sc=dem(s['lat'],s['lon'],HALF,PX)
        if empty(g): raise ValueError('no elevation here')
        if coarse(g,sc): note='NO 1 m LiDAR HERE: coarse model, shows nothing small'
        g=np.where(np.isfinite(g)&(g>-1000),g,np.nan); g=np.nan_to_num(g,nan=float(np.nanmin(g)))
        im=Image.fromarray(shade(g,sc)).convert('RGB')
    except Exception as e: im=Image.new('RGB',(PX,PX),'#444'); note='no LiDAR picture: '+str(e)[:40]
    d=ImageDraw.Draw(im); c=PX//2; r=30/(2*HALF)*PX
    d.ellipse([c-r,c-r,c+r,c+r],outline='#ff2d95',width=2); d.line([c-8,c,c+8,c],fill='#ff2d95',width=2); d.line([c,c-8,c,c+8],fill='#ff2d95',width=2)
    d.rectangle([0,0,PX,34],fill='#000000'); d.text((5,3),f"{i}  [{s['prec']}/{s['st']}]",fill='#ffffff'); d.text((5,18),note,fill='#ffb347' if note.startswith('NO') else '#bbbbbb')
    return im,note
todo=[]
for i in ids:
    s=S.get(i)
    if not s: print('unknown id',i); continue
    todo.append((i,s))
    if s.get('th'):                                        # the parking or trailhead point gets its own tile: it can land on a house too
        t=dict(s); t['lat'],t['lon']=s['th'][0],s['th'][1]; t['_th']=s.get('thn') or 'trailhead'; todo.append((i+' TRAILHEAD',t))
FAILED=[]
for i,s in todo:
    src='Esri satellite (leaves may be on)'; im=None
    if MA_TEST(s['lat'],s['lon']):                         # Massachusetts: the state's leaf-off imagery comes as tiles (tools/ortho.py)
        try:
            im,src=ortho(s['lat'],s['lon'],HALF,PX)
            if src.startswith('no aerial'): im=None
        except Exception: im=None
    for name,test,url in STATE:
        if im is None and test(s['lat'],s['lon']):
            try: im=grab(url,s['lat'],s['lon']); src=name
            except Exception: im=None
            break
    if im is None:
        try: im=grab(ESRI,s['lat'],s['lon'])
        except Exception:
            import time; time.sleep(5)
            try: im=grab(ESRI,s['lat'],s['lon'])
            except Exception as e:
                im=Image.new('RGB',(PX,PX),'#7a1010'); src='DOWNLOAD FAILED: not a picture of the ground'; FAILED.append(i)
    ld=land(s)
    if s.get('_th'):
        if not ld or ld.endswith('(XA)'): WARN.append('%s (%s) is not on mapped public land: look at its tile and make sure it is a lot or a road shoulder, not a house or a yard'%(i,s['_th']))
    elif s.get('acc')=='public' and (not ld or ld.endswith('(XA)')): WARN.append('%s is marked public, but the pin is %s'%(i,('on land the public-land map calls closed: '+ld) if ld else 'not on mapped public land: say in the access note who owns it and how you know, or change the access type'))
    d=ImageDraw.Draw(im); c=PX//2; r=30/(2*HALF)*PX
    d.ellipse([c-r,c-r,c+r,c+r],outline='#ff2d95',width=3); d.line([c-8,c,c+8,c],fill='#ff2d95',width=2); d.line([c,c-8,c,c+8],fill='#ff2d95',width=2)
    d.rectangle([0,0,PX,34],fill='#000000'); d.text((5,3),f"{i}  [{s['prec']}/{s['st']}]" if not s.get('_th') else f"{i}: {s['_th']}"[:66],fill='#ffffff' if not s.get('_th') else '#8fd3ff'); d.text((5,18),f"{s['lat']},{s['lon']}  {src}",fill='#bbbbbb')
    d.rectangle([0,PX-16,PX,PX],fill='#000000'); d.text((5,PX-14),('land: '+ld) if ld else 'land: not on mapped public land',fill='#7CFC98' if ld and not ld.endswith('(XA)') else '#ffb347')
    tiles.append(im); print(i,'|',src,'| land:',ld or 'not on mapped public land')
    if LIDAR:
        lim,note=lidar_tile(s,i); ltiles.append(lim); print(' ',note)
os.makedirs('research',exist_ok=True); PER=12
for T,suf in ((tiles,''),(ltiles,'_lidar')):
    for n in range(0,len(T),PER):
        part=T[n:n+PER]; cols=4; rows=math.ceil(len(part)/cols); sh=Image.new('RGB',(cols*PX,rows*PX),'#222')
        for k,im in enumerate(part): sh.paste(im,((k%cols)*PX,(k//cols)*PX))
        p=f'research/pincheck_{tag}{suf}_{n//PER+1}.jpg'; sh.save(p,quality=82); print('wrote',p)
for w in WARN: print('CHECK ACCESS:',w)
for f in FAILED: print('WARNING: no aerial came back for',f,'(red tile). That is a failed download, NOT empty ground: run the pin check again for it.')
print('To move a pin onto something you can see: python3 tools/pix.py pin <lat> <lon> <x> <y>   (lat,lon = the pin over the tile; x,y = the pixel in the sheet)')
