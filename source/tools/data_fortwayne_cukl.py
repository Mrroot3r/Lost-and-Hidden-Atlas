# November 24, 2026: downtown Fort Wayne, Indiana, and two buildings just outside it. The names came from one
# video (a stranger's tip, never a source); every fact here is from a source opened while this batch was written:
# Wikipedia articles, National Register forms on NPGallery, the parishes' and museums' own pages, Indiana Landmarks.
from data_b import N
from data_ma import W

BATCH={'key':'fortwayne_cukl','label':'Fort Wayne, Indiana: courthouse, churches and old downtown','added':'2026-11-24 03:38'}

def NR(ref,label):
    return ['National Register form: '+label,'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/%s_text'%ref]

DT='Downtown Fort Wayne has metered street parking and many lots and garages; who may use each lot was not checked.'

PLACES=[
N('allen-county-courthouse-fort-wayne','Allen County Courthouse','Fort Wayne','in','civic','standing',41.07972,-85.13917,'exact','open','walk','','1897–1902',
  'Allen County\'s working courthouse, filling the block between Clinton, Calhoun, Main and Berry streets. Brentwood S. Tolan designed it in the Beaux-Arts style; the cornerstone was laid on November 17, 1897 and it was dedicated on September 23, 1902, at a cost of about $817,500. A seven-year restoration costing $8.6 million ended with its re-dedication on its hundredth birthday in 2002. It is a National Historic Landmark (2003).',
  'Bedford limestone and Vermont granite outside, with Italian marble details. Over the rotunda rises a copper-clad dome 255 feet high, topped by a 14-foot wind vane in the form of Lady Liberty. Inside, by Wikipedia: four large murals by Charles Holloway, some 15,000 square feet of scagliola in 28 kinds, bas-reliefs and art glass, and five courtrooms each in its own colour scheme. A tunnel joins it to the City-County Building across the street.',
  'A working courthouse with a 255-foot copper dome and walls of painted scagliola.',
  'Owned by Allen County and in daily use as a court. The courthouse\'s own site (allencountycourthouse.org, which could not be opened when this was written; its hours are as a web search quoted it) gives the building open on weekdays for self-guided walks with a free guide booklet, and docent tours of about an hour on weekdays by arrangement, with a $5 donation suggested; phones and cameras are not allowed during business hours. '+DT,
  [W('Allen County Courthouse (Indiana)'),['Allen County Courthouse: tours','https://allencountycourthouse.org/?p=17']],
  brick='no',hours='Monday to Friday 8 a.m. to 4:30 p.m. (tours by arrangement, weekdays 9 a.m. to 4 p.m.)'),

N('old-city-hall-fort-wayne','Old City Hall (The History Center)','Fort Wayne','in','civic','standing',41.07948,-85.1363,'exact','open','walk','','1893–1971',
  'Fort Wayne\'s city hall from 1893 until 1971, when the city moved to the City-County Building. Wing & Mahurin designed it in the Richardsonian Romanesque style. Since 1980 it has been the History Center, the museum and headquarters of the Allen County–Fort Wayne Historical Society, and it was listed on the National Register in 1973.',
  'Built of large sandstone blocks, which the Register form of 1973 says had changed outwardly only by cleaning since it opened. The museum shows the region\'s history from the Ice Age on, including Miami chiefs Little Turtle and Richardville and the founding of the fort in 1794; the small city jail in the building, used from 1893 to 1971 mostly as a holding cell for those awaiting trial, is part of the museum (Wikipedia).',
  'A sandstone city hall with its old jail, now the county\'s history museum.',
  'Owned and run by the Allen County–Fort Wayne Historical Society, at 302 East Berry Street. Its own site (fwhistorycenter.org) could not be opened when this was written; the hours and fees are as a web search quoted that site: adults $7, seniors and youth $5, under-3s free. '+DT,
  [W('Fort Wayne Old City Hall Building'),NR('73000027','Fort Wayne City Hall'),['The History Center','https://fwhistorycenter.org/']],
  brick='no',hours='Monday to Friday 10 a.m. to 5 p.m.; Saturday 9 a.m. to 5 p.m.; first Sunday of the month noon to 5 p.m.'),

N('cathedral-immaculate-conception-fort-wayne','Cathedral of the Immaculate Conception','Fort Wayne','in','worship','standing',41.0757,-85.13783,'exact','open','walk','','1859–1860',
  'The cathedral of the Catholic Diocese of Fort Wayne–South Bend. Its parish began in 1836 with St. Augustine\'s, a log church of 1839 on land bought from the Miami chief Jean-Baptiste de Richardville; St. Augustine\'s, made a cathedral in 1857, burned in 1859. The present Gothic Revival cathedral was built on the same ground, partly over the old cemetery, and dedicated in 1860. Listed on the National Register in 1980.',
  'Two bell towers topped by spires rise about 200 feet; the front is faced with Indiana limestone and Lannon stone from Wisconsin. Wikipedia names wood-carved Stations of the Cross brought from Germany. Around it, Cathedral Square holds the chancery, MacDougal Chapel, the old Cathedral Boys School, the rectory and the grave of Chief Richardville. Interior beyond that not checked.',
  'A cathedral built in 1860 on the site of a log church bought from a Miami chief.',
  'An active Catholic parish at 1105 South Calhoun Street; the business office is at 1102 South Clinton Street. Times from the parish\'s own page; weekday Mass at 8 a.m. is in the chapel. '+DT,
  [W('Cathedral of the Immaculate Conception (Fort Wayne, Indiana)'),['Cathedral parish: Mass times','https://cathedralfw.org/']],
  brick='no',hours='Mass Saturday 5 p.m.; Sunday 8:30 a.m., 11:30 a.m. and 5 p.m.; Monday to Friday 12:05 p.m.'),

N('st-pauls-lutheran-fort-wayne','St. Paul\'s Evangelical Lutheran Church','Fort Wayne','in','worship','standing',41.07559,-85.13591,'exact','open','walk','','1889; rebuilt 1903–1905',
  'Founded in 1837, the oldest Lutheran congregation in northern Indiana, with its churches on this one site since 1839. The present High Victorian Gothic church by Wing & Mahurin was finished in 1889; a fire on December 3, 1903 left it in ruins, and it was rebuilt by April 1905. Listed on the National Register in 1982.',
  'A Gothic Revival church at Barr and Madison streets, rebuilt after the 1903 fire. A 2012 photograph on Wikipedia shows red brick with pale stone trim, tall traceried windows and a slate-covered spire on the corner tower. Interior not checked.',
  'A Gothic church that burned in 1903 and was rebuilt in eighteen months.',
  'An active congregation of the Lutheran Church–Missouri Synod at 1126 Barr Street, with its school across the street. Service time from the congregation\'s own page. '+DT,
  [W('Saint Paul\'s Evangelical Lutheran Church (Fort Wayne, Indiana)'),['St. Paul\'s Lutheran Church','https://www.stpaulsfw.org/']],
  brick='yes',hours='Sunday 9:30 a.m. Divine Service'),

N('st-peters-church-fort-wayne','St. Peter\'s Catholic Church','Fort Wayne','in','worship','standing',41.06559,-85.13021,'exact','open','walk','','1892–1893',
  'The church of St. Peter\'s Square, a Catholic complex on the south side listed on the National Register in 1991: the Gothic Revival church (cornerstone 1893 by the Register form, 1892 by Wikipedia), the school of 1904 and 1914–15, a boiler house and the 1911 Suelzer house, now the rectory. Three more buildings that stood between church and school in the 1940s (the first church and school, the old rectory and the convent) have been demolished.',
  'Load-bearing brick walls on a rock-faced limestone base, with carved limestone trim, and a tower of four brick stages 120 feet high over the west door; its wooden and slate spire was replaced in 1967 with an open-work steel one. Inside, by the Register form: three altars of 1908 by the Hackner company of La Crosse, Wisconsin, the high altar with a reredos about 25 feet high, carved confessionals, and stained glass with circular tracery. The school\'s 1904 wing has a red brick cupola.',
  'A brick Gothic church with Hackner altars, on a square that has lost half its buildings.',
  'An active Catholic parish at 518 East Dewald Street. Times from the parish\'s own page; confessions on Saturdays 3 to 3:45 p.m. A mapped parking lot is on Dewald Street by the church; whether it is the parish\'s was not checked.',
  [W('St. Peter\'s Square (Fort Wayne, Indiana)'),NR('91000259','St. Peter\'s Square'),['St. Peter\'s Catholic Church','https://www.stpetersfortwayne.org/']],
  brick='some',hours='Mass Saturday 4 p.m.; Sunday 9 a.m.; Tuesday, Thursday and Friday 9 a.m.; Wednesday 5:30 p.m.',
  th=[41.06567,-85.12945],thn='Parking lot on East Dewald Street'),

N('engine-house-3-fort-wayne','Engine House No. 3 (Firefighters Museum)','Fort Wayne','in','civic','standing',41.07723,-85.14186,'exact','open','walk','','1893–1972',
  'A fire station on West Washington Boulevard by Wing & Mahurin, built in 1893 with two bays for six men, four horses and two wagons. In 1907 it was more than doubled with a two-storey wing and a bell tower, becoming the city\'s largest firehouse, and a rear wing followed in 1909. It closed in 1972, was nearly razed for a parking lot in 1974, and since 1975 has held the Fort Wayne Firefighters Museum, which has owned it since 1987.',
  'A two-storey red brick Romanesque Revival firehouse with arched bay doors and towers on the front. The Register form of 1979 says the 1907 bell tower over the main entrance had been removed by then. The museum shows the city\'s fire service from hand pumpers and steamers on, with equipment the department itself used.',
  'A red brick firehouse of 1893 that lost its bell tower and nearly lost the rest to a parking lot.',
  'Owned and run by the Fort Wayne Firefighters Museum, at 226 West Washington Boulevard. Its own page says it has had regular hours since 2001 but gives none; hours not checked. '+DT,
  [W('Engine House No. 3 (Fort Wayne, Indiana)'),NR('79003772','Engine House No. 3'),['Fort Wayne Firefighters Museum','https://www.fortwaynefiremuseum.com/']],
  brick='yes',hours='?'),

N('embassy-theatre-fort-wayne','Embassy Theatre and Indiana Hotel','Fort Wayne','in','civic','standing',41.07571,-85.13981,'exact','open','walk','','1926–1928',
  'A movie palace and hotel built together from 1926 to 1928 for Clyde Quimby; the theatre opened as the Emboyd and has been the Embassy since 1952. It reopened as a performing arts centre in 1975, the year it was listed on the National Register, and its organ was restored from 1976 to 1996. The seven-storey Indiana Hotel, attached on the west, had its lobby and mezzanine restored in 1995.',
  'A seven-storey brick and terra cotta front with a tower at each corner and Corinthian columns. The auditorium (2,471 seats) is 110 by 140 feet under a ceiling over 80 feet high with a 60-foot dome; the lobby has black and white marble, a grand marble staircase and a twenty-foot mirror, and the stage is flanked by the pipes of a Page theatre organ (Register form and Wikipedia).',
  'A 1928 movie palace with its Page organ and its own hotel.',
  'Run by the Embassy Theatre Foundation at 125 West Jefferson Boulevard. The inside is seen at its shows and events. The box office times are from the theatre\'s own pages as a web search quoted them, and the two pages disagree (closing at 5 p.m. on one and 6 p.m. on the other); it also opens two hours before each show. Tours are arranged through the theatre\'s office. '+DT,
  [W('Embassy Theatre (Fort Wayne)'),NR('75000041','Embassy Theater and Indiana Hotel'),['Embassy Theatre','https://www.fwembassytheatre.org/']],
  conf='mixed',brick='no',hours='Box office Monday to Friday 10 a.m. to 5 or 6 p.m., and two hours before each show'),

N('baker-street-station-fort-wayne','Pennsylvania Railroad Station (Baker Street Station)','Fort Wayne','in','rail','standing',41.07222,-85.14056,'exact','view','walk','stations','1914–1990',
  'The Pennsylvania Railroad\'s passenger station, opened on March 23, 1914 at a cost of $550,000 in the Arts and Crafts style. About 3,000 people a day passed through it in the Second World War, and Presidents from Harding to Eisenhower stopped here on whistle-stop tours. Amtrak\'s Broadway Limited and Capitol Limited called until November 1990, when the line was rerouted. Listed on the National Register in 1998.',
  'A two-storey station in semi-glazed buff brick, first trimmed in yellow terra cotta, on the raised track line, with a pedestrian tunnel that led to the platforms. The freight house beside it has been demolished. The concourse is now a banquet hall and events space and the wings are offices (Wikipedia).',
  'Where presidents stopped on whistle-stop tours, now a banquet hall.',
  'Privately run as an events venue and offices at 221 West Baker Street; seen from the street, and inside only at events. '+DT,
  [W('Fort Wayne station'),NR('98001056','Pennsylvania Railroad Station')],brick='no'),

N('lincoln-bank-tower-fort-wayne','Lincoln Bank Tower','Fort Wayne','in','civic','standing',41.07923,-85.1388,'exact','view','walk','','1929–1930',
  'An Art Deco skyscraper begun late in 1929 and opened on November 16, 1930 as the headquarters of Lincoln National Bank and Trust, a bank founded in 1905 as the German American National Bank and renamed in 1918. For decades it was the tallest building in Indiana. Its president meant it as a monument to the German immigrants of the Fort Wayne area.',
  'Steel faced with Indiana limestone and granite, with lead spandrel panels, a terra cotta crown and a slender observation tower and flagpole on top. Seven bronze panels at the entrance show scenes from the life of Abraham Lincoln; inside, by Wikipedia, a snack shop keeps its 1930 soda fountain, and the two-storey banking hall has Art Deco murals of the industries and the seasons and walls of bronze, travertine and green Vermont marble.',
  'Indiana\'s tallest building for decades, with its 1930 soda fountain.',
  'A private office building at Berry and Calhoun streets, across from the courthouse. Seen from the street; whether the public may go into the lobby was not checked. '+DT,
  [W('Lincoln Bank Tower')],brick='no'),

N('masonic-temple-fort-wayne','Masonic Temple','Fort Wayne','in','civic','standing',41.07725,-85.13676,'exact','view','walk','','1926',
  'A twelve-storey Masonic lodge building designed by Charles R. Weatherhogg and built in 1926. Listed on the National Register in 1991.',
  'A rectangular Classical Revival block on a steel frame faced with Indiana limestone; the front has four Ionic columns five storeys tall between the windows. Interior not checked.',
  'A twelve-storey temple with five-storey columns.',
  'At 216 East Washington Boulevard (OpenStreetMap); private. Seen from the street. '+DT,
  [W('Masonic Temple (Fort Wayne, Indiana)')],brick='no'),

N('electric-works-fort-wayne','Electric Works (General Electric works)','Fort Wayne','in','industry','standing',41.07112,-85.15057,'site','open','walk','','1883–2015',
  'A factory campus on Broadway built from 1883 for the Fort Wayne Jenney Electric Light Company. General Electric took it over in 1899 and within a decade had more than 1.3 million square feet here making alternators, dynamos, motors and transformers, and aircraft superchargers in the Second World War; in 1944 it employed about a third of the city\'s workers. GE closed it in 2015, and after a sale in 2017 the west campus was rebuilt as Electric Works, opened in 2023.',
  'Red brick buildings over concrete frames, most designed by Harris & Richards of Philadelphia, with big windows and open floors on massive columns. The west campus keeps eight buildings of 1907 to 1942, among them the GE Club of 1926 with its gymnasium and bowling alley. Inside are offices, a clinic, a high school and Union Street Market, a food hall (Indiana Landmarks).',
  'A General Electric works that once employed a third of the city, now a food hall and offices.',
  'Privately owned and run as a mixed-use campus on Broadway; Union Street Market and other parts are open to the public, but no hours were found on a page of whoever runs them. The rest of the 39-acre site is still being redeveloped. Where visitors park was not checked.',
  [['Indiana Landmarks: Electric Works','https://www.indianalandmarks.org/?p=103889'],
   ['National Trust: Electric Works','https://savingplaces.org/stories/development-puts-fort-waynes-historic-electric-works-in-new-light']],
  brick='yes',hours='?'),

N('north-side-high-school-fort-wayne','North Side High School','Fort Wayne','in','civic','standing',41.09718,-85.13548,'site','view','drive','','1927',
  'A public high school designed by Charles R. Weatherhogg and opened in 1927. Its gymnasium was home to the Fort Wayne General Electrics basketball team from 1936 and to the Fort Wayne Zollner Pistons, now the Detroit Pistons, from 1941 until 1952; games were played there until 2004, when the school was renovated and the old gym was made into its library.',
  'The school as rebuilt in the 2000s; what of the 1927 building survives inside was not checked.',
  'Where the Pistons played before they left Fort Wayne.',
  'A working public school of Fort Wayne Community Schools; seen from the street, not open to visitors. Street parking nearby; the school lots are for the school.',
  [W('North Side High School (Fort Wayne, Indiana)')],brick='?'),
]

PIN_NOTES={
 'allen-county-courthouse-fort-wayne':'Wikipedia coordinate, on the courthouse block.',
 'old-city-hall-fort-wayne':'Wikipedia coordinate.',
 'cathedral-immaculate-conception-fort-wayne':'Wikipedia coordinate.',
 'st-pauls-lutheran-fort-wayne':'OpenStreetMap point for the church at 1126 Barr Street.',
 'st-peters-church-fort-wayne':'Wikipedia coordinate for St. Peter\'s Square fell on the parking lot east of the church; moved about 60 m west onto the church, seen on the aerial.',
 'engine-house-3-fort-wayne':'Wikipedia coordinate, moved about 15 m west onto the firehouse roof seen on the aerial.',
 'embassy-theatre-fort-wayne':'OpenStreetMap point for the theatre at 125 West Jefferson Boulevard.',
 'baker-street-station-fort-wayne':'Wikipedia coordinate.',
 'lincoln-bank-tower-fort-wayne':'Wikipedia coordinate.',
 'masonic-temple-fort-wayne':'OpenStreetMap point at 216 East Washington Boulevard; the National Register list gives a point about 1 km west, which was not used.',
 'electric-works-fort-wayne':'OpenStreetMap area for Union Street Market, on the west campus; the pin marks the campus.',
 'north-side-high-school-fort-wayne':'Wikipedia coordinate; the pin marks the school grounds.',
}
