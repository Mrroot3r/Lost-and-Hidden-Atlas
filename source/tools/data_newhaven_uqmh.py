# November 26, 2026: New Haven, Connecticut. A "videos" session (PROMPTS.md job 9): the names came from one video's tour
# of old New Haven buildings (the record is source/videos/20251107_NqHcwWIYeSQ.md); the video is a tip and nothing here
# rests on it. Sources read: Wikipedia (each article named in the links), the National Register nomination for the New Haven
# Green Historic District (1970), the National Park Service's Amistad page for United Church, the New Haven Building Archive
# (Yale) on Center Church, and the pages of Center Church, Trinity Church, Christ Church, the New Haven Free Public Library,
# the Yale Peabody Museum and the Yale Visitor Center for hours. United Church's and the Catholic parish's own sites would
# not open; the City of New Haven's park pages refused every request.
# Pins are address-lookup points (PointAddress) or a Wikipedia point, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'newhaven_uqmh','label':'Connecticut: old New Haven, the Green, Yale and East Rock','added':'2026-11-26 07:35'}

IVES=['New Haven Free Public Library: Ives Main Library','https://nhfpl.org/locations/ives-main-library/']
GREEN=' Parking round the Green is two-hour metered street parking on Elm, Grove, College and Temple Streets (meters run 7 a.m. to 9 p.m. Monday to Saturday), and Yale\'s Lot 51 on Temple Street at Wall Street is open to the public after 4:30 p.m. (the public library\'s page).'
NHGNR=['National Register nomination: New Haven Green Historic District (1970)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/70000838_text']
YVC=['Yale Visitor Center: tours','https://visitorcenter.yale.edu/tours']
YARD=' Yale buildings are seen from the street and the open courtyards; the Yale Visitor Center, 149 Elm Street, is open Monday to Saturday and runs one-hour campus tours for the general public (registration required).'

PLACES=[
N('center-church-on-the-green-new-haven','Center Church on the Green (First Church of Christ) and its crypt','New Haven','ctsw','worship','standing',41.30788,-72.92659,'exact','open','walk','','1812–1814',
  'The congregation began in 1638, the year New Haven was founded, and its first meeting house went up on this spot in 1639. The present building, its fourth, was built in 1812–1814: Asher Benjamin of Boston drew the first plans and his former pupil Ithiel Town made the final design and oversaw the work. It was built over part of the old burying ground on the Green, and a crypt beneath it keeps graves of the colony\'s first settlers. It is one of the three churches that make the New Haven Green a National Historic Landmark district.',
  'A brick Federal meeting house with wood trim and a tall spire, the middle of the three churches on the east side of the Green. The 1970 Register form says its exterior had remained unchanged. The crypt under the church, with old gravestones, can be seen on the church\'s crypt tours. Interior not otherwise checked.',
  '',
  'Owned by the congregation, First Church of Christ, 250 Temple Street. Sunday service at 11 a.m.; crypt tours on the second Sunday of each month at 10 a.m., meeting in the narthex, limited to 30 people, first come first served (the church\'s own page). Other sources give older crypt-tour days; the church\'s page wins.'+GREEN,
  [['Center Church on the Green','https://www.newhavencenterchurch.org/'],['New Haven Building Archive (Yale): Center Church on the Green','https://nhba.yale.edu/building?id=205'],NHGNR,W('New Haven Green')],
  brick='yes',hours='Sunday service 11 a.m.; crypt tours second Sunday of the month at 10 a.m.'),

N('trinity-church-on-the-green-new-haven','Trinity Church on the Green','New Haven','ctsw','worship','standing',41.30688,-72.92719,'exact','open','walk','','1814–1816',
  'Ithiel Town designed this Episcopal church in 1813 and it was built in 1814–1816 of local trap rock. It is counted as one of the first large Gothic churches in America, built before the Gothic Revival took hold in England. It stands at the corner of Temple and Chapel Streets, the southernmost of the three churches on the Green.',
  'The early Gothic exterior of red-brown trap rock survives largely as built. Inside, mostly later: oak pews with doors, gilt arches, eight stained glass windows on the side walls, four of them by Tiffany, and a nine-petalled rose window over the chancel. Open for services; interior otherwise not checked.',
  '',
  'Owned by the Episcopal parish, 230 Temple Street. Sunday services at 7:45 a.m. and 10:30 a.m., a Wednesday Eucharist at 12:10 p.m., and Thursday choral evensong at 5:30 p.m. from mid-January (the parish\'s weekly worship page, November 2026).'+GREEN,
  [W('Trinity Church on the Green'),['Trinity on the Green: weekly worship schedule','https://www.trinitynewhaven.org/weekly-worship-schedule'],NHGNR],
  brick='no',hours='Sunday 7:45 and 10:30 a.m.; Wednesday 12:10 p.m.'),

N('united-church-on-the-green-new-haven','United Church on the Green (Old North Church)','New Haven','ctsw','worship','standing',41.30864,-72.92603,'exact','open','walk','','1813–1815',
  'Built in 1813–1815 as the North Church, the northernmost of the three churches on the Green. The plans are attributed to David Hoadley and were changed by the builder, Ebenezer Johnson Jr. In 1884 the congregation merged with Third Church to make the United Church. Members of both churches worked against slavery: one helped found the committee that raised the defence of the Amistad captives, and Roger Sherman Baldwin, a member here, argued their case.',
  'A brick Federal church with wood trim and four fluted Ionic columns on its front, at the corner of Temple and Elm Streets. A plaque inside remembers Roger Sherman Baldwin. Interior not otherwise checked.',
  '',
  'Owned by the congregation, 270 Temple Street. The church\'s own site could not be opened when this was written; a web search quoting it gives Sunday worship at 10 a.m.'+GREEN,
  [['National Park Service: United Church on the Green','https://www.nps.gov/places/united-church-on-the-green.htm'],NHGNR,['United Church on the Green','https://unitednewhaven.org']],
  brick='yes',hours='Sunday 10 a.m. (from a search result; the church\'s site would not open)'),

N('new-haven-city-hall','New Haven City Hall','New Haven','ctsw','civic','standing',41.30738,-72.92459,'exact','public','walk','','1861',
  'Henry Austin designed City Hall, finished in 1861, and the county courthouse beside it on the north went up in 1871–1873; they are early examples of High Victorian Gothic in the United States. The brownstone weathered badly, the clock tower came down in the 1950s, and by the 1970s both were to be demolished. In 1976 much of the back and north parts were torn down, but local preservationists saved the front, and the clock tower was rebuilt.',
  'The Victorian Gothic front of banded brownstone on Church Street, facing the Green, with the rebuilt clock tower. The Amistad memorial (1992) stands in front. What is behind the front is newer. Interior not checked.',
  '',
  'A working city hall at 165 Church Street, owned by the City of New Haven (it is the city\'s seat of government); seen from the street and the Green.'+GREEN,
  [W('New Haven City Hall and County Courthouse')],
  brick='no',hours=''),

N('new-haven-county-courthouse','New Haven County Courthouse','New Haven','ctsw','civic','standing',41.30879,-72.92398,'exact','view','walk','','1914–1917',
  'Built in 1914–1917 to a competition design by William H. Allen and Richard Williams, it helped bring the City Beautiful movement to New Haven. It was the scene of Griswold v. Connecticut, the case over the right to birth control. It was threatened with demolition in 1956 and was listed on the National Register in 2003.',
  'A three-storey Beaux Arts building of white Vermont marble with Ionic porches, at the corner of Elm and Church Streets facing the Green. Inside, a central atrium finished in marble, mahogany, brass and plaster; whether visitors may walk in was not checked.',
  '',
  'A state court building at 121 Elm Street; seen from the street and the Green.'+GREEN,
  [W('New Haven County Courthouse')],
  brick='no',hours=''),

N('richard-c-lee-courthouse-new-haven','Richard C. Lee United States Courthouse (old Post Office)','New Haven','ctsw','civic','standing',41.30665,-72.92515,'exact','view','walk','','1913–1919',
  'James Gamble Rogers designed this federal courthouse and post office, built in 1913–1919, to suit the older public buildings on the Green, as Frederick Law Olmsted Jr. and Cass Gilbert had advised in their 1910 plan for the city. William Howard Taft, then teaching at Yale, spoke at the cornerstone ceremony in 1914. It was to be demolished in the 1960s but was renovated instead; the post office left in 1979.',
  'A Classical Revival building clad in Tennessee marble on the east side of the Green, on Church Street. Interior not checked.',
  '',
  'A federal court building at 141 Church Street; seen from the street and the Green.'+GREEN,
  [W('Richard C. Lee United States Courthouse')],
  brick='no',hours=''),

N('christ-church-new-haven','Christ Church New Haven','New Haven','ctsw','worship','standing',41.31199,-72.93227,'exact','open','walk','','1895–1898',
  'An Episcopal parish that began as an offshoot of Trinity Church on the Green. Its Gothic Revival church on Broadway, designed by Henry Vaughan, was finished in 1898; the stone tower is modelled on that of Magdalen College, Oxford. It was listed on the National Register in 2009.',
  'Inside: wood carving by Johannes Kirchmayer, above all on the rood screen; stained glass by C. E. Kempe of London, including a large window over the font; stone figures and a carved Caen stone reredos at the high altar. Open for its daily services.',
  '',
  'Owned by the parish, 84 Broadway. Services every day; Sunday Masses at 8:45, 10 and 11 a.m., weekday morning prayer at 8 a.m. and a noon Mass on Monday, Wednesday and Friday (the parish\'s own page). Off-street parking at 90 Broadway on Sundays and after 5 p.m. on weekdays (the same page).',
  [W('Christ Church (New Haven)'),['Christ Church New Haven','https://www.christchurchnh.org/']],
  brick='?',hours='Sunday Mass 8:45, 10 and 11 a.m.; weekdays 8 a.m. morning prayer, Mass 12:15 p.m. Monday, Wednesday, Friday'),

N('st-mary-church-new-haven','St. Mary Church, birthplace of the Knights of Columbus','New Haven','ctsw','worship','standing',41.3117,-72.92382,'exact','view','walk','','1870–1874',
  'The first Catholic parish in New Haven, begun in 1832. The church on Hillhouse Avenue, drawn by James Murphy of Providence, was dedicated in 1874; the spire in his plans was not built until a later renovation paid for by the Knights of Columbus. In 1882 the assistant pastor, Michael J. McGivney, founded the Knights of Columbus here; his remains lie in the church, and he was beatified in 2020. It is now the seat of the city-wide Blessed Michael McGivney Parish.',
  'A Gothic church at the foot of Hillhouse Avenue with McGivney\'s tomb inside. The arches, aisle walls and wainscot were stencilled in a renovation to patterns found from the church\'s early decoration. Interior not otherwise checked.',
  '',
  'Owned by the Archdiocese of Hartford, 5 Hillhouse Avenue. The parish\'s own pages could not be read when this was written, so Mass times are not given here. Street parking.',
  [W("St. Mary's Church (New Haven, Connecticut)")],
  brick='?',hours='?'),

N('plymouth-congregational-church-new-haven','Plymouth Congregational Church (Temple Keser Israel)','New Haven','ctsw','worship','standing',41.31144,-72.94462,'site','view','walk','','1901',
  'A brownstone Romanesque Revival church at Chapel and Sherman Streets, built for a congregation founded in 1831 and dedicated as Plymouth Congregational Church in 1901. It was sold in 1949 to a Jewish congregation, Temple Keser Israel, and used as a synagogue until 1968. It was later rebuilt inside for medical offices.',
  'The brownstone front with a gable between two square towers, the taller with a turreted belfry; the old entrances are at its base. The inside was rebuilt for offices.',
  '',
  'Private offices, 1469 Chapel Street. Look from the street.',
  [W('Plymouth Congregational Church (New Haven, Connecticut)')],
  brick='no',hours=''),

N('union-station-new-haven','New Haven Union Station','New Haven','ctsw','rail','standing',41.29763,-72.92675,'exact','open','walk','stations','1920',
  'Cass Gilbert designed this Beaux Arts station, opened in 1920 after the earlier Union Station near the foot of Meadow Street burned. It served the New York, New Haven and Hartford Railroad; the building was shut in 1973, leaving only the passage under the tracks open, and was nearly demolished before a rebuilding reopened it in 1985. It is the city\'s main station.',
  'A 35-foot-high waiting room with limestone walls, ornate ceilings, chandeliers, marble fittings and wooden benches carrying models of New Haven Railroad trains.',
  '',
  'A working railway station at 50 Union Avenue, owned by the state. Its opening hours were not checked on a page of whoever runs it. A parking garage stands beside it.',
  [W('Union Station (New Haven)')],
  brick='?',hours='?'),

N('quinnipiac-brewery-new-haven','Quinnipiac Brewery (Brewery Square)','New Haven','ctsw','industry','standing',41.30363,-72.89324,'exact','view','walk','','1882–1916',
  'Two German-born brewers, Peter Schleipmann and William Spittler, founded the brewery in 1882. Its six-storey Romanesque main building dates from 1882 and got its present front in 1896; the office is of the 1880s and the bottling plant of 1916, put across a street to satisfy the tax men. Brewing went on until the 1930s; it was listed on the National Register in 1983 and most of it is now homes.',
  'A complex of brick buildings by the Quinnipiac River in Fair Haven, led by the six-storey brewhouse with corner towers.',
  '',
  'Private apartments, 19–23 River Street. Look from the street.',
  [W('Quinnipiac Brewery')],
  brick='?',hours=''),

N('taft-hotel-new-haven','Hotel Taft','New Haven','ctsw','hotel','standing',41.30683,-72.92872,'exact','view','walk','hotels','1912',
  'Frank Mills Andrews designed this twelve-storey hotel at Chapel and College Streets, finished in 1912 with 450 rooms. A tavern had stood on the corner since 1659. The hotel shut in 1973, after a new hotel opened nearby in the urban-renewal years, and the building was turned into apartments.',
  'The tall hotel on the corner of College and Chapel Streets across from the Green. A bar on the ground floor carries on the corner\'s long run as a drinking place; the rest is private.',
  '',
  'Private apartments, 265 College Street; look from the street.'+GREEN,
  [W('Taft Hotel (New Haven)')],
  brick='?',hours=''),

N('ives-memorial-library-new-haven','Ives Memorial Library (New Haven Free Public Library)','New Haven','ctsw','civic','standing',41.30906,-72.9248,'exact','open','walk','','1908–1911',
  'The main library of New Haven\'s public library, which began in 1887 in rented rooms. Cass Gilbert designed the neo-Georgian building on the Green, finished in 1911, and it was renovated and enlarged in 1990.',
  'Inside: two lunette murals of New Haven history in the main hall by Bancel LaFarge, Rip Van Winkle murals of 1934 in the meeting room painted under the Public Works program, and stained glass laylights and windows by David Wilson.',
  '',
  'A public library at 133 Elm Street, corner of Temple Street. Hours from the library\'s own page, November 2026; it shuts on holidays.'+GREEN,
  [W('New Haven Free Public Library'),IVES],
  brick='yes',hours='Monday to Thursday 10 a.m. to 8 p.m.; Friday and Saturday 10 a.m. to 5 p.m.'),

N('peabody-museum-new-haven','Yale Peabody Museum','New Haven','ctsw','civic','standing',41.31599,-72.92124,'site','open','walk','','1925',
  'George Peabody founded the museum in 1866 at the urging of his nephew, the fossil hunter Othniel Charles Marsh. Its first building opened in 1876 and was pulled down in 1917 for the Memorial Quadrangle; the present building on Whitney Avenue was dedicated in 1925. It closed in 2020 for its first full renovation in ninety years and reopened in 2024.',
  'The Great Hall of Dinosaurs with a mounted young Brontosaurus and the 110-foot mural The Age of Reptiles, with wildlife dioramas and Egyptian, mineral and Connecticut collections. The 1876 building is gone.',
  '',
  'Owned by Yale University, 170 Whitney Avenue. Free. Open Tuesday to Saturday 10 a.m. to 5 p.m. and Sunday noon to 5 p.m.; shut Mondays and on major holidays. Yale parking lot 22V on weekdays and metered street parking nearby (the museum\'s visit page).',
  [W('Peabody Museum of Natural History'),['Yale Peabody Museum: visit','https://peabody.yale.edu/visit']],
  brick='?',hours='Tuesday to Saturday 10 a.m. to 5 p.m.; Sunday noon to 5 p.m. Free'),

N('harkness-tower-yale','Harkness Tower','New Haven','ctsw','landmark','standing',41.3093,-72.9294,'site','view','walk','','1917–1921',
  'Part of Yale\'s Memorial Quadrangle, given by Anna M. Harkness in memory of her son Charles. James Gamble Rogers designed the tower, built in 1917–1921 in English Perpendicular Gothic after the tower of St Botolph\'s in Boston, Lincolnshire, with details from St Giles\' in Wrexham, where Elihu Yale is buried. It is 216 feet tall, a foot for each year of Yale up to then, and holds a carillon. Since 1933 it has been part of Branford College.',
  'A stone tower rising in stages to a double crown with stone finials, with the carillon bells behind the clock faces. Repaired in 2009–2010.',
  '',
  'Owned by Yale University; seen from High Street and Library Walk.'+YARD,
  [W('Harkness Tower'),YVC],
  brick='no',hours=''),

N('sterling-memorial-library-yale','Sterling Memorial Library','New Haven','ctsw','civic','standing',41.31116,-72.92851,'exact','open','walk','','1931',
  'Yale\'s main library, opened in 1931 and designed by James Gamble Rogers as the centre of the Gothic Revival campus. It was paid for from the bequest of John W. Sterling, which asked for an "enduring, useful and architecturally beautiful edifice". Before it, Yale\'s books had been kept in the College Library on the Old Campus, now Dwight Hall.',
  'The entrance hall is built like the nave of a cathedral, of Indiana limestone and Ohio sandstone, with stone and wood carving, ironwork and hundreds of stained glass panes by G. Owen Bonawit. The nave and main reading rooms can be seen on guided tours; the collections are for cardholders.',
  '',
  'Owned by Yale University, 120 High Street. The Yale Visitor Center\'s campus tour (one hour, from 149 Elm Street, registration required) takes in the library. Street and garage parking downtown.',
  [W('Sterling Memorial Library'),YVC],
  brick='no',hours='By Yale Visitor Center campus tour, Monday to Saturday; registration required'),

N('woolsey-hall-yale','Woolsey Hall','New Haven','ctsw','civic','standing',41.31163,-72.92628,'site','view','walk','','1901',
  'Yale\'s largest hall, about 2,650 seats, built for the university\'s bicentennial in 1901 with the Memorial Rotunda and the University Commons, to designs by Carrère and Hastings. It is named for Theodore Dwight Woolsey, Yale\'s president from 1846 to 1871, and holds the Newberry Memorial Organ.',
  'A Beaux Arts hall at the corner of College and Grove Streets. Concerts by the New Haven Symphony Orchestra and Yale ensembles are the way in; times not checked.',
  '',
  'Owned by Yale University, 500 College Street; seen from the street.'+YARD,
  [W('Woolsey Hall'),YVC],
  brick='?',hours=''),

N('yale-bowl','Yale Bowl','New Haven','ctsw','landmark','standing',41.31334,-72.96053,'site','view','drive','','1913–1914',
  'Yale\'s football stadium, begun in August 1913 and opened in 1914 with 70,896 seats; the earth dug from the field was heaped round it to make the bowl. It gave the Rose Bowl its design and name, and so, in the end, the Super Bowl its name. The New York Giants played here in 1973 and 1974.',
  'An earth-banked elliptical bowl with an outer wall in a Gothic style echoing the campus. Games are the way in; ticket times not checked.',
  '',
  'Owned by Yale University, 81 Central Avenue, about 1.5 miles west of the campus. Seen from Central Avenue and Derby Avenue.',
  [W('Yale Bowl')],
  brick='?',hours=''),

N('soldiers-sailors-monument-east-rock','Soldiers\' and Sailors\' Monument, East Rock','New Haven','ctsw','landmark','standing',41.32722,-72.90472,'exact','public','drive','','1886–1887',
  'A war memorial on the summit of East Rock to the New Haven men who died in the Revolutionary War, the War of 1812, the Mexican War and the Civil War. Moffit & Doyle won the design competition; it was built in 1886 and dedicated on June 17, 1887, before a crowd of 175,000 with Generals Sherman and Sheridan as guests. It is 112 feet high and is seen for miles.',
  'A red granite shaft with bronze figures, topped by the Angel of Peace, with the names of battles on its four faces and a plaque listing the Civil War dead. The summit also looks out over New Haven and Long Island Sound.',
  '',
  'In East Rock Park, owned and run by the City of New Haven. The city\'s park pages could not be opened when this was written. Wikipedia gives the road to the summit as open April 1 to November 1, 8 a.m. to sunset, and in winter Friday to Sunday and holidays 8 a.m. to 4 p.m.; other listings say the park is shut from sunset to sunrise. On foot, the Giant Steps Trail climbs steeply to the summit from the south.',
  [["Wikipedia: Soldiers' and Sailors' Monument (New Haven)","https://en.wikipedia.org/wiki/Soldiers%27_and_Sailors%27_Monument_(New_Haven)"],W('East Rock Park'),W('East Rock')],
  conf='mixed',brick='no',hours='Summit road: April 1 to November 1, 8 a.m. to sunset; winter Friday to Sunday 8 a.m. to 4 p.m. (not confirmed by the city)'),
]

PIN_NOTES={
 'center-church-on-the-green-new-haven':'Address lookup of 250 Temple Street (a match on the house number).',
 'trinity-church-on-the-green-new-haven':'Address lookup of 230 Temple Street (a match on the house number).',
 'united-church-on-the-green-new-haven':'Address lookup of 270 Temple Street (a match on the house number).',
 'new-haven-city-hall':'Address lookup of 165 Church Street (a match on the house number).',
 'new-haven-county-courthouse':'Address lookup of 121 Elm Street (a match on the house number).',
 'richard-c-lee-courthouse-new-haven':'Address lookup of 141 Church Street (a match on the house number).',
 'christ-church-new-haven':'Address lookup of 84 Broadway (a match on the house number).',
 'st-mary-church-new-haven':'Address lookup of 5 Hillhouse Avenue (a match on the house number).',
 'plymouth-congregational-church-new-haven':'Address lookup of 1469 Chapel Street (placed along the street, not on a mapped house number). On the aerial it falls on the corner of Chapel and Sherman Streets; the church is the building on the north-east corner.',
 'union-station-new-haven':'Address lookup of 50 Union Avenue (a match on the house number).',
 'quinnipiac-brewery-new-haven':'Address lookup of 19 River Street (a match on the house number).',
 'taft-hotel-new-haven':'Address lookup of 265 College Street (a match on the house number).',
 'ives-memorial-library-new-haven':'Address lookup of 133 Elm Street (a match on the house number).',
 'peabody-museum-new-haven':'Address lookup of 170 Whitney Avenue (a match on the house number); Wikipedia\'s point is about 200 m north-east.',
 'harkness-tower-yale':'The point in the Wikipedia article; on the aerial it falls at the edge of High Street beside the tower.',
 'sterling-memorial-library-yale':'Address lookup of 120 High Street (a match on the house number).',
 'woolsey-hall-yale':'Address lookup of 500 College Street (a match on the house number).',
 'yale-bowl':'Address lookup of 81 Central Avenue (a match on the house number).',
 'soldiers-sailors-monument-east-rock':'Wikipedia\'s point for East Rock, which falls on the monument on the aerial.',
}
