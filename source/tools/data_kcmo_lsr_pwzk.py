# November 23, 2026: south Kansas City, Raytown, Lee's Summit, Raymore, Belton, Pleasant Hill and Harrisonville, Missouri.
# Part of filling in the Kansas City area on purpose for a local researcher. Facts come from the linked sources only:
# Wikipedia read as raw text (tools/wiki_raw.py), the National Park Service pages for the Raytown museum and New Santa Fe
# cemetery, the Great American Stations page for the Lee's Summit depot, the VisitMO page for the Lee's Summit museum, and
# Clio's entry for the Belton society. Hours the operators' own pages give were taken as web search results quote them.
# The National Register forms for these places could not be read. Nothing was checked on the ground.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_lsr_pwzk', 'label': 'Kansas City: south, Lee\'s Summit and Cass County', 'added': '2026-11-23 14:55'}

PLACES = [
N('new-santa-fe-cemetery-ruts-kc-mo', 'New Santa Fe Cemetery trail ruts', 'Kansas City', 'kcmo', 'landmark', 'traces',
  38.9065, -94.6064, 'site', 'public', 'drive', '', '1840s–1860',
  'New Santa Fe stood at the western edge of Missouri on the Santa Fe Trail, a place to outfit and load for the journey west. When emigrant traffic grew in the 1840s the Oregon and California trails shared this road. '
  'Dabney Lipscomb platted the town in 1851, and the border conflict of 1860 disrupted traffic and led to its decline. The cemetery was made a burial ground in 1880, after trail traffic had faded, and its plots were spaced to leave the ruts alone. '
  'As Kansas City grew the town was taken down and replaced by houses.',
  look='Wagon ruts that show as shallow dips in the grass between rows of weathered late-1800s gravestones, with an iron "New Santa Fe" sign at the gate, a historical marker and an information panel. The cemetery sits inside a neighborhood built in the 1980s.',
  accn='Managed by the Historical Society of New Santa Fe, 122nd Street and State Line Road, according to the National Park Service. It is a certified site on the national trails. A photograph taken at the pin shows the cemetery gate and its marker. Hours and where to park were not found: look for the iron sign at the gate, use the public streets and keep to the paths between graves.',
  links=[['National Park Service: New Santa Fe Cemetery Trail Ruts', 'https://nps.gov/places/new-santa-fe-cemetery-trail-ruts.htm'], W('Santa Fe Trail')],
  conf='mixed', brick='no', hours=''),

N('raytown-historical-society-museum-mo', 'Raytown Historical Society Museum', 'Raytown', 'kcmo', 'civic', 'standing',
  39.00841, -94.46685, 'exact', 'open', 'drive', '', '1945',
  'The museum stands on the old Santa Fe Trail route, in the town that grew from blacksmith William Ray\'s shop in 1849. '
  'The National Park Service says it tells the story of overland travel with a re-created general store and blacksmith shop and original artifacts. '
  'Search results quoting the society\'s page say the building began as Raytown\'s first fire station, built in 1945, and that the society bought it in 1982.',
  look='A small museum building with a re-created general store and blacksmith shop inside. What survives of the 1945 fire station fabric was not checked.',
  accn='Run by the Raytown Historical Society, 9705 East 63rd Street. A certified site on the national trails (National Park Service). Hours as the society\'s own page was quoted in search results: Thursday and Friday 10 a.m. to 2 p.m., other times by appointment; the page itself was not opened, so call 816-353-5033 before going.',
  links=[['National Park Service: Raytown Historical Society Museum', 'https://www.nps.gov/places/raytown-historical-society-museum.htm'], ['Raytown Historical Society', 'https://raytownhistoricalsociety.org/']],
  conf='mixed', brick='?', hours='Thursday and Friday 10 a.m. to 2 p.m.; other times by appointment (from a search result)'),

N('lees-summit-history-museum-mo', 'Lee\'s Summit History Museum (1939 post office)', 'Lee\'s Summit', 'kcmo', 'civic', 'standing',
  38.91284, -94.37874, 'exact', 'open', 'drive', '', '1939',
  'The Historical Society of Lee\'s Summit keeps its museum in a 1939 post office built under the New Deal, in the town\'s old downtown. '
  'VisitMO says exhibits tell the story of the town, first called Big Cedar, and show a recreated Vogue Theatre. '
  'A search result says the museum began in 1991 in the south end of the 1905 train depot and moved here in April 2015.',
  look='A one-storey public building with exhibits, maps, photographs and artifacts, and a recreated movie theatre. A search result says the post office mural "Pastoral" by Ted Gilien (1940) is still in the building, in the mayor\'s office; this was not checked. A National Register listing named Lee\'s Summit Post Office (2018) gives an address on Southwest Market Street, so it may be a different building: not settled.',
  accn='Historical Society of Lee\'s Summit, 220 SW Main Street, one block from Amtrak and the old depot. Hours: VisitMO gives Thursday and Friday 10 a.m. to 2 p.m. and Saturday 10 a.m. to 4 p.m.; a search result quoting the museum\'s own page gives shorter winter hours (January to March). Admission was quoted as $5 for adults and free for children 12 and under. Call 816-287-4477.',
  links=[['VisitMO: Lee\'s Summit History Museum', 'https://www.visitmo.com/things-to-do/lees-summit-history-museum'], ['Lee\'s Summit History Museum', 'https://leessummitmuseum.com/']],
  conf='mixed', brick='?', hours='April to December: Thursday and Friday 10 a.m. to 2 p.m., Saturday 10 a.m. to 4 p.m.; January to March shorter (from search results)'),

N('lees-summit-mopac-depot-mo', 'Lee\'s Summit Missouri Pacific depot (1905)', 'Lee\'s Summit', 'kcmo', 'rail', 'standing',
  38.91271, -94.37816, 'exact', 'view', 'drive', '', '1905',
  'Lee\'s Summit began with a boxcar for a depot, which a wooden building replaced; that burned in 1903. The brick depot that stands today on the east side of the tracks was finished in 1905. '
  'The Great American Stations page says it is now used by the chamber of commerce and the historical society, though the society\'s museum has since moved to the old post office.',
  look='A one-storey depot about 150 feet long, with dark red brick walls rising from a stone base, a band of pressed brick between the lintels and a hipped-gabled roof with deep eaves. A three-sided bay juts out on the trackside. A red caboose with the Missouri Pacific buzz-saw sign stands beside it. Interior not checked.',
  accn='Beside William B. Howard Station Park and the Amtrak Missouri River Runner station, 217 SW Main Street. Look from the park and platform; the building\'s use and hours were not confirmed.',
  links=[['Great American Stations: Lee\'s Summit, MO', 'https://www.greatamericanstations.com/stations/LEE']],
  conf='mixed', brick='yes', hours=''),

N('pleasant-hill-historical-museum-mo', 'Pleasant Hill Historical Society Museum', 'Pleasant Hill', 'kcmo', 'civic', 'standing',
  38.78544, -94.27546, 'exact', 'open', 'drive', '', '',
  'A public museum and research library at 125 Wyoming Street, beside the Pleasant Hill Downtown Historic District. '
  'Wikipedia says it holds about 8,000 indexed photographs going back to the late 1880s, artifacts and genealogical resources, and that its front includes elements of old local buildings. '
  'It is not funded by the city; its main fundraiser is Railroad Days each April.',
  look='A museum with a front that reuses pieces of historic Pleasant Hill buildings, a photograph archive and a research room. Interior not checked.',
  accn='Pleasant Hill Historical Society, 125 Wyoming Street, a short walk from the 1903 Missouri Pacific depot. VisitMO lists free admission. No page that gives opening hours could be read, so hours not checked: call before going.',
  links=[W('Pleasant Hill Historical Society Museum'), W('Pleasant Hill Downtown Historic District')],
  conf='mixed', brick='?', hours='?'),

N('belton-historical-society-museum-mo', 'Belton Historical Society Museum (Old City Hall)', 'Belton', 'kcmo', 'civic', 'standing',
  38.81093, -94.53126, 'site', 'open', 'drive', '', '',
  'The Belton Historical Society runs a small local-history museum in the town\'s Old City Hall building on Main Street. '
  'The building\'s date and what the museum shows were not found in a source that could be read.',
  look='A small museum in a former city hall. Its date, what original fabric remains and its displays were not checked.',
  accn='512 Main Street, Belton. Clio\'s entry gives March to December, Tuesday and Thursday 1 to 4 p.m. and Saturday 10 a.m. to 1 p.m., and phone 816-331-8044; other sources disagree on the days and the society\'s own page was not opened, so hours not checked.',
  links=[['Clio: Belton Historical Society and Museum', 'https://www.theclio.com/entry/10927']],
  conf='mixed', brick='?', hours='?'),

N('belton-historical-railroad-mo', 'Belton Missouri Historical Railroad (Belton, Grandview & Kansas City)', 'Belton', 'kcmo', 'rail', 'standing',
  38.81268, -94.5316, 'site', 'open', 'drive', '', '1964',
  'A heritage railroad and museum run by the Smoky Hill Railway and Historical Society on the old St. Louis and San Francisco (Frisco) line from Kansas City to Springfield. '
  'The society formed in 1964 to take a 1918 Baldwin steam locomotive. A few miles of track join Grandview and Belton, and a 1956 GP9 diesel pulls the excursion train.',
  look='Locomotives, cars and equipment in the society\'s collection and the excursion train. Wikipedia says the track north of 155th Street was sold to Kansas City Southern and the line south of Peculiar is scrapped. Running days and what can be seen between runs were not checked.',
  accn='Run by the Smoky Hill Railway and Historical Society in Belton. The coordinate is Wikipedia\'s; the entrance and parking were not checked and no schedule page was read, so hours not checked.',
  links=[W('Belton, Grandview and Kansas City Railroad')],
  conf='mixed', brick='?', hours='?'),

N('robert-a-brown-house-harrisonville-mo', 'Robert A. Brown House', 'Harrisonville', 'kcmo', 'landmark', 'standing',
  38.68417, -94.38722, 'area', 'view', 'drive', '', 'about 1850',
  'Wikipedia describes a two-storey, five-bay Classic Revival red brick house built about 1850 on a limestone foundation, with a two-storey central wooden portico. '
  'A brick slave house, a smokehouse and an apple house also stand on the property. It was listed on the National Register of Historic Places in 1970.',
  look='The red brick house with its portico and, behind it, the brick outbuildings, seen from the road if at all. Interior not checked.',
  accn='Near Harrisonville, Cass County. Ownership and whether the public can visit were not found: treat it as private and look from the public road only. The pin is Wikipedia\'s coordinate, falls in woods and marks the general area, not the house.',
  links=[W('Robert A. Brown House')],
  conf='mixed', brick='yes', hours=''),

N('obannon-homestead-garden-city-mo', 'O\'Bannon Homestead (Schuyler Stock Farm)', 'Garden City', 'kcmo', 'landmark', 'standing',
  38.57333, -94.15694, 'site', 'view', 'drive', '', '1893',
  'Wikipedia describes a farm complex near Garden City, also known as Schuyler Stock Farm, Steeple House and Four Leaf Clover Farm. The 1893 two-storey frame farmhouse has Queen Anne decoration. '
  'Six outbuildings also count: a wash house and smokehouse, work house, pump house, chicken house, outhouse and barn. It was listed on the National Register in 1979.',
  look='A frame farmhouse with an octagonal tower, an encircling verandah, stained glass and spindle, spool and shingle work, with its farm outbuildings. Interior not checked.',
  accn='Near Garden City, Cass County. Ownership and visiting were not found: treat it as private and look from the road. The pin is Wikipedia\'s coordinate and was not confirmed on the ground.',
  links=[W('O\'Bannon Homestead')],
  conf='mixed', brick='no', hours=''),

N('watkins-family-farm-raymore-mo', 'Watkins Family Farm Historic District (Lakeland Farm)', 'Raymore', 'kcmo', 'landmark', 'standing',
  38.77556, -94.46, 'site', 'view', 'drive', '', '1868–1957',
  'Wikipedia describes a farm and historic district near Raymore with 18 contributing buildings, three sites and 21 structures from about 1868 to 1957: three houses, eight barns, machine sheds, wells, ten dams and ponds, a milk house, a silo, corn bins and a cattle loading ramp. '
  'The Allen-Watkins Residence (1913) was built from a Sears and Roebuck kit, plan #227 "The Castleton". It was listed on the National Register in 2007.',
  look='A working-farm landscape: the Prairie School style kit house, barns, ponds and farm structures. Whether any can be seen from a public road was not checked.',
  accn='Private farm near Raymore, Cass County, owner not found: look only from the road if at all. The pin is Wikipedia\'s coordinate and was not confirmed on the ground; the Register list gives no coordinate for it.',
  links=[W('Watkins Family Farm Historic District')],
  conf='mixed', brick='no', hours=''),
]

PIN_NOTES = {
 'new-santa-fe-cemetery-ruts-kc-mo': 'Coordinate from the Wikipedia Register list for the New Santa Fe trail swales, near 122nd Street and State Line Road. A photograph on Wikimedia Commons taken at the pin shows the cemetery gate and its marker; the aerial shows a wooded plot among houses but not the ruts.',
 'raytown-historical-society-museum-mo': 'Address match in OpenStreetMap for 9705 East 63rd Street, which names the museum.',
 'lees-summit-history-museum-mo': 'Address match for 220 SW Main Street, checked on the aerial.',
 'lees-summit-mopac-depot-mo': 'Address match for 217 SW Main Street put the point on the tracks; moved about 48 m onto the long depot building east of them, seen on the aerial.',
 'pleasant-hill-historical-museum-mo': 'Address match in OpenStreetMap that names the society, 125 Wyoming Street.',
 'belton-historical-society-museum-mo': 'Address match for 512 Main Street; the building was not named by the match.',
 'belton-historical-railroad-mo': 'Wikipedia\'s coordinate for the railroad, checked on the aerial.',
 'robert-a-brown-house-harrisonville-mo': 'Wikipedia\'s coordinate for the house. It falls in woods on the aerial and no house could be picked out, so the pin marks the general area only.',
 'obannon-homestead-garden-city-mo': 'Wikipedia\'s coordinate for the homestead, checked on the aerial.',
 'watkins-family-farm-raymore-mo': 'Wikipedia\'s coordinate for the farm, checked on the aerial.',
}
