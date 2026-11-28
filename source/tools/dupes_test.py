#!/usr/bin/env python3
"""The guard against one place entered twice (tools/dupes.py, used by tools/check.py).
   python3 tools/dupes_test.py [<clone>]      run it after changing dupes.py or how check.py uses it
What it holds the guard to. Two entries clash when they are on one spot (15 m) or carry the same name close by (300 m: the
same words, or one name inside the other, with the town's own words and anything in brackets left out). The pairs below are
the doubles found by hand on November 26, 2026, as they stood, and neighbours that are rightly two places. A clash is
settled in the entry itself, apart='<other id>: <why they are two places>'. check.py refuses a clash that involves the
newest batch (the one being published) and only warns about one between older entries, so that a pair which slipped in
cannot stop every other session."""
import sys,os,subprocess,tempfile,shutil,re
W=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(W,'tools')); sys.dont_write_bytecode=True
import dupes
fails=[]; n=[0]
def ok(name,cond,extra=''):
    n[0]+=1; print(('ok   ' if cond else 'FAIL ')+name+(('  ['+str(extra)[:200]+']') if extra!='' else ''))
    if not cond: fails.append(name)
def P(id,name,lat,lon,town='Sometown',**k): return dict(id=id,name=name,town=town,lat=lat,lon=lon,name2=k.pop('name2',''),**k)
def north(m): return m/111200.0          # metres to degrees of latitude
def kind(a,b):
    c=dupes.clash(a,b); return c and c[0]

# ---- the doubles found by hand, as they stood
ok('same name 99 m apart (St. George\'s, Austin)',kind(P('a',"St. George's Episcopal Church",39.0,-117.0,'Austin'),P('b',"St. George's Episcopal Church",39.0+north(99),-117.0,'Austin'))=='name')
ok('one name inside the other, 43 m apart (Five Combines)',kind(P('a','Five Combines locks',43.3,-73.58,'Hudson Falls'),P('b','Five Combines, Glens Falls Feeder Canal',43.3+north(43),-73.58,'Hudson Falls'))=='name')
ok('the town added to the name makes no difference (Insley House)',kind(P('a','Merritt Insley House and outbuildings',39.3,-94.9,'Leavenworth, Kansas'),P('b','Merritt Insley House and outbuildings, Leavenworth',39.3+north(120),-94.9,'Leavenworth, Kansas'))=='name')
ok('a bare name inside a longer one (Rush)',kind(P('a','Rush',36.13,-92.57,'Yellville'),P('b','Rush zinc-mining ghost town, Buffalo National River',36.13+north(200),-92.57,'Yellville'))=='name')
ok('a district and the place it is named for (Elkmont)',kind(P('a','Elkmont',35.65,-83.58,'Gatlinburg'),P('b','Elkmont Historic District',35.65+north(60),-83.58,'Gatlinburg'))=='name')
ok('two names for one building, 10 m apart, are caught by the spot (Lawrence library)',kind(P('a','Carnegie Library at Ninth and Vermont (old Lawrence public library)',38.9690,-95.2370,'Lawrence, Kansas'),P('b','Old Lawrence City Library (1904 Carnegie library)',38.9690+north(10),-95.2370,'Lawrence'))=='spot')
ok('a name given in brackets is not a name, but the words outside are (Roberts House, The Castle)',kind(P('a','John N. Roberts House ("The Castle"), Lawrence',38.96,-95.23,'Lawrence, Kansas'),P('b','The Castle (John N. Roberts House, Castle Tea Room)',38.96+north(37),-95.23,'Lawrence, Kansas'))=='name')
# ---- neighbours that are two places
ok('two mansions of one family, 65 m apart, are two places',kind(P('a','Asa Packer Mansion',40.86,-75.74),P('b','Harry Packer Mansion',40.86+north(65),-75.74)) is None)
ok('an opera house and a hotel of one name, 17 m apart, are two places',kind(P('a','Wareham Opera House',39.18,-96.56),P('b','Wareham Hotel',39.18+north(17),-96.56)) is None)
ok('the same name 400 m apart is not refused',kind(P('a','First Baptist Church',40.0,-75.0),P('b','First Baptist Church',40.0+north(400),-75.0)) is None)
ok('the same name 299 m apart is',kind(P('a','First Baptist Church',40.0,-75.0),P('b','First Baptist Church',40.0+north(299),-75.0))=='name')
ok('words in brackets do not make two branch libraries one',kind(P('a','Webster Library (Carnegie branch)',40.77,-73.95),P('b','Yorkville Library (Carnegie branch)',40.77+north(200),-73.95)) is None)
ok('a shared group title (name2) does not',kind(P('a','Griswold Opera House site',42.73,-73.69,'Troy',name2="Troy's lost theaters"),P('b','Troy Theatre site',42.73+north(114),-73.69,'Troy',name2="Troy's lost theaters")) is None)
ok('a name that begins with the town does not match every other in the town',kind(P('a','Kansas City, Kansas YMCA (8th Street)',39.11,-94.63,'Kansas City, Kansas'),P('b','Kansas City, Kansas High School Gymnasium',39.11+north(265),-94.63,'Kansas City, Kansas')) is None)
ok('16 m apart with different names is not a clash',kind(P('a','Smith Block',40.0,-75.0),P('b','Jones Hardware',40.0+north(16),-75.0)) is None)
ok('14 m apart is, whatever the names',kind(P('a','Smith Block',40.0,-75.0),P('b','Jones Hardware',40.0+north(14),-75.0))=='spot')
ok('"old", "former", "site" and "ruins" are not part of a name',kind(P('a','Old Stone Mill ruins',40.0,-75.0),P('b','Stone Mill',40.0+north(150),-75.0))=='name')
ok('accents and apostrophes make no difference',kind(P('a',"Église Saint-Rémi",46.0,-73.0),P('b','Eglise Saint-Remi',46.0+north(100),-73.0))=='name')
c=dupes.clash(P('a','Smith Block',40.0,-75.0),P('b','Jones Hardware',40.0+north(14),-75.0))
ok('a clash says how far apart the two are',c and 13<=c[1]<=15,c)
# ---- the whole list
L=[P('one','Scott Ice House',42.4,-73.78),P('two','Scott Ice House',42.4+north(80),-73.78),P('far','Scott Ice House',44.0,-73.78),P('lone','Brick Kiln',42.9,-73.0)]
f=dupes.find(L)
ok('find() gives each pair once, lower id first',[(x['a'],x['b'],x['kind']) for x in f]==[('one','two','name')],f)
L2=L+[P('three','Scott Ice House boathouse',42.4+north(5),-73.78,apart='one: the ice house stands beside this boathouse, a separate building')]
f=dupes.find(L2); pr={(x['a'],x['b']) for x in f}
ok('apart= on either entry settles that pair and no other',('one','three') not in pr and ('three','two') in pr and ('one','two') in pr,pr)
ok('find(only=...) reports only pairs that involve those ids',[(x['a'],x['b']) for x in dupes.find(L2,only={'three'})]==[('three','two')])
ok('a thin landmark pin clashes like any other entry',[(x['a'],x['b']) for x in dupes.find([P('lm-scott-ice-house','Scott Ice House',42.4,-73.78),P('scott-ice-house-nutten-hook','Scott Ice House',42.4+north(30),-73.78)])]==[('lm-scott-ice-house','scott-ice-house-nutten-hook')])
ln=dupes.line(dupes.find(L)[0],{p['id']:p for p in L})
ok('the line for a clash names both ids, the distance and both ways out',all(t in ln for t in('one','two','80 m',"was='","apart='")),ln)
ok('a name that only says what kind of thing it is does not sit inside every other',kind(P('a','The "Old House", 580 First Avenue',42.77,-73.67),P('b','Herman Melville House',42.77+north(241),-73.67)) is None)
ok('but two entries both called just that do clash',kind(P('a','Post Office',42.77,-73.67),P('b','Old Post Office',42.77+north(120),-73.67))=='name')
# ---- apart= itself
ids={'one','two','three'}
ok('apart= needs an id and a reason',dupes.apart_problem(P('three','X',0,0,apart='one'),ids) and dupes.apart_problem(P('three','X',0,0,apart='one: yes'),ids))
ok('apart= must name a place that exists',bool(dupes.apart_problem(P('three','X',0,0,apart='nobody-here: a separate building behind the hotel'),ids)))
ok('apart= cannot name the entry itself',bool(dupes.apart_problem(P('three','X',0,0,apart='three: a separate building behind the hotel'),ids)))
ok('a good apart= raises nothing',dupes.apart_problem(P('three','X',0,0,apart='one: the ice house stands beside this boathouse'),ids) is None)
ok('apart= may be a list',dupes.apart_problem(P('three','X',0,0,apart=['one: the ice house stands beside this boathouse','two: the second ice house, across the road']),ids) is None and dupes.apart_ids(P('three','X',0,0,apart=['one: aaaaaaaaaaaaaaaaa','two: bbbbbbbbbbbbbbbbbb']))=={'one','two'})

# ---- end to end: check.py on a copy of the sources with one batch added
REPO=sys.argv[1] if len(sys.argv)>1 else (open(os.path.join(W,'.repo')).read().strip() if os.path.exists(os.path.join(W,'.repo')) else '')
if not REPO or not os.path.isdir(os.path.join(REPO,'source','tools')): print('(no clone given: the end-to-end checks were skipped)')
else:
    d=tempfile.mkdtemp(); T=os.path.join(d,'source','tools')
    shutil.copytree(os.path.join(REPO,'source','tools'),T,ignore=shutil.ignore_patterns('__pycache__'))
    import glob as _g          # the workspace's own tools over the clone's, so a check.py that needs a module the clone does not have yet still runs; the place lists stay the clone's
    for f_ in _g.glob(os.path.join(W,'tools','*.py')):
        if not re.match(r'(data|pics|hours|bricks|legos)_',os.path.basename(f_)) or os.path.basename(f_)=='data_b.py': shutil.copy(f_,T)
    shutil.copytree(os.path.join(REPO,'source','src'),os.path.join(d,'source','src')); shutil.copytree(os.path.join(REPO,'notes'),os.path.join(d,'notes'))
    os.makedirs(os.path.join(d,'source','build')); shutil.copy(os.path.join(REPO,'source','build','states.json'),os.path.join(d,'source','build'))
    sys.path.insert(0,T); import data_b
    old=next(b for b in data_b.B if b['st']=='standing' and not b.get('was'))        # any long-standing entry will do
    def batch(extra,added='2099-01-01 00:00'):
        open(os.path.join(T,'data_zzzz_test.py'),'w').write("from data_b import N\nBATCH=dict(key='zzzz-test',label='Guard test',added=%r)\nPLACES=[N('zzzz-guard-test-place',%r,%r,%r,'landmark','standing',%r,%r,'exact','view','drive','','1900','A test entry.',brick='?'%s)]\nPIN_NOTES={}\n"%(added,old['name'],old['town'],old['reg'],old['lat']+north(40),old['lon'],extra))
    def run():
        out=subprocess.run([sys.executable,os.path.join(T,'check.py'),d,'--sources'],capture_output=True,text=True).stdout
        return [l for l in out.split('\n') if 'zzzz-guard-test-place' in l and ('same place' in l or 'apart=' in l)]
    # (the batch time is in the future, which check.py also refuses: only the lines about the pair are read here)
    batch(''); l=run()
    ok('check.py refuses a new entry that repeats an old one',len(l)==1 and l[0].startswith('ERROR') and old['id'] in l[0],l)
    batch(",apart=%r"%(old['id']+': a made-up second building for the test')); l=run()
    ok('and lets it through once apart= says why they are two',l==[],l)
    batch('',added='2020-01-01 00:00'); l=run()
    ok('a pair between older entries is a warning, not an error',len(l)==1 and l[0].startswith('warning'),l)
    batch(",apart='no-such-place-anywhere: a made-up second building'"); l=run()
    ok('check.py refuses an apart= that names no place',any(x.startswith('ERROR') and 'no-such-place-anywhere' in x for x in l),l)
    # a thin landmark pin (lm-...), which is in no place list: build_sites.py makes it from src/landmarks.json
    import json,glob
    gone=set(re.findall(r"was='(lm-[a-z0-9-]+)'",''.join(open(x,encoding='utf-8').read() for x in glob.glob(os.path.join(T,'data_*.py')))))
    bs=open(os.path.join(T,'build_sites.py'),encoding='utf-8').read(); skip=eval(re.search(r'^SKIP=(\{.*\})\s*$',bs,re.M).group(1)); fix=eval(re.search(r'^FIX=(\{.*\})\s*$',bs,re.M).group(1))
    L_=json.load(open(os.path.join(d,'source','src','landmarks.json'),encoding='utf-8')); G_=json.load(open(os.path.join(d,'source','src','g2.json'),encoding='utf-8'))
    i_,r_=next((i,r) for i,r in enumerate(L_) if i not in skip and i not in fix and 'lm-'+re.sub(r'[^a-z0-9]+','-',r['name'].lower()).strip('-')[:40] not in gone)
    lm='lm-'+re.sub(r'[^a-z0-9]+','-',r_['name'].lower()).strip('-')[:40]
    old=dict(old,name=r_['name'],town=r_['town'],lat=G_['L%d'%i_][0],lon=G_['L%d'%i_][1]); batch(''); l=run()
    ok('a new entry beside a thin landmark pin of the same name is refused, and told to replace it',any(x.startswith('ERROR') and "was='%s'"%lm in x for x in l),(lm,l))
    shutil.rmtree(d)
print(f'{len(fails)} FAILED' if fails else f'dupes test: {n[0]} checks passed'); sys.exit(1 if fails else 0)
