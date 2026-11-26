# November 26, 2026: downtown South Bend, Indiana, its near west side, and the University of Notre Dame. The names came
# from one video (a stranger's tip, never a source); every fact here is from a source opened while this batch was written:
# Wikipedia articles, National Register records and forms on NPGallery, the Indiana nomination for St. Adalbert, the
# University of Notre Dame's Building South Bend survey, Visit South Bend, the Near West Side neighbourhood's church page,
# and the pages of the parishes, the Basilica, the Morris Center, the Civic Theatre and Notre Dame's tour and parking pages.
from data_b import N
from data_ma import W

BATCH={'key':'southbend_qvzr','label':'South Bend, Indiana: downtown, the west side and Notre Dame','added':'2026-11-26 19:41'}

def NR(ref,label):
    return ['National Register record: '+label,'https://npgallery.nps.gov/AssetDetail/NRIS/%s'%ref]

def BSB(n,label):
    return ['Building South Bend (University of Notre Dame): '+label,'https://buildingsouthbend.nd.edu/properties/nd-sb-%s/'%n]

DT='Downtown South Bend has metered street parking and public garages; which is nearest was not checked.'
ND=('The University of Notre Dame owns the campus, which visitors may walk. Its tour page lists visitor parking at the Hammes Notre Dame '
    'Bookstore (one hour), the Visitor Lot and the Joyce and Compton lots (paid), and the campus police page says visitors pay through ParkMobile; '
    'parking rules change on home football weekends and other big event days.')
SBT=['Visit South Bend: Studebaker-Bendix Heritage Trail','https://www.visitsouthbend.com/blog/studebaker-bendix-trail/']
WWC=['Near West Side Neighborhood: churches','https://westwashington.org/Churches.html']

PLACES=[
N('citizens-bank-south-bend','Citizens Bank Building','South Bend','in','civic','standing',41.67467,-86.25106,'exact','view','walk','','1913',
  'A six-storey bank and office building put up in 1913 to designs by the South Bend firm of Freyermuth and Maurer, with a rear addition of 1923. Its Register form calls it one of only a few terra-cotta buildings left downtown, and shows the influence of the white classical buildings of the 1893 Chicago fair. The bank changed its name over the years; it was listed on the National Register in 1985.',
  'A white terra-cotta front of three bays on Jefferson Boulevard, with a flat portico on Ionic columns over the central entrance. The form (1985) says every original window had been replaced and the east side covered over where a neighbouring building was pulled down. Interior not checked.',
  '',
  'A private building; what it is used for now was not checked. Look from Jefferson Boulevard. '+DT,
  [W('Citizens Bank (South Bend, Indiana)'),NR('85001207','Citizens Bank')],brick='?'),

N('old-courthouse-south-bend','Old Courthouse (Second St. Joseph County Courthouse)','South Bend','in','civic','standing',41.67596,-86.2531,'exact','view','walk','','1853–1855',
  'St. Joseph County\'s second courthouse, designed by John M. Van Osdel, Chicago\'s first architect; the Register record gives 1853 and 1855 as its key years. When a bigger courthouse was decided on in 1896, this one was turned round and moved onto the lot behind it on Lafayette Boulevard. It then served as the local Grand Army of the Republic hall and the county\'s historical museum. Wikipedia says the traffic, misdemeanour and small claims courts use it now. Its 1970 Register form calls it probably the oldest building in downtown South Bend.',
  'A two-storey Greek Revival temple with a Doric portico, a front gable and a cupola. By the form, the walls are bush-hammered Athens stone over thick brick, the portico columns are brick coated in cement, and the stone is a creamy colour. It stands just west of the 1897 courthouse, back to back with it. Interior not checked.',
  'A courthouse that was picked up, turned round and set down behind its replacement.',
  'Owned by St. Joseph County and used by the courts. Look from Lafayette Boulevard; court visitors go in on business, and no visiting hours were found. '+DT,
  [W('Second St. Joseph County Courthouse'),NR('70000007','Old Courthouse (Second St. Joseph County Courthouse)')],brick='no'),

N('st-joseph-county-courthouse-south-bend','Third St. Joseph County Courthouse','South Bend','in','civic','standing',41.67577,-86.25254,'exact','view','walk','','1896–1898',
  'The domed county courthouse at Main and Washington streets, begun on October 31, 1896 and in use from 1898, on the lots set aside for a courthouse in the town\'s first plat. It was drawn by the Chicago office of Shepley, Rutan and Coolidge and built by James Stewart and Company for $184,246; the Register form calls it the earliest and one of the finest Neo-Classical buildings downtown. The county kept using it after the County-City Building went up in 1967.',
  'Bedford limestone over a granite base: rusticated lower floor, pilasters and blind arches above, and a tiled dome on a garlanded drum. The east entrance keeps its paired-column portico and a clock in the pediment; the west entrance was remodelled in the late 1960s and many lower windows were filled in (form, 1985). A soldiers\' and sailors\' monument stands in the small park to the north. Interior not checked.',
  '',
  'Owned by St. Joseph County. Look from Main and Washington streets; no visiting hours were found. '+DT,
  [W('Third St. Joseph County Courthouse'),NR('85001230','Third St. Joseph County Courthouse')],brick='no'),

N('morris-performing-arts-center-south-bend','Morris Performing Arts Center (Palace Theater)','South Bend','in','civic','standing',41.67822,-86.25075,'exact','open','walk','','1921–1922',
  'Opened in 1922 as the Palace, a vaudeville house that later showed films, built with the Palais Royale ballroom next door. It was to be pulled down in 1959 but was saved, and was restored and remodelled between 1998 and 2000. It seats 2,564 and is home to the South Bend Symphony Orchestra and touring shows.',
  'A Spanish Renaissance front of terra cotta tinted in pastel shades over light-coloured brick, with round-arched windows and a cartouche bearing the letter P (Register form). Inside, a rose, blue and cream auditorium in the colours it opened with, and more than half the seats in the balcony.',
  'A 1922 vaudeville palace saved from the wrecking ball in 1959.',
  'Run as a city-owned performance hall; you go in with a ticket to a show. Box office hours are from the Morris Center\'s own page. '+DT,
  [W('Morris Performing Arts Center'),NR('85001226','Palace Theater'),['Morris Performing Arts Center: plan your visit','https://morriscenter.org/plan-your-visit/']],
  brick='no',hours='Box office Wednesday and Thursday 10 a.m. to 4 p.m., Friday 10 a.m. to 5:30 p.m., and two hours before shows'),

N('lasalle-hotel-south-bend','LaSalle Hotel','South Bend','in','hotel','standing',41.67888,-86.25089,'exact','view','walk','','1921',
  'A nine-storey hotel of 1921, built with more than 220 rooms across the street from the South Shore interurban railway\'s first South Bend station; a tunnel ran from the station to the hotel. It was listed on the National Register in 1985.',
  'Brick with terra-cotta trim and a wide overhanging cornice, next to the older Hoffman Hotel on Michigan Street. Interior not checked.',
  '',
  'A private building; what it is used for now was not checked. Look from Michigan Street. '+DT,
  [W('LaSalle Hotel (South Bend, Indiana)'),NR('85001221','LaSalle Hotel')],brick='?'),

N('jms-building-south-bend','J.M.S. Building','South Bend','in','civic','standing',41.67653,-86.25175,'exact','view','walk','','1910',
  'An eight-storey office block built in 1910 by John Mohler Studebaker of the wagon and carriage company, the initials his. It was designed by Solon S. Beman of Chicago, best known for the company town of Pullman, Illinois. Visit South Bend gives 1909 for it; the Register and Notre Dame\'s survey give 1910.',
  'White terra cotta and brick with large round-arched windows on the top floor and a bracketed cornice. Black marble replaced the classical entrance and street-level windows were changed; inside, the Notre Dame survey says the lobby keeps a marble stair and panelling, brass elevator doors and a classical cornice, and the basement a bank vault with a 12-ton door.',
  '',
  'A private office building. Look from Main Street; whether the lobby is open to visitors was not checked. '+DT,
  [W('J.M.S. Building'),BSB('00251','J.M.S. Building'),SBT],conf='mixed',brick='?'),

N('knights-of-columbus-building-south-bend','Knights of Columbus Building (Indiana Club)','South Bend','in','civic','standing',41.67462,-86.25453,'exact','view','walk','','1924',
  'A three-storey lodge built in 1924 for the Knights of Columbus to designs by Nichol, Sholer and Hoffman of Lafayette. The Indiana Club bought it in 1939 and stayed until 1976. It was listed on the National Register in 1985.',
  'A Renaissance Revival front with a ground floor of terra-cotta blocks and brick above; round-arched windows are crowned with alternating brick and terra-cotta voussoirs (Register form). Interior not checked.',
  '',
  'A private building; what it is used for now was not checked. Look from Jefferson Boulevard. '+DT,
  [W('Knights of Columbus-Indiana Club'),NR('85001218','Knights of Columbus-Indiana Club')],brick='?'),

N('north-pumping-station-south-bend','North Pumping Station','South Bend','in','water','standing',41.68617,-86.25023,'exact','public','walk','','1912',
  'A city waterworks building of 1912 by Freyermuth and Maurer, put up to replace a pumping station of the 1890s on the same spot by the river. South Bend had built its first standpipe and pumping station in 1873, drawing on artesian wells. Part of the old foundation was built into the new one. It was listed on the National Register in 1997.',
  'A brick temple to water with a red tile hipped roof, a limestone colonnade of four Ionic columns under a pediment carved NORTH PUMPING STATION, and small copper domes. The 1996 form says the steam engines were gone but huge iron pipes, a pressed-metal ceiling and iron stair rails remained, and a round brick cistern from the 1890s stands behind. Interior not checked.',
  'A waterworks dressed as a Greek temple.',
  'Owned by the City of South Bend, at the edge of Leeper Park on North Michigan Street. Look from the park and the street; the building is not open.',
  [W('North Pumping Station'),NR('96001538','North Pumping Station')],brick='?'),

N('st-patricks-church-south-bend','St. Patrick\'s Catholic Church','South Bend','in','worship','standing',41.67336,-86.25764,'exact','open','walk','','1886–1887',
  'The church of South Bend\'s oldest Catholic parish, founded by Irish immigrants in 1858. The land was bought in 1882, the cornerstone laid in 1886 and the church finished in 1887. The parish merged with neighbouring St. Hedwig\'s in 2001 by the neighbourhood\'s page, and its own page says the two became one parish with two churches on August 22, 2024. Notre Dame\'s survey calls the style Gothic Revival and the neighbourhood page Renaissance Revival.',
  'Yellow brick with red brick banding low on the front, limestone trim, a large rose window and two unequal towers with steeples; the north tower has brick panels, pinnacles and blind arcades. The side walls keep nineteenth-century glazing, and the organ is a three-manual Austin of 1929 (neighbourhood page).',
  '',
  'An active Catholic church of Saint Patrick and Saint Hedwig Parish. Mass times are from the parish\'s own page and bulletin; street parking. ',
  [BSB('00893','St. Patrick\'s Catholic Church'),WWC,['Saint Patrick and Saint Hedwig Parish','https://saintpatricksainthedwig.church']],
  brick='some',hours='Sunday Mass 10:30 a.m. and 5:30 p.m.; weekday Mass 12:15 p.m.'),

N('st-adalbert-church-south-bend','St. Adalbert Church','South Bend','in','worship','standing',41.67016,-86.28392,'site','open','walk','','1923–1926',
  'A Polish parish church on the west side, built 1923 to 1926 to designs by Worthmann and Steinbach of Chicago in the "Polish Cathedral" style; at its dedication the bishop called it the most beautiful church in the diocese. It cost almost $250,000. With its school of 1909 to 1911, rectory and convent it was listed on the National Register in 2025, its form calling it the largest and best-preserved Polish religious complex in Indiana.',
  'Late Gothic Revival brick with 150-foot twin steeples, a limestone entrance of three arches with a carved crucifix and angels above, stained-glass transoms and plaster reliefs of St. Michael, the Lamb of God and a pelican. The north tower keeps three original bells. The nomination says the complex is little altered.',
  'A Polish cathedral of the 1920s on South Bend\'s west side.',
  'An active Catholic church of St. Adalbert and St. Casimir Parish. Mass times are as a web search quoted the parish\'s own page, which could not be read directly when this was written. Street parking.',
  [['Indiana nomination: St. Adalbert Church Complex','https://www.in.gov/dnr/historic-preservation/files/hp-StAdalbert-Complex.pdf'],
   ['St. Adalbert Parish','https://stadalbertparish.org']],
  brick='?',hours='Sunday Mass 8 a.m. (English), 9:30 a.m. and 1:30 p.m. (Spanish); Friday Mass 8 a.m.'),

N('st-pauls-memorial-church-south-bend','St. Paul\'s Memorial Church','South Bend','in','worship','standing',41.67783,-86.26438,'exact','view','walk','','1901–1903',
  'A Gothic Revival church built 1901 to 1903 and given to its congregation by Clement and Ann Studebaker. The congregation began in 1872 in a school house and built the Milburn Memorial Chapel in 1882, named for Ann Studebaker\'s father; the church\'s own page says the cornerstone of this one was laid on May 12, 1901. It stands in the West Washington historic district.',
  'Cut limestone (Visit South Bend). The nave is dominated by a large stained-glass window of St. Paul preaching, ordered from Mayer and Company of Munich, and rooms off the Great Hall have windows of the life of Christ (neighbourhood page). Interior not checked.',
  '',
  'An active church. No service times were found on its own page; look from Colfax Avenue. Street parking.',
  [['St. Paul\'s Memorial Church: history','https://www.stpaulsmemorial.com/copy-of-welcome'],WWC,SBT],brick='no',hours='?'),

N('civic-theatre-christian-science-south-bend','South Bend Civic Theatre (former First Church of Christ, Scientist)','South Bend','in','worship','standing',41.68076,-86.2526,'exact','open','walk','','',
  'A former First Church of Christ, Scientist on North Main Street that the South Bend Civic Theatre made its home in January 2007. The company, founded in 1957, has a 209-seat auditorium and a 90-seat studio theatre here. When the church was built and by whom was not found.',
  'A domed former church; inside it is now a working theatre, seen by going to a play. Interior not checked.',
  '',
  'Owned and run by the South Bend Civic Theatre; you go in with a ticket. No box office hours were found on its page. '+DT,
  [['South Bend Civic Theatre: about','https://sbct.org/about/'],W('South Bend Civic Theatre')],brick='?',hours='?'),

N('studebaker-administration-building-south-bend','Studebaker Administration Building','South Bend','in','industry','standing',41.6685,-86.25266,'exact','view','walk','','1906',
  'The Studebaker company\'s head office, built in 1906 at Bronson and Main streets beside the great wagon and car works. Solon Beman of Chicago, who also drew the J.M.S. Building, designed it, and it held the engineering, sales, accounting and executive offices.',
  'Clad in oversize brick made to look like street pavers (Visit South Bend); a 2006 photograph by Indiana Landmarks shows a three-storey red brick block. It is a stop on the city\'s Studebaker-Bendix heritage trail. Interior not checked.',
  '',
  'Ownership and present use were not checked; look from Main Street. Street parking.',
  [SBT],brick='yes'),

N('main-building-notre-dame','Main Building (the Golden Dome)','Notre Dame','in','inst','standing',41.7031,-86.2389,'exact','open','walk','','1879–1882',
  'The third main building on the site. The second burned on April 23, 1879; Willoughby J. Edbrooke drew new plans and the building was finished before the autumn term of 1879, with some 300 tradesmen and 4.35 million bricks. The gilded dome followed in 1882, crowned by a 19-foot cast-iron statue of Mary. It holds the university president\'s office and other offices, and is listed with the main quadrangles on the National Register.',
  'A tall "modern Gothic" block, as its architect called it, under the gilded dome; the solid gold crown from the 1865 building\'s statue is kept on display inside (Wikipedia). The free public tour from the Eck Visitors Center includes the Main Building.',
  'Rebuilt in a single summer after the fire of 1879.',
  ND+' The free public tours start at the Eck Visitors Center; register there in person within half an hour of a tour. Tour times were not found on the page read.',
  [W('Main Building (University of Notre Dame)'),['Notre Dame: on-campus tours','https://tour.nd.edu/on-campus-tours/'],
   ['Notre Dame police: guest and visitor parking','https://police.nd.edu/parking/guest-visitor-parking/']],brick='?',hours='?'),

N('basilica-sacred-heart-notre-dame','Basilica of the Sacred Heart','Notre Dame','in','worship','standing',41.70258,-86.23974,'exact','open','walk','','1871–1892',
  'The university\'s church and the mother church of the Congregation of Holy Cross in the United States. The cornerstone was laid on May 31, 1871, the first Mass said on August 15, 1875, the sanctuary consecrated in 1888 and the steeple, 230 feet tall, finished in 1892. It replaced earlier log and frame churches going back to the log chapel of 1832.',
  'Neo-Gothic in yellow brick, with 44 large stained-glass windows from the Carmelite glassworks of Le Mans and murals painted over 17 years by Luigi Gregori. A small museum past the sacristy is open when the sign says so.',
  '',
  ND+' The Basilica\'s own page says it is open year round with hours that follow the academic calendar, that volunteer guides are on hand on weekday mornings, and that tours are cancelled over the Thanksgiving and Christmas holidays.',
  [W('Basilica of the Sacred Heart (Notre Dame)'),['Basilica of the Sacred Heart: visit and tours','https://basilica.nd.edu/about/visit-and-tours/']],
  brick='no',hours='Open daily year round, hours vary with the university calendar; Mass 11:30 a.m. daily; guides Monday to Friday 9 to 11 a.m.'),

N('washington-hall-notre-dame','Washington Hall','Notre Dame','in','inst','standing',41.7023,-86.23818,'exact','view','walk','','1881',
  'The university\'s theatre and music hall, built in 1881 to replace a frame music hall lost in the fire of April 1879; the first play on its stage was Oedipus Tyrannus in 1882. It was the seventh oldest building on the historic campus when the district was listed, and the home of music and drama until the performing arts moved in 2004; it is now a student venue.',
  'A "Modern Gothic" hall just east of the Main Building on the main quadrangle. Interior not checked.',
  '',
  ND+' Look from the quadrangle; the hall is a student venue and no visiting hours were found.',
  [W('Washington Hall (University of Notre Dame)')],brick='?'),
]

PIN_NOTES={
 'citizens-bank-south-bend':'Address point for 112 West Jefferson Boulevard, the address on the National Register record.',
 'old-courthouse-south-bend':'Address point for 112 South Lafayette Boulevard (National Register record); the 1985 form for the newer courthouse puts this one immediately west of it.',
 'st-joseph-county-courthouse-south-bend':'The address point for 105 South Main Street (National Register record) fell on Main Street; moved about 40 m west onto the domed courthouse, seen on the aerial.',
 'morris-performing-arts-center-south-bend':'Address point for 211 North Michigan Street (National Register record and the Morris Center\'s page).',
 'lasalle-hotel-south-bend':'Address point for 237 North Michigan Street (National Register record).',
 'jms-building-south-bend':'Address point for 108 North Main Street (Wikipedia and the Notre Dame survey).',
 'knights-of-columbus-building-south-bend':'Address point for 320 West Jefferson Boulevard (National Register record).',
 'north-pumping-station-south-bend':'Address point for 830 North Michigan Street (National Register record).',
 'st-patricks-church-south-bend':'Address point for 309 South Taylor Street (neighbourhood page).',
 'st-adalbert-church-south-bend':'The address point for 2505 West Grace Street (Indiana nomination) fell on a smaller building on Grace Street; moved about 100 m north-east onto the large cruciform building by Olive Street, taken from the aerial to be the church (the nomination\'s map reference falls between the two). The pin marks the site of the complex.',
 'st-pauls-memorial-church-south-bend':'Address point for 1001 West Colfax Avenue (neighbourhood page).',
 'civic-theatre-christian-science-south-bend':'Address point for 403 North Main Street (Wikipedia).',
 'studebaker-administration-building-south-bend':'Address point for 635 South Main Street (Visit South Bend).',
 'main-building-notre-dame':'Coordinates from the Wikipedia article.',
 'basilica-sacred-heart-notre-dame':'The Wikipedia coordinates fell on the path at the south end; moved about 30 m north onto the church, seen on the aerial.',
 'washington-hall-notre-dame':'Coordinates from the Wikipedia article.',
}
