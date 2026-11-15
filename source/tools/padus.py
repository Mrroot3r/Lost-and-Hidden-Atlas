import json,requests,time,os
S=json.load(open('build/sites.json'))
P='build/padus.json'; C=json.load(open(P)) if os.path.exists(P) else {}
U='https://services.arcgis.com/v01gqwM5QqNysAAi/arcgis/rest/services/PADUS_Public_Access/FeatureServer/0/query'
RANK={'OA':0,'RA':1,'UK':2,'XA':3}
for s in S:
    key=f"{s['lat']:.5f},{s['lon']:.5f}"
    if key in C: continue
    for a in range(3):
        try:
            j=requests.get(U,params={'geometry':f"{s['lon']},{s['lat']}",'geometryType':'esriGeometryPoint','inSR':4326,'spatialRel':'esriSpatialRelIntersects','outFields':'Unit_Nm,MngNm_Desc,Pub_Access,DesTp_Desc,GIS_Acres','returnGeometry':'false','f':'json'},timeout=40).json()
            fs=[f['attributes'] for f in j.get('features',[])]
            fs.sort(key=lambda a:(RANK.get(a['Pub_Access'],9),a.get('GIS_Acres') or 0))
            C[key]=[fs[0]['Unit_Nm'],fs[0]['MngNm_Desc'],fs[0]['Pub_Access']] if fs else None
            break
        except Exception as e:
            time.sleep(2)
    else: print('fail',s['id'])
    if len(C)%40==0: json.dump(C,open(P,'w'))
json.dump(C,open(P,'w'))
n=0
for s in S:
    v=C.get(f"{s['lat']:.5f},{s['lon']:.5f}")
    if v: s['pl']=v; n+=1
    else: s.pop('pl',None)
json.dump(S,open('build/sites.json','w'),indent=1,ensure_ascii=False)
print(n,'of',len(S),'on mapped protected land')
