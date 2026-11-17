import json,urllib.request,urllib.parse,os,re,io,sys,time,base64
sys.path.insert(0,'tools')
from topocrop import crop
UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
S=json.load(open('build/sites.json'))
os.makedirs('cache/tnm',exist_ok=True); os.makedirs('cache/topo',exist_ok=True); os.makedirs('build/topo',exist_ok=True)
OVR=json.load(open('src/topo_override.json')) if os.path.exists('src/topo_override.json') else {}
def tnm(lat,lon):
    key=f"{lat:.3f}_{lon:.3f}"; p=f'cache/tnm/{key}.json'
    if os.path.exists(p): return json.load(open(p))
    d=0.0005
    u='https://tnmaccess.nationalmap.gov/api/v1/products?'+urllib.parse.urlencode({'datasets':'Historical Topographic Maps','bbox':f'{lon-d},{lat-d},{lon+d},{lat+d}','prodFormats':'GeoTIFF','max':100})
    for a in range(4):
        try:
            j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60)); break
        except Exception as e:
            time.sleep(3); j=None
    if j is None: return []
    items=[]
    for it in j.get('items',[]):
        m=re.search(r'_(\d{4})_(\d+)_geo\.tif$',it['downloadURL'])
        if not m: continue
        items.append({'url':it['downloadURL'],'year':int(m.group(1)),'scale':int(m.group(2)),'title':it['title']})
    json.dump(items,open(p,'w')); time.sleep(0.3); return items
def pick(items,site):
    c=[i for i in items if i['scale']<=63360]
    if not c: return None
    o=OVR.get(site['id'])
    if o:
        cc=[i for i in c if i['year']==o]
        if cc: return cc[0]
    if 'drowned' in site['tags'] or site['st']=='water':
        return sorted(c,key=lambda i:(i['year'],i['scale']))[0]
    pre=[i for i in c if i['year']<=1936]
    if pre: return sorted(pre,key=lambda i:(-i['year'],i['scale']))[0]
    return sorted(c,key=lambda i:(i['year'],i['scale']))[0]
def fetch(url):
    p='cache/topo/'+url.split('/')[-1]
    if not os.path.exists(p):
        for a in range(3):
            try:
                urllib.request.urlretrieve(url,p+'.part'); os.rename(p+'.part',p); break
            except Exception as e: time.sleep(3)
    return p if os.path.exists(p) else None
meta={}
# "--missing": every place that has no crop yet and is not known to have no old map (build/topo/none.json). The site
# build on GitHub runs it this way, so a session need not cut or commit crops for the places it adds.
NF='build/topo/none.json'; NONE=json.load(open(NF)) if os.path.exists(NF) else {}
if sys.argv[1:2]==['--missing']:
    _old=json.load(open('build/topo/meta.json')) if os.path.exists('build/topo/meta.json') else {}
    only={s['id'] for s in S if s['cat']!='landmark' and s['id'] not in _old and NONE.get(s['id'])!='%.5f,%.5f'%(s['lat'],s['lon'])}
    print(len(only),'places need an old-map crop')
    if not only: sys.exit(0)
else: only=set(sys.argv[1:])
def none(s,why): NONE[s['id']]='%.5f,%.5f'%(s['lat'],s['lon']); print(why,s['id'])
old=json.load(open('build/topo/meta.json')) if os.path.exists('build/topo/meta.json') else {}
for s in S:
    if s['cat']=='landmark': continue
    if only and s['id'] not in only:
        if s['id'] in old: meta[s['id']]=old[s['id']]
        continue
    it=pick(tnm(s['lat'],s['lon']),s)
    if not it:
        if os.path.exists(f"cache/tnm/{s['lat']:.3f}_{s['lon']:.3f}.json"): none(s,'no map')      # the map list answered and had nothing; a failed request is not remembered
        else: print('map list did not answer',s['id'])
        continue
    tif=fetch(it['url'])
    if not tif: print('dl fail',s['id']); continue
    hw=1200 if s['prec']=='area' else 800
    try:
        im,bb=crop(tif,s['lat'],s['lon'],hw,512)
    except Exception as e:
        print('crop fail',s['id'],e); continue
    import numpy as np
    a=np.asarray(im)
    if (a.max(axis=2)<8).mean()>0.5: none(s,'mostly empty'); continue
    im.save(f"build/topo/{s['id']}.webp",quality=52,method=6)
    quad=re.sub(r'^USGS 1:\d+-scale Quadrangle for ','',it['title'])
    meta[s['id']]={'b':[round(v,6) for v in bb],'y':it['year'],'q':quad,'sc':it['scale']}
    print(s['id'],it['year'],quad,os.path.getsize(f"build/topo/{s['id']}.webp"))
json.dump(meta,open('build/topo/meta.json','w'))
json.dump(dict(sorted(NONE.items())),open(NF,'w'))
print('done',len(meta))
