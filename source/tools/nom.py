# look a named feature up in OpenStreetMap (Nominatim), one request a second:  python3 tools/nom.py "name, town, state" ...
# Give several names in ONE command: the pause between them is kept here. Run one command a name, back to back, and the
# service answers HTTP 429 after about ten. When a name finds nothing, find the thing by what it is and where:
#   python3 tools/osmnear.py <lat> <lon> 800 buildings tourism -g 'ruins|bunker|museum|historic'
import sys,json,time,urllib.parse,urllib.request,urllib.error
UA={'User-Agent':'lost-hidden-atlas-research/1.0 (personal research tool)'}
def ask(q):
    u='https://nominatim.openstreetmap.org/search?'+urllib.parse.urlencode({'q':q,'format':'jsonv2','limit':3,'countrycodes':'us,ca'})
    return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))
for q in sys.argv[1:]:
    try:
        try: j=ask(q)
        except urllib.error.HTTPError as e:
            if e.code!=429: raise
            time.sleep(20); j=ask(q)                      # asked too fast (often by an earlier command): wait once and ask again
        print(q,'->',' | '.join(f"{round(float(x['lat']),5)},{round(float(x['lon']),5)} [{x.get('category')}/{x.get('type')}] {x['display_name'][:70]}" for x in j) or 'nothing')
    except Exception as e: print(q,'-> ERROR',str(e)[:80]+('. The name search is refusing requests for now: use tools/osmnear.py by tag, or wait a few minutes.' if '429' in str(e) else ''))
    time.sleep(1.1)
