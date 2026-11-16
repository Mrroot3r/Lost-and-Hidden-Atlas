# look a named feature up in OpenStreetMap (Nominatim), one request a second:  python3 tools/nom.py "name, town, state" ...
import sys,json,time,urllib.parse,urllib.request
UA={'User-Agent':'lost-hidden-atlas-research/1.0 (personal research tool)'}
for q in sys.argv[1:]:
    u='https://nominatim.openstreetmap.org/search?'+urllib.parse.urlencode({'q':q,'format':'jsonv2','limit':3,'countrycodes':'us,ca'})
    try:
        j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))
        print(q,'->',' | '.join(f"{round(float(x['lat']),5)},{round(float(x['lon']),5)} [{x.get('category')}/{x.get('type')}] {x['display_name'][:70]}" for x in j) or 'nothing')
    except Exception as e: print(q,'-> ERROR',str(e)[:80])
    time.sleep(1.1)
