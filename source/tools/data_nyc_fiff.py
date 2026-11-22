# November 22, 2026: the North Shore of central Suffolk County, Long Island: the Three Villages (Stony Brook, Setauket,
# East Setauket, Old Field), Port Jefferson and Miller Place in the Town of Brookhaven, and St. James, Kings Park and
# Smithtown in the Town of Smithtown. Region drawn at random by tools/choose.py --state ny (nyc, which offered Port
# Jefferson); tools/start.py showed only three Atlas places within 15 km of Port Jefferson, none in these villages.
# Sources read in this session: the Register lists for the towns of Brookhaven and Smithtown and Wikipedia articles
# (tools/wiki_raw.py), and the pages of the bodies that run the places (NYS Parks, Suffolk County Parks, NYS DEC, the
# Ward Melville Heritage Organization, Preservation Long Island, the Long Island Museum, the Village of Old Field, the
# Historical Society of Greater Port Jefferson, Frank Melville Memorial Park, Caroline Church, Setauket Presbyterian
# Church) and local news reports, all read with tools/page.py. No interior was visited by any source opened unless the
# entry says so.
from data_b import N
from data_ma import W
BATCH={'key':'nyc_fiff','label':'Long Island: Stony Brook, Setauket, Port Jefferson and Kings Park','added':'2026-11-22 16:56'}

TOWN='Street parking or the public lots in the village; parking was not checked on the ground.'

PLACES=[
N('kings-park-psychiatric-center','Kings Park Psychiatric Center and York Hall','Kings Park','nyc','inst','standing',40.89684,-73.23563,'site','public','walk','','1885–1996',
  'Brooklyn (then Kings County) opened the Kings County Asylum here in 1885 as a "farm colony", where patients worked the fields and tended livestock as therapy. The state took it over in 1895 as Kings Park State Hospital; the 13-storey Building 93 was added later, and the patient count topped 9,300 in 1954 before drugs such as Thorazine emptied the wards. The state closed it in the fall of 1996. About nine-tenths of the campus is now Nissequogue River State Park; the state pulled down 15 of the worst buildings and the smokestack in 2012 and 2013, and more in 2016 and 2017. York Hall, the hospital\'s auditorium, church and theatre at the park entrance, was put on the National Register on October 23, 2023, and State Parks has sought a partner to restore it as a performance hall.',
  'Many hospital buildings still stand empty and covered in graffiti across the park, Building 93 the tallest of them, with York Hall at the entrance. Look from the park roads and the Greenbelt Trail only: entering the buildings is illegal and State Park Police patrol the grounds. Interiors are closed.',
  'A 111-year asylum town, now half park and half shell.',
  'Nissequogue River State Park (NYS Parks). Its page (read November 2026) says the grounds are open year round from sunrise to sunset and the main grounds entrance south of St. Johnland Road has no fee; the marina area charges a vehicle fee in summer. The Long Island Greenbelt Trail runs along the bluffs above the river. Every building is closed: do not go in. Mapped lot on Garage Road inside the park.',
  [W('Kings Park Psychiatric Center'),['NYS Parks: Nissequogue River State Park','https://www.parks.ny.gov/parks/nissequogueriver/details.aspx'],['NYS Parks: State Parks seeks partnerships to renew York Hall','https://parks.ny.gov/news/press-releases/state-parks-seeks-partnerships-renew-york-hall-nissequogue-river-state-park'],['Preservation Long Island: York Hall added to the National Register','https://preservationlongisland.org/preservation-update-york-hall-added-to-national-register-of-historic-places/']],
  th=[40.89800,-73.23417],thn='Park lot on Garage Road',brick='?',hours='Park grounds sunrise to sunset, year round; buildings closed'),

N('stony-brook-grist-mill','Stony Brook Grist Mill','Stony Brook','nyc','industry','standing',40.91491,-73.14767,'exact','open','walk','','c. 1751',
  'A mill was first built here in 1699, damming the Mill Pond on the line between Brookhaven and Smithtown; the present mill dates from about 1751. In the late 1800s grapes from a vineyard on the pond\'s island were pressed and fermented in it, and farmers still brought wheat and corn to be ground into the 1950s, when the miller shipped his whole-wheat "health food" to 42 states. A storm in August 2024 washed out the road beside it and drained the pond into the harbour; the mill itself was not damaged but was buried in sand.',
  'The Ward Melville Heritage Organization calls it Long Island\'s most completely equipped working mill. Tours are led by a miller or guide, with a small country store. Interior not described beyond that.',
  '',
  'Owned and run by the Ward Melville Heritage Organization at 100 Harbor Road. Its page (read November 2026): guided tours and the country store Sundays 1 to 4 p.m., April through October; $4 adults, $2 children. A mapped lot off Main Street in Stony Brook village is about 200 m away.',
  [W('Stony Brook Grist Mill'),['Ward Melville Heritage Organization: properties','https://wmho.org/properties/']],
  th=[40.91648,-73.14677],thn='Lot off Main Street, Stony Brook',brick='?',hours='Sundays 1 to 4 p.m., April to October ($4 adults, $2 children)'),

N('william-sidney-mount-house-stony-brook','Hawkins-Mount House (William Sidney Mount House)','Stony Brook','nyc','landmark','standing',40.90686,-73.13838,'exact','open','drive','','1725',
  'Eleazer Hawkins built the left half of this house about 1725 as an "ordinary", a tavern; it was enlarged about 1810. It was the lifelong home of the genre painter William Sidney Mount (1807–1868), Hawkins\'s grandson, who had his studio in the attic, and it was made a National Historic Landmark in 1965.',
  'A broad seven-bay shingled house with two front doors at the corner of North Country Road (Route 25A) and Stony Brook Road. Wikipedia says it has more than twenty rooms, among them the restored original tavern kitchen and Mount\'s attic studio.',
  '',
  'Owned by the Long Island Museum, at 1556 Stony Brook Road. Wikipedia says it is opened only occasionally; the museum lists special "Hawkins-Mount House" tours as events on its calendar (read November 2026), with no standing hours. The house is otherwise seen from the road.',
  [W('William Sidney Mount House'),['Long Island Museum: Hawkins-Mount House tours','https://longislandmuseum.org/event/hawkins-mount-house-tours/']],
  brick='?',hours='?'),

N('thompson-house-setauket','Thompson House','Setauket','nyc','landmark','standing',40.93352,-73.11778,'exact','open','drive','','1709',
  'A timber-frame saltbox built in 1709, with a steep, uneven gable roof, a one-storey wing and a central chimney. It was the home of the Thompson family; an exhibit opened by the Ward Melville Heritage Organization in July 2026 argues from new finds that Jonathan Thompson (1710–1786) and Dr. Samuel Thompson stayed in Setauket through the seven years of British occupation, and that British troops used the house, rather than the family fleeing to Connecticut as long believed.',
  'The saltbox roof sweeping low at the back is the thing to see from North Country Road. Inside is the "Out of the Shadows" exhibit on the family in the Revolution; interior fabric not checked.',
  '',
  'Exhibit run by the Ward Melville Heritage Organization at 91 North Country Road (its page, read November 2026, gives no hours: call 631-751-2244). '+TOWN,
  [W('Thompson House (Setauket, New York)'),['Ward Melville Heritage Organization: Out of the Shadows, Thompson House exhibit','https://wmho.org/out-of-the-shadows-thompson-house-exhibit-coming-soon/']],
  brick='?',hours='?'),

N('sherwood-jayne-farm-east-setauket','Sherwood-Jayne Farm','East Setauket','nyc','landmark','standing',40.93952,-73.08868,'exact','open','drive','','c. 1730',
  'A two-storey, six-bay saltbox farmhouse begun about 1730 and added to into the 1900s, including a north wing by the architect Arthur C. Nash. A barn, carriage house, corn crib, privy and pump house stand with it among split-rail and picket fences. It belongs to Preservation Long Island, which furnished it with period antiques.',
  'The farmhouse and its five outbuildings in their old fenced landscape. Preservation Long Island shows the house on seasonal tours; the grounds and a three-mile Suffolk County nature trail along the moraine behind are open all year.',
  '',
  'Owned by Preservation Long Island, 55 Old Post Road. Its page (read November 2026): house tours seasonally, June to October (days not given there; booking through its tours page; private tours $12 a person, $120 minimum); the grounds and the county nature trail are open year round dawn to dusk. Dogs are not allowed on the trails. Parking not checked on the ground.',
  [W('Sherwood-Jayne House'),['Preservation Long Island: Sherwood-Jayne Farm','https://preservationlongisland.org/sherwood-jayne-farm/'],['Preservation Long Island: tours','https://preservationlongisland.org/tours/']],
  brick='?',hours='House tours June to October; grounds and nature trail dawn to dusk, year round'),

N('brewster-house-east-setauket','Brewster House','East Setauket','nyc','landmark','standing',40.94338,-73.10289,'exact','view','drive','','1665',
  'Built in 1665 and enlarged in the early 1700s, it is called the oldest house in the Town of Brookhaven, and six generations of Brewsters lived in it. In the Revolution Joseph Brewster ran it as a tavern and general store and served British troops in it, while his cousin Caleb Brewster rowed for Washington\'s Culper spy ring. It was restored in 1968 to look as it does in William Sidney Mount\'s 1845 painting "Long Island Farmhouses".',
  'The restored shingled farmhouse that Mount painted. Interior not checked.',
  '',
  'Owned by the Ward Melville Heritage Organization; its properties page (read November 2026) gives the history but no visiting hours, so it is marked view only from the road. '+TOWN,
  [W('Brewster House (East Setauket, New York)'),['Ward Melville Heritage Organization: properties','https://wmho.org/properties/']],
  brick='?'),

N('caroline-church-setauket','Caroline Church and burying ground','Setauket','nyc','worship','standing',40.94673,-73.11222,'exact','open','walk','','1729',
  'The parish was organized in 1723 as Christ Church and renamed for Queen Caroline of England; the church was built in 1729 and still stands where it was put up, above the Setauket village green. It is a heavy timber-framed building, 42 by 30 feet, sheathed in wood shingles, with a 42-foot tower and a 25-foot spire. The cemetery began in 1734; the parish house dates from 1905 and the barn from 1893.',
  'The shingled colonial church and its spire, and the 18th- and 19th-century gravestones round it. Interior not checked.',
  '',
  'An active Episcopal parish at the junction of Dyke and Bates roads; anyone may attend its services (times from its page, read November 2026). '+TOWN,
  [W('Caroline Church and Cemetery'),['Caroline Church of Setauket','https://carolinedev.squarespace.com']],
  brick='no',hours='Saturday 5 p.m.; Sunday 8 and 9:30 a.m.'),

N('setauket-presbyterian-church','Setauket Presbyterian Church and burying ground','Setauket','nyc','worship','standing',40.94598,-73.11093,'exact','open','walk','','1812',
  'The First Presbyterian Church of Brookhaven. An earlier church on the village green burned after a lightning strike; this Federal-style church, timber-framed and shingled with a bell tower over the entrance, was built in 1812. The burying ground was begun in the 1660s and holds about 800 graves, among them early ministers and Abraham Woodhull, leader of the Culper spy ring, and Benjamin Tallmadge, father of the Revolutionary officer. In August 1777 the churchyard was a Loyalist fort attacked by Continental troops from Connecticut.',
  'The white shingled church on the green and the old graves behind. The church says history visitors often come to walk the graveyard and see the sanctuary. Interior not checked.',
  '',
  'An active congregation at 5 Caroline Avenue on the Setauket green; worship Sundays at 9:30 and 11 a.m. (its page, read November 2026). '+TOWN,
  [W('Setauket Presbyterian Church and Burial Ground'),['Setauket Presbyterian Church','https://www.setauketpresbyterian.org']],
  brick='no',hours='Sunday 9:30 and 11 a.m.'),

N('frank-melville-memorial-park-setauket','Frank Melville Memorial Park and its mill house','Setauket','nyc','inst','standing',40.94672,-73.11670,'site','public','walk','','1937',
  'Ward Melville set up the park in 1937 round the Melville Mill Pond, in memory of his father, Frank Melville Jr.; mills have stood on the pond since about 1660. The present mill house, with a working imitation wheel, dates from 1937 and is the park office. The Satterly Barn is from the early 1700s, re-sided in 1968, and the John Satterly House nearby was restored the same year. The park was put on the National Register in 2010.',
  'The park\'s own page counts five historic buildings: a Greek Revival post office, the replica grist mill, the last miller\'s cottage, a 20th-century barn and the Bates House, with trails down toward Conscience Bay and Caroline Church.',
  '',
  'Run privately by the park\'s foundation at 1 Old Field Road; its page (read November 2026) says it is free and open to all. A mapped lot is on Bates Road. Opening times not given on the page read.',
  [W('Frank Melville Memorial Park'),['Frank Melville Memorial Park','https://www.frankmelvillepark.org/']],
  th=[40.94887,-73.11461],thn='Lot on Bates Road',brick='?'),

N('old-field-point-light','Old Field Point Light','Old Field','nyc','light','standing',40.97691,-73.11862,'exact','open','drive','','1823; present light 1868',
  'The first lighthouse on the point between Port Jefferson and Stony Brook harbours was built in 1823–24 and lit by nine whale-oil lamps. The present lighthouse of 1868 burned kerosene, and an automatic revolving light was put in in 1933. The government gave it to the Village of Old Field in 1935 for a public park, took it back for the Coast Guard in the Second World War, and returned it afterwards; the lighthouse is now the village hall. The light, keeper\'s house and oil shed are on the State and National Registers (2024).',
  'The lighthouse, keeper\'s house and oil shed on the point over Long Island Sound. The village says it needs a major restoration and is raising money for it.',
  '',
  'Owned by the Village of Old Field, whose page (read November 2026) invites all to visit the lighthouse and grounds; the village clerk, in the building Monday, Tuesday and Thursday 9 a.m. to 3 p.m., stamps the lighthouse passport. A paved lot lies southwest of the lighthouse.',
  [W('Old Field Point Light'),['Village of Old Field: Preserving and restoring the lighthouse','https://oldfieldny.org/preserving-restoring-the-lighthouse/']],
  th=[40.97582,-73.11967],thn='Paved lot southwest of the lighthouse',brick='?',hours='Grounds open to visitors; village clerk in the lighthouse Monday, Tuesday and Thursday 9 a.m. to 3 p.m.'),

N('bayles-shipyard-port-jefferson','Bayles Shipyard buildings','Port Jefferson','nyc','industry','standing',40.94840,-73.06756,'site','public','walk','','1897–1917',
  'What is left of Port Jefferson\'s Bayles shipyard: the 1897 Bayles Chandlery, the 1917 machine shop and mould loft, and the 1917 compressor house, put on the National Register in 2000. The machine shop and mould loft is now the Port Jefferson Village Center, and the old Mobil oil terminal beside it became the Jeanne Garant Harborfront Park in 2004.',
  'The big former mould loft (the Village Center) and the smaller chandlery and compressor house at the harbour edge, seen from Harborfront Park.',
  '',
  'Owned by the Village of Port Jefferson; Harborfront Park round the buildings is public. Village Center opening hours not checked. A mapped lot is on East Broadway beside it.',
  [W('Bayles Shipyard')],
  th=[40.94833,-73.06849],thn='Lot on East Broadway',brick='?'),

N('mather-house-museum-port-jefferson','Mather House Museum','Port Jefferson','nyc','landmark','standing',40.94599,-73.06561,'exact','open','walk','','c. 1840–1860',
  'The house of the Mathers, 19th-century Port Jefferson shipbuilders, built about 1840 to 1860; John T. Mather made possible the community hospital that still carries his name. It is the headquarters of the Historical Society of Greater Port Jefferson, with outbuildings: the Spinney Clock Building (2002), a re-created country store, barber shop, butcher shop and post office in the Sherman Mills Country Shops, and an herb garden.',
  'The house and its museum outbuildings at 115 Prospect Street; guided tours.',
  '',
  'Run by the Historical Society of Greater Port Jefferson; its home page (read November 2026) gives the season. '+TOWN,
  [W('Mather House Museum'),['Historical Society of Greater Port Jefferson','https://portjeffhistorical.org/'],['The museum complex','https://portjeffhistorical.org/museum-complex']],
  brick='?',hours='Wednesday to Sunday noon to 4 p.m., late May to mid-October'),

N('first-national-bank-port-jefferson','First National Bank of Port Jefferson','Port Jefferson','nyc','civic','standing',40.94528,-73.06833,'area','view','walk','','',
  'A brick bank building with a two-storey turret under a steep cone-shaped slate roof at its corner; the entrance under the turret was made into a window about 1949, when the Town of Brookhaven, which bought it in 1948, added a one-storey wing. The town used it as its tax office; a plan for a Long Island Music Hall of Fame in 2011 came to nothing, and in 2016 it was remodelled with a shop downstairs and two apartments upstairs. It was put on the National Register in 2005.',
  'The turret corner with its slate cone. The old vault was reported in 2021 to be a shop dressing room. Interior not checked.',
  '',
  'Privately used (shop and apartments); look from the street in the village centre. '+TOWN,
  [W('First National Bank of Port Jefferson')],
  brick='?'),

N('william-miller-house-miller-place','William Miller House','Miller Place','nyc','landmark','standing',40.95799,-73.00490,'area','open','drive','','1720',
  'Built in 1720, with additions in 1750 and 1816; much of the inside has been left unchanged since the Miller Place-Mount Sinai Historical Society bought it in 1979 and made it its headquarters. It stands at the west end of the Miller Place Historic District, the first Register district in the Town of Brookhaven (1976), a mile-long run of 18th- and 19th-century wood-frame houses and the old Miller Place Academy along North Country Road.',
  'The house and its clothesline, which the society uses to hang messages (overalls upside down mean it is closed). Walk on east along North Country Road and Lower Rocky Point Road for the rest of the historic district.',
  '',
  'The Miller Place-Mount Sinai Historical Society, 75 North Country Road. A TBR News Media report gave tours on Saturdays noon to 2 p.m. and by appointment for groups; the society\'s own page could not be opened when this was written, so hours not checked. '+TOWN,
  [W('Miller Place Historic District'),['TBR News Media: History in full view at William Miller house','https://tbrnewsmedia.com/?p=5039']],
  brick='?',hours='?'),

N('st-james-general-store','St. James General Store','St. James','nyc','civic','standing',40.88777,-73.16185,'exact','open','drive','','1857',
  'Ebenezer Smith, a descendant of Smithtown\'s founder, built the store in 1857 after trading out West and trying the California gold rush. It served farmers and sailors, held the post office and later the hamlet\'s first telephone. Run by Karl Ericson until he was 90, then the Havriskos from 1959 and the Oakleys from 1980, it was bought by Suffolk County Parks in 1990 and dedicated to the county\'s Historical Trust.',
  'A working general store in its 19th-century building at Moriches and Harbor Hill roads, selling Victorian-style goods, with a post office sub-station inside (county page). Interior fabric not checked.',
  '',
  'Owned by Suffolk County Parks, 516 Moriches Road; the county page (read November 2026) says it is open year round but gives no hours. Parking not checked on the ground.',
  [W('St. James General Store'),['Suffolk County Parks: St. James General Store','https://www.suffolkcountyny.gov/Departments/Parks/Historic-Sites/St-James-General-Store']],
  brick='?',hours='?'),

N('blydenburgh-new-mill-smithtown','Blydenburgh Farm and New Mill','Smithtown','nyc','industry','standing',40.84304,-73.22789,'exact','public','walk','','1798',
  'Isaac Blydenburgh and his cousins Joshua and Caleb Smith dammed the head of the Nissequogue River in 1798 for a grist mill, making Stump Pond. The mill, the 1802 miller\'s house, the Blydenburgh farmhouse, an 1860 farm cottage and farm outbuildings make the Blydenburgh Park Historic District (1983). The mill was in poor shape when documented in 1980, with its frame intact and some machinery left. The New Mill dam and spillway failed in an extreme rainstorm in August 2024 and the pond drained; in July 2026 Suffolk County cleared a plan to rebuild them with a fish passage and a footbridge to rejoin the Greenbelt Trail.',
  'The mill, the miller\'s house, the Blydenburgh-Weld farmhouse and ice house at the north end of the park, and the broken dam. The mill\'s state since the 2024 storm was not checked.',
  '',
  'Blydenburgh County Park (Suffolk County Parks). The county page (read November 2026) says the New Mill Road entrance, the nearest to the mill, has been closed since August 20, 2024, and that guided tours of the farm and mill district run Saturdays at 1 p.m. (call 631-360-0753, the Long Island Greenbelt Trail Conference). A Clio entry says the park is for county residents and their guests, 8 a.m. to 3:30 p.m.; not checked on the county page. The Greenbelt Trail runs round the pond.',
  [W('Blydenburgh Park Historic District'),['Suffolk County Parks: Blydenburgh County Park','https://suffolkcountyny.gov/Departments/Parks/Our-Parks/Blydenburgh-County-Park'],['NYS DEC: New Mill Dam reconstruction (July 2026)','https://dec.ny.gov/news/environmental-notice-bulletin/2026-07-15/seqr/town-of-smithtown-proposed-new-mill-dam-reconstruction-project-at-blydenburgh-county-park'],['Clio: Blydenburgh Farm and New Mill','https://theclio.com/entry/130327']],
  brick='?',hours='Guided tours of the farm and mill Saturdays 1 p.m.',conf='mixed'),

N('caleb-smith-house-wyandanch-club','Wyandanch Club, Caleb Smith State Park Preserve','Smithtown','nyc','inst','standing',40.85272,-73.22538,'site','open','walk','','1753',
  'Caleb Smith (1724–1800), great-grandson of Smithtown\'s founder Richard "Bull" Smith, and his father built a house here in 1753 (that house was moved behind the Smithtown library in the 1950s). The Brooklyn Gun Club bought the estate by 1888 and named it the Wyandanch Club in 1893, a hunting and fishing preserve, and the state took it in 1963. The club grounds are a Register historic district (1990) inside the 543-acre preserve.',
  'The old club buildings by the lake, a visitor centre with a nature museum and wildlife displays, and trails along two branches of the Nissequogue River.',
  '',
  'Caleb Smith State Park Preserve (NYS Parks), 581 West Jericho Turnpike. Its page (read November 2026): open Tuesday to Sunday, closed Mondays except holidays; no pets, bikes, picnics or metal detecting; a permit is needed for posed photography. Vehicle fee in season.',
  [W('Caleb Smith State Park Preserve'),['NYS Parks: Caleb Smith State Park Preserve','https://parks.ny.gov/parks/calebsmith/details.aspx']],
  brick='?',hours='Tuesday to Sunday 9 a.m. to 5 p.m. April to mid-November, 9 to 4 mid-November to March; closed Mondays except holidays'),
]

PIN_NOTES={
 'kings-park-psychiatric-center':'Moved 43 m from the Register point for York Hall (which fell on the road) onto the large building east of it seen on the aerial; the campus spreads over several hundred acres round it.',
 'stony-brook-grist-mill':'ArcGIS PointAddress for 100 Harbor Road; Wikipedia\'s point is 3 m away.',
 'william-sidney-mount-house-stony-brook':'ArcGIS PointAddress for 1556 Stony Brook Road.',
 'thompson-house-setauket':'ArcGIS PointAddress for 91 North Country Road; Wikipedia\'s point is the same.',
 'sherwood-jayne-farm-east-setauket':'ArcGIS PointAddress for 55 Old Post Road; Wikipedia\'s point is 12 m away.',
 'brewster-house-east-setauket':'OpenStreetMap building named Brewster House; Wikipedia\'s point is the same.',
 'caroline-church-setauket':'ArcGIS PointAddress for 1 Dyke Road.',
 'setauket-presbyterian-church':'Wikipedia point on the church at the Setauket green; the street-address lookup for 5 Caroline Avenue fell 360 m north and was not used.',
 'frank-melville-memorial-park-setauket':'ArcGIS PointAddress for 1 Old Field Road, the park\'s address.',
 'old-field-point-light':'OpenStreetMap lighthouse; the ArcGIS point for 207 Old Field Road is the same.',
 'bayles-shipyard-port-jefferson':'ArcGIS PointAddress for 101 East Broadway, the Village Center; the Register point is 70 m west.',
 'mather-house-museum-port-jefferson':'ArcGIS PointAddress for 115 Prospect Street.',
 'first-national-bank-port-jefferson':'Wikipedia point, on a large flat-roofed building in the village centre; the turreted bank could not be picked out on the aerial and no street address was found in a source, so the pin marks the block only.',
 'william-miller-house-miller-place':'ArcGIS street-address match (interpolated) for 75 North Country Road; on the aerial it falls on the road, and which house is the Miller House could not be told, so the pin marks the area only.',
 'st-james-general-store':'ArcGIS PointAddress for 516 Moriches Road.',
 'blydenburgh-new-mill-smithtown':'OpenStreetMap building named New Mill, 150 m from the Register point for the district.',
 'caleb-smith-house-wyandanch-club':'ArcGIS PointAddress for 581 West Jericho Turnpike, the park\'s address; the Register point for the district is 290 m southwest.',
}
