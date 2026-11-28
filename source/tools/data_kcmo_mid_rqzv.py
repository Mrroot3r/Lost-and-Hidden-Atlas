# November 25, 2026: ten more places in Kansas City, Missouri: the West Bottoms, downtown, the east side and Midtown.
# Part of filling in the Kansas City area on purpose for a local researcher. The Atlas had none of these.
# Facts come from National Register registration forms that the Park Service's online copy gives as text (read with
# tools/page.py) and, for Quality Hill, a Wikipedia article read as raw text. Most older Register forms in Kansas City
# are only a placeholder page online, so only the forms that could be read were used. Where a form gives the use of a
# building, that use is the one when the form was written (2013 to 2019) and is said so. Pins are street addresses on
# the Esri geocoder, then looked at on the aerial.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_mid_rqzv', 'label': 'Kansas City: West Bottoms, downtown, east side and Midtown', 'added': '2026-11-25 22:01'}

NPS = 'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/%s_text'
STREET = 'Private building; look at it from the public street. Parking was not checked. '

PLACES = [
N('crane-company-building-west-bottoms-kc', 'Crane Company Building (Jacobs Warehouse), West Bottoms', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.10137, -94.60106, 'site', 'view', 'drive', '', '1904–1905',
  'A six-storey warehouse at 1105-1107 Hickory Street, designed by the Kansas City architect Louis S. Curtiss and built in 1904 and 1905 for the Crane Company, a supplier of pipes, pumps, valves and fittings. It stood behind the firm\'s five-storey Romanesque branch office at Hickory and 12th Street, which burned down in 2005. '
  'The Register form says the warehouse kept the Crane Company\'s stock until 1951, and that it was later sold to the Jacobs Warehouse Company.',
  look='Tall brick piers with stone capitals and bases mark the first two storeys of the west front, which faces Hickory Street. Inside, the frame is steel columns and beams with heavy timber floors, and most floors are still open warehouse space, according to the form. When the form was written (2018) it was used for warehouse storage; interior not checked.',
  accn=STREET + 'The West Bottoms is flat industrial ground below the bluff; the building is on the west side of Hickory Street.',
  links=[['National Register registration form, The Crane Company Building (2018)', NPS % '100002424']],
  brick='?'),

N('murdock-manufacturing-building-west-bottoms-kc', 'C. A. Murdock Manufacturing Company Building, West Bottoms', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.10221, -94.59946, 'site', 'view', 'drive', '', '1887',
  'A five-storey Romanesque Revival warehouse at 1225-1227 Union Avenue, two blocks from the Union Depot, built in September 1887. Charles A. Murdock made and sold his own brand of coffee, tea and spices here and shipped them by rail from the loading dock at the back, which is still there. '
  'The design is attributed to the Kansas City architect Frederick B. Hamilton. Murdock moved his business out in April 1918, to a larger building at 1219 West 10th Street in the same district.',
  look='A heavy timber building with thick brick piers rising to an arcade of arches on the fourth floor, a deeply recessed polygonal entrance and large wood-framed shop windows (protected by wood panels when the form was written, in 2016). The rail loading dock survives behind. Interior not checked.',
  accn=STREET + 'The building is on Union Avenue in the West Bottoms. The Register form lists it as a manufacturing facility and a specialty business in 2016.',
  links=[['National Register registration form, C. A. Murdock Manufacturing Company Building (2016)', NPS % '16000234']],
  brick='?'),

N('west-bottoms-north-historic-district-kc', 'West Bottoms – North Historic District', 'Kansas City', 'kcmo', 'town', 'standing',
  39.1050, -94.6010, 'area', 'view', 'drive', '', 'c. 1880–1970',
  'The northern part of the West Bottoms, the flat ground west of downtown where Kansas City\'s railroad freight, wholesale houses and factories gathered after the Hannibal Bridge opened in 1869 and the Union Depot in 1878. The 2016 Register form counts 29 contributing buildings between West 9th Street, Wyoming Avenue, Union Avenue and the Kansas City Southern rail line. '
  'It describes warehouses, factories and distribution buildings from about 1880 to 1970, some of them red or orange brick and up to seven storeys.',
  look='Blocks of multi-storey brick warehouses beside active rail lines. The Murdock and Crane warehouses, which have their own places on this map, are close to its southern edge. Most buildings are private and used for storage, shops, studios or event space; the district is for walking and looking, not for going in.',
  accn='Streets and sidewalks are public; the buildings are private. This is an industrial district with active railroad tracks and truck traffic: stay out of the rail yards. Parking was not checked.',
  links=[['National Register registration form, West Bottoms – North Historic District (2016)', NPS % '16000771']],
  brick='some'),

N('kansas-city-star-building-1729-grand-kc', 'Kansas City Star Building (1911), 1729 Grand Boulevard', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.09254, -94.58069, 'site', 'view', 'drive', '', '1911–1924',
  'The Chicago architect Jarvis Hunt designed this four-storey building in 1909 and 1910 as the offices and printing plant of The Kansas City Star, and it was finished in 1911. In 1924 Hunt added a northern wing that nearly doubled its size. The Register form calls its Italian Villa style (asymmetrical, with a tower, wide eaves and round arches) rare for a commercial building in Kansas City. '
  'The office wing and the printing wing are joined by a narrow link, and the whole block between 17th and 18th Streets is the site.',
  look='Patterned "tapestry" brick, marble ornament, deep bracketed eaves and big round-arched entrances. The towers drawn in 1924 were taken down during the Second World War, and only their cast-iron bases are left on the roof. The form lists the use in 2019 as a communications facility with work in progress; present use and interior not checked.',
  accn=STREET + 'Grand Boulevard, south of the downtown business district.',
  links=[['National Register registration form, Kansas City Star Building (2019)', NPS % '100004102']],
  brick='?'),

N('hoover-brothers-building-oak-street-kc', 'Hoover Brothers Building, 922 Oak Street', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.10261, -94.57875, 'exact', 'view', 'drive', '', '1914–1923',
  'The Kansas City firm of Saylor and Seddon designed this commercial building in 1914 as a warehouse and showroom for Hoover Brothers, a school-supply dealer, and a third storey was added in 1923. It is reinforced concrete, and red brick with terra cotta trim faces the street. '
  'It stands between two other Register buildings, the Stine and McClure Undertaking Company Building next door and the Pickwick complex, a block west of the Kansas City Hall district.',
  look='A storefront of large windows on the ground floor, with the richest terra cotta on the second floor. The form notes later changes but says the building keeps most of its original character. When the form was written (2019) part of it was a specialty store and the rest a vacant warehouse; interior not checked.',
  accn=STREET + 'Oak Street, downtown, beside a park on its east side.',
  links=[['National Register registration form, Hoover Brothers Building (2019)', NPS % '100004600']],
  brick='yes'),

N('campbell-continental-baking-building-kc', 'Campbell-Continental Baking Company Building, 30th and Troost', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.07273, -94.57055, 'site', 'view', 'drive', '', '1915–1925',
  'A bread bakery on the northeast corner of Troost Avenue and East 30th Street, begun in 1915 and enlarged in 1922, 1924 and 1925, with later additions in 1975 and about 1993. It made bread for the Campbell Baking Company and then for Continental Baking, until it closed in 1997. '
  'The Register form says it is an excellent example of an early bread factory built to meet new rules and public concern about clean baking.',
  look='Two storeys of buff brick with terra cotta trim in a plain Italian Renaissance Revival style: round-arched openings, keystones, quoins and a corbelled cornice. The form says the oven niches and platforms, mixing room, freight elevator and workers\' locker rooms survive inside. When the form was written (2016) the building was vacant; present use not checked.',
  accn=STREET + 'Troost Avenue at East 30th Street.',
  links=[['National Register registration form, Campbell-Continental Baking Company Building (2016)', NPS % '16000235']],
  brick='no'),

N('st-regis-hotel-linwood-kc', 'St. Regis Hotel (apartment hotel), Linwood and The Paseo', 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.06895, -94.56657, 'exact', 'view', 'drive', '', '1914',
  'A nine-storey apartment hotel at the corner of Linwood Boulevard and The Paseo, designed by the Kansas City firm of Owen and Payson in the Italian Renaissance Revival style and built in 1914. On its narrow lot the builders used a reinforced concrete frame, still an early choice, to go high. '
  'The Register form ties it to the city\'s parks and boulevards system, which pushed up land values along the boulevards and brought apartment hotels like this one.',
  look='Red brick with terra cotta details, a modillion cornice and, on the ninth floor, a colonnaded pergola between two hipped towers. The west front on The Paseo is as important as the south front. Present use and interior not checked.',
  accn=STREET + 'Linwood Boulevard at The Paseo; the Register form gives the address as 1400-1402 East Linwood.',
  links=[['National Register registration form, St. Regis Hotel (2013)', NPS % '13000885']],
  brick='yes'),

N('westport-junior-high-school-kc', 'Westport Junior High School (Westport Middle School), 300 East 39th Street', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.05681, -94.58229, 'exact', 'view', 'drive', '', '1924',
  'A big five-storey school on a hill above Gillham Park and the Hyde Park neighbourhood, built in 1924 to the design of Charles Smith, architect for the Kansas City school district. The Register form calls it an excellent example of the junior high school building of its day: fireproof, with wide corridors, large windows and rooms for art, music, science and manual training, two gymnasiums and a swimming pool. '
  'A modern building from 1992 is joined to it by a glazed walkway.',
  look='Red brick walls with limestone and terra cotta ornament that mixes Jacobethan strapwork, Italian arcaded windows and Beaux-Arts festoons and shields. Inside, the form lists plasterwork at the entrance and auditorium, marble floors on the first floor, built-in lockers and a three-storey auditorium. The form gives the use as education in 2014; present use not checked.',
  accn=STREET + 'East 39th Street, three blocks east of 39th and Main.',
  links=[['National Register registration form, Westport Junior High School (2014)', NPS % '14000162']],
  brick='yes',apart='westport-high-school-kc: the 1908 high school across East 39th Street; this is the 1924 junior high'),

N('agee-apartments-historic-district-linwood-kc', 'Agee Apartments Historic District, 3200-3218 Linwood Boulevard', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.06817, -94.54587, 'site', 'view', 'drive', '', '1925',
  'Four nearly identical three-storey brick apartment buildings with columned porches along Linwood Boulevard, built in 1925 for the Agee Realty Company. The architect was Nelle E. Peters. A building permit of April 1925 gave $140,000 for them, and together they held 52 apartments, 13 in each building. '
  'The Register form places them among the "colonnade apartments", a type common on Kansas City\'s boulevards.',
  look='Square brick porch columns, barrel clay-tile pent roofs, small peaked parapets and terra cotta trim, a mix of Spanish, Classical and other revival details. The buildings were still apartments when the form was written (2018). Private homes: look from the street only.',
  accn='Private apartment buildings; look at them from the public sidewalk on Linwood Boulevard. Parking was not checked.',
  links=[['National Register registration form, Agee Apartments Historic District (2018)', NPS % '100001347']],
  brick='yes'),

N('quality-hill-historic-district-kc', 'Quality Hill historic district, Kansas City', 'Kansas City', 'kcmo', 'town', 'standing',
  39.10491, -94.59209, 'area', 'public', 'walk', '', '1820s',
  'A neighbourhood on a 200-foot bluff over the West Bottoms, west of downtown, and the oldest part of the Kansas City area to have been lived in without a break. Its first recorded church dates to 1822. In the later 1800s the city\'s leaders built large houses on its limestone bluffs, and the district was listed on the National Register in 1978. '
  'It fell into disrepair in the 1900s and has been rebuilt and refurbished since the 1980s, so old and new buildings stand together.',
  look='Walk the streets between Broadway, 7th and 14th Streets to see the gold-domed Cathedral of the Immaculate Conception, the oldest standing building on the hill (it has its own place on this map), Grace and Holy Trinity Cathedral, begun in the 1860s, and 19th-century houses. Wikipedia says several buildings here date to before the Civil War. Case Park on the bluff has a statue of Jim Pendergast.',
  accn='Public streets and sidewalks; most buildings are private, and the cathedrals have their own hours. The pin is on Case Park, a city park on the edge of the bluff (Wikipedia says the city built it in the Pendergast years); its hours and parking were not checked.',
  links=[['Wikipedia: Quality Hill, Kansas City', 'https://en.wikipedia.org/wiki/Quality_Hill%2C_Kansas_City']],
  brick='?'),
]

PIN_NOTES = {
 'crane-company-building-west-bottoms-kc': 'Street address 1105 Hickory Street on the Esri geocoder; it agrees with the Register list point. Checked on the aerial.',
 'murdock-manufacturing-building-west-bottoms-kc': 'Street address 1225 Union Avenue on the Esri geocoder; the Register list point is about 30 metres away. Checked on the aerial.',
 'west-bottoms-north-historic-district-kc': 'The middle of the district, placed from the boundary streets the form names. The pin marks the area, not one building.',
 'kansas-city-star-building-1729-grand-kc': 'Street address 1729 Grand Boulevard on the Esri geocoder; the Register list point is about 30 metres away. Checked on the aerial.',
 'hoover-brothers-building-oak-street-kc': 'The form gives 39.102611, -94.578741 for the building; the Esri geocoder for 922 Oak Street agrees. Checked on the aerial.',
 'campbell-continental-baking-building-kc': 'Street address 1108 East 30th Street on the Esri geocoder; the Register list point is within 20 metres. Checked on the aerial.',
 'st-regis-hotel-linwood-kc': 'Street address 1400 East Linwood Boulevard on the Esri geocoder, matching the Register list point. Checked on the aerial.',
 'westport-junior-high-school-kc': 'Street address 300 East 39th Street on the Esri geocoder; the Register list point is within 15 metres. Checked on the aerial.',
 'agee-apartments-historic-district-linwood-kc': 'Street address 3200 Linwood Boulevard on the Esri geocoder, matching the Register list point. The four buildings run east along the street.',
 'quality-hill-historic-district-kc': 'Taken from Wikipedia\'s coordinates for the neighbourhood. On the aerial it falls on Case Park, the round plaza on the bluff edge, so the pin marks the area and not one building.',
}
