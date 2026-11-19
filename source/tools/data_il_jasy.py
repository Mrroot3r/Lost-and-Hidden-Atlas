# November 18, 2026: the Illinois side of the Mississippi above St. Louis: Elsah, Grafton and Pere Marquette State Park
# in Jersey County, Alton and Godfrey, Edwardsville, the Chain of Rocks, and Kampsville up the Illinois River.
# Region il drawn at random by choose.py; the ground inside it was picked by a random draw among six towns (Elsah).
# Facts come only from sources opened in this session: Wikipedia read as raw text (tools/wiki_raw.py), HMdb.org marker
# texts (read with tools/page.py), the Illinois DNR park and lodge pages, the National Park Service's Route 66 page,
# Principia College's campus page, the Stephenson House's own visit page, historic-leclaire.org, the SIUE Madison
# Historical encyclopedia, the Village of Godfrey's parks page and the Great Rivers & Routes tourism bureau listings.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
HM=lambda n,t: ['HMdb: '+t,'https://www.hmdb.org/m.asp?m=%d'%n]
GRR='Great Rivers & Routes tourism bureau'
PMSP=L('Illinois DNR: Pere Marquette State Park','https://dnr.illinois.gov/parks/park.peremarquette.html')

PLACES=[
N('elsah-historic-district','Elsah village','Elsah','il','town','standing',38.95465,-90.36131,'site','view','walk','','1853–1861',
  'James Semple founded Elsah on the Mississippi in 1853 and gave free lots to anyone who built with stone from his quarry. By 1861 the village had reached the size it still is: hemmed in by the bluffs, and passed by when the railroad came, it stopped growing. It was the shipping point for Jersey County farm produce until then, and Principia College revived it from the 1930s. The whole village was put on the National Register in 1973.',
  'Forty-eight contributing buildings from the 1850s growth: the commercial blocks of LaSalle Street, three blocks in from the river, are mostly stone, and every pre-1861 building there but one still stands, all four old taverns among them; Mill Street has stone and brick houses and a block of Greek Revival homes. The houses are private and not open, except on the annual house tour in December. The Village of Elsah Museum on LaSalle Street sells the historic guidebook with a walking tour.',
  'A whole river village frozen at its 1861 size.',
  'Public streets; the houses are private homes and are seen from the street (greatriverroad.com, which also says the village is "not a museum village"). The Village of Elsah Museum at 26 LaSalle Street is listed as open Fridays to Sundays, 1 to 4 pm, April to October, on greatriverroad.com; the village\'s own page was not opened, so take those hours as not checked. Park in the small lots on Mill Street, Maple Street or LaSalle Street.',
  [W('Elsah Historic District'),W('Elsah, Illinois'),L('Great River Road: visitors guide to Elsah','https://www.greatriverroad.com/elsah')],brick='some'),

N('elsah-ice-house-ruin','Elsah ice house ruin','Elsah','il','industry','ruins',38.95263,-90.36205,'site','view','walk','','mid-1800s–',
  'A stone building put up in the middle 1800s of limestone quarried from the bluffs. It began as a private home and a meeting place for the village; Christian Loehr bought it in 1873 from the Elsah Building and Manufacturing Company, and it was later turned into an ice house for blocks cut from the frozen Mississippi. Elsah once had five ice houses.',
  'The stone walls of the ruin at the corner of Mill Street and Elm Street, beside an HMdb-listed marker ("The Ice House") with an old photograph of men cutting river ice by hand. Who owns the ruin was not checked.',
  'One of five ice houses in a village of 500.',
  'Seen from Mill Street, a public street, by the marker; owner not checked, so stay on the street. A small mapped lot on Mill Street is a few metres north.',
  [HM(216141,'The Ice House (Elsah)')],conf='mixed',brick='no'),

N('principia-college-maybeck','Principia College: the Maybeck campus','Elsah','il','inst','standing',38.9503,-90.3503,'area','open','drive','','1930s–',
  'Principia, a college for Christian Scientists founded by Mary Kimball Morgan, moved to the bluffs above Elsah in the 1930s. Bernard Maybeck, the California architect, designed the new campus, giving each of the first dormitories a different style and building method and trying them out first on a small test building the students still call the Mistake House; he also designed the chapel. Part of the campus became a National Historic Landmark district in 1993.',
  'The Maybeck chapel, the dormitories such as Buck House, and the Mistake House, on a self-guided driving tour with signs: the gatehouse gives out a map with the route marked (Great Rivers & Routes). Maybeck architectural tours can be arranged with the college. Which interiors visitors may enter on their own was not checked.',
  'An Arts and Crafts architect\'s campus on a Mississippi bluff.',
  'Private college with a staffed entrance. Its campus page says the campus is open to the public for visits and tours Monday to Saturday, 10 a.m. to sunset; guided tours through the President\'s office, (618) 374-5148. Check in at the gatehouse. Pin is the middle of the Register district from the Wikipedia list, not a building.',
  [W('Principia College'),L('Principia College: campus and location','https://www.principiacollege.edu/about/campus-and-location'),L(GRR+': exploring Principia College','https://www.riversandroutes.com/blog/top-reasons-to-explore-principia-college/')],brick='?',hours="Campus open for visits Monday to Saturday, 10 a.m. to sunset; guided tours through the President's office, (618) 374-5148"),

N('pere-marquette-lodge','Pere Marquette State Park Lodge','Grafton','il','hotel','standing',38.97176,-90.54115,'exact','open','drive','','1930s–',
  'The Civilian Conservation Corps built the lodge of Pere Marquette State Park, at the meeting of the Illinois and Mississippi rivers, in the 1930s. It was enlarged in 1985 and is still a working lodge run within the state park. The lodge and its cabins were listed on the National Register in 1985.',
  'The CCC\'s native limestone and heavy timbers in the original part, and in the Great Room a 50-foot vaulted roof and a stone fireplace said to weigh 700 tons (Illinois DNR). Stone guest cabins stand nearby. The lobby is open to lodge visitors; opening hours of the public rooms were not checked.',
  'A 700-ton CCC fireplace.',
  'Illinois DNR state park; the lodge is a hotel and conference centre within it. The park\'s visitor center winter hours are Monday to Saturday 8:00 am to 3:30 pm, closed Sundays (IDNR page read November 18, 2026); park gate hours not checked. Parking at the lodge on Lodge Boulevard off Illinois Route 100.',
  [W('Pere Marquette State Park'),PMSP,L('Illinois DNR: Pere Marquette Lodge','https://dnr.illinois.gov/parks/lodge/park.peremarquette.html')],th=[38.97129,-90.54000],thn='Lodge lot, Lodge Boulevard',brick='no',hours='Park visitor center in winter: Monday to Saturday 8:00 a.m. to 3:30 p.m., closed Sundays; park gate hours not checked'),

N('smith-duncan-house-eastman-barn','Smith-Duncan House and Eastman Barn','Grafton','il','landmark','standing',38.9692,-90.5119,'area','view','drive','','c. 1861–',
  'A two-storey limestone farmhouse of about 1861 and a stone-founded barn on the Duncan farmstead, now inside Pere Marquette State Park. Limestone was the common building stone round Grafton in the mid-1800s, and the Register (1999) took them as well-kept examples of it, with two stone retaining walls.',
  'The house, two rooms deep with a central hall, and the barn with three sections over a raised limestone basement for livestock and a gabled cupola on the roof. Interior not checked; no source says either is open.',
  '',
  'Within Pere Marquette State Park (Illinois DNR), on the Duncan farmstead south of Route 100 according to Wikipedia. No IDNR page about the buildings was found, so whether you may walk up to them was not checked: view them from the road. A mapped lot on the Sam Vadalabene Bike Trail is about 600 m east.',
  [W('Smith-Duncan House and Eastman Barn'),PMSP],conf='mixed',th=[38.96924,-90.50479],thn='Bike trail lot, Route 100',brick='no'),

N('grafton-historic-district','Grafton Main Street, ice house and stone wharf','Grafton','il','town','standing',38.9692,-90.4378,'area','public','walk','','1836–1925',
  'Grafton was founded in 1832 by the brothers James and Paris Mason and platted by Paris and James\'s widow Sarah; it is the oldest permanent settlement in Jersey County. Its limestone went into St. Louis buildings, and the 1844 flood destroyed the low town and its first wharf. The historic district (1994) takes in two blocks of Main Street and Maple Street down to the river.',
  'Houses built from 1836 to 1925 along Main Street (Route 100), Queen Anne and Italianate among them; the Grafton Ice House of about 1840, the one building left from the town\'s trade in river ice; and the limestone wharf of 1846, the town\'s second, on the Mississippi at the foot of Maple Street. The houses are private.',
  'A river town\'s last ice house and its 1846 stone wharf.',
  'Public streets and riverfront; the houses are private. Street parking and a mapped lot on Water Street by the river. Pin is the middle of the district from the Wikipedia list; the ice house and wharf were not located on the aerial.',
  [W('Grafton Historic District (Grafton, Illinois)'),HM(210702,'Grafton'),L(GRR+': a walk through Grafton\'s past','https://www.riversandroutes.com/blog/take-a-walk-through-graftons-past/')],th=[38.96925,-90.43922],thn='Water Street lot',brick='?'),

N('ruebel-hotel-grafton','Ruebel Hotel','Grafton','il','hotel','standing',38.96972,-90.43222,'site','open','drive','','1913–',
  'The first Ruebel Hotel was built in 1879 and burned in 1912; this one went up in its place in 1913, with a saloon and a restaurant, and was counted one of the best in Jersey County. It is the only hotel left of Grafton\'s old ones and still takes guests.',
  'A two-storey red brick Commercial-style front (Wikipedia photograph) of decorative brickwork: corbelled brick at the cornice and raised brick panels over arched second-floor windows. Interior not checked.',
  '',
  'A working hotel at 207–215 East Main Street (Route 100); the tourism bureau lists it among places to stay. Street parking; a mapped lot is about 100 m west on East Main Street.',
  [W('Ruebel Hotel'),L(GRR+': a walk through Grafton\'s past','https://www.riversandroutes.com/blog/take-a-walk-through-graftons-past/')],brick='yes'),

N('jersey-county-courthouse','Jersey County Courthouse','Jerseyville','il','civic','standing',39.11889,-90.32889,'exact','view','drive','','1893–1894',
  'The county\'s third courthouse, built in 1893–94 to a Romanesque Revival design by Henry Elliott of Chicago and Jacksonville. Its tower stands 124 feet tall. The limestone came from the quarries at Grafton.',
  'The Grafton limestone front, richly carved, with a tall central tower and octagonal cupola, towers at the front corners and a raised porch. Still the courthouse; interior not checked.',
  '',
  'A working county courthouse at 201 West Pearl Street; seen freely from the street. Opening hours not checked. Mapped lots on North Lafayette Street and around the square.',
  [W('Jersey County Courthouse')],brick='no'),

N('alton-prison-ruins','Alton Penitentiary and Military Prison wall','Alton','il','inst','ruins',38.89138,-90.18956,'exact','public','drive','','1833–1865',
  'Illinois\'s first state penitentiary, built with public money on land given by William Russell. An older roadside marker says it was built in 1830–31; Wikipedia and the Looking for Lincoln site say it opened in 1833. It was replaced by Joliet and emptied by 1860, then reopened in 1862 as a Union prison for Confederate soldiers and civilians: more than 11,000 passed through and about 1,500 died, many of smallpox. It closed in July 1865 and was pulled down over the next twenty years.',
  'One piece of a stone cell block wall, with interpretive markers round it. It is not where it stood: the remnant was moved here in 1970 when the old site was paved as a parking lot. Stone from the prison is built into walls all over Alton.',
  'All that is left of a Civil War prison, moved across the road.',
  'Kept by the State of Illinois as a historic site (Wikipedia), on William Street just north of West Broadway (Route 100). Hours not checked. A mapped lot is on William Street beside it.',
  [W('Alton Military Prison'),HM(211807,'After the War'),HM(144762,'Ruins of First State Prison in Illinois'),HM(211622,'The First Illinois State Penitentiary'),L('Looking for Lincoln: Alton Prison','https://www.lookingforlincoln.org/explore/sites/326')],conf='mixed',th=[38.89165,-90.19030],thn='William Street lot',brick='no'),

N('mcpike-mansion','McPike Mansion (Mount Lookout)','Alton','il','landmark','standing',38.90583,-90.18333,'area','open','drive','','1869–',
  'Henry Guest McPike, mayor of Alton, box maker and prize-winning grape grower, began this house in 1869 on Mount Lookout, one of the highest points in town; Lucas Pfeiffenberger was the architect. A later owner rented out rooms until his death (Wikipedia gives 1945 or 1951). Empty for years after, it was stripped by vandals of its banisters and fittings and nearly cleared for a shopping centre; it was listed on the Register in 1980. Its present owners are restoring it with money from historic and ghost tours.',
  'The red brick house with its mansard roof and columned porch (Wikipedia photograph, 2017) on Alby Street, still under restoration, and the McPike crypt in the grounds, shown on group tours. Not open outside scheduled events.',
  'A stripped mansion paid for by its ghosts.',
  'Privately owned. Great Rivers & Routes says the mansion is not open outside scheduled, ticketed tours, listed on the mansion\'s own calendar and busiest in autumn; tours last about an hour and a half. Otherwise view from Alby Street. Street parking.',
  [W('McPike Mansion'),L(GRR+': The McPike Mansion','https://www.riversandroutes.com/directory/mcpike-mansion/')],conf='mixed',brick='yes'),

N('lyman-trumbull-house','Lyman Trumbull House','Alton','il','landmark','standing',38.89707,-90.17583,'site','view','drive','','c. 1849–',
  'Lyman Trumbull, senator from Illinois and a co-author of the Thirteenth Amendment, lived here from 1849 to 1863. The house was built about 1849 and made L-shaped by a rear addition late in the 1800s. It became a National Historic Landmark in 1975.',
  'A storey-and-a-half red brick house on a limestone foundation, with three gabled dormers and a small wooden entrance porch on fluted pilasters, in the Middletown neighbourhood. Private home; interior not open.',
  'Where a co-author of the Thirteenth Amendment lived.',
  'Private house; seen from the street only. Street parking in Middletown.',
  [W('Lyman Trumbull House')],brick='yes'),

N('union-brewery-alton','Yakel House and Union Brewery','Alton','il','industry','standing',38.8925,-90.16444,'site','view','drive','','1836–1952',
  'Philip Yakel, from Germany, started Alton\'s first brewery soon after he came to America in 1836. His son George built the family house beside it in 1863. William Netzhammer of St. Louis bought the brewery in 1882 and his family ran it until 1952, keeping it going through Prohibition with near beer.',
  'The red brick house of 1863 behind a limestone retaining wall (Wikipedia photograph), in a plain German-influenced style, and the brewery buildings at 1421–1431 Pearl Street. Private; interior not checked.',
  'A brewery that made near beer through Prohibition.',
  'Private property; view from Pearl Street. Street parking.',
  [W('Yakel House and Union Brewery')],brick='yes'),

N('godfrey-memorial-chapel','Benjamin Godfrey Memorial Chapel','Godfrey','il','worship','standing',38.95030,-90.19192,'site','view','drive','','1854–',
  'Captain Benjamin Godfrey, a Massachusetts sea captain who founded Monticello Seminary for girls in 1838, had this church built in 1854 to look like one he remembered from his New England childhood; W.H. Howell was the builder. It served the seminary, later Monticello College, until the college closed in 1971 and Lewis and Clark Community College took over the campus. In 1991 it was moved from across the road to its present place on the campus.',
  'A Greek Revival temple front with six Doric columns under a pediment, and a Gothic steeple; the 1934 Historic American Buildings Survey named it one of the six most authentic New England churches built outside New England. Some of the original window glass remains (HMdb marker). Interior not checked: the college rents it for events.',
  'A New England meeting house on a prairie campus.',
  'On the Lewis and Clark Community College campus, 5800 Godfrey Road. Seen from the campus grounds; whether it is open outside events was not checked. Campus lots beside it.',
  [W('Benjamin Godfrey Memorial Chapel'),HM(144922,'Benjamin Godfrey Memorial Chapel'),L(GRR+': Benjamin Godfrey Chapel','https://riversandroutes.com/directory/benjamin-godfrey-chapel')],th=[38.95001,-90.19244],thn='Campus lot',brick='?'),

N('clifton-terrace-wine-cellar','Clifton Terrace wine cellar and terraces','Godfrey','il','hotel','ruins',38.92911,-90.25443,'area','public','walk','','1852–1959',
  'Louis Stiritz brought vines from the Neckar in Germany and built stone terraces up the bluff here from 1852 to 1865, making a sweet wine popular in St. Louis. In 1874 he opened the Clifton Inn for workers at a cement plant on Clifton Terrace Road; later, weekend crowds came up by paddle steamer to its dance pavilion and cottages. The inn became the Clifton Terrace Hotel in 1929 and burned in 1959, on the spot that is now the park\'s parking lot. The Village of Godfrey bought the land in 1995.',
  'The marker says a 30-by-60-foot wine cellar lined with hand-cut arched stone remains at the foot of the terraces, with the stone terraces themselves on the bluff. The terraces show as steps on the bare-ground LiDAR on the bluff face about 100 m north-west of the marker; the cellar was not seen on the aerial. Start at the marker on McAdams Parkway.',
  'Rhine-style terraces on a Mississippi bluff.',
  'Captain Jake Ringering Park at Clifton Terrace, a Village of Godfrey park open sunrise to sunset, dogs on a leash, no alcohol (village parks page, read November 18, 2026). Park in its lot beside the Sam Vadalabene Trail on McAdams Parkway (Route 100).',
  [HM(220760,'A History of Clifton Terrace'),L('Village of Godfrey: parks','https://www.godfreyil.org/parks')],conf='mixed',th=[38.92855,-90.25413],thn='Clifton Terrace Park lot',brick='no'),

N('old-chain-of-rocks-bridge','Old Chain of Rocks Bridge','Madison','il','landmark','standing',38.75850,-90.17067,'site','public','walk','','1929–1968',
  'A mile-long steel truss bridge over the Mississippi, opened to traffic in July 1929 after floods and ice held up the work. It carried U.S. Route 66 for a time. A newer bridge opened upstream in 1967 and the old one closed in 1968; it reopened to walkers and cyclists in 1999. It takes its name from the rock ledges in the river below, now mostly hidden by a low dam built in the 1960s.',
  'The bend in the middle of the bridge, needed because of a water intake and weak bedrock: Wikipedia gives it as 22 degrees, the National Park Service as 30. The concrete piers, the trusses and the two old St. Louis water intake towers in the river.',
  'A Route 66 bridge with a kink in the middle.',
  'Open to walkers and cyclists daily (National Park Service); hours not checked on the managers\' own page, which did not open. Free parking at the Illinois end on Chouteau Island at the end of Chain of Rocks Road, and on the Missouri side at a park opened in 2024. Pin is where the bridge leaves the Illinois bank on Chouteau Island; the bend is out over the river to the west, about 1 km away.',
  [W('Chain of Rocks Bridge'),L('National Park Service: Chain of Rocks Bridge','https://www.nps.gov/places/chain-of-rocks-bridge.htm')],conf='mixed',th=[38.75702,-90.16463],thn='Illinois bridge entrance lot',brick='no'),

N('stephenson-house-edwardsville','1820 Colonel Benjamin Stephenson House','Edwardsville','il','landmark','standing',38.80722,-89.95222,'exact','open','drive','','1820–',
  'Benjamin Stephenson, an early Illinois politician, built this Federal house in 1820 as his home, office and political headquarters, and died soon after. Fifteen owners followed, adding an ell in 1845; the last private one was a fraternity. The city bought it in 1999 and restored it to its 1820s look at a cost of over a million dollars; it opened as a house museum in 2006.',
  'Walls three bricks thick, inside and out, made on the site by people Stephenson enslaved (Wikipedia). Furnished rooms of the 1820s shown on guided tours.',
  'Bricks made on the spot in 1820.',
  'House museum owned by the City of Edwardsville, 409 South Buchanan Street. Its own page (read November 18, 2026): March to December Thursday to Saturday 10 am to 3 pm and Sunday 12 to 3 pm; January and February Saturday and Sunday only, by reservation; last tour starts by 2 pm; closed December 14, 2026 to January 2, 2027. Adults $10, children 6 to 12 $5. Reservations recommended, (618) 692-1818. Mapped lot on South Buchanan Street.',
  [W('Benjamin Stephenson House'),L('Stephenson House: visit','https://stephensonhouse.org/visit-1')],th=[38.80805,-89.95231],thn='South Buchanan Street lot',brick='yes',hours='March to December: Thursday to Saturday 10 a.m. to 3 p.m., Sunday 12 to 3 p.m. January and February: Saturday and Sunday by reservation. Last tour starts by 2 p.m.'),

N('leclaire-nelson-factory','LeClaire: N. O. Nelson\'s cooperative village and factory','Edwardsville','il','industry','standing',38.80621,-89.94994,'site','public','drive','','1890–',
  'N. O. Nelson founded LeClaire in 1890 as a cooperative village round his plumbing-fixture factory, with profit sharing on the model of the Maison Leclaire in Paris, free adult classes and reading rooms. Nellie Bly compared it favourably with Pullman. It stayed a separate village until Edwardsville annexed it (Wikipedia says 1933, the SIUE encyclopedia 1934). The empty factory was used by Southern Illinois University from 1964 and later deeded to Lewis and Clark Community College, which reopened it as a branch campus from 2004.',
  'The factory buildings by E. A. Cameron: red brick fronts with rows of arched windows and roof-top monitors, gutted and refitted inside for classrooms. Round them the village\'s houses, and the 1931 water tower known as the Tin Man. The NONCO mark of the company can still be seen on some Edwardsville fire hydrants.',
  'A utopian factory town that became a college.',
  'The N. O. Nelson Campus of Lewis and Clark Community College, 600 Troy Road; the grounds are a working campus, the buildings open in college hours (not checked). The village houses are private. Street parking and campus lots.',
  [W('LeClaire Historic District'),L('Historic LeClaire: the Nelson Manufacturing Complex','https://historic-leclaire.org/new-page-2'),L('Madison Historical (SIUE): Leclaire','https://madison-historical.siue.edu/encyclopedia/leclaire/')],conf='mixed',brick='yes'),

N('kamp-store-kampsville','Kamp Store','Kampsville','il','town','standing',39.29833,-90.61028,'exact','open','drive','','1902–',
  'Joseph Kamp, son of Kampsville\'s founder, opened this general store in 1902 and ran it until he died in 1952, selling everything from household goods to cars and farm machinery brought up by barge from St. Louis. It was a grocery into the 1970s and then a carpet store. The Center for American Archeology bought it in 1991 for its visitor centre and museum.',
  'A two-storey wooden store with a false front trimmed in pressed metal, at Oak Street and Broadway.',
  '',
  'The Center for American Archeology\'s visitor centre. Its hours are not settled: greatriverroad.com lists it open mid-April to mid-November, Tuesday to Friday 10 am to 5 pm, free with donations welcome, while the Great Rivers & Routes listing says "closed until further notice". Hours not checked with the Center. Mapped lot on Oak Street.',
  [W('Kamp Store'),L('Great River Road: Center for American Archeology','https://www.greatriverroad.com/mgr-attractions-2/center-american-archeology'),L(GRR+': Center for American Archeology','https://riversandroutes.com/directory/center-for-american-archeology')],conf='mixed',th=[39.29829,-90.60974],thn='Oak Street lot',brick='no'),

N('salem-baptist-church-alton','Salem Baptist Church','Alton','il','worship','standing',38.96694,-90.1225,'site','view','drive','','1912–',
  'A Black Baptist congregation formed in 1819 built this, its third church, in 1912. The African-American stonemason Madison Banks and the white contractor Samuel Marshall, both of Alton, built it with help from two members, John Walker and William Emery. In years of segregation it was the social centre for the area\'s Black community, with picnics, hay rides, a Ladies Aid Society that gave a college scholarship, and a youth club; membership fell away after the 1960s.',
  'The 1912 church on Seiler Road in rural Foster Township: white-painted walls of block and a corner tower with a spire, in the photograph on Wikipedia. Interior not checked.',
  'Built by a Black stonemason in 1912.',
  'A church at 2001 Seiler Road; seen from the road. Whether it still holds services and who owns it now were not checked. No mapped parking.',
  [W('Salem Baptist Church (Alton, Illinois)')],brick='no'),
]

PIN_NOTES={
 'elsah-historic-district':'The Register list coordinate (38.9542,-90.3602) fell in the wooded ravine south-east of the houses on the aerial; moved with pix.py about 110 m north-west onto the houses along Mill Street.',
 'elsah-ice-house-ruin':'HMdb marker 216141 position (38 57.158 N, 90 21.723 W), at Mill and Elm streets; the ruin is beside the marker.',
 'principia-college-maybeck':'Register list coordinate for the Principia College Historic District; the middle of the campus, not a building. Kept as area.',
 'pere-marquette-lodge':'OpenStreetMap hotel point for the lodge (nom.py), matching the Register list coordinate 38.9717,-90.5411.',
 'smith-duncan-house-eastman-barn':'Register list coordinate (Wikipedia). On the aerial it is on the edge of the park road under trees, with one small roofed building about 100 m west; neither the aerial nor the LiDAR shows which is the house or the barn, so kept as area.',
 'grafton-historic-district':'Register list coordinate for the district (Wikipedia); the middle of Main Street, not the ice house or wharf.',
 'ruebel-hotel-grafton':'Wikipedia infobox coordinate for 207-215 East Main Street.',
 'jersey-county-courthouse':'Wikipedia infobox coordinate.',
 'alton-prison-ruins':'OpenStreetMap point "Alton Military Prison Site" on William Street (nom.py); HMdb marker 211807 is at 38.89115,-90.18952, 25 m away.',
 'mcpike-mansion':'Wikipedia infobox coordinate, just west of Alby Street; on the aerial it is under trees and the house cannot be picked out, so kept as area.',
 'lyman-trumbull-house':'Wikipedia infobox coordinate.',
 'union-brewery-alton':'Wikipedia infobox coordinate for 1421-1431 Pearl Street.',
 'godfrey-memorial-chapel':'HMdb marker 144922 position (38 57.018 N, 90 11.515 W), beside the chapel.',
 'clifton-terrace-wine-cellar':'HMdb marker 220760 is at 38.92837,-90.25373 by the park lot. The LiDAR sheet shows a stepped series of terraces on the bluff face about 100 m north-west; pin moved there with pix.py. The wine cellar itself was not seen. Area.',
 'old-chain-of-rocks-bridge':'First put on the OpenStreetMap cycleway over the river (38.75977,-90.17377), but that point is on the Missouri side of the state line, so check.py refused it for region il. Moved with look.py and pix.py to where the bridge deck meets the Illinois bank on the aerial (900 m view, November 18, 2026).',
 'stephenson-house-edwardsville':'Wikipedia infobox coordinate.',
 'leclaire-nelson-factory':'OpenStreetMap point for the Lewis and Clark Community College N. O. Nelson Campus, 600 Troy Road (nom.py).',
 'kamp-store-kampsville':'Wikipedia infobox coordinate, northeast corner of Oak and Broadway.',
 'salem-baptist-church-alton':'Wikipedia infobox coordinate for 2001 Seiler Road.',
}
BATCH={'key':'il_jasy','label':'Illinois: Elsah, Grafton, Alton and Edwardsville','added':'2026-11-18 15:32'}
