import json,re,base64,os,datetime,hashlib,shutil
R=os.environ.get('ATLAS','/home/claude/atlas').rstrip('/')+'/'
S=json.load(open(R+'build/sites.json')); HUBS=json.load(open(R+'build/hubs.json')); TM=json.load(open(R+'build/topo/meta.json'))
topo={}
for s in S:
    s.pop('snap',None)
    for k in ('name2','look','hook','accn','years'):
        if not s.get(k): s.pop(k,None)
    if not s.get('now'): s.pop('now',None)
    if not s.get('links'): s.pop('links',None)
    if not s.get('tags'): s.pop('tags',None)
    m=TM.get(s['id']); p=R+f"build/topo/{s['id']}.webp"
    if m and os.path.exists(p):
        raw=open(p,'rb').read()
        s['tm']={'y':m['y'],'q':m['q'],'sc':m['sc'],'b':m['b'],'v':hashlib.md5(raw).hexdigest()[:6]}
        topo[s['id']]=base64.b64encode(raw).decode()
md=open(R+'src/catalogue.md').read()
tk=[]
for line in md.split('## Research toolkit')[1].split('**Five tells')[0].split('\n'):
    m=re.match(r'\| (.+?) \| (.+?) \| \[(.+?)\]\((.+?)\) \|',line)
    if m and m.group(1)!='Resource': tk.append([m.group(1),m.group(2),m.group(4)])
tells=[re.sub(r'^- ','',l) for l in md.split('**Five tells of a lost building**')[1].split('## ')[0].strip().split('\n') if l.startswith('- ')]
rules=[re.sub(r'^- ','',l) for l in md.split('**Access and legal notes**')[1].split('## ')[0].strip().split('\n') if l.startswith('- ')]
series=[
 ['now','Watch it disappear: 2026','Now. The Central Warehouse demolition runs through this winter.'],
 ['trolleyparks','Trolley parks','Summer, to match the old postcards. Scout the woods in leaf-off months first. Now includes Whalom, Norumbega, Mountain Park and Lincoln Park in Massachusetts.'],
 ['cemeteries',"The cemeteries that moved (and the ones that didn't)",'Any time. Be respectful filming at active cemeteries.'],
 ['burned','Burned on purpose','Fall for escarpment views; spring for the Laurel House foundations.'],
 ['inclines','Inclines and funiculars','Leaf-off for the Otis grade; summer for the Prospect Mountain road.'],
 ['canal','The canal you can still touch','Spring before leaf-out. Low water helps at the aqueducts.'],
 ['monitor','The Monitor trail',"Pair a Troy day with an Adirondack day."],
 ['stations','Stations they tore down','Any time. Albany\'s surviving station is the contrast.'],
 ['drowned','Drowned valleys','Late summer to fall droughts. Check DEP permit rules first.'],
 ['hotels','Hotels that ate the mountains','Fall color; Overlook any season.'],
 ['stove','Stove capital, iron city','Winter. Good indoor archive pairing at the Albany Institute.'],
 ['amusements','Dead amusements','Knox Cave by permit only, mid-May to September 30.'],
 ['renewal','Bulldozed downtowns','Any time. Bring 1950s photographs for then-and-now shots.'],
 ['forts','Forts under the streets','Any time. Early Sunday morning for empty streets.'],
]
aerial=[
 ['Historic Aerials','Air photos lined up on a modern map, with a year picker. Coverage varies by county. Free to browse with a watermark. Every place page opens its own spot there.','https://www.historicaerials.com/viewer'],
 ['USGS EarthExplorer','Free downloads of single government air-photo frames from the 1940s on. Needs a free account; choose "Aerial Photo Single Frames" and search by coordinates.','https://earthexplorer.usgs.gov/'],
 ['Cornell: New York aerial photographs','About 50,000 contact prints from 1936 to 1995 across 48 counties. Browse by county and year.','https://digital.library.cornell.edu/collections/aerialny'],
 ['Skidmore: Saratoga County air photos','1948, 1960, 1968 and 1986 flights from the county Soil and Water collection, chosen from a map. Worth checking for Luna Park, Forest Park and Kaydeross.','https://www.skidmore.edu/gis/visual-landscape/index.php'],
 ['Andy Arthur: 1952 Albany and Schenectady','Ready-made 1952-versus-today overlays for downtown Albany, the Stockade, the West Albany yards, the Pine Bush and more.','https://andyarthur.org/'],
 ['USGS topoView','Every edition of every USGS sheet, free, with a timeline. The Atlas old-map overlays are cut from these.','https://ngmdb.usgs.gov/topoview/viewer/'],
]
V=os.environ.get('ATLAS_V') or datetime.datetime.now().strftime('%y%m%d%H%M')     # ATLAS_V: build under a given version, to see whether anything but the stamp changed
import sys; sys.path.insert(0,R+'tools')
from states import STATES
data={'v':V,'states':[{'k':s['k'],'name':s['name'],'legal':s['legal'],'regions':[list(r) for r in s['regions']]} for s in STATES],'outlines':json.load(open(R+'build/states.json')),'batches':json.load(open(R+'build/batches.json')),'built':(os.environ.get('ATLAS_BUILT') or datetime.date.today().strftime('%B %-d, %Y')),'sites':S,'hubs':HUBS,'series':[{'tag':a,'title':b,'note':c} for a,b,c in series],'aerial':aerial,'toolkit':tk,'tells':tells,'rules':rules,'alias':(json.load(open(R+'build/alias.json')) if os.path.exists(R+'build/alias.json') else {})}
# The old rail and canal lines, cut up for the hosted copy: one file for each state, a thinned picture of them all, and
# the index of both, which goes in the page data (tools/lines_split.py). The app uses the index only on the hosted copy.
import lines_split
LSTATE,LWIDE,data['lx']=lines_split.split(json.load(open(R+'build/lines.json',encoding='utf-8')))
def js(o): return json.dumps(o,separators=(',',':'),ensure_ascii=False).replace('</','<\\/').replace('<!--','\\u003c!--')      # text in a place can never end the script element or open a comment in it
css=open(R+'src/app.css').read()
lcss=open(R+'cache/leaflet.min.css').read()
lcss=re.sub(r'url\([^)]*\)','none',lcss)
body=open(R+'src/app.body.html').read()
app=open(R+'src/app.js').read()
fonts='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans+Condensed:wght@500;600;700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap">'
head='<title>Lost &amp; Hidden Atlas</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'+fonts+'\n<style>\n'+lcss+'\n'+css+'\n</style>\n'
scripts=('<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>\n'
 '<script type="application/json" id="d-sites">'+js(data)+'</script>\n'
 '<script type="application/json" id="d-base">'+open(R+'build/base.json').read().replace('</','<\\/')+'</script>\n'
 '<script type="application/json" id="d-lines">'+open(R+'build/lines.json').read().replace('</','<\\/')+'</script>\n'
 '<script type="application/json" id="d-topo">'+js(topo)+'</script>\n'
 '<script type="application/json" id="d-leads">'+open(R+'build/leads.json').read().replace('</','<\\/')+'</script>\n'
 '<script>\n'+app+'\n</script>\n')
os.makedirs(R+'dist',exist_ok=True)
open(R+'dist/atlas-artifact.html','w').write(head+body+scripts)
full_scripts=scripts.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>','<script>'+open(R+'cache/leaflet.min.js').read()+'</script>')
full=('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
 '<style>:root{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'+head+'</head>\n<body>\n'+body+full_scripts+'</body>\n</html>\n')
open(R+'dist/Lost-and-Hidden-Atlas.html','w').write(full)
print(len(S),'sites',len(topo),'topo',len(tk),'toolkit',len(tells),len(rules),'bytes',len(full))

# ---- hosted copy: a small page plus separate files that load when needed ----
WEB=R+'dist/web/'
for d in ('data','topo'):
    shutil.rmtree(WEB+d,ignore_errors=True); os.makedirs(WEB+d)
for i in topo: shutil.copyfile(R+f'build/topo/{i}.webp',WEB+f'topo/{i}.webp')
open(WEB+'data/lines.json','w').write(open(R+'build/lines.json').read())      # every line in one file: what the Android app reads, and what the next build starts from
os.makedirs(WEB+'data/lines')
for k,txt in LSTATE.items(): open(WEB+f'data/lines/{k}.json','w',encoding='utf-8').write(txt)
open(WEB+'data/lines/wide.json','w',encoding='utf-8').write(LWIDE)
open(WEB+'data/leads.json','w').write(open(R+'build/leads.json').read())
# The leads' second file: Native American sites and leads on reservation land, which the app fetches only for a reader who
# switches them on under the gear (tools/leads.py). Its name carries the stamp that data/leads.json gives in x.native.h.
_lx=(json.load(open(R+'build/leads.json',encoding='utf-8')).get('x') or {}).get('native')
if _lx:
    _nb=open(R+'build/leads_native.json','rb').read()
    if hashlib.md5(_nb).hexdigest()[:8]!=_lx['h'] or len(json.loads(_nb)['p'])!=_lx['n']: sys.exit('make.py: build/leads_native.json does not match what build/leads.json says of it: run  python3 tools/leads.py  (or setup.sh again)')
    os.makedirs(WEB+'data/leads'); open(WEB+'data/leads/native-%s.json'%_lx['h'],'wb').write(_nb)
if os.path.exists(R+'build/pockets.json'):       # historic pockets (tools/pockets.py); fetched only when the layer is turned on
    pj=json.load(open(R+'build/pockets.json',encoding='utf-8'))
    for part in ('m','r','d'): pj.setdefault(part,[])     # empty, for an Android app built before the detail moved to one file per state
    open(WEB+'data/pockets.json','w',encoding='utf-8').write(json.dumps(pj,separators=(',',':'),ensure_ascii=False))
    os.makedirs(WEB+'data/pock')
    for k in pj.get('s',{}): shutil.copyfile(R+f'build/pock/{k}.json',WEB+f'data/pock/{k}.json')   # one state's markers and listings, fetched when the map is zoomed in there
if os.path.exists(R+'build/walls.json'):         # stone walls found on LiDAR (tools/walls.py); the index when the layer is switched on, a cell when zoomed in there
    shutil.copyfile(R+'build/walls.json',WEB+'data/walls.json'); shutil.copytree(R+'build/walls',WEB+'data/walls')
if os.path.exists(R+'src/photos.json'):          # photo details gathered ahead of time (tools/photos.py): only for places that still exist
    _ph=json.load(open(R+'src/photos.json',encoding='utf-8')); _ids={s['id'] for s in S}
    open(WEB+'data/photos.json','w',encoding='utf-8').write(json.dumps({'asof':_ph.get('asof',''),'p':{k:v for k,v in _ph['p'].items() if k in _ids}},separators=(',',':'),ensure_ascii=False))
# The optional lead layers (tools/vanished.py, tools/mines.py), fetched only when switched on. Each goes out in pieces:
# data/<layer>/index.json (the kinds of point, and for each state its count, a stamp and its box) and one file per state,
# data/<layer>/<state>-<stamp>.json, which the app fetches when the map is zoomed in there or the reader stands there.
# data/<layer>.json, the whole layer in one file, is still written for copies of the Android app built before November 20, 2026,
# which read nothing else; it holds only the eleven states it held then, so it grows no further. Drop it when those are gone.
XL_OLD=('ny','ma','vt','ct','nh','nj','pa','ri','me','mo','ks')
for extra in ('vanished','mines'):
    if not os.path.exists(R+f'build/{extra}.json'): continue
    _d=json.load(open(R+f'build/{extra}.json',encoding='utf-8')); _by={}
    for _r in _d['p']: _by.setdefault(_r[-1],[]).append(_r)
    os.makedirs(WEB+f'data/{extra}'); _s={}
    for _k in sorted(_by):
        _txt=json.dumps({'p':_by[_k]},separators=(',',':'),ensure_ascii=False); _h=hashlib.md5(_txt.encode('utf-8')).hexdigest()[:8]
        open(WEB+f'data/{extra}/{_k}-{_h}.json','w',encoding='utf-8').write(_txt)
        _la=[r[0] for r in _by[_k]]; _lo=[r[1] for r in _by[_k]]
        if min(_lo)<0<max(_lo): _lo=[x for x in _lo if x<0]      # Alaska's last islands lie past 180 degrees: left out of the box, or it would wrap the world
        _s[_k]={'n':len(_by[_k]),'h':_h,'b':[round(min(_la)-0.005,2),round(min(_lo)-0.005,2),round(max(_la)+0.005,2),round(max(_lo)+0.005,2)]}
    open(WEB+f'data/{extra}/index.json','w',encoding='utf-8').write(json.dumps({'v':2,'t':_d['t'],'s':_s},separators=(',',':'),ensure_ascii=False))
    _old=[r for r in _d['p'] if r[-1] in XL_OLD]
    open(WEB+f'data/{extra}.json','w',encoding='utf-8').write(json.dumps({'v':_d.get('v',1),'t':_d['t'],'p':_old,'s':{k:v for k,v in _d['s'].items() if k in XL_OLD}},separators=(',',':'),ensure_ascii=False))
open(WEB+'app.js','w').write(app)
open(WEB+'leaflet.js','w').write(open(R+'cache/leaflet.min.js').read())
web_scripts=('<script src="leaflet.js?v=1.9.4"></script>\n'
 '<script type="application/json" id="d-sites">'+js(data)+'</script>\n'
 '<script type="application/json" id="d-base">'+open(R+'build/base.json').read().replace('</','<\\/')+'</script>\n'
 '<script src="app.js?v='+V+'"></script>\n')
web=('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<meta name="theme-color" content="#a33a24">\n'
 '<style>:root{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'+head+'</head>\n<body>\n'+body+web_scripts+'</body>\n</html>\n')
open(WEB+'index.html','w').write(web)
open(WEB+'.nojekyll','w').write('')
# for the Android app: its start-up script, and a small file it reads to see whether the places have changed
open(WEB+'boot.js','w').write(open(R+'src/boot.js').read())
open(WEB+'version.json','w').write(json.dumps({'v':V,'places':len(S),'built':data['built']}))
open(WEB+'sw.js','w').write(open(R+'src/sw.js').read().replace('__V__',V))
tot=sum(os.path.getsize(os.path.join(dp,f)) for dp,_,fs in os.walk(WEB) for f in fs)
print('hosted copy: index',len(web)//1024,'KB, app',len(app)//1024,'KB, lines',os.path.getsize(WEB+'data/lines.json')//1024,'KB in',len(LSTATE),'state files,',len(topo),'old maps; total',tot//1024,'KB; version',V)
