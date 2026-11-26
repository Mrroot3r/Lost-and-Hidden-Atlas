#!/usr/bin/env python3
"""Find a photograph for a place that has none, among the freely licensed ones on Wikimedia Commons.

   python3 tools/photo_find.py                         how many places have no picture, state by state
   python3 tools/photo_find.py next 5 ["<state>"]      the next five places that have candidates: a sheet and a list for each. A place
                                                       Commons has nothing for is recorded as "none" by the tool on the way
   python3 tools/photo_find.py list "<state>" --n 30   thirty waiting places, in a different order each time
   python3 tools/photo_find.py look <place id> ...     the candidates for each: a numbered sheet to LOOK at (research/photofind_<id>.jpg)
                                                       and a list (how each was found, the file's name and description, who, licence)
   python3 tools/photo_find.py set <place id> <n>      choose candidate n from that sheet
   python3 tools/photo_find.py set <place id> none "<why>"     looked, and none of them shows this place
   python3 tools/photo_find.py sheet [<pics file>]     one sheet of everything chosen in a file, each beside its place's name, for a second look
   python3 tools/photo_find.py sheet --unsure          the same for every picture chosen on a partial name match or from further off

Why: about half the places have a picture, all from the lead image of their own Wikipedia article (tools/photos.py). The other
half have no article or an article with no usable picture, and a reader hunting a ruin in the woods wants to know what he is
looking for. Commons holds millions of photographs.

What the tool decides, so that no session can get it wrong: only Wikimedia Commons; only a photograph (never a map, a plan, a
seal, a logo, a drawing sheet or a scanned book); only a free licence (CC BY, CC BY-SA, CC0, public domain) and a photographer
to credit. The address, the size, the credit and the licence are copied from Commons by the tool, never typed.

Where it looks (gather(), widened November 22, 2026 after the owner found it passing over photographs that were there: of ten
places recorded "nothing on Commons", five had some):
  - photographs taken within reach of the pin (150 m for an exact pin, 250 m for a site, 400 m for an area), whatever they are called;
  - photographs taken further off (to 600 m or 1,000 m) whose own words name the place: a lighthouse or a fort is photographed from afar;
  - photographs found under the place's names: the whole title with the town, and each part of a long title by itself
    ("Adirondac (Tahawus) and McIntyre furnace" is also asked for as "McIntyre furnace"); the hamlet in brackets counts as the town;
  - photographs in a Commons category whose title names the place;
  - TIFF files as well as JPEG and PNG: the Library of Congress building surveys (HABS, HAER, HALS; public domain) are TIFF.
A name that only partly matches (one word short, or no town) is offered marked LOOK TWICE. A photograph that carries a position
more than 1,500 m from the pin is a namesake and never offered. Commons allows few questions a minute from a shared address
(HTTP 429 with a wait): the tool waits and asks again, asks three name questions a place at most, and stops asking once it has
plenty. Do not hurry it and do not run two at once.

What the session decides, by looking: WHICH of the candidates shows THIS place. Read the place's name and description, read
each candidate's file name and description, and look at the sheet. Choose the one that most likely shows the building, ruin
or site from outside, as someone arriving would see it. The owner's rule since November 21, 2026: a likely picture is better
than no picture, because a wrong one is easy for a person to spot and take away (set <id> none), and a place with no picture
stays that way. So choose when a candidate plausibly shows the place, and say `none` only when none plausibly does. Still never:
an interior, a plaque close-up, a view from the place of something else, a person as the subject, a plainly different building.

Reading the sheets (from the sessions' notes):
  - Each small caption carries the file name and the by-name marker: for a candidate found by name, read the caption as well as
    the picture. Candidates are numbered afresh on every run, so `set` from the sheet of the same run. `look <id> ...` draws a
    sheet again (a long `next` scrolls the first ones away), and runs `look` for a place whatever `new` said about it: `new`
    passes over a place whose only Wikipedia link is a "List of ..." page. A place with nothing prints one long "Nothing on
    Commons" line; do not filter long lines out of the output.
  - A name shared with another town or thing brings that one's pictures: Sheffield, Woonsocket, Fort Totten, Fort Brown (Texas),
    Livingston Manor (the Sullivan County hamlet), Oak Ridge (Tennessee), Thistle (flowers). Check the town line; those are
    usually none. Two places in one town (a society and its railroad in Belton) share candidates: read each description, not
    the distance; "names it" candidates can be other houses with like file names (other Hook houses): check the house's name.
  - Near a downtown pin most candidates are the neighbours; a museum's pin brings the art inside; a place in the news brings
    the event. For lighthouses and churches the wide view from the road is nearly always the best candidate.

Choices go in tools/pics_<four letters>.py (PICS = {place id: (address, width, height, photographer, licence, the file's page,
day chosen, how it was found)} or ('', day, why, which search) for "none fits"), which tools/make.py folds into
data/photos.json. A "none" recorded under an earlier, narrower search is asked again (SEARCH). A picture from a place's own
Wikipedia article still wins. Nothing is copied but an address and a credit. Test: tools/photo_find_test.py."""
import sys,os,re,json,math,time,html,random,datetime,glob,importlib,urllib.parse
HERE=os.path.dirname(os.path.abspath(__file__)); W=os.path.dirname(HERE)
UA={'User-Agent':'lost-hidden-atlas-photos/1.0 (https://github.com/Mrroot3r/Lost-and-Hidden-Atlas)'}
API='https://commons.wikimedia.org/w/api.php'
FREE=re.compile(r'^(CC BY(-SA)?( \d(\.\d)?)?( [a-z]{2,3})?|CC0( 1\.0)?|Public domain|PD[- ].*|No restrictions)$',re.I)
NOTPHOTO=re.compile(r'\b(map|maps|plan|plans|diagram|logo|seal|coat of arms|flag|locator|location|survey|chart|drawing|drawings|sketch|blueprint|elevation|postmark|signature|sanborn|topo|usgs|aerial|sheet \d+ of \d+)\b',re.I)
SEARCH=3                  # which search a "none" was recorded under. 1 (or no number): before November 22, 2026, when the finder refused TIFF files,
                          # 3: since November 23, 2026, when every preview became a small copy. Before, a candidate whose address was the file
                          # itself came out as a grey box, and a session could say none without having seen the picture that fitted
                          # asked Commons only under a place's whole title and its town, opened no category and looked no further than the pin's reach.
UNSURE=('loose','far')    # how a chosen picture was found, when that is worth a second look: its name only partly matched, or it was taken further off
HOW=('pin','pin+name','name','category')+UNSURE
REACH={'exact':150,'site':250,'area':400}
def nomail(t):
    """a credit sometimes carries the photographer's e-mail address: the name is credit enough, and the Atlas publishes no addresses"""
    return re.sub(r'\s+',' ',re.sub(r'[\s,;:·|/-]*[(<\[]?\s*(?:mailto:)?[\w.+-]+@[\w-]+(?:\.[\w-]+)+\s*[)>\]]?','',str(t or ''))).strip(' ,;:·|/-')
def credit(h):
    """the photographer's name out of Commons' Artist field (the same rule as by() in tools/photos.py and photoBy() in app.js)"""
    h=str(h or ''); t=nomail(re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',re.sub(r'(?is)<(style|script)[^>]*>.*?</\1>','',h)))).strip())
    t=re.sub(r'(?i),\s*(creator|photographer)$','',t).strip()          # the Library of Congress surveys: "Lowe, Jet, creator"
    m=re.fullmatch(r"([A-Z][\w'-]+), ([A-Z][\w.'-]*(?: [A-Z][\w.'-]*)?)",t)
    if m: t=m.group(2)+' '+m.group(1)
    if t and len(t)<=70: return t
    for m in re.finditer(r'(?is)<a\b[^>]*href="([^"]*)"[^>]*>(.*?)</a>',h):
        x=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',m.group(2)))).strip()
        if 'User:' in m.group(1) and nomail(x): return nomail(x)[:70]
    if not t or re.search(r'(?i)<(table|img|figure)\b',h): return ''
    return re.sub(r'\s+\S*$','',t[:68])+'…'
def usable(c):
    """'' when a candidate may be offered, else the reason it may not. c: title, mime, width, height, lic, artist"""
    if c.get('mime') not in('image/jpeg','image/png','image/tiff'): return 'not a photograph file'      # TIFF: the federal building surveys; Commons serves a JPEG of each
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
def variants(name):
    """the ways a place may be named on Commons: its title without what is in brackets, then each part of a title joined by "and" or a
    colon, then each name in brackets (a year in brackets is not a name)"""
    name=str(name or ''); base=re.sub(r'\s+',' ',re.sub(r'\(.*?\)',' ',name)).strip(' ,:;'); out=[base]
    out+=[x.strip(' ,') for x in re.split(r'\s+(?:and|&)\s+|:\s+|;\s+|\s+/\s+',base)]
    out+=[x.strip() for x in re.findall(r'\(([^()]*)\)',name) if not re.fullmatch(r'(?i)[^a-z]*|(c\.|ca\.?|circa|about|built|from|since|until|to)?[\s\d,.–-]*s?',x.strip())]
    return [v for v in dict.fromkeys(out) if v]
def _norm(text):
    """a file's words for matching: "MesierHomestead.JPG" is read as "mesier homestead jpg"""
    return ' '+re.sub(r'[^a-z0-9]+',' ',fold(re.sub(r'(?<=[a-z])(?=[A-Z])',' ',str(text or ''))))+' '
STATUS=r'(?i)^(the|former|site of( the)?|ruins of( the)?|remains of( the)?)\s+|\s+(site|ruins?|remains|foundations?|cellar holes?)$'
def _town(s): return str(s.get('town') or '').split(',')[0].split('(')[0].strip()
def raw_places(s):
    """the town, the hamlet in brackets after it, and any name in brackets in the title (often the hamlet or the older name)"""
    V=variants(s.get('name')); inb=[x.strip() for x in re.findall(r'\(([^()]*)\)',str(s.get('name') or ''))]
    return [x for x in dict.fromkeys([_town(s)]+[x.strip() for x in re.findall(r'\(([^()]*)\)',str(s.get('town') or ''))]+[x for x in inb if x in V]) if x]
def places_of(s):
    return [x for x in dict.fromkeys(re.sub(r'[^a-z0-9]+',' ',fold(x)).strip() for x in raw_places(s)) if x]
def _telling(s):
    """[(a way of naming the place, folded; its telling words)]; a part of a title counts only if it has a telling word of its own"""
    town=fold(_town(s)); tw=set(re.split(r'[^a-z0-9]+',town)); out=[]
    for i,v in enumerate(variants(s.get('name'))):
        nw=name_words(v,town)
        if not nw or (i>0 and not [w for w in nw if w not in COMMON and w not in tw]): continue
        out.append((re.sub(r'[^a-z0-9]+',' ',fold(v)).strip(),nw))
    return out
def named(text,s):
    """how well a file's own words name this place. 2: every telling word of one of its names, and the town or hamlet (a name in
    brackets that is itself the hamlet, "(Tahawus)", does not count as both). 1 (look twice): all but one word of a name of three or
    more, with the town; or every word of a name of two or more with no town. 0: neither"""
    t=_norm(text); P=places_of(s); best=0
    for v,nw in _telling(s):
        inplace=any((' '+x+' ') in t for x in P if x!=v); hit=sum(1 for w in nw if (' '+w) in t)
        if hit==len(nw) and inplace: return 2
        if (len(nw)>=3 and hit==len(nw)-1 and inplace) or (len(nw)>=2 and hit==len(nw)): best=1
    return best
def words_only(text,s,least=2):
    """every telling word of one of the place's names, town or no town: enough for a photograph that carries a position near the pin
    (least=1), or for a category's title (two words at least)"""
    t=_norm(text)
    return any(len(nw)>=least and all((' '+w) in t for w in nw) for v,nw in _telling(s))
def queries(s):
    """what Commons is asked, three questions at most (it allows few a minute): the whole title with the town; then each part of a
    title, or the title itself when it has no parts, alone when it has two telling words (the filter afterwards wants the town or a
    position), else with the town; then a name in brackets with the town"""
    town=_town(s); V=variants(s.get('name')); T=fold(town)
    if not V: return []
    two=lambda v:len([w for w in name_words(v,T) if w not in COMMON])>=2
    inb=[x.strip() for x in re.findall(r'\(([^()]*)\)',str(s.get('name') or ''))]; parts=[v for v in V[1:] if v not in inb]
    out=[('%s %s'%(V[0],town)).strip()]
    out+=[v if two(v) else ('%s %s'%(v,town)).strip() for v in (parts or [V[0]]) if name_words(v,T)]
    out+=[('%s %s'%(v,town)).strip() for v in V[1:] if v in inb]
    def bare(q):          # without "site", "ruins", "the": no photograph is filed under those
        tail=' '+town if town and q.endswith(' '+town) else ''; core=q[:len(q)-len(tail)]
        return (re.sub(STATUS,'',re.sub(STATUS,'',core)).strip() or core)+tail
    out=[bare(q) for q in out]
    return [q for q in dict.fromkeys(re.sub(r'\s+',' ',re.sub(r'[:;"]',' ',x)).strip() for x in out) if q][:3]
_ST=[None]
def _states():
    if _ST[0] is None:
        try:
            from states import STATES
            _ST[0]=({c:st['name'] for st in STATES for c,l in st['regions']},[st['name'] for st in STATES])
        except Exception: _ST[0]=({},[])
    return _ST[0]
def state_of(s): return _states()[0].get(s.get('reg'))
def other_state(text,state):
    """does a file's own wording put it in another state or province: it names one, and does not name this place's. "Washington" and
    "Georgia" are too often a person, a park or a street to count"""
    if not state: return False
    t=' '+re.sub(r'[^a-z]+',' ',fold(text))+' '; own=' '+fold(state)+' '
    if own in t: return False
    return any((' '+fold(n)+' ') in t for n in _states()[1] if n not in('Washington','Georgia',state) and fold(n) not in fold(state) and fold(state) not in fold(n))
def thumb330(u):
    """the address of a small copy, for the sheet (a TIFF's JPEG copy is named lossy-page1-960px-...). For a picture narrower than the
    width asked of it Commons gives the address of the file itself; a small copy is made of that too, because Commons refuses a tool
    that fetches files themselves ("instead use thumbnails", with a ten-minute wait)"""
    u=str(u).split('?')[0]
    if '/thumb/' in u: return re.sub(r'(/(?:lossy-page\d+-)?)\d+px-(?=[^/]*$)',r'\g<1>330px-',u)
    m=re.match(r'(https://upload\.wikimedia\.org/wikipedia/[a-z]+)/([0-9a-f]/[0-9a-f]{2})/([^/]+)$',u)
    if not m: return u
    n=m.group(3); tif=n.lower().endswith(('.tif','.tiff'))
    return '%s/thumb/%s/%s/%s330px-%s%s'%(m.group(1),m.group(2),n,'lossy-page1-' if tif else '',n,'.jpg' if tif else '')
def row_problem(v):
    """'' when a pics file's row is one the Atlas may show or a well-formed "none"; else what is wrong with it (tools/check.py asks)"""
    if not isinstance(v,(list,tuple)) or not v: return 'is not a row'
    if v[0]=='':
        if len(v) in (3,4) and re.fullmatch(r'20\d\d-[01]\d-[0-3]\d',str(v[1])) and isinstance(v[2],str) and 0<len(v[2])<=160 and (len(v)==3 or isinstance(v[3],int)): return ''
        return "is not ('', day, why none fits[, which search])"
    if not(len(v) in (7,8) and all(isinstance(x,str) for x in (v[0],v[3],v[4],v[5],v[6])) and isinstance(v[1],int) and isinstance(v[2],int)): return 'is not (address, width, height, photographer, licence, file page, day[, how found])'
    if len(v)==8 and v[7] not in HOW: return 'how it was found must be one of '+', '.join(HOW)
    if not re.match(r'https://(upload|thumb)\.wikimedia\.org/[^\s<>"]+\.(jpe?g|png)$',v[0],re.I): return 'the picture must be an address at Wikimedia (upload.wikimedia.org)'
    if not re.match(r'https://commons\.wikimedia\.org/wiki/File:[^\s<>"]+$',v[5]): return 'the file page must be on commons.wikimedia.org'
    if not FREE.match(v[4]): return "'%s' is not a free licence the Atlas shows"%v[4]
    if not v[3].strip() or len(v[3])>80 or chr(64) in v[3]: return 'the photographer must be a name (no address), 80 characters at most'
    if not re.fullmatch(r'20\d\d-[01]\d-[0-3]\d',v[6]): return 'the day chosen must be YYYY-MM-DD'
    return ''
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
        f.write('# id: (picture address, width, height, photographer, licence, the file\'s page on Commons, day chosen, how it was found)   or   (\'\', day, why none fits, which search)\n')
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
def asked_again(v):
    """a "none" is offered once more when it was recorded before the searches were numbered or under the first (a wider search may now have
    a picture for it), or was given after a look under the second, when one candidate may have been a grey box. A place Commons had
    nothing for under the second search is not: nothing about that has changed"""
    return bool(v) and not v[0] and (len(v)<4 or v[3]<2 or (v[3]<SEARCH and v[2]!=NOTHING))
def seen_whole(prior,C):
    """True when a place was given "none" after a look under the second search and every candidate now found is a small copy, so that
    look saw all of them: the none stands and nobody looks again. A candidate whose address is the file itself was a grey box then"""
    return bool(prior) and not prior[0] and len(prior)>3 and prior[3]==2 and prior[2]!=NOTHING and all('/thumb/' in str(c.get('src') or '').split('?')[0] for c in C)
def rank(C,nw,town):
    """candidates in the order shown: those whose own name and description name the place first (taken at the pin before those with no
    position), then the rest, nearest first"""
    def key(c):
        named=names_it(str(c.get('title') or '')+' '+str(c.get('desc') or ''),nw,town)
        return (0 if named else 1, 0 if c.get('m') is not None else 1, c.get('m') or 0)
    return sorted(C,key=key)
def no_article(p):
    """a place with no Wikipedia article of its own: the page has no article picture to show, so a session looks for one"""
    # by the rule the page itself uses (wikiTitle() in app.js, title_of() in photos.py): a link to one of Wikipedia's lists, to a Register
    # listings page or to a Category is not the place's article, and the page takes no picture from it
    for l in (p.get('links') or []):
        m=re.match(r'https?://en\.(?:m\.)?wikipedia\.org/wiki/([^#?]+)',str(l[1] if isinstance(l,(list,tuple)) and len(l)>1 else l) or '')
        if not m: continue
        t=urllib.parse.unquote(m.group(1)).replace('_',' ')
        if re.match(r'(list of|lists of|national register of historic places listings)',t,re.I) or ':' in t: continue
        return False
    return True
def new_places(P,done,nopic=()):
    """of one batch's places, those a research session should look for a picture for: something still there, no answer yet, and either
    no article or (nopic) an article that turned out to have no picture the Atlas may show"""
    return [p for p in P if p.get('st')!='gone' and (no_article(p) or p['id'] in nopic) and (p['id'] not in done or asked_again(done[p['id']]))]
def trial_line(pid,page,why):
    """one answer of a trial: place id | the chosen file's page on Commons, or none | why. Nothing here reaches the map"""
    return '%s | %s | %s\n'%(pid,page or 'none',str(why or '').replace('|','/').replace('\n',' ')[:160])
def trial_read(text):
    """the answers in a trial file: {place id: the chosen file's page, or '' for none}; a later line for the same place wins"""
    R={}
    for l in str(text).split('\n'):
        p=[x.strip() for x in l.split('|')]
        if len(p)>=2 and re.fullmatch(r'[a-z0-9-]+',p[0]) and (p[1]=='none' or p[1].startswith('https://commons.wikimedia.org/wiki/File:')): R[p[0]]='' if p[1]=='none' else p[1]
    return R
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
PACE=6.5; _last=[0.0]      # seconds between questions to Commons. Its allowance for a tool like this one is about ten questions a minute
                           # after a first burst (its own page says 10 for a client known only by its address), and every Atlas session
                           # asking in the same hour shares it. At 2.5 s every fourth question was refused with a 45-second wait, which made
                           # a place cost half a minute or more and the first unattended batch reach 20 places in 40 minutes; spaced
                           # under the allowance, nothing is refused and a place costs about 20 seconds (November 22, 2026)
# Logged in, Commons allows a tool several thousand questions an hour where one known only by its address gets a few hundred
# (its rate-limit page, 2026). The login is a bot password with basic rights only, made by the owner at Special:BotPasswords; it
# is kept outside the repository, in two environment variables of the cloud environment the pictures job runs in, and is never
# printed, logged or written to a file. Without the variables, or if the login is refused, the tool works as it did before.
PACE_IN=2.0; _S={}          # 1,800 questions an hour when logged in: well under "several thousand", and a refusal is still obeyed
def new_session():
    import requests
    x=requests.Session(); x.headers.update(UA); return x
def login(sess,user,pw):
    """True when Commons accepts the bot password. Says nothing that holds the name or the password."""
    try:
        t=sess.get(API,params=dict(action='query',meta='tokens',type='login',format='json',formatversion='2'),timeout=60).json()['query']['tokens']['logintoken']
        j=sess.post(API,data=dict(action='login',lgname=user,lgpassword=pw,lgtoken=t,format='json',formatversion='2'),timeout=60).json()
        if (j.get('login') or {}).get('result')=='Success': return True
        print('Commons did not accept the login (%s); carrying on without it, at the slower pace.'%str((j.get('login') or {}).get('result') or 'no answer')[:30])
    except Exception as e:
        print('Commons could not be logged in to (%s); carrying on without it, at the slower pace.'%type(e).__name__)
    return False
def _sess():
    if 's' not in _S:
        _S['s']=new_session(); u=os.environ.get('ATLAS_COMMONS_USER','').strip(); pw=os.environ.get('ATLAS_COMMONS_PASS','').strip()
        _S['in']=bool(u and pw) and login(_S['s'],u,pw)
        if _S['in']: print('Logged in to Commons: questions go faster.')
    return _S['s']
def pace(): return PACE_IN if _S.get('in') else PACE
_T=dict(q=0,qs=0.0,qw=0.0,p=0,ps=0.0,pw=0.0,pr=0)      # where a run's time went: questions to Commons, and the preview pictures for the sheets
def time_note():
    """One line for the end of a run. A round took ten minutes with the login on (November 23, 2026) and nothing said whether the
    questions or the preview pictures, which Wikimedia limits separately, had cost the time."""
    return 'Time: %d questions took %d s (%d s of it waiting); %d preview pictures took %d s (%d s of it waiting, %d refused and tried again).'%(_T['q'],_T['qs'],_T['qw'],_T['p'],_T['ps'],_T['pw'],_T['pr'])
def login_note():
    """One line for the end of a run, so whoever reads the log can tell which allowance the run had. Names the two settings, never their values."""
    if not (os.environ.get('ATLAS_COMMONS_USER','').strip() and os.environ.get('ATLAS_COMMONS_PASS','').strip()):
        return 'Commons login: none set in this environment (ATLAS_COMMONS_USER and ATLAS_COMMONS_PASS), so questions were asked at the slower pace.'
    if _S.get('in'): return 'Commons login: logged in, so questions were asked at the faster pace.'
    return 'Commons login: one is set, but Commons did not accept it, so questions were asked at the slower pace.'
def _get(params,tries=8):
    sess=_sess()
    t0=time.time(); _T['q']+=1
    def nap(x): _T['qw']+=x; time.sleep(x)
    try: return _get1(sess,params,tries,nap)
    finally: _T['qs']+=time.time()-t0
def _get1(sess,params,tries,nap):
    for k in range(tries):
        w=pace()-(time.time()-_last[0])
        if w>0: nap(w)
        _last[0]=time.time()
        q=dict(params,format='json',formatversion='2')
        if _S.get('in'): q['assert']='user'          # if the login has lapsed Commons says so, where it would otherwise answer at the anonymous allowance without a word
        r=sess.get(API,params=q,headers=UA,timeout=60)
        if r.status_code==429 or r.status_code>=500: nap(min(90,int(r.headers.get('Retry-After') or 0) or 8*(k+1))); continue
        r.raise_for_status(); j=r.json()
        if refused(j):
            if _S.get('in') and isinstance(j['error'],dict) and j['error'].get('code')=='assertuserfailed':          # logged out part-way: log in again once, or go on without
                u=os.environ.get('ATLAS_COMMONS_USER','').strip(); pw=os.environ.get('ATLAS_COMMONS_PASS','').strip(); _S['in']=(not _S.get('again')) and login(sess,u,pw); _S['again']=True; continue
            if k>=3: raise SystemExit('Wikimedia Commons answered with an error: %s. Nothing was recorded; run the same command again later.'%str(j['error'].get('code') if isinstance(j['error'],dict) else j['error'])[:80])
            nap(8*(k+1)); continue        # an error inside a 200 reply (too busy, too many requests): never read it as "nothing here"
        return j
    raise SystemExit('Wikimedia Commons keeps refusing (too many requests). Wait a few minutes and run the same command again.')
def _hav(a,b,c,d):
    p=math.pi/180; h=math.sin((c-a)*p/2)**2+math.cos(a*p)*math.cos(c*p)*math.sin((d-b)*p/2)**2
    return 2*6371000*math.asin(math.sqrt(h))
def _plain(t,n=140): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',str(t or '')))).strip()[:n]
PROPS=dict(prop='imageinfo|coordinates|categories',coprimary='all',colimit='max',clshow='!hidden',cllimit='max',iiprop='url|size|mime|extmetadata',iiurlwidth='900',iiextmetadatafilter='LicenseShortName|Artist|ImageDescription|DateTimeOriginal')
NOBOOKS=' -filemime:pdf -filemime:djvu'      # Commons holds whole scanned books and newspapers, searched by every word in them: without this
                                           # a question like "McIntyre furnace" returned thirty of them and no photograph
ORDER={'pin+name':0,'name':1,'category':2,'far':3,'pin':4,'loose':5}
SHOWN=16; SHOWN_LOOSE=4      # candidates on a sheet. Each costs one small preview picture, about a second
def pick(C):
    """the sixteen shown, best first: those that name the place, those in its category, those taken further off that name it, those
    taken at the pin nearest first, and last those whose name half matches, for which four places are kept however many were at the pin"""
    C=sorted(C,key=lambda c:(ORDER[c['how']],c['m'] if c.get('m') is not None else 99999,c['title']))
    loose=[c for c in C if c['how']=='loose']; rest=[c for c in C if c['how']!='loose']
    keep=min(len(loose),max(SHOWN_LOOSE,SHOWN-len(rest)))
    return rest[:SHOWN-keep]+loose[:keep]
def _pages(params):
    """one question's pages. Commons answers in parts when there is much to say (the categories of fifty files, say): the parts that
    carry on the same pages are fetched too, two more at most, and put together. Without colimit=max it gave the position of ten files
    only, and the first finder took the other fifty for files with no position"""
    P={}; par=dict(params)
    for k in range(3):
        j=_get(par)
        for pg in (j.get('query') or {}).get('pages',[]):
            o=P.setdefault(pg.get('title'),pg)
            if o is not pg:
                for f in ('imageinfo','coordinates','categories'):
                    if pg.get(f): o[f]=(o.get(f) or [])+[x for x in pg[f] if x not in (o.get(f) or [])]
        c=j.get('continue') or {}
        more={x:y for x,y in c.items() if x in('clcontinue','cocontinue','iicontinue')}
        if not more: break
        par=dict(params,**more,**{'continue':c.get('continue','')})
    return list(P.values())
def _cand(pg,s):
    """one of Commons' pages as a candidate, or None when it is not a file the Atlas may offer"""
    ii=(pg.get('imageinfo') or [None])[0]
    if not ii: return None
    m=ii.get('extmetadata') or {}; co=(pg.get('coordinates') or [{}])[0]
    c=dict(title=pg['title'],mime=ii.get('mime'),width=ii.get('width'),height=ii.get('height'),lic=_plain((m.get('LicenseShortName') or {}).get('value'),40),artist=(m.get('Artist') or {}).get('value'),
           desc=_plain((m.get('ImageDescription') or {}).get('value')),when=_plain((m.get('DateTimeOriginal') or {}).get('value'),10),src=ii.get('thumburl'),tw=ii.get('thumbwidth'),th=ii.get('thumbheight'),page=ii.get('descriptionurl'),
           cats=' ; '.join(str(x.get('title') or '')[9:] for x in (pg.get('categories') or []))[:400],
           m=round(_hav(s['lat'],s['lon'],co['lat'],co['lon'])) if 'lat' in co else None)
    if usable(c) or not c['src'] or not c['page']: return None
    c['n']=named(c['title']+' '+c['desc']+' '+c['cats'],s)
    if c['n']==2 and c['m'] is None and other_state(c['title']+' '+c['desc']+' '+c['cats'],state_of(s)): c['n']=1; c['elsewhere']=True      # a namesake in another state, most likely
    return c
def gather(s):
    """the candidates for one place, best first, 16 at most; each says how it was found (c['how']):
       pin       taken within reach of the pin (150 m exact, 250 m a site, 400 m an area), whatever it is called; pin+name when it names the place too
       far       taken further off (to 600 m, 1,000 m for a site or an area) and its own words name the place
       name      found under one of the place's names, and its words hold every telling word and the town or hamlet
       loose     found by name, but the name only partly matches: LOOK TWICE
       category  it is in a Commons category whose title names the place
    A photograph that carries a position more than 1,500 m from the pin is a namesake and is never offered."""
    reach=REACH.get(s.get('prec') or 'site',250); wide=600 if reach<=150 else 1000; C={}
    def add(c,how):
        o=C.get(c['title'])
        if o is None or ORDER[how]<ORDER[o['how']]: c['how']=how; C[c['title']]=c
    for pg in _pages(dict(PROPS,action='query',generator='geosearch',ggsnamespace='6',ggscoord='%s|%s'%(s['lat'],s['lon']),ggsradius=str(wide),ggslimit='50')):
        c=_cand(pg,s)
        if not c or c['m'] is None or c['m']>wide: continue
        if c['m']<=reach: add(c,'pin+name' if c['n']==2 else 'pin')
        elif c['n'] or words_only(c['title']+' '+c['desc']+' '+c['cats'],s,1): add(c,'far')
    cats=[]
    for q in queries(s):
        if sum(1 for c in C.values() if c['how'] in('pin+name','name'))>=3: break          # three that name it already: ask Commons no more
        for pg in _pages(dict(PROPS,action='query',generator='search',gsrnamespace='6|14',gsrlimit='30',gsrsearch=q+NOBOOKS)):
            if str(pg.get('title') or '').startswith('Category:'):
                t=pg['title'][9:]
                if pg['title'] not in cats and (named(t,s) or words_only(t,s,2) or _norm(re.sub(r'\(.*?\)','',t)).strip() in [v for v,nw in _telling(s)]): cats.append(pg['title'])
                continue
            c=_cand(pg,s)
            if not c or not c['n']: continue
            if c['m'] is not None and c['m']>1500:
                # its own position is somewhere else. A namesake, unless it names the place AND its town and is within a day's walk of
                # wrong: Commons copies the Register's coordinate, and the Register's is sometimes miles out (Fendall Hall, 27 km)
                if c['n']<2 or c['m']>100000: continue
                c['off']=True; add(c,'loose'); continue
            add(c,('pin+name' if c['n']==2 else 'pin') if c['m'] is not None and c['m']<=reach else 'name' if c['n']==2 else 'loose')
    for t in cats[:2]:
        if len(C)>=16 or sum(1 for c in C.values() if c['how'] in('pin+name','name','category'))>=3: break
        for pg in _pages(dict(PROPS,action='query',generator='categorymembers',gcmtitle=t,gcmtype='file',gcmlimit='30')):
            c=_cand(pg,s)
            if not c or (c['m'] is not None and c['m']>1500): continue
            add(c,'category')
    return pick(list(C.values()))
LABEL={'pin':'%s m from the pin','pin+name':'%s m from the pin, NAMES IT','far':'%s m AWAY, names it','name':'BY NAME ONLY','loose':'NAME PARTLY MATCHES: LOOK TWICE','category':'IN A CATEGORY NAMED FOR IT'}
def label(c):
    if c.get('elsewhere'): return 'NAMES ANOTHER STATE: LOOK TWICE'
    if c.get('off'): return 'NAMES IT, BUT ITS POSITION IS %d km OFF: LOOK TWICE'%round(c['m']/1000)
    t=LABEL[c['how']]; return t%c['m'] if '%s' in t else t+(' (%d m)'%c['m'] if c.get('m') is not None else ', no position')
NOTHING='nothing on Commons near the pin, under its names or in a category of its own'
def look(s,record=None):
    """print the candidates for one place and write its sheet. Returns how many there were. With record (a pics file), a place with
    none at all is recorded as "none" there and then: nobody needs to look at an empty sheet"""
    import requests,io
    from PIL import Image,ImageDraw
    C=gather(s)
    print('\n== %s  |  %s, %s  |  %s  |  %s pin'%(s['id'],s['name'],s.get('town',''),s.get('years',''),s.get('prec','')))
    print('   '+_plain(s.get('story') or s.get('note') or '',300))
    os.makedirs('research',exist_ok=True)
    json.dump(C,open('research/photofind_%s.json'%s['id'],'w',encoding='utf-8'))
    if not C:
        if record: write_pick(record,s['id'],('',datetime.date.today().isoformat(),NOTHING,SEARCH)); print('   Nothing on Commons: no free photograph near the pin, none under its names, no category of its own. Recorded as none by the tool; nothing for you to do.')
        else: print('   Nothing on Commons: no free photograph near the pin, none under its names, no category of its own.')
        return 0
    if record:
        prior=all_pics().get(s['id'])
        if seen_whole(prior,C):
            write_pick(record,s['id'],('',prior[1],prior[2],SEARCH)); print('   Looked at before, and every candidate was on the sheet then: the earlier none stands. Recorded by the tool; nothing for you to do.')
            return 0
    tiles=[]
    for n,c in enumerate(C,1):
        im=None; _t0=time.time(); _T['p']+=1
        for k in range(3):          # a refused download (429) is tried again; a grey tile hides a candidate from whoever chooses
            try:
                r=_sess().get(thumb330(c['src']),headers=UA,timeout=60); r.raise_for_status(); im=Image.open(io.BytesIO(r.content)).convert('RGB'); break      # the same session as the questions, so a login, where it counts for pictures, is used
            except Exception as e:
                ra=getattr(getattr(e,'response',None),'headers',{}).get('Retry-After') if getattr(e,'response',None) is not None else None
                _w=min(60,int(ra)) if str(ra or '').isdigit() else 6*(k+1); _T['pr']+=1; _T['pw']+=_w; _T['gap']=min(4.0,_T.get('gap',1.0)*2); time.sleep(_w)      # a refusal is rare now that every preview is a small copy; after one, ask more slowly
        _T['ps']+=time.time()-_t0
        if im is None: im=Image.new('RGB',(330,220),(90,90,90)); c['grey']=True
        im.thumbnail((330,250)); t=Image.new('RGB',(340,286),(255,255,255)); t.paste(im,((340-im.width)//2,30+(250-im.height)//2)); d=ImageDraw.Draw(t); d.text((6,4),'%d   %s'%(n,label(c)),fill=(0,0,0) if c['how'] in('pin','pin+name') else (170,0,0) if c['how'] in UNSURE else (0,110,40)); d.text((6,17),c['title'][5:60],fill=(0,70,160)); tiles.append(t)
        print('  %2d  %s  |  %s  |  %s  |  %s, %s%s'%(n,label(c),c['title'][5:95],c['desc'][:110] or '(no description)',credit(c['artist']),c['lic'],', '+c['when'][:4] if c['when'] else ''))
        time.sleep(_T.get('gap',1.0))          # a second between previews
    cols=4; rows=(len(tiles)+cols-1)//cols; sheet=Image.new('RGB',(cols*340,rows*286),(255,255,255))
    for i,t in enumerate(tiles): sheet.paste(t,((i%cols)*340,(i//cols)*286))
    out='research/photofind_%s.jpg'%s['id']; sheet.save(out,quality=82)
    print('   LOOK at %s, then:  python3 tools/photo_find.py set %s <n>   or   set %s none "<why>"'%(out,s['id'],s['id']))
    return len(C)
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
            try: look(BY[i],_myfile())
            except Exception as e: print('%s: the look failed (%s); the others go on. Run  look %s  again by itself.'%(i,str(e)[:100],i))      # one place's error used to stop the whole batch
        return
    if a[0]=='next':
        # the next places that have something to look at: python3 tools/photo_find.py next 5 ["<state>"]. A place Commons has nothing for is
        # recorded as none by the tool on the way and costs nobody a look.
        n=int(a[1]) if len(a)>1 and a[1].isdigit() else 5; st=[x for x in a[1:] if not x.isdigit()]
        Wt=[s for s in _waiting(S) if not os.path.exists('research/photofind_%s.json'%s['id'])]
        if st: key=next((k for k,v in STNAME.items() if v.lower()==st[0].lower() or k==st[0].lower()),None); Wt=[s for s in Wt if REGST.get(s['reg'])==key or s['reg']==st[0]]
        random.shuffle(Wt); got=[]; empty=0
        for s in Wt[:n*4+10]:
            if look(s,_myfile()): got.append(s['id'])
            else: empty+=1
            if len(got)>=n: break
        print('\n%d place(s) to look at: %s. %d had nothing on Commons, or nothing that an earlier look had not seen, and were recorded as none by the tool. %d still wait.'%(len(got),' '.join(got) or 'none',empty,len(Wt)-len(got)-empty))
        if got: print('For each: LOOK at its sheet, then  set <id> <n>  or  set <id> none "<what they showed>" . Then run  next  again.')
        return
    if a[0]=='set':
        if len(a)<3 or a[1] not in BY: sys.exit('set <place id> <n>   or   set <place id> none "<why>"')
        f=_myfile()
        if a[2]=='none':
            why=(a[3] if len(a)>3 else '').strip()
            if len(why)<8: sys.exit('Say why in a few words: what the candidates showed instead.')
            write_pick(f,a[1],('',today,why[:160],SEARCH)); print('Recorded: no picture fits %s.'%a[1]); return
        cf='research/photofind_%s.json'%a[1]
        if not os.path.exists(cf): sys.exit('Run  python3 tools/photo_find.py look %s  first, and look at its sheet.'%a[1])
        C=json.load(open(cf,encoding='utf-8'))
        if not a[2].isdigit() or not 1<=int(a[2])<=len(C): sys.exit('Candidate numbers for %s run from 1 to %d.'%(a[1],len(C)))
        c=C[int(a[2])-1]
        if usable(c): sys.exit('That candidate may not be used: '+usable(c))
        write_pick(f,a[1],(c['src'].split('?')[0],c['tw'] or 0,c['th'] or 0,credit(c['artist']),c['lic'],c['page'],today,c.get('how') or 'pin'))
        print('Recorded for %s: %s, by %s (%s). It is in %s.'%(a[1],c['title'][5:],credit(c['artist']),c['lic'],os.path.relpath(f,W))); return
    if a[0]=='try':
        # a trial: the same choice as set, written to research/trial.md and nowhere else. For comparing two models on the same places.
        if len(a)<3 or a[1] not in BY: sys.exit('try <place id> <n>   or   try <place id> none "<why>"')
        os.makedirs('research',exist_ok=True); tf='research/trial.md'
        if a[2]=='none':
            open(tf,'a',encoding='utf-8').write(trial_line(a[1],'',a[3] if len(a)>3 else '')); print('Trial answer for %s: none. Written to %s only.'%(a[1],tf)); return
        cf='research/photofind_%s.json'%a[1]
        if not os.path.exists(cf): sys.exit('Run  python3 tools/photo_find.py look %s  first, and look at its sheet.'%a[1])
        C=json.load(open(cf,encoding='utf-8'))
        if not a[2].isdigit() or not 1<=int(a[2])<=len(C): sys.exit('Candidate numbers for %s run from 1 to %d.'%(a[1],len(C)))
        c=C[int(a[2])-1]; open(tf,'a',encoding='utf-8').write(trial_line(a[1],c['page'],a[3] if len(a)>3 else ''))
        print('Trial answer for %s: %s. Written to %s only.'%(a[1],c['title'][5:],tf)); return
    if a[0]=='sheet':
        import requests,io
        from PIL import Image,ImageDraw
        if len(a)>1 and a[1]=='--unsure':
            # every chosen picture whose name only partly matched or that was taken further off, across all files: the ones a person
            # should look over (python3 tools/photo_find.py sheet --unsure). A wrong one is taken away with  set <id> none "<why>" .
            f='pics_unsure.py'; P={k:v for k,v in all_pics().items() if v and v[0] and len(v)>7 and v[7] in UNSURE}
        else:
            f=a[1] if len(a)>1 else _myfile()
            sys.path.insert(0,os.path.dirname(os.path.abspath(f))); P=importlib.import_module(os.path.basename(f)[:-3]).PICS
        rows=[(k,v) for k,v in sorted(P.items()) if v and v[0]]; tiles=[]
        for k,v in rows:
            try: r=requests.get(thumb330(v[0]),headers=UA,timeout=60); r.raise_for_status(); im=Image.open(io.BytesIO(r.content)).convert('RGB')
            except Exception: im=Image.new('RGB',(330,220),(90,90,90))
            im.thumbnail((330,230)); t=Image.new('RGB',(340,296),(255,255,255)); t.paste(im,((340-im.width)//2,62+(230-im.height)//2)); d=ImageDraw.Draw(t); s=BY.get(k,{})
            d.text((6,6),(s.get('name') or k)[:52],fill=(0,0,0)); d.text((6,22),('%s  %s'%(s.get('town',''),s.get('years','')))[:54],fill=(60,60,60)); d.text((6,38),os.path.basename(v[5])[5:57],fill=(0,70,160)); d.text((6,50),'look twice: '+v[7] if len(v)>7 and v[7] in UNSURE else '',fill=(170,0,0)); tiles.append(t); time.sleep(0.4)
        os.makedirs('research',exist_ok=True); n=0
        for i in range(0,len(tiles),12):
            part=tiles[i:i+12]; sheet=Image.new('RGB',(4*340,((len(part)+3)//4)*296),(255,255,255))
            for j,t in enumerate(part): sheet.paste(t,((j%4)*340,(j//4)*296))
            n+=1; sheet.save('research/photosheet_%s_%d.jpg'%(os.path.basename(f)[5:-3],n),quality=82)
        print('%d chosen pictures in %d sheet(s): research/photosheet_%s_*.jpg. %d places had none that fits.'%(len(rows),n,os.path.basename(f)[5:-3],len(P)-len(rows))); return
    sys.exit(__doc__)
if __name__=='__main__':
    _a=sys.argv[1:]
    try: main(_a)
    finally:
        if not _a or _a[0] in ('next','look','new'):          # the last line of the output, where a cut-off log still shows it
            try: _sess()
            except Exception: pass
            print(time_note()); print(login_note())
