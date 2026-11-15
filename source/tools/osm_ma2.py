import urllib.request,urllib.parse,json,time
UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
EP=['https://overpass.private.coffee/api/interpreter','https://overpass-api.de/api/interpreter','https://maps.mail.ru/osm/tools/overpass/api/interpreter','https://overpass.kumi.systems/api/interpreter']
out=[]; ok=0
for i,b in enumerate(['41.2,-72.65,42.95,-72.0','41.2,-72.0,42.95,-71.4','41.2,-71.4,42.95,-70.8','41.2,-70.8,42.95,-69.85']):
    q=f'''[out:json][timeout:90];(nwr["historic"~"^(ruins|archaeological_site|mine|mine_shaft|adit|kiln|lime_kiln|charcoal_pile|industrial|railway_station|aqueduct|lock|fort|quarry)$"]({b});nwr["ruins"~"."]["ruins"!="no"]({b});nwr["abandoned"="yes"]["building"]({b});nwr["man_made"~"^(kiln|adit|mineshaft)$"]({b});way["tunnel"="yes"]["railway"~"abandoned|disused|razed"]({b});nwr["abandoned:aerialway"]({b}););out tags center;'''
    for a in range(8):
        ep=EP[(a+i)%len(EP)]
        try:
            r=urllib.request.urlopen(urllib.request.Request(ep,data=urllib.parse.urlencode({'data':q}).encode(),headers=UA),timeout=120).read()
            els=json.loads(r)['elements']; out+=els; ok+=1; print('ok',i,len(els),ep,flush=True); break
        except Exception as e: print('fail',i,ep[8:30],str(e)[:50],flush=True); time.sleep(6)
    json.dump({'elements':out,'parts':ok},open('cache/osm/leads_ma.json','w'))
print('done',ok,len(out))
