# November 25, 2026: Lexington's remaining Register houses, and a Liberty historic district.
# Facts come only from sources opened in this session: Wikipedia read as raw text, the Clio entry for the O'Bannon Homestead,
# and web search results that quote National Park Service listing addresses. National Register forms could not be read.
from data_b import N
from data_ma import W

LNR = ['Missouri State Parks: Lafayette County National Register listings', 'https://mostateparks.com/basic-page/missouri-national-register-listings/Lafayette']
PRIV = 'A private house; no public access is described in any source read, so look from the public road and do not go onto the property. '

BATCH = {'key': 'mo_hvxk', 'label': 'Lexington houses, Garden City and Liberty, Missouri', 'added': '2026-11-25 12:51'}

PLACES = [
N('gosewisch-house-lexington-mo', 'Theodore Gosewisch House (Fuenfhausen Residence)', 'Lexington', 'kcmo', 'landmark', 'standing',
  39.15778, -93.89167, 'area', 'view', 'drive', '', '1847',
  'A two-story Greek Revival brick house of about 1847 near Lexington, with a central hall and a two-story rear ell. A Victorian front porch was added in the early 1900s. It was listed on the National Register of Historic Places in 1997.',
  look='A brick I-house with a one-story Victorian porch on the front and an open shed-roofed porch on the back ell. Interior not checked.',
  accn=PRIV + 'A web search result quoting the Park Service listing puts it about a mile west of the junction of Highway 13 and Marshall School Road. The pin is the Wikipedia coordinate for the house, not checked on the ground. Owner not checked.',
  links=[W('Theodore Gosewisch House'), LNR], conf='mixed', brick='?'),

N('catron-house-lexington-mo', 'Minatree Catron House (Minatree Acres)', 'Lexington', 'kcmo', 'landmark', 'standing',
  39.18028, -93.79861, 'area', 'view', 'drive', '', '1843',
  'A Greek Revival brick house of about 1843 near Lexington, two stories with a central hall and a one-story rear ell. A two-story pedimented portico on square brick columns marks the front. It was listed on the National Register in 1997.',
  look='The two-story portico with square brick columns is the part to look for from the road. Interior not checked.',
  accn=PRIV + 'The pin is the Wikipedia coordinate, which lies in open country east of the town; the address is not published and the pin was not checked on the ground. Owner not checked.',
  links=[W('Minatree Catron House'), LNR], conf='mixed', brick='?'),

N('tevis-house-lexington-mo', 'D. W. B. and Julia Waddell Tevis House', 'Lexington', 'kcmo', 'landmark', 'standing',
  39.17861, -93.87861, 'area', 'view', 'drive', '', '1868',
  'An Italianate brick house of about 1868 in Lexington, two stories on a cruciform plan, with a roofline of heavy modillions and two Queen Anne porches. A small frame outbuilding on the lot is part of the listing. It was listed on the National Register in 1993 among Lexington\'s older houses.',
  look='Heavy brackets under the roof and two Queen Anne porches on the front. Interior not checked.',
  accn=PRIV + 'A web search result quoting the Park Service listing gives the address as South 13th Street. Park on the street.',
  links=[W('D. W. B. and Julia Waddell Tevis House'), LNR], conf='mixed', brick='?'),

N('cheatham-house-lexington-mo', 'John E. Cheatham House', 'Lexington', 'kcmo', 'landmark', 'standing',
  39.1725, -93.87917, 'site', 'view', 'drive', '', '1868',
  'An Italianate brick house of about 1868 in Lexington, two stories under a low metal-covered hipped roof with a bracketed cornice. A one-story kitchen was added about 1880, and a brick root cellar on the lot is part of the listing. It was listed on the National Register in 1993.',
  look='The bracketed cornice and hipped roof; the brick root cellar is behind the house. Interior not checked.',
  accn=PRIV + 'A web search result quoting the Park Service listing puts it on Highway 13 (the road south out of Lexington). Look from the road shoulder only where it is safe.',
  links=[W('John E. Cheatham House'), LNR], conf='mixed', brick='?'),

N('spratt-allen-aull-house-lexington-mo', 'Spratt-Allen-Aull House', 'Lexington', 'kcmo', 'landmark', 'standing',
  39.175, -93.86583, 'site', 'view', 'drive', '', '1840',
  'A Greek Revival house of red brick built about 1840 in Lexington. Its front has a tall pedimented four-column portico with an upper deck across the whole facade. An octagonal two-story frame ice house stands on the grounds and is part of the listing. It was listed on the National Register in 1993. An earlier Aull house nearby, also listed, is recorded as no longer standing.',
  look='The portico with its upper deck; the eight-sided frame ice house is an uncommon survivor. Interior not checked.',
  accn=PRIV + 'A web search result quoting the Park Service listing gives the address as Aull Lane. Owner not checked.',
  links=[W('Spratt-Allen-Aull House'), LNR], conf='mixed', brick='yes'),

N('stramcke-house-the-cedars-lexington-mo', 'Stramcke House (The Cedars)', 'Lexington', 'kcmo', 'landmark', 'standing',
  39.14, -93.8825, 'area', 'view', 'drive', '', '1887',
  'A Queen Anne frame house of about 1887 in the Lexington area, known as The Cedars, with a round three-story tower under a conical roof, a wraparound porch with Eastlake supports and spindlework, and ornamented gables. It was listed on the National Register in 1999.',
  look='The round tower and the spindlework porch. Interior not checked.',
  accn=PRIV + 'A web search result quoting the Park Service listing gives the address as Highway O, south of town. The pin is the Wikipedia coordinate, rounded to two decimals, so it may be some way off the house.',
  links=[W('Thomas Talbot and Rebecca Walton Smithers Stramcke House'), LNR], conf='mixed', brick='no'),

N('arthur-leonard-district-liberty-mo', 'Arthur–Leonard Historic District', 'Liberty', 'kcmo', 'town', 'standing',
  39.24472, -94.41556, 'area', 'public', 'drive', '', '1868–1946',
  'A residential part of Liberty, Missouri, with 36 buildings that count toward its National Register listing of 2001. It grew between about 1868 and 1946 and holds Greek Revival, Queen Anne, Prairie School and bungalow houses.',
  look='Walk or drive the streets and look at the houses from the sidewalk; the district is a mix of styles from the 1860s to the 1940s rather than one landmark. The Register summary does not name the streets or the best houses.',
  accn='Ordinary city streets (public right of way, owned by the city of Liberty; the Register summary does not say otherwise) with private houses along them; look from the sidewalk and keep off private lots. The district\'s street boundaries were not read, so the pin is the Wikipedia coordinate for it. Park on the street.',
  links=[W('Arthur–Leonard Historic District')], conf='mixed', brick='?'),
]

PIN_NOTES = {
 'gosewisch-house-lexington-mo': 'Wikipedia coordinate for the house; the address is not published.',
 'catron-house-lexington-mo': 'Wikipedia coordinate for the house; the address is not published.',
 'tevis-house-lexington-mo': 'Wikipedia coordinate for the house; on the aerial the pin falls on the road, with several older houses within a block, so the house itself was not picked out.',
 'cheatham-house-lexington-mo': 'Wikipedia coordinate for the house.',
 'spratt-allen-aull-house-lexington-mo': 'Wikipedia coordinate for the house.',
 'stramcke-house-the-cedars-lexington-mo': 'Wikipedia coordinate for the house, given to two decimals.',
 'arthur-leonard-district-liberty-mo': 'Wikipedia coordinate for the district; its outline was not read. On the aerial the pin falls on a busy intersection with shops, and the houses lie to the south and east, so it marks the general area only.',
}
