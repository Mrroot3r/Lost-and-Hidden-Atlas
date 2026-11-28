# November 25, 2026: Excelsior Springs, Clay County, Missouri, a second pass (the first was kcmo_exsp_hrqd).
# Sources opened: the National Register registration forms for the Elms Historic District (2014) and the Boarding House District,
# the multiple-property form "Historic Resources of Excelsior Springs, Missouri" (all read through NPGallery), Wikipedia read as raw
# text, an Excelsior Citizen article of November 2024 on the sulpho-saline wells and one of September 2025 on the Royal Hotel, a
# one-page city trail guide, and search results quoting a Missouri State Parks survey. Forms for the two downtown districts could not be read.
from data_b import N
from data_ma import W

BATCH={'key':'kcmo_exsp2_wvnk','label':'Excelsior Springs, second pass','added':'2026-11-25 23:01'}

PLACES = [
N('wabash-station-1-excelsior-springs-mo', 'Wabash Railway Station No. 1 (1907), Excelsior Springs', 'Excelsior Springs', 'kcmo', 'rail', 'standing',
  39.33802, -94.22740, 'site', 'view', 'drive', 'stations', '1907',
  'A small brick depot of 1907 on the short Wabash "dummy line" that joined the Milwaukee Road depot, a mile out of town, to Excelsior Springs. The hotel owners behind the Elms had the line built, and its tracks ran along the west side of the neighbourhood now called the Elms Historic District, so that visitors could step off the train near the hotel. A second, larger Wabash station was built a block south in 1927.',
  look='A rectangular brick depot with a moderately steep hipped roof. The old front, which faced the Elms Hotel, has tall and small window openings with a double row of radiating brick arches above and a stone lintel below, most of them boarded over; one large door at the north end is partly bricked in. The 2014 Register form says it still shows the marks of a train depot. Interior not checked.',
  accn='Corner of Leavenworth Avenue and Dunbar Street. Look from the public sidewalk. Present owner and use not checked, and the 2014 form is the latest source read.',
  links=[W('The Elms Historic District')], brick='yes'),

N('wabash-station-2-excelsior-springs-mo', 'Wabash Railway Station No. 2 (1927, later "The Dairy"), Excelsior Springs', 'Excelsior Springs', 'kcmo', 'rail', 'standing',
  39.33530, -94.22733, 'site', 'open', 'drive', 'stations', '1927',
  'The second Wabash station, built in 1927 in the Mission style by R. E. Mohr. The railway was given up, and in the late 1930s the Quality Milk Company took over the empty depot as a dairy, with a small restaurant in the old waiting-room end and a new bottling wing on the south side. It is again a restaurant: OpenStreetMap lists a barbecue restaurant at this address.',
  look='A one-story brick depot with a low tile hipped roof, wide open eaves with exposed rafters and cross bays. The 2014 Register form says the original waiting room, restrooms, baggage rooms and ticket office are still to be made out inside, and that a 1940s dairy garage stands behind. The south addition has a window of glass blocks. Interior not checked.',
  accn='646 Kansas City Avenue South; a working restaurant, so it is open to customers. Customer parking on the east and west sides. Hours not checked: the restaurant\'s own page was not read.',
  links=[W('The Elms Historic District')], hours='?', brick='yes'),

N('st-lukes-episcopal-church-excelsior-springs-mo', 'St. Luke\'s Episcopal Church (1933), Excelsior Springs', 'Excelsior Springs', 'kcmo', 'worship', 'standing',
  39.33734, -94.22634, 'site', 'view', 'drive', '', '1932–1933',
  'A small Gothic Revival church of 1932-33 across the street from the Elms Hotel, designed by George M. Siemens and built of rough local limestone. It was finished in 1933 and carries that date on its cornerstone.',
  look='Quarry-faced limestone walls, a T-shaped plan, a stone bell-cote at the junction of the nave and the entry porch, a cross on the west gable, and a stone chimney on the east end. The 2014 Register form says all the windows are original: leaded casements with stained-glass shields, a Gothic-arched stained-glass window in the east transept, and a large pointed window in the west wall. Service times and whether the inside can be visited were not checked.',
  accn='404 Regent Avenue, opposite the Elms Hotel. Active church; look from the street. Service times not checked.',
  links=[W('The Elms Historic District')], brick='no'),

N('st-ann-catholic-church-excelsior-springs-mo', 'St. Ann Catholic Church (1907, 1917), Excelsior Springs', 'Excelsior Springs', 'kcmo', 'worship', 'standing',
  39.33724, -94.22724, 'site', 'view', 'drive', '', '1907; 1917',
  'A tall brick Gothic Revival church on Kansas City Avenue, built in 1907 and added to in 1917, in the Elms neighbourhood where many of the town\'s boarding houses stood. The Register form calls it a late example of the Gothic Revival.',
  look='A Latin-cross plan with a steeply roofed belfry tower in the middle of the front, a stone doorway with a cross over it, wide flattened-Gothic windows with stone drip moulds, and a continuous stone band across the front. Brick is the main material. The 2014 form says the front doors are new and that a window in the tower is boarded over but keeps its original mullions. Interior not checked.',
  accn='552 Kansas City Avenue South. Active parish; look from the street. Service times not checked.',
  links=[W('The Elms Historic District')], brick='?'),

N('elms-pump-house-well-carriage-house-excelsior-springs-mo', 'Elms Hotel pump house, well and carriage house, Excelsior Springs', 'Excelsior Springs', 'kcmo', 'water', 'standing',
  39.33690, -94.22600, 'area', 'view', 'drive', 'hotels', 'about 1912–1920',
  'Behind the Elms Hotel stand the plain buildings that served it. A small brick building of about 1912 was a carpenter\'s shop in 1913 and a pump house by 1926; local people told the Register nomination writers that mineral water was served from it. In the guest lot is the hotel\'s own sulpho-saline well, a long slot in the ground under metal plates, whose water was used only for hotel guests and never sold from a pavilion. A one-story limestone carriage house or garage of about 1920 completes the group.',
  look='The brick pump house with a gable roof and a porch on its south end (now a meeting space), the metal-plated well opening in the east service lot south of the east wing, and the limestone carriage house with two cross-braced board doors. All three are inside the hotel\'s grounds; the pump house and carriage house are by the western guest lot. Interior not checked.',
  accn='Private grounds of the Elms Hotel, 401 Regent Avenue. These are service buildings: ask at the hotel before walking the grounds; the pin marks the general area behind the hotel.',
  links=[W('The Elms Historic District'), W('Elms Hotel (Excelsior Springs, Missouri)')], conf='mixed', brick='some',apart=['elms-hotel-excelsior-springs-mo: these are the service buildings behind the hotel, listed separately from it', 'elms-historic-district-excelsior-springs-mo: the service buildings behind the hotel; the district is the streets around it']),

N('barbee-memorial-church-excelsior-springs-mo', 'Barbee Memorial Presbyterian Church (Siloam Spring Baptist Church), Excelsior Springs', 'Excelsior Springs', 'kcmo', 'worship', 'standing',
  39.34129, -94.21881, 'site', 'view', 'drive', '', 'about 1902',
  'A Gothic Revival church of about 1902 in the Boarding House District, built as the Barbee Memorial Presbyterian Church and later the Siloam Spring Baptist Church. In the years when Excelsior Springs was a health resort, its streets were lined with boarding houses for visitors who came to drink and bathe in the mineral waters.',
  look='A steeple tower with a square hipped roof on the southeast corner, Gothic-arched stained-glass windows in the front wall, a raised stone basement dug out in 1911, and a stone entry surround added in 1954. The walls are now covered in metal siding, and a brick addition of 1947 and 1954 stands behind. Interior not checked.',
  accn='438 Benton Avenue at Temple Avenue. Active or recent church (present use not checked); look from the public sidewalk.',
  links=[['National Register form, Boarding House District (NPGallery)', 'https://npgallery.nps.gov/GetAsset/fb78e52d-b7b9-4048-bb37-975616d209a6']], brick='no'),

N('hiawatha-rooming-house-excelsior-springs-mo', 'Hiawatha Rooming House, 101 Linden Avenue, Excelsior Springs', 'Excelsior Springs', 'kcmo', 'hotel', 'standing',
  39.34245, -94.21954, 'exact', 'view', 'drive', 'hotels', 'about 1907',
  'A Queen Anne boarding house of about 1907, one of the 85 buildings of the Boarding House District. The district\'s houses stand within walking distance of the mineral-water pavilions and bath houses that visitors came for. Search results also describe a "soda well pagoda" on its grounds where guests drew mineral water; that was not confirmed on a page read.',
  look='A tall 2½-story house with a three-story six-sided tower at the southwest corner under a pointed roof with a finial, a one-story porch that wraps round the tower, and a stained-glass window in the front. It is now covered in asbestos shingles. Interior not checked.',
  accn='Southeast corner of Linden Avenue and East Excelsior Street; private. Look from the sidewalk. Present use not checked.',
  links=[['National Register form, Boarding House District (NPGallery)', 'https://npgallery.nps.gov/GetAsset/fb78e52d-b7b9-4048-bb37-975616d209a6']], brick='no'),

N('boarding-house-district-excelsior-springs-mo', 'Boarding House District, Excelsior Springs', 'Excelsior Springs', 'kcmo', 'town', 'standing',
  39.34190, -94.21900, 'area', 'view', 'walk', 'hotels', '1895–1963',
  'Listed on the National Register in 2018: 85 buildings of 1895 to 1963 on the east edge of downtown, within walking distance of the mineral-spring pavilions, bath houses and sanitariums. The 1923 count of the town included twenty bathhouses and nineteen mineral-water dispensaries, and the visitors who came for them were put up in houses like these. Many were later made into apartments and re-sided; a good number have been pulled down.',
  look='Plain frame houses, many with deep porches, close together on narrow lots with stone retaining walls, along East Excelsior Street, East Broadway, Benton Avenue and Isley Boulevard; a heavily wooded slope between East Broadway and East Excelsior. Named buildings include the Hiawatha Rooming House (101 Linden) and a Gothic Revival church at 438 Benton. Most are re-sided, so look at the porches, rooflines and the stone walls.',
  accn='Public streets and sidewalks only; every building is private. Park downtown by the Hall of Waters and walk east. The pin is a point in the middle of the district, not a building.',
  links=[['National Register form (NPGallery)', 'https://npgallery.nps.gov/GetAsset/fb78e52d-b7b9-4048-bb37-975616d209a6'], W('National Register of Historic Places listings in Clay County, Missouri')], brick='?'),

N('elms-historic-district-excelsior-springs-mo', 'The Elms Historic District, Excelsior Springs', 'Excelsior Springs', 'kcmo', 'town', 'standing',
  39.33740, -94.22611, 'area', 'view', 'walk', 'hotels', '1887–1963',
  'Listed in 2014: 55 buildings, sites and structures, anchored by the Elms Hotel, in the two plats called Central Park and the Elms Addition. It was built up from 1911 as a place of boarding houses and houses round the hotel, with two railway depots, three churches and a school. The district runs from about 1887 to 1963.',
  look='Tudor Revival, Gothic Revival and bungalow houses along Regent Avenue, Elms Boulevard and Kansas City Avenue; stone retaining walls and planted medians on Regent Avenue; the 1912 stone Elms Hotel; St. Luke\'s Episcopal Church; St. Ann Church; and the two old Wabash depots (separate entries). Private houses are seen from the street only.',
  accn='Public streets; the hotel and houses are private. Park on Regent Avenue by the hotel or at the Hall of Waters and walk.',
  links=[W('The Elms Historic District')], brick='?'),

N('hall-of-waters-west-district-excelsior-springs-mo', 'Hall of Waters Commercial West Historic District, Excelsior Springs', 'Excelsior Springs', 'kcmo', 'town', 'standing',
  39.34180, -94.22450, 'area', 'view', 'walk', 'hotels', '1894–1948',
  'Twenty buildings on the west side of downtown, listed in 1999, built between about 1894 and 1948: Victorian, Classical Revival and Art Deco. Wikipedia names the Post Office (1914), the McCleary Thornton-Minor Hospital (about 1910), the Montgomery Ward Building (1929), J. J. Newberry and J. C. Penney (both about 1929), the Elks Lodge (1913-1926), the Washington Hotel and Orpheus Theatre, the I.O.O.F. Building (1913-1917), the Arlington Hotel (1899-1900) and the Ideal Hotel (about 1900-1905). Several of those are separate entries on the Atlas; the Ideal Hotel, the hospital, Newberry, Penney and I.O.O.F. buildings are only named here.',
  look='A walk along West Broadway and the streets off it, past two- and three-story brick fronts. The district\'s 1999 form could not be read, so which buildings keep their original fronts is not checked.',
  accn='Public sidewalks downtown; the buildings are shops and offices (private). Free street parking nearby; not checked.',
  links=[W('Excelsior Springs Hall of Waters Commercial West Historic District')], brick='?',apart='hall-of-waters-excelsior-springs-mo: the Hall of Waters itself; this is the commercial district west of it, named for it'),

N('hall-of-waters-east-district-excelsior-springs-mo', 'Hall of Waters Commercial East Historic District, Excelsior Springs', 'Excelsior Springs', 'kcmo', 'town', 'standing',
  39.34220, -94.22080, 'area', 'view', 'walk', 'hotels', '1894–1948',
  'Twenty-four buildings and two structures round the Hall of Waters, listed in 1999, built between about 1894 and 1948. Wikipedia names the Flanders Dry Goods Store (about 1900-05), the A. M. Howard Drug Store (1905-09), the Clay County State Bank (1906), the Huey Building (1908), the Oriental Bazaar (1908), the Excelsior Baths and Broadway Rooms, the Eagles Lodge Hall (about 1905-09) and the Kennedy Building (1902).',
  look='Victorian commercial fronts along East Broadway either side of the 1936-38 Hall of Waters (its own entry). The 1999 form could not be read, so which fronts remain unaltered is not checked.',
  accn='Public sidewalks downtown; shops and offices are private. Park by the Hall of Waters; hours of individual businesses not checked.',
  links=[W('Excelsior Springs Hall of Waters Commercial East Historic District')], brick='?',apart='hall-of-waters-excelsior-springs-mo: the Hall of Waters itself; this is the commercial district east of it, named for it'),

N('royal-hotel-excelsior-springs-mo', 'Royal Hotel (Wholf\'s Tavern), 201 South Street, Excelsior Springs', 'Excelsior Springs', 'kcmo', 'hotel', 'standing',
  39.34116, -94.22419, 'exact', 'view', 'drive', 'hotels', '1898–1998',
  'It began as Wholf\'s Tavern in 1898, built by local businessmen who feared the town would lose well-off guests after the first Elms Hotel burned; a man named James Snapp later ran it as a tavern. It grew into a much larger hotel, the Royal, with a rooftop ballroom and a rooftop sign, and was one of the hotels licensed to give the town\'s sulpho-saline baths. Sources disagree on its height: Missouri State Parks (as quoted by the Excelsior Citizen) says six stories; the newspaper\'s 2025 story says five. It stood empty from 1998. In 2025 a Kansas City restoration firm bought it; the newspaper showed demolition under way on its eastern side and a plan to restore the rest as rooms, a ballroom and shops, finishing about mid-2027.',
  look='A tall masonry hotel on a corner lot, with its rooftop sign and former wrap-around porch to look for. The state survey, as quoted in the newspaper, calls its original character well kept because it never had a major fire. It is a building site while work goes on: keep to the street.',
  accn='Private; being rebuilt. Look from South Street. Do not enter. Street parking nearby.',
  links=[['Excelsior Citizen, September 9, 2025: plans for the Royal Hotel', 'https://excelsiorcitizen.com/the-royal-set-to-rise-again-as-restoration-company-purchases-the-historic-landmark-hotel'], W('Excelsior Springs Hall of Waters Commercial West Historic District')], conf='mixed', brick='?'),

N('superior-well-pagoda-excelsior-springs-mo', 'Superior No. 1 well and pagoda, Fishing River Linear Park, Excelsior Springs', 'Excelsior Springs', 'kcmo', 'water', 'standing',
  39.33890, -94.22440, 'area', 'public', 'walk', 'hotels', 'pagoda 1901',
  'The pagoda over the Superior spring was built in 1901. The 2012 Register multiple-property form calls it one of only two surviving pavilions in Excelsior Springs that also stand over their own well (the other is a stone one for the Link Soda and Sulpho Salt springs). A city trail guide says the "historic Superior Well" can be seen from the Fishing River Linear Park Trail, and visitor guides call it the only complete mineral-spring pagoda left in town. The spring is one of the saline waters sold in the town\'s bath houses.',
  look='A small pagoda over the well, on or beside the paved Fishing River Linear Park Trail. The pin marks the park area, not the pagoda itself, which was not found on the aerial; the trail guide places it on the Fishing River Linear Park Trail near the Elms. Condition not checked.',
  accn='Fishing River Linear Park is a city park and trail system (the city\'s trail guide); park hours not checked. The Elms Hotel and Hall of Waters are close by. A mineral well: do not drink from it.',
  links=[['National Register multiple-property form (NPGallery)', 'https://npgallery.nps.gov/GetAsset/023103d8-f693-4dac-a575-e1c33e6e0dda'], ['City trail guide (PDF)', 'https://www.kansascityhiker.com/s/Downtown-Trail-System-Excelsior-Springs-MO.pdf']], conf='mixed', brick='no'),

N('link-soda-sulpho-salt-pavilion-excelsior-springs-mo', 'Link Soda and Sulpho Salt spring pavilion, East Excelsior Street, Excelsior Springs', 'Excelsior Springs', 'kcmo', 'water', 'traces',
  39.34295, -94.22218, 'area', 'view', 'drive', 'hotels', 'early 1900s',
  'A stone pavilion, now partly standing, over the Link Soda and Sulpho Salt springs. The 2012 Register form calls it a stone pagoda on East Excelsior Street. Search results quoting a Missouri State Parks survey describe the remains of a circular stone balustrade of square-cut, quarry-faced limestone, built after an earlier brick structure over the wells was torn down. Sources differ on the address: an Excelsior Citizen article lists the Sulfo Salt Spring at 200 East Excelsior Street; the survey is quoted as 120 East Bluff Street.',
  look='A curved low stone wall of rough-faced limestone near the street, the remnant of the pavilion. Which lot it is on was not settled, so the pin is only the near area.',
  accn='Probably private lots in a residential block; look from East Excelsior Street and do not step onto the property. Owner not checked.',
  links=[['National Register multiple-property form (NPGallery)', 'https://npgallery.nps.gov/GetAsset/023103d8-f693-4dac-a575-e1c33e6e0dda'], ['Excelsior Citizen, November 24, 2024: the sulpho-saline wells', 'https://excelsiorcitizen.com/secrets-of-the-depths-excelsior-springs-sulpho-saline-wells/']], conf='mixed', brick='no'),

N('salem-road-salt-sulphur-wells-excelsior-springs-mo', 'Salt Sulphur and Sulpho-Saline wells, Salem Road, Excelsior Springs', 'Excelsior Springs', 'kcmo', 'water', 'ruins',
  39.34705, -94.21379, 'area', 'view', 'drive', 'hotels', '1888–1930s',
  'The 2012 Register form says that at 905 Salem Road the extant features of the Salt Sulphur Spring and the Sulpho Saline Spring wells, although in partial ruins, still show the steps by which mineral water was pumped and used. The Salt Sulphur spring was found in 1888. After the city bought the privately owned wells in 1935 and piped them to the Hall of Waters, most well houses were pulled down; some sites are still marked by concrete well pads and metal manholes. The form also names two of the city\'s wells at the end of North Main Street that keep several concrete and metal structures.',
  look='Concrete and metal well-related remains. What is visible from a public way was not checked, and the address may be a house. The pin is on the Salem Road address, not on a located well.',
  accn='The address on Salem Road may be private land: look from the road and ask the city or the owner before going on. Owner not checked.',
  links=[['National Register multiple-property form (NPGallery)', 'https://npgallery.nps.gov/GetAsset/023103d8-f693-4dac-a575-e1c33e6e0dda'], ['Excelsior Citizen, November 24, 2024: the sulpho-saline wells', 'https://excelsiorcitizen.com/secrets-of-the-depths-excelsior-springs-sulpho-saline-wells/']], conf='mixed', brick='no'),
]

PIN_NOTES = {
 'wabash-station-1-excelsior-springs-mo': 'Address point for 514 Leavenworth Avenue from OpenStreetMap; the Register form puts it at the corner of Dunbar and Leavenworth.',
 'wabash-station-2-excelsior-springs-mo': 'OpenStreetMap restaurant point at 646 Kansas City Avenue South.',
 'st-lukes-episcopal-church-excelsior-springs-mo': 'Address point for 404 Regent Avenue from OpenStreetMap.',
 'st-ann-catholic-church-excelsior-springs-mo': 'Address point for 552 Kansas City Avenue South from OpenStreetMap.',
 'elms-pump-house-well-carriage-house-excelsior-springs-mo': 'Behind the Elms Hotel; the three buildings are not individually located.',
 'barbee-memorial-church-excelsior-springs-mo': 'Address point for 438 Benton Avenue from OpenStreetMap.',
 'hiawatha-rooming-house-excelsior-springs-mo': 'Address point for 101 Linden Avenue from OpenStreetMap.',
 'boarding-house-district-excelsior-springs-mo': 'Middle of the streets the Register form names; the Register gives no point.',
 'elms-historic-district-excelsior-springs-mo': 'Register point for the district (Wikipedia).',
 'hall-of-waters-west-district-excelsior-springs-mo': 'West Broadway downtown, among the Atlas pins for its named buildings; the Register point on Wikipedia is in a residential block 1 km west and was not used.',
 'hall-of-waters-east-district-excelsior-springs-mo': 'East Broadway beside the Hall of Waters; the Register point on Wikipedia falls in woods and was not used.',
 'royal-hotel-excelsior-springs-mo': 'Address point for 201 South Street from OpenStreetMap.',
 'superior-well-pagoda-excelsior-springs-mo': 'Fishing River Linear Park, near the Elms; the pagoda was not located exactly.',
 'link-soda-sulpho-salt-pavilion-excelsior-springs-mo': 'Address point for 200 East Excelsior Street; sources disagree on the address.',
 'salem-road-salt-sulphur-wells-excelsior-springs-mo': 'Address point for 905 Salem Road from OpenStreetMap; no well was located.',
}
