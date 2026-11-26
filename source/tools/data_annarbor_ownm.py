# November 26, 2026: Ann Arbor, Michigan. A "videos" session (PROMPTS.md job 9): the names came from one video's tour of
# old Ann Arbor and University of Michigan buildings (the record is source/videos/20230726_PVgwIMM2rr8.md); the video is a
# tip and nothing here rests on it. Sources read: Wikipedia (each article named in the links), SAH Archipedia (Buildings of
# Michigan, 2012), the Ann Arbor District Library's "Historic Buildings, Ann Arbor, Michigan" pages and an Ann Arbor News
# caption it holds, and for hours the pages of the Hands-On Museum, the Kelsey Museum and the three parishes. Pins are
# OpenStreetMap points and buildings, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'annarbor_ownm','label':'Michigan: old Ann Arbor','added':'2026-11-26 12:36'}

DT=' Downtown parking is in public parking structures, lots and street meters; their hours and fees were not checked.'
UM=' The University of Michigan\'s own lots need a permit; park in a downtown structure (Maynard Street, Liberty Square) and walk. Fees not checked.'
SAH='https://sah-archipedia.org/buildings/MI-01-'
AADL='https://aadl.org/'

PLACES=[

N('ann-arbor-central-fire-station','Ann Arbor Central Fire Station (Hands-On Museum)','Ann Arbor','mi','civic','standing',42.28171,-83.74654,'site','open','walk','','1882–1883',
  'The city\'s main firehouse from 1882 to 1978. When the aldermen set aside $10,000 for it in 1882 the local press called the sum extravagant for a city of fewer than 10,000 people. William Scott and Company of Detroit drew it, and it was finished in 1883; the first professional firemen were hired in 1888 and horses gave way to motor engines in 1915. The fire department moved to a new station on the same block in 1978, and the Ann Arbor Hands-On Museum opened in the old firehouse in 1982. On the National Register since 1972.',
  'A polychrome brick building with stone trim and corbelled brick, three pedimented engine doors with round- and segmental-arched windows grouped in threes above, gabled wall dormers, and an Italianate hose and bell tower on the corner of Huron Street and Fifth Avenue. The museum\'s large addition of 1999 and 2000 sits behind. Inside it is a children\'s science museum.',
  '',
  'A private science museum at 220 East Ann Street (the old firehouse faces Huron Street at Fifth Avenue). Admission was $16 for adults and children when read, babies free; the hours are from the museum\'s page.'+DT,
  [W('Ann Arbor Hands-On Museum'),['SAH Archipedia: Ann Arbor Central Fire Station',SAH+'WA1'],['Ann Arbor Hands-On Museum','https://discoverscienceandnature.org/aahom']],
  brick='yes',hours='Tuesday to Sunday 10 a.m. to 5 p.m.; closed Monday'),

N('detroit-observatory-ann-arbor','Detroit Observatory','Ann Arbor','mi','inst','standing',42.28198,-83.73168,'exact','open','walk','','1854',
  'The University of Michigan\'s first scientific research building, put up in 1854 with money raised mostly from citizens of Detroit, hence the name. It held a 12⅝-inch refracting telescope by Henry Fitz, the third largest refractor in the world when it was installed in 1857, and a meridian circle from Berlin. Later wings were added and then taken down (the director\'s house in 1954, the 1908 wing in 1976). The astronomers left in 1963, the building fell derelict and was threatened with demolition, and it was restored in 1997 and 1998; it reopened in 2022 after an addition was built.',
  'A small Greek Revival and Italianate building with a dome, on a rise at Ann and Observatory streets. The 1857 Fitz telescope is still in the dome. Inside by its public open hours and events.',
  '',
  'Run by the University of Michigan\'s Bentley Historical Library, at 1398 East Ann Street; the entrance is on Observatory Street. Its own page could not be opened when this was written; event listings show free Saturday open houses, so check its calendar before going.'+UM,
  [W('Detroit Observatory'),['Detroit Observatory','https://detroitobservatory.umich.edu/visit/']],
  brick='?',hours='?'),

N('first-national-bank-building-ann-arbor','First National Bank Building','Ann Arbor','mi','civic','standing',42.28033,-83.74817,'exact','view','walk','','1927–1930',
  'A ten-storey bank and office building at Main and Washington streets, designed by the Ann Arbor firm of Fry and Kasurin for the First National Bank, the first bank in Washtenaw County (founded 1863). Begun in 1927 and finished in 1930, it was then the tallest building in Ann Arbor. The bank merged and moved out in 1936; the building was renovated in 1982. On the National Register since 1982.',
  'A steel-framed tower clad in pale terra-cotta made by the Northwestern Terra Cotta Company, with broad vertical lines and gargoyles under a decorative cornice near the top. Offices and shops; the inside was not checked.',
  '',
  'A private office building at 201–205 South Main Street; seen from the street.'+DT,
  [W('First National Bank Building (Ann Arbor, Michigan)'),['Ann Arbor District Library: First National Bank Building',AADL+'buildings_hhaa087']],
  brick='no'),

N('michigan-central-depot-ann-arbor','Michigan Central Railroad Depot (Gandy Dancer)','Ann Arbor','mi','rail','standing',42.28719,-83.74169,'exact','open','walk','stations','1886',
  'The Michigan Central came through Ann Arbor in 1839. This depot, by Frederick Spier of the Detroit firm Spier and Rohns, was finished in 1886, and the local Courier called it the finest station between Buffalo and Chicago. Thirteen Detroit to Chicago trains a day stopped in 1915. In 1970 the railroad sold it to the restaurateur Chuck Muer, who opened the Gandy Dancer restaurant in it; the space to the old baggage room was enclosed in 1976. On the National Register since 1975.',
  'Richardsonian Romanesque in rock-faced granite fieldstone, quarried at Four Mile Lake between Chelsea and Dexter: a squat tower and turret, deep round arches, a high gabled roof with eyelid dormers. The original waiting room had a red oak ceiling and trim, French tile floors, stained glass and a terra-cotta fireplace; whether all of it survives was not checked. Go in as a diner.',
  '',
  'A private restaurant at 401 Depot Street, beside the working railroad; stay off the tracks. Its own page could not be opened when this was written, so its hours were not checked.',
  [W('Ann Arbor station (Michigan Central Railroad)'),['SAH Archipedia: Gandy Dancer',SAH+'WA4']],
  brick='no',hours='?'),

N('nickels-arcade-ann-arbor','Nickels Arcade','Ann Arbor','mi','civic','standing',42.27836,-83.74139,'exact','open','walk','','1915–1918',
  'A covered shopping arcade built from 1915 to 1918 for Tom E. Nickels on the site of his grandfather\'s meat market, designed by the Ann Arbor architect Herman Pipp. The first tenant, the Farmers and Mechanics Bank, moved in in 1915; the war delayed the rest. It may be the only free-standing arcade of its kind left in Michigan. On the National Register since 1987.',
  'A 261-foot skylit passage from State Street through to Maynard Street, with two storeys of small shops and offices facing it. The State Street front is a three-storey open portico in buff glazed terra-cotta; the Maynard Street end is yellow brick; the floor is square red tile in black borders under a glass gable roof.',
  '',
  'A private arcade of shops at 326–330 South State Street; walk through it when the shops are open (their hours were not checked). The Maynard Street parking structure is at the back.'+DT,
  [W('Nickels Arcade'),['SAH Archipedia: Nickels Arcade',SAH+'WA6']],
  brick='no',hours='?'),

N('first-unitarian-church-ann-arbor','First Unitarian Church (100 North State Street)','Ann Arbor','mi','worship','standing',42.28142,-83.74056,'exact','view','walk','','1881–1882',
  'Built in 1881 and 1882 for the First Unitarian Society under its pastor Jabez Sunderland, to the design of the Detroit firm of Donaldson and Meier, with the stonework by the Walker Brothers of Ann Arbor. A student centre was added in 1920. The Unitarians moved out in 1946; two other congregations followed, and in 1985 the run-down building was renovated as offices for the architects Hobbs and Black. On the National Register since 1978.',
  'A two-storey Richardsonian Romanesque church of ashlar with bands of darker stone, a cross-gabled roof and a square turreted tower at the back. During the 1985 renovation an 1890s Tiffany window, covered over in the 1930s, was found. Offices now; seen from the street.',
  '',
  'A private office building at 100 North State Street, at Huron Street; seen from the street.'+DT,
  [W('Unitarian Universalist Church (Ann Arbor, Michigan)')],
  brick='no'),

N('hill-auditorium-ann-arbor','Hill Auditorium','Ann Arbor','mi','civic','standing',42.27918,-83.73908,'exact','open','walk','','1913',
  'The University of Michigan\'s great concert hall, paid for by a $200,000 bequest from the regent Arthur Hill and opened in 1913. Albert Kahn and Ernest Wilby designed it, with the acoustics by Hugh Tallant of New York, who shaped the hall like a megaphone so that every seat would hear the stage. It was restored in 2002 to 2004, with fewer seats and the original pale blue, grey, orange and gold paint, the lights and the pipe organ brought back.',
  'A massive block with a row of engaged Doric columns framing the stone entrance; red and brown patterned brick laid in English bond, with terra-cotta and limestone trim. Inside, a fan-shaped hall of about 3,500 seats and a large pipe organ: go in for a concert, lecture or recital.',
  '',
  'Owned by the University of Michigan, at 825 North University Avenue; it opens for performances, whose times are on the university\'s and the University Musical Society\'s calendars (not checked).'+UM,
  [W('Hill Auditorium'),['SAH Archipedia: Hill Auditorium',SAH+'WA7.1']],
  brick='yes',hours='?'),

N('burton-memorial-tower-ann-arbor','Burton Memorial Tower','Ann Arbor','mi','landmark','standing',42.27942,-83.73871,'exact','view','walk','','1935–1936',
  'A carillon tower built in 1935 and 1936 in memory of Marion Leroy Burton, the university\'s president from 1920 to 1925. Albert Kahn designed it, after an unbuilt scheme by Eliel Saarinen. The carillon was given by Charles Baird, the university\'s first athletic director. Wikipedia gives 53 bells weighing 43 tons, the world\'s fourth heaviest; Buildings of Michigan gives a one-hundred-ton carillon of sixty-seven bells, so the count is not settled. The rest of the tower holds music classrooms and offices.',
  'An Art Deco tower of reinforced concrete faced with limestone, about 42 feet square at the base, with setbacks near the top and a clock. It chimes the quarter hours. Carl Milles\'s fountain of Triton and his children (1940) is on the mall to the north. The inside was not checked.',
  '',
  'University of Michigan, 230 South Ingalls Street; seen from the campus walks and Ingalls Mall.'+UM,
  [W('Burton Memorial Tower'),['SAH Archipedia: Burton Memorial Tower',SAH+'WA7.2']],
  brick='no',conf='mixed'),

N('law-quadrangle-ann-arbor','Law School Quadrangle','Ann Arbor','mi','inst','standing',42.27420,-83.73960,'site','view','walk','','1923–1933',
  'Four Collegiate Gothic buildings round a courtyard, the gift of the alumnus William Wilson Cook: the Lawyers\' Club (1924), the John P. Cook dormitory (1930), the William W. Cook Legal Research Building (1931) and Hutchins Hall (1933). The New York firm of York and Sawyer designed them on the model of the Oxford and Cambridge colleges and the Inns of Court; Jacob Van Heiningen of Pitkin and Mott laid out the grounds. An underground addition to the library went in at the corner of the courtyard in 1978 to 1981.',
  'Rock-faced granite from Weymouth, Massachusetts, trimmed with Indiana limestone and grown with ivy; slate roofs, buttresses with pinnacles, a turreted gate tower on the north, oriel bays and traceried windows of stained glass. The library\'s main reading room, panelled in oak with great stained-glass windows bearing university crests, is likened to King\'s College Chapel; the Lawyers\' Club dining hall has a hammer-beam roof. Whether visitors may go inside was not checked.',
  '',
  'University of Michigan, bounded by South State Street, South University Avenue, Tappan and Monroe streets; seen from the streets round it. Whether the courtyard and buildings are open to visitors was not checked.'+UM,
  [W('University of Michigan Law School'),['SAH Archipedia: Law School Quadrangle',SAH+'WA7.7']],
  brick='no'),

N('clements-library-ann-arbor','William L. Clements Library','Ann Arbor','mi','civic','standing',42.27547,-83.73800,'exact','open','walk','','1922–1923',
  'A rare-book library of early American history, founded in 1923 by the regent William L. Clements with his own collection. Albert Kahn and Ernest Wilby designed the building in a late Italian Renaissance manner, perhaps after Vignola\'s casino in the gardens of the Villa Farnese at Caprarola; it was said to be Kahn\'s favourite of all his buildings.',
  'Indiana limestone, approached up a broad stepped terrace to a triple arcade on two slender Corinthian columns, a loggia once tiled with vaulted ceilings in gold and blue mosaic, and three bronze doors with grilles. Exhibits from the collection are shown to the public on weekday afternoons.',
  '',
  'University of Michigan, 909 South University Avenue. The hours are the exhibits page\'s, as quoted in search results (the page would not open); research is by appointment.'+UM,
  [W('William L. Clements Library'),['SAH Archipedia: Clements Library',SAH+'WA7.6'],['Clements Library: exhibits','https://clements.umich.edu/public-programs/exhibits']],
  brick='no',hours='Exhibits Monday to Friday noon to 4 p.m.'),

N('michigan-union-ann-arbor','Michigan Union','Ann Arbor','mi','inst','standing',42.27517,-83.74151,'exact','open','walk','','1917',
  'The university\'s student union, a club founded in 1904 that first met in the old Waterman Gymnasium and moved into Judge Thomas Cooley\'s fieldstone house on this corner in 1907. The Chicago architects Irving and Allen Pond designed a new building; the Cooley house came down in 1916 and the new union was built in 1917. Until the Michigan League opened in 1929 women could enter only by the north door with a man.',
  'A large building at State Street and South University Avenue, now with restaurants, study rooms and meeting rooms; a renovation enclosed the old first-floor courtyard and restored the windows. What the building is faced with was not checked.',
  '',
  'University of Michigan, 530 South State Street; its own hours page could not be opened when this was written.'+UM,
  [W('Michigan Union')],
  brick='?',hours='?'),

N('angell-hall-ann-arbor','Angell Hall','Ann Arbor','mi','inst','standing',42.27672,-83.73975,'exact','view','walk','','1920–1924',
  'The main building of the College of Literature, Science, and the Arts, named for James Burrill Angell, president from 1871 to 1909. Albert Kahn designed it as part of the 1920 campus plan; it was begun in 1920 and finished in 1924 for about $1 million. A 1952 addition replaced the 1841 Mason Hall and old Haven Hall, burned in 1950. The first teach-in against the Vietnam War was held here on March 24, 1965.',
  'A great Classical Revival front of pale stone on State Street with a giant Doric portico. A student observatory is on the fifth-floor roof. The inside was not checked.',
  '',
  'University of Michigan, 435 South State Street; seen from State Street and the Diag.'+UM,
  [W('Angell Hall'),['SAH Archipedia: University of Michigan Central Campus',SAH+'WA7']],
  brick='no'),

N('yost-field-house-ann-arbor','Yost Field House (Yost Ice Arena)','Ann Arbor','mi','inst','standing',42.26758,-83.74102,'exact','view','walk','','1923',
  'Built in 1923 as the university\'s field house and named for the football coach and athletic director Fielding H. Yost. The men\'s basketball team played here until 1967 and the track teams used it until 1973, when it was turned into the ice arena of the Michigan hockey team. It has been renovated several times since 1996.',
  'A long field house on South State Street. The inside is a hockey arena, seen at games; it was not checked.',
  '',
  'University of Michigan Athletics, 1116 South State Street; seen from the street, or inside at a game (tickets and times not checked).'+UM,
  [W('Yost Ice Arena')],
  brick='?'),

N('newberry-hall-kelsey-museum-ann-arbor','Newberry Hall (Kelsey Museum of Archaeology)','Ann Arbor','mi','inst','standing',42.27685,-83.74099,'site','open','walk','','1888',
  'Built in 1888 for the Students\' Christian Association, for religious services and meetings, to the design of Spier and Rohns of Detroit; Helen Newberry gave $18,000 toward it. The university leased it in 1921, kept its collection of ancient objects here from 1928, and bought it in 1937. The collection, begun by the Latin professor Francis Kelsey in 1893, now holds over 100,000 objects from the Mediterranean and the Near East, shown since 2009 in a new wing behind. On the National Register since 1972.',
  'A Richardsonian Romanesque hall of rough grey stone with a round corner turret, on State Street. The galleries, in the Upjohn wing at the back, hold Egyptian, Greek and Roman objects, among them a painted mummy, Roman glass and brick stamps, and 1920s watercolour copies of the Villa of the Mysteries murals at Pompeii. Free.',
  '',
  'University of Michigan, 434 South State Street; the public door is on Maynard Street. Free, no ticket; hours from the museum\'s page. Open late (to 7:30 p.m.) on the third Thursday of each month.'+UM,
  [W('Kelsey Museum of Archaeology'),['Kelsey Museum: visit','https://prod.lsa.umich.edu/kelsey/visit.html']],
  brick='no',hours='Tuesday to Friday 10 a.m. to 4 p.m.; Saturday and Sunday 11 a.m. to 4 p.m.; closed Monday'),

N('st-thomas-apostle-church-ann-arbor','St. Thomas the Apostle Church','Ann Arbor','mi','worship','standing',42.28519,-83.74133,'exact','open','walk','','1897–1905',
  'The Catholic parish of Ann Arbor, whose first church of 1842 to 1845 was the town\'s first brick church. Father Edward Kelly began raising money in 1896 for a larger one, by Spier and Rohns of Detroit: the cornerstone went in in 1897, it was dedicated in 1899 and finished in 1905. The yellow brick rectory came in 1902 and the convent in 1911. It is a Michigan State Historic Site.',
  'A Richardsonian Romanesque church of local fine-grained rough-cut granite on a cross-shaped plan, with a rose window inside. A working parish church: go in at Mass.',
  '',
  'A working Catholic parish at 530 Elizabeth Street, at Kingsley Street; the Mass times are from the parish\'s own page.'+DT,
  [W('St. Thomas the Apostle Catholic Church (Ann Arbor, Michigan)'),['St. Thomas the Apostle Parish','https://sta2.org/church']],
  brick='no',hours='Saturday 4:30 p.m.; Sunday 7:30, 9:30, 11:30 a.m. (Latin), 6 p.m.; Monday 7 a.m.; Tuesday to Friday 7, 8 a.m., noon; Saturday 9 a.m.'),

N('st-andrews-episcopal-ann-arbor','St. Andrew\'s Episcopal Church','Ann Arbor','mi','worship','standing',42.28339,-83.74322,'exact','open','walk','','1868–1869',
  'An Episcopal parish founded in the 1820s (sources give 1827 and 1828). Its stone church, designed by the Detroit architect Gordon W. Lloyd, was begun in 1868 and finished the following year; an Ann Arbor News caption of 1973 called it the oldest church building surviving in Ann Arbor. The tower was added in 1903 in keeping with the first design, a bequest of Mrs. Alonzo Palmer. It anchors the Division Street historic district.',
  'An English Gothic church of stone at Division and Catherine streets, with its 1903 tower. A working church: go in at a service. The interior was not checked.',
  '',
  'A working Episcopal parish at 306 North Division Street; the service times are from the parish\'s own page.'+DT,
  [['Ann Arbor District Library: St. Andrew\'s Episcopal Church (Ann Arbor News, 1973)',AADL+'node/350640'],['St. Andrew\'s Episcopal Church','https://standrewsaa.org/']],
  brick='no',conf='mixed',hours='Sunday 8, 9:15 and 10 a.m., Compline 5 p.m.; Wednesday 7 a.m. and Evensong 6 p.m.; Friday 12:15 p.m.'),

N('first-congregational-church-ann-arbor','First Congregational Church','Ann Arbor','mi','worship','standing',42.27757,-83.74136,'exact','view','walk','','1872–1876',
  'A congregation formed in 1847 by members who left the Presbyterian church, largely over its stand on slavery. Its church at State and William streets, by Gordon W. Lloyd of Detroit (the architect of St. Andrew\'s), was begun in 1872 and dedicated on May 10, 1876. The Douglas Memorial Chapel and parish house, named for the minister and novelist Lloyd C. Douglas (The Robe), were finished in 1953.',
  'Gothic, in multi-coloured cut fieldstone and Indiana limestone, under an elaborate slate roof patterned with lozenges in contrasting colours. Inside are wooden hammer or collar beams, 21 stained glass windows added in 1946 and a Wilhelm tracker organ installed in the 1980s. The church\'s own page could not be opened when this was written, so its service times were not checked.',
  '',
  'A working church at 608 East William Street, at State Street; seen from the street. The Maynard Street parking structure is a block north.'+DT,
  [['Ann Arbor District Library: First Congregational Church, 1872-1876',AADL+'node/236329']],
  brick='no'),

N('bethlehem-church-ann-arbor','Bethlehem United Church of Christ','Ann Arbor','mi','worship','standing',42.27703,-83.74700,'exact','open','walk','','1894–1896',
  'A German congregation gathered in 1833 by Frederich Schmid from Basel, which the State of Michigan recognises as the oldest German church in the state. After a split in 1874 that formed Zion Lutheran, the members built this church in 1895 to the design of Richard Rasemann of Detroit; it was dedicated in January 1896. Sources differ on the start: the library\'s page gives 1895, the church gives a cornerstone of 1894. An annex in matching style followed in 1935. It is on the State Register.',
  'Native fieldstone in a Richardsonian Romanesque manner with Gothic touches; a state marker stands in front. A working church: go in at the Sunday service. The interior was not checked.',
  '',
  'A working church at 423 South Fourth Avenue; the service time is from the church\'s own page.'+DT,
  [['Ann Arbor District Library: Bethlehem Church, 1895-96',AADL+'buildings_hhaa046'],['Bethlehem United Church of Christ','https://www.bethlehem-ucc.org/']],
  brick='no',conf='mixed',hours='Sunday 10 a.m.'),

N('main-street-post-office-ann-arbor','Main Street Post Office (Washtenaw County Administration Building)','Ann Arbor','mi','civic','standing',42.28286,-83.74806,'exact','view','walk','','1906–1909',
  'Ann Arbor\'s post office from 1909, built on the site of a livery stable to plans by the staff of the United States Treasury, under the architect Fremont Ward; additions in 1928 and 1932 to 1933 matched the old work. It was the main post office until 1959 and a branch until 1977. Washtenaw County bought and renovated it, and its offices moved in in 1981. On the National Register since 1978.',
  'A federal-style post office of 1909 with its matching 1930s additions. County offices inside; the interior was not checked.',
  '',
  'Owned by Washtenaw County, 220 North Main Street; seen from the street.'+DT,
  [W('Washtenaw County Administration Building')],
  brick='?'),

]

PIN_NOTES={
 'ann-arbor-central-fire-station':'OpenStreetMap point of the Hands-On Museum, looked at on the aerial: it falls on the museum\'s addition; the old firehouse is the corner at Huron Street and Fifth Avenue, so the pin marks the site.',
 'detroit-observatory-ann-arbor':'OpenStreetMap point of the Detroit Observatory, 1398 East Ann Street, looked at on the aerial.',
 'first-national-bank-building-ann-arbor':'OpenStreetMap building of the First National Bank Building, looked at on the aerial.',
 'michigan-central-depot-ann-arbor':'OpenStreetMap point of the Gandy Dancer, 401 Depot Street, looked at on the aerial.',
 'nickels-arcade-ann-arbor':'OpenStreetMap point of Nickels Arcade, 326 South State Street, looked at on the aerial.',
 'first-unitarian-church-ann-arbor':'OpenStreetMap point for 100 North State Street, looked at on the aerial.',
 'hill-auditorium-ann-arbor':'OpenStreetMap point of Hill Auditorium, looked at on the aerial.',
 'burton-memorial-tower-ann-arbor':'OpenStreetMap point of Burton Memorial Tower, looked at on the aerial.',
 'law-quadrangle-ann-arbor':'The courtyard in the middle of the quadrangle, between the OpenStreetMap buildings of Hutchins Hall, the Cook library and the Lawyers\' Club; looked at on the aerial.',
 'clements-library-ann-arbor':'OpenStreetMap point of the William L. Clements Library, looked at on the aerial.',
 'michigan-union-ann-arbor':'OpenStreetMap point of the Michigan Union, 530 South State Street, looked at on the aerial.',
 'angell-hall-ann-arbor':'OpenStreetMap building of Angell Hall, looked at on the aerial.',
 'yost-field-house-ann-arbor':'OpenStreetMap point of Yost Ice Arena, looked at on the aerial.',
 'newberry-hall-kelsey-museum-ann-arbor':'OpenStreetMap building of the Kelsey Museum, 434 South State Street; the old hall and the new wing join, so the pin marks the site.',
 'st-thomas-apostle-church-ann-arbor':'OpenStreetMap building of Saint Thomas Catholic Church, looked at on the aerial.',
 'st-andrews-episcopal-ann-arbor':'OpenStreetMap point of Saint Andrew\'s Episcopal Church, 306 North Division Street, looked at on the aerial.',
 'first-congregational-church-ann-arbor':'OpenStreetMap point of the First Congregational Church, 608 East William Street, looked at on the aerial.',
 'bethlehem-church-ann-arbor':'OpenStreetMap point of Bethlehem United Church of Christ, 423 South Fourth Avenue, looked at on the aerial.',
 'main-street-post-office-ann-arbor':'OpenStreetMap building of the Washtenaw County Administration Building, 220 North Main Street, looked at on the aerial.',
}
