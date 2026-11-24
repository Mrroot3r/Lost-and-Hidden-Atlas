# November 24, 2026: Grand Rapids, Michigan. A "videos" session (PROMPTS.md job 9): the names came from one video's tour of
# old Grand Rapids buildings (the record is source/videos/20241101_iVyr5gTGF2U.md); the video is a tip and nothing here
# rests on it. Sources read: Wikipedia (each article named in the links), SAH Archipedia (Buildings of Michigan, 2012),
# Fox 17 and Rapid Growth Media news reports, a 1926 county history of the YMCA, and for service times the pages of
# St. Mark's and of the Cathedral of Saint Andrew. Pins are OpenStreetMap buildings, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'grandrapids_ukls','label':'Michigan: old Grand Rapids','added':'2026-11-24 19:31'}

DT=' Downtown parking is in city ramps, lots and street meters; their hours and fees were not checked.'
SAH='https://sah-archipedia.org/buildings/MI-01-'

PLACES=[

N('st-marks-episcopal-grand-rapids','St. Mark\'s Episcopal Church','Grand Rapids','mi','worship','standing',42.96623,-85.66776,'exact','open','walk','','1847–1848',
  'Grand Rapids\' oldest church building, a Gothic Revival church of limestone rubble taken from the bed of the Grand River and hauled to the site by oxen. The parish was organised in 1836; the church was built in 1847 and 1848 to the design of a member, Peter Randolph Livingston Pierce, who with the rector meant it to recall old Trinity Church in New York. In 1848 it was the largest church west of Detroit. The twin octagonal towers came in 1851, the transepts in 1855, the chancel and chapel in 1872 and the parish house in 1902.',
  'Rough grey limestone walls and two octagonal front towers on Division Avenue. Inside, the congregation sits under a hammer-beam roof; the chapel has an Adoration of the Magi window made in Milwaukee in 1959. A working Episcopal church: go in at a service.',
  '',
  'A working parish church at 134 North Division Avenue, downtown; the service times are from the parish\'s own page.'+DT,
  [['SAH Archipedia: St. Mark\'s Episcopal Church',SAH+'KT13'],['St. Mark\'s Episcopal Church','https://www.stmarksgr.org/']],
  brick='no',hours='Sunday 8 and 10:30 a.m.; Wednesday noon Eucharist, September to May'),

N('michigan-trust-building-grand-rapids','Michigan Trust Company Building','Grand Rapids','mi','civic','standing',42.96606,-85.66969,'exact','view','walk','','1891–1892',
  'An early office skyscraper built in 1891 and 1892 for the Michigan Trust Company, organised in 1889 by Grand Rapids businessmen. The Chicago architect Solon S. Beman drew it in the Richardsonian Romanesque style; it was the city\'s first building put up only for offices and, when new, its tallest. Two ten-storey sections were added at the back in 1913 and an eleventh floor in the 1920s; Old Kent Bank made it its headquarters in 1957. On the National Register since 1983.',
  'Rock-faced red sandstone on the two lowest storeys and dark red brick with red terra-cotta trim above, with round-arched window groups that get smaller as they rise. Offices; the inside was not checked.',
  '',
  'A private office building at 40 Pearl Street NW, on the corner of Ottawa Avenue; seen from the streets.'+DT,
  [W('Michigan Trust Company Building'),['SAH Archipedia: Trust Building',SAH+'KT9']],
  brick='yes'),

N('grand-rapids-trust-building','Grand Rapids Trust Building (77 Monroe Center)','Grand Rapids','mi','civic','standing',42.96447,-85.66966,'exact','view','walk','','1926',
  'A bank and office tower of 1926 by Wirt C. Rowland of Smith, Hinchman and Grylls, built for the Grand Rapids Trust Company. Its strong piers rise to pinnacles above great three-storey arches; the architectural historian Kathryn Bishop Eckert likens it to H. H. Richardson\'s Marshall Field store in Chicago turned on end.',
  'The whole front is terra-cotta, with reliefs by the sculptor Corrado Parducci on the city\'s early history: tomahawks, canoes, pine trees, wolverines and other animals. The second-floor banking room, with columns, marble, terrazzo and metalwork, was not checked for visitors.',
  '',
  'A private building at 77 Monroe Center NW; the reliefs are seen from the pedestrian street.'+DT,
  [['SAH Archipedia: 77 Monroe Center',SAH+'KT10']],
  brick='no'),

N('pantlind-hotel-grand-rapids','Pantlind Hotel (Amway Grand Plaza)','Grand Rapids','mi','hotel','standing',42.96681,-85.67251,'site','open','walk','','1913–1915',
  'A hotel of over five hundred rooms built on the site of an older Pantlind Hotel and run by J. Boyd Pantlind, for the furniture buyers who came to the city\'s furniture shows. The New York firm Warren and Wetmore, known for Grand Central Terminal, designed it in a restrained Renaissance Revival manner. The building dates are not settled: Buildings of Michigan gives 1913 to 1915, Wikipedia says it opened in 1913. Amway bought it in 1979, renovated it and reopened it in 1981 as the Amway Grand Plaza, adding a glass tower beside it.',
  'The old Pantlind is the lower, older block beside the later glass tower, with classical columns and terra-cotta work. Wikipedia says it had one of the largest gold-leaf ceilings in the world. A working hotel: the public rooms are seen by going in as a guest or to a restaurant.',
  '',
  'A working hotel run by AHC+Hospitality at 187 Monroe Avenue NW; its hours were not read.'+DT,
  [W('Amway Grand Plaza Hotel'),['SAH Archipedia: Amway Grand Plaza Hotel (Pantlind Hotel)',SAH+'KT4']],
  conf='mixed',brick='?',hours='?'),

N('woodbridge-ferris-building-grand-rapids','Old Federal Building (Woodbridge N. Ferris Building)','Grand Rapids','mi','civic','standing',42.96658,-85.66829,'exact','view','walk','','1908–1911',
  'The federal courthouse and post office of 1908 to 1911, by James K. Taylor, Supervising Architect of the Treasury, in rusticated grey Vermont granite; it replaced a federal building of 1879. Alice Roosevelt Longworth laid the cornerstone in 1909, and Gerald R. Ford had his congressional office here in the 1950s. The post office and court left in 1972; the Grand Rapids Art Museum used it from 1981 to 2007, and since about 2011 it has held classrooms and galleries of Kendall College of Art and Design.',
  'A Beaux-Arts granite block with a two-storey colonnade between two pedimented entrance pavilions. The rehabilitation of 1980 kept the plasterwork, woodwork and mosaic floors inside. Galleries in it open at times; these were not checked.',
  '',
  'Owned by the city and used by Kendall College of Art and Design (Ferris State University), at 17 Pearl Street NW; seen from Pearl Street and Division Avenue.'+DT,
  [W('Woodbridge N. Ferris Building'),['SAH Archipedia: Kendall College (Old Federal Building)',SAH+'KT12']],
  brick='no'),

N('morton-hotel-grand-rapids','Morton Hotel','Grand Rapids','mi','hotel','standing',42.96508,-85.66922,'exact','view','walk','','1923',
  'A thirteen-storey hotel on the corner of Monroe Center and Ionia Avenue. After a fire, the New Morton Hotel opened in 1923. The Saperstein family bought it in 1971 and made it the Morton House Apartments; Rockford Construction bought it and in 2014 was turning it into apartments and shops, uncovering old public rooms, stairs, restaurants and bars that had been closed off for decades.',
  'The tall corner block at Monroe Center and Ionia. Now apartments with shops on the ground floor; the old public rooms were not checked for visitors.',
  '',
  'Private apartments at 55 Ionia Avenue NW; seen from the streets and the Monroe Center pedestrian street.'+DT,
  [['Fox 17: old Morton Hotel rooms uncovered, 2014','https://www.fox17online.com/2014/04/01/walk-through-time-old-morton-hotel-rooms-uncovered-after-decades']],
  brick='?'),

N('central-high-school-grand-rapids','Central High School (Innovation Central)','Grand Rapids','mi','civic','standing',42.96603,-85.65884,'site','view','walk','','1910–1911',
  'The city\'s high school, whose roots go back to 1849, moved into this building, built from 1910 to 1911 for 435,000 dollars, on January 31, 1911. Its auditorium was then the largest in Michigan, and Theodore Roosevelt and William Howard Taft spoke there; the first classes of what became Grand Rapids Community College were held in it from 1914. Renamed Innovation Central High School in 2014.',
  'A large school building on Fountain Street at the edge of the Heritage Hill district. A working public school; seen from the street only.',
  '',
  'A Grand Rapids public school at 421 Fountain Street NE; not open to visitors. Street parking only; do not use the school\'s lots in school hours.',
  [W('Innovation Central High School')],
  brick='?'),

N('ymca-fitzgerald-grand-rapids','YMCA Building (The Fitzgerald)','Grand Rapids','mi','civic','standing',42.96443,-85.66656,'site','view','walk','','1915',
  'The YMCA\'s central building in Grand Rapids, opened on Library Street in 1915 after a 1913 campaign raised 300,000 dollars; a 1926 county history lists two gymnasiums, a swimming pool and rooms for young men. The YMCA later moved out, and in 2008 the building reopened as the Fitzgerald, thirty-nine condominiums with penthouses on the top.',
  'The old Y on Library Street beside the public library and Veterans Park. Private homes inside; seen from the street.',
  '',
  'Private condominiums at 27 Library Street NE; seen from the street and Veterans Park.'+DT,
  [['Rapid Growth Media: Fitzgerald condos, 2008','https://www.rapidgrowthmedia.com/devnews/fitz0918.aspx'],['Etten (1926): Young Men\'s Christian Association','https://kent.migenweb.org/etten1926/ymca.html']],
  brick='?'),

N('cathedral-saint-andrew-grand-rapids','Cathedral of Saint Andrew','Grand Rapids','mi','worship','standing',42.95806,-85.66714,'exact','open','walk','','1874–1876; rebuilt 1903',
  'The cathedral of the Catholic Diocese of Grand Rapids. The parish began with a church Frederic Baraga built on the west bank of the river; this church on Sheldon Avenue was begun in 1875 to a parishioner\'s design and became the cathedral when the diocese was formed in 1882. Lightning set it on fire in 1901, and it was rebuilt and enlarged in 1903 to plans by Brielmaier and Sons of Milwaukee. Some beams above the ceiling still show the char of the fire.',
  'A cross-shaped Gothic Revival church of pale yellowish-white Milwaukee brick, with unequal spired towers, the taller 192 feet high. Inside, stained glass of 1915 from F. X. Zettler of Munich, including the Nativity and Ascension in the transepts, and windows by Mayer of Munich and the Grand Rapids Art Glass Company. Go in at Mass.',
  '',
  'A working cathedral on Sheldon Boulevard SE, south of downtown; Mass times from the cathedral\'s own page. Street parking nearby; lots not checked.',
  [W('Cathedral of Saint Andrew (Grand Rapids, Michigan)'),['SAH Archipedia: St. Andrew\'s Catholic Cathedral',SAH+'KT23'],['Cathedral of Saint Andrew','https://cathedralofsaintandrew.org/']],
  brick='no',hours='Saturday 4:30 p.m.; Sunday 10 a.m., noon (Spanish), 5:30 and 7:30 p.m.; weekdays 7 a.m. and 12:05 p.m.'),

]

PIN_NOTES={
 'st-marks-episcopal-grand-rapids':'OpenStreetMap building of Saint Mark\'s Church on Division Avenue, looked at on the aerial.',
 'michigan-trust-building-grand-rapids':'OpenStreetMap building named Trust Building at Pearl and Ottawa, looked at on the aerial.',
 'grand-rapids-trust-building':'OpenStreetMap building at 77 Monroe Center, looked at on the aerial.',
 'pantlind-hotel-grand-rapids':'OpenStreetMap point of the Amway Grand Plaza at 187 Monroe Avenue, looked at on the aerial; the old Pantlind is the block at Monroe and Pearl.',
 'woodbridge-ferris-building-grand-rapids':'OpenStreetMap building named Historic Federal Building, 17 Pearl Street, looked at on the aerial.',
 'morton-hotel-grand-rapids':'OpenStreetMap building of The Morton, 55 Ionia Avenue, looked at on the aerial.',
 'central-high-school-grand-rapids':'OpenStreetMap building of Innovation Central High School on Fountain Street, looked at on the aerial.',
 'ymca-fitzgerald-grand-rapids':'OpenStreetMap address point for 27 Library Street NE, looked at on the aerial.',
 'cathedral-saint-andrew-grand-rapids':'OpenStreetMap place of worship for the Cathedral of Saint Andrew, looked at on the aerial.',
}
