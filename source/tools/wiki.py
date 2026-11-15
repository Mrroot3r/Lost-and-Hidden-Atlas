import json,sys,urllib.request,urllib.parse,time,os
UA={'User-Agent':'LostHiddenAtlas/1.0 (personal history mapping project; contact via claude.ai user)'}
def summ(t):
    u='https://en.wikipedia.org/api/rest_v1/page/summary/'+urllib.parse.quote(t.replace(' ','_'),safe='')
    for a in range(3):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))
        except urllib.error.HTTPError as e:
            if e.code==404: return None
            time.sleep(2+3*a)
        except Exception as e: time.sleep(2)
    return {'err':1}
out=json.load(open('research/wiki.json')) if os.path.exists('research/wiki.json') else {}
n=int(sys.argv[2]) if len(sys.argv)>2 else 420
for t in open(sys.argv[1]).read().strip().split('\n'):
    t=t.strip()
    if not t or t.startswith('#'): continue
    if t not in out:
        j=summ(t); time.sleep(0.25)
        out[t]=None if j is None else {'title':j.get('title'),'x':j.get('extract',''),'c':j.get('coordinates'),'u':(j.get('content_urls') or {}).get('desktop',{}).get('page'),'type':j.get('type')}
    o=out[t]
    if o is None: print('--MISSING',t); continue
    c=o.get('c') or {}
    print(f"## {t} | {round(c.get('lat',0),5)},{round(c.get('lon',0),5)}\n{(o.get('x') or '')[:n]}")
json.dump(out,open('research/wiki.json','w'))
