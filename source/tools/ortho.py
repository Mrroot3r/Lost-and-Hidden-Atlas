"""The best leaf-off aerial for a point, as a picture of a given ground size. Used by the LiDAR evidence sheets
(tools/lidar_sheet.py) and the pin check (tools/pincheck.py).

   from ortho import ortho;  im,label = ortho(lat, lon, half_m, px)          a square of 2*half_m metres, px*px
   python3 tools/ortho.py <lat> <lon> [half_m]                             writes research/ortho_test.jpg

  New York        the state's leaf-off orthoimagery (orthos.its.ny.gov), cut to the frame by the service
  Massachusetts   MassGIS 2023 aerial imagery: leaf-off, flown 21 February to 28 April 2023, 15 cm. It is published as
                  map tiles only, so the frame is put together from tiles here. MassGIS: "No restrictions apply".
  Rhode Island    RIGIS, March 2026, 3 inch
  Vermont         VCGI's statewide mosaic (tiles)
  New Jersey      NJ Office of GIS, 2020 natural colour, 1 foot, leaf-off (tiles)
  Connecticut     CT ECO, spring 2023, 3 inch, leaf-off (tiles)
  New Hampshire   NH GRANIT, spring 2021 and 2022, 6 inch (tiles). Bare hardwoods in the frames looked at; snow near summits.
  Pennsylvania    PEMA 2021-2023 through PASDA, leaf-off. SLOW: three to nine seconds a frame.
  Maine           Maine GeoLibrary's statewide mosaic of its spring flights. It has holes in the north woods: a hole comes
                  back black and falls through to Esri.
  Kansas          the state's NG911 flight of 2024, 1 foot. The service does not say leaf-off; trees were bare in the frames
                  looked at.
  anywhere else   Esri World Imagery. The leaves may be on: say so wherever the picture is used as evidence.
The state is taken from the coarse outlines (lidar_dem.state_of); a blank or failed answer falls through to Esri.
The app draws from the same services (leafUrl in src/app.js): change an address in both places.
   python3 tools/ortho.py --which <lat> <lon>        only says which aerial a point would get"""
import io,math,os,sys,requests
from PIL import Image
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lidar_dem import merc,state_of
NY='https://orthos.its.ny.gov/arcgis/rest/services/wms/Latest/MapServer/export'
MA='https://tiles.arcgis.com/tiles/hGdibHYSPO59RG1h/arcgis/rest/services/orthos2023/MapServer/tile/%d/%d/%d'
ESRI='https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/export'
ESRI_TILES='https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/%d/%d/%d'
# state key -> (label, 'export' or 'tiles', address, extra request parameters or deepest tile zoom)
SRC={'ny':('New York leaf-off aerial','export',NY,None),
     'ma':('MassGIS leaf-off aerial, spring 2023','tiles',MA,20),
     'ri':('Rhode Island aerial, March 2026','export','https://maps.edc.uri.edu/rigis/rest/services/IMG/RI_202603_RGB_3in_web/ImageServer/exportImage',None),
     'vt':('Vermont state aerial (VCGI)','tiles','https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/IMG_VCGI_CLR_WM_CACHE/ImageServer/tile/%d/%d/%d',19),
     'nj':('New Jersey leaf-off aerial, 2020','tiles','https://maps.nj.gov/arcgis/rest/services/Basemap/Orthos_Natural_2020_NJ_WM/MapServer/tile/%d/%d/%d',20),
     'ct':('Connecticut leaf-off aerial, spring 2023','tiles','https://cteco.uconn.edu/ctraster/rest/services/images/Ortho_2023_tiled/ImageServer/tile/%d/%d/%d',20),
     'nh':('New Hampshire aerial, spring 2021-22','tiles','https://nhgeodata.unh.edu/image/rest/services/ImageServices/NH_2021_2022_6in_tiled/ImageServer/tile/%d/%d/%d',20),
     'pa':('Pennsylvania leaf-off aerial, 2021-23','export','https://imagery.pasda.psu.edu/arcgis/rest/services/pasda/PEMAImagery2021_2023/MapServer/export',{'layers':'show:3'}),
     'me':('Maine state aerial, spring flights','export','https://gis.maine.gov/image/rest/services/Misc/MaineOrthoimageryAggregate/ImageServer/exportImage',{'bandIds':'0,1,2'}),
     'ks':('Kansas state aerial, 2024','export','https://services.kgs.ku.edu/arcgis7/rest/services/IMAGERY_STATEWIDE/NG911_Imagery_2024/ImageServer/exportImage',None)}
ESRI_LABEL='Esri satellite (leaves may be on)'
UA={'User-Agent':'lost-hidden-atlas-research/1.0'}; R=20037508.342789244
def blank(im):
    lo,hi=im.resize((8,8)).convert('L').getextrema(); return hi-lo<12
def export(url,la,lo,half,px,extra=None):
    x,y=merc(la,lo); h=half/math.cos(math.radians(la))
    q={'bbox':f'{x-h},{y-h},{x+h},{y+h}','bboxSR':3857,'imageSR':3857,'size':f'{px},{px}','format':'jpg','f':'image'}; q.update(extra or {})
    r=requests.get(url,params=q,headers=UA,timeout=90)
    r.raise_for_status(); return Image.open(io.BytesIO(r.content)).convert('RGB')
def tiles(tpl,la,lo,half,px,zmax=20):
    """A frame put together from 256-pixel web map tiles (z/y/x), at the zoom whose detail is nearest what is asked for."""
    x,y=merc(la,lo); h=half/math.cos(math.radians(la)); want=2*h/px                                  # mercator metres to a pixel
    z=max(0,min(zmax,int(round(math.log2(2*R/256/want))))); res=2*R/256/2**z
    px0=(x-h+R)/res; px1=(x+h+R)/res; py0=(R-(y+h))/res; py1=(R-(y-h))/res                           # the frame in that zoom's pixels
    tx0,tx1,ty0,ty1=int(px0//256),int(px1//256),int(py0//256),int(py1//256)
    if (tx1-tx0+1)*(ty1-ty0+1)>64: raise ValueError('too many tiles for one frame')
    big=Image.new('RGB',((tx1-tx0+1)*256,(ty1-ty0+1)*256),'#444'); got=0
    for tx in range(tx0,tx1+1):
        for ty in range(ty0,ty1+1):
            for k in range(3):
                try:
                    r=requests.get(tpl%(z,ty,tx),headers=UA,timeout=40)
                    if r.status_code==200: big.paste(Image.open(io.BytesIO(r.content)).convert('RGB'),((tx-tx0)*256,(ty-ty0)*256)); got+=1
                    break
                except Exception: pass
    if not got: raise ValueError('no tiles')
    return big.crop((int(round(px0-tx0*256)),int(round(py0-ty0*256)),int(round(px1-tx0*256)),int(round(py1-ty0*256)))).resize((px,px),Image.LANCZOS)
def which(la,lo):
    """The label of the aerial a point would get first (it still falls through to Esri when that one is blank)."""
    st=state_of(la,lo)
    if st is None and -80<lo<-71.8 and 40.4<la<45.1: st='ny'                                         # the coarse outline can miss a point on the state line
    return SRC[st][0] if st in SRC else ESRI_LABEL
def ortho(la,lo,half,px):
    st=state_of(la,lo); tries=[]
    if st is None and -80<lo<-71.8 and 40.4<la<45.1: st='ny'                                         # the coarse outline can miss a point on the state line
    if st in SRC:
        label,kind,url,arg=SRC[st]
        tries.append((label,(lambda: tiles(url,la,lo,half,px,arg)) if kind=='tiles' else (lambda: export(url,la,lo,half,px,arg))))
    tries.append((ESRI_LABEL,lambda: export(ESRI,la,lo,half,px)))
    tries.append((ESRI_LABEL,lambda: tiles(ESRI_TILES,la,lo,half,px,19)))   # export answers 500 at close zoom over parts of rural Saskatchewan (sk_fwmi, Nov 2026); its tiles still come
    for label,f in tries:
        for k in range(2):
            try:
                im=f()
                if not blank(im): return im,label
                break
            except Exception: pass
    return Image.new('RGB',(px,px),'#444'),'no aerial could be fetched'
if __name__=='__main__':
    if sys.argv[1:2]==['--which']: print(which(float(sys.argv[2]),float(sys.argv[3]))); sys.exit(0)
    la,lo=float(sys.argv[1]),float(sys.argv[2]); half=int(sys.argv[3]) if len(sys.argv)>3 else 100
    im,label=ortho(la,lo,half,500); os.makedirs('research',exist_ok=True); im.save('research/ortho_test.jpg',quality=88); print(label,'-> research/ortho_test.jpg')
