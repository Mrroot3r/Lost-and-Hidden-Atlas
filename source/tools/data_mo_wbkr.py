# November 25, 2026: Warrensburg, Knob Noster, Chilhowee and Medford, Johnson County, Missouri (about 50 miles south-east of Kansas City).
# Part of filling in the Kansas City area on purpose for a local researcher. The Atlas had no place in Johnson County apart from the
# Joseph M. Miller Mausoleum at Holden. Facts come from the sources linked on each place: Wikipedia read as raw text (tools/wiki_raw.py),
# the Johnson County Historical Society's own driving-tour page, the Missouri State Parks lists and the National Register forms that
# opened (courthouse, Chilhowee, Holden and Pine Streets district), Cedarcroft Farm's own history page, Clio, and web search results
# that quote the pages they came from. The forms for the other places could not be read.
from data_b import N
from data_ma import W

PLACES = [
N('old-johnson-county-courthouse-warrensburg-mo', 'Old Johnson County Courthouse (Johnson County Historical Society), Warrensburg', 'Warrensburg', 'mo', 'civic', 'standing',
  38.76561, -93.75036, 'site', 'open', 'drive', '', '1838–1878',
  'Johnson County\'s first permanent courthouse, a two-story Federal-style building of stuccoed brick with a hipped roof, built between 1838 and 1841 on the old public square. The county used it until 1878 (the historical society\'s tour page gives 1842 to 1878). '
  'The 1870 "Old Drum" trial, in which a lawyer\'s closing speech about a shot dog became the source of the saying "a man\'s best friend", was held here, and so was a political gunfight in 1861, according to the society. It has been restored to look as it did about 1870 and is on the National Register of Historic Places (1970).',
  look='The old courtroom building, now part of the historical society\'s museum group on North Main Street with the Mary Miller Smiser Heritage Library and Museum and the Culp Building of early farm tools. Tours are given by the society. Original fabric inside was not described on the pages read.',
  accn='Run by the Johnson County Historical Society, 302 to 304 North Main Street; telephone 660-747-6480. The society\'s own tour page says the old courthouse is open Tuesday to Friday 1 to 4 p.m. with $3 admission; a 2024 newspaper article says Tuesday and Thursday to Saturday 1 to 4 p.m. with $5 for adults; a Missouri Life piece, as quoted in a search result, says Tuesday and Saturday 1 to 4 p.m. and Thursday 1 to 8 p.m. or by appointment. The pages disagree, so call first. Street parking on North Main Street. The Register\'s point is off the museum address and was moved on the aerial.',
  links=[['Johnson County Historical Society: Historic Tour Sites in Johnson County', 'https://jocomohistory.org/national-register-sites-in-johnson-county/'], ['Columbia Missourian: Johnson County Historical Society', 'https://www.columbiamissourian.com/special_section/tourism/southwest_missouri/johnson-county-historical-society-in-warrensburg-offers-tours-archives-glimpses-of-history/article_f9774cfa-064b-11ef-8452-ef274ee34cb8.html'], W('Johnson County Courthouse (Old Public Square, Warrensburg, Missouri)')],
  hours='Sources differ: Tue and Thu to Sat 1 to 4 p.m. (2024 article); Tue to Fri 1 to 4 p.m. (society tour page). Call 660-747-6480.', conf='mixed', brick='no'),

N('johnson-county-courthouse-warrensburg-mo', 'Johnson County Courthouse (1898), Warrensburg', 'Warrensburg', 'mo', 'civic', 'standing',
  38.76500, -93.74056, 'exact', 'open', 'drive', '', '1896–1898',
  'The county\'s third courthouse, a Richardsonian Romanesque building of rough-faced sandstone designed by George E. McDonald, built 1896 to 1898 and still the seat of county government. Wikipedia and the National Register form name McDonald; the sources give his home as Omaha or Lincoln, Nebraska. '
  'It was the first of several courthouses McDonald designed in Missouri and other states, and it is on the National Register of Historic Places (1994).',
  look='A two-and-a-half-story cross-gabled building of brown-tinged gray sandstone with a central square tower, an octagonal ogee dome topped by a metal goddess statue, and four corner towers with domes. The Register form says much of the original interior is intact, including tall panel doors and ornate trim. A statue of Old Drum stands outside, according to a 2024 newspaper caption.',
  accn='A working county building on Courthouse Square, Holden Street; the historical society\'s tour page says it is open daily for public business and that the County Clerk\'s office (660-747-6161) has historic information. Opening hours were not read on any page. Street parking round the square.',
  links=[['National Register form (Missouri State Parks)', 'https://mostateparks.com/sites/g/files/zuston361/files/media/pdf/2025/02/johnson-county-courthouse.pdf'], ['Clio: Johnson County Courthouse', 'https://theclio.com/entry/141227'], W('Johnson County Courthouse (Courthouse Square, Warrensburg, Missouri)')],
  hours='?', brick='no'),

N('masonic-temple-warrensburg-mo', 'Masonic Temple (Corinthian Lodge No. 265), Warrensburg', 'Warrensburg', 'mo', 'civic', 'standing',
  38.76528, -93.73972, 'exact', 'view', 'drive', '', '1893–1894',
  'A three-story Italianate lodge building of 1893 to 1894, about 48 by 92 feet, for many years the meeting hall of Corinthian Lodge No. 265. The lodge has since moved elsewhere. It is on the National Register of Historic Places (1998) and stands across Holden Street from the courthouse.',
  look='Red brick with a lot of sandstone trim on a rectangular three-story block at Market and Holden streets. The historical society\'s tour page says it has been restored and holds shops and offices, and is not open for tours.',
  accn='Private commercial building at 101 West Market Street and 301 North Holden Street: look from the street. Street parking round the courthouse square.',
  links=[['Johnson County Historical Society: Historic Tour Sites in Johnson County', 'https://jocomohistory.org/national-register-sites-in-johnson-county/'], W('Masonic Temple (Warrensburg, Missouri)')],
  hours='', brick='yes'),

N('jones-brothers-mule-barn-warrensburg-mo', 'Jones Brothers Mule Barn (Cassingham & Son Hardware), Warrensburg', 'Warrensburg', 'mo', 'industry', 'standing',
  38.76329, -93.73783, 'exact', 'view', 'drive', '', '1912',
  'Built in 1912 as a sales barn for mules, which the historical society calls a major shipping point for Missouri mules. It later served for many years as a hardware store. Wikipedia dates the National Register listing to 2010 and the Missouri State Parks list to February 2011.',
  look='A two-story red brick block with a monitor roof and a one-story rear ell, on a stone foundation, at College Avenue and the railroad tracks. What it is used for now was not checked.',
  accn='Private commercial building at 101 North College Avenue, a block from the Holden Street shops: look from the sidewalk. Street parking.',
  links=[['Johnson County Historical Society: Historic Tour Sites in Johnson County', 'https://jocomohistory.org/national-register-sites-in-johnson-county/'], W('Jones Brothers Mule Barn')],
  hours='', conf='mixed', brick='yes'),

N('holden-pine-commercial-district-warrensburg-mo', 'Holden and Pine Streets Commercial Historic District, Warrensburg', 'Warrensburg', 'mo', 'town', 'standing',
  38.76390, -93.74060, 'area', 'public', 'walk', '', '',
  'The old downtown of Warrensburg, laid out beside the Missouri Pacific tracks, listed as a historic district on the National Register of Historic Places in 2017. The Register form describes brick and stone commercial blocks in Late Victorian Romanesque, Second Empire and Italianate styles, with some later Moderne fronts. '
  'It takes in the courthouse square, the 1890 depot and the Magnolia Opera House of 1889 at 145 West Pine Street, now apartments, whose brick panels still carry the painted words "Magnolia Opera 1889".',
  look='Walk Holden and Pine streets. The form lists the depot at 100 South Holden Street and an opera house among its landmarks. The district boundary is roughly Maynard, North College, East Gay, West Market and Railroad streets and North Washington Avenue. The buildings are shops, offices and homes, mostly closed to the public beyond their business hours.',
  accn='Public streets and sidewalks owned by the City of Warrensburg (the federal public-land map does not show city streets); the buildings are private or in business use. Street parking on Holden and Pine. The pin is the middle of the walk, not one building.',
  links=[['National Register form (Missouri State Parks)', 'https://mostateparks.com/sites/g/files/zuston361/files/media/pdf/2025/02/holden-and-pine-streets-commercial-hd.pdf'], ['Johnson County Historical Society: Historic Tour Sites in Johnson County', 'https://jocomohistory.org/national-register-sites-in-johnson-county/']],
  hours='', brick='yes'),

N('warrensburg-depot-mo', 'Warrensburg depot (Missouri Pacific, now Amtrak station), Warrensburg', 'Warrensburg', 'mo', 'rail', 'standing',
  38.76281, -93.74066, 'exact', 'open', 'drive', '', '1890',
  'The Missouri Pacific Railroad opened this station in 1890 (Amtrak\'s own page, as quoted by a web search, gives 1889). It is a sandstone building in the Richardsonian Romanesque style, altered several times, most recently with a baggage section and platform in 1984 and an improvement project of about $2.6 million in the early 2020s. Trains to Kansas City and St. Louis still stop here twice a day each.',
  look='A sandstone depot beside the tracks at the south end of Holden Street, inside the Holden and Pine Streets historic district. It also holds the Warrensburg Chamber of Commerce visitor centre. Its original interior was not described on the pages read.',
  accn='Amtrak station at 100 South Holden Street. The waiting room hours are as a web search quoted Amtrak\'s station page; the Chamber\'s visitor-centre hours were not found. Parking beside the station was not checked.',
  links=[W('Warrensburg station'), ['National Register form for the district (Missouri State Parks)', 'https://mostateparks.com/sites/g/files/zuston361/files/media/pdf/2025/02/holden-and-pine-streets-commercial-hd.pdf']],
  hours='Waiting room Mon to Fri 7:30 a.m. to 9 p.m., Sat and Sun 7 a.m. to 9 p.m. (Amtrak, as quoted by search). Visitor centre hours not checked.', conf='mixed', brick='no'),

N('warren-street-methodist-church-warrensburg-mo', 'Warren Street Methodist Episcopal Church, Warrensburg', 'Warrensburg', 'mo', 'worship', 'standing',
  38.76212, -93.74495, 'exact', 'view', 'drive', '', '1898–1899',
  'A Gothic Revival church built in 1898 to 1899 by a local African American congregation, at 201 South Warren Street, and listed on the National Register of Historic Places in 1996. The historical society\'s tour page says it is now closed and believed to be under restoration inside; the date of that note is not given.',
  look='A one-story building of orange-tinted brick (a photograph on Wikimedia Commons shows red brick) with a square entrance tower under a concave dome and a gabled cornice (Wikipedia). It is closed, so look from the street. Whether any original woodwork or glass survives was not checked.',
  accn='Private property, closed to the public as far as the sources say: look from Warren Street. Street parking.',
  links=[['Johnson County Historical Society: Historic Tour Sites in Johnson County', 'https://jocomohistory.org/national-register-sites-in-johnson-county/'], W('Warren Street Methodist Episcopal Church')],
  hours='', brick='yes'),

N('grover-street-victorian-district-warrensburg-mo', 'Grover Street Victorian Historic District, Warrensburg', 'Warrensburg', 'mo', 'town', 'standing',
  38.76194, -93.73722, 'site', 'view', 'walk', '', '1887–1944',
  'A block of nine houses on the 200 block of Grover Street, built between about 1887 and 1944 and listed as a historic district in 2012. Wikipedia names the Leonidus and Mary Jack House (about 1887), the Bradley, Markward, Lee, McElvain and Stewart houses, and one house of 1944 in the builder style.',
  look='Queen Anne and Stick or Eastlake houses along both sides of the street, one block south of the depot. The historical society\'s driving tour starts here. What the houses are made of was not checked.',
  accn='Private homes on a public street: look from the sidewalk and respect the residents. Street parking on Grover Street or at the depot.',
  links=[['Johnson County Historical Society: Historic Tour Sites in Johnson County', 'https://jocomohistory.org/national-register-sites-in-johnson-county/'], W('Grover Street Victorian Historic District')],
  hours='', brick='?'),

N('garden-of-eden-station-warrensburg-mo', 'Garden of Eden Station (Pickel\'s Station), near Warrensburg', 'Warrensburg', 'mo', 'landmark', 'standing',
  38.79139, -93.74194, 'exact', 'view', 'drive', '', '1928',
  'A small roadside filling station built about 1928 of local sandstone by the Pickel family beside old Highway 13, later called McBride\'s Station. The historical society calls it the Ben Pickel gas station; a Clio entry names a Bill Pickel. It was listed on the National Register of Historic Places in 1994 (Wikipedia\'s text says 1995; the Missouri State Parks list says April 1994). '
  'A city of Warrensburg historic-resources page, as quoted by a web search, says it has been restored and shows two old gas pumps.',
  look='A little building of coursed sandstone blocks at the junction of Missouri 13 and County Road 215 NW. The historical society says to look from the road only: there is no tour. Whether the restoration is open to walk round was not checked.',
  accn='Private property: drive-by view only, from old Highway 13. Pull off only where the shoulder is wide and safe; the pin is the Register point and was moved on the aerial where noted.',
  links=[['Johnson County Historical Society: Historic Tour Sites in Johnson County', 'https://jocomohistory.org/national-register-sites-in-johnson-county/'], ['Clio: Pickel\'s Garden of Eden Station', 'https://theclio.com/entry/186855'], W('Garden of Eden Station')],
  hours='', conf='mixed', brick='no'),

N('cress-griebel-houses-warrensburg-mo', 'Cress House and Griebel House (West Gay Street), Warrensburg', 'Warrensburg', 'mo', 'landmark', 'standing',
  38.76606, -93.74483, 'site', 'view', 'drive', '', '1885–1888',
  'Two Victorian frame houses face each other across the corner of Gay and Warren streets. The Herbert and Bettie Cress House, at 222 West Gay, was built about 1888 in the Queen Anne and Shingle styles and listed on the National Register of Historic Places in 1995. The Lewis and Sophie Griebel House, at 300 West Gay, was built about 1885 in Folk Victorian style and listed in 2012.',
  look='The Cress House has beveled siding below and sawn shingles above, a sandstone foundation and full-width porches on two floors. The Griebel House is a one-story cruciform house with a steep cross-gabled roof, lacy vergeboards, turned porch posts and a three-sided oriel window. Both are on the historical society\'s drive-by tour; neither is open for tours.',
  accn='Private homes: look from the public sidewalk only. Street parking on Gay Street.',
  links=[['Johnson County Historical Society: Historic Tour Sites in Johnson County', 'https://jocomohistory.org/national-register-sites-in-johnson-county/'], W('Herbert A. and Bettie E. Cress House'), W('Lewis and Sophie Griebel House')],
  hours='', brick='no'),

N('pleasant-view-school-medford-mo', 'Pleasant View School, near Medford', 'Medford', 'mo', 'civic', 'standing',
  38.670833, -94.006111, 'exact', 'ask', 'drive', '', '1915–1957',
  'A one-room country school of 1915 on Missouri 131, listed on the National Register of Historic Places in 1999. Wikipedia says the blackboard, desks, bookcases, water cooler and oil stove are still inside from its last year as a school, 1957; the historical society\'s tour page gives its school years as 1915 to 1949. A search result says it opened on September 14, 1915, with 27 pupils.',
  look='A one-story side-gabled frame schoolhouse in the bungalow manner, with the school privy, the foundation of the coal shed and a well with a hand pump on the grounds. Inside, the furnishings are largely original (Wikipedia). It is kept up by a local community group that has held open days; none was scheduled on the pages read.',
  accn='Address 674 SW Highway 131. Not open on a regular schedule as far as the pages read show: a Facebook page for the schoolhouse says to schedule a tour or private event, and an undated post gave 1 to 4 p.m. for a fall open house. Ask first through that page. Roadside parking only.',
  links=[['Johnson County Historical Society: Historic Tour Sites in Johnson County', 'https://jocomohistory.org/national-register-sites-in-johnson-county/'], ['Clio: Pleasant View Schoolhouse near Medford', 'https://theclio.com/entry/194911'], W('Pleasant View School (Medford, Missouri)')],
  hours='', conf='mixed', brick='no'),

N('chilhowee-historic-district-mo', 'Chilhowee Historic District (Main and Walnut Streets), Chilhowee', 'Chilhowee', 'mo', 'town', 'standing',
  38.58902, -93.85554, 'site', 'public', 'walk', '', '1904–1930',
  'The business street of a railroad town on the prairie, listed on the National Register of Historic Places in 1988. The Register form counts 21 contributing buildings and says all but two are brick. It says no other railroad town in Johnson County keeps so unspoiled a trading centre, and that the approach over gravel roads from the west is an abrupt change from farm country to brick fronts.',
  look='Brick fronts about a block long: the Farmers Bank of 1907, Murphy Brothers Hardware of 1907, Valentine & Son\'s General Store, the Chilhowee Bank of 1915 with its lettered stone over the door, and an old garage. Clio and the historical society say several buildings have been lost to fire or collapse in recent years, among them a grocery in the 2010s, so the street is thinner than the form describes.',
  accn='Public streets owned by the village of Chilhowee (the federal public-land map does not show them); the buildings are private or village-owned and not described as open. The Farmers Bank was said to be vacant. Street parking on Main Street.',
  links=[['National Register form (Missouri State Parks)', 'https://mostateparks.com/sites/g/files/zuston361/files/media/pdf/2025/02/chilhowee-hd.pdf'], ['Clio: Chilhowee Bank', 'https://theclio.com/entry/195380'], W('Chilhowee Historic District')],
  hours='', brick='yes'),

N('adams-farmstead-cedarcroft-warrensburg-mo', 'John A. Adams Farmstead (Cedarcroft Farm), near Warrensburg', 'Warrensburg', 'mo', 'landmark', 'standing',
  38.69487, -93.66613, 'site', 'ask', 'drive', '', '1867–1880',
  'A farm where John A. Adams, after the Civil War, built a house (about 1867 to 1876) and two barns (about 1867 and 1880) and from 1875 laid one of the first underground drainage tile systems in Missouri, tied to cross-gully dams that filled in washed-out gullies. Wikipedia and the farm\'s own history page agree on the drainage; Adams is credited as an early soil conservationist. It was listed on the National Register of Historic Places in 1994.',
  look='An 1867 farmhouse and two old barns on a working-farm site. The tile system lies under the ground and cannot be seen. The owners say they recovered some original tiles when building.',
  accn='Private home at 431 SE County Road Y. The historical society\'s tour page says tours are by appointment on 660-624-4944, but the owners\' own history page says the farmhouse bed and breakfast closed in 2002 and the cottage in 2016, and that they live in the house, so ask before going. Look from the road only otherwise.',
  links=[['Cedarcroft Farm: farm history', 'https://www.cedarcroft.com/farm/history.html'], ['Johnson County Historical Society: Historic Tour Sites in Johnson County', 'https://jocomohistory.org/national-register-sites-in-johnson-county/'], W('John A. Adams Farmstead Historic District')],
  hours='', conf='mixed', brick='?'),

N('montserrat-works-knob-noster-state-park-mo', 'Montserrat Recreation Demonstration Area works (stone bath house, dam, bridge), Knob Noster State Park', 'Knob Noster', 'mo', 'inst', 'standing',
  38.75216, -93.57894, 'area', 'public', 'walk', '', '1936–1941',
  'Knob Noster State Park began in the 1930s as the Montserrat Recreation Demonstration Area, a federal scheme to turn worn-out farmland into recreation ground. Relief workers of the Civilian Conservation Corps and the Works Progress Administration built its roads, bridges, camp areas and park buildings, and the state took the park over in 1946. '
  'Several of their works were listed on the National Register of Historic Places in 1985: a stone bridge of 1937, a dam and spillway of 1938 to 1939, a stone bath house of 1939, an entrance portal and a warehouse and workshop of 1939 to 1940, and the 30 frame buildings of Camp Shawnee, 1936 to 1941.',
  look='Wikipedia, from the Register forms, describes the bath house as a modest stone building with a pitched roof and small windows under the eaves; the dam as concrete with a curved tailrace between cut-stone walls and seven stone steps; the bridge as two flat arches in a random ashlar wall; and Camp Shawnee as large rustic frame buildings with saltbox roofs. Which dam and lake the Register means was not settled: the park has two dams, Clearfork Lake and Lake Buteo, and the Register points lie one to two kilometres east of them.',
  accn='Knob Noster State Park, 873 SE 10 Road, run by Missouri State Parks; park office 660-563-2463. The state parks page says the park closes from sunset December 2 to sunrise December 7, 2026 for a managed deer hunt. Daily park hours were not found on a page that opened. The pin is the park visitor centre, mapped on OpenStreetMap: it marks the park, not any one structure. Ask at the visitor centre which of the 1930s works can be seen.',
  links=[['Missouri State Parks: Knob Noster State Park', 'https://mostateparks.com/park/knob-noster-state-park'], ['Missouri State Parks: Johnson County National Register listings', 'https://mostateparks.com/basic-page/missouri-national-register-listings/Johnson'], ['Johnson County Historical Society: Historic Tour Sites in Johnson County', 'https://jocomohistory.org/national-register-sites-in-johnson-county/'], W('Knob Noster State Park')],
  hours='', conf='mixed', brick='no'),
]

BATCH = {'key': 'mo_wbkr', 'label': 'Johnson County, Missouri: Warrensburg, Knob Noster, Chilhowee', 'added': '2026-11-25 09:58'}

PIN_NOTES = {
  'old-johnson-county-courthouse-warrensburg-mo': 'Address match for 302 North Main Street, the historical society\'s address; the Wikipedia point lies about 100 m west and falls on houses.',
  'johnson-county-courthouse-warrensburg-mo': 'Wikipedia and Register list point on the courthouse square. Check on the aerial.',
  'masonic-temple-warrensburg-mo': 'Register list point at Market and Holden streets. Check on the aerial.',
  'jones-brothers-mule-barn-warrensburg-mo': 'Address match for 101 North College Avenue; the Wikipedia point is a block south, at the railroad crossing.',
  'holden-pine-commercial-district-warrensburg-mo': 'The middle of Holden and Pine streets, chosen by hand; the pin marks the district, not one building.',
  'warrensburg-depot-mo': 'Address match for 100 South Holden Street, about 15 m from the Wikipedia point.',
  'warren-street-methodist-church-warrensburg-mo': 'Address match for 201 South Warren Street.',
  'grover-street-victorian-district-warrensburg-mo': 'Wikipedia point for the district on Grover Street. Check on the aerial.',
  'garden-of-eden-station-warrensburg-mo': 'Wikipedia and Register list point at the junction of Missouri 13 and County Road 215 NW. Check on the aerial.',
  'cress-griebel-houses-warrensburg-mo': 'Register list points of the two houses, about 60 m apart; the pin sits between them. Check on the aerial.',
  'pleasant-view-school-medford-mo': 'Register list point for 674 SW Highway 131. Check on the aerial.',
  'chilhowee-historic-district-mo': 'Address match for East Walnut and North Main streets, where the Register form puts the district; the Wikipedia point is 100 m south, in trees.',
  'adams-farmstead-cedarcroft-warrensburg-mo': 'Address match for 431 SE County Road Y; the Wikipedia point is 200 m north, in a field.',
  'montserrat-works-knob-noster-state-park-mo': 'The park visitor centre, a point mapped on OpenStreetMap. The Register points for the bath house, dam and bridge fall one to two kilometres east of the park\'s two dams, so none of the structures was found; the pin marks the park only.',
}
