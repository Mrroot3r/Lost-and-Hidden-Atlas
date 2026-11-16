#!/usr/bin/env python3
"""Checks a repository clone before a change is proposed. No network, standard library only.
   python3 source/tools/check.py [path-to-repo]
Exit code 1 on any error. Warnings are for a person to read."""
import sys,os,re,json,glob,importlib
REPO=os.path.abspath(sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(__file__),'..','..'))
T=os.path.join(REPO,'source','tools'); sys.path.insert(0,T); sys.dont_write_bytecode=True
err=[]; warn=[]
CAT='amuse hotel canal rail industry burial town civic fort water inst light landmark'.split()
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
BOUNDS=[float(x) for x in re.search(r"maxBounds:\[\[([\d.,\-\[\]]+)\]\]",app).group(1).replace('[','').replace(']','').split(',')]
# ---- place lists ----
ids={}
def seen(i,where):
    if i in ids: err.append(f"duplicate id '{i}' in {where} and {ids[i]}: add a town or state suffix to the new one")
    ids[i]=where
from data_a import A
for r in A: seen(r[1],'data_a')
from data_b import B
for b in B: seen(b['id'],'data_b')
keys=set()
for f in sorted(glob.glob(os.path.join(T,'data_*.py'))):
    name=os.path.basename(f)[:-3]
    if name in('data_a','data_b'): continue
    m=importlib.import_module(name)
    for need in('BATCH','PLACES','PIN_NOTES'):
        if not hasattr(m,need): err.append(f'{name}: missing {need}')
    if not hasattr(m,'PLACES'): continue
    k=getattr(m,'BATCH',{}).get('key')
    if k in keys: err.append(f'{name}: batch key {k} is already used')
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
        if not m.PIN_NOTES.get(i): err.append(f'{w}: no pin note saying where the coordinate came from')
        if not p.get('links') and (p.get('conf') or '')!='lead': err.append(f"{w}: no source link (allowed only when conf='lead')")
        if p['acc'] in('ask','view','permit','boat') and not p.get('accn'): warn.append(f'{w}: access is {p["acc"]} but there is no access note')
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
for need in('data/lines.json','data/leads.json','leaflet.js','GUIDE.md','CLAUDE.md','source/build/states.json'):
    if not os.path.exists(os.path.join(REPO,need)): err.append('missing '+need)
# ---- nothing personal in a public repository ----
MAIL=re.compile(r'[\w.+-]+@[\w-]+\.[\w.]+'); OKMAIL=('noreply@anthropic.com','users.noreply.github.com','example.com','2x.png')
for dp,dn,fn in os.walk(REPO):
    if '.git' in dp.split(os.sep): continue
    for f in fn:
        if not f.endswith(('.md','.py','.js','.json','.html','.sh','.txt','.css','.yml')): continue
        p=os.path.join(dp,f)
        if os.path.getsize(p)>3_000_000: continue
        for a in set(MAIL.findall(open(p,encoding='utf-8',errors='ignore').read())):
            if not any(o in a for o in OKMAIL) and not re.search(r'\.(png|jpg|webp|js|css)$',a): err.append(f'{os.path.relpath(p,REPO)}: contains what looks like an email address ({a})')
for w in warn: print('warning:',w)
for e in err: print('ERROR:',e)
print(f'{len(ids)} place ids, {len(keys)} batches, {len(warn)} warnings, {len(err)} errors')
sys.exit(1 if err else 0)
