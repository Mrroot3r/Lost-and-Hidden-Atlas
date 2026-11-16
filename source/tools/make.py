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
V=datetime.datetime.now().strftime('%y%m%d%H%M')
data={'v':V,'batches':json.load(open(R+'build/batches.json')),'built':datetime.date.today().strftime('%B %-d, %Y'),'sites':S,'hubs':HUBS,'series':[{'tag':a,'title':b,'note':c} for a,b,c in series],'aerial':aerial,'toolkit':tk,'tells':tells,'rules':rules}
def js(o): return json.dumps(o,separators=(',',':'),ensure_ascii=False).replace('</','<\\/')
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
open(WEB+'data/lines.json','w').write(open(R+'build/lines.json').read())
open(WEB+'data/leads.json','w').write(open(R+'build/leads.json').read())
open(WEB+'app.js','w').write(app)
open(WEB+'leaflet.js','w').write(open(R+'cache/leaflet.min.js').read())
web_scripts=('<script src="leaflet.js?v=1.9.4"></script>\n'
 '<script type="application/json" id="d-sites">'+js(data)+'</script>\n'
 '<script type="application/json" id="d-base">'+open(R+'build/base.json').read().replace('</','<\\/')+'</script>\n'
 '<script src="app.js?v='+V+'"></script>\n')
web=('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<meta name="theme-color" content="#a3238e">\n'
 '<style>:root{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'+head+'</head>\n<body>\n'+body+web_scripts+'</body>\n</html>\n')
open(WEB+'index.html','w').write(web)
open(WEB+'.nojekyll','w').write('')
open(WEB+'sw.js','w').write(open(R+'src/sw.js').read().replace('__V__',V))
tot=sum(os.path.getsize(os.path.join(dp,f)) for dp,_,fs in os.walk(WEB) for f in fs)
print('hosted copy: index',len(web)//1024,'KB, app',len(app)//1024,'KB, lines',os.path.getsize(WEB+'data/lines.json')//1024,'KB,',len(topo),'old maps; total',tot//1024,'KB; version',V)
