import json,sys,urllib.request,urllib.parse,time,os,re
UA={'User-Agent':'LostHiddenAtlas/1.0 (personal history mapping project)'}
P='research/wikifull.json'
out=json.load(open(P)) if os.path.exists(P) else {}
spec=[l.strip() for l in open(sys.argv[1]).read().split('\n') if l.strip() and not l.startswith('#')]
cap=int(sys.argv[2]) if len(sys.argv)>2 else 600
for line in spec:
    t,_,kw=line.partition('|')
    t=t.strip()
    if t not in out:
        u='https://en.wikipedia.org/w/api.php?'+urllib.parse.urlencode({'action':'query','format':'json','redirects':1,'prop':'extracts|coordinates','explaintext':1,'titles':t})
        j=None
        for a in range(6):
            try: j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=40)); break
            except Exception as e: time.sleep(8+8*a)
        if not j: print('--FAIL',t); continue
        p=list(j['query']['pages'].values())[0]; c=(p.get('coordinates') or [{}])[0]
        out[t]=None if 'missing' in p else {'x':p.get('extract') or '','lat':c.get('lat'),'lon':c.get('lon'),'title':p.get('title')}
        json.dump(out,open(P,'w')); time.sleep(2.5)
    o=out[t]
    if not o: print('--MISSING',t); continue
    rx=re.compile(kw.strip() or r'ruin|remain|foundation|demolish|razed|burn|fire|abandon|closed|today|public|tour|restor|collaps|flood|still stand|vacant|preserv', re.I)
    sents=re.split(r'(?<=[.!?])\s+', re.sub(r'\n+=+[^=]+=+\n+',' ',o['x']).replace('\n',' '))
    hit=[s for s in sents if rx.search(s) and 30<len(s)<420]
    txt=' '.join(hit); 
    print(f"## {t} [{o['lat']},{o['lon']}] {txt[:cap]}")
