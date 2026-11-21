#!/usr/bin/env python3
"""Turn the owner's visit reports into a list of corrections (GUIDE.md section 6, "Visit reports").

   python3 tools/visits.py additions.json            prints the worklist
   python3 tools/visits.py additions.json --ledger   also notes each visit to a LiDAR lead on its candidate in lidar/units/

additions.json is what "Copy my additions for Claude" gives in the app (Settings, Your data): paste it into a file.
A visit report is the best source the Atlas has: the owner stood there. What to do with each, by what he found:
  found it        the place is real. A LiDAR lead can lose conf='lead' (make it 'verified'); rewrite "look" from his words,
                  keep "Not checked on the ground" out, and say in the pin note that he confirmed it and when.
  something else  rewrite the texts to say what is there; change cat or st if they are now wrong.
  nothing there   say so in "look" and set st='gone', or take the place out if it was only ever a LiDAR lead.
  could not get   put what stopped him in the access note (accn); change acc if the land turned out closed.
A true spot more than a few metres from the pin: move the pin to it, set prec='exact', and say so in PIN_NOTES.
Never rename the place id. The standard library only; no network."""
import sys,json,math,os,datetime
V={'found':'FOUND IT','else':'SOMETHING ELSE IS THERE','nothing':'NOTHING THERE','blocked':'COULD NOT GET TO IT'}
def metres(a,b,c,d): return math.hypot((c-a)*111320,(d-b)*111320*math.cos(math.radians(a)))
a=[x for x in sys.argv[1:] if not x.startswith('--')]
if not a: print(__doc__); sys.exit(0)
j=json.load(open(a[0],encoding='utf-8')); vs=j.get('visits') if isinstance(j,dict) else j
# Spots: bare marks the owner dropped on buildings he wants researched ("Spot many" in the app). He can tell what is old at a
# glance and place a mark in a second, so these come before any other lead. Each is printed as a LEADS.md row; start.py finds a
# row by the coordinate in it and lists the owner's spots first.
sp=(j.get('spots') if isinstance(j,dict) else None) or []
if sp:
    print('SPOTS: %d building(s) the owner marked for research. Put these rows at the top of the table in LEADS.md; delete a row when its place is added.'%len(sp))
    for x in sp:
        note=str(x.get('note') or '').replace('|','/').strip()
        print('| Spot %s (owner, %s) | %.5f, %.5f | The owner marked this building as old and worth researching%s | Everything: work out which building stands at this point, then research it |'%(x.get('n','?'),x.get('t','?'),x['lat'],x['lon'],(': "'+note+'"') if note else ''))
    print()
if not vs: print('No visit reports in that file.'); sys.exit(0)
ledger='--ledger' in sys.argv; L=None
if ledger:
    sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import lidar; L=lidar.load()
n=0
for p in sorted(vs,key=lambda p:p['id']):
    for r in p['reports']:
        n+=1; lead=p.get('cat')=='lidar'
        print('%s  %s  %s%s' % (r.get('t','?'),p['id'],V.get(r.get('v'),r.get('v')),'   (a LiDAR lead)' if lead else ''))
        print('   %s, %s' % (p['name'],p.get('town') or '?'))
        if r.get('x'): print('   what is there: '+r['x'])
        if r.get('a'): print('   access as found: '+r['a'])
        if r.get('at'):
            d=metres(p['pin'][0],p['pin'][1],r['at'][0],r['at'][1])
            print('   true spot %.6f,%.6f, %d m from the Atlas pin %s' % (r['at'][0],r['at'][1],d,'-> MOVE THE PIN there, prec=\'exact\', and say so in the pin note' if d>=5 else '(the pin is right)'))
        todo={'found':"confirm it: conf='verified'"+(' (drop conf=\'lead\')' if lead else '')+', rewrite "look" from his words','else':'rewrite the texts; check cat and st','nothing':"say so in \"look\" and set st='gone'"+(', or take this lead out' if lead else ''),'blocked':'put what stopped him in accn; check acc'}.get(r.get('v'))
        if p.get('mine'): todo='this is a place he added himself: fold it into a batch with his words as the source'
        if todo: print('   to do: '+todo)
        if L is not None and lead:
            hit=[(u,c) for u,c in lidar.allc(L) if c.get('place')==p['id']]
            if hit:
                u,c=hit[0]; c['visit']={'when':r.get('t'),'v':r.get('v'),'note':(r.get('x') or '')[:300]}
                if r.get('at'): c['visit']['at']=r['at']
                lidar.save(u); print('   noted on LiDAR candidate '+c['id'])
            else: print('   (no LiDAR candidate is recorded for this place)')
        print()
print('%d visit report(s) for %d place(s).' % (n,len(vs)))
