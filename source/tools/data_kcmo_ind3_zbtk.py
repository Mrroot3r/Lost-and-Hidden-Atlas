# November 24, 2026: a third pass over Independence, Jackson County, Missouri: the National Register houses
# that the two earlier passes left out. Facts from the linked pages only (National Park Service place pages, the Santa Fe Trail
# Historic Sites pages of the University of New Mexico and historical-marker texts on Waymarking). The older National Register forms for the houses are not on line.
from data_b import N
from data_ma import W

NRHP = ['Wikipedia: National Register listings in Jackson County, Missouri', 'https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Jackson_County,_Missouri']
CITY = ['City of Independence: National Register properties', 'https://www.independencemo.gov/government/city-departments/community-development/historic-preservation/designated-historical-resources-architectural-surveys/national-register-properties']

BATCH = {'key': 'kcmo_ind3_zbtk', 'label': 'Independence, Missouri (third pass)', 'added': '2026-11-24 19:57'}

PLACES = [
N('lewis-jones-house-independence-mo', 'Lewis Jones House', 'Independence', 'kcmo', 'landmark', 'standing',
  39.10620, -94.41546, 'exact', 'view', 'drive', '', '1840',
  'A red brick house of 1840 that belonged to Lewis Jones, a wagonmaker, trader and merchant who backed other traders on the Santa Fe Trail and owned the Nebraska House Hotel in Independence. The Jones family left for Colorado in 1857. The house was listed on the National Register in 1994.',
  look='Built as a two-story, three-bay house with red brick walls and wood trim and a porch along one side of the ground floor. It was later enlarged by two bays, which gave it its L shape. Interior not checked.',
  accn='Private house at 104 Elizabeth Street. The Santa Fe Trail Historic Sites page says it is not open for tours: look from the street and watch the parking rules. No hours.',
  links=[['Santa Fe Trail Historic Sites: Lewis Jones House', 'https://historic-trails.unm.edu/sites/lewis-jones-house'], CITY, NRHP],
  brick='yes'),

N('lewis-webb-house-independence-mo', 'Lewis-Webb House', 'Independence', 'kcmo', 'landmark', 'standing',
  39.09991, -94.41845, 'exact', 'view', 'drive', '', '1834',
  'A brick house at 302 West Mill, built in 1834 for John and Susan Lewis, who came to Independence about 1825 and were involved in a saddlery, in financing a trading trip to Santa Fe and in land near the trail. Later it belonged to the poet Mabelle Brown Webb and the writer William Larkin Webb. The National Park Service says it has been altered many times but much of its character remains.',
  look='A two-story L-shaped brick house in the late Greek Revival style, with later additions that the Park Service dates possibly to 1845 and 1853 and Victorian trim added in the 1880s. A Wikimedia Commons photograph shows it painted a pale colour, so the brick is not visible. Interior not checked.',
  accn='Private house; the National Park Service says it is not open to the public. Look from the street. No hours.',
  links=[['National Park Service: Lewis-Webb House', 'https://www.nps.gov/places/lewis-webb-house.htm'], CITY, NRHP],
  brick='no'),

N('owens-mccoy-house-independence-mo', 'Owens-McCoy House', 'Independence', 'kcmo', 'landmark', 'standing',
  39.09615, -94.42032, 'exact', 'view', 'drive', '', '',
  'The home of two Santa Fe Trail businessmen. Samuel Owens ran large caravans on the trail; after he died at the Battle of Sacramento the house was sold in 1851 to John McCoy, who was also a banker, a merchant, an army freighter and a partner in early stagecoach lines, with the first government contract to carry U.S. mail on the trail.',
  look='A red brick two-story house with limestone and wood trim, in a plain Greek Revival style with Italianate touches added later as tastes changed. It was first rectangular and two additions changed its look. The year it was built was not found on the pages read. Interior not checked.',
  accn='Private house on Farmer Avenue at 410 West Farmer. The National Park Service says it is not open to the public: look from the street. No hours.',
  links=[['National Park Service: Owens-McCoy House', 'https://www.nps.gov/places/owens-mccoy-house.htm'], CITY, NRHP],
  conf='mixed', brick='yes'),

N('overfelt-johnston-house-independence-mo', 'Overfelt-Campbell-Johnston House', 'Independence', 'kcmo', 'landmark', 'standing',
  39.08971, -94.42107, 'exact', 'view', 'drive', '', 'about 1850',
  'A Gothic Revival house built about 1850 by John A. Overfelt, a flour miller. Courtney Campbell bought it in 1866 or 1867, and a marker says it passed to his granddaughter, Harriett Campbell Johnston. It is on the National Register (1975). The marker calls it the oldest in a group of houses on the street.',
  look='A red brick house with steep gables and white wooden trim in the Gothic style of its day, seen in a Wikimedia Commons photograph, and a historical marker. Interior not checked.',
  accn='Private house at 305 South Pleasant Street; look from the street. No hours.',
  links=[['Waymarking: Overfelt-Johnston House marker', 'https://www.waymarking.com/waymarks/WMEERP_Overfelt_Johnston_House_Independence_Missouri'], CITY, NRHP],
  conf='mixed', brick='yes'),

N('charles-minor-house-independence-mo', 'Charles Minor House', 'Independence', 'kcmo', 'landmark', 'standing',
  39.09444, -94.42012, 'exact', 'view', 'drive', '', 'about 1885',
  'A late Victorian house built about 1885 on a lot once owned by the pioneer blacksmith Samuel Weston. Charles Lindsay Minor and his wife bought it about 1900, and their daughters Eleanor and Grace lived there for eighty years. Weston\'s great-great-granddaughter restored it in 1982 and 1983, and it joined the National Register in 1984.',
  look='A house with a historical marker on North Spring Street. A painted wooden house with a hipped roof and a porch, seen in a Wikimedia Commons photograph. Interior not checked.',
  accn='Private house at 314 North Spring Street; look from the street. No hours.',
  links=[['Waymarking: Minor House marker', 'https://www.waymarking.com/waymarks/WMBM2Z_Minor_House_Independence_Missouri'], CITY, NRHP],
  brick='no'),

N('hughes-house-independence-mo', 'Mollie and Josephine Hughes House (Hughes-Childers House)', 'Independence', 'kcmo', 'landmark', 'standing',
  39.08389, -94.41489, 'exact', 'view', 'drive', '', '1887',
  'A Queen Anne house of about 1887, designed by the firm Gibbs and Parker for the sisters Mollie and Josie Hughes. Its marker says it shows the architecture that earned Independence the name "Royal Suburb" of Kansas City in the late 1800s. It was bought for restoration in 1966 and is still owned by that family. It joined the National Register in 1994.',
  look='A white-painted wooden Queen Anne house with a round corner tower and a wraparound porch, seen in a Wikimedia Commons photograph. Interior not checked.',
  accn='Private house at 801 South Main Street; look from the street. No hours.',
  links=[['Waymarking: Hughes House marker', 'https://www.waymarking.com/waymarks/WMEEJM_Hughes_House'], CITY, NRHP],
  brick='no'),

N('bryant-house-independence-mo', 'Dr. John S. and Harriet Smart Bryant House', 'Independence', 'kcmo', 'landmark', 'standing',
  39.08709, -94.41554, 'exact', 'view', 'drive', '', '1892',
  'A large Queen Anne-Eastlake house on South Main, begun as a four-room house and, by 1892 according to its marker, enlarged to 21 rooms for Dr. John S. Bryant Jr. and Harriet Smart Bryant. It was split into 11 apartments in the 1950s and the marker says new owners were restoring it as a single home. Listed on the National Register in 1992 and as a local landmark in 1998.',
  look='A large house of red brick with a wide porch and a marker in front, seen in a Wikimedia Commons photograph. Interior not checked.',
  accn='Private house at 519 South Main Street, at Pacific Avenue; look from the street. No hours.',
  links=[['Waymarking: Bryant House marker', 'https://www.waymarking.com/waymarks/WMEEJN_Bryant_House'], CITY, NRHP],
  conf='mixed', brick='yes'),

]

PIN_NOTES = {
'lewis-jones-house-independence-mo': 'Address lookup (104 Elizabeth Street) matched the Wikipedia Register coordinate to within about 30 metres.',
'lewis-webb-house-independence-mo': 'Address lookup (302 West Mill) put the pin on the house, near the Register list coordinate.',
'owens-mccoy-house-independence-mo': 'Address lookup (410 West Farmer Avenue); matched the Wikipedia Register coordinate.',
'overfelt-johnston-house-independence-mo': 'Address lookup (305 South Pleasant Street); matched the Wikipedia Register coordinate.',
'charles-minor-house-independence-mo': 'Address lookup (314 North Spring Street); matched the Wikipedia Register coordinate.',
'hughes-house-independence-mo': 'Address lookup (801 South Main Street); matched the Wikipedia Register coordinate.',
'bryant-house-independence-mo': 'Address lookup (519 South Main Street); matched the Wikipedia Register coordinate.',
}
