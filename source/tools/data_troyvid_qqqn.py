# November 26, 2026: buildings named in an Old World Exploration video about Troy, New York (region troy), checked
# one by one against sources. Most of the buildings it names were already on the Atlas; these four were not.
# Sources: the National Register form for the Central Troy Historic District boundary increase (16000367, NPGallery),
# the Rensselaer Polytechnic Institute archives' building history, Wikipedia's list of RPI buildings, a Times Union
# article (August 4, 2009) and an Evangelist article on the St. Francis de Sales sale.
from data_b import N
from data_ma import W

CTHD = ['National Register form: Central Troy Historic District boundary increase (PDF)',
        'https://npgallery.nps.gov/GetAsset/71d78e40-4df4-4d96-95d4-791ef968fa3f']

BATCH = {'key': 'troyvid_qqqn', 'label': 'Troy, New York (from a video)', 'added': '2026-11-26 20:32'}

PLACES = [
N('caldwell-apartments-troy', 'The Caldwell (Caldwell Apartments)', 'Troy', 'troy', 'landmark', 'standing',
  42.73049, -73.69235, 'exact', 'view', 'drive', '', '1907',
  'A six-storey corner apartment house at State and Second streets, built in 1907 to the design of the architect '
  'J. W. Woollett, in an Arts and Crafts manner. Clearing its site meant moving a house of about 1814, which now '
  'stands a few doors away at 12 State Street. It is one of the buildings of the Central Troy Historic District.',
  'Fifteen bays along State Street and three on Second. The walls are a pale brick over a first storey of cast '
  'stone with a pared-down egg-and-dart moulding; look for the bay windows on the second and fifth bays and at the '
  'sixth floor, the raised brick panels at the second storey and the heavily bracketed metal cornice. The 1814 house '
  'it displaced is at 12 State Street. Private apartments: interior not checked.',
  '', 'Private apartment building at 17 State Street, at the corner of Second Street; see it from the sidewalk. '
  'Street parking downtown.',
  [CTHD], brick='no'),

N('quackenbush-building-troy', 'Quackenbush Building', 'Troy', 'troy', 'civic', 'standing',
  42.73107, -73.68994, 'site', 'view', 'drive', '', '1857',
  'A four-storey commercial building of 1857 at Third Street and Broadway, designed by Henry Dudley in the '
  'Italianate style. A mansard roof of patterned slate with heavy pedimented dormers was '
  'added later in the nineteenth century, and the storefronts, much altered in the late twentieth century, were '
  'rebuilt in a more fitting design between 2014 and 2016.',
  'A stuccoed front on both Third Street and Broadway. In the middle of the Third Street side a slightly projecting '
  'bay holds three two-storey pairs of arched windows with crested cast-iron frames and sills; above are a bracketed '
  'cornice and the patterned slate mansard. A large addition runs to the south. Interior not checked.',
  '', 'Private commercial building at 30 Third Street, at the corner of Broadway; see it from the sidewalk. '
  'Street parking downtown.',
  [CTHD], brick='no'),

N('pittsburgh-building-rpi-troy', 'Pittsburgh Building (Lally School of Management), RPI', 'Troy', 'troy', 'inst',
  'standing', 42.73103, -73.68314, 'exact', 'view', 'drive', '', '1909–1912',
  'Rensselaer Polytechnic Institute\'s administration building, paid for by its Pittsburgh alumni, who pledged '
  '$125,000 in 1909; W. G. Wilkins, one of them, designed it without charge. It was dedicated on June 13, 1911 and '
  'finished in February 1912. Built into the hillside, it held the library, the trustees\' room, the president\'s '
  'and registrar\'s offices, a geology museum and a 100-by-64-foot hall. After a renovation in 1998 it became the '
  'home of the Lally School of Management.',
  'Walls of Harvard brick with Indiana limestone. Because of the slope the main entrance is on the third floor. '
  'Interior not checked.',
  '', 'Rensselaer Polytechnic Institute campus, on 8th Street; see it from the street and '
  'the campus walks. Visitor parking on campus is under the Institute\'s rules (not checked); street parking nearby.',
  [['RPI Institute Archives: Pittsburgh Building',
    'https://archives.rpi.edu/institute-history/building-histories/pittsburgh-building'], W('List of RPI buildings')],
  brick='?'),

N('st-francis-de-sales-church-troy', 'Former St. Francis de Sales Church', 'Troy', 'troy', 'worship', 'standing',
  42.72417, -73.68161, 'exact', 'view', 'drive', '', '',
  'A Roman Catholic church on Congress Street beside the entrance to Prospect Park. Its parish closed on '
  'February 1, 2009, one of several Catholic churches in Troy closed about then, and the Diocese of Albany agreed '
  'that year to sell the church and its rectory to the RPI chapter of the Phi Sigma Kappa fraternity, which planned '
  'to live in the rectory and use the church for meals, meetings and community events. The year it was built was '
  'not confirmed from a source that could be opened.',
  'The church and the rectory beside it, seen from Congress Street. Interior not checked.',
  '', 'Private (a fraternity property since the sale) at 320 Congress Street, by the Prospect Park entrance; see it '
  'from the street. Street parking.',
  [['Times Union (August 4, 2009): RPI fraternity hopes to move into church site',
    'https://www.timesunion.com/local/article/rpi-fraternity-hopes-to-move-into-church-site-545661.php'],
   ['The Evangelist: Closed church, rectory purchased by RPI frat',
    'https://evangelist.org/news/2018/apr/06/closed-church-rectory-purchased-by-rpi-frat']],
  brick='?'),
]

PIN_NOTES = {
  'caldwell-apartments-troy': 'OpenStreetMap\'s outline of the Caldwell Apartments; the street address 17 State Street falls beside it. On the aerial the pin is on the large flat-roofed corner building.',
  'quackenbush-building-troy': 'Address point for 30 Third Street, at the Broadway corner; on the aerial it is on the corner block, so the pin marks the site.',
  'pittsburgh-building-rpi-troy': 'OpenStreetMap\'s outline of the Pittsburgh Building; on the aerial the pin is on the building\'s roof.',
  'st-francis-de-sales-church-troy': 'OpenStreetMap\'s outline of the church, mapped with its old name; the address 320 Congress Street falls beside it. On the aerial the pin is on the church roof at the edge of Prospect Park.',
}
