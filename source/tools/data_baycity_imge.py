# November 28, 2026: Bay City, Michigan. A "videos" session (PROMPTS.md job 9): the names came from one video's tour of
# old Bay City buildings (the record is source/videos/20260424_00xc5Vx6vNY.md); the video is a tip and nothing here
# rests on it. Sources read: Wikipedia (each article named in the links), SAH Archipedia (Buildings of Michigan, 2012),
# the Bay County Historical Society's pages, Route Bay City (Second Wave Media) walking-tour articles, the Shearer Block
# condominium association's history page, a Michigan Building Trades report on the Crapo Building, the Our Lady of
# Czestochowa parish pages, the Bay County Library System's Sage branch page, and a Michigan historical marker's text as
# printed by Lost in Michigan. Pins are address points, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'baycity_imge','label':'Michigan: old Bay City','added':'2026-11-28 05:42'}

DT=' Downtown parking is on the street and in city lots; their hours and fees were not checked.'
SAH='https://sah-archipedia.org/buildings/MI-01-'
RBC='https://secondwavemedia.com/baycity/features/'

PLACES=[

N('bay-city-hall-mi','Bay City Hall','Bay City','mi','civic','standing',43.59341,-83.88908,'exact','open','walk','','1894–1897',
  'Voters approved a new city hall in 1889; the local architects Leverett A. Pratt and Walter Koeppe were hired in 1892, the cornerstone went down in 1894, and the building was finished in 1897 for $175,000. It is Richardsonian Romanesque, of granite and pale Berea sandstone from Amherst, Ohio, with a clock and bell tower about 180 feet high at one corner. It was restored in the late 1970s. A roofing job in 2010 started a large fire; the building was shut for three years, renovated for about $10 million and reopened in 2013. It is still the seat of city government. On the National Register since 1975.',
  'The tower with a clock face on each side, round arches and heavy stone mullions. Inside, a four-storey atrium rises about 65 feet to a skylight, with a cast-iron stair whose banister is elaborately scrolled, and much ornamental metal and woodwork. City offices; the hours they are open to the public were not checked.',
  '',
  'Owned and used by the City of Bay City, at 301 Washington Avenue on the east bank of the Saginaw River. The city\'s own site could not be opened when this was written, so office hours were not checked.'+DT,
  [W('City Hall (Bay City, Michigan)'),['SAH Archipedia: Bay City Hall',SAH+'BY1']],
  brick='no',hours='?',arch='Pratt and Koeppe',archw='SAH Archipedia (Leverett A. Pratt and Walter Koeppe) and Wikipedia'),

N('bay-city-masonic-temple','Bay City Masonic Temple','Bay City','mi','civic','standing',43.59693,-83.88429,'exact','view','walk','','1890–1893; rebuilt 1903–1905',
  'Built for Bay City\'s Masonic lodges to the design of the local firm Pratt and Koeppe: begun in 1890, cornerstone in 1891, finished in February 1893. An electrical fire in May 1903 gutted it, destroying the roof, a 114-foot tower and three Moorish domes and leaving only the walls; the Masons rebuilt it to somewhat different plans and rededicated it in November 1905. A Scottish Rite cathedral was added beside it in 1926. With membership falling, demolition was considered in 2004; the Bay City Arts Council bought it in 2005, and friends of the building have since repaired the roof and use it for the arts. On the National Register since 2016.',
  'A three-storey red-brown sandstone building in the Moorish Revival manner with Richardsonian touches, on a rusticated base. The onion domes over the entrance and the corner bays are gone. Look for the horseshoe-arched windows, the stained-glass lunette over the door with the words MASONIC TEMPLE, and a round stained-glass window above it. The building holds concerts, films and other public events and a wedding venue; there are no regular opening hours that could be found, so the interior was not checked.',
  '',
  'At 700 North Madison Avenue, on the corner of Sixth Street; owned for the arts since 2005. Seen from the street; go in for a public event.'+DT,
  [W('Bay City Masonic Temple'),['Route Bay City: Bay City\'s historic Masonic Temple',RBC+'bay-city-masonic-temple.aspx']],
  brick='no',arch='Pratt and Koeppe',archw='Wikipedia, from the National Register nomination'),

N('crapo-building-bay-city','Crapo Building (The Legacy)','Bay City','mi','civic','standing',43.59828,-83.88803,'exact','view','walk','','1891–1892',
  'A five-storey Romanesque business block on the corner of Center and Washington avenues, named for William Crapo, son of a Michigan governor and a director of the Flint and Pere Marquette Railroad. Pratt and Koeppe designed it and had their own offices in it; the railroad, a dry-goods store and lawyers were early tenants, and later it was mostly a bank. Sources give 1890, 1891 and 1892 for its building. In 1959 and 1960 the upper floors were wrapped in white metal panels; these came off in a renovation of 2017 and 2018 that made it The Legacy, with apartments above and shops below.',
  'The brick front of the upper floors, hidden for nearly sixty years behind the metal screen, can be seen again, with its round arches. Restaurant and shops on the ground floor; the apartments are private.',
  '',
  'A private building at 213 Center Avenue, downtown; seen from the street, and the ground-floor businesses are open in their own hours.'+DT,
  [['Michigan Building Trades: Crapo Building\'s old beauty bared','https://michiganbuildingtrades.org/newspaper/crapo-buildings-old-beauty-bared-behind-modern-aluminum-skin'],
   ['Route Bay City: Center Avenue walking tour',RBC+'center-avenue-walking-tour.aspx']],
  conf='mixed',brick='?',arch='Pratt and Koeppe',archw='Michigan Building Trades report, 2018: "the building\'s designers Pratt & Koeppe architects"'),

N('shearer-brothers-block-bay-city','Shearer Brothers Block','Bay City','mi','civic','standing',43.59830,-83.88683,'exact','view','walk','','1884 or 1886',
  'The last of three business blocks put up by James Shearer, a Scottish-born lumberman and builder, with his brother George, a former mayor; the two ran a real-estate office in it. It stands on the northwest corner of Center Avenue and Adams Street. The condominium association that owns it gives 1884 as the year it was finished; a Route Bay City walking tour gives 1886. Over the years it held banks, lawyers, a photographer, a dance studio and shops. A restoration begun in 2003 brought the front back near to its first look and turned the upper floors into condominiums.',
  'A tall downtown block on the corner; shops and a restaurant on the ground floor, private homes above. Interior not checked.',
  '',
  'A private building at 315 Center Avenue, on the corner of Adams Street; seen from the street.'+DT,
  [['Shearer Block Condominium Association: our history','https://shearercondo.yolasite.com/'],['Route Bay City: Center Avenue walking tour',RBC+'center-avenue-walking-tour.aspx']],
  conf='mixed',brick='?'),

N('first-presbyterian-bay-city','First Presbyterian Church, Bay City','Bay City','mi','worship','standing',43.59805,-83.88178,'exact','view','walk','','1884–1893',
  'The congregation began with services in a schoolhouse in 1848, was organised in 1856 and built its first church in 1863. In 1884 its minister, J. Ambrose Wight, urged the members to build a church that would last, fearing the lumber and salt wealth would not; this one, of Ionia sandstone in the Richardsonian style, was dedicated on June 4, 1893. Pratt and Koeppe designed it, four years before their City Hall. Its bell, cast in 1866, once rang three times a day as the town\'s clock. A Michigan historical marker stands at the church.',
  'A rough-faced sandstone church with round arches on Center Avenue; read the state marker. Interior not checked.',
  '',
  'A working church at 805 Center Avenue. No page of the church\'s own was found, so service times were not checked; seen from the street. Street parking.',
  [['Lost in Michigan: the marker text','https://lostinmichigan.net/?p=472']],
  brick='no',arch='Pratt and Koeppe',archw='Michigan historical marker text: "designed in the Richardsonian style by local architects Pratt and Koeppe"'),

N('elm-lawn-cemetery-bay-city','Elm Lawn Cemetery','Bay City','mi','burial','standing',43.58923,-83.85890,'site','public','walk','','1890–1892',
  'Founded in 1890 by Bay City businessmen when the older cemeteries were filling; the Detroit landscape architect Mason L. Brown laid out the grounds, and the first burial was in October 1891. Pratt and Koeppe designed the gatehouse and the chapel, built in 1891 and 1892. Families of means added mausoleums from 1899, when the Eddy family built the first, to 1948. About 13,000 people are buried on its 60 acres, and it is still in use. On the National Register since 2006.',
  'You enter through a stone archway, 47 feet long and 35 feet high, joined to the gatehouse that holds the office. Inside are a small Richardsonian Romanesque chapel of buff sandstone with a slate roof and a scattering of family mausoleums.',
  '',
  'A working cemetery at 300 Ridge Road, owned by Midwest Memorial Group as of 2018. Drive in through the gate; its opening hours were not checked. Visit quietly and keep to the roads.',
  [W('Elm Lawn Cemetery')],
  brick='no',arch='Pratt and Koeppe',builder='Mason L. Brown (landscape)',archw='Wikipedia, from the National Register nomination: Pratt & Koeppe designed the gatehouse and chapel; Mason L. Brown planned the grounds'),

N('pere-marquette-depot-bay-city','Pere Marquette Railroad Depot, Bay City','Bay City','mi','rail','standing',43.59980,-83.88505,'exact','view','walk','stations','1904',
  'The Pere Marquette railway\'s passenger and freight depot, opened in 1904 to the design of the Saginaw architect William T. Cooper. It served trains until about 1951. Greyhound used it as a bus station from 1953, taking off the tower and the porte-cochere, and left in 1969; it then stood empty until 2003, when the Great Lakes Center Foundation bought it. Restoration began in 2007, the tower and porte-cochere were rebuilt, and tenants moved in the next year. On the National Register since 1982.',
  'A two-storey red brick depot with limestone trim and its rebuilt tower. Offices; interior not checked.',
  '',
  'At 919 Boutell Place, now an office building known as The Depot Building; seen from the street.'+DT,
  [W('Bay City station')],
  brick='yes',bcol='red',arch='William T. Cooper',archw='Wikipedia, from the National Register nomination'),

N('sage-library-bay-city','Sage Library','Bay City','mi','civic','standing',43.60151,-83.90468,'exact','open','walk','','1882–1884',
  'A gift to West Bay City from the lumberman Henry W. Sage, who with John McGraw ran the town\'s largest mill. Pratt and Koeppe designed it and Andrew Thomson built it; it opened on January 16, 1884, with 10,000 books on the second floor and school classrooms below. It came into Bay City\'s system when the two towns joined in 1903, and is said to be the oldest library building in Michigan in use as a library all along. Restored in 1983 and 1984 and again in 2002 to 2004.',
  'Red brick with bands of light yellow brick and pink Amherst stone, with round arches, corbelling, a quatrefoil and dormers. In the grounds is a Victorian fountain of Leda and the Swan cast by the Mott foundry of New York. Inside, the old reading room has an octagonal bay window and a tiled fireplace.',
  '',
  'A branch of the Bay County Library System at 100 East Midland Street, west of the river; the hours are from the library\'s own page. Street parking on Midland Street.',
  [W('Sage Library'),['SAH Archipedia: Sage Library',SAH+'BY11'],['Bay County Library System: Sage branch','https://baycountylibrary.org/about/hours-locations/historical-sage-library']],
  brick='yes',bcol='red',hours='Monday and Tuesday 9 a.m. to 5 p.m.; Wednesday and Thursday noon to 8 p.m.; Friday 9 a.m. to 5 p.m.',
  arch='Pratt and Koeppe',builder='Andrew Thomson',archw='Wikipedia and SAH Archipedia'),

N('st-stanislaus-kostka-bay-city','St. Stanislaus Kostka Church, Bay City','Bay City','mi','worship','standing',43.58039,-83.88097,'exact','view','walk','','1890–1892',
  'Polish immigrants who had left Prussian rule formed a society under St. Stanislaus Kostka in 1874 and built a wooden church that year. This large Neo-Gothic church replaced it at a cost of over $60,000: the cornerstone was blessed on June 24, 1890, and it was dedicated on July 17, 1892. It is a Michigan Historic Site. Since 2014 it is the parish church of Our Lady of Czestochowa parish, formed when St. Stanislaus and St. Hyacinth were joined again.',
  'The parish says the church looks much as it first did: an ornate high altar, shrines under the side balconies, a font and stained glass, and a 4,000-pipe organ restored in 2010, when its pipes were moved to show the window behind. A state marker in Polish and English stands near the main door.',
  '',
  'A working Catholic church at 1503 Kosciuszko Avenue; go in at Mass. The parish\'s Mass times could not be read from its site when this was written. Parish parking by the church.',
  [['Our Lady of Czestochowa Parish: St. Stanislaus Kostka campus','https://baycityolc.com/history-stanislaus.html']],
  brick='?',hours='?'),

N('swart-block-bay-city','Swart Block','Bay City','mi','civic','standing',43.60135,-83.89948,'exact','view','walk','','1891',
  'Built for Stephen Swart, a Civil War veteran who opened a jewellery shop in West Bay City; the city approved the building in 1891. The local architect Phillip C. Floeter designed it in the Romanesque Revival style, of brick and Michigan buff stone. The shop and workrooms were on the ground floor and offices above. Swart died in 1905 and his son Arthur closed the business in 1914; the Bay County Historical Society and Route Bay City give different years for some events.',
  'A corner block of five shopfronts at South Linn and East John streets. The corner turret, which once carried a three-faced clock 54 feet up, still has SWART carved into it with the year near its small mansard roof.',
  '',
  'A private building at 108 South Linn Street, by the Midland Street district; seen from the street. Street parking.',
  [['Bay County Historical Society: Swart Jewelry','https://bchsmuseum.org/2024.05.01_arch.html'],['Route Bay City: historic Midland Street businesses','https://www.secondwavemedia.com/baycity/features/historic-midland-street-businesses.aspx']],
  conf='mixed',brick='?',arch='Phillip C. Floeter',archw='Bay County Historical Society: "designed by P.C. Floeter, a local architect"'),

N('bay-city-armory-museum','Bay City Armory (Historical Museum of Bay County)','Bay City','mi','fort','standing',43.59387,-83.88904,'exact','open','walk','','1910–1911',
  'Pratt and Koeppe designed this armory for Bay City\'s National Guard units in 1910, on the site of an older one used since 1894, and it was dedicated on September 18, 1911. At the Republican state convention here in April 1912, fights broke out between supporters of Theodore Roosevelt and of President Taft, and the governor called in the militia; the split led to Roosevelt\'s Progressive party. Guard units were based here until 1986, and the building was also the town\'s hall for dances, boxing and shows. The Bay County Historical Society bought it and opened it as the county museum in 1988.',
  'The old armory front on Washington Avenue, a few doors from City Hall. Inside are the county museum\'s exhibits, a research library and a small theatre showing local history films.',
  '',
  'Run by the Bay County Historical Society at 321 Washington Avenue; the hours are from the society\'s own page.'+DT,
  [['Bay County Historical Society: history and the Armory','https://www.bchsmuseum.org/history.html'],['Bay County Historical Museum','https://www.bchsmuseum.org/']],
  brick='?',hours='Tuesday to Saturday 10 a.m. to 4 p.m.',arch='Pratt and Koeppe',archw='Bay County Historical Society: "designed by local architects Pratt and Koeppe in 1910"'),

N('whitney-residence-bay-city','Whitney Residence','Bay City','mi','landmark','standing',43.59740,-83.87628,'exact','view','walk','','1887',
  'A two-and-a-half-storey Queen Anne house of 1887 on Center Avenue, the street of the lumber barons, built for Charles Whitney, who was not one. He came to Bay City in 1874, opened pharmacies, and in 1880 founded with William Pomeroy a bakery known across Michigan for its cookies and crackers.',
  'Four cross-gables, a red sandstone foundation and a witch\'s-cap turret over the bay window facing the corner of Center Avenue and Lincoln Street. A private house: interior not checked.',
  '',
  'A private house at 1315 Center Avenue, in the Center Avenue historic district; see it from the sidewalk only. Street parking.',
  [['Route Bay City: Center Avenue walking tour',RBC+'center-avenue-walking-tour.aspx']],
  brick='?'),

N('trombley-house-bay-city','Trombley House (Centre House)','Bay City','mi','landmark','standing',43.59111,-83.89972,'site','ask','walk','','1835–1837',
  'Built in 1835 to 1837 by the carpenter Nathan C. Case for the French-Canadian fur traders Medor and Joseph Trombley, who used it as a house, a trading post and a kind of inn; it is the oldest frame house standing in Bay County. It stood on the east bank on Webster Street. In 1981 its owner wanted the site for a parking lot, so the house was floated down the Saginaw River on a barge to Veterans Memorial Park. On the National Register since 1973.',
  'A two-storey Greek Revival frame house, five openings across the front, with an herb garden kept by a local herb society. The historical society uses it for a holiday open house, luncheons and programs.',
  '',
  'In Veterans Memorial Park at 901 John F. Kennedy Drive, cared for by the Bay County Historical Society. The outside can be seen from the park; tours are by appointment through the museum (989-893-5733), as its page says. Park parking.',
  [W('Trombley House'),['Bay County Historical Society: Trombley/Centre House','https://www.bchsmuseum.org/trombleyhouse.html']],
  brick='no',bcol='none',builder='Nathan C. Case',archw='Wikipedia: the Trombleys hired Nathan C. Case, a carpenter, to construct it'),

N('trinity-episcopal-bay-city','Trinity Episcopal Church, Bay City','Bay City','mi','worship','standing',43.59808,-83.88032,'exact','view','walk','','1885–1887',
  'A Gothic Revival church of 1885 to 1887 designed by Phillip C. Floeter of Bay City, who had come from Chatham, Ontario. A rectory followed in 1896 and a parish house by Smith, Hinchman and Grylls in 1924; it was renovated from 2005 to 2009.',
  'Rough-faced Bay Port limestone walls, window tracery and a square buttressed bell tower with pinnacles at the corner. Inside, SAH Archipedia describes a reredos carved in 1923 by Alois Lang, a Grand Rapids carver born in Oberammergau; the interior was not checked for visitors.',
  '',
  'A working Episcopal church on the corner of Center Avenue and North Grant Street (815 North Grant). No page of the church\'s own was found, so service times were not checked. Street parking.',
  [['SAH Archipedia: Trinity Episcopal Church',SAH+'BY5']],
  brick='no',arch='Phillip C. Floeter; Smith, Hinchman and Grylls',archw='SAH Archipedia: church by Floeter, 1924 parish house by Smith, Hinchman and Grylls'),

N('bay-county-building-mi','Bay County Building','Bay City','mi','civic','standing',43.59838,-83.88483,'exact','view','walk','','1931–1934',
  'An eight-storey Art Deco county building put up in the Depression as a county-funded relief project, pushed by the circuit judge Samuel G. Houghton. It replaced the county\'s brick Italianate courthouse of the 1860s by C. K. Porter of Buffalo. The local architect Joseph C. Goddeyne designed it. On the National Register since 1982.',
  'A steel frame sheathed in limestone and granite, with piers running the full height and set-back upper floors. SAH Archipedia says the inside keeps its Art Deco detail: a painted frieze and engraved brass lift doors in the entrance hall, and an oak-panelled fourth-floor courtroom with a balcony and plaster reliefs. County offices; their public hours were not checked.',
  '',
  'Owned by Bay County, at 515 Center Avenue; seen from the street, and the public may go in on county business.'+DT,
  [['SAH Archipedia: Bay County Building',SAH+'BY3']],
  brick='no',arch='Joseph C. Goddeyne',archw='SAH Archipedia'),

]

PIN_NOTES={
 'bay-city-hall-mi':'Address point for 301 Washington Avenue; on the aerial it is on the city hall.',
 'bay-city-masonic-temple':'Address point for 700 North Madison Avenue; on the aerial it is on the temple at the corner of Sixth Street.',
 'crapo-building-bay-city':'Address point for 213 Center Avenue, at Washington Avenue; looked at on the aerial.',
 'shearer-brothers-block-bay-city':'Address point for 315 Center Avenue, at Adams Street; looked at on the aerial.',
 'first-presbyterian-bay-city':'Address point for 805 Center Avenue; looked at on the aerial.',
 'elm-lawn-cemetery-bay-city':'Address point for 300 Ridge Road; it falls inside the grounds, among the graves, not on the gate.',
 'pere-marquette-depot-bay-city':'The address lookup for 919 Boutell Place fell on the drive beside it; moved 26 m west onto the long red-roofed depot with its tower, seen on the aerial.',
 'sage-library-bay-city':'Address point for 100 East Midland Street; on the aerial it is on the library.',
 'st-stanislaus-kostka-bay-city':'OpenStreetMap point for the church; the parish address lookup fell in the street. On the aerial it is on the tall church whose tower casts a long shadow.',
 'swart-block-bay-city':'Address point for 108 South Linn Street; looked at on the aerial.',
 'bay-city-armory-museum':'Address point for 321 Washington Avenue; looked at on the aerial.',
 'whitney-residence-bay-city':'Address point for 1315 Center Avenue; looked at on the aerial.',
 'trombley-house-bay-city':'Wikipedia coordinate, in Veterans Memorial Park; looked at on the aerial.',
 'trinity-episcopal-bay-city':'Address point for 815 North Grant Street, at Center Avenue; looked at on the aerial.',
 'bay-county-building-mi':'Address point for 515 Center Avenue; looked at on the aerial.',
}
