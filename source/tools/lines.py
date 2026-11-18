import json,re,math,urllib.request,urllib.parse,time
from shapely.geometry import LineString, MultiLineString, box
from shapely.ops import linemerge, unary_union
BB=box(-75.35,41.2,-69.85,44.4)      # the first area: eastern New York and New England
OLDNY=box(-75.35,41.55,-73.05,44.45)  # the part of New York whose raw data came from Overpass (cache/osm/rail_old.json, canal.json)
# Whole states whose raw data came from tools/osm_layers.py and tools/ohm_state.py (cache/osm/<key>_rail.json, <key>_canal.json,
# <key>_ohm_rail.json, <key>_ohm_canal.json). To add a state: run those two tools for it, add its key here, run this file.
STATE_KEYS=['ny','ct','ri','vt','nh','me','nj','pa']
from shapely.geometry import Polygon
import os
_ST=json.load(open('build/states.json'))
def _poly(k): return unary_union([Polygon(list(zip(r[0::2],r[1::2]))).buffer(0) for r in _ST[k]])
STATE_POLY={k:_poly(k).buffer(0.01) for k in STATE_KEYS}
CLIP=unary_union([BB]+list(STATE_POLY.values()))
NEWAREA={k:STATE_POLY[k].difference(OLDNY) for k in STATE_KEYS}   # where a state's layer data is used; inside OLDNY the Overpass data stays
# Every state whose lines the Atlas holds. Massachusetts is not in STATE_KEYS because its old lines come from the state's own
# rail inventory, not from a layer download. Each piece of line is filed under one of these (see "which state" at the end).
LINE_STATES=STATE_KEYS+['ma']
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
TROL=re.compile(r'electric|trolley|traction|international railway|rapid railway|rochester subway|street railroad|niagara gorge|great gorge|lockport (and|&) rochester|syracuse (and|&) eastern|lake shore (and|&) northern|rochester (and|&) sodus bay|jamestown, westfield|street railway|schenectady railway|hudson valley railway|albany (and|&) hudson|rutland railway light|new york state railways|southern new york railway|interurban|troy (and|&) new england|huckleberry|worcester consolidated|berkshire street|bay state|pittsburgh, harmony|wilkes-barre (and|&) hazleton|west penn railway|laurel line|lackawanna (and|&) wyoming valley|atlantic shore line|north jersey rapid transit|njrt',re.I)
# The six names on the last line were each checked in the line's Wikipedia article (November 2026): all electric interurban or trolley lines.
# Two things the pattern catches that are not trolley lines: a works siding named for General Electric, and the International
# Railway in northern Maine (the pattern means the Buffalo and Niagara Falls company of that name).
def _nottrol(name,g): return name.strip().lower() in('general electric','general electric company') or (name.strip().lower()=='international railway' and g.centroid.x>-75)
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
# The layer files of neighbouring states overlap, because each is a box round its state. So a way is taken once, and what is
# kept of it is everything inside any state being rebuilt (NEWALL), not only the part inside the state whose file it came from.
# A way the first Overpass downloads already hold is taken from there: that copy is whole and has more tags.
# Known gap, left as it was: a railway mapped as a route relation (a negative id) comes as several pieces under one id, and
# the id check below keeps only the first. The pieces mostly repeat ordinary ways, but about 1,700 km in New York and 800 km
# in Pennsylvania lie under no abandoned way: partly real (the old line is a trail or a road now), partly track still in use
# (most of the West Shore). Taking them would need the same cut against the railroads in use that OpenHistoricalMap lines get.
NEWALL=unary_union(list(NEWAREA.values())+[Polygon()])
_first=_ld('cache/osm/rail_old.json')+_ld('cache/osm/rail_old_east.json')
_over={str(e['id']) for e in _first if e['type']=='way'}
for e in _first+_state('rail'):
    if e['type']!='way' or e['id'] in _seen: continue
    if e.get('_st') and e.get('osm') in _over: continue
    _seen.add(e['id'])
    t=e['tags']; g=geom(e)
    if g is None: continue
    if e.get('_st'):
        g=g.intersection(NEWALL)
        if g.is_empty or g.length<0.0002: continue
    sub=t.get('abandoned:railway') or t.get('disused:railway') or t.get('razed:railway') or t.get('historic:railway') or t.get('railway:historic') or ''
    if sub in('station','roundhouse','carbarn','platform','turntable','yard'): continue
    if t.get('building') or t.get('area')=='yes': continue
    rname=t.get('old_name') or t.get('abandoned:name') or t.get('railway:name') or t.get('historic:name') or t.get('old_railway_operator') or t.get('old_operator') or ''
    name=t.get('name') or rname or t.get('operator') or ''
    hw=t.get('highway','')
    trol= sub in('tram','light_rail') or (bool(TROL.search(name+' '+rname+' '+t.get('description',''))) and not _nottrol(name,g))
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
        for go in range(5):          # the service answers 502 now and then on a big state: wait and ask for the same page again
            try: fs=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'x'}),timeout=180)).get('features',[]); break
            except Exception as ex:
                if go==4: raise
                print('  rail network: asking again,',str(ex)[:60],flush=True); time.sleep(8*(go+1))
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
import resource
_T0=time.time()
def _at(what): print(f'  {what}: {time.time()-_T0:.0f} s, {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss//1024} MB',flush=True)   # where the time and memory go
actu=unary_union(act).intersection(AREA) if act else None
_at('railroads in use joined')
if actu is not None: feats[('rr','Rail line in use','')]=[actu]
from shapely.strtree import STRtree
def _flat(g): return [g] if g.geom_type=='LineString' else [x for q in getattr(g,'geoms',[]) for x in _flat(q)]
class Band:
    """The ground within r of any of a great many lines. Buffering them all in one go needed more memory than a session has
    once Pennsylvania was added (the run was simply killed), so the band is only ever built round the lines near the piece
    being cut. The result is the same."""
    def __init__(self,geoms,r):
        self.g=[x for g in geoms if g is not None and not g.is_empty for x in _flat(g)]; self.r=r; self.t=STRtree(self.g) if self.g else None
    def cut(self,g):
        if self.t is None or g.is_empty: return g
        ix=self.t.query(g.buffer(self.r),predicate='intersects')
        return g.difference(unary_union([self.g[i] for i in ix]).buffer(self.r)) if len(ix) else g
actbuf=Band([actu],0.00035) if actu is not None else None
_at('band round the railroads in use')
oldbuf=Band(old_all,0.0007)
_at('band round the old lines')
n_ohm=0
_oseen=set()
for e in _ld('cache/osm/ohm_rail.json')+[x for k in STATE_KEYS for x in _ld(f'cache/osm/{k}_ohm_rail.json')]:
    if e['id'] in _oseen: continue
    _oseen.add(e['id'])
    t=e['tags']; g=geom(e)
    if g is None or not t.get('end_date'): continue
    if t.get('railway') not in('rail','tram','light_rail','narrow_gauge','abandoned','funicular'): continue
    out=oldbuf.cut(g)
    if actbuf is not None and not out.is_empty: out=actbuf.cut(out)
    if out.is_empty or out.length<0.004: continue
    y=(t.get('start_date','?')[:4]+'–'+t['end_date'][:4])
    add('tr' if (t.get('railway') in('tram','light_rail') or (TROL.search(t.get('name','')) and not _nottrol(t.get('name',''),g))) else 'ab',t.get('name',''),y,out); n_ohm+=1
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
    if not ed and re.search(r'Point Pleasant|Cape May',n): continue     # in use today (New Jersey Intracoastal Waterway): OpenStreetMap supplies it
    y=(sd or '?')+'–'+ed if ed else (('from '+sd) if sd else '')
    cur= ('Barge' in n) or (not ed and n in('Champlain Canal','Black River Canal','') )
    if n=='Champlain Canal' and not ed: cur=False; k='co'   # OHM Champlain is the old canal alignment
    k='cn' if ('Barge' in n) else 'co'
    add(k,n or 'Old canal',y,g)
    if k=='co': can_old.append(g)
    else: can_now.append(g)
cbuf=unary_union(can_old).buffer(0.0006) if can_old else None
nbuf=unary_union(can_now).buffer(0.0008) if can_now else None
# Canals from the layer files, taken once each like the railways above. Outside New York a layer file gives only a name and
# waterway=canal, so the kind comes from the name: the towpath canals listed in OLDCANAL are old canals (each checked in its
# Wikipedia article, November 2026: Delaware Canal, a state park since 1940; Delaware and Raritan, worked until 1932; Morris,
# abandoned 1924; Lehigh, until 1931 and in part the 1940s; Schuylkill, until 1931; Union, closed in the 1880s; Enfield Falls,
# closed to navigation; Bald Eagle Crosscut, part of the state's West Branch canal), and any other named canal is shown as
# in use, which is what OpenStreetMap says of it.
_cfirst=_ld('cache/osm/canal.json')+_ld('cache/osm/canal_ma.json')
_cover={str(e['id']) for e in _cfirst if e['type']=='way'}; _cs=set()
from shapely.prepared import prep
_NYP=prep(STATE_POLY['ny']) if 'ny' in STATE_POLY else None
OLDCANAL=r'|Delaware Canal|Delaware and Raritan|Morris Canal|Lehigh Canal|Schuylkill Canal|Union Canal|P[ew]nnsylvania Canal|Bald Eagle Crosscut|Chester County Canal|Enfield Falls|Cumberland and Oxford|Erie Extension'
for e in _cfirst+_state('canal'):
    if e['type']!='way': continue
    if e.get('_st'):          # a canal mapped as a relation (the Erie Canal) comes as several pieces under one id: only an exact repeat is a duplicate
        q=e.get('geometry') or [{}]; sig=(e['id'],len(q),q[0].get('lat'),q[0].get('lon'),q[-1].get('lat'),q[-1].get('lon'))
        if e.get('osm') in _cover or sig in _cs: continue
        _cs.add(sig)
    t=e['tags']; g=geom(e)
    if g is not None and e.get('_st'):
        g=g.intersection(NEWALL)
        if g.is_empty: continue
    if g is None or t.get('waterway') in('lock_gate','river') or t.get('tunnel'): continue
    n=t.get('name','').replace('Pwnnsylvania','Pennsylvania')      # as OpenStreetMap spells one stretch
    if re.search(r'Spillway|Plunge|Brook|River|Creek|Avenue|Road|Shandaken',n): continue
    oldish= t.get('waterway') in('dismantled','derelict_canal') or 'disused:waterway' in t or 'abandoned:waterway' in t or t.get('disused')=='yes' or t.get('historic')=='canal' or re.search(r'Enlarged|Old |Delaware and Hudson|Sidecut|Feeder|Chenango|Genesee Valley|Chemung|Crooked Lake|Junction Canal|Black River Canal|Oneida Lake Canal|Clinton.s Ditch|Abandoned|Original Erie|Former |Historic |Inland Lock|Blackstone Canal|Middlesex Canal|Farmington Canal|Hampshire and Hampden|New Haven and Northampton'+OLDCANAL,n)
    if oldish:
        if cbuf is not None:
            g=g.difference(cbuf)
            if g.is_empty or g.length<0.002: continue
        add('co',n or 'Old canal','',g)
    elif t.get('waterway')=='canal' and n in('Erie Canal','Champlain Canal','Oswego Canal','Cayuga-Seneca Canal','Cayuga and Seneca Canal','Cayuga–Seneca Canal','New York State Barge Canal'):
        if nbuf is not None: g=g.difference(nbuf)
        if g.is_empty or g.length<0.002: continue
        add('cn',n+' (Barge Canal, in use)','',g)
    elif t.get('waterway')=='canal' and 'Canal' in n and ((g.centroid.x>-73.3 and g.centroid.y<42.95) or (e.get('_st') and not _NYP.contains(g.centroid))):
        add('cn',n,'',g)
_at('canals')
_named=Band([g for (k2,n2,y2),gs in feats.items() if k2 in('ab','di','tr','tl','co') and n2 for g in gs],0.00006)
for kk in ('ab','di','tr','tl','co'):         # an unnamed piece lying under a named line is the same track mapped twice
    un=feats.get((kk,'',''))
    if un and _named.t is not None: feats[(kk,'','')]=[x for x in (_named.cut(g) for g in un) if not x.is_empty]
# keep what was already built for every area that was not rebuilt this time
if not AREA.equals(CLIP) and os.path.exists('build/lines.json'):
    kept=0
    for f in json.load(open('build/lines.json')):
        ls=[LineString([(x,y) for y,x in pp]) for pp in f['c'] if len(pp)>1]
        if not ls: continue
        g=MultiLineString(ls).difference(AREA)
        if not g.is_empty: feats.setdefault((f['k'],f['n'],f['y']),[]).append(g); kept+=1
    print('kept',kept,'features from the existing build/lines.json outside the rebuilt area')
# Which state each piece lies in. The hosted copy fetches the lines one state at a time (tools/lines_split.py cuts the file
# up at build time), so every feature carries "s", the key of its state, and a line that crosses a border is two features with
# the same name. A piece is filed whole under the state its middle is in; one that is in none of them (a bridge over a border
# river, a sliver across the Canadian line) goes to the nearest.
_LP={k:_poly(k) for k in LINE_STATES}; _LPP={k:prep(v) for k,v in _LP.items()}
def which(p):
    m=p.interpolate(0.5,normalized=True)
    for k in LINE_STATES:
        if _LPP[k].contains(m): return k
    return min(LINE_STATES,key=lambda k:_LP[k].distance(m))
_at('unnamed pieces under named lines removed')
out=[]; km=0
def parts(g):
    if g.is_empty: return []
    if g.geom_type=='LineString': return [g]
    if g.geom_type in('MultiLineString','GeometryCollection'): return [p for x in g.geoms for p in parts(x)]
    return []
from collections import Counter
kc=Counter(); skm={}
for (k,n,y),gs in feats.items():
    m=unary_union(gs); m=linemerge(m) if m.geom_type=='MultiLineString' else m
    m=m.simplify(0.00007 if k!='rr' else 0.00015)
    ps=[p for p in parts(m) if p.length>(0.0006 if k!='rr' else 0.002)]
    if not ps: continue
    L=sum(p.length for p in ps)*95; kc[k]+=L
    by={}
    for p in ps: by.setdefault(which(p),[]).append(p)
    for st in sorted(by):
        skm.setdefault(st,Counter())[k]+=sum(p.length for p in by[st])*95
        out.append({'k':k,'n':n,'y':y,'s':st,'c':[[[round(yy,5),round(xx,5)] for xx,yy in p.coords] for p in by[st]]})
s=json.dumps(out,separators=(',',':'),ensure_ascii=False)
open('build/lines.json','w').write(s)
print(len(out),'features',len(s),'bytes',{k:round(v) for k,v in kc.items()})
print('kilometres in each state (roughly):')
for st in sorted(skm): print('  ',st,{k:round(v) for k,v in sorted(skm[st].items())})
