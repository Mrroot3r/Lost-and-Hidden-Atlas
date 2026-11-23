# November 23, 2026: south and east Jackson County and Cass County, Missouri (Lee's Summit, Raytown, Grandview, Blue Springs,
# Sibley, Lone Jack, Harrisonville, Pleasant Hill). Part of filling in the Kansas City area on purpose for a local researcher.
# Facts from the linked sources only: Wikipedia read as raw text (tools/wiki_raw.py), the Lone Jack Historical Society and National
# Park Service pages read with tools/page.py, and the pages of Jackson County Parks, the Raytown chamber, VisitMO and St. Paul's
# parish as web search results quote them. The National Register forms could not be read (NPGallery holds only a placeholder
# and the Missouri State Parks copies answer 404). Nothing was checked on the ground.
from data_b import N
from data_ma import W

PLACES = [
N('fort-osage-sibley-mo', 'Fort Osage (reconstructed fort)', 'Sibley', 'kcmo', 'fort', 'standing',
  39.18808, -94.19211, 'exact', 'open', 'drive', '', '1808; replica 1948–1961',
  'William Clark began this U.S. government trading post on a bluff over the Missouri River in September 1808, after the Treaty of Fort Clark with some of the Osage. '
  'Lewis and Clark had noted the spot in June 1804, 70 feet above the river. The post stopped work in the 1820s. '
  'The fort seen today is a replica, built on the site between 1948 and 1961.',
  look='A log-and-timber fort on the bluff with its blockhouses, factory (trading house) and officers\' quarters, shown by costumed staff. It is a rebuilding, not original fabric. Interior of each building not checked.',
  accn='Run by Jackson County Parks + Rec as a National Historic Landmark and education center, Osage Street, Sibley. Search results quoting county and visitor pages give Tuesday to Sunday 9 a.m. to 4:30 p.m. all year, $8 adults, $4 ages 5 to 13 and seniors, with a combined ticket for Missouri Town. The sources give the street number as 105 or 107. Pages were of different years: call 816-650-3278 before going.',
  links=[W('Fort Osage'), ['National Park Service: Fort Osage National Historic Landmark', 'https://www.nps.gov/places/fort-osage-national-historic-landmark.htm'], ['Jackson County Parks + Rec: Fort Osage', 'https://www.makeyourdayhere.com/205/Fort-Osage']],
  conf='mixed', brick='?', hours='Tuesday to Sunday 9 a.m. to 4:30 p.m., year-round (confirm; from search results)'),

N('rice-tremonti-house-raytown-mo', 'Rice–Tremonti House', 'Raytown', 'kcmo', 'landmark', 'standing',
  39.00389, -94.48167, 'site', 'ask', 'drive', '', '1844',
  'Archibald and Sally Rice settled here about 1836 on the Santa Fe Trail and built the present Gothic Revival frame farmhouse in 1844, on a farm worked by enslaved people. '
  'Wikipedia says it is believed to be the oldest surviving frame building in Jackson County. The Rice family moved to Texas in the Civil War and the house was not burned under General Order No. 11. '
  'Dr. Louis Tremonti bought it in 1929; the Friends of the Rice-Tremonti Home bought it in 1988 and restored it. A replica of "Aunt Sophie\'s Cabin", for the woman Kitty Rice enslaved, stands on the grounds.',
  look='The farmhouse and the cabin replica. Wikipedia says the Friends hold open houses; a search result says tours are by arrangement and not at regular hours. Interior not checked.',
  accn='Owned by the City of Raytown according to a chamber listing, run by the Friends of the Rice-Tremonti Home, 8801 East 66th Street. No regular hours: ask the Friends (816-358-7423, as the Raytown chamber lists it). The Friends\' own page would not load, so hours not checked.',
  links=[W('Rice-Tremonti House'), ['Raytown Chamber: Rice-Tremonti Historic Home', 'https://raytownchamber.com/?p=3507']],
  conf='mixed', brick='no', hours=''),

N('truman-farm-home-grandview-mo', 'Harry S. Truman Farm Home', 'Grandview', 'kcmo', 'landmark', 'standing',
  38.90171, -94.53091, 'site', 'public', 'drive', '', '1894–1895',
  'The farmhouse was built in 1894–95 by Harry Truman\'s grandmother after an 1867 house burned. Truman worked the farm from 1906 to 1917. '
  'About 10 acres of what was a 600-acre farm are now part of Harry S. Truman National Historic Site, a National Historic Landmark, in the middle of Grandview\'s commercial strip.',
  look='The farmhouse, a reconstructed smokehouse, the old Grandview post office that Truman moved here as a garage, a box wagon and stone fence posts that mark the old boundary. An audio tour is on the NPS app. House tours have been seasonal and at times suspended; interior not checked.',
  accn='Owned by the National Park Service as part of Harry S. Truman National Historic Site (the federal public-land map shows no unit here), 12301 Blue Ridge Boulevard. The NPS photo-tour page says the grounds are open daily sunrise to sunset and tours of the house are paused for foundation work; the page is undated. Call the visitor center in Independence (816-254-9929) to ask whether the house is open.',
  links=[W('Harry S. Truman Farm Home'), ['NPS: Truman Farm Home photo tour', 'https://www.nps.gov/hstr/learn/historyculture/truman-farm-home-photo-tour.htm']],
  brick='?', hours='Grounds sunrise to sunset daily; house tours seasonal or paused (call 816-254-9929)'),

N('unity-village-tower-mo', 'Unity Village: Unity Tower and campus', 'Unity Village', 'kcmo', 'inst', 'standing',
  38.94745, -94.40752, 'site', 'view', 'drive', '', '1920s',
  'Charles and Myrtle Fillmore bought a farm here in 1919 and the Unity movement\'s headquarters moved out to it after the Second World War; the village was incorporated in 1953. '
  'Wikipedia says the Tower and an office building opened in 1929 and are on the National Register. The tower held 100,000 gallons of water. A concrete buttress dam of 1926 made Lake Charles R. Fillmore, said to be the only dam of its kind in Missouri.',
  look='The Tower, the Cotswold-style and Mediterranean-style buildings of the campus, and the buttress dam. One account says the Tower was shut for almost a decade for falling stone and was to reopen as a spa; its present use was not checked. Interior not checked.',
  accn='A working campus with offices, owned by Unity. A third-party listing says free tours start at the visitor center and must be booked; the Unity page was not read, so hours not checked. Look from the public roads and ask at the visitor center.',
  links=[W('Unity Village, Missouri'), ['Unity Village: about', 'https://www.unityvillage.org/about']],
  conf='mixed', brick='?', hours=''),

N('st-pauls-episcopal-lees-summit-mo', 'St. Paul\'s Episcopal Church', 'Lee\'s Summit', 'kcmo', 'worship', 'standing',
  38.91083, -94.3725, 'site', 'open', 'drive', '', '1884',
  'The parish was founded in 1867 and the church, designed by the Rev. Frederick B. Scheetz, was finished in 1884. Wikipedia calls it a rare surviving wood-frame Carpenter Gothic church in Missouri, with a stone foundation and a bell tower. '
  'It was listed on the National Register in 1985 and has had few if any changes since it was built. Another listing dates the parish from 1879, so its founding year is not settled.',
  look='Diagonal narrow wood strips cover the interior walls, and horizontal strips the vaulted ceiling. Three stained-glass windows sit over the wooden altar in the apse.',
  accn='Active parish, 416 SE Grand Avenue at Fifth and Green streets; street parking. The parish site, as search results quote it, gives Sunday services at 8 a.m. in the historic nave and 10 a.m. in the Apostles\' Chapel. Open outside services not checked.',
  links=[W('Saint Paul\'s Episcopal Church (Lee\'s Summit, Missouri)'), ['St. Paul\'s Episcopal Church', 'https://stpaulsls.org/']],
  brick='no', hours='Sunday 8 a.m. (historic nave) and 10 a.m. (Apostles\' Chapel)'),

N('missouri-town-1855-lees-summit-mo', 'Missouri Town 1855 Living History Museum', 'Lee\'s Summit', 'kcmo', 'town', 'standing',
  38.97471, -94.32142, 'site', 'open', 'drive', '', 'buildings 1820–1860',
  'Missouri Town was never a real town. Jackson County built it in Fleming Park from more than 25 buildings, most from 1820 to 1860, moved from other places in Missouri, and shows an 1855 village with costumed interpreters, crops and rare livestock. '
  'Only the root cellar belonged to the farm that stood on the site, and the mercantile and blacksmith shop are reproductions made with salvaged material.',
  look='Moved log and frame houses, a church, shops and farm buildings along a village street, with period gardens and animals. Which buildings keep original interiors was not checked. Wikipedia says workshops run in spring to fall.',
  accn='Run by Jackson County Parks + Rec, 8010 East Park Road, Fleming Park. One visitor listing gives 9 a.m. to 4:30 p.m. Tuesday to Sunday from April 1 to November 15 and weekends only from November 16 to March 31, closed on some holidays; $8 adults. The county page would not load here, so check 816-229-8980. Tuesdays are "drive-thru" days in the listing. No pets in the village.',
  links=[W('Missouri Town 1855'), ['Jackson County Parks + Rec: Missouri Town', 'https://www.makeyourdayhere.com/213/Missouri-Town-1855']],
  conf='mixed', brick='?', hours='Apr 1–Nov 15 Tue–Sun 9–4:30; Nov 16–Mar 31 weekends (from a listing; confirm)'),

N('lone-jack-civil-war-museum-mo', 'Lone Jack Civil War Museum and Battlefield', 'Lone Jack', 'kcmo', 'fort', 'standing',
  38.86565, -94.17314, 'exact', 'open', 'drive', '', '1862; museum 1963',
  'On August 16, 1862 Union troops were beaten here in the Battle of Lone Jack by a much larger Confederate force; Wikipedia says the fighting raged for five hours on the town\'s main street. '
  'The museum, a round building of native limestone, opened in 1963. The historical society bought the Cave Hotel in 2014, which a visit page offers as a guided tour. One search result says the hotel\'s owner, Lucinda Cave, was killed in the battle; that was not confirmed.',
  look='The limestone museum, the soldiers\' cemetery beside it holding Union and Confederate dead, and the Cave Hotel on request. Ask the volunteer on duty for the hotel. Museum contents not checked.',
  accn='Run by the Lone Jack Historical Society, 301 South Bynum Road. The society\'s visit page lists $7 for adults, $3 for ages 6 to 12 and free under 6, but the page text read gave no days or times: call 816-697-8833 (a travel-site number). Another site gives the battle month as September; the town and Wikipedia say August.',
  links=[W('Lone Jack, Missouri'), ['Lone Jack Historical Society: visit', 'https://historiclonejack.org/visit']],
  conf='mixed', brick='no', hours='?'),

N('harrisonville-courthouse-square-mo', 'Harrisonville Courthouse Square Historic District', 'Harrisonville', 'kcmo', 'town', 'standing',
  38.65444, -94.34861, 'site', 'public', 'drive', '', '1880–1943',
  'The district has 34 contributing buildings in the town centre, built between about 1880 and 1943 in Italianate, Queen Anne, Colonial Revival, Tudor Revival and Renaissance Revival styles. '
  'Wikipedia names the Cass County Courthouse (1897, by Kansas City architect Walter C. Root), the Bank of Harrisonville (1900–01), Wirt\'s Opera House Building (1907, altered 1940), the 1925 post office, the 1892 Deacon Building and the c. 1903 "Racket" Store. It was listed in 1994.',
  look='Walk the streets round the 1897 courthouse and read the upper storeys and cornices of the commercial blocks. Interiors not checked; the courthouse is a working county office.',
  accn='Town streets and a courthouse square owned by the city and county (the federal public-land map shows none); park round the square. Shops and county offices keep their own hours; none were read.',
  links=[W('Harrisonville Courthouse Square Historic District')],
  brick='?', hours=''),

N('st-peters-episcopal-harrisonville-mo', 'St. Peter\'s Episcopal Church', 'Harrisonville', 'kcmo', 'worship', 'standing',
  38.65452, -94.35106, 'exact', 'view', 'drive', '', '1895',
  'A one-storey, cross-shaped Tudor Gothic Revival church of 1895 at 400 West Wall Street, listed on the National Register in 1982. '
  'Wikipedia describes yellow-beige quarry-faced limestone walls with stick work and false half-timbering, a square shingled cupola, lancet windows and a crenellated parapet.',
  look='The limestone walls, half-timbered gables, cupola and lancets from the street. Interior and services not checked.',
  accn='Active church, public sidewalk views only; no page of the parish was read, so service times are not given.',
  links=[W('St. Peter\'s Episcopal Church (Harrisonville, Missouri)')],
  brick='no', hours=''),

N('pleasant-hill-downtown-historic-district-mo', 'Pleasant Hill Downtown Historic District', 'Pleasant Hill', 'kcmo', 'town', 'standing',
  38.7862, -94.2742, 'area', 'public', 'drive', '', '1865–1959',
  'The district has 53 contributing buildings and covers the railroad town\'s centre, built between about 1865 and 1959 in Italianate, Jacobethan, Colonial Revival, Classical Revival and Modern styles. '
  'A local history summary names the 1899 Kellogg Opera House, the Peoples Theater and Depot Park. It was listed in 1994 per Wikipedia (another summary says 2005).',
  look='Streets of old storefronts around the depot and Depot Park, with murals. Interiors not checked.',
  accn='Town streets and Depot Park, owned by the city (the federal public-land map shows none). The Historical Society Museum is at 125 Wyoming Street; no hours were found, so hours not checked.',
  links=[W('Pleasant Hill Downtown Historic District'), W('Pleasant Hill Historical Society Museum')],
  conf='mixed', brick='?', hours=''),

N('pleasant-hill-depot-mo', 'Pleasant Hill Missouri Pacific Depot', 'Pleasant Hill', 'kcmo', 'rail', 'standing',
  38.78557, -94.27408, 'exact', 'view', 'drive', '', '1903',
  'The first depot here was a wood-frame building of 1866 that burned in 1901. The Missouri Pacific built this one in 1903, at 100 Wyoming Street, and it is part of the downtown historic district.',
  look='The 1903 depot beside the tracks and Depot Park. Whether the inside can be visited was not checked.',
  accn='Look from Depot Park or Wyoming Street. Use of the building today and its hours not checked.',
  links=[['Historical Marker Project: Missouri Pacific Railroad Depot, Pleasant Hill', 'https://www.historicalmarkerproject.com/markers/HM1NQ2_missouri-pacific-railroad-depot_Pleasant-Hill-MO.html']],
  conf='mixed', brick='?', hours=''),

N('german-evangelical-pastors-home-blue-springs-mo', 'German Evangelical Pastors\' Home (Blue Springs Terrace)', 'Blue Springs', 'kcmo', 'inst', 'standing',
  39.01583, -94.28667, 'area', 'view', 'drive', '', '1906–',
  'A home for retired pastors of the German Evangelical Church, put together in 1906–07 under the pastor of St. Peter\'s Evangelical Church of Kansas City. It was listed on the National Register as a 13-building district in 1988. '
  'It still houses retired United Church of Christ and Disciples pastors as Blue Springs Terrace. One ministry publication calls it the first retirement community of any Protestant denomination in the United States; that was not confirmed.',
  look='A group of houses on one residential block, seen from the street. Which buildings are original was not checked.',
  accn='Private homes where people live: look from the public street only. Parking not checked.',
  links=[['Clio: German Evangelical Pastors\' Home', 'https://theclio.com/entry/144586']],
  conf='mixed', brick='?', hours=''),

N('lees-summit-downtown-historic-district-mo', 'Lee\'s Summit Downtown Historic District and Sherwood Building', 'Lee\'s Summit', 'kcmo', 'town', 'standing',
  38.91333, -94.37667, 'area', 'public', 'drive', '', '1860s–1940s',
  'The railroad town\'s centre was listed on the National Register as a downtown district in 2005. '
  'The Sherwood Manufacturing Company Building at 123 SE 3rd Street was listed in 2010; the nomination, as an index summary gives it, names industry as its theme and 1946 as its year, and shows the city as owner. '
  'No source on the district\'s buildings was read in full.',
  look='Old commercial blocks along the downtown streets near the tracks. What survives inside was not checked.',
  accn='Town streets (the federal public-land map shows none); shops keep their own hours. Parking not checked.',
  links=[['National Register: Sherwood Manufacturing Company Building', 'https://npgallery.nps.gov/AssetDetail/NRIS/10000204'], ['National Register of Historic Places listings in Jackson County, Missouri', 'https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Jackson_County,_Missouri']],
  conf='mixed', brick='?', hours=''),

N('lees-summit-christian-church-mo', 'Lee\'s Summit Christian Church Building', 'Lee\'s Summit', 'kcmo', 'worship', 'standing',
  38.91111, -94.37528, 'area', 'view', 'drive', '', '1949',
  'The Disciples of Christ congregation, founded in 1870, tore down an older church and finished a wood-frame one in 1898. The Colonial Revival building on the Register, at SE Douglas and Fourth streets, is a later one, finished in 1949, and was listed in 2011. '
  'A Clio entry says it later housed an antique shop.',
  look='A Colonial Revival church of 1949. Its present use and interior were not checked.',
  accn='Look from the street. Owner and use not checked.',
  links=[['Clio: Lee\'s Summit Christian Church Building', 'https://theclio.com/entry/143544'], ['National Register: Lee\'s Summit Christian Church Building', 'https://historypointer.com/nris/resource/11000213']],
  conf='mixed', brick='?', hours=''),
]

PIN_NOTES = {
  'fort-osage-sibley-mo': 'Moved from the park point to the reconstructed stockade, seen on the aerial on the bluff above the river.',
  'rice-tremonti-house-raytown-mo': 'Coordinate from the National Register list via Wikipedia.',
  'truman-farm-home-grandview-mo': 'Wikipedia\'s coordinate fell on a shopping centre roof; moved about 57 m south to the farmhouse seen in the field beyond it.',
  'unity-village-tower-mo': 'OpenStreetMap building named Unity Tower.',
  'st-pauls-episcopal-lees-summit-mo': 'Coordinate from Wikipedia and the Register list; trees hide the roof on the aerial.',
  'missouri-town-1855-lees-summit-mo': 'Wikipedia\'s coordinate is about 2 km west, in woods; moved to the village, which is where OpenStreetMap puts it and where the aerial shows scattered buildings round a green.',
  'lone-jack-civil-war-museum-mo': 'OpenStreetMap museum node at 301 South Bynum Road.',
  'harrisonville-courthouse-square-mo': 'Coordinate from the Register list; centred on the square.',
  'st-peters-episcopal-harrisonville-mo': 'Coordinate from Wikipedia.',
  'pleasant-hill-downtown-historic-district-mo': 'Wikipedia\'s coordinate fell on houses; moved to the storefronts by the depot. The pin marks the area only.',
  'pleasant-hill-depot-mo': 'OpenStreetMap building at 100 Wyoming Street.',
  'german-evangelical-pastors-home-blue-springs-mo': 'Coordinate from the Register list; the houses were not located individually.',
  'lees-summit-downtown-historic-district-mo': 'Coordinate from the Register list; centre of the district.',
  'lees-summit-christian-church-mo': 'Coordinate from the Register list; the aerial does not show which building is the church, so the pin marks the area only.',
}

BATCH = {'key': 'kcmo_jcse', 'label': 'South and east Jackson County and Cass County, Missouri', 'added': '2026-11-23 08:52'}
