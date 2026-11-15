#!/usr/bin/env python3
"""Fetch imagery crops around a point for visual verification.
usage: img.py name lat lon halfwidth_m [layers comma] """
import sys, math, urllib.request, urllib.parse, io, json, os
from PIL import Image, ImageDraw
UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
def bbox3857(lat,lon,hw):
    R=6378137.0
    x=math.radians(lon)*R; y=math.log(math.tan(math.pi/4+math.radians(lat)/2))*R
    k=1/math.cos(math.radians(lat))
    return (x-hw*k,y-hw*k,x+hw*k,y+hw*k)
def get(url):
    req=urllib.request.Request(url,headers=UA)
    return urllib.request.urlopen(req,timeout=60).read()
def layer_url(layer,bb,size):
    b=','.join('%.2f'%v for v in bb)
    if layer.startswith('ny'):   # ny:Latest, ny:2004, ny:napp
        svc=layer.split(':')[1]
        return f"https://orthos.its.ny.gov/arcgis/rest/services/wms/{svc}/MapServer/export?bbox={b}&bboxSR=3857&imageSR=3857&size={size},{size}&format=jpg&f=image"
    if layer=='hill':
        return f"https://elevation.its.ny.gov/arcgis/rest/services/NYS_Statewide_Hillshade/MapServer/export?bbox={b}&bboxSR=3857&imageSR=3857&size={size},{size}&format=jpg&f=image"
    if layer.startswith('dem'):
        z=float(layer[3:] or 2)
        rr=urllib.parse.quote(json.dumps({"rasterFunction":"Hillshade","rasterFunctionArguments":{"Azimuth":315,"Altitude":40,"ZFactor":z},"variableName":"DEM"}))
        return f"https://elevation.its.ny.gov/arcgis/rest/services/Latest_DEM/ImageServer/exportImage?bbox={b}&bboxSR=3857&imageSR=3857&size={size},{size}&format=jpg&renderingRule={rr}&f=image"
    if layer=='esri':
        return f"https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/export?bbox={b}&bboxSR=3857&imageSR=3857&size={size},{size}&format=jpg&f=image"
    if layer=='topo':
        return f"https://services.arcgisonline.com/ArcGIS/rest/services/USA_Topo_Maps/MapServer/export?bbox={b}&bboxSR=3857&imageSR=3857&size={size},{size}&format=jpg&f=image"
    if layer=='usgs':
        return f"https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/export?bbox={b}&bboxSR=3857&imageSR=3857&size={size},{size}&format=jpg&f=image"
    if layer=='osm':
        return f"https://services.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/export?bbox={b}&bboxSR=3857&imageSR=3857&size={size},{size}&format=jpg&f=image"
    raise SystemExit('layer?')
def panel(layer,lat,lon,hw,size=640,pin=True,label=None):
    bb=bbox3857(lat,lon,hw)
    try:
        im=Image.open(io.BytesIO(get(layer_url(layer,bb,size)))).convert('RGB')
    except Exception as e:
        im=Image.new('RGB',(size,size),(60,0,0)); ImageDraw.Draw(im).text((10,10),str(e)[:80],fill='white')
    d=ImageDraw.Draw(im)
    if pin:
        c=size//2; d.ellipse((c-9,c-9,c+9,c+9),outline=(255,0,255),width=3); d.line((c-16,c,c-4,c),fill=(255,0,255),width=2); d.line((c+4,c,c+16,c),fill=(255,0,255),width=2); d.line((c,c-16,c,c-4),fill=(255,0,255),width=2); d.line((c,c+4,c,c+16),fill=(255,0,255),width=2)
    # scale bar 100m or so
    bar_m = 100 if hw<=600 else (500 if hw<=3000 else 2000)
    px=bar_m/(2*hw)*size
    d.rectangle((10,size-22,10+px,size-16),fill=(255,255,0),outline=(0,0,0))
    d.text((12,size-36),f"{bar_m} m  {label or layer}",fill=(255,255,0))
    # grid ticks every quarter for referencing offsets
    return im
if __name__=='__main__':
    name,lat,lon,hw=sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])
    layers=(sys.argv[5] if len(sys.argv)>5 else 'ny:Latest,hill,topo').split(',')
    size=int(sys.argv[6]) if len(sys.argv)>6 else 640
    ims=[panel(l,lat,lon,hw,size) for l in layers]
    W=sum(i.width for i in ims); out=Image.new('RGB',(W,size)); x=0
    for i in ims: out.paste(i,(x,0)); x+=i.width
    os.makedirs('img',exist_ok=True); out.save(f'img/{name}.jpg',quality=82); print('saved',f'img/{name}.jpg',out.size)
