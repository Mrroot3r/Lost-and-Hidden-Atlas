# Kansas City, Missouri: Country Club District, Sunset Hill and Midtown houses and a church, November 25, 2026.
# Part of filling in the Kansas City area on purpose for a local researcher. The Atlas had none of these buildings.
# Facts from Wikipedia read as raw text only; the National Register forms could not be opened (the state's PDFs answer
# 404 and the archive copies cannot be fetched). Every house is private or a closed building: seen from the street.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_scc_gjwm', 'label': 'Kansas City: Country Club District, Sunset Hill and Midtown houses', 'added': '2026-11-25 15:09'}

PLACES = [
N('epperson-house-kc-mo', 'Epperson House, UMKC, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.0311, -94.5813, 'exact', 'view', 'drive', '', '1919–1923',
  'Banker and meat-packing and insurance man Uriah Spray Epperson hired the French architect Horace LaPierre to design a Tudor-Gothic mansion at 5200 Cherry Street. Building began in 1919 and ended in 1923, at a cost of $450,000. Its four storeys held 54 rooms, six bathrooms, elevators, a swimming pool, a billiard room, a barbershop, a custom organ and a tunnel joining the east and west wings. '
  'Epperson died in 1927. His widow gave the house to the University of Missouri-Kansas City in 1942 and it was a men\'s dormitory until 1956. Wikipedia says it is vacant and awaiting renovation.',
  look='A large Tudor-Gothic mansion on the university campus. Seen from outside; what remains of the interior (organ, pool) was not checked.',
  accn='Owned by the University of Missouri-Kansas City, on its campus at 5200 Cherry Street, and described as vacant. Look from the public paths and streets; do not try to go in. Parking and any tours were not checked.',
  links=[W('Epperson House')], hours='', brick='?'),

N('dr-generous-henderson-house-kc-mo', 'Dr. Generous Henderson House, 1016 The Paseo, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.10106, -94.56428, 'exact', 'view', 'drive', '', '1899',
  'Designed by the local architect Rudolf Markgraf and built in 1899 for the physician Dr. Generous Henderson (1844-1924), who practised in Kansas City for forty-five years. It is a three-storey Second Renaissance Revival dwelling of brick and stone with terra-cotta ornament, a cast-iron cornice, an oriel window and columns, and a carriage house stands on the property. '
  'Wikipedia calls it one of the few surviving examples of the style in Kansas City. It was listed on the National Register of Historic Places in 1979.',
  look='Brick and stone walls with terra-cotta trim, the cast-iron cornice and the oriel window, from the street. Wikipedia describes the house as brick and stone; its present use and interior were not checked.',
  accn='At 1016 The Paseo, once one of the city\'s most prestigious streets. Treat it as private or closed; look from the public sidewalk. Current owner and use were not checked.',
  links=[W('Dr. Generous Henderson House')], hours='', brick='some'),

N('charles-s-keith-house-kc-mo', 'Charles S. Keith House (J. C. Nichols House), Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.02907, -94.60556, 'exact', 'view', 'drive', '', '1913–1914',
  'A Georgian Revival house at 1214 West 55th Street in the Country Club District, designed in 1913 by the Kansas City firm Shepard, Farrar and Wiser and finished in 1914 for the lumber man Charles S. Keith, president of the Central Coal and Coke Company. Keith sold it in 1920 to the real-estate developer J. C. Nichols, who lived there until he died in 1950. '
  'Keith later served as interim mayor of Kansas City in 1940. The house has 22 rooms, cut-stone trim, several pergolas and a large carriage house, on three acres laid out by Hare and Hare.',
  look='A Georgian Revival mansion with cut-stone trim and pergolas, set in grounds by the firm that planned much of the Country Club District. Seen from the street; the interior was not checked.',
  accn='A private residence on West 55th Street near Ward Parkway. Look from the public street only. Current owner was not checked.',
  links=[W('Charles S. Keith House')], hours='', brick='yes'),

N('mack-b-nelson-house-kc-mo', 'Mack B. Nelson House, 5500 Ward Parkway, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.02779, -94.60449, 'exact', 'view', 'drive', '', '1915',
  'Built in 1915 to a design by Henry F. Hoit, who also designed the R. A. Long house now called the Kansas City Museum, for Mack B. Nelson, then vice president of the Long-Bell Lumber Company and later its head. The big rectangular house is built round an interior atrium lit by a movable skylight, and has 16 bedrooms, 8 bathrooms, a swimming pool with a pool house and a basketball court. '
  'It faces the Bernard Corrigan House across 55th Street. Wikipedia records that the film director Tressie Souders worked as a maid here in 1921.',
  look='A large house at the corner of Ward Parkway and 55th Street, in the Sunset Hill part of the Country Club District. Seen from the street; the atrium and interior were not checked.',
  accn='At 5500 Ward Parkway, directly across 55th Street from the Corrigan House. Treat as private; look from the public sidewalk. Ownership not checked.',
  links=[W('Mack B. Nelson House')], hours='', brick='?'),

N('tom-pendergast-house-kc-mo', 'Tom Pendergast House, 5650 Ward Parkway, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.02513, -94.60341, 'exact', 'view', 'drive', '', '1927',
  'A modified French Provincial house at 5650 Ward Parkway in the Country Club District, designed by J. C. Nichols Company architect Edward Tanner and finished in 1927. Members of the Pendergast family lived here until the political boss Tom Pendergast died in 1945. '
  'Pendergast\'s machine ran Kansas City in the 1920s and 1930s, looked the other way on liquor and gambling (which helped Kansas City jazz grow), and also brought large building projects such as the Jackson County Courthouse and City Hall. He was convicted and served a fifteen-month sentence.',
  look='A French Provincial style house on Ward Parkway, known as the home of the city\'s political boss. Seen from the street; Wikipedia does not describe the interior and it was not checked.',
  accn='A private residence on Ward Parkway. Look from the public sidewalk only. Ownership not checked.',
  links=[W('Tom Pendergast House')], hours='', brick='?'),

N('mary-rockwell-hook-house-kc-mo', 'Mary Rockwell Hook House, 4940 Summit, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.03742, -94.59681, 'exact', 'view', 'drive', '', '1925–1927',
  'The architect Mary Rockwell Hook designed this house at 4940 Summit Street for herself and built it between 1925 and 1927. It is a rambling mix of intersecting wings, gables, dormers, decks and porches, and it had a swimming pool that Hook believed was one of the first private pools in the Kansas City area. '
  'Hook lived here with her husband and two children, and the house stayed in her family until 1972. It was listed on the National Register of Historic Places in 1983.',
  look='Intersecting wings and gables, dormers and porches, from the street. The architect built several houses on these streets (see the Pink House and the Rockwell, Love and Jacobs houses nearby).',
  accn='A private residence at 4940 Summit Street. Look from the public street only; parking is on the street.',
  links=[W('Mary Rockwell Hook House')], hours='', brick='?'),

N('house-5011-sunset-drive-kc-mo', 'House at 5011 Sunset Drive (Mary Rockwell Hook), Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.03687, -94.59706, 'exact', 'view', 'drive', '', '1922–1923',
  'A three-storey, L-plan Bungalow or American Craftsman house faced in stone, designed by Mary Rockwell Hook and built in 1922-1923. It has an overhanging hipped roof with heavily bracketed eaves and an "outdoor living room". '
  'It was listed on the National Register of Historic Places in 1983 as one of Hook\'s houses in the Country Club District.',
  look='Stone veneer, a wide hipped roof and bracketed eaves, from the street.',
  accn='A private residence at 5011 Sunset Drive. Look from the public street only.',
  links=[W('House at 5011 Sunset Drive')], hours='', brick='some'),

N('bertrand-rockwell-house-kc-mo', 'Bertrand Rockwell House, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.03391, -94.59963, 'exact', 'view', 'drive', '', '1908–1909',
  'Mary Rockwell Hook designed this house, built in 1908-1909, for her parents, Mr. and Mrs. Bertrand Rockwell. It is a three-storey rectangular dwelling faced with rubble stone and stucco, with Classical Revival details: a recessed entry and end porches with Doric columns. '
  'It was listed on the National Register of Historic Places in 1983.',
  look='Rubble stone and stucco walls with Doric porch columns, from the street.',
  accn='A private residence in the Country Club District. Look from the public street only.',
  links=[W('Bertrand Rockwell House')], hours='', brick='?'),

N('emily-rockwell-love-house-kc-mo', 'Emily Rockwell Love House, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.0361, -94.5975, 'site', 'view', 'drive', '', '1915',
  'Mary Rockwell Hook designed this house, built in 1915, as a home for her sister Emily. It is built on a slope on three levels, in coursed rubble fieldstone that Wikipedia says "appears to have had a Cotswold cottage or a Norman farmhouse among its antecedents". '
  'It was listed on the National Register of Historic Places in 2003.',
  look='Coursed fieldstone walls stepping down a slope, like a small English cottage; seen from the street.',
  accn='A private residence in the Country Club District. Look from the public street only.',
  links=[W('Emily Rockwell Love House')], hours='', brick='?'),

N('floyd-jacobs-house-kc-mo', 'Floyd Jacobs House, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.03627, -94.59862, 'exact', 'view', 'drive', '', '1925',
  'Designed by Mary Rockwell Hook and built in 1925 for the lawyer Floyd Jacobs to show what could be done with hillside lots in the new development. It is a three-storey, hip-roofed house faced in rubble stone and stucco, planned to deal with a steep slope and frontage on two streets at different levels. '
  'It was listed on the National Register of Historic Places in 1983.',
  look='A hip-roofed house of rubble stone and stucco fitted into a hillside with two street fronts; seen from the street.',
  accn='A private residence in the Country Club District. Look from the public street only.',
  links=[W('Floyd Jacobs House')], hours='', brick='?'),

N('robert-ostertag-house-kc-mo', 'Robert Ostertag House, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.0361, -94.5969, 'site', 'view', 'drive', '', '1922',
  'Mary Rockwell Hook designed this T-shaped, stucco-faced house and it was built in 1922 for $15,000 for Robert A. Ostertag, president of a tin can company. It was listed on the National Register of Historic Places in 1983, with the other Hook houses nearby.',
  look='A T-shaped stucco house, from the street, near the Pink House.',
  accn='A private residence in the Country Club District. Look from the public street only.',
  links=[W('Robert Ostertag House')], hours='', brick='?'),
]

PIN_NOTES = {
 'epperson-house-kc-mo': "Wikipedia's point, checked on the aerial: it falls on the large mansion at 5200 Cherry Street.",
 'dr-generous-henderson-house-kc-mo': "A street-address lookup (OpenStreetMap) for 1016 The Paseo, which falls on a building there; the National Register point is within about 15 m.",
 'charles-s-keith-house-kc-mo': "A street-address lookup (OpenStreetMap) for 1214 West 55th Street, which names this house. Wikipedia's own point fell on a road and lawn and was not used.",
 'mack-b-nelson-house-kc-mo': "A street-address lookup (OpenStreetMap) that names this house, checked on the aerial.",
 'tom-pendergast-house-kc-mo': "A street-address lookup (OpenStreetMap) that names this house, checked on the aerial.",
 'mary-rockwell-hook-house-kc-mo': "A street-address lookup (OpenStreetMap) that names this house at 4940 Summit Street.",
 'house-5011-sunset-drive-kc-mo': "The building OpenStreetMap lists at 5011 Sunset Drive. Wikipedia's own point was on another street and was not used.",
 'bertrand-rockwell-house-kc-mo': "A street-address lookup (OpenStreetMap) that names this house at 1004 West 52nd Street.",
 'emily-rockwell-love-house-kc-mo': "The National Register point. No street address was found, so the pin marks the house nearest that point and could be one house off; not confirmed by an address.",
 'floyd-jacobs-house-kc-mo': "A street-address lookup (OpenStreetMap) that names this house at 5050 Sunset Drive.",
 'robert-ostertag-house-kc-mo': "The National Register point. No street address was found, so the pin marks the house nearest that point and could be one house off; not confirmed by an address.",
}
