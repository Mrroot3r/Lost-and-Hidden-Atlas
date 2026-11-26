#!/usr/bin/env python3
"""Red brick: which places have it. The channel looks for red brick buildings and ruins, so every place says
yes (mostly brick), some (part brick: a chimney, an arch, brick over stone), no, or is not checked yet.

   python3 tools/brick.py                       how many places are settled, and how many wait, state by state
   python3 tools/brick.py list [state|region]   the standing places, ruins and traces nobody has looked at, with their links
                                                (--n 40 for how many; in a different order each time, those with an encyclopedia article first)
   python3 tools/brick.py look <id> [--pic N] [picture address]
                                                fetch a picture of the place into research/brick/<id>.jpg and say where it
                                                came from: a picture of its Wikipedia article (it lists them all with their captions;
                                                --pic 2 takes the second), or the address you give.
                                                Open that file and LOOK at it.
   python3 tools/brick.py set <id> yes|some|no "<what you saw, and the picture's address or the source's words>" --colour <colour>
                                                with the colour of the brick itself: red, buff (yellow, cream, tan), dark, glazed,
                                                painted, mixed (red with another), or none (no brick at all). For "yes" the colour
                                                is red and may be left off. Add  --fire "<the source's words>"  ONLY when a source
                                                says fire brick (refractory brick) is there: a kiln, a furnace, coke ovens.
   python3 tools/brick.py list --colour [state|region]
                                                places whose red-brick answer (some or no) was recorded before colours were: look again
                                                record it in tools/bricks_<four letters>.py (this workspace's own file, so
                                                sessions working side by side do not collide)

The rule: a value is a fact like any other, so it comes from something you opened in this session: a picture that
plainly shows this building or ruin, or a source that says what it is built of. A picture of the town, of a sign, or of
a building you cannot tell is this one settles nothing: leave the place unset. Red or red-brown brick counts; yellow or
buff brick, painted brick (even painted red: the owner, November 26, 2026) and brick-coloured stone do not ('no', and say so).
The colour is recorded beside that answer, and fire brick only from a source: a picture cannot tell it from buff face brick
(tools/brickrule.py holds the rules; test tools/brick_test.py). A place that is gone, a marker or under
water is not asked."""
import sys,os,re,json,glob,random,importlib,urllib.request,urllib.parse
HERE=os.path.dirname(os.path.abspath(__file__)); W=os.path.dirname(HERE); os.chdir(W); sys.path.insert(0,HERE); sys.dont_write_bytecode=True
UA={'User-Agent':'lost-hidden-atlas-research/1.0 (https://github.com/Mrroot3r/Lost-and-Hidden-Atlas)'}
if not os.path.exists('build/sites.json'): os.system(sys.executable+' tools/build_sites.py > /dev/null')
S=json.load(open('build/sites.json',encoding='utf-8')); BY={s['id']:s for s in S}
from states import STATES
REGST={c:st['k'] for st in STATES for c,l in st['regions']}; STNAME={st['k']:st['name'] for st in STATES}
ASK=('standing','ruins','traces')
def wiki(s):
    for l in s.get('links') or []:
        u=l[1] if isinstance(l,(list,tuple)) else str(l)
        m=re.search(r'en\.wikipedia\.org/wiki/([^#?]+)',u)
        if m: return m.group(1)
def raw(t,hop=0):
    """An article's wikitext, kept under research/wikiraw/ as tools/wiki_raw.py keeps it; follows a redirect."""
    import time,requests
    p='research/wikiraw/'+re.sub(r'[^\w]+','_',t)+'.txt'
    if os.path.exists(p): w=open(p,encoding='utf-8').read()
    else:
        for k in range(4):
            r=requests.get('https://en.wikipedia.org/w/index.php',params={'title':t,'action':'raw'},headers=UA,timeout=40)
            if r.status_code in(200,404): break
            time.sleep(8*(k+1))
        if r.status_code==404: return None,t
        if r.status_code!=200: return 'HTTP %d'%r.status_code,t
        os.makedirs('research/wikiraw',exist_ok=True); w=r.text; open(p,'w',encoding='utf-8').write(w); time.sleep(1.5)
    m=re.match(r'\s*#REDIRECT\s*\[\[([^\]|#]+)',w,re.I)
    return raw(m.group(1).strip(),hop+1) if m and hop<3 else (w,t)
def waiting(): return [s for s in S if s['st'] in ASK and 'bk' not in s and not s['id'].startswith('lm-')]
def colourless(): return [s for s in S if s['st'] in ASK and s.get('bk') in ('s','n') and 'bc' not in s and not s['id'].startswith('lm-')]      # red brick settled before colours were recorded (November 26, 2026): 'some' may be red or mixed, 'no' may be buff, dark, glazed, painted or no brick at all
def myfile():
    kf=os.path.join(W,'.brickkey')
    if not os.path.exists(kf): open(kf,'w').write(''.join(random.SystemRandom().choice('abcdefghjkmnpqrstvwxyz') for _ in range(4)))
    return 'tools/bricks_%s.py'%open(kf).read().strip()
a=sys.argv[1:]
if not a:
    by={}
    for s in S:
        if s['st'] not in ASK or s['id'].startswith('lm-'): continue
        r=by.setdefault(REGST.get(s['reg'],'?'),[0,0,0,0]); r[{'y':0,'s':1,'n':2}.get(s.get('bk'),3)]+=1
    print('Red brick, places that are standing, ruins or traces:  yes / some / no / not looked at')
    for k in sorted(by,key=lambda k:-by[k][3]):
        if sum(by[k])>1: print('  %-22s %3d %3d %3d %4d'%(STNAME.get(k,k),*by[k]))
    print('  (%d states and provinces with one place each are not listed)'%sum(1 for k in by if sum(by[k])==1))
    t=[sum(v[i] for v in by.values()) for i in range(4)]; print('  %-22s %3d %3d %3d %4d'%('all',*t))
    print('Brick colour: %d places have one; %d with a red-brick answer of some or no still wait for a colour (list them:  python3 tools/brick.py list --colour ).'%(sum(1 for x in S if x.get('bc')),len(colourless())))
    sys.exit(0)
if a[0]=='list':
    n=40; rest=[]; COL=False
    i=1
    while i<len(a):
        if a[i]=='--n': n=int(a[i+1]); i+=2
        elif a[i] in ('--colour','--color'): COL=True; i+=1
        else: rest.append(a[i]); i+=1
    w=colourless() if COL else waiting()
    if rest:
        q=' '.join(rest).lower(); st=[k for k,v in STNAME.items() if v.lower()==q or k==q]
        w=[s for s in w if (st and REGST.get(s['reg'])==st[0]) or s['reg']==q]
    random.SystemRandom().shuffle(w); w.sort(key=lambda s:wiki(s) is None)      # in no fixed order, so sessions working side by side take different places; those with an article first
    print(len(w),'places wait'+(' there' if rest else '')+'; the first',min(n,len(w)),':')
    for s in w[:n]:
        links=[(l[1] if isinstance(l,(list,tuple)) else str(l)) for l in (s.get('links') or [])][:3]
        print('  %s | %s, %s | %s | %s%s'%(s['id'],s['name'],s['town'],s['st'],'  '.join(links) or 'no link',(' | red brick: '+{'s':'some','n':'no'}[s['bk']]) if COL else ''))
    if COL: print('Each of these has a red-brick answer (the last column) and no colour yet. Look at a picture and record the answer again with its colour; keep the answer unless the picture shows it was wrong.')
    print('Next:  python3 tools/brick.py look <id>   then open the picture, then   python3 tools/brick.py set <id> yes|some|no "<what you saw; where>" --colour red|buff|dark|glazed|painted|mixed|none')
    sys.exit(0)
if a[0]=='look':
    s=BY.get(a[1]) or sys.exit('No such place id: '+a[1])
    os.makedirs('research/brick',exist_ok=True); out='research/brick/%s.jpg'%s['id']; src=None; n=1
    if '--pic' in a: k=a.index('--pic'); n=max(1,int(a[k+1])); del a[k:k+2]
    if len(a)>2: src=a[2]; page=a[2]
    else:
        t=wiki(s)
        if not t: sys.exit('%s has no Wikipedia link. Find a picture of it on one of its sources (%s) and run: brick.py look %s <picture address>'%(s['name'],'  '.join((l[1] if isinstance(l,(list,tuple)) else str(l)) for l in (s.get('links') or [])[:3]) or 'it has none',s['id']))
        # The article as raw text (the route tools/wiki_raw.py uses; Wikipedia's summary service answers 429 from cloud machines),
        # then the first picture it names, by file name, from Wikimedia Commons.
        t=urllib.parse.unquote(t).replace('_',' '); w,t2=raw(t)
        if not w or w.startswith('HTTP '): sys.exit('The article "%s" could not be read (%s). Try again later, or give a picture address.'%(t,w or 'no such article'))
        # every picture the article names, in order: the infobox picture first, then those in the text, with their captions
        pics=[]
        m=re.search(r'\|\s*(?:image|image_name|photo|image_skyline)\s*=\s*(?:\[\[)?(?:File:|Image:)?([^\|\]\n<{]+?\.(?:jpe?g|png))',w,re.I)
        if m:
            cap=re.search(r'\|\s*(?:caption|image_caption)[ \t]*=[ \t]*([^\n]*)',w); pics.append((m.group(1).strip(),cap.group(1) if cap else ''))
        for m in re.finditer(r'\[\[(?:File|Image):([^\|\]\n]+?\.(?:jpe?g|png))((?:\|(?:[^\[\]]|\[\[[^\]]*\]\])*)?)\]\]',w,re.I):
            if m.group(1).strip() not in [x[0] for x in pics]: pics.append((m.group(1).strip(),(m.group(2) or '').split('|')[-1]))
        if not pics: sys.exit('The article "%s" names no picture. Find one on the place\'s sources and give its address.'%t2)
        clean=lambda c:re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]|'{2,}|<[^>]+>|\{\{[^}]*\}\}",r'\1',c).strip()[:150]
        if n>len(pics): sys.exit('The article "%s" names only %d picture(s).'%(t2,len(pics)))
        print('Article: %s. It names %d picture(s):'%(t2,len(pics)))
        for k,(f,c) in enumerate(pics[:8],1): print('  %s%d. %s%s'%('>' if k==n else ' ',k,f,(' | '+clean(c)) if clean(c) else ''))
        fn=pics[n-1][0]
        src='https://commons.wikimedia.org/wiki/Special:FilePath/'+urllib.parse.quote(fn.replace(' ','_'))+'?width=960'; page='https://en.wikipedia.org/wiki/'+t2.replace(' ','_')
    import time
    for go in range(4):          # Wikimedia answers 429 when pictures are asked for quickly: wait and ask again
        try:
            d=urllib.request.urlopen(urllib.request.Request(src,headers=UA),timeout=60).read()
            if len(d)<2000: raise ValueError('too small to be a picture')
            open(out,'wb').write(d); break
        except Exception as ex:
            if go==3: sys.exit('The picture could not be fetched (%s). Wait a minute and try again.'%str(ex)[:70])
            time.sleep(10*(go+1))
    print('Saved %s (%d KB) from %s'%(os.path.join(W,out),len(d)//1024,src))
    if len(a)<=2: print('That is picture %d of the article. The first is often a drawing, a map or an old postcard: only a photograph of the place as it stands settles brick. For another:  python3 tools/brick.py look %s --pic <number>'%(n,s['id']))
    print('Open it and decide:')
    print('is it plainly %s (%s)? Then:  python3 tools/brick.py set %s yes|some|no "<what you saw>; %s" --colour red|buff|dark|glazed|painted|mixed|none'%(s['name'],s['town'],s['id'],page))
    print('The colour is the brick\'s own: red or red-brown; buff (yellow, cream, tan); dark (brown or black by its own colour, not soot); glazed; painted (its colour cannot be seen: never red brick, even painted red); mixed (red with another); none (no brick). Fire brick is never judged from a picture: add  --fire "<the source\'s words>"  only when a source says so.')
    sys.exit(0)
if a[0]=='set':
    import brickrule
    col=None; fire=''
    if '--colour' in a or '--color' in a: k=a.index('--colour' if '--colour' in a else '--color'); col=a[k+1].lower(); del a[k:k+2]
    if '--fire' in a: k=a.index('--fire'); fire=a[k+1].strip(); del a[k:k+2]
    if len(a)<4 or a[2] not in ('yes','some','no'): sys.exit('usage: brick.py set <id> yes|some|no "<what you saw, and where>" --colour red|buff|dark|glazed|painted|mixed|none [--fire "<the source\'s words>"]')
    if a[1] not in BY: sys.exit('No such place id: '+a[1])
    if len(a[3].strip())<12: sys.exit('Say how it is known: what the picture shows and its address, or the words of the source.')
    if col is None:
        if a[2]=='yes': col='red'
        else: sys.exit('Say the colour of the brick you saw as well:  --colour red|buff|dark|glazed|painted|mixed , or  --colour none  when there is no brick at all (stone, wood, concrete, earth). "some" goes with red or mixed; "no" with buff, dark, glazed, painted or none.')
    row=(a[2],a[3].strip(),col,fire); why=brickrule.row_problem(row)
    if why: sys.exit('Not recorded: '+why)
    f=myfile(); cur={}
    if os.path.exists(f): cur=dict(importlib.import_module(os.path.basename(f)[:-3]).BRICK)
    cur[a[1]]=row
    open(f,'w',encoding='utf-8').write('# Brick, looked up after the places were written (tools/brick.py set; the rules are in tools/brickrule.py).\n# id: (red brick yes|some|no, how it is known, the brick\'s colour or \'\', the words of a source that says fire brick or \'\')\nBRICK={\n'+''.join(' %r:%r,\n'%(k,tuple(v)) for k,v in sorted(cur.items()))+'}\n')
    print('Recorded in %s: %s = %s%s%s (%d in this file). It reaches the map at the next build.'%(f,a[1],a[2],', no brick at all' if col=='none' else ', colour '+col,', fire brick per a source' if fire else '',len(cur)))
    sys.exit(0)
sys.exit(__doc__)
