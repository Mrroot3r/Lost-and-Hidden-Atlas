# November 24, 2026: Dayton, Ohio. A "videos" session (PROMPTS.md job 9): the names came from one video's tour of
# old Dayton buildings (the record is source/videos/20221029_H5qt3Q5vqeg.md); the video is a tip and nothing here
# rests on it. Sources read: Wikipedia (each article named in the links), the National Register list for Dayton,
# National Park Service pages (the Central Branch soldiers' home, the Dayton Aviation Heritage park's hours), the
# Department of Veterans Affairs history page on the Dayton chapel, a WYSO report on the Old Courthouse, and for
# hours the pages of whoever runs each place (St. Mary parish, Woodland Cemetery, the Dayton Arcade).
# Pins are ArcGIS address points or OpenStreetMap buildings, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'dayton_qtnc','label':'Ohio: old Dayton','added':'2026-11-24 06:39'}

DT=' Downtown parking is in garages, lots and street meters; their owners, hours and fees were not checked.'

PLACES=[

N('old-courthouse-dayton','Old Montgomery County Courthouse','Dayton','oh','civic','standing',39.75976,-84.19240,'exact','view','walk','','1847',
  'Dayton\'s old county courthouse, a Greek Revival temple of limestone modelled on the Temple of Hephaestus in Athens. A Dayton man, Horace Pease, showed the county commissioners sketches of the Acropolis, and they hired the New York architect Howard Daniels to draw the plans; Wikipedia gives 1847 as the year it was built. It is called the best surviving Greek Revival courthouse in the country and was put on the National Register in 1970.',
  'A columned limestone temple front on the corner of Third and Main, the centre of downtown. The building has been restored and is now used for events and exhibits; in May 2025 it opened to the public for a few days with a history exhibit. Interior not checked.',
  '',
  'Owned by Montgomery County, on Courthouse Square at the north-west corner of Third and Main Streets; seen from the square and the streets. It is not open at regular hours.'+DT,
  [W('Montgomery County Courthouse (Ohio)'),['WYSO: Old Courthouse open with an exhibit, May 2025','https://www.wyso.org/news/2025-05-27/old-courthouse-now-open-to-public-with-dayton-around-the-world-exhibit']],
  brick='no'),

N('dayton-arcade','Dayton Arcade','Dayton','oh','civic','standing',39.75817,-84.19256,'site','open','walk','','1902–1904',
  'Nine joined buildings round a glass-domed rotunda, built in 1902 to 1904 for a company led by Eugene J. Barney of the Barney & Smith Car Company, to plans by Frank M. Andrews. It was restored and reopened as a shopping centre in 1980, closed in 1991, and stood empty for about thirty years before a new restoration; it reopened to the public in August 2021 with apartments, offices, galleries and shops.',
  'The Third Street front is in a Flemish style said to be modelled on a guildhall in Amsterdam; the Fourth and Ludlow Street fronts are Italian Renaissance. Inside, a rotunda 90 feet across and 70 feet high under a glass dome, its trim carved with oak leaves, acorns, rams\' heads, wild turkeys and horns of plenty. The rotunda keeps its own hours, given on the Arcade\'s home page, and opens for events; shops and restaurants keep theirs.',
  '',
  'Privately owned and run as the Dayton Arcade, entered from Third, Fourth and Ludlow Streets. Its own page says to park in the garages nearby or at the meters round the block; pets are not allowed inside. The rotunda hours on its home page could not be read when this was written.',
  [W('Dayton Arcade'),['The Dayton Arcade','https://www.arcadedayton.com/'],['Dayton Arcade: questions and parking','https://www.arcadedayton.com/faqs/']],
  brick='?',hours='?'),

N('victoria-theatre-dayton','Victoria Theatre','Dayton','oh','civic','standing',39.76213,-84.19214,'exact','open','walk','','1866; rebuilt 1871',
  'Opened on New Year\'s Day 1866 as the Turner Opera House. Fire, thought to be arson, destroyed it on May 16, 1869; it was rebuilt to three storeys instead of six, partly on the surviving front, and reopened in 1871. It was later the Music Hall, the Grand Opera House, the Victoria Opera House and from 1903 the Victoria Theatre; the 1913 flood damaged it, and after the First World War it was remodelled and reopened in 1919 as the Victory Theatre. Set for demolition for a parking lot in 1975, it was saved by a public campaign and the National Register listing.',
  'A working 1,154-seat theatre on Main Street. A renovation from 1989 kept and restored the 1866 to 1871 front and the 1919 auditorium, with its plasterwork, marble, gilding and frescoes; it has an Estey pipe organ given by NCR. You see the inside by going to a show.',
  '',
  'Owned and run by Dayton Live, a non-profit arts group, at 138 North Main Street. Shows and box office hours are on its page; they were not read when this was written.'+DT,
  [W('Victoria Theatre (Dayton, Ohio)'),['Dayton Live: plan your visit','https://www.daytonlive.org/plan-your-visit']],
  brick='?',hours='?'),

N('dayton-masonic-center','Dayton Masonic Center','Dayton','oh','civic','standing',39.76535,-84.20290,'exact','view','walk','','1928',
  'Built as the Dayton Masonic Temple by an association of 14 Masonic bodies, and finished in 2 years and 9 months by 450 workers, most of them Masons; Wikipedia files it as completed in 1928. It is a contributing building in the Steele\'s Hill-Grafton Hill Historic District, on the National Register since 1986.',
  'A stone temple 265 feet long, 190 wide and 80 high, on the hill above the Great Miami River, built of steel, cement, Bedford stone and limestone and marble from Vermont, Alabama and Tennessee. Inside is used for lodge meetings, events and occasional guided tours; interior not checked.',
  '',
  'Owned by the Masonic temple association, 525 West Riverview Avenue; seen from the street. It has no regular public hours that a page read here gave. OpenStreetMap maps a garage about 500 m south-east, across the river on West First Street.',
  [W('Dayton Masonic Center')],
  brick='no'),

N('southern-ohio-lunatic-asylum','Southern Ohio Lunatic Asylum (Dayton State Hospital)','Dayton','oh','inst','standing',39.73790,-84.16088,'exact','view','drive','','1850s',
  'A state asylum laid out on the plan advocated by the Philadelphia doctor Thomas Story Kirkbride, on a 300-acre grounds; Wikipedia lists Samuel Sloan as its architect and files it under 1854. It was later the Dayton State Hospital and then the Dayton Mental Health Center. The hospital farm is now the Miami Valley Research Park in Kettering, and other land holds houses and Hospice of Dayton. On the National Register since 1979.',
  'The main building stands at Wayne and Wilmington Avenues and is now a retirement home. Seen from the street only; interior not checked.',
  '',
  'Private retirement housing at 2335 Wayne Avenue; not open to visitors. Seen from Wayne and Wilmington Avenues.',
  [W('Southern Ohio Lunatic Asylum')],
  brick='?'),

N('dayton-biltmore-hotel','Dayton Biltmore Hotel','Dayton','oh','hotel','standing',39.76285,-84.19213,'exact','view','walk','','1929',
  'A Beaux-Arts hotel by Frederick Hughes, opened on November 16, 1929, at First and Main Streets, and one of the tallest buildings in Dayton. Hilton bought it in 1946; it was a Sheraton from 1965 and the Biltmore Towers Hotel from 1974. In 1981 it became housing for older people, and it went on the National Register in 1982. Related Companies bought it in 2020 and renovated it in 2022.',
  'A tall brick and terra cotta tower in dark brown and white. Apartments; seen from the street. Interior not checked.',
  '',
  'Private apartments at 210 North Main Street; seen from the street.'+DT,
  [W('The Dayton Biltmore Hotel')],
  brick='?'),

N('st-mary-catholic-church-dayton','St. Mary Catholic Church','Dayton','oh','worship','standing',39.75338,-84.16812,'exact','open','drive','','1905–1906',
  'A parish church on Xenia Avenue at Allen Street. The parish was formed from Emanuel Church, Dayton\'s first Catholic parish; a first church on this land was consecrated in 1860. The present church was begun in July 1905 and consecrated in November 1906, and the parish is still active, with Mass in English and Spanish. Its size has made it a landmark for pilots.',
  'A large church on its rise east of downtown. The parish page shows a 1920 Austin pipe organ. Inside can be seen at Mass; other interior detail not checked.',
  '',
  'Run by St. Mary parish, Archdiocese of Cincinnati, 310 Allen Street. Mass times are from the parish page; it was read in November 2026 and still showed its Christmas 2025 notice. Parking was not checked.',
  [W('St. Mary\'s Catholic Church (Dayton, Ohio)'),['St. Mary Catholic Church, Dayton','https://stmarydayton.org']],
  brick='?',hours='Mass Sunday 9:45 a.m. (English) and 12:15 p.m. (Spanish); Monday to Thursday 6 p.m. (Spanish)'),

N('home-chapel-dayton-va','Home Chapel, Central Branch of the National Home for Disabled Volunteer Soldiers','Dayton','oh','worship','standing',39.74358,-84.25729,'exact','view','drive','','1868–1870',
  'The chapel of the Central Branch of the National Home for Disabled Volunteer Soldiers, founded at Dayton in 1867 for Union veterans of the Civil War and now the Dayton VA Medical Center. Authorized in December 1868 and dedicated on October 26, 1870, it was the first chapel building in the history of what became the Department of Veterans Affairs; veterans living at the Home quarried the limestone on the grounds and helped build it. It was rededicated in 2012 after a renovation. The old part of the campus and the national cemetery beside it are a National Historic Landmark district.',
  'A limestone chapel (Building 118). In the 1870s it had stained-glass windows; what survives inside was not checked. East of the modern hospital 28 buildings from before 1930 survive, among them the Putnam Library (Building 120), with a lake, a stone grotto arch of about 1900 and two springs on the east side of the campus; the Catholic chapel, Building 119, stands close by.',
  '',
  'On the grounds of the working Dayton VA Medical Center, 4100 West Third Street, run by the Department of Veterans Affairs; the American Veterans Heritage Center looks after the historic district. Seen from the campus roads; whether the chapel opens to visitors was not checked. OpenStreetMap maps a small lot on New Hampshire Avenue just south of the chapel.',
  [['National Park Service: Central Branch, Dayton','https://www.nps.gov/places/central-branch-dayton-ohio.htm'],['VA history: the oldest chapel','https://department.va.gov/history/the-history-of-vas-oldest-chapel/'],W('Dayton Veterans Affairs Medical Center')],
  brick='no',th=[39.74303,-84.25738],thn='Lot on New Hampshire Avenue'),

N('dayton-ymca-building','Dayton YMCA Building (Landing Apartments)','Dayton','oh','civic','standing',39.76355,-84.19567,'exact','view','walk','','1928–1929',
  'The YMCA\'s downtown building, designed by Schenck & Williams; Wikipedia files it as completed in 1928, and a Dayton Daily News piece gives its dedication as September 1929. It went on the National Register in 1988 and is now the Landing Apartments.',
  'A tall building on Monument Avenue facing the river. Apartments; seen from the street. Interior not checked.',
  '',
  'Private apartments at 117 West Monument Avenue; seen from the street.'+DT,
  [W('Landing Apartments')],
  brick='?'),

N('woodland-cemetery-gateway-dayton','Woodland Cemetery gateway, chapel and office','Dayton','oh','burial','standing',39.74253,-84.17832,'exact','public','walk','cemeteries','1842; gateway 1889',
  'One of the oldest garden cemeteries in the country, incorporated in 1842 by John Whitten Van Cleve and grown from 40 to 200 acres. The Romanesque gateway, chapel and office, finished in 1889, were built of stone from the cemetery\'s first wall and are on the National Register; the oldest 105 acres are a historic district as well. The hill, the highest point in Dayton, was a refuge in the 1913 flood.',
  'The stone gateway on Woodland Avenue; Wikipedia says the chapel has one of the finest original Tiffany windows in the country. Inside the grounds a receiving vault of 1847, a 1970 mausoleum with twelve large stained glass windows, and over 3,000 trees. The cemetery runs tours and events.',
  '',
  'Run by the Woodland Cemetery Association, 118 Woodland Avenue. The grounds are open to visitors at the hours on its page; drive in and park on the cemetery roads.',
  [W('Woodland Cemetery and Arboretum'),['Woodland Cemetery and Arboretum','https://www.woodlandcemetery.org/']],
  brick='no',hours='Grounds daily 8 a.m. to 7 p.m. (6 p.m. in winter); office Monday to Friday 8 a.m. to 5 p.m.; mausoleum 9 a.m. to 5 p.m.'),

N('wright-cycle-company-dayton','Wright Cycle Company shop','Dayton','oh','industry','standing',39.75560,-84.21179,'exact','open','walk','','1895–1897',
  'Orville and Wilbur Wright ran a bicycle business in Dayton from 1892 at six places in turn, and used its profits to pay for their flying experiments. The brick building at 22 South Williams Street, where they worked from 1895 to 1897 with their print shop upstairs, is the only one of their bicycle shops still on its first foundation and in its first place. It is part of Dayton Aviation Heritage National Historical Park.',
  'The small brick shop on Williams Street. Tours of the shop start at the Wright-Dunbar Interpretive Center round the corner, which has exhibits and a recreated print shop.',
  '',
  'Run by the National Park Service. The visitor centre is at 16 South Williams Street; hours are from the park\'s page. OpenStreetMap maps a lot about 90 m north-east on Sanford Court.',
  [W('Wright Cycle Company'),['National Park Service: hours','https://www.nps.gov/daav/planyourvisit/hours.htm']],
  brick='?',hours='Wednesday to Sunday 9 a.m. to 4 p.m.; closed Thanksgiving, Christmas and New Year\'s Day',th=[39.75595,-84.21082],thn='Lot on Sanford Court'),

]

PIN_NOTES={
'old-courthouse-dayton':'Address point for 7 North Main Street, on the courthouse.',
'dayton-arcade':'Address point for 35 West Fourth Street, on the Arcade block.',
'victoria-theatre-dayton':'Address point for 138 North Main Street, on the theatre.',
'dayton-masonic-center':'Address point for 525 West Riverview Avenue, on the temple.',
'southern-ohio-lunatic-asylum':'Moved about 190 m south from the street address point for 2335 Wayne Avenue, which fell on Wilmington Avenue, onto the centre of the long winged main building seen on the aerial.',
'dayton-biltmore-hotel':'Address point for 210 North Main Street, at First and Main.',
'st-mary-catholic-church-dayton':'Address point for 310 Allen Street, on the church.',
'home-chapel-dayton-va':'OpenStreetMap building mapped as Building 118, the Protestant chapel.',
'dayton-ymca-building':'OpenStreetMap building named The Landing, a 12-storey apartment block on West Monument Avenue; the street address point fell about 50 m east, by the church next door.',
'woodland-cemetery-gateway-dayton':'Address point for 118 Woodland Avenue, at the gateway.',
'wright-cycle-company-dayton':'Address point for 22 South Williams Street, on the shop.',
}
