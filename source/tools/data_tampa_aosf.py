# November 28, 2026: downtown Tampa, Ybor City and Tampa Heights, Hillsborough County, Florida. The names came from a
# video walk through old Tampa photographs (a tip only); every fact below is from the sources linked on each place:
# Wikipedia articles, National Register records and forms from the Park Service, and the owners' own pages.
# Nothing was checked on the ground.
from data_b import N
from data_ma import W

BATCH={'key':'tampa_aosf','label':'Tampa, Florida (downtown and Ybor City)','added':'2026-11-28 18:41'}

NR='https://npgallery.nps.gov/AssetDetail/NRIS/'

PLACES=[
N('sacred-heart-church-tampa','Sacred Heart Catholic Church','Tampa','fl','worship','standing',27.94933,-82.45724,'exact','open','walk','','1898–1905',
  'The first Catholic parish on Florida\'s west coast was founded here in 1860 as St. Louis Parish, with a wooden church on this lot. Jesuits took over the parish in 1888, ground was broken for the present church in 1898, the cornerstone was laid in 1900, and it was dedicated in 1905, when the parish took the name Sacred Heart. The architect was Nicholas J. Clayton of Galveston, Texas.',
  'A Romanesque Revival church of granite and marble with a dome 135 feet high. Wikipedia lists solid oak pews and doors, porcelain tiles, a Carrara marble altar and 70 stained glass windows made for the church by Franz Mayer & Co. of Munich. The parish says the church is open to the public on weekdays until 3 p.m.',
  'A Munich-glass Romanesque church with a 135-foot dome in downtown Tampa.',
  'Sacred Heart Parish, Diocese of St. Petersburg, 509 North Florida Avenue. The parish page says the church is often closed on Saturdays until 4 p.m. for weddings, and on weekends closes after the last Mass. Metered street parking and private lots downtown; no lot of its own is named on its page. Hours from the parish\'s Mass times page, November 2026.',
  [W('Sacred Heart Catholic Church (Tampa, Florida)'),['Parish Mass times','https://sacredheartfla.org/mass-times/']],
  hours='Weekdays open to 3 p.m.; Mass Mon–Fri 7 a.m. and 12:10 p.m., Sat 5:30 p.m., Sun 7:30, 9, 10:30 a.m., noon, 5:30 p.m.',
  brick='?', arch='Nicholas J. Clayton', archw='Wikipedia: "The architect for the new Sacred Heart Church was Nicholas J. Clayton"'),

N('tampa-city-hall-1915','Old Tampa City Hall','Tampa','fl','civic','standing',27.94767,-82.45724,'exact','view','walk','','1915',
  'Tampa\'s city hall since it was built in 1915, designed by the Tampa firm Bonfoey & Elliott and listed on the National Register in 1974. It was recorded by the Historic American Buildings Survey in 1981 and renovated for about $16 million in 2017.',
  'A three-storey base carries a five-storey tower with a mansard clock stage under heavy brackets; the Register form gives the materials as granite, brick and terra cotta, with figure sculpture, a stone cornice and a stone balustrade at the roofline. Interior not checked.',
  'A 1915 clock tower still keeping time over Kennedy Boulevard.',
  'City of Tampa offices, 315 East Kennedy Boulevard at Florida Avenue. Seen from the sidewalks; office hours not checked. Metered street parking and private lots downtown.',
  [W('Tampa City Hall'),['National Register record',NR+'74000639']],
  brick='?', arch='Bonfoey & Elliott', archw='Wikipedia: "designed by Bonfoey & Elliott"; the National Register record also names McGucken & Hyer'),

N('us-courthouse-tampa-1905','Old U.S. Courthouse and Post Office (Le Méridien)','Tampa','fl','civic','standing',27.95007,-82.45747,'exact','open','walk','','1902–1905',
  'The federal courthouse, post office and custom house finished in 1905 under James Knox Taylor, Supervising Architect of the Treasury; the Register record gives 1902, 1905 and 1931 as its years. It held the federal court for the Southern District of Florida and, from 1962 to 2001, the Middle District. The City of Tampa now owns it, and it is a Le Méridien hotel.',
  'The whole block-long federal building still stands on Florida Avenue across from Sacred Heart church. As a hotel its lobby is open to guests; how much of the old courtroom fabric survives inside was not checked.',
  'A 1905 federal courthouse where you can now book a room.',
  'Owned by the City of Tampa and run as a Le Méridien hotel, 601 North Florida Avenue. Hours: a working hotel, front desk hours not checked. Metered street parking and private lots downtown.',
  [W('United States Courthouse Building and Downtown Postal Station (Tampa, Florida)'),['National Register record',NR+'74000633']],
  hours='?', brick='?', arch='James Knox Taylor', archw='Wikipedia and the National Register record: built under the supervision of James Knox Taylor, Supervising Architect of the Treasury'),

N('circulo-cubano-tampa','El Círculo Cubano (Cuban Club)','Tampa','fl','civic','standing',27.96219,-82.44455,'exact','view','walk','','1917',
  'The Cuban mutual aid society of Ybor City, founded as El Club Nacional Cubano in 1899 and renamed El Círculo Cubano in 1902. Its first clubhouse of 1908, on this corner, burned in 1916, and the present one was built in 1917 to the design of Tampa architect M. Leo Elliott. It once held a theatre, bowling alley, spa, pharmacy, ballroom, library and cantina; part of the ballroom ceiling fell on New Year\'s Day 1996, after restoration work completed in 1995.',
  'Imported tile, stained glass, sgraffito spandrels and murals (Wikipedia). The building has a theatre; it was listed on the National Register in 1972. Interior not checked.',
  'The Cuban workers\' clubhouse of Cigar City.',
  'El Círculo Cubano, Palm Avenue at 14th Street, Ybor City. The club uses it as a hall for events; no public opening hours were found, so it is seen from the street. Street parking and lots in Ybor City.',
  [W('Circulo Cubano de Tampa'),['National Register record',NR+'72000320']],
  brick='?', arch='M. Leo Elliott', archw='Wikipedia: "designed by Tampa architect M. Leo Elliott"; the National Register record gives the architect as unknown', conf='mixed'),

N('centro-espanol-de-tampa','El Centro Español de Tampa','Tampa','fl','civic','standing',27.96064,-82.44196,'exact','view','walk','','1912',
  'Spanish immigrants founded El Centro Español in Ybor City in 1891, the first of the neighbourhood\'s ethnic clubs and mutual aid societies and the model for the others. This clubhouse was built in 1912 to the design of Francis J. Kennard and became a National Historic Landmark in 1988. The society moved to its West Tampa clubhouse in 1983 and sold this one, which stood empty for some years before it was restored in 2010 as part of a shopping and entertainment block.',
  'A dark red brick building about 38 feet high, with arched windows and doors trimmed in white stone keystones, eyebrow windows in the half storey, and a red tile roof (Register form); Wikipedia describes the style as French Renaissance Revival with Moorish and Spanish touches. Interior not checked.',
  'The 1912 clubhouse of Ybor City\'s first mutual aid society.',
  'Privately owned, 1526–1536 East 7th Avenue, Ybor City; the ground floor has been let to a restaurant, which was not checked. Seen from 7th Avenue. Street parking and lots in Ybor City.',
  [W('El Centro Español de Tampa'),['National Register record',NR+'88001823']],
  brick='yes', bcol='red', arch='Francis J. Kennard', archw='National Register record and Wikipedia name Francis J. Kennard; the Register form describes "the 38\'-high dark red brick edifice"'),

N('tampa-theatre','Tampa Theatre','Tampa','fl','civic','standing',27.95038,-82.45881,'exact','open','walk','','1925–1926',
  'An atmospheric movie palace designed by John Eberson, opened on October 15, 1926, and the first commercial building in Tampa with air conditioning. Threatened with demolition in 1973, it was saved when the City took over its leases, and it reopened in 1978; the Tampa Theatre Foundation led a restoration after a fire in 1991. It still shows films and holds hundreds of events a year.',
  'Inside, the auditorium is made to look like a Mediterranean courtyard at night, with statues, flowers, gargoyles and stars on the ceiling (Wikipedia). The theatre runs guided tours of the building.',
  'A 1926 movie palace with a starry sky for a ceiling.',
  'Tampa Theatre Foundation, 711 North Franklin Street. The box office opens weekdays at 10 a.m. and, in the evening and at weekends, at least 30 minutes before the first show (the theatre\'s Know Before You Go page, November 2026). Its page says street meters are enforced from 8 a.m. to midnight every day and names the Royal Regional Lot, about seven minutes\' walk.',
  [W('Tampa Theatre'),['National Register record',NR+'78000945'],['Theatre: Know Before You Go','https://tampatheatre.org/?p=187']],
  hours='Box office weekdays from 10 a.m.; evenings and weekends from 30 minutes before the first show',
  brick='?', arch='John Eberson', archw='Wikipedia and the National Register record: designed by John Eberson'),

N('tampa-union-station','Tampa Union Station','Tampa','fl','rail','standing',27.95267,-82.45055,'exact','open','walk','stations','1912',
  'Opened on May 15, 1912, to serve three railroads, the Atlantic Coast Line, the Seaboard Air Line and the Tampa Northern, and designed by Joseph F. Leitner. The waiting room was divided by a wall under segregation. The station closed in 1984 and reopened in 1998 after a restoration; Amtrak trains still use it.',
  'An Italian Renaissance Revival station of reddish-brown tapestry brick, with light stone and terra cotta for the cornice, quoins and the Corinthian columns at the two entrances (Great American Stations). Poured-concrete track bumpers from the old tracks remain, beside planters cast with "TUS" (Wikipedia).',
  'A 1912 brick depot where the trains still stop.',
  'Amtrak station, 601 North Nebraska Avenue. The station\'s own page gives its hours and says a little free parking is at the station, with paid parking in the City of Tampa\'s Twiggs Street Garage nearby (page read November 2026).',
  [W('Tampa Union Station'),['National Register record',NR+'74000640'],['Tampa Union Station: train service','https://tampaunionstation.com/train-service/'],['Great American Stations','https://www.greatamericanstations.com/stations/tampa-fl-tpa/']],
  hours='Daily 9:45 a.m. to 6 p.m.', brick='yes', bcol='red',
  arch='Joseph F. Leitner', builder='W. C. Hobbs Company', archw='Wikipedia: "designed by Joseph F. Leitner"; the National Register record names J. F. Leitner and the W. C. Hobbs Co.'),

N('old-hillsborough-county-high-school','Old Hillsborough County High School','Tampa','fl','civic','standing',27.96806,-82.46306,'site','view','walk','','1911',
  'Built in Tampa Heights in 1911 for about $60,000, when it was the county\'s only high school, and designed by William Potter; the Register form says it went up in two phases, 1911 and 1923. Hillsborough High moved out in 1928, Jefferson High School began here in 1939, and later George Washington Junior High used it until 1979. Restored in 2003, it is now the D. W. Waters Career Center of the county schools.',
  'Red brick walls laid in English bond, with a classical entablature at the parapet, Palladian windows over the side porticoes, and a yellow brick water table over a basement whose brick imitates rusticated stone (Register form). Brick streets surround the block. Interior not checked.',
  'Tampa\'s 1911 high school, still a school.',
  'Hillsborough County Public Schools, 2704 North Highland Avenue. A working school: seen from the surrounding streets only.',
  [W('D. W. Waters Career Center'),['National Register record',NR+'07000423']],
  brick='yes', bcol='red', stone='HILLSBOROUGH COUNTY HIGH SCHOOL ERECTED 1911', stonew='Photograph of the cornerstone on Wikimedia Commons: https://commons.wikimedia.org/wiki/File:Tampa_FL_Hillsborough_Cty_High_stone01a.jpg', arch='William Potter', archw='Wikipedia: "Architect William Potter designed the three-story masonry block building"'),

N('masonic-temple-no-25-tampa','Masonic Temple No. 25','Tampa','fl','civic','standing',27.94861,-82.45571,'exact','view','walk','','1927–1929',
  'The fourth lodge building of Hillsborough Lodge No. 25, Free and Accepted Masons, designed by M. Leo Elliott after three medieval Italian cathedrals. Wikipedia says it was erected in 1927, the cornerstone was laid on June 18, 1928, and the first lodge meeting was held in it on February 19, 1929. It was listed on the National Register in 1986.',
  'Terra cotta trim on the entrances (Register form). Wikipedia says the lodge room has a hand-painted ceiling 40 feet high; the lodge lets three shopfronts on the ground floor. Interior not checked.',
  'A Masonic temple modelled on Italian cathedrals.',
  'Hillsborough Lodge No. 25, 508 East Kennedy Boulevard at Morgan Street. A private lodge: seen from the street. Metered street parking and private lots downtown.',
  [W('Masonic Temple No. 25'),['National Register record',NR+'86002415']],
  brick='?', arch='M. Leo Elliott', archw='Wikipedia and the National Register record: designed by M. Leo Elliott'),

N('lafayette-street-bridge-tampa','Lafayette Street Bridge (Kennedy Boulevard Bridge)','Tampa','fl','landmark','standing',27.94667,-82.46111,'site','public','walk','','1913',
  'Built in 1913 across the Hillsborough River, linking downtown with the Tampa Bay Hotel side; the Register form names the Oswego Bridge Company as designer and the Edwards Construction Company as builder. Its middle span is the original skewed double-leaf Scherzer bascule, about 80 feet wide and 120 feet long, still working. In 1995 the concrete arch approach spans were taken down and rebuilt to follow the original plans.',
  'The 1913 bascule span with walkways of perforated steel panels, a small tender\'s house with a Spanish tile roof at each end of it (the eastern one carries a large bronze plaque), and rebuilt concrete arches with neoclassical balustrades. The Tampa Bay Hotel\'s minarets rise at the west end.',
  'A working 1913 drawbridge in front of Plant\'s minarets.',
  'Carries Kennedy Boulevard, a public highway, with sidewalks on both sides (the Florida Department of Transportation carried out its 1995 rehabilitation, says the Register form); the Tampa Riverwalk passes the east end. Metered street parking and private lots downtown.',
  [['National Register record',NR+'100002094']],
  brick='no', arch='Oswego Bridge Company', builder='Edwards Construction Company', archw='National Register form: "Oswego Bridge Company, Designer"; the record lists the Edwards Construction Company and the Oswego Bridge Company'),

N('ybor-city-historic-district','Ybor City Historic District','Tampa','fl','town','standing',27.9625,-82.44111,'area','public','walk','','1880s–1930s',
  'The cigar-making town founded in the 1880s by Vicente Martinez Ybor and other manufacturers, and peopled by thousands of immigrants from Cuba, Spain and Italy. For about fifty years its factories rolled hundreds of millions of cigars a year and gave Tampa the name Cigar City; the Depression and machines emptied it, and by the late 1970s much of it was abandoned. Artists began to bring it back in the 1980s, and the streets round 7th Avenue are now a nightlife district. It was listed on the National Register in 1974 and became a National Historic Landmark District in 1990.',
  'Brick cigar factories, the clubhouses of the mutual aid societies (El Centro Español and El Círculo Cubano are entered on their own), and the Ybor City Museum State Park in the old Ferlita bakery, whose brick bread oven survived a fire in 1922 (Wikipedia).',
  'Cigar City: the factories and immigrant clubs that built Tampa.',
  'The district\'s buildings are seen from the public streets of the City of Tampa; most are privately owned. The pin is the Register\'s point for the district, which covers many blocks round 7th Avenue. Street parking and lots throughout Ybor City.',
  [W('Ybor City'),['National Register record',NR+'74000641'],W('Ybor City Museum State Park')],
  brick='?'),

N('first-baptist-church-tampa','First Baptist Church of Tampa','Tampa','fl','worship','standing',27.94554,-82.46308,'exact','open','walk','','1924',
  'The congregation began in downtown Tampa on July 23, 1859. After the Lafayette Street Bridge was built and members began building houses in Hyde Park, it moved in 1896 to the corner of Lafayette Street (now Kennedy Boulevard) and Hyde Park Avenue, and the present Classical Revival sanctuary was dedicated in 1924.',
  'A Classical Revival sanctuary of buff brick with a gilded dome (a photograph on Wikimedia Commons shows the brick and dome), and the congregation\'s later chapel and buildings round it (AIA Tampa Bay\'s architecture tour). Interior not checked.',
  'A domed 1924 Baptist church on Kennedy Boulevard.',
  'First Baptist Church of Tampa, 302 West Kennedy Boulevard. The church\'s visitors\' page names guest parking off Hyde Park Avenue just west of the main building, a south lot across Grand Central Avenue, and free street parking on Sunday mornings until 2 p.m.',
  [['AIA Tampa Bay: First Baptist Church','https://tourtampabayarchitecture.com/?p=668'],['Church: new here','https://fbctampa.org/new-here/']],
  hours='Sunday worship 10:45 a.m.', brick='no', bcol='buff'),
]

PIN_NOTES={
 'sacred-heart-church-tampa':'OpenStreetMap point for the church on North Florida Avenue, a few metres from the Wikipedia coordinate.',
 'tampa-city-hall-1915':'Address lookup of 315 East Kennedy Boulevard.',
 'us-courthouse-tampa-1905':'OpenStreetMap point for the Le Méridien hotel at 601 North Florida Avenue, within 30 m of the Wikipedia coordinate.',
 'circulo-cubano-tampa':'OpenStreetMap point for the Círculo Cubano events hall, Palm Avenue at 14th Street.',
 'centro-espanol-de-tampa':'OpenStreetMap historic building "El Centro Español", East 7th Avenue.',
 'tampa-theatre':'OpenStreetMap point for the theatre at 711 North Franklin Street.',
 'tampa-union-station':'OpenStreetMap building for the station at 601 North Nebraska Avenue.',
 'old-hillsborough-county-high-school':'Wikipedia and Register list coordinate; the building fills a whole block, so the pin marks the site.',
 'masonic-temple-no-25-tampa':'Address lookup of 508 East Kennedy Boulevard.',
 'lafayette-street-bridge-tampa':'Register list coordinate on the bridge over the Hillsborough River.',
 'ybor-city-historic-district':'Register list coordinate for the district; on the aerial it falls on a green strip among the district\'s streets. The district covers many blocks, so the pin marks the area only.',
 'first-baptist-church-tampa':'OpenStreetMap point for the church at 302 West Kennedy Boulevard.',
}
