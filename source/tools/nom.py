# look a named feature up in OpenStreetMap (Nominatim), one request a second:  python3 tools/nom.py "name, town, state" ...
# Give several names in ONE command: the pause between them is kept here. Run one command a name, back to back, and the
# service answers HTTP 429 after about ten. When a name finds nothing, find the thing by what it is and where:
#   python3 tools/osmnear.py <lat> <lon> 800 buildings tourism -g 'ruins|bunker|museum|historic'
import sys,re,json,time,urllib.parse,urllib.request,urllib.error
UA={'User-Agent':'lost-hidden-atlas-research/1.0 (personal research tool)'}
def ask(q):
    u='https://nominatim.openstreetmap.org/search?'+urllib.parse.urlencode({'q':q,'format':'jsonv2','limit':3,'countrycodes':'us,ca'})
    return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))
# The service refuses a caller who asks faster than about once a second, with HTTP 429 or, as a dozen sessions met in November 2026,
# HTTP 629. The pause is kept across commands too (a file holds the time of the last question), and a refusal is waited out and
# asked again, up to three times, before the tool gives up on a name.
import os
LAST=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','cache','nom_last')
def pace():
    try: w=1.3-(time.time()-float(open(LAST).read()))
    except Exception: w=0
    if w>0: time.sleep(min(w,1.3))
    try: os.makedirs(os.path.dirname(LAST),exist_ok=True); open(LAST,'w').write(str(time.time()))
    except Exception: pass
def patient(q,sleep=time.sleep):
    for k,wait in enumerate((5,15,30,0)):
        pace()
        try: return ask(q)
        except urllib.error.HTTPError as e:
            if e.code not in (429,629,503) or not wait: raise
            sleep(wait)
if __name__=='__main__':
  for q in sys.argv[1:]:
    try:
        j=patient(q)
        print(q,'->',' | '.join(f"{round(float(x['lat']),5)},{round(float(x['lon']),5)} [{x.get('category')}/{x.get('type')}] {x['display_name'][:70]}" for x in j) or 'nothing')
    except Exception as e: print(q,'-> ERROR',str(e)[:80]+('. The name search is refusing requests for now: use tools/osmnear.py by tag or tools/geo.py by address, or wait a few minutes.' if re.search('429|629',str(e)) else ''))
