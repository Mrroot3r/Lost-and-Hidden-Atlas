#!/usr/bin/env python3
"""Read Wikipedia articles one at a time as raw text. The search and query APIs are usually throttled (HTTP 429)
from cloud machines; this route has kept working.
   python3 tools/wiki_raw.py "Exact article title" "Another title" ...        prints coordinates and the opening text
   python3 tools/wiki_raw.py -g 'closed|demol|remain|ruin' "Title" ...       prints only sentences matching the pattern
   python3 tools/wiki_raw.py --rows "National Register of Historic Places listings in X County, State"
                                  every row of a Register list: name | town | lat, lon | reference number | description
                                  (add -g pattern to keep only rows that match, e.g. -g 'mill|lock|ruin|site|bridge')
A wrong title prints NO SUCH ARTICLE: titles must be exact, so find them by opening a list or category page first
(for example "National Register of Historic Places listings in <county>") and copying the names from it.
Text is cached under research/wikiraw/ as raw wikitext (templates and references left in): read an article with -g
rather than from the file."""
import sys,os,re,time,urllib.parse,requests
UA={'User-Agent':'lost-hidden-atlas-research/1.0 (personal research tool)'}
a=sys.argv[1:]; pat=None
ROWS='--rows' in a
if ROWS: a.remove('--rows')
if '-g' in a and a.index('-g')+1<len(a):          # -g and its pattern may come before or after the titles (after them they used to be read as titles)
    i=a.index('-g'); pat=re.compile(a[i+1],re.I); a=a[:i]+a[i+2:]
os.makedirs('research/wikiraw',exist_ok=True)
def cache(t):
    """The cache file for a title. An en or em dash gets its own mark: "Hill-Stead Museum" (a redirect) and
    "Hill–Stead Museum" (the article) used to share one file, so the redirect came back as the article, empty."""
    return 'research/wikiraw/'+re.sub(r'[^\w]+','_',t.replace('–',' ndash ').replace('—',' mdash '))+'.txt'
def fetch(t,hop=0,fresh=False):
    p=cache(t)
    if os.path.exists(p) and not fresh: w=open(p,encoding='utf-8').read()
    else:
        r=None
        for k in range(4):
            try:
                r=requests.get('https://en.wikipedia.org/w/index.php',params={'title':t,'action':'raw'},headers=UA,timeout=40)
                if r.status_code in(200,404): break
            except requests.RequestException as e: r=None; err=type(e).__name__      # a reset by the proxy: wait and ask again
            time.sleep(8*(k+1))
        if r is None: return 'no answer (%s)'%err,t
        if r.status_code==404: return None,t
        if r.status_code!=200: return 'HTTP %d'%r.status_code,t
        w=r.text; open(p,'w',encoding='utf-8').write(w); time.sleep(1.5)
    m=re.match(r'\s*#REDIRECT\s*\[\[([^\]|#]+)',w,re.I)
    if m and hop<3:
        n=m.group(1).strip()
        return fetch(n,hop+1,fresh=cache(n)==p)      # a target that maps to this same file (an apostrophe or dash apart) is fetched fresh, not read back as the redirect
    return w,t
def coords(w):
    m=re.search(r'\{\{[Cc]oord\|([^}]*)\}\}',w)
    if not m:
        la=re.search(r'\|\s*lat(?:itude|_d)?\s*=\s*(-?[\d.]+)',w); lo=re.search(r'\|\s*long?(?:itude|_d)?\s*=\s*(-?[\d.]+)',w)
        return (float(la.group(1)),float(lo.group(1))) if la and lo else None
    p=[x.strip() for x in m.group(1).split('|') if x.strip() and '=' not in x and ':' not in x]
    nums=[]; hemi=[]
    for x in p:
        if x in('N','S','E','W'): hemi.append((x,len(nums)))
        else:
            try: nums.append(float(x))
            except ValueError: pass
    try:
        if not hemi: return round(nums[0],5),round(nums[1],5)
        k=hemi[0][1]; dms=lambda v:sum(x/60**i for i,x in enumerate(v))
        la=dms(nums[:k])*(-1 if hemi[0][0]=='S' else 1); lo=dms(nums[k:hemi[1][1]])*(-1 if hemi[1][0]=='W' else 1)
        return round(la,5),round(lo,5)
    except Exception: return None
def clean(w):
    w=re.sub(r'<ref[^>]*/>','',w); w=re.sub(r'<ref[^>]*>.*?</ref>','',w,flags=re.S); w=re.sub(r'<!--.*?-->','',w,flags=re.S)
    w=re.sub(r'\{\{(?:convert|cvt)\|([\d.,]+)\|(?:(?:-|to|and|by|x)\|([\d.,]+)\|)?([^|{}]+)[^{}]*\}\}',lambda m:m.group(1)+('–'+m.group(2) if m.group(2) else '')+' '+m.group(3),w,flags=re.I)   # {{convert|60|ft|m}} -> 60 ft
    w=re.sub(r'\{\{\s*frac\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\}\}',r'\1 \2/\3',w,flags=re.I)      # {{frac|2|1|2}} -> 2 1/2 (was dropped: "a -story house")
    w=re.sub(r'\{\{\s*frac\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\}\}',r'\1/\2',w,flags=re.I)
    for _ in range(5): w=re.sub(r'\{\{[^{}]*\}\}','',w)
    w=re.sub(r'\[\[(?:File|Image):[^\]]*\]\]','',w); w=re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]',r'\1',w); w=re.sub(r"'{2,}",'',w); w=re.sub(r'<[^>]+>','',w)
    w=re.sub(r'\[https?://\S+ ([^\]]*)\]',r'\1',w); w=re.sub(r'^[=|!{}*#:;].*$','',w,flags=re.M)
    return re.sub(r'\s+',' ',w).strip()
for t in a:
    w,real=fetch(t)
    if w is None: print(f'## {t}: NO SUCH ARTICLE (check the exact title)\n'); continue
    if w.startswith(('HTTP ','no answer')): print(f'## {t}: could not fetch ({w}); try again later\n'); continue
    if ROWS:
        w=re.sub(r'<!--.*?-->','',w,flags=re.S); rows=re.findall(r'\{\{NRHP row(.*?)\n\}\}',w,re.S); k=0
        lk=lambda v:re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]',r'\1',re.sub(r'<ref.*','',v,flags=re.S)).strip()
        print(f'## {real}: {len(rows)} rows'+('' if rows else '  (no {{NRHP row}} templates: is this a Register list page? A state-level list links to county lists; open one of those)'))
        for r in rows:
            f=dict((m.group(1),m.group(2).strip()) for m in re.finditer(r'\|\s*(\w+)\s*=\s*([^\n]*)',r))
            line=' | '.join([lk(f.get('name','?')),lk(f.get('city','')),(f.get('lat','')+', '+f.get('lon','')) if f.get('lat') else 'no coordinates (often address restricted)',f.get('refnum',''),lk(f.get('description',''))[:160]])
            if f.get('article') and lk(f['article'])!=lk(f.get('name','')): line+=' | article: '+lk(f['article'])
            if pat and not pat.search(line): continue
            print(' -',line); k+=1
        if pat: print(f'  ({k} of {len(rows)} rows match)')
        print(); continue
    c=coords(w); txt=clean(w)
    if re.search(r'\b(may|can) (also )?refer to\b',txt[:400]) or re.search(r'\{\{\s*(disambiguation|hndis|geodis)',w,re.I):    # a disambiguation page: its choices are list lines, which clean() drops
        ch=[m.group(1) for m in re.finditer(r'^\*+[^\[\n]*\[\[([^\]|#]+)',w,re.M)]
        print(f'## {t}: a disambiguation page, not an article. Ask again with one of these titles:'); print('\n'.join(' - '+x.strip() for x in ch) or ' (no linked choices found)'); print(); continue
    print(f"## {t}"+(f" => {real}" if real!=t else '')+f"  coordinates: {c if c else 'none in the article'}")
    print('https://en.wikipedia.org/wiki/'+urllib.parse.quote(real.replace(' ','_')))
    if pat: print('\n'.join('- '+s for s in re.split(r'(?<=[.!?])\s+(?=[A-Z])',txt) if pat.search(s) and 25<len(s)<400)[:4000])      # one sentence a line
    else:
        print(txt[:1500])
        if len(txt)>1500: print('[... %d characters more: use -g, or read the raw wikitext in %s]'%(len(txt)-1500,cache(real)))
    print()
