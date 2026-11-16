#!/usr/bin/env python3
"""Download OpenStreetMap's old railways, canals and mapped ruins for one whole state or province, from the
copies of OpenStreetMap that Esri hosts as feature layers (updated daily). Use this when Overpass cannot be reached,
which has been the usual case from cloud machines.

   python3 tools/osm_layers.py ny            writes cache/osm/ny_rail.json, ny_canal.json and ny_leads.json

The files have the same shape as an Overpass download ({"elements":[{type,id,tags,geometry}]}), so tools/lines.py
and tools/leads.py read them with the code they already had. Then list the key in STATE_KEYS at the top of both.

What this route loses compared with Overpass, measured on the Capital Region download of November 2026:
  - a way tagged only with a prefix (abandoned:railway=rail and no railway=abandoned) is missing: about 5% by length;
  - old_name, abandoned:name and similar tags are missing, so a line is labelled by its name or operator only;
  - a rail trail is recognised by looking the way up in the highways layer (same OpenStreetMap id), not by its tags.
Data is OpenStreetMap, © OpenStreetMap contributors, ODbL."""
import sys,os,json,time,math,urllib.request,urllib.parse
if len(sys.argv)<2: sys.exit(__doc__)
KEY=sys.argv[1]; RINGS=json.load(open('build/states.json'))[KEY]
xs=[r[i] for r in RINGS for i in range(0,len(r),2)]; ys=[r[i+1] for r in RINGS for i in range(0,len(r),2)]
W,E,S,N=min(xs)-0.02,max(xs)+0.02,min(ys)-0.02,max(ys)+0.02
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
def strips(n):
    for c in range(n): yield W+(E-W)*c/n, W+(E-W)*(c+1)/n
def pull(layer,where,fields,extra=None,nstrips=6):
    """Every feature matching `where` inside the state's box, strip by strip, page by page."""
    out={}
    for w,e in strips(nstrips):
        off=0
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
def lines_to_elements(fs,tagf):
    els=[]
    for f in fs:
        g=f.get('geometry'); p=f['properties']
        if not g: continue
        parts=[g['coordinates']] if g['type']=='LineString' else g['coordinates'] if g['type']=='MultiLineString' else []
        oid=str(p.get('osm_id2') or p.get('osm_id') or p['OBJECTID'])
        for n,c in enumerate(parts):
            if len(c)<2: continue
            els.append({'type':'way','id':oid if n==0 else f'{oid}:{n}','osm':oid,'tags':tagf(p),'geometry':[{'lat':y,'lon':x} for x,y in c]})
    return els
def tags(p,keys): return {k:p[k] for k in keys if p.get(k) not in (None,'')}
TRAIL="('cycleway','path','footway','track','bridleway','pedestrian')"
# ---- old railways ----
print(KEY,'old railways')
rail=pull('OSM_NA_Railways',"railway IN ('abandoned','disused','razed','dismantled')",'OBJECTID,osm_id2,name,operator,description,railway')
els=lines_to_elements(rail,lambda p:tags(p,('railway','name','operator','description')))
ids=sorted({e['osm'] for e in els if not e['osm'].startswith('-')})
print('  ',len(els),'line parts from',len(ids),'ways; looking them up in the highways layer for rail trails')
hw={}
for k in range(0,len(ids),150):
    chunk=ids[k:k+150]
    j=post('OSM_NA_Highways',{'where':"osm_id2 IN ("+','.join("'"+i+"'" for i in chunk)+") AND highway IN "+TRAIL,'outFields':'osm_id2,highway,name','returnGeometry':'false','f':'json'})
    for f in j.get('features',[]): hw[f['attributes']['osm_id2']]=(f['attributes']['highway'],f['attributes'].get('name') or '')
    if (k//150)%20==0: print('   trail lookup',k,'of',len(ids),len(hw),'found',flush=True)
for e in els:
    h=hw.get(e['osm'])
    if h:
        e['tags']['highway']=h[0]
        if h[1] and not e['tags'].get('name'): e['tags']['name']=h[1]
json.dump({'elements':els},open(f'cache/osm/{KEY}_rail.json','w'),separators=(',',':')); print('wrote',f'cache/osm/{KEY}_rail.json',len(els),'parts,',len(hw),'are trails')
# ---- canals ----
print(KEY,'canals')
can=pull('OSM_NA_Waterways',"waterway IN ('canal','derelict_canal','dismantled','disused','lock')",'OBJECTID,osm_id2,name,waterway,tunnel',nstrips=4)
els=lines_to_elements(can,lambda p:tags(p,('waterway','name','tunnel')))
json.dump({'elements':els},open(f'cache/osm/{KEY}_canal.json','w'),separators=(',',':')); print('wrote',f'cache/osm/{KEY}_canal.json',len(els))
# ---- mapped ruins and other leads ----
print(KEY,'leads')
H="('ruins','archaeological_site','mine','mine_shaft','adit','kiln','lime_kiln','charcoal_pile','industrial','farm','railway_station','railway','aqueduct','lock','canal','fort','ghost_town','locomotive','quarry')"
leads=[]
def pts(fs,keys):
    for f in fs:
        g=f.get('geometry'); p=f['properties']
        if not g or g['type']!='Point': continue
        leads.append({'type':'node','id':str(p.get('osm_id2') or p['OBJECTID']),'lat':g['coordinates'][1],'lon':g['coordinates'][0],'tags':tags(p,keys)})
pts(pull('OSM_NA_POIs',f"historic IN {H} OR man_made IN ('kiln','adit','mineshaft')",'OBJECTID,osm_id2,name,historic,man_made,railway,building,landuse',nstrips=4),('name','historic','man_made','railway','building','landuse'))
n1=len(leads)
try:
    b=pull('OSM_NA_Buildings',f"(ruins IS NOT NULL AND ruins <> 'no') OR abandoned = 'yes' OR building = 'ruins' OR historic IN {H}",'OBJECTID,osm_id2,name,historic,ruins,abandoned,disused,building,man_made,railway',{'returnGeometry':'false','returnCentroid':'true','f':'json'},nstrips=4)
except Exception as ex: b=[]; print('  buildings layer failed:',str(ex)[:100])
for f in b:
    a=f.get('attributes') or f.get('properties') or {}; c=f.get('centroid')
    if c: leads.append({'type':'way','id':str(a.get('osm_id2') or a.get('OBJECTID')),'center':{'lat':c['y'],'lon':c['x']},'tags':tags(a,('name','historic','ruins','abandoned','disused','building','man_made','railway'))})
json.dump({'elements':leads},open(f'cache/osm/{KEY}_leads.json','w'),separators=(',',':')); print('wrote',f'cache/osm/{KEY}_leads.json',n1,'points +',len(leads)-n1,'buildings')
