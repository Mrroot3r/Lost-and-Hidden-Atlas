"""Fetch the outline of one public-land unit from the USGS public-land map (PAD-US), for lidar_scan.py.
   python3 tools/lidar_unit.py "Partridge Run"            lists units whose name contains the text, with acres
   python3 tools/lidar_unit.py "Partridge Run Wma" save   writes research/lidar/unit_<name>.json for the exact name
   python3 tools/lidar_unit.py "Wendell State Forest" save -73.52,41.2,-69.9,42.9     the same, keeping only pieces that
                                                          touch the box (so a name used in two states gives one unit)
The outline is only a guide to where to look. PAD-US outlines are generalised and can take in private lots: check every
find against the tax parcel (tools/parcel.py) before calling it public land."""
import sys,json,os,requests
U='https://services.arcgis.com/v01gqwM5QqNysAAi/arcgis/rest/services/PADUS_Public_Access/FeatureServer/0/query'
name=sys.argv[1].replace("'","''"); save=len(sys.argv)>2; box=sys.argv[3] if len(sys.argv)>3 else ''       # box: "west,south,east,north", only pieces touching it
w=f"Unit_Nm='{name}'" if save else f"Unit_Nm LIKE '%{name}%'"
geo={'geometry':box,'geometryType':'esriGeometryEnvelope','inSR':4326,'spatialRel':'esriSpatialRelIntersects'} if box else {}
# The service has bad minutes, and answers them with an error or nothing at all. That used to read as "no unit with exactly that name"
# (a Kansas City session was told two real units did not exist, November 23, 2026), so it is asked three times and then said plainly.
import time
j=None
for k in range(3):
    try:
        j=requests.get(U,params={**geo,'where':w,'outFields':'Unit_Nm,MngNm_Desc,Pub_Access,GIS_Acres,ST_Name','returnGeometry':'true' if save else 'false','outSR':4326,'geometryPrecision':6,'f':'json'},timeout=120).json()
        if 'error' not in j: break
    except Exception: pass
    j=None; time.sleep(8*(k+1))
if j is None: sys.exit('the public-land service did not answer; run the same command again in a minute')
fs=j.get('features',[])
if not save:
    for a in sorted({(f['attributes']['Unit_Nm'],f['attributes']['ST_Name'],round(f['attributes']['GIS_Acres'] or 0),f['attributes']['Pub_Access']) for f in fs}): print(a)
    sys.exit()
rings=[r for f in fs for r in f['geometry']['rings']]
if not rings: sys.exit('no unit with exactly that name; run without "save" to list names')
os.makedirs('research/lidar',exist_ok=True); p='research/lidar/unit_'+''.join(c for c in sys.argv[1] if c.isalnum())+'.json'
json.dump({'name':sys.argv[1],'rings':rings},open(p,'w')); print('wrote',p,len(rings),'rings from',len(fs),'pieces')
