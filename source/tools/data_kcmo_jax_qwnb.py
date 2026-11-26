# November 26, 2026: eleven more National Register listings in Jackson County, Missouri (Kansas City, Independence and
# Lee's Summit). Sources: the Park Service's record for each listing and the registration form, read from the
# Missouri State Historic Preservation Office's copy. Listings that are modernist, pulled down or already on the Atlas
# were left out.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_jax_qwnb', 'label': 'Jackson County, Missouri: eleven more Register listings', 'added': '2026-11-26 18:55'}

def NPS(n): return ['National Register record', 'https://npgallery.nps.gov/AssetDetail/NRIS/' + n]
def FORM(t, f): return [t + ': National Register form (Missouri State Historic Preservation Office copy)', 'https://mostateparks.com/sites/g/files/zuston361/files/media/pdf/2025/02/' + f + '.pdf']

PLACES = [
N('smallwood-noland-house-independence-mo', 'Smallwood V. Noland House, Independence', 'Independence', 'kcmo', 'landmark', 'standing',
  39.08164, -94.43729, 'site', 'view', 'drive', '', '1845–1854',
  'A brick I-house built between about 1845 and 1854 for Smallwood Noland, who traded on the Santa Fe Trail from about 1845 until 1854 and also owned a hotel in Independence that served travellers on the Santa Fe and Oregon-California trails until he died in 1858. The 1994 Register listing calls it a good example of the house a successful Santa Fe merchant built in Independence in the 1840s and 1850s.',
  look='Brick laid in seven-course common bond on a brick foundation, Greek Revival in style, with a gable roof. Later additions to the back wing made its T plan rectangular, and the original porch was closed in about 1900. Inside was not checked.',
  accn='Private property at 1024 South Forest Street on the west side of the street; look from the public sidewalk. Parking and whether anyone may go in were not checked. The pin is the Register point for the address and was not looked at on the ground.',
  links=[NPS('94000319'), FORM('Noland House', 'noland-smallwood-v-house')], brick='?', conf='mixed'),

N('nettleton-home-swope-parkway-kc', 'George H. Nettleton Home, Swope Parkway, Kansas City', 'Kansas City', 'kcmo', 'inst', 'standing',
  39.03300, -94.54189, 'area', 'view', 'drive', '', '1915',
  'A home for homeless and aged women and girls, begun by the Women\'s Christian Temperance Union in Kansas City in 1890 and moved to this H-shaped building on Swope Parkway in 1915. Wilder and Wight designed it, and Wight and Wight finished the work. It went on caring for women until it closed in 1999, the year it was listed on the National Register.',
  look='A two-storey Colonial Revival building with a four-column portico, white stone quoins and keystone lintels over eight-over-one windows, and green slate on the roof. The brick is a rug-faced "tapestry" brick in shades of red and reddish-brown, laid in Flemish bond. When the form was written the building was boarded up and empty. A photograph taken in 2015 shows it with tidy lawns and its red brick and white porches in good order, so it has been taken in hand since; what it is used for now was not checked.',
  accn='Private property at 5125 Swope Parkway when last recorded; look from the public side. Who owns it now, whether it has been reused and where to park were not checked.',
  links=[NPS('99001253'), FORM('Nettleton Home', 'nettleton-george-h-home')], brick='yes', conf='mixed'),

N('acme-brass-machine-works-kc', 'Acme Brass and Machine Works Building, East 17th Street, Kansas City', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.09297, -94.57608, 'site', 'view', 'walk', '', '1922',
  'A small two-storey factory of 1922 at 609 to 611 East 17th Street, designed by S. W. Hitt, for the Acme Brass and Machine Works (also called Acme Pattern and Model Works). It stands in a secondary industrial district about a mile south of downtown, half a mile from the Crossroads freight district. The form uses it as an example of a two-part commercial block adapted for industry.',
  look='Red brick laid in common bond on a concrete foundation, with textured reddish-brown brick on the north front rising to a stepped parapet. The only ornament is brickwork in header and soldier courses framing the windows, a sign panel and a belt course. Inside was not checked.',
  accn='Private; look from East 17th Street. A studio company owned it when the form was written in 2004. Present use, parking and whether the public may go in were not checked.',
  links=[NPS('04000694'), FORM('Acme Brass', 'acme-brass-and-machine-works-building')], brick='yes', conf='mixed'),

N('vaccaro-soda-water-building-kc', 'Joe Vaccaro Soda Water Manufacturing Company Building, North End, Kansas City', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.11061, -94.57248, 'site', 'view', 'walk', '', '1921–1923',
  'A two-storey soda-water factory and shop at 918 to 922 East 5th Street, built from 1921 to 1923 in the Italian-American North End. The Register form calls it one of the best surviving examples in Kansas City of an immigrant community building through its own business and social investment. A penthouse was added in 1928.',
  look='Grooved orange-brown face brick on the south and east fronts, with limestone trim: the coping, round windows, a sign panel and a belt course. The roof is hidden behind a shaped parapet. The form says the exterior is little altered. Inside was not checked.',
  accn='Private; look from East 5th Street or Harrison Street. Present use, parking and whether the public may go in were not checked.',
  links=[NPS('03001055'), FORM('Vaccaro Building', 'vaccaro-joe-soda-water-manufacturing-co-building')], brick='some', conf='mixed'),

N('barclay-building-broadway-kc', 'Barclay Building, Broadway Boulevard, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.06122, -94.59009, 'site', 'view', 'walk', '', '1924',
  'A two-storey shop building at 3613 to 3623 Broadway, designed in 1924 by the Kansas City architect Robert F. Gornall and built by Edelman-Fleming Construction Company. The form says it helped move shopping out of the downtown department stores into one neighbourhood strip, and that its large second-floor display windows were unusual.',
  look='The front is clad in terra cotta in a Beaux-Arts design, with a full entablature, dentils and decorative panels at the corners, under a green clay-tile roof. Gornall designed neighbouring buildings of the same date to the north. Inside was not checked.',
  accn='Shops on a city street; look from the sidewalk. Which shops are open, and when, was not checked; the form was written in 2006. Street parking, not checked.',
  links=[NPS('07000042'), FORM('Barclay Building', 'barclay-building')], brick='no', conf='mixed'),

N('bancroft-school-kc', 'Bancroft School, Tracy Avenue, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.04833, -94.57064, 'site', 'view', 'drive', '', '1909–1922',
  'A two-storey public school on a hill at 4300 Tracy Avenue, built in three stages: the centre and south wing in 1909 and the north wing in 1913, both designed by Charles A. Smith, architect for the school board, and a south addition in 1922. All three keep the same front and materials.',
  look='Classical Revival with two-storey brick pilasters, a diamond pattern in brick and arched stone ornament at the parapet, on a rusticated limestone base with terra cotta trim. The form says many original interior features survive: the corridors and classrooms, and the wood doors and trim. The windows have been replaced. Whether visitors may go in was not checked.',
  accn='The form describes a school at 4300 Tracy Avenue in a quiet residential area. Present use, ownership and parking were not checked; look from the public streets.',
  links=[NPS('11001017'), FORM('Bancroft School', 'bancroft-school')], brick='?', conf='mixed'),

N('seven-oaks-school-kc', 'Seven Oaks School, Jackson Avenue, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.05803, -94.53450, 'site', 'view', 'drive', '', '1926–1927',
  'A two-storey school at 3711 Jackson Avenue, on a hill at the corner of Seven Oaks Park, built in 1926 and 1927 and designed by Charles A. Smith, architect for the Kansas City school district. It was listed on the National Register in 2012.',
  look='Buff brick with glazed terra cotta trim in a plain Spanish Colonial Revival style, on a limestone base. The form says the corridors, gym and auditorium are substantially intact and most classrooms keep their layout and finishes. Whether visitors may go in was not checked.',
  accn='Look from Jackson Avenue and from the park, which lies south and east of the school. The school\'s present use, ownership and parking were not checked.',
  links=[NPS('12000847'), FORM('Seven Oaks School', 'seven-oaks-school')], brick='no', conf='mixed'),

N('abc-storage-van-company-kc', 'A.B.C. Storage and Van Company Building, East 8th Street, Kansas City', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.10377, -94.57017, 'area', 'view', 'walk', '', '1908–1911',
  'A four-storey fireproof warehouse at 1015 East 8th Street, built in 1908 with an addition in 1911. The form calls it a good early example of the fireproof storage warehouse, and ties it to the A.B.C. Storage and Van Company, whose moving and storage business in Kansas City led to the later founding of Allied Van Lines.',
  look='Reinforced concrete frame faced in brick, with terra cotta moulding over the ground-floor bays; when the form was written some storefront transoms were covered in plywood. Inside was not checked.',
  accn='Private; look from East 8th Street on the east edge of downtown. Present use and parking were not checked.',
  links=[NPS('06001334'), FORM('A.B.C. Storage and Van', 'abc-storage-van-co-building')], brick='?', conf='mixed'),

N('st-teresas-academy-music-arts-building-kc', "St. Teresa's Academy Music and Arts Building, Main Street, Kansas City", 'Kansas City', 'kcmo', 'civic', 'standing',
  39.02628, -94.58900, 'site', 'view', 'drive', '', '1909',
  "Built in 1909 on the campus of St. Teresa's Academy at 5600 Main Street and designed by Wilder and Wight, masters of the Neo-Classical style in Kansas City. The Sisters had electricity run to the building before it was finished. The form says the outside has changed little.",
  look='Red brick walls over a steel frame, with four colossal brick pilasters on the east front and a pilaster at each corner. An art-glass skylight dome and its frame are under a metal covering put on in 1988. The lamp posts by the east door are Art Deco, of about 1945. Inside was not checked.',
  accn="An active school campus; look from Main Street. Whether visitors may go in, and where to park, were not checked.",
  links=[NPS('00001375'), FORM("St. Teresa's Academy", 'st-teresas-academy-music-and-arts-building')], brick='yes', conf='mixed'),

N('park-lane-apartments-kc', 'Park Lane Apartments, J. C. Nichols Parkway, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.04385, -94.58893, 'site', 'view', 'walk', '', '1925–1926',
  'A six-storey apartment building at 4600 to 4606 J. C. Nichols Parkway, built in 1925 and 1926 by Collins Brothers to a design by the New York firm of George B. Post and Sons. J. C. Nichols planned apartment blocks on three sides of the Country Club Plaza, and this one sits beside Mill Creek Park.',
  look='A reinforced concrete and steel frame with a brick and stone exterior and Mission-style details that echo the Plaza. The form (written about 2004) calls it in excellent condition with most historic features kept. The inside was not checked.',
  accn='Private apartments; look from the sidewalk. The pin is the Register point. Parking was not checked.',
  links=[NPS('04000387'), FORM('Park Lane Apartments', 'park-lane-apartments')], brick='?', conf='mixed'),

N('tocoma-netherlands-hotel-kc', 'The Tocoma (Netherlands Hotel), Main Street, Kansas City', 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.05700, -94.58587, 'site', 'view', 'walk', '', '1927–1928',
  'An apartment hotel at 3835 Main Street begun in June 1927 as the Tocoma and later called the Netherlands. Robert F. Gornall designed it in a Spanish Revival style with baroque and Moorish touches, as a follow-on to his Uptown Theatre of 1926. By its 1982 listing it was being turned into the Hawthorn Plaza Apartments for elderly residents.',
  look='A stucco-finished Spanish Revival front facing Main Street. The form says the lobby light fittings were taken out about 1955, the stucco was later sprayed with a synthetic finish, and oak wainscoting was added. Its condition now was not checked.',
  accn='Apartments when last recorded; look from Main Street. Whether the public may go in and where to park were not checked.',
  links=[NPS('79003782'), FORM('The Tocoma', 'tocoma')], brick='no', conf='mixed'),
]

PIN_NOTES = {
 'smallwood-noland-house-independence-mo': 'Address lookup (ArcGIS) for 1024 South Forest Street.',
 'nettleton-home-swope-parkway-kc': 'Address lookup (ArcGIS) for 5125 Swope Parkway. On the aerial the pin falls among several large buildings and the Home could not be picked out, so it marks the address only.',
 'acme-brass-machine-works-kc': 'Address lookup (ArcGIS) for 609 East 17th Street.',
 'vaccaro-soda-water-building-kc': 'Address lookup (ArcGIS) for 922 East 5th Street.',
 'barclay-building-broadway-kc': 'Address lookup (ArcGIS) for 3613 Broadway.',
 'bancroft-school-kc': 'Address lookup (ArcGIS) for 4300 Tracy Avenue.',
 'seven-oaks-school-kc': 'Address lookup (ArcGIS) for 3711 Jackson Avenue.',
 'abc-storage-van-company-kc': 'Address lookup (ArcGIS) for 1015 East 8th Street. The pin falls on a small flat-roofed building; the four-storey warehouse could not be picked out on the aerial, so it marks the address only.',
 'st-teresas-academy-music-arts-building-kc': 'Address lookup (ArcGIS) for 5600 Main Street.',
 'park-lane-apartments-kc': 'Address lookup (ArcGIS) for 4600 J. C. Nichols Parkway.',
 'tocoma-netherlands-hotel-kc': 'Address lookup (ArcGIS) for 3835 Main Street.',
}
