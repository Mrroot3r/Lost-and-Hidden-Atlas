# November 23, 2026: a third scatter of places in Wisconsin, away from the lead region (wi_axaz) and from the places wi_plir
# covered: Grant County on the Mississippi (Platteville, Potosi, Cassville), Rock County (Milton, Janesville, Beloit),
# Jefferson County (Aztalan), Kenosha on Lake Michigan, Fond du Lac, Green Bay, Baraboo and the Chippewa River at Cornell.
# Region wi drawn by choose.py --thinnest. Facts come from sources opened in this session: Wikipedia read as raw text
# (tools/wiki_raw.py, including the Register list rows for each county), the Wisconsin DNR page for Aztalan, the Wisconsin
# Historical Society's Stonefield page, and the pages of whoever runs each place (Milton House Museum, Brown County
# Historical Society). Hours for places whose own page could not be opened are as web search results quoted them, and the
# access note says so. Most of these are seasonal and were out of season when read.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]

BATCH={'key':'wi_kzdf','label':'Wisconsin: houses, a brewery and a village site in the south and east','added':'2026-11-23 09:33'}

RK=W('National Register of Historic Places listings in Rock County, Wisconsin')
GT=W('National Register of Historic Places listings in Grant County, Wisconsin')
JF=W('National Register of Historic Places listings in Jefferson County, Wisconsin')
FD=W('National Register of Historic Places listings in Fond du Lac County, Wisconsin')
BR=W('National Register of Historic Places listings in Brown County, Wisconsin')
SK=W('National Register of Historic Places listings in Sauk County, Wisconsin')
CH=W('National Register of Historic Places listings in Chippewa County, Wisconsin')
KE=W('National Register of Historic Places listings in Kenosha County, Wisconsin')

PLACES=[
N('milton-house-milton','Milton House','Milton','wi','landmark','standing',42.77643,-88.93635,'exact','open','walk','','1845',
  'A six-sided inn and stagecoach stop of poured grout (an early concrete), built by Joseph Goodrich, the founder of Milton, at the crossing of two early roads. Goodrich was an abolitionist, and a tunnel from the cellar to a log cabin behind is said to have hidden people escaping slavery. Sojourner Truth stayed here in the 1860s. It is a National Historic Landmark and Wisconsin\'s best-known Underground Railroad site.',
  'The three-storey hexagonal tower with its central spiral stair and a two-storey hexagonal wing, still in their grout walls. Guided tours of about an hour take in two floors of the block and the hexagon, the cellar, the tunnel and the 1837 pioneer cabin behind (the museum\'s tours page). What furnishings are original was not checked.',
  'A concrete inn with a tunnel for people escaping slavery.',
  'Run by the Milton Historical Society as the Milton House Museum, 18 South Janesville Street. Tours must be booked ahead by phone, 608-868-7772; the museum says it keeps a winter and a summer season with different tours. Hours as the museum\'s site gave them in a web search result of November 2026 (its tours page opened but carried no table); admission was quoted two ways, so ask. Park on the street.',
  [W('Milton House (Milton, Wisconsin)'),L('Milton House Museum: tours','https://miltonhouse.org/tours'),RK],
  th=None,brick='no',hours='Winter season Wednesday and Thursday 10 a.m. to 3 p.m., Friday 10 to 2; tours booked ahead'),
N('lincoln-tallman-house-janesville','Lincoln-Tallman House','Janesville','wi','landmark','standing',42.686111,-89.031389,'exact','open','walk','','1857',
  'An Italian villa of cream-coloured brick built in 1857 for the lawyer and abolitionist William Tallman. Abraham Lincoln spent the nights of October 1 to 3, 1859 here when he spoke in Janesville, the only Wisconsin place known to have put him up. The city owns it and the Rock County Historical Society runs it as a museum.',
  'Cream City brick walls, cast-iron window parts and hand-carved black walnut doors outside; Wikipedia says more than 75 percent of the furnishings are original to the house. Shown by guided tour.',
  'Where Lincoln slept in Wisconsin.',
  'City of Janesville, run by the Rock County Historical Society, 440 North Jackson Street. Tickets are sold at the society\'s museum centre at 426 North Jackson Street. A society page (found in a web search, undated) gave tours on the hour from 11 a.m., last at 2 p.m., and a 10 a.m. and 3 p.m. servants\' tour; a tourism listing gave other times, so call 608-756-4509. Its own booking page opened but gave no times. Street parking.',
  [W('Lincoln–Tallman House'),L('Rock County Historical Society: book a tour','https://rchs.us/book-a-tour'),RK],
  brick='no',hours='Tours daily on the hour 11 a.m. to 2 p.m., servants\' tours 10 and 3; undated, call to confirm'),
N('aztalan-state-park','Aztalan','Aztalan','wi','town','traces',43.0665,-88.86042,'site','public','walk','','900–1200s',
  'A village of the Mississippian culture on the Crawfish River, first settled about 900 CE and flourishing between the 10th and 13th centuries. Its people built flat-topped earth mounds and a stockade round their houses. It is a National Historic Landmark. Wikipedia says it was a northern outpost of the culture whose centre was at Cahokia, in Illinois.',
  'Three platform mounds remain on the site and a row of round mounds lies north-west of the stockade; the Wisconsin DNR says parts of the stockade and two of the mounds have been reconstructed in the park, so not everything seen is original.',
  'A Mississippian village with mounds and a stockade.',
  'Aztalan State Park, run by the Wisconsin DNR; a vehicle admission sticker is required (DNR page). The pin is the OpenStreetMap park point; park hours and the lot were not checked. A separate Register listing for the 1830s village of Aztalan lies beside it.',
  [W('Aztalan State Park'),L('Wisconsin DNR: Aztalan State Park','https://dnr.wisconsin.gov/topic/parks/aztalan'),JF],
  brick='no'),
N('stonefield-cassville','Stonefield (Nelson Dewey Homestead)','Cassville','wi','landmark','standing',42.73079,-91.01771,'site','open','walk','','1860s',
  'The estate that Nelson Dewey, Wisconsin\'s first governor, began in the 1860s above the Mississippi. He finished a three-storey Gothic Revival brick house in 1868 but could not enjoy it long, and a fire in 1873 is named in the article. Part of the land is now Nelson Dewey State Park and part is a Wisconsin Historical Society site.',
  'The society\'s site has a rebuilt Dewey house set up as a museum, a farmhouse, an agricultural museum and a village of more than thirty buildings from about 1900, some moved here and some built as replicas (Wikipedia). The Register lists the estate with its original Gothic Revival outbuildings. Which buildings are original was not sorted out.',
  'A governor\'s farm estate over the Mississippi.',
  'Wisconsin Historical Society, 12195 County Road VV. Closed for the winter when read: the society\'s page said it reopens in May 2027. Days and times not checked. A lot is mapped at 42.73118, -91.01795.',
  [W('Stonefield (Wisconsin)'),L('Wisconsin Historical Society: Stonefield','https://stonefield.wisconsinhistory.org/'),GT],
  th=[42.73118,-91.01795],thn='Stonefield Historic Site lot',brick='?',hours='Seasonal; closed for winter, reopens May 2027 (days and times not checked)'),
N('hazelwood-green-bay','Hazelwood Historic House','Green Bay','wi','landmark','standing',44.500833,-88.018889,'exact','open','walk','','1837',
  'A Greek Revival house built in 1837 for Morgan L. Martin, a territorial legislator and later a delegate to Congress, and his bride Elizabeth. Wikipedia says much of his work on the state constitution was done here. The Brown County Historical Society bought it in 1989 and runs it as a museum.',
  'The 1837 house, shown on tours. What survives inside was not checked.',
  'A territorial politician\'s house from 1837.',
  'Brown County Historical Society, 1008 South Monroe Avenue. Tours are by appointment, 920-437-1840; non-members pay $6 (seniors $5, students $4); the society\'s office is open weekdays 8:30 to 4 (its page). A travel listing gave May to August afternoon tours; not confirmed.',
  [W('Hazelwood (Green Bay, Wisconsin)'),L('Brown County Historical Society: admission and hours','https://browncohistoricalsoc.org/visit/admission-hours-location'),BR],
  brick='?',hours='Tours by appointment, 920-437-1840; society office weekdays 8:30 a.m. to 4 p.m.'),
N('cornell-pulpwood-stacker','Cornell Pulpwood Stacker','Cornell','wi','industry','standing',45.16612,-91.15515,'site','public','walk','','1912–1971',
  'A 175-foot steel conveyor set at a 45-degree angle, built in 1912 to pile pulpwood logs at the Cornell Wood Products mill on the Chippewa River; they were then floated to paper mills. It worked until 1971. The National Park Service called it possibly the only remaining structure of its kind. A fire about two decades after it closed destroyed most of the mill buildings.',
  'A rusted double-trussed stacker beside a catwalk, standing in Millyard Park. Condition: it had deteriorated by 1991, and the city has raised money for repairs since. Nothing else of the mill is described as standing.',
  'A 175-foot log conveyor, probably the last of its kind.',
  'Owned by the City of Cornell and kept in Millyard Park. Hours and parking were not checked. The pin is the Wikipedia point; the Register list point is 100 m north.',
  [W('Cornell Pulpwood Stacker'),CH],
  brick='no'),
N('beloit-water-tower','Beloit Water Tower','Beloit','wi','water','standing',42.5091,-89.0305,'exact','public','walk','','1889',
  'An octagonal limestone water tower on a high point of Beloit, built in 1889 for a private water company. Its walls are 36 feet tall and eight feet thick at the base. The cypress tank on top fell in 1914 and a metal one replaced it. In 1929 the city built a steel tower; workmen began to pull this one down but gave up because the walls were so well built.',
  'The stone tower stands in Water Tower Park, which has an accessible walkway; the tank and the inside stairs were removed. The Shingle Style pump house at the foot of the bluff is now a visitor centre.',
  'A water tower too well built to demolish.',
  'In Water Tower Park, a city park (Wikipedia). Hours of the visitor centre not checked. Look from the park; the tower is not entered.',
  [W('Beloit water tower'),RK],
  brick='no'),
N('potosi-brewery','Potosi Brewery and National Brewery Museum','Potosi','wi','industry','standing',42.67672,-90.72562,'exact','open','walk','','1852',
  'A limestone brewery begun in 1852 by Gabriel Hail and John Albrecht and run from 1906 by the Schumacher brothers, at one time the fifth-largest brewer in the country. It made non-alcoholic beer through Prohibition and closed in 1972. A nonprofit foundation restored it for $7.5 million and reopened it in 2008 as a museum and brewpub.',
  'The limestone brewery buildings, with the National Brewery Museum and a brewpub in them. Interior features not checked.',
  'A limestone brewery reopened as a beer museum.',
  'Potosi Foundation, 209 South Main Street, 608-763-4002. Hours as the brewery\'s site was quoted in a web search result of November 2026: closed Monday and Tuesday January to March, Wednesday to Saturday 11 a.m. to 9, Sunday 11 to 6; its own page would not load text. Parking in town.',
  [W('Potosi Brewery'),GT],
  brick='no',hours='Wednesday to Saturday 11 a.m. to 9 p.m., Sunday 11 to 6; closed Mondays and Tuesdays in January to March (as quoted by a search)'),
N('mitchell-rountree-stone-cottage-platteville','Mitchell-Rountree Stone Cottage','Platteville','wi','landmark','standing',42.741389,-90.4825,'exact','open','walk','','1830s',
  'A one-and-a-half-storey cottage of closely fitted dolomite built for the Rev. Samuel Mitchell, a Revolutionary War veteran, in the Virginia style of his birthplace. John Rountree, one of the founders of Platteville and Mitchell\'s son-in-law, probably built it, and the Rountrees lived there for many years. The Grant County Historical Society runs it as a museum.',
  'The stone cottage itself, shown by volunteer guides. Interior not checked. The Register lists it as an early house, but the building date was not given in the sources read.',
  'A Virginia-style stone cottage from Platteville\'s earliest years.',
  'Grant County Historical Society, 460 West Madison Street. Open Saturdays May to October 10 a.m. to 4, otherwise by appointment (the society\'s listing, quoted by search); admission $5 for adults. Call 608-723-4925.',
  [W('Mitchell-Rountree House'),L('Grant County Historical Society: Stone Cottage','https://grantcountyhistory.org/stone-cottage/'),GT],
  brick='no',hours='Saturdays 10 a.m. to 4 p.m., May to October; otherwise by appointment'),
N('kemper-hall-kenosha','Kemper Hall (Kemper Center)','Kenosha','wi','inst','standing',42.57592,-87.81397,'exact','open','walk','','1861',
  'A girls\' boarding school that grew from Senator Charles Durkee\'s 1861 Italianate mansion on Lake Michigan. The Episcopal church made the house a school in 1871, and the Sisters of St. Mary ran it from 1878; Gothic Revival wings, a chapel (1875), an observatory and dormitories were added. The school closed in 1975 and a preservation group gave the buildings to Kenosha County.',
  'The mansion, chapel, Griffin Observatory and later wings stand together on 17.5 acres by the lake as the Kemper Center. Interior not checked.',
  'A convent school grown from a senator\'s mansion.',
  'Kenosha County\'s Kemper Center, 6501 Third Avenue. The Durkee Mansion is open for free self-guided tours 1:30 to 4:30 p.m. on the first and third weekends of the month, the centre otherwise by appointment (its site, as a web search quoted it; call 262-925-8040).',
  [W('Kemper Hall'),L('Kemper Center','https://kempercenter.com/visit/durkee-mansion'),KE],
  brick='?',hours='Durkee Mansion 1:30 to 4:30 p.m. first and third weekends; other times by appointment'),
N('ringlingville-baraboo','Ringling Brothers winter quarters (Ringlingville)','Baraboo','wi','industry','standing',43.46564,-89.73446,'site','open','walk','','1884–1918',
  'The winter quarters of the Ringling Brothers Circus from 1884, when it began touring from Baraboo, until 1918, just before it joined Barnum and Bailey. The site is a National Historic Landmark, and the Wisconsin Historical Society owns it as the Circus World Museum.',
  'Ringlingville holds the surviving original buildings, among them the Ring Barn, Elephant House, Animal House, Baggage Horse Barn, Winter Quarters Office and Wardrobe Department; the museum sits on eight of the ten remaining Ringling buildings (Wikipedia).',
  'The barns where the Ringlings\' circus wintered.',
  'Circus World, 550 Water Street, run by the Circus World Museum Foundation for the Wisconsin Historical Society. The 2026 Big Top season ran May 15 to September 6, closed Tuesdays; winter openings are on a few weekends only (a search result of November 2026). Check circusworld.wisconsinhistory.org.',
  [W('Circus World Museum'),L('Circus World','https://circusworld.wisconsinhistory.org/explore'),SK],
  brick='?',hours='Summer season May to early September, closed Tuesdays; a few weekends in winter (check its site)'),
N('galloway-house-fond-du-lac','Galloway House and Village','Fond du Lac','wi','landmark','standing',43.754722,-88.435278,'exact','open','walk','','1846',
  'An Italianate mansion with a three-storey tower, begun in 1846 by Selim Newton and enlarged between 1868 and 1880 by Edwin H. Galloway, who dealt in lumber and real estate. It now stands with a museum village of moved buildings run by the Fond du Lac County Historical Society.',
  'The Galloway mansion. Which buildings in the village are original and what survives inside were not checked.',
  'A lumberman\'s Italianate mansion with a moved village.',
  'Fond du Lac County Historical Society, 336 Old Pioneer Road, 920-922-1166. Seasonal: the society\'s 2025 listing was Friday to Sunday 11 a.m. to 3, closed for winter when read; 2026 hours were not found.',
  [L('Register list for Fond du Lac County','https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Fond_du_Lac_County,_Wisconsin'),L('Fond du Lac County Historical Society','https://www.fdlhistory.org/')],
  conf='mixed',brick='?',hours='Seasonal, closed for winter; 2025 season Friday to Sunday 11 a.m. to 3 p.m.'),
]

PIN_NOTES={
 'milton-house-milton':'OpenStreetMap point for the Milton House Museum (nom.py), 10 m from the Register point.',
 'lincoln-tallman-house-janesville':'Register list point; on the aerial the pin sits on a building of the right size.',
 'aztalan-state-park':'OpenStreetMap park point (nom.py); the Register point is 160 m north-west. The mounds and stockade lie within the park, so site precision.',
 'stonefield-cassville':'Moved with pix.py 340 m from the Register list point, which falls on a road in woods, onto the cluster of buildings the aerial shows by the historic site\'s lot; the lot is the OpenStreetMap parking point.',
 'hazelwood-green-bay':'Register list point for Hazelwood; on the aerial the pin sits on a building of the right size.',
 'cornell-pulpwood-stacker':'Wikipedia point for the stacker; the Register list point is about 100 m north.',
 'beloit-water-tower':'Wikipedia point for the water tower; on the aerial the pin sits on a building of the right size.',
 'potosi-brewery':'OpenStreetMap point for the brewery (nom.py), 10 m from the Register point.',
 'mitchell-rountree-stone-cottage-platteville':'Wikipedia and Register list point; on the aerial the pin sits on a building of the right size.',
 'kemper-hall-kenosha':'OpenStreetMap building point for the Kemper Center (nom.py), 80 m from the Register point.',
 'ringlingville-baraboo':'Moved with pix.py about 300 m from the Register list point, which falls on downtown streets, onto the group of buildings south of the river on the Circus World grounds (the museum\'s OpenStreetMap points are 100 to 200 m away); which of them are the original Ringling barns was not settled.',
 'galloway-house-fond-du-lac':'Register list point for the Galloway House; on the aerial the pin sits on a building of the right size.',
}
