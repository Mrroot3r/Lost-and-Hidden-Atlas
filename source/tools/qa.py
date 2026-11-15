import json,urllib.request,urllib.parse,time
S=json.load(open('build/sites.json'))
UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
bad=[]
for s in S:
    u='https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode?'+urllib.parse.urlencode({'location':f"{s['lon']},{s['lat']}",'f':'json','featureTypes':'StreetAddress,StreetInt,POI,Locality'})
    try:
        j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30)); a=j.get('address',{})
    except Exception as e:
        a={'Match_addr':'ERR'}
    city=(a.get('City') or '')+'|'+(a.get('Neighborhood') or '')+'|'+(a.get('Subregion') or '')
    town=s['town'].split('/')[0].strip()
    ok=any(t.lower() in (city+' '+a.get('Match_addr','')).lower() for t in [town]+town.split())
    if not ok: bad.append((s['id'],s['town'],a.get('Match_addr','')[:60],city))
    time.sleep(0.05)
for b in bad: print(b)
print(len(bad),'to review of',len(S))
