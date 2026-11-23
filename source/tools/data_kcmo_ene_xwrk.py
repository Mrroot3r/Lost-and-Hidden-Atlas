# November 23, 2026: 18th and Vine, the east side and the Northeast (Scarritt Point, the East Bottoms), Kansas City, Missouri.
# Part of filling in the Kansas City area on purpose for a local researcher. Facts come from the linked sources only:
# Wikipedia read as raw text, the National Register forms for the Mutual Musicians' building, the Heim bottling plant and the
# National Cloak and Suit building (read), the Museum of Kansas City's own visit page, a Clio entry and a KCUR article.
# The Register forms for the others were not available online, so those entries say only what the other sources give.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_ene_xwrk', 'label': 'Kansas City: 18th and Vine and the Northeast', 'added': '2026-11-23 21:51'}

NRL = ['Wikipedia: National Register listings in Kansas City, Missouri (Jackson County, outside downtown)', 'https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Jackson_County,_Missouri:_Kansas_City_other']

PLACES = [
N('mutual-musicians-foundation-kc', "Mutual Musicians' Foundation Building", 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.09028, -94.56194, 'exact', 'open', 'drive', '', '1904',
  "Built in 1904 as an apartment house, this two-story building at 18th and Highland became the clubhouse of the Black musicians' union local, which bought it with money raised at musicians' contests. The National Register form says it now serves as a clubhouse, recital hall and museum, and the Pete Johnson and Joe Turner boogie-woogie tune \"627 Stomp\" is named for it. "
  "It is a National Historic Landmark. The materials are given two ways: the 1979 form says the walls are pressed red brick on a rubble limestone foundation, while Wikipedia says the pressed brick is covered in painted stucco.",
  look="A plain two-story building with a flat roof, glass-block windows and blocked openings where the form says the original entrances and five of six chimneys were removed. Late-night jam sessions are reported here, but the foundation's own page was not read, so days and times are not given. Interior not checked.",
  accn="Owned by the Mutual Musicians' Foundation at 1823 Highland Avenue, in the 18th and Vine district. Visit KC lists tours on weekdays and weekend-night jams, and Atlas Obscura says to call 816-471-5212 to ask for a tour; neither is the foundation's own page, so hours are not given. Street parking.",
  links=[W("Mutual Musicians' Foundation Building"), ['National Register form (1979)', 'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/79001372_text'], ['KCUR: Kansas City\'s oldest jazz house', 'https://www.kcur.org/podcast/up-to-date/2022-04-28/kansas-citys-oldest-jazz-house-set-to-celebrate-105-years-of-making-music'], NRL],
  conf='mixed', brick='?', hours='?'),

N('paseo-ymca-kc', 'Paseo YMCA', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.09028, -94.56472, 'exact', 'view', 'drive', '', '1914',
  "The YMCA for Black Kansas Citians opened in 1914 after Julius Rosenwald urged the city to raise $80,000 toward it, and local architect Charles A. Smith designed it. In 1920 eight independent Black baseball team owners met here to form what became the Negro National League. "
  "The Y closed in the 1970s. The Negro Leagues Baseball Museum planned in 2006 to turn it into a research centre named for Buck O'Neil; that did not happen, and in May 2023 the museum renewed the plan, with an opening hoped for in 2028.",
  look="A large early-1900s city building on the 18th and Vine corner. It is a shut building waiting for its restoration, so the outside is what there is to see. Its materials were not checked.",
  accn="Owned by the museum organisation named above; closed and not open to visitors. View it from the sidewalk at 18th Street and The Paseo; the Negro Leagues Baseball Museum is a short walk away.",
  links=[W('Paseo YMCA'), NRL],
  brick='?'),

N('gillis-orphans-home-kc', "Gillis Orphans' Home", 'Kansas City', 'kcmo', 'inst', 'standing',
  39.08647, -94.56787, 'area', 'view', 'drive', '', '1900',
  "Funded by an inheritance given by Mary Ann Gillis and built by members of the YWCA in 1900 on 3.5 acres given by Thomas H. Swope, with $25,000 from the wife of S. B. Armour, it was first called the Children's Home. The Margaret Klock Armour Memorial Home went up next door in 1904. "
  "In the 1920s and 1930s the grounds grew to 26 acres. It was listed on the National Register on July 10, 2017.",
  look="A three-storey Georgian-style building on a T-shaped plan; a 2018 photograph on Wikimedia Commons shows red brick walls with a pedimented centre. Wikipedia gives no account of what survives inside, and its present use and condition were not checked.",
  accn="Not known to be open; look from the public street. Who owns it now was not checked.",
  links=[W("Gillis Orphans' Home"), ['Wikimedia Commons: Gillis Orphans\' Home KCMO.jpg', 'https://commons.wikimedia.org/wiki/File:Gillis_Orphans%27_Home_KCMO.jpg'], NRL],
  conf='mixed', brick='yes'),

N('fire-station-11-vine-kc', 'Fire Station No. 11 (Vine Street)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.08803, -94.56374, 'exact', 'view', 'drive', '', '1931',
  "For nearly 90 years this was the fire company that served Kansas City's Black community, a product of the city's segregated policy and a source of jobs and pride. The 1931 building replaced the 1812 Vine Street station, which came down in 1967. "
  "It is two storeys of reinforced concrete faced in Bethany Falls limestone, in Art Deco style with a stepped parapet and geometric limestone patterns. It stands beside the 1897 city workhouse castle, and now houses the Vine Street Studio for artists. It was listed on the Kansas City register in 2009 and on the National Register in 2026.",
  look="The limestone front with its stepped parapet and steel windows on the upper floor. The station's journals and photographs are kept at the Black Archives of Mid-America. Inside not checked.",
  accn="A working artists' studio building on Vine Street, next to the Workhouse Castle; look from the street. Any open days were not checked.",
  links=[W('Fire Station No. 11 (Kansas City, Missouri)')],
  brick='no'),

N('museum-of-kansas-city-corinthian-hall', 'Museum of Kansas City (Corinthian Hall)', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.11580, -94.54240, 'exact', 'open', 'drive', '', '1910',
  "Lumber baron Robert A. Long built Corinthian Hall in 1910 as his house, on the bluff over North Terrace Park (now Kessler Park). His daughters gave it to the Kansas City Museum Association in 1939 and the museum opened there on May 5, 1940. The city took it over in 1948. "
  "A long restoration began about 2015, and the museum's own page says the mansion is the only building on the property that is open to the public.",
  look="A grand 1910 mansion with an on-site soda fountain, a shop and the historic grounds. Admission is free according to the museum. What original woodwork survives was not checked here.",
  accn="Run by the city's museum at 3218 Gladstone Boulevard. Parking is free on Gladstone Boulevard and around the grounds on Indiana, Norledge and Walrond avenues, according to the museum. Hours as read November 2026 from the museum's page and a search result quoting it.",
  links=[W('Museum of Kansas City'), ['The Museum of Kansas City: plan your visit', 'https://museumofkansascity.org/plan-your-visit/'], NRL],
  brick='?', hours='Thursday 10 a.m. to 8 p.m.; Friday and Saturday 10 a.m. to 5 p.m.; Sunday noon to 5 p.m. Free.'),

N('william-chick-scarritt-house-kc', 'William Chick Scarritt House', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.11712, -94.54247, 'site', 'view', 'drive', '', '1888',
  "John Wellborn Root designed this Chateau-style house in 1888 for the lawyer William Chick Scarritt, a son of the Rev. Nathan Scarritt, who founded this part of the Northeast. Scarritt was police commissioner in 1896 and 1897. It served as a nursing home from the 1940s into the 2000s. "
  "It has limestone foundations, brownstone walls and a hip roof. It was renovated in 2012, caught fire on September 12, 2016, and was rebuilt in 2017 with help from neighbours. National Register 1976; Kansas City register 1983.",
  look="A two-storey stone mansion in the Scarritt Point neighbourhood; the 2016 fire and rebuild mean the roof and interior are new work. The pin is the Register coordinate and was checked against the aerial.",
  accn="Private; view from the street. The address on Wikipedia is 3240 Norledge Avenue, a few minutes' walk from the Museum of Kansas City.",
  links=[W('William Chick Scarritt House'), NRL],
  conf='mixed', brick='no'),

N('edward-lucky-scarritt-house-kc', 'Edward Lucky Scarritt House (Scarritt-Royster Residence)', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.11562, -94.54003, 'site', 'view', 'drive', '', '',
  "Edward Lucky Scarritt, the eldest son of the Rev. Nathan Scarritt, was born in 1853 near where he later lived; a 1902 book on the men who made Kansas City says so. The house at 3500 Gladstone Boulevard was added to the National Register on May 23, 1977, under the names Scarritt-Royster Residence. "
  "No year of building was found in a page that could be read, and the Register form is not online.",
  look="A house on the Gladstone Boulevard bluff, close to the Museum of Kansas City. Its materials and condition were not checked.",
  accn="Private; look from Gladstone Boulevard. Whether anyone lives in it now was not checked.",
  links=[['National Register entry (NRIS 77000809)', 'https://historypointer.com/nris/resource/77000809'], ['Men Who Made Kansas City: Edward Lucky Scarritt (1902)', 'https://www.vintagekansascity.com/menwhomadekc/scarritt_edward_lucky'], NRL],
  conf='mixed', brick='?'),

N('beth-shalom-synagogue-kc', 'Beth Shalom Synagogue (Victorious Life Church)', 'Kansas City', 'kcmo', 'worship', 'standing',
  39.06468, -94.56740, 'exact', 'view', 'drive', '', '1927',
  "Congregation Beth Shalom's Moorish-inspired temple at 34th Street and The Paseo went up in 1927. The congregation built a new temple in south Kansas City and left in the early 1970s; Victorious Life Church, a mostly African-American Pentecostal church founded in 1938, then moved in. "
  "KCUR says its members have kept the stained glass, ornamentation and Jewish symbols, and that the sanctuary is looked after much like a museum. Sources differ on the year the sale was made: one search result says 1969, KCUR says the early 1970s.",
  look="Moorish and Byzantine-style towers and the Jewish symbols still on the building, with stained glass inside. The church holds two services each Sunday per KCUR in 2016; times were not checked on its own page.",
  accn="An active church at 3400 The Paseo. Visit on a Sunday service or ask the church; the church's own page was not read, so hours are not given.",
  links=[['KCUR: Midtown temple became home to Pentecostals (2016)', 'https://www.kcur.org/community/2016-08-09/how-midtown-kansas-citys-ornate-jewish-temple-became-home-to-pentecostals'], ['Clio: Beth Shalom Synagogue', 'https://theclio.com/tour/2331/9'], NRL],
  conf='mixed', brick='?', hours='?'),

N('attucks-school-kc', 'Attucks School (Zhou B Art Center)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.09020, -94.56038, 'exact', 'view', 'drive', '', '1905',
  "Named for Crispus Attucks, this school in the 18th and Vine district was designed by Charles Smith and built in two stages, 1905 and 1922. Clio says it was a grade school into the 1960s and sat vacant for many years from the early 2000s. "
  "The first Attucks School began in 1880 in two rooms at 18th and Euclid, in a building now gone. Sources give other founding years; Clio cites a 1928 Kansas City Call article.",
  look="A large two-part school building near 19th Street and Woodland Avenue. Its present use as an art centre is from a Clio caption; its materials and any open days were not checked.",
  accn="At 1815 Woodland Avenue; look from the street. Hours were not checked.",
  links=[['Clio: Zhou B Art Center; Attucks School', 'https://www.theclio.com/tour/360/24'], NRL],
  conf='mixed', brick='?'),

N('heim-bottling-plant-kc', 'Ferd. Heim Brewing Company Bottling Plant', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.11986, -94.54895, 'exact', 'view', 'drive', '', '1901',
  "Finished in 1901, this two-storey bottling plant is the one building left of the Heim brewery, which became the largest brewery west of St. Louis; the National Register form says Prohibition in 1918 closed it. "
  "The form says the building is much as it was built, with a brick exterior and contrasting brick trim. It was vacant when the form was written, and in 2014 its south side was joined to a 1977 concrete warehouse.",
  look="Brick walls with contrasting brick detail and its original window pattern, standing on a stone foundation. Inside not checked.",
  accn="At 507 North Montgall Avenue in the East Bottoms; private and vacant when the form was written. View from the street.",
  links=[['National Register form (2015)', 'https://npgallery.nps.gov/GetAsset/d06aa64b-8741-4836-a08f-78870bbbcb06'], NRL],
  brick='yes'),

N('national-cloak-suit-kc', 'National Cloak and Suit Company Building', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.10462, -94.51803, 'site', 'view', 'drive', '', '1919–1920',
  "Built in 1919 and 1920 as a mail-order warehouse for the National Cloak and Suit Company, the New York firm that sold women's fashions by post. The form shows a 12-inch brick exterior with steel-framed factory windows, built for light and air. "
  "It later became part of the Hardesty Federal Complex. A developer has proposed turning it into apartments.",
  look="A huge brick factory with rows of industrial windows and a power house beside it, on Independence Avenue. Inside not checked.",
  accn="At 5401 Independence Avenue. Private; view from the street.",
  links=[['National Register form (2018)', 'https://npgallery.nps.gov/GetAsset/046dce28-a889-47e6-8fa0-7d775bea7e54'], ['Flatland: housing plan for the building', 'https://flatlandkc.org/news-issues/housing/developer-tackles-historic-building-for-120m-affordable-housing-project/'], NRL],
  brick='yes'),
]

PIN_NOTES = {
 'mutual-musicians-foundation-kc': 'Wikipedia and the Register give this point on the building at 18th and Highland.',
 'paseo-ymca-kc': 'Wikipedia infobox coordinate, checked on the aerial.',
 'gillis-orphans-home-kc': 'Register coordinate falls on the street; which building on the aerial is the home could not be settled, so the pin marks the area only.',
 'fire-station-11-vine-kc': 'Wikipedia infobox coordinate fell on the street; moved about 100 m north onto the building beside the Workhouse Castle, as the aerial shows.',
 'museum-of-kansas-city-corinthian-hall': 'Wikipedia infobox coordinate, checked on the aerial.',
 'william-chick-scarritt-house-kc': 'National Register list coordinate, checked on the aerial.',
 'edward-lucky-scarritt-house-kc': 'National Register list coordinate, checked on the aerial.',
 'beth-shalom-synagogue-kc': 'National Register list coordinate, checked on the aerial.',
 'attucks-school-kc': 'National Register list coordinate, checked on the aerial.',
 'heim-bottling-plant-kc': 'Register coordinate was at the building edge; moved about 20 m east onto it, as the aerial shows.',
 'national-cloak-suit-kc': 'Register coordinate fell on the street; moved about 65 m south onto the factory roof seen on the aerial.',
}
