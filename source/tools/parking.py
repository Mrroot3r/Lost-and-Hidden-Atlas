#!/usr/bin/env python3
"""Where to leave the car: parking lots OpenStreetMap has mapped near a place, nearest first.
   python3 tools/parking.py <lat> <lon> [metres=1500]
For each lot: distance and direction from the point, its coordinate, the road it is on, and the public-land unit under it
(blank = not on mapped public land: then say in the access note whose lot it is, or do not use it).
Use the coordinate as the place's trailhead point (th=[lat,lon], thn='what the lot is'), then run the pin check, which
draws a tile for it. Nothing listed does not mean nowhere to park: small gravel pull-offs are often unmapped. Then
look for one on the aerial (tools/look.py) along the road the managing body's page names, or leave th out and say so."""
import sys,json,math,time,urllib.parse,urllib.request
try: la,lo=float(sys.argv[1]),float(sys.argv[2]); m=float(sys.argv[3]) if len(sys.argv)>3 else 1500.0
except (IndexError,ValueError): sys.exit(__doc__)
UA={'User-Agent':'lost-hidden-atlas-research/1.0 (personal research tool)'}
PAD='https://services.arcgis.com/v01gqwM5QqNysAAi/arcgis/rest/services/PADUS_Public_Access/FeatureServer/0/query'
def get(u,p):
    for k in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u+'?'+urllib.parse.urlencode(p),headers=UA),timeout=40))
        except Exception as e: err=e; time.sleep(2+2*k)
    raise err
dla=m/111320; dlo=m/(111320*math.cos(math.radians(la)))
try: j=get('https://nominatim.openstreetmap.org/search',{'q':'[parking]','format':'jsonv2','limit':30,'viewbox':f'{lo-dlo},{la+dla},{lo+dlo},{la-dla}','bounded':1})
except Exception as e: sys.exit('lookup failed: '+str(e)[:100]+'  (run it again; the service allows one request a second)')
rows=[]
for x in j:
    a,b=float(x['lat']),float(x['lon']); e=(b-lo)*111320*math.cos(math.radians(la)); n=(a-la)*111320
    rows.append((math.hypot(e,n),'N NE E SE S SW W NW'.split()[int((math.degrees(math.atan2(e,n))+382.5)%360//45)],a,b,x['display_name']))
rows.sort()
print(f'{len(rows)} mapped parking lot(s) within {m:g} m of {la}, {lo}'+('' if rows else ': none mapped. Look along the access road on the aerial (tools/look.py), or widen the distance.'))
for d,c,a,b,name in rows[:12]:
    land=''
    try:
        fs=get(PAD,{'geometry':f'{b},{a}','geometryType':'esriGeometryPoint','inSR':4326,'spatialRel':'esriSpatialRelIntersects','outFields':'Unit_Nm,Pub_Access','returnGeometry':'false','f':'json'}).get('features',[])
        if fs: land='%s (%s)'%(fs[0]['attributes']['Unit_Nm'],fs[0]['attributes']['Pub_Access'])
    except Exception: land='land lookup failed'
    print(f"  {d:5.0f} m {c:2}  {a:.5f}, {b:.5f}  |  {', '.join(name.split(', ')[:3])}  |  land: {land or 'not on mapped public land'}")
if rows: print('Check the one you use on the aerial: the pin check draws a TRAILHEAD tile for a place that has th=[lat,lon].')
