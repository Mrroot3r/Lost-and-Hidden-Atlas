# November 23, 2026: Lexington, Higginsville and Odessa, Lafayette County, Missouri, about 40 miles east of Kansas City.
# Part of filling in the Kansas City area on purpose for a local researcher. The Atlas had two places within 25 km of Lexington.
# Facts from the linked sources only: Wikipedia read as raw text (tools/wiki_raw.py), Missouri State Parks pages as web
# search results quote them, VisitMO and the Harvey J. Higgins Historical Society listings, and a KSHB news report.
# The National Register forms could not be read: the Missouri State Parks copies answer 404 and NPGallery was not reached.
from data_b import N
from data_ma import W

VMO = ['VisitMO (Missouri tourism): Lexington Historical Museum', 'https://www.visitmo.com/things-to-do/lexington-historical-museum']
LNR = ['Missouri State Parks: Lafayette County National Register listings', 'https://mostateparks.com/basic-page/missouri-national-register-listings/Lafayette']

PLACES = [
N('lafayette-county-courthouse-lexington-mo', 'Lafayette County Courthouse', 'Lexington', 'kcmo', 'civic', 'standing',
  39.18548, -93.88317, 'site', 'public', 'drive', '', '1847–1849',
  'The county planned this Greek Revival courthouse in 1847, on the new Main Street, to replace the one in the old town. The accepted plans set aside $12,000 and the finished cost was $14,382. '
  'Wikipedia calls it the oldest courthouse in continuous use west of the Mississippi River. One of the sources gives the finishing year as 1849, so the completion date is not settled. '
  'A cannonball from the Battle of Lexington in September 1861 is still lodged in a column on the front.',
  look='Look for the cannonball in the upper left column of the front, which has a painted label. The courthouse is a working county office, so only its outside is described here; interior not checked.',
  hook='A cannonball from 1861 is still stuck in a column of a courthouse that is still in use.',
  accn='A county courthouse, owned by Lafayette County, on Main Street in Lexington (the federal public-land map holds only parks, so it shows none here). Park on the street. A third-party listing gives weekday office hours; no page of the county was read, so hours are not given.',
  links=[W('Lafayette County Courthouse (Missouri)'), ['VisitMO: Lafayette County Courthouse', 'https://www.visitmo.com/things-to-do/lafayette-county-courthouse'], LNR],
  conf='mixed', brick='?', hours='?'),

N('lexington-historical-museum-mo', 'Lexington Historical Museum (Cumberland Presbyterian Church)', 'Lexington', 'kcmo', 'worship', 'standing',
  39.18515, -93.87974, 'exact', 'open', 'drive', '', '1846',
  'The Greek Revival building went up in 1846 as the Cumberland Presbyterian Church and was later the town library. A local gardening club helped restore it, and it opened as a museum in 1976. '
  'It stands in the Old Neighborhoods Historic District and was listed on the National Register in 1978.',
  look='A museum of Lexington history; exhibits named by one listing cover the Pony Express, steamboats, the Civil War, coal mining and Wentworth Military Academy, and a memorial to the victims of the 1852 Saluda steamboat disaster is on the grounds. Whether any church fittings survive inside was not checked.',
  accn='Museum at 112 South 13th Street, Lexington. Street parking. VisitMO lists admission as $3 for adults, $1.50 for ages 6 to 18 and free for 6 and under, and says it is not wheelchair accessible. No page of the museum gave days or times, so hours are not given; call ahead.',
  links=[W('Lexington Historical Museum'), VMO, LNR],
  brick='?', hours='?'),

N('wentworth-military-academy-lexington-mo', 'Wentworth Military Academy campus', 'Lexington', 'kcmo', 'inst', 'standing',
  39.18662, -93.87288, 'site', 'view', 'drive', '', 'buildings from 1838; school 1880–2017',
  'Stephen Wentworth founded the military school in 1880, and it grew into one of six military junior colleges in the country. It closed in May 2017 and was sold in 2020 to a Christian arts organisation, Jubilee University. '
  'Wikipedia says the buildings have stood vacant since the closure and have fallen into disrepair. The 1980 National Register district names seven buildings from about 1830 to 1920: Hickman Hall (1907), "D" Company (1884), the Administration Building (1865, with later additions), the Student Union, the Marine Barracks, the Superintendent\'s Residence (1838 and 1848) and the Junior Barracks (1920).',
  look='Look at the campus buildings from the street. Their present condition was not checked; Wikipedia describes them as vacant and decaying. Interior not checked.',
  accn='Private grounds at 1880 Washington Avenue, owned by Jubilee University according to Wikipedia. Look from the public street; the campus is not open to visitors as far as any source read says. One street-side lot lies on North 18th Street.',
  links=[W('Wentworth Military Academy and College'), LNR],
  conf='mixed', brick='?', hours=''),

N('linwood-lawn-lexington-mo', 'Linwood Lawn', 'Lexington', 'kcmo', 'landmark', 'standing',
  39.16523, -93.84745, 'exact', 'view', 'drive', '', '1850–1854',
  'Linwood Lawn is an Italianate brick house built between 1850 and 1854, 71 feet by 110 feet, with a heavy cornice, balustrades, bay windows and columns. A brick octagonal ice house stands on the grounds. It was listed on the National Register in 1973.',
  look='The house and the octagonal ice house are what the Register listing names. An older web listing describes the house as a bed and breakfast; whether it takes guests or visitors now was not checked.',
  accn='Private property reached from Linwood Lawn Road south of Lexington; the lane to the house runs from the county road to the south. No source read says the public may go in, so treat it as view-only unless the owner invites you.',
  links=[W('Linwood Lawn'), LNR],
  conf='mixed', brick='?'),

N('confederate-memorial-chapel-higginsville-mo', 'Confederate Memorial State Historic Site: chapel, cottage and cemetery', 'Higginsville', 'kcmo', 'inst', 'standing',
  39.09826, -93.72910, 'site', 'open', 'drive', 'cemeteries', '1891–1950',
  'From 1891 to 1950 these grounds were a home for old Confederate soldiers. The state took the site over after the last veteran died in 1950. '
  'Three things are on the National Register: a weatherboard chapel of 1892 with a tower and a stained glass window, moved in 1913 and returned in 1978; a small wooden cottage on a brick foundation; and a cemetery of 723 graves with a 1906 monument modelled on the Lion of Lucerne. '
  'The monument was put up by the United Daughters of the Confederacy.',
  look='The chapel, cottage and cemetery stand together; the park also has trails, picnic sites and fishing ponds. Chapel interior beyond the stained glass window was not checked.',
  accn='A Missouri State Park historic site at 211 West 1st Street, Higginsville; free parking by West 1st Street. Missouri State Parks pages, as a web search quoted them, say the grounds are open sunrise to sunset daily and chapel and cemetery tours are by appointment.',
  links=[W('Confederate Memorial State Historic Site'), ['Missouri State Parks: Confederate Memorial hours', 'https://mostateparks.com/hours/811/historic-site/confederate-memorial-state-historic-site']],
  th=[39.09858, -93.72894], thn='Parking by West 1st Street',
  brick='some', hours='Grounds sunrise to sunset daily; chapel and cemetery tours by appointment'),

N('waddell-house-lexington-mo', 'Waddell House (Van Amburg House)', 'Lexington', 'kcmo', 'landmark', 'standing',
  39.18389, -93.87472, 'exact', 'view', 'drive', '', 'about 1840',
  'A two-storey red brick house of about 1840 on a partial basement, with clustered chimney pots, scalloped bargeboards and a Victorian stickwork porch with a mansard roof. '
  'William Bradford Waddell took it in 1869 in trade for stock in the local Baptist Female College. It was listed on the National Register in 1979 and stands in the Old Neighborhoods Historic District.',
  look='Look for the chimney pots and the porch from the street. Interior not checked.',
  accn='Private house in town; look from the public street. Current ownership and use were not checked.',
  links=[W('Waddell House (Lexington, Missouri)'), LNR],
  brick='yes'),

N('hicklin-hearthstone-lexington-mo', 'Hicklin Hearthstone', 'Lexington', 'kcmo', 'landmark', 'standing',
  39.18611, -93.82889, 'site', 'view', 'drive', '', 'about 1838',
  'A two-storey Greek Revival brick house with a pedimented portico, built about 1838 by James Hicklin, one of Lexington\'s earliest settlers. Wikipedia says its group of outbuildings is the most extensive of its kind in Missouri: a store house, carpenter\'s quarters, wash house, servants\' quarters and a large summer kitchen, with an overseer\'s cabin and smokehouse. '
  'Other farm buildings are gone, including the large barn, the root cellar and the slave cabins. A domed limestone mausoleum stands in the fields to the west. A descendant has restored the outbuildings since 2018.',
  look='The house and its brick outbuildings, glimpsed from the road. Interior not checked.',
  accn='A private family property near US 24 east of Lexington. No source read says the public may visit, so treat it as view-only from the road and do not enter the farm.',
  links=[W('Hicklin Hearthstone'), LNR],
  conf='mixed', brick='?'),

N('hicklin-school-lexington-mo', 'Hicklin School', 'Lexington', 'kcmo', 'civic', 'standing',
  39.18472, -93.82472, 'site', 'view', 'drive', '', '1914–1957',
  'A one-room school built in 1914 to a standard plan drawn by J. H. Felt and Company, with a cross-gabled frame building and a two-hole privy. It closed about 1957 and was listed on the National Register in 2004. '
  'The Hicklin family\'s farmhouse is a few hundred yards to the west.',
  look='A small cross-gabled frame schoolhouse and its privy. Condition and interior not checked.',
  accn='Near US 24 east of Lexington; its owner was not found, so look from the road only.',
  links=[W('Hicklin School'), LNR],
  conf='mixed', brick='no'),

N('higginsville-depot-mo', 'Chicago and Alton Railroad depot, Higginsville', 'Higginsville', 'kcmo', 'rail', 'standing',
  39.07352, -93.71678, 'exact', 'open', 'drive', 'stations', '1888–1889',
  'The Chicago and Alton Railroad built this one-and-a-half-storey Stick style frame depot in 1888 to 1889. It has projecting eaves on large brackets and walls faced in vertical boards and battens with horizontal clapboards. It was listed on the National Register in 1987.',
  look='The brackets under the eaves and the mixed board-and-batten and clapboard walls. A listing says the Harvey J. Higgins Historical Society runs a museum in the old depot on South Main Street; what is shown inside was not checked.',
  accn='In town on South Main Street, Higginsville; street parking. Hours were not found on any page of the society, so call ahead.',
  links=[W('Higginsville station'), ['Waymarking: Harvey J. Higgins Historical Society Museum', 'https://waymarking.com/waymarks/WMNQ47_Harvey_J_Higgins_Historical_Society_Museum_Higginsville_MO'], LNR],
  conf='mixed', brick='no', hours='?'),

N('douglass-school-higginsville-mo', 'Douglass School, Higginsville', 'Higginsville', 'kcmo', 'civic', 'standing',
  39.07892, -93.72116, 'exact', 'view', 'drive', '', '1925–1955',
  'This was the school for Black students in Higginsville and Lafayette County for nearly 70 years after the Civil War, until the Brown v. Board of Education decision integrated classrooms and it closed in 1955. '
  'A former student\'s family bought the building in 1990, and former students have since worked to turn it into a museum, the Douglass School Project. It is on the National Register; Wikipedia gives the reference number 100008715 and the state list the date March 10, 2023.',
  look='A two-storey red brick school in the Prairie style, about 65 by 33 feet according to the photograph descriptions on Wikimedia Commons, which quote the Register form; the photographs show weathered, boarded-up windows. The same descriptions say it served grades 1 to 12 from 1925. Interior not checked.',
  accn='Private property at 215 West 16th Street, Higginsville. Look from the street. Whether the museum has opened or has visiting times was not checked.',
  links=[['KSHB: Former students at all-Black school in Higginsville working to preserve history', 'https://www.kshb.com/news/local-news/former-students-at-all-black-school-in-higginsville-working-to-preserve-history'], LNR],
  conf='mixed', brick='yes'),

N('odessa-ice-cream-company-odessa-mo', 'Odessa Ice Cream Company building', 'Odessa', 'kcmo', 'industry', 'standing',
  38.99333, -93.95417, 'area', 'view', 'drive', '', '1929',
  'A two-storey clay block and brick building of 1929 that housed an ice cream factory. The rear was raised to two storeys about 1946. Wikipedia says the company\'s ice cream was the official ice cream of the Missouri State Fair in the 1930s. It was listed on the National Register in 1996.',
  look='The plain brick and clay block street front of a small-town factory. What it is used for now was not checked.',
  accn='In the town of Odessa; look from the public street. Present owner and use not checked.',
  links=[W('Odessa Ice Cream Company Building'), LNR],
  conf='mixed', brick='?'),

N('highland-avenue-historic-district-lexington-mo', 'Highland Avenue Historic District, Lexington', 'Lexington', 'kcmo', 'town', 'standing',
  39.18444, -93.87500, 'area', 'public', 'walk', '', 'about 1830–1930',
  'A residential district of 64 contributing buildings that grew between about 1830 and 1930, with Greek Revival and late Victorian houses. The Register listing names the William H. Russell houses (about 1840 and 1845), the Frick House, Arnold House, Hinesley House, O\'Malley-Kelly House and Old Winkler House, and the 1928 Madonna of the Trail statue. '
  'Sources disagree on which corner the statue stands on: web listings give Highland Avenue and Broadway, Highland and Cliff Drive, or Commerce Street, so its exact spot was not settled.',
  look='Walk the street and look at the 1840s and 1850s houses and the statue. Houses are private.',
  accn='City streets in Lexington, open to anyone (the federal public-land map does not show city streets). Park on the street and look from the sidewalk.',
  links=[W('Highland Avenue Historic District (Lexington, Missouri)'), ['HMdb: Madonna of the Trail, Lexington', 'https://www.hmdb.org/m.asp?m=90919'], LNR],
  conf='mixed', brick='?'),
]

BATCH = {'key': 'kcmo_lex_mhzv', 'label': 'Lexington, Higginsville and Odessa, Missouri', 'added': '2026-11-23 05:41'}

PIN_NOTES = {
 'lafayette-county-courthouse-lexington-mo': 'Pin is the street address lookup for the courthouse block on Main Street. Wikipedia\'s coordinate falls about 250 m east, near 13th Street, where the aerial shows no courthouse.',
 'lexington-historical-museum-mo': 'Pin is the street address 112 South 13th Street (map address lookup); it agrees with the Wikipedia coordinate.',
 'wentworth-military-academy-lexington-mo': 'Pin is the street address 1880 Washington Avenue (map address lookup), in the middle of the campus.',
 'linwood-lawn-lexington-mo': 'Moved about 75 m east of the Wikipedia coordinate onto the red-roofed house seen on the aerial, at the end of a lane from the road.',
 'confederate-memorial-chapel-higginsville-mo': 'Pin is the street address 211 West 1st Street (map address lookup); the chapel, cottage and cemetery are inside the grounds around it.',
 'waddell-house-lexington-mo': 'Pin is the Wikipedia coordinate.',
 'hicklin-hearthstone-lexington-mo': 'Pin is the Wikipedia coordinate; the farm buildings on the aerial lie just north-west of it, so it marks the site.',
 'hicklin-school-lexington-mo': 'Pin is the Wikipedia coordinate; on the aerial it falls on a small road loop with a building just east, so it marks the site.',
 'higginsville-depot-mo': 'Pin is the Wikipedia coordinate.',
 'douglass-school-higginsville-mo': 'Pin is the street address 215 West 16th Street (map address lookup).',
 'odessa-ice-cream-company-odessa-mo': 'Pin is the Wikipedia coordinate; on the aerial it falls on the street, so the exact building was not picked out and the pin marks the area.',
 'highland-avenue-historic-district-lexington-mo': 'Pin is the Wikipedia coordinate for the district, an area mark.',
}
