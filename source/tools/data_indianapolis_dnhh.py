# November 23, 2026: downtown Indianapolis and its old north side. The names came from one video (a stranger's tip,
# never a source); every fact here is from a source opened while this batch was written: Wikipedia articles, the
# Indiana War Memorials' own pages, the Scottish Rite's tour page, the Indianapolis Public Library's page, the Crown
# Hill Heritage Foundation's pages, St. Joan of Arc parish's page and the archdiocesan newspaper, the City Market
# Corporation's May 2026 release and a WFYI report of June 2026 on Old City Hall.
from data_b import N
from data_ma import W

BATCH={'key':'indianapolis_dnhh','label':'Indianapolis: Monument Circle, the War Memorial and the old north side','added':'2026-11-23 03:40'}

DT='Downtown Indianapolis has metered street parking and many garages and lots; which of them are public, and their prices, were not checked.'
IWM=['Indiana War Memorials: tours and reservations','https://www.in.gov/iwm/visitor-information/tours-and-reservations/']

PLACES=[
N('indiana-world-war-memorial','Indiana World War Memorial','Indianapolis','in','fort','standing',39.77336,-86.15695,'exact','open','walk','','1926–1965',
  'The centrepiece of the Indiana World War Memorial Plaza, begun after the city won the American Legion\'s national headquarters in 1919; the plaza was dedicated in November 1921 with a cornerstone taken from the bridge over the Marne at Château-Thierry. Work on the memorial building, modelled on the Mausoleum of Halicarnassus, began in early 1926 and General John Pershing laid its cornerstone on July 4, 1927; money ran short for decades, and the memorial and its grounds were finally finished in 1965. The plaza was made a National Historic Landmark district in 1994 and enlarged in 2016 to take in the Soldiers\' and Sailors\' Monument.',
  'A cube of plain Indiana limestone on a rusticated base under a low pyramid roof, with shield-bearing limestone lions at the north and south doors and urns on the terrace corners. Inside, the north entrance opens into a hall with Tennessee marble floors and Art Deco Egyptian themes; the military museum on the lower level holds over 400 flags, more than 300 of them from the Civil War, and the Colonel Eli Lilly Civil War Museum moved here from the Soldiers\' and Sailors\' Monument after water damage in 2018. The Shrine Room high in the building was closed for renovation in January 2026; whether it has reopened was not checked on the memorial\'s own page.',
  'A five-block war memorial plaza with a mausoleum for its heart.',
  'State-owned, run by the Indiana War Memorials Commission; free. The museum is open Wednesday to Sunday and closed on national and state holidays except Memorial Day and Veterans Day (the commission\'s page). Guided tours for groups are booked ahead. The plaza and its parks are open ground. '+DT,
  [IWM,['Indiana War Memorials (archived copy of January 2026)','https://www.in.gov/iwm/index.html'],W('Indiana World War Memorial Plaza')],
  brick='no',hours='Museum Wednesday to Sunday 9 a.m. to 5 p.m.; closed Monday, Tuesday and holidays except Memorial Day and Veterans Day'),

N('soldiers-sailors-monument-indianapolis','Soldiers\' and Sailors\' Monument','Indianapolis','in','curio','standing',39.76851,-86.15804,'exact','public','walk','','1888–1901',
  'An obelisk at the centre of Monument Circle, designed by the Berlin architect Bruno Schmitz after an international contest and built between 1888 and 1901; the obelisk was finished in 1892 and the monument dedicated on May 15, 1902. It was raised for Indiana\'s Civil War veterans and also honours the state\'s soldiers of the Revolution, the wars of 1811–12, the Mexican–American War and the Spanish–American War. Wikipedia calls it the first monument in the United States dedicated to the common soldier.',
  'Oolitic limestone from Owen County, crowned by George Brewster\'s 30-foot bronze Victory, with Rudolf Schwarz\'s great limestone groups of War and Peace, bronze astragals, pools and fountains, and an observation deck reached by stairs or a lift inside. The Civil War museum that was in its basement moved to the Indiana World War Memorial after leaks in 2018. The Circle round it is brick-paved.',
  'The state\'s Civil War obelisk, built by a Berlin architect over thirteen years.',
  'State-owned, run by the Indiana War Memorials Commission; the Circle and the monument\'s steps are open ground. The inside and the observation level: the commission\'s tours page says they open on Fridays 10 a.m. to 4 p.m., but its home page in January 2026 said the monument and its shop were closed until further notice for repairs; check before going. '+DT,
  [W('Soldiers\' and Sailors\' Monument (Indianapolis)'),IWM],conf='mixed',brick='no',
  hours='Inside: Fridays 10 a.m. to 4 p.m. by the tours page, but closed for repairs by the home page in January 2026'),

N('scottish-rite-cathedral-indianapolis','Scottish Rite Cathedral','Indianapolis','in','civic','standing',39.77616,-86.15829,'exact','open','walk','','1927–1929',
  'A Masonic meeting house of the Scottish Rite, designed by George F. Schreiber and built in 1927–1929 for $2.5 million. Wikipedia calls it the largest Scottish Rite building anywhere and one of the largest Masonic buildings in the world. Every dimension in feet is divisible by three, and many by 33, for the degrees of the order. It is still owned and used by the Valley of Indianapolis Scottish Rite.',
  'Gothic Revival in Indiana limestone, patterned largely on details of Cologne Cathedral, with the 212-foot "Singing Tower" holding a carillon of 54 bells. Inside: over 100 painted-glass windows of Masonic and Scottish Rite symbols, woodwork of Russian curly oak, an Elizabethan ballroom 99 feet square with a white-oak floor laid on felt, and a theatre with more than 50 hand-painted backdrops. Bronze medallions are set in the travertine floors at the doors.',
  'The biggest Scottish Rite building in the world, with a carillon tower.',
  'Owned by the Valley of Indianapolis Scottish Rite. Guided tours for walk-ins and small groups, adults $10, children $5; groups over ten book ahead (the Scottish Rite\'s tour page). The building is also hired out for events. 650 North Meridian Street; it has a west parking lot (the same page). '+DT,
  [['Scottish Rite Valley of Indianapolis: tour the Cathedral','https://aasr-indy.org/cathedral/tour-the-cathedral/'],W('Scottish Rite Cathedral (Indianapolis)')],
  brick='?',hours='Guided tours Tuesday, Wednesday and Thursday, 10 a.m. to 2 p.m.'),

N('indianapolis-union-station','Indianapolis Union Station','Indianapolis','in','rail','standing',39.76309,-86.15960,'exact','open','walk','','1886–1888',
  'Indianapolis had the world\'s first union station in 1848. The present head house, by the Pittsburgh architect Thomas Rodd, was begun in November 1886 and opened in September 1888 in the Richardsonian Romanesque style, and is one of the oldest surviving examples of it. The elevated train shed behind it was built from 1915 to 1922 when more than 200 trains a day came through. After passenger traffic fell it became a festival market in 1986; a hotel now fills much of the shed, and Amtrak still stops here.',
  'Granite and brick trimmed with Hummelstown brownstone, with great round arches, an enormous rose window, a slate roof, corner bartizans and a 185-foot clock tower. Inside the head house is the Grand Hall, now hired out for weddings and events. The Crowne Plaza hotel in the old shed kept 13 Pullman cars as rooms. Amtrak passengers wait in a room under the shed along Illinois Street.',
  'The heir of the world\'s first union station, with a rose window and a clock tower.',
  'A working station: Amtrak\'s Cardinal stops three times a week each way (Wikipedia), and its waiting room opens for the trains. The head house and the Grand Hall are leased by the hotel for events; whether visitors may walk in at other times was not checked. Look from Jackson Place and Illinois Street. OpenStreetMap maps the Union Station garage on South Meridian Street. '+DT,
  [W('Indianapolis Union Station')],brick='?',hours='?',th=[39.76257,-86.15756],thn='Union Station parking garage, South Meridian Street'),

N('birch-bayh-federal-building-indianapolis','Birch Bayh Federal Building and U.S. Courthouse','Indianapolis','in','civic','standing',39.77083,-86.15704,'exact','view','walk','','1902–1905',
  'Built from 1902 to 1905 as the U.S. Courthouse and Post Office, one of only 35 federal buildings designed under the Tarsney Act by private architects chosen in competition: John Hall Rankin and Thomas Kellogg of Philadelphia. It cost nearly $2 million, against a bid of $1.3 million, and filled a whole block. It still houses the federal court for the Southern District of Indiana and was renamed for Senator Birch Bayh in 2003.',
  'A U-shaped Beaux-Arts block with Ionic pilasters and balustraded terraces. Inside, by Wikipedia: barrel-vaulted marble corridors, octagonal vestibules with red marble walls and Roman-style mosaic ceilings, semicircular cantilevered marble staircases, and courtrooms with gilded and painted plaster ceilings and their original furniture. Interior not checked for visitors.',
  'A whole-block Beaux-Arts courthouse with mosaic ceilings and floating marble stairs.',
  'A working federal courthouse owned by the General Services Administration; entry is through security for court business. No visiting hours were found: look from Ohio and Meridian streets. '+DT,
  [W('Birch Bayh Federal Building and United States Courthouse')],brick='?'),

N('central-library-indianapolis','Central Library','Indianapolis','in','civic','standing',39.77841,-86.15674,'exact','open','walk','','1917',
  'The main library of the Indianapolis Public Library, opened in October 1917 on land given by the poet James Whitcomb Riley. Paul Philippe Cret of Philadelphia designed it in the Greek Doric style. A glass and steel addition by Evans Woollen opened in 2007 behind it; during that work the library moved for five years into Old City Hall.',
  'Indiana limestone on a Vermont marble base, with a Doric colonnade. The names of authors are carved into the limestone walls, and in 2022 ten Black American authors were added to the more than 80 earlier names (the library\'s page). It is a working public library, open to all.',
  'A Doric temple of a library on land given by James Whitcomb Riley.',
  'Run by the Indianapolis Public Library; free. Hours from the library\'s own page. 40 East St. Clair Street, at the north end of the War Memorial Plaza. '+DT,
  [['Indianapolis Public Library: Central Library','https://www.indypl.org/locations/central-library'],W('Central Library (Indianapolis)')],
  brick='no',hours='Monday and Tuesday 10 a.m. to 8 p.m.; Wednesday and Thursday 10 a.m. to 6 p.m.; Friday and Saturday 10 a.m. to 5 p.m.; Sunday 1 to 5 p.m.'),

N('old-indianapolis-city-hall','Old Indianapolis City Hall','Indianapolis','in','civic','standing',39.7702,-86.15295,'exact','view','walk','','1909–1910',
  'The city hall from 1910 until city offices moved to the City-County Building in 1962. It then housed the Indiana State Museum from 1966 to 2001 and the Central Library while that was rebuilt. It has stood empty for about a decade: a plan for a hotel and a 32-storey tower fell through in April 2026, and in June 2026 the city asked again for proposals while Indiana Landmarks pointed out water damage inside (WFYI).',
  'Four storeys of Classical Revival, brick faced in Indiana limestone. Interior not checked; it is shut.',
  'An empty city hall waiting for its next use.',
  'City-owned and closed. Look from Alabama and Ohio streets. '+DT,
  [W('Old Indianapolis City Hall'),['WFYI, June 18, 2026: Old City Hall needs repairs','https://www.wfyi.org/wfyi-news/2026-06-18/old-city-hall-needs-repairs-as-developers-consider-redevelopment-plans-again']],
  brick='no'),

N('indianapolis-city-market','Indianapolis City Market','Indianapolis','in','civic','standing',39.76878,-86.15345,'exact','view','walk','','1886',
  'A public market founded in 1821; the present Market House opened in 1886. It once stood beside Tomlinson Hall, and the vaulted basement left under the site became known as the Indianapolis Catacombs. The market closed in March 2024 for redevelopment. By the City Market Corporation\'s release of May 2026, the first phase is Whistler Plaza, a terraced public space that will show parts of the old underground work, due to be finished by the end of 2027; the restoration and reopening of the Market House itself is still being planned.',
  'A one-storey brick hall trimmed in limestone, with a gabled centre between two square towers. While it is shut, only the outside can be seen. Wikipedia says the Tomlinson Hall archway is to be kept in the new plaza.',
  'A market hall of 1886 with old vaults under its plaza.',
  'Owned by the city and run by the City Market Corporation; closed for redevelopment since March 2024, with construction round Whistler Plaza (the corporation\'s page). Look from Market and Delaware streets. '+DT,
  [W('Indianapolis City Market'),['City Market Corporation: next steps for the redevelopment, May 2026','https://www.indycm.com/?p=7862']],
  brick='?'),

N('columbia-club-indianapolis','Columbia Club','Indianapolis','in','civic','standing',39.7692,-86.1573,'exact','view','walk','','1925',
  'A private club founded in 1889 by Republicans who had marched for Benjamin Harrison, now non-partisan. This ten-storey clubhouse of 1925, by Rubush & Hunter, is the club\'s third on the same spot on Monument Circle; it replaced a building of 1898. The club says the founders of the Indianapolis Motor Speedway met here.',
  'Gothic Revival with Tudor touches, a tall oriel window and relief panels carved in Indiana limestone by Alexander Sangernebo, designed to sit well beside the Soldiers\' and Sailors\' Monument. Interior not checked; it is a members\' club.',
  'A ten-storey Gothic clubhouse on Monument Circle.',
  'Private club: look from Monument Circle. '+DT,
  [W('The Columbia Club')],brick='?'),

N('crown-hill-gothic-chapel','Crown Hill Cemetery and its Gothic Chapel','Indianapolis','in','burial','standing',39.81734,-86.17174,'site','public','drive','cemeteries','1863–1875',
  'A rural cemetery founded in 1863 on Strawberry Hill and dedicated in 1864; at 555 acres Wikipedia calls it the third largest non-governmental cemetery in the United States. President Benjamin Harrison, three vice presidents, the poet James Whitcomb Riley (on "The Crown", the hilltop) and John Dillinger are buried here. The limestone Gothic Chapel was designed in 1875 by Diedrich A. Bohlen as a holding vault, with 96 crypts in its side rooms.',
  'The Gothic Chapel, now used for funerals, tours and events, and a gift organ inside (the Heritage Foundation). The Gothic gate and waiting station on the old south entrance at 34th Street. Over 25 miles of road, many mausoleums and monuments, and the Crown Hill National Cemetery of 1866 in sections 9 and 10. Interior of the chapel not checked.',
  'A president\'s grave, a poet on the hilltop and a Gothic vault of 1875.',
  'A privately owned cemetery (Wikipedia) whose gates open to visitors daily; drive in by the North Gate, 700 West 38th Street, where the office is, or the Gothic gate at 34th Street and Boulevard Place (the Crown Hill Heritage Foundation). Where to leave a car inside was not checked. Be respectful of funerals.',
  [W('Crown Hill Cemetery'),['Crown Hill Heritage Foundation: visit','https://crownhillhf.org/visit/'],['Crown Hill Heritage Foundation: places of interest','https://crownhillhf.org/structure/']],
  brick='no',hours='North Gate 8 a.m. to 6 p.m. October to March, 8 a.m. to 8 p.m. April to September; Gothic gate 8 a.m. to 5 p.m. daily'),

N('marott-hotel-indianapolis','Marott Hotel','Indianapolis','in','hotel','standing',39.80522,-86.15610,'site','view','drive','hotels','1926',
  'A residential hotel of 1926 on North Meridian Street: two 11-storey towers joined by a one-storey wing that held the lobby, event halls, a gym and an indoor pool. Listed on the National Register in 1982.',
  'Georgian Revival, reinforced concrete faced in red brick with terracotta and glazed tile trim (Wikipedia). Interior not checked.',
  'A pair of red-brick towers that were a 1920s apartment hotel.',
  'Private residential building: look from North Meridian Street. Parking not checked.',
  [W('Marott Hotel')],brick='yes'),

N('athenaeum-indianapolis','Athenæum (Das Deutsche Haus)','Indianapolis','in','civic','standing',39.77351,-86.15027,'exact','open','walk','','1893–1898',
  'A clubhouse built by the city\'s German clubs as "Das Deutsche Haus": the east wing in 1893–1894 and the west in 1897–1898, both by Bernard Vonnegut (Kurt Vonnegut\'s grandfather) and Arthur Bohn. It held a Turnverein gymnasium, a hall and the meetings of many German-American societies. It was listed on the National Register in 1973 and made a National Historic Landmark in 2016. A foundation looks after it and it houses several groups and businesses.',
  'German Renaissance Revival: two brick towers, one under a conical slate roof and one under a curved mansard and spire, a limestone arch on Doric columns at the entrance, stained glass in some windows and terracotta grotesques on the front. Inside is the Rathskeller, which Wikipedia calls the oldest restaurant in the city.',
  'Kurt Vonnegut\'s grandfather\'s German clubhouse, with the city\'s oldest restaurant in it.',
  'Run by the Athenæum Foundation. The Rathskeller restaurant and biergarten are open to the public (its page lists live music Wednesday to Saturday); Wikipedia says the foundation gives free tours twice a month from March to December, but the foundation\'s own page did not give dates when read. 401 East Michigan Street. '+DT,
  [W('Athenæum (Das Deutsche Haus)'),['Athenaeum Foundation','https://athenaeumindy.org/'],['The Rathskeller','https://www.rathskeller.com/']],
  brick='?',hours='?'),

N('old-national-centre-murat','Old National Centre (Murat Shrine)','Indianapolis','in','civic','standing',39.77458,-86.15108,'exact','open','walk','','1909–1922',
  'The Murat Temple of the Shriners, built in 1909 by the William P. Jungclaus Company to the design of Oscar D. Bohlen, with its theatre of 1910 and an Egyptian-themed hall added in 1922. Wikipedia calls it the largest Shrine Center in North America, and its theatre holds the oldest stage house still standing in downtown Indianapolis. The Shriners still own it; it is now a concert and event venue.',
  'Middle Eastern and Egyptian styling outside: minarets, terracotta trim, stained glass and banding of brown and yellow brick. Inside, the Murat Theatre and the Egyptian Room, which holds 2,000 standing. Seen inside only at shows and events.',
  'A Shriners\' temple with minarets, still a working theatre.',
  'Owned by the Murat Shriners; open for concerts and events, with tickets. No visiting hours were found. North and New Jersey streets, across Massachusetts Avenue from the Athenæum. '+DT,
  [W('Old National Centre')],brick='no',hours='?'),

N('indiana-theatre-indianapolis','Indiana Theatre','Indianapolis','in','civic','standing',39.7675,-86.16105,'exact','open','walk','','1927',
  'A movie palace and ballroom built in 1927 at 140 West Washington Street, with bowling alleys and billiard rooms in the basement and a 3,200-seat auditorium. It was restored and the auditorium remodelled in 1979–1980 for the Indiana Repertory Theatre, which plays there today. Listed on the National Register in 1979.',
  'A white terracotta front with a great curving arch in Churrigueresque frame above the original marquee. On top is the Indiana Roof Ballroom, an atmospheric ballroom made to look like a town square, under an elliptical dome with sky effects. Seen inside at performances.',
  'A 1927 movie palace with a town square of a ballroom on its roof.',
  'Home of the Indiana Repertory Theatre: open for performances, with tickets; the ballroom is hired for events. No visiting hours were found. '+DT,
  [W('Indiana Theatre (Indianapolis)')],brick='no',hours='?'),

N('st-joan-of-arc-church-indianapolis','St. Joan of Arc Church','Indianapolis','in','worship','standing',39.83279,-86.14877,'site','open','drive','','1929',
  'A Catholic parish founded in 1921, when it was the northernmost in the city, at Central Avenue and 42nd Street. The present church was dedicated in 1929, when the parish had nearly 3,000 members. After years of a leaking roof and peeling plaster, a restoration began in February 2019 and was in its last phase for the parish\'s centenary in July 2021 (the archdiocesan newspaper).',
  'Stained-glass windows from Munich and solid Indiana limestone pillars, so heavy that a temporary rail spur was laid to deliver them; a carillon (The Criterion). Open for services.',
  'A 1929 church with Munich glass and pillars that came by their own railway spur.',
  'An active parish church, 4217 Central Avenue. Mass times are from an archived copy of the parish\'s page of October 2025; check its page before going. Parking not checked: OpenStreetMap maps a lot on North College Avenue about 300 m east.',
  [['The Criterion: a century of St. Joan of Arc (2021)','https://archindy.org/criterion/local/2021/10-01/joan.html'],['St. Joan of Arc Parish','https://www.sjoa.org/']],
  brick='?',hours='Saturday 5:30 p.m.; Sunday 8:30 and 10:30 a.m. and 5:30 p.m.; weekday Mass Tuesday to Friday (as read October 2025)'),

N('shortridge-high-school-indianapolis','Shortridge High School','Indianapolis','in','civic','standing',39.81852,-86.15528,'site','view','drive','','1927–1928',
  'Indiana\'s first free public high school, opened in 1864 as Indianapolis High School and renamed for Abram C. Shortridge in 1896. It moved four times downtown before this building at 34th and Meridian streets was begun in 1927 and opened in 1928. Its daily paper, the Shortridge Daily Echo, began in 1898; Kurt Vonnegut, class of 1940, edited it.',
  'Interior not checked; it is a working public school.',
  'Indiana\'s first free high school, where Kurt Vonnegut edited the daily paper.',
  'A working Indianapolis Public Schools high school: look from Meridian and 34th streets, and do not go onto the grounds in school hours. Parking not checked.',
  [W('Shortridge High School')],brick='?'),
]

PIN_NOTES={
 'indiana-world-war-memorial':'OpenStreetMap\'s building for the memorial, checked on the aerial.',
 'soldiers-sailors-monument-indianapolis':'OpenStreetMap\'s point for the monument at the centre of Monument Circle, checked on the aerial.',
 'scottish-rite-cathedral-indianapolis':'OpenStreetMap\'s point for the cathedral at 650 North Meridian Street, checked on the aerial.',
 'indianapolis-union-station':'OpenStreetMap\'s building for the head house at 39 West Jackson Place, moved onto the head house roof seen on the aerial (the first point fell on the train shed); the parking point is the Union Station garage that OpenStreetMap maps.',
 'birch-bayh-federal-building-indianapolis':'OpenStreetMap\'s courthouse at 46 East Ohio Street, checked on the aerial.',
 'central-library-indianapolis':'OpenStreetMap\'s library at 40 East St. Clair Street, checked on the aerial.',
 'old-indianapolis-city-hall':'OpenStreetMap\'s building at 202 North Alabama Street, checked on the aerial.',
 'indianapolis-city-market':'OpenStreetMap\'s building for the City Market at 222 East Market Street, checked on the aerial.',
 'columbia-club-indianapolis':'OpenStreetMap\'s building at 121 Monument Circle, checked on the aerial.',
 'crown-hill-gothic-chapel':'OpenStreetMap\'s point for the Gothic Chapel inside the cemetery, checked on the aerial; the cemetery spreads far round it.',
 'marott-hotel-indianapolis':'Moved onto the towers seen on the aerial, beside OpenStreetMap\'s ten-storey building at 2625 North Meridian Street; the National Register list\'s point fell on Fall Creek Parkway beside it.',
 'athenaeum-indianapolis':'OpenStreetMap\'s building at 401 East Michigan Street, checked on the aerial.',
 'old-national-centre-murat':'OpenStreetMap\'s point for the theatre at 502 North New Jersey Street, checked on the aerial.',
 'indiana-theatre-indianapolis':'OpenStreetMap\'s point for the Indiana Repertory Theatre at 140 West Washington Street, checked on the aerial.',
 'st-joan-of-arc-church-indianapolis':'OpenStreetMap\'s parish grounds at Central Avenue and 42nd Street, checked on the aerial.',
 'shortridge-high-school-indianapolis':'One of the school buildings OpenStreetMap maps on the campus between Meridian and Pennsylvania streets; the school\'s own point fell on its running track. Which wing is the 1928 building was not checked.',
}
