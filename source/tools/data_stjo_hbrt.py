# November 26, 2026: St. Joseph, Buchanan County, Missouri, about 48 miles north-west of Kansas City.
# Part of filling in the Kansas City area on purpose for a local researcher. The Atlas had one place in St. Joseph.
# The Midtown and east-side Kansas City listings that were still missing could not be read (see the note), so this
# batch works the St. Joseph National Register listings instead.
# Facts come from the linked sources only: Wikipedia read as raw text (tools/wiki_raw.py), the Allied Arts Council's
# page for the Missouri Theater, and the St. Joseph Museums page. The National Register forms could not be opened.
from data_b import N
from data_ma import W


PLACES = [
N('buchanan-county-courthouse-stjo-mo', 'Buchanan County Courthouse', 'St. Joseph', 'mo', 'civic', 'standing',
  39.76877, -94.85485, 'exact', 'view', 'drive', '', '1873',
  'The county courthouse in St. Joseph was built in 1873. It was first listed on the National Register in 1972 together with the county jail; a boundary change in 1978 took the jail out of the listing.',
  look='A brick courthouse on a cross-shaped plan in the Renaissance Revival style, with pedimented porches on columns of the Corinthian order and a central dome of glass and tin. Interior not checked.',
  accn='A working county building, so look from the street. Parking and public hours were not checked.',
  links=[W('Buchanan County Courthouse (Missouri)')], brick='?'),

N('central-police-station-stjo-mo', 'Central Police Station (National Military Heritage Museum)', 'St. Joseph', 'mo', 'civic', 'standing',
  39.76272, -94.85161, 'exact', 'open', 'drive', '', '1891–1909',
  'St. Joseph\'s central police station stands at 701 Messanie Street. The architects Eckel & Mann designed it and it was built in 1891, with an addition in 1909. It now houses the National Military Heritage Museum and was listed on the National Register in 2009.',
  look='A three-storey brick building on an L plan in the Richardsonian Romanesque style, with limestone trim, a hipped roof and a round corner tower. Interior beyond the museum use not checked.',
  hook='The old police station that became a military museum.',
  accn='Operated as a museum; the museum\'s own page could not be read, so its days and times are not recorded here. Call ahead. Street parking was not checked.',
  hours='?', links=[W('Central Police Station (St. Joseph, Missouri)')], brick='?'),

N('german-american-bank-stjo-mo', 'German-American Bank Building', 'St. Joseph', 'mo', 'civic', 'standing',
  39.76639, -94.85194, 'exact', 'view', 'drive', '', '1889',
  'The bank was founded to serve the many German speakers in the region and put up this six-storey building in 1889. It was renamed the American National Bank in 1918 and later became a savings and loan office. It was listed on the National Register in 1978, and the Historic American Buildings Survey recorded it in 1986.',
  look='A six-storey rectangular brick building in the Richardsonian Romanesque style with Beaux-Arts detail added. A 2014 plan by two health systems called for restoring the natural brick walls and carved columns for offices; whether that was finished was not checked.',
  accn='Downtown street frontage; look from the sidewalk. Present use and parking not checked.',
  links=[W('German-American Bank Building (St. Joseph, Missouri)')], brick='?'),

N('robidoux-row-stjo-mo', 'Robidoux Row', 'St. Joseph', 'mo', 'landmark', 'standing',
  39.77472, -94.85704, 'site', 'open', 'drive', '', 'late 1840s–early 1850s',
  'Joseph Robidoux, the founder of St. Joseph, built this row of apartments in the late 1840s or early 1850s, and at one point lived in it. The Saint Joseph Historical Society restored it and runs it as a local history museum. It was added to the National Register in 1973.',
  look='A brick row of apartments with an attached one-storey brick building, at 219–225 East Poulin Street. The museum inside tells the town\'s early history; what survives of the original interiors was not checked.',
  hook='The founder\'s own apartment row, now the town\'s history museum.',
  accn='Run by the Saint Joseph Historical Society. Listings disagree on its days and times (one says Tuesday to Friday, another Tuesday to Saturday afternoons) and one source says it closes in winter, so the hours are not recorded: call ahead.',
  hours='?', links=[W('Robidoux Row')], brick='?'),

N('missouri-theater-stjo-mo', 'Missouri Theater', 'St. Joseph', 'mo', 'civic', 'standing',
  39.76611, -94.85056, 'exact', 'open', 'drive', '', '1927',
  'The Boller Brothers of Kansas City designed the Missouri Theater as a film palace, finished in July 1927, with sculpture by Waylande Gregory. It was built for the local lawyer and promoter Joseph Goldman. It worked as a cinema for decades and was placed on the National Register in 1979. The City of St. Joseph owns it today and rents it to arts groups.',
  look='An "atmospheric" theater, with Art Deco and Moorish detail, whose auditorium was made to look like a tented courtyard with Assyrian and Persian ornament. It has one balcony, dressing rooms, a fly loft, an orchestra pit and a Wurlitzer organ. The 1960s canopy has been removed and the marquee restored.',
  hook='A cinema built to feel like an open-air courtyard in Persia.',
  accn='Owned by the City of St. Joseph; open for shows, and guided tours by appointment through Friends of the Missouri Theatre (816-271-4717; $5 adults, children 12 and under free, per the Allied Arts Council page). Show times are on the Arts Calendar.',
  hours='Guided tours by appointment (816-271-4717); otherwise open for performances',
  links=[W('Missouri Theater (St. Joseph, Missouri)'), ['Allied Arts Council: Missouri Theater', 'https://stjoearts.org/our-partners/missouri-theater.html']], brick='?'),

N('wyeth-flats-stjo-mo', 'Wyeth Flats (San Regis Apartments)', 'St. Joseph', 'mo', 'landmark', 'standing',
  39.76926, -94.84714, 'site', 'view', 'drive', '', '1888',
  'Wyeth Flats was built in 1888 as a row of multi-storey townhouses and became an apartment building in the 1940s. It is also known as the San Regis Apartments and was listed on the National Register in 1985.',
  look='A large four-storey brick building. Interior not checked.',
  accn='Apartments; look from the street. Parking not checked.',
  links=[W('Wyeth Flats')], brick='?'),

N('maple-grove-davis-house-stjo-mo', 'Maple Grove (Joseph Davis House)', 'St. Joseph', 'mo', 'landmark', 'standing',
  39.78472, -94.84611, 'exact', 'view', 'drive', '', '1847',
  'Maple Grove, also called the Joseph Davis House, was built in 1847. It was listed on the National Register in 1974.',
  look='A two-storey, five-bay brick house on an L plan in a Classical style, with a one-storey wing and a small entrance portico. Interior not checked.',
  accn='A house; its present use and ownership were not checked, so look from the public street.',
  links=[W('Maple Grove (St. Joseph, Missouri)')], brick='?'),

N('richardson-dry-goods-stjo-mo', 'John D. Richardson Dry Goods Company (American Electric Company)', 'St. Joseph', 'mo', 'civic', 'standing',
  39.76861, -94.85694, 'exact', 'view', 'drive', '', '1892',
  'The architect Edmond Jacques Eckel designed this seven-storey wholesale building in 1892 for the Richardson dry goods firm. It later housed the American Electric Company. It was listed on the National Register in 1982 and stands in the Central–North Commercial Historic District.',
  look='A seven-storey brick and stone building, 196 by 136 feet, in the Richardsonian Romanesque style, with terra-cotta facing on the Jules and Third Street fronts carved with Renaissance-style motifs.',
  accn='Downtown street frontage; look from the sidewalk. Present use and parking not checked.',
  links=[W('John D. Richardson Dry Goods Company')], brick='?'),

N('city-hose-company-9-stjo-mo', 'City Hose Company No. 9 (Fire Station No. 9)', 'St. Joseph', 'mo', 'civic', 'standing',
  39.77556, -94.83333, 'area', 'view', 'drive', '', '1901',
  'Edmond Jacques Eckel designed this fire station and it was built in 1901. It was listed on the National Register in 1985.',
  look='A picturesque two-storey brick station with a decorative oriel window. Whether it is still a fire station was not checked.',
  accn='Look from the street. Present use and parking not checked.',
  links=[W('City Hose Company No. 9')], brick='?'),

N('sachau-saloon-stjo-mo', 'Christian Sachau Saloon (American-Gertsch Glass)', 'St. Joseph', 'mo', 'civic', 'standing',
  39.77250, -94.84056, 'area', 'view', 'drive', '', '1889',
  'A saloon built in 1889 for Christian Sachau, later the home of a glass company. It was listed on the National Register in 1985.',
  look='A two-storey brick building with elaborate cast-metal ornament on its main front and a central doorway under a round arch.',
  accn='Look from the street. Present use and parking not checked.',
  links=[W('Christian Sachau Saloon')], brick='?'),

N('everett-school-stjo-mo', 'Everett School (St. Joseph Christian School)', 'St. Joseph', 'mo', 'civic', 'standing',
  39.75944, -94.84361, 'exact', 'view', 'drive', '', '1909',
  'Everett School was built in 1909 and later became St. Joseph Christian School. The gymnasium and power plant on the property are listed with it. It was added to the National Register in 2005.',
  look='A two-storey brick school on an E-shaped plan in the Colonial Revival style, set on a raised basement, with a crenellated parapet and a central bay topped by a large metal arch with a prominent keystone.',
  accn='A school; look from the street. Parking not checked.',
  links=[W('Everett School (St. Joseph, Missouri)')], brick='?'),

N('patee-house-stjo-mo', 'Patee House (Patee House Museum)', 'St. Joseph', 'mo', 'hotel', 'standing',
  39.75595, -94.84492, 'exact', 'open', 'drive', '', '1858',
  'John Patee built this 140-room hotel, finished in 1858, at the Hannibal and St. Joseph Railroad station. Its offices held the headquarters of the Pony Express, which began in 1860. In the Civil War the Union army\'s provost marshal worked here and held trials in the second-floor ballroom. Female colleges used the building from 1865 to 1868 and from 1875 to 1880. It has been a museum since 1963 and is a National Historic Landmark.',
  look='A large 1858 hotel building turned into a museum of United States history with an emphasis on transport. It marks the eastern end of the Pony Express National Historic Trail.',
  hook='The luxury hotel that was the Pony Express headquarters.',
  accn='Owned and run by the Pony Express Historical Association, a non-profit. Its days and times were not found on its own page, and listings disagree (a winter weekends-only schedule is quoted by some): call ahead (816-232-8206 is listed).',
  hours='?', links=[W('Patee House')], brick='yes'),

N('jesse-james-home-stjo-mo', 'Jesse James Home Museum', 'St. Joseph', 'mo', 'landmark', 'standing',
  39.75550, -94.84514, 'exact', 'open', 'drive', '', 'moved in 1939 and 1977',
  'The one-storey frame house is where Jesse James was living and was shot by Robert Ford on April 3, 1882. It stood at 1318 Lafayette Street, was moved to the Belt Highway in 1939 and in 1977 to the grounds behind Patee House, two blocks from where it began. A 1995 autopsy found the fatal bullet entered behind his right ear, so the bullet hole in the north wall is not from that shot. It was listed on the National Register in 1980.',
  look='A small Greek Revival frame house, about 24 by 30 feet, with a bullet hole in the north wall inside. The museum shows items from the 1995 exhumation, such as coffin handles and a pin he wore in his death photograph.',
  accn='Owned and run by the Pony Express Historical Association, on the Patee House grounds at 12th and Mitchell. Days and times were not found on its own page: call ahead.',
  hours='?', links=[W('Jesse James Home Museum')], brick='no'),

N('buchanan-county-infirmary-stjo-mo', 'Buchanan County Infirmary (Poor Farm, Green Acres)', 'St. Joseph', 'mo', 'inst', 'standing',
  39.81737, -94.81153, 'site', 'view', 'drive', '', '1919',
  'The county built this infirmary in 1919. It is the last surviving building of the Buchanan County Poor Farm, and was listed on the National Register in 2009.',
  look='A two-storey, F-shaped Classical Revival building with a fireproof concrete frame, brick walls and a hipped roof of red ceramic tile. A central porch has four full-height concrete columns of the Doric order under a pediment.',
  accn='Present owner and use not checked; look from the public road.',
  links=[W('Buchanan County Infirmary')], brick='?'),

N('thompson-brown-sandusky-house-stjo-mo', 'Thompson-Brown-Sandusky House (Jess Marriott House)', 'St. Joseph', 'mo', 'landmark', 'standing',
  39.70917, -94.86000, 'exact', 'view', 'drive', '', 'about 1850',
  'A house built about 1850, also called the Jess Marriott House. It was listed on the National Register in 1983.',
  look='A brick house in the Federal style with one-storey wings either side and a front porch on Doric columns.',
  accn='Present owner and use not checked; look from the public street.',
  links=[W('Thompson-Brown-Sandusky House')], brick='?'),

N('ryan-block-stjo-mo', 'Ryan Block', 'St. Joseph', 'mo', 'civic', 'standing',
  39.77002, -94.84528, 'exact', 'view', 'drive', '', '1889',
  'The Ryan Block is a three-unit commercial row built in 1889 and listed on the National Register in 2012.',
  look='A three-storey, trapezoid-shaped Italianate brick building of three units sharing walls, with cast-iron storefronts, a metal cornice with small tooth-like blocks and a two-storey oriel window covered in decorative metal.',
  accn='Downtown street frontage; look from the sidewalk. Present use and parking not checked.',
  links=[W('Ryan Block (St. Joseph, Missouri)')], brick='?'),

N('miller-porter-lacy-house-stjo-mo', 'Miller-Porter-Lacy House (Lacy House)', 'St. Joseph', 'mo', 'landmark', 'standing',
  39.77611, -94.82056, 'exact', 'view', 'drive', '', '1883; remodelled 1902',
  'An Italianate brick farmhouse of 1883 that Edmond Jacques Eckel enlarged and remodelled in 1902 in a Colonial and Georgian Revival style. It was listed on the National Register in 1982.',
  look='A large brick house with a low hipped roof, porches on columns of the Tuscan order and a porte cochere. A carriage house and the sites of croquet and tennis courts are also listed.',
  accn='Present owner and use not checked; look from the public street.',
  links=[W('Miller-Porter-Lacy House')], brick='?'),

N('lawler-motor-company-stjo-mo', 'Lawler Motor Company Building (Farmer Automobile Company)', 'St. Joseph', 'mo', 'landmark', 'standing',
  39.77222, -94.84444, 'exact', 'view', 'drive', '', '1913',
  'A car showroom and garage built in 1913, with an apartment upstairs. A Ford dealership ran from it from 1917 to 1928. It is on the National Register.',
  look='A small two-storey brick commercial building on a trapezoid plan, built as a showroom and service garage.',
  accn='Present use not checked; look from the street.',
  links=[W('Lawler Motor Company Building')], brick='?'),
]

BATCH = {'key': 'stjo_hbrt', 'label': 'St. Joseph, Missouri', 'added': '2026-11-26 08:51'}

PIN_NOTES = {
'buchanan-county-courthouse-stjo-mo': 'Wikipedia\'s coordinate fell about 100 m south-west on a modern building; moved onto the domed cross-plan courthouse seen on the aerial.',
'central-police-station-stjo-mo': 'Wikipedia coordinates for 701 Messanie; the pin sits on a corner building with a round tower on the aerial.',
'german-american-bank-stjo-mo': 'Wikipedia coordinates; the pin sits on a building of the right size on the aerial.',
'robidoux-row-stjo-mo': 'Wikipedia\'s point fell on the road; OpenStreetMap places the museum at 225 East Poulin Street, on a building the aerial shows east of the road. The pin marks the site.',
'missouri-theater-stjo-mo': 'Wikipedia coordinates; the pin sits on a building of the right size on the aerial.',
'wyeth-flats-stjo-mo': 'Wikipedia\'s point fell on a street junction; moved about 40 m west to the large dark-roofed building with rows of windows. The pin marks the site.',
'maple-grove-davis-house-stjo-mo': 'Wikipedia coordinates; the pin sits on a building of the right size on the aerial.',
'richardson-dry-goods-stjo-mo': 'Wikipedia coordinates; the pin sits on a building of the right size on the aerial.',
'city-hose-company-9-stjo-mo': 'Wikipedia\'s point fell on a street and the aerial did not settle which building is the station, so this marks the area only.',
'sachau-saloon-stjo-mo': 'Wikipedia\'s point fell on a street and the aerial did not settle which building is the saloon, so this marks the area only.',
'everett-school-stjo-mo': 'Wikipedia coordinates; the pin sits on a building of the right size on the aerial.',
'patee-house-stjo-mo': 'Wikipedia coordinates; the pin sits on a building of the right size on the aerial.',
'jesse-james-home-stjo-mo': 'Wikipedia coordinates, behind Patee House; the pin sits on a building of the right size on the aerial.',
'buchanan-county-infirmary-stjo-mo': 'Wikipedia\'s point fell in a car park. OpenStreetMap places Green Acres Rest Home about 200 m south, where the aerial shows a red-tile roof; the pin marks that site.',
'thompson-brown-sandusky-house-stjo-mo': 'Wikipedia coordinates; the pin sits on a building of the right size on the aerial.',
'ryan-block-stjo-mo': 'Wikipedia coordinates; the pin sits on a building of the right size on the aerial.',
'miller-porter-lacy-house-stjo-mo': 'Wikipedia coordinates; the pin sits on a building of the right size on the aerial.',
'lawler-motor-company-stjo-mo': 'Wikipedia coordinates; the pin sits on a building of the right size on the aerial.',
}
