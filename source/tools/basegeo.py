import json
from shapely.geometry import shape, box, mapping
BB=box(-75.35,41.2,-69.85,44.45)
def clip(fn,keep=lambda p:True,simp=0.002,props=()):
    out=[]
    for f in json.load(open('cache/ne/'+fn))['features']:
        if not f.get('geometry'): continue
        p=f['properties']
        if not keep(p): continue
        g=shape(f['geometry'])
        if not g.intersects(BB): continue
        g=g.intersection(BB).simplify(simp)
        if g.is_empty: continue
        out.append((g,{k:p.get(k) for k in props}))
    return out
def rnd(c):
    if isinstance(c[0],(int,float)): return [round(c[0],4),round(c[1],4)]
    return [rnd(x) for x in c]
def lines(geoms):
    res=[]
    for g,p in geoms:
        m=mapping(g)
        t=m['type']
        if t=='LineString': res.append(rnd(m['coordinates']))
        elif t=='MultiLineString': res+=[rnd(c) for c in m['coordinates']]
        elif t=='Polygon': res.append(rnd(m['coordinates'][0]))
        elif t=='MultiPolygon': res+=[rnd(c[0]) for c in m['coordinates']]
        elif t=='GeometryCollection':
            for gg in g.geoms: res+=lines([(gg,p)])
    return res
riv=clip('ne_10m_rivers_lake_centerlines.geojson',simp=0.0015)+clip('ne_10m_rivers_north_america.geojson',simp=0.0015)
lak=clip('ne_10m_lakes.geojson',simp=0.001)+clip('ne_10m_lakes_north_america.geojson',simp=0.001)
cty=clip('ne_10m_admin_2_counties.geojson',keep=lambda p:(p.get('REGION') or p.get('REGION_COD') or p.get('ISO_3166_2') or '') is not None,simp=0.003,props=('NAME','REGION'))
rd=clip('ne_10m_roads.geojson',keep=lambda p:p.get('type') in ('Major Highway','Beltway','Secondary Highway') ,simp=0.002,props=('type','name'))
print(len(riv),len(lak),len(cty),len(rd))
towns=[['Worcester',42.2626,-71.8023,1],['Springfield',42.1015,-72.5898,1],['Boston',42.3601,-71.0589,1],['Pittsfield',42.4501,-73.2454,1],['Fitchburg',42.5834,-71.8023,0],['Lowell',42.6334,-71.3162,0],['Greenfield',42.5879,-72.5994,0],['Northampton',42.3251,-72.6412,0],['New Bedford',41.6362,-70.9342,0],['Hyannis',41.6525,-70.2881,0],['Gloucester',42.6159,-70.6620,0],['Providence',41.8240,-71.4128,0],['Hartford',41.7658,-72.6734,0],['Albany',42.6526,-73.7562,1],['Schenectady',42.8142,-73.9396,1],['Troy',42.7284,-73.6918,1],['Saratoga Springs',43.0831,-73.7846,1],['Glens Falls',43.3095,-73.6440,1],['Lake George',43.4262,-73.7123,0],['Amsterdam',42.9387,-74.1882,0],['Hudson',42.2529,-73.7910,1],['Catskill',42.2173,-73.8646,0],['Kingston',41.9270,-73.9974,1],['Cohoes',42.7743,-73.7001,0],['Ballston Spa',43.0009,-73.8490,0],['Coxsackie',42.3509,-73.8029,0],['Woodstock',42.0409,-74.1182,0],['Hunter',42.2137,-74.2193,0],['Northville',43.2259,-74.1721,0],['Ticonderoga',43.8487,-73.4235,0],['Schoharie',42.6659,-74.3096,0],['Liberty',41.8012,-74.7466,0],['Newcomb',43.9695,-74.1632,0],['Wells',43.4012,-74.2896,0],['Gilboa',42.3973,-74.4460,0],['Phoenicia',42.0834,-74.3113,0],['Saugerties',42.0776,-73.9529,0],['Voorheesville',42.6539,-73.9287,0],['Coeymans',42.4740,-73.7923,0],['Waterford',42.7926,-73.6812,0]]
out={'rivers':lines(riv),'lakes':lines(lak),'counties':lines(cty),'roads':[{'t':(0 if p['type']=='Secondary Highway' else 1),'c':c} for g,p in rd for c in lines([(g,p)])],'towns':towns}
s=json.dumps(out,separators=(',',':'))
open('build/base.json','w').write(s); print(len(s))
