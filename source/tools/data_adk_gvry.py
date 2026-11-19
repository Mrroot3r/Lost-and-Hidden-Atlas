# November 18, 2026: the Champlain shore of Clinton and northern Essex counties, New York (Keeseville, Ausable Chasm,
# Port Kent, Peru, Valcour Island, Plattsburgh, Willsboro, Essex). Drawn at random by tools/choose.py --state ny
# (region adk, which offered Keeseville); start.py found one Atlas place within 20 km of Keeseville and none round
# Plattsburgh. Sources were opened in this session: Wikipedia as raw text (tools/wiki_raw.py); ASCE's landmark page for
# the Bridges of Keeseville; the Champlain Valley National Heritage Partnership's Valcour Island Heritage Trail guide
# (2020, by the Clinton County Historical Association; its GPS waypoints placed the island pins); NYS DEC's Lake
# Champlain Islands Complex page; the CCHA island-events page; the Kent-Delord House, Valcour Brewing, Ausable Chasm,
# Protect the Adirondacks, Passageport (Adsit Cabin), Town of Essex and Lake Champlain Basin Program (Heyworth/Mason Park)
# pages through tools/page.py; a change.org update (June 2021) for the Upper Bridge's closure.
# Every National Register form tried (99001319, 99001322, 99001323, 83001665) came back as the one-page NPGallery
# placeholder and was not read.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'adk_gvry','label':'Champlain shore: Keeseville, Valcour Island, Plattsburgh and Essex','added':'2026-11-18 20:33'}
ASCE=L('ASCE: Bridges of Keeseville (National Historic Civil Engineering Landmark)','https://asce.org/about-civil-engineering/history-and-heritage/historic-landmarks/bridges-of-keeseville')
LCR=L('Lake Champlain Region: Historic Bridges of Keeseville','https://www.lakechamplainregion.com/history/historic-bridges-of-keeseville')
VG=L('Valcour Island Heritage Trail guide (CCHA / Champlain Valley NHP, 2020, PDF)','https://champlainvalleynhp.org/wp-content/uploads/2020/09/Valcour-Guide-2020.pdf')
DEC=L('NYS DEC: Lake Champlain Islands Complex','https://dec.ny.gov/places/lake-champlain-islands-complex')
CCHA=L('Clinton County Historical Association: island events','https://www.clintoncountyhistorical.org/island-events')
VALC_ACC=('Valcour Island is state Forest Preserve (Valcour Island Primitive Area), managed by NYS DEC, reached only by boat; the '
  'nearest launch is the DEC Peru Dock (Valcour) boat launch on US 9, about a mile across the channel. DEC: between Memorial Day '
  'and Labor Day the 29 designated campsites are by permit, given out at the site by the island caretaker. The heritage trail '
  'guide says the trails are open year-round, the full loop is 7.5 miles (4 to 5 hours), and asks visitors to take nothing.')
PLACES=[
# ---- Keeseville ----
N('stone-arch-bridge-keeseville','Stone Arch Bridge (Keystone Arch Bridge)','Keeseville','adk','landmark','standing',44.50528,-73.48111,'exact','public','drive','','1843',
  'A stone arch of about 110 feet over the Ausable River, built by the mason Solomon Townsend and finished in 1843. A spring flood in 1842 undermined the half-built arch and the stone, falsework and fill fell into the river; Townsend started again. It has carried traffic ever since, and with the Upper Bridge and the Swing Bridge it was made a National Historic Civil Engineering Landmark in 1987.',
  'The single arch carrying Main Street over the river, beside the falls the hamlet was first named after (Anderson Falls). The Anderson Falls Heritage House Museum at 98 Clinton Street covers the mill town\'s history (the Peru Gazette gave 2024 hours of Thursday 10 to 2 and Saturday 1 to 3, late May to mid October; current hours not checked).',
  'One of three 19th-century bridges within a half-mile, each built a different way.',
  'A public street bridge carrying Main Street (the ASCE page says it is still in service). Park on the village streets; no mapped lot was found.',
  [W('Stone Arch Bridge (Keeseville, New York)'),W('Bridges of Keeseville'),ASCE,LCR,L('Peru Gazette: Anderson Falls Heritage House Museum (2024)','https://perugazette.com/?p=85493')],brick='no'),
N('swing-bridge-keeseville','Swing Bridge (Ausable River footbridge)','Keeseville','adk','landmark','standing',44.50361,-73.48278,'exact','public','walk','','1888',
  'A pedestrian suspension bridge, called the Swing Bridge because it sways. The Berlin Iron Bridge Company of East Berlin, Connecticut supplied the lattice-braced steel towers, five-strand wire cables and deck for $3,500 in 1888. It replaced earlier suspended footbridges for the mill hands; one of them, hung on forged chains, broke on September 13, 1842 while militiamen marched across, and thirteen people drowned.',
  'A 240-foot (by the regional tourism page) footbridge between the Clinton and Essex county sides of the hamlet, below the stone arch.',
  'Keeseville\'s bridge that swings, built after the one that fell.',
  'A public footbridge (ASCE: in service). Park on the village streets.',
  [W('Swing Bridge (Keeseville, New York)'),ASCE,LCR],brick='no'),
N('upper-bridge-keeseville','Upper Bridge (Double-Span Pratt Truss)','Keeseville','adk','landmark','standing',44.50028,-73.48528,'site','view','drive','','1877–1878',
  'A pin-connected Pratt truss of two 107-foot spans on a mid-river pier, built by Murray, Dougal & Company of Milton, Pennsylvania after a 214-foot covered bridge here collapsed under snow in the winter of 1875. Wikipedia says it was built in 1877 and is the oldest metal Pratt truss in the state; ASCE says it was completed in 1878, for $3,500. It carries Liberty Street (also called River Street or Mill Hill) between the two counties.',
  'An ornamented iron "catalogue bridge" of the 1870s, also called the Old Iron Bridge. Closed since 2008. A petition update of June 2021 said it was still closed and on the state inspection list; whether it has reopened since was not checked.',
  'The rarest of the three Keeseville bridges, and the one that is shut.',
  'Owned by the county or town (not checked which). Closed to traffic since 2008: look at it from the ends or from the river banks, not on it. Park on the village streets.',
  [W('Double-Span Metal Pratt Truss Bridge'),W('Bridges of Keeseville'),ASCE,L('change.org update: Clarification on Upper Bridge inspection (June 2021)','https://www.change.org/p/save-keeseville-s-historic-bridges/u/29177789')],
  conf='mixed',brick='no'),
N('ausable-chasm-bridges','Bridges at Rainbow Falls, Ausable Chasm','Ausable Chasm','adk','landmark','standing',44.52472,-73.46333,'site','public','drive','','1890 (Old State Road Bridge); 1925 or 1932–1933 (US 9 arch)',
  'The US 9 steel arch over the top of Ausable Chasm, with stone-faced concrete approach spans, is on the National Register; Wikipedia dates it 1932–1933, the chasm company 1925 (built by Burr M. Stark), so the year is not settled. Before it, a short-lived railroad from Port Kent to Keeseville (the company calls it the Peanut Railroad) crossed here, and the company says its bridge foundations still show below the road bridge. Upstream, the Old State Road Bridge is a Pratt pony truss of 1890, 107 feet long.',
  'Rainbow Falls from the US 9 bridge, the old railroad bridge foundations below it, and the 1890 pony truss a short way up the river.',
  'Three generations of crossing at the head of the chasm.',
  'The road bridges carry public roads (US 9 and the old state road). The chasm itself is a private attraction (Ausable Chasm Recreation Center) with its own lots on Mace Chasm Road; the falls can be seen from the US 9 sidewalk. Lot fees were not checked.',
  [W('AuSable Chasm Bridge'),W('Old State Road Bridge'),L('Ausable Chasm: Historic Bridges','https://ausablechasm.com/historic-bridges')],
  conf='mixed',th=[44.52557,-73.46031],thn='Ausable Chasm Lot A, Mace Chasm Road',brick='no'),
# ---- Port Kent and Peru ----
N('elkanah-watson-house','Elkanah Watson House','Port Kent','adk','landmark','standing',44.52495,-73.40587,'exact','view','drive','','1828',
  'A square two-storey house of ashlar granite with a hip roof and belvedere, built in 1828 to a design by Sheldon & Merritt for Elkanah Watson (1758–1842), the founder of the agricultural fair, who lived here until he died. It was the centre of his 5,000-acre lakeside estate. It is a National Historic Landmark (1964).',
  'The granite front with its two-storey columned portico, round ground-floor windows and a porte-cochere on the south side, at Lake and South Streets above the lake. A private home: interior not checked and not open.',
  '',
  'Private residence. See it from Lake Street or South Street; do not go onto the grounds.',
  [W('Elkanah Watson House')],brick='no'),
N('heyworth-mason-building-peru','Heyworth–Mason stone mill','Peru','adk','industry','standing',44.57889,-73.52444,'exact','view','walk','','1836',
  'A three-storey sandstone factory of 1836, 35 by 60 feet, on the Little Ausable River. Peru\'s riverbank held a gristmill, tannery, starch factory, woolen mill and cider mill from the 1790s; most were short-lived, but A. Mason & Sons ran a lumber mill on the site from 1883 to 1972. The stone building became apartments in the 1970s and is the survivor the town park is built round.',
  'The stone mill building, seen from Heyworth/Mason Park, where wayside signs tell the site\'s industrial history; the paved Little Ausable River Trail starts at the back of the park. The building is apartments: interior not open.',
  '',
  'The park is the Town of Peru\'s (the Lake Champlain Basin Program wayside sign); park in the small lot on Mason Hill Road. The building itself is private apartments.',
  [W('Heyworth–Mason Industrial Building'),L('Heyworth/Mason Park wayside sign (PDF)','https://lcbp-089519.s3.us-east-2.amazonaws.com/wayside/PDFS/Peru_NY/Heyworth_Mason_Park.pdf')],
  th=[44.57901,-73.52420],thn='Lot on Mason Hill Road',brick='no'),
# ---- Valcour Island ----
N('bluff-point-light','Bluff Point Lighthouse, Valcour Island','Peru','adk','light','standing',44.62279,-73.43124,'exact','boat','boat','','1874',
  'A Victorian lighthouse on a blue limestone base high above the west shore of Valcour Island, built in 1874 after Congress gave $15,000 in 1870. It was dark from 1930, when a steel tower took over, until the Coast Guard lit it again in 2002. The keeper William Herwerth, a disabled Civil War veteran, died on duty in 1881 and his wife Mary kept the light until 1902. DEC has held the deed since 1986; the Clinton County Historical Association runs it as a museum.',
  'The lighthouse, a cistern and a privy (the shed collapsed and was removed), the foundation of the old oil shed behind it, and a wayside exhibit. CCHA ran "Sunday on the Island" open hours from 1 to 3 p.m. on Sundays in July and August 2026, and fall boat trips; interior fabric not checked.',
  'A woman kept this light for 21 years after her husband died in it.',
  VALC_ACC+' Lighthouse open hours are on the CCHA events page (2026: Sundays 1 to 3 p.m., July to late August).',
  [W('Bluff Point Light'),VG,DEC,CCHA],
  th=[44.61917,-73.44532],thn='DEC Peru Dock (Valcour) boat launch, US 9',brick='?'),
N('raboff-camp-valcour','Raboff Great Camp remains, Valcour Island','Peru','adk','landmark','ruins',44.62115,-73.43102,'site','boat','boat','','20th century',
  'Dr. Otto Raboff of Middleboro, Massachusetts held this property south of the lighthouse for almost 30 years before the state bought it. He also gave the historical association a conservation easement for the lighthouse.',
  'Near campsite 25, south of the lighthouse: the remains of a guest house and an ice house, and one of the camp\'s docks beside campsite 26 (under water when the lake is high).',
  '',
  VALC_ACC,[VG,DEC],th=[44.61917,-73.44532],thn='DEC Peru Dock (Valcour) boat launch, US 9',brick='?'),
N('dawn-community-harney-farm-valcour','Dawn Valcour community and Harney Farm foundations','Peru','adk','town','ruins',44.63142,-73.42390,'site','boat','boat','','1874 (Dawn community)',
  'In the summer of 1874 Colonel John Wilcox started the Dawn Valcour Agricultural and Horticultural Association here, a utopian commune built on spiritualism and free love. It had few members, lived in one small room, and failed that fall. The ground later belonged to the Harney family, who farmed about 600 acres on the north end of the island.',
  'A partial foundation of the community\'s building, and nearby the foundations of the Harney farmhouse and barns, a well and a dock, with old farm machinery (a hay baler and a loader) lying about. The guide warns that the well is beside the barn foundations and can be hidden in grass.',
  'A free-love commune that lasted one summer.',
  VALC_ACC,[VG,W('Valcour Island'),DEC],th=[44.61917,-73.44532],thn='DEC Peru Dock (Valcour) boat launch, US 9',brick='?'),
N('hudson-chimney-valcour','Hudson camp chimney and cave, Valcour Island','Peru','adk','landmark','ruins',44.62512,-73.40643,'site','boat','boat','','about 1900',
  'The geologist Dr. George Hudson built a camp here on Paradise Bay about 1900, and used one of the small caves facing the bay as a darkroom; Hudson Hall at SUNY Plattsburgh is named for him. Father Robert Edward Moore later had the largest camp on the east side of the island and preached from his terrace to boaters on Sundays; M. H. "Doc" Yager bought it and sold it to the state.',
  'Only the chimney of about 1900 and an old dock are left. The Hudson Cave can be seen from the dock.',
  '',
  VALC_ACC,[VG,DEC],th=[44.61917,-73.44532],thn='DEC Peru Dock (Valcour) boat launch, US 9',brick='?'),
N('seton-house-valcour','Seton Stone House, Valcour Island','Peru','adk','landmark','standing',44.60877,-73.42299,'exact','boat','boat','','1929',
  'A stone house built in 1929 by the Harvard paleontologist Henry Seton on his 129 acres at the south end of the island. With the lighthouse it is one of only two buildings left on Valcour of the many camps and farms that stood there before the state bought the island.',
  'The empty stone house on the south shore, seen from the perimeter trail. Closed to the public, for safety and against vandalism: interior not open.',
  '',
  VALC_ACC+' The house itself is closed.',
  [VG,DEC],th=[44.61917,-73.44532],thn='DEC Peru Dock (Valcour) boat launch, US 9',brick='no'),
# ---- Plattsburgh ----
N('kent-delord-house','Kent-Delord House Museum','Plattsburgh','adk','landmark','standing',44.70054,-73.44806,'exact','open','drive','','1797',
  'A two-storey wood-frame house of 1797 with a gable roof, a small pedimented entrance porch and brick end chimneys, said to be the oldest house in Plattsburgh. It is a local history museum and has been on the National Register since 1971.',
  'Guided tours of the house (interior fabric not checked). The museum\'s page gives tours Tuesday to Saturday at 11, noon, 1 and 2, $10 for adults and $5 for students.',
  '',
  'Run by the Kent-Delord House Museum, 17 Cumberland Avenue, which sells tours (tours Tuesday to Saturday, 11 a.m. to 2 p.m. starts; read November 18, 2026). Parking not checked; the nearest mapped public-street lot is on Sailly Avenue.',
  [W('Kent-Delord House'),L('Kent-Delord House Museum','https://www.kentdelordhouse.org/')],brick='?'),
N('old-stone-barracks-plattsburgh','Old Stone Barracks','Plattsburgh','adk','fort','standing',44.68084,-73.44473,'exact','open','drive','','1838',
  'The last building of an Army post begun at Plattsburgh in 1838. Of four planned barracks only two were built, an officers\' barracks and this 200-foot, two-storey enlisted men\'s barracks of local limestone; the Air Force tore the officers\' building down in the winter of 1963 (Ulysses S. Grant had once stayed in it). Empty for decades and nearly sold for apartments in 2010, it was bought in 2014 and restored as Valcour Brewing Company, which opened in 2016.',
  'The long limestone barracks. Inside is a brewery, restaurant, event space and inn; the bar top is new (from a Harkness sawmill), and how much original interior survives was not checked.',
  'An 1838 Army barracks you can now drink in.',
  'Privately owned; open to the public as Valcour Brewing Company during its business hours (hours not checked). Parking is in the lots beside the building (the aerial shows them; who may use them was not checked).',
  [W('Old Stone Barracks'),L('Valcour Brewing Company: The Old Stone Barracks','https://valcourbrewingcompany.com/the-old-stone-barracks')],
  brick='no'),
# ---- Essex County ----
N('poke-o-moonshine-fire-tower','Poke-O-Moonshine fire tower and observer\'s cabin','Chesterfield','adk','landmark','standing',44.40167,-73.51306,'site','public','hike','','1917',
  'A prefabricated steel fire tower made by the Aermotor Windmill Company and put up in 1917 on the summit of Poke-O-Moonshine Mountain; it was the first in the state to use an alidade to fix a fire\'s position. The listing also takes in the old jeep trail up the mountain, a spring house and the remains of an observer\'s cabin possibly built by the CCC in 1936.',
  'The tower on the summit (no longer used for fire watch), and on the way up the remains of the observer\'s cabin. The tower\'s exact spot was not checked on the ground.',
  '',
  'Forest Preserve in the Taylor Pond Wild Forest (NYS DEC). The Observer\'s Trail, 2.3 miles each way with blue markers, starts from a parking area on US 9 five miles south of Northway Exit 33 (Protect the Adirondacks).',
  [W('Poke-O-Moonshine Mountain Fire Observation Station'),W('Poke-O-Moonshine Mountain'),L('Protect the Adirondacks: Poke-O-Moonshine Mountain','https://www.protectadks.org/hike-poke-o-moonshine-mountain/')],
  th=[44.38911,-73.50745],thn='Observer\'s Trail parking, US 9',brick='no'),
N('adsit-log-cabin','Adsit Log Cabin','Willsboro','adk','landmark','standing',44.42134,-73.375,'exact','open','drive','','1778 or soon after 1790',
  'A log cabin long said to have been built in 1778 by Samuel Adsit, a Revolutionary War veteran, for his family of sixteen; the town historian\'s records suggest he came to Willsboro Point soon after 1790, so the date is not settled. It survived because a larger house was built round it, later torn down. The town restored it in the 1980s for $70,000.',
  'The log cabin on Point Road, furnished with period pieces and kept by volunteers who explain its history.',
  'One of the oldest log cabins in the country still on its own ground.',
  'Restored by the Town of Willsboro in the 1980s (Wikipedia); who holds title was not checked. Passageport gives it as free, Saturdays and Sundays June to September 10 a.m. to 4 p.m., other times by appointment (the town\'s own page was not found). Parking at the cabin was not checked.',
  [W('Adsit Log Cabin'),L('Passageport: Adsit Cabin','https://passageport.org/places-to-go/adsit-cabin/')],conf='mixed',brick='?'),
N('octagonal-schoolhouse-boquet','Octagonal Schoolhouse, Boquet','Essex','adk','civic','standing',44.30389,-73.40222,'exact','view','drive','','1827–1952',
  'An eight-sided stone school built in 1827 by the mill superintendent Benjamin Gilbert for the mill owner William Ross, who gave money and land, with the mill workers; its walls are of local stone three feet thick. Attendance fell from about 1870 and the school closed in 1952. The Town of Essex looks after it.',
  'The stone octagon with its porch and the shed behind; the town had its window sashes repaired and reglazed in 2024. Whether and when the inside opens was not checked.',
  '',
  'Town of Essex. Seen from the road in the hamlet of Boquet (it stands at the road junction). Opening hours not checked.',
  [W('Octagonal Schoolhouse (Essex, New York)'),L('Town of Essex: Octagonal Schoolhouse maintenance','https://www.essexnewyork.com/octagonal-schoolhouse'),L('ADK Taste: the Essex octagonal school','https://www.adktaste.com/blog/where-in-the-adk-essex-octagonal-school')],
  brick='no'),
N('essex-village-historic-district','Essex village','Essex','adk','town','standing',44.31222,-73.35278,'area','view','walk','','before 1793–1853',
  'Essex was settled from about 1765 as part of William Gilliland\'s planned estate and became a shipbuilding port on Lake Champlain until the railroads came after 1849. Its core is a National Register district of about 150 early 19th-century buildings, none over two and a half storeys: the Dower House (before 1793), Wright\'s Inn (1798), the Essex Free Library (1818), Hickory Hill (1822), Rosslyn (about 1830), the Old Brick Schoolhouse (1830) and Greystone (1853).',
  'A walk down the main street past clapboard, brick and stone houses of the early 1800s. Interiors not checked; most are private.',
  'A lake port that stopped growing in 1849 and kept its houses.',
  'Public streets in the hamlet; most buildings are private. Park on the hamlet streets; no lot was checked.',
  [W('Essex Village Historic District'),W('Essex, New York')],brick='some'),
]
PIN_NOTES={
 'stone-arch-bridge-keeseville':'Wikipedia (National Register) coordinate for the bridge; not moved.',
 'swing-bridge-keeseville':'Wikipedia (National Register) coordinate for the footbridge; not moved.',
 'upper-bridge-keeseville':'Wikipedia (National Register) coordinate; on the aerial it falls on the south-bank road end rather than the truss, so prec is site.',
 'ausable-chasm-bridges':'Wikipedia coordinate for the US 9 arch; the Old State Road Bridge is about 250 m east-southeast (44.52361, -73.46028).',
 'elkanah-watson-house':'Wikipedia coordinate for the house at Lake and South Streets.',
 'heyworth-mason-building-peru':'Wikipedia (National Register) coordinate; parking from tools/parking.py.',
 'bluff-point-light':'OpenStreetMap lighthouse (tools/nom.py), matching the guide waypoint N44 37.367 W73 25.871; boat launch from tools/parking.py.',
 'raboff-camp-valcour':'Heritage trail guide waypoint N44 37.269 W73 25.861 for the Raboff Great Camp.',
 'dawn-community-harney-farm-valcour':'Heritage trail guide waypoint for the Dawn Community House (N44 37.885 W73 25.434), in old fields on the aerial with a small low mound on the LiDAR inside the ring; the Harney farm foundations are close by.',
 'hudson-chimney-valcour':'Heritage trail guide waypoint for the chimney (N44 37.507 W73 24.386); the aerial shows only treetops and the LiDAR nothing distinct, so prec is site.',
 'seton-house-valcour':'OpenStreetMap building named Seton House (tools/nom.py), matching the guide waypoint N44 36.529 W73 25.380.',
 'kent-delord-house':'OpenStreetMap museum at 17 Cumberland Avenue (tools/nom.py); the Wikipedia coordinate is about 450 m west and was not used.',
 'old-stone-barracks-plattsburgh':'Wikipedia (National Register) coordinate, moved 21 m east with tools/pix.py onto the long barracks building seen on the leaf-off aerial.',
 'poke-o-moonshine-fire-tower':'Wikipedia summit coordinate for the mountain (the Register coordinate, 44.38778, -73.50806, is at the trailhead by the road, not the tower).',
 'adsit-log-cabin':'OpenStreetMap museum Adsit Cabin on Point Road (tools/nom.py).',
 'octagonal-schoolhouse-boquet':'Wikipedia (National Register) coordinate.',
 'essex-village-historic-district':'Wikipedia (National Register) coordinate for the district; an area pin.',
}
