import urllib.request,urllib.parse,json,time,sys
UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
EP=['https://maps.mail.ru/osm/tools/overpass/api/interpreter','https://overpass.private.coffee/api/interpreter','https://overpass-api.de/api/interpreter','https://overpass.kumi.systems/api/interpreter','https://maps.mail.ru/osm/tools/overpass/api/interpreter']
def run(q,t=200):
    for ep in EP:
        try:
            r=urllib.request.urlopen(urllib.request.Request(ep,data=urllib.parse.urlencode({'data':q}).encode(),headers=UA),timeout=t).read()
            j=json.loads(r); return j['elements'],ep
        except Exception as e: print('fail',ep,str(e)[:70],flush=True); time.sleep(4)
    return None,None
BB='41.45,-75.35,44.15,-72.55'
q=f'''[out:json][timeout:180];(
nwr["historic"~"^(ruins|archaeological_site|mine|mine_shaft|adit|kiln|lime_kiln|charcoal_pile|industrial|farm|railway_station|railway|aqueduct|lock|canal|fort|battlefield|ghost_town|locomotive|quarry)$"]({BB});
nwr["ruins"~"."]["ruins"!="no"]({BB});
nwr["abandoned"="yes"]["building"]({BB});nwr["abandoned:building"]({BB});nwr["ruins:building"]({BB});
nwr["abandoned:place"]({BB});nwr["place"]["abandoned"="yes"]({BB});
nwr["man_made"~"^(kiln|adit|mineshaft)$"]({BB});nwr["man_made"="chimney"]["disused"="yes"]({BB});
nwr["disused:railway"~"station|halt"]({BB});nwr["abandoned:railway"~"station|halt"]({BB});nwr["railway"="station"]["disused"="yes"]({BB});
nwr["abandoned:aerialway"]({BB});nwr["abandoned:leisure"]({BB});nwr["abandoned:amenity"]({BB});nwr["abandoned:tourism"]({BB});nwr["abandoned:man_made"]({BB});nwr["abandoned:landuse"~"quarry|industrial|winter_sports"]({BB});
nwr["landuse"="quarry"]["disused"="yes"]({BB});nwr["disused:landuse"="quarry"]({BB});
nwr["tunnel"="yes"]["railway"~"abandoned|disused|razed"]({BB});nwr["bridge"="yes"]["railway"~"abandoned|disused"]({BB});
);out tags center;'''
els,ep=run(q)
if els is not None:
    json.dump({'elements':els},open('cache/osm/leads.json','w')); print('leads',len(els),ep)
