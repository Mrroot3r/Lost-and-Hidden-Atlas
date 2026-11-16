"""The base every state is built on: its name, regions, start cities and what is wired up for it.
build_sites.py, drive.py, make.py and check.py all read this file, and the app gets it through index.html.
To open a new area inside a listed state you only add places (GUIDE.md section 6).
Region codes, once used by published places, should not be renamed."""
STATES=[
 {'k':'ny','name':'New York','imagery':'state leaf-off and LiDAR (NYS ITS)','owners':'some counties','legal':True,
  'regions':[('alb','Albany'),('albco','Albany County'),('troy','Troy & Lansingburgh'),('renss','Rensselaer County'),('conf','Cohoes · Waterford · Watervliet'),('sch','Schenectady'),('mohawk','Mohawk Valley'),('sar','Saratoga'),('hud','Hudson Valley'),('cat','Catskills'),('adk','Lake George & Adirondacks'),('wash','Upper Hudson & Washington Co.'),('mohw','Mohawk Valley west'),('scho','Schoharie, Otsego & Delaware'),('midh','Mid-Hudson'),
             ('nyc','New York City & Long Island'),('cny','Central New York'),('wny','Western New York & Finger Lakes'),('nny','North Country & St. Lawrence')],
  'hubs':[('alb','Albany',42.6526,-73.7562),('sch','Schenectady',42.8142,-73.9396),('troy','Troy',42.7284,-73.6918),('sar','Saratoga Springs',43.0831,-73.7846),('syr','Syracuse',43.0481,-76.1474),('buf','Buffalo',42.8864,-78.8784)]},
 {'k':'ma','name':'Massachusetts','imagery':'state leaf-off and LiDAR (MassGIS)','owners':'statewide','legal':True,
  'regions':[('berk','Berkshires'),('pv','Pioneer Valley'),('cmass','Quabbin & central Massachusetts'),('worc','Worcester & Blackstone Valley'),('bos','Greater Boston & MetroWest'),('nshore','North Shore & Merrimack Valley'),('south','South Shore, South Coast & Cape Cod')],
  'hubs':[('wor','Worcester',42.2626,-71.8023),('bost','Boston',42.3601,-71.0589)]},
 {'k':'ri','name':'Rhode Island','imagery':'state leaf-off and LiDAR (RIGIS)','owners':'not built','legal':True,
  'regions':[('riprov','Providence, Blackstone Valley & western Rhode Island'),('ribay','Narragansett Bay & Newport'),('risouth','South County, Rhode Island')],
  'hubs':[('prov','Providence',41.8242,-71.4126)]},
 {'k':'vt','name':'Vermont','imagery':'state aerial and LiDAR (VCGI)','owners':'not built','legal':False,
  'regions':[('vt','Southern Vermont'),('vtc','Central Vermont'),('vtn','Northern Vermont & Champlain Valley')],
  'hubs':[('mont','Montpelier',44.2601,-72.5754),('burl','Burlington',44.4759,-73.2121)]},
 {'k':'ct','name':'Connecticut','imagery':'fallback (Esri satellite and world hillshade)','owners':'not built','legal':False,
  'regions':[('ct','Northwest Connecticut'),('cthv','Hartford & the Connecticut Valley'),('ctsw','New Haven & southwest Connecticut'),('cte','Eastern Connecticut')],
  'hubs':[('hart','Hartford',41.7658,-72.6734)]},
 {'k':'nh','name':'New Hampshire','imagery':'fallback (Esri satellite and world hillshade)','owners':'not built','legal':False,
  'regions':[('nhs','Southern New Hampshire'),('nhl','Lakes Region & Seacoast'),('nhw','White Mountains & North Country')],
  'hubs':[('conc','Concord',43.2081,-71.5376)]},
 {'k':'me','name':'Maine','imagery':'fallback (Esri satellite and world hillshade)','owners':'not built','legal':False,
  'regions':[('mes','Southern Maine & Portland'),('mec','Midcoast & central Maine'),('men','Northern & Downeast Maine')],
  'hubs':[('aug','Augusta',44.3106,-69.7795),('port','Portland',43.6591,-70.2568)]},
 {'k':'nj','name':'New Jersey','imagery':'fallback (Esri satellite and world hillshade)','owners':'not built','legal':False,
  'regions':[('njn','North Jersey'),('njc','Central Jersey'),('njs','South Jersey & the Pine Barrens')],
  'hubs':[('tren','Trenton',40.2206,-74.7597)]},
 {'k':'pa','name':'Pennsylvania','imagery':'fallback (Esri satellite and world hillshade)','owners':'not built','legal':False,
  'regions':[('pae','Philadelphia & southeast Pennsylvania'),('pane','Northeast Pennsylvania & the Poconos'),('pac','Central Pennsylvania'),('paw','Western Pennsylvania')],
  'hubs':[('harr','Harrisburg',40.2732,-76.8867),('phil','Philadelphia',39.9526,-75.1652),('pitt','Pittsburgh',40.4406,-79.9959)]},
 {'k':'mo','name':'Missouri','imagery':'fallback (Esri satellite and world hillshade)','owners':'not built','legal':False,
  'regions':[('kcmo','Kansas City, Missouri')],
  'hubs':[('kc','Kansas City',39.0997,-94.5786)]},
]
REG={c:l for s in STATES for c,l in s['regions']}
REG_STATE={c:s['k'] for s in STATES for c,l in s['regions']}
HUBS=[(i,n,la,lo,s['k']) for s in STATES for i,n,la,lo in s['hubs']]
assert len(REG)==sum(len(s['regions']) for s in STATES),'a region code is used twice'
assert len({h[0] for h in HUBS})==len(HUBS),'a start-city id is used twice'
