# November 22, 2026: Springfield, Massachusetts. A "videos" session (PROMPTS.md job 9): the names came from one video's
# tour of old Springfield buildings (the record is source/videos/20231217_bmx9lrgqaFQ.md); the video is a tip and nothing
# here rests on it. Sources read: Wikipedia (each article named in the links); Lost New England (Trinity Methodist, the
# Union Stations, the Smith & Wesson factory, the old post office, the Hall of Records, the old high school); Historic
# Buildings of Massachusetts (Classical High School); Sacred Spaces of New England (Trinity United Methodist); and the
# pages of whoever runs each place for its hours: the City of Springfield, the Springfield Museums, the Springfield City
# Library, Springfield Union Station, South Congregational Church and Trinity United Methodist Church.
# Pins are OpenStreetMap points or Wikipedia points, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'springfield_mcmc','label':'Massachusetts: old Springfield, from Court Square to the Quadrangle','added':'2026-11-22 18:36'}

DT=' Downtown street meters and public garages are close by; their hours and fees were not checked.'
QUAD='The Springfield Museums share one ticket and one set of hours for their five museums on the Quadrangle, entered from 21 Edwards Street; the Museum Parking lot is off Edwards and Mattoon streets.'
MUSL=['Springfield Museums: hours and admission','https://springfieldmuseums.org/hours-and-admission/']
LNE_US=['Lost New England: Union Station (2)','https://lostnewengland.com/2020/01/union-station-springfield-mass-2/']

PLACES=[
N('springfield-municipal-group','Springfield Municipal Group (City Hall, Symphony Hall and the Campanile)','Springfield','pv','civic','standing',42.10111,-72.59012,'site','open','walk','','1911–1913',
  'Three city buildings on Court Street facing Court Square: City Hall, Symphony Hall (built as the Municipal Auditorium) and, between them, a clock tower about 300 feet high called the Campanile. They were built from 1911 to 1913 in the City Beautiful manner, after Springfield\'s first city hall burned in 1905. The Campanile was the tallest structure in the city until 1973; its bells fell silent and the tower was closed for years for want of repair, and money for restoring the group was set aside in 2006.',
  'Two matching temple-fronted halls with columns, and the tall Italianate tower in the middle with a clock face fourteen feet across and a carillon of twelve bells. Symphony Hall, at the south end, seats about 2,600 and is known for its sound; it was rededicated in 1980 and renovated in 2004. Inside City Hall not checked.',
  'The tower that answers the old city hall fire of 1905.',
  'Owned by the City of Springfield. City Hall is at 36 Court Street; its weekday hours are from the city\'s own page. Symphony Hall opens for concerts and shows on their own dates. Court Square in front is an open city square.'+DT,
  [W('Springfield Municipal Group'),['City of Springfield: City Hall hours','https://www.springfield-ma.gov/cos/']],
  brick='no',hours='City Hall Monday to Friday 8:30 a.m. to 4 p.m., Thursday until 6 p.m.; Symphony Hall for shows'),

N('hampden-county-courthouse-springfield','Hampden County Courthouse (H. H. Richardson)','Springfield','pv','civic','standing',42.10027,-72.58861,'exact','view','walk','','1871–1874',
  'A courthouse designed by Henry Hobson Richardson and dedicated on April 28, 1874, to replace one of 1822, after a grand jury had indicted the county commissioners in 1869 for keeping the deeds and records in a building that was not fireproof. It is built of light grey Monson granite in rough-faced blocks, shaped roughly like a capital I, with a bell tower between two tall dormers. Richardson\'s successor firm, Shepley, Rutan and Coolidge, later remodelled it and took off the steep roof and high dormers.',
  'Rough grey granite walls with smooth trim, tall windows and the square tower, at the head of the walkway from Court Square to the Old First Church. It now houses the juvenile court and the western division of the Massachusetts Housing Court. Interior not checked.',
  '',
  'A working state court building on Elm Street, in the Court Square Historic District; seen from the street and from Court Square. Court visitors go through security; it is not a place to tour.'+DT,
  [W('Hampden County Courthouse')],
  brick='no',hours=''),

N('south-congregational-church-springfield','South Congregational Church','Springfield','pv','worship','standing',42.10259,-72.58314,'site','open','walk','','1875',
  'A High Victorian Gothic church at 45 Maple Street, built in 1875 to designs by William Appleton Potter for a congregation formed in 1842, which still worships here. Among those who paid for it were Daniel B. Wesson of Smith & Wesson and Charles and George Merriam of Merriam-Webster. It is listed on the National Register.',
  'Limestone from Longmeadow on a Monson granite base, 136 feet long, with a round apse facing Maple Street under a conical slate roof banded in red, nine Gothic windows in alternating light and dark stone, and a tower 120 feet high trimmed with yellow Ohio sandstone. Inside, the pews in the transepts were laid out to see the pulpit like an amphitheatre, with carvings drawn from nature in the tower entrance.',
  '',
  'An active United Church of Christ congregation; anyone may come to the Sunday service, whose time is from the church\'s own page.'+DT,
  [W('South Congregational Church (Springfield, Massachusetts)'),['South Congregational Church: questions','https://sococh.org/faq/']],
  brick='no',hours='Sunday service 10 a.m.'),

N('trinity-united-methodist-springfield','Trinity United Methodist Church','Springfield','pv','worship','standing',42.08478,-72.56251,'exact','open','drive','','1929',
  'A Gothic Revival church at 361 Sumner Avenue in Forest Park, finished in 1929 to designs by the Boston firm Allen and Collens. The congregation of Trinity Methodist began downtown in 1844; its 1869 church on Bridge Street, with a steeple 185 feet high, was left in the early 1920s when the congregation moved here, and pulled down in 1922.',
  'The church takes pride in its stained glass by Wilbur Herbert Burnham of Boston, above all the rose window at the back of the nave, on the theme of Psalm 150. The old downtown church is gone: the Trinity Block on Bridge Street stands on its site.',
  '',
  'An active church; its Sunday service is open to all, in person and streamed. Street parking on Sumner Avenue was not checked; Forest Park, a city park, lies across the road.',
  [['Sacred Spaces of New England: Trinity United Methodist','https://seththompson.info/sacredspacesne/tag/methodist'],['Trinity United Methodist Church: I\'m new','https://www.trinityspringfield.org/about/Im-new'],['Lost New England: Trinity Methodist Church','https://lostnewengland.com/2019/10/trinity-methodist-church-springfield-mass/']],
  brick='?',hours='Sunday worship 10:30 a.m.'),

N('springfield-union-station-ma','Springfield Union Station','Springfield','pv','rail','standing',42.10654,-72.59376,'exact','open','walk','','1926',
  'The third union station on this spot, opened on December 18, 1926. The first station of 1839 was a wooden Egyptian Revival building that burned in 1851; its brick and iron successor was pulled down in 1889 for a Romanesque station of two buildings either side of the tracks, from plans begun by H. H. Richardson, which was torn down from 1925. The 1926 station fell out of use and was restored at a cost of $94 million, reopening in June 2017 as a rail and bus station; Amtrak moved back into it in 2019.',
  'The restored 1926 station building with its main concourse, and the tunnel under the tracks that leads to the platforms. Amtrak, the Hartford Line commuter trains, PVTA buses, Peter Pan and Greyhound all use it.',
  'Three stations in a century on one site, the middle one condemned as dingy and dangerous within twenty years.',
  'The station building is open daily, and the hours are from the station\'s own page. Parking lots on Frank B. Murray Street.',
  [W('Springfield Union Station (Massachusetts)'),['Springfield Union Station: questions','https://springfieldunionstation.com/about/faqs'],LNE_US],
  brick='?',hours='Daily 4 a.m. to 12:30 a.m.',th=[42.10752,-72.59263],thn='Parking on Frank B. Murray Street'),

N('springfield-central-library-ma','Springfield City Library, Central Library','Springfield','pv','civic','standing',42.10342,-72.58481,'exact','open','walk','','1910–1912',
  'The city\'s main library at 220 State Street, at the corner of the Quadrangle. Andrew Carnegie gave $260,000 in 1905 toward it and three branches, and residents gave $155,000 more; Edward Lippincott Tilton designed it in the Renaissance Revival style, building began in April 1910 and it opened on January 10, 1912. The Gothic library of 1871 that stood here was rolled 200 feet aside to make room.',
  'A Renaissance Revival front on State Street beside Merrick Park, where Augustus Saint-Gaudens\'s statue The Puritan stands. Adult books are in Rice Hall, named for William Rice, who ran the library for 36 years. Anyone may go in during opening hours.',
  '',
  'Run by the Springfield City Library; the hours are from its own page and Sunday opening runs only from Labor Day to Memorial Day.'+DT,
  [W('Springfield City Library (Massachusetts)'),['Springfield City Library: Central Library','https://www.springfieldlibrary.org/library/central/']],
  brick='no',hours='Monday and Wednesday noon to 8 p.m.; Tuesday, Thursday and Saturday 9 a.m. to 5 p.m.; Friday closed; Sunday noon to 5 p.m., Labor Day to Memorial Day'),

N('springfield-science-museum','Springfield Science Museum','Springfield','pv','civic','standing',42.10439,-72.58567,'exact','open','walk','','1899',
  'A museum founded in 1859 as a natural history and curiosities collection in City Hall, which moved to the library in 1871 and to the art museum in the early 1890s, and opened in its own building on the Quadrangle on October 16, 1899. The building was enlarged in 1934 and 1970. It holds the Seymour Planetarium, the oldest working projection planetarium in the country.',
  'Exhibit halls of the 1930s still in use: the Native American Hall with its diorama and Habitat Hall with mounted animals. Open to visitors with a museum ticket.',
  '',
  QUAD,
  [W('Springfield Science Museum'),MUSL],
  brick='no',hours='Tuesday to Saturday 10 a.m. to 5 p.m., Sunday 11 a.m. to 5 p.m.; Monday closed',th=[42.10506,-72.58682],thn='Museum Parking, Mattoon Street'),

N('george-walter-vincent-smith-art-museum','George Walter Vincent Smith Art Museum','Springfield','pv','civic','standing',42.10385,-72.58508,'exact','open','walk','','1895',
  'The oldest of the museums on the Quadrangle, opened in 1895 to hold the collection of George Walter Vincent Smith, a retired carriage maker, and his wife Belle Townsley Smith. The Italian palazzo-style building was designed by Renwick, Aspinwall and Renwick of New York with Springfield architect Walter Tallant Owen. The Smiths\' ashes are kept on its second floor. It was closed for restoration in 2026 and has since reopened.',
  'When it opened it had Tiffany windows, fireproof walls and fourteen skylights. The galleries hold the Smiths\' Japanese and Chinese armour, swords, cloisonné, bronzes and jade, carpets and lace. Open to visitors with a museum ticket.',
  '',
  QUAD,
  [W('George Walter Vincent Smith Art Museum'),MUSL],
  brick='?',hours='Tuesday to Saturday 10 a.m. to 5 p.m., Sunday 11 a.m. to 5 p.m.; Monday closed',th=[42.10506,-72.58682],thn='Museum Parking, Mattoon Street'),

N('hotel-kimball-springfield','Hotel Kimball (Kimball Towers)','Springfield','pv','hotel','standing',42.10507,-72.58928,'exact','view','walk','','1910',
  'A Renaissance Revival hotel at 140 Chestnut Street, designed by Albert Winslow Cobb in 1910 and later run as the Sheraton-Kimball. Westinghouse\'s WBZ, the first commercial radio station in the United States, began here, and presidents and film stars stayed. It is now the Kimball Towers condominiums, in the Apremont Triangle Historic District, listed on the National Register in 1983.',
  'The tall hotel block and its entrance on Chestnut Street between Bridge and Hillman streets. Private homes inside.',
  'Where American commercial radio began.',
  'Private condominiums; look from Chestnut Street.'+DT,
  [W('Hotel Kimball')],
  brick='?',hours=''),

N('paramount-theater-springfield-ma','Paramount Theater (Julia Sanderson Theater, the Hippodrome)','Springfield','pv','civic','standing',42.10433,-72.59513,'exact','view','walk','','1926',
  'A picture palace at 1676 to 1708 Main Street, built in 1926 for over $1 million out of part of the old Massasoit House hotel, and the most ornate in western Massachusetts. It changed names several times, once honouring the Springfield actress Julia Sanderson, and showed films until the 1960s, then became a disco and concert hall, the Hippodrome. A renovation began around 2011; the New England Farm Workers Council put it up for sale in 2024, and the buyer at the auction said he would start work in March 2026. Whether that work has begun was not checked.',
  'The theatre front and the Massasoit House block on Main Street, across from Union Station. Closed; interior not checked.',
  'The grandest movie palace in western Massachusetts, waiting for its second act.',
  'Privately owned and closed; look from Main Street.'+DT,
  [W('Paramount Theater (Springfield, Massachusetts)')],
  brick='no',hours=''),

N('classical-high-school-springfield','Classical High School (Central High School)','Springfield','pv','civic','standing',42.10345,-72.58293,'exact','view','walk','','1897–1898',
  'Built in 1897 and 1898 as Springfield\'s Central High School, on State Street where the county jail had stood, to designs by Hartwell, Richardson and Driver of Boston. A wing for junior high pupils was added on the west end in 1922 and 1923, after the older high school of 1874 beside it was pulled down. It was renamed Classical High School in 1934, closed in 1986 and turned into condominiums.',
  'The long school front on State Street, now the Classical Condominiums. Private homes inside.',
  '',
  'Private condominiums at 235 State Street; look from the street.'+DT,
  [['Historic Buildings of Massachusetts: Classical High School','https://mass.historicbuildingsct.com/?p=143'],['Lost New England: Springfield High School','https://lostnewengland.com/2013/12/springfield-high-school-springfield/']],
  brick='no',hours=''),

N('big-e-coliseum-west-springfield','Eastern States Coliseum (Big E Coliseum)','West Springfield','pv','amuse','standing',42.09139,-72.61868,'exact','view','walk','','1916',
  'An arena built in 1916 for the Eastern States Exposition, the fair for the six New England states first held in West Springfield that October. It was the Springfield area\'s main indoor hall until 1972, home ice of the Springfield Indians hockey team, and from 1926 held hockey games; the ice plant was taken out in 1991. It still seats about 5,900 and is used during the fair each September and for circuses, horse shows and rodeos.',
  'The arena on the fairgrounds on Memorial Avenue. Interior not checked.',
  '',
  'On the private Eastern States Exposition grounds, 1305 Memorial Avenue; seen from the road, and open to ticket holders during the Big E (seventeen days from the second Friday after Labor Day) and other events. Large fairground lots surround it.',
  [W('Big E Coliseum'),W('Eastern States Exposition')],
  brick='yes',hours=''),
]

PIN_NOTES={
 'springfield-municipal-group':'Wikipedia point for the group, in front of the Campanile on Court Street.',
 'hampden-county-courthouse-springfield':'OpenStreetMap point for the historic courthouse building.',
 'south-congregational-church-springfield':'OpenStreetMap point for the church; on the aerial the buildings at the bend of Maple Street could not be told apart for certain, so the pin marks the site.',
 'trinity-united-methodist-springfield':'OpenStreetMap point for the church on Sumner Avenue.',
 'springfield-union-station-ma':'OpenStreetMap outline of the station building, north of the tracks; the first point tried fell on the platforms.',
 'springfield-central-library-ma':'OpenStreetMap point for the library at 220 State Street.',
 'springfield-science-museum':'OpenStreetMap point for the museum on the Quadrangle.',
 'george-walter-vincent-smith-art-museum':'OpenStreetMap point for the museum on the Quadrangle.',
 'hotel-kimball-springfield':'OpenStreetMap outline of Kimball Towers.',
 'paramount-theater-springfield-ma':'OpenStreetMap point for the theatre on Main Street.',
 'classical-high-school-springfield':'OpenStreetMap outline of the Classical Condominiums at 235 State Street.',
 'big-e-coliseum-west-springfield':'OpenStreetMap point for the arena.',
}
