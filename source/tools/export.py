import json,csv,html,os
R=os.environ.get('ATLAS','/home/claude/atlas').rstrip('/')+'/'
S=json.load(open(R+'build/sites.json'))
# the kinds of place, their names and colours: read from the one list in the app (KML wants a colour as aabbggrr)
import re
_C=re.findall(r"(\w+):\['([^']+)','#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})'\]",re.search(r'const CAT=\{[^\n]*\};',open(R+'src/app.js',encoding='utf-8').read()).group(0))
CAT={k:n for k,n,r,g,b in _C}; COL={k:'ff'+b+g+r for k,n,r,g,b in _C}
ST={'ruins':'Ruins','traces':'Traces','standing':'Standing','marker':'Marker only','gone':'Nothing visible','water':'Under water'}
PREC={'exact':'Exact','site':'On site','area':'Approximate'}
ACC={'public':'Public land or street','view':'View from the public way','ask':'Ask permission first','permit':'Permit required','boat':'On the water'}
EFF={'drive':'Drive-up','walk':'Short walk','hike':'Hike','boat':'Boat or shore view'}
with open(R+'dist/lost-hidden-atlas-places.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['Name','Town','Years','Kind','What is left','Pin accuracy','Latitude','Longitude','Access','Effort','Parking latitude','Parking longitude','Minutes from Albany','Minutes from Schenectady','Minutes from Troy','Minutes from Saratoga Springs','Verified','Changing now','Old USGS map year','What was here','Look for','Access notes','Pin evidence','Google Maps','Sources'])
    TM=json.load(open(R+'build/topo/meta.json'))
    for s in S:
        th=s.get('th') or ['','']
        w.writerow([s['name'],s['town'],s.get('years',''),CAT[s['cat']],ST[s['st']],PREC[s['prec']],s['lat'],s['lon'],ACC[s['acc']],EFF[s['eff']],th[0],th[1],s['dt'].get('alb',[''])[0],s['dt'].get('sch',[''])[0],s['dt'].get('troy',[''])[0],s['dt'].get('sar',[''])[0],{'verified':'Verified','lead':'Lead','mixed':'Partly verified','reference':'Reference'}[s['conf']],'Yes' if s.get('now') else '',(TM.get(s['id']) or {}).get('y',''),s.get('story',''),s.get('look',''),s.get('accn',''),s.get('pn',''),f"https://www.google.com/maps/search/?api=1&query={s['lat']},{s['lon']}",' | '.join(l[1] for l in s.get('links',[]))])
e=html.escape
k=['<?xml version="1.0" encoding="UTF-8"?>','<kml xmlns="http://www.opengis.net/kml/2.2"><Document>','<name>Lost &amp; Hidden Atlas</name>','<description>Lost and hidden places across upstate New York, Massachusetts and Rhode Island. Built '+__import__('datetime').date.today().strftime('%B %-d, %Y')+'.</description>']
for c,col in COL.items():
    k.append(f'<Style id="c-{c}"><IconStyle><color>{col}</color><scale>1.0</scale><Icon><href>http://maps.google.com/mapfiles/kml/paddle/wht-blank.png</href></Icon></IconStyle><LabelStyle><scale>0.8</scale></LabelStyle></Style>')
for c,label in CAT.items():
    k.append(f'<Folder><name>{e(label)}</name>')
    for s in S:
        if s['cat']!=c: continue
        d=[f"<b>{e(s['town'])}</b>"+(f" · {e(s['years'])}" if s.get('years') else ''),f"{ST[s['st']]} · Pin: {PREC[s['prec']].lower()} · {ACC[s['acc']]} · {EFF[s['eff']]}",e(s.get('story',''))]
        if s.get('look'): d.append('<b>Look for:</b> '+e(s['look']))
        if s.get('accn'): d.append('<b>Access:</b> '+e(s['accn']))
        if s.get('pn'): d.append('<b>Pin:</b> '+e(s['pn']))
        if s.get('th'): d.append(f"<b>Park at:</b> {e(s.get('thn',''))} ({s['th'][0]}, {s['th'][1]})")
        if all(h in s['dt'] for h in ('alb','sch','troy','sar')): d.append(f"Drive: Albany {s['dt']['alb'][0]} min · Schenectady {s['dt']['sch'][0]} · Troy {s['dt']['troy'][0]} · Saratoga {s['dt']['sar'][0]}")
        for l in s.get('links',[])[:4]: d.append(f'<a href="{e(l[1])}">{e(l[0])}</a>')
        k.append(f"<Placemark><name>{e(s['name'])}</name><styleUrl>#c-{c}</styleUrl><description><![CDATA[{'<br><br>'.join(x for x in d if x)}]]></description><Point><coordinates>{s['lon']},{s['lat']},0</coordinates></Point></Placemark>")
    k.append('</Folder>')
k.append('</Document></kml>')
open(R+'dist/lost-hidden-atlas-places.kml','w',encoding='utf-8').write('\n'.join(k))
import xml.dom.minidom as x; x.parse(R+'dist/lost-hidden-atlas-places.kml'); print('kml ok')
