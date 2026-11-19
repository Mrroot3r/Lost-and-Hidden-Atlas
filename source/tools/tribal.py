#!/usr/bin/env python3
"""Download the outlines of American Indian reservations and trust lands, for tools/leads.py.

   python3 tools/tribal.py          writes cache/tribal.json (about 500 outlines, under a megabyte; takes a minute)

Why: OpenStreetMap leads on reservation land are left out of the leads layer. Whether anyone may go there is the tribe's
to say, and most ruins mapped there are ancestral sites, which the Atlas does not list as leads (the rules are at the top
of tools/leads.py). The outlines are the Census Bureau's (TIGERweb, public domain): federal reservations, off-reservation
trust lands, state reservations and joint-use areas, simplified to about 200 metres. Alaska Native village areas,
Oklahoma tribal statistical areas and Hawaiian home lands are not included: they are statistical areas or homestead
land where most ground is ordinary private or public land. Canada's reserves are not included either."""
import json,os,urllib.request,urllib.parse
B='https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/AIANNHA/MapServer/'
LAYERS=(2,3,4,10)
def rings(g):
    if not g: return []
    polys=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
    return [[v for xy in poly[0] for v in (round(xy[0],4),round(xy[1],4))] for poly in polys if poly and len(poly[0])>=4]   # outer rings only
def main():
    out=[]
    for lay in LAYERS:
        off=0
        while True:
            p={'where':'1=1','outFields':'NAME','returnGeometry':'true','outSR':4326,'maxAllowableOffset':0.002,'geometryPrecision':4,
               'resultOffset':off,'resultRecordCount':200,'f':'geojson'}
            j=json.loads(urllib.request.urlopen(urllib.request.Request(B+str(lay)+'/query?'+urllib.parse.urlencode(p),headers={'User-Agent':'lost-hidden-atlas-research/1.0'}),timeout=120).read())
            fs=j.get('features',[])
            for f in fs:
                for r in rings(f.get('geometry')):
                    out.append([min(r[0::2]),min(r[1::2]),max(r[0::2]),max(r[1::2]),r])
            off+=len(fs)
            if len(fs)<200: break
        print('layer',lay,off,'areas',flush=True)
    os.makedirs('cache',exist_ok=True)
    json.dump({'asof':__import__('datetime').date.today().isoformat(),'r':out},open('cache/tribal.json','w'),separators=(',',':'))
    print('wrote cache/tribal.json',len(out),'outlines',os.path.getsize('cache/tribal.json')//1024,'KB')
if __name__=='__main__': main()
