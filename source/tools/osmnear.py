#!/usr/bin/env python3
"""Find a mapped feature by WHERE it is, not by its name: what OpenStreetMap has inside a box round a point.
   python3 tools/osmnear.py <lat> <lon> [metres=500] [layer ...] [-g pattern]
        layers: railways highways waterways buildings amenities tourism   (default: railways highways waterways tourism)
        -g pattern   keep only features whose tags match, e.g. -g 'tunnel|bridge|ruins|abandoned|disused'
tools/nom.py finds a thing by name. This finds the unnamed tunnel, the abandoned rail bed or the ruin you know is near a
spot (the Steep Rock railroad tunnel in Connecticut was found this way, by its tunnel tag). It reads the copy of
OpenStreetMap that Esri hosts as feature layers for North America, which answers from cloud machines when the Overpass
servers do not. That copy lags OpenStreetMap by weeks and carries only the commoner tags."""
import sys,math,re,requests
a=sys.argv[1:]; pat=None
if '-g' in a: i=a.index('-g'); pat=re.compile(a[i+1],re.I); a=a[:i]+a[i+2:]
if len(a)<2: sys.exit(__doc__)
la,lo=float(a[0]),float(a[1]); rest=a[2:]; m=500.0
if rest and re.match(r'^\d+(\.\d+)?$',rest[0]): m=float(rest[0]); rest=rest[1:]
layers=rest or ['railways','highways','waterways','tourism']
dla=m/111320; dlo=m/(111320*math.cos(math.radians(la)))
SKIP={'OBJECTID','osm_id','osm_version','osm_timestamp','osm_uid','osm_user','osm_changeset','Shape__Length','Shape__Area','source_transform','source_date','source_ref','attribution'}
for ly in layers:
    u='https://services6.arcgis.com/Do88DoK2xjTUCXd1/arcgis/rest/services/OSM_NA_%s/FeatureServer/0/query'%ly.capitalize()
    try:
        j=requests.get(u,params={'geometry':f'{lo-dlo},{la-dla},{lo+dlo},{la+dla}','geometryType':'esriGeometryEnvelope','inSR':4326,'spatialRel':'esriSpatialRelIntersects','outFields':'*','returnGeometry':'true','outSR':4326,'geometryPrecision':5,'resultRecordCount':400,'f':'json'},timeout=60).json()
    except Exception as e: print('##',ly,'-> ERROR',str(e)[:80]); continue
    if 'error' in j: print('##',ly,'->',j['error'].get('message')); continue
    out=[]
    for f in j.get('features',[]):
        t={k:v for k,v in f['attributes'].items() if v not in (None,'',' ') and k not in SKIP}
        s=' '.join('%s=%s'%kv for kv in sorted(t.items()))
        if pat and not pat.search(s): continue
        g=f.get('geometry') or {}
        pts=[p for part in (g.get('paths') or g.get('rings') or []) for p in part] or ([[g['x'],g['y']]] if 'x' in g else [])
        if not pts: continue
        mid=pts[len(pts)//2]; d=math.hypot((mid[1]-la)*111320,(mid[0]-lo)*111320*math.cos(math.radians(la)))
        out.append((d,'%.5f,%.5f'%(mid[1],mid[0]),s[:230]))
    print('##',ly,':',len(out),'feature(s) within',int(m),'m'+(' matching' if pat else ''))
    for d,p,s in sorted(out)[:40]: print('  %4d m  %s  %s'%(d,p,s))
