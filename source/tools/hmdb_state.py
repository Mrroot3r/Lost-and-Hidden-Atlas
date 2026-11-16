#!/usr/bin/env python3
"""Download the lists of historical markers in one state from the Historical Marker Database (HMdb.org), county by
county, for the historic-pockets layer (tools/pockets.py).

   python3 tools/hmdb_state.py "New York" ny        writes cache/hmdb/ny.json and prints which counties are incomplete

The county names come from cache/nrhp/<key>.json, so run tools/nrhp_state.py first.

What is kept: only what a list page shows, and only the marker's number, title, town, county and coordinate.
No inscription, photo or other text is stored.

The rules this tool keeps to:
  - HMdb.org's copyright page allows copying its information without asking, for uses that are not commercial, when it
    is credited to HMdb.org with a link. The Atlas credits and links every marker it shows. Do not reuse this data
    in anything that earns money without written permission from HMdb.org.
  - HMdb.org shows the first 500 markers of any list without signing in and asks for a sign-in beyond that. This tool
    never signs in and never asks for a sixth page. A county with more than 500 markers is therefore incomplete; the
    tool prints those counties, and the pockets there are undercounted. A registered user can download full lists by
    hand from the site.
  - Its robots.txt allows crawling with a short delay; this tool waits several seconds between pages and can be stopped
    and run again (pages already saved are skipped)."""
import sys,os,re,json,time,html,urllib.request,urllib.parse
if len(sys.argv)<3: sys.exit(__doc__)
STATE,KEY=sys.argv[1],sys.argv[2]
UA={'User-Agent':'lost-hidden-atlas-research/1.0 (personal research tool)'}
D=f'cache/hmdb/{KEY}'; os.makedirs(D,exist_ok=True)
ITEM=re.compile(r"<a Name=(\d+)>(.*?)&#8212;\s*<a[^>]*href='\.\./m\.asp\?m=\d+'>(.*?)</a>(.*?)</table>",re.S)
DEST=re.compile(r'destination=(-?[\d.]+),(-?[\d.]+)')
def clean(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',s))).strip(' "“”—-')
def page(county,n):
    p=f'{D}/{re.sub(r"[^A-Za-z]+","_",county)}_{n}.html'
    if os.path.exists(p): return open(p,encoding='utf-8').read()
    u='https://www.hmdb.org/results.asp?'+urllib.parse.urlencode({'Search':'County','County':county,'State':STATE},quote_via=urllib.parse.quote)+(f'&Page={n}' if n>1 else '')
    for k in range(4):
        try:
            t=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=90).read().decode('windows-1252','ignore')
            if 'You Must Sign In' in t: return None
            if 'Just a moment' in t[:600]: raise ValueError('challenge page')
            open(p,'w',encoding='utf-8').write(t); time.sleep(4); return t
        except Exception as e:
            print('  retry',county,n,str(e)[:60],flush=True); time.sleep(30*(k+1))
    raise SystemExit(f'{county} page {n} would not load; run the command again later')
counties=sorted({e['county'] for e in json.load(open(f'cache/nrhp/{KEY}.json')) if e.get('county')})
out={}; short=[]; none=[]
for c in counties:
    names=[c+' County']+([c.replace('St. ','Saint ')+' County'] if 'St. ' in c else [])
    total=0
    for nm in names:
        t=page(nm,1); m=re.search(r'([\d,]+) entr(?:ies|y) match',t or '')
        total=int(m.group(1).replace(',','')) if m else 0
        if total: break
    if not total: none.append(c); continue
    got=0
    for n in range(1,min(5,-(-total//100))+1):
        t=page(nm,n) if n>1 else t
        if not t: break
        for mm in ITEM.finditer(t):
            mid,place,title,rest=mm.groups(); d=DEST.search(rest)
            if not d: continue
            parts=[x.strip() for x in clean(place).split(',')]
            out[mid]={'id':int(mid),'t':clean(title)[:90],'lat':round(float(d.group(1)),5),'lon':round(float(d.group(2)),5),'county':c,'town':parts[2] if len(parts)>2 else ''}; got+=1
    if total>500: short.append((c,total))
    print(f'{c}: {got} of {total}',flush=True)
json.dump(list(out.values()),open(f'cache/hmdb/{KEY}.json','w'),separators=(',',':'),ensure_ascii=False)
json.dump({'short':short,'none':none,'counties':len(counties)},open(f'cache/hmdb/{KEY}_gaps.json','w'))
print('wrote',f'cache/hmdb/{KEY}.json',len(out),'markers from',len(counties)-len(none),'counties')
print('incomplete (more than 500 markers, sign-in needed for the rest):',short)
print('no list found under these names:',none)
