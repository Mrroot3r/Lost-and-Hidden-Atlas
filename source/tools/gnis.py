import json,urllib.request,urllib.parse,sys,time
UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
B='https://carto.nationalmap.gov/arcgis/rest/services/geonames/MapServer'
def layers():
    j=json.load(urllib.request.urlopen(urllib.request.Request(B+'?f=json',headers=UA),timeout=30))
    return [(l['id'],l['name']) for l in j['layers'] if not l.get('subLayerIds')]
def q(name,lyrs):
    out=[]
    for lid,ln in lyrs:
        w=f"upper(gaz_name) LIKE '{name.upper().replace(chr(39),chr(39)*2)}%' AND state_alpha='NY'"
        u=f"{B}/{lid}/query?"+urllib.parse.urlencode({'where':w,'outFields':'*','returnGeometry':'true','outSR':4326,'f':'json'})
        try:
            j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))
        except Exception as e:
            continue
        for f in j.get('features',[]):
            a=f['attributes']; g=f.get('geometry') or {}; p=(g.get('points') or [[g.get('x',0),g.get('y',0)]])[0]
            out.append((a.get('gaz_name'),a.get('gaz_featureclass'),a.get('county_name'),round(p[1],5),round(p[0],5),ln))
    return out
if __name__=='__main__':
    L=layers()
    if sys.argv[1]=='layers': print(L); sys.exit()
    for n in sys.argv[1:]:
        r=q(n,L); print(n,'->'); [print('   ',x) for x in r[:8]]
