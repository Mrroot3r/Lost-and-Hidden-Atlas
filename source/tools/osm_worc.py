import urllib.request,urllib.parse,json,time
UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
EP=['https://overpass-api.de/api/interpreter','https://overpass.private.coffee/api/interpreter','https://maps.mail.ru/osm/tools/overpass/api/interpreter','https://overpass.kumi.systems/api/interpreter']
out=[]; ok=0
BOX=['42.0,-72.35,42.45,-71.45','42.45,-72.35,42.75,-71.45','41.2,-72.65,42.95,-72.35','41.2,-71.45,42.95,-70.8','41.2,-70.8,42.95,-69.85','41.2,-72.35,42.0,-71.45']
for i,b in enumerate(BOX):
    q=f'''[out:json][timeout:60];(nwr["historic"~"^(ruins|archaeological_site|mine|mine_shaft|adit|kiln|lime_kiln|charcoal_pile|industrial|railway_station|aqueduct|lock|fort|quarry)$"]({b});nwr["ruins"~"."]["ruins"!="no"]({b});nwr["abandoned"="yes"]["building"]({b});nwr["abandoned:building"]({b});nwr["man_made"~"^(kiln|adit|mineshaft)$"]({b});way["tunnel"="yes"]["railway"~"abandoned|disused|razed"]({b});nwr["abandoned:aerialway"]({b});nwr["abandoned:amenity"]({b});nwr["abandoned:leisure"]({b}););out tags center;'''
    for a in range(6):
        ep=EP[(a+i)%len(EP)]
        try:
            r=urllib.request.urlopen(urllib.request.Request(ep,data=urllib.parse.urlencode({'data':q}).encode(),headers=UA),timeout=90).read()
            els=json.loads(r)['elements']; out+=els; ok+=1; print('ok',i,len(els),ep[8:28],flush=True); break
        except Exception as e: print('fail',i,ep[8:28],str(e)[:40],flush=True); time.sleep(5)
    json.dump({'elements':out,'parts':ok},open('cache/osm/leads_ma.json','w'))
print('done',ok,len(out))
