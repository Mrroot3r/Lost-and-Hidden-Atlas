# November 24, 2026: Lawrence, Lecompton, Baldwin City and Vinland, Douglas County, Kansas (west of Kansas City).
# Part of filling in the Kansas City area on purpose for a local researcher.
# Facts from the Kansas Historical Society's register listings for Douglas County (read as pages), the National Register
# nominations it publishes (the ones with a text layer were read whole; the older scanned ones could not be), the
# Lawrence Journal-World's local history column, a City of Lawrence planning report and Wikipedia read as raw text.
# Nothing was checked on the ground.
from data_b import N
from data_ma import W

KS_LIST = ['Kansas Historical Society: National and State Registers, Douglas County', 'https://www.kansashistory.gov/natreg/natreg_listings/search/county:DG/records:all']
NOM = 'https://www.kansashistory.gov/resource/national_register/nominationsNRDB/'

BATCH = {'key': 'ks_dgco_fmqb', 'label': 'Douglas County, Kansas (Lawrence area)', 'added': '2026-11-24 06:00'}

PLACES = [
N('winter-school-70-lecompton-ks', 'Winter School No. 70', 'Lecompton', 'ks', 'civic', 'standing',
  39.00083, -95.3646, 'exact', 'view', 'drive', '', '1869',
  'A one-room schoolhouse of local limestone with walls nearly two feet thick, built in 1869 by a Swedish stonemason, Chris Christensen. The district closed in 1949 and the building was given to a community club, then used for hay storage and left to decay. '
  'A family-run nonprofit bought it in 1984; it was rehabilitated in 2019 and listed on the National Register in 2020.',
  look='Stone walls with a wooden bell tower above the original date stone (1869, "No. 70"). It stands on a hill beside the county road known as the Farmers Turnpike, in view of the interstate. Interior not checked.',
  accn='Private; the 2020 nomination says it is owned by descendants of the founding Winter family. Look from the county road (N 1800 Road). The nomination does not say that the public may go in, and no parking is mentioned.',
  links=[['Kansas Historical Society: Winter School No. 70 nomination (2020)', NOM + 'KS_DouglasCounty_WinterSchoolNo70_Listed12222020.pdf'], KS_LIST],
  conf='mixed', brick='no', hours=''),

N('kibbee-farmstead-lawrence-ks', 'Kibbee Farmstead', 'Lawrence', 'ks', 'landmark', 'standing',
  38.95666, -95.22311, 'site', 'view', 'drive', '', 'about 1909–1910',
  'Walter and Fannie Kibbee developed a small farm on what was then the edge of Lawrence, with milk cows, poultry and pigs and butter and eggs sold in town. The six surviving buildings (a Dutch Colonial Revival house, barn, chicken house, shed, outhouse and a 1920s garage) make heavy use of concrete. '
  'Lawrence annexed the land in 1959 and houses, a recreation centre and a Boys and Girls Club school now surround the 5 acres that are left.',
  look='A farmyard of small concrete-and-frame buildings on the corner of East 15th Street and Haskell Avenue, with suburban Lawrence all round it. The nomination calls it in excellent condition. Interior not checked.',
  accn='Private; the 2013 nomination says "current owners" and does not name them. Look from East 15th Street or Haskell Avenue. It is not described as open to visitors.',
  links=[['Kansas Historical Society: Kibbee Farmstead nomination (2013)', NOM + 'Douglas_KibbeeFarmsteadNR.pdf'], KS_LIST],
  conf='mixed', brick='?', hours=''),

N('lucy-hobbs-taylor-house-lawrence-ks', 'Lucy Hobbs Taylor House', 'Lawrence', 'ks', 'landmark', 'standing',
  38.96895, -95.23737, 'exact', 'view', 'walk', '', 'about 1871',
  'An Italianate house at 809 Vermont Street, listed on the National Register in 1982 as the Lucy Hobbs Taylor Building. Taylor graduated from the Ohio College of Dental Surgery in 1866, often called the first woman to graduate from a dental school, and practised dentistry in Lawrence after moving there. '
  'A 2015 City of Lawrence report says the property was built in 1871 and is the only house left in the 800 block of Vermont; a staff report in the same file gives a later date, so the year is not settled.',
  look='The only house still standing in this block of Vermont Street, among downtown buildings. Interior not checked, and no source read says who uses it now.',
  accn='Present owner and use not checked. Look from Vermont Street; street parking downtown. Listed on the National Register and, per the City of Lawrence report, a local landmark.',
  links=[['Kansas Historical Society: Lucy Hobbs Taylor Building listing', 'https://www.kansashistory.gov/natreg/natreg_listings/search/county:DG/records:all'],
         ['City of Lawrence: analysis of the environs of 809 Vermont (2015)', 'https://assets.lawrenceks.org/agendas/cc/2015/04-28-15/pl_l-15-00048_environs_definition_and_map.pdf'], W('Lucy Hobbs Taylor')],
  conf='mixed', brick='?', hours=''),

N('first-methodist-episcopal-church-lawrence-ks', 'First Methodist Episcopal Church (Lawrence First United Methodist)', 'Lawrence', 'ks', 'worship', 'standing',
  38.96604, -95.23691, 'exact', 'view', 'walk', '', '1889–1891',
  'John G. Haskell designed the Romanesque Revival church in 1888 and it was built between 1889 and 1891; the congregation has used it without a break since 1891. A modern L-shaped education wing by Robert & Ericson was added in 1962 and a third addition in 1987. '
  'It was listed on the National Register in 2019, which says the building keeps good integrity from 1891 through the 1960s addition.',
  look='The Romanesque front on Vermont Street, with the 1962 wing beside it. Which interior fittings survive was not checked, and no page of the church was read for visiting times.',
  accn='An active church at 946 Vermont Street, downtown; street parking. No page of the church could be opened when this was written (it answered "forbidden"), so no service times are given; a directory lists Sunday morning worship.',
  links=[['Kansas Historical Society: First Methodist Episcopal Church listing (2019)', 'https://www.kansashistory.gov/natreg/natreg_listings/search/county:DG/records:all']],
  conf='mixed', brick='?', hours='?'),

N('english-lutheran-church-lawrence-ks', 'English Lutheran Church (now law offices), 1040 New Hampshire', 'Lawrence', 'ks', 'worship', 'standing',
  38.96411, -95.2345, 'exact', 'view', 'walk', '', '1870',
  'A small Gothic church of local stone quarried from the hill where the University of Kansas now stands, designed by John G. Haskell and dedicated on December 18, 1870 at an estimated cost of $4,500. It measures 30 by 50 feet. '
  'The Lutherans added to it in 1895, renamed it Trinity in 1910 and moved to a new church in 1929; a Church of God congregation used it from 1933 to 1974. Three law offices occupy it now (2023 report).',
  look='Rough stone walls, a steep gable roof and cut-stone trim round doors and windows under Gothic arches. The old interior had plain walls and exposed roof beams; whether any of that survives inside was not checked.',
  accn='Private offices on New Hampshire Street, a short walk from the courthouse; street parking. Look from the street. The building is a business and not open as a sight.',
  links=[['Lawrence Journal-World: Local History, historic former church (2023)', 'https://www2.ljworld.com/living/columns/2023/oct/20/local-history-historic-former-church-still-gets-plenty-of-use-today/'], KS_LIST],
  conf='', brick='no', hours=''),

N('trinity-lutheran-church-lawrence-ks', 'Trinity Lutheran Church (1928) and parsonage', 'Lawrence', 'ks', 'worship', 'standing',
  38.96024, -95.2344, 'exact', 'open', 'walk', '', '1928',
  'The Gothic Revival church of 1928 was designed by Henry C. Eckland and has a 1992 addition. With a Tudor Revival parsonage (1941), a Colonial Revival house bought in 1969 and two garages, it forms a five-building historic district listed on the National Register in 2024. '
  'The congregation moved here from its 1870 stone church on New Hampshire Street.',
  look='A Gothic church and Tudor parsonage together on New Hampshire Street. Interior fittings not checked.',
  accn='An active church at 1245 New Hampshire Street; street parking. Hours are from the church\'s own web page, read November 2026.',
  links=[['Trinity Lutheran Church, Lawrence', 'https://tlclawrence.org'], KS_LIST],
  conf='mixed', brick='?', hours='Sundays: worship 9:30 a.m. (also livestreamed)'),

N('fernand-strong-house-lawrence-ks', 'Fernand-Strong House', 'Lawrence', 'ks', 'landmark', 'standing',
  38.96028, -95.25295, 'exact', 'view', 'drive', '', 'about 1872',
  'A wood-frame Italianate house of about 1872 with a large addition of about 1905, built on land first claimed by early Lawrence settler James S. Emery near the University of Kansas. '
  'Former KU chancellor Frank Strong and James Naismith, the inventor of basketball, are among its notable owners. It was listed on the National Register in 2008.',
  look='An Italianate main block with its early-1900s addition, seen from University Drive. Interior not checked.',
  accn='Private house at 1515 University Drive; present owner and use not checked. Look from the street.',
  links=[['Kansas Historical Society: Fernand-Strong House listing (2008)', 'https://www.kansashistory.gov/natreg/natreg_listings/search/county:DG/records:all']],
  conf='mixed', brick='?', hours=''),

N('mackie-house-lawrence-ks', 'George K. Mackie House (former Lawrence Women\'s Club)', 'Lawrence', 'ks', 'landmark', 'standing',
  38.94861, -95.23631, 'exact', 'view', 'drive', '', '1917',
  'Coal-company owner George Mackie commissioned this Neoclassical Revival house in 1917 from Kansas City architect H. Alexander Drake. His widow sold it in 1937 to the Lawrence Women\'s Club, which used it for meetings and gatherings until 1975. '
  'The listing calls it a textbook example of the style, with a monumental portico, a side porch and heavy window and door surrounds. It was listed on the National Register in 2009.',
  look='A big white-columned portico on a corner lot on Massachusetts Street south of downtown. Present use and interior not checked.',
  accn='Present owner and use not checked. Look from Massachusetts Street (1941 Massachusetts); street parking.',
  links=[['Kansas Historical Society: George K. Mackie House listing (2009)', 'https://www.kansashistory.gov/natreg/natreg_listings/search/county:DG/records:all']],
  conf='mixed', brick='?', hours=''),

N('beal-house-lawrence-ks', 'Beal House (1950 Usonian house)', 'Lawrence', 'ks', 'landmark', 'standing',
  38.95436, -95.24268, 'exact', 'view', 'drive', '', '1950',
  'George Malcolm Beal, a University of Kansas architecture professor, designed and lived in this Usonian house, applying Frank Lloyd Wright\'s ideas. He worked out sun angles with a "heliodon" he built himself, so the roof overhangs a nearly all-glass south wall to take in winter sun and shade summer sun. '
  'It was listed on the National Register in 2015 as part of Lawrence\'s post-war resources.',
  look='A low modern house with a long south glass wall under a deep roof overhang. Interior not checked.',
  accn='Private house at 1624 Indiana Street; look from the street only.',
  links=[['Kansas Historical Society: Beal House listing (2015)', 'https://www.kansashistory.gov/natreg/natreg_listings/search/county:DG/records:all']],
  conf='mixed', brick='?', hours=''),

N('chewning-house-lawrence-ks', 'Chewning House (1936 General Electric "New American Home")', 'Lawrence', 'ks', 'landmark', 'standing',
  38.96176, -95.25292, 'exact', 'view', 'drive', '', '1936',
  'Built in 1936 and designed by George M. Beal, then chair of the architecture programme at the University of Kansas. It is one of about 1,000 houses built across the United States in a General Electric and Federal Housing Administration "New American Home" programme meant to put people to work in the Depression. '
  'It is the only known one near Lawrence and one of the earliest Modern houses in the city; it was listed on the National Register in 2019.',
  look='An early Modern house in the West Hills neighbourhood, west of the university. Interior not checked.',
  accn='Private house at 1510 Stratford Road; look from the street only.',
  links=[W('Chewning House (Lawrence, Kansas)'), KS_LIST],
  conf='', brick='?', hours=''),

N('star-cash-grocery-vinland-ks', 'Star Cash Grocery Store and Residence', 'Vinland', 'ks', 'civic', 'standing',
  38.83989, -95.18275, 'exact', 'view', 'drive', '', '1890 and 1921',
  'A village grocery of 1921 and the Late Victorian residence of 1890 beside it, tied to early Vinland settlers and to the mercantile families that ran the store until the 1950s. '
  'The nomination calls them part of a nearly unbroken row of largely unaltered period buildings on Vinland\'s main street; it was listed on the National Register in 2019.',
  look='The 1921 store front and the 1890 house on Vinland\'s old main street, next to the Grange hall and Presbyterian church already on the Atlas. Interior not checked.',
  accn='Present owner and use not checked. Look from the street (696 East 1719 Road); no parking is described.',
  links=[['Kansas Historical Society: Star Cash Grocery Store and Residence nomination (2019)', 'https://www.kansashistory.gov/resource/national_register/nominationsNRDB/KS_DouglasCounty_StarCashGroceryResidence_Listed%2009302019.pdf'], KS_LIST],
  conf='mixed', brick='?', hours=''),

N('marion-springs-school-baldwin-city-ks', 'Marion Springs Elementary School', 'Baldwin City', 'ks', 'civic', 'standing',
  38.78444, -95.33413, 'exact', 'view', 'drive', '', 'after 1962; Baldwin City district from 1966',
  'A Modern Movement consolidated country school designed by architect Joseph Radotinsky, built to replace several one-room schools in south Douglas County. It was joined to the Baldwin City school district in 1966. '
  'The state register describes it as a good example of the two-or-more-teacher consolidated country school, standing on a section corner as such schools usually did.',
  look='A low modern school building at the corner of East 900 Road, out in farmland. A Wikimedia Commons caption says the 9.5-acre site was bought in 1962 for the new school, so it was built after that; its present use was not found. Interior not checked.',
  accn='Present owner and use not checked. Look from the county road (316 East 900 Road); no parking is described.',
  links=[['Kansas Historical Society: Marion Springs School listing', 'https://www.kansashistory.gov/natreg/natreg_listings/view/1813'], KS_LIST],
  conf='mixed', brick='?', hours=''),

N('lone-star-lake-dam-douglas-county-ks', 'Lone Star Lake Dam (CCC and Art Deco guardrails)', 'Lawrence', 'ks', 'water', 'standing',
  38.8402, -95.3806, 'site', 'public', 'drive', '', '1934–1940',
  'The Civilian Conservation Corps built the earthen dam between 1934 and 1940, and its guardrails have Art Deco detailing. The dam holds back the 185-acre lake, and the National Register listing of 2023 treats it as an example of New Deal work in Kansas; the original spillway has been replaced. '
  'The camp that housed the crew is already on the Atlas.',
  look='The dam along East 582 Road on the north side of the park, with its low concrete guardrails. Walk the top of the dam and look at the rails.',
  accn='Lone Star Lake Park is owned and run by Douglas County (Wikipedia), about 10 miles southwest of Lawrence; the nomination lists a campground, beach and boat ramps. Park hours, fees and the parking lot nearest the dam were not read; the county ownership comes from Wikipedia, not from the county\'s own page.',
  links=[['Kansas Historical Society: Lone Star Lake Dam nomination (2023)', NOM + 'DouglasCo_LoneStarLakeDam_listed_10172023_compres.pdf'], W('Lone Star Lake')],
  conf='mixed', brick='no', hours=''),

N('first-presbyterian-church-clinton-parkway-lawrence-ks', 'First Presbyterian Church (1967–68, Sovik, Mathre & Madson)', 'Lawrence', 'ks', 'worship', 'standing',
  38.94166, -95.26442, 'exact', 'view', 'drive', '', '1967–1968',
  'A modern church of concrete, brick and glass built in 1967 and 1968 to a design by the Minnesota firm of Sovik, Mathre and Madson, known for liturgical design. The register says it is the only church in Lawrence, and in Kansas, by the architect Edward A. Sovik. '
  'It was listed on the National Register in 2024.',
  look='A modern church on Clinton Parkway. Interior not checked.',
  accn='An active church at 2415 Clinton Parkway; parking lot not checked. No page of the church was read, so no service times are given.',
  links=[['Kansas Historical Society: First Presbyterian Church listing (2024)', 'https://www.kansashistory.gov/natreg/natreg_listings/search/county:DG/records:all']],
  conf='mixed', brick='some', hours='?'),
]

PIN_NOTES = {
 'winter-school-70-lecompton-ks': 'The pin is on the address lookup for 744 N 1800 Road, checked on the aerial.',
 'kibbee-farmstead-lawrence-ks': 'The pin is on the address lookup for 1500 Haskell Avenue, checked on the aerial.',
 'lucy-hobbs-taylor-house-lawrence-ks': 'The pin is on the address lookup for 809 Vermont Street, checked on the aerial.',
 'first-methodist-episcopal-church-lawrence-ks': 'The pin is on the address lookup for 946 Vermont Street, checked on the aerial.',
 'english-lutheran-church-lawrence-ks': 'The pin is on the address lookup for 1040 New Hampshire Street, checked on the aerial.',
 'trinity-lutheran-church-lawrence-ks': 'The pin is on the address lookup for 1245 New Hampshire Street, checked on the aerial.',
 'fernand-strong-house-lawrence-ks': 'The pin is on the address lookup for 1515 University Drive, checked on the aerial.',
 'mackie-house-lawrence-ks': 'The pin is on the address lookup for 1941 Massachusetts Street, checked on the aerial.',
 'beal-house-lawrence-ks': 'The pin is on the address lookup for 1624 Indiana Street, checked on the aerial.',
 'chewning-house-lawrence-ks': 'The pin is on the address lookup for 1510 Stratford Road, checked on the aerial.',
 'star-cash-grocery-vinland-ks': 'The pin is on the address lookup for 696 East 1719 Road, checked on the aerial.',
 'marion-springs-school-baldwin-city-ks': 'The pin is on the address lookup for 316 East 900 Road, checked on the aerial.',
 'lone-star-lake-dam-douglas-county-ks': 'The coordinate is the National Register list entry for the dam.',
 'first-presbyterian-church-clinton-parkway-lawrence-ks': 'The pin is on the address lookup for 2415 Clinton Parkway, checked on the aerial.',
}
