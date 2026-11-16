#!/usr/bin/env python3
"""Fill the holes in the Park Service's map of National Register listings from Wikidata, for tools/pockets.py.

   python3 tools/wd_nrhp.py ny        writes cache/nrhp/ny_wd.json: [{ref, n, k, lat, lon}]

Why: the Park Service's public map layer (tools/nrhp_state.py) does not hold every listing. Whole downtown districts
are absent from it (Hudson, Ballston Spa, Fort Plain and Round Lake in New York, for example). Wikidata records the
Register's reference number for nearly every listing, with a coordinate. pockets.py adds the listings the Park
Service file lacks.

The first run asks once (a public copy of Wikidata at qlever.dev) for every item in the country that carries a Register reference number and keeps
the answer in cache/wd/nrhp_all.json; every later state is cut from that file without asking again. (Wikidata's
own query service allows very few requests, at times one a minute, so never loop over either.)

What Wikidata does not have is the number of contributing buildings in a district, so a district that comes only from
here is shown without a building count and is ranked as a district of middling size.
Wikidata is in the public domain (CC0)."""
import sys,os,json,time,re,urllib.request,urllib.parse
if len(sys.argv)<2: sys.exit(__doc__)
KEY=sys.argv[1]; RINGS=json.load(open('build/states.json'))[KEY]
ALL='cache/wd/nrhp_all.json'
U='https://qlever.dev/api/wikidata'   # the University of Freiburg's public copy of Wikidata; query.wikidata.org itself was refusing nearly every request when this was written
UA={'User-Agent':'lost-hidden-atlas-research/1.0 (personal research tool)','Accept':'application/sparql-results+json'}
def ask(q):
    for k in range(4):
        try:
            return json.loads(urllib.request.urlopen(urllib.request.Request(U+'?'+urllib.parse.urlencode({'query':q,'format':'json'}),headers=UA),timeout=300).read())['results']['bindings']
        except Exception as ex:
            if k==3: raise
            print('  waiting to retry:',str(ex)[:90],flush=True); time.sleep(70*(k+1))
if not os.path.exists(ALL):
    rows=ask('PREFIX wdt: <http://www.wikidata.org/prop/direct/> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> SELECT ?ref ?c ?l WHERE { ?i wdt:P649 ?ref ; wdt:P625 ?c ; rdfs:label ?l . FILTER(LANG(?l)="en") }')
    got={}
    for b in rows:
        m=re.match(r'POINT\s*\((-?[\d.]+) (-?[\d.]+)\)',b['c']['value'],re.I); ref=b['ref']['value'].strip()
        if m and re.fullmatch(r'\d{8,9}',ref) and not ref.startswith('64'):      # 64…… numbers are cover documents, not places
            got.setdefault(ref,[ref,b['l']['value'].strip(),round(float(m.group(2)),5),round(float(m.group(1)),5)])
    os.makedirs('cache/wd',exist_ok=True); json.dump(list(got.values()),open(ALL,'w'),separators=(',',':'),ensure_ascii=False)
    print('asked Wikidata once:',len(rows),'rows,',len(got),'listings with a coordinate ->',ALL)
def inring(r,x,y):
    ins=False; n=len(r)//2; j=n-1
    for i in range(n):
        xi,yi,xj,yj=r[2*i],r[2*i+1],r[2*j],r[2*j+1]
        if (yi>y)!=(yj>y) and x<(xj-xi)*(y-yi)/(yj-yi)+xi: ins=not ins
        j=i
    return ins
xs=[r[i] for r in RINGS for i in range(0,len(r),2)]; ys=[r[i+1] for r in RINGS for i in range(0,len(r),2)]
W,E,S,N=min(xs),max(xs),min(ys),max(ys)
out=[]
for ref,n,lat,lon in json.load(open(ALL)):
    if not (S<=lat<=N and W<=lon<=E) or sum(1 for r in RINGS if inring(r,lon,lat))%2!=1: continue
    k='district' if re.search(r'\bDistrict\b',n) else 'site' if re.search(r'\b(Site|Battlefield|Mound|Ruins?)\b',n) else 'building'
    out.append({'ref':ref,'n':n,'k':k,'lat':lat,'lon':lon})
os.makedirs('cache/nrhp',exist_ok=True); json.dump(out,open(f'cache/nrhp/{KEY}_wd.json','w'),separators=(',',':'),ensure_ascii=False)
nps={e['ref'] for e in json.load(open(f'cache/nrhp/{KEY}.json'))} if os.path.exists(f'cache/nrhp/{KEY}.json') else set()
new=[e for e in out if e['ref'] not in nps]
print('wrote',f'cache/nrhp/{KEY}_wd.json',len(out),'listings;',len(new),'of them are not in the Park Service file, of which',sum(1 for e in new if e['k']=='district'),'districts')
