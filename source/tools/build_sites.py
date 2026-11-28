import json,sys,re
import brickrule, legorule, archrule, stonerule
sys.path.insert(0,'tools')
# Before a single place list is run: prove that each one is only data (tools/safe_data.py says why this matters).
import safe_data; safe_data.must('tools')
from data_a import A
from data_b import B
from data_c import FR,EXTRA_C
# Every tools/data_*.py file (other than the original catalogue files data_a and data_b) is a batch.
# It must define BATCH={'key','label','added'}, PLACES (a list of N(...) records) and PIN_NOTES (id -> one sentence).
import glob,os,importlib
BATCHES=[]; C=[]; PNC={}; BATCH_OF={}
for f in sorted(glob.glob('tools/data_*.py')):
    name=os.path.basename(f)[:-3]
    if name in ('data_a','data_b'): continue
    m=importlib.import_module(name)
    for need in ('BATCH','PLACES','PIN_NOTES'):
        if not hasattr(m,need): raise SystemExit(f'{name}.py must define {need} (see GUIDE.md section 4)')
    bt=dict(m.BATCH); bt['n']=len(m.PLACES); bt['file']=name; BATCHES.append(bt)
    for p in m.PLACES:
        if not m.PIN_NOTES.get(p['id']): raise SystemExit(f"{name}.py: place '{p['id']}' has no pin note")
        if p.get('st') not in ('ruins','traces','standing','marker','gone','water'): raise SystemExit(f"{name}.py: place '{p['id']}' has st='{p.get('st')}': it must be one of ruins, traces, standing, marker, gone, water (a wrong one used to stop the build later with a bare KeyError)")
        if re.search(r'\d|\s',p.get('tags') or ''): raise SystemExit(f"{name}.py: place '{p['id']}' has tags='{p['tags']}', which looks like years: an N(...) line is probably missing its tags argument ('' between eff and years), so every later field has moved one place along")
        BATCH_OF[p['id']]=bt['key']
    C+=m.PLACES; PNC.update(m.PIN_NOTES)
BATCHES.sort(key=lambda x:(x['added'],x['file']))
assert len({x['key'] for x in BATCHES})==len(BATCHES),'two batches share a key'
json.dump(BATCHES,open('build/batches.json','w'))
E=json.load(open('src/entries.json')); L=json.load(open('src/landmarks.json')); G2=json.load(open('src/g2.json'))
def conf_of(s):
    s=s.lower()
    if s.startswith('lead'): return 'lead'
    if 'lead' in s: return 'mixed'
    return 'verified'
def notes_text(n):
    look=' '.join(x for x in [n.get('Look for'),n.get('Also here') and ('Also here: '+n['Also here']),n.get('Lead') and ('Unconfirmed lead: '+n['Lead']),n.get('Source material') and ('Source material: '+n['Source material']),n.get('Background') and ('Background: '+n['Background']),n.get('note')] if x)
    return look
sites=[]
for row in A:
    i,id_,name,town,reg,cat,st,lat,lon,prec,acc,eff,tags,x=row
    e=E[i]
    s=dict(id=id_,name=name,name2=x.get('name2',''),town=town,reg=reg,cat=cat,st=st,lat=lat,lon=lon,prec=prec,acc=acc,eff=eff,
           tags=[t for t in tags.split(',') if t],years=x.get('years',''),conf=conf_of(e['conf']),
           story=e['story'],look=notes_text(e['notes']),hook=e['notes'].get('Hook',''),
           accn=x.get('accn') or e['notes'].get('Access',''),links=e['links'],now=('time-sensitive' in e['conf'] or 'new in 2026' in e['conf'] or 'now' in tags.split(',')))
    if x.get('th'): s['th']=x['th']; s['thn']=x.get('thn','')
    sites.append(s)
for b in B+C:
    e=E[b['p']] if b.get('p') is not None else None
    s=dict(id=b['id'],name=b['name'],name2=b.get('name2',''),town=b['town'],reg=b['reg'],cat=b['cat'],st=b['st'],lat=b['lat'],lon=b['lon'],prec=b['prec'],acc=b['acc'],eff=b['eff'],
           tags=[t for t in b['tags'].split(',') if t],years=b['years'],conf=(b['conf'] or '').lower() or (conf_of(e['conf']) if e else 'verified'),
           story=b['story'],look=b['look'],hook=b['hook'],accn=b['accn'],links=(b['links'] or (e['links'] if e else [])),now='now' in b['tags'].split(','))
    if b.get('th'): s['th']=b['th']; s['thn']=b.get('thn','')
    if b.get('brick') in ('yes','some','no'): s['bk']=b['brick'][0]      # red brick: y, s or n; left out when nobody has looked
    if brickrule.code(b.get('bcol')): s['bc']=brickrule.code(b['bcol'])   # the brick's colour: r, b(uff), d(ark), g(lazed), p(ainted), m(ixed), x (looked: no brick at all); left out when nobody could tell
    if legorule.code(b.get('lego')): s['lg']=legorule.code(b['lego'])        # "Legos" (mutules): p pegs, h holes, y yes of a kind not seen, n none; left out when nobody has looked (tools/legorule.py)
    if archrule.names(b.get('arch')): s['ar']=archrule.names(b['arch'])        # the architect or architects, one spelling each (tools/archrule.py)
    if archrule.names(b.get('builder')): s['bb']=archrule.names(b['builder'])  # who built it, when a source says so and it is not the architect
    if (b.get('stone') or '').strip(): s['sx']=b['stone'].strip()            # the words cut on the building, as cut (tools/stonerule.py)
    if b.get('trig')=='yes': s['tg']=1                                     # the grooved blocks that go with them (triglyphs)
    if (b.get('fireb') or '').strip(): s['fb']=1                          # a source says fire brick is there
    if b.get('tip'): s['tip']=b['tip']                                   # the day a reader sent it in; left out for every other place
    if (b.get('hours') or '').strip() not in ('','?'): s['hrs']=b['hours'].strip()   # when it is open, as a source gave it; '?' means looked for and not found
    sites.append(s)
# landmarks
LREG={'Albany':'alb','Menands':'albco','Normanskill Farm':'alb','Rensselaer':'renss','Troy':'troy','Cohoes':'conf','Waterford':'conf','Schenectady':'sch','Rotterdam Junction':'mohawk','Scotia':'mohawk','Colonie':'albco','Fort Hunter':'mohawk','Schoharie':'mohawk','Saratoga Springs':'sar','Mount McGregor':'sar','Catskill':'hud','Hudson':'hud','Coxsackie':'hud','Hudson River':'hud','Woodstock':'cat','Saugerties':'cat','Ticonderoga':'adk','Raquette Lake':'adk'}
FIX={3:(42.6537,-73.7503),8:(42.6485,-73.7497),12:(42.6338,-73.7968),25:(42.8177,-73.9297),29:(42.7412,-73.8160),7:(42.65148,-73.74951),17:(42.7324,-73.6880)}
SKIP={30,37,38}
def slug(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
for i,r in enumerate(L):
    if i in SKIP: continue
    g=G2.get(f'L{i}'); lat,lon=(FIX[i] if i in FIX else (g[0],g[1]))
    v=r['visit'].lower()
    acc='public'
    if 'exterior' in v or 'private' in v or 'from the road' in v: acc='view'
    # a museum, a house shown by tour, a working theatre: you go in, at set times (GUIDE.md section 4, the access types)
    if acc=='public' and re.search(r'^museum|house museum|museum and grounds|\btours?\b|working theat|concert hall|check (?:hours|season)',v): acc='open'
    if 'call ahead' in v: acc='ask'
    sites.append(dict(id='lm-'+slug(r['name'])[:40],name=r['name'],name2='',town=r['town'],reg=LREG.get(r['town'],'alb'),cat='landmark',st='standing',lat=lat,lon=lon,
        prec='site' if i in (11,12,23) else 'exact',acc=acc,eff='drive',tags=[],years=r['built'],conf='reference',
        story=r['why']+'.',look='',hook='',accn=r['visit']+'. Open the Google Maps link for current hours.',links=[],now=False))
from pinnotes import PN,EXTRA_LOOK
PN=dict(PN); PN.update(PNC)
for s in sites:
    if s['id'] in PN: s['pn']=PN[s['id']]
    if s['id'] in EXTRA_LOOK: s['look']=(s['look']+EXTRA_LOOK[s['id']]).strip()
    if s['id'] in FR: s['fr']=FR[s['id']]
    if s['id'] in BATCH_OF: s['new']=BATCH_OF[s['id']]
    if s['id'] in EXTRA_C: s['story']=(s['story']+EXTRA_C[s['id']]).strip()
# Red brick found out after a place was written: tools/bricks_*.py, each BRICK={id:(yes|some|no, how it is known)} (tools/brick.py writes them).
# A place's own brick= wins; among these files the later name wins.
BRICKS={}
for f in sorted(glob.glob('tools/bricks_*.py')):
    BRICKS.update(importlib.import_module(os.path.basename(f)[:-3]).BRICK)
for s in sites:
    v=BRICKS.get(s['id'])
    if v and 'bk' not in s and v[0] in ('yes','some','no'): s['bk']=v[0][0]
    if v and len(v)==4:          # a row may also carry the colour and a fire-brick source (tools/brickrule.py); the place's own values win, field by field
        if 'bc' not in s and brickrule.code(v[2]): s['bc']=brickrule.code(v[2])
        if 'fb' not in s and (v[3] or '').strip(): s['fb']=1
    if s.get('bk')=='y' and 'bc' not in s: s['bc']='r'      # "red brick is the main thing you see" says the colour already
    if s.get('bk')=='n' and s.get('bc') in ('r','m'): del s['bc']      # a place list and a later look disagree: the red-brick answer stands, the colour is dropped
# "Legos" found out after a place was written: tools/legos_*.py, each LEGO={id:(pegs|holes|yes|no, triglyphs yes|no|'', how it is known)}
# (tools/legos.py writes them). A place's own lego= and trig= win, field by field; among these files the later name wins.
LEGOS={}
for f in sorted(glob.glob('tools/legos_*.py')):
    LEGOS.update(importlib.import_module(os.path.basename(f)[:-3]).LEGO)
for s in sites:
    v=LEGOS.get(s['id'])
    if v and 'lg' not in s and legorule.code(v[0]): s['lg']=legorule.code(v[0])
    if v and 'tg' not in s and v[1]=='yes': s['tg']=1
# Who designed or built a place, found out after it was written: tools/archs_*.py, each ARCH={id:(architects, builder, how it is known)}
# (tools/archs.py writes them). A place's own arch= and builder= win, field by field; among these files the later name wins.
ARCHS={}
for f in sorted(glob.glob('tools/archs_*.py')):
    ARCHS.update(importlib.import_module(os.path.basename(f)[:-3]).ARCH)
for s in sites:
    v=ARCHS.get(s['id'])
    if v and 'ar' not in s and archrule.names(v[0]): s['ar']=archrule.names(v[0])
    if v and 'bb' not in s and archrule.names(v[1]): s['bb']=archrule.names(v[1])
# The words cut on a building, found out after the place was written: tools/stones_*.py, each STONE={id:(words, how they are known)}
# (tools/stones.py writes them). A place's own stone= wins. The kind (sk) and the year (sy) are read from the words, and sd says
# the stone's year is outside the years the write-up gives, so the page can say both.
STONES={}
for f in sorted(glob.glob('tools/stones_*.py')):
    STONES.update(importlib.import_module(os.path.basename(f)[:-3]).STONE)
for s in sites:
    v=STONES.get(s['id'])
    if v and 'sx' not in s and str(v[0]).strip(): s['sx']=str(v[0]).strip()
    if 'sx' in s:
        s['sk']=stonerule.kind(s['sx']); _y=stonerule.year(s['sx'])
        if _y: s['sy']=_y
        if stonerule.differs(_y,s.get('years')): s['sd']=1
_one=archrule.unify([s.get('ar',[])+s.get('bb',[]) for s in sites])      # one spelling for one name across the whole map, so a tap on it finds every place
for s in sites:
    for _k in ('ar','bb'):
        if _k in s: s[_k]=_one(s[_k])
# Hours looked up after a place was written: tools/hours_*.py, each HOURS={id:(hours, day read 'YYYY-MM-DD', the page's address, opens)}
# (tools/hours.py writes them). They win over the place's own hours=, carry their own date, and when 'opens' is true a place
# that was only 'view' or 'public' becomes 'open'. hours '?' means looked for and not found: nothing is shown.
HOURS={}
for f in sorted(glob.glob('tools/hours_*.py')):
    HOURS.update(importlib.import_module(os.path.basename(f)[:-3]).HOURS)
for s in sites:
    v=HOURS.get(s['id'])
    if not v or v[0].strip() in ('','?'): continue
    s['hrs']=v[0].strip(); s['hrd']=v[1][:7]; s['hru']=v[2]
    if len(v)>3 and v[3] and s['acc'] in ('view','public'): s['acc']='open'
# A full entry can take the place of an older, thinner one for the same place: was='lm-mabee-farm'. The old pin is dropped
# here, and the app is told (build/alias.json, D.alias) so a reader's notes, status and trip stop move to the new id.
ALIAS={}
for b in B+C:
    for o in ([b['was']] if isinstance(b.get('was'),str) and b.get('was') else list(b.get('was') or [])):
        if o in ALIAS: raise SystemExit(f"Two places say they replace '{o}': {ALIAS[o]} and {b['id']}")
        ALIAS[o]=b['id']
if ALIAS:
    import math
    by={s['id']:s for s in sites}
    for o,n in ALIAS.items():
        if o in by:
            a,c=by[o],by[n]; m=math.hypot((a['lat']-c['lat'])*111000,(a['lon']-c['lon'])*111000*math.cos(math.radians(a['lat'])))
            # it was 600 m; some thin landmark pins sit over a kilometre from the place they name (Oakwood Cemetery's), and a full entry could not replace them
            if m>1500: raise SystemExit(f"{n} says it replaces '{o}', but that pin is {int(m)} m away: was= is for the same place only")
    sites=[s for s in sites if s['id'] not in ALIAS]
json.dump(ALIAS,open('build/alias.json','w'),indent=0,sort_keys=True)
ids=[s['id'] for s in sites]
dup=sorted({i for i in ids if ids.count(i)>1})
if dup: raise SystemExit('Duplicate place ids: '+', '.join(dup)+'. Ids are shared across every state, so add a town or state suffix to the NEW one (queens-fort-exeter). Never rename an id that is already published.')
import plainwords      # workshop talk out of what a reader sees ("in this session", a tool's name in a pin note): wording only
sites=[plainwords.site(x) for x in sites]
json.dump(sites,open('build/sites.json','w'),indent=1,ensure_ascii=False)
from collections import Counter
print(len(sites),Counter(s['cat'] for s in sites),Counter(s['st'] for s in sites),Counter(s['prec'] for s in sites),Counter(s['reg'] for s in sites))
miss=[e['i'] for e in E if e['i'] not in {r[0] for r in A} and e['i'] not in {b['p'] for b in B}]
print('unused entries',miss)
