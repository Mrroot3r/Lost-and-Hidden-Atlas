# Kansas City, Missouri: Midtown, Hyde Park, Sunset Hill and the east-of-Troost blocks, November 24, 2026.
# Part of filling in the Kansas City area on purpose for a local researcher. These are National Register listings the Atlas
# did not have. Facts come from the nomination forms (NPGallery text) and the Wikipedia list of Jackson County listings.
# (The Wikipedia list of Jackson County listings gave the coordinates and listing dates.) Each form was written between 2013 and 2021, so present use and ownership were not checked.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_hyde_bzkp', 'label': 'Kansas City: Midtown, Hyde Park and Sunset Hill', 'added': '2026-11-24 13:02'}

def F(ref, label='National Register nomination form'): return [label, 'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/%s_text' % ref]

PLACES = [
N('peters-house-sunset-hill-kc', 'Charles and Josephine Peters House, Sunset Hill, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.02919, -94.6068, 'site', 'view', 'drive', '', '1916',
  'A Colonial Revival mansion of 1916 at 1228 West 55th Street, built for Charles Peters of the Emery, Bird, Thayer department store. Henry Hoit designed it and Joe Hellman built it. It was remodelled in 1936 for Porter T. Hall, the store\'s president, and his wife Josephine Bird Hall, to plans by Hoit, Price and Barnes, which changed the front and some rooms. It stands on its original 3.23 acres.',
  look='A red brick house with a symmetrical front, many-paned windows with shutters, Tuscan columns and wrought iron balustrades, and a carriage house of 1916 in the grounds. The form says the wide lawn is still open to the street, so the house is seen from the road. Interior not checked.',
  accn='A private house. Look from the public street only. The owner and present use were not checked; the 2016 nomination form was the source. No parking was checked.',
  links=[F('16000085')], brick='yes'),

N('braley-house-sunset-hill-kc', 'Charles A. Braley House, Sunset Hill, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.02986, -94.60689, 'site', 'view', 'drive', '', '1919',
  'A three-storey mansion of 1919 at 3 Dunford Circle, built for Charles Braley, a lawyer and oil man. Henry Hoit designed it in the Jacobethan Revival style, a rare one in Kansas City, and the R. A. Long Construction Company built it. The form calls it one of Hoit\'s last houses before he joined Edwin Price and Alfred Barnes in a partnership.',
  look='Red brick and stone with gables, buttresses, tall chimneys and detailed stonework. The form says the back, facing State Line Road, is as notable as the front. The grounds have a curving drive from Dunford Circle. Interior not checked.',
  accn='A private house on a large lot on a cul-de-sac between Ward Parkway and State Line Road. Look from the public street only. The owner and present use were not checked; the 2013 nomination form was the source. No parking was checked.',
  links=[F('13000821')], brick='yes'),

N('michelson-building-troost-kc', 'Michelson Building, Troost Avenue, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.06974, -94.57106, 'site', 'view', 'drive', '', '1923',
  'A two-storey shop and office block of 1923 at 3125 to 3133 Troost Avenue, designed by William J. Koch and built by Patrick J. Morley for $60,000. The nomination form says it is one of Kansas City\'s earliest commercial buildings to mix classical Beaux Arts form with simple geometric ornament, a step toward Art Deco.',
  look='A terracotta front with a classical layout and geometric patterns; the sides are red brick. The shop fronts have been replaced, but the form notes original ceramic hex tile and terrazzo in some shop entrances. Interior not checked.',
  accn='Private commercial building on a public street. Look from the pavement; go in only where a business is open. The owner and present use were not checked; the 2018 nomination form was the source. Street parking was not checked.',
  links=[F('100002033')], brick='some'),

N('shankman-building-troost-kc', 'Shankman Building, Troost Avenue, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.07022, -94.57105, 'site', 'view', 'drive', '', '1929',
  'A three-storey Art Deco block of 1929 at 3115 to 3123 Troost Avenue, built for shops and a post office substation on the ground floor with offices above. The nomination form calls it an intact early example of Kansas City\'s ornamental Art Deco, the zigzag phase, and it stands beside the Michelson Building.',
  look='A front of terracotta with smooth vertical lines, bas-relief panels of stylised leaves and scrolls between the windows, and octagonal medallions on the parapet. The side and back walls are red brick on an exposed concrete frame. Interior not checked.',
  accn='Private commercial building on a public street. Look from the pavement. The owner and present use were not checked; the 2018 nomination form was the source. Street parking was not checked.',
  links=[F('100002035')], brick='some'),

N('luzier-laboratories-gillham-plaza-kc', 'Luzier Special Formula Laboratories Building, Gillham Plaza, Kansas City', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.06777, -94.57933, 'site', 'view', 'drive', '', '1927–1933',
  'A Spanish Colonial Revival factory at 3216 Gillham Plaza made of two buildings. The north one was designed in 1927 by Hoit, Price and Barnes for the Martha Washington Candy Company. The south one was designed in 1928 by Nelle E. Peters for Thomas Luzier\'s cosmetics firm, and a one-storey link joined them in 1933. The form says Luzier gave women work in sales and manufacturing, which was unusual then.',
  look='Two storeys of brick and coloured terracotta with Spanish Colonial Revival detail. At the time of the form one entry in the north bay was boarded up. Interior not checked.',
  accn='Private building on a public street. Look from the pavement. The owner and present use were not checked; the 2018 nomination form was the source. Street parking was not checked.',
  links=[F('100001351')], brick='no'),

N('first-swedish-baptist-church-kc', 'First Swedish Baptist Church, Washington Street, Kansas City', 'Kansas City', 'kcmo', 'worship', 'standing',
  39.0557, -94.59191, 'site', 'view', 'drive', '', '1920–1923',
  'A Gothic Revival church at 3931 Washington Street, designed in 1920 by Phillip Drotts, a member of the congregation, and built by Swan E. Johnson, also a member. The basement opened for services in 1921 and the sanctuary and upper floors were finished in 1923. The nomination form calls it the earliest surviving building that shows Swedish immigrants passing through Kansas City.',
  look='Limestone walls with large pointed-arch art glass windows, and Tudor Revival upper storeys at the west end in stone and stucco with false half-timbering. At the time of the form, rooms to the west served as offices and storage. Service times and whether visitors may go in were not found.',
  accn='A church on a street corner. Look from the public street. Who uses it now, and when it opens, was not checked; the 2018 nomination form was the source. No parking was checked.',
  links=[F('100002425')], brick='no'),

N('acme-cleansing-company-kc', 'ACME Cleansing Company Building, Gillham Road, Kansas City', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.06851, -94.57817, 'site', 'view', 'drive', '', '1925',
  'A two-storey cleaning plant of 1925 at 3200 Gillham Road, built to clean household clothes and upholstery. Its U-shaped plan wraps around three sides of an odd-shaped lot with the entrance on the corner of Gillham Road and Linwood Boulevard. A garage was added in 1936.',
  look='Buff brick with terracotta trim, quoins topped by twisted colonettes, and limestone at the basement level. The form says the windows were boarded with plywood for security at the time it was written; the openings were still there. Interior not checked.',
  accn='Private building at a street corner. Look from the pavement. The owner and present use were not checked; the nomination form (about 2017) was the source. Street parking was not checked.',
  links=[F('100001346')], brick='no'),

N('gotham-apartments-linwood-kc', 'Gotham Apartments, Linwood Boulevard, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.0682, -94.5509, 'site', 'view', 'drive', '', '1919',
  'A four-storey brick apartment building of 1919 at 2718 Linwood Boulevard, designed by Greenebaum and Hardy in an H shape. Four three-storey classical columns hold up a deep entablature over a recessed porch. It is one of the "colonnade apartments" Kansas City built in the early 1900s. By the late 1950s about a quarter of the flats stood empty.',
  look='The big columned porch on Linwood Boulevard, with classical ornament at the door and a balustrade and parapet above. The north back wall is red brick. Interior not checked.',
  accn='A private apartment building when its form was written. Look from the public street. The owner and present use were not checked. No parking was checked.',
  links=[F('100001349')], brick='yes'),

N('aurora-apartments-linwood-kc', 'Aurora Apartments, Linwood Boulevard, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.06822, -94.54764, 'site', 'view', 'drive', '', '1925',
  'A modest two-storey apartment house of 1925 at 3012 to 3014 Linwood Boulevard, designed and built by Leon Ludwig. It has ten flats. The form says it is a good example of the ordinary walk-up apartment building that many Kansas City workers and middle-class families lived in, now increasingly rare.',
  look='Red brick over concrete block, a two-storey recessed porch with stone columns, pointed parapets with stone coping and stone beams that stick out like vigas. Interior not checked.',
  accn='A private apartment building. Look from the public street. The owner and present use were not checked; the 2017 nomination form was the source. No parking was checked.',
  links=[F('100001758')], brick='yes'),

N('swinney-school-kc', 'E. F. Swinney School (Open Air school), Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.04286, -94.6001, 'site', 'view', 'drive', '', '1914–1927',
  'A school at 1106 West 47th Street, just west of the Country Club Plaza. The east wing and centre were built in 1914 to plans by the school district\'s architect, Charles A. Smith, and a west wing followed in 1927. The nomination form calls it a rare survivor of the "open air" school, built so classrooms had fresh air, and the only one in the district that keeps its pergola.',
  look='Tapestry brick walls with terracotta ornament in the Sullivan manner. The form says the pergola railing can still be seen, and that a concrete tower added in 1987 was taken off in April 2013, showing the old brick entrance. The form says the inside is highly intact. It is a school: look from the street.',
  accn='A school on a hill in a residential area. Look from the public street. Whether it is still used as a school was not checked; the 2013 nomination form was the source. No parking was checked.',
  links=[F('13000838')], brick='yes'),

N('norman-school-kc', 'Norman School, Valentine neighborhood, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.06403, -94.5942, 'site', 'view', 'drive', '', '1906–1911',
  'A limestone school at 3514 Jefferson Street. A wooden school opened on the site in November 1901, named for the school superintendent Joseph Lafayette Norman. The present building went up in two planned stages, 1906 and 1911, designed by Charles A. Smith. It served as a school and later housed a "Parents as Teachers" programme until 2006. The form says a private developer bought it in 2009 and it was still empty.',
  look='Rusticated limestone blocks with dressed limestone trim, beige brick chimneys and terracotta details. The form says the stone walls, wide corridors and fire-safe design are largely intact. Interior not checked and the building was not open to visitors.',
  accn='Private property when the 2013 form was written, standing empty. Look from the public street only. Its present state was not checked. No parking was checked.',
  links=[F('13001087')], brick='no'),

N('spofford-home-for-children-kc', 'Thomas M. Spofford Receiving Home for Children, Kansas City', 'Kansas City', 'kcmo', 'inst', 'standing',
  39.02571, -94.54074, 'site', 'view', 'drive', '', '1934–1956',
  'A Colonial Revival children\'s home at 5501 Cleveland Avenue. The Spofford Home began in 1916 under an agreement between Jackson County and the Institutional Methodist-Episcopal Church, and this was its second site. The west and centre parts were built in 1934, the east addition in 1956 and the swimming pool in 1965. The 2016 form says it was unoccupied and in fair condition.',
  look='A two-storey I-shaped building in red brick with a side-gable roof and a centred porch. The form says it has been changed very little. A large worn car park lies to the south. Interior not checked.',
  accn='Private property when the 2016 form was written, empty. Look from the public street only. Its present state was not checked. No parking was checked.',
  links=[F('16000545')], brick='yes'),

N('interstate-bakeries-headquarters-kc', 'Interstate Bakeries Corporation Headquarters, Armour Boulevard, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.06434, -94.58489, 'site', 'view', 'drive', '', '1952–1961',
  'A modern two-storey office building at 12 East Armour Boulevard, the headquarters of the Interstate Bakeries Corporation. The south wing was built in 1952 and an L-shaped north wing in 1961, joined by a courtyard facing west. The nomination form lists it as vacant in 2015 and says the company\'s bread-wrapper and baking ideas made it a national player.',
  look='A concrete frame clad in orange variegated brick with concrete and cut stone trim, ribbon windows and precast concrete awnings; a stone retaining wall and wide steps front the street. Interior not checked.',
  accn='Private commercial property, vacant at the time of the 2015 form. Look from Armour Boulevard. Its present state was not checked. No parking was checked.',
  links=[F('15000553')], brick='?'),

N('ladd-school-kc', 'Sanford B. Ladd School, Benton Boulevard, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.0593, -94.54722, 'site', 'view', 'drive', '', '1912–1922',
  'A two-storey elementary school at 3640 Benton Boulevard, built in 1912 with a second main stage in 1922 and a small wing about 1990. The nomination form calls it an excellent example of a Progressive Era school and says its red brick and cream terracotta give it Jacobethan details.',
  look='Red brick walls with brown brick bands and cream terracotta, shaped parapets, keystones and capitals. The form lists a raised basement and an L-shaped plan. Interior not checked.',
  accn='A school. Look from the public street. Whether it is still used as a school was not checked; the 2021 nomination form was the source. No parking was checked.',
  links=[F('100006918')], brick='yes'),

N('st-francis-xavier-school-kc', 'St. Francis Xavier School, Troost Avenue, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.0316, -94.57391, 'site', 'view', 'drive', '', '1962',
  'A Catholic school at 5220 Troost Avenue, designed in 1962 by the local firm Shaughnessy, Bower and Grimaldi in the International Style. Three wings are linked by corridors and every classroom opens to the outside. The nomination form lists it as a good example of a modern-era school and says it was built in a "finger plan".',
  look='Low, wide shapes under flat roofs, with walls of stacked brown and buff brick, concrete block and large-pebble concrete panels, and bands of aluminium windows. An enclosed courtyard lies on the east side. Interior not checked.',
  accn='A school beside the Catholic church on Troost. Look from the public street. Whether it still teaches was not checked; the 2017 nomination form was the source. No parking was checked.',
  links=[F('100001760')], brick='no'),
]

PIN_NOTES = {
  'peters-house-sunset-hill-kc': 'The address point from the ArcGIS address lookup, which falls on the building on the aerial. The Register list point was off the building.',
  'braley-house-sunset-hill-kc': 'The address point from the ArcGIS address lookup, which falls on the building on the aerial. The Register list point was off the building.',
  'michelson-building-troost-kc': 'Moved from the Register list point to the building on the aerial; the address lookup alone fell on the wrong side of the street or on a neighbour.',
  'shankman-building-troost-kc': 'Moved from the Register list point to the building on the aerial; the address lookup alone fell on the wrong side of the street or on a neighbour.',
  'luzier-laboratories-gillham-plaza-kc': 'The address point from the ArcGIS address lookup, which falls on the building on the aerial. The Register list point was off the building.',
  'first-swedish-baptist-church-kc': 'Moved from the Register list point to the building on the aerial; the address lookup alone fell on the wrong side of the street or on a neighbour.',
  'acme-cleansing-company-kc': 'The address point from the ArcGIS address lookup, which falls on the building on the aerial. The Register list point was off the building.',
  'gotham-apartments-linwood-kc': 'The Register list point for 2718 Linwood Boulevard; checked on the aerial.',
  'aurora-apartments-linwood-kc': 'The address point from the ArcGIS address lookup, which falls on the building on the aerial. The Register list point was off the building.',
  'swinney-school-kc': 'The address point from the ArcGIS address lookup, which falls on the building on the aerial. The Register list point was off the building.',
  'norman-school-kc': 'The address point from the ArcGIS address lookup, which falls on the building on the aerial. The Register list point was off the building.',
  'spofford-home-for-children-kc': 'The address point from the ArcGIS address lookup, which falls on the building on the aerial. The Register list point was off the building.',
  'interstate-bakeries-headquarters-kc': 'The address point from the ArcGIS address lookup, which falls on the building on the aerial. The Register list point was off the building.',
  'ladd-school-kc': 'The address point from the ArcGIS address lookup, which falls on the building on the aerial. The Register list point was off the building.',
  'st-francis-xavier-school-kc': 'The address point from the ArcGIS address lookup, which falls on the building on the aerial. The Register list point was off the building.',
}
