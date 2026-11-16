#!/usr/bin/env python3
"""Make the outline of a state or province for build/states.json (GUIDE.md section 8).

   python3 tools/outlines.py            add every US state and Canadian province that is not in the file yet
   python3 tools/outlines.py tx on      (re)make only these keys

The app and check.py use the outlines to tell which state a point is in. They do not draw them, so the
outlines are kept coarse. Outlines already in build/states.json are never changed unless you name their key.

Sources, downloaded once into cache/outl/ (needs: pip install pyshp shapely):
  US states   Census cartographic boundary file, 1:20,000,000 (cb_2023_us_state_20m), www2.census.gov
  Canada      Natural Earth 1:10,000,000 admin-1 states and provinces, naciscdn.org
How each outline is made: the state's shape is pushed out by about 3 km so that pins on a shore, a pier or a
near island still fall inside it, then every other state's and province's land is cut away so neighbours do
not overlap, then it is simplified and small islands are dropped. Each ring is stored closed, as a flat list
[lon, lat, lon, lat, ...] with three decimals, the same as the original Northeast outlines.
A country other than the US or Canada needs its own source added to load() below."""
import sys,os,json,io,zipfile,urllib.request
import shapefile
from shapely.geometry import shape,Polygon,MultiPolygon
from shapely.ops import unary_union
C='cache/outl'; os.makedirs(C,exist_ok=True)
SRC={'us':('https://www2.census.gov/geo/tiger/GENZ2023/shp/cb_2023_us_state_20m.zip','cb_2023_us_state_20m'),
     'ne':('https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_1_states_provinces.zip','ne_10m_admin_1_states_provinces')}
PROV={'BC':'bc','AB':'ab','SK':'sk','MB':'mb','ON':'on','QC':'qc','NB':'nb','NS':'ns','PE':'pe','NL':'nl'}   # territories are left out
COARSE={'ak':0.05,'bc':0.04,'qc':0.04,'nl':0.04,'on':0.03,'mb':0.03,'sk':0.03,'ab':0.03,'ns':0.02,'nb':0.02}   # simplify tolerance in degrees; 0.012 otherwise
def get(k):
    url,name=SRC[k]; d=os.path.join(C,name)
    if not os.path.exists(os.path.join(d,name+'.shp')):
        print('downloading',url)
        z=zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'lost-hidden-atlas-research/1.0'}),timeout=300).read())); z.extractall(d)
    return shapefile.Reader(os.path.join(d,name+'.shp'))
def west_only(g):
    """Alaska's Aleutians cross the 180th meridian; keep the part with negative longitudes."""
    ps=[p for p in (g.geoms if isinstance(g,MultiPolygon) else [g]) if p.bounds[2]<0]
    return MultiPolygon(ps)
def load():
    G={}; other=[]
    r=get('us')
    for sr in r.shapeRecords():
        k=sr.record['STUSPS'].lower()
        if k=='pr': continue
        g=shape(sr.shape.__geo_interface__).buffer(0)
        G[k]=west_only(g) if k=='ak' else g
    n=get('ne')
    for sr in n.shapeRecords():
        if sr.record['adm0_a3']!='CAN': continue
        g=shape(sr.shape.__geo_interface__).buffer(0)
        k=PROV.get(sr.record['postal'])
        if k: G[k]=g
        else: other.append(g)
    return G,other
def rings(g,tol,minarea):
    g=g.simplify(tol,preserve_topology=True)
    ps=sorted((p for p in (g.geoms if isinstance(g,MultiPolygon) else [g]) if p.area>=minarea),key=lambda p:-p.area)
    out=[]
    for p in ps:
        xy=list(p.exterior.coords); flat=[]
        for x,y in xy: flat+= [round(x,3),round(y,3)]
        out.append(flat)
    return out
if __name__=='__main__':
    P='build/states.json'; S=json.load(open(P))
    G,other=load()
    want=[k.lower() for k in sys.argv[1:]] or [k for k in sorted(G) if k not in S]
    for k in want:
        if k not in G: print('no source shape for',k); continue
        rest=unary_union([g for j,g in G.items() if j!=k]+other)
        g=G[k].buffer(0.03).difference(rest).union(G[k]).buffer(0)
        tol=COARSE.get(k,0.012)
        rs=rings(g,tol,0.004 if k!='hi' else 0.002)
        S[k]=rs; print(k,len(rs),'rings',sum(len(r) for r in rs)//2,'points')
    json.dump(S,open(P,'w'),separators=(',',':'))
    print('wrote',P,os.path.getsize(P),'bytes,',len(S),'outlines')
