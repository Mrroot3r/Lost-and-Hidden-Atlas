#!/usr/bin/env python3
"""Build the old-mines-and-quarries layer from the U.S. Geological Survey's Mineral Resources Data System (MRDS).

   python3 tools/mines.py             reads cache/mrds/mrds-csv.zip; writes build/mines.json (make.py copies it to data/)

Get the file once (26 MB, the whole country):
   curl -o cache/mrds/mrds-csv.zip https://mrdata.usgs.gov/mrds/mrds-csv.zip
It is a work of the U.S. government and in the public domain. The USGS stopped updating MRDS in 2011.

What is kept: sites recorded as a past producer or a prospect, in the states in STATES. Left out: working operations
("Producer"), bare mineral occurrences with no workings, wells, and sand and gravel pits (a third of the file, and
nothing to see). Positions in MRDS are often only good to a few hundred metres, and many old workings are flooded,
fenced or on private land. Every point is an unchecked lead.

Rows: [lat, lon, type, name, MRDS deposit id, commodity, 'P' past producer | 'S' prospect, last year worked or 0, state].
The record for a point is at https://mrdata.usgs.gov/mrds/show-mrds.php?dep_id=<id>."""
import zipfile,csv,io,json,os,re,sys
from collections import Counter
STATES={'New York':'ny','Massachusetts':'ma','Vermont':'vt','Connecticut':'ct','New Hampshire':'nh','New Jersey':'nj','Pennsylvania':'pa','Rhode Island':'ri','Maine':'me','Missouri':'mo','Kansas':'ks'}
TYPES=['Old iron mine','Old quarry','Old clay pit','Old mine or prospect']
QUARRY=re.compile(r'stone|limestone|granite|marble|slate|sandstone|dolomite|dimension|trap|quartzite|cement|lime\b|gypsum',re.I)
SRC='cache/mrds/mrds-csv.zip'
if not os.path.exists(SRC):
    print('no '+SRC+' here; keeping the existing build/mines.json'); sys.exit(0)
z=zipfile.ZipFile(SRC); out={'v':1,'t':TYPES,'p':[],'s':{}}; n=Counter()
for r in csv.DictReader(io.TextIOWrapper(z.open('mrds.csv'),encoding='latin-1')):
    k=STATES.get(r['state'])
    if not k or r['dev_stat'] not in ('Past Producer','Prospect') or r['oper_type']=='Well': continue
    c=r['commod1'].strip(); first=c.split(',')[0].strip()
    if not c or re.match(r'sand and gravel|peat|water|geothermal|natural gas|petroleum',c,re.I): continue
    try: la,lo=float(r['latitude']),float(r['longitude'])
    except ValueError: continue
    if not la or not lo: continue
    t=0 if first=='Iron' else 2 if first=='Clay' else 1 if QUARRY.search(first) else 3
    try: yr=int(r['yr_lst_prd']) if r['yr_lst_prd'].strip().isdigit() else 0
    except Exception: yr=0
    nm=re.sub(r'\s+',' ',r['site_name']).strip()[:60] or 'Unnamed'
    out['p'].append([round(la,5),round(lo,5),t,nm,int(r['dep_id']),first[:24],'P' if r['dev_stat']=='Past Producer' else 'S',yr,k]); n[k]+=1
out['s']=dict(n)
s=json.dumps(out,separators=(',',':'),ensure_ascii=False); open('build/mines.json','w',encoding='utf-8').write(s)
print(dict(n)); print(Counter(TYPES[p[2]] for p in out['p']))
print('wrote build/mines.json',len(s)//1024,'KB;',len(out['p']),'sites')
