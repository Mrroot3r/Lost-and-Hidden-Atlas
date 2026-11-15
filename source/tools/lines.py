import json,re,math,urllib.request,urllib.parse,time
from shapely.geometry import LineString, MultiLineString, box
from shapely.ops import linemerge, unary_union
BB=box(-75.35,41.2,-69.85,44.4)
def geom(e): 
    g=e.get('geometry') or []
    return LineString([(p['lon'],p['lat']) for p in g]) if len(g)>1 else None
TROL=re.compile(r'electric|trolley|traction|street railway|schenectady railway|hudson valley railway|albany (and|&) hudson|rutland railway light|new york state railways|southern new york railway|interurban|troy (and|&) new england|huckleberry|worcester consolidated|berkshire street|bay state',re.I)
TRAILHW={'cycleway','path','footway','track','bridleway','pedestrian'}
feats={}  # (kind,name,years)->[geoms]
def add(k,n,y,g):
    if g is None: return
    g=g.intersection(BB)
    if g.is_empty: return
    feats.setdefault((k,n or '',y or ''),[]).append(g)
old_all=[]
_seen=set()
import os
def _ld(f): return json.load(open(f))['elements'] if os.path.exists(f) else []
for e in _ld('cache/osm/rail_old.json')+_ld('cache/osm/rail_old_east.json'):
    if e['type']!='way' or e['id'] in _seen: continue
    _seen.add(e['id'])
    t=e['tags']; g=geom(e)
    if g is None: continue
    sub=t.get('abandoned:railway') or t.get('disused:railway') or t.get('razed:railway') or t.get('historic:railway') or t.get('railway:historic') or ''
    if sub in('station','roundhouse','carbarn','platform','turntable','yard'): continue
    if t.get('building') or t.get('area')=='yes': continue
    rname=t.get('old_name') or t.get('abandoned:name') or t.get('railway:name') or t.get('historic:name') or t.get('old_railway_operator') or t.get('old_operator') or ''
    name=t.get('name') or rname or t.get('operator') or ''
    hw=t.get('highway','')
    trol= sub in('tram','light_rail') or bool(TROL.search(name+' '+rname+' '+t.get('description','')))
    dis = t.get('railway')=='disused' or 'disused:railway' in t
    if hw in TRAILHW: k='tl'
    elif trol: k='tr'
    elif dis: k='di'
    else: k='ab'
    label=name
    if hw in TRAILHW and rname and rname!=name: label=f'{name} (former {rname})' if name else rname
    add(k,label,'',g); old_all.append(g)
# Massachusetts: the state's own rail inventory (MassGIS Trains), which carries abandoned, never-finished and trolley lines
def _ma_trains():
    pth='cache/ma_trains.json'
    if os.path.exists(pth): return json.load(open(pth))
    out=[]; off=0
    while True:
        u='https://services1.arcgis.com/hGdibHYSPO59RG1h/arcgis/rest/services/Trains_gdb/FeatureServer/0/query?'+urllib.parse.urlencode({'where':'TYPE<>1 AND TYPE<>9','outFields':'TYPE,LINE_BRNCH,RAIL_TRL,DATE_ABAND','outSR':4326,'geometryPrecision':5,'resultOffset':off,'resultRecordCount':1000,'orderByFields':'OBJECTID','f':'geojson'})
        fs=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'x'}),timeout=120)).get('features',[])
        out+=fs; off+=len(fs)
        if len(fs)<1000: break
    json.dump(out,open(pth,'w')); return out
def _tc(n):
    n=(n or '').strip().title().replace(' Rr',' Railroad').replace(' Br',' Branch').replace('Ind Trk','Industrial Track').replace(' Trk',' Track').replace('&',' & ').replace('  ',' ')
    return re.sub(r'\bMa\b','MA',n)
n_ma=0
for f in _ma_trains():
    g=f.get('geometry'); p=f['properties']
    if not g: continue
    cs=[g['coordinates']] if g['type']=='LineString' else g['coordinates']
    nm=p.get('LINE_BRNCH') or ''; trl=p.get('RAIL_TRL'); t=p.get('TYPE'); y=p.get('DATE_ABAND')
    never=bool(re.search(r'NOT COMP|NEVER',nm))
    base=_tc(re.sub(r'-?NOT COMP|-?NEVER OP','',nm))
    base={'Southern Ne':'Southern New England Railway','Ma Cntrl Rt':'Massachusetts Central','MA Cntrl Rt':'Massachusetts Central','Hampden Railroad':'Hampden Railroad'}.get(base,base)
    if trl: k='tl'; label=_tc(trl)+(f' (former {base})' if base else '')
    elif re.search(r'TROLLEY|TRANSIT',nm): k='tr'; label='Old trolley or transit line' if 'TRANSIT' in nm or nm=='TROLLEY' else base
    elif t==2: k='di'; label=base
    else: k='ab'; label=base+(' (never finished)' if never else '')
    for c in cs:
        if len(c)>1:
            ln=LineString(c); add(k,label,(f'abandoned {y}' if y and y>1800 and not never else ''),ln); old_all.append(ln); n_ma+=1
print('MA rail segments',n_ma)
oldbuf=unary_union(old_all).buffer(0.0007)
n_ohm=0
for e in json.load(open('cache/osm/ohm_rail.json'))['elements']:
    t=e['tags']; g=geom(e)
    if g is None or not t.get('end_date'): continue
    if t.get('railway') not in('rail','tram','light_rail','narrow_gauge','abandoned','funicular'): continue
    out=g.difference(oldbuf)
    if out.is_empty or out.length<0.004: continue
    y=(t.get('start_date','?')[:4]+'–'+t['end_date'][:4])
    add('tr' if (t.get('railway') in('tram','light_rail') or TROL.search(t.get('name',''))) else 'ab',t.get('name',''),y,out); n_ohm+=1
print('ohm rail segments added',n_ohm)
# canals
can_old=[]
for e in json.load(open('cache/osm/ohm_canal.json'))['elements']:
    t=e['tags']; g=geom(e)
    if g is None: continue
    n=t.get('name',''); sd=t.get('start_date','')[:4]; ed=t.get('end_date','')[:4]
    y=(sd or '?')+'–'+ed if ed else (('from '+sd) if sd else '')
    cur= ('Barge' in n) or (not ed and n in('Champlain Canal','Black River Canal','') )
    if n=='Champlain Canal' and not ed: cur=False; k='co'   # OHM Champlain is the old canal alignment
    k='cn' if ('Barge' in n) else 'co'
    add(k,n or 'Old canal',y,g)
    if k=='co': can_old.append(g)
cbuf=unary_union(can_old).buffer(0.0006) if can_old else None
for e in json.load(open('cache/osm/canal.json'))['elements']+_ld('cache/osm/canal_ma.json'):
    if e['type']!='way': continue
    t=e['tags']; g=geom(e)
    if g is None or t.get('waterway') in('lock_gate','river') or t.get('tunnel'): continue
    n=t.get('name','')
    if re.search(r'Spillway|Plunge|Brook|River|Creek|Avenue|Road|Shandaken',n): continue
    oldish= t.get('waterway') in('dismantled','derelict_canal') or 'disused:waterway' in t or 'abandoned:waterway' in t or t.get('disused')=='yes' or t.get('historic')=='canal' or re.search(r'Enlarged|Old |Delaware and Hudson|Sidecut|Feeder|Chenango|Inland Lock|Blackstone Canal|Middlesex Canal|Farmington Canal|Hampshire and Hampden|New Haven and Northampton',n)
    if oldish:
        if cbuf is not None:
            g=g.difference(cbuf)
            if g.is_empty or g.length<0.002: continue
        add('co',n or 'Old canal','',g)
    elif t.get('waterway')=='canal' and n in('Erie Canal','Champlain Canal'):
        add('cn',n+' (Barge Canal, in use)','',g)
    elif t.get('waterway')=='canal' and 'Canal' in n and g.centroid.x>-73.3 and g.centroid.y<42.95:
        add('cn',n,'',g)
# active rail from the federal rail network
act=[]; off=0
while True:
    u='https://services.arcgis.com/xOi1kZaI0eWDREZv/arcgis/rest/services/NTAD_North_American_Rail_Network_Lines/FeatureServer/0/query?'+urllib.parse.urlencode({'where':"NET<>'A' OR NET IS NULL",'geometry':'-75.35,41.2,-69.85,44.4','geometryType':'esriGeometryEnvelope','inSR':4326,'spatialRel':'esriSpatialRelIntersects','outFields':'RROWNER1,SUBDIV,NET','outSR':4326,'f':'geojson','resultOffset':off,'resultRecordCount':2000})
    j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'x'}),timeout=120)); fs=j.get('features',[])
    for f in fs:
        if not f.get('geometry'): continue
        c=f['geometry']['coordinates']; gs=[c] if f['geometry']['type']=='LineString' else c
        for cc in gs:
            if len(cc)>1: act.append(LineString(cc))
    off+=len(fs)
    if len(fs)<2000: break
print('active rail segs',len(act))
if act: feats[('rr','Rail line in use','')]=[unary_union(act).intersection(BB)]
out=[]; km=0
def parts(g):
    if g.is_empty: return []
    if g.geom_type=='LineString': return [g]
    if g.geom_type in('MultiLineString','GeometryCollection'): return [p for x in g.geoms for p in parts(x)]
    return []
from collections import Counter
kc=Counter()
for (k,n,y),gs in feats.items():
    m=unary_union(gs); m=linemerge(m) if m.geom_type=='MultiLineString' else m
    m=m.simplify(0.00007 if k!='rr' else 0.00015)
    ps=[p for p in parts(m) if p.length>(0.0006 if k!='rr' else 0.002)]
    if not ps: continue
    L=sum(p.length for p in ps)*95; kc[k]+=L
    out.append({'k':k,'n':n,'y':y,'c':[[[round(yy,5),round(xx,5)] for xx,yy in p.coords] for p in ps]})
s=json.dumps(out,separators=(',',':'),ensure_ascii=False)
open('build/lines.json','w').write(s)
print(len(out),'features',len(s),'bytes',{k:round(v) for k,v in kc.items()})
