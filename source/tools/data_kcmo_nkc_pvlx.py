# November 23, 2026: North Kansas City, Parkville, Gladstone, north Kansas City and Liberty, Clay and Platte counties, Missouri.
# Part of filling in the Kansas City area on purpose for a local researcher. The Atlas had no place in North Kansas City or Parkville.
# Facts from the linked sources only: Wikipedia read as raw text (tools/wiki_raw.py), the pages of the Atkins-Johnson Farm, Screenland
# Armour, Antioch Community Church, the Banneker School Foundation, the City of Liberty, Clay County African American Legacy, Clio and
# Flatland KC, and web search results that quote the City of Parkville's park page. The National Register forms could not be read.
from data_b import N
from data_ma import W

PLACES = [
N('armour-theatre-north-kansas-city-mo', 'Armour Theatre Building (Screenland Armour)', 'North Kansas City', 'kcmo', 'civic', 'standing',
  39.14257, -94.57580, 'exact', 'open', 'drive', '', '1928',
  'The Armour Theatre was built in 1927–28 as the "Community and Theater Building" of the new industrial town of North Kansas City, for the North Kansas City Development Company, to a design by the Kansas City firm Keene & Simpson. It opened on September 6, 1928, in the last years of silent film, when a blind local pianist played to the pictures. '
  'It was renamed the Centre Theatre in 1963 and the Paradise in 1984, stood empty, and was bought and restored as a film theatre that reopened on May 23, 2008. It is on the National Register of Historic Places (2008).',
  look='A two-story building in the Spanish Eclectic style, with polychromatic brick, a Mission tile roof, arched openings on the front, decorative tiles over the cut-off corner and glazed terra cotta trim. It is a working cinema, so the lobby and screens are open to anyone with a ticket; the original auditorium was not described on the pages read.',
  accn='A working cinema (Screenland Armour) at 408 Armour Road, in the middle of the town. Street parking on Armour Road. Showtimes vary by day: a visitor guide says hours "vary" and gives telephone (816) 994-7380; see the theatre\'s own page for the day\'s films.',
  links=[['Screenland Armour: history', 'https://screenland.com/history'], ['Clio: Armour Theatre Building', 'https://theclio.com/entry/88068'], W('Armour Theatre Building')],
  hours='?', brick='?'),

N('sears-warehouse-north-kansas-city-mo', 'Sears, Roebuck and Company Warehouse (Park Lofts)', 'North Kansas City', 'kcmo', 'industry', 'standing',
  39.14248, -94.57176, 'exact', 'view', 'drive', '', '1912–1923',
  'Sears, Roebuck and Company built this merchandise warehouse in North Kansas City after outgrowing a West Bottoms building it had used since 1910. It rose in stages between 1912 and 1923 to nine stories, in a Late Gothic Revival and Chicago school style, and Sears later moved to another site and sold it. Later the Bellas-Hess catalogue firm took it over (a local history blog dates that to about 1924–25), and it housed the Missouri Poster and Sign Company and an antique mall. '
  'It has been converted to apartments called Park Lofts and is on the National Register of Historic Places (1997).',
  look='A very large warehouse seen from Armour Road. The National Park Service lists the architect as George C. Nimmons. Interior and the exact start date were not checked: Wikipedia gives 1912–1923 in one place and 1913 in another.',
  accn='Private apartment building at 715 Armour Road: look from the street. Residents\' parking is not open to visitors; use street parking on Armour Road.',
  links=[W('Sears, Roebuck and Company Warehouse Building (North Kansas City, Missouri)'), ['National Park Service listing 97000411', 'https://npgallery.nps.gov/AssetDetail/037d788d-c954-4f43-b00e-6fa4ec513d49']],
  hours='', brick='?', conf='mixed'),

N('wheeling-corrugating-building-north-kansas-city-mo', 'Wheeling Corrugating Company Building', 'North Kansas City', 'kcmo', 'industry', 'standing',
  39.13444, -94.57056, 'site', 'view', 'drive', '', '1920',
  'The Wheeling Corrugating Company built this plant in 1920 to make corrugated galvanized iron for roofing and worked here until 1956, when it moved to a larger plant and sold the building to the Cook Paint and Varnish Company (later Cook Composites and Polymers). '
  'It was designed by the Kansas City firm Tarbet & Gornall and is on the National Register of Historic Places (1994).',
  look='A five-story, six-bay reinforced concrete building faced in brick with cut stone trim, with a one-story concrete block addition of about 1950. What it is used for now was not checked.',
  accn='Private industrial property: look from the public street. Owner and present use not checked. The pin is the Register\'s point and was not confirmed on the building by a source.',
  links=[W('Wheeling Corrugating Company Building'), ['National Park Service listing 94001220', 'https://npgallery.nps.gov/AssetDetail/NRIS/94001220']],
  hours='', brick='?', conf='mixed'),

N('mackay-hall-parkville-mo', 'Mackay Hall, Park University', 'Parkville', 'kcmo', 'civic', 'standing',
  39.18987, -94.68018, 'exact', 'view', 'drive', '', '1886–1893',
  'Park College, founded in 1875 on the bluff above the Missouri River, taught students who paid part of their way by work. Mackay Hall was built that way: more than 300 students did the labour over seven years, using limestone quarried on the campus. '
  'Sources disagree on the dates. The National Register gives 1886, Park University gives 1886 as the start and 1893 as the finish, and Wikipedia\'s article on the university says work began in 1883. It is on the National Register of Historic Places (1979).',
  look='A three-story rock-faced limestone building of about 137 by 84 feet in Richardsonian Romanesque style, with a clock tower and tall spire, steep roofs, wall dormers and towers, and bands of colour in the stone. The cornerstone, replaced in a renovation, holds a time capsule meant to be opened in 2093. Interior not checked.',
  accn='Main building of Park University, 8700 NW River Park Drive. It is a working campus: look from the grounds and the public sidewalks, and ask at the university for any tour. Visitor parking on campus was not checked.',
  links=[['Clio: Mackay Hall', 'https://theclio.com/entry/31742'], W('Mackay Building'), W('Park University')],
  hours='', brick='no'),

N('waddell-a-truss-bridge-parkville-mo', 'Waddell "A" Truss Bridge, English Landing Park', 'Parkville', 'kcmo', 'landmark', 'standing',
  39.18586, -94.68222, 'site', 'public', 'walk', '', '1898',
  'Built in 1898 over Linn Branch Creek near Trimble for the Quincy, Omaha and Kansas City Railway, to J. A. L. Waddell\'s patented "A" truss design. The railway was abandoned in 1939; the bridge then carried State Route 4 from 1953. It was taken down when Smithville Lake was built, stored by the Army Corps of Engineers, and rebuilt in English Landing Park in 1987, where it carries walkers. '
  'It is one of two "A" truss bridges known to survive in the country and was listed on the National Register of Historic Places in 1991. Sources differ on when it left road service and on what its move cost.',
  look='A short riveted steel truss shaped like the letter A, crossing a small backwater of the Missouri River inside the park. It is a footbridge: walk across it.',
  accn='City park run by the City of Parkville. Its page, as search results quote it, gives hours of 5 a.m. to midnight daily and says parking is allowed only in the marked lots (the entrance lot off McAfee Drive has just a few spaces); a travel site that said "dawn to dusk" disagrees. The park page itself was not opened.',
  links=[['Clio: Waddell "A" Truss Bridge', 'https://www.theclio.com/entry/149629'], W('Waddell "A" Truss Bridge (Parkville, Missouri)')],
  hours='5 a.m. to midnight daily (park)', brick='no'),

N('banneker-school-parkville-mo', 'Benjamin Banneker School, Parkville', 'Parkville', 'kcmo', 'civic', 'standing',
  39.19298, -94.68583, 'exact', 'view', 'drive', '', '1885',
  'A one-room school for Black children, begun in 1885 on land Park College had bought, with bricks made by Park College students in the college kilns. Before it, Black children in Parkville were taught in a hotel basement and then in a college hall. The date it was finished is not certain, and it probably closed about 1905 after a larger school was planned in 1902. '
  'It was then lived in for many years. In the 1980s Lucille Douglass, who taught at the later Banneker School in the 1940s, found that a developer meant to demolish it, bought it and gave it to the Platte County Historical Society. It is on the National Register (1995) and was on Missouri\'s most endangered list in 2008. The Banneker School Foundation, formed in 2008, is restoring it.',
  look='A one-story red brick building with a gable roof of about 34 by 18 feet, on a rubble limestone foundation. The foundation says it plans a living-history museum when restoration is done. Whether it opens for visits now was not stated on its page.',
  accn='Owned by the Banneker School Foundation and Historic Site at 31 W. 8th Street; look from the street and write to the foundation (P.O. Box 29028, Parkville, MO 64152) about a visit. Street parking in town.',
  links=[['Banneker School Foundation: history', 'https://bannekerschoolparkvillemo.org/history'], W('Benjamin Banneker School')],
  hours='', brick='yes'),

N('washington-chapel-cme-parkville-mo', 'Washington Chapel C.M.E. Church', 'Parkville', 'kcmo', 'worship', 'standing',
  39.19510, -94.68594, 'exact', 'view', 'drive', '', '1907',
  'A Christian Methodist Episcopal church for Parkville\'s small Black community, built of native limestone shaped from a local quarry by formerly enslaved men and Park College students. It opened on June 29, 1907, on land Park College lent the congregation money to buy. '
  'The street was not paved until the 1960s, and as families moved away the building decayed. A $160,000 grant from the National Trust\'s African American Cultural Heritage Action Fund in 2024 and more than $80,000 raised in Parkville paid for a restoration, and a reopening was planned for June 27, 2026. It is on the National Register (1992).',
  look='A two-story rectangular Late Gothic Revival church in rough limestone, with a castellated corner tower and projecting bays. A date of June 29, 1907 is carved on it. The sanctuary is upstairs; a staircase was added inside later so the first floor need not be left to go up. Interior after the restoration not checked.',
  accn='Active congregation at 1137 West Street; look from the street. Service times were not found on a page of the church. The pastor, as a news article reports, also serves a church in Leavenworth, so visits are best arranged through the church.',
  links=[['Flatland KC: restoration of Washington Chapel', 'https://flatlandkc.org/news-issues/restoration-of-black-church-in-parkville-inspires-rainbow-coalition/'], W('Washington Chapel C.M.E. Church')],
  hours='', brick='no'),

N('atkins-johnson-farm-gladstone-mo', 'Atkins-Johnson Farm and Museum', 'Gladstone', 'kcmo', 'landmark', 'standing',
  39.21278, -94.53105, 'exact', 'open', 'drive', '', 'c. 1826–1853',
  'A log house of about 1826 (the museum\'s own history dates the cabin to the early 1830s) that Jonathan Atkins enlarged in 1853 into a two-story I-house, more than doubling it. The land was granted in 1824; Atkins bought it in 1834 and kept a carding machine and grist mill running on it. Mary Johnson bought it in 1920. '
  'The City of Gladstone bought the house in 2005, it was listed on the National Register in 2007, and the museum opened April 27, 2013. Wikipedia lists a root cellar and entrance, a milk house, a well and pump and a garage among the other buildings.',
  look='The farmhouse with its early log core, shown as a museum with docents. Visitors can see part of the main floor; the parlor, living room, foyer and upstairs are not open to those who cannot use stairs, and docents describe those rooms. Other buildings on the grounds were not described on its pages.',
  accn='Run by the City of Gladstone at 4109 NE Pleasant Valley Road. Free admission; free parking at the main entrance or at Big Shoal Cemetery, 4125 NE 64th Street. Walkways and restrooms are wheelchair accessible. Hours as the museum\'s own visit page gave them on November 23, 2026; telephone (816) 423-4107.',
  links=[['Atkins-Johnson Farm: visit', 'https://www.atkinsjohnsonfarm.com/visit'], ['Atkins-Johnson Farm: site history', 'https://www.atkinsjohnsonfarm.com/site-history'], W('Atkins-Johnson Farmhouse Property')],
  hours='Wednesday to Saturday 11 a.m. to 4 p.m., April 1 to December 5, 2026', brick='?'),

N('big-shoal-cemetery-gladstone-mo', 'Big Shoal Cemetery, Gladstone', 'Gladstone', 'kcmo', 'burial', 'standing',
  39.20982, -94.53068, 'site', 'public', 'walk', '', '',
  'An old burying ground next to the Atkins-Johnson Farm. It had been abandoned when the City of Gladstone took it over in 2009 through the Missouri Attorney General, and it is now cared for as public property with a self-guided walking tour.',
  look='Old gravestones on the hill. A walking-tour brochure is at the information kiosk and can be downloaded from the museum\'s page. The cemetery\'s first burial year was not on the pages read.',
  accn='City of Gladstone public property, open from dawn to dusk every day of the year, free. Parking off NE 64th Street (4125 NE 64th Street).',
  links=[['Atkins-Johnson Farm: visit (cemetery section)', 'https://www.atkinsjohnsonfarm.com/visit'], ['Atkins-Johnson Farm: site history', 'https://www.atkinsjohnsonfarm.com/site-history']],
  hours='Dawn to dusk daily', brick='?'),

N('antioch-christian-church-kansas-city-mo', 'Antioch Christian Church (1859 chapel)', 'Kansas City', 'kcmo', 'worship', 'standing',
  39.18151, -94.54827, 'site', 'view', 'drive', '', '1859',
  'The congregation began in 1853 under the preaching of Moses E. Lard, on a campground at the Winn farm in rural Clay County. Its first church, a simple white frame building of 1859 (credited to a master carpenter, Ben Ricketts, in a search summary of the Register form), was the meeting place through the Civil War. '
  'The congregation reorganised as Antioch Community Church in 1930 and built a brick sanctuary in 1957. The old chapel was moved to its present site: the Register and most sources say 1968, while the congregation\'s own story says it was restored and set on a new foundation in 1964. It is on the National Register (1979).',
  look='A one-story white clapboard chapel with a front gable roof, about 33 by 51 feet. The congregation says it still uses the chapel for weddings and other events.',
  accn='Private church property at 4805 NE Antioch Road; look from the road. Whether the chapel can be seen inside, or when services are held, was not stated on the page read. Church parking lot.',
  links=[['Antioch Community Church: our story', 'https://acckc.org/our-story'], W('Antioch Christian Church (Kansas City, Missouri)')],
  hours='', brick='no', conf='mixed'),

N('compton-house-kansas-city-mo', 'Dr. James Compton House (Oak Ridge)', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.19476, -94.51298, 'site', 'view', 'drive', '', 'c. 1829',
  'A log house of about 1829 that Dr. James Howard Compton, born in Virginia in 1815, bought with its farm in 1844 and named Oak Ridge. The Compton family owned it until 1952 and enlarged it several times in that time. '
  'A frame blacksmith shop and a frame guest house also stand on the property. Wikipedia calls it one of the oldest surviving houses in the city; it is on the National Register (1979) and was once known as Sandy\'s Oak Ridge Manor Tea House.',
  look='A much-enlarged house that began as a log dwelling, with a blacksmith shop and guest house beside it. Whether anyone can go in, and what it is used for now, was not found.',
  accn='Address 5410 NE Oak Ridge Road. Ownership and present use were not checked; treat it as private and look from the public road only. The pin is the address match and was not checked against a source on the building.',
  links=[W('Dr. James Compton House'), ['Missouri State Parks: Register form (could not be opened when this was written)', 'https://mostateparks.com/sites/mostateparks/files/Compton%2C%20Dr.%20James%2C%20Residence.pdf']],
  hours='', brick='?', conf='mixed'),

N('garrison-school-liberty-mo', 'Garrison School and its historic district, Liberty', 'Liberty', 'kcmo', 'civic', 'standing',
  39.25214, -94.42025, 'exact', 'view', 'drive', '', '1877–1942',
  'Garrison School was set up in 1877 to teach Black children in Liberty. The Clay County African American Legacy group bought it from the Liberty School District in 2003 and runs it as the Garrison School Cultural Center. '
  'The Register district around it has six buildings of about 1900 to 1942 from Liberty\'s Black community: houses of ordinary types, the brick school and a limestone African Methodist church. It is on the National Register (2001). A one-mile walking tour of the town\'s Black history begins at the school.',
  look='The brick school with the neighbouring houses and the limestone church. The Legacy group\'s page says exhibits and programmes are held in the school; a search listing gave weekday hours but a news report called it open by appointment, so no hours are recorded.',
  accn='Owned by Clay County African American Legacy, Inc., 502 N. Water Street, telephone (816) 781-7918. Hours not confirmed: ask before going. The City of Liberty\'s walking-tour leaflet (about a mile) starts here and ends on the courthouse square; street parking.',
  links=[['Clay County African American Legacy, Inc.', 'https://ccaal-garrisonschool.org'], ['City of Liberty: African-American history walking tour (PDF)', 'https://www.libertymissouri.gov/DocumentCenter/View/19496'], W('Garrison School Historic District')],
  hours='?', brick='?'),

N('mt-memorial-cemetery-liberty-mo', 'Mt. Memorial Cemetery ("The Old Graveyard"), Liberty', 'Liberty', 'kcmo', 'burial', 'standing',
  39.24902, -94.41237, 'site', 'public', 'walk', '', 'c. 1827–1828',
  'Liberty\'s first public burying ground, beside the William Jewell College campus. The city says it was in use well before the town trustees bought the one-and-a-half acres for $30 on July 5, 1836; a marker puts the first burial in 1827 and the Register says about 1828. '
  'It holds 554 documented burials, including the town\'s first mayor, Madison Miller. Union troops used Jewell Hall as a hospital in the Civil War and buried soldiers here; in 1912 the remains of 27 were moved to Fort Leavenworth, and at least six are believed to remain. It was not officially named until 1916 and is on the National Register (2012).',
  look='A small rectangular graveyard of about 140 by 435 feet with early headstones. The pin is the OpenStreetMap cemetery point.',
  accn='A City of Liberty cemetery on the Jewell campus. Opening times were not found on the city\'s pages read; as with other city cemeteries, daylight visits are the usual courtesy. Park on the public streets by the campus.',
  links=[['City of Liberty: Mt. Memorial Cemetery history', 'https://www.libertymissouri.gov/2113/Mt-Memorial-Cemetery-History'], W('Mt. Memorial Cemetery')],
  hours='', brick='?', conf='mixed'),

N('major-hotel-liberty-mo', 'Major Hotel (Franklin House Apartments), Liberty', 'Liberty', 'kcmo', 'hotel', 'standing',
  39.24722, -94.41833, 'area', 'view', 'drive', 'hotels', '1912',
  'Built in 1912 to a design by Keene & Simpson as the Major Hotel (later the Colonial Hotel), it was rebuilt after a fire in 1934 and turned into 21 apartments in 1987. It is on the National Register of Historic Places (1992).',
  look='A three-story brick building in a mix of Colonial Revival and Prairie style, with a low hipped roof and wide eaves, shed dormers and a one-story veranda along the front. Now apartments; interior not checked.',
  accn='Private apartment building near the courthouse square; look from the public street. The pin is the Register\'s point, not checked on the building.',
  links=[W('Major Hotel')],
  hours='', brick='?', conf='mixed'),

N('miller-building-liberty-mo', 'Miller Building (1868), Liberty', 'Liberty', 'kcmo', 'civic', 'standing',
  39.24722, -94.42000, 'area', 'view', 'drive', '', '1868',
  'A commercial block on Liberty\'s square built in 1868, one of the oldest on the town\'s National Register list (1992).',
  look='A two-story brick building with a flat roof, a decorative brick cornice, hooded window surrounds and a storefront that still has its cast-iron columns. What it is used for now was not checked.',
  accn='A shop building on the courthouse square; look from the public sidewalk and go in only when the business is open. The pin is the Register\'s point, not checked on the building.',
  links=[W('Miller Building (Liberty, Missouri)')],
  hours='', brick='?', conf='mixed'),
]

BATCH = {'key': 'kcmo_nkc_pvlx', 'label': 'North Kansas City, Parkville, Gladstone and Liberty, Missouri', 'added': '2026-11-23 12:52'}

PIN_NOTES = {
  'armour-theatre-north-kansas-city-mo': 'ArcGIS address match for 408 Armour Road, which agrees with the Register list point to about 20 m.',
  'sears-warehouse-north-kansas-city-mo': 'ArcGIS address match for 715 Armour Road, about 50 m from the Register point.',
  'wheeling-corrugating-building-north-kansas-city-mo': 'Register list point; the street address was not found. Check on the aerial.',
  'mackay-hall-parkville-mo': 'Moved onto the large towered building seen on the aerial, north of the campus entrance; the address match for Park University fell on a small building in woods about 40 m away.',
  'waddell-a-truss-bridge-parkville-mo': 'Wikipedia\'s point for the relocated bridge in English Landing Park; the ArcGIS point for the park is 15 m away.',
  'banneker-school-parkville-mo': 'ArcGIS address match for 31 W. 8th Street, about 50 m from the Register point.',
  'washington-chapel-cme-parkville-mo': 'ArcGIS address match for 1137 West Street, about 100 m from the Register point.',
  'atkins-johnson-farm-gladstone-mo': 'Moved onto the farmhouse seen among trees on the aerial, west of the museum\'s car park; the museum\'s street address matches only the car park, about 60 m away.',
  'big-shoal-cemetery-gladstone-mo': 'OpenStreetMap cemetery outline point.',
  'antioch-christian-church-kansas-city-mo': 'The church group\'s buildings at 4805 NE Antioch Road as seen on the aerial; which of them is the 1859 chapel could not be told from above, so the pin marks the site only.',
  'compton-house-kansas-city-mo': 'ArcGIS address match for 5410 NE Oak Ridge Road; the Register list point is about 300 m away. Check on the aerial.',
  'garrison-school-liberty-mo': 'ArcGIS address match for 502 N. Water Street, which the Legacy group gives as its address. The Register list point is off by about 100 m.',
  'mt-memorial-cemetery-liberty-mo': 'OpenStreetMap cemetery point, agreeing with the Register list point to about 50 m.',
  'major-hotel-liberty-mo': 'Register list point only; no street address was found. Check on the aerial.',
  'miller-building-liberty-mo': 'Register list point only; no street address was found. Check on the aerial.',
}
