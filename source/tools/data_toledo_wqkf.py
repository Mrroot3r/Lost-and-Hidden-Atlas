# November 23, 2026: Toledo, Ohio. A "videos" session (PROMPTS.md job 9): the names came from one video's tour of
# old Toledo buildings (the record is source/videos/20230122_W6cUcDA_7_k.md); the video is a tip and nothing here
# rests on it. Sources read: Wikipedia (each article named in the links), the National Register list for Lucas County,
# the Clio page and the Toledo Lucas County Public Library's architecture collection for the Secor Hotel, the Ohio
# History Connection's marker text for the State Hospital cemetery, a University of Toledo news story, and for hours the
# pages of whoever runs each place (the cathedral, the Historic Church of St. Patrick, the Episcopal Church's map of its
# parishes, the Valentine Theatre). Pins are ArcGIS address points, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'toledo_wqkf','label':'Ohio: old downtown Toledo','added':'2026-11-23 14:33'}

DT=' Downtown Toledo has metered streets and public garages; their hours and fees were not checked.'

PLACES=[

N('nasby-building-toledo','Nasby Building','Toledo','oh','civic','standing',41.65233,-83.53721,'exact','view','walk','','1891–1895',
  'An eight-storey office block at Madison Avenue and Huron Street, built 1891 to 1895 for Horace Walbridge to designs by Toledo architect Edward Fallis, who kept his office in it until he died in 1927. It was Toledo\'s tallest building until 1906 and is named for Petroleum V. Nasby, the pen name of Blade editor David Ross Locke. Its corner tower was said to be modelled on the Giralda in Seville; the cupola on top came off in the 1930s.',
  'In the 1960s the Nasby and the Wayne Building next door were wrapped in glass and enamel panels to look like one building, the "Madison Building". Whether that cladding has now come off, and the state of the inside, were not checked.',
  '',
  'Privately owned, at 605 Madison Avenue; seen from the street.'+DT,
  [W('Nasby Building')],
  brick='?'),

N('secor-hotel-toledo','Secor Hotel (Secor Building)','Toledo','oh','hotel','standing',41.65013,-83.53684,'exact','view','walk','','1906–1908',
  'A large luxury hotel built 1906 to 1908 at 425 Jefferson Avenue, with over 300 rooms and two dining rooms, advertised as the first fireproof hotel between New York and Chicago. Sources differ on the architect: the city library holds George S. Mills\'s drawings for it, while one account names Charles Nordhoff or Mills. Renovated in 1935 and 1947, it closed in 1969 and later held offices. On the National Register since 1976.',
  'The hotel\'s French Renaissance lobby was its show piece. Whether any of it survives, and the inside generally, were not checked; an account of 2018 said most of the building stood empty.',
  '',
  'Privately owned office building at 425 Jefferson Avenue; seen from the street.'+DT,
  [['Clio: The Hotel Secor','https://theclio.com/entry/68360'],['Toledo Lucas County Public Library: George S. Mills drawings, 425 Jefferson Avenue','https://tlcplarchitecture.omeka.net/items/show/172']],
  conf='mixed',brick='yes'),

N('rosary-cathedral-toledo','Our Lady, Queen of the Most Holy Rosary Cathedral','Toledo','oh','worship','standing',41.67249,-83.55611,'exact','open','walk','','1925–1931',
  'The cathedral of the Catholic Diocese of Toledo, on Collingwood Boulevard in the Old West End. Pittsburgh architect William Perry designed it; ground was broken in 1925 and it opened for services in 1931, though it was not dedicated until 1940. Its builders say it was designed with Toledo, Spain, in mind, in the Spanish Plateresque style, and it seats 1,400.',
  'Massachusetts granite with Indiana limestone trim; a rose window showing the life of Mary, paid for in children\'s pennies; two octagonal bell towers flank the front (a third was planned and never built); mosaics over the altar, cleaned in 2000; a four-manual Skinner pipe organ of 1930.',
  '',
  'An active cathedral at 2535 Collingwood Boulevard. Its own page welcomes visitors around Mass times and during parish office hours. OpenStreetMap maps a parking lot to the south, off Delaware Avenue; whose it is was not checked.',
  [W('Rosary Cathedral (Toledo, Ohio)'),['Rosary Cathedral: Visit us','https://rosarycathedral.org/about-us/visit-us/']],
  th=[41.67158,-83.55588],thn='Lot on Delaware Avenue',brick='no',hours='Around Mass times, and Monday to Friday 9 a.m. to 4 p.m. (parish office hours)'),

N('jefferson-center-toledo','Old Central Post Office (Jefferson Center)','Toledo','oh','civic','standing',41.65482,-83.54397,'exact','view','walk','','1911',
  'Toledo\'s main post office of 1911, in a classical design by the government architect James Knox Taylor, faced in sandstone. The post office left in the 1970s, and from 1972 to 2000 the city schools ran a vocational school in it. The schools considered demolishing it in 2011; they sold it to ProMedica in 2019, and a plan for a technology campus inside stalled in 2023.',
  'A sandstone classical front on Jefferson Avenue. Interior not checked; what use it has now was not checked.',
  '',
  'Privately owned, at 1300 Jefferson Avenue; seen from the street.'+DT,
  [W('Jefferson Center (Toledo, Ohio)')],
  brick='no'),

N('ymca-building-toledo','Central YMCA Building','Toledo','oh','civic','standing',41.65352,-83.54281,'exact','view','walk','','1934–1935',
  'The Toledo YMCA\'s building of 1934 to 1935 by architect John N. Richards, scaled down from a 1930 design because of the Depression, with 153 bedrooms, a chapel, a pool and two gymnasiums. The dormitories closed in the 1970s and the YMCA left in 1980; Lucas County later used it for court services. On the National Register since 1982.',
  'Modelled on the Palazzo Davanzati in Florence: patterned polychrome brick with diaper work along the top, clay pan-tile roofs, round windows, and over the stone-and-tile entrance a medallion of St. George and the dragon, with terra cotta from St. Louis. Interior not checked.',
  '',
  'Owned and used by Lucas County, at 1100 Jefferson Avenue; seen from the street.'+DT,
  [W('YMCA Building (Toledo, Ohio)')],
  brick='?'),

N('blade-building-toledo','The Blade Building','Toledo','oh','civic','standing',41.65502,-83.53330,'exact','view','walk','','1926–1927',
  'The home of the Toledo Blade, the city\'s newspaper since 1835, at Superior, Huron and Beech streets. Construction photographs date from the autumn of 1926, and it opened on May 1, 1927, when President Coolidge started the presses from the White House with a golden key. The printing presses here closed after 2014.',
  'A grey castle-like stone front on Superior Street, with a historical marker beside it. Interior not checked; whether the newsroom is still inside was not checked.',
  '',
  'Privately owned, at 541 North Superior Street; seen from the street. The opening date and the golden key are from the newspaper\'s own history pages as a search result quoted them; the pages themselves could not be read when this was written.'+DT,
  [W('The Blade (Toledo, Ohio)'),['The Blade: Monday Memories, the Blade building','https://www.toledoblade.com/a-e/monday-memories/2020/01/13/monday-memories-the-blade-building-downtown-toledo-1926/stories/20200108156']],
  conf='mixed',brick='?'),

N('second-national-bank-toledo','Second National Bank Building (Edge21 Apartments)','Toledo','oh','civic','standing',41.65089,-83.53425,'exact','view','walk','','1912–1913',
  'A 21-storey, 289-foot tower built in 1912 and 1913 for the Second National Bank on Summit Street at Madison Avenue, designed by D. H. Burnham and Company of Chicago. It was Toledo\'s tallest building until 1930, then the Toledo Trust Building until the bank moved across the street in 1981. It became apartments in 1999 (Riverfront Apartments) and was renamed Edge21 in 2023.',
  'The bank on the lower floors and offices above, now flats. Interior not checked.',
  '',
  'A private apartment building at 245 North Summit Street; seen from the street.'+DT,
  [W('Riverfront Apartments')],
  brick='?'),

N('ohio-building-toledo','Ohio Building','Toledo','oh','civic','standing',41.65188,-83.53532,'exact','view','walk','','1906',
  'A twelve-storey office tower built in 1906 by the Ohio Savings Bank and Trust Company at Madison Avenue and Superior Street, 178 feet tall. George S. Mills designed it and moved his own office into it; in 1910 it was called one of the finest structures in the state.',
  'A neoclassical office tower of the early skyscraper years. Interior not checked.',
  '',
  'Privately owned, at 420 Madison Avenue; seen from the street.'+DT,
  [W('Ohio Building (Toledo, Ohio)')],
  brick='?'),

N('lucas-county-courthouse-toledo','Lucas County Courthouse','Toledo','oh','civic','standing',41.65529,-83.53714,'exact','view','walk','','1897',
  'The county courthouse at 700 Adams Street, opened in 1897, designed by David L. Stine and built by Dun, Perley and Company. The courthouse and the county jail are on the National Register together since 1973.',
  'A domed courthouse with landmark plaques by the entrance. Interior and public hours not checked.',
  '',
  'Owned by Lucas County and still a working courthouse; seen from Adams Street and the surrounding streets.'+DT,
  [W('Lucas County Courthouse and Jail')],
  brick='?'),

N('valentine-theatre-toledo','Valentine Theatre','Toledo','oh','civic','standing',41.65328,-83.53375,'exact','open','walk','','1895',
  'A downtown theatre of 1895 at Superior and Adams streets, seating 901. A $28 million restoration by architect Charles H. Stark, begun in 1978, reopened it in 1999; a gas explosion in the basement in November 2007 closed it until April 2008. On the National Register since 1987.',
  'A working theatre: the inside is seen by going to a show. What original work survives inside was not checked.',
  '',
  'Run as a performing-arts theatre at 410 Adams Street; the theatre and box office open an hour before each show. The theatre\'s page names two Downtown Parking Authority garages on Superior Street within a block.',
  [W('Valentine Theatre'),['Valentine Theatre: Visit','https://valentinetheatre.com/visit']],
  brick='?',hours='Box office Monday to Friday 10 a.m. to 4 p.m.; the theatre opens an hour before each show'),

N('pythian-castle-toledo','Pythian Castle','Toledo','oh','civic','standing',41.65199,-83.54027,'exact','view','walk','','1890',
  'A Romanesque castle built in 1890 by the Knights of Pythias to designs by Bacon and Huber of Toledo, at Jefferson Avenue and Ontario Street, with shops on the ground floor; its turret rises 122 feet. The Knights sold it to Greyhound in 1951. A fire in 1978 ended its use and it decayed; the county land bank took it in 2013 and sold it in 2016 to a developer, who put on a new roof and new windows by 2022.',
  'The tall corner turret on Jefferson Avenue is the thing to see. Whether it is now occupied, and the inside, were not checked.',
  '',
  'Privately owned, at the corner of Jefferson Avenue and North Ontario Street; seen from the street.'+DT,
  [W('Pythian Castle (Toledo, Ohio)')],
  brick='?'),

N('trinity-episcopal-toledo','Trinity Episcopal Church','Toledo','oh','worship','standing',41.65298,-83.53305,'exact','open','walk','','1863',
  'A Gothic Revival Episcopal church of 1863 at 316 Adams Street, a parish of the Diocese of Ohio. In 1910 the Skinner Organ Company built it what was then the largest organ in Toledo. On the National Register since 1983.',
  'A Gothic church in the middle of downtown. Interior not checked.',
  '',
  'An active church; anyone may attend the Sunday service, which is when the building is open. Service time from the Episcopal Church\'s listing of its parishes.'+DT,
  [W('Trinity Episcopal Church (Toledo, Ohio)'),['Episcopal Asset Map: Trinity Episcopal Church','https://www.episcopalassetmap.org/node/4370']],
  brick='?',hours='Sunday service 10 a.m.'),

N('st-patrick-church-toledo','Historic Church of St. Patrick','Toledo','oh','worship','standing',41.64900,-83.54601,'exact','open','walk','','1901',
  'A Gothic Revival Catholic church of Amherst blue sandstone, dedicated on April 13, 1901, replacing a church of 1863 that was found unsafe and pulled down in 1891. Lightning set the steeple on fire on September 9, 1980; a parishioner\'s bequest paid to rebuild it, finished in 2007. On the National Register since 1972.',
  'Inside, ten red granite columns, and chandeliers and art work from a renovation in the 1920s; the organ keeps 17 ranks of pipes from an earlier Kilgen organ.',
  '',
  'An active parish at 130 Avondale Avenue; Mass times from the parish bulletin of July 2026.'+DT,
  [W("St. Patrick's Catholic Church (Toledo, Ohio)"),['Historic St. Patrick: parish bulletin, July 19, 2026','https://stpatshistoric.org/bulletins/20260719.pdf']],
  brick='no',hours='Mass Sunday 8 and 10 a.m., Wednesday 5:30 p.m.'),

N('toledo-state-hospital-old-cemetery','Toledo State Hospital Old Cemetery','Toledo','oh','burial','standing',41.62341,-83.60195,'site','view','walk','','1888–1922',
  'The first burial ground of the Toledo State Hospital, which opened in January 1888 as the Toledo Asylum for the Insane, a self-contained community of cottages, wards, a church and a bakery just south of here. Over 900 patients were buried here, the most (53) in 1918, under small numbered concrete markers; when it filled in 1922 a new cemetery opened half a mile to the southwest. Most of the hospital was later razed and its land passed to what became the University of Toledo\'s Health Science Campus.',
  'An Ohio Historical Marker stands by Arlington Avenue just west of the entrance to Bowsher High School. Volunteers have been raising the sunken numbered markers since 2005. The rest of the old hospital is gone.',
  '',
  'On land of the University of Toledo. The marker is by the road; whether visitors may walk into the cemetery itself was not checked. OpenStreetMap maps a small lot on the Arlington Avenue side path about 150 m northeast; who it belongs to was not checked.',
  [['Remarkable Ohio: marker 56-48, the Toledo State Hospital Old Cemetery','https://remarkableohio.org/marker/56-48-the-toledo-state-hospital-old-cemetery-1888-1922/'],['UToledo News: cemeteries restored, 2011','https://news.utoledo.edu/?p=12609']],
  brick='?'),

]

PIN_NOTES={
 'nasby-building-toledo':'ArcGIS address point for 605 Madison Avenue, close to the Wikipedia coordinate; looked at on the aerial.',
 'secor-hotel-toledo':'ArcGIS address point for 425 Jefferson Avenue; looked at on the aerial.',
 'rosary-cathedral-toledo':'The ArcGIS address point for 2535 Collingwood Boulevard fell on a smaller building south of the cathedral; moved onto the long cathedral roof seen on the aerial, which is where the Wikipedia coordinate also falls.',
 'jefferson-center-toledo':'ArcGIS address point for 1300 Jefferson Avenue; looked at on the aerial.',
 'ymca-building-toledo':'ArcGIS address point for 1100 Jefferson Avenue, beside the Register point; looked at on the aerial.',
 'blade-building-toledo':'The ArcGIS address point for 541 North Superior Street fell at the street corner; moved to the Toledo Blade Building as OpenStreetMap maps it, and looked at on the aerial.',
 'second-national-bank-toledo':'ArcGIS address point for 245 North Summit Street, matching the Wikipedia coordinate; looked at on the aerial.',
 'ohio-building-toledo':'ArcGIS address point for 420 Madison Avenue, matching the Wikipedia coordinate; looked at on the aerial.',
 'lucas-county-courthouse-toledo':'ArcGIS address point for 700 Adams Street, matching the Register point; looked at on the aerial.',
 'valentine-theatre-toledo':'ArcGIS address point for 410 Adams Street; looked at on the aerial.',
 'pythian-castle-toledo':'ArcGIS address point for 801 Jefferson Avenue at Ontario Street, matching the Register point; looked at on the aerial.',
 'trinity-episcopal-toledo':'The ArcGIS address point for 316 Adams Street fell beside the church; moved to Trinity Episcopal Church as OpenStreetMap maps it, and looked at on the aerial.',
 'st-patrick-church-toledo':'ArcGIS address point for 130 Avondale Avenue, matching the Register point; looked at on the aerial.',
 'toledo-state-hospital-old-cemetery':'The marker position the Ohio History Connection gives; the pin marks the marker, by the cemetery.',
}
