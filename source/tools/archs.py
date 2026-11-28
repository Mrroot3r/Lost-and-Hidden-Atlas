#!/usr/bin/env python3
"""Record who designed or built places already on the map. Run from the workspace after tools/build_sites.py.
tools/archrule.py holds the rules and the list of spellings.
   python3 tools/archs.py set <id> "<architect>; <architect>" "<how it is known>" [--builder "<who built it>"]
                                      record it (give "" for the architect when only the builder is known). A place that
                                      already has a row keeps it in the same file; a new one goes in this workspace's own
                                      tools/archs_<four letters>.py, which goes out with tools/publish.sh
   python3 tools/archs.py list [name]  everything recorded in the archs files, or the rows that name somebody
   python3 tools/archs.py count        how many places each name is on, most first (from build/sites.json)
   python3 tools/archs.py wikidata     fill in from Wikidata, in one question: every National Register listing's
                                      architect, matched to the Atlas's places by a Register link on the place or by
                                      the same name within 400 m. Writes rows only for places that name nobody yet.
                                      It asks a public copy of Wikidata ONCE and keeps the answer (cache/wd/nrhp_arch.json):
                                      never loop over it. Wikidata is in the public domain (CC0)."""
import sys,os,re,json,glob,ast,random
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.dont_write_bytecode=True
import archrule as A
HEAD='# Who designed or built a place, found out after it was written (tools/archs.py writes this file; tools/archrule.py holds\n# the rules). id: (architects separated by "; ", builder or \'\', how it is known)\n'
def read(f):
    s=open(f,encoding='utf-8').read(); return ast.literal_eval(s[s.index('ARCH=')+5:])
def files(): return sorted(glob.glob('tools/archs_*.py'))
def allrows():
    d={}
    for f in files(): d.update(read(f))
    return d
def myfile():
    kf='tools/.archs_key'
    if not os.path.exists(kf): open(kf,'w').write(''.join(random.SystemRandom().choice('abcdefghjkmnpqrstvwxyz') for _ in range(4)))
    return 'tools/archs_%s.py'%open(kf).read().strip()
def write(f,d): open(f,'w',encoding='utf-8').write(HEAD+'ARCH={\n'+''.join(' %r:%r,\n'%(k,tuple(d[k])) for k in sorted(d))+'}\n')
def put(rows):
    """write rows {id: row}: a place that has a row keeps it in its file; the rest go in this workspace's own"""
    held={}
    for f in files():
        for k in read(f): held[k]=f
    by={}
    for k,v in rows.items(): by.setdefault(held.get(k) or myfile(),{})[k]=v
    for f,new in by.items():
        d=read(f) if os.path.exists(f) else {}; d.update(new); write(f,d)
    return by
def sites(): return json.load(open('build/sites.json',encoding='utf-8'))
a=sys.argv[1:]
if a[:1]==['set']:
    b=''
    if '--builder' in a: i=a.index('--builder'); b=a[i+1] if i+1<len(a) else ''; a=a[:i]+a[i+2:]
    if len(a)!=4: sys.exit('python3 tools/archs.py set <id> "<architect>; <architect>" "<how it is known>" [--builder "<who built it>"]')
    pid=a[1]; row=('; '.join(A.names(a[2])),'; '.join(A.names(b)),a[3].strip())
    if pid not in {s['id'] for s in sites()}: sys.exit('%s is not a place id (run tools/build_sites.py first if it is new)'%pid)
    p=A.row_problem((a[2],b,a[3]))
    if p: sys.exit('Not recorded: '+p)
    by=put({pid:row}); print('Recorded in %s: %s  %s%s. It goes out with your pull request (tools/publish.sh).'%(list(by)[0],pid,row[0] or '(no architect)',', built by '+row[1] if row[1] else '')); sys.exit(0)
if a[:1]==['list']:
    d=allrows(); q=A.key(a[1]) if len(a)>1 else ''; n=0
    for k in sorted(d):
        if q and q not in A.key(d[k][0]+' '+d[k][1]): continue
        n+=1; print('%-50s %-40s %s'%(k[:50],(d[k][0]+(' / built by '+d[k][1] if d[k][1] else ''))[:40],d[k][2][:70]))
    print('%d place(s).'%n); sys.exit(0)
if a[:1]==['count']:
    import collections; c=collections.Counter(n for s in sites() for n in (s.get('ar') or [])+(s.get('bb') or []))
    for n,k in c.most_common(int(a[1]) if len(a)>1 else 40): print('%4d  %s'%(k,n))
    print('%d names on %d places; %d names are on two or more.'%(len(c),sum(1 for s in sites() if s.get('ar') or s.get('bb')),sum(1 for v in c.values() if v>1))); sys.exit(0)
if a[:1]==['wikidata']:
    import collections,urllib.request,urllib.parse,dupes
    f='cache/wd/nrhp_arch.json'
    if not os.path.exists(f):
        os.makedirs('cache/wd',exist_ok=True)
        q='PREFIX wdt: <http://www.wikidata.org/prop/direct/> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> SELECT ?ref ?a ?al ?s ?sl WHERE { ?i wdt:P649 ?ref . OPTIONAL { ?i wdt:P84 ?a . ?a rdfs:label ?al . FILTER(LANG(?al)="en") } OPTIONAL { ?i wdt:P149 ?s . ?s rdfs:label ?sl . FILTER(LANG(?sl)="en") } FILTER(BOUND(?a)||BOUND(?s)) }'
        r=json.loads(urllib.request.urlopen(urllib.request.Request('https://qlever.dev/api/wikidata?'+urllib.parse.urlencode({'query':q,'format':'json'}),headers={'User-Agent':'lost-hidden-atlas-research/1.0 (personal research tool)','Accept':'application/sparql-results+json'}),timeout=280).read())['results']['bindings']
        json.dump([(b['ref']['value'],b.get('a',{}).get('value','').rsplit('/',1)[-1],b.get('al',{}).get('value',''),b.get('sl',{}).get('value','')) for b in r],open(f,'w'))
    AR=collections.defaultdict(list)
    for ref,qid,al,sl in json.load(open(f)):
        if al and not re.fullmatch(r'Q\d+',al) and al not in AR[ref]: AR[ref].append(al)
    reg={}
    for g in glob.glob('cache/nrhp/*.json'):
        for r in json.load(open(g)):
            if r.get('lat') is not None: reg.setdefault(r['ref'],r)
    if len(reg)<1000: sys.exit('The Register lists are not here (cache/nrhp/<state>.json; tools/nrhp_state.py downloads one). Nothing was written.')
    G=collections.defaultdict(list)
    for r in reg.values(): G[(int(r['lat']/0.01),int(r['lon']/0.01))].append(r)
    def regname(n):      # the Register writes a person's name surname first: "Long, R. A., House"
        m=re.match(r'^([^,]+), ([^,]+?)(, (?:Jr\.|Sr\.|II|III))?, (House|Farm|Building|Homestead|Farmstead|Block|Store|Mill|Barn|Cottage|Estate|School|Mansion|Residence|Hotel|Library)(.*)$',n)
        return ('%s %s %s%s'%(m.group(2),m.group(1),m.group(4),m.group(5))) if m else n
    have=allrows(); rows={}; nlink=0
    for s in sites():
        if s.get('ar') or s['id'] in have or s['id'].startswith('lm-'): continue
        refs={x for x in re.findall(r'(?:NRHP/|NRIS/)(\d{8,9})\b',json.dumps(s.get('links') or []).replace('_text','').replace('_photos','')) if x in reg}; hit=None
        if len(refs)==1: hit=reg[list(refs)[0]]; nlink+=1 if hit['ref'] in AR else 0
        else:
            ca,cb=int(s['lat']/0.01),int(s['lon']/0.01); best=None
            for da in(-1,0,1):
                for db in(-1,0,1):
                    for r in G.get((ca+da,cb+db),()):
                        dm=dupes._m(s['lat'],s['lon'],r['lat'],r['lon'])
                        if dm<=400 and dupes.same_name(dict(name=s['name'],town=s.get('town','')),dict(name=regname(r['n']),town=r.get('town') or '')) and (not best or dm<best[0]): best=(dm,r)
            hit=best and best[1]
        if not hit or hit['ref'] not in AR: continue
        nm=[n for n in A.names(AR[hit['ref']]) if not A._name_problem(n)]
        if nm: rows[s['id']]=('; '.join(nm),'',"Wikidata's entry for National Register listing %s (%s)"%(hit['ref'],hit['n']))
    by=put(rows) if rows else {}
    print('%d place(s) given an architect from Wikidata (%d matched by a Register link on the place, the rest by name within 400 m), in %s.'%(len(rows),nlink,', '.join(by) or 'no file')); sys.exit(0)
sys.exit(__doc__)
