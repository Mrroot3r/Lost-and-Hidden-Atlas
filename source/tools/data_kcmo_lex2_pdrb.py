# November 25, 2026: a second pass round Lexington, Missouri (Lafayette County), with three leads finished from the first pass
# (the Madonna of the Trail, Machpelah Cemetery, Forest Grove Cemetery), plus Higginsville and Dover houses, and three places
# nearer Kansas City (Blue Mills, the Sibley railroad bridge, the Lee's Summit historical cemetery).
# Facts come only from sources opened in this session: Wikipedia read as raw text, the Lexington chamber of commerce and city
# pages, Missouri Preservation, the Santa Fe Trail Historic Sites page of the University of New Mexico, the parish page of Christ
# Church, and Waymarking pages that copy the text of historical markers. National Register forms could not be read.
from data_b import N
from data_ma import W

LNR = ['Missouri State Parks: Lafayette County National Register listings', 'https://mostateparks.com/basic-page/missouri-national-register-listings/Lafayette']

PLACES = [
N('machpelah-cemetery-lexington-mo', 'Machpelah Cemetery', 'Lexington', 'kcmo', 'burial', 'standing',
  39.17871, -93.87286, 'site', 'view', 'drive', 'cemeteries', '1839–',
  'The first burial here, in 1839, was in the Waddell family cemetery. In 1849 William Bradford Waddell gave it and nearby land to form Machpelah, which the city says an act of the Missouri General Assembly set up that year. '
  'Soldiers from both sides of the 1861 Battle of Lexington are buried here, and so are victims of the 1852 Saluda steamboat explosion, in a mass grave with a memorial. It was added to the National Register in 2022.',
  look='Old monuments and iron work made at a local foundry. Look for the Saluda memorial and the graves of Wentworth Academy\'s founder and of a Pony Express founder. The Lexington Historical Association holds a candlelight tour here each October.',
  accn='A cemetery on South 20th Street at Jefferson Avenue, Lexington, run by its own corporation (the city\'s page describes it). The pin is the street corner by the north gate: the cemetery\'s whole outline was not read. Opening hours were not found; current burial information is by a message to the volunteer sexton, whose number is on the chamber page. Park on the street.',
  links=[['City of Lexington: Machpelah Cemetery', 'https://lexingtonmo.gov/machpelahcemetery'], ['Lexington Area Chamber of Commerce: Machpelah Cemetery', 'https://historiclexington.com/?p=5822'], LNR],
  conf='mixed', brick='?'),

N('forest-grove-cemetery-lexington-mo', 'Forest Grove Cemetery', 'Lexington', 'kcmo', 'burial', 'standing',
  39.20109, -93.86408, 'area', 'view', 'drive', 'cemeteries', '1854–',
  'The town of Lexington held this ground by 1854. It may have been a burying place for enslaved people and a pauper\'s field; on October 28, 1890 the city deeded it to "trustees for the colored people of Lexington, Missouri". '
  'George H. Green, who was principal of the Douglass School from 1886 to 1936, is buried here, and so is the Black baseball pitcher William Lindsay. It was added to the National Register in 2022.',
  look='A burying ground whose first graves include people born into slavery, later joined by veterans, miners, teachers, musicians and craftsmen. Read the chamber of commerce page for the people buried here before you go.',
  accn='Address 892 Golf Road, Lexington (an address lookup, not the cemetery\'s outline; sources give both 892 and 900). Owner today and opening hours were not found; look from the road unless the nonprofit Forest Grove Cemetery Project, which works on the stones and fence, says otherwise. Park on the road.',
  links=[['Lexington Area Chamber of Commerce: Forest Grove Cemetery', 'https://historiclexington.com/?p=5895'], LNR],
  conf='mixed', brick='?'),

N('madonna-of-the-trail-lexington-mo', 'Madonna of the Trail, Lexington', 'Lexington', 'kcmo', 'curio', 'marker',
  39.18662, -93.88628, 'exact', 'view', 'drive', '', '1928',
  'A statue of a pioneer mother with a baby and a boy, unveiled on September 17, 1928 by the Missouri Daughters of the American Revolution. August Leimbach of St. Louis made it. It is one of 12 along the National Old Trails Road, and Jackson County judge Harry Truman gave the main speech. A Potawatomi "Trail of Death" marker of 1838 shares the spot.',
  look='A ten-foot statue of Missouri granite on a square base, with the DAR\'s inscription on the front and the names of Lexington traders such as the Aull brothers and Russell, Majors and Waddell on one side. Views over the Missouri valley.',
  accn='On a street corner in the Highland Avenue Historic District (the marker pages say Highland and Broadway; a first-pass note found three different corner names, so check the pin). Seen from the street; the owner was not found (the federal map shows no public land here). Park on the street.',
  links=[['Waymarking: Madonna of the Trail, Lexington', 'https://www.waymarking.com/waymarks/WMBK33_Madonna_of_the_Trail_Lexington_Missouri'], W('Madonna of the Trail'), ['Lexington Area Chamber of Commerce: Must See', 'https://historiclexington.com/visit-lexington/must-see/']],
  conf='mixed', brick='no'),

N('christ-episcopal-church-lexington-mo', 'Christ Episcopal Church', 'Lexington', 'kcmo', 'worship', 'standing',
  39.18470, -93.87975, 'exact', 'open', 'drive', '', '1848',
  'The parish was founded in 1844 by Bishop Jackson Kemper, and the Gothic Revival church was built in 1848 of pink brick. Cannon fire hit it in the 1861 Battle of Lexington. The bell tower was added in 1890. One source attributes the design to the Rev. J. W. Dunn; another page names a different person, so the designer is not settled.',
  look='Gothic Revival brick church with an open-truss roof, lancet windows with some fine painted glass (the Register form, as a marker quotes it, says glass by Booth of New York in the chancel in 1884), walnut furnishings, original pews and a small tracker organ brought by steamboat in 1870. The 1890 tower has battlements. Inside not seen.',
  accn='1300 Franklin Avenue (corner of 13th Street), Lexington; an active parish. Its page says the Sunday service is at 10 a.m. Street parking. Other days: a Waymarking page says tours are available, which the parish page does not confirm.',
  links=[['Christ Church, Lexington (parish page)', 'https://christchurchlexington.diowestmo.org/'], ['Waymarking: Christ Episcopal Church (copies the marker and Register text)', 'https://www.waymarking.com/waymarks/WM11846_Christ_Episcopal_Church_Lexington_MO']],
  conf='mixed', brick='yes', hours='Sunday service 10 a.m. (parish page); other times not listed'),

N('zion-ame-church-lexington-mo', 'Zion African Methodist Episcopal Church', 'Lexington', 'kcmo', 'worship', 'standing',
  39.18711, -93.87613, 'area', 'view', 'drive', '', '1870',
  'Built in 1870 in the Romanesque style, this was once the largest Black congregation in Lafayette County. The AME church closed it in 2006 after the congregation shrank, and it was damaged by vandals. Missouri Preservation put it on its endangered list in 2010 and 2011. It was bought and restored in 2017 as an event space, and a comment on the Preservation page says it was bought again in 2023 for a house, so its present use is not settled.',
  look='A Romanesque church with its tower and the look of the 1870s. Look from the street at the walls and windows. Whether the interior survives was not found.',
  accn='201 North 16th Street, Lexington, between the old hospital and Wentworth Academy grounds. Private; look from the street. The Preservation page says it was restored as an event space in 2017 and sold again in 2023; check before a visit.',
  links=[['Missouri Preservation: Zion AME Church', 'https://preservemo.org/zion-african-methodist-episcopal-church/']],
  conf='mixed', brick='?'),

N('saluda-memorial-heritage-park-lexington-mo', 'Saluda Memorial, Heritage Park', 'Lexington', 'kcmo', 'curio', 'marker',
  39.18455, -93.88002, 'area', 'view', 'drive', '', '1852; memorial 2002',
  'On April 9, 1852 the steamboat Saluda blew up just above Lexington on the Missouri River, killing most of the people on board, many of them Latter-day Saint emigrants from Britain bound for Utah. The count differs: Wikipedia says over 100, a Lexington tourism page says about 75. Townspeople rescued survivors and took in orphans. The town put up this memorial in 2002 for the 150th year.',
  look='A small park memorial with information panels, a bell and a plaque of victims\' names, across from the Lexington Historical Museum. Many of the dead lie in Machpelah Cemetery, which has its own memorial.',
  accn='In Heritage Park, across the street from the museum (112 South 13th Street), Lexington; the tourism bureau lists it as open year round. The owner was not found (the federal map shows no public land here; the park is probably the city\'s, not checked). Street parking. The river has moved north, so the site of the explosion is not at the memorial.',
  links=[['VisitMO: Saluda Memorial at Heritage Park', 'https://visitmo.com/things-to-do/saluda-memorial-at-heritage-park'], W('Saluda (steamship)'), ['City of Lexington: Machpelah Cemetery', 'https://lexingtonmo.gov/machpelahcemetery']],
  conf='mixed', brick='?'),

N('houx-hoefer-rehkop-house-higginsville-mo', 'Houx-Hoefer-Rehkop House', 'Higginsville', 'kcmo', 'landmark', 'standing',
  39.07583, -93.71861, 'site', 'view', 'drive', '', 'about 1882',
  'A two-story Italianate brick house in a T plan with a hipped roof, built about 1882. The front porch has four round columns and two pilasters with Corinthian capitals. It was added to the National Register in 1983, under the Houx, Hoefer and Rehkop family names. The land was first taken from the government in 1843 by the Speers, according to the search listing of the Register record; the form itself was not read.',
  look='Look for the Corinthian porch and the hipped roof from the road. A web search listing for the form says five brick chimneys painted white; not checked.',
  accn='A private house at 1900 Walnut Street in Higginsville per a search listing of the Register record. Look from the street only; owner not checked.',
  links=[W('Houx-Hoefer-Rehkop House'), LNR],
  conf='mixed', brick='?'),

N('dinwiddie-house-dover-mo', 'James M. Dinwiddie House (Maple Grove Stock Farm)', 'Dover', 'kcmo', 'landmark', 'standing',
  39.19222, -93.70167, 'area', 'view', 'drive', '', 'about 1840',
  'A two-story brick house of about 1840 in vernacular Greek Revival style, with a central passage, a one-story portico on the front and a one-story rear ell. Also known as Maple Grove Stock Farm, it is one of the antebellum houses of Lafayette and nearby counties listed on the National Register together in 1997.',
  look='A brick house of the I-house plan. A web search listing places it about a quarter mile east of the US 24 and Missouri 184 junction near Dover.',
  accn='A private farm, location from the Register list coordinate only (the pin may not be on the house). Look from the public road; owner not checked and no visiting is described.',
  links=[W('James M. Dinwiddie House'), LNR],
  conf='mixed', brick='?'),

N('george-johnson-house-lexington-mo', 'George Johnson House', 'Lexington', 'kcmo', 'landmark', 'standing',
  39.18528, -93.85444, 'area', 'view', 'drive', '', 'about 1894',
  'A frame house of about 1894 in the Queen Anne style, with a contributing two-story building behind that served as a summer kitchen and servants\' quarters. It was added to the National Register in 1993.',
  look='A Queen Anne frame house; look from the street for its porch and trim. The rear outbuilding is the unusual survivor. Not seen from inside.',
  accn='A private house in Lexington; the Register list coordinate only, and the street address was not found. Look from a public street; owner not checked.',
  links=[W('George Johnson House (Lexington, Missouri)'), LNR],
  conf='mixed', brick='no'),

N('blue-mills-independence-mo', 'Blue Mills (site of the gristmill and sawmill)', 'Independence', 'kcmo', 'industry', 'gone',
  39.1576, -94.30932, 'area', 'view', 'drive', '', '1834–1860s',
  'Blue Mills was a pair of mills on the Little Blue River beside a Santa Fe Trail crossing. A gristmill went up in 1834 and a sawmill in 1835, built for James Aull and others. A small town, a post office and a warehouse grew round them, and flour went to Independence, St. Joseph, Fort Leavenworth and farther. The mills ran into the early 1860s and were ruins by the 1920s. The National Park Service says the mill no longer stands.',
  look='Nothing is described as standing. The Register lists it as an archaeological site and the city lists it among its own National Register properties. Look for the river crossing and the old road line on the aerial, not for walls.',
  accn='The city lists the address as 3101 Lentz Drive (a lookup of "3101 N Lentz Rd" gave the pin). The pin is an address point only. Whether the ground is public or private, and whether any traces can be seen, was not found; treat as view-only from the public road.',
  links=[['Santa Fe Trail Historic Sites (UNM): Blue Mills', 'https://historic-trails.unm.edu/sites/blue-mills.html'], ['City of Independence: National Register properties', 'https://www.independencemo.gov/government/city-departments/community-development/historic-preservation/designated-historical-resources-architectural-surveys/national-register-properties'], W('Blue Mills, Missouri')],
  conf='lead', brick='?'),

N('sibley-railroad-bridge-mo', 'Sibley Railroad Bridge', 'Sibley', 'kcmo', 'rail', 'standing',
  39.1801, -94.1793, 'exact', 'view', 'drive', '', '1887–1888',
  'A three-span through-truss bridge that carries the BNSF railway over the Missouri River at Sibley, between Jackson and Ray counties. The first bridge of 1887 to 1888 had three Whipple truss spans and was later rebuilt with Parker truss spans. A second bridge alongside has been built since 2023 for the busy single track.',
  look='A long steel truss over the river, still working; trains cross it. It can be seen from the visitor centre deck at Fort Osage.',
  accn='Seen from Fort Osage\'s visitor centre, a county site; the Fort Osage entry on the Atlas gives its hours. The bridge belongs to a working railroad: do not go onto the tracks or the bridge.',
  links=[W('Sibley Railroad Bridge')],
  conf='mixed', brick='no'),

N('lees-summit-historical-cemetery-mo', 'Lee\'s Summit Historical Cemetery', 'Lee\'s Summit', 'kcmo', 'burial', 'standing',
  38.91622, -94.36384, 'exact', 'view', 'drive', 'cemeteries', '1865–',
  'William Bullitt Howard gave about two acres in 1865 to the town of Strother, which later became Lee\'s Summit. More land was added in 1875, 1887 and 1907. The potter\'s field holds many who could not buy a lot, among them victims of the 1918 influenza, infants and enslaved people whose stones have worn away. The original 1860 wrought-iron entrance sign was restored in 2002.',
  look='Old stones among the cemetery lanes, the restored iron sign at the southeast corner, and the unmarked potter\'s field.',
  accn='A city cemetery near the old town centre of Lee\'s Summit; who runs it and its hours were not read. Street parking. Treat as a quiet burying ground.',
  links=[W('Lee\'s Summit Historical Cemetery')],
  conf='mixed', brick='?'),
]

BATCH = {'key': 'kcmo_lex2_pdrb', 'label': 'Lexington, Higginsville and Lee\'s Summit, Missouri: second pass', 'added': '2026-11-25 02:01'}

PIN_NOTES = {
 'machpelah-cemetery-lexington-mo': 'Started from the address lookup for South 20th Street at Jefferson, which fell on the road, and moved about 100 m west onto the rows of graves seen on the aerial.',
 'forest-grove-cemetery-lexington-mo': 'The address lookup for 892 Golf Road. The aerial shows a loop road and open ground at the pin but no clear graves, so the pin marks the area only.',
 'madonna-of-the-trail-lexington-mo': 'The coordinate on a Waymarking page that copies the marker; it agrees with an OpenStreetMap point of a first-pass note.',
 'christ-episcopal-church-lexington-mo': 'The coordinate on a Waymarking page that copies the marker.',
 'zion-ame-church-lexington-mo': 'The address lookup for 201 North 16th Street; the aerial shows houses at the pin and the church could not be told apart, so the pin marks the area only.',
 'saluda-memorial-heritage-park-lexington-mo': 'The coordinate on a Waymarking page about the memorial. The aerial shows a street corner of houses and small buildings, and the park could not be picked out, so the pin marks the area only.',
 'houx-hoefer-rehkop-house-higginsville-mo': 'The Register list coordinate (Wikipedia).',
 'dinwiddie-house-dover-mo': 'The Register list coordinate (Wikipedia); the aerial is used to check it.',
 'george-johnson-house-lexington-mo': 'The Register list coordinate (Wikipedia).',
 'blue-mills-independence-mo': 'The address lookup for 3101 Lentz Road. Wikipedia places the community of Blue Mills farther south-east.',
 'sibley-railroad-bridge-mo': 'The coordinate in the Wikipedia article.',
 'lees-summit-historical-cemetery-mo': 'The address lookup for the cemetery, which matches Wikipedia.',
}
