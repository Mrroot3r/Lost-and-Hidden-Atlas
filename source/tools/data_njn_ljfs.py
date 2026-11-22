# November 22, 2026: Newark, New Jersey, downtown and the wards round it (region njn, North Jersey). The names came from a
# video walk-through of Newark's old buildings, taken as tips only; every fact below is from a source opened and read:
# Wikipedia articles read with tools/wiki_raw.py, the Essex County National Register list, the National Register form for the
# Mutual Benefit building, New Jersey Historic Trust pages, the Newark Public Library's "Knowing Newark" articles, Cinema
# Treasures, Jersey Digs, and the own pages of the cathedral, the library and the New Jersey Historical Society (page.py).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'njn_ljfs','label':'Newark, New Jersey: cathedral, courthouse, theatres and the old downtown','added':'2026-11-22 16:48'}
NRHP_LIST=W('National Register of Historic Places listings in Essex County, New Jersey')
BASILICA=L('Cathedral Basilica of the Sacred Heart: Planning your visit (hours, tours)','https://www.newarkbasilica.org/other')
NJHT_COURT=L('New Jersey Historic Trust: Essex County Court House','https://www.nj.gov/dca/njht/funded/sitedetails/essexcountycourthouse.shtml')
CGS_COURT=L('Cass Gilbert Society: Essex County Courthouse','https://cassgilbertsociety.org/works/essex-county-courthouse/')
BETELLE_HOR=L('James Betelle, Where Are You?: Essex County Hall of Records (1927 description)','https://jamesbetelle.com/2006/10/31/essex-county-hall-of-records/')
NPL_MAIN=L('Newark Public Library: Main Library (hours, parking)','https://www.npl.org/main-library')
MAKER=L('Makerhoods: Krueger-Scott Mansion','https://www.makerhoods.com/krueger-scott-mansion')
JD_KRUEGER=L('Jersey Digs: Krueger-Scott Mansion Makerhoods project','https://jerseydigs.com/developer-expects-newarks-krueger-scott-mansion-makerhoods-project-to-open-in-december/')
NWKHIST_PEDDIE=L('NewarkHistory.com: The Peddie Memorial/First Baptist Church','https://www.newarkhistory.com/peddie1.html')
NJHT_SP=L('New Jersey Historic Trust: South Park Presbyterian Church','https://www.nj.gov/dca/njht/funded/sitedetails/south_park_presbyterian_church.shtml')
JD_SP=L('Jersey Digs: Landmark church in Lincoln Park could be converted into apartments','https://jerseydigs.com/south-park-presbyterian-church-newark-conversion/')
JD_NSH=L('Jersey Digs: Newark Symphony Hall completes first phase of renovation','https://jerseydigs.com/newark-symphony-hall-renovation/')
CT_PROCTOR=L('Cinema Treasures: RKO Proctor\'s Theatre, 116 Market Street','https://cinematreasures.org/theaters/7023')
JD_PROCTOR=L('Jersey Digs: Newark\'s RKO Proctor\'s Palace could be restored as apartments','https://jerseydigs.com/rko-proctor-palace-newark/')
CT_ADAMS=L('Cinema Treasures: Adams Theatre, 28 Branford Place','https://cinematreasures.org/theaters/7011')
NJHS=L('New Jersey Historical Society (hours, admission)','https://www.jerseyhistory.org')
KN_TIFF=L('Knowing Newark (Newark Public Library): City\'s industrial past shines with jewelry of gold and gems','https://knowingnewark.npl.org/citys-industrial-past-shines-with-jewelry-of-gold-and-gems/')
KN_TIFF2=L('Knowing Newark (Newark Public Library): Relics of industry and commerce reborn as gracious homes','https://knowingnewark.npl.org/relics-of-industry-and-commerce-reborn-as-gracious-homes/')
SM_TIFF=L('Specialty Metals: The old Tiffany factory in Newark (quotes the 1887 newspaper)','https://specialtymetals.squarespace.com/blog/2018/7/26/precious-metals-building-profile')
PLACES=[
N('sacred-heart-cathedral-newark-nj','Cathedral Basilica of the Sacred Heart','Newark','njn','worship','standing',40.75498,-74.17839,'exact','open','drive','','1899–1954',
  'The seat of the Roman Catholic Archdiocese of Newark, facing Branch Brook Park. Building began in 1899 and was finished in 1954; it was first designed as an English-Irish Gothic church and changed to French Gothic along the way. It is the fifth-largest cathedral in North America, about the size of Westminster Abbey.',
  'Rose windows of stained glass by the Zettler studio, the one over the main door 36 feet across, and the largest pipe organ the Schantz company ever built. Chapels inside honour several saints. Visitors may go in at set times (below); a free tour follows the noon Mass on the first Sunday of the month.',
  '',
  'An active cathedral of the Archdiocese of Newark. Outside Mass times enter through the rectory at 89 Ridge Street. It shuts for private events such as weddings and funerals, so its page asks visitors to telephone first. Group tours on weekdays by appointment. Parking not checked.',
  [W('Cathedral Basilica of the Sacred Heart (Newark)'),BASILICA,NRHP_LIST],brick='no',
  hours='Monday 9 a.m. to 5 p.m., Tuesday to Friday 9 a.m. to 7 p.m., Saturday 9 a.m. to 5 p.m., closed at lunch; Sunday Masses 8:30, 10 and noon'),
N('essex-county-courthouse-newark-nj','Essex County Courthouse','Newark','njn','civic','standing',40.73711,-74.17866,'exact','view','drive','','1904–1908',
  'The county courthouse designed by Cass Gilbert, architect of the Woolworth Building, on a hill at the west end of Market Street. The dates differ by source: Wikipedia says it was built in 1904, the New Jersey Historic Trust says 1906, and the Cass Gilbert Society gives design and building as 1904 to 1908. In 1929 Guilbert and Betelle remodelled it when the Hall of Records was built behind it.',
  'A broad flight of steps up to a portico of eight Corinthian columns, with a seated figure of Justice on the pediment and nine sculptures by the Piccirilli Brothers on the front. Inside, a four-storey rotunda under a Tiffany stained-glass skylight, with murals; the state restored the interior and exterior in the late 1990s. Gutzon Borglum\'s Seated Lincoln is on the plaza in front.',
  '',
  'Part of the Essex County Government Complex. Whether the public may walk in to see the rotunda, and when, was not checked: look from the plaza, where the Lincoln statue is. Parking not checked.',
  [W('Essex County Courthouse'),NJHT_COURT,CGS_COURT,W('Essex County Government Complex'),NRHP_LIST],conf='mixed',brick='no'),
N('essex-county-hall-of-records-newark-nj','Essex County Hall of Records','Newark','njn','civic','standing',40.73764,-74.17997,'exact','view','drive','','1925–1927',
  'A neo-classical county office tower by Guilbert and Betelle, built from 1925 to 1927 (cornerstone 1926) behind the Cass Gilbert courthouse, to take county offices out of it. It was refitted as offices from 2008 to 2010.',
  'Limestone walls, rusticated and hammered on the first storey. A glass skywalk joins it to a newer court building to the south, and the Legends Way promenade runs beside it.',
  '',
  'County offices at 465 Dr. Martin Luther King Jr. Boulevard, in the Essex County Government Complex. Look from the street. Parking not checked.',
  [W('Essex County Government Complex'),BETELLE_HOR],brick='no'),
N('newark-city-hall-nj','Newark City Hall','Newark','njn','civic','standing',40.73188,-74.17397,'exact','view','drive','','1902',
  'A five-storey Beaux-Arts city hall built in 1902 for about $2.6 million. In 1986 a developer paid to cover the dome in 24-carat gold, and the building was renovated in 2006.',
  'The gilded dome. Inside, according to Wikipedia: carved marble, a grand central staircase, stained-glass skylights, ornamental plaster and wrought iron. Whether visitors may go in to look was not checked.',
  '',
  'The working city hall, 920 Broad Street. Look from Broad Street. Parking not checked.',
  [W('Newark City Hall'),NRHP_LIST],brick='no'),
N('newark-public-library-main-nj','Newark Public Library, Main Library','Newark','njn','civic','standing',40.74452,-74.17066,'exact','open','drive','','1899–1901',
  'The main building of Newark\'s free public library, facing Washington Park. The cornerstone was laid in January 1899 and the building opened in 1901; Rankin and Kellogg modelled it on the Palazzo Strozzi in Florence. It has also served as a museum, lecture hall and gallery.',
  'The Florentine palace front on Washington Street. Inside, galleries on several floors, the Philip Roth Personal Library and the James Brown African American Room on the second floor, and six floors of book stacks at the back.',
  '',
  'A public library, free to go into. No parking of its own: metered spaces on Washington Street (no parking 7 to 9 a.m. and 4 to 6 p.m.) and private lots nearby; many buses stop on Broad Street. The hours below are the summer hours its page gives.',
  [W('Newark Public Library'),NPL_MAIN],brick='no',
  hours='Summer: Monday to Friday 9 a.m. to 5:30 p.m. (Wednesday to 8:30 p.m.), Saturday 9 a.m. to 1:30 p.m.'),
N('american-insurance-company-building-newark-nj','American Insurance Company Building','Newark','njn','civic','standing',40.74433,-74.17107,'exact','view','drive','','1930',
  'A sixteen-storey neo-classical tower, 326 feet tall, finished in 1930 as the home office of the American Insurance Company (founded in Newark in 1846), one of the city\'s oldest and tallest skyscrapers. The company gave it to Rutgers University; after a hotel plan fell through it reopened in November 2015 as student rooms, event space and the chancellor\'s apartment, and in 2023 it was renamed for Ruth Bader Ginsburg.',
  'The tower on Washington Park, next to the Main Library. Its great hall has 20-foot ceilings and 15-foot windows (not checked whether the public may see it).',
  '',
  'A Rutgers University–Newark building at 15 Washington Street. Look from Washington Park. Parking not checked.',
  [W('American Insurance Company Building')],brick='no'),
N('krueger-scott-mansion-newark-nj','Krueger-Scott Mansion','Newark','njn','landmark','standing',40.73258,-74.18161,'exact','view','drive','','1888',
  'A 40-room mansion built in 1888 for Gottfried Krueger, founder of the Krueger brewery, at Court Street and what is now Dr. Martin Luther King Jr. Boulevard. The Scottish Rite Freemasons bought it in 1926 and added a 700-seat auditorium; in 1958 Louise Scott bought it and ran a beauty school on the ground floor. It stood empty after 1982 and was looted, then the city and the state spent millions to stabilise it.',
  'Wikipedia says that by 2023 it had been almost completely restored and landscaped. Makerhoods, which owns it, is turning it into co-working, offices, event space and history displays, with new mixed-income apartments in a building next door on Court Street.',
  '',
  'Owned by Newark Makerhoods (city tax records, as quoted by Jersey Digs). Whether it is open to visitors was not checked: look from Dr. Martin Luther King Jr. Boulevard or Court Street. Parking not checked.',
  [W('Krueger Mansion'),MAKER,JD_KRUEGER,NRHP_LIST],brick='yes'),
N('peddie-memorial-church-newark-nj','First Baptist Peddie Memorial Church','Newark','njn','worship','standing',40.7416,-74.16873,'exact','view','drive','','1888',
  'A Baptist church at Broad and Fulton streets paid for by Thomas Baldwin Peddie, a leather-goods maker who was mayor of Newark and a congressman. The Register gives 1888; NewarkHistory.com says the congregation, which dates from 1801, moved in in 1890. The architect was William Halsey Wood.',
  'A domed building mixing Byzantine, Romanesque, Moorish and Gothic touches, with grotesques, carved flowers and a thistle on one front column. Inside, oak and metalwork, lamps hung from gargoyles, and a large baptism pool behind the stage. NewarkHistory.com says the front doors are shut on weekdays and the side door may be open.',
  '',
  'An active church at 572 Broad Street. No service times were found on a page of its own, so look from Broad Street. Parking not checked.',
  [W('First Baptist Peddie Memorial Church'),NWKHIST_PEDDIE,NRHP_LIST],conf='mixed',brick='no',hours='?'),
N('south-park-presbyterian-facade-newark-nj','South Park Presbyterian Church front','Newark','njn','worship','ruins',40.72773,-74.1771,'exact','view','drive','','1853',
  'A Greek Revival church of 1853 by John Welch on Broad Street at Lincoln Park, where Abraham Lincoln spoke in 1861 on his way to his inauguration. A fire in 1992 destroyed most of it; only the stone front and its two towers survived. The Lincoln Park Coast Cultural District owns it and has had state grants to stabilise the front; plans have moved from an outdoor stage to apartments built behind it.',
  'The brownstone portico with four Ionic columns between two round colonnaded towers, standing alone.',
  'A church front that outlived its church.',
  'Owned by the Lincoln Park Coast Cultural District. Look from Broad Street. Parking not checked.',
  [W('South Park Calvary United Presbyterian Church'),NJHT_SP,JD_SP,NRHP_LIST],brick='no'),
N('newark-symphony-hall-nj','Newark Symphony Hall (Salaam Temple)','Newark','njn','civic','standing',40.72779,-74.17563,'exact','open','drive','','1925',
  'Built by the Shriners in 1925 as Salaam Temple, known for years as the Mosque Theater, and Newark Symphony Hall since 1964. Frank Grad designed it. The city bought it in 2018 and a $75 million restoration in four phases began, the first finished by 2023, with the hall staying open meanwhile.',
  'Greek and Egyptian motifs, marble columns, a crystal chandelier and gold-leaf fretwork inside; a 3,500-seat main hall named for Sarah Vaughan and a restored 15,000-square-foot Terrace Ballroom.',
  '',
  'A working performing-arts hall at 1020 Broad Street, run by the Newark Performing Arts Corporation; you go in for a show or an event. Parking not checked.',
  [W('Newark Symphony Hall'),JD_NSH,NRHP_LIST],brick='no',hours='?'),
N('proctors-palace-theatre-newark-nj','Proctor\'s Palace Theatre','Newark','njn','civic','standing',40.73603,-74.17436,'exact','view','drive','','1915–1968',
  'A "double-decker" vaudeville house that opened on Thanksgiving Day 1915: a 2,800-seat theatre at street level and a roof-garden theatre of about 1,400 seats on the top floors, by architect John W. Merrow. It became RKO Proctor\'s and closed in 1968, and has stood more or less derelict since. Jersey Digs reports a plan, approved by the city\'s landmarks commission, to make the Market Street front building into 38 apartments; the main auditorium behind is on a separate lot, and the city has said it would have to be demolished.',
  'The ten-storey Market Street front. The auditorium is not open.',
  'A theatre stacked on a theatre.',
  'Private and closed, at 116 Market Street. Look from Market Street only. Parking not checked.',
  [CT_PROCTOR,JD_PROCTOR],brick='?'),
N('adams-theatre-newark-nj','Adams Theatre','Newark','njn','civic','standing',40.73477,-74.17424,'exact','view','drive','','1912–1986',
  'Opened on January 8, 1912 as the Shubert Theatre, by architect William E. Lehman, for Broadway plays; it became Keeney\'s, with vaudeville and films, in 1913, and the Adams in 1939. It ran as a burlesque house in its best years and closed as a cinema on April 1, 1986.',
  'The front on Branford Place. Cinema Treasures says the 2,037-seat auditorium is abandoned while the lobby is used as a clothing store; in 2019 the front was dressed for filming a feature set in 1967.',
  '',
  'Private, at 28 Branford Place. Look from the street. Parking not checked.',
  [CT_ADAMS],brick='?'),
N('essex-club-nj-historical-society-newark','Essex Club (New Jersey Historical Society)','Newark','njn','civic','standing',40.73879,-74.16851,'exact','open','drive','','1926',
  'A Georgian-style club house by Guilbert and Betelle, built in 1926 for the Essex Club on Military Park. The New Jersey Historical Society, founded in 1845 and in Newark since 1846, moved in in 1997.',
  'Two floors of exhibitions and a library reading room on the fifth floor, in what were the club\'s squash courts.',
  '',
  'Museum of the New Jersey Historical Society, 52 Park Place. Admission $4 to the museum, $7 to the library, members free; the library asks for an appointment. Closed for Thanksgiving. Parking not checked.',
  [W('New Jersey Historical Society'),NJHS,NRHP_LIST],brick='yes',
  hours='Museum Tuesday to Saturday 10 a.m. to 5 p.m.; library Tuesday to Saturday noon to 5 p.m., by appointment'),
N('bamberger-building-newark-nj','Bamberger\'s store (165 Halsey Street)','Newark','njn','civic','standing',40.73689,-74.17345,'exact','view','drive','','1912–1929',
  'The flagship of the Bamberger\'s department stores, designed by Jarvis Hunt and opened on October 16, 1912 as an eight-storey store; it was raised to fourteen storeys in 1922 and 1929 and fills the block of Market, Washington, Bank and Halsey streets. After 1929 it was the country\'s sixth-largest store. Macy\'s, which had taken over Bamberger\'s, closed it in 1992; it is now 165 Halsey Street, an office building and one of the world\'s largest carrier hotels for telecommunications.',
  'The whole block of the old store, in the Four Corners Historic District.',
  '',
  'Private offices. Look from the street. Parking not checked.',
  [W('165 Halsey Street'),W('Bamberger\'s')],brick='no'),
N('central-king-building-newark-nj','Central King Building (old Central High School)','Newark','njn','civic','standing',40.74154,-74.17706,'site','view','drive','','1912',
  'Built as the Central Commercial and Manual Training School, a vocational high school with a forge, a foundry and a 1,500-seat auditorium, and dedicated on January 31, 1912. Ernest F. Gilbert, the school board\'s architect, designed it. Central High School used it until the New Jersey Institute of Technology bought it in 2010; after a renovation it reopened as a university building in April 2017.',
  'Collegiate Gothic, terracotta and brick, three storeys with a taller tower at each corner. The grand front staircase was taken down long ago for an indoor swimming pool.',
  '',
  'A building of the New Jersey Institute of Technology. Look from the street. Parking not checked.',
  [W('Central King Building'),W('Central High School (Newark, New Jersey)')],brick='?'),
N('newark-broad-street-station-nj','Newark Broad Street station','Newark','njn','rail','standing',40.74745,-74.17225,'exact','public','drive','stations','1903',
  'The Delaware, Lackawanna and Western Railroad\'s Newark station, opened in 1903 after two years of building, on the site of the 1836 station of the Morris and Essex Railroad. New Jersey Transit runs its trains, and since 2006 it has also been the north end of the Newark Light Rail extension. It was renovated from 2004 to 2008, when the old westbound shelter was removed.',
  'A clock tower and a brick and stone front on the main building.',
  '',
  'A working station; New Jersey Transit runs it (Wikipedia). Open to anyone using or meeting the trains. Parking not checked.',
  [W('Newark Broad Street station'),NRHP_LIST],brick='yes'),
N('tiffany-factory-newark-nj','Tiffany & Company silver works','Newark','njn','industry','standing',40.78466,-74.16642,'exact','view','drive','','1887–1984',
  'Tiffany & Company\'s silver and jewellery works, finished in 1887 according to the local newspaper quoted by Specialty Metals. Here the company made its silver flatware, its stationery and its blue boxes. The factory was sold in 1984 and turned into housing; the 130-unit Tiffany Manor apartments opened in 1993, with townhouses on the rest.',
  'The old red-brick factory with its tower, built to hold a 23,000-gallon water tank, at 90 Tiffany Boulevard.',
  '',
  'Private apartments. Look from Tiffany Boulevard. Parking not checked.',
  [KN_TIFF,KN_TIFF2,SM_TIFF],conf='mixed',brick='yes'),
]
PIN_NOTES={
 'sacred-heart-cathedral-newark-nj':'Pin is the ArcGIS address point for 89 Ridge Street, the entrance the cathedral\'s page gives; it matches the Wikipedia coordinate.',
 'essex-county-courthouse-newark-nj':'Pin is the ArcGIS address point for 470 Dr. Martin Luther King Jr. Boulevard, beside the Wikipedia coordinate.',
 'essex-county-hall-of-records-newark-nj':'Pin moved on the aerial onto the large block with a light well just north-west of the courthouse. The OpenStreetMap point for the Hall of Records fell on the street at its east corner, and the ArcGIS point for 465 Dr. Martin Luther King Jr. Boulevard about 80 m further west.',
 'newark-city-hall-nj':'Pin is the ArcGIS address point for 920 Broad Street, beside the Register coordinate.',
 'newark-public-library-main-nj':'Pin is the ArcGIS address point for 5 Washington Street.',
 'american-insurance-company-building-newark-nj':'Pin is the ArcGIS address point for 15 Washington Street.',
 'krueger-scott-mansion-newark-nj':'Pin is an ArcGIS address point on Dr. Martin Luther King Jr. Boulevard that matches the Register coordinate.',
 'peddie-memorial-church-newark-nj':'Pin is the ArcGIS address point for 572 Broad Street, beside the Register coordinate.',
 'south-park-presbyterian-facade-newark-nj':'Pin is the OpenStreetMap ruin named South Park Presbyterian Church (1033 Broad Street). The ArcGIS point for 1035 Broad Street fell on the lawn of Lincoln Park and was moved.',
 'newark-symphony-hall-nj':'Pin is the ArcGIS address point for 1020 Broad Street.',
 'proctors-palace-theatre-newark-nj':'Pin is the ArcGIS address point for 116 Market Street, the front building.',
 'adams-theatre-newark-nj':'Pin is the ArcGIS address point for 28 Branford Place.',
 'essex-club-nj-historical-society-newark':'Pin is the ArcGIS address point for 52 Park Place.',
 'bamberger-building-newark-nj':'Pin is the ArcGIS address point for 165 Halsey Street; the building fills the block.',
 'central-king-building-newark-nj':'Pin is the OpenStreetMap building named Central King Building, about 90 m from the Wikipedia coordinate; on the aerial it is a square block round a courtyard.',
 'newark-broad-street-station-nj':'Pin is the OpenStreetMap building named Broad Street Station, beside the tracks; the ArcGIS point for 25 University Avenue fell on an empty lot south of it.',
 'tiffany-factory-newark-nj':'Pin is the ArcGIS address point for 90 Tiffany Boulevard.',
}
