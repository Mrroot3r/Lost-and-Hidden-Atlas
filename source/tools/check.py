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
# Before a single place list is run: prove that each one is only data. A list that holds anything else stops the check here.
import safe_data; safe_data.must(T)
err=[]; warn=[]
ST='ruins traces standing marker gone water'.split(); PREC='exact site area'.split()
ACC='public view ask permit boat'.split(); EFF='drive walk hike boat'.split(); CONF=('', 'verified','mixed','lead')
app=open(os.path.join(REPO,'source','src','app.js'),encoding='utf-8').read()
CAT=re.findall(r"(\w+):\['[^']+','#[0-9a-f]{6}'\]",re.search(r'const CAT=\{[^\n]*\};',app).group(0))      # the kinds of place: app.js holds the one list
if len(CAT)<10: sys.exit('check.py could not read the kinds of place (const CAT) from app.js')
from states import REG,HUBS,REG_STATE
OUTL=json.load(open(os.path.join(REPO,'source','build','states.json'))) if os.path.exists(os.path.join(REPO,'source','build','states.json')) else {}
def _in(r,x,y):
    ins=False; n=len(r)//2; j=n-1
    for i in range(n):
        xi,yi,xj,yj=r[2*i],r[2*i+1],r[2*j],r[2*j+1]
        if (yi>y)!=(yj>y) and x<(xj-xi)*(y-yi)/(yj-yi)+xi: ins=not ins
        j=i
    return ins
def states_at(lat,lon):
    """every state whose outline holds the point: the outlines are coarse and overlap along shores and rivers"""
    return [k for k,rs in OUTL.items() if any(_in(r,lon,lat) for r in rs)]
def state_of(lat,lon):
    s=states_at(lat,lon); return s[0] if s else None
def near_state(lat,lon,k,m=1000):
    """is the point within m metres of state k's outline? The outlines are simplified to about a kilometre and run a few
    hundred metres off border rivers (the Salmon Falls at South Berwick, the Connecticut), so a pin on the right bank can
    fall just outside its own state."""
    import math
    kx=math.cos(math.radians(lat))*111320; ky=110540
    for r in OUTL.get(k,[]):
        n=len(r)//2
        for i in range(n):
            ax,ay,bx,by=(r[2*i]-lon)*kx,(r[2*i+1]-lat)*ky,(r[2*((i+1)%n)]-lon)*kx,(r[2*((i+1)%n)+1]-lat)*ky
            dx,dy=bx-ax,by-ay; L=dx*dx+dy*dy; t=max(0,min(1,-(ax*dx+ay*dy)/L)) if L else 0
            if (ax+t*dx)**2+(ay+t*dy)**2<=m*m: return True
    return False
mk=open(os.path.join(T,'make.py'),encoding='utf-8').read()
TAGS=set(re.findall(r"^ \['(\w+)',",mk,re.M))|{'now'}
BOUNDS=[float(x) for x in re.search(r"MAXB=\[\[([\d.,\-\[\]]+)\]\]",app).group(1).replace('[','').replace(']','').split(',')]
# ---- place lists ----
ids={}; WAS={}      # WAS: old id -> the place that says it replaces it (was=)
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
        # red brick (GUIDE.md section 4): every place written since November 19, 2026 says yes, some, no, or ? for not checked
        for _o in ([p['was']] if isinstance(p.get('was'),str) and p.get('was') else list(p.get('was') or [])):      # this entry replaces an older, thinner one for the same place
            if not isinstance(_o,str) or not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*',_o) or _o==i: err.append(f"{w}: was='{_o}' must be the id of the older entry this one replaces")
            elif _o in WAS: err.append(f"{w}: was='{_o}', but {WAS[_o]} already replaces it")
            else: WAS[_o]=w
        # the kind of place: a church filed as a civic building, or a road bridge as one, is the commonest slip (GUIDE.md section 4 says what each kind holds)
        if p['cat'] in('civic','landmark','inst') and re.search(r'\b(church|meeting ?house|synagogue|cathedral|basilica|chapel)\b',p['name'],re.I) and not re.search(r'\b(park|street|centre|center|grange|academy|courthouse|museum of|hall, )\b',p['name'],re.I) and _ad[:10]>='2026-11-19': warn.append(f"{w}: the name reads as a place of worship but cat='{p['cat']}'. A church, meeting house, synagogue or chapel is cat='worship', standing or not; keep '{p['cat']}' only if the entry is really about something else")
        if p['cat']=='civic' and re.search(r'\bbridge\b',p['name'],re.I) and _ad[:10]>='2026-11-19': warn.append(f"{w}: a road or covered bridge is cat='landmark' (a railway bridge is 'rail'), not 'civic'")
        _tip=p.get('tip') or ''      # a place that began as a reader's lead carries the day it was sent (GUIDE.md section 15)
        if _tip and not(re.fullmatch(r'20\d\d-[01]\d-[0-3]\d',_tip) and _tip<=_ad[:10]): err.append(f"{w}: tip='{_tip}' must be the day the reader sent it, as YYYY-MM-DD, and not after the batch's own date")
        _bk=p.get('brick') or ''
        if _bk not in ('','yes','some','no','?'): err.append(f"{w}: brick='{_bk}' must be yes, some, no or ? (not checked)")
        if not _bk and _ad[:10]>='2026-11-19': err.append(f"{w}: no brick=. Say whether red brick can be seen there: brick='yes' (mostly brick), 'some' (part brick), 'no', or '?' if no source or picture settles it")
        for fld,ok in(('cat',CAT),('st',ST),('prec',PREC),('acc',ACC),('eff',EFF)):
            if p[fld] not in ok: err.append(f"{w}: {fld}='{p[fld]}' is not one of {' '.join(ok)}")
        if p['reg'] not in REG: err.append(f"{w}: region '{p['reg']}' is not listed in tools/states.py")
        if (p.get('conf') or '').lower() not in CONF: err.append(f"{w}: conf='{p['conf']}' must be empty, 'mixed' or 'lead'")
        for t in [x for x in p['tags'].split(',') if x]:
            if t not in TAGS: err.append(f"{w}: tag '{t}' is not a series tag ({' '.join(sorted(TAGS))})"+(" (a burial ground's series tag is cemeteries; burial is a category)" if t=='burial' else " (a railroad building's series tag is stations; a freight house or a line fits none: leave tags empty)" if t=='rail' else " ('"+t+"' is a category, cat=, not a tag)" if t in CAT else ''))
        if not(BOUNDS[0]<=p['lat']<=BOUNDS[2] and BOUNDS[1]<=p['lon']<=BOUNDS[3]): err.append(f"{w}: pin {p['lat']},{p['lon']} is outside the map bounds; widen maxBounds in app.js if this is a new area")
        sts=states_at(p['lat'],p['lon']); stt=sts[0] if sts else None; want=REG_STATE.get(p['reg'])
        if want and want not in sts and near_state(p['lat'],p['lon'],want): warn.append(f"{w}: the pin is just outside {want}'s outline, which is coarse along borders; fine if the pin is on the {want} side on the aerial")
        elif p['reg'] in REG_STATE and want not in sts: err.append(f"{w}: the pin is in {stt or 'no listed state'} but region '{p['reg']}' belongs to {REG_STATE[p['reg']]}; check the coordinate and the region")
        if p.get('th') and not(isinstance(p['th'],(list,tuple)) and len(p['th'])==2): err.append(f'{w}: th must be [lat, lon]')
        if not p['story'].strip(): err.append(f'{w}: empty story')
        # a drafted place (tools/lidar.py draft) is not finished while any of its text still says TODO
        if any('TODO' in str(p.get(k) or '') for k in ('id','name','town','reg','years','story','look','hook','accn')) or 'TODO' in str(m.PIN_NOTES.get(i) or ''): err.append(f'{w}: a text still says TODO; finish the draft (LIDAR.md step 6)')
        if not m.PIN_NOTES.get(i): err.append(f'{w}: no pin note saying where the coordinate came from')
        if not p.get('links') and (p.get('conf') or '')!='lead': err.append(f"{w}: no source link (allowed only when conf='lead')")
        for l in p.get('links') or []:      # a link is [label, address]; the address opens in the reader's browser, so it must be a web address and nothing else
            if not(isinstance(l,(list,tuple)) and len(l)==2 and all(isinstance(x,str) for x in l) and l[0].strip()): err.append(f"{w}: a link must be [label, address], both text: {str(l)[:80]}"); continue
            if not re.match(r'https?://[^\s<>"]+$',l[1]) and not re.match(r'https?://[^<>"\n\r\t]+$',l[1]): err.append(f"{w}: the link '{l[0][:40]}' is not a web address (it must begin http:// or https:// and hold no < > or quote marks): {l[1][:80]}")
            elif ' ' in l[1]: warn.append(f"{w}: the link '{l[0][:40]}' has a space in its address; write %20")
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
    # the old rail and canal lines: the hosted copy fetches them a state at a time (tools/lines_split.py), so every state the
    # page lists needs its file, and the file must be the one the page's stamp was made from
    if mm:
        import hashlib
        lx=D.get('lx') or {}
        if not lx.get('s'): err.append('the page data has no index of the old lines ("lx"): rebuild with tools/make.py')
        for k,v in (lx.get('s') or {}).items():
            pth=os.path.join(REPO,'data','lines',k+'.json')
            if not os.path.exists(pth): err.append(f'the page lists old lines for {k} but data/lines/{k}.json is missing (rebuild needed)')
            elif hashlib.md5(open(pth,'rb').read()).hexdigest()[:8]!=v.get('h'): err.append(f'data/lines/{k}.json is not the file the page was built with (rebuild needed)')
        if lx.get('s') and not os.path.exists(os.path.join(REPO,'data','lines','wide.json')): err.append('data/lines/wide.json is missing (rebuild needed)')
# ---- red brick found out later (tools/bricks_*.py, written by tools/brick.py) ----
for f in sorted(glob.glob(os.path.join(T,'bricks_*.py'))):
    nm=os.path.basename(f)[:-3]
    try: BR=importlib.import_module(nm).BRICK
    except Exception as ex: err.append(f'{nm}: cannot be read ({str(ex)[:60]})'); continue
    for i,v in BR.items():
        if i not in ids: err.append(f'{nm}: {i} is not a place id')
        elif not(isinstance(v,(list,tuple)) and len(v)==2 and v[0] in ('yes','some','no') and len(str(v[1]).strip())>=12): err.append(f"{nm}: {i} must be ('yes'|'some'|'no', 'how it is known: the picture's address, or the words of the source')")
# ---- the old lines: every feature says which state it is in, or the hosted copy cannot fetch them a state at a time ----
_lp=os.path.join(REPO,'data','lines.json')
if os.path.exists(_lp):
    try:
        _nos=sum(1 for f in json.load(open(_lp,encoding='utf-8')) if not f.get('s'))
        if _nos: err.append(f'data/lines.json: {_nos} lines carry no state ("s"). The file was not written by the current tools/lines.py: run it (GUIDE.md section 8, "Lines and leads for a new state")')
    except Exception as ex: err.append('data/lines.json cannot be read: '+str(ex)[:80])
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
for _o,_w in WAS.items():      # an entry may replace a landmark pin (lm-...) or an id that is gone from every list; never a full entry that is still in one
    if _o in ids: err.append(f"{_w}: was='{_o}', but that place is still in {ids[_o]}. was= is for a landmark pin (lm-...) or an entry that has been taken out")
print(f'{len(ids)} place ids, {len(keys)} batches, {len(warn)} warnings, {len(err)} errors'+(' (sources only: the built site was not checked)' if SRC_ONLY else ''))
print('(The built site shows about 39 more places than this count: the Albany and Troy landmark pins, ids starting lm-, are made by build_sites.py from the landmark list and are not in a place list. That is expected.)')
sys.exit(1 if err else 0)
