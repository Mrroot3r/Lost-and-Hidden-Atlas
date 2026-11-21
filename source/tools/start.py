#!/usr/bin/env python3
"""The first command of a research session: everything the Atlas already knows about an area, in one go.
   python3 tools/start.py "Syracuse, New York" [km=15]
   python3 tools/start.py 43.05 -76.15 [km=15]
   python3 tools/start.py --prs                  only the open pull requests (the look just before publishing)
It prints: where the area is and which state; the region codes a new place there can use; the places already on the map
(so nothing is added twice) and which data files hold them; the unchecked leads already carried there (mapped ruins,
vanished places, old mines), each with a coordinate; the rows of LEADS.md for that ground; what GUIDE.md says about the
state and the area; and the order of work. Read its output instead of reading GUIDE.md section 10 or LEADS.md whole."""
import sys,os,re,json,math,time,subprocess,urllib.parse,urllib.request
a=sys.argv[1:]
if not a: sys.exit(__doc__)
if a[0]=='--prs':          # only the open pull requests: the second look just before publishing (gh may print nothing in a scheduled session)
    try:
        pr=json.load(urllib.request.urlopen(urllib.request.Request('https://api.github.com/repos/Mrroot3r/Lost-and-Hidden-Atlas/pulls?state=open&per_page=50',headers={'User-Agent':'lost-hidden-atlas-research/1.0','Accept':'application/vnd.github+json'}),timeout=30))
        print('Open pull requests: %d'%len(pr))
        for x in pr: print('  #%d  %s  [branch %s, opened %s]'%(x['number'],x['title'][:110],x['head']['ref'],x['created_at'][:16].replace('T',' ')))
    except Exception as e: print('The open pull requests could not be listed (%s): look at the repository\'s pull requests page.'%str(e)[:60])
    sys.exit(0)
HERE=os.path.dirname(os.path.abspath(__file__)); W=os.path.dirname(HERE)
num=lambda s:re.fullmatch(r'-?\d+(\.\d+)?',s) is not None
a=[re.sub(r'^km=','',x) for x in a]          # the usage line writes the distance as [km=15]: take "km=15" as well as "15"
name=''; words=[]
if len(a)>=2 and num(a[0]) and num(a[1]): la,lo=float(a[0]),float(a[1]); km=float(a[2]) if len(a)>2 else 15.0
else:
    name=a[0]; km=float(a[1]) if len(a)>1 and num(a[1]) else 15.0
    u='https://nominatim.openstreetmap.org/search?'+urllib.parse.urlencode({'q':name,'format':'jsonv2','limit':8,'countrycodes':'us,ca'})
    j=None
    for k in range(3):
        try: j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'lost-hidden-atlas-research/1.0 (personal research tool)'}),timeout=30)); break
        except Exception as e: time.sleep(2+2*k)
    if not j: sys.exit(f'Could not find "{name}". Give it as "Town, State", or give a latitude and longitude.')
    import placepick      # several places share a name: stay in the state named, and take a town before a county (tools/placepick.py)
    best,others=placepick.pick(j,name)
    la,lo=float(best['lat']),float(best['lon']); words=[w.strip() for w in best['display_name'].split(',')][:4]
    print(f'== {name}: {la:.5f}, {lo:.5f}  ({best["display_name"][:90]})')
    if others:
        print('   CHECK THAT THIS IS THE PLACE YOU MEAN. Others of that name:')
        for o in others[:4]: print(f'     {o["display_name"][:80]}:   python3 tools/start.py {float(o["lat"]):.4f} {float(o["lon"]):.4f}')
os.chdir(W)
if not os.path.exists('build/sites.json'): subprocess.run([sys.executable,'tools/build_sites.py'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
def d(p,q): return math.hypot((p-la)*111.32,(q-lo)*111.32*math.cos(math.radians(la)))
# ---- state and regions
sys.path.insert(0,HERE); st=None
try:
    O=json.load(open('build/states.json'))
    def inr(r,x,y):
        ins=False; n=len(r)//2; j2=n-1
        for i in range(n):
            xi,yi,xj,yj=r[2*i],r[2*i+1],r[2*j2],r[2*j2+1]
            if (yi>y)!=(yj>y) and x<(xj-xi)*(y-yi)/(yj-yi)+xi: ins=not ins
            j2=i
        return ins
    st=next((k for k,rs in O.items() if any(inr(r,lo,la) for r in rs)),None)
except Exception: pass
S=json.load(open('build/sites.json')); sname=''
try:
    from states import STATES
    row=next((s for s in STATES if s['k']==st),None)
    if row:
        sname=row['name']; cnt={}
        for s in S: cnt[s['reg']]=cnt.get(s['reg'],0)+1
        near={}
        for s in S:
            if d(s['lat'],s['lon'])<=max(km,40): near[s['reg']]=near.get(s['reg'],0)+1
        print(f'== State: {sname}. Region codes for reg= (places so far; * = used by places within {max(km,40):g} km of here):')
        print('   '+'   '.join(f"{c}{'*' if c in near else ''} = {l} ({cnt.get(c,0)})" for c,l in row['regions']))
except Exception as e: print('== (region list not read:',str(e)[:60]+')')
try:
    sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from ortho import which
    w=which(la,lo); print('== The pin check (tools/pincheck.py) will show: '+w+('. Expect leaves on the trees: for anything in woods the --lidar sheet is the one that shows the ground.' if 'Esri' in w else '. Bare trees: a ruin in woods can show on it; look at the --lidar sheet as well.' if 'leaf-off' in w else '. A state flight. The trees were bare in the frames looked at when it was added (tools/ortho.py), but check that in each tile; look at the --lidar sheet as well.')+(' This state\'s server takes several seconds a pin.' if 'Pennsylvania' in w else ''))
except Exception as e: print('== (which aerial the pin check uses: not worked out,',str(e)[:60]+')')
# ---- what is already there
print(subprocess.run([sys.executable,'tools/nearby.py',str(la),str(lo),str(km)],capture_output=True,text=True).stdout.rstrip())
files={}
for s in S:
    if d(s['lat'],s['lon'])<=km: files[s.get('new') or 'the first catalogue (data_a.py, data_b.py)']=files.get(s.get('new') or 'the first catalogue (data_a.py, data_b.py)',0)+1
if files: print('== Batches holding those places (the data file of batch key K is the one whose BATCH key is K; grep tools/data_*.py for an id): '+', '.join(f'{k} ({v})' for k,v in sorted(files.items(),key=lambda x:-x[1])))
towns=sorted({s['town'] for s in S if d(s['lat'],s['lon'])<=km})
# ---- the repository's notes
repo=None
for c in ([open('.repo').read().strip()] if os.path.exists('.repo') else [])+[os.environ.get('REPO',''),'/home/claude/lost-and-hidden-atlas',os.path.join(W,'..','lost-and-hidden-atlas')]:
    if c and os.path.exists(os.path.join(c,'LEADS.md')): repo=c; break
if not repo: print('== LEADS.md and GUIDE.md not found from here (set REPO=<clone>): grep them yourself for the town names.'); sys.exit(0)
strip=lambda w:re.sub(r'^(Town|City|Village) of | County$','',w).strip()
keys=[w for w in dict.fromkeys([strip(w) for w in words[:3]]+towns) if len(w)>3 and w.lower() not in('united states','town','city') and w!=sname]
# ---- the notes sessions leave (notes/<batch key>.md): what a batch was, its leads, its tips
import glob
NOTES=[]
for f in sorted(glob.glob(os.path.join(repo,'notes','*.md'))):
    t=open(f,encoding='utf-8').read(); head=t.split('\n## ')[0]
    get=lambda k: (re.search(r'^'+k+r':\s*(.*)$',head,re.M) or [None,''])[1].strip()
    sec=lambda name: (re.search(r'^## '+name+r'[^\n]*\n(.*?)(?=^## |\Z)',t,re.M|re.S) or [None,''])[1].strip()
    NOTES.append({'key':os.path.basename(f)[:-3],'title':head.split('\n')[0].lstrip('# ').strip(),'state':get('state'),'region':get('region'),'date':get('date'),'what':sec('What this batch is'),'leads':[l for l in sec('Leads').split('\n') if l.startswith('|') and not l.startswith('| Place') and not l.startswith('|---') and not l.startswith('| Example mill')],'tips':[l.strip() for l in sec('Tips').split('\n') if l.strip().startswith('-') and 'Delete this bracketed text' not in l and l.strip().lower() not in('- none','- none.')]})
rows=[]
for l in list(open(os.path.join(repo,'LEADS.md'),encoding='utf-8'))+[x for n in NOTES for x in n['leads']]:
    if not l.startswith('|') or l.startswith('| Place') or l.startswith('|---'): continue
    hit=False
    for m in re.finditer(r'(-?\d{2}\.\d{3,}),\s*(-\d{2,3}\.\d{3,})',l):
        if d(float(m.group(1)),float(m.group(2)))<=km*1.5: hit=True
    where=l.split('|')[2] if l.count('|')>3 else l
    other=[c for c in re.findall(r',\s*([A-Z]{2})\b',where) if c.lower()!=(st or '')]      # a row in another state ("New Orleans, LA" for Orleans County, NY)
    if not hit and not other and any(re.search(r'\b'+re.escape(k)+r'\b',where) for k in keys): hit=True
    if hit: rows.append(l.strip())
rows.sort(key=lambda l:not l.startswith('| Spot '))       # the owner's own spots first: he marked these buildings himself (tools/visits.py)
print(f'== Leads on file for this ground (LEADS.md and the notes/ files): {len(rows)}'+(' (try these before hunting for new names; delete a row, wherever it is, when its place is added)' if rows else ''))
for r in rows[:25]: print('  '+(r if len(r)<520 else r[:520]+' …'))
g=open(os.path.join(repo,'GUIDE.md'),encoding='utf-8').read()
if sname:
    m=re.search(r'^\| '+re.escape(sname)+r' \|.*$',g,re.M)
    if m: print('== GUIDE.md section 8, the row for '+sname+':\n  '+m.group(0)[:700])
sec=re.search(r'^## 10\. .*?(?=^## 11\. )',g,re.M|re.S)
if sec:
    area=[]; state=[]
    for b in re.findall(r'^- .*$',sec.group(0),re.M):
        n=sum(1 for k in keys[:10] if re.search(r'\b'+re.escape(k)+r'\b',b))
        if n: area.append((-n,b))
        elif sname and re.search(r'\b'+re.escape(sname)+r'\b',b): state.append(b)
    area.sort(key=lambda x:x[0])
    print(f'== GUIDE.md section 10, known gaps that name this area: {len(area)}'+('' if area else ' (nothing written about this ground yet)'))
    for n,b in area[:5]: print('  '+(b if len(b)<800 else b[:800]+' …'))
    if state: print(f'   and {len(state)} more that mention {sname} in general; their openings:')
    for b in state[:5]: print('     '+b[:150]+' …')
# ---- what earlier sessions wrote: about this state's ground, and their tips
mine=[n for n in NOTES if sname and sname in n['state']]
regs={s['reg'] for s in S if d(s['lat'],s['lon'])<=max(km,40)}
mine.sort(key=lambda n:(not (set(re.split(r'[,\s]+',n['region']))&regs),n['date']),reverse=False)
if mine:
    print(f'== Notes from earlier sessions in {sname}: {len(mine)} (nearest ground first; the whole of each is in notes/<key>.md)')
    for n in mine[:6]: print('  [%s, %s, region %s] %s'%(n['key'],n['date'],n['region'],(n['what'].replace('\n',' ') if len(n['what'])<600 else n['what'].replace('\n',' ')[:600]+' …')))
# ---- what the tidy job has kept from earlier notes (GUIDE.md section 16): the lists for every state and for this one
m16=re.search(r'^## 16\.[^\n]*\n(.*?)(?=^## \d|\Z)',g,re.M|re.S)
if m16:
    def kept(h):
        mm=re.search(r'^### '+re.escape(h)+r'[ \t]*\n(.*?)(?=^### |\Z)',m16.group(1),re.M|re.S)
        return [l.strip() for l in (mm.group(1) if mm else '').split('\n') if l.strip().startswith('- ')]
    here=kept(sname) if sname else []; every=kept('Every state')
    if here:
        print(f'== What earlier sessions learned in {sname} (GUIDE.md section 16): {len(here)}')
        for t in here: print('  '+t)
    if every:
        print(f'== What earlier sessions learned that holds in every state (GUIDE.md section 16): {len(every)}')
        for t in every: print('  '+t)
tips=[]
for n in sorted(NOTES,key=lambda n:n['date'],reverse=True):
    for t in n['tips']: tips.append((n in mine,n['date'],n['key'],t))
tips.sort(key=lambda x:(not x[0],),reverse=False)
if tips:
    print(f'== Tips left by earlier sessions: {len(tips)} (this state\'s first, then the newest; they are not yet in GUIDE.md)')
    for own,dt_,k,t in tips[:14]: print('  [%s] %s'%(k,t if len(t)<420 else t[:420]+' …'))
# ---- work other sessions have open: two sessions given the same job at the same hour have picked the same county
try:
    pr=json.load(urllib.request.urlopen(urllib.request.Request('https://api.github.com/repos/Mrroot3r/Lost-and-Hidden-Atlas/pulls?state=open&per_page=30',headers={'User-Agent':'lost-hidden-atlas-research/1.0','Accept':'application/vnd.github+json'}),timeout=30))
    print(f'== Open pull requests: {len(pr)}'+(' (work another session has not had merged yet. If one covers this ground, pick other ground or other places, and do not reuse its file name, batch key or ids)' if pr else ''))
    for x in pr[:12]: print('  #%d  %s  [branch %s, opened %s]'%(x['number'],x['title'][:110],x['head']['ref'],x['created_at'][:16].replace('T',' ')))
except Exception as e: print('== Open pull requests could not be listed ('+str(e)[:50]+'): look at the repository\'s pull requests page before choosing ground.')
print('''== The order of work (GUIDE.md sections 4 to 6 have the detail)
  1. Find places: tools/wiki_raw.py --rows "National Register of Historic Places listings in <County>, <State>" -g 'mill|lock|ruin|site|kiln|fort'
     then tools/wiki_raw.py "Exact title", tools/page.py <url> (reads PDFs; falls back to an archived copy), tools/nom.py "name, town, state".
  2. Write tools/data_<area>.py (BATCH, PLACES, PIN_NOTES). Batch time: copy the output of  date -u '+%Y-%m-%d %H:%M'
  3. Parking for each place: tools/parking.py <lat> <lon>  -> th=[lat,lon], thn='...'
  4. python3 tools/build_sites.py && python3 tools/pincheck.py --batch <key> --lidar ; look at both sheets; move pins with tools/pix.py
     (fifteen places take two to four minutes with --lidar: give the command a long timeout, or run it in the background)
  5. ATLAS=$PWD bash tools/all.sh ; the smoke test ; then tools/publish.sh <clone> <branch> ONCE ; then  python3 tools/note.py <batch key> <clone>
     and fill in notes/<batch key>.md. Do NOT edit GUIDE.md, LEADS.md or PROMPTS.md: other sessions are writing too.''')
