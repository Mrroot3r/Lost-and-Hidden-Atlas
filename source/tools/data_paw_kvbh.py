# November 23, 2026: Erie, Pennsylvania (region paw). The first places in the city of Erie: downtown round Perry Square
# and West Sixth Street, the cathedral and the older parish churches, three schools and colleges, and the city cemetery.
# The names came from a video walk-through of the city's old buildings, taken as a tip only; every fact here comes
# from the linked sources. SAH Archipedia (Buildings of Pennsylvania) pages, the Diocese of Erie's parish pages, the
# churches', museum's and cemetery association's own pages and the Erie Polonia history site were read with
# tools/page.py; Wikipedia articles as raw text with tools/wiki_raw.py. Where sources disagree the text gives both;
# where a source is silent it says "not checked".
# Pins: ArcGIS PointAddress matches for each street address, looked at on the pin check (state leaf-off aerial).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
SAH_CH=L('SAH Archipedia: Erie County Courthouse','https://sah-archipedia.org/buildings/PA-01-ER1')
SAH_GAN=L('SAH Archipedia: Gannon University (Scott-Strong house; Villa Maria)','https://sah-archipedia.org/buildings/PA-01-ER2')
SAH_CLUB=L('SAH Archipedia: Erie Club (Charles Manning Reed House)','https://sah-archipedia.org/buildings/PA-01-ER3')
SAH_EAM=L('SAH Archipedia: Erie Art Museum (Old Custom House) and Cashier\'s House','https://sah-archipedia.org/buildings/PA-01-ER5')
SAH_PAT=L('SAH Archipedia: St. Patrick\'s Roman Catholic Church','https://sah-archipedia.org/buildings/PA-01-ER12')
SAH_LIB=L('SAH Archipedia: U.S. Courthouse (Erie Public Library)','https://sah-archipedia.org/buildings/PA-01-ER16')
SAH_REN=L('SAH Archipedia: Renaissance Centre (Erie Trust Company Building)','https://sah-archipedia.org/buildings/PA-01-ER19')
SAH_PET=L('SAH Archipedia: St. Peter Roman Catholic Cathedral','https://sah-archipedia.org/buildings/PA-01-ER23')
SAH_SV=L('SAH Archipedia: Strong Vincent High School','https://sah-archipedia.org/buildings/PA-01-ER27')
SAH_MERC=L('SAH Archipedia: Mercyhurst College Main Campus','https://sah-archipedia.org/buildings/PA-01-ER32')
DIO_PAT=L('Diocese of Erie: St. Patrick Parish (Mass times)','https://eriercd.org/Parish10219-St-Patrick.html')
DIO_PET=L('Diocese of Erie: St. Peter Cathedral (Mass times)','https://eriercd.org/Parish10317-St-Peter-Cathedral.html')
STAN=L('St. Stanislaus Parish (Mass times)','https://www.ststanserie.org')
STAN_HIST=L('Erie Polonia History: History of St. Stanislaus Church','https://www.eriepoloniahistory.com/st-stanislaus-history.html')
EAM=L('Erie Art Museum: hours, admission and parking','https://www.erieartmuseum.org/visit')
CEM=L('Erie Cemetery Association: Erie Cemetery','https://www.eriecemeteryassoc.com/eriecemetery')
CEM_C=L('Erie Cemetery Association: contact and grounds hours','https://www.eriecemeteryassoc.com/contact-6')
FPC=L('First Presbyterian Church of the Covenant: history','https://firstcovenanterie.org/about-us/history')
FPC_I=L('First Presbyterian Church of the Covenant: visiting and worship times','https://www.firstcovenanterie.org/about-us/general-information')
PLACES=[
N('erie-club-reed-mansion','Erie Club (Charles Manning Reed Mansion)','Erie','paw','landmark','standing',42.12922,-80.08699,'exact','view','walk','','1846–1849',
  'A Greek Revival mansion built for Charles Manning Reed, who made his fortune in Great Lakes shipping, to a design by the Buffalo architect Edward Smith; SAH Archipedia dates it 1846–48, Wikipedia 1846–49. Bays were added about 1855 and 1865. The Erie Club, a private club, bought it in 1904 and has owned it since, so the house has had only two owners. It was listed on the National Register in 1982.',
  'A seven-bay front behind four two-story fluted Ionic columns carrying a pediment, in soft orange brick with cream limestone window trim. North of it a long, narrow one-story wing repeats the portico in small with Tuscan columns; it holds the club\'s offices and a bowling alley. Inside, much of the carved woodwork by the head ship\'s carpenter of Reed\'s shipping line was kept when the club fitted it out in 1905, but the club is private.',
  'The house a historian called the high point of Greek Revival in Pennsylvania.',
  '524 Peach Street at West Sixth Street, beside the courthouse. A private club: look from the street. Parking not checked; downtown has metered street parking.',
  [SAH_CLUB,W('Charles Manning Reed Mansion')],brick='?'),
N('erie-county-courthouse-pa','Erie County Courthouse','Erie','paw','civic','standing',42.12922,-80.08807,'site','view','walk','','1853–1855',
  'The county courthouse on West Sixth Street. Its west wing of 1853–55 is credited to Thomas U. Walter, who was paid for a design that has never been found, so whether it was followed is not known; its bell tower came down in 1894. An addition of 1889 made it an L, and Walter Monahan\'s matching east wing of 1929–30 was built seventy-three years after the first. A glass lobby of 2005 joins the two wings.',
  'Two matching temple-fronted wings with a dozen Corinthian columns under their pediments, either side of a courtyard, and the glass entrance lobby between them. The old west wing keeps one large courtroom across the whole second floor, with furnishings from about 1870 to 1900. Whether visitors may look in was not checked.',
  '',
  '140 West Sixth Street, a working county courthouse. Look from the street; opening hours and security not checked. Parking not checked.',
  [SAH_CH],brick='?'),
N('scott-strong-house-gannon','Scott-Strong house (Gannon University)','Erie','paw','landmark','standing',42.12854,-80.08679,'exact','view','walk','','1896',
  'A 46-room mansion that William L. Scott commissioned from the Buffalo firm Green and Wicks and gave to his daughter Anna Scott Strong, wife of Charles H. Strong; she led Erie society from the 1890s until she died in 1928. The college that became Gannon University began in this one house and grew to about thirty buildings across twelve blocks.',
  'A soaring hipped roof broken by gables and dormers over a stone first story with a triple-arched entrance; SAH Archipedia says it is closer to the Chateauesque than to the Romanesque it is often called. It is a university building; whether the interior can be seen was not checked.',
  'A father\'s gift of a chateau that grew into a university.',
  '109 West Sixth Street, on the Gannon University campus. Look from the street. Parking not checked.',
  [SAH_GAN,W('Gannon University')],brick='?'),
N('old-customshouse-erie','Old Custom House (Erie Art Museum)','Erie','paw','civic','standing',42.13122,-80.08595,'exact','open','walk','','1838–1839',
  'A Greek Revival temple front by William Kelly, modelled on the Theseion in Athens, built in 1838–39 for a bank. It held Erie\'s post office until 1867 and the custom house for the port from 1849 to 1888, then a Grand Army of the Republic post and the county historical society. It is now part of the Erie Art Museum\'s five-building complex. Next door the bank\'s Cashier\'s House, also Greek Revival, is a house museum of the Erie County Historical Society.',
  'A building raised on a podium with a marble stair, six Doric columns and a pediment of white Vermont marble; the walls are brick and marble. Next door the Cashier\'s House is brick stuccoed to look like stone, with Egyptian Revival ornament in its main rooms.',
  'A bank built as a Greek temple, now the art museum.',
  'Erie Art Museum, entrance at 20 East Fifth Street between State and French streets. Adults $10, seniors and students $8, 16 and under free (museum page, read November 2026). Metered street parking on State Street and round Perry Square. The Cashier\'s House\'s own hours were not checked.',
  [EAM,SAH_EAM,W('Old Customshouse (Erie, Pennsylvania)')],brick='?',hours='Wednesday to Friday 11 a.m. to 6 p.m., Saturday 10 a.m. to 5 p.m., Sunday 1 to 6 p.m. Closed Monday, Tuesday and some holidays'),
N('erie-public-library-1899','Old Erie Public Library (U.S. Courthouse)','Erie','paw','civic','standing',42.12879,-80.08522,'site','view','walk','','1897–1899',
  'The city\'s public library of 1897–99 by Alden and Harlow of Pittsburgh, on Perry Square; it also held an art gallery and a ladies\' assembly hall, and several of its features were used again at the Carnegie Institute in Pittsburgh. In 2003–04 it was joined by a glass atrium to the 1938 Federal Building next door and to a 1947 department store, and the three serve as the federal courthouse.',
  'A Renaissance Revival block with a roof balustrade, a cornice with lions\' heads, Corinthian brick pilasters, terra-cotta trim and a Palladian window over the old entrance; a marble portico that a former owner took down was put back. Sources differ on the brick: SAH Archipedia calls it golden-orange Pompeian brick, Wikipedia both Pompeian red and light-brown. Inside are a restored rotunda and murals by Elmer Garnsey; whether the public may see them was not checked.',
  '',
  'South Park Row at Perry Square, part of the U.S. Courthouse. Look from the square; entry to a federal courthouse goes through security and was not checked. Metered parking round Perry Square.',
  [SAH_LIB,W('Main Library (Erie, Pennsylvania)')],brick='?'),
N('st-peter-cathedral-erie','St. Peter Cathedral','Erie','paw','worship','standing',42.12401,-80.08761,'exact','open','walk','','1873–1893',
  'The cathedral of the Diocese of Erie, designed by Patrick Charles Keely of Brooklyn. Bishop Tobias Mullen commissioned it in 1873 and laid the cornerstone in 1875, but would not borrow, so it took twenty years and was called "Mullen\'s Folly"; it was dedicated on 1 August 1893. Much of the foundation stone came from the locks of the Erie Extension Canal, which closed in 1871.',
  'Three towers with doors at their feet; the central one, 265 feet with a clock on each side, is the tallest structure in Erie. The walls are rough red Medina sandstone with white sandstone trim. Inside: marble and wood, clustered columns, stained glass by the Franz Mayer firm of Munich in the sanctuary and transepts, a crypt of 1902 under the high altar where bishops are buried, and a Casavant organ of 1977.',
  'Twenty years to build, from the stones of a dead canal.',
  '230 West Tenth Street. The church is open for Mass; times from the Diocese of Erie\'s parish page, read November 2026. Parking not checked.',
  [SAH_PET,DIO_PET,W('St. Peter Cathedral (Erie, Pennsylvania)')],brick='no',hours='Mass Monday to Friday 6:30 and 8 a.m., 12:10 and 5:15 p.m.; Saturday 8 a.m. and 4 p.m.; Sunday 6:30, 8:30 and 11 a.m.'),
N('st-patrick-church-erie','St. Patrick Church','Erie','paw','worship','standing',42.13282,-80.08375,'exact','open','walk','','1906',
  'The parish was founded in 1837, and was the diocese\'s pro-cathedral before St. Peter\'s was built. Its pastor Peter Cauley had the present stone church designed in 1906 by William Ginther of Akron to hold fourteen life-size Stations of the Cross carved by the Mayer studio of Munich, which he had seen at the 1893 Chicago fair, for an Irish congregation that worked on the canal and docks. Four Cauley brothers served the parish together from a 47-room rectory of 1913–14.',
  'A Romanesque front with a triple-arched entrance between two square towers of very different heights, and three round apses behind. The ground floor has no windows, to make room for the fourteen sculpture niches, each with murals by Italian painters; German stained glass in the clerestory lights a church that seats eight hundred.',
  'A church built around its fourteen life-size carved Stations of the Cross.',
  '130 East Fourth Street. Open for Mass; times from the Diocese of Erie\'s parish page, read November 2026. Parking not checked.',
  [SAH_PAT,DIO_PAT,L('Wikipedia: St. Peter Cathedral (St. Patrick\'s as pro-cathedral)','https://en.wikipedia.org/wiki/St._Peter_Cathedral_(Erie,_Pennsylvania)')],brick='no',hours='Mass Saturday 5 p.m., Sunday 8 and 10:30 a.m.; holy days noon'),
N('st-stanislaus-church-erie','St. Stanislaus Church','Erie','paw','worship','standing',42.12723,-80.06958,'exact','open','walk','','1895–1898',
  'The first Polish parish in Erie, founded in the 1880s by families who had worshipped at the German St. Mary\'s; the first, wooden church was blessed in 1885. The cornerstone of the present church was blessed in September 1895, the first services held in April 1897, and it was dedicated in September 1898. A fire in the sacristy in January 1900 gutted the interior, which was rebuilt; the two towers were begun the same year. The interior was renovated and the church rededicated in 2000.',
  'A Romanesque church 66 feet wide in the nave and 147 feet long, with two towers that were planned as 135-foot steeples. The brick rectory beside it dates from 1895. The interior was redone in 1999–2000; original fabric not checked.',
  '',
  '516 East Thirteenth Street. The parish asks anyone coming to a weekday Mass to call the office the day before so the church can be opened. Times from the parish\'s own page, read November 2026. Parking not checked.',
  [STAN_HIST,STAN],brick='?',hours='Mass Saturday 4 p.m., Sunday 9 a.m.; Monday to Friday 8 a.m. (call the day before)'),
N('renaissance-centre-erie','Erie Trust Company Building (Renaissance Centre)','Erie','paw','civic','standing',42.12540,-80.08175,'exact','view','walk','','1925–1928',
  'A fourteen-story bank and office tower designed in 1925 by Frederick Hirons and Ethan Allen Dennison of New York for the Erie Trust Company, then the richest bank in town, and finished in 1928. The bank failed after the Depression began and the state took the building; G. Daniel Baldwin bought it in 1943 and gave it his name. Restored from 1996 as the Renaissance Centre, offices and shops, it was listed on the National Register in 2000. At 198 feet it is Erie\'s tallest office building.',
  'Tan brick above a limestone base of three stories, with tall arched openings and concentric limestone arches over the State Street door whose capitals are small carved grotesques. Inside, the original marble, walnut doorways and bronze elevator doors remain, and five of seven murals of the region\'s history by Edward Trumbull; SAH Archipedia says they were restored, Wikipedia that they were hidden by renovations.',
  '',
  '1001 State Street at East Tenth Street. An office and retail building; look from the street. Whether the lobby and murals can be seen was not checked. Parking not checked.',
  [SAH_REN,W('Renaissance Centre (Erie, Pennsylvania)')],conf='mixed',brick='no'),
N('strong-vincent-school-erie','Strong Vincent High School','Erie','paw','civic','standing',42.11740,-80.11339,'exact','view','walk','','1929–1930',
  'A public school of 1929–30 by Meyers and Johnson, named for General Strong Vincent, who led Erie\'s regiment in the Civil War and was killed holding Little Round Top at Gettysburg in 1863. The school district made it a middle school in 2017.',
  'A classical front with six Tuscan columns under a pediment and a clock guarded by carved griffins; plaques on the walls carry carved mottoes, among them the Vincent family\'s coat of arms with "By courage, not by force of arms, we conquer" and "Labor is man\'s greatest function." A working school: look from the street.',
  'Griffins and carved mottoes on a 1930 school.',
  '1330 West Eighth Street. A working school: look from the street and do not go onto the grounds during the school day. Parking not checked.',
  [SAH_SV,L('Wikipedia: Erie High School (Strong Vincent made a middle school in 2017)','https://en.wikipedia.org/wiki/Erie_High_School_(Pennsylvania)')],brick='?'),
N('villa-maria-academy-erie','Villa Maria Academy (1892)','Erie','paw','civic','standing',42.12056,-80.10154,'exact','view','walk','','1892–1927',
  'The motherhouse and academy of the Sisters of St. Joseph, built in 1892 to a design by David K. Dean and Sons, with an addition of 1904 by Sidney F. Heckert and Gannon Hall, a gymnasium, kitchen and chapel by Fuller and Stickle, in 1927. Gannon University absorbed Villa Maria College between 1989 and 1993; the buildings went back to the sisters in 1993 and now hold about seventy low-income apartments. Listed on the National Register in 1996; the chapel was put on Preservation Pennsylvania\'s at-risk list in 2011.',
  'A red brick High Victorian Gothic building with terra-cotta trim, dormers and two conical turrets; the 1904 Gothic wing with parapets; and Gannon Hall, joined by a two-story bridge, with stepped gables, buttresses, a conical tower and the stained glass of the chapel. Apartments: look from the street.',
  '',
  '819 West Eighth Street (Villa Maria Apartments). Private homes: look from the street. Parking not checked.',
  [SAH_GAN,W('Villa Maria Academy (1892)')],brick='yes'),
N('mercyhurst-old-main-erie','Mercyhurst Old Main','Erie','paw','inst','standing',42.10340,-80.05600,'area','view','walk','','1925–1926',
  'The first building of Mercyhurst, founded by the Sisters of Mercy under Mother Borgia Egan as a women\'s college in 1926 (men were admitted from 1969). Old Main was designed in 1925–26 by the Philadelphia architect Francis Ferdinand Durang. The twenty-foot iron gates at the entrance were made for Harry K. Thaw, who murdered Stanford White in 1906; the college bought them for $600 when his Pittsburgh estate was sold in 1950.',
  'A Collegiate Gothic building in golden brick with limestone trim, a massive square four-story entrance pavilion and a slate roof with long dormers, joined by a cloister to Weber Hall of 1953. The Thaw gates stand at the campus entrance. Whether visitors may walk the campus was not checked.',
  'A murderer\'s gates in front of a convent college.',
  'Mercyhurst University, 501 East 38th Street. Campus visiting rules and parking not checked.',
  [SAH_MERC,W('Mercyhurst University')],brick='no'),
N('erie-cemetery-pa','Erie Cemetery','Erie','paw','burial','standing',42.11225,-80.08471,'site','public','walk','','1850–',
  'A rural cemetery of 75 acres between Chestnut and Cherry streets and 19th and 26th streets. Citizens petitioned for it in 1846, it was incorporated in 1850 and opened on 20 May 1851. An iron gateway went up in 1867 and a porters\' lodge was built by the main entrance before 1885. The Erie Cemetery Association runs it with two other cemeteries.',
  'Iron fencing, the 1867 iron gateway and walks; a porters\' lodge stood by the main entrance by 1885, and whether it survives was not checked. Which monuments are of note was not checked.',
  '',
  'Erie Cemetery Association, 2116 Chestnut Street. Open to the public; the association says the grounds are open in daylight while the gates are open. Office Monday to Friday 8 a.m. to 4 p.m. (association page, read November 2026). Parking not checked.',
  [CEM,CEM_C,W('Erie Cemetery')],brick='?',hours='Grounds open in daylight while the gates are open; office Monday to Friday 8 a.m. to 4 p.m.'),
N('first-presbyterian-covenant-erie','First Presbyterian Church of the Covenant','Erie','paw','worship','standing',42.12687,-80.09034,'exact','open','walk','','1929–1930',
  'Built for the Church of the Covenant, formed when the downtown Park and Central Presbyterian churches merged in 1929; the cornerstone was laid on 16 June 1929 and the church dedicated on 14 December 1930. First Presbyterian, founded in 1815, joined it in 1980. The Gothic Revival design is by Corbusier and Foster of Cleveland.',
  'A Gothic Revival church and school with a bell tower, limestone base and trim, floor tiles made by Henry Chapman Mercer\'s Moravian Pottery and Tile Works, stained glass by Connick, D\'Ascenzo and Tiffany studios, and a Skinner organ.',
  'Tiffany, Connick and D\'Ascenzo glass under one roof.',
  'Church entrance on West Sixth Street; office at 250 West Seventh Street with a parking lot. Visitors are welcome at Sunday worship; the church office is open Monday to Friday 9 a.m. to 4 p.m. Times from the church\'s own page, read November 2026.',
  [FPC,FPC_I,W('First Presbyterian Church of the Covenant (Erie, Pennsylvania)')],brick='?',hours='Sunday worship 11 a.m.; 10 a.m. from Memorial Day to Labor Day weekend'),
]
PIN_NOTES={
 'erie-club-reed-mansion':'ArcGIS PointAddress for 524 Peach Street; checked on the leaf-off aerial.',
 'erie-county-courthouse-pa':'ArcGIS PointAddress for 140 West Sixth Street; checked on the leaf-off aerial.',
 'scott-strong-house-gannon':'ArcGIS PointAddress for 109 West Sixth Street; checked on the leaf-off aerial.',
 'old-customshouse-erie':'ArcGIS PointAddress for 411 State Street; checked on the leaf-off aerial.',
 'erie-public-library-1899':'ArcGIS PointAddress for 17 South Park Row (the courthouse complex); checked on the leaf-off aerial.',
 'st-peter-cathedral-erie':'ArcGIS PointAddress for 230 West Tenth Street; checked on the leaf-off aerial.',
 'st-patrick-church-erie':'ArcGIS PointAddress for 130 East Fourth Street; checked on the leaf-off aerial.',
 'st-stanislaus-church-erie':'ArcGIS PointAddress for 516 East Thirteenth Street; checked on the leaf-off aerial.',
 'renaissance-centre-erie':'ArcGIS PointAddress for 1001 State Street; checked on the leaf-off aerial.',
 'strong-vincent-school-erie':'ArcGIS PointAddress for 1330 West Eighth Street; checked on the leaf-off aerial.',
 'villa-maria-academy-erie':'ArcGIS PointAddress for 819 West Eighth Street; checked on the leaf-off aerial.',
 'mercyhurst-old-main-erie':'Between the ArcGIS PointAddress for 501 East 38th Street and the Wikipedia coordinate for the university, in the main campus. Old Main could not be picked out on the leaf-off aerial, so the pin marks the campus, not the building.',
 'erie-cemetery-pa':'ArcGIS PointAddress for 2116 Chestnut Street, the association office by the gate; checked on the leaf-off aerial.',
 'first-presbyterian-covenant-erie':'ArcGIS PointAddress for 250 West Seventh Street; checked on the leaf-off aerial.',
}
BATCH={'key':'paw_kvbh','label':'Erie, Pennsylvania','added':'2026-11-23 01:42'}
