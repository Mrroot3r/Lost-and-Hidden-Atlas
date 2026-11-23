#!/usr/bin/env python3
"""Hours: when a place is open, looked up after it was written. Readers want to know when they can get inside, churches most of all.

   python3 tools/hours.py                         how many places that take visitors have hours, and how many wait, state by state
   python3 tools/hours.py list [state|region] [--kind worship] [--n 30]
                                                  standing places of worship, and open-to-visitors places, with no hours on record,
                                                  each with its town and links (in a different order each time)
   python3 tools/hours.py set <id> "<days and times>" <address of the page> [--open]
                                                  record them in tools/hours_<four letters>.py (this workspace's own file, so sessions
                                                  working side by side do not collide), with today's date. --open: the page shows the
                                                  place lets visitors in (a church with open hours, tours or services anyone may attend),
                                                  so a place marked "view from the public way" becomes "open to visitors"
   python3 tools/hours.py page <address> [<address> ...]
                                                  read a page frugally: only its lines with clock times, and its address and
                                                  telephone lines (to prove it is this building and not a namesake)
   python3 tools/hours.py set <id> "?" <address of the page you tried>
                                                  looked for and not found: nothing is shown, and the place stops being listed

The rule: hours are a fact like any other, so they come from a page you opened in this session, and it must be the page of whoever
runs the place (the parish's or congregation's own site, its diocese's or denomination's listing for it, the museum's own page), not a
map listing, a review site or memory. Make sure the page is for THIS building: churches share names, and parishes merge and move their
Masses. Give service times as the page gives them, and say when the building is open outside services if the page says so
("Sunday 9 and 11 a.m.; open for prayer weekdays 12 to 1"). One row, 180 characters at most: seasons first when they differ, then
days, then times. If the page says the church is closed, sold or has no regular services, say that ("No regular services; open for
concerts") rather than '?'. Find the page with a web search for the name and town; read it with tools/page.py."""
import sys,os,re,json,random,importlib,datetime
HERE=os.path.dirname(os.path.abspath(__file__)); W=os.path.dirname(HERE); os.chdir(W); sys.path.insert(0,HERE); sys.dont_write_bytecode=True
if not os.path.exists('build/sites.json') or '--fresh' in sys.argv: os.system(sys.executable+' tools/build_sites.py > /dev/null')
S=json.load(open('build/sites.json',encoding='utf-8')); BY={s['id']:s for s in S}
from states import STATES
REGST={c:st['k'] for st in STATES for c,l in st['regions']}; STNAME={st['k']:st['name'] for st in STATES}
def myfile():
    kf=os.path.join(W,'.hourskey')
    if not os.path.exists(kf): open(kf,'w').write(''.join(random.SystemRandom().choice('abcdefghjkmnpqrstvwxyz') for _ in range(4)))
    return 'tools/hours_%s.py'%open(kf).read().strip()
def tried():
    import glob; t=set()
    for f in glob.glob('tools/hours_*.py'): t|=set(importlib.import_module(os.path.basename(f)[:-3]).HOURS)
    return t
SHUT=re.compile(r'derelict|vacant|closed\b(?! (?:mon|tue|wed|thu|fri|sat|sun|for the season|in winter|on))|not open|no longer (?:a church|used)|private (?:home|house|residence)|now (?:a|an) (?:house|home|residence|apartment)|apartments|deconsecrated',re.I)
def wants(s):      # a church that is plainly shut or turned into a house is not asked
    return s['st']=='standing' and not s.get('mine') and (s['acc']=='open' or (s['cat']=='worship' and s['acc'] in('view','public') and not SHUT.search(s.get('accn') or '')))
def waiting(): T=tried(); return [s for s in S if wants(s) and not s.get('hrs') and s['id'] not in T and not s['id'].startswith('lm-')]      # a thin landmark pin has no place list of its own to take hours: check.py refuses one in an hours file
a=[x for x in sys.argv[1:] if x!='--fresh']
if not a:
    by={}; T=tried()
    for s in S:
        if not wants(s): continue
        r=by.setdefault(REGST.get(s['reg'],'?'),[0,0,0,0]); w=s['cat']=='worship'
        r[(0 if s.get('hrs') else 1)+(0 if w else 2)]+=0 if (not s.get('hrs') and s['id'] in T) else 1
    print('Standing places that take visitors:  places of worship with hours / without   |   others with hours / without')
    for k in sorted(by,key=lambda k:-(by[k][1]+by[k][3])):
        if by[k][1]+by[k][3]>1: print('  %-22s %4d %4d   | %4d %4d'%(STNAME.get(k,k),*by[k]))
    t=[sum(v[i] for v in by.values()) for i in range(4)]; print('  %-22s %4d %4d   | %4d %4d'%('all',*t)); sys.exit(0)
if a[0]=='list':
    n=30; kind=None; rest=[]; i=1
    while i<len(a):
        if a[i]=='--n': n=int(a[i+1]); i+=2
        elif a[i]=='--kind': kind=a[i+1]; i+=2
        else: rest.append(a[i]); i+=1
    w=waiting()
    if kind: w=[s for s in w if s['cat']==kind]
    if rest:
        q=' '.join(rest).lower(); st=[k for k,v in STNAME.items() if v.lower()==q or k==q]
        w=[s for s in w if (st and REGST.get(s['reg'])==st[0]) or s['reg']==q]
    random.SystemRandom().shuffle(w)
    print(len(w),'places wait'+(' there' if rest else '')+'; the first',min(n,len(w)),':')
    for s in w[:n]:
        links=[(l[1] if isinstance(l,(list,tuple)) else str(l)) for l in (s.get('links') or [])][:2]
        print('  %s | %s, %s, %s | %s | %s\n      note: %s'%(s['id'],s['name'],s['town'],STNAME.get(REGST.get(s['reg']),''),s['acc'],'  '.join(links) or 'no link',(s.get('accn') or '')[:200]))
    print('Next: find the page of whoever runs it, read it, then   python3 tools/hours.py set <id> "<days and times>" <page address> [--open]'); sys.exit(0)
if a[0]=='page':
    import requests,html
    TM=re.compile(r"\b\d{1,2}(?::\d\d)? ?(?:a\.?m\.?|p\.?m\.?)\b|\bnoon\b",re.I); IDL=re.compile(r"\b[A-Z]{2}\b,? ?\d{5}|\b\d{3}[-.) ]\d{3}[-.]\d{4}\b|\b[A-Z]\d[A-Z] ?\d[A-Z]\d\b")
    for u in a[1:]:
        try: r=requests.get(u,headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) lost-hidden-atlas-research/1.0 (https://github.com/Mrroot3r/Lost-and-Hidden-Atlas)'},timeout=40); t=r.text
        except Exception as ex: print('##',u,'could not be read:',str(ex)[:70]); continue
        t=re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>',' ',t); t=re.sub(r'(?i)<(br|/p|/div|/li|/h\d|/tr|/td)[^>]*>','\n',t); t=html.unescape(re.sub(r'<[^>]+>',' ',t))
        L=[x for x in (re.sub(r'\s+',' ',x).strip() for x in t.split('\n')) if x]; seen=set(); n=0
        print('## %s (HTTP %d, %d lines of text)%s'%(u,r.status_code,len(L),'' if len(L)>8 else '  <- nearly empty: drawn by script or refused; try tools/page.py or another page of the site'))
        for k,x in enumerate(L):
            if (TM.search(x) or IDL.search(x)) and x not in seen and n<16:
                seen.add(x); n+=1; print('  -',((L[k-1]+' / ') if k and len(L[k-1])<60 and not TM.search(L[k-1]) else '')[:70]+x[:240])
    sys.exit(0)
if a[0]=='set':
    op='--open' in a; a=[x for x in a if x!='--open']
    if len(a)<4: sys.exit('usage: hours.py set <id> "<days and times, or ?>" <address of the page> [--open]')
    i,h,u=a[1],a[2].strip(),a[3].strip()
    if i not in BY: sys.exit('No such place id: '+i)
    if not h or len(h)>180: sys.exit('The hours are one row: 1 to 180 characters (this is %d). Put the rest in a note for the next session.'%len(h))
    if not re.match(r'https?://[^\s<>"]+$',u): sys.exit('Give the address of the page the hours were read on (http:// or https://).')
    if h!='?' and not re.search(r'\d|noon|appointment|services?|closed|no regular|daily|every day|weekends?|sunrise|sunset|dawn|dusk|daylight|year.round|summer|winter|spring|autumn|fall|season|(mon|tues|wednes|thurs|fri|satur|sun)day',h,re.I): sys.exit('That does not read as days and times. Use "?" if the page gives none.')
    f=myfile(); cur={}
    if os.path.exists(f): cur=dict(importlib.import_module(os.path.basename(f)[:-3]).HOURS)
    cur[i]=(h,datetime.date.today().isoformat(),u,True) if op else (h,datetime.date.today().isoformat(),u)
    open(f,'w',encoding='utf-8').write('# Hours, looked up after the places were written (tools/hours.py set). id: (hours or ?, day read, page, [opens to visitors])\nHOURS={\n'+''.join(' %r:%r,\n'%(k,v) for k,v in sorted(cur.items()))+'}\n')
    print('Recorded in %s: %s%s (%d in this file). It reaches the map at the next build.'%(f,i,' (now open to visitors)' if op and BY[i]['acc'] in('view','public') else '',len(cur))); sys.exit(0)
sys.exit(__doc__)
