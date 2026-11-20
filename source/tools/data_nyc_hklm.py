# November 20, 2026: the Town of Huntington, Suffolk County, Long Island (Huntington village, Halesite, Cold Spring Harbor,
# Lloyd Harbor and Lloyd Neck, Centerport, Eatons Neck, West Hills, Northport). Region nyc drawn at random by
# choose.py --state ny (it offered Huntington); tools/start.py found no Atlas place within 6 km of Huntington.
# Facts come only from sources opened in this session: Wikipedia read as raw text (tools/wiki_raw.py) and its Register list
# for the town, the Town of Huntington's "Famous People & Places" history sheets (huntingtonny.gov filestorage PDFs), the
# Huntington Historical Society's property and tour pages, Preservation Long Island (Joseph Lloyd Manor, Coindre Hall
# boathouse), NYS Parks (Walt Whitman Birthplace, Caumsett), the Huntington Lighthouse Preservation Society, the Vanderbilt
# Museum, OHEKA's tour page, the Greenlawn-Centerport Historical Association and the Whaling Museum of Cold Spring Harbor.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
TOH='https://www.huntingtonny.gov/filestorage/13747/99540/16499/'
T=lambda f,t: ['Town of Huntington history sheet: '+t,TOH+f]
HHS='https://huntingtonhistoricalsociety.org/'
GOLD=[40.89659,-73.43445]
GOLDN='Gold Star Battalion Beach lot, West Shore Road (tour boats leave from its dock)'

BATCH={'key':'nyc_hklm','label':'Town of Huntington, Long Island','added':'2026-11-20 02:40'}

PLACES=[
N('walt-whitman-birthplace','Walt Whitman Birthplace State Historic Site','West Hills (Huntington Station)','nyc','landmark','standing',40.81704,-73.41157,'exact','open','drive','','1816–1819',
  'Walter Whitman Sr., a Quaker carpenter, built this two-story cedar-shingled farmhouse by hand in West Hills (Wikipedia gives 1816; the NYS Parks page says about 1819), and the poet Walt Whitman was born in it in 1819. The family moved to Brooklyn when he was five. He came back to Long Island at 17 to teach, founded the Long Islander newspaper in Huntington, and later wrote Leaves of Grass. The house is a New York State Historic Site and on the National Register.',
  'The restored farmhouse, furnished with nineteenth-century pieces including an old schoolmaster\'s desk, shown on guided tours, and an interpretive center with more than 100 portraits, original letters, manuscripts and artifacts, a film, a bookshop and a picnic area (NYS Parks). Original fabric of the house beyond that not checked.',
  'The farmhouse Whitman\'s father built with his own hands, now hemmed in by Route 110\'s shopping strip.',
  'New York State Office of Parks, Recreation and Historic Preservation, with the Walt Whitman Birthplace Association; 246 Old Walt Whitman Road, Huntington Station, phone 631-427-5240. Admission on the NYS Parks page: adults $12, seniors, groups and veterans $11, students $10, 5 and under free; the Empire Pass is not accepted. Hours from the same page, read November 2026. Parking: the mapped lot next to the site on Walt Whitman Road; that it is the site\'s own lot was not checked.',
  [L('NYS Parks: Walt Whitman Birthplace State Historic Site','https://www.parks.ny.gov/historic-sites/waltwhitmanbirthplace/details.aspx'),W('Walt Whitman Birthplace State Historic Site')],
  conf='mixed',brick='?',hours='June 16 to Labor Day daily 11 a.m. to 4 p.m.; rest of year Wednesday to Friday 1 to 4, Saturday and Sunday 11 to 4'),

N('old-first-church-huntington','Old First Presbyterian Church','Huntington','nyc','worship','standing',40.87461,-73.41981,'exact','view','walk','','1784 (congregation 1658; second church on this site 1715)',
  'Huntington\'s congregation was organized in 1658 and built its first meeting house in 1665 near what is now Prime Avenue; a second went up on this rise in 1715. During the British occupation the church was used as stables and stores, and on November 26, 1782 Colonel Benjamin Thompson had it pulled down and its timbers used to build Fort Golgotha on the town\'s burying ground. The townspeople rebuilt it on the same site in 1784. The bell, carried off by the British and found cracked on a ship in the East River in 1783, was recast in Hartford and rang here until 1967.',
  'A large white-shingled meeting house of two and a half stories with a steep gable roof and a tall square five-story bell tower in the middle of the front; a two-story addition with five gables was built on the back about 1900. The recast bell, engraved inside "THE TOWN ENDURES", is on display in the church (Town of Huntington sheet). Interior not checked, and service times were not found on a page of the church\'s own.',
  'A church the British tore down for firewood and fort timbers, rebuilt by the town the year after they left.',
  'An active Presbyterian church at 125 Main Street (north-west corner of Main Street and Sabbath Day Path), phone 631-427-2101 on the Town sheet. Seen from Main Street. A mapped lot on Prime Avenue by Heckscher Park is about 150 m west; whether it is public was not checked.',
  [W('Old First Church (Huntington, New York)'),T('Old_First_Presbyterian_Church.pdf','Old First Presbyterian Church')],
  th=[40.87442,-73.42154],thn='Lot on Prime Avenue by Heckscher Park',brick='?'),

N('old-burying-ground-fort-golgotha','Old Burying Ground and the site of Fort Golgotha','Huntington','nyc','burial','standing',40.87163,-73.42368,'site','public','walk','','17th century (oldest stone 1712); fort 1782–1783',
  'Huntington\'s first public cemetery, on the small hill behind the Soldiers and Sailors Memorial Building, probably laid out soon after the town was founded in 1653; the oldest stone left is dated 1712. In November 1782 Colonel Benjamin Thompson (later Count Rumford) had the King\'s American Dragoons build a fort on top of it in fifteen days, from the timbers of the Old First Church. More than 100 gravestones were pulled up and used in its floors, fireplaces and ovens; tradition has it that the bread baked there came out with the inscriptions reversed on the bottom crust. The British left in March 1783 and the fort was torn down.',
  'The hilltop burying ground with its old stones; the fort itself is gone. The town\'s information board stands on Main Street at the foot of the hill. Part of the Old Town Hall and Old Town Green historic districts.',
  'Tombstone bread: the British fort built on Huntington\'s graves.',
  'The Town of Huntington\'s sheet calls it the earliest public cemetery in Huntington; who holds title now was not checked. On the hill behind the Soldiers and Sailors Memorial Building, 228 Main Street at Nassau Road, reached from Main Street. Hours not checked. Mapped lots on Main Street and Nassau Road are about 70 to 100 m away; whether they are public was not checked.',
  [W('Fort Golgotha and the Old Burial Hill Cemetery'),T('Old_Burying_Ground_%26_Fort_Golgotha.pdf','Old Burying Ground & Fort Golgotha')],
  th=[40.87089,-73.42356],thn='Lot on Nassau Road',brick='no'),

N('soldiers-sailors-memorial-huntington','Soldiers and Sailors Memorial Building and the Old Town Hall district','Huntington','nyc','civic','standing',40.87150,-73.42444,'exact','open','walk','','1892–1910',
  'Huntington\'s veterans formed the Soldiers and Sailors Memorial Association in 1886 to remember the town\'s 39 Civil War dead, and the memorial building, designed in the Tudor Revival style by Cady, Berg and See (architects of the American Museum of Natural History), was finished in 1892 as the town library. The library stayed until 1958; the building then held town offices and from 1969 the Town Historian, and in 2000 the association gave it to the Huntington Historical Society. It is one of eight buildings in the Old Town Hall Historic District with the 1905 Huntington Sewing and Trade School (same architects, now the society\'s offices and archives), the 1910 Old Town Hall at Main Street and Stewart Avenue, and the First Universalist church at 6 Nassau Road.',
  'The memorial building with a cannon in front, given by the federal government in 1903 for the town\'s 250th anniversary after guarding New York Harbor. Across Main Street, the Trade School at 209 Main and the Old Town Hall. Interior fabric not checked.',
  'A Civil War memorial that was the town library for 66 years.',
  'Huntington Historical Society, 228 Main Street; the Trade School office at 209 Main Street is open weekdays 9 to 5 and its archives by appointment. Hours from the society\'s properties page, read November 2026. Mapped lots on Main Street and Nassau Road are within 100 m; whether they are public was not checked.',
  [L('Huntington Historical Society: our properties',HHS+'for-your-visit/our-properties/'),T('Soldiers_%26_Sailors_Memorial_Building.pdf','Soldiers & Sailors Memorial Building'),W('Old Town Hall Historic District (Huntington, New York)')],
  th=[40.87089,-73.42356],thn='Lot on Nassau Road',brick='?',hours='Tuesday to Sunday noon to 4 p.m.; closed Monday'),

N('david-conklin-farmhouse','David Conklin Farmhouse','Huntington','nyc','landmark','standing',40.86787,-73.42598,'exact','open','walk','','c. 1750',
  'A farmhouse built about 1750 and lived in by the Conklin family for more than 150 years. Sybel Conklin ran the farm with her children while her husband David was held prisoner by the British in 1777. Ella Conklin Hurd gave it to the Huntington Historical Society in 1911, making it one of the earliest museums on Long Island. The original barn was taken down long ago; an 1830 barn from the Taylor farm in Laurel Hollow was moved here in 1990.',
  'The original rooms of about 1750, furnished to show three periods (Colonial, Federal and Victorian), with a table and chair George Washington used on his 1790 tour of Long Island and the Conklins\' bed; a 1922 meeting room at the back is now an exhibit hall. Docent-led tours.',
  'A farmhouse that has been a museum since 1911.',
  'Huntington Historical Society, 2 High Street at New York Avenue. The society\'s properties page gives Sundays noon to 4; the farmhouse page says docents show it Sundays 1 to 4 "until further notice", groups by appointment, and that it is closed on holidays. Read November 2026. Parking not checked.',
  [L('Huntington Historical Society: David Conklin Farmhouse',HHS+'?p=1108'),L('Huntington Historical Society: our properties',HHS+'for-your-visit/our-properties/')],
  conf='mixed',brick='?',hours='Sunday afternoons (noon to 4 or 1 to 4: the society\'s two pages differ); groups by appointment'),

N('kissam-house-huntington','Dr. Daniel Kissam House','Huntington','nyc','landmark','standing',40.87403,-73.41229,'exact','open','walk','','1795',
  'Timothy Jarvis, a housewright, built this house in 1795 on one of the original home lots facing the old Town Green, and Dr. Daniel Whitehead Kissam, a physician from Oyster Bay, was the first to live in it. His son-in-law Dr. Charles Sturges added a kitchen wing in 1840 and made the old kitchen a formal dining room. The Huntington Historical Society bought it from the estate of Hilda Taylor in 1967 and began restoring it in 1984; the kitchen wing was put back to its 1840 form in 2006.',
  'A three-quarter-plan house the society calls one of the finest on Long Island for its architectural detail; the 1840 dining room has Egyptian Revival woodwork. Behind it the 1790 Kissam Barn, moved from the Rogers homestead in Lloyd Harbor, used for festivals. The Adams House on the same property is not open.',
  '',
  'Huntington Historical Society, 434 Park Avenue; shown by appointment only through the society (properties page, read November 2026). The Arsenal, a town property, is across the road at 425 Park Avenue. Parking not checked.',
  [L('Huntington Historical Society: the Kissam House Museum',HHS+'for-your-visit/our-properties/kissam-property/')],
  brick='?',hours='By appointment only'),

N('bethel-ame-church-huntington','Bethel AME Church and Manse','Huntington','nyc','worship','standing',40.87844,-73.41774,'exact','view','walk','','1843 (congregation); church 1845 or 1925',
  'The oldest African-American church in Huntington, founded in 1843 by Peter Crippen and Nelson Smith (Wikipedia); the Town of Huntington\'s sheet says its incorporators worked in the Crossman brickyards on West Neck. It bought this lot in 1844 from the Methodists, whose 1837–38 chapel became its first church. The dates of the present building disagree: the Register listing as summed up on Wikipedia has a church built about 1845 and a manse of 1915, while the Town sheet says the parsonage was built in 1907 and the present church in 1925 by the Rev. George A. Lonzo, replacing the first.',
  'A wood-frame church of one and a half stories with a central pedimented entrance, clapboard and shingle walls, round-headed stained-glass windows (four a side and a pair over the door) and a large pointed-arch window behind the altar; the Town sheet says the interior keeps its original woodwork, pressed-tin ceiling and Gothic oak altar fittings. Eleven headstones survive in the small churchyard behind, where the founders are buried. Interior not seen; service times not found on a page of the church\'s own.',
  'Huntington\'s oldest Black church, founded by brickyard workers.',
  'Active church at 291 Park Avenue (phone 631-549-5014 on the Town sheet). Seen from Park Avenue. Parking not checked.',
  [W('Bethel AME Church and Manse'),T('Bethel_A.M.E._Church.pdf','Bethel A.M.E. Church')],
  conf='mixed',brick='?'),

N('van-wyck-lefferts-tide-mill','Van Wyck–Lefferts Tide Mill','Lloyd Harbor','nyc','industry','standing',40.89986,-73.44466,'exact','boat','boat','','c. 1793–1795',
  'A tide mill built by the Van Wyck family (Wikipedia gives about 1793, the Huntington Historical Society 1795) on a dam across Puppy Cove off Huntington Harbor. High tide filled the mill pond through the tide gate; at low tide the trapped water was let out to turn the wheel. The society says it is the only one of the scores of tide mills on Long Island\'s north shore still standing with its building, on its original dam, with its original wooden gears.',
  'A timber-framed mill with a gable roof, little changed since the early 1800s, on its earthen dam with sluice gates; inside, the original massive wooden gearing. Reached only by boat on guided tours: a short ride from Gold Star Battalion Beach into Puppy Cove, then the mill. The tour takes about an hour and a half, needs climbing in and out of a boat, is not wheelchair accessible and takes children 12 and over.',
  'The last north-shore tide mill with its gears still in it.',
  'The mill belongs to the Lefferts Tide Mill & Preserve; the Huntington Historical Society runs the public tours by boat from the Town of Huntington\'s Gold Star Battalion Beach, 324 West Shore Road, where there are restrooms. The 2026 tours were in summer (one listed for Tuesday, August 4, 2026, sold out); private tours can be arranged. Puppy Cove is ringed by private land: no way to it on foot.',
  [W('Van Wyck-Lefferts Tide Mill'),L('Huntington Historical Society: Lefferts Tide Mill tour',HHS+'events/lefferts-tide-mill-tour/')],
  conf='mixed',th=GOLD,thn=GOLDN,brick='no',hours='Guided boat tours on set dates in summer and fall, booked through the Huntington Historical Society'),

N('joseph-lloyd-manor','Joseph Lloyd Manor','Lloyd Harbor','nyc','landmark','standing',40.91437,-73.47753,'exact','open','drive','','1766–1767',
  'Built in 1766–67 for Joseph Lloyd (1716–1780) on the Manor of Queens Village, a 3,000-acre provisioning plantation set up in the late 1600s on the ancestral lands of the Matinecock that took in all of Lloyd Neck. Jupiter Hammon (1711–before 1806), one of the first published African American writers, was enslaved here by the Lloyds and wrote his best-known works here; the British occupied the house in the Revolution while Joseph Lloyd, a patriot, fled to Connecticut. The Lloyds kept it until 1876; Anna Matheson Wood gave it to Preservation Long Island in 1968.',
  'The 1760s manor house on a 2.5-acre site above Lloyd Harbor, shown on guided tours; it is a national Literary Landmark for Jupiter Hammon. Interior fabric not checked.',
  'The house where the first published Black poet in America wrote while enslaved.',
  'Preservation Long Island, 1 Lloyd Lane at Lloyd Harbor Road. House tours June to October; private and group tours at $12 a person with a $120 minimum, booked through its page (read November 2026). The nearest mapped public lot is at the Caumsett State Historic Park Preserve entrance, about 500 m north-east; parking at the house itself not checked.',
  [L('Preservation Long Island: Joseph Lloyd Manor','https://preservationlongisland.org/joseph-lloyd-manor/'),W('Joseph Lloyd House'),T('Lloyds_of_Lloyd_Neck.pdf','Lloyds of Lloyd Neck')],
  th=[40.91732,-73.47317],thn='Caumsett State Historic Park Preserve entrance lot',brick='?',hours='House tours June to October, seasonal dates; private and group tours by request'),

N('henry-lloyd-manor','Henry Lloyd Manor House','Lloyd Harbor','nyc','landmark','standing',40.91455,-73.46849,'site','open','drive','','1711',
  'Henry Lloyd, 24, gave up a shipping business in Newport, Rhode Island in 1711 to farm his father James\'s Manor of Queens Village on Lloyd Neck, and built this saltbox house. Jupiter Hammon was born on the manor in 1711 in the first manor house, which went to Henry Lloyd II on his father\'s death in 1763, when Joseph built the larger house to the west. The house now stands on the grounds of Caumsett State Historic Park Preserve, leased to the Lloyd Harbor Historical Society, which has restored it with the George Weir Barn and the gardens round it.',
  'A 1711 saltbox and the George Weir Barn. Interior not checked; when it is open to visitors was not found.',
  'The oldest house on Lloyd Neck, a century older than the Gold Coast round it.',
  'Owned by the State (Caumsett State Historic Park Preserve) and leased to the Lloyd Harbor Historical Society, 41 Lloyd Harbor Road, phone (631) 424-6110 on the Town of Huntington\'s page. Opening times not found on any page read. Pin from the museum point in OpenStreetMap.',
  [L('Town of Huntington: Lloyd Harbor Historical Society','https://huntingtonny.gov/content/13747/99544/25719/25772/default.aspx'),T('Lloyds_of_Lloyd_Neck.pdf','Lloyds of Lloyd Neck'),L('NYS Parks: Caumsett State Historic Park Preserve','https://parks.ny.gov/parks/23/details.aspx')],
  brick='?',hours='?'),

N('caumsett-marshall-field-estate','Caumsett: the Marshall Field III estate','Lloyd Harbor','nyc','inst','standing',40.93072,-73.45862,'exact','public','hike','','1921–1961',
  'Marshall Field III bought 1,750 acres of Lloyd Neck in 1921 (Wikipedia gives 1,426 acres for the estate the state later bought) and named it Caumsett, the Matinecock name for the neck, "place by a sharp rock". He made it a self-sufficient English-style estate, country club and hunting preserve with its own water and power and facilities for every sport but golf; the estate house, Caumsett Hall, was built in 1925 (the Register names John Russell Pope among the architects). New York State bought it in 1961 for $4 million. The British built Fort Franklin on Lloyd Neck during the Revolution, the largest fortification on Long Island in its day.',
  'Caumsett Hall, the polo pony barn (now the Lloyd Harbor Equestrian Center: do not enter without an appointment), the Masters Garage (a BOCES outdoor school) and a nature museum in the Smith family house of 1751, over miles of paths through woods, meadows and shore. The pin is Caumsett Hall; it is seen from the paths, and whether it opens inside was not checked.',
  'A Gold Coast estate built to need nothing from outside.',
  'NYS Office of Parks, Recreation and Historic Preservation, 25 Lloyd Harbor Road, phone (631) 423-1770. Open sunrise to sunset every day. Vehicle fee $8, collected 8 to 4 on weekends and holidays in spring and fall and daily from late May to early September (2026 dates). No pets, drones, metal detecting, skates or fires; bikes not allowed on the beach. Café May to October, Friday to Sunday 9 to 5. All from the NYS Parks page, read November 2026. From the entrance lot it is about 2.5 km on foot to the hall; a mapped lot by the hall is on the service drive.',
  [L('NYS Parks: Caumsett State Historic Park Preserve','https://parks.ny.gov/parks/23/details.aspx'),W('Caumsett State Historic Park Preserve')],
  conf='mixed',th=[40.91732,-73.47317],thn='Caumsett State Historic Park Preserve entrance lot',brick='?',hours='Sunrise to sunset daily'),

N('huntington-harbor-light','Huntington Harbor Light','Lloyd Harbor','nyc','light','standing',40.91072,-73.43131,'exact','boat','boat','','1910–1912 (first light nearby 1857)',
  'The first Lloyd Harbor light of 1857, a wooden house with a brick tower at the southern tip of Lloyd Neck, did little for ships making for Huntington Harbor; this one was built from 1910 to 1912 by the Charles Meade Company. Its concrete crib foundation was built ashore, floated out, sunk and filled with concrete. The light was automated (in 1949 says Wikipedia, 1967 says the Town sheet); in 1984 the government decided to tear it down, and a local campaign, now the Huntington Lighthouse Preservation Society, saved it and leases it from the Coast Guard. The 1857 light burned on November 12, 1947.',
  'A 42-foot reinforced-concrete lighthouse in the shape of a small Beaux-Arts castle, still a working light. On the tour you land, go inside and may climb the tower.',
  'A concrete castle floated out to sea, saved from demolition by its neighbours.',
  'Huntington Lighthouse Preservation Society; tours by boat from the Town of Huntington\'s Gold Star Battalion Beach dock, 324 West Shore Road, weather and wind permitting, about 1 hour 15 minutes. 2026 prices: adults $35, seniors $30, children 5 to 12 $25; no children under 5, not wheelchair accessible, closed flat rubber-soled shoes only. The 2026 season is over; 2027 dates were not yet posted when read (November 2026). Seen from the shore at Gold Star Battalion Beach and Coindre Hall.',
  [L('Huntington Lighthouse Preservation Society: tours','https://www.huntingtonlighthouse.org/tours'),W('Huntington Harbor Light'),T('Huntington%27s_Lighthouses.pdf','Huntington\'s Lighthouses')],
  conf='mixed',th=GOLD,thn=GOLDN,brick='no',hours='Boat tours on set dates in summer; 2027 dates not yet posted'),

N('eatons-neck-light','Eatons Neck Light and Coast Guard Station','Asharoken','nyc','light','standing',40.95394,-73.39549,'site','ask','drive','','1798–1799',
  'Designed and built by John McComb Jr., who also built the Montauk Point light two years earlier, and first lit in 1799 (Wikipedia; the Town sheet dates it 1798). It is one of only two 18th-century lighthouses still standing in New York State. The keeper\'s quarters were replaced by Coast Guard housing. The station on the grounds was founded in 1849 by the New York Lifesaving Benevolent Association and is the oldest Coast Guard station in New York.',
  'An octagonal sandstone tower 73 feet tall, its light 126 feet above the sea, still showing a fixed white light through its Third Order Fresnel lens made by Henry-Lepaute of Paris (the Town sheet calls it the only Fresnel lens still in use on Long Island).',
  'Long Island\'s second-oldest lighthouse, still burning behind a Coast Guard gate.',
  'U.S. Coast Guard Station Eatons Neck, an active station with family housing. The Town of Huntington\'s sheet says to ask the station (phone 631-261-6959 on it) for permission to tour the grounds; without it, see the tower from the water. Not on public land.',
  [W('Eatons Neck Light'),W('Coast Guard Station Eatons Neck'),T('Huntington%27s_Lighthouses.pdf','Huntington\'s Lighthouses')],
  conf='mixed',brick='?'),

N('vanderbilt-eagles-nest','Eagle\'s Nest: the Vanderbilt Museum','Centerport','nyc','inst','standing',40.90657,-73.36881,'exact','open','drive','','1910–1936',
  'William K. Vanderbilt II built his estate, Eagle\'s Nest, above Northport Bay in three stages from 1910 to 1936; the 24-room Spanish Revival mansion was designed by Warren and Wetmore, one of the two firms behind Grand Central Terminal. His will left the house and its 43 acres to Suffolk County as a museum for his marine, natural-history and ethnographic collections, and it opened as one in 1950; the county added a planetarium in 1970.',
  'The mansion with its furnishings and art, a marine museum of specimens, a curator\'s cottage, a seaplane hangar, a boathouse, gardens, and collections of arms, ship models and objects from Europe, Asia and Africa, among them what is probably the mummy of a young woman buried at Deir el-Bahari, bought in Cairo in 1931.',
  'A Vanderbilt\'s Spanish palace on the Sound, left full of his collections.',
  'Suffolk County Vanderbilt Museum and Reichert Planetarium, 180 Little Neck Road, Centerport. Last admission 3:30 p.m. Hours from the museum\'s visitor page, read November 2026; General admission covers the mansion, the Hall of Fishes marine museum, the planetarium exhibits and the grounds; mansion tours are $9 more, bought at the admissions desk. Prices not checked. A lot by the planetarium is seen on the aerial about 170 m south-west of the mansion; that it is the visitors\' lot was not checked.',
  [L('Vanderbilt Museum: visitor\'s guide','https://www.vanderbiltmuseum.org/welcome-to-the-vanderbilt/'),W('Vanderbilt Museum')],
  th=[40.90510,-73.36936],thn='Lot by the planetarium (seen on the aerial)',brick='?',hours='Friday noon to 4 p.m.; Saturday and Sunday 11 a.m. to 4 p.m. (last admission 3:30)'),

N('oheka-castle','OHEKA Castle (the Otto Kahn estate)','West Hills (Cold Spring Hills)','nyc','hotel','standing',40.82900,-73.44853,'exact','open','drive','','1914–1919',
  'The financier Otto Hermann Kahn built this house from 1914 to 1919 and named it from the first letters of his name. With 127 rooms and over 109,000 square feet as first built, it is the largest private house in New York and the second largest in the United States, said to stand on the highest point on Long Island. Kahn built it fireproof after a fire nearly destroyed his earlier country house, Cedar Court, in 1905, and in answer to Jews being kept out of the clubs and golf courses of Morristown, New Jersey. It is now a hotel of 32 rooms and on the National Register (2004).',
  'The château, its estate and gardens, seen on a guided tour of about an hour of the designated public areas; some areas may be closed on the day. Country-club casual dress; phones only for photographs. Interior fabric not checked.',
  'The second-largest house in America, built by a banker shut out of the clubs.',
  'Privately owned hotel, 135 West Gate Drive, Huntington. Mansion tours by reservation only: adults $30, seniors $25, students $20, children $10 (2026 prices on the tour page, read November 2026); group tours Monday to Thursday. Not open without a booking. Parking not checked.',
  [L('OHEKA Castle: mansion tours','https://www.oheka.com/tours'),W('Oheka Castle')],
  brick='?',hours='Guided tours daily at 11 a.m., some days also noon or 6 p.m.; by reservation only'),

N('coindre-hall','Coindre Hall (George McKesson Brown estate)','Huntington','nyc','inst','standing',40.89305,-73.43739,'exact','public','walk','','1912',
  'A 40-room mansion in the style of a French château, designed by Clarence Sumner Luce and finished in 1912 for the pharmaceutical magnate George McKesson Brown as West Neck Farm. The Brothers of the Sacred Heart bought it for a boarding school and named it for their founder, Father André Coindre (Wikipedia says 1939; the Town trail guide says 1930); the school closed in 1971 and Suffolk County bought the estate in 1972. The boathouse, built to match the house, has stood empty for years and its seawall was damaged in Superstorm Sandy; Preservation Long Island listed it as endangered in 2023.',
  'The château on the hill above Huntington Harbor (stucco towers with red-tile cones, brick chimneys and brick terraces in the Wikipedia photograph), used for weddings and events, and down by the water the turreted boathouse. A 1.1-mile trail goes down the field, through woods and wetland to the boathouse and along the harbor to Gold Star Battalion Beach. Interior not open except to events.',
  'A pharmaceutical fortune\'s château with a crumbling twin by the water.',
  'Suffolk County Parks (31 acres), 101 Browns Road at West Shore Road; the Town of Huntington uses the gym and runs programs. Parking lot at the mansion. Leashed dogs in parts of the park. Hours not checked. Facts from the Town trail guide and Preservation Long Island\'s 2023 endangered-places page.',
  [W('Coindre Hall'),L('Town of Huntington: Coindre Hall trail guide','https://huntingtonny.gov/filestorage/13749/13843/15187/99828/153038/17956/Trails_Guide_Coindre_Call.pdf'),L('Preservation Long Island: Coindre Hall boathouse (2023)','https://preservationlongisland.org/ehp2023coindre/')],
  conf='mixed',th=[40.89345,-73.43709],thn='Coindre Hall lot, Browns Road',brick='some'),

N('suydam-homestead-centerport','Suydam Homestead','Centerport','nyc','landmark','standing',40.88599,-73.36660,'exact','view','drive','','c. 1730',
  'A farmhouse begun about 1730 as one room, given a lean-to kitchen about 1760 and extended east about 1790 under one gabled roof with a central chimney for three fireplaces; a workshop was added on the west, probably in the 1830s. The Suydams, who farmed, oystered and built boats, lived in it from the late 1700s until 1957. After a fire and poor repairs, the Greenlawn-Centerport Historical Association bought it in 1989 and restored the outside in 1997.',
  'A shingled 18th-century farmhouse at the corner of NY 25A and Centerport Road, with recreated cedar shingles copying the surviving old ones on the front, new period windows, and some original woodwork and hardware inside; a modern barn behind holds the association\'s collection. The association says the house is closed to the public for maintenance, including mold remediation, and it hopes to reopen it.',
  '',
  'Greenlawn-Centerport Historical Association, 1 Fort Salonga Road (NY 25A), Centerport. Closed to the public when read (November 2026): look from the road. Parking not checked.',
  [L('Greenlawn-Centerport Historical Association: Suydam Homestead','https://www.greenlawncenterporthistorical.org/index.php/historical-properties/suydam-homestead'),T('Suydam_Homestead.pdf','Suydam Homestead'),W('Suydam House')],
  brick='?'),

N('cold-spring-harbor-main-street','Cold Spring Harbor Main Street and the Whaling Museum','Cold Spring Harbor','nyc','town','standing',40.87258,-73.45355,'area','public','walk','','1855–1890 (most buildings)',
  'The village\'s historic core, 32 buildings mostly from 1855 to 1890, shows its change from a major whaling port to a summer resort. The Whaling Museum Society was founded in 1936 and opened its museum in 1942; it holds about 6,000 documents and objects from Cold Spring Harbor and other Long Island whaling towns, including a 19th-century whaleboat with its gear, scrimshaw, and the records of the Cold Spring Whaling Company and of the Cold Spring Harbor customs house (1798 to 1908).',
  'Main Street\'s 19th-century houses and shops, walkable in a few minutes; the museum at 301 Main Street (pin) has the whaleboat and scrimshaw. The museum runs themed walking tours of Main Street and of St. John\'s Memorial Cemetery, tickets in advance. The houses are private.',
  'A whaling port turned summer village, still on one street.',
  'Public street; the Whaling Museum (Whaling Museum Society) is at 301 Main Street, phone 631-367-3418, admission adults $8, seniors and children 4 to 17 $6, members and active military free; closed Thanksgiving and Christmas. Free street parking by the museum, or the free town lot between 90 and 126 Main Street next to the post office, a 5-minute walk. Hours from the museum\'s page, read November 2026.',
  [W('Main Street Historic District (Cold Spring Harbor, New York)'),W('The Whaling Museum & Education Center'),L('Whaling Museum: hours and admission','https://cshwhalingmuseum.org/visit.html')],
  th=[40.87070,-73.45771],thn='Free town lot by the post office, Main Street',brick='?',hours='Museum fall and winter Thursday to Sunday 11 a.m. to 4 p.m.'),

N('northport-carnegie-library','Northport Carnegie library (Northport Historical Society)','Northport','nyc','civic','standing',40.90106,-73.34769,'exact','open','walk','','1914',
  'A small Carnegie library, one of 107 in New York State, built in 1914 with $10,000 from Andrew Carnegie in the Jacobethan Revival style. It was enlarged in 1958, served as the library until 1967, and since 1974 has housed the Northport Historical Society\'s museum.',
  'A red-brick building (as the Wikipedia photograph shows) with a gable-fronted reading room and stacks, a side wing with the entrance and stair, a slate roof and a barrel-vaulted reading room. Interior otherwise not checked.',
  '',
  'Northport Historical Society museum, 215 Main Street, Northport. Hours not checked: the society\'s site refused the tool and its archived copy could not be read. Parking not checked.',
  [W('Northport Public Library')],
  brick='yes',hours='?'),
]

PIN_NOTES={
 'walt-whitman-birthplace':'ArcGIS geocoder PointAddress for 246 Old Walt Whitman Road.',
 'old-first-church-huntington':'ArcGIS geocoder PointAddress for 125 Main Street; Wikipedia point is within 20 m.',
 'old-burying-ground-fort-golgotha':'Moved with pix.py onto the wooded hill with stones east of the memorial building, seen on the aerial; the first guess fell on a parking lot. OpenStreetMap has the town board on Main Street at 40.87138,-73.42437.',
 'soldiers-sailors-memorial-huntington':'ArcGIS geocoder PointAddress for 228 Main Street.',
 'david-conklin-farmhouse':'ArcGIS geocoder PointAddress for 2 High Street.',
 'kissam-house-huntington':'ArcGIS geocoder PointAddress for 434 Park Avenue.',
 'bethel-ame-church-huntington':'ArcGIS geocoder PointAddress for 291 Park Avenue; Wikipedia point within 30 m.',
 'van-wyck-lefferts-tide-mill':'OpenStreetMap watermill (nom.py), on the Puppy Cove dam; Register point within 30 m.',
 'joseph-lloyd-manor':'ArcGIS geocoder PointAddress for 1 Lloyd Lane; Wikipedia point within 15 m.',
 'henry-lloyd-manor':'OpenStreetMap museum point (nom.py), Lloyd Harbor Road.',
 'caumsett-marshall-field-estate':'OpenStreetMap building named Caumsett Hall (nom.py); the Register point is 1.4 km south-west.',
 'huntington-harbor-light':'Wikipedia coordinates.',
 'eatons-neck-light':'OpenStreetMap lighthouse (nom.py); on the aerial the pin is among the station buildings and the round tower was not picked out for certain, so site precision.',
 'vanderbilt-eagles-nest':'Moved with pix.py onto the tile-roofed mansion seen on the aerial; the geocoder point for 180 Little Neck Road fell on a small building on the shore 130 m east.',
 'oheka-castle':'ArcGIS geocoder PointAddress for 135 West Gate Drive.',
 'coindre-hall':'ArcGIS geocoder PointAddress for 101 Browns Road.',
 'suydam-homestead-centerport':'ArcGIS geocoder PointAddress for 1 Fort Salonga Road.',
 'cold-spring-harbor-main-street':'ArcGIS geocoder StreetAddress for 301 Main Street (the Whaling Museum); stands for the street.',
 'northport-carnegie-library':'ArcGIS geocoder PointAddress for 215 Main Street, also the OpenStreetMap museum point.',
}
