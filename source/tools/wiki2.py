import json,sys,urllib.request,urllib.parse,time,os
UA={'User-Agent':'LostHiddenAtlas/1.0 (personal history mapping project)'}
P='research/wiki2.json'
out=json.load(open(P)) if os.path.exists(P) else {}
titles=[t.strip() for t in open(sys.argv[1]).read().split('\n') if t.strip() and not t.startswith('#')]
need=[t for t in titles if t not in out]
for i in range(0,len(need),18):
    ch=need[i:i+18]
    u='https://en.wikipedia.org/w/api.php?'+urllib.parse.urlencode({'action':'query','format':'json','redirects':1,'prop':'extracts|coordinates|info','exintro':1,'explaintext':1,'exlimit':'max','colimit':'max','inprop':'url','titles':'|'.join(ch)})
    for a in range(5):
        try:
            j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=40)); break
        except Exception as e:
            print('retry',str(e)[:50],file=sys.stderr); time.sleep(6+6*a); j=None
    if not j: continue
    q=j['query']; red={r['from']:r['to'] for r in q.get('redirects',[])}; norm={r['from']:r['to'] for r in q.get('normalized',[])}
    pages={p.get('title'):p for p in q['pages'].values()}
    for t in ch:
        tt=norm.get(t,t); tt=red.get(tt,tt); p=pages.get(tt)
        if not p or 'missing' in p: out[t]=None; continue
        c=(p.get('coordinates') or [{}])[0]
        out[t]={'title':p['title'],'x':p.get('extract') or '','lat':c.get('lat'),'lon':c.get('lon'),'u':p.get('fullurl')}
    json.dump(out,open(P,'w')); time.sleep(2)
n=int(sys.argv[2]) if len(sys.argv)>2 else 420
for t in titles:
    o=out.get(t)
    if o is None: print('--MISSING',t); continue
    print(f"## {t}{'' if o['title']==t else ' => '+o['title']} | {o['lat']},{o['lon']} | {o['x'][:n].replace(chr(10),' ')}")
