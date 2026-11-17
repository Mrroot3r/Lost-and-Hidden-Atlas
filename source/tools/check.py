#!/usr/bin/env python3
"""Checks a repository clone before a change is proposed. No network, standard library only.
   python3 source/tools/check.py [path-to-repo] [--sources]
--sources: check the place lists, the ledger and the privacy rule only, and skip "the built site matches the sources".
That is for a branch that carries sources alone; GitHub builds the site and runs the full check (tools/ci_build.sh).
Exit code 1 on any error. Warnings are for a person to read."""
import sys,os,re,json,glob,importlib
SRC_ONLY='--sources' in sys.argv; _args=[a for a in sys.argv[1:] if not a.startswith('--')]
REPO=os.path.abspath(_args[0] if _args else os.path.join(os.path.dirname(__file__),'..','..'))
T=os.path.join(REPO,'source','tools'); sys.path.insert(0,T); sys.dont_write_bytecode=True
err=[]; warn=[]
CAT='amuse hotel canal rail industry burial town civic fort water inst light landmark lidar'.split()
ST='ruins traces standing marker gone water'.split(); PREC='exact site area'.split()
ACC='public view ask permit boat'.split(); EFF='drive walk hike boat'.split(); CONF=('', 'verified','mixed','lead')
app=open(os.path.join(REPO,'source','src','app.js'),encoding='utf-8').read()
from states import REG,HUBS,REG_STATE
OUTL=json.load(open(os.path.join(REPO,'source','build','states.json'))) if os.path.exists(os.path.join(REPO,'source','build','states.json')) else {}
def _in(r,x,y):
    ins=False; n=len(r)//2; j=n-1
    for i in range(n):
        xi,yi,xj,yj=r[2*i],r[2*i+1],r[2*j],r[2*j+1]
        if (yi>y)!=(yj>y) and x<(xj-xi)*(y-yi)/(yj-yi)+xi: ins=not ins
        j=i
    return ins
def state_of(lat,lon):
    for k,rs in OUTL.items():
        if any(_in(r,lon,lat) for r in rs): return k
    return None
mk=open(os.path.join(T,'make.py'),encoding='utf-8').read()
TAGS=set(re.findall(r"^ \['(\w+)',",mk,re.M))|{'now'}
BOUNDS=[float(x) for x in re.search(r"MAXB=\[\[([\d.,\-\[\]]+)\]\]",app).group(1).replace('[','').replace(']','').split(',')]
# ---- place lists ----
ids={}
def seen(i,where):
    if i in ids: err.append(f"duplicate id '{i}' in {where} and {ids[i]}: add a town or state suffix to the new one")
    ids[i]=where
from data_a import A
for r in A: seen(r[1],'data_a')
from data_b import B
for b in B: seen(b['id'],'data_b')
keys=set(); stamps=[]
for f in sorted(glob.glob(os.path.join(T,'data_*.py'))):
    name=os.path.basename(f)[:-3]
    if name in('data_a','data_b'): continue
    m=importlib.import_module(name)
    for need in('BATCH','PLACES','PIN_NOTES'):
        if not hasattr(m,need): err.append(f'{name}: missing {need}')
    if not hasattr(m,'PLACES'): continue
    k=getattr(m,'BATCH',{}).get('key')
    if 'TODO' in str(getattr(m,'BATCH',{}).get('label','')): err.append(f'{name}: the batch label still says TODO')
    if k in keys: err.append(f'{name}: batch key {k} is already used')
    _ad=str(getattr(m,'BATCH',{}).get('added',''))
    if _ad:
        import datetime as _dt
        _now=_dt.datetime.now(_dt.timezone.utc).replace(tzinfo=None)
        try:
            _t=_dt.datetime.strptime(_ad,'%Y-%m-%d %H:%M' if len(_ad)>10 else '%Y-%m-%d')
            if _t>_now+_dt.timedelta(minutes=10): err.append(f"{name}: BATCH 'added' is {_ad}, which is in the future (it is {_now:%Y-%m-%d %H:%M} UTC now). Use the time printed by: date -u '+%Y-%m-%d %H:%M'")
            stamps.append((_ad if len(_ad)>10 else _ad+' 00:00',name))
        except ValueError: err.append(f"{name}: BATCH 'added' must look like '2026-11-17 06:27' (UTC), not '{_ad}'")
    keys.add(k)
    for p in m.PLACES:
        i=p['id']; w=f'{name}:{i}'; seen(i,name)
        if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*',i): err.append(f'{w}: id must be lowercase words joined by hyphens')
        for fld,ok in(('cat',CAT),('st',ST),('prec',PREC),('acc',ACC),('eff',EFF)):
            if p[fld] not in ok: err.append(f"{w}: {fld}='{p[fld]}' is not one of {' '.join(ok)}")
        if p['reg'] not in REG: err.append(f"{w}: region '{p['reg']}' is not listed in tools/states.py")
        if (p.get('conf') or '').lower() not in CONF: err.append(f"{w}: conf='{p['conf']}' must be empty, 'mixed' or 'lead'")
        for t in [x for x in p['tags'].split(',') if x]:
            if t not in TAGS: err.append(f"{w}: tag '{t}' is not a series tag ({' '.join(sorted(TAGS))})")
        if not(BOUNDS[0]<=p['lat']<=BOUNDS[2] and BOUNDS[1]<=p['lon']<=BOUNDS[3]): err.append(f"{w}: pin {p['lat']},{p['lon']} is outside the map bounds; widen maxBounds in app.js if this is a new area")
        stt=state_of(p['lat'],p['lon'])
        if p['reg'] in REG_STATE and stt!=REG_STATE[p['reg']]: err.append(f"{w}: the pin is in {stt or 'no listed state'} but region '{p['reg']}' belongs to {REG_STATE[p['reg']]}; check the coordinate and the region")
        if p.get('th') and not(isinstance(p['th'],(list,tuple)) and len(p['th'])==2): err.append(f'{w}: th must be [lat, lon]')
        if not p['story'].strip(): err.append(f'{w}: empty story')
        # a drafted place (tools/lidar.py draft) is not finished while any of its text still says TODO
        if any('TODO' in str(p.get(k) or '') for k in ('id','name','town','reg','years','story','look','hook','accn')) or 'TODO' in str(m.PIN_NOTES.get(i) or ''): err.append(f'{w}: a text still says TODO; finish the draft (LIDAR.md step 6)')
        if not m.PIN_NOTES.get(i): err.append(f'{w}: no pin note saying where the coordinate came from')
        if not p.get('links') and (p.get('conf') or '')!='lead': err.append(f"{w}: no source link (allowed only when conf='lead')")
        if p['acc'] in('ask','view','permit','boat') and not p.get('accn'): warn.append(f'{w}: access is {p["acc"]} but there is no access note')
if not SRC_ONLY:
    # ---- built site matches the sources ----
    def rd(*p): return open(os.path.join(REPO,*p),encoding='utf-8').read()
    idx=rd('index.html'); mm=re.search(r'<script type="application/json" id="d-sites">(.*?)</script>',idx,re.S)
    if not mm: err.append('index.html has no d-sites block')
    else:
        D=json.loads(mm.group(1).replace('<\\/','</')); built={s['id'] for s in D['sites']}
        miss=sorted(set(ids)-built); extra=sorted(i for i in built-set(ids) if not i.startswith('lm-'))
        if miss: err.append('in the place lists but not in the built site (rebuild needed): '+', '.join(miss[:12]))
        if extra: err.append('in the built site but not in the place lists: '+', '.join(extra[:12]))
        for s in D['sites']:
            if s.get('tm') and not os.path.exists(os.path.join(REPO,'topo',s['id']+'.webp')): err.append(f"topo/{s['id']}.webp is missing")
        v=D.get('v','')
        if f"const V='{v}'" not in rd('sw.js'): err.append('sw.js version does not match index.html (rebuild needed)')
        if f'app.js?v={v}' not in idx: err.append('index.html does not reference this build of app.js')
    if rd('app.js')!=rd('source','src','app.js'): err.append('app.js in the root differs from source/src/app.js: edit the source and rebuild, never the root file')
    # the Android app reads boot.js and version.json from the built site
    if os.path.exists(os.path.join(REPO,'source','src','boot.js')):
        if not os.path.exists(os.path.join(REPO,'boot.js')) or rd('boot.js')!=rd('source','src','boot.js'): err.append('boot.js in the root differs from source/src/boot.js (rebuild needed)')
        try:
            if mm and json.loads(rd('version.json')).get('v')!=D.get('v'): err.append('version.json does not match index.html (rebuild needed); the Android app would never see the new places')
        except Exception: err.append('version.json is missing or unreadable (rebuild needed)')
    for need in('data/lines.json','data/leads.json','data/pockets.json','leaflet.js','GUIDE.md','CLAUDE.md','source/build/states.json'):
        if not os.path.exists(os.path.join(REPO,need)): err.append('missing '+need)
    # the historic-pockets layer: every state it lists needs its detail file, or zooming in there shows nothing
    try:
        pj=json.loads(rd('data','pockets.json'))
        for k in pj.get('s',{}):
            if not os.path.exists(os.path.join(REPO,'data','pock',k+'.json')): err.append(f'data/pockets.json lists {k} but data/pock/{k}.json is missing (the workspace lost build/pock: run setup.sh again, or tools/pockets.py)')
        if not pj.get('k'): err.append('data/pockets.json holds no pockets')
    except Exception: pass
# ---- the LiDAR ledger (source/lidar/units, kept by tools/lidar.py; LIDAR.md) ----
LSEEN={}
for f in sorted(glob.glob(os.path.join(REPO,'source','lidar','units','*.json'))):
    rel=os.path.relpath(f,REPO)
    try: u=json.load(open(f,encoding='utf-8'))
    except Exception as e: err.append(f'{rel}: not valid JSON ({str(e)[:60]}); it is written by tools/lidar.py, not by hand'); continue
    if not u.get('name') or not re.fullmatch(r'[a-z]+',u.get('code') or ''): err.append(f'{rel}: no unit name or letter code'); continue
    for c in u.get('cands',[]):
        ci=c.get('id','?')
        if ci in LSEEN: err.append(f'{rel}: candidate id {ci} is also in {LSEEN[ci]}')
        LSEEN[ci]=rel
        if not str(ci).startswith(u['code']): err.append(f'{rel}: candidate {ci} does not carry the unit code {u["code"]}')
        if c.get('status') not in('new','no','maybe','yes','published'): err.append(f'{rel}: {ci} has status {c.get("status")!r}')
        if c.get('status')=='published' and c.get('place') not in ids: err.append(f'{rel}: {ci} is marked published as {c.get("place")!r}, but no place list has that id (lost draft? run: python3 tools/lidar.py mark {ci} yes)')
        if c.get('status')=='no' and not c.get('why'): err.append(f'{rel}: {ci} is set aside with no reason word')
        if ((c.get('check') or {}).get('parcel') or {}).get('kind')=='PRIVATE' and c.get('status')=='published': err.append(f'{rel}: {ci} is published but its tax parcel is private')
# ---- nothing personal in a public repository ----
MAIL=re.compile(r'[\w.+-]+@[\w-]+\.[\w.]+'); OKMAIL=('noreply@anthropic.com','users.noreply.github.com','example.com','2x.png')
for dp,dn,fn in os.walk(REPO):
    if '.git' in dp.split(os.sep): continue
    if os.path.relpath(dp,REPO).split(os.sep)[0]=='android-app':   # downloaded packages and build output of the Android app are not ours to check
        dn[:]=[d for d in dn if d not in('node_modules','www','build','.gradle','assets','capacitor-cordova-android-plugins')]
    for f in fn:
        if not f.endswith(('.md','.py','.js','.json','.html','.sh','.txt','.css','.yml','.java','.xml','.gradle','.properties')): continue
        p=os.path.join(dp,f)
        if os.path.getsize(p)>3_000_000: continue
        for a in set(MAIL.findall(open(p,encoding='utf-8',errors='ignore').read())):
            if not any(o in a for o in OKMAIL) and not re.search(r'\.(png|jpg|webp|js|css)$',a): err.append(f'{os.path.relpath(p,REPO)}: contains what looks like an email address ({a})')
# ---- session notes (notes/<batch key>.md): every batch from November 19, 2026 on has one, and it is filled in
_nl=warn if SRC_ONLY else err      # publish.sh makes the empty note and checks sources: a warning there, an error on GitHub
for st_,nm in stamps:
    if st_<'2026-11-19': continue
    m_=importlib.import_module(nm); k_=m_.BATCH['key']; np_=os.path.join(REPO,'notes',k_+'.md')
    if not os.path.exists(np_): _nl.append(f"{nm}: no note file notes/{k_}.md. Run  python3 tools/note.py {k_} <clone>  after publish.sh and fill it in (it replaces the lines sessions used to add to GUIDE.md and LEADS.md)"); continue
    t_=open(np_,encoding='utf-8').read()
    if 'Delete this bracketed text' in t_ or '| Example mill |' in t_: _nl.append(f'notes/{k_}.md still holds the template text: fill in "What this batch is", the leads and the tips, and delete the bracketed lines and the example row')
    for h_ in('## What this batch is','## Leads','## Tips'):
        if h_ not in t_: _nl.append(f'notes/{k_}.md: the heading "{h_}" is missing')
for w in warn: print('warning:',w)
for e in err: print('ERROR:',e)
if stamps:
    stamps.sort(); print(f'newest batch: {stamps[-1][1]} ({stamps[-1][0]} UTC). A new batch must be the newest, or the app will not mark its places as new.')
print(f'{len(ids)} place ids, {len(keys)} batches, {len(warn)} warnings, {len(err)} errors'+(' (sources only: the built site was not checked)' if SRC_ONLY else ''))
print('(The built site shows about 39 more places than this count: the Albany and Troy landmark pins, ids starting lm-, are made by build_sites.py from the landmark list and are not in a place list. That is expected.)')
sys.exit(1 if err else 0)
