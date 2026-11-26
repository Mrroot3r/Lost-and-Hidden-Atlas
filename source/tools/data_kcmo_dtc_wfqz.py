# November 26, 2026: downtown Kansas City, Missouri, and a few buildings on the Paseo and Gillham Road. Earlier
# batches took nearly every National Register listing in Jackson County that has a readable source; these are
# the downtown listings that were left. Sources: Wikipedia read as raw text, the pages of St. Mary's church and of
# Knuckleheads, and a web search result that quotes the church's service times.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_dtc_wfqz', 'label': 'Kansas City, Missouri: downtown commercial buildings, the Paseo and Gillham Road', 'added': '2026-11-26 04:21'}

PLACES = [
N('title-and-trust-building-kansas-city-mo', 'Kansas City Title and Trust Building, 10th and Walnut, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.10250, -94.58167, 'site', 'view', 'walk', '', '1922',
  'A seven-storey office building on the corner of Walnut and 10th streets, begun on August 1, 1922. Sunderland and Besecke designed it and Mosby-Goodrich Construction Company built it. It was listed on the National Register of Historic Places in 2005.',
  look='The frame is reinforced concrete, faced in red brick, with cream terra cotta on the base. The site slopes, and the front has three bays on Walnut Street and seven on 10th. Inside was not checked.',
  accn='Downtown office building; look from the sidewalk. Street and garage parking downtown. Whether the public may go in was not checked. The pin is the Wikipedia coordinate, rounded.',
  links=[W('Kansas City Title and Trust Building')], brick='yes', conf='mixed'),

N('kansas-city-southern-railway-building-mo', 'Kansas City Southern Railway Building, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.10333, -94.58500, 'site', 'view', 'walk', '', '1914',
  'Local architect John McKecknie designed this downtown building, which went up in 1914. For almost ninety years, from 1914 to 2002, it was the national headquarters of the Kansas City Southern Railway Company; shops took the ground floor. It was listed on the National Register of Historic Places in 2004.',
  look='A downtown commercial front with shops at street level, which is how Wikipedia says it was used from the start. What the facade is built of and how much of the original railway offices survive were not checked.',
  accn='Downtown building; look from the sidewalk. Its present use and whether the public may go in were not checked. The pin is the Wikipedia coordinate, rounded.',
  links=[W('Kansas City Southern Railway Building (Kansas City, Missouri)')], brick='?', conf='mixed'),

N('police-station-no-4-kansas-city-mo', 'Kansas City Police Station No. 4 (later an elevator works), Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.09306, -94.58528, 'site', 'view', 'walk', '', '1916',
  'Built in 1916 as a police station to a Mission Revival design by Clarence K. Birdsall and Edgar P. Madorie. It was later the Kansas City Elevator Manufacturing Company, then the Todd Jack Company, then Turner Elevator Manufacturing, and at some time a Works Progress Administration office. It was listed on the National Register of Historic Places in 2005.',
  look='The style is Mission Revival. What the building looks like today and what it is used for now were not checked.',
  accn='City street; look from the sidewalk. Ownership, present use and parking were not checked. The pin is the Wikipedia coordinate, rounded.',
  links=[W('Kansas City Police Station Number 4')], brick='?', conf='mixed'),

N('water-department-building-kansas-city-mo', 'Kansas City Water Department Building, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.11056, -94.58306, 'site', 'view', 'walk', '', '1904',
  'A commercial building of 1904 that served the city water department. It was listed on the National Register of Historic Places in 1994. Wikipedia has no more about it than that.',
  look='Nothing about its look or present use was found in a source that could be read, so there is nothing to say yet about what survives inside or out. A reader who goes could add it.',
  accn='City street; look from the sidewalk. Ownership, present use and parking were not checked. The pin is the Wikipedia coordinate, rounded, and was not confirmed on the ground.',
  links=[W('Kansas City Water Department Building')], brick='?', conf='mixed'),

N('kessler-apartments-kansas-city-mo', 'Kessler Apartments, north Paseo, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.10417, -94.56361, 'area', 'view', 'walk', '', '1925',
  'Built in 1925 and listed on the National Register of Historic Places on October 22, 2002, as one of a group of buildings at the north end of Paseo Boulevard.',
  look='An apartment building of the 1920s. Wikipedia gives only the date and the listing, so the materials and the details that survive were not checked.',
  accn='Private apartments; look from the public sidewalk only. The pin is the Wikipedia coordinate and falls in the Paseo roadway, so it marks only the stretch of boulevard where the listed apartment buildings stand.',
  links=[W('Kessler Apartments')], brick='?', conf='mixed'),

N('palace-clothing-building-kansas-city-mo', 'Palace Clothing Company Building, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.10000, -94.58083, 'site', 'view', 'walk', '', '1924',
  'Henry Guettel and Henry Auerbach founded the Palace Clothing Company in 1893. Its 1924 building by Kansas City architect Frederic E. McIlvain, in the Chicago School style, was one of the largest clothing stores in the West, with 275 feet of frontage; sales passed $6 million a year before the company closed in 1964. The building stood empty until 1972 and was then given a metal facade, which was taken off in 1984 to show the original front. It was listed on the National Register of Historic Places in 1985.',
  look='The front is mostly terra cotta and brick, with cartouches and other ornament, and the Chicago School design shows its structural frame plainly. Inside was not checked.',
  accn='Downtown commercial building; look from the sidewalk. Present use and whether the public may go in were not checked. The pin is the Wikipedia coordinate, rounded.',
  links=[W('Palace Clothing Company Building')], brick='some', conf='mixed'),

N('professional-building-kansas-city-mo', 'Professional Building, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.10083, -94.58028, 'site', 'view', 'walk', '', '1929',
  'An office building of 1929 downtown, listed on the National Register of Historic Places in 1982. Wikipedia says no more than that.',
  look='Nothing about its design or materials was found in a source that could be read, so what survives was not checked.',
  accn='Downtown office building; look from the sidewalk. Present use and whether the public may go in were not checked. The pin is the Wikipedia coordinate, rounded.',
  links=[W('Professional Building (Kansas City, Missouri)')], brick='?', conf='mixed'),

N('safeway-office-warehouse-kansas-city-mo', 'Safeway Stores Office and Warehouse Building, Kansas City', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.09111, -94.58500, 'site', 'view', 'walk', '', '1929',
  'Archer and Gloyd designed this four-storey warehouse, which J. H. Thompson built in 1929. It held Safeway\'s produce and canned goods for a region reaching from Topeka to St. Joseph, Columbia and Joplin, and housed the regional headquarters. Safeway used it until 1953, when the Halls Company bought it; a loading dock came in 1949 and another addition in 1976.',
  look='A concrete building of about 100 by 140 feet. Only the west front is dressed in brick and stone; the other sides show the bare concrete, and inside the floors rest on concrete mushroom columns. Whether the public may go in was not checked.',
  accn='Private building near downtown; look from the street. Present use and parking were not checked. The pin is the Wikipedia coordinate, rounded.',
  links=[W('Safeway Stores Office and Warehouse Building')], brick='some', conf='mixed'),

N('stuart-hall-building-kansas-city-mo', 'Stuart Hall Building (former Nabisco bakery), 2121 Central Street, Kansas City', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.08740, -94.58750, 'site', 'view', 'walk', '', '1910–1911',
  'A seven-storey factory built in 1910 and 1911 for the National Biscuit Company. Later the Stuart Hall company, which made envelopes and notebooks, used it as a warehouse and as its base. A renovation costing $24 million, finished in 2004, turned it into 127 apartments known as the Freight House Lofts or Stuart Hall Lofts.',
  look='Wikipedia says the massive brick ovens still remain in the building, though they are inside apartments and halls that are not open to the public. From the street you see a big early-1900s factory block in the Crossroads Arts District. What the outside walls are made of was not checked.',
  accn='Private apartment building; look from the sidewalk. Street parking in the Crossroads. The pin is the Wikipedia coordinate for the building at 2121 Central Street.',
  links=[W('Stuart Hall Building')], brick='?', conf='mixed'),

N('inter-state-building-kansas-city-mo', 'Inter-State Building, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.09831, -94.57779, 'site', 'view', 'walk', '', '1914–1915',
  'A six-storey office building put up in 1914 and 1915 to a Chicago-style design by Kansas City architect James C. Sunderland. It is 50 by 132 feet and has a reinforced concrete frame. It was listed on the National Register of Historic Places in 2008.',
  look='A narrow downtown commercial building in the Chicago style. What the front is faced with was not checked.',
  accn='Downtown building; look from the sidewalk. Present use and whether the public may go in were not checked. The pin is the Wikipedia coordinate.',
  links=[W('Inter-State Building')], brick='?', conf='mixed'),

N('pilgrim-lutheran-church-deaf-kansas-city-mo', 'Pilgrim Lutheran Church for the Deaf, 3801 Gillham Road, Kansas City', 'Kansas City', 'kcmo', 'worship', 'standing',
  39.06000, -94.59250, 'site', 'view', 'drive', '', '1941',
  'Frederick Roth Webber designed the church and parsonage, built in 1941. Wikipedia says Pilgrim Chapel was one of fewer than ten churches the Lutheran Church–Missouri Synod built across the country for deaf worshippers. The design gave clear sight lines and good lighting on the minister at the altar, which Wikipedia says suited a deaf congregation. It was listed on the National Register of Historic Places in 2001.',
  look='A Gothic Revival chapel with a parsonage beside it, at 3801 to 3807 Gillham Road. Wikipedia says the chapel held memorial services for people who died of AIDS and their families during the first years of the epidemic. The materials, the interior and whether the congregation still meets were not checked.',
  accn='Look from the public sidewalk. Service times, whether the church is open to visitors and parking were not checked, so it is marked view only. The pin is the Wikipedia coordinate, rounded.',
  links=[W('Pilgrim Lutheran Church for the Deaf of Greater Kansas City and Parsonage')], brick='?', conf='mixed'),

N('knuckleheads-railroad-boarding-house-kansas-city-mo', 'Knuckleheads Saloon (1887 railroad boarding house), East Bottoms, Kansas City', 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.12047, -94.54874, 'site', 'open', 'drive', '', '1887',
  "The saloon grew from a railroad boarding house built in 1887; its present owners bought the building in 1985 and opened the bar in 2001. Wikipedia says the boarding house stood across the street from the first Electric Park, the early amusement park; the venue's own history page says Electric Park was built on the grounds where Knuckleheads stands, so the two accounts disagree. A busy railroad runs close by, and trains passing during shows are part of the place.",
  look="The venue is a group of four stages: a big outdoor stage and courtyard, the saloon, the Gospel Lounge and the Garage, which was a truck and bus repair shop before. Which part is the 1887 building was not stated in a source read. Music runs Wednesday to Sunday, with some Tuesdays, according to Wikipedia.",
  accn="A privately run music venue at 2715 Rochester Avenue in the East Bottoms. Its own site draws its pages by script, so the opening times could not be read; check knuckleheadskc.com or call before going. Parking was not checked.",
  links=[W('Knuckleheads Saloon'), ['Knuckleheads: history', 'https://www.knuckleheadskc.com/history']],
  hours='?', brick='?', conf='mixed'),
]

PIN_NOTES = {
  'title-and-trust-building-kansas-city-mo': "Wikipedia's coordinate for the building; the corner of Walnut and 10th.",
  'kansas-city-southern-railway-building-mo': "Wikipedia's coordinate, which is rounded to a few hundred metres.",
  'police-station-no-4-kansas-city-mo': "Wikipedia's coordinate for the building.",
  'water-department-building-kansas-city-mo': "Wikipedia's coordinate; no address was read.",
  'kessler-apartments-kansas-city-mo': "Wikipedia's coordinate; on the aerial it falls in the Paseo roadway between apartment buildings, so the pin marks the area only.",
  'palace-clothing-building-kansas-city-mo': "Wikipedia's coordinate, rounded.",
  'professional-building-kansas-city-mo': "Wikipedia's coordinate, rounded.",
  'safeway-office-warehouse-kansas-city-mo': "Wikipedia's coordinate for the warehouse near downtown.",
  'stuart-hall-building-kansas-city-mo': "Wikipedia's coordinate for 2121 Central Street.",
  'inter-state-building-kansas-city-mo': "Wikipedia's coordinate for the building.",
  'pilgrim-lutheran-church-deaf-kansas-city-mo': "Wikipedia's coordinate, rounded, for 3801 Gillham Road.",
  'knuckleheads-railroad-boarding-house-kansas-city-mo': "Wikipedia's coordinate; OpenStreetMap puts the bar within 50 metres.",
}
