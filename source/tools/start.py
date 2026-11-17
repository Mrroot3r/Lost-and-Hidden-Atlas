#!/usr/bin/env python3
"""The first command of a research session: everything the Atlas already knows about an area, in one go.
   python3 tools/start.py "Syracuse, New York" [km=15]
   python3 tools/start.py 43.05 -76.15 [km=15]
It prints: where the area is and which state; the region codes a new place there can use; the places already on the map
(so nothing is added twice) and which data files hold them; the unchecked leads already carried there (mapped ruins,
vanished places, old mines), each with a coordinate; the rows of LEADS.md for that ground; what GUIDE.md says about the
state and the area; and the order of work. Read its output instead of reading GUIDE.md section 10 or LEADS.md whole."""
import sys,os,re,json,math,time,subprocess,urllib.parse,urllib.request
a=sys.argv[1:]
if not a: sys.exit(__doc__)
HERE=os.path.dirname(os.path.abspath(__file__)); W=os.path.dirname(HERE)
num=lambda s:re.fullmatch(r'-?\d+(\.\d+)?',s) is not None
name=''; words=[]
if len(a)>=2 and num(a[0]) and num(a[1]): la,lo=float(a[0]),float(a[1]); km=float(a[2]) if len(a)>2 else 15.0
else:
    name=a[0]; km=float(a[1]) if len(a)>1 and num(a[1]) else 15.0
    u='https://nominatim.openstreetmap.org/search?'+urllib.parse.urlencode({'q':name,'format':'jsonv2','limit':1,'countrycodes':'us,ca'})
    j=None
    for k in range(3):
        try: j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'lost-hidden-atlas-research/1.0 (personal research tool)'}),timeout=30)); break
        except Exception as e: time.sleep(2+2*k)
    if not j: sys.exit(f'Could not find "{name}". Give it as "Town, State", or give a latitude and longitude.')
    la,lo=float(j[0]['lat']),float(j[0]['lon']); words=[w.strip() for w in j[0]['display_name'].split(',')][:4]
    print(f'== {name}: {la:.5f}, {lo:.5f}  ({j[0]["display_name"][:90]})')
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
rows=[]
for l in open(os.path.join(repo,'LEADS.md'),encoding='utf-8'):
    if not l.startswith('|') or l.startswith('| Place') or l.startswith('|---'): continue
    hit=False
    for m in re.finditer(r'(-?\d{2}\.\d{3,}),\s*(-\d{2,3}\.\d{3,})',l):
        if d(float(m.group(1)),float(m.group(2)))<=km*1.5: hit=True
    where=l.split('|')[2] if l.count('|')>3 else l
    if not hit and any(re.search(r'\b'+re.escape(k)+r'\b',where) for k in keys): hit=True
    if hit: rows.append(l.strip())
print(f'== LEADS.md rows for this ground: {len(rows)}'+(' (try these before hunting for new names; delete a row when its place is added)' if rows else ''))
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
print('''== The order of work (GUIDE.md sections 4 to 6 have the detail)
  1. Find places: tools/wiki_raw.py --rows "National Register of Historic Places listings in <County>, <State>" -g 'mill|lock|ruin|site|kiln|fort'
     then tools/wiki_raw.py "Exact title", tools/page.py <url> (reads PDFs; falls back to an archived copy), tools/nom.py "name, town, state".
  2. Write tools/data_<area>.py (BATCH, PLACES, PIN_NOTES). Batch time: copy the output of  date -u '+%Y-%m-%d %H:%M'
  3. Parking for each place: tools/parking.py <lat> <lon>  -> th=[lat,lon], thn='...'
  4. python3 tools/build_sites.py && python3 tools/pincheck.py --batch <key> --lidar ; look at both sheets; move pins with tools/pix.py
  5. ATLAS=$PWD bash tools/all.sh ; the smoke test ; then tools/publish.sh <clone> <branch> ONCE ; then edit GUIDE.md and LEADS.md in the clone.''')
