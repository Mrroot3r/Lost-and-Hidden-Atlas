# Kansas City, Missouri: Quality Hill, downtown, Crossroads and Midtown, November 24, 2026.
# Part of filling in the Kansas City area on purpose for a local researcher. The Atlas had none of these buildings.
# Facts from the linked sources only: Wikipedia read as raw text, the cathedral's own page (Mass times), the Nelson-Atkins
# page (free admission, closed holidays), and a web search result quoting the City of Kansas City's page for the City Hall
# deck and the Grace and Holy Trinity Cathedral page for its services. Register forms could not be read.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_midt_zqrp', 'label': 'Kansas City: Quality Hill, downtown and Midtown', 'added': '2026-11-24 11:55'}

PLACES = [
N('cathedral-immaculate-conception-kc-mo', 'Cathedral of the Immaculate Conception (the gold dome), Kansas City', 'Kansas City', 'kcmo', 'worship', 'standing',
  39.10072, -94.58929, 'exact', 'open', 'drive', '', '1882–1883',
  'The first Catholic church in Kansas City was a log chapel at Eleventh and Broadway built in 1835. In 1857 a brick church replaced it on the same site, and when the diocese was formed in 1880 the bishop made that church his cathedral and began planning a larger one. The present cathedral was built in 1882–1883. '
  'It is the oldest building still standing on Quality Hill, and it counts as part of the Quality Hill historic district on the National Register of Historic Places (1978).',
  look='A domed cathedral known for its gold dome. Wikipedia names ten bells, each for a saint, the biggest being St. Thomas. The cathedral\'s own page offers a self-guided tour; the interior fittings were not checked in detail.',
  accn='A working parish, at 416 West 12th Street. The doors are open at the times of Mass and confession (below); the cathedral\'s page has a parking map. Hours read from the cathedral\'s own page in November 2026.',
  links=[W('Cathedral of the Immaculate Conception (Kansas City, Missouri)'), ['Cathedral of the Immaculate Conception (own page)', 'https://www.kcgolddome.org']],
  hours='Mass Sunday 9 a.m., 11 a.m., 8 p.m.; Monday to Friday 12:15 p.m. (chapel). Confession Tuesday and Thursday 11:30 to noon, Saturday 1:30 to 2:15 p.m.', brick='?'),

N('grace-holy-trinity-cathedral-kc-mo', 'Grace and Holy Trinity Cathedral, Kansas City', 'Kansas City', 'kcmo', 'worship', 'standing',
  39.09817, -94.58933, 'exact', 'open', 'drive', '', '1893–1898',
  'The parish began in 1870 as St. Paul\'s Church and became Grace Church in 1873. Its first stone building on West 13th Street, Guild Hall, went up in 1888–1890. The present nave was begun in June 1893 to a design by Frederick Elmer Hill of the New York firm McKim, Mead and White and was consecrated on May 15, 1898. '
  'It is now the seat of the Episcopal Diocese of West Missouri.',
  look='A church in what Wikipedia calls transitional Norman Gothic: round-headed windows and doors, but a pointed chancel arch. The stained glass is the draw: windows by Heinigke and Bowen (1901), Lamb Studios (1903), Duffner and Kimberly (1911), a Berlin-made window of 1913 that Wikipedia thinks is the maker\'s only work in North America, a Munich-style Madonna window of 1926 and a Tiffany Studios window of 1930. The door and window frames were meant to be carved and never were.',
  accn='A working cathedral at 415 West 13th Street in Quality Hill. The service times come from the cathedral\'s own site as a web search result quoted it; the site itself would not open here. Whether the building is open between services was not found; telephone the cathedral office before a visit.',
  links=[W('Grace and Holy Trinity Cathedral (Kansas City, Missouri)'), ['Grace and Holy Trinity Cathedral (own site)', 'https://www.kccathedral.org/about/']],
  hours='Sundays 8 a.m., 10:30 a.m. and 5 p.m.; Wednesdays 12:05 p.m.', brick='?'),

N('city-hall-kansas-city-mo', 'Kansas City City Hall and its 30th-floor observation deck', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.10057, -94.57800, 'exact', 'open', 'drive', '', '1937',
  'The third city hall since Kansas City was incorporated in 1853, built over 22 months and finished in 1937 to a Beaux-Arts and Art Deco design by Wight and Wight. It was part of the 1931 Ten-Year Plan bond program, along with the Municipal Auditorium and the Jackson County Courthouse. It cost about $6 million against $4 million of bond money. '
  'It was the tallest building in the city when new and is still one of the tallest city halls in the country.',
  look='An Indiana limestone tower of 29 stories with a six-story base whose top band is a frieze of relief sculpture on the settling of the Kansas City area (work by C. Paul Jennewein, Ulric Ellerhusen and Walker Hancock). South of it are fountains with seahorses that city workers nicknamed "Lug" and "Cut", and a statue of Abraham Lincoln and his son Tad. Inside, marble stairways, bronze work and brass elevator doors; the top floor is an observation deck.',
  accn='Owned by the City of Kansas City, at 414 East 12th Street. The deck is reached by tour only and needs an appointment made by email to the city\'s security desk, per the city\'s page as a search result quoted it. The deck is up a flight of stairs, is not wheelchair-accessible and closes in bad weather. Older listings give weekday hours that conflict with the city\'s current page.',
  links=[W('Kansas City City Hall'), ['City of Kansas City: observation deck tours', 'https://kcmo.gov/city-hall/city-hall-observation-deck-tour-information']],
  hours='Observation deck tours by appointment only: Monday, Wednesday and Friday 10 a.m. to 2 p.m.; closed in bad weather', brick='no'),

N('jackson-county-courthouse-kansas-city-mo', 'Jackson County Courthouse, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.09913, -94.57799, 'exact', 'view', 'drive', '', '1933–1934',
  'A 22-story Art Deco courthouse for the western part of Jackson County, begun in 1933 and dedicated on December 27, 1934, for $4 million from the 1931 bond issue. Harry S. Truman, then presiding judge of the county court, wanted it modelled on the Caddo Parish courthouse in Shreveport and hired its architect, Edward F. Neild, as consulting architect. Wight and Wight are credited with the design. '
  'Truman kept an office here for most of his first Senate term, 1935 to 1939.',
  look='A statue of Andrew Jackson at the 12th Street entrance. Inside, a painted second-floor ceiling with portraits of county employees (Chris Doyle, 2006) and five lobby medallions for Faith, Authority, Justice, Aspiration and Progress by Jorgen Dreyer. Public access to the lobby was not checked.',
  accn='Owned by Jackson County, at 415 East 12th Street, across the street from City Hall. A working courthouse: look from the street, and ask about public hours before going in. Hours not checked.',
  links=[W('Jackson County Courthouse (Kansas City, Missouri)')],
  hours='', brick='?'),

N('municipal-auditorium-kansas-city-mo', 'Municipal Auditorium, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.09835, -94.58642, 'exact', 'view', 'drive', '', '1935',
  'The first building of the 1931 Ten-Year Plan, opened in 1935 in the Streamline Moderne and Art Deco styles. It replaced the Convention Hall across the street, which was torn down and is now Barney Allis Plaza. Gentry, Voskamp and Neville were the lead architects, with Homer Neville as lead designer, and Hoit, Price and Barnes shared the work. '
  'Wikipedia says the Princeton Architectural Press called it one of the 500 most important architectural works in the United States (2000). It hosted the NCAA Final Four in its early years and now holds the NAIA men\'s basketball tournament.',
  look='A large streamlined arena building at 301 West 13th Street, joined to the Bartle Convention Center by skywalks. Seen from the street; the inside is open for events. Interior beyond the arena was not checked.',
  accn='Owned by the City of Kansas City and run for events. Public street and garage parking downtown. Look from the street; to go in, buy a ticket for an event. Hours not checked.',
  links=[W('Municipal Auditorium (Kansas City, Missouri)')],
  hours='', brick='?'),

N('western-auto-building-kansas-city-mo', 'Western Auto Building (Coca-Cola Building), Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.08778, -94.58111, 'exact', 'view', 'drive', '', '1914',
  'A 12-story triangular building at 2107 Grand Boulevard in the Crossroads, designed by Arthur C. Tufts and Company and built in 1914 by the Swenson Construction Company for the Coca-Cola Company (it was first called the Coca-Cola or Candler Building). The Western Auto Supply Company later had its headquarters here and put up the lighted sign on top. '
  'It joined the National Register in 1988 and is now loft condominiums. The sign was relit on July 13, 2018, after a refurbishment paid for by the condominium association.',
  look='The sign on the roof, visible from much of the Crossroads and from Interstate 35, and the narrow triangular plan the architect fitted to the lot. Wikipedia calls it a plain commercial design, not an ornate one.',
  accn='Private condominiums: look from the public sidewalks. Street parking in the Crossroads.',
  links=[W('Western Auto Building')],
  hours='', brick='?'),

N('sweeney-school-kansas-city-mo', 'Sweeney School building (Sweeney Automobile School), Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.08322, -94.58694, 'exact', 'view', 'drive', '', '1917–1929',
  'Emory Sweeney opened a trade school in 1908 and built this ten-story school across from Union Station, finished October 1, 1917. It claimed the largest school cafeteria and the largest electric sign in the world, and rooms for 800 students. In the 1918 flu epidemic 2,300 of its 3,000 students fell ill and the school was put under a quarantine that army officials called a reverse quarantine. '
  'Radio station WHB began here in 1922. The school closed after financial trouble and in 1929 the Businessmen\'s Assurance Company took the building, using it until its BMA Tower opened in 1963. The building joined the National Register in 2014.',
  look='A tall building on Pershing Road facing Union Station. Wikipedia says the University of Missouri-Kansas City\'s Institute for Human Development and the Associated Press have offices in it, and a home-goods showroom opened on the ground floor in 2011; whether those are still there was not checked.',
  accn='Private offices: look from Pershing Road. Street parking near Union Station.',
  links=[W('Sweeney School')],
  hours='', brick='?'),

N('bryant-building-kansas-city-mo', 'Bryant Building, 11th and Grand, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.10081, -94.58105, 'exact', 'view', 'drive', '', '1930–1931',
  'A 26-story Art Deco office tower at 11th and Grand, built in 1930–1931 to a design by the Chicago firm Graham, Anderson, Probst and White, adapted from the runner-up entry in the 1922 Tribune Tower competition. It replaced a seven-story Bryant Building of 1891, razed in 1931. '
  'It is on the Kansas City Register (1979) and the National Register (1989). It now houses a data centre.',
  look='A three-story granite base under a steel frame faced in brick and terra cotta (the colour of the brick is not given). The Bryant heirs sealed family records in the cornerstone.',
  accn='A private office and data-centre building: look from the sidewalk. Downtown street and garage parking.',
  links=[W('Bryant Building (Kansas City, Missouri)')],
  hours='', brick='?'),

N('federal-reserve-925-grand-kansas-city-mo', 'Former Federal Reserve Bank of Kansas City (925 Grand)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.10275, -94.58038, 'exact', 'view', 'drive', '', '1921',
  'The Kansas City Fed\'s first home was in the R. A. Long Building, 1914. This building opened across the street in November 1921, cost $4.3 million and was designed by the Chicago firm Graham, Anderson, Probst and White, who also did the Wrigley Building. It was Missouri\'s tallest building from 1921 to 1926. '
  'Harry Truman had an office in room 1107 after leaving the presidency in 1953, until the Truman Library opened in 1957. The Fed moved out in 2008 and the building was later converted to apartments and offices. It joined the National Register in 2007.',
  look='A 16-story bank-and-office building on Grand. Interior not checked.',
  accn='Private apartments and offices: look from the street. Downtown street and garage parking.',
  links=[W('925 Grand')],
  hours='', brick='?'),

N('masonic-temple-kansas-city-mo', 'Kansas City Masonic Temple (Tiffany Ballroom)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.10296, -94.57069, 'exact', 'view', 'drive', '', '1910–1911',
  'A Neoclassical building in the Beaux-Arts style designed by J. C. Sunderland, with its cornerstone laid on October 8, 1910 and a public dedication on September 30, 1911. The 6,600-square-foot Tiffany Ballroom has plaster columns and a set of Tiffany glass windows. A restoration project began in 2017. '
  'It is listed on the National Register (1980).',
  look='The Beaux-Arts front on Harrison Street and, inside, the Tiffany Ballroom. A web search found a venue that rents the rooms for events and reported past tours by outside groups; no current tour schedule was found.',
  accn='A Masonic hall at 903 Harrison Street; look from the street. Interior visits only by an event or tour arranged with the temple. Hours not found.',
  links=[W('Kansas City Masonic Temple')],
  hours='', brick='?'),

N('nelson-atkins-museum-kansas-city-mo', 'Nelson-Atkins Museum of Art (1933 building), Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.04531, -94.58084, 'exact', 'open', 'drive', '', '1930–1933',
  'The museum stands on the grounds of Oak Hall, the home of the Kansas City Star publisher William Rockhill Nelson. His will left his estate for buying art. Wight and Wight designed the Beaux-Arts building, modelled on the Cleveland Museum of Art; ground was broken in July 1930 and it opened on December 11, 1933 at a cost of $2.75 million. '
  'A newer wing, the Bloch Building, opened later and is not part of what this entry is about.',
  look='A limestone temple-like building. Charles Keck made 23 limestone panels on the outside showing the march of civilization from east to west, including wagon trains leaving Westport Landing, and the door grilles carry oak leaves for Oak Hall. The south front looks over terraces to Brush Creek.',
  accn='Run by the museum at 4525 Oak Street. Admission is free every day, per the museum\'s page read in November 2026; the museum is closed on Thanksgiving, Christmas Eve, Christmas Day and New Year\'s Day. The hours below are those Wikipedia gives; the museum\'s own page would not show them to the tool, so check before going. Hall Sculpture Park is free from sunrise to sundown.',
  links=[W('Nelson-Atkins Museum of Art'), ['Nelson-Atkins Museum (visit page)', 'https://www.nelson-atkins.org/visit/']],
  hours='Mon 10 a.m. to 5 p.m.; closed Tue and Wed; Thu and Fri 10 a.m. to 9 p.m.; Sat and Sun 10 a.m. to 5 p.m. (from Wikipedia; check the museum). Free.', brick='no'),

N('kemper-arena-hy-vee-arena-kansas-city-mo', 'Kemper Arena (Hy-Vee Arena), West Bottoms', 'Kansas City', 'kcmo', 'amuse', 'standing',
  39.09194, -94.60583, 'exact', 'view', 'drive', '', '1973–1974',
  'Built in 18 months for $22 million on the site of the Kansas City Stockyards, to replace Municipal Auditorium as home to the city\'s pro basketball and hockey teams. It was Helmut Jahn\'s first major project: a nearly windowless hall with the roof hung from steel trusses outside the walls, so no columns block the view. '
  'It held the 1976 Republican National Convention. A storm collapsed part of the roof on June 4, 1979. It joined the National Register in 2016 and has since been converted to a youth sports and community gym, and still hosts the American Royal livestock show.',
  look='The big exterior steel trusses and the plain, windowless walls. Seen from the street; whether visitors can look inside outside of events was not checked.',
  accn='A working sports and event building in the West Bottoms. Look from the street; go in for an event. Parking on the surrounding lots. Hours not checked.',
  links=[W('Hy-Vee Arena')],
  hours='', brick='?'),

N('hyde-park-historic-district-kansas-city-mo', 'Hyde Park historic neighborhood, Kansas City', 'Kansas City', 'kcmo', 'town', 'standing',
  39.05639, -94.57667, 'site', 'view', 'walk', '', '1880s–1920',
  'A residential district between Linwood Boulevard and 47th Street, laid out as an exclusive subdivision for the city\'s elite. It was annexed by Westport in 1891 and by Kansas City in 1897, and most houses were done by 1920. About 1,500 historic homes stand there, of which 291 in Central Hyde Park and 767 in South Hyde Park count toward the National Register district. '
  'After World War II many houses were split into apartments. A plaque at 36th and Gillham marks the 17-hole Kenwood Golf Links of 1894, Kansas City\'s first golf course.',
  look='Walk or drive the streets round Gillham Park; the houses are private and seen from the street. Wikipedia also names the Bellerive, once a hotel on Armour Boulevard with a lounge that drew headliners such as Billie Holiday and Liberace.',
  accn='Public streets and Gillham Park (tennis courts, ball fields, playground); the houses are private homes. Street parking.',
  links=[W('Hyde Park, Kansas City')],
  hours='', brick='?'),

N('penn-valley-park-kansas-city-mo', 'Penn Valley Park, Kansas City', 'Kansas City', 'kcmo', 'inst', 'standing',
  39.07700, -94.58900, 'site', 'public', 'walk', '', '1904',
  'A 176-acre park above downtown, developed in 1904 on land the Santa Fe Trail once crossed. It holds the Scout statue, the Pioneer Mother Memorial and The Hiker, and the Liberty Memorial with the National World War I Museum and Memorial stands beside it.',
  look='The statues and the lake, a fitness trail, tennis courts and ball fields; there is a dog park and a skate park in the south-west corner.',
  accn='A city park, open to walk through; the pin marks the middle of the park. Park hours were not checked.',
  links=[W('Penn Valley Park')],
  hours='', brick='no'),
]

PIN_NOTES = {
 'cathedral-immaculate-conception-kc-mo': 'From a street-address lookup (ArcGIS) that fell on the building, a little off Wikipedia\'s point; checked on the aerial.',
 'grace-holy-trinity-cathedral-kc-mo': 'Wikipedia\'s coordinate, checked on the aerial.',
 'city-hall-kansas-city-mo': 'Wikipedia\'s coordinate, checked on the aerial.',
 'jackson-county-courthouse-kansas-city-mo': 'From a street-address lookup (ArcGIS) that fell on the building, a little off Wikipedia\'s point; checked on the aerial.',
 'municipal-auditorium-kansas-city-mo': 'Wikipedia\'s coordinate, checked on the aerial.',
 'western-auto-building-kansas-city-mo': 'Wikipedia\'s coordinate, checked on the aerial.',
 'sweeney-school-kansas-city-mo': 'Wikipedia\'s coordinate, checked on the aerial.',
 'bryant-building-kansas-city-mo': 'Wikipedia\'s coordinate, checked on the aerial.',
 'federal-reserve-925-grand-kansas-city-mo': 'From a street-address lookup (ArcGIS) that fell on the building, a little off Wikipedia\'s point; checked on the aerial.',
 'masonic-temple-kansas-city-mo': 'From a street-address lookup (ArcGIS) that fell on the building, a little off Wikipedia\'s point; checked on the aerial.',
 'nelson-atkins-museum-kansas-city-mo': 'Wikipedia\'s coordinate, checked on the aerial.',
 'kemper-arena-hy-vee-arena-kansas-city-mo': 'Wikipedia\'s coordinate, checked on the aerial.',
 'hyde-park-historic-district-kansas-city-mo': 'Wikipedia\'s coordinate for the neighbourhood; the pin marks the district.',
 'penn-valley-park-kansas-city-mo': 'Wikipedia\'s coordinate for the park; the pin marks the park.',
}
