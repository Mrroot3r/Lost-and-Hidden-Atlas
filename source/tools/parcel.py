"""Who owns the ground under a point (New York State tax parcels; only some counties publish owner names).
   python3 tools/parcel.py <lat> <lon> [<lat> <lon> ...]
Prints the owner TYPE and property class, not the owner's name: names of private owners do not go in the repository.
Owner type 2 or a name starting "NYS"/"State of New York" is state land; class 9xx is public or conservation land."""
import sys,requests
U='https://services6.arcgis.com/EbVsqZ18sv1kVJ3k/arcgis/rest/services/NYS_Tax_Parcels_Public/FeatureServer/1/query'
a=sys.argv[1:]
for i in range(0,len(a)-1,2):
    la,lo=a[i],a[i+1]
    try:
        fs=requests.get(U,params={'geometry':f'{lo},{la}','geometryType':'esriGeometryPoint','inSR':4326,'spatialRel':'esriSpatialRelIntersects','outFields':'PRIMARY_OWNER,PROP_CLASS,ACRES,MUNI_NAME,OWNER_TYPE,PARCEL_ADDR','returnGeometry':'false','f':'json'},timeout=60).json().get('features',[])
    except Exception as e: print(la,lo,'lookup failed:',str(e)[:60]); continue
    if not fs: print(la,lo,'no parcel record (the county may not publish, or the point is on a road)'); continue
    p=fs[0]['attributes']; o=(p.get('PRIMARY_OWNER') or '').upper()
    kind='STATE LAND' if o.startswith(('NYS','STATE OF NEW YORK','NEW YORK STATE','PEOPLE OF THE STATE')) else ('public or conservation land (class 9xx)' if str(p.get('PROP_CLASS','')).startswith('9') else ('owner not published' if not o else 'PRIVATE'))
    print(la,lo,'->',kind,'| class',p.get('PROP_CLASS'),'|',p.get('ACRES'),'acres |',p.get('MUNI_NAME'),'|',(p.get('PARCEL_ADDR') or '') if kind!='PRIVATE' else 'address withheld')
