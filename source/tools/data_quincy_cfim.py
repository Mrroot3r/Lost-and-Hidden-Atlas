# November 24, 2026: ten standing buildings in Quincy, Illinois, a Mississippi River town with no place on the map before.
# The names came from a walk-through video about the town's old buildings, used only as a list of names to look up;
# every fact here comes from a source opened while this was written: Wikipedia read as raw text, the Historical Society
# of Quincy and Adams County's articles and museum pages, the churches' and the brewery district's own pages, St. Louis
# Public Radio, Saint Louis Patina, the visitors' bureau's architecture guide, and the Quincy Park District.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
HS='Historical Society of Quincy and Adams County'
DQ=W('Downtown Quincy Historic District')
SEE='Quincy visitors bureau architecture guide'

BATCH={'key':'quincy_cfim','label':'Quincy, Illinois','added':'2026-11-24 16:41'}

PLACES=[
N('dick-brothers-brewery-quincy','Dick Brothers Brewery','Quincy','il','industry','standing',39.92944,-91.40094,'site','open','walk','','1857–1951',
  'A German brewery on York Street in the South Side German Historic District, founded in 1857 by the brothers Matthew, John and Jacob Dick. At its height it shipped 70,000 barrels round the Midwest; Prohibition and the Second World War hurt it, and it went bankrupt in 1951. Its main buildings stand, and since 2015 two local men who own the Stock House buildings (917 to 935 York) have turned the complex into an arts and events district with a brewery museum.',
  'A block of red brick brewery buildings in the round-arched German manner: the office, the tall brew house and storage house with their names on them, the stock house with small windows, the bottle works and a power house with a square chimney across York Street. Underground cellars and tunnels are shown on guided tours, and a museum room of Dick Brothers bottles and signs opened in the old Stock House in 2018. A bar, the Ratskeller, is in the basement.',
  'A pre-Prohibition brewery that kept nearly all its buildings, cellars included.',
  'Privately owned; the Dick Brothers Brewery District at South 9th and York Streets. The owners\' page says every tour includes the museum room and that tours and events are booked through them; no fixed opening days are given there. Street parking. The cellars are shown only on tours.',
  [L('Dick Brothers Brewery District: Museum','https://dickbrothersbrewery.com/museum'),L('Saint Louis Patina: Dick Brothers Brewery','https://stlouispatina.com/dick-brothers-brewery-quincy-illinois/'),W('South Side German Historic District')],
  brick='yes',hours='Tours by booking with the owners; no set opening days on their page'),

N('history-museum-on-the-square-quincy','Old Quincy Public Library (History Museum on the Square)','Quincy','il','civic','standing',39.93177,-91.41029,'exact','open','walk','','1888',
  'Built in 1888 as the Quincy Public Library, a Romanesque Revival building facing Washington Park, the square where Lincoln and Douglas held their sixth debate in 1858. From 1977 it was the Gardner Museum of Architecture and Design. The Historical Society of Quincy and Adams County bought it in 2012 and reopened it in 2015 as its history museum.',
  'A grey stone library of 1888 with a round corner tower under a cone roof. Inside, permanent exhibits on early Quincy and the Mormon refugees of 1838 to 1839, and a stained glass gallery on the second floor with pieces the society names as designed by Frank Lloyd Wright and Tiffany. The society says admission is free and tours are self-guided, with guided tours by reservation. Original library fittings not checked.',
  'The 1888 library on the Lincoln-Douglas square, now full of the town\'s stained glass.',
  'Run by the Historical Society of Quincy and Adams County, 332 Maine Street on the south side of Washington Park. Free admission. Its page gives no days or times that could be read: check the society\'s page before going. Street parking round the square.',
  [L(HS+': History Museum on the Square','https://www.hsqac.org/history-museum'),L(HS+': Visit','https://www.hsqac.org/visit'),DQ],
  brick='no',hours='?'),

N('us-post-office-courthouse-quincy','U.S. Post Office and Courthouse','Quincy','il','civic','standing',39.93336,-91.4031,'exact','view','walk','','1885–1887',
  'A federal post office and courthouse designed in 1885 by Mifflin E. Bell, Supervising Architect of the Treasury, and finished in 1887. Wikipedia says Bell took the idea from Richard Morris Hunt\'s William K. Vanderbilt House in New York, and that the French Renaissance style was then new to Illinois. It is also called the Orville H. Browning Station, and was added to the National Register in 1977.',
  'Limestone walls over brick bearing walls, arched entrances and ground-floor windows, and a steep roof with pointed gables and dormers. The windows of the lower floor go below the street, lit through gratings in the pavement. Interior not checked.',
  'A château of a post office from 1887.',
  'Federal building at 200 North Eighth Street, at Hampshire Street. Seen from the street; whether the post office lobby is still open to the public was not checked. Street parking.',
  [W('United States Post Office and Courthouse (Quincy, Illinois)'),DQ],brick='no'),

N('state-savings-loan-trust-quincy','State Savings Loan and Trust','Quincy','il','civic','standing',39.93175,-91.40899,'exact','view','walk','','1892, 1906',
  'A bank built in 1892 for the brothers Lorenzo and Charles H. Bull, to designs by the Chicago firm Patton and Fisher, with an addition of 1906 by the Quincy architect Ernest M. Wood. The bank did badly after the Depression and the building was nearly torn down before George M. Irwin bought it in 1964 and turned the banking hall into shops. It was added to the National Register in 1979.',
  'A Richardsonian Romanesque front of five bays on Maine Street, each with a window under a heavy stone arch: three bays in the first part, under a big front gable, and two in the 1906 addition. Interior not checked.',
  'Heavy stone arches on Maine Street, saved from the wrecker in 1964.',
  'Privately owned, 428 Maine Street, a block east of Washington Park. View from the street. Street parking.',
  [W('State Savings Loan and Trust'),DQ],brick='?'),

N('hotel-quincy','Hotel Quincy (New Tremont Hotel)','Quincy','il','hotel','standing',39.93337,-91.40767,'site','view','walk','','1910',
  'A seven-storey hotel of 1910 in the downtown historic district, first called the New Tremont Hotel. It is now apartments and, at 513 Hampshire Street, the studios of the television station WGEM and its radio sister.',
  'A seven-storey downtown hotel block about 100 feet tall. Interior not checked.',
  'A 1910 hotel that became a television studio.',
  'Privately owned apartments and studios, 513 Hampshire Street. View from the street. Street parking.',
  [DQ,W('WGEM-TV')],brick='?'),

N('bnai-sholom-temple-quincy','B\'nai Sholom Temple','Quincy','il','worship','standing',39.93657,-91.40205,'exact','view','walk','','1869–1870',
  'A Reform congregation founded in 1852 built this Moorish Revival synagogue, begun in 1869 and finished in 1870 to designs by Robert Bunce. A tornado in 1947 damaged its twin minaret-like towers, 80 feet high, and they were not rebuilt. The shrinking congregation closed it with a deconsecration service in May 2019, and the building was later sold.',
  'A Moorish Revival synagogue front on North Ninth Street, its two corner towers cut short since 1947. What it is used for now was not checked. Interior not checked.',
  'One of the oldest synagogue buildings in Illinois, minus its minarets.',
  'Privately owned since its sale, 427 North Ninth Street. View from the street only. Street parking.',
  [W('B\'nai Sholom Temple'),L('St. Louis Public Radio: Quincy synagogue turns off the lights (2019)','https://www.stlpr.org/arts/2019-05-21/quincy-synagogue-turns-off-the-lights-for-the-last-time'),L(SEE+': Temple B\'nai Shalom','https://seequincy.com/?p=6045')],
  brick='?'),

N('st-francis-solanus-church-quincy','St. Francis Solanus Church','Quincy','il','worship','standing',39.93952,-91.38815,'exact','open','walk','','1885',
  'A Catholic parish founded in 1860 by Franciscan friars from Germany, who ran it for 160 years before handing it to the Diocese of Springfield in 2020; it was their novitiate, and at one time 55 priests lived here. The church was built in 1885. Father Augustus Tolton, the first Black priest in the United States, studied at the friars\' college next door.',
  'The church is 75 feet high with a steeple of 217 feet and seats nearly 1,000. The parish describes a white and gilded high altar more than three storeys tall, designed by the Franciscan brother Adrian Wewer and built by Henry Schenk of Quincy, with a copy of the Last Supper at its base and a crucifix that turns to show three different backgrounds; carved friars\' choir stalls with a psalm in Latin running across them; painted stations of the cross; relics; and a front window of St. Francis Solanus playing the violin.',
  'A Franciscan church with a high altar three storeys tall.',
  'St. Francis Solanus Parish, 1721 College Avenue, next to Quincy University. The church opens for Mass; times from the parish\'s own page. Street parking.',
  [L('St. Francis Solanus Parish','https://stfrancissolanus.com/?p=573'),L('St. Francis Solanus: video tour and history','https://stfrancissolanus.com/about/video-tour/')],
  brick='?',hours='Saturday 4:30 p.m.; Sunday 7, 9 and 11 a.m. Masses'),

N('francis-hall-quincy-university','Francis Hall, Quincy University','Quincy','il','inst','standing',39.93959,-91.38664,'exact','view','walk','','1871–1898',
  'Franciscan friars from Germany founded St. Francis Solanus College in 1860 at Eighth and Maine Streets; under Father Anselm Mueller it moved to what is now College Avenue. Francis Hall, at the centre of the campus, was built and enlarged between 1871 and 1898, and for decades held nearly all the college\'s classes. Father Augustus Tolton entered the college in 1878. It became Quincy College and Seminary in 1917 and is now Quincy University.',
  'A long hall of 1871 to 1898 at the heart of the campus, with the college chapel of 1911 beside it. Interior not checked.',
  'Where the first Black Catholic priest in the United States went to college.',
  'Quincy University, a private Franciscan university, College Avenue at North 18th Street. Seen from the street and campus walks; visiting rules not checked. Street parking.',
  [W('Quincy University'),L(HS+': Quincy University, a glance at a community treasure','https://www.hsqac.org/quincy-university-a-glance-at-a-community-treasuree9471ceb/')],
  brick='?'),

N('salem-evangelical-church-quincy','Salem Evangelical Church (Salem United Church of Christ)','Quincy','il','worship','standing',39.92675,-91.40137,'exact','open','walk','','1876–1877',
  'A German congregation first met at Easter 1848 and built a small brick church on this corner that year. The present church, by the architect John S. McKeen, was begun in June 1876 and dedicated on September 23, 1877; the parish history says women of the congregation carried bricks in their aprons to the men on the scaffolding. It joined the United Church of Christ in 1957.',
  'A Victorian Gothic hall church 110 feet long with a spire of 237 feet. The church\'s own history lists a carved walnut apse, high pulpit and choir, a full balcony, seats for 1,000, a Sermon on the Mount window and a rose window put in in 1910, side windows of 1952, three hand-rung bells (the smallest from the first church), a four-faced clock of 1894 still wound by hand twice a week, a font from the first church, and an altar Bible given by Kaiser Wilhelm II in 1898.',
  'A German hall church whose clock is still wound by hand.',
  'Salem United Church of Christ, 435 South Ninth Street at State Street, in the South Side German Historic District. Sunday worship is open to all; church office Tuesday and Thursday mornings. Street parking.',
  [L('Salem UCC: Architecture','https://salemquincy.org/achitecture'),L('Salem UCC: History','https://www.salemquincy.org/history'),L('Salem UCC','https://www.salemquincy.org/'),L(SEE+': Salem Evangelical Church','https://seequincy.com/?p=6026')],
  brick='yes',hours='Sunday worship 9 a.m.; office Tuesday and Thursday 9 a.m. to noon'),

N('south-park-stone-bridge-quincy','South Park stone arch bridge','Quincy','il','landmark','standing',39.91055,-91.40324,'site','public','walk','','1899',
  'South Park was bought from Judge B. F. Berrian and his brothers, a 55-acre tract that took in the old picnic grounds of Watson\'s Spring and Curtis Creek. In 1899 a stone arched bridge designed by the Quincy architect E. M. Wood was built over Curtis Creek at Eighth Street, for $5,600.',
  'A stone arch carrying South Eighth Street over Curtis Creek at the west side of the park. The pin is on the Eighth Street bridge as OpenStreetMap maps it; that this is the 1899 arch was read from the park history, not checked on the ground.',
  'An 1899 stone arch at the gate of Quincy\'s South Park.',
  'Quincy Park District; South Park covers 135 acres at 12th and Harrison Streets, with walking paths, shelters and restrooms. The bridge is on a public street. Park hours not checked. Parking along the park roads.',
  [L(HS+': Parker\'s vision, 125 years of Quincy parks','https://www.hsqac.org/parker-s-vision-125-years-of-quincy-parks97a496cb'),L('Quincy Park District: South Park','https://www.quincyparkdistrict.com/parks/south')],
  conf='mixed',brick='no'),
]

PIN_NOTES={
 'dick-brothers-brewery-quincy':'Address lookup for 917 York Street, the Stock House buildings the museum is in; the aerial shows it on the building.',
 'history-museum-on-the-square-quincy':'Address lookup for 332 Maine Street; the aerial shows it on the building.',
 'us-post-office-courthouse-quincy':'Address lookup for 200 North Eighth Street; the aerial shows it on the building.',
 'state-savings-loan-trust-quincy':'Address lookup for 428 Maine Street; the aerial shows it on the building.',
 'hotel-quincy':'Address lookup for 513 Hampshire Street; the aerial shows it on the building.',
 'bnai-sholom-temple-quincy':'Address lookup for 427 North Ninth Street; the aerial shows it on the building.',
 'st-francis-solanus-church-quincy':'Address lookup for 1721 College Avenue; the aerial shows it on the building.',
 'francis-hall-quincy-university':'OpenStreetMap building named Francis Hall; the aerial shows it on the building.',
 'salem-evangelical-church-quincy':'Address lookup for 435 South Ninth Street; the aerial shows it on the building.',
 'south-park-stone-bridge-quincy':'OpenStreetMap bridge carrying South Eighth Street over Curtis Creek; the aerial shows the road crossing the wooded creek.',
}
