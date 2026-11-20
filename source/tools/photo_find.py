#!/usr/bin/env python3
"""Find a photograph for a place that has none, among the freely licensed ones on Wikimedia Commons taken near its pin.

   python3 tools/photo_find.py                         how many places have no picture, state by state
   python3 tools/photo_find.py list "<state>" --n 30   thirty of them, in a different order each time
   python3 tools/photo_find.py look <place id> ...     the candidates for each: a numbered sheet to LOOK at (research/photofind_<id>.jpg)
                                                       and a list (distance from the pin, the file's name and description, who, licence)
   python3 tools/photo_find.py set <place id> <n>      choose candidate n from that sheet
   python3 tools/photo_find.py set <place id> none "<why>"     looked, and none of them shows this place
   python3 tools/photo_find.py sheet [<pics file>]     one sheet of everything chosen in a file, each beside its place's name, for a second look

Why: about half the places have a picture, all from the lead image of their own Wikipedia article (tools/photos.py). The other
half have no article or an article with no usable picture, and a reader hunting a ruin in the woods wants to know what he is
looking for. Commons holds millions of photographs that carry the spot they were taken from.

What the tool decides, so that no session can get it wrong: only Wikimedia Commons; only a photograph (never a map, a plan, a
seal, a logo or a drawing file); only a free licence (CC BY, CC BY-SA, CC0, public domain) and a photographer to credit; only one
taken within reach of the pin (150 m for an exact pin, 250 m for a site, 400 m for an area) or, when fewer than four were, one
whose own name and description hold the town and every telling word of the place's name (marked BY NAME ONLY in red: look twice
at those, a namesake is the classic mistake). The address, the size, the credit and the licence are copied from Commons by the
tool, never typed.

What the session decides, by looking: WHICH of the candidates, if any, shows THIS place. Read the place's name and description,
read each candidate's file name and description, and look at the sheet. Choose one that shows the building, ruin or site from
outside, as someone arriving would see it. If none plainly does, say `none`: a wrong picture is worse than no picture. A
namesake down the street, an interior, a plaque close-up, a view from the place of something else, a person: none of these.

Choices go in tools/pics_<four letters>.py (PICS = {place id: (address, width, height, photographer, licence, the file's page,
day chosen)} or ('', day, why) for "none fits"), which tools/make.py folds into data/photos.json. A picture from a place's own
Wikipedia article still wins. Nothing is copied but an address and a credit. Test: tools/photo_find_test.py."""
import sys,os,re,json,math,time,html,random,datetime,glob,importlib
HERE=os.path.dirname(os.path.abspath(__file__)); W=os.path.dirname(HERE)
UA={'User-Agent':'lost-hidden-atlas-photos/1.0 (https://github.com/Mrroot3r/Lost-and-Hidden-Atlas)'}
API='https://commons.wikimedia.org/w/api.php'
FREE=re.compile(r'^(CC BY(-SA)?( \d(\.\d)?)?( [a-z]{2,3})?|CC0( 1\.0)?|Public domain|PD[- ].*|No restrictions)$',re.I)
NOTPHOTO=re.compile(r'\b(map|maps|plan|plans|diagram|logo|seal|coat of arms|flag|locator|location|survey|chart|drawing|sketch|blueprint|elevation|postmark|signature|sanborn|topo|usgs|aerial)\b',re.I)
REACH={'exact':150,'site':250,'area':400}
def nomail(t):
    """a credit sometimes carries the photographer's e-mail address: the name is credit enough, and the Atlas publishes no addresses"""
    return re.sub(r'\s+',' ',re.sub(r'[\s,;:·|/-]*[(<\[]?\s*(?:mailto:)?[\w.+-]+@[\w-]+(?:\.[\w-]+)+\s*[)>\]]?','',str(t or ''))).strip(' ,;:·|/-')
def credit(h):
    """the photographer's name out of Commons' Artist field (the same rule as by() in tools/photos.py and photoBy() in app.js)"""
    h=str(h or ''); t=nomail(re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',re.sub(r'(?is)<(style|script)[^>]*>.*?</\1>','',h)))).strip())
    if t and len(t)<=70: return t
    for m in re.finditer(r'(?is)<a\b[^>]*href="([^"]*)"[^>]*>(.*?)</a>',h):
        x=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',m.group(2)))).strip()
        if 'User:' in m.group(1) and nomail(x): return nomail(x)[:70]
    if not t or re.search(r'(?i)<(table|img|figure)\b',h): return ''
    return re.sub(r'\s+\S*$','',t[:68])+'…'
def usable(c):
    """'' when a candidate may be offered, else the reason it may not. c: title, mime, width, height, lic, artist"""
    if c.get('mime') not in('image/jpeg','image/png'): return 'not a photograph file'
    if not FREE.match(str(c.get('lic') or '').strip()): return 'no free licence'
    if not credit(c.get('artist')): return 'no photographer to credit'
    w,h=c.get('width') or 0,c.get('height') or 0
    if w<800 or h<500: return 'too small'
    if w/h>3 or h/w>2.2: return 'a sliver, not a view'
    if NOTPHOTO.search(re.sub(r'[_\-.]',' ',str(c.get('title') or ''))): return 'reads as a map, a plan or an emblem'
    return ''
COMMON=set('the and of at on in new old north south east west upper lower great little county city town village historic district site former saint street avenue road park building house hall church ruins ruin mill bridge station school farm company works first second'.split())
def fold(t):
    import unicodedata
    return unicodedata.normalize('NFD',str(t or '').lower()).encode('ascii','ignore').decode()
def name_words(name,town=None):
    """the telling words of a place's name: not 'the', 'house', 'church' and the like. When nothing is left but the town's own name
    ("Charlottetown City Hall"), the plain words stay too, or every photograph of the town would count as naming the place"""
    allw=[w for w in re.split(r'[^a-z0-9]+',fold(re.sub(r'\(.*?\)','',str(name or '')))) if len(w)>=3]
    nw=[w for w in allw if w not in COMMON]
    tw=set(re.split(r'[^a-z0-9]+',fold(town or ''))) if town else set()
    if town and not [w for w in nw if w not in tw]: return [w for w in allw if w not in('the','and')]
    return nw
def names_it(text,nw,town):
    """does a file's name and description name this place: the town, and every telling word of the place's name"""
    t=' '+re.sub(r'[^a-z0-9]+',' ',fold(text))+' '
    return bool(nw) and bool(town) and (' '+re.sub(r'[^a-z0-9]+',' ',town).strip()+' ') in t and all((' '+w) in t for w in nw)
def write_pick(path,pid,row):
    """add or replace one place's row in a pics file, keeping the rest"""
    P={}
    if os.path.exists(path):
        import ast
        for n in ast.parse(open(path,encoding='utf-8').read()).body:
            if isinstance(n,ast.Assign) and getattr(n.targets[0],'id','')=='PICS': P=dict(ast.literal_eval(n.value))
    P[pid]=tuple(row)
    with open(path,'w',encoding='utf-8') as f:
        f.write('# Pictures found on Wikimedia Commons near a place\'s pin, chosen by looking (tools/photo_find.py). Data only.\n')
        f.write('# id: (picture address, width, height, photographer, licence, the file\'s page on Commons, day chosen)   or   (\'\', day, why none fits)\n')
        f.write('PICS={\n'+''.join(' %r:%r,\n'%(k,P[k]) for k in sorted(P))+'}\n')
def merge(p,pics,ids):
    """what data/photos.json holds: the article pictures (p), then a found picture wherever a place has none. ids: the places that exist"""
    out={k:v for k,v in p.items() if k in ids}
    for k,v in pics.items():
        if k not in ids or not v or not v[0] or out.get(k): continue
        out[k]=[v[0],v[1],v[2],v[3],v[4],v[5],'']
    return out
def _day(v): return str(v[1] if not v[0] else v[6])
def all_pics(folder=None):
    """every recorded choice. Where two files answer for one place the later day wins (a picture found after an earlier "none", or a
    "none" that takes a wrong picture away); on the same day a picture wins over "none"."""
    P={}; folder=folder or HERE
    import ast
    for f in sorted(glob.glob(os.path.join(folder,'pics_*.py'))):
        for n in ast.parse(open(f,encoding='utf-8').read()).body:
            if not(isinstance(n,ast.Assign) and getattr(n.targets[0],'id','')=='PICS'): continue
            for k,v in ast.literal_eval(n.value).items():
                o=P.get(k)
                if o is None or _day(v)>_day(o) or (_day(v)==_day(o) and (v[0] or not o[0])): P[k]=tuple(v)
    return P
WIDENED='2026-11-21'      # from this day the finder always asks for photographs that name the place, not only ones taken at the pin
def asked_again(v):
    """a "none" recorded before the search was widened is offered once more: the wider search may now have a picture for it"""
    return bool(v) and not v[0] and str(v[1])<WIDENED
def rank(C,nw,town):
    """candidates in the order shown: those whose own name and description name the place first (taken at the pin before those with no
    position), then the rest, nearest first"""
    def key(c):
        named=names_it(str(c.get('title') or '')+' '+str(c.get('desc') or ''),nw,town)
        return (0 if named else 1, 0 if c.get('m') is not None else 1, c.get('m') or 0)
    return sorted(C,key=key)
def no_article(p):
    """a place with no Wikipedia article of its own: the page has no article picture to show, so a session looks for one"""
    return not any('en.wikipedia.org/wiki/' in str(l[1] if isinstance(l,(list,tuple)) and len(l)>1 else l) for l in (p.get('links') or []))
def new_places(P,done,nopic=()):
    """of one batch's places, those a research session should look for a picture for: something still there, no answer yet, and either
    no article or (nopic) an article that turned out to have no picture the Atlas may show"""
    return [p for p in P if p.get('st')!='gone' and (no_article(p) or p['id'] in nopic) and (p['id'] not in done or asked_again(done[p['id']]))]
def id_ok(i,ids):
    """may a pics file answer for this id: a place in a place list, or a landmark pin (lm-...), which build_sites.py makes and no list holds"""
    return i in ids or bool(re.fullmatch(r'lm-[a-z0-9-]+',str(i)))
# ---------------------------------------------------------------- the commands
def _sites():
    os.chdir(W)
    if not os.path.exists('build/sites.json'): os.system(sys.executable+' tools/build_sites.py > /dev/null')
    return json.load(open('build/sites.json',encoding='utf-8'))
def _myfile():
    kf=os.path.join(W,'.picskey')
    if not os.path.exists(kf): open(kf,'w').write(''.join(random.SystemRandom().choice('abcdefghjkmnpqrstvwxyz') for _ in range(4)))
    return os.path.join(W,'tools','pics_%s.py'%open(kf).read().strip())
def _waiting(S):
    ph=json.load(open('src/photos.json',encoding='utf-8'))['p'] if os.path.exists('src/photos.json') else {}
    done=all_pics()
    wiki=lambda s:not no_article(s)
    # waiting: its own article gave no usable picture (0 in photos.json), or it has no article at all. A place with an article that
    # tools/photos.py has not asked about yet is left for that tool first.
    done={k for k,v in done.items() if not asked_again(v)}
    return [s for s in S if not s.get('mine') and s['st']!='gone' and s['id'] not in done and (ph.get(s['id'])==0 or (s['id'] not in ph and not wiki(s)))]
def refused(j):
    """Commons answered, but with an error in place of results. That is not the same as finding nothing"""
    return isinstance(j,dict) and 'error' in j
def _get(params,tries=8):
    import requests
    for k in range(tries):
        r=requests.get(API,params=dict(params,format='json',formatversion='2'),headers=UA,timeout=60)
        if r.status_code==429 or r.status_code>=500: time.sleep(min(90,int(r.headers.get('Retry-After') or 0) or 8*(k+1))); continue
        r.raise_for_status(); j=r.json()
        if refused(j):
            if k>=3: raise SystemExit('Wikimedia Commons answered with an error: %s. Nothing was recorded; run the same command again later.'%str(j['error'].get('code') if isinstance(j['error'],dict) else j['error'])[:80])
            time.sleep(8*(k+1)); continue        # an error inside a 200 reply (too busy, too many requests): never read it as "nothing here"
        return j
    raise SystemExit('Wikimedia Commons keeps refusing (too many requests). Wait a few minutes and run the same command again.')
def _hav(a,b,c,d):
    p=math.pi/180; h=math.sin((c-a)*p/2)**2+math.cos(a*p)*math.cos(c*p)*math.sin((d-b)*p/2)**2
    return 2*6371000*math.asin(math.sqrt(h))
def _plain(t,n=140): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',str(t or '')))).strip()[:n]
def look(s):
    import requests,io
    from PIL import Image,ImageDraw
    reach=REACH.get(s.get('prec') or 'site',250)
    j=_get(dict(action='query',generator='geosearch',ggsnamespace='6',ggscoord='%s|%s'%(s['lat'],s['lon']),ggsradius=str(reach),ggslimit='60',
                prop='imageinfo|coordinates',coprimary='all',iiprop='url|size|mime|extmetadata',iiurlwidth='900',iiextmetadatafilter='LicenseShortName|Artist|ImageDescription|DateTimeOriginal'))
    C=[]
    for pg in (j.get('query') or {}).get('pages',[]):
        ii=(pg.get('imageinfo') or [None])[0]
        if not ii: continue
        m=ii.get('extmetadata') or {}; co=(pg.get('coordinates') or [{}])[0]
        c=dict(title=pg['title'],mime=ii.get('mime'),width=ii.get('width'),height=ii.get('height'),lic=_plain((m.get('LicenseShortName') or {}).get('value'),40),artist=(m.get('Artist') or {}).get('value'),
               desc=_plain((m.get('ImageDescription') or {}).get('value')),when=_plain((m.get('DateTimeOriginal') or {}).get('value'),10),src=ii.get('thumburl'),tw=ii.get('thumbwidth'),th=ii.get('thumbheight'),page=ii.get('descriptionurl'),
               m=round(_hav(s['lat'],s['lon'],co['lat'],co['lon'])) if 'lat' in co else None)
        if usable(c) or not c['src'] or not c['page'] or c['m'] is None or c['m']>reach: continue
        C.append(c)
    C.sort(key=lambda c:c['m']); C=C[:12]
    town=fold((s.get('town') or '').split(',')[0].split('(')[0]).strip(); nw=name_words(s.get('name'),town)
    # Second, always (since November 20, 2026; before that only when fewer than four were taken near the pin, and the first batch showed
    # why that was wrong: a ranch and a city hall each had four poor photographs nearby and good ones elsewhere on Commons that were never
    # asked for): photographs that NAME the place. Many carry no camera position, so the tool asks for the file's name and description to
    # hold the town and every telling word of the place's name before it offers one.
    if True:
        have={c['title'] for c in C}
        if nw and town:
            j=_get(dict(action='query',generator='search',gsrnamespace='6',gsrlimit='30',gsrsearch='%s %s'%(re.sub(r'\(.*?\)','',s['name']).strip(),(s.get('town') or '').split(',')[0]),
                        prop='imageinfo|coordinates',coprimary='all',iiprop='url|size|mime|extmetadata',iiurlwidth='900',iiextmetadatafilter='LicenseShortName|Artist|ImageDescription|DateTimeOriginal'))
            for pg in (j.get('query') or {}).get('pages',[]):
                ii=(pg.get('imageinfo') or [None])[0]
                if not ii or pg['title'] in have: continue
                m=ii.get('extmetadata') or {}; co=(pg.get('coordinates') or [{}])[0]
                c=dict(title=pg['title'],mime=ii.get('mime'),width=ii.get('width'),height=ii.get('height'),lic=_plain((m.get('LicenseShortName') or {}).get('value'),40),artist=(m.get('Artist') or {}).get('value'),
                       desc=_plain((m.get('ImageDescription') or {}).get('value')),when=_plain((m.get('DateTimeOriginal') or {}).get('value'),10),src=ii.get('thumburl'),tw=ii.get('thumbwidth'),th=ii.get('thumbheight'),page=ii.get('descriptionurl'),m=None,byname=True)
                if usable(c) or not c['src'] or not c['page'] or not names_it(c['title']+' '+c['desc'],nw,town): continue
                if 'lat' in co:
                    c['m']=round(_hav(s['lat'],s['lon'],co['lat'],co['lon']))
                    if c['m']>1500: continue          # it carries a position, and the position is somewhere else: a namesake
                C.append(c)
    C=rank(C,nw,town) if nw and town else C
    named=[c for c in C if nw and town and names_it(c['title']+' '+c['desc'],nw,town)][:8]; C=named+[c for c in C if c not in named][:12-len(named)]
    print('\n== %s  |  %s, %s  |  %s  |  %s pin'%(s['id'],s['name'],s.get('town',''),s.get('years',''),s.get('prec','')))
    print('   '+_plain(s.get('story') or s.get('note') or '',300))
    os.makedirs('research',exist_ok=True)
    json.dump(C,open('research/photofind_%s.json'%s['id'],'w',encoding='utf-8'))
    if not C: print('   No free photograph on Commons was taken within %d m of the pin, and none names the place.  ->  python3 tools/photo_find.py set %s none "nothing on Commons within %d m"'%(reach,s['id'],reach)); return
    tiles=[]
    for n,c in enumerate(C,1):
        im=None
        for k in range(3):          # a refused download (429) is tried again; a grey tile hides a candidate from whoever chooses
            try:
                r=requests.get(re.sub(r'/\d+px-','/330px-',c['src'].split('?')[0]),headers=UA,timeout=60); r.raise_for_status(); im=Image.open(io.BytesIO(r.content)).convert('RGB'); break
            except Exception: time.sleep(6*(k+1))
        if im is None: im=Image.new('RGB',(330,220),(90,90,90)); c['grey']=True
        im.thumbnail((330,250)); t=Image.new('RGB',(340,286),(255,255,255)); t.paste(im,((340-im.width)//2,30+(250-im.height)//2)); d=ImageDraw.Draw(t); d.text((6,4),'%d   %s'%(n,('%d m from the pin'%c['m']) if c['m'] is not None and not c.get('byname') else 'BY NAME ONLY'+(' (%d m)'%c['m'] if c['m'] is not None else ', no position')),fill=(0,0,0) if not c.get('byname') else (170,0,0)); d.text((6,17),c['title'][5:60],fill=(0,70,160)); tiles.append(t)
        print('  %2d  %s  %s  |  %s  |  %s, %s%s'%(n,('%3d m'%c['m']) if not c.get('byname') else 'by name'+(' %d m'%c['m'] if c['m'] is not None else ''),c['title'][5:75],c['desc'][:110] or '(no description)',credit(c['artist']),c['lic'],', '+c['when'][:4] if c['when'] else ''))
        time.sleep(0.4)
    cols=4; rows=(len(tiles)+cols-1)//cols; sheet=Image.new('RGB',(cols*340,rows*286),(255,255,255))
    for i,t in enumerate(tiles): sheet.paste(t,((i%cols)*340,(i//cols)*286))
    out='research/photofind_%s.jpg'%s['id']; sheet.save(out,quality=82)
    print('   LOOK at %s, then:  python3 tools/photo_find.py set %s <n>   or   set %s none "<why>"'%(out,s['id'],s['id']))
def main(a):
    S=_sites(); BY={s['id']:s for s in S}
    from states import STATES
    REGST={c:st['k'] for st in STATES for c,l in st['regions']}; STNAME={st['k']:st['name'] for st in STATES}
    today=datetime.date.today().isoformat()
    if not a:
        Wt=_waiting(S); n={}
        for s in Wt: n[REGST.get(s['reg'],'?')]=n.get(REGST.get(s['reg'],'?'),0)+1
        print('%d places have no picture (of %d):'%(len(Wt),len(S)))
        for k,v in sorted(n.items(),key=lambda x:-x[1]): print('  %-22s %d'%(STNAME.get(k,k),v))
        return
    if a[0]=='list':
        n=int(a[a.index('--n')+1]) if '--n' in a else 30; st=[x for x in a[1:] if x!='--n' and not x.isdigit()]
        Wt=_waiting(S)
        if st: key=next((k for k,v in STNAME.items() if v.lower()==st[0].lower() or k==st[0].lower()),None); Wt=[s for s in Wt if REGST.get(s['reg'])==key or s['reg']==st[0]]
        random.shuffle(Wt)
        for s in Wt[:n]: print('%s  |  %s, %s  |  %s'%(s['id'],s['name'],s.get('town',''),s['st']))
        print('\n%d listed of %d waiting%s. Next:  python3 tools/photo_find.py look %s'%(min(n,len(Wt)),len(Wt),' there' if st else '',' '.join(s['id'] for s in Wt[:6])+(' ...' if len(Wt)>6 else '')))
        return
    if a[0]=='new':
        # a research session, for the places it has just written: python3 tools/photo_find.py new data_cortland_qhzm
        if len(a)<2: sys.exit('new <your data file>, for example: new data_cortland_qhzm')
        nm=os.path.basename(a[1]).replace('.py','')
        try: P=importlib.import_module(nm).PLACES
        except Exception as e: sys.exit('Cannot read tools/%s.py (%s)'%(nm,str(e)[:80]))
        os.system(sys.executable+' tools/build_sites.py > /dev/null'); BY={s['id']:s for s in _sites()}
        # a place with an article shows the article's picture by itself, if it has one the Atlas may show. Ask which do not (the same
        # question tools/photos.py asks, for this batch only, writing nothing): those are looked for on Commons like the ones with no article.
        import photos
        linked=[(BY[p['id']],photos.title_of(BY[p['id']])) for p in P if p['id'] in BY and photos.title_of(BY[p['id']])]
        try: R=photos.lookup(linked,{},tries=6) if linked else {}
        except SystemExit: R=None
        nopic={k for k,v in (R or {}).items() if not v}; L=new_places(P,all_pics(),nopic)
        print('%d places in %s. %d have a Wikipedia article with a picture: the page shows it by itself. %d wait for a look: %d with no article, %d whose article has no picture the Atlas may show.'%(len(P),nm,sum(1 for v in (R or {}).values() if v),len(L),sum(1 for p in L if no_article(p)),sum(1 for p in L if not no_article(p))))
        if R is None: print('Wikipedia would not answer just now, so places WITH an article were not checked: only those with no article are listed.')
        for p in L: print('%s  |  %s, %s  |  %s'%(p['id'],p['name'],p.get('town',''),p['st']))
        if L: print('\nNext, five at a time:  python3 tools/photo_find.py look '+' '.join(p['id'] for p in L[:5])+(' ...' if len(L)>5 else '')+'\nthen  set <id> <n>  or  set <id> none "<what they showed>"  for each. The pics file goes in the same pull request.')
        return
    if a[0]=='look':
        for i in a[1:]:
            if i not in BY: print(i,'is not a place id'); continue
            look(BY[i])
        return
    if a[0]=='set':
        if len(a)<3 or a[1] not in BY: sys.exit('set <place id> <n>   or   set <place id> none "<why>"')
        f=_myfile()
        if a[2]=='none':
            why=(a[3] if len(a)>3 else '').strip()
            if len(why)<8: sys.exit('Say why in a few words: what the candidates showed instead.')
            write_pick(f,a[1],('',today,why[:160])); print('Recorded: no picture fits %s.'%a[1]); return
        cf='research/photofind_%s.json'%a[1]
        if not os.path.exists(cf): sys.exit('Run  python3 tools/photo_find.py look %s  first, and look at its sheet.'%a[1])
        C=json.load(open(cf,encoding='utf-8'))
        if not a[2].isdigit() or not 1<=int(a[2])<=len(C): sys.exit('Candidate numbers for %s run from 1 to %d.'%(a[1],len(C)))
        c=C[int(a[2])-1]
        if usable(c): sys.exit('That candidate may not be used: '+usable(c))
        write_pick(f,a[1],(c['src'].split('?')[0],c['tw'] or 0,c['th'] or 0,credit(c['artist']),c['lic'],c['page'],today))
        print('Recorded for %s: %s, by %s (%s). It is in %s.'%(a[1],c['title'][5:],credit(c['artist']),c['lic'],os.path.relpath(f,W))); return
    if a[0]=='sheet':
        import requests,io
        from PIL import Image,ImageDraw
        f=a[1] if len(a)>1 else _myfile()
        sys.path.insert(0,os.path.dirname(os.path.abspath(f))); P=importlib.import_module(os.path.basename(f)[:-3]).PICS
        rows=[(k,v) for k,v in sorted(P.items()) if v and v[0]]; tiles=[]
        for k,v in rows:
            try: r=requests.get(re.sub(r'/\d+px-','/330px-',v[0]),headers=UA,timeout=60); r.raise_for_status(); im=Image.open(io.BytesIO(r.content)).convert('RGB')
            except Exception: im=Image.new('RGB',(330,220),(90,90,90))
            im.thumbnail((330,230)); t=Image.new('RGB',(340,296),(255,255,255)); t.paste(im,((340-im.width)//2,62+(230-im.height)//2)); d=ImageDraw.Draw(t); s=BY.get(k,{})
            d.text((6,6),(s.get('name') or k)[:52],fill=(0,0,0)); d.text((6,22),('%s  %s'%(s.get('town',''),s.get('years','')))[:54],fill=(60,60,60)); d.text((6,38),os.path.basename(v[5])[5:57],fill=(0,70,160)); tiles.append(t); time.sleep(0.4)
        os.makedirs('research',exist_ok=True); n=0
        for i in range(0,len(tiles),12):
            part=tiles[i:i+12]; sheet=Image.new('RGB',(4*340,((len(part)+3)//4)*296),(255,255,255))
            for j,t in enumerate(part): sheet.paste(t,((j%4)*340,(j//4)*296))
            n+=1; sheet.save('research/photosheet_%s_%d.jpg'%(os.path.basename(f)[5:-3],n),quality=82)
        print('%d chosen pictures in %d sheet(s): research/photosheet_%s_*.jpg. %d places had none that fits.'%(len(rows),n,os.path.basename(f)[5:-3],len(P)-len(rows))); return
    sys.exit(__doc__)
if __name__=='__main__': main(sys.argv[1:])
