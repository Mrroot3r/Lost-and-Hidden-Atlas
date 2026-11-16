#!/usr/bin/env python3
"""Build the vanished-places layer: features the federal names file marks "(historical)".

   python3 tools/vanished.py          reads cache/gnis/<ST>_Features_20210825.txt for every state in KEYS that is
                                      present; writes build/vanished.json (make.py copies it to data/)

The source is the U.S. Board on Geographic Names' file of August 25, 2021, the last one issued before the Board
stopped keeping schools, churches, post offices, mines, hospitals, airfields and other man-made features. Get a state:
   curl -o cache/gnis/NY_Features_20210825.txt \
     https://prd-tnm.s3.amazonaws.com/StagedProducts/GeographicNames/Archive/MainDomestic/NY_Features_20210825.txt
It is a work of the U.S. government and in the public domain.

What "(historical)" means there: the feature no longer exists or no longer serves that purpose. It does NOT mean
nothing is left: a "historical" school may be a house today, a cellar hole, or a field. Positions were mostly read off
old maps and can be 100 m or more out. Every point is an unchecked lead, like the OpenStreetMap leads.

Rows: [lat, lon, type, name, GNIS id, state]. Like the other layers this rebuilds the states whose raw file is
present and keeps the rest of an existing build/vanished.json."""
import csv,io,json,os
from collections import Counter
KEYS=['ny','ma','vt','ct','nh','nj','pa','ri','me']
TYPES=['Vanished hamlet or locale','Old school site','Old church site','Old military site','Old airfield','Old hospital','Old post office','Old mine','Other vanished building or structure']
CLASS={'Populated Place':0,'Locale':0,'School':1,'Church':2,'Military':3,'Airport':4,'Hospital':5,'Post Office':6,'Mine':7,
       'Building':8,'Cemetery':8,'Bridge':8,'Dam':8,'Reservoir':8,'Canal':8,'Park':8,'Tower':8,'Tunnel':8,'Crossing':8,'Harbor':8,'Trail':8,'Oilfield':8,'Well':8}
old=json.load(open('build/vanished.json')) if os.path.exists('build/vanished.json') else None
out={'v':1,'t':TYPES,'p':[],'s':{}}
have=[k for k in KEYS if os.path.exists(f'cache/gnis/{k.upper()}_Features_20210825.txt')]
if old:
    keep=[s for s in old.get('s',{}) if s not in have]
    out['p']+=[p for p in old['p'] if p[5] in keep]
    for s in keep: out['s'][s]=old['s'][s]
    if keep: print('kept from the existing build/vanished.json:',' '.join(keep))
for k in have:
    rows=csv.DictReader(io.StringIO(open(f'cache/gnis/{k.upper()}_Features_20210825.txt',encoding='utf-8-sig').read()),delimiter='|')
    n=Counter()
    for r in rows:
        nm=r['FEATURE_NAME']
        if '(historical)' not in nm or r['FEATURE_CLASS'] not in CLASS: continue
        try: la,lo=float(r['PRIM_LAT_DEC']),float(r['PRIM_LONG_DEC'])
        except ValueError: continue
        if not la or not lo: continue
        t=CLASS[r['FEATURE_CLASS']]
        out['p'].append([round(la,5),round(lo,5),t,nm.replace(' (historical)','').strip()[:60],int(r['FEATURE_ID']),k]); n[TYPES[t]]+=1
    out['s'][k]=sum(n.values())
    print(k,sum(n.values()),dict(n.most_common(4)))
s=json.dumps(out,separators=(',',':'),ensure_ascii=False); open('build/vanished.json','w',encoding='utf-8').write(s)
print('wrote build/vanished.json',len(s)//1024,'KB;',len(out['p']),'places in',len(out['s']),'states')
