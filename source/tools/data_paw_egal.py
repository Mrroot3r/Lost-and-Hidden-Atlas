# November 18, 2026: Western Pennsylvania (region paw, drawn at random by tools/choose.py), first close pass:
# Beaver County, where the Beaver River meets the Ohio. The Harmonists' village at Economy, two frontier army sites
# (Fort McIntosh and Legionville), the 1786 starting point of the federal land survey, a 1904 Ohio River lock station,
# a canal lock, an 1806 stone academy, an 1820s stone mansion, railroad stations, a Carnegie library, an iron truss
# bridge with a mill site on State Game Land, and the ruins of a mineral-springs resort in Raccoon Creek State Park.
# Facts come from the linked sources only. Wikipedia articles were read as raw text (tools/wiki_raw.py); HMdb marker
# pages, SAH Archipedia (Buildings of Pennsylvania), PHMC, Old Economy Village, DCNR, Beaver County Library System,
# the Beaver Area Heritage Foundation, the Little Beaver Historical Society, Atlas Obscura and one National Register
# form (88000868) were read with tools/page.py. Where sources disagree the text gives both; where a source is silent
# it says "not checked".
# Pins: a Wikipedia/Register coordinate, an HMdb marker position, an ArcGIS address match or an OpenStreetMap feature,
# as each pin note says, then looked at on the pin check (aerial and LiDAR sheets).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
OEV_VISIT=L('Old Economy Village: Plan your visit (hours, admission, parking)','https://www.oldeconomyvillage.org/visit')
PHMC_OEV=L('PHMC: Old Economy Village','https://www.pa.gov/agencies/phmc/historic-sites-and-museums/rural-farm-and-village-history-trail/old-economy')
SAH_OEV=L('SAH Archipedia: Old Economy Historic District and Visitor Center','https://sah-archipedia.org/node/17161')
HM_LEG1=L('HMdb: Legionville Monument (DAR, 1916)','https://www.hmdb.org/m.asp?m=40300')
HM_LEG2=L('HMdb: Legionville (PHMC marker)','https://www.hmdb.org/m.asp?m=56581')
HM_FM=L('HMdb: Fort McIntosh (one of four site panels)','https://www.hmdb.org/m.asp?m=44888')
HM_BAHF=L('HMdb: Beaver Area Heritage Foundation timeline','https://www.hmdb.org/m.asp?m=176908')
BCPA_FM=L('Beaver County history pages: Site of Fort McIntosh','https://bcpahistory.org/beavercounty/BeaverCountyCommunities/Beaverfolder/Tour/Tour.FortMcIntosh.html')
SAH_LOCK6=L('SAH Archipedia: Lock 6 Landing Restaurant and Marina (Merrill Station Lockhouse)','https://sah-archipedia.org/node/17171')
AO_LOCK6=L('Atlas Obscura: Old Lock Six on the Ohio River','https://atlasobscura.com/places/old-lock-six-on-the-ohio-river')
LBHS_HOURS=L('Little Beaver Historical Society: open museum days (2022)','https://littlebeaverhistorical.org/event/open-museum-hours')
LBHS_ABOUT=L('Little Beaver Historical Society: history of the museum','https://littlebeaverhistorical.org/about-lbhs')
BCHRLF=L('Beaver County Historical Research & Landmarks Foundation','https://bchrlf.org/')
HM_WATTS=L('HMdb: Foulks-Martin-Watts Mill and Bridge','https://www.hmdb.org/m.asp?m=62684')
NR_WATTS=L('National Register form: Bridge in South Beaver Township (88000868)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/88000868_text')
SAH_ALIQ=L('SAH Archipedia: Pittsburgh and Lake Erie Railroad Station, Aliquippa','https://sah-archipedia.org/node/17153')
DCNR_RC_HIST=L('DCNR: History of Raccoon Creek State Park (Frankfort Mineral Springs)','https://www.dcnr.pa.gov/StateParks/FindAPark/RaccoonCreekStatePark/Pages/History.aspx')
DCNR_RC_HIKE=L('DCNR: Hiking at Raccoon Creek State Park','https://www.pa.gov/agencies/dcnr/recreation/where-to-go/state-parks/find-a-park/raccoon-creek-state-park/hiking')
DCNR_RC=L('DCNR: Raccoon Creek State Park (hours)','https://www.pa.gov/agencies/dcnr/recreation/where-to-go/state-parks/find-a-park/raccoon-creek-state-park')
HM_GIRARD=L('HMdb: Girard Locks','https://www.hmdb.org/m.asp?m=206673')
SAH_BEAVSTA=L('SAH Archipedia: Beaver P&LE passenger and freight depots (Beaver Area Heritage Museum)','https://sah-archipedia.org/node/17169')
BAHF_ABOUT=L('Beaver Area Heritage Foundation: about the museum','https://beaverheritage.org/about/')
BCLS_BF=L('Beaver County Library System: Carnegie Free Library, Beaver Falls (hours)','https://beaverlibraries.org/libraries/beaver-falls')
PLACES=[
# ---- Standing ----
N('old-economy-village-ambridge','Old Economy Village','Ambridge','paw','town','standing',40.59612,-80.23300,'site','open','walk','','1824–1905',
  'The third and last town of the Harmony Society, a celibate Christian commune led by George Rapp that came from Württemberg in 1803–04 and built Harmony (Butler County) and New Harmony (Indiana) before settling here on the Ohio in 1824. Between 1824 and 1832 the Harmonists built more than a hundred houses, mills and a church; Frederick Rapp, a stonemason, designed the larger buildings. The society ran mills, a brick works, an oil company and a savings bank, and was dissolved in 1906. The Commonwealth bought 6 acres and 17 buildings in 1916; it is a National Historic Landmark.',
  'Seventeen buildings and the gardens inside a picket fence, in red brick and frame: the Feast Hall (offices below, a 96-by-50-foot hall with an elliptical ceiling above, its ground floor once one of the country\'s earliest museums), the joined George and Frederick Rapp houses with their portico and jerkinhead roof, the half-timbered 1824 Granary on a rubble foundation, and in the garden the round Grotto of yellow sandstone with a thatched roof and a plastered Greek Revival room inside. Around the village, about eighty more Harmonist-era houses and shops still stand in Ambridge. Part of the visit is a guided tour, the rest self-guided.',
  'A celibate commune\'s last town, with its feast hall, granary and hermit\'s grotto still standing.',
  'Old Economy Village (Pennsylvania Historical and Museum Commission), 270 16th Street, Ambridge; tickets at the Museum Store in the Feast Hall, 1401 Church Street. The village\'s own page gives: closed January to March; open April 10 to December 20, 2026, Friday and Saturday 10 am to 4 pm and Sunday noon to 4 pm, with guided tours at 10:30, 12:30 and 2. The PHMC page lists Wednesday and Thursday 10 to 4 and guided tours Friday to Sunday 10 to 4, so check before a weekday visit. Adults $10, seniors $9, youth $6. Free parking at the Visitor Center, free street parking at the historic site. Read November 2026.',
  [OEV_VISIT,PHMC_OEV,SAH_OEV,W('Old Economy Village')],conf='mixed',th=[40.59833,-80.23153],thn='Old Economy Visitor Center, 270 16th Street',brick='yes',hours='April 10 to December 20, 2026: Friday and Saturday 10 a.m. to 4 p.m., Sunday noon to 4 p.m. Closed January to March. The PHMC page also lists Wednesday and Thursday 10 to 4'),
N('merrill-lock-6-industry','Merrill Lock No. 6 lock station','Industry','paw','canal','standing',40.66890,-80.35140,'site','view','drive','','1892–1936',
  'Part of the canalization of the Ohio River: building began on 2 June 1892, the lock opened on 3 August 1904, and the whole cost $1,123,441.80. The concrete lock, 600 by 110 feet, lay at the north end of a dam with a weir. The station was named for William E. Merrill of the Army Corps of Engineers, and was replaced by the Montgomery Lock and Dam in 1936. The buildings stood empty for about 45 years, were listed on the National Register in 1980, and the powerhouse opened as a restaurant, Lock 6 Landing, in 2000; Atlas Obscura says it has been closed since 2012 and the site abandoned.',
  'Orange-red brick Romanesque or Italianate buildings on a strip between PA 68 and the river: the three-story lockhouse that held the lock machinery, with round-arched windows, stone trim and a tower that hid a water tank, and a foursquare lockmaster\'s house to its east. Sources disagree on what else stands: Wikipedia says all three buildings remain, SAH Archipedia that the matching house to the west was demolished. Inside, the lockhouse keeps a metal stair rail (SAH Archipedia); whether the interior can be seen now was not checked.',
  'An Ohio River lock station from 1904, left almost as built.',
  'Beside Midland-Beaver Road (PA 68), 610 Midland-Beaver Road, Industry. Who owns it now was not checked; Atlas Obscura describes two large parking lots and no one in attendance, but the buildings are closed. Look from the road and do not go in.',
  [SAH_LOCK6,AO_LOCK6,W('Merrill Lock No. 6')],conf='mixed',brick='yes'),
N('greersburg-academy-darlington','Greersburg Academy','Darlington','paw','civic','standing',40.80990,-80.42342,'exact','open','drive','','1806–',
  'A college-preparatory academy founded in 1802 by the Reverend Thomas Hughes; the stone building went up about 1806, which makes it one of the oldest standing in Beaver County. John Brown the abolitionist, John White Geary and William Holmes McGuffey studied here. From 1883 to 1972 the building served several railroads as a station. The Little Beaver Historical Society keeps it as a museum.',
  'A Georgian stone schoolhouse on Market Street. The Historical Society\'s displays inside have included the 100th Pennsylvania Volunteers and a scale model of Legionville; original interior fabric not checked.',
  'The school John Brown attended, later a railroad station.',
  'Little Beaver Historical Society, Market Street, Darlington. Open on set days only: in 2022 the society opened the museum one Saturday a month from July to October, 10 am to 4 pm. This year\'s dates not checked. Parking not checked; street parking in the borough.',
  [LBHS_HOURS,LBHS_ABOUT,W('Greersburg Academy')],brick='no'),
N('vicary-house-freedom','Captain William Vicary House','Freedom','paw','civic','standing',40.68214,-80.25054,'exact','view','drive','','1826–1829',
  'A mansion of locally quarried sandstone built from 1826 to 1829 for William Vicary, a Navy captain in the War of 1812, at the edge of the town he laid out as "St. Clair" next to the Harmonists\' Economy. A dispute with one of his builders went to the Pennsylvania Supreme Court and was not settled until after his death in 1842. His family lived here until 1912. The house was condemned for Route 65 in the 1960s and saved by a local campaign; Beaver County owns it.',
  'The large, finely dressed sandstone blocks, rare in western Pennsylvania at that date (Wikipedia). It is the home of the Beaver County Historical Research and Landmarks Foundation, the county\'s historical society, which holds open houses; interior not checked.',
  '',
  'Owned by Beaver County and used by the Beaver County Historical Research and Landmarks Foundation, 1235 3rd Avenue, Freedom. Hours not checked: see the foundation\'s page for open houses. Parking not checked.',
  [BCHRLF,W('Captain William Vicary House')],brick='no'),
N('aliquippa-ple-station','Pittsburgh and Lake Erie station, Aliquippa','Aliquippa','paw','rail','standing',40.61878,-80.24284,'exact','view','drive','','1911–',
  'The Pittsburgh and Lake Erie Railroad\'s station for Woodlawn (Aliquippa), replacing a first station that was little more than a shed. Wikipedia gives 1911; SAH Archipedia dates it about 1915 (1914–16) and attributes it to Joseph Ladd Neal. After passenger service ended it was used as offices by Jones and Laughlin Steel. Wikipedia says it now stands empty; SAH Archipedia (2010) has it as offices of LTV Structural Steel. The line is now CSX.',
  'The largest and best-kept station in Beaver County (SAH Archipedia): a cross-shaped plan, brown brick and stone walls, Dutch gables with ball finials, big wooden brackets under deep eaves, a castellated bay, a tile roof and a corbeled chimney. Interior not checked.',
  '',
  'Station Street, Aliquippa, beside the active CSX line. Owner not checked. Look from the street; keep off the tracks.',
  [SAH_ALIQ,W('Aliquippa station')],conf='mixed',brick='?'),
N('beaver-ple-stations','Beaver P&LE stations (Beaver Area Heritage Museum)','Beaver','paw','rail','standing',40.69780,-80.29671,'site','open','drive','','1897–',
  'The Pittsburgh and Lake Erie Railroad\'s passenger station (1897) and freight station (1911) in Beaver. The borough acquired them when the railroad sold its real estate, and in 1996 made the freight house available to the Beaver Area Heritage Foundation, which opened it as a museum in 1998 and later restored the passenger station as an event center. A log house built in 1998 from 18th-century logs salvaged from a local house stands beside the museum.',
  'Brick and stone stations with deep eaves on oversized wooden brackets; the passenger station has eyebrow dormers and stone round arches, and lost its porte-cochère. A tunnel under the tracks leads to the far platform. The freight office now holds railroad displays and the museum shop.',
  '',
  'Beaver Area Heritage Museum (Beaver Area Heritage Foundation), in the borough-owned freight station on East End Avenue / River Road, Beaver. Free parking beside the building. The foundation\'s page said only that the museum would reopen in spring 2025; current hours not checked.',
  [SAH_BEAVSTA,BAHF_ABOUT,HM_BAHF],brick='?'),
N('carnegie-library-beaver-falls','Carnegie Free Library of Beaver Falls','Beaver Falls','paw','civic','standing',40.75427,-80.31973,'exact','open','drive','','1899–1903',
  'Beaver County\'s first purpose-built library, paid for with $50,000 from Andrew Carnegie and designed by Pittsburgh architect Frederick J. Osterling. Building began in 1899 and it opened a week before Christmas 1903. It is still the town library.',
  'A Neoclassical building of yellow brick on a raised stone foundation, with granite trim and terracotta round many windows. The second floor holds a genealogy and local-history library, and the city\'s historical museum is in the basement, in what was the performance hall until 1961. Original interior fittings not checked.',
  '',
  'Carnegie Free Library of Beaver Falls, 1301 7th Avenue, a public library (owner not checked). Open Monday and Wednesday 10 am to 7 pm, Tuesday and Thursday 10 to 5, Saturday 9 to 4 (Beaver County Library System page, read November 2026). Parking not checked.',
  [BCLS_BF,W('Carnegie Free Library of Beaver Falls')],brick='no',hours='Monday and Wednesday 10 a.m. to 7 p.m.; Tuesday and Thursday 10 to 5; Saturday 9 to 4'),
# ---- Ruins, traces and sites ----
N('fort-mcintosh-site-beaver','Fort McIntosh site','Beaver','paw','fort','traces',40.69122,-80.30340,'site','public','walk','','1778–1791',
  'The first American fort north of the Ohio, built in 1778 under the French engineer Cambray-Digny and named for General Lachlan McIntosh: a trapezoid about 150 feet a side with earthen corner bastions, log walls and a ditch, above the Ohio near the mouth of the Beaver. It held the 1785 Treaty of Fort McIntosh and, in 1784–85, most of the United States Army. It was abandoned in 1791. Volunteers began digging for it in 1974, and the dig was finished for the fort\'s 200th anniversary in 1978.',
  'A roadside park on River Road with four panels and a DAR granite monument. Uncovered and left to see: stone fireplace hearths and a stretch of the fieldstone footer of the fort\'s south wall; the panels say the angle of one foundation wall fixed the fort\'s size and shape.',
  'The fort that once held nearly the whole U.S. Army.',
  'A public park on River Road at Insurance Street in Beaver, opened to the public in 1978 (Beaver Area Heritage Foundation marker; HMdb calls it a roadside park). Who owns the ground and its hours were not checked; the federal land map does not hold it. Street parking; the mapped lots nearest are in town to the north.',
  [HM_FM,HM_BAHF,BCPA_FM,W('Fort McIntosh (Pennsylvania)')],brick='no'),
N('legionville-baden','Legionville','Baden','paw','fort','marker',40.62282,-80.22662,'area','view','drive','','1792–1793',
  'Where Major General Anthony Wayne trained the new Legion of the United States in the winter of 1792–93, after St. Clair\'s defeat in 1791: the first formal training camp of the United States Army. The Legion left in spring 1793 and won the Battle of Fallen Timbers in August 1794. The same stretch of the Ohio was the site of Logstown, where the 1748 treaty was signed and George Washington stopped in 1753.',
  'A 1916 DAR monument and a 1946 state marker at Duss Avenue and Anthony Wayne Drive, with Logstown markers beside them, in what HMdb calls the Logstown/Legionville Historic Park and Center. Nothing of the camp itself is said to show.',
  '',
  'Duss Avenue (PA 65) at Anthony Wayne Drive, Harmony Township near Baden. Owner of the park, parking and hours not checked: look from the roadside.',
  [HM_LEG1,HM_LEG2,W('Legionville')],conf='mixed',brick='?'),
N('beginning-point-land-survey','Beginning Point of the U.S. Public Land Survey','Ohioville','paw','landmark','marker',40.64250,-80.51903,'area','view','drive','','1785–',
  'In 1786 Thomas Hutchins, Geographer of the United States, began the survey of the Northwest Territory from a stake on the north bank of the Ohio that a Virginia–Pennsylvania team had set in 1785 to fix their boundary. The survey grid it began now covers Ohio, Indiana, Illinois, Michigan, Wisconsin and part of Minnesota. The point itself is under the river; a monument was put up near it in 1881, and the area is a National Historic Landmark.',
  'The 1881 monument on the state line, beside PA 68 / Ohio 39 at the Ohio–Pennsylvania border, inscribed that the point of beginning lay 1,112 feet south of it. Kept by the East Liverpool Historical Society.',
  'Where the grid of the American Midwest begins.',
  'On the south side of PA 68 / Ohio 39 at the state line, between Ohioville and East Liverpool, Ohio. Owner and a place to pull off were not checked; the mapped lots nearest are on Midland Road in Smiths Ferry, half a kilometre east.',
  [W('Beginning Point of the U.S. Public Land Survey')],brick='?'),
N('girard-locks-rochester','Girard Locks (Beaver Division Canal)','Rochester','paw','canal','traces',40.70195,-80.28910,'area','view','walk','','1833–1870s',
  'The entrance to the Beaver Division Canal, which ran up the Beaver River to the Erie Extension Canal near New Castle and opened in December 1834. The two Girard Locks, numbers 16 and 17, were finished in 1833 to take boats round Dam No. 6 between Rochester and Bridgewater, and were built 25 by 120 feet, bigger than the canal\'s other locks, so small Ohio River steamboats could use them. They are named for Stephen Girard, who gave $300,000 to Pennsylvania\'s canals. The canal was used until the 1870s.',
  'Part of the locks is still to be seen below the Bridgewater–Rochester Bridge (HMdb marker text). How much, and from where, was not checked.',
  '',
  'The marker is at Madison Street and Delaware Avenue, Rochester. Owner of the lock remains not checked: look from public ground near the bridge.',
  [HM_GIRARD],brick='?'),
N('watts-mill-bridge','Watts Mill Bridge and mill site','South Beaver Township','paw','industry','standing',40.79056,-80.49389,'site','public','walk','','1878–',
  'A pin-connected Pratt pony truss over Little Beaver Creek, built in 1878 by the West Penn Bridge Company of Beaver Falls, beside a mill site: George Foulks built saw and grist mills here, and Jesse Martin, then Reuben Watt and his sons, ran them. The bridge and the mill remains were listed together on the National Register in 1988. PennDOT considered tearing the rusting bridge down; it was taken out in 2019, restored with Workin\' Bridges for foot traffic only, and put back in March 2023.',
  'The iron truss, now a footbridge, on stone abutments (Register form), with a county landmarks marker just east of it. What is left of the mill was not checked.',
  '',
  'On State Game Land 285 (Pennsylvania Game Commission land, open to the public; hunting is allowed in season), on Watts Mill Road, about an eighth of a mile west of the North Country Trail. HMdb points to a parking lot off Cannelton Road with a spur trail to the bridge; the lot used for th= is the one on Watts Mill Road. Hours and rules not checked.',
  [HM_WATTS,NR_WATTS,W('Watts Mill Bridge')],th=[40.78210,-80.48990],thn='State Game Land 285 lot, Watts Mill Road',brick='no'),
N('frankfort-mineral-springs','Frankfort Mineral Springs resort ruins','Hanover Township','paw','hotel','ruins',40.49851,-80.43133,'site','public','walk','','1827–',
  'Springs that rise from the shale and sandstone across from a waterfall at the head of a wooded ravine. Edward McGinnis bought the land in 1827, found the water "healing to his ailments" and built a health spa and resort; the village of Frankfort grew with it and took the name Frankfort Springs. The land became part of Raccoon Creek, built in the 1930s as a Recreational Demonstration Area by the CCC and the WPA, now a state park.',
  'The falls over a U-shaped grotto, the springs that run year round, and above them remnants of the 1800s resort (DCNR hiking page). What the remnants are was not checked.',
  'A forgotten 19th-century spa beside a waterfall.',
  'Raccoon Creek State Park (DCNR). Park open every day, sunrise to sunset. Walk the short Mineral Springs Loop Trail from the parking lot on PA 18 or from the park office; the park office has a brochure. Read November 2026.',
  [DCNR_RC_HIST,DCNR_RC_HIKE,DCNR_RC],th=[40.49776,-80.42788],thn='Raccoon Creek SP lot by PA 18 (Heritage Trail)',brick='?'),
]
PIN_NOTES={
 'old-economy-village-ambridge':'OpenStreetMap park polygon for the village (40.59612, -80.233), matching Wikipedia; the leaf-off aerial shows the ring on the village garden with the round Grotto. The parking point is the ArcGIS match for the Visitor Center, 270 16th Street; the tile shows the Visitor Center and its lot.',
 'merrill-lock-6-industry':'OpenStreetMap historic feature "Merrill Lock No. 6" (40.6689, -80.3514), matching the Register list; the ArcGIS match for 610 Midland-Beaver Road fell 500 m east and was not used. Leaf-off aerial: the ring is on the lockhouse by the river, with a second building just to the north.',
 'greersburg-academy-darlington':'OpenStreetMap feature "Greersburg Academy", Market Street (40.8099, -80.42342), matching the Register list; the Esri tile shows the ring on a building on Market Street.',
 'vicary-house-freedom':'ArcGIS address match for 1235 3rd Avenue, Freedom; the ring is on the house in its triangle of roads above Route 65.',
 'aliquippa-ple-station':'ArcGIS address match for 111 Station Street, Aliquippa (SAH Archipedia address), 10 m from the Wikipedia point; the aerial shows the ring on the station beside the tracks.',
 'beaver-ple-stations':'ArcGIS match for 250 East End Avenue, Beaver; SAH Archipedia gives 250 River Road East. The aerial shows the ring on a station-like building beside the tracks; which of the two stations it is was not told apart.',
 'carnegie-library-beaver-falls':'ArcGIS address match for 1301 7th Avenue, Beaver Falls; the ring is on the corner building.',
 'fort-mcintosh-site-beaver':'HMdb position of the Fort McIntosh panel at River Road and Insurance Street (40° 41.473′, 80° 18.204′); the aerial shows the ring in the grassy park strip between River Road and the railroad above the Ohio.',
 'legionville-baden':'HMdb position of the 1916 DAR monument at Duss Avenue and Anthony Wayne Drive (40° 37.369′, 80° 13.597′); the camp covered the ground round it. The ring is on the roadside green west of Duss Avenue.',
 'beginning-point-land-survey':'Wikipedia coordinate for the landmark; the monument is by the road at the state line. The ring falls on the road and rail strip north of the river; the monument itself was not seen on the aerial, hence prec area.',
 'girard-locks-rochester':'HMdb position of the Girard Locks marker, Madison Street and Delaware Avenue, Rochester (40° 42.117′, 80° 17.346′); the lock remains are below the Bridgewater–Rochester Bridge, not at the pin. The aerial shows the marker corner at the east end of the bridge; the river bank under the bridge is about 150 m west.',
 'watts-mill-bridge':'Wikipedia coordinate for the bridge; the HMdb marker just east of it is at 40° 47.496′, 80° 29.553′. The leaf-off aerial shows the ring on the truss over the creek. The parking point is an OpenStreetMap lot on Watts Mill Road 1 km south, on State Game Land 285; its tile shows only a small opening where the road meets a track in the woods, so the lot is not confirmed.',
 'frankfort-mineral-springs':'OpenStreetMap waterfall "Frankfort Mineral Springs" (40.49851, -80.43133); the resort remnants are above the falls. The LiDAR sheet shows the ring at the head of a ravine with a trail on the slope above. The parking point is an OpenStreetMap lot on the park\'s Heritage Trail; the aerial shows a pull-off by the road, which was not confirmed as PA 18.',
}
BATCH={'key':'paw_egal','label':'Beaver County, Pennsylvania','added':'2026-11-18 23:08'}
