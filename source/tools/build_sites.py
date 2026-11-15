import json,sys,re
sys.path.insert(0,'tools')
from data_a import A
from data_b import B
from data_c import C,PNC,FR,EXTRA_C
from data_ma import M,PNM
from data_worc import X,PNX
C=C+M+X; PNC=dict(PNC); PNC.update(PNM); PNC.update(PNX)
NEW2={m['id'] for m in M}
NEW3={x['id'] for x in X}
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
    if 'call ahead' in v: acc='ask'
    sites.append(dict(id='lm-'+slug(r['name'])[:40],name=r['name'],name2='',town=r['town'],reg=LREG.get(r['town'],'alb'),cat='landmark',st='standing',lat=lat,lon=lon,
        prec='site' if i in (11,12,23) else 'exact',acc=acc,eff='drive',tags=[],years=r['built'],conf='reference',
        story=r['why']+'.',look='',hook='',accn=r['visit']+'. Open the Google Maps link for current hours.',links=[],now=False))
from pinnotes import PN,EXTRA_LOOK
PN=dict(PN); PN.update(PNC)
NEWIDS={c['id'] for c in C}
for s in sites:
    if s['id'] in PN: s['pn']=PN[s['id']]
    if s['id'] in EXTRA_LOOK: s['look']=(s['look']+EXTRA_LOOK[s['id']]).strip()
    if s['id'] in FR: s['fr']=FR[s['id']]
    if s['id'] in NEWIDS: s['new']=True
    if s['id'] in NEW2: s['new']=2
    if s['id'] in NEW3: s['new']=3
    if s['id'] in EXTRA_C: s['story']=(s['story']+EXTRA_C[s['id']]).strip()
ids=[s['id'] for s in sites]; assert len(ids)==len(set(ids)),[i for i in ids if ids.count(i)>1]
json.dump(sites,open('build/sites.json','w'),indent=1,ensure_ascii=False)
from collections import Counter
print(len(sites),Counter(s['cat'] for s in sites),Counter(s['st'] for s in sites),Counter(s['prec'] for s in sites),Counter(s['reg'] for s in sites))
miss=[e['i'] for e in E if e['i'] not in {r[0] for r in A} and e['i'] not in {b['p'] for b in B}]
print('unused entries',miss)
