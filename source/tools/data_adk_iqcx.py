# November 21, 2026: Hamilton County, New York (Speculator, Lake Pleasant, Wells, Piseco, Indian Lake, Blue Mountain
# Lake and Raquette Lake). Drawn at random by tools/choose.py --state ny (region adk, which offered Speculator);
# start.py found one Atlas place (Griffin) within 30 km of Speculator and a thin landmark pin for Sagamore.
# Sources opened in this session: Wikipedia as raw text (tools/wiki_raw.py, the county's National Register list and the
# articles), and with tools/page.py the DEC pages for the Blue Mountain Wild Forest, the Jessup River Wild Forest and
# the Moose River Plains Complex, the Adirondack Experience's visit page, Great Camp Sagamore's tours page, the Town of
# Lake Pleasant's history page (museum hours), the Episcopal Diocese of Albany's page for the Church of the
# Transfiguration, the National Register form for CCC Camp S-90 (NPGallery), HMdb markers, St. William's on Long
# Point's home page, Hamilton County tourism's page for the Piseco Lake Historical Society, and two Adirondack Life
# articles (the Wells church, 2018; the Irondequoit Inn, 2019).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
def HM(n,t): return ['HMdb: '+t,'https://www.hmdb.org/m.asp?m='+n]
BATCH={'key':'adk_iqcx','label':'Hamilton County: Speculator, Piseco, Blue Mountain and Raquette lakes','added':'2026-11-21 23:43'}
DECBM=L('DEC: Blue Mountain Wild Forest','https://dec.ny.gov/places/blue-mountain-wild-forest')
DECJR=L('DEC: Jessup River Wild Forest','https://dec.ny.gov/places/jessup-river-wild-forest')
DECMR=L('DEC: Moose River Plains Complex','https://dec.ny.gov/places/moose-river-plains-complex')
LPHIST=L('Town of Lake Pleasant: our history (museum hours)','https://lakepleasantny.gov/our-history/')
ADKX=L('Adirondack Experience: plan your visit','https://www.theadkx.org/visit/plan-your-visit/')
PLACES=[
# ---- Blue Mountain Lake ----
N('blue-mountain-fire-tower','Blue Mountain fire tower, Blue Mountain Lake','Blue Mountain Lake','adk','landmark','standing',43.87238,-74.40096,'exact','public','hike','','1917',
  'A 35-foot steel Aermotor lookout tower put up on the summit of Blue Mountain in 1917 to watch over the Forest Preserve for fires. The station also holds an observer\'s cabin of 1975, the remains of three older observers\' cabins (one of 1949), the remains of a radar station of the 1960s, bits of the old telephone line along the foot trail and a stone survey benchmark of the 1890s. It was listed on the National Register in 2001.',
  'The steel tower on the 3,760-foot summit, which DEC says is open to the public; look for the cabin foundations, the radar station remains and the telephone-line remnants on the way up (all from the Register summary on Wikipedia; what is left of each not checked on the ground).',
  'A 1917 fire tower with the remains of a Cold War radar station beside it.',
  'State Forest Preserve, Blue Mountain Wild Forest (DEC), open year-round. DEC gives the Blue Mountain Trail as 2.2 miles, climbing 1,550 feet from the trailhead on State Route 30 near the Adirondack Museum. The trailhead lot OpenStreetMap maps is on the east side of Route 30 at Town Dump Road; the federal land map puts the lot on the Township 19 easement tract, which DEC says is open to public recreation.',
  [W('Blue Mountain Fire Observation Station'),DECBM],th=[43.87466,-74.43101],thn='Blue Mountain trailhead, Route 30 (OpenStreetMap)',brick='no'),
N('log-hotel-blue-mountain-lake','Log Hotel (Blue Mountain House Annex), Adirondack Experience','Blue Mountain Lake','adk','hotel','standing',43.86954,-74.43314,'site','open','drive','hotels','1876',
  'Built in 1876 as an annex of the Blue Mountain House, this two-storey hotel of square-hewn spruce logs with halved corners is one of the earliest and best known of the Adirondack resort hotels. The Adirondack Museum (now the Adirondack Experience) bought the property in 1954 and restored the annex where it stands. It was listed on the National Register in 1977. The museum also shows a 1909 fire tower moved from Whiteface Mountain, which a 1935 state marker calls the second fire tower in the Adirondacks.',
  'The log hotel with its verandah on the south and east sides, on the museum grounds, and the old Whiteface fire tower with its 1935 marker. Which rooms are open inside not checked.',
  'An 1876 log hotel saved as part of a museum.',
  'On the grounds of the Adirondack Experience, The Museum on Blue Mountain Lake, 9097 State Route 30. Admission charged (adults $22 to $24 on its page). Its page, read November 21, 2026, says it is closed for the 2026 season and that the 2027 season runs May 28 to October 11; the visitor centre is open 9:30 to 5:30 each day of the season. Parking at the museum.',
  [W('Blue Mountain House Annex'),ADKX,HM('44649','Fire Tower')],th=[43.87041,-74.43194],thn='Adirondack Experience lot, Route 30 (OpenStreetMap)',brick='no',
  hours='May 28 to October 11 (2027 season): visitor centre daily 9:30 a.m. to 5:30 p.m.'),
N('church-transfiguration-blue-mountain-lake','Church of the Transfiguration (log church), Blue Mountain Lake','Blue Mountain Lake','adk','worship','standing',43.85947,-74.43167,'exact','view','drive','','1880s',
  'A small Episcopal summer church of barked spruce logs, mitred at the corners, on a high fieldstone foundation, built to face the lake because most worshippers came by boat. Its date is not settled: the county\'s Register list on Wikipedia gives 1881, the article 1885, and the Diocese of Albany\'s page 1855. The article names Manley N. Cutter as designer and Thomas Wallace as builder, and says the first bellcote gave way to the present tower early in the 20th century. It was listed on the National Register in 1977.',
  'The log walls and stone base from Route 30, and the belfry at the lake end. Inside, the article names Tiffany glass windows and a Meneely bell given by Mrs. Levi P. Morton; interior not checked.',
  'A log church with Tiffany windows.',
  'An active Episcopal church of the Diocese of Albany, at 8927 Route 30 (OpenStreetMap), with a summer vicar. The diocese\'s page gives no service times, and no other page of the church\'s own was read. Look from the road outside services.',
  [W('Church of the Transfiguration (Blue Mountain Lake, New York)'),L('Episcopal Diocese of Albany: Church of the Transfiguration','https://albanyepiscopaldiocese.org/church-of-the-transfiguration-blue-mountain-lake-ny/')],conf='mixed',brick='no',hours='?'),
# ---- Raquette Lake ----
N('great-camp-sagamore','Great Camp Sagamore, Raquette Lake','Raquette Lake','adk','inst','standing',43.76422,-74.6301,'site','open','drive','','1895–1897',
  'William West Durant built Sagamore on Sagamore Lake between 1895 and 1897, after Pine Knot and Uncas. It has two complexes half a mile apart: the plain Upper, or workers\', complex and the Lower complex for guests. A lawsuit pushed Durant towards bankruptcy and he sold it in 1901 to Alfred Gwynne Vanderbilt, who added flush toilets, running water, a hydroelectric plant and an outdoor bowling alley. It later went to Syracuse University as a conference centre; to keep it from being torn down under the Forest Preserve\'s "forever wild" rule, the Preservation League of New York State arranged for a not-for-profit to own it under deed restrictions.',
  'The guest and workers\' complexes on a guided walking tour of about two hours with about half a mile on gravel paths (the camp\'s page). Rooms seen inside on the tour not checked.',
  'The Vanderbilts\' wilderness camp, bowling alley and all.',
  'Run by the Sagamore Institute of the Adirondacks, on Sagamore Road from Raquette Lake. Its tours page, read November 21, 2026, gives the 2026 guided history tour as daily at 10 a.m. and 1:30 p.m. from June 14 to October 16, and says the tours have ended for the season; book ahead. The camp also has rooms and programmes from May to October (Wikipedia). Parking not checked; a DEC lot for the Beaverflow trail is about 150 m south-west.',
  [W('Great Camp Sagamore'),L('Great Camp Sagamore: tours, hikes and paddles','https://greatcampsagamore.org/tours-hikes-paddles')],was='lm-great-camp-sagamore',brick='?',
  hours='Guided tour daily 10 a.m. and 1:30 p.m., June 14 to October 16 (2026 season); book ahead'),
N('camp-pine-knot-raquette-lake','Camp Pine Knot (Huntington Memorial Camp), Raquette Lake','Raquette Lake','adk','inst','standing',43.82133,-74.6262,'site','boat','boat','','1877',
  'The first of the Adirondack Great Camps, begun in 1877 by the railroad builder Thomas C. Durant as a showplace for investors and built up by his son William West Durant: a compound of log and stone buildings with twig work, among them a seven-room Swiss Cottage, four log cottages, a Glass Dining Room and a horse barn, joined by covered walks. William sold it in 1895 to Collis P. Huntington, who died there in 1900. It stood unused until 1947, when it was sold to the State University of New York at Cortland for one dollar as an outdoor education centre. It is a National Historic Landmark (2004). Echo Camp, built in 1883 for Governor Phineas C. Lounsbury, is beside it on Long Point and is a private summer home.',
  'The log and stone cottages on the south-west tip of Long Point, seen from the water. Not open to the public as far as any source read says; interior not checked.',
  'Where the Great Camp style began.',
  'Owned by SUNY Cortland and used for its outdoor education programmes; no public visiting found. Seen only from Raquette Lake by boat; St. William\'s, also on Long Point, says the point is reached by water. Echo Camp next door is private.',
  [W('Camp Pine Knot'),W('Echo Camp')],brick='?'),
N('st-williams-long-point-raquette-lake','St. William\'s church on Long Point, Raquette Lake','Raquette Lake','adk','worship','standing',43.82587,-74.63225,'exact','boat','boat','','1890',
  'William West Durant built this Shingle Style church in 1890 to designs from J. Cleaveland Cady\'s firm: a one-storey building with a steep roof and a two-storey round tower with a conical roof, between two open porches. It no longer belongs to the Catholic diocese. Since 1993 a non-denominational not-for-profit, St. William\'s on Long Point, has kept it, steadying the foundation and floor, replacing the cedar shingles and redoing the plaster and floors. It was listed on the National Register in 2004.',
  'The round shingled tower and porches from the water or on the grounds. Interior not checked.',
  'A Durant church you can only reach by boat.',
  'Kept by St. William\'s on Long Point Inc. Its page says the place is open seasonally and reached only by water; it rents housekeeping rooms and holds summer events, including an ecumenical service. No visiting hours given.',
  [W('St. William\'s Catholic Church (Long Lake, New York)'),L('St. William\'s on Long Point','https://www.stwilliamslongpoint.org/')],brick='?',hours='?'),
# ---- Lake Pleasant and Speculator ----
N('ccc-camp-s90-speculator','CCC Camp S-90 (Camp Speculator), Lake Pleasant','Speculator','adk','inst','standing',43.4856,-74.38504,'site','view','drive','','1934–1941',
  'The Civilian Conservation Corps built this camp in 1934 for up to 200 men, who built campgrounds in northern New York; it closed in November 1941. From 1945 4-H clubs ran it as Camp Sacandaga until 2004. It was bought in 2010 and reopened in 2014 as Camp Tekoa, a camp for children with special needs; the CCC infirmary was pulled down for a pool. The Register form of 2016 calls it the most intact group of CCC buildings in the state.',
  'Five barracks in a row along one side of the old parade ground and the dining and recreation halls opposite, board and batten with metal roofs, and the entrance gate: two cut-off pyramid posts on cobblestone bases with a log beam carrying the sign (Wikipedia, the Register form). A copy of the 1937 mural by the enrollee Hans Held is at the camp (form). Interior not checked.',
  'The best-kept CCC camp in New York, still a summer camp.',
  'A private children\'s camp on Page Street; look from the road at the gates. Do not go in. Not on public land.',
  [W('Civilian Conservation Corps Camp S-90'),L('National Register form (NPGallery, PDF)','https://npgallery.nps.gov/GetAsset/2379a74a-6737-4525-9846-d785ed528482')],brick='no'),
N('lake-pleasant-town-hall-speculator','Lake Pleasant Town Hall (historical museum), Speculator','Speculator','adk','civic','standing',43.49979,-74.36635,'exact','open','drive','','1894',
  'A plain front-gabled clapboard town hall of one and a half storeys, built in 1894 and listed on the National Register in 2009. Wikipedia says it was town hall and library until 1961 and library alone until 2003; the historical society\'s marker gives the library joining in 1937, the building becoming library only in 1965, the library moving out in 2002 and the museum opening in 2006. It is now the town\'s historical museum.',
  'The small white hall on Route 8 with the society\'s "First Town Hall" marker. Exhibits not checked.',
  '',
  'In the village of Speculator on Route 8, a short way west of Route 30 (HMdb). The Town of Lake Pleasant\'s history page gives the museum\'s season as June through August from Memorial Day weekend, and by appointment or when the open flag is flying. Street parking not checked.',
  [W('Lake Pleasant Town Hall'),LPHIST,HM('137052','First Town Hall')],conf='mixed',brick='no',
  hours='Memorial Day weekend to August: Tuesday 2 to 4 p.m., Friday and Saturday 10 a.m. to 2 p.m.; or by appointment'),
N('grace-methodist-church-speculator','Grace Methodist Church, Speculator','Speculator','adk','worship','standing',43.50104,-74.36582,'site','view','drive','','1908–1909',
  'The cornerstone was laid on November 15, 1908 and the church dedicated in October 1909 (the historical society\'s marker). It is a compact Gothic Revival frame church on a stock plan by Benjamin D. Price, with an engaged bell tower and a concrete block Sunday school wing of 1957, and much like the 1903 Methodist church at Indian Lake. The 1928 parsonage beside it is Dutch Colonial Revival with a gambrel roof. Listed on the National Register in 2015; the congregation left the United Methodist Church for the Global Methodist Church in 2024.',
  'Three pointed-arch windows on the front and the bell tower. Wikipedia says its memorial stained glass sets it apart from churches of the same plan; interior not checked.',
  '',
  'An active church (Mountain Community Methodist Church) on Route 8 in Speculator; no page of its own giving service times was found. Look from the street.',
  [W('Grace Methodist Church Complex'),HM('137055','Grace Methodist Episcopal Church')],brick='no',hours='?'),
N('hamilton-county-courthouse-lake-pleasant','Hamilton County Courthouse and 1848 stone jail, Lake Pleasant','Lake Pleasant','adk','civic','standing',43.4703,-74.4126,'exact','view','drive','','1848',
  'The county seat of one of the emptiest counties in the state. The complex has a Greek Revival stone jail with a stone addition of 1940, and a brick courthouse and county clerk\'s office of 1929 with porticos and cupolas, which replaced the frame courthouse of 1843. The Register gives the jail as 1848; the Town of Lake Pleasant\'s history says it was finished in 1849 of limestone from the south shore of Lake Pleasant, with Josiah Moffitt as mason. It was listed on the National Register in 1992 and the jail is called a rare survivor of its kind from before the Civil War.',
  'The stone jail and the two 1929 Colonial Revival buildings, red brick with white porticos and cupolas (Commons photograph of 2010 on the Wikipedia article), from Route 8. Interior not checked.',
  'A pre-Civil War stone jail beside a 1929 courthouse.',
  'Working county buildings on Route 8 in the hamlet of Lake Pleasant (the ArcGIS geocoder\'s point). Look from the road; whether the jail can be seen inside not checked.',
  [W('Hamilton County Courthouse Complex'),LPHIST],conf='mixed',brick='yes'),
N('pillsbury-mountain-fire-tower','Pillsbury Mountain fire tower, Lake Pleasant','Lake Pleasant','adk','landmark','standing',43.5809,-74.5121,'site','public','hike','','1924',
  'A 69-foot Aermotor steel lookout tower built on the summit of Pillsbury Mountain in 1924, with an observer\'s cabin and a shed added in 1950. It was listed on the National Register in 2010.',
  'The tower on the 3,597-foot summit, and the observer\'s cabin (Wikipedia; their state now not checked on the ground).',
  '',
  'State Forest Preserve, Jessup River Wild Forest (DEC), open year-round. DEC gives the Pillsbury Mountain Trail as 1.6 miles, climbing 1,480 feet from the Pillsbury Mountain Parking Area on Military Road, off State Route 30. Military Road crosses the Perkins Clearing easement lands. The trailhead point is OpenStreetMap\'s "Pillsbury Mountain Trailhead".',
  [W('Pillsbury Mountain Forest Fire Observation Station'),DECJR],th=[43.58714,-74.48536],thn='Pillsbury Mountain trailhead, Military Road (OpenStreetMap)',brick='no'),
N('wakely-mountain-fire-tower','Wakely Mountain fire tower','Lake Pleasant','adk','landmark','standing',43.73648,-74.51472,'site','public','hike','','1916',
  'A 70-foot steel Aermotor tower erected on Wakely Mountain in 1916, one of the first ten towers the State Conservation Commission bought to watch the Forest Preserve for fires. The three-mile foot trail counts as part of the Register listing of 2003.',
  'The tall tower on the 3,744-foot summit; DEC says the summit is in the Blue Ridge Wilderness. Its state now not checked.',
  '',
  'State Forest Preserve (DEC). DEC gives the Wakely Mountain Trail as 3.0 miles, climbing 1,600 feet; part of it is in very poor condition and the last half mile is steep. The trailhead is in the Moose River Plains on the Cedar River Road side; DEC notes the eastern part of the Limekiln Lake-Cedar River Road is closed west of the Cedar River Flow headquarters after a bridge failure. Seasonal road.',
  [W('Wakely Mountain Fire Observation Station'),DECMR],th=[43.73151,-74.47306],thn='Wakely Mountain trailhead parking (OpenStreetMap)',brick='no'),
# ---- Indian Lake ----
N('snowy-mountain-fire-tower','Snowy Mountain fire tower, Indian Lake','Indian Lake','adk','landmark','standing',43.70022,-74.38677,'site','public','hike','','1917',
  'Built in 1917 as a 22-foot prefabricated Aermotor tower; four more flights of stairs were added in 1933 as the trees grew, making it 45 feet. It closed in 1971 when fire spotting moved to aircraft, was listed on the National Register in 2001, and has been restored by DEC and volunteers and opened to the public.',
  'The tower on the summit. Its state now not checked on the ground.',
  '',
  'State Forest Preserve, Jessup River Wild Forest (DEC). DEC gives the Snowy Mountain Trail as 3.8 miles, climbing 2,000 feet from the Snowy Mountain Trail Parking Area off State Route 30, which holds nine cars.',
  [W('Snowy Mountain Fire Observation Station'),DECJR],th=[43.70125,-74.33473],thn='Snowy Mountain trail parking, Route 30 (OpenStreetMap)',brick='no'),
# ---- Wells ----
N('wells-baptist-church','Wells Baptist Church (The Revival), Wells','Wells','adk','worship','standing',43.40056,-74.28659,'area','view','drive','','1845',
  'A post-and-beam Greek Revival meeting house of 1845 on a rubble stone foundation, with a pedimented front and a louvred bell tower with a pyramid roof. It closed in 1949 (Wikipedia) or 1950 (Adirondack Life) and passed to the Hamilton County Historical Society; it was listed on the National Register in 1988. Private owners bought it in 2012 and opened it as a performance and event venue, The Revival.',
  'The white clapboard church with pointed-arch windows and doors and its bell tower, on Main Street. Adirondack Life in 2018 described a plain white interior, a pew with old spruce gum under it, hymnals of 1897 and workers\' names in the belfry; interior not checked since.',
  '',
  'Privately owned; open only for its events. Look from the street.',
  [W('Wells Baptist Church'),L('Adirondack Life: Born again (2018)','https://www.adirondacklife.com/2018/12/06/born-again/')],conf='mixed',brick='no'),
# ---- Piseco ----
N('riley-tavern-piseco','Riley Tavern and Riley House (Piseco museum), Piseco','Piseco','adk','hotel','standing',43.43481,-74.50852,'exact','open','drive','hotels','c. 1880',
  'The Piseco Historical Society\'s marker calls the Riley Tavern one of the oldest buildings in Piseco, of about 1880, used as a tavern and post office, and says it first stood just south of where it is now. The Piseco Lake Historical Society keeps it and the Riley House as its museum, with displays on hunting, fishing, ice cutting, tools, hotels and life on the lake.',
  'The small old tavern and the house beside it on Old Piseco Road, with the 2008 marker. Interior not checked.',
  '',
  'Piseco Lake Historical Society, 155 Old Piseco Road, about two miles north of Route 8 (HMdb). Hamilton County tourism\'s page gives open from the Fourth of July weekend to Labor Day weekend, Saturdays and Sundays 1 to 4; the society\'s own page was not found. Parking not checked.',
  [HM('137241','Riley Tavern'),L('Hamilton County tourism: Piseco Lake Historical Society','https://www.experienceouradirondacks.com/history/piseco-lake-historical-society')],conf='mixed',brick='?',
  hours='Fourth of July weekend to Labor Day weekend: Saturday and Sunday 1 to 4 p.m.'),
N('irondequoit-inn-piseco','Irondequoit Inn, Piseco Lake','Piseco','adk','hotel','standing',43.44719,-74.52608,'site','open','drive','hotels','1890s',
  'Albert Doubleday came to Piseco Lake on foot in 1877; in 1892 five of his friends pooled money as the Piseco Company to buy land here and built the clubhouse that still stands on a rise at the north end of the lake (Adirondack Life, 2019). Cabins were added in the 1960s. The founders\' descendants, who still run the company, turned the clubhouse into a country inn with renovations of over a million dollars in the five years before 2019.',
  'The old clubhouse and its lakeside cabins. Interior not checked.',
  'A club built by friends in 1892, now an inn their families still run.',
  'A working inn of the Piseco Company at the north end of Piseco Lake (the ArcGIS geocoder\'s point). Rooms and cabins for guests; whether non-guests may walk the grounds not checked. Season and hours not checked.',
  [L('Adirondack Life: The Irondequoit (2019)','https://www.adirondacklife.com/2019/01/03/the-irondequoit/')],brick='?',hours='?'),
]
PIN_NOTES={
 'blue-mountain-fire-tower':'OpenStreetMap tower point (nom.py), 1 m from the Wikipedia coordinate. Trailhead is the mapped lot at Town Dump Road.',
 'log-hotel-blue-mountain-lake':'OpenStreetMap museum point on the Adirondack Experience campus; the Log Hotel itself is not named on the map. The Register list point (43.855, -74.434) is 1.6 km south, off the campus.',
 'church-transfiguration-blue-mountain-lake':'OpenStreetMap building, 8927 Route 30, within 25 m of the Register point.',
 'great-camp-sagamore':'OpenStreetMap point for the tour start beside the gift shop (nom.py); replaces the landmark pin lm-great-camp-sagamore about 120 m away.',
 'camp-pine-knot-raquette-lake':'Register point on the tip of Long Point; OpenStreetMap buildings lie 50 to 100 m west.',
 'st-williams-long-point-raquette-lake':'OpenStreetMap building 25 m from the Register point on Long Point.',
 'ccc-camp-s90-speculator':'Register list point; the form gives the address as Page Street, and the geocoder\'s interpolated point for it is 100 m west.',
 'lake-pleasant-town-hall-speculator':'HMdb position of the society\'s First Town Hall marker on Route 8, about 100 m from the Register point.',
 'grace-methodist-church-speculator':'ArcGIS geocoder point for Mountain Community Methodist Church, beside the HMdb marker on Route 8. The Register list point (43.50058, -74.36776) is in woods 160 m west.',
 'hamilton-county-courthouse-lake-pleasant':'ArcGIS geocoder point for the Hamilton County Courthouse Complex, 10 m from the Register point.',
 'pillsbury-mountain-fire-tower':'OpenStreetMap peak, 60 m from the Register point; the tower stands on the summit.',
 'wakely-mountain-fire-tower':'Moved with pix.py 74 m from the OpenStreetMap peak onto the summit clearing with a small building, where the tower should stand. The Wikipedia/Register coordinate (43.7306, -74.4736) sits at the trailhead lot, 3.4 km away, not on the summit.',
 'snowy-mountain-fire-tower':'OpenStreetMap peak and observation-station point; the federal land map calls the spot Township 33 (closed), but DEC\'s page puts the trail and tower in the Jessup River Wild Forest. The Wikipedia coordinate (43.7019, -74.335) sits at the trail parking on Route 30, 4 km east of the summit.',
 'wells-baptist-church':'The Register list point fell on the lakeshore behind the houses; moved with pix.py 96 m east onto the main road through the hamlet. The church itself was not picked out on the aerial, so the pin marks only the stretch of street.',
 'riley-tavern-piseco':'ArcGIS PointAddress for 155 Old Piseco Road, 35 m from the HMdb marker.',
 'irondequoit-inn-piseco':'ArcGIS geocoder point of interest for the Irondequoit Inn.',
}
