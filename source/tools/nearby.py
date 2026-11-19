#!/usr/bin/env python3
"""What the Atlas already knows round a spot: run this FIRST for any area, before searching the web.
   python3 tools/nearby.py <lat> <lon> [km=8]        (get the lat,lon of a town with: python3 tools/nom.py "Town, State")
Prints 1. places already in the Atlas there (do not add them again);
       2. unchecked leads the Atlas already carries there: OpenStreetMap ruins and old sites, vanished places from the
          federal names file, old mines and quarries. A named lead is a ready-made starting point: it has a coordinate,
          so all it needs is a source and an owner. (All three kinds cover every state; the OpenStreetMap leads cover the
          ten provinces too, the other two do not.)
       3. a reminder to read LEADS.md for the same towns.
Run it from the workspace. It builds the place list itself if setup has not."""
import sys,json,math,os,re
try: la,lo=float(sys.argv[1]),float(sys.argv[2]); km=float(sys.argv[3]) if len(sys.argv)>3 else 8.0
except (IndexError,ValueError): sys.exit(__doc__)
def d(a,b): return math.hypot((a-la)*111.32,(b-lo)*111.32*math.cos(math.radians(la)))
def comp(a,b):
    e=(b-lo)*math.cos(math.radians(la)); n=a-la
    return 'N NE E SE S SW W NW'.split()[int((math.degrees(math.atan2(e,n))+382.5)%360//45)]
if not os.path.exists('build/sites.json'):                # a fresh workspace: make the place list first (a second, no network)
    import subprocess; subprocess.run([sys.executable,os.path.join(os.path.dirname(os.path.abspath(__file__)),'build_sites.py')],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
S=[s for s in json.load(open('build/sites.json')) if d(s['lat'],s['lon'])<=km]
print(f'== Already in the Atlas within {km:g} km: {len(S)}')
for s in sorted(S,key=lambda s:d(s['lat'],s['lon'])): print(f"  {d(s['lat'],s['lon']):4.1f} km {comp(s['lat'],s['lon']):2}  {s['id']}  |  {s['name']}, {s['town']}  [{s['st']}/{s['acc']}]"+("   <- a thin landmark pin from the first catalogue. If you write a full entry for this same place, give yours was='"+s['id']+"' so it replaces the pin (GUIDE.md section 4); do not leave both" if s['id'].startswith('lm-') else ''))
for f,title in (('leads','OpenStreetMap leads (mapped ruins and old sites)'),('vanished','Vanished places (federal names file)'),('mines','Old mines and quarries (USGS)')):
    p='build/%s.json'%f
    if not os.path.exists(p): continue
    L=json.load(open(p)); P=[x for x in L['p'] if d(x[0],x[1])<=km]
    named=[x for x in P if str(x[3]).strip()]
    # numbered district schools are many and seldom lead anywhere: count them, do not list them
    dull=[x for x in named if re.match(r'(School|District)( School)? (Number|No\.?) ?\d+|District (Number )?\d+ School',str(x[3]))]; named=[x for x in named if x not in dull]
    print(f'== {title}: {len(P)} within {km:g} km, {len(named)} with a name')
    for x in sorted(named,key=lambda x:d(x[0],x[1]))[:60]: print(f"  {d(x[0],x[1]):4.1f} km {comp(x[0],x[1]):2}  {x[3]}  |  {L['t'][x[2]]}  |  {x[0]}, {x[1]}")
    if len(named)>60: print(f'  ... {len(named)-60} more: use a smaller distance')
    if dull: print(f'  and {len(dull)} numbered district schools, not listed')
    un={}
    for x in P:
        if not str(x[3]).strip(): un[L['t'][x[2]]]=un.get(L['t'][x[2]],0)+1
    if un: print('  without a name: '+', '.join(f'{v} {k.lower()}' for k,v in un.items()))
    if f=='leads' and os.path.exists('build/leads_native.json'):      # the switched-off category: counted, not listed
        nat=[x for x in json.load(open('build/leads_native.json'))['p'] if d(x[0],x[1])<=km]
        if nat: print(f'  and {len(nat)} more in the category a reader must switch on (Native American sites, leads on reservation land), not listed here. One belongs in the Atlas only where whoever manages it invites visitors and says so on its own page (GUIDE.md section 8).')
    for x in sorted([x for x in P if not str(x[3]).strip()],key=lambda x:d(x[0],x[1]))[:25]: print(f"  {d(x[0],x[1]):4.1f} km {comp(x[0],x[1]):2}  (no name)  |  {L['t'][x[2]]}  |  {x[0]}, {x[1]}   <- look at it: python3 tools/look.py out.jpg lead,{x[0]},{x[1]},150")
print('== Also read LEADS.md for these towns (grep the town names), and try its rows before hunting for new names.')
