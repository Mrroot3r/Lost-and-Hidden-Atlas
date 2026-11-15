import requests,json,time,sys,os,re
UA={'User-Agent':'lost-hidden-atlas-research/1.0 (personal research tool)'}
P='research/wt_ma.json'; C=json.load(open(P)) if os.path.exists(P) else {}
spec=[l.rstrip('\n').split('|',1) for l in open(sys.argv[1]) if l.strip()]
cap=int(sys.argv[2]) if len(sys.argv)>2 else 420
todo=[t for t,_ in spec if t not in C]
for i in range(0,len(todo),25):
    b=todo[i:i+25]
    for a in range(6):
        r=requests.get('https://en.wikipedia.org/w/api.php',params={'action':'query','prop':'revisions','rvprop':'content','rvslots':'main','redirects':1,'titles':'|'.join(b),'format':'json','formatversion':2},headers=UA,timeout=60)
        if r.status_code==200: break
        time.sleep(10+8*a)
    else: print('FAIL batch',i,r.status_code); continue
    q=r.json()['query']; red={x['from']:x['to'] for x in q.get('redirects',[])}; norm={x['from']:x['to'] for x in q.get('normalized',[])}
    by={p['title']:p for p in q['pages']}
    for t in b:
        k=red.get(norm.get(t,t),norm.get(t,t)); p=by.get(k)
        C[t]=p['revisions'][0]['slots']['main']['content'] if p and p.get('revisions') else None
    json.dump(C,open(P,'w')); time.sleep(5)
def clean(w):
    w=re.sub(r'<ref[^>]*/>','',w); w=re.sub(r'<ref[^>]*>.*?</ref>','',w,flags=re.S)
    for _ in range(4): w=re.sub(r'\{\{[^{}]*\}\}','',w)
    w=re.sub(r'\[\[(?:File|Image):[^\]]*\]\]','',w)
    w=re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]',r'\1',w); w=re.sub(r"'{2,}",'',w); w=re.sub(r'<[^>]+>','',w)
    w=re.sub(r'\[https?://\S+ ([^\]]*)\]',r'\1',w); w=re.sub(r'^[=|!{}*#:;].*$','',w,flags=re.M)
    return re.sub(r'\s+',' ',w)
for t,rx in spec:
    w=C.get(t)
    if not w: print('--MISSING',t); continue
    out=[]; n=0
    for s in re.split(r'(?<=[.!?])\s+(?=[A-Z])',clean(w)):
        if re.search(rx,s) and 25<len(s)<330:
            out.append(s); n+=len(s)
            if n>cap: break
    print('##',t,'::',' '.join(out)[:cap+200])
