import requests,json,time,sys,os,re
UA={'User-Agent':'lost-hidden-atlas-research/1.0 (personal research tool)'}
P='research/wiki_ma.json'; C=json.load(open(P)) if os.path.exists(P) else {}
T=[t.strip() for t in open(sys.argv[1]) if t.strip()]
todo=[t for t in T if t not in C]
for i in range(0,len(todo),18):
    b=todo[i:i+18]
    for a in range(6):
        r=requests.get('https://en.wikipedia.org/w/api.php',params={'action':'query','prop':'extracts|coordinates','exintro':1,'explaintext':1,'exlimit':20,'colimit':50,'redirects':1,'titles':'|'.join(b),'format':'json'},headers=UA,timeout=40)
        if r.status_code==200: break
        time.sleep(8+6*a)
    else: print('FAIL batch',i); continue
    q=r.json()['query']; red={x['from']:x['to'] for x in q.get('redirects',[])}; norm={x['from']:x['to'] for x in q.get('normalized',[])}
    by={p['title']:p for p in q['pages'].values()}
    for t in b:
        k=red.get(norm.get(t,t),norm.get(t,t)); p=by.get(k)
        if not p or 'missing' in p: C[t]=None; continue
        co=p.get('coordinates',[{}])[0]
        C[t]={'title':k,'lat':co.get('lat'),'lon':co.get('lon'),'x':p.get('extract','')}
    json.dump(C,open(P,'w')); time.sleep(4)
n=int(sys.argv[2]) if len(sys.argv)>2 else 380
for t in T:
    c=C.get(t)
    if not c: print('--MISSING',t); continue
    print(f"## {t}{' => '+c['title'] if c['title']!=t else ''} [{c['lat']},{c['lon']}] {re.sub(chr(10)+'+',' ',c['x'])[:n]}")
