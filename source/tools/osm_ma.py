import urllib.request,urllib.parse,json,time,sys,os
UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
EP=['https://maps.mail.ru/osm/tools/overpass/api/interpreter','https://overpass.private.coffee/api/interpreter','https://overpass-api.de/api/interpreter','https://overpass.kumi.systems/api/interpreter','https://maps.mail.ru/osm/tools/overpass/api/interpreter','https://overpass-api.de/api/interpreter']
def run(q,t=200):
    for ep in EP:
        try:
            r=urllib.request.urlopen(urllib.request.Request(ep,data=urllib.parse.urlencode({'data':q}).encode(),headers=UA),timeout=t).read()
            j=json.loads(r); return j['elements'],ep
        except Exception as e: print('fail',ep,str(e)[:70],flush=True); time.sleep(5)
    return None,None
BB='41.2,-72.65,42.95,-69.85'
Q={}
for _i,_b in enumerate(['41.2,-72.65,42.95,-72.0','41.2,-72.0,42.95,-71.4','41.2,-71.4,42.95,-70.8','41.2,-70.8,42.95,-69.85']):
  Q[f'rail_old_ma{_i}']=f'''[out:json][timeout:170];(way["railway"~"^(abandoned|disused|razed|dismantled)$"]({_b});way["abandoned:railway"]({_b});way["disused:railway"]({_b});way["razed:railway"]({_b}););out tags geom;'''
Q.update({
'rail_old_maX':f'''[out:json][timeout:280];(
way["railway"~"^(abandoned|disused|razed|dismantled)$"]({BB});
way["abandoned:railway"]({BB});way["disused:railway"]({BB});way["razed:railway"]({BB});way["historic:railway"]({BB});way["railway:historic"]({BB});
);out tags geom;''',
'canal_ma':f'''[out:json][timeout:200];(
way["waterway"="canal"]({BB});way["historic"="canal"]({BB});way["disused:waterway"="canal"]({BB});way["abandoned:waterway"="canal"]({BB});way["waterway"~"dismantled|derelict_canal"]({BB});
);out tags geom;''',
'leads_ma':open('tools/osm_leads.py').read().split("q=f'''")[1].split("'''")[0].replace('{BB}',BB)
})
Q={k:v for k,v in Q.items() if k in('leads_ma','canal_ma')}
for k,q in Q.items():
    p=f'cache/osm/{k}.json'
    if os.path.exists(p): print('have',k); continue
    els,ep=run(q)
    if els is None: print('FAILED',k,flush=True); continue
    json.dump({'elements':els},open(p,'w')); print(k,len(els),ep,flush=True)
