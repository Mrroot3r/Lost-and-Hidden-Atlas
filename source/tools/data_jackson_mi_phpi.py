# November 28, 2026: Jackson, Michigan. A "videos" session (PROMPTS.md job 9): the names came from one video's tour of
# old Jackson buildings (the record is source/videos/20250919_-NTAzQ-wecY.md); the video is a tip and nothing here
# rests on it. Sources read: Wikipedia (each article named in the links), SAH Archipedia (Buildings of Michigan, 2012),
# the National Register record pages, the Michigan Stained Glass Census, a WKAR news report (March 2026), the City of
# Jackson's news page, and for service times the parishes' own pages. Pins are OpenStreetMap points, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'jackson_mi_phpi','label':'Michigan: old Jackson','added':'2026-11-28 13:49'}

DT=' Downtown Jackson has street parking and public lots; their hours and fees were not checked.'
SAH='https://sah-archipedia.org/buildings/MI-01-'
NR='https://npgallery.nps.gov/AssetDetail/NRIS/'

PLACES=[

N('first-congregational-church-jackson-mi','First Congregational Church','Jackson','mi','worship','standing',42.24817,-84.40911,'exact','open','walk','','1859–1860',
  'The congregation broke away from Jackson\'s first Presbyterian church in 1841. This, its second church, was designed by Horatio Nelson White of Syracuse, New York, and built by James Morwick, also of Syracuse: work began in 1859 and the church was dedicated on October 18, 1860. In 1871 the whole building was raised eight feet so that parlours, classrooms and a kitchen could be built underneath. A new entrance came in 1895 and a modern education wing in 1960. It stands on the one surviving quarter of the old Jackson town square, is a Michigan State Historic Site (1987) and has been on the National Register since 2017.',
  'A large reddish-brown brick church in the round-arched (Romanesque Revival) manner, with two towers of different heights either side of the projecting entrance, corbelled and buttressed walls, and round-headed stained glass windows that are original to the building. SAH Archipedia says the plain interior has three aisles before a central pulpit. The two-storey wing at the side is modern.',
  '',
  'A working church (First Congregational Church, United Church of Christ) at 120 North Jackson Street, at West Michigan Avenue; go in at a service. Its service times could not be read from its own page when this was written.'+DT,
  [W('First Congregational Church (Jackson, Michigan)'),['SAH Archipedia: First Congregational Church',SAH+'JA2']],
  brick='yes',bcol='red',hours='?',arch='Horatio Nelson White',builder='James Morwick',archw='Wikipedia and SAH Archipedia: designed by White of Syracuse, built by Morwick of Syracuse'),

N('st-pauls-episcopal-jackson-mi','St. Paul\'s Episcopal Church','Jackson','mi','worship','standing',42.24529,-84.40892,'exact','open','walk','','1850–1852',
  'Built in 1850 to 1852 by the builders Hubbell and Langdon to the design of Calvin N. Otis of Buffalo, New York. SAH Archipedia calls it one of Michigan\'s earliest churches in the Romanesque Revival manner, at a time when nearly every new Episcopal church was Gothic. Additions followed in 1865 and 1888, a parish house in 1898 and a Sunday school in 1965. The parish sold its first church to the Free Will Baptists in 1851. A Michigan State Historic Site since 1985.',
  'An orangish-tan brick church on a sandstone foundation, with helmeted square towers at the corners of the west front and round-arched windows set in corbelled panels. Inside are stained glass windows by Tiffany, by J. and R. Lamb of New York and others, and a Second World War memorial window by Paine-Spiers Studios (1946 to 1948). The church\'s own page mentions its organ and a chapel.',
  '',
  'A working Episcopal church at 309 South Jackson Street; anyone may come to a service. The times are from the parish\'s own page.'+DT,
  [['SAH Archipedia: St. Paul\'s Episcopal Church',SAH+'JA7'],['St. Paul\'s Episcopal Church','https://stpauljxmi.org/visitor-information/']],
  brick='no',bcol='buff',hours='Sunday 8 and 10:30 a.m.; a small service most Wednesdays at 12:15 p.m.',arch='Calvin N. Otis',builder='Hubbell and Langdon',archw='SAH Archipedia (Buildings of Michigan)'),

N('first-baptist-church-jackson-mi','First Baptist Church (former)','Jackson','mi','worship','standing',42.24635,-84.40848,'site','view','walk','','1870–1872',
  'A downtown church designed by J. R. Lewis of Jackson. The Michigan Stained Glass Census gives 1870 as the year it was built; a WKAR news report of March 2026 says the congregation had been in the building since it was built in 1872. Claude Sampson of Jackson altered it in 1950. After 187 years the First Baptist congregation closed: WKAR reported the last service for April 26, 2026 and the building for sale, its future unknown. A Michigan State Historic Site since 1984.',
  'A red brick church with two tall white spires, at the corner of South Jackson and West Cortland streets. The stained glass census lists 27 pictorial windows: the Good Shepherd, Christ in Gethsemane, and symbols such as an ark, a menorah, lilies and an all-seeing eye. Whether the windows are still there after the sale was not checked; the interior was not checked.',
  '',
  'At 201 South Jackson Street. The congregation has closed and the building was offered for sale in 2026: look from the street; who owns it now was not checked.'+DT,
  [['Michigan Stained Glass Census: First Baptist Church','https://michiganstainedglass.org/collections/building.php/id=208-792-639/'],['WKAR: Historic church closes, future of building is unknown (March 23, 2026)','https://www.wkar.org/wkar-news/2026-03-23/historic-church-closes-future-of-building-is-unknown']],
  conf='mixed',brick='yes',bcol='red',arch='J. R. Lewis',archw='Michigan Stained Glass Census: architect J.R. Lewis of Jackson; 1950 alterations by Claude Sampson'),

N('st-john-evangelist-jackson-mi','St. John the Evangelist Catholic Church','Jackson','mi','worship','standing',42.25449,-84.40366,'exact','open','walk','','1856',
  'Jackson\'s oldest Catholic parish. The parish says the cornerstone was laid in 1856 and that the church is the oldest church building in the Diocese of Lansing still in use. Since 2010 St. Joseph\'s, the other old Jackson parish, has been an oratory of St. John\'s. A Michigan State Historic Site since 1978, listed at 711 Cooper Street; Cooper Street there is now Martin Luther King Jr. Drive.',
  'A working Catholic church north of downtown. The fabric that survives and the interior were not checked.',
  '',
  'A working parish church on North Martin Luther King Jr. Drive (the old Cooper Street); anyone may come to Mass. The times are from the parish\'s own page. Parking was not checked.',
  [['St. John the Evangelist: church history','https://saintjohnjackson.org/church-history-st-john-the-evangelist/'],['St. John the Evangelist: Mass and confession times','https://saintjohnjackson.org/mass-and-confession-times/']],
  brick='?',hours='Saturday 4:15 p.m.; Sunday 8 and 10 a.m. and noon; Wednesday to Friday 9 a.m.'),

N('michigan-theatre-jackson-mi','Michigan Theatre','Jackson','mi','civic','standing',42.24814,-84.40623,'exact','open','walk','','1928–1930',
  'A movie palace built for W. S. Butterfield Theatres to the design of the Detroit architect Maurice H. Finkel, who also drew the Michigan Theater in Ann Arbor. It opened on April 30, 1930 for films and vaudeville, the first air-conditioned building in downtown Jackson. Butterfield ran it until 1978; the city took it over for unpaid taxes in 1993 and passed it that year to a non-profit, which still runs it. Renovations came in 2005 and 2022 to 2024. On the National Register since 1980.',
  'A narrow three-storey entrance block faced with cream-yellow terra-cotta, with gold, green and blue shields and swags, four arches on Churrigueresque columns and a hexagonal tower with a red tile roof; the red brick auditorium behind seats about 1,600. Wikipedia says the interior keeps lavish 1930 plasterwork. The marquee is a replacement (1989, now digital).',
  '',
  'A working theatre at 124 North Mechanic Street, owned by a non-profit; the inside is seen by buying a ticket to a film or show. Its box-office hours were not read.'+DT,
  [W('Michigan Theatre (Jackson, Michigan)'),['SAH Archipedia: Michigan Theatre',SAH+'JA3']],
  brick='some',bcol='red',hours='?',arch='Maurice H. Finkel',archw='Wikipedia and SAH Archipedia'),

N('hayes-hotel-jackson-mi','Hayes Hotel','Jackson','mi','hotel','standing',42.24783,-84.41041,'site','view','walk','','1924–1926',
  'A ten-storey hotel paid for by the Jackson Community Hotel Company, formed by Jackson\'s leading citizens in 1924, and designed by the Chicago firm Holabird & Roche. It opened in November 1926 with over 200 rooms, a ballroom and shops on the ground floor, near the Michigan Central station. Hotel business ended in 1975; Consumers Energy used it for offices, and the city bought it in 2000. Wikipedia says it stood empty until 2024, when the city was selling it to developers who planned 84 apartments with event space and shops. On the National Register since 2024.',
  'Smooth red brick with brick quoins, a granite water table, terra-cotta frames round the third-, fourth-, ninth- and tenth-floor windows and a gable at the top of the seven-bay front. Whether the conversion has been finished was not checked; the inside was not checked.',
  '',
  'A privately redeveloped building at 226 to 234 West Michigan Avenue; look from the street.'+DT,
  [W('Hayes Hotel')],
  brick='yes',bcol='red',arch='Holabird & Roche',archw='Wikipedia: the Chicago firm of Holabird & Roche'),

N('otsego-hotel-jackson-mi','Otsego Hotel (Otsego Apartments)','Jackson','mi','hotel','standing',42.24722,-84.40444,'site','view','walk','','1902–1904',
  'Built by the heirs of Henry Haden on the site of the Hibbard House, an 1865 hotel they pulled down in 1901. Work began in 1902 and the Otsego, named for Otsego Lake in New York near Haden\'s birthplace, opened early in 1904. It was renovated in 1918 and given a six-storey addition in 1929, closed as a hotel in 1962, was a missionary school in the 1970s and since 1981 has been subsidised housing, now for older people. On the National Register since 2015.',
  'A five-storey brick hotel block with a six-storey addition along the street; the colour of the brick and what is left inside were not checked.',
  '',
  'A private apartment building for older residents at 102 to 106 Francis Street (now Martin Luther King Jr. Drive) by West Michigan Avenue; look from the street and do not go in.'+DT,
  [W('Otsego Apartments')],
  brick='?'),

N('commercial-exchange-jackson-mi','Collins Manufacturing–Jackson Automobile Company complex (Commercial Exchange Building)','Jackson','mi','industry','standing',42.25268,-84.37495,'site','view','drive','','1895–1909',
  'Collins Manufacturing made wagons, carts, surreys, sleighs and buggies here from 1885; when its factory burned in 1895 it built the great U-shaped building that stands now the same year. The National Wheel Company took over in 1897, and in 1908 the Jackson Automobile Company bought the works and built cars here until 1922, adding three buildings in 1908 and 1909. Later tenants made neon signs, radio tubes and radios (Sparks-Withington, later Sparton, until the late 1950s). Renamed the Commercial Exchange Building in 1961, it is leased to many tenants. On the National Register since 1993.',
  'Building A (1895) is three storeys of red brick round a courtyard, 27 bays long on East Michigan Avenue, with segmental-arched windows and a six-storey corner tower holding the main door, which was remodelled in Art Deco style in 1930 with brass doors and limestone panels. Buildings B, C and D (about 1908 and 1909) are brick too.',
  '',
  'Private business premises at 2301 East Michigan Avenue at Horton Street, east of downtown; look from the street. The lots round it are the tenants\'.',
  [W('Commercial Exchange Building (Jackson, Michigan)'),['The Commercial Exchange','https://thecommercialexchange.com/']],
  brick='yes',bcol='red'),

N('michigan-state-prison-jackson-mi','Michigan State Prison (Armory Arts Village)','Jackson','mi','inst','standing',42.25633,-84.40591,'site','view','walk','','1842–1920s',
  'Michigan\'s first prison opened in Jackson in 1839, and its first permanent building went up in 1842. Inmates slept here and worked by day making binder twine, farm implements and furniture; the prison was overcrowded almost from the start, holding about 2,200 men at its peak. In 1926 the prisoners began to move to a new prison north of the city, and the old site became a National Guard armory. In 2007 and 2008 it was turned into Armory Arts Village, with sixty-two loft apartments for artists. On the National Register since 1979.',
  'SAH Archipedia says the stone walls and guard towers of the prison remain, with the gable-roofed west cell block of 1842 that once held 328 tiny cast-iron cells. What can be seen from outside the walls was not checked.',
  '',
  'Housing and studios at 100 Armory Court, off North Mechanic Street; look at the walls and towers from the public streets, and go inside only to a gallery or event that is open to the public.',
  [W('Michigan State Prison'),['SAH Archipedia: Jackson Armory Arts Village',SAH+'JA10'],['National Register record',NR+'79001156']],
  brick='?',arch='Scott & Co.; Robert Lake',archw='National Register record: architects "Scott & Co. Lake, Robert"'),

N('stone-post-office-jackson-mi','Stone Post Office (Blackwell Building)','Jackson','mi','civic','standing',42.24806,-84.40833,'site','view','walk','','1839',
  'Built in 1839 by Joseph G. R. Blackwell, a wealthy businessman, as his general store facing the town\'s small public square. It later held the post office until 1894, when the town outgrew it. Bigger buildings rose round it and left it at the back of the lot, and it has mostly been a warehouse since. On the National Register since 1972.',
  'Wikipedia describes a two-storey sandstone building with six pillars and two engaged columns across the ground floor of what was its front, nineteen boarded windows and five doors, joined at one end to the building on North Jackson Street. How much of it can be seen from a public way was not checked.',
  '',
  'Behind 125 North Jackson Street; part of a private business. Look from the street or alley only.'+DT,
  [W('Stone Post Office'),['National Register record',NR+'72000623']],
  brick='no',bcol='none',builder='Joseph G. R. Blackwell',archw='Wikipedia: built by Blackwell; the National Register record names him as architect'),

N('jackson-high-school-mi','Jackson High School','Jackson','mi','civic','standing',42.25027,-84.41886,'exact','view','walk','','1926–1927',
  'Jackson\'s west and east high schools merged in 1908, and this building was put up in 1926 and 1927 to the design of Childs & Smith. Its 1,800-seat auditorium was the largest in the city when it opened. In the late 1990s the architects Dabbert and Fleming found it cheaper to renew the building than to build a new school, and voters approved the work in 1999; it was done in 2000 to 2003.',
  'A three-storey Collegiate Gothic school of brown brick trimmed with limestone, with a tall pinnacled tower over the central entrance. SAH Archipedia says Britten Hall, the two-storey "Shakespeare Room" with leaded-glass windows, survives inside.',
  '',
  'A working public high school at 544 Wildwood Avenue; look from the street, and do not go onto the grounds during school hours.',
  [['SAH Archipedia: Jackson High School',SAH+'JA8']],
  brick='no',bcol='dark',arch='Childs & Smith',archw='SAH Archipedia (Buildings of Michigan)'),

N('jackson-post-office-1933-mi','Former U.S. Post Office (Consumers Energy)','Jackson','mi','civic','standing',42.24668,-84.40224,'site','view','walk','','1932–1933',
  'The post office of 1932 and 1933, designed by Claire Allen of Jackson with Russell Allen, who won a national competition for it; the work was supervised by James Wetmore, Supervising Architect of the Treasury. In 2001 to 2003 Consumers Energy made it the grand entrance of its new headquarters.',
  'A wedge-shaped building fitted to a triangular site, clad in smooth Indiana limestone over a granite base, with an entrance portico of six Roman Doric columns on its concave west front. A twelve-storey office tower of 2003 stands behind it.',
  '',
  'Company offices at Michigan Avenue and Francis Street (now Martin Luther King Jr. Drive); look from the street. The grounds by the Grand River are part of a public walk, but their hours were not checked.'+DT,
  [['SAH Archipedia: Consumers Energy\'s Corporate Headquarters (U.S. Post Office)',SAH+'JA5']],
  brick='no',bcol='none',arch='Claire Allen; Russell Allen',archw='SAH Archipedia: Claire Allen with Russell Allen (Allen and Sons of Jackson)'),

]

PIN_NOTES={
 'first-congregational-church-jackson-mi':'OpenStreetMap place of worship for the First Congregational Church, looked at on the aerial.',
 'st-pauls-episcopal-jackson-mi':'OpenStreetMap address point for 309 South Jackson Street, looked at on the aerial.',
 'first-baptist-church-jackson-mi':'The church building at South Jackson and West Cortland streets, moved off the street from the address point after a look at the aerial.',
 'st-john-evangelist-jackson-mi':'OpenStreetMap place of worship for St. John the Evangelist, looked at on the aerial.',
 'michigan-theatre-jackson-mi':'OpenStreetMap point of the Michigan Theater on North Mechanic Street, looked at on the aerial.',
 'hayes-hotel-jackson-mi':'The tall white-roofed building on the north side of West Michigan Avenue at 226 to 234, by the point the National Register list gives; moved off the street after a look at the aerial.',
 'otsego-hotel-jackson-mi':'The point Wikipedia gives for the Otsego Apartments, looked at on the aerial.',
 'commercial-exchange-jackson-mi':'OpenStreetMap building at 2301 East Michigan Avenue, looked at on the aerial.',
 'michigan-state-prison-jackson-mi':'OpenStreetMap address point for 100 Armory Court, in the middle of the old prison site; which building is the 1842 cell block was not settled on the aerial.',
 'stone-post-office-jackson-mi':'The point Wikipedia gives, behind the buildings on the east side of North Jackson Street; the stone building itself could not be picked out on the aerial.',
 'jackson-high-school-mi':'The main school building south of the playing fields, moved from a parking lot after a look at the aerial; which wing holds the tower was not checked.',
 'jackson-post-office-1933-mi':'OpenStreetMap building at 1 Energy Plaza: the pin is on the headquarters, and the old post office is its low limestone front on the west side; the two could not be told apart on the aerial.',
}
