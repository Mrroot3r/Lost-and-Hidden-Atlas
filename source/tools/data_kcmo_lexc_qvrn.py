# November 26, 2026: a short pass over registered districts round Lexington and Liberty, Missouri, that earlier batches left out.
# Facts come from Wikipedia's articles on each district, read as raw text in this session. The National Register forms are not
# on line (the National Park Service holds only a placeholder page for each), so nothing here rests on a form.
from data_b import N
from data_ma import W

PLACES = [
N('commercial-community-district-lexington-mo', 'Commercial Community Historic District, Lexington', 'Lexington', 'mo', 'town', 'standing',
  39.18583, -93.88111, 'area', 'view', 'drive', '', '1830–1930',
  'This is the business centre of Lexington and the streets round it, built up between about 1830 and 1930. The National Register lists 106 buildings and one structure in it, in Late Victorian and Gothic Revival styles. The Lafayette County Courthouse stands inside it and is listed on its own.',
  look='Wikipedia names a former German Methodist Episcopal church (about 1878, rebuilt 1910, now a racquetball club), the Wright House (about 1840), Goehner\'s Marbleworks (about 1857), the First Presbyterian Church and a former beer cellar of about 1871 once run by Baehr, now a storage building. Walk the streets round the courthouse square. Interiors were not checked.',
  accn='City streets and sidewalks round the courthouse square; the land is not mapped as public land, so the buildings are looked at from the street. The buildings are mostly in private or business hands, so look from the street. The pin is the district\'s one coordinate on Wikipedia, near the square: not checked against the district\'s outline. Park on the street.',
  links=[W('Commercial Community Historic District'), ['Missouri State Parks: Lafayette County National Register listings', 'https://mostateparks.com/basic-page/missouri-national-register-listings/Lafayette']],
  conf='mixed', brick='?'),

N('dougherty-prospect-heights-district-liberty-mo', 'Dougherty–Prospect Heights Historic District, Liberty', 'Liberty', 'kcmo', 'town', 'standing',
  39.24816, -94.42525, 'area', 'view', 'drive', '', '1850–1946',
  'This is a residential part of Liberty, in Clay County, that grew between about 1850 and 1946. The National Register lists 139 buildings in it, put up in Greek Revival, Queen Anne, Tudor Revival, Prairie School and Craftsman styles, with a good many foursquare houses and bungalows. It was listed in 2001.',
  look='Streets of older houses a short way from Liberty\'s courthouse square, with the styles above side by side. Which houses are the oldest was not checked; the form is not on line.',
  accn='City streets in a residential area; the street frontage is public but the land is not mapped as public land. The houses are private homes: look from the sidewalk and do not enter yards. The pin is Wikipedia\'s single point for the district and not an outline. Park on the street away from driveways.',
  links=[W('Dougherty–Prospect Heights Historic District'), ['Missouri State Parks: Clay County National Register listings', 'https://mostateparks.com/basic-page/missouri-national-register-listings/Clay']],
  conf='mixed', brick='?'),
]
BATCH={'key':'kcmo_lexc_qvrn','label':'Kansas City, Missouri','added':'2026-11-26 02:46'}
PIN_NOTES={
'commercial-community-district-lexington-mo':'Wikipedia gives one point for the district, near the courthouse square; the pin check looked at the aerial and the pin marks the district centre, not a building.',
'dougherty-prospect-heights-district-liberty-mo':'Wikipedia gives one point for the district, which fell on a house; the pin was moved 50 metres onto the street beside it, and marks the district only roughly.',
}
