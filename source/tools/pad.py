#!/usr/bin/env python3
"""Public-land (PAD-US) units at points or within a distance: python3 tools/pad.py label,lat,lon[,metres] ..."""
import sys,requests
U='https://services.arcgis.com/v01gqwM5QqNysAAi/arcgis/rest/services/PADUS_Public_Access/FeatureServer/0/query'
for a in sys.argv[1:]:
    p=a.split(','); lab,la,lo=p[0],float(p[1]),float(p[2]); d=float(p[3]) if len(p)>3 else 0
    q={'geometry':f'{lo},{la}','geometryType':'esriGeometryPoint','inSR':4326,'spatialRel':'esriSpatialRelIntersects','outFields':'Unit_Nm,MngNm_Desc,Pub_Access','returnGeometry':'false','f':'json'}
    if d: q.update({'distance':d,'units':'esriSRUnit_Meter'})
    try:
        j=requests.get(U,params=q,timeout=60).json()
        print(lab,d,'->',sorted({(f['attributes']['Unit_Nm'],f['attributes']['MngNm_Desc'],f['attributes']['Pub_Access']) for f in j.get('features',[])}) or 'nothing')
    except Exception as e: print(lab,'ERROR',str(e)[:80])
