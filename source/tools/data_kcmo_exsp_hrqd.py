# November 23, 2026: Excelsior Springs, Kearney, Smithville, Missouri City and Liberty, Clay County, Missouri, north-east of Kansas City.
# Part of filling in the Kansas City area on purpose for a local researcher. The Atlas had one place within 25 km of Excelsior Springs.
# Facts from the linked sources only: Wikipedia read as raw text (tools/wiki_raw.py), the Friends of the James Farm page, and search
# results that quote the pages of the Jesse James Bank Museum and Liberty Jail. The National Register forms were not read.
from data_b import N
from data_ma import W

PLACES = [
N('hall-of-waters-excelsior-springs-mo', 'Hall of Waters', 'Excelsior Springs', 'kcmo', 'water', 'standing',
  39.34167, -94.22222, 'site', 'open', 'drive', '', '1936–1937',
  'The Hall of Waters stands on the site of Excelsior Springs\' first spring, found in the 1880s. It was built in 1936–37 as a federal Public Works Administration project (No. 5252), to house mineral baths and a water bottling plant, and was designed by the firm Keene & Simpson. '
  'It is now the city hall and has a visitor centre and a museum.',
  look='A 30-foot boiler stack tower of cast stone with an aluminum cap. Search results describe a self-guided walking tour at no charge, one bath department that still has its old bathing equipment, and a water bar that is closed to the public; none of this was confirmed on a page of the city, so ask at the front desk. Interior not otherwise checked.',
  accn='City hall at 201 E. Broadway, owned by the city of Excelsior Springs. Street parking downtown. Hours not checked: the city\'s own page could not be read, and the hours search results gave disagreed.',
  links=[W('Hall of Waters'), W('Excelsior Springs Hall of Waters Commercial East Historic District')],
  hours='?', brick='?'),

N('elms-hotel-excelsior-springs-mo', 'The Elms Hotel and Spa', 'Excelsior Springs', 'kcmo', 'hotel', 'standing',
  39.33693, -94.22589, 'exact', 'open', 'drive', 'hotels,burned', '1912',
  'Excelsior Springs\' resort hotel burned twice before the stone building now on the site opened on September 7, 1912: the first Elms (opened 1888) burned in May 1898, and a second, 300-room Elms (opened July 1909) burned in October 1910. '
  'The hotel closed in 1971, reopened in 1977 under local owners, was bought by the city in 1995 and renovated in 1998, and closed again for a renovation in 2011 before reopening in 2012. A 1931 hold-up of the hotel ended in a gunfight in the lobby and on the veranda.',
  look='The 1912 building is made of native stone. It is a working hotel and spa, so the lobby and public rooms can be seen by guests and by those who ask at the desk; interior not checked. Search results disagree on the second hotel\'s dates (Wikipedia gives 1909 to 1910; one travel article gives only 1898, 1910 and 1912).',
  accn='Private hotel at 401 Regent Street; hotel parking. Hours not checked: it is open to guests, and the hotel\'s own page was not read.',
  links=[W('The Elms Hotel and Spa'), ['The Elms Hotel history page', 'https://www.elmshotelandspa.com/elms-history.htm']],
  hours='?', brick='no'),

N('colonial-hotel-excelsior-springs-mo', 'Colonial Hotel (Colonial Apartments)', 'Excelsior Springs', 'kcmo', 'hotel', 'standing',
  39.34250, -94.22028, 'site', 'view', 'drive', 'hotels', '1924',
  'Built in 1924 for people staying a long while in Excelsior Springs to "take the waters" at the town\'s mineral springs. It is a three-story red brick building with a three-tiered porch held up by four nearly full-height square brick columns, and is on the National Register of Historic Places (2010).',
  look='The tiered porch and brick columns on the front. Interior not checked.',
  accn='Look from the public sidewalk; the building has been used as apartments and is not known to open to visitors. Owner not checked.',
  links=[W('Colonial Hotel (Excelsior Springs, Missouri)')], brick='yes'),

N('ligon-apartments-excelsior-springs-mo', 'Ligon Apartments (Udell Apartments)', 'Excelsior Springs', 'kcmo', 'hotel', 'standing',
  39.34273, -94.22168, 'area', 'view', 'drive', 'hotels', '1917',
  'A red brick apartment building of 1917, with a two-story porch under a low hipped roof carried on four square brick columns. Like the Colonial, it housed visitors who stayed a long time for the mineral waters. It was listed on the National Register in 2010.',
  look='The two-story colonnade on the front. Interior not checked.',
  accn='Look from the public sidewalk; used as apartments. Owner not checked.',
  links=[W('Ligon Apartments')], brick='yes'),

N('wyman-school-excelsior-springs-mo', 'Wyman School', 'Excelsior Springs', 'kcmo', 'civic', 'standing',
  39.34288, -94.22829, 'exact', 'view', 'drive', '', '1912–mid-1990s',
  'Excelsior Springs High School when built in 1912, later Wyman Elementary, named for Anson Wyman, founder of the town. It stopped being a school in the mid-1990s, served as a community theatre, then stood empty. The city bought it. '
  'A partial roof collapse was noted in 2008; the separate 1913 boiler house was pulled down in July 2022 after an environmental study. News reports quoted in a search say the main building still stands, and that the city awarded a contract for removing hazardous materials in September 2025.',
  look='A three-story brick Classical Revival school on a limestone foundation, with its boiler house gone. Dangerous inside: do not go in.',
  accn='City-owned and closed. Look from Dunbar Street, 100 Dunbar St. Its future was still being discussed in the news reports found.',
  links=[W('Wyman School'), ['Excelsior Citizen: Wyman School power plant demolished', 'https://excelsiorcitizen.com/powering-down-wyman-school-power-plant-demolished']],
  conf='mixed', brick='yes'),

N('first-methodist-church-excelsior-springs-mo', 'First Methodist Church', 'Excelsior Springs', 'kcmo', 'worship', 'standing',
  39.34273, -94.22436, 'site', 'view', 'drive', '', '1903; 1948',
  'On Marietta Street. The church was built in 1948 and kept parts of an earlier Gothic Revival church of 1903. It is on the National Register of Historic Places (2009).',
  look='A Gothic Revival church. Windows, woodwork and interior not checked.',
  accn='Active church; service times not checked. Look from the street.',
  links=[W('First Methodist Church (Excelsior Springs, Missouri)')], brick='?'),

N('missouri-city-savings-bank-mo', 'Missouri City Savings Bank Building (Nowlin Store)', 'Missouri City', 'kcmo', 'civic', 'standing',
  39.23833, -94.29417, 'site', 'view', 'drive', '', 'about 1858',
  'Built about 1858 and said to be the oldest and largest commercial building left in Missouri City, on the Missouri River bottom. Shops filled the first floor and a meeting hall and private rooms the second. It was listed on the National Register in 2010.',
  look='A two-floor commercial building at 417-419 Main Street. Interior and present use not checked.',
  accn='Look from Main Street. Owner and use not checked.',
  links=[W('Missouri City Savings Bank Building and Meeting Hall')], brick='?'),

N('james-farm-kearney-mo', 'James Farm (Jesse James Birthplace)', 'Kearney', 'kcmo', 'landmark', 'standing',
  39.39333, -94.32167, 'site', 'open', 'drive', '', 'about 1822',
  'The farmhouse where Jesse and Frank James grew up. The oldest part is a log house of about 1822, later enlarged with a frame addition into a T shape. Clay County bought the farm in 1974, and it is run as a house museum with a visitor centre.',
  look='The log and frame farmhouse, shown on guided tours, and the visitor centre\'s museum. On the National Register since 1972.',
  accn='Owned by Clay County. Hours are from the Friends of the James Farm page; a search listing also gives Sunday noon to 4 p.m. and tickets of about $8.50 to $10 (two listings disagree), so call (816) 736-8500 before going. Parking at the farm.',
  links=[W("James Brothers' House and Farm"), ['Friends of the James Farm: visit', 'https://www.jessejames.org/the-farm']],
  hours='Monday to Saturday 9 a.m. to 4 p.m. (the Friends page; one listing adds Sunday noon to 4)', brick='no'),

N('downtown-smithville-historic-district-mo', 'Downtown Smithville Historic District', 'Smithville', 'kcmo', 'town', 'standing',
  39.38722, -94.58028, 'area', 'public', 'walk', '', '1868–1964',
  'Thirty buildings in Smithville\'s old business centre, built between about 1868 and 1964, in Gothic Revival and Classical Revival styles. The Register lists the IOOF Lodge Hall, later the city hall (about 1890), and the C. C. Kindred Motor Company building among them. It was listed in 2014.',
  look='Walk the main street and look at the upper facades. Which buildings keep their original fronts was not checked.',
  accn='Public streets; the shops open their own hours. Park on the street.',
  links=[W('Downtown Smithville Historic District')], brick='?'),

N('clay-county-savings-bank-liberty-mo', 'Clay County Savings Association Building (Jesse James Bank Museum)', 'Liberty', 'kcmo', 'civic', 'standing',
  39.24711, -94.41899, 'exact', 'open', 'drive', '', '1859',
  'Built in 1859 as a two-story Federal-style brick building. On February 13, 1866 armed men robbed the bank of at least $60,000 and shot a passer-by dead outside, one of the first daylight bank robberies. They were never caught; the James–Younger gang, Jesse James or Archie Clement have been named, but this is not proven. The bank settled with its creditors for 60 cents on the dollar and closed. '
  'It is now a museum run by Clay County Historic Sites.',
  look='The 1859 building on Liberty Square. Hours below are from search results that quote the museum\'s listings, which also mention a closing in January and February in one place: check before going. Interior not otherwise checked.',
  accn='In the town square at 103 N. Water Street; street parking. Tickets are priced by age (listings give from $6.50 to $7).',
  links=[W('Clay County Savings Association Building')],
  hours='Monday to Saturday 10 a.m. to 4 p.m. (from listings; may close January and February)', brick='?'),

N('liberty-jail-mo', 'Liberty Jail Historic Site', 'Liberty', 'kcmo', 'inst', 'marker',
  39.24852, -94.42075, 'exact', 'open', 'drive', '', '1834–1853',
  'The Clay County jail from 1834 to 1853. Joseph Smith and five companions were held here from about November 30, 1838 to April 1839; the Latter Day Saint movement values it for that winter. The jail was pulled down and a house built over it, and the church bought the site in 1939. '
  'The jail seen today is a partial reconstruction of 1963 built inside a visitors\' centre on the original site, with a limestone front on the east side and a cutaway view of the upper room and the dungeon. The walls of the old jail were two feet of stone, and double.',
  look='The reconstruction and the exhibits in the visitors\' centre. Free admission was not confirmed from the page opened.',
  accn='Run by the Church of Jesus Christ of Latter-day Saints at 216 N. Main Street. Hours: the church\'s own pages quoted in search results gave two different schedules, so they are not stated here; check the church\'s Liberty Jail page. Phone (816) 781-3188 from one listing.',
  links=[W('Liberty Jail'), ['Liberty Jail on churchofjesuschrist.org', 'https://www.churchofjesuschrist.org/learn/locations/liberty-jail']],
  hours='?', conf='mixed', brick='?'),

N('clinton-house-liberty-mo', 'Clinton House', 'Liberty', 'kcmo', 'landmark', 'standing',
  39.23961, -94.42060, 'site', 'view', 'drive', '', '1875 or 1889',
  'An Italianate house at 404 S. Main Street in Liberty, with stone keystones cut with the fleur-de-lis. It was listed on the National Register in 1978. Wikipedia gives two dates for it: the article says 1875, its category says 1889. The dates are not confirmed.',
  look='The Italianate front and the stone keystones. Interior not checked.',
  accn='Look from the street; use and owner not checked.',
  links=[W('Clinton House (Liberty, Missouri)')], conf='mixed', brick='?'),

N('jewell-hall-liberty-mo', 'Jewell Hall, William Jewell College', 'Liberty', 'kcmo', 'civic', 'standing',
  39.24694, -94.41222, 'area', 'view', 'drive', '', '1850–1853',
  'The first main building of William Jewell College, built 1850–53 as a three-story H-shaped building of brick and Missouri limestone in Classical Revival style. Its inside was completely remodelled in 1946–48. It is on the National Register (1978).',
  look='The columned front from the campus lawn. Interior not checked.',
  accn='On the campus of William Jewell College; look from the campus road. Rules for visitors on campus were not checked.',
  links=[W('Jewell Hall')], brick='?'),

N('odd-fellows-home-liberty-mo', 'Odd Fellows Home District', 'Liberty', 'kcmo', 'inst', 'standing',
  39.22895, -94.40725, 'site', 'view', 'drive', '', '1900–1935',
  'The Missouri Odd Fellows\' home and hospital at Liberty: three listed buildings, the Administration Building, the Old Folks Building (1907–08, said to be designed by E. C. Eckle) and the Old Hospital (1923), in Tudor and Jacobethan Revival style, with the home\'s cemetery. It was listed on the National Register in 1987. '
  'A local news item says the old home now holds Belvoir Winery and Inn; whether the winery is open to visitors and when was not checked.',
  look='Tudor Revival buildings and the cemetery on the grounds. Interior not checked.',
  accn='Private property: look from the public road unless the winery is open, and check with it first.',
  links=[W('Odd Fellows Home District')], conf='mixed', brick='?'),

N('woodneath-farmhouse-kc-mo', 'Woodneath (Elbridge Arnold Homestead)', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.25333, -94.46750, 'site', 'open', 'drive', '', '1855–1856',
  'A Greek Revival farmhouse built in 1855–56 and lived in by the Arnold, Moore and Crouch families until the late 1970s. Presley Moore named it Woodneath for the oaks, pines and sugar maples. The library system bought it and 33 acres in 2008 and built a new library branch around the restored house in 2013. It is on the National Register (1978).',
  look='The farmhouse inside the library building, planned as a "story center" for the library. Open to library visitors; how much of the house can be entered was not checked.',
  accn='Mid-Continent Public Library branch; parking lot. Library hours were not checked.',
  links=[W('Woodneath')], hours='?', brick='?'),
]

PIN_NOTES = {
 'hall-of-waters-excelsior-springs-mo': 'Pin is the Wikipedia coordinate for the building at 201 E. Broadway.',
 'elms-hotel-excelsior-springs-mo': 'Pin is the National Register coordinate, moved about 43 m onto the large hotel building seen on Esri satellite.',
 'colonial-hotel-excelsior-springs-mo': 'Pin is the National Register list coordinate.',
 'ligon-apartments-excelsior-springs-mo': 'Pin is the National Register list coordinate; the aerial shows a street of houses and I could not tell which building it is, so it marks the block.',
 'wyman-school-excelsior-springs-mo': 'Pin is the map address lookup for 100 Dunbar Street, moved about 57 m onto the large school building seen on Esri satellite; the address point fell on the cleared lot of the demolished boiler house.',
 'first-methodist-church-excelsior-springs-mo': 'Pin is the National Register list coordinate on Marietta Street.',
 'missouri-city-savings-bank-mo': 'Pin is the National Register coordinate for 417-419 Main Street.',
 'james-farm-kearney-mo': 'Pin is the National Register coordinate for the farm.',
 'downtown-smithville-historic-district-mo': 'Pin is the middle of the National Register district.',
 'clay-county-savings-bank-liberty-mo': 'Pin is the National Register coordinate on Liberty Square.',
 'liberty-jail-mo': 'Pin is the Wikipedia coordinate for the visitors\' centre at 216 N. Main Street.',
 'clinton-house-liberty-mo': 'Pin is the map address lookup for 404 S. Main Street; the Register coordinate fell on the street.',
 'jewell-hall-liberty-mo': 'Pin is the National Register coordinate on the William Jewell College campus; the aerial could not show which building is Jewell Hall, so it marks the campus area.',
 'odd-fellows-home-liberty-mo': 'Pin is moved about 126 m from the Register point (an empty field) onto the group of old buildings seen on Esri satellite.',
 'woodneath-farmhouse-kc-mo': 'Pin is the National Register coordinate; the library was built around the house.',
}
BATCH = {'key': 'kcmo_exsp_hrqd', 'label': 'Excelsior Springs and Clay County, Missouri', 'added': '2026-11-23 07:50'}
