# Kansas City, Missouri: Automobile Row and a few Midtown survivors, November 25, 2026.
# Part of filling in the Kansas City area on purpose for a local researcher. The Atlas had none of these buildings.
# Facts from the linked sources only: Wikipedia read as raw text, the Kansas City Auto Museum, Clio, Flatland KC and KCUR pages,
# the National Park Service's own record pages and the full Register form for the substation (read). The other Register forms
# could not be read (the park service serves only a placeholder for them), so builders and dates are given only where a page said so.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_auto_xqmv', 'label': 'Kansas City: Automobile Row and Midtown survivors', 'added': '2026-11-25 06:00'}

PLACES = [
N('buick-automobile-company-building-kc-mo', 'Buick Automobile Company Building, 216 Admiral Boulevard, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.10572, -94.57977, 'exact', 'view', 'drive', '', '1907–1948',
  'A three-story brick building put up for the Buick company as a showroom and warehouse. Clio says it was the first building in Kansas City made for a car company to show and store its line, and that Buick used it from 1908 to 1948. Wikipedia gives the building date as 1907 and Clio as 1908. '
  'Kansas City grew into one of the country\'s biggest car markets in the 1910s, and this was one of the first dealerships on what became Automobile Row. It is on the National Register of Historic Places (2004).',
  look='A brick front with some Tudor Revival touches (Wikipedia). It held a showroom on the ground floor, repair shops in the basement and on the third floor and a garage on the second. A three-story brick addition was made around 1934 and a two-story extension at the rear in 1958. Clio says it is now loft apartments, so the inside is not open.',
  accn='Private apartments at 216 Admiral Boulevard, on the north edge of downtown. Look from the sidewalk; the residents\' building is not open to visitors. Parking was not checked.',
  links=[W('Buick Automobile Company Building'), ['Clio: Buick Automobile Company Building', 'https://theclio.com/entry/157288'], ['Kansas City Auto Museum: Automobile Row', 'https://kansascityautomuseum.com/automobile-row/']],
  conf='mixed', brick='?'),

N('mcgee-1901-automotive-service-building-kc-mo', '1901 McGee Street Automotive Service Building, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.09013, -94.57988, 'exact', 'view', 'drive', '', '1912',
  'A car dealership built in 1912 by the builder C. C. Smith, early in Automobile Row\'s life, when car ownership was starting to climb. Clio names three dealers who held it: the Dey Motor Company, the Century Motor Company and Erwin Davis Motors. It stood empty from 1935 to 1940 in the Depression and a new dealership took it at the start of World War II. '
  'It was listed on the National Register of Historic Places in 2009 and is the one separately listed building among the McGee Street dealerships.',
  look='A two-story commercial block with walls of hollow tile (Wikipedia). Large ground-floor windows that once showed cars to people on the sidewalk and the streetcar are still there (Clio). What it is used for now was not checked.',
  accn='Private building at 1901 to 1907 McGee Street in the East Crossroads. Look from the sidewalk. Parking was not checked.',
  links=[W('1901 McGee Street Automotive Service Building'), ['Clio: 1901 McGee Street Automotive Service Building', 'https://theclio.com/tour/2305/12']],
  brick='?'),

N('kirkwood-building-1737-mcgee-kc-mo', 'Kirkwood Building, 1737 McGee Street, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.09186, -94.57979, 'exact', 'view', 'drive', '', '1920',
  'A car dealership built in 1920 to a design by Wight and Wight, the Kansas City firm better known for the Nelson-Atkins Museum and several courthouses. Its first tenants were the Gridley Motor Company and the Indiana Truck Company. Car dealers used it for only the first several years; by 1954 it housed the Central Surety and Insurance Corporation.',
  look='Clio calls the style a restrained, streamlined Neoclassical and says it was made for commercial use, with a showroom, sales offices and garage space, and large windows so that people on foot or on the streetcar could see the new models. It says the building is well preserved. What it holds now was not checked.',
  accn='Private building at 1737 McGee Street in the East Crossroads. Look from the sidewalk. Whether it is itself on the National Register was not checked; it stands inside the McGee Street dealership district. Parking was not checked.',
  links=[['Clio: Kirkwood Building', 'https://theclio.com/tour/2305/14'], ['Kansas City Auto Museum: Automobile Row', 'https://kansascityautomuseum.com/automobile-row/']],
  brick='yes'),

N('auto-coach-building-kc-mo', 'Auto Coach Building, 1730 to 1734 Oak Street, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.09226, -94.57931, 'exact', 'view', 'drive', '', '1917–1926',
  'A three-story building of brick and stone on the edge of Automobile Row, put up in two stages, in 1917 and 1926. Wikipedia names the architects as Raney and Botkin and E. L. Bryant and does not say who the "auto coach" business was. It was listed on the National Register of Historic Places in 2007.',
  look='A three-story brick and stone commercial block (Wikipedia). Its use now and its interior were not checked.',
  accn='Private building on Oak Street between 17th and 18th streets. Look from the sidewalk. Parking was not checked.',
  links=[W('Auto Coach Building')],
  brick='?'),

N('mcgee-street-automotive-district-kc-mo', 'McGee Street Automotive Historic District, Kansas City', 'Kansas City', 'kcmo', 'town', 'standing',
  39.09071, -94.58054, 'area', 'view', 'drive', '', '1912–1968',
  'A block of old car-dealer buildings along McGee Street between East 17th and East 20th streets, listed on the National Register of Historic Places in 2018 for the years 1912 to 1968. By the mid-1910s, 22 car makers had dealers or factory branches in Kansas City, the Kansas City Auto Museum says, and the row began on Main, Grand, McGee and Locust between 11th and 18th streets and later spread south.',
  look='Plain commercial buildings with big display windows, the Park Service says One-Part Commercial Block. Flatland KC says the building at 1824 to 1832 McGee was finished in 1919 for dealers, had stood empty with a T-shirt shop as its last use, and a developer meant to turn it into offices. That plan was reported some years ago and what was built was not checked. The pin marks 1824 McGee, near the middle of the district.',
  accn='City streets, open to walk at any time. The buildings are private; look from the sidewalk. Street parking and paid lots were not checked.',
  links=[['National Park Service record: McGee Street Automotive Historic District', 'https://npgallery.nps.gov/AssetDetail/NRIS/100002427'], ['Flatland KC: office plan for 1824 McGee', 'https://flatlandkc.org/news-issues/developer-plans-to-convert-former-auto-row-building-on-mcgee-into-offices/'], ['Kansas City Auto Museum: Automobile Row', 'https://kansascityautomuseum.com/automobile-row/']],
  brick='?'),

N('greenlease-cadillac-building-kc-mo', 'Greenlease Cadillac Building, 2929 McGee Trafficway, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.07401, -94.57906, 'exact', 'view', 'drive', '', '1918',
  'Robert Greenlease won a Cadillac franchise in 1908 and outgrew his shop at 1612 Grand. In 1916 he announced a new building at Gillham Road and McGee Trafficway, south of 29th Street, convenient to downtown and the new suburbs to the south. The Kansas City Auto Museum says it opened in 1918, designed by the architect Lewis Haverkamp after he and Greenlease toured showrooms and service centers around the country. '
  'It was listed on the National Register of Historic Places in 2003 and was turned into condominiums in 2006.',
  look='The museum describes a triangular showroom that could display up to 12 cars, with Cadillac crests carved into the inside columns and into the terra-cotta of the upper outside walls. Whether the crests are still there after the conversion was not checked.',
  accn='Private condominiums on McGee Trafficway just south of 29th Street. Look from the sidewalk. Parking was not checked.',
  links=[['Kansas City Auto Museum: Greenlease Cadillac', 'https://kansascityautomuseum.com/?p=4645']],
  brick='yes'),

N('pickwick-plaza-kc-mo', 'Pickwick Plaza (Pickwick Hotel and Greyhound bus terminal), Kansas City', 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.10251, -94.57926, 'exact', 'view', 'drive', '', '1929–1930',
  'A downtown block built in 1929–1930 to a design by Wight and Wight (the firm behind City Hall and the Jackson County Courthouse). It held an 11-story hotel, a six-story office building, a three-story garage and a six-story bus terminal, said to be the largest west of the Mississippi. At its peak the terminal handled 4,433 scheduled departures a month. '
  'As a county judge in the early 1930s Harry Truman stayed at the hotel and wrote the memoir later called the "Pickwick Papers" on its stationery. The hotel became subsidized housing in 1972, a fire in 1996 destroyed much of its lobby ornament, and it closed in 2009. It was turned into 260 apartments, with the old bus terminal now holding a pool. Clio puts the finish in 2017. It was listed on the National Register of Historic Places in 2005.',
  look='A tall brick and cut-stone hotel with a clock tower over McGee Street. The clock, eight feet across and seven stories up, was out of order for about 60 years and put back for the reopening (Flatland KC). Clio calls the style Art Deco; Flatland KC calls it "streamline Gothic". The hotel and bus terminal are apartments now, so the inside is not open.',
  accn='Private apartments (East 9 at Pickwick Plaza) at 10th Street and McGee, downtown. Look from the sidewalk. Parking was not checked.',
  links=[['Clio: Pickwick Complex', 'https://theclio.com/entry/39878'], ['Flatland KC: the Pickwick clock goes back up', 'https://flatlandkc.org/news-issues/historic-pickwick-plaza-gets-its-landmark-clock-back-just-in-time-for-grand-opening/']],
  conf='mixed', brick='yes'),

N('kcpl-substation-a-kc-mo', 'Kansas City Power and Light Substation "A", 2645 Madison Avenue, Kansas City', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.07884, -94.59495, 'exact', 'view', 'drive', '', '1922',
  'A small brick power substation built in 1922 for the Kansas City Power and Light Company, designed by H. F. Harrison. The Register form calls it the city\'s first fully automatic substation still standing: it ran without anyone on duty, so it needed no big windows. '
  'It was listed on the National Register of Historic Places in 2018 for its place in the spread of electric service. The form says the building stood vacant when it was written, and that Robert Shapiro owned it from 1981 to 2017.',
  look='A one-story rectangle with a concrete base and walls of decorated "tapestry" brick: tall panels flank the door on the west front, and the east wall is brick laid in a seven-course common bond. The openings once had metal shutters and louvers. Garages on the north side, which are not original, stand where two transformers once sat; the 12-foot concrete walls that separated them still stand inside the garages. The inside is bare of equipment. What it is used for now was not checked.',
  accn='Private building at the corner of Madison Avenue and West 27th Street in a residential block, a few blocks east of the Southwest Boulevard industrial strip and next to Interstate 35. Look from the sidewalk. Parking was not checked.',
  links=[['National Register registration form (National Park Service)', 'https://npgallery.nps.gov/GetAsset/8eb0adc9-d269-4cd5-8f91-fa67e9faa56c']],
  brick='yes'),

N('holy-rosary-church-columbus-park-kc-mo', 'Holy Rosary Church, Columbus Park (Little Italy), Kansas City', 'Kansas City', 'kcmo', 'worship', 'standing',
  39.1092, -94.57276, 'exact', 'view', 'drive', '', '1903',
  'The parish was founded in 1891 for the Italian families of the North End. Its first church, at 5th Street and Forest Avenue, was built five years later and burned to the ground on Easter Sunday 1903. A new church was built the same year on the southeast corner of Missouri Avenue and Campbell Street and dedicated on a day in 1903 by Monsignor Hogan. '
  'Flatland KC calls it the rock of Columbus Park. Italian prisoners of war were let attend Mass here in World War II and gave the church a carved wooden statue of Mary when the war ended. The church is part of the Holy Rosary Historic District, listed on the National Register of Historic Places in 2007.',
  look='A church with a bell tower, whose bells ring over a neighborhood of old brick buildings, some with faded painted signs. The names of founding families are written on the church walls (Flatland KC). The Don Bosco Community Center, finished in 1940, is across Campbell Street. Interior not checked and Mass times were not read from the parish\'s own page.',
  accn='A working Catholic parish at Missouri Avenue and Campbell Street in Columbus Park. Look from the street; telephone the parish for service times before a visit. Street parking was not checked.',
  links=[['Flatland KC: what Columbus Park was like in its heyday', 'https://flatlandkc.org/curiouskc/curiouskc-what-was-columbus-park-like-in-its-heyday/'], ['Flatland KC: Holy Rosary and the North End', 'https://flatlandkc.org/news-issues/farina-valet-holy-rosary-northeast-kansas-city/']],
  brick='yes'),

N('linwood-presbyterian-church-kc-mo', 'Linwood Presbyterian Church and Home for Convalescent Employed Women, Kansas City', 'Kansas City', 'kcmo', 'worship', 'standing',
  39.06812, -94.56162, 'exact', 'view', 'drive', '', 'c. 1900',
  'A large church and community complex at Linwood Boulevard and U.S. 71. KCUR says it has been an architectural landmark of the Ivanhoe neighborhood since about 1900. The congregation shrank until it had to sell the buildings, and since the mid-1990s church and neighborhood leaders have been repairing them with tax credits, loans and gifts. '
  'It is on the National Register of Historic Places (2012) as the church and the Home for Convalescent Employed Women; no page read here said what the home was.',
  look='A large church beside the Harold Thomas Center. KCUR reported in 2014 that the work would keep the stained glass and let in more daylight, and that a new bridge would join the center to the church. How much of that was finished was not checked.',
  accn='The address on the Register is 1801 Linwood Boulevard and 3212 Michigan Avenue. KCUR reported in 2014 that the Heartland Presbytery planned to move in; who uses it now and whether it opens to visitors was not checked. Look from the street.',
  links=[['KCUR: construction at Linwood Presbyterian (2014)', 'https://www.kcur.org/community/2014-12-09/for-neighbors-construction-on-kansas-city-church-is-good-news']],
  conf='mixed', brick='yes'),
]

PIN_NOTES = {
 'buick-automobile-company-building-kc-mo': 'Address lookup for 216 Admiral Boulevard; the Wikipedia point is within a few meters.',
 'mcgee-1901-automotive-service-building-kc-mo': 'Address lookup for 1901 McGee Street, agreeing with the Register list point.',
 'kirkwood-building-1737-mcgee-kc-mo': 'Address lookup for 1737 McGee Street.',
 'auto-coach-building-kc-mo': 'Address lookup for 1730 Oak Street, agreeing with the Register list point.',
 'mcgee-street-automotive-district-kc-mo': 'Address lookup for 1824 McGee Street, near the middle of the district; the district has no published point.',
 'greenlease-cadillac-building-kc-mo': 'Address lookup for 2929 McGee Trafficway, close to the Register list point.',
 'pickwick-plaza-kc-mo': 'OpenStreetMap point for the apartments at 933 McGee Street; the Register list point lies about 35 meters north across the block.',
 'kcpl-substation-a-kc-mo': 'Address lookup for 2645 Madison Avenue, agreeing with the Register list point; the form puts it at the corner of Madison and West 27th.',
 'holy-rosary-church-columbus-park-kc-mo': 'OpenStreetMap point for the church at 531 Campbell Street; an address lookup landed on the parking lot to its south.',
 'linwood-presbyterian-church-kc-mo': 'Address lookup for 1801 Linwood Boulevard, close to the Register list point.',
}
