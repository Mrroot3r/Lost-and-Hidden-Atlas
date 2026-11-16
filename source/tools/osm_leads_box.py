#!/usr/bin/env python3
"""Download OpenStreetMap's mapped ruins and other leads for one box, not a whole state: the leads half of
tools/osm_layers.py, for when only a metropolitan area is wanted and the state's rail lines are not being added yet.

   python3 tools/osm_leads_box.py -95.80 38.20 -93.40 40.00 mo ks
        west south east north, then the state keys the box touches. Add --skip-mines to leave out mapped mine
        entrances: round Kansas City nearly all of them are the doors of working underground business parks. Writes cache/osm/<key>_leads.json for each key
        (the same download in each; tools/leads.py keeps only the points inside that state's outline).
Then list the keys in STATE_KEYS at the top of tools/leads.py and run it, then all.sh.

It asks the copies of OpenStreetMap that Esri hosts as feature layers (updated daily), as osm_layers.py does, so it
works when Overpass cannot be reached. Data is OpenStreetMap, (c) OpenStreetMap contributors, ODbL.
The box used for Kansas City in November 2026 is the one above: about 60 miles each way from downtown."""
import sys,os,json,time,urllib.request,urllib.parse
SKIP='--skip-mines' in sys.argv; ARGS=[a for a in sys.argv[1:] if a!='--skip-mines']
if len(ARGS)<5: sys.exit(__doc__)
W,S,E,N=[float(x) for x in ARGS[:4]]; KEYS=ARGS[4:]
R='https://services6.arcgis.com/Do88DoK2xjTUCXd1/arcgis/rest/services/'; UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
os.makedirs('cache/osm',exist_ok=True)
def post(layer,params):
    d=urllib.parse.urlencode(params).encode()
    for k in range(5):
        try:
            j=json.loads(urllib.request.urlopen(urllib.request.Request(R+layer+'/FeatureServer/0/query',data=d,headers=UA),timeout=180).read())
            if 'error' in j: raise ValueError(str(j['error'])[:120])
            return j
        except Exception as e:
            if k==4: raise
            print('  retry',layer,str(e)[:70],flush=True); time.sleep(6*(k+1))
def pull(layer,where,fields,extra=None,nstrips=3):
    out={}
    for c in range(nstrips):
        w,e=W+(E-W)*c/nstrips,W+(E-W)*(c+1)/nstrips; off=0
        while True:
            p={'where':where,'geometry':f'{w},{S},{e},{N}','geometryType':'esriGeometryEnvelope','inSR':4326,'spatialRel':'esriSpatialRelIntersects',
               'outFields':fields,'outSR':4326,'geometryPrecision':5,'orderByFields':'OBJECTID','resultOffset':off,'resultRecordCount':2000,'f':'geojson'}
            if extra: p.update(extra)
            fs=post(layer,p).get('features',[])
            for f in fs: out[(f.get('properties') or f.get('attributes'))['OBJECTID']]=f
            off+=len(fs)
            if len(fs)<2000: break
        print(f'  {layer} strip {w:.2f}..{e:.2f}: {len(out)} so far',flush=True)
    return list(out.values())
def tags(p,keys): return {k:p[k] for k in keys if p.get(k) not in (None,'')}
H="('ruins','archaeological_site','mine','mine_shaft','adit','kiln','lime_kiln','charcoal_pile','industrial','farm','railway_station','railway','aqueduct','lock','canal','fort','ghost_town','locomotive','quarry')"
leads=[]
for f in pull('OSM_NA_POIs',f"historic IN {H} OR man_made IN ('kiln','adit','mineshaft')",'OBJECTID,osm_id2,name,historic,man_made,railway,building,landuse'):
    g=f.get('geometry'); p=f['properties']
    if g and g['type']=='Point': leads.append({'type':'node','id':str(p.get('osm_id2') or p['OBJECTID']),'lat':g['coordinates'][1],'lon':g['coordinates'][0],'tags':tags(p,('name','historic','man_made','railway','building','landuse'))})
n1=len(leads)
try:
    b=pull('OSM_NA_Buildings',f"(ruins IS NOT NULL AND ruins <> 'no') OR abandoned = 'yes' OR building = 'ruins' OR historic IN {H}",'OBJECTID,osm_id2,name,historic,ruins,abandoned,disused,building,man_made,railway',{'returnGeometry':'false','returnCentroid':'true','f':'json'})
except Exception as ex: b=[]; print('  buildings layer failed:',str(ex)[:100])
for f in b:
    a=f.get('attributes') or f.get('properties') or {}; c=f.get('centroid')
    if c: leads.append({'type':'way','id':str(a.get('osm_id2') or a.get('OBJECTID')),'center':{'lat':c['y'],'lon':c['x']},'tags':tags(a,('name','historic','ruins','abandoned','disused','building','man_made','railway'))})
if SKIP:
    n0=len(leads); leads=[e for e in leads if e['tags'].get('man_made') not in ('adit','mineshaft') and e['tags'].get('historic') not in ('mine','mine_shaft','adit')]
    print('left out',n0-len(leads),'mine entrances'); n1=min(n1,len(leads))
for k in KEYS:
    json.dump({'elements':leads},open(f'cache/osm/{k}_leads.json','w'),separators=(',',':')); print('wrote',f'cache/osm/{k}_leads.json',n1,'points +',len(leads)-n1,'buildings')
