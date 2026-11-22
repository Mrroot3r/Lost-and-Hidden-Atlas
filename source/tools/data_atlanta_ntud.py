# November 22, 2026: Atlanta, Georgia, from the buildings named in one video of old architecture (Old World Exploration,
# "Old World Atlanta, Georgia", 2023). The video was used only as a list of names; the record of every name and what came of
# it is source/videos/20230701_j5c5IBAGQbo.md. Facts from the linked sources only, read in this session: Wikipedia through
# tools/wiki_raw.py; National Register forms on NPGallery, the Basilica's, the Fox Theatre's, Oglethorpe University's and
# Invest Atlanta's pages through tools/page.py.
from data_b import N
from data_ma import W

BATCH={'key':'atlanta_ntud','label':'Atlanta: buildings from an old-architecture video','added':'2026-11-22 23:34'}

NR='https://npgallery.nps.gov/NRHP/GetAsset/NRHP/'

PLACES=[
N('candler-building-atlanta','Candler Building','Atlanta','ga','civic','standing',33.75689,-84.38788,'exact','open','drive','','1904–1906',
  'A 17-storey Beaux-Arts office tower that Asa Griggs Candler, who built up the Coca-Cola Company, put up at 127 Peachtree Street; when it was finished in 1906 it was the tallest building in the city. His Central Bank and Trust had its headquarters here. The cornerstone reads "Candler Investment Co. 1904 Geo. E. Murphy Architect". It was turned into a hotel, the Candler Hotel, which opened in October 2019.',
  'The Beaux-Arts carving on the front is intact, and the hotel kept the original lobby; a restaurant fills the old banking room. On the north side of Woodruff Park. Interior beyond the lobby not checked.',
  'The Coca-Cola fortune\'s skyscraper, tallest in town in 1906.',
  'A working hotel (the Candler Hotel, Hilton\'s Curio Collection), on the corner where John Wesley Dobbs Avenue meets Peachtree Street. Downtown street and garage parking; parking not checked. Listed on the National Register.',
  [W('Candler Building (Atlanta)'),['National Register form (77000424)',NR+'77000424_text']],
  brick='?',hours='?'),

N('flatiron-building-atlanta','Flatiron Building (English-American Building)','Atlanta','ga','civic','standing',33.75594,-84.38887,'exact','view','drive','','1897',
  'An 11-storey office building on the wedge-shaped block where Peachtree, Broad and Poplar streets meet, completed in 1897 to designs by Bradford Gilbert, five years before New York\'s Flatiron Building. Its proper name is the English-American Building. It is the oldest standing skyscraper in Atlanta and the second the city built.',
  'The narrow prow of the building points up Peachtree Street; the Rhodes-Haverty Building stands across the street. Interior not checked.',
  'Atlanta\'s flatiron, five years older than New York\'s.',
  'Privately owned offices at 84 Peachtree Street NW, in the Fairlie-Poplar district; look from the street. Listed on the National Register and protected by the city. Parking not checked.',
  [W('Flatiron Building (Atlanta)'),['National Register form (76000626)',NR+'76000626_text']],
  brick='?',hours=''),

N('hurt-building-atlanta','Hurt Building','Atlanta','ga','civic','standing',33.75417,-84.38722,'exact','view','drive','','1913–1926',
  'An 18-storey triangular office building that the developer Joel Hurt began in 1913 and finished in 1926, designed by J. E. R. Carpenter; it was the first home of the Federal Reserve Bank of Atlanta. Hurt had already built the city\'s first skyscraper, the old Equitable Building. It was renovated in 1985 and listed on the National Register in 1977.',
  'Marble and glazed brick piers with ornamental terra cotta between the windows, under a heavy decorated cornice. Inside, a circular marble staircase leads down to an event room; interior visiting not checked.',
  '',
  'Privately owned offices at 50 Hurt Plaza, downtown; look from the street. Parking not checked.',
  [W('Hurt Building'),['National Register form (77000431)',NR+'77000431_text']],
  brick='?',hours=''),

N('fox-theatre-atlanta','Fox Theatre','Atlanta','ga','civic','standing',33.7725,-84.38556,'exact','open','drive','','1929',
  'Built as the Yaarab Shrine Temple, the Shriners\' headquarters, the project ran over budget and the auditorium was leased to William Fox and opened as a 4,665-seat movie palace in 1929; Olivier Vinour of Marye, Alger and Vinour was the principal architect. In 1974 Southern Bell offered to buy it and pull it down for a parking deck; a public campaign led the city to refuse a demolition permit, and a deal saved it. It is a National Historic Landmark and now a performing arts hall.',
  'A Moorish exterior; inside, the auditorium is made to look like an Arabian courtyard under a ceiling of 96 crystal "stars", with Egyptian-style ballroom and lounges. Seen inside at a show or on one of the theatre\'s tours.',
  'Saved from a phone company\'s parking deck in 1975.',
  'A working theatre, 660 Peachtree Street NE, Midtown. The theatre\'s tours page could not be opened when this was written; its home page gives the ticket window as Friday 10 a.m. to 5 p.m. and Saturday 10 a.m. to 3 p.m., and opening three hours before doors on show days. Parking not checked.',
  [W('Fox Theatre (Atlanta)'),['Fox Theatre','https://www.foxtheatre.org/']],
  brick='?',hours='Shows on the theatre\'s calendar; ticket window Friday 10 a.m. to 5 p.m., Saturday 10 a.m. to 3 p.m.'),

N('georgian-terrace-hotel','Georgian Terrace Hotel','Atlanta','ga','hotel','standing',33.7726,-84.3846,'exact','open','drive','','1910–1911',
  'A ten-storey Beaux-Arts hotel by William Lee Stoddart, built from July 1910 to September 1911 and opened on October 2, 1911, as a Southern take on a Parisian hotel. It was one of the first hotels built outside downtown, where the trolley lines met at Peachtree Street and Ponce de Leon Avenue. A 19-storey wing was added in 1991 and the hotel was renovated in 2009. It is part of the Fox Theatre Historic District.',
  'Butter-coloured brick, marble and limestone, turreted corners, tall Palladian windows and wide columned terraces, with decorated terra cotta along the cornice. Across Peachtree Street from the Fox Theatre.',
  '',
  'A working hotel, on the corner of Peachtree Street and Ponce de Leon Avenue, Midtown. Parking not checked.',
  [W('Georgian Terrace Hotel')],
  brick='no',hours='?'),

N('atlanta-biltmore-hotel','Atlanta Biltmore Hotel and Biltmore Apartments','Atlanta','ga','hotel','standing',33.77699,-84.387,'exact','view','drive','','1924',
  'A hotel and an apartment building put up together in 1924 on the block between West Peachtree, Cypress, Fifth and Sixth streets. Both have reinforced-concrete frames faced with red tapestry brick. The National Register form of 1980 says the 1969 remodelling replaced the marble stairs of the two-storey lobby with escalators and took out the black-and-gold marble and mahogany fittings.',
  'Red brick in English bond with triangular and broken-scroll pediments over the windows, round-arched windows between paired pilasters on the top floor, and limestone corner pilasters. The hotel faces West Peachtree Street and the apartments face Fifth Street. Present use and interior not checked.',
  '',
  'Privately owned; look from West Peachtree Street or Fifth Street, Midtown. Parking not checked.',
  [['National Register form (80001071)',NR+'80001071_text']],
  brick='yes',hours=''),

N('tech-tower-atlanta','Tech Tower (Georgia Tech Administration Building)','Atlanta','ga','inst','standing',33.77239,-84.39472,'exact','view','walk','','1888',
  'Built in 1888 as the Academic Building of the Georgia School of Technology, it was the second building on the campus and is the oldest one left. Lighted signs spelling TECH hang on all four sides of its seven-storey tower, and students have several times stolen the T. It is the centre of the Georgia Institute of Technology Historic District, twelve buildings on the hill of the old campus, and holds the institute\'s administration.',
  'A red brick Victorian and Romanesque Revival building with its central tower; around it the Carnegie Building (the old library), Lyman Hall and the 1910 YMCA building. Interior not checked.',
  'The tower whose T keeps getting stolen.',
  'Georgia Institute of Technology, 225 North Avenue NW. The building is offices; look from the campus walks. Campus parking not checked.',
  [W('Tech Tower'),W('Georgia Institute of Technology Historic District')],
  brick='yes',hours=''),

N('basilica-sacred-heart-atlanta','Basilica of the Sacred Heart of Jesus','Atlanta','ga','worship','standing',33.76375,-84.38569,'exact','open','drive','','1897–1898',
  'The Marist Fathers took over the parish in 1897 and built this church to designs by Walter T. Downing, in French Romanesque and Romanesque Revival styles; it was dedicated in 1898 as the Church of the Sacred Heart of Jesus. It survived the decline of the area round it, was listed on the National Register in 1976 and was made a minor basilica in 2010. It is one of the few buildings left downtown from around 1900.',
  'Brick and terra cotta outside with marble trim. Inside, 28 stained glass windows from the Mayer studios of Munich line the nave, and a baldachin over the altar holds a life-size crucifix. An interior renovation ended with a dedication Mass on November 16, 2025.',
  '',
  'An active Catholic parish at Peachtree Street and Peachtree Center Avenue, downtown. Mass and office times are from the parish\'s own page; the office is open Monday to Thursday 10 a.m. to 4 p.m. Parking not checked.',
  [W('Basilica of the Sacred Heart of Jesus (Atlanta)'),['Basilica: Mass times','https://sacredheartatlanta.org/mass-times/'],
   ['Basilica: interior renovation','https://sacredheartatlanta.org/for-such-a-time-as-this-interior-renovation/']],
  brick='?',hours='Mass Saturday 4 p.m.; Sunday 8 and 10 a.m., 12:30 p.m. (Spanish) and 5 p.m.; Monday, Tuesday, Wednesday and Friday 12:10 p.m.'),

N('atlanta-federal-penitentiary','Atlanta Federal Penitentiary','Atlanta','ga','inst','standing',33.71111,-84.36861,'site','view','drive','','1899–1902',
  'One of the three federal prisons set up under the Three Prisons Act of 1891. The site was chosen in 1899 and the prison, designed by the St. Louis firm Eames & Young (who also drew the main building at Leavenworth), opened in January 1902 with six prisoners brought from Sing Sing. It was the largest federal prison. In the 1980s it held Cuban refugees from the Mariel boatlift, who rioted in 1987. It is still a working prison, now the Federal Correctional Institution, Atlanta.',
  'The prison and its wall, seen from the public road outside. Nothing inside can be visited.',
  '',
  'An operating federal prison (Federal Bureau of Prisons), in southeast Atlanta. Look only from the public road; there is no visitor access except for people visiting prisoners under the Bureau\'s rules.',
  [W('Federal Correctional Institution, Atlanta')],
  brick='?',hours=''),

N('fountain-hall-atlanta','Fountain Hall (Stone Hall, Atlanta University)','Atlanta','ga','inst','standing',33.75444,-84.40861,'exact','view','drive','','1882',
  'Built in 1882 as Stone Hall, the main building of Atlanta University, the first of the historically Black colleges and universities in the South; G. L. Norrman designed it in the High Victorian Gothic style. W. E. B. Du Bois had his office here from 1897 to 1910. In 1929 Atlanta University leased it to Morris Brown College, and it is now named for Bishop William A. Fountain. It is a National Historic Landmark.',
  'A three-and-a-half-storey red brick building with a hip roof and a five-storey tower over the recessed entrance. The 1974 National Register form says the outside had not been altered since 1882; the inside has been changed for modern heating and wiring. Interior not checked.',
  'Where W. E. B. Du Bois kept his office.',
  'Morris Brown College, on the south side of Martin Luther King Jr. Drive SW between Sunset Avenue and Vine Street, in the Atlanta University Center. Look from the street. Parking not checked.',
  [W('Fountain Hall'),['National Register form (74000680)',NR+'74000680_text']],
  brick='yes',hours=''),

N('agnes-scott-hall-decatur','Agnes Scott Hall ("Main"), Agnes Scott College','Decatur','ga','inst','standing',33.76923,-84.29451,'exact','view','drive','','1891',
  'Built in 1891, the oldest building of Agnes Scott College, a women\'s college founded in 1889 as Decatur Female Seminary by the Presbyterian minister Frank Henry Gaines and renamed for the mother of its benefactor, George Washington Scott. Main once held the whole school and was the first building on the campus and in the neighbourhood to have electric light. The campus is in the South Candler Street–Agnes Scott College Historic District, listed in 1994.',
  'The hall stands at the centre of the main loop of the campus and is still a residence hall; a gazebo from 1891 stood in front of it until 1926 and is now by Rebekah Scott Hall (1906). Interior not checked.',
  '',
  'Agnes Scott College (private), East College Avenue and South Candler Street, Decatur. Look from the campus walks or the street. Parking not checked.',
  [W('Agnes Scott College')],
  brick='?',hours=''),

N('oglethorpe-university-historic-district','Oglethorpe University Gothic campus and the Crypt of Civilization','Brookhaven','ga','inst','standing',33.87477,-84.33155,'exact','view','drive','','1915–1940',
  'Oglethorpe University, first chartered in 1835 near Milledgeville and closed by the Civil War, was refounded in 1913 and laid the cornerstone of this campus on Peachtree Road in 1915. Its Gothic Revival buildings were modelled on Corpus Christi College, Oxford. In Phoebe Hearst Hall is the Crypt of Civilization, a room-sized time capsule built from 1936 to 1940 and sealed in the hall\'s foundation, not to be opened before 8113 AD. Lupton Hall, Phoebe Hearst Hall, Lowry Hall and Hermance Stadium were put on the National Register in 1994, with a historic district over part of the campus.',
  'Gothic Revival halls; carillon bells hang in the top of Lupton Hall. The Crypt is sealed and not open. Interiors not checked.',
  'A time capsule not to be opened until 8113.',
  'Oglethorpe University (private), Peachtree Road, Brookhaven. Look from the campus. Parking not checked.',
  [W('Oglethorpe University'),W('Crypt of Civilization'),['Oglethorpe University: history','https://oglethorpe.edu/about/history/']],
  brick='?',hours=''),

N('atlanta-constitution-building','Atlanta Constitution Building','Atlanta','ga','civic','standing',33.75411,-84.39265,'exact','view','drive','','1947',
  'A five-storey building put up in 1947 for the Atlanta Constitution newspaper, designed by Robert and Company, with a radio station on the top floor and shops in its sloping base. The paper merged with the Atlanta Journal three years later. It later served Georgia Power and stood empty from 1972. It was listed on the National Register on January 21, 2026, and Invest Atlanta reports that a renovation has begun, turning the upper floors into 50 affordable flats with shops below.',
  'A 1940s building at the northwest corner of Alabama and Forsyth streets, by the railway gulch. Under renovation when this was written.',
  'Empty for half a century, then saved.',
  'Owned by the state transport department, with a developer renovating it; look from Alabama or Forsyth Street. Parking not checked.',
  [W('Atlanta Constitution Building'),['Invest Atlanta: renovations underway','https://www.investatlanta.com/impact-insights/renovations-underway-for-atlanta-constitution-building']],
  brick='?',hours=''),

N('henry-grady-statue-atlanta','Henry W. Grady statue','Atlanta','ga','curio','standing',33.75563,-84.39129,'exact','public','walk','','1890–1891',
  'A bronze statue of Henry W. Grady, editor of the Atlanta Constitution, who coined the phrase "New South" and died in 1889 aged 39. Money was raised within a month of his death; Alexander Doyle made the statue, which was cast in Chicopee, Massachusetts, and set on a granite pedestal from Constitution, Georgia. It was unveiled in 1891 by Grady\'s daughter. Since 2019 groups have called for it to be moved because of Grady\'s support of white supremacy; state law forbids moving monuments.',
  'The bronze figure on its granite pedestal at the meeting of Marietta Street and Forsyth Street.',
  '',
  'On a public street downtown, at Marietta and Forsyth streets. Parking not checked.',
  [W('Statue of Henry W. Grady')],
  brick='no',hours=''),

N('grady-hospital-georgia-hall','Georgia Hall (first Grady Hospital)','Atlanta','ga','inst','standing',33.75326,-84.38101,'exact','view','drive','','1890–1892',
  'Grady Memorial Hospital, named for the editor Henry W. Grady, was founded in 1890 and opened in 1892 with 14 rooms. It was built as a connected row of buildings that the architect called Italianate; the brick and frame wards, outbuildings and an eighth of a mile of corridors were later torn down, and the building that is left, now Georgia Hall, holds the hospital\'s staff offices.',
  'A three-storey brick building on a granite basement that rises five feet above the ground, at Jesse Hill Jr. Drive and Coca-Cola Place. Interior not checked.',
  '',
  'Grady Health System offices, beside the present hospital; look from the street. Parking not checked.',
  [W('Grady Memorial Hospital'),['National Register form (81000652)',NR+'81000652_text']],
  brick='?',hours=''),
]

PIN_NOTES={
 'candler-building-atlanta':'Wikipedia coordinate, which matches the National Register list; checked on the aerial.',
 'flatiron-building-atlanta':'OpenStreetMap point for the building, about 35 m from the Wikipedia coordinate, which fell in the street; checked on the aerial.',
 'hurt-building-atlanta':'Wikipedia coordinate; checked on the aerial.',
 'fox-theatre-atlanta':'Wikipedia coordinate; checked on the aerial.',
 'georgian-terrace-hotel':'Wikipedia coordinate; checked on the aerial.',
 'atlanta-biltmore-hotel':'OpenStreetMap point for the hotel building at 817 West Peachtree Street; the National Register list point fell in the courtyard behind it. Checked on the aerial.',
 'tech-tower-atlanta':'Wikipedia coordinate; checked on the aerial.',
 'basilica-sacred-heart-atlanta':'Wikipedia coordinate; checked on the aerial.',
 'atlanta-federal-penitentiary':'Wikipedia coordinate, inside the prison grounds between buildings; the pin marks the site, not one building.',
 'fountain-hall-atlanta':'Wikipedia coordinate, which matches the National Register list; checked on the aerial.',
 'agnes-scott-hall-decatur':'OpenStreetMap point for Agnes Scott Hall; checked on the aerial.',
 'oglethorpe-university-historic-district':'OpenStreetMap point for Phoebe Hearst Hall, where the Crypt of Civilization is; checked on the aerial.',
 'atlanta-constitution-building':'Wikipedia coordinate; checked on the aerial.',
 'henry-grady-statue-atlanta':'Wikipedia coordinate; checked on the aerial.',
 'grady-hospital-georgia-hall':'OpenStreetMap point for Georgia Hall; checked on the aerial.',
}
