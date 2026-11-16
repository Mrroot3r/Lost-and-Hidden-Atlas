import json,re,math,urllib.request,urllib.parse,time
from shapely.geometry import LineString, MultiLineString, box
from shapely.ops import linemerge, unary_union
BB=box(-75.35,41.2,-69.85,44.4)      # the first area: eastern New York and New England
OLDNY=box(-75.35,41.55,-73.05,44.45)  # the part of New York whose raw data came from Overpass (cache/osm/rail_old.json, canal.json)
# Whole states whose raw data came from tools/osm_layers.py and tools/ohm_state.py (cache/osm/<key>_rail.json, <key>_canal.json,
# <key>_ohm_rail.json, <key>_ohm_canal.json). To add a state: run those two tools for it, add its key here, run this file.
STATE_KEYS=['ny']
from shapely.geometry import Polygon
import os
_ST=json.load(open('build/states.json'))
def _poly(k): return unary_union([Polygon(list(zip(r[0::2],r[1::2]))).buffer(0) for r in _ST[k]])
STATE_POLY={k:_poly(k).buffer(0.01) for k in STATE_KEYS}
CLIP=unary_union([BB]+list(STATE_POLY.values()))
NEWAREA={k:STATE_POLY[k].difference(OLDNY) for k in STATE_KEYS}   # where a state's layer data is used; inside OLDNY the Overpass data stays
# The raw downloads are not in the repository. A fresh workspace therefore cannot rebuild everything, and does not have to:
# whatever raw data is missing, the lines already in build/lines.json are kept for that area, and only the areas whose raw
# files are present in cache/osm/ are rebuilt. With every raw file present the whole layer is rebuilt.
HAVE_OLD=all(os.path.exists('cache/osm/'+f) for f in ('rail_old.json','ohm_rail.json','ohm_canal.json','canal.json'))
HAVE=[k for k in STATE_KEYS if os.path.exists(f'cache/osm/{k}_rail.json')]
AREA=CLIP if (HAVE_OLD and len(HAVE)==len(STATE_KEYS)) else unary_union(([BB.difference(unary_union([NEWAREA[k] for k in STATE_KEYS if k not in HAVE]+[Polygon()]))] if HAVE_OLD else [])+[NEWAREA[k] for k in HAVE]+[Polygon()])
print('rebuilding:',('the first area ' if HAVE_OLD else '')+' '.join(HAVE) or 'nothing', '| kept from build/lines.json: everything else')
def geom(e): 
    g=e.get('geometry') or []
    return LineString([(p['lon'],p['lat']) for p in g]) if len(g)>1 else None
TROL=re.compile(r'electric|trolley|traction|international railway|rapid railway|rochester subway|street railroad|niagara gorge|great gorge|lockport (and|&) rochester|syracuse (and|&) eastern|lake shore (and|&) northern|rochester (and|&) sodus bay|jamestown, westfield|street railway|schenectady railway|hudson valley railway|albany (and|&) hudson|rutland railway light|new york state railways|southern new york railway|interurban|troy (and|&) new england|huckleberry|worcester consolidated|berkshire street|bay state',re.I)
TRAILHW={'cycleway','path','footway','track','bridleway','pedestrian'}
feats={}  # (kind,name,years)->[geoms]
def add(k,n,y,g):
    if g is None: return
    g=g.intersection(AREA)
    if g.is_empty: return
    feats.setdefault((k,n or '',y or ''),[]).append(g)
old_all=[]
_seen=set()
import os
def _ld(f): return json.load(open(f))['elements'] if os.path.exists(f) else []
def _state(kind):
    out=[]
    for k in STATE_KEYS:
        for e in _ld(f'cache/osm/{k}_{kind}.json'): e['_st']=k; out.append(e)
    return out
for e in _ld('cache/osm/rail_old.json')+_ld('cache/osm/rail_old_east.json')+_state('rail'):
    if e['type']!='way' or e['id'] in _seen: continue
    _seen.add(e['id'])
    t=e['tags']; g=geom(e)
    if g is None: continue
    if e.get('_st'):
        g=g.intersection(NEWAREA[e['_st']])
        if g.is_empty or g.length<0.0002: continue
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
for f in (_ma_trains() if HAVE_OLD else []):
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
# active rail from the federal rail network (cached in cache/narn_*.json)
def _narn(env):
    pth='cache/narn_'+env.replace(',','_').replace('-','m')+'.json'
    if os.path.exists(pth): return json.load(open(pth))
    cs=[]; off=0
    while True:
        u='https://services.arcgis.com/xOi1kZaI0eWDREZv/arcgis/rest/services/NTAD_North_American_Rail_Network_Lines/FeatureServer/0/query?'+urllib.parse.urlencode({'where':"NET<>'A' OR NET IS NULL",'geometry':env,'geometryType':'esriGeometryEnvelope','inSR':4326,'spatialRel':'esriSpatialRelIntersects','outFields':'NET','outSR':4326,'geometryPrecision':5,'resultOffset':off,'resultRecordCount':2000,'f':'geojson'})
        fs=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'x'}),timeout=180)).get('features',[])
        for f in fs:
            if not f.get('geometry'): continue
            c=f['geometry']['coordinates']; cs+= [c] if f['geometry']['type']=='LineString' else c
        off+=len(fs)
        if len(fs)<2000: break
    json.dump(cs,open(pth,'w')); return cs
act=[LineString(c) for c in _narn('-75.35,41.2,-69.85,44.4') if len(c)>1]
for k in STATE_KEYS:
    w,s_,e,n=STATE_POLY[k].bounds
    act+=[LineString(c) for c in _narn(f'{w:.2f},{s_:.2f},{e:.2f},{n:.2f}') if len(c)>1]
print('active rail segs',len(act))
actu=unary_union(act).intersection(AREA) if act else None
if actu is not None: feats[('rr','Rail line in use','')]=[actu]
actbuf=actu.buffer(0.00035) if actu is not None else None
oldbuf=unary_union(old_all).buffer(0.0007)
n_ohm=0
_oseen=set()
for e in _ld('cache/osm/ohm_rail.json')+[x for k in STATE_KEYS for x in _ld(f'cache/osm/{k}_ohm_rail.json')]:
    if e['id'] in _oseen: continue
    _oseen.add(e['id'])
    t=e['tags']; g=geom(e)
    if g is None or not t.get('end_date'): continue
    if t.get('railway') not in('rail','tram','light_rail','narrow_gauge','abandoned','funicular'): continue
    out=g.difference(oldbuf)
    if actbuf is not None and not out.is_empty: out=out.difference(actbuf)
    if out.is_empty or out.length<0.004: continue
    y=(t.get('start_date','?')[:4]+'–'+t['end_date'][:4])
    add('tr' if (t.get('railway') in('tram','light_rail') or TROL.search(t.get('name',''))) else 'ab',t.get('name',''),y,out); n_ohm+=1
print('ohm rail segments added',n_ohm)
# canals
can_old=[]; can_now=[]
_cseen=set()
for e in _ld('cache/osm/ohm_canal.json')+[x for k in STATE_KEYS for x in _ld(f'cache/osm/{k}_ohm_canal.json')]:
    if e['id'] in _cseen: continue
    _cseen.add(e['id'])
    t=e['tags']; g=geom(e)
    if g is None: continue
    if re.search(r'Creek|Run$|River|Brook|Croton|Aqueduct|raceway|Gracht|Graft|Trent',t.get('name','')) and 'Canal' not in t.get('name',''): continue
    n=t.get('name',''); sd=t.get('start_date','')[:4]; ed=t.get('end_date','')[:4]
    y=(sd or '?')+'–'+ed if ed else (('from '+sd) if sd else '')
    cur= ('Barge' in n) or (not ed and n in('Champlain Canal','Black River Canal','') )
    if n=='Champlain Canal' and not ed: cur=False; k='co'   # OHM Champlain is the old canal alignment
    k='cn' if ('Barge' in n) else 'co'
    add(k,n or 'Old canal',y,g)
    if k=='co': can_old.append(g)
    else: can_now.append(g)
cbuf=unary_union(can_old).buffer(0.0006) if can_old else None
nbuf=unary_union(can_now).buffer(0.0008) if can_now else None
for e in _ld('cache/osm/canal.json')+_ld('cache/osm/canal_ma.json')+_state('canal'):
    if e['type']!='way': continue
    t=e['tags']; g=geom(e)
    if g is not None and e.get('_st'):
        g=g.intersection(NEWAREA[e['_st']])
        if g.is_empty: continue
    if g is None or t.get('waterway') in('lock_gate','river') or t.get('tunnel'): continue
    n=t.get('name','')
    if re.search(r'Spillway|Plunge|Brook|River|Creek|Avenue|Road|Shandaken',n): continue
    oldish= t.get('waterway') in('dismantled','derelict_canal') or 'disused:waterway' in t or 'abandoned:waterway' in t or t.get('disused')=='yes' or t.get('historic')=='canal' or re.search(r'Enlarged|Old |Delaware and Hudson|Sidecut|Feeder|Chenango|Genesee Valley|Chemung|Crooked Lake|Junction Canal|Black River Canal|Oneida Lake Canal|Clinton.s Ditch|Abandoned|Original Erie|Former |Historic |Inland Lock|Blackstone Canal|Middlesex Canal|Farmington Canal|Hampshire and Hampden|New Haven and Northampton',n)
    if oldish:
        if cbuf is not None:
            g=g.difference(cbuf)
            if g.is_empty or g.length<0.002: continue
        add('co',n or 'Old canal','',g)
    elif t.get('waterway')=='canal' and n in('Erie Canal','Champlain Canal','Oswego Canal','Cayuga-Seneca Canal','Cayuga and Seneca Canal','Cayuga–Seneca Canal','New York State Barge Canal'):
        if nbuf is not None: g=g.difference(nbuf)
        if g.is_empty or g.length<0.002: continue
        add('cn',n+' (Barge Canal, in use)','',g)
    elif t.get('waterway')=='canal' and 'Canal' in n and g.centroid.x>-73.3 and g.centroid.y<42.95:
        add('cn',n,'',g)
for kk in ('ab','di','tr','tl','co'):
    un=feats.get((kk,'',''))
    named=[g for (k2,n2,y2),gs in feats.items() if k2 in('ab','di','tr','tl','co') and n2 for g in gs]
    if un and named:
        nb=unary_union(named).buffer(0.00006); feats[(kk,'','')]=[unary_union(un).difference(nb)]
# keep what was already built for every area that was not rebuilt this time
if not AREA.equals(CLIP) and os.path.exists('build/lines.json'):
    kept=0
    for f in json.load(open('build/lines.json')):
        ls=[LineString([(x,y) for y,x in pp]) for pp in f['c'] if len(pp)>1]
        if not ls: continue
        g=MultiLineString(ls).difference(AREA)
        if not g.is_empty: feats.setdefault((f['k'],f['n'],f['y']),[]).append(g); kept+=1
    print('kept',kept,'features from the existing build/lines.json outside the rebuilt area')
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
