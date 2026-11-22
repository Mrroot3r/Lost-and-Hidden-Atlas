# November 22, 2026: a second scatter across Florida, which was again the state with the fewest places that nobody held
# (tools/choose.py --thinnest). Nineteen places from DeFuniak Springs to Key West, none of them on the map before:
# a Chautauqua hall, a Carpenter Gothic church, antebellum and pioneer houses, a farm, a 1930s lodge, a sugar-mill ruin,
# Spanish-American War batteries, a Life-Saving Service house of refuge, two lighthouses, Gilded Age hotels and estates,
# a twelfth-century Spanish cloister rebuilt in Miami, a coral-rock garden, a derelict Flagler rail bridge, a wreckers'
# ghost town and a Civil War tower fort.
# Sources read in this session: Wikipedia articles and Register lists (tools/wiki_raw.py); the operators' own pages read
# with tools/page.py (Florida State Parks system guide booklet, Volusia County, Pinellas County, Ponce de Leon Inlet
# Lighthouse, Plant Museum, The Ringling, Edison Ford, Historical Society of Martin County, Jupiter Inlet Lighthouse,
# Ancient Spanish Monastery, Coral Castle, Key West Art & Historical Society, St. Mary's Madison, the Lodge at Wakulla
# Springs); one HMdb marker. Nothing was checked on the ground.
from data_b import N
from data_ma import W
BATCH={'key':'fl_ajmb','label':'Florida: second scatter, DeFuniak Springs to Key West','added':'2026-11-22 13:24'}

FSP=['Florida State Parks system guide (PDF; hours where it gives them)','https://www.floridastateparks.org/sites/default/files/media/file/FSPSystemGuide_Booklet_ForReview-1.pdf']
SPN=' The park\'s own web page refused to open (HTTP 403) when this was written, so hours not given here are not checked.'

PLACES=[
N('chautauqua-hall-of-brotherhood','Chautauqua Hall of Brotherhood','DeFuniak Springs','fl','civic','standing',30.71682,-86.11593,'exact','view','walk','','1909',
  'The grand entrance of a 4,000-seat auditorium opened in 1909 for the lectures of the Florida Chautauqua Assembly, the winter education resort on the round lake at DeFuniak Springs. It replaced a 2,500-seat tabernacle that had grown too small; speakers included Vice President Thomas Marshall and William Jennings Bryan. The auditorium behind it was destroyed by a hurricane in 1975 (the state marker calls it Hurricane Boise); the columned front survives and was listed on the National Register in 1972.',
  'The wooden front, designed to look like the United States Capitol, with columns that two senators, George Wetmore of Rhode Island and one from New York, each sponsored in the fund drive (state marker). It stands at 95 Circle Drive on Lake DeFuniak and has housed a branch of the Walton County Chamber of Commerce (Wikipedia). Interior not checked.',
  'A Capitol-style wooden front is all that is left of a 4,000-seat lecture hall.',
  'Owner and opening times not checked; Wikipedia says a branch of the Walton County Chamber of Commerce is housed there. It is seen from Circle Drive, the street round Lake DeFuniak. Street parking on Circle Drive was not checked.',
  [W('Chautauqua Hall of Brotherhood'),['HMdb: Chautauqua Hall of Brotherhood (state marker)','https://www.hmdb.org/m.asp?m=269668']],
  brick='no'),

N('st-marys-episcopal-church-madison','St. Mary\'s Episcopal Church','Madison','fl','worship','standing',30.46993,-83.41357,'site','open','walk','','1879–1881',
  'A Carpenter Gothic church in Madison, the county seat on the old road across north Florida. The parish was organized in 1859, lapsed during the Civil War and was re-formed in 1879; the cornerstone was laid in August 1879, the church was finished in 1881 and consecrated in 1883 (the parish gives May 27, Wikipedia May 1). It was listed on the National Register in 1997.',
  'A small wooden church with a steep roof, scissor trusses inside, pointed-arch windows and doors and stained glass (the parish\'s own page). Sunday service is open to all.',
  '',
  'St. Mary\'s Episcopal Church, 140 NE Horry Avenue, Madison (the parish\'s page). Street parking not checked.',
  [W('St. Mary\'s Episcopal Church (Madison, Florida)'),['St. Mary\'s Madison: about','https://stmarysofmadison.org/about-st-marys'],['St. Mary\'s Madison: services','https://stmarysofmadison.org/services']],
  conf='mixed',hours='Sunday service 10 a.m. (Rite I on the first Sunday)',brick='no'),

N('orman-house-apalachicola','Orman House','Apalachicola','fl','landmark','standing',29.73015,-84.98993,'exact','open','walk','','1838',
  'The house of Thomas Orman, built in 1838 on a rise above the Apalachicola River in the cotton port of Apalachicola, and used for both business and gatherings. Its doors, windows, trim and finished woodwork were made in Syracuse, New York, shipped by sea and put together on the site. It is now a state park.',
  'Federal and Greek Revival details, wooden mantelpieces, moulded plaster cornices and wide heart-pine floorboards (state parks guide), shown by tour. The Chapman Botanical Garden is beside it.',
  '',
  'Orman House Historic State Park, 177 5th Street, Apalachicola (Florida State Parks). Wikipedia gives tours Monday and Thursday to Sunday, 9 a.m. to 5 p.m., with a small fee, but that was not read on the park\'s own page.'+SPN+' Parking not checked.',
  [W('Orman House Historic State Park'),FSP],
  hours='?',brick='no'),

N('lodge-at-wakulla-springs','The Lodge at Wakulla Springs','Wakulla Springs','fl','hotel','standing',30.23415,-84.30188,'exact','open','drive','hotels','1935–1937',
  'A hotel built in 1935–1937 by the financier Edward Ball beside Wakulla Springs, which he had bought in 1931 to keep it from being developed. Scenes for Tarzan\'s Secret Treasure (1941) and Creature from the Black Lagoon (1954) were filmed at the spring. The lodge still takes guests, inside Edward Ball Wakulla Springs State Park, and belongs to Historic Hotels of America.',
  'Tennessee marble on the floors, stairs and counters, a 70-foot marble soda-fountain bar, an Art Deco elevator panelled in walnut marquetry, and a lobby ceiling of cypress beams painted with Florida scenes that was conserved from 2002 (the lodge\'s history page; Wikipedia). It has 27 guest rooms, a dining room and a gift shop, open year-round (state parks guide).',
  'A 1930s lodge on the spring where the Creature from the Black Lagoon swam.',
  'Edward Ball Wakulla Springs State Park, 465 Wakulla Park Drive (Florida State Parks); the lodge is at 550 Wakulla Park Drive and is run by a concessioner. The park charges an entrance fee (not checked).'+SPN+' Park in the lot south of the lodge.',
  [W('Lodge at Wakulla Springs'),['The Lodge at Wakulla Springs: history','https://thelodgeatwakullasprings.com/history-2/'],FSP],
  th=[30.23367,-84.30184],thn='Lodge lot, south of the lodge',hours='Lodge open year-round; park hours not checked',brick='?'),

N('dudley-farm-newberry','Dudley Farm','Newberry','fl','landmark','standing',29.65884,-82.53993,'area','open','drive','','1850s–1940s',
  'A family farm worked by three generations of the Dudley family from the 1850s to the 1940s, and by a few of them for their own needs into the 1990s. Myrtle Dudley, the last of the third generation, died in 1996 and left it to the Florida Park Service. It is a National Historic Landmark since 2021.',
  'Twenty-one historic buildings and 13 structures on about 325 acres: the farmhouse, an 1880s kitchen, a general store and post office, and a cane-syrup works, with their original furnishings and equipment (Wikipedia). It is run as a working farm, with cane boils and other demonstrations through the year.',
  '',
  'Dudley Farm Historic State Park, 18730 W. Newberry Road (State Road 26), Newberry (Florida State Parks). Visitor parking is in the south part of the park (Wikipedia).'+SPN,
  [W('Dudley Farm Historic State Park'),FSP],
  th=[29.65643,-82.54148],thn='Visitor center lot, West Newberry Road',hours='Self-guided tours Wednesday to Sunday 9 a.m. to 4 p.m.',brick='no'),

N('marjorie-kinnan-rawlings-home','Marjorie Kinnan Rawlings home','Cross Creek','fl','landmark','standing',29.48174,-82.15993,'exact','open','drive','','19th century',
  'The orange-grove farmhouse at Cross Creek where the novelist Marjorie Kinnan Rawlings lived and wrote after she and her husband bought the 75-acre grove with its old dogtrot house in 1929. She won the Pulitzer Prize in 1939 for The Yearling. It is a National Historic Landmark and a state park.',
  'A rambling one-storey frame house whose core is a 19th-century dogtrot, with a pump house, a barn and a small tenant house, and orange trees round it. The house is shown by tour; the farm is kept as in the 1930s (state parks guide).',
  '',
  'Marjorie Kinnan Rawlings Historic State Park, 18700 S. County Road 325, Cross Creek (Florida State Parks). Public parking and a boat ramp are south of the house (Wikipedia).'+SPN,
  [W('Marjorie Kinnan Rawlings Historic State Park'),FSP],
  th=[29.48,-82.15993],thn='Park lot south of the house',hours='Grounds daily 9 a.m. to 5 p.m.; house tours six times a day Thursday to Sunday; closed Thanksgiving and Christmas',brick='no'),

N('dunlawton-sugar-mill-ruins','Dunlawton Plantation sugar mill ruins','Port Orange','fl','industry','ruins',29.14083,-81.00611,'site','public','walk','','1804–1836',
  'A sugar and indigo plantation of 995 acres granted by the Spanish Crown in 1804 and worked by enslaved Africans. The Anderson family bought it in 1832 and made sugar, molasses and rum there until the Second Seminole War: in January 1836 soldiers found the house and slave cabins burning, though the mill was only partly destroyed. The ruins sit in Dunlawton Sugar Mill Gardens, given to Volusia County in 1963.',
  'Ruins of coquina-block and brick buildings, with the gears of the cane press, iron boiling kettles and the steam furnace and piston works (Wikipedia), behind a fence with signs. The gardens round them also hold big concrete dinosaurs left from a 1950s attraction.',
  'Sugar-mill ruins guarded by concrete dinosaurs.',
  'Volusia County park, 950 Old Sugar Mill Road, Port Orange, run by the volunteer Botanical Gardens of Volusia; free. When this was written the county\'s page said the gardens were closed because of high water. Visitor parking on Old Sugar Mill Road.',
  [W('Dunlawton Plantation and Sugar Mill'),['Volusia County: Dunlawton Sugar Mill Gardens','https://www.volusia.org/services/community-services/parks-recreation-and-culture/parks-and-trails/park-facilities-and-locations/historical-parks/dunlawton-sugar-mill-gardens.stml']],
  th=[29.14061,-81.00610],thn='Sugar Mill visitor parking',hours='Daily 8 a.m. to 5 p.m.; closed Christmas and New Year\'s Day (closed for high water, November 2026)',brick='some'),

N('ponce-de-leon-inlet-light','Ponce de Leon Inlet Light','Ponce Inlet','fl','light','standing',29.08062,-80.92802,'exact','open','drive','','1887',
  'At 175 feet the tallest lighthouse in Florida, lit in 1887 on the north side of the inlet once called Mosquito Inlet. An earlier tower of 1835 on the south side never worked and fell. The town took over the station from the Coast Guard in 1972 and a preservation association restored it; it is a National Historic Landmark.',
  'The tower can be climbed. Three keepers\' houses are restored, and the museum shows the 1867 first-order lens first lit here, the 1860 rotating lens from Cape Canaveral, and the 1904 third-order lens that is back in service in the tower (Wikipedia). The Pacetti Hotel museum is on the same ground. In a 2018 photograph the tower is painted red-orange and a keeper\'s house beside it shows red brick.',
  '',
  'Ponce de Leon Inlet Lighthouse & Museum, 4931 S. Peninsula Drive; admission charged. Last admission an hour before closing; the tower closes in storms. Parking lot on South Peninsula Drive.',
  [W('Ponce de Leon Inlet Light'),['Ponce Inlet Lighthouse: hours','https://www.ponceinlet.org/visit/hours-of-operation']],
  th=[29.08003,-80.92742],thn='Lighthouse lot, South Peninsula Drive',hours='Daily 10 a.m. to 6 p.m., to 9 p.m. Memorial Day to Labor Day; closed Thanksgiving and Christmas',brick='some'),

N('tampa-bay-hotel-plant-hall','Tampa Bay Hotel (Plant Hall)','Tampa','fl','hotel','standing',27.9468,-82.46402,'site','open','walk','hotels','1888–1891',
  'Henry B. Plant\'s 511-room resort hotel at the end of his railway, opened in 1891 in the Moorish Revival style, with the first elevator in Florida and electric light and telephones in every room. Theodore Roosevelt and the Rough Riders were stationed there in the Spanish–American War of 1898. It ran as a hotel until 1932 (the museum) or 1930 (Wikipedia), and since 1933 has housed the University of Tampa; the south wing is the Henry B. Plant Museum.',
  'Six minarets, four cupolas and three domes over five storeys, trimmed with gingerbread. The museum keeps rooms as the first guests knew them, with the hotel\'s own furnishings, and the old elevator still works (Wikipedia; museum page).',
  'Moorish minarets over the hotel where the Rough Riders waited for Cuba.',
  'Henry B. Plant Museum, 401 W. Kennedy Boulevard, on the University of Tampa campus; admission charged. Parking in front of the museum, or the free Thomas Parking Garage about five minutes\' walk through campus (museum page).',
  [W('Henry B. Plant Museum'),['Plant Museum: visit','https://www.plantmuseum.com/discover/visit-accessibility'],['Plant Museum','https://plantmuseum.com/discover']],
  conf='mixed',hours='Tuesday to Saturday 10 a.m. to 5 p.m.',brick='?'),

N('fort-de-soto-batteries','Fort De Soto batteries','Tierra Verde (Mullet Key)','fl','fort','ruins',27.6155,-82.7359,'site','public','drive','forts','1898–1906',
  'A coast-defence fort built on Mullet Key from 1898 to 1906 to guard the mouth of Tampa Bay, active until 1910 and then left to a caretaker. Battery Bigelow was destroyed in 1932; Battery Laidley still stands. The islands became a Pinellas County park after the state road reached them in 1962, and the batteries were listed on the National Register in 1977.',
  'Battery Laidley\'s concrete walls and mortar pits, with four 12-inch mortars of 1890 and two 6-inch Armstrong guns, said to be the only ones of their kind left in the United States. A rebuilt quartermaster storehouse of 1999 holds a small museum (Wikipedia).',
  'The last 12-inch coast mortars in the country, still in their pits.',
  'Fort De Soto Park (Pinellas County), reached by the toll road from the mainland; the county charges a $6 parking fee. Lot by the battery, beside the 1898 brick road.',
  [W('Fort De Soto Park'),['Pinellas County: Fort De Soto Park','https://pinellas.gov/parks/fort-de-soto-park/']],
  th=[27.61428,-82.73583],thn='Battery lot by the 1898 brick road',hours='Daily 7 a.m. to sunset',brick='no'),

N('ca-d-zan-sarasota','Ca\' d\'Zan','Sarasota','fl','landmark','standing',27.38306,-82.56472,'exact','open','walk','','1924–1926',
  'The winter house of the circus owner John Ringling and his wife Mable on Sarasota Bay, built in 1924–1926 and named "House of John" in Venetian. It mixes Venetian Gothic with Italian Renaissance, Moorish and Spanish ideas. Ringling left it to the state with his art museum; it opened to the public in 1946 and was restored from 1996 to 2002.',
  'Fifty-six rooms behind a front of coloured terra cotta made in Pennsylvania, with Gothic-arched windows; the first floor holds the great hall, ballroom and other rooms for entertaining (Wikipedia). Shown by ticket, with guided tours on offer.',
  '',
  'The Ringling (Florida State University), 5401 Bay Shore Road, Sarasota; tickets for Ca\' d\'Zan are sold with the museums. Last entry 30 minutes before closing; closed Thanksgiving, Christmas and New Year\'s Day. Parking at the estate (the Ringling\'s page gives directions).',
  [W('Ca\' d\'Zan'),['The Ringling: helpful info','https://ringling.org/visit/help']],
  hours='Daily 10 a.m. to 5 p.m.',brick='no'),

N('edison-ford-winter-estates','Edison and Ford Winter Estates','Fort Myers','fl','landmark','standing',26.63472,-81.88,'site','open','walk','','1886',
  'Thomas Edison bought land beside the Caloosahatchee River in 1885 and finished his winter house, Seminole Lodge, in 1886; he came until his death in 1931. Henry Ford bought the house next door, The Mangoes, in 1916. Mina Edison gave the Edison property to the city, it has been open since 1947, and a nonprofit runs it.',
  'The two houses, the 1928 Edison Botanic Research laboratory (a National Historic Chemical Landmark), a museum and about 20 acres of gardens with a banyan tree planted in the 1920s (Wikipedia).',
  '',
  'Edison & Ford Winter Estates, 2350 McGregor Boulevard, Fort Myers; admission charged; last admission 4:30 p.m. (the estates\' own page). Parking not checked.',
  [W('Edison and Ford Winter Estates'),['Edison & Ford Winter Estates','https://www.edisonford.org']],
  hours='Daily 9 a.m. to 5:30 p.m.',brick='?'),

N('house-of-refuge-gilberts-bar','House of Refuge at Gilbert\'s Bar','Stuart (Hutchinson Island)','fl','landmark','standing',27.19954,-80.16563,'exact','open','drive','','1876',
  'One of a dozen houses of refuge the United States Life-Saving Service built on Florida\'s Atlantic shore in 1876, where a keeper and his family walked the beach after storms looking for castaways, and the only one left. It sheltered seven survivors of the Georges Valentine wreck in 1904 and watched for submarines in the Second World War. It is the oldest building in Martin County.',
  'The house on the coastal rocks of the Anastasia Formation, with its boathouse, kitchen, dining room, parlour and bedroom open to see, and a lookout tower from the Second World War (Wikipedia).',
  '',
  'Owned by Martin County and run as a museum by the Historical Society of Martin County, 301 SE MacArthur Boulevard; closed New Year\'s Eve and Day, Easter, the Fourth of July, Thanksgiving, Christmas Eve and Christmas (the society\'s page). Gilbert\'s Bar beach parking is beside it.',
  [W('House of Refuge at Gilbert\'s Bar'),['Historical Society of Martin County: hours','https://hsmc-fl.com/contact/']],
  th=[27.20005,-80.16588],thn='Gilbert\'s Bar parking',hours='Monday to Saturday 10 a.m. to 4 p.m., Sunday 1 to 4 p.m.',brick='no'),

N('jupiter-inlet-light','Jupiter Inlet Light','Jupiter','fl','light','standing',26.94861,-80.08204,'exact','open','drive','','1860',
  'A brick lighthouse finished in May 1860 on a sand dune at the north side of Jupiter Inlet, to a design by George G. Meade, later the Union general at Gettysburg. The work was slowed when the inlet silted shut and by the Third Seminole War. The Loxahatchee River Historical Society has given tours to the top since 1994 and runs the museum in Lighthouse Park.',
  'A double-walled brick tower, eight bricks thick at the base, painted red since 1910 to hide damp stains (Wikipedia). Visitors may climb it; children must be at least 48 inches tall, and bags and pets are not allowed (the museum\'s page).',
  '',
  'Jupiter Inlet Lighthouse & Museum, 500 Captain Armour\'s Way, in the Jupiter Inlet Lighthouse Outstanding Natural Area (Bureau of Land Management); adults $15. Last entry 4 p.m.; closed Thanksgiving, Christmas Eve and Christmas. Lighthouse Park lot west of the tower.',
  [W('Jupiter Inlet Light'),['Jupiter Inlet Lighthouse: hours and tickets','https://jupiterlighthouse.org/plan/hours-ticket-prices-directions-include-special-notices']],
  th=[26.94894,-80.08445],thn='Lighthouse Park lot',hours='Tuesday to Sunday 10 a.m. to 5 p.m.; closed Monday',brick='no'),

N('ancient-spanish-monastery','Ancient Spanish Monastery (St. Bernard de Clairvaux)','North Miami Beach','fl','worship','standing',25.93029,-80.15517,'site','open','walk','','1133–1141',
  'The cloister of a Cistercian monastery built in 1133–1141 at Sacramenia in Segovia, Spain. William Randolph Hearst bought it in 1926, against Spanish restrictions, and had it taken apart and shipped in 11,000 numbered crates; the stones lay in a Brooklyn warehouse until 1952, when they were bought and rebuilt on a former nursery in north Miami. It is now an Episcopal church as well as a place to visit.',
  'The twelfth-century stone cloister, chapel and gardens; pieces from other Spanish buildings were added in the rebuilding, such as the carved stone coat of arms in the cloister, and some original stones were never used (Wikipedia).',
  'Twelfth-century Spanish stones rebuilt beside a Miami highway.',
  'St. Bernard de Clairvaux Episcopal Church, 16711 West Dixie Highway. It is often closed for church services and private events, and always on Mondays and Tuesdays; its page links a month-by-month opening schedule. Parking not checked.',
  [W('St. Bernard de Clairvaux Church'),['Ancient Spanish Monastery','https://www.spanishmonastery.com']],
  hours='Wednesday to Sunday on the days its monthly schedule gives; closed Monday and Tuesday',brick='no'),

N('coral-castle','Coral Castle','Homestead (Leisure City)','fl','curio','standing',25.50056,-80.44444,'exact','open','drive','','1923–1951',
  'A garden of carved stone made alone by Edward Leedskalnin, a Latvian immigrant, from about 1923 until his death in 1951. He began it at Florida City and around 1936 moved the pieces ten miles north to this spot, which he called Rock Gate. It was listed on the National Register in 1984 and is a private attraction.',
  'About 1,100 tons of oolite limestone (not coral) cut into walls, a tower, tables, chairs, a crescent moon, a fountain and a sundial, and a 9-ton gate that turned on a balanced bearing until it rusted in 1986 (Wikipedia). Entry is by guided tour with a short film.',
  'One man, 1,100 tons of rock, and no one watching him work.',
  'Coral Castle Museum, 28655 S. Dixie Highway, Homestead; adults $25, tickets at the gift shop. Last tour 7 p.m. (the museum\'s page). Parking not checked.',
  [W('Coral Castle'),['Coral Castle: visit','https://coralcastle.com/visit']],
  hours='Daily 9 a.m. to 8 p.m.',brick='no'),

N('bahia-honda-rail-bridge','Bahia Honda Rail Bridge','Bahia Honda Key','fl','rail','ruins',24.6552,-81.29253,'site','public','walk','stations','1912',
  'A steel-truss bridge of Henry Flagler\'s Overseas Railroad to Key West, opened in 1912 across the deepest channel the line crossed, where the usual concrete arches would not do. After the 1935 Labor Day hurricane the state bought it and in 1938 laid a road deck on top of the trusses for the Overseas Highway. A new bridge replaced it in 1972, two spans were taken out, and the rest has been left to decay.',
  'A Parker truss of 247 feet in the middle with Pratt trusses either side; it is said to be the longest pin-connected truss bridge in the country. Signs warn boats of falling pieces. Only the easternmost section is open on foot, as a lookout kept by Bahia Honda State Park (Wikipedia).',
  'Flagler\'s railway with a highway sitting on its roof.',
  'Bahia Honda State Park, 36850 Overseas Highway (Florida State Parks). Only the eastern section in the park is open to walk on; stay off the rest of the bridge.'+SPN+' Park in the state park lots.',
  [W('Bahia Honda Rail Bridge'),FSP],
  th=[24.65569,-81.27931],thn='Bahia Honda State Park lot, Old US 1',hours='?',brick='no'),

N('indian-key-ghost-town','Indian Key','Islamorada','fl','town','ruins',24.87806,-80.67694,'site','boat','boat','burned','1830s–1840',
  'A tiny island off the upper Keys that the wrecker Jacob Housman made into a salvage town, with a customs inspector from 1832 and a post office from 1834; in 1836 it became the first county seat of Dade County. On August 7, 1840, during the Second Seminole War, a war party under Chakaika raided it, killed the botanist Henry Perrine among others, and burned the buildings. The state bought it in 1971 as a historic state park.',
  'Masonry foundations, ruined cisterns and plants left from Perrine\'s gardens, such as sisal (Wikipedia, from visits in 1921 and 1944); archaeologists have been uncovering the house foundations. Not checked on the ground.',
  'A wreckers\' county seat burned in one night in 1840.',
  'Indian Key Historic State Park, offshore at Mile Marker 78.5, Atlantic side (Florida State Parks). It is reached only by boat; local charter firms rent boats and kayaks (state parks guide).'+SPN,
  [W('Indian Key'),FSP],
  hours='?',brick='?'),

N('fort-east-martello','Fort East Martello','Key West','fl','fort','standing',24.55235,-81.75489,'exact','open','drive','forts','1862',
  'A Civil War tower fort that the Army began in 1862 to guard Key West against a Confederate attack from the sea. No fighting came, and the Army left it unfinished as the war ended. The Key West Art & Historical Society cleared it in 1950 to open its first museum and has restored it to the 1860s plan.',
  'A central brick citadel with a rooftop lookout over the Atlantic, inside an outer battlement and courtyard. The museum shows Civil War relics, Keys wrecking and cigar-making, and the metal sculptures of Stanley Papio (the society\'s page). A photograph of a vaulted passage inside shows red brick.',
  '',
  'Key West Art & Historical Society, 3501 S. Roosevelt Boulevard, near the airport; adults $17. Last admission 4:30 p.m. Parking not checked.',
  [['Key West Art & Historical Society: Fort East Martello','https://www.kwahs.org/visit/fort-east-martello']],
  hours='Daily 10 a.m. to 5 p.m.',brick='some'),
]

PIN_NOTES={
 'chautauqua-hall-of-brotherhood':'OpenStreetMap building at 95 Circle Drive; the Wikipedia point was about 20 m off, on open ground.',
 'st-marys-episcopal-church-madison':'Address point for 140 NE Horry Avenue (ArcGIS geocoder); the aerial shows a small dark-roofed building there but the church was not told apart from its neighbours for certain, so site precision.',
 'orman-house-apalachicola':'OpenStreetMap point for the Orman House at 177 5th Street; the Wikipedia point fell on the lawn of the Chapman Botanical Garden next door.',
 'lodge-at-wakulla-springs':'Wikipedia infobox coordinate; on the aerial it is on the lodge\'s red tile roof. The lot is the paved area just south of the lodge, moved onto it from the aerial.',
 'dudley-farm-newberry':'The Wikipedia point fell on State Road 26. The pin is on the cluster of farm buildings seen on the aerial in the middle of the park, which is likely but not certainly the farmstead, so area precision; the parking point is the visitor center at the park\'s address on West Newberry Road (ArcGIS geocoder), where buildings and a lot show on the aerial.',
 'marjorie-kinnan-rawlings-home':'OpenStreetMap building "Marjorie Kinnan Rawlings House"; the Wikipedia point, about 190 m south, is the park\'s parking loop and is used as the parking point.',
 'dunlawton-sugar-mill-ruins':'Wikipedia infobox coordinate, under the gardens\' tree canopy; the ruin was not picked out on the aerial, so site precision. The visitor parking is OpenStreetMap\'s lot on Old Sugar Mill Road.',
 'ponce-de-leon-inlet-light':'Wikipedia infobox coordinate; on the aerial it is on the tower in the middle of the keepers\' houses. The lot to the south-east shows parked cars.',
 'tampa-bay-hotel-plant-hall':'OpenStreetMap building "H. B. Plant Hall"; the Wikipedia point fell on Kennedy Boulevard. The building is long, so site precision.',
 'fort-de-soto-batteries':'Wikipedia infobox coordinate; on the aerial it is on the concrete battery with its round pits, west of the paved lot.',
 'ca-d-zan-sarasota':'Wikipedia infobox coordinate; on the aerial it is on the house at the water\'s edge.',
 'edison-ford-winter-estates':'Wikipedia infobox coordinate, inside the riverside grounds among the houses and gardens, so site precision.',
 'house-of-refuge-gilberts-bar':'Wikipedia infobox coordinate; on the aerial it is on the house on the rocks between the road and the beach. The lot is the parking row along the road just north.',
 'jupiter-inlet-light':'Wikipedia infobox coordinate; on the aerial it is on the tower and its shadow on the wooded hill. The Lighthouse Park lot shows parked cars.',
 'ancient-spanish-monastery':'Address point for 16711 West Dixie Highway (ArcGIS geocoder), on the orange-roofed cloister; the Wikipedia point was in trees by the canal.',
 'coral-castle':'Wikipedia infobox coordinate; on the aerial it is inside the walled stone garden beside Dixie Highway.',
 'bahia-honda-rail-bridge':'Wikipedia infobox coordinate, on the old truss bridge over the channel, so site precision; the walkable eastern end is reached from the state park lot given as the parking point.',
 'indian-key-ghost-town':'Wikipedia infobox coordinate, in the clearing at the middle of the island where paths meet; the foundations were not picked out on the aerial.',
 'fort-east-martello':'The National Register point fell on Roosevelt Boulevard; moved about 50 m north onto the fort\'s central citadel seen on the aerial.',
}
