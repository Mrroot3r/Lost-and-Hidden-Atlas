# November 25, 2026: three places in Lafayette and Johnson counties, Missouri, east of Kansas City, from Wikipedia read as
# raw text, a Missouri Preservation page, the Clio entry for the Odessa building, a KSHB news report, and Waymarking pages that
# copy the text of National Register forms. The Register forms themselves could not be opened.
from data_b import N
from data_ma import W

LNR = ['Missouri State Parks: Lafayette County National Register listings', 'https://mostateparks.com/basic-page/missouri-national-register-listings/Lafayette']

PLACES = [
N('joseph-miller-mausoleum-holden-mo', 'Joseph M. Miller Mausoleum', 'Holden', 'mo', 'burial', 'standing',
  38.73026, -93.99304, 'site', 'view', 'drive', 'cemeteries', '1915–1927',
  'Joseph M. Miller, a Bible scholar, moved to Holden from Macon in 1915 and had this tomb built beside the highway, in a steel-reinforced concrete design drawn from tombs described in the Bible. '
  'Sources disagree on when it was finished: Missouri Preservation says 1915 to 1918, Wikipedia says by 1927. Miller relatives were buried here until 1931 (Missouri Preservation counts eighteen; Wikipedia says fifteen to twenty). '
  'A descendant took over its care in 2010 and the dead have since been moved to the town cemetery. It was added to the National Register in 2018.',
  look='A small castle-like concrete tomb standing alone at the roadside, not inside a cemetery. Interior not checked.',
  accn='Beside Missouri Highway 131 just north of Holden. A Waymarking page says the grounds are open in daylight; no page of the owner was read, so treat this as look from the road unless a current page says tours run. Do not stop on the highway: park where the shoulder is safe or in Holden.',
  links=[['Missouri Preservation: The Miller Mausoleum', 'https://preservemo.org/the-miller-mausoleum/'], W('Joseph M. Miller Mausoleum'), ['Waymarking: Miller Mausoleum', 'https://www.waymarking.com/waymarks/wm146Z7_Miller_Mausoleum_Holden_MO']],
  conf='mixed', brick='no'),

N('robinson-house-lexington-mo', 'William P. Robinson House', 'Lexington', 'mo', 'landmark', 'standing',
  39.16139, -93.84, 'area', 'view', 'drive', '', 'c. 1850',
  'A two-story Greek Revival brick I-house of about 1850 with a central passage and a two-story rear ell that has an enclosed two-story porch. It was added to the National Register in 1997. Wikipedia\'s short article is the only account read; the form could not be opened.',
  look='A plain, symmetrical brick farmhouse of the Missouri River country. Look from the public road if one passes it.',
  accn='A private house near Lexington; the pin is the Register list point and its owner and what can be seen from a public road were not checked. Treat as view-only and do not go onto the property.',
  links=[W('William P. Robinson House'), LNR],
  conf='mixed', brick='?'),

N('house-1413-lafayette-lexington-mo', 'House at 1413 Lafayette Street', 'Lexington', 'mo', 'landmark', 'standing',
  39.18694, -93.8775, 'area', 'view', 'walk', '', 'c. 1840',
  'A Greek Revival brick house of about 1840 with one and a half stories and a side passage, in the older part of Lexington. Wikipedia describes a handsome entrance with transom and sidelights, a parapet gable roof and segmental-arched windows on the rear wing. It was added to the National Register in 1999.',
  look='The doorway with its transom and sidelights, and the arched windows at the back. Only Wikipedia was read.',
  accn='A private house at 1413 Lafayette Street, Lexington; look from the street. The pin is the Register list point.',
  links=[W('House at 1413 Lafayette St.'), LNR],
  conf='mixed', brick='?'),
]

BATCH = {'key': 'mo_lafy', 'label': 'Lafayette and Johnson counties, Missouri: a roadside mausoleum and two Lexington-area houses', 'added': '2026-11-25 08:54'}

PIN_NOTES = {
 'joseph-miller-mausoleum-holden-mo': 'The coordinate in Wikipedia fell on the road; moved 23 m west onto the small white building beside it on the aerial.',
 'robinson-house-lexington-mo': 'The Register list coordinate (Wikipedia); checked on the aerial.',
 'house-1413-lafayette-lexington-mo': 'The Register list coordinate (Wikipedia); checked on the aerial.',
}
