#!/usr/bin/env python3
"""Build the "Stone walls" map layer from the walls found in each swept unit (lidar/walls/<unit>.json, written by
tools/lidar.py; the finder is tools/lidar_walls.py). No network, standard library only: the site build runs it.
Only pieces that form a run, a corner or a yard are put on the map (tools/walls_structure.py says why and how); the
unit files keep everything the finder drew.

   python3 tools/walls.py          writes build/walls.json and build/walls/<cell>.json

  build/walls.json     small, fetched when the layer is switched on:
      {"n": pieces, "km": total, "units": [names], "c": {"<cell>": pieces, ...},     which cells hold walls
       "d": [[i, j, metres], ...]}                                                   wall length in each 0.005-degree box
      A box (i, j) covers latitude i*0.005 .. +0.005 and longitude j*0.005 .. +0.005. The app shades them when zoomed out,
      which shows where the old farms were.
  build/walls/<cell>.json   one per 0.05-degree cell that has walls, fetched when the map is zoomed in there:
      {"o": [lat, lon] of the cell's south-west corner in 0.00001 degree, "w": [[dlat0, dlon0, dlat1, dlon1], ...]}
      A cell is named "<floor(lat/0.05)>_<floor(lon/0.05)>". A piece goes in the cell its middle falls in.
tools/make.py copies both into the site's data/ folder."""
import json,glob,os,math,shutil,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from walls_structure import structured
CELL=5000; BOX=500                        # in units of 0.00001 degree
units=[]; cells={}; dens={}; total=0.0; n=0; drawn=0; left=[]
for f in sorted(glob.glob('lidar/walls/*.json')):
    u=json.load(open(f)); keep=structured(u['w']); drawn+=len(u['w'])
    ws=[w for w,k in zip(u['w'],keep) if k]            # only pieces that are part of a run, a corner or a yard (tools/walls_structure.py)
    if ws: units.append(u['name'])
    else: left.append(u['name'])
    for a,b,c,d in ws:
        la=(a+c)//2; lo=(b+d)//2; k=(la//CELL,lo//CELL); cells.setdefault(k,[]).append((a,b,c,d))
        m=math.hypot((c-a)*1.1132,(d-b)*1.1132*math.cos(math.radians(la/1e5))); total+=m; n+=1
        kb=(la//BOX,lo//BOX); dens[kb]=dens.get(kb,0)+m
shutil.rmtree('build/walls',ignore_errors=True); os.makedirs('build/walls')
for (i,j),ws in cells.items():
    o=[i*CELL,j*CELL]; ws.sort()
    json.dump({'o':o,'w':[[a-o[0],b-o[1],c-o[0],d-o[1]] for a,b,c,d in ws]},open('build/walls/%d_%d.json'%(i,j),'w'),separators=(',',':'))
idx={'n':n,'km':round(total/1000,1),'units':units,'c':{'%d_%d'%k:len(v) for k,v in sorted(cells.items())},'d':[[i,j,round(m)] for (i,j),m in sorted(dens.items()) if m>=60]}
json.dump(idx,open('build/walls.json','w'),separators=(',',':'))
print('walls:',n,'of',drawn,'pieces kept,',idx['km'],'km in',len(units),'units'+(' (nothing kept in: '+', '.join(left)+')' if left else '')+';',len(cells),'cells,',len(idx['d']),'shaded boxes;',sum(os.path.getsize(p) for p in glob.glob('build/walls/*.json'))//1024,'KB of cell files')
