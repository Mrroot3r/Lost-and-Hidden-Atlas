#!/usr/bin/env python3
"""A sanity panel for tools/pockets.py: where do towns I expect to be old town centres land, and do places that are
not towns (estates, battlefields, cemeteries) stay out of the centres list?

   python3 tools/pock_panel.py           prints one line per panel entry and a pass count

Run it after changing any number in tools/pockets.py. The panel is New York round Albany, which the owner knows.
It needs cache/osm/ny_places.json (tools/osm_places.py ny) for the town positions, and build/pockets.json.
The towns that print MISSING with nothing nearby have no Register district and few plaques: no rule can find them.
The panel is a working aid, not published data."""
import json,math,sys
P=json.load(open('build/pockets.json'))['k']; PL=json.load(open('cache/osm/ny_places.json'))
def m(a,b,c,d): return math.hypot((c-a)*111320,(d-b)*111320*math.cos(math.radians(a)))
ALB=(42.6526,-73.7562)
TOWNS='''Kinderhook Hudson Catskill Athens Coxsackie Cohoes Waterford Troy Schenectady Albany Ballston_Spa Saratoga_Springs
Schuylerville Greenwich Cambridge Salem Hoosick_Falls Chatham Valatie Rensselaerville Altamont Schoharie Middleburgh
Cobleskill Sharon_Springs Cherry_Valley Canajoharie Fort_Plain Johnstown Amsterdam Coeymans New_Baltimore
Castleton-on-Hudson Cooperstown Stillwater Mechanicville Round_Lake Fonda Gloversville Glens_Falls Fort_Edward
Hudson_Falls Whitehall Granville Claverack Spencertown New_Lebanon Esperance Scotia Vischer_Ferry Saugerties Kingston
Rhinebeck Tivoli Oak_Hill Windham Prattsville Lake_George Waterville Clinton Skaneateles Geneva Lewiston'''.split()
NOT=[('Lindenwald',42.3697,-73.7040),('Olana',42.2177,-73.8290),('Saratoga battlefield',42.999,-73.637),('Albany Rural Cemetery',42.7075,-73.7290),
     ('Grant Cottage',43.2005,-73.7445),('Copake Iron Works',42.1195,-73.5140),('Bennington battlefield',42.9330,-73.3040),('Fort Ticonderoga',43.8417,-73.3875),
     ('West Point',41.3915,-73.9560),('Sagamore Hill',40.8855,-73.4990)]
ok=0; n=0
print('--- expected old town centres')
for t in TOWNS:
    nm=t.replace('_',' ')
    c=sorted((m(ALB[0],ALB[1],q['lat'],q['lon']),q) for q in PL if q['n']==nm)
    if not c: print(f'{nm:22} not in the settlements file'); continue
    q=c[0][1]; near=sorted((m(q['lat'],q['lon'],k[0],k[1]),k) for k in P if abs(k[0]-q['lat'])<0.03)
    near=[x for x in near if x[0]<1500]; n+=1
    hit=[x for x in near if x[1][10]=='c' and x[1][7]==nm]
    if hit:
        k=hit[0][1]; ok+=1; print(f'{nm:22} c {k[11]:5} {k[13]} plaques {k[3]:3} at {k[9]:3} spots, listed {k[4]:3}, district bldgs {k[6]:4}  {k[12]}')
    else: print(f'{nm:22} MISSING as a centre ({q["p"]}); nearby:',[(x[1][7][:28],x[1][10],x[1][11],round(x[0])) for x in near[:3]])
print(f'{ok} of {n} are centres under their own name')
print('--- expected NOT to be centres')
bad=0
for nm,la,lo in NOT:
    near=sorted((m(la,lo,k[0],k[1]),k) for k in P if abs(k[0]-la)<0.03); near=[x for x in near if x[0]<900]
    c=[x for x in near if x[1][10]=='c']; bad+=bool(c)
    print(f'{nm:22}',('CENTRE: ' if c else 'ok: ')+str([(x[1][7][:30],x[1][10],x[1][11],round(x[0])) for x in near[:2]]))
print(bad,'wrongly centres')
