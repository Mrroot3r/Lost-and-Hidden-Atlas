# November 24, 2026: Peoria, Illinois, and the old state hospital in Bartonville next to it, from the names in one
# walk-through video of the city's old buildings. The video was only a list of names to look up; every fact here
# comes from a source opened while writing: Wikipedia read as raw text, Clio, Cinema Treasures, Peoria Magazine,
# Peoria Public Radio and the City of Peoria's own pages.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
DT='Downtown Peoria: street parking and paid lots and garages nearby; which lot is closest was not checked. '

BATCH={'key':'peoria_rgld','label':'Peoria, Illinois','added':'2026-11-24 08:36'}

PLACES=[
N('madison-theatre-peoria','Madison Theatre','Peoria','il','civic','standing',40.69436,-89.59149,'exact','view','walk','','1920',
  'A movie and vaudeville palace built for the local businessman Dee Robinson and designed by Frederic J. Klein, who later drew the Coronado Theatre in Rockford. It opened on October 16, 1920, switched to sound films by the late 1920s, and was the last big movie palace built in Peoria. It closed as a cinema in 1983, came back as a concert hall from 1996 to 2002 and shut in 2003. A fire in June 2016 badly damaged it and the city filed to condemn it, but repairs saved it. In July 2026 the city approved a plan by developers to rebuild the storefronts at 500 to 516 Main Street, which are part of the theatre building, as a step toward reopening the theatre itself, still dormant.',
  'A pale Italian Renaissance front of terra-cotta work, with red brick walls behind it, and a triple-arched window over the marquee, the name cut into the facade. Inside, which the public cannot see now, the auditorium and lobby have domed ceilings with classical plasterwork. It has been closed since 2003; look from Main Street and Madison Avenue.',
  'Peoria\'s last movie palace, dark since 2003.',
  'Closed; owner not checked. Look from the sidewalk. 502 Main Street, at the corner of Madison Avenue (Cinema Treasures gives the address as 107 NE Madison Avenue). '+DT,
  [L('Clio: Madison Theater','https://theclio.com/entry/81344'),L('Cinema Treasures: Madison Theatre','https://cinematreasures.org/theater/2647'),L('Peoria Public Radio, July 2026: Main Street storefronts','https://www.wcbu.org/local-news/2026-07-29/peoria-greenlights-7-3m-renovation-of-main-street-storefronts-agrees-to-sell-nearby-parking-lot-to-developers')],
  brick='some',hours=''),

N('commerce-bank-building-peoria','Commerce Bank Building (Peoria Life Building)','Peoria','il','civic','standing',40.69328,-89.59065,'exact','view','walk','','1918–1920',
  'A 17-story neoclassical office tower built for the Peoria Life Insurance Company on the site of Rouse\'s Opera Hall, to a design by the Peoria firm Hewitt & Emerson. Work began in the spring of 1918, stopped for about four months during the First World War and ended in 1920. At 256 feet, or 302 with its lantern, it was the tallest building in Peoria until 1984. It was renovated in 2022 and lies in the Downtown Peoria Historic District, listed on the National Register in 2018.',
  'Look up: the top is crowned by a lantern. It is an office building; interior not checked.',
  '',
  'Private office building at 416 Main Street; look from the street. '+DT,
  [W('Commerce Bank Building (Peoria, Illinois)'),W('Downtown Peoria Historic District')],
  brick='?',hours=''),

N('central-national-bank-building-peoria','Central National Bank Building','Peoria','il','civic','standing',40.69188,-89.58999,'exact','view','walk','','1913–1914',
  'A ten-story bank and office building, also called the Central Building, designed by the Chicago office of Daniel Burnham in 1913 and 1914; Burnham himself had died two years before it was finished. It was listed on the National Register in 1978.',
  'A Renaissance Revival front: pilasters between the windows of the first two floors, spandrels over the ground-floor windows and terra-cotta cornice lines above the second and third floors. Interior not checked.',
  '',
  'Private building at 103 SW Adams Street; look from the street. '+DT,
  [W('Central National Bank Building (Peoria, Illinois)')],
  brick='?',hours=''),

N('peoria-city-hall','Peoria City Hall','Peoria','il','civic','standing',40.69257,-89.59301,'exact','open','walk','','1897–1899',
  'Built in 1897 for $271,500 to a design by Reeves and Baillee and dedicated in January 1899, it is still the city hall. The Flemish Renaissance building was planned so that any of its four sides could serve as the front, and its walls are red sandstone from the Lake Superior region. The cupola bell tower from the earlier city hall stands on top, with a 4,300-pound bell made in 1865.',
  'Inside are a marble staircase, iron railings, stained glass windows, a mural commissioned in 1912 of the muses of learning, peace and medicine, and in the front hall an 1889 statue, "Love Knows No Caste", by Fritz Triebel.',
  'A sandstone city hall with four fronts and the old hall\'s bell on top.',
  'City of Peoria, 419 Fulton Street. A working city hall: the public may come in on weekdays. Hours from the City Clerk\'s page, read November 2026. '+DT,
  [W('Peoria City Hall'),L('City of Peoria: City Clerk','https://www.peoriagov.org/158/City-Clerk')],
  brick='no',hours='Monday to Friday 8 a.m. to 5 p.m., except holidays'),

N('pere-marquette-hotel-peoria','Hotel Père Marquette (Peoria Marriott Pere Marquette)','Peoria','il','hotel','standing',40.69382,-89.5924,'exact','open','walk','','1926',
  'A 14-story hotel built in 1926, designed by the Philadelphia architect Horace Trumbauer with the Peoria architect Herbert Edmund Hewitt. It is the only one of Peoria\'s upscale 1920s hotels still standing; the Jefferson Hotel, built in 1910, was imploded in 1978 to make way for the Peoria Civic Center. It became the Peoria Hilton in 1972, closed in December 2011 for a rebuilding and reopened in June 2013 as a Marriott, and was renovated again in 2022. It was listed on the National Register in 1982.',
  'Brick and stone outside, with stone frames round the second-floor windows and a stone cornice carved with Native American and animal faces. The Cotillion Room, the old ballroom, has a high domed ceiling, French window mirrors and plasterwork; the lobby and the ballroom first had murals by George Matthews Harding. A working hotel: the lobby is open to guests and visitors.',
  '',
  'A working hotel at 501 Main Street, across Main Street from the Madison Theatre. '+DT,
  [W('Peoria Marriott Pere Marquette'),W('Peoria Civic Center')],
  brick='?',hours='?'),

N('ywca-building-peoria','YWCA Building','Peoria','il','civic','standing',40.69485,-89.5882,'exact','view','walk','','1928–1929',
  'Peoria\'s YWCA, founded in 1893, outgrew its first building and raised $350,000 in eight days to build this one, designed by Hewitt, Emerson & Gregg and dedicated on September 16, 1929. It held an auditorium, a swimming pool, a chapel, club rooms and rooms for 86 residents. The YWCA left in 2003, and since April 2008 the building has been New Hope Apartments, with 79 apartments, some built over the old pool and inside the two-story gymnasium. It was listed on the National Register in 2007.',
  'The building at the north corner of Jefferson Avenue and Fayette Street. It is housing: interior not open to visitors.',
  '',
  'Private apartment building at 301 NE Jefferson Avenue; look from the street. '+DT,
  [W('YWCA Building (Peoria, Illinois)')],
  brick='?',hours=''),

N('gar-hall-peoria','Grand Army of the Republic Memorial Hall (Greenhut Memorial)','Peoria','il','civic','standing',40.69449,-89.58984,'exact','view','walk','','1909',
  'A hall for Civil War veterans built in 1909 for $22,000, two-thirds of it given by Joseph B. Greenhut, once captain of Company K, 82nd Illinois Volunteer Infantry, to whom it is dedicated. Hewitt & Emerson designed it in a Classical Revival and Beaux-Arts style. The Grand Army society had died out by the 1950s; the Central Illinois Landmarks Foundation bought and restored the hall in the 1970s and it was rededicated in 1979. It was listed on the National Register in 1976.',
  'Wikipedia lists portraits of Greenhut and his wife, a marble bust of General John Logan by the Peoria sculptor Fritz Triebel and other Civil War pieces inside. The hall is hired out for events, so the inside is seen only then; interior not checked.',
  '',
  'Owned by the Central Illinois Landmarks Foundation, 416 Hamilton Boulevard; let for events. Look from the street. '+DT,
  [W('Grand Army of the Republic Memorial Hall (Peoria, Illinois)')],
  brick='?',hours=''),

N('us-post-office-courthouse-peoria','U.S. Post Office and Courthouse','Peoria','il','civic','standing',40.6949,-89.59174,'exact','view','walk','','1937–1938',
  'A federal courthouse and, until 1981, Peoria\'s main post office, built in 1937 and 1938 in the PWA Moderne style. Louis A. Simon, the government\'s Supervising Architect, provided the plans and Howard Lovewell Cheney was architect of record. It is still the federal court for the Central District of Illinois and was listed on the National Register in 2012.',
  'Granite walls with limestone carving, including bas-relief panels by Freeman L. Schoolcraft over the Main Street door: a man of industry, a woman of agriculture, a Native American and a postal worker. Inside are painted ceilings, Ste. Genevieve marble walls and terrazzo floors; it is a working court with security, and the inside was not checked for visitors.',
  '',
  'Federal court building, 100 NE Monroe Street; look at the carved panels from the Main Street sidewalk. '+DT,
  [W('United States Post Office and Courthouse (Peoria, Illinois)')],
  brick='no',hours=''),

N('cumberland-presbyterian-church-peoria','Cumberland Presbyterian Church (Musicians Hall)','Peoria','il','worship','standing',40.69258,-89.59606,'exact','view','walk','','1856',
  'Built in 1856 for the First Cumberland Presbyterian Church, it is the oldest church building standing in Peoria. It passed to St. John\'s Episcopal Church in 1863, the First German Baptist Church in 1875 and the Agudas Achim congregation in 1897, and was briefly a YMCA training school for Black youth in 1911. The musicians\' union, Local 26, bought it in 1913. It was listed on the National Register in 1980 and is now a branch of Busey Bank.',
  'A small church building used as a bank branch; interior not checked.',
  '',
  'A bank branch; look from the street. '+DT,
  [W('Cumberland Presbyterian Church (Peoria, Illinois)')],
  brick='?',hours=''),

N('westlake-bradley-halls-peoria','Bradley Hall and Westlake (Horology) Hall, Bradley University','Peoria','il','inst','standing',40.69777,-89.61704,'site','view','walk','','1897',
  'Lydia Moss Bradley founded Bradley Polytechnic Institute in 1897, in memory of her husband and six children. Classes began in Bradley Hall on October 4, 1897, with builders still at work. Beside it Horology Hall, of Bedford stone and designed by Henry Ives Cobb, was dedicated on November 19, 1897 as the first building in the country put up only for a watchmaking school; it was renamed Westlake Hall in 1946 after the department\'s founding dean. Wikipedia calls Westlake the oldest building on the campus, while Peoria Magazine calls it the second oldest. A renovation and enlargement of Westlake Hall, due to finish in summer 2012, gave its clock tower a new face with Roman numerals like the first one.',
  'Two pale stone buildings of 1897 on the university campus: Bradley Hall with its battlemented tower, and Westlake Hall with the clock tower and a red roof. Both are in use for teaching; interior not checked.',
  'America\'s first purpose-built watchmaking school.',
  'Bradley University, a private university; the halls are seen from the campus walks. The pin is between the two halls. University lots are marked for faculty, commuters and visitors; which a visitor may use was not checked.',
  [W('Bradley University'),L('Peoria Magazine, April 2012: Bradley University and its watchmaking past','https://ww2.peoriamagazines.com/node/7998')],
  brick='no',hours=''),

N('flanagan-house-peoria','Judge John C. Flanagan House','Peoria','il','landmark','standing',40.70452,-89.5855,'exact','open','walk','','1837',
  'Built in 1837 for John C. Flanagan, a Philadelphian who came to Peoria in 1831, it is the oldest house still standing in Peoria. It was built of local walnut, locally made brick and Kickapoo Valley limestone, with lumber, lime and glass from Chicago, on the East Bluff above the Illinois River, and locals called it the Mansion on the Hill. The Peoria Historical Society bought it in 1962 and runs it as a house museum. It was listed on the National Register in 1975.',
  'A Federal-style brick house with Italianate touches and ornamental ironwork shipped from France in 1852, furnished as a 19th-century house museum.',
  'Peoria\'s oldest house, a museum on the bluff.',
  'Peoria Historical Society, 942 NE Glen Oak Avenue. Shown by tour; the Society\'s page could not be opened when this was written, so hours not checked.',
  [W('John C. Flanagan House Museum'),L('Peoria Historical Society: house museums','https://www.peoriahistoricalsociety.com/houses')],
  brick='?',hours='?'),

N('pettengill-morron-house-peoria','Pettengill–Morron House','Peoria','il','landmark','standing',40.694,-89.61186,'exact','open','walk','','1868',
  'Moses Pettengill, a hardware merchant who came from New Hampshire in 1833, had lived downtown from 1836 to 1862 in a house used on the Underground Railroad; that house was torn down in 1910 for the Jefferson Hotel. His new house on Moss Avenue burned in 1865, and this brick Second Empire house replaced it in 1868 for $12,000; a Colonial Revival porch and porte-cochere were added in 1900. Jean Morron lived here until 1966, and the Peoria Historical Society has run it as a museum since 1967. It was listed on the National Register in 1976.',
  'A Second Empire brick house in the Moss-High historic district. The collection includes the family\'s restored paintings and Blanchard Pettengill\'s diary of growing up here.',
  '',
  'Peoria Historical Society, 1212 W Moss Avenue. Shown by tour; the Society\'s page could not be opened when this was written, so hours not checked.',
  [W('Pettengill–Morron House'),L('Peoria Historical Society: house museums','https://www.peoriahistoricalsociety.com/houses')],
  brick='?',hours='?'),

N('peoria-state-hospital-bartonville','Peoria State Hospital','Bartonville','il','inst','standing',40.63881,-89.66167,'area','view','drive','','1895–1973',
  'Built as the Illinois Asylum for the Incurable Insane. Work began in 1895 and the main building, on the Kirkbride plan, was finished in 1897 but never used: Wikipedia says abandoned mine shafts under it made it unsafe, and adds that the hospital\'s own 1927 history gives another reason. Under Dr. George Zeller it reopened in 1902 as a cottage-plan hospital of 33 buildings, and the state ran it until 1973. It grew to 63 buildings; after closing most were sold, many torn down and others turned to business use. The Bowen Building, the nurses\' and administration building, was demolished in 2016, and 12 of the 63 buildings stood in July 2019. The grounds are listed on the National Register as a historic district.',
  'A dozen surviving hospital buildings scattered over the old grounds, all in use by businesses. News reports describe a Peoria State Hospital Museum on Pfeiffer Road that gives history and ghost tours, including the old cemeteries; its own page was not found, so this was not checked.',
  'The asylum that could not use its own first building.',
  'The surviving buildings are privately owned and occupied; look from the public roads. The pin marks the middle of the old grounds as Wikipedia gives it.',
  [W('Peoria State Hospital')],
  brick='?',hours='?',conf='mixed'),
]

PIN_NOTES={
  'madison-theatre-peoria':'OpenStreetMap building for the Madison Theater, 502 Main Street.',
  'commerce-bank-building-peoria':'OpenStreetMap building, 416 Main Street.',
  'central-national-bank-building-peoria':'OpenStreetMap building for the Central Building, 101 SW Adams Street.',
  'peoria-city-hall':'OpenStreetMap town hall point, 419 Fulton Street.',
  'pere-marquette-hotel-peoria':'OpenStreetMap hotel point, 501 Main Street.',
  'ywca-building-peoria':'OpenStreetMap building for the Peoria YWCA Building, 301 NE Jefferson Avenue.',
  'gar-hall-peoria':'OpenStreetMap point for the Greenhut Memorial Grand Army of the Republic Hall, 416 Hamilton Boulevard.',
  'us-post-office-courthouse-peoria':'OpenStreetMap courthouse point, 100 NE Monroe Street.',
  'cumberland-presbyterian-church-peoria':'OpenStreetMap building for the Musicians Union Hall and Cumberland Presbyterian Church.',
  'westlake-bradley-halls-peoria':'Between the OpenStreetMap buildings for Bradley Hall and Westlake Hall.',
  'flanagan-house-peoria':'OpenStreetMap museum point, 942 NE Glen Oak Avenue.',
  'pettengill-morron-house-peoria':'Address point for 1212 W Moss Avenue, which matches the OpenStreetMap museum point.',
  'peoria-state-hospital-bartonville':'Wikipedia coordinate for the historic district, moved about 20 m onto the road through the old grounds, off a business building; the pin marks the grounds only.',
}
