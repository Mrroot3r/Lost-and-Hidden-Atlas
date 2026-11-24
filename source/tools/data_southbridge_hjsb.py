# November 24, 2026: Southbridge, Massachusetts. A "videos" session (PROMPTS.md job 9): the names came from one video's
# tour of old Southbridge buildings (the record is source/videos/20261002_AzXuV8WNDEM.md); the video is a tip and nothing
# here rests on it. Sources read: Wikipedia (each article named in the links), the Worcester Business Journal and Global
# Traveler on the American Optical plant's hotel, and web search results quoting the Worcester diocese's paper on Notre
# Dame's facade and the Associated Press on the sale of Sacred Heart. The parish's own site and its news pages refused
# every request, so no church hours are given.
# Pins are OpenStreetMap points, address-lookup points or Register points, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'southbridge_hjsb','label':'Massachusetts: old Southbridge, from Elm Street to the mills','added':'2026-11-24 09:37'}

EB=[42.07477,-72.03493]
EBN='Edwards Block municipal parking lot, off Main Street by Strand Place'
DT=' Downtown street parking and the Edwards Block municipal lot are close by; their hours and fees were not checked.'

PLACES=[
N('notre-dame-church-southbridge','Notre Dame Catholic Church','Southbridge','worc','worship','standing',42.07796,-72.03658,'exact','view','walk','','1912–1916',
  'The church of Southbridge\'s French Canadian parish, founded in 1869, whose first church was a wooden one. The land at Main and Marcy streets was bought in 1895, but the deal barred building until the seller, Mr. Marcy, had died; he died in 1908, and the present church went up from 1912 to 1916 to designs by the Canadian architect Joseph Venne, the last of his three churches for French congregations in Massachusetts. It now serves the Parish of Saint John Paul II together with St. Mary Church on Hamilton Street.',
  'A big stone-faced church with a tower given as 210 feet high. Inside is a 1916 Casavant Freres organ (Opus 649) of four keyboards and 42 ranks, one of the largest in any Catholic church in Massachusetts. The diocese\'s paper, as quoted in search results, reported that the church was to close in part because the marble facing on the south side had worked loose from the brick wall behind it, with repairs put at $550,000 to $625,000; the date of that report and the state of the repairs were not checked. Interior not checked.',
  '',
  'An active Catholic church of the Parish of Saint John Paul II at 446 Main Street; look from Main and Marcy streets. The parish\'s own pages could not be opened when this was written, so Mass times and any opening for visitors were not checked.'+DT,
  [W('Notre Dame Catholic Church (Southbridge, Massachusetts)'),['Parish of Saint John Paul II (official site)','https://stjp2parish.org']],
  th=EB,thn=EBN,brick='no'),

N('southbridge-town-hall','Southbridge Town Hall','Southbridge','worc','civic','standing',42.07339,-72.03424,'exact','view','walk','','1888',
  'Built in 1888 to serve both as the town hall and the public high school, after the town decided one building would cost less than two. Classrooms and town offices were on the first floor and a large meeting hall on the second. The high school moved out when a school of its own was built in 1927. Of the three Romanesque Revival buildings Southbridge put up in that period it is the only one left: the other two, a bank and the YMCA, are gone.',
  'Massive stone blocks, big arches and textured ornamental brickwork, with a round clock tower on the left and a two-story brick arch over the paired front doors, each framed by a stone arch on twin columns. The interior was renovated in the 1970s; inside not checked.',
  '',
  'Owned by the Town of Southbridge, at 41 Elm Street; town offices are inside, but their hours were not checked. Look from Elm Street.'+DT,
  [W('Southbridge Town Hall')],
  th=EB,thn=EBN,brick='yes'),

N('elm-street-congregational-southbridge','Elm Street Congregational Church','Southbridge','worc','worship','standing',42.07315,-72.03449,'exact','view','walk','','1885',
  'The congregation was founded in 1801 and built its first church on this spot in 1822. In 1884 a storm blew that church\'s steeple into its roof, and this brick church replaced it, dedicated on September 4, 1885, at a cost of $17,500. Its tower lost its upper stages in the 1938 New England hurricane and they were never rebuilt. It belongs to the United Church of Christ.',
  'High Victorian Gothic in brick: a steep roof with pinnacles, decorative brickwork and Gothic-arched stained glass windows, with the entrance in the transept. The square, buttressed tower at the corner stops short where its upper stages blew down in 1938. Interior not checked.',
  '',
  'An active church on the east side of Elm Street, just south of Main Street and opposite Dresser Street. No page of the church\'s own could be found, so service times were not checked. Look from Elm Street.'+DT,
  [W('Congregational Church (Southbridge, Massachusetts)')],
  th=EB,thn=EBN,brick='yes'),

N('elm-street-fire-house-southbridge','Elm Street Fire House','Southbridge','worc','civic','standing',42.0743,-72.03453,'exact','view','walk','','1899',
  'Built in 1899 to designs by the Worcester architect George H. Clemence, this was the second of the two fire houses Southbridge built in the 1890s, after the Globe Village one. The town\'s fire service had begun with a hand engine owned by the Hamilton Woolen Company; the town bought its own in 1832 and set up its fire department in 1880. The building is given as the fire department\'s headquarters.',
  'A two-story brick house with a hip roof and a tall Italianate hose-drying tower at the northeast corner, round-arch windows and a bracketed pyramid roof. The ground-floor bays have rusticated brick arches, and the dormers have Gothic-arched gables. A one-story addition on the south side holds more bays.',
  '',
  'A working fire station at 24 Elm Street, owned by the town: look from the street and keep clear of the bays and the apron.'+DT,
  [W('Elm Street Fire House')],
  th=EB,thn=EBN,brick='yes'),

N('globe-village-fire-house-southbridge','Globe Village Fire House','Southbridge','worc','civic','standing',42.08032,-72.04528,'area','view','walk','','1894',
  'Built in 1894 as the second home of the Globe Village Fire Company, which was founded in 1832; its first house, of 1860, stood on the north side of Main Street. It was the first of the two fire houses Southbridge built in the 1890s. When it was listed on the National Register in 1989 a veterans group was using it.',
  'A modest Colonial Revival brick building, two and a half stories, with three equipment bays, a corner tower with a mansard cap, segmental-arched doors and windows, a round window in the front gable, brick pilasters at the corners and a line of brick corbels under the eaves.',
  '',
  'On the south side of West Street near Main Street, in Globe Village. Its present owner and use were not checked: look from the street.',
  [W('Globe Village Fire House')],
  brick='yes'),

N('american-optical-southbridge','American Optical Company main plant (Wellsworth Hotel)','Southbridge','worc','industry','standing',42.07491,-72.02547,'exact','open','walk','','early 1900s',
  'The American Optical Company, formed in Southbridge in 1869 out of lens makers working in the town since the 1830s, became the world\'s largest maker of eyewear by the early 20th century and at its height employed more than 6,000 people. Its works spread over about 80 acres on both banks of the Quinebaug River; the main plant on Mechanic Street, from the early 20th century, was designed by Earle & Fuller. The company shut down in Southbridge in 1984. In 2001 the main plant became the Southbridge Hotel and Conference Center, renamed the Wellsworth Hotel in 2024 after a line of AO glasses, and the American Optical Company Historic District was listed on the National Register in 2023.',
  'The large Romanesque brick plant with its clock tower; the conversion kept the tower, the front, the foyer and the marble staircase. The later company buildings around it are mostly concrete.',
  '',
  'A hotel and conference center at 14 Mechanic Street, privately owned and trading as a hotel in 2024; hotel hours were not checked. A mortgagee sale of the property has been advertised (its date was not given), so check that the hotel is still trading before going.',
  [W('American Optical Company Historic District'),['Worcester Business Journal: the hotel\'s new name','https://wbjournal.com/article/southbridge-hotel-changes-name-following-historic-designation'],['Global Traveler: the factory as a hotel','https://www.globaltravelerusa.com/former-massachusetts-glasses-factory-transforms-into-new-hotel']],
  brick='yes',hours='?'),

N('hamilton-woolen-big-mill-southbridge','Hamilton Woolen Company Big Mill and Brick Square','Southbridge','worc','industry','standing',42.08265,-72.04317,'site','view','walk','','1836',
  'A mill site since 1750. James and Perez Wolcott built a cotton mill here in 1812, and in 1814 what was then the world\'s largest cotton mill, but a dam of theirs gave way and ruined them. Boston investors formed the Hamilton Woolen Company in 1831, raised the dam and in 1836 built the Big Mill, a five-story brick mill much altered in 1850, with Brick Square, a quadrangle of brick housing for the mill hands, beside it.',
  'The Big Mill, with a stairwell at one end topped by a tower and a Romanesque belfry; the Wikipedia article says the last main mill building left is the Dresser Street mill. Five Greek Revival brick worker houses of the 1830s survive around Mill Street, Canal Street and Brick Row, one of them later used as company offices. What the buildings are used for now was not checked.',
  '',
  'Private buildings at the meeting of McKinstry Brook and the Quinebaug River; look from Mill Street, Canal Street and Brick Row. The pin is on the mill complex as seen on the aerial.',
  [W('Hamilton Woolen Company Historic District')],
  brick='yes'),

N('central-mills-southbridge','Central Mills','Southbridge','worc','industry','standing',42.07727,-72.03114,'site','view','walk','','1837, 1908',
  'The Central Manufacturing Company was set up in 1837 on the site of Southbridge\'s first grist and saw mills, and the town grew up around it. When most New England textile mills were failing, it rebuilt instead: in 1908 it pulled down much of the 1837 mill and put up the present two-story brick mill, with the surviving 1837 section joined to its back.',
  'Three brick buildings at Foster and North streets: the 1908 Romanesque Revival mill with round-arched windows and a small tower, the small one-story 1908 office in the same style, and a plain 1915 brick warehouse across North Street. The mill stands at the dam on the Quinebaug River.',
  '',
  'Private buildings; look from Foster, North and Central streets. Inside not checked.'+DT,
  [W('Central Mills Historic District')],
  th=[42.07560,-72.03256],thn='Foster Street parking lot',brick='yes'),

N('sacred-heart-church-southbridge','Sacred Heart Church and its school, rectory and convent','Southbridge','worc','worship','standing',42.0779,-72.0289,'exact','view','walk','','1909–1926',
  'Southbridge\'s second French Canadian Catholic parish, set up in 1908. The rectory and convent were built first, from 1909; the school opened in 1910, first run by the same sisters as the Notre Dame school; the church was not finished until 1926. The diocese announced in 2010 that the parish would close and join Notre Dame, and the Associated Press reported in 2018 that a developer had bought the church for $325,000 and planned apartments on part of the site.',
  'Four buildings on Charlton Street. The church is Gothic, with pointed windows and buttresses; the other three are Colonial Revival brick: the two-and-a-half-story rectory at 40 Charlton Street with its round front bay, the convent with two round bays and a porch, and the two-story school with three round-arched doors. What has been done with the buildings since 2018 was not checked.',
  '',
  'Closed as a church and privately owned: look from Charlton Street only.',
  [W('Sacred Heart Church Historic District (Southbridge, Massachusetts)')],
  brick='some',conf='mixed'),

N('centre-village-southbridge','Centre Village: Main Street, Southbridge','Southbridge','worc','town','standing',42.0755,-72.0345,'area','public','walk','','1810s–1910s',
  'Southbridge\'s old business street, along Main Street for about 0.4 miles from Hamilton Street to Coombs Street. The town grew as the Quinebaug was harnessed for textiles and then optical goods, and Main Street became both its shopping street and where its mill owners built their houses, so commercial blocks of the 1840s to the 1910s stand among good houses of the same years.',
  'At the east end the 1810s house of Ebenezer Ammidown, now a cultural center; at the west end the Greek Revival former Universalist church of about 1840; and the Jacob Edwards Library of 1914, a Georgian Revival design by Daniel Burnham. Brick and wooden commercial blocks in between, in many styles.',
  '',
  'Public streets owned by the town; Main Street is Route 131. The buildings are private: look from the sidewalk.'+DT,
  [W('Centre Village Historic District')],
  th=EB,thn=EBN,brick='?'),
]

PIN_NOTES={
 'notre-dame-church-southbridge':'OpenStreetMap point on the church, 446 Main Street; looked at on the aerial.',
 'southbridge-town-hall':'OpenStreetMap point on the town hall, 41 Elm Street; looked at on the aerial.',
 'elm-street-congregational-southbridge':'OpenStreetMap point on the church, 61 Elm Street; looked at on the aerial.',
 'elm-street-fire-house-southbridge':'OpenStreetMap point on the fire station, 24 Elm Street; looked at on the aerial.',
 'globe-village-fire-house-southbridge':'Address-lookup point for West Street near Main Street; the building itself was not picked out on the aerial, so the pin marks only the general spot near the corner of West and Main streets.',
 'american-optical-southbridge':'OpenStreetMap point on the hotel, 14 Mechanic Street; looked at on the aerial.',
 'hamilton-woolen-big-mill-southbridge':'Moved onto the large mill complex by the river seen on the aerial, about 60 m from the Register point.',
 'central-mills-southbridge':'Moved onto the mill complex north of North Street seen on the aerial, about 90 m from the Register point.',
 'sacred-heart-church-southbridge':'Register point, which falls on the cross-shaped church on the aerial.',
 'centre-village-southbridge':'Register point for the district, on Main Street; the district runs about 0.4 miles along it.',
}
