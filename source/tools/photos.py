#!/usr/bin/env python3
"""Photo details gathered ahead of time, so a place page shows its picture at once and asks Wikipedia nothing.

   python3 tools/photos.py            look up every place with a Wikipedia article that is not yet in src/photos.json
   python3 tools/photos.py --all      look every one up again (pictures and credits change)
   python3 tools/photos.py --n 300    at most 300 places this run

The app used to ask Wikipedia twice each time a place page opened (which picture, then whose it is), and the page jumped when the
answer came. This asks the same two questions here, fifty places to a request, by the same rules as placePhoto() in app.js: a free
picture, from an article whose coordinates are within 1 km of the pin and whose title shares a word with the place's name, never a
map, a seal or a diagram, and only with a photographer and a licence to credit. What it learns goes in src/photos.json:
  {"asof": "2026-11-19", "p": {place id: [picture address, width, height, photographer, licence, the file's page, article title], or 0}}
0 means looked for, nothing usable. tools/make.py ships it as data/photos.json. A place that is not in the file (written since the
last run) is still asked for when its page opens, as before. Run it again every week or two; it needs the network, so it is not
part of the build. Titles and credits only: no picture is copied."""
import sys,os,re,json,math,time,html,unicodedata,datetime,urllib.parse,requests
HERE=os.path.dirname(os.path.abspath(__file__)); W=os.path.dirname(HERE); os.chdir(W)
UA={'User-Agent':'lost-hidden-atlas-photos/1.0 (https://github.com/Mrroot3r/Lost-and-Hidden-Atlas)'}
API='https://en.wikipedia.org/w/api.php'
COMMON=set('the and of at on in new york north south east west upper lower old great little county city town village historic district site former saint street avenue road park building house hall church school mill works company station state national'.split())
def fold(t): return unicodedata.normalize('NFD',str(t or '').lower()).encode('ascii','ignore').decode()
def words(t): return [w for w in re.split(r'[^a-z0-9]+',fold(t)) if len(w)>=3 and w not in COMMON]
def allw(t): return ' '+' '.join(w for w in re.split(r'[^a-z0-9]+',fold(t).replace('&',' and ')) if w)+' '
def title_of(s):
    """the article a place links, as wikiTitle() in app.js chooses it"""
    for l in s.get('links') or []:
        u=l[1] if isinstance(l,(list,tuple)) else str(l); m=re.match(r'https?://en\.(?:m\.)?wikipedia\.org/wiki/([^#?]+)',u or '')
        if not m: continue
        t=urllib.parse.unquote(m.group(1)).replace('_',' ')
        if re.match(r'(list of|lists of|national register of historic places listings)',t,re.I) or ':' in t: continue
        return t
def fits(s,title,co):
    """photoFits() in app.js"""
    if not co or 'lat' not in co or 'lon' not in co: return False
    d=2*6371000*math.asin(math.sqrt(math.sin(math.radians(co['lat']-s['lat'])/2)**2+math.cos(math.radians(s['lat']))*math.cos(math.radians(co['lat']))*math.sin(math.radians(co['lon']-s['lon'])/2)**2))
    if d>1000: return False
    tt=allw(re.sub(r'\s*\(.*\)\s*$','',title))
    if ' ' in tt.strip() and (tt in allw(s['name']) or tt in allw(s.get('name2'))): return True
    town=set(words(s.get('town'))); mine=set(w for w in words(s['name'])+words(s.get('name2')) if w not in town)
    return any(w not in town and w in mine for w in words(re.sub(r'\s*\(.*\)\s*$','',title)))
def nomail(t):
    """a credit sometimes carries the photographer's e-mail address: the name is credit enough, and the Atlas publishes no addresses"""
    return re.sub(r'\s+',' ',re.sub(r'[\s,;:·|/-]*[(<\[]?\s*(?:mailto:)?[\w.+-]+@[\w-]+(?:\.[\w-]+)+\s*[)>\]]?','',str(t or ''))).strip(' ,;:·|/-')
def by(h):
    """photoBy() in app.js: the photographer's name out of Commons' Artist field"""
    h=str(h or ''); t=nomail(re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',re.sub(r'(?is)<(style|script)[^>]*>.*?</\1>','',h)))).strip())
    if t and len(t)<=70: return t
    for m in re.finditer(r'(?is)<a\b[^>]*href="([^"]*)"[^>]*>(.*?)</a>',h):
        x=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',m.group(2)))).strip()
        if 'User:' in m.group(1) and nomail(x): return nomail(x)[:70]
    if not t or re.search(r'(?i)<(table|img|figure)\b',h): return ''
    return re.sub(r'\s+\S*$','',t[:68])+'…'
def ask(params,tries=40):
    """one question to Wikipedia, patiently: it answers 429 to machines that hurry"""
    p=dict(action='query',format='json',formatversion='2',**params); out=[]
    while True:
        for go in range(tries):
            try:
                r=requests.get(API,params=p,headers=UA,timeout=60)
                if r.status_code==200: break
                wait=int(r.headers.get('retry-after') or 0)        # it says how long to stay away; stay a little longer
            except Exception as ex: r=None; wait=0
            time.sleep(min(120,max(wait,5)+4+3*go))
        else: raise SystemExit('Wikipedia would not answer (last: %s). Run again later; what was learned so far is saved.'%(r.status_code if r is not None else 'no reply'))
        j=r.json(); out.append(j); time.sleep(3)
        if 'continue' not in j: return out
        p.update(j['continue'])
def lookup(todo,P,done=None,tries=40):
    """ask Wikipedia about (place, article title) pairs, fifty to a request, and put each answer in P: the picture's row, or 0 when the
    article has no picture the Atlas may show. It writes no file. done(n) is called after each fifty. tools/photo_find.py asks it
    about one batch's new places; main() below asks it about every place not yet known."""
    for i in range(0,len(todo),50):
        part=todo[i:i+50]; titles=sorted({t for s,t in part}); pages={}; alias={}
        for j in ask(tries=tries,params=dict(redirects='1',prop='pageimages|coordinates',piprop='thumbnail|name',pithumbsize='900',pilicense='free',pilimit='50',colimit='max',titles='|'.join(titles))):
            q=j.get('query') or {}
            for x in (q.get('normalized') or [])+(q.get('redirects') or []): alias[x['from']]=x['to']
            for pg in q.get('pages') or []:
                o=pages.setdefault(pg['title'],{})
                for k in ('thumbnail','pageimage','coordinates'):
                    if k in pg: o[k]=pg[k]
        def page(t):
            for _ in range(4):
                if t in alias: t=alias[t]
            return t,pages.get(t) or {}
        want={}
        for s,t in part:
            tt,pg=page(t); img=pg.get('pageimage')
            if not pg.get('coordinates') or not pg.get('thumbnail') or not img or not fits(s,tt,pg['coordinates'][0]) or re.search(r'\.svg$',img,re.I) or re.search(r'(^|[^a-z])(map|locator|location|seal|flag|logo|coat[ _]of[ _]arms|diagram|plan)([^a-z]|$)',img,re.I): P[s['id']]=0
            else: want[s['id']]=(tt,pg,img)
        files=sorted({'File:'+v[2] for v in want.values()}); info={}; fal={}
        for k in range(0,len(files),50):
            for j in ask(tries=tries,params=dict(prop='imageinfo',iiprop='extmetadata|url',iiextmetadatafilter='Artist|LicenseShortName',titles='|'.join(files[k:k+50]))):
                q=j.get('query') or {}
                for x in q.get('normalized') or []: fal[x['from']]=x['to']
                for pg in q.get('pages') or []:
                    if pg.get('imageinfo'): info[pg['title']]=pg['imageinfo'][0]
        for sid,(tt,pg,img) in want.items():
            f='File:'+img; ii=info.get(fal.get(f,f)) or info.get(f.replace('_',' ')); m=(ii or {}).get('extmetadata') or {}
            who=by((m.get('Artist') or {}).get('value')); lic=by((m.get('LicenseShortName') or {}).get('value'))
            if not ii or not who or not lic: P[sid]=0; continue
            th=pg['thumbnail']; P[sid]=[th['source'],th.get('width',0),th.get('height',0),who,lic,ii.get('descriptionurl') or 'https://commons.wikimedia.org/wiki/File:'+urllib.parse.quote(img),tt]
        if done: done(min(i+50,len(todo)))
    return P
def main():
    a=sys.argv[1:]; n=int(a[a.index('--n')+1]) if '--n' in a else 10**9
    S=json.load(open('build/sites.json',encoding='utf-8')); F='src/photos.json'
    D=json.load(open(F,encoding='utf-8')) if os.path.exists(F) else {'p':{}}
    P={} if '--all' in a else dict(D['p']); live={s['id'] for s in S}
    P={k:v for k,v in P.items() if k in live}
    todo=[(s,title_of(s)) for s in S if title_of(s) and s['id'] not in P][:n]
    print(len(todo),'places to look up;',len(P),'already known')
    if not todo and len(P)==len(D['p']): print('src/photos.json: nothing new to look up; left as it is'); return      # so a build that runs this every time does not rewrite the file for nothing
    def save():
        json.dump({'asof':datetime.date.today().isoformat(),'p':dict(sorted(P.items()))},open(F+'.part','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':')); os.replace(F+'.part',F)      # whole or not at all: a build may be reading it
    lookup(todo,P,lambda k:(save(),print('  %d of %d looked up; %d with a picture so far'%(k,len(todo),sum(1 for v in P.values() if v)))))
    save(); print('src/photos.json: %d places, %d with a picture, %d KB'%(len(P),sum(1 for v in P.values() if v),os.path.getsize(F)//1024))
if __name__=='__main__': main()
