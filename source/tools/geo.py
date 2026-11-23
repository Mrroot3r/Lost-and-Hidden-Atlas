#!/usr/bin/env python3
"""The ArcGIS world geocoder, for a street address or a named place anywhere the Atlas covers.
   python3 tools/geo.py "641 Sudderth Drive, Ruidoso, NM" ["another address, town, ST" ...]
       prints lat, lon, the kind of match (PointAddress lands on the building; StreetAddress is interpolated along the
       street; POI is a named place) and the score. A two-letter state or province at the end of the address keeps the
       search inside that state's box, so "Pine Street, Manchester, CT" is not taken for Manchester, England.
   python3 tools/geo.py queries.json results.json      the older batch form: {"id": "address", ...}, New York's box
Give a house number and a ZIP where you have them; nom.py (OpenStreetMap) is the other route, and often has the
building's own mapped name."""
import json,urllib.request,urllib.parse,time,sys,os,re
UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
NYBOX='-75.2,41.6,-73.2,44.3'
def box(q):
    m=re.search(r',\s*([A-Za-z]{2})\b(?:\s+\d{5})?\s*$',q)
    if not m: return None
    try: rs=json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'build','states.json')))[m.group(1).lower()]
    except Exception: return None
    xs=[r[i] for r in rs for i in range(0,len(r),2)]; ys=[r[i] for r in rs for i in range(1,len(r),2)]
    return '%.3f,%.3f,%.3f,%.3f'%(min(xs)-0.05,min(ys)-0.05,max(xs)+0.05,max(ys)+0.05)
def arc(q,ext=NYBOX,n=1):
    p={'SingleLine':q,'f':'json','maxLocations':n,'outFields':'Addr_type,Match_addr'}
    if ext: p['searchExtent']=ext
    j=json.load(urllib.request.urlopen(urllib.request.Request('https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates?'+urllib.parse.urlencode(p),headers=UA),timeout=30))
    c=j.get('candidates') or []
    if not c: return None
    if n>1: return [(round(x['location']['y'],5),round(x['location']['x'],5),x['attributes'].get('Addr_type'),x['score'],x['address']) for x in c]
    c=c[0]; return (round(c['location']['y'],5),round(c['location']['x'],5),c['attributes'].get('Addr_type'),c['score'],c['address'])
if __name__=='__main__':
    a=sys.argv[1:]
    if not a: sys.exit(__doc__)
    if a[0].endswith('.json'):
        qs=json.load(open(a[0]))
        res=json.load(open(a[1])) if len(a)>1 and os.path.exists(a[1]) else {}
        for k,q in qs.items():
            if k in res: continue
            try: res[k]=arc(q)
            except Exception as e: res[k]=['ERR',str(e)]
            print(k,'|',q,'->',res[k]); time.sleep(0.15)
        if len(a)>1: json.dump(res,open(a[1],'w'),indent=0)          # without a second argument the answers are only printed (it used to crash here)
        sys.exit(0)
    for q in a:
        b=box(q)
        try: r=arc(q,b,3)
        except Exception as e: print(q,'-> failed:',str(e)[:80]); continue
        print(q+('' if b else '   (no state at the end: searched the whole world)'))
        for x in r or []: print('   %.5f, %.5f  %-14s score %s  %s'%x)
        if not r: print('   nothing found')
        time.sleep(0.2)
