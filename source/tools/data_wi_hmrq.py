# November 24, 2026: a fourth scatter of places in Wisconsin, in counties the first three batches did not touch:
# Manitowoc on Lake Michigan, Portage (Nelsonville), Eau Claire (Augusta), Wood (Marshfield), Oconto
# (Lakewood), Green Lake (Green Lake), Waukesha (Delafield) and the Apostle Islands off Bayfield.
# Region wi drawn by choose.py --thinnest. Facts come from sources opened in this session: the Register county lists
# (wiki_raw.py --rows), the National Register nomination forms on NPGallery (page.py), the Wisconsin DNR, National Park
# Service, Oconto County Historical Society, Wisconsin Historical Society and dellsmill.com pages, and Wikipedia.
# Hours that only a web search result quoted are said to be so in the access note. Most places are private or seasonal.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]

BATCH={'key':'wi_hmrq','label':'Wisconsin: mills, barns, a logging camp and a lighthouse in counties not yet covered','added':'2026-11-24 08:35'}

MA=W('National Register of Historic Places listings in Manitowoc County, Wisconsin')
SB=W('National Register of Historic Places listings in Sheboygan County, Wisconsin')
PT=W('National Register of Historic Places listings in Portage County, Wisconsin')
EC=W('National Register of Historic Places listings in Eau Claire County, Wisconsin')
AS=W('National Register of Historic Places listings in Ashland County, Wisconsin')
OC=W('National Register of Historic Places listings in Oconto County, Wisconsin')
WD=W('National Register of Historic Places listings in Wood County, Wisconsin')
WK=W('National Register of Historic Places listings in Waukesha County, Wisconsin')
def NR(n): return L('National Register nomination form (National Park Service)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/%s_text'%n)

PLACES=[
N('rock-mill-maribel','Rock Mill','Maribel','wi','industry','standing',44.29946,-87.77530,'area','view','drive','','1847',
  'A wooden mill on the Devil\'s River, built in 1847 as a sawmill and changed into a gristmill in the 1850s. It stood beside the old military road between Fort Dearborn and Fort Howard. Emil Schlegelmilch bought it in 1878 and ran it until his death in 1934, the year the river\'s dam was destroyed. A later owner restored it from 1975.',
  'A two-and-a-half-storey frame mill on a limestone foundation with a tin roof, a sixteen-foot overshot wheel put in during the 1976 restoration, and, the 1982 nomination says, the only original grinding machinery left in the county. The mill race and tail race can be seen, and the remains of the 1915 dam lie about 500 feet to the north-west. Interior not checked for this entry.',
  'A restored 1847 frame mill with its grinding machinery.',
  'Privately owned (Travel Wisconsin lists it as private). Whether tours run now is not checked; look from the road and ask the owner before going in. The mill stands beside a campground and a county park lies near it, so do not assume either is the mill\'s own ground.',
  [W('Rock Mill (Maribel, Wisconsin)'),NR('82000680'),L('Travel Wisconsin: Old Rock Mill','https://www.travelwisconsin.com/things-to-do/culture-arts/museums-history/old-rock-mill'),MA],conf='mixed',brick='no',hours='?'),
N('lutze-housebarn-newton','Lutze Housebarn','Newton','wi','landmark','standing',43.93306,-87.78278,'site','view','drive','','1850',
  'A German "housebarn" built in 1850 by immigrants: one long building with the family\'s rooms at the east end and the cattle stable at the west, under one roof. Its older part was framed in fachwerk, hewn oak timbers pegged together. The nomination form calls it one of the best surviving examples in the country of a house-and-barn form that is far older than Wisconsin.',
  'The long timber-framed building on a farmstead that also has an 1896 brick farmhouse and a newer barn. Inside, the form describes a clay-brick chimney in the attic and hand-forged hooks in a thick-walled arched cellar. Whether visitors may go in is not stated in any source read: look from the public road only.',
  'A German house and cow barn under one roof, 1850.',
  'Private farmstead; the form lists a private owner. No visiting hours found. Look from the road; do not enter the yard. The Register point may not sit on the building and was not matched to a visible building when this was written.',
  [NR('84003702'),MA],conf='mixed',brick='?'),
N('rawley-point-light','Rawley Point Light','Two Rivers','wi','light','standing',44.21078,-87.50878,'exact','public','walk','','1873–1894',
  'Wisconsin\'s tallest lighthouse, 111 feet, at the tip of Rawley Point in Point Beach State Forest. A light was shown here from 1853; the present keeper\'s house dates from 1873. The skeletal tower was taken from the old Chicago Harbor Light and re-erected here and first lit on November 20, 1894. Before the new light was built 26 ships had been wrecked or stranded on the point.',
  'A black iron skeletal tower beside a Victorian keeper\'s house and a round oil house (built 1893, per Wikipedia). It can be seen and photographed from the beach and dunes. The Coast Guard still runs the light and the keeper\'s house is used as a rest house for military families, so there are no inside tours.',
  'The tallest lighthouse on the Wisconsin shore.',
  'Point Beach State Forest (Wisconsin DNR). A state park vehicle admission sticker is needed to drive in; park in the forest and walk to the beach. Look from the beach: the light station grounds are the Coast Guard\'s. The DNR page says the light "may be viewed and photographed from the beach"; the no-tours detail comes from a web search result.',
  [W('Rawley Point Light'),L('Wisconsin DNR: Rawley Point Lighthouse','https://dnr.wisconsin.gov/topic/parks/pointbeach/lighthouse'),MA],brick='some',th=[44.21219,-87.50790],thn='Sandy Bay Road parking lot, Point Beach State Forest'),


N('rising-star-mill-nelsonville','Rising Star Mill','Nelsonville','wi','industry','standing',44.49411,-89.31086,'exact','view','drive','','1868',
  'A wooden gristmill on the Waupaca River built by Jerome Nelson in 1868 (the Historical Society\'s older page gives 1855, which is the date of his dam and sawmill). It ground winter wheat for logging camps and farms, worked as a business until 1984, then became a museum of the Portage County Historical Society. Listed on the National Register in 2018.',
  'The mill beside the dam on the west bank, with much of its old machinery. The society holds a summer concert series, an art show and an open house here; no indoor plumbing and no wheelchair access. Interior not checked for this entry.',
  'A mill turned concert hall: the Music at the Mill series.',
  'Owned by the Portage County Historical Society. No regular public hours were found: a search result says groups can arrange visits through the society (pchswi.org) and that open days are events. Check the society\'s page before going.',
  [NR('100002444'),L('Portage County Historical Society','https://www.pchswi.org'),PT],conf='mixed',brick='no',hours='?'),
N('dells-mill-augusta','Dells Mill','Augusta','wi','industry','standing',44.72556,-91.14833,'exact','open','drive','','1864–1867',
  'A five-level gristmill on Bridge Creek, built in the mid-1860s and opened in 1867 when wheat farming was spreading across north-western Wisconsin. It worked until 1968 and then became a museum. Listed on the National Register in 1974.',
  'A hand-hewn maple frame joined with wooden pegs, clad in clapboard, with a two-storey wing added in 1904 and lean-tos of 1940. Some of the original machinery remains, including the power turbine and the wooden cogged wheel, and the 1974 form says they were still in use. Part of the building stands over the water on later concrete columns. The mill\'s own page says it still grinds for local farmers now and then, and shows flour and Amish goods.',
  'Wisconsin\'s most photographed mill, still grinding.',
  'Run as a museum (dellsmill.com, E18855 County Road V). Hours below are from that page; a 2015 listing warned that the museum\'s future was uncertain, so telephone first on (715) 286-2714 (a listing\'s number, not checked).',
  [W('Dells Mill'),NR('74000086'),L('The Dells Mill and Museum','https://www.dellsmill.com'),L('Wisconsin Historical Society: Dells Mill','https://www.wisconsinhistory.org/Records/Property/HI16146'),EC],brick='no',hours='Summer: Fridays and Saturdays, usually 9 a.m. to 5 p.m.; no Sunday hours'),
N('basswood-island-quarry','Basswood Island brownstone quarry','La Pointe','wi','industry','ruins',46.83222,-90.75556,'site','boat','boat','','1868–1893',
  'A sandstone quarry on the southern end of Basswood Island, worked by the Bass Island Brownstone Company from 1868 to the early 1890s. Its brownstone first went into the second Milwaukee County Courthouse and later the old Chicago Tribune building and two Milwaukee churches. The quarry pit is about 200 feet long and 25 feet deep and is now full of water.',
  'Large blocks of cut brownstone lie in and around the pit and rusting machinery remains; the company\'s buildings and workers\' cabins are gone. The Park Service describes a 5.5-mile loop trail from the island dock that passes the McCloud-Brigham farm site and then reaches overlooks of the main quarry.',
  'A flooded Lake Superior brownstone quarry on an island.',
  'Apostle Islands National Lakeshore (National Park Service). There is no road: reach the island by boat (water taxi or your own) and land at the dock; camping permits come from the Bayfield visitor center. Take only pictures: the blocks are part of a listed site.',
  [W('Bass Island Brownstone Company Quarry'),NR('78000075'),L('National Park Service: Basswood Island','https://www.nps.gov/apis/planyourvisit/basswood-island.htm'),AS],brick='no'),
N('holt-balcom-logging-camp-lakewood','Holt and Balcom Logging Camp No. 1','Lakewood','wi','industry','standing',45.29833,-88.49556,'exact','open','drive','','1880',
  'A log camp built in 1880 at the height of the white-pine logging era, with a cookhouse and a bunkhouse. The Register list says it may be the oldest logging camp in the United States still on its original site. The Oconto County Historical Society deeded it in 1976 to the McCauslin Lions Club on the condition that it be restored and kept open to the public.',
  'Log buildings with the cook shack table set with blue porcelain tableware, a massive cast-iron stove, and bunks, a hollowed-log wash basin and a stove in the bunkhouse (the 1978 nomination). The old supply road survives as a winding trace beside the brook.',
  'The oldest logging camp still on its original site, perhaps.',
  'On the grounds of McCauslin Brook Golf Club, 17067 Club House Lane, Lakewood. Free. Open Saturdays in summer (Oconto County Historical Society page); special tours by arrangement on (920) 629-0870. Closed for the winter when this was written.',
  [W('Holt and Balcom Logging Camp No. 1'),NR('78000121'),L('Oconto County Historical Society: Holt & Balcom Logging Camp','https://ocontohistory.org/plan-your-visit/historic-and-archaeological-sites-of-oconto-county/holt-balcom-logging-camp/'),OC],brick='no',hours='Saturdays 10 a.m. to 3 p.m., Memorial Day to Labor Day; tours by arrangement'),

N('central-wisconsin-state-fair-round-barn','Central Wisconsin State Fair Round Barn','Marshfield','wi','landmark','standing',44.65222,-90.17417,'exact','view','drive','','1915–1916',
  'A huge red circular show-and-sale barn built in 1915 and 1916 by local builder Frank Felhofer as the focal point of the fairgrounds. It is 150 feet across in two tiers and about 70 feet tall, and it covers over a third of an acre. Marshfield bills it as the world\'s largest round barn; that is the town\'s own claim. Listed on the National Register in 1997.',
  'Horizontal tongue-and-groove siding painted bright red with white trim, 28 windows on each tier, and an open show ring in the middle that once had bleachers for about 1,000. It is still used each year during the Central Wisconsin State Fair for livestock shows and sales. Interior open only on event days, not checked.',
  'A 150-foot round barn.',
  'In the south-west corner of the Wood County fairgrounds (Vine Avenue and East 17th Street), which are owned by the fair association. It is usually visible from the street; the grounds are open for events. No regular visiting hours found.',
  [W('World\'s Largest Round Barn'),NR('97000269'),WD],brick='no'),
N('wakeleys-tavern-nekoosa','Wakeley\'s Tavern (Historic Point Basse)','Nekoosa','wi','hotel','standing',44.29944,-89.89083,'site','open','drive','','1837',
  'A two-storey frame tavern built in 1837 by Robert and Mary Wakeley of Lake George, New York, who were stopped by rapids on the Wisconsin River and saw that other travellers would be too. The Register list calls it the oldest building in Wood County. A cable ferry ran from the inn across the river from the 1870s to 1916. Beside it stood the village of Pointe Basse, which became a ghost town in the 1870s when the railroad went through Nekoosa.',
  'A simple frame house, 20 by 30 feet, from which later Victorian porches were removed to bring it back toward its original look. The nonprofit Historic Point Basse has also restored a trading post, a blacksmith shop and a schoolhouse on the site. Interior not checked.',
  'The oldest building in Wood County.',
  'Historic Point Basse, 364 Wakely Road, Nekoosa, run by volunteers. Its own page says it is open during scheduled events and classes through the year, admission free at the events it lists; check its schedule before going. The Register list gives the older spelling Wakeley, the society Wakely.',
  [NR('74000146'),L('Historic Point Basse - Wakely Historical Site','https://historicpointbasse.com'),WD],conf='mixed',brick='no',hours='Open during scheduled events and classes through the year; see its schedule'),
N('thrasher-opera-house-green-lake','Thrasher Opera House','Green Lake','wi','amuse','standing',43.8447,-88.9599,'exact','open','walk','','1909–1910',
  'A small-town theatre built in 1909 for Charles Thrasher by D. W. Taylor (the Register list; the house\'s own page says 1910). It had vaudeville, films, basketball, dances and school plays, was turned into a factory and warehouse after World War II, and was restored from 1996 as a theatre again.',
  'A wooden building on a fieldstone basement with its original window glass (the frames were rebuilt to match in 1996). It is used for concerts, comedy and plays. Whether it can be seen inside outside show times is not checked.',
  'A restored 1909 opera house on the main street.',
  '506 Mill Street, Green Lake. It is open for shows; one search result mentions a tour as part of a 2025 event. No regular tour hours found: see its page for what is on.',
  [NR('99000921'),L('Thrasher Opera House','https://www.thrasheroperahouse.com'),W('National Register of Historic Places listings in Green Lake County, Wisconsin')],conf='mixed',brick='no',hours='Open for shows; see its page for dates'),
N('delafield-fish-hatchery','Delafield Fish Hatchery','Delafield','wi','industry','standing',43.06111,-88.40722,'exact','public','walk','','1907–1953',
  'The state\'s fish hatchery, where walleye and bass fry were raised to stock lakes and streams from 1907 until 1950 (the Historical Society says it was used until 1953, when it became a research centre). Only one of the six ponds survives.',
  'The 1907 Tudor Revival administration and walleye-tank building, with contrasting glazed brick on its upper and lower walls, stands in a park by the Bark River. The nomination form says its original tile roof was replaced and its openings covered; the building is now rented out for events through the city. Interior not checked.',
  'A Tudor Revival fish hatchery in a city park.',
  'Fish Hatchery Park, owned by the City of Delafield (the 1981 form lists the city; the park is at 425 Main Street). Park hours not found. Look at it from the park grounds.',
  [NR('81000064'),L('Wisconsin Historical Society: Delafield Fish Hatchery','https://www.wisconsinhistory.org/Records/Article/CS6988'),WK],conf='mixed',brick='?'),
]

PIN_NOTES={
'wakeleys-tavern-nekoosa':'The Register list point; checked against the aerial.',
'thrasher-opera-house-green-lake':'The Register list point; checked against the aerial.',
'rock-mill-maribel':'OpenStreetMap\'s point for the mill\'s roadside historical marker on County Road R. Trees hide the mill on the aerial, so the pin marks the area.',
'lutze-housebarn-newton':'The Register list point; checked against the aerial before publishing.',
'rawley-point-light':'Wikipedia and Register point for the tower; checked against the aerial.',
'rising-star-mill-nelsonville':'OpenStreetMap\'s point for the museum, on the building beside the river bridge on the aerial.',
'dells-mill-augusta':'Wikipedia and Register point; checked against the aerial.',
'basswood-island-quarry':'The Register and Wikipedia point at the quarry on the island\'s south end; checked on the aerial and the bare-ground LiDAR.',
'holt-balcom-logging-camp-lakewood':'The Register list point; checked against the aerial.',
'central-wisconsin-state-fair-round-barn':'The Register list point; checked against the aerial.',
'delafield-fish-hatchery':'The Register list point; checked against the aerial.',
}
