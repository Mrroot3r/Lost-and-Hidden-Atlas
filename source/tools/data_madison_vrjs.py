# November 28, 2026: Madison, Wisconsin. Thirteen standing buildings in the city, mostly on the old University of
# Wisconsin campus, taken as leads from the names in one walk-through video and then each checked in sources opened
# for this batch: Wikipedia read as raw text (the Bascom Hill article and the Madison Register list among them), the
# Park Service's National Register records and the Register forms for the Orpheum, the Masonic Temple and the Garver
# factory, and the pages of the Wisconsin Union, the Wisconsin Historical Society, Garver Feed Mill, the UW School of
# Music and UW news. Nothing in an entry comes from the video.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]

BATCH={'key':'madison_vrjs','label':'Madison, Wisconsin: the old campus, theatres and a sugar factory','added':'2026-11-28 15:34'}

NR_LIST=W('National Register of Historic Places listings in Madison, Wisconsin')
BH=W('Bascom Hill')
def NR(n,label): return L('National Register record: '+label,'https://npgallery.nps.gov/AssetDetail/NRIS/'+n)

PLACES=[
N('bascom-hall-madison','Bascom Hall','Madison','wi','civic','standing',43.07537,-89.40436,'exact','view','walk','','1857–1859',
  "The University of Wisconsin's third building and its first given wholly to teaching, designed by William Tinsley of Indianapolis and built from 1857 to 1859 at the top of Bascom Hill. It was first called Main Hall or University Hall; a new portico went on in 1894, wings followed in 1899, 1907 and 1926, and it took John Bascom's name in 1920. Its dome burned on October 10, 1916 and was never rebuilt.",
  look="A long Italian Renaissance Revival hall with a columned portico facing down the hill toward the Capitol, and a seated statue of Abraham Lincoln in front, added in 1909. There has been no dome since the 1916 fire. It is the campus's main administration building; interior not checked.",
  accn="University of Wisconsin–Madison building at 500 Lincoln Drive, at the head of Bascom Hill: the hill and the outside are open ground on the campus. Part of the Bascom Hill Historic District.",
  links=[BH,NR('74000065','Bascom Hill Historic District')],brick='?',hours='',arch='William Tinsley',archw='Wikipedia, Bascom Hill'),
N('uw-music-hall-madison','Music Hall (Assembly Hall), University of Wisconsin','Madison','wi','civic','standing',43.07462,-89.40138,'exact','view','walk','','1879',
  "Built in 1879 to a design by Madison architect David R. Jones as the university's Assembly Hall, a room big enough for the whole student body, with the library in the same building; it was soon renamed Library Hall. The music department moved in around 1900 and the name became Music Hall. Robert La Follette, John F. Kennedy and Frank Lloyd Wright spoke in its auditorium, and the university's opera department still stages operas there.",
  look="Gothic Revival in Madison sandstone trimmed with darker Superior brownstone: a big square clock tower on the corner, buttresses and pinnacles, and pointed windows of stained glass made by George A. Misch of Chicago. Interior not checked.",
  accn="University building at the foot of Bascom Hill (925 Lathrop Drive on the map): seen from the campus walks. Part of the Bascom Hill Historic District.",
  links=[BH,NR('74000065','Bascom Hill Historic District')],brick='no',hours='',arch='David R. Jones',archw='Wikipedia, Bascom Hill'),
N('uw-science-hall-madison','Science Hall, University of Wisconsin','Madison','wi','civic','standing',43.07588,-89.40106,'exact','view','walk','','1885–1888',
  "Built from 1885 to 1888 on the site of the first Science Hall, which burned in December 1884. Henry C. Koch of Milwaukee designed it; Allan Conover, a professor of civil engineering who was made contractor, replaced the wooden frame with steel and hollow clay tile against fire, making it one of the first steel-framed buildings in the country. It is a National Historic Landmark for the geologist Charles Van Hise, who worked there and later led the university.",
  look="A U-shaped Romanesque Revival block of red brick over rough rhyolite, with a five-storey tower over the main door on Park Street, corner towers and a crowd of corbelled brick chimneys. Interior not checked.",
  accn="University building at 550 North Park Street: seen from the street and the campus walks.",
  links=[W('University of Wisconsin Science Hall'),BH,NR('93001616','University of Wisconsin Science Hall')],brick='yes',hours='',arch='Henry C. Koch',builder='Allan D. Conover',archw='Wikipedia, University of Wisconsin Science Hall and Bascom Hill'),
N('uw-red-gym-madison','Armory and Gymnasium (the Red Gym)','Madison','wi','fort','standing',43.07632,-89.39849,'exact','view','walk','','1892–1894',
  "A combined armory for military drill and a university gymnasium, designed by Allan Conover and Lew F. Porter and built from fall 1892 to September 1894 after the old wooden drill hall burned in 1891. In 1904 the state Republican convention met here and Robert La Follette's Progressives took control of the party, which made the building a National Historic Landmark. It was twice slated for demolition and kept; an anti-war firebomb in 1970 did severe damage that was repaired.",
  look="A Romanesque Revival castle of red brick on the Lake Mendota shore, with massive walls, small windows and battlements. It now holds student-service offices; interior not checked.",
  accn="University building at 716 Langdon Street, next to Memorial Union: seen from Langdon Street, Library Mall and the lakeshore path.",
  links=[W('University of Wisconsin Armory and Gymnasium'),BH,NR('93001618','University of Wisconsin Armory and Gymnasium')],brick='yes',hours='',arch='Allan D. Conover; Lew F. Porter',builder='T. C. McCarthy',archw='Wikipedia, University of Wisconsin Armory and Gymnasium'),
N('wisconsin-historical-society-headquarters-madison','Wisconsin Historical Society Headquarters','Madison','wi','civic','standing',43.07541,-89.40007,'exact','open','walk','','1896–1900',
  "Built from 1896 to 1900 to a design by Ferry & Clas of Milwaukee as a shared library for the State Historical Society, whose collections had been crowded into the Capitol, and the university. The university library moved out across the square in 1952 and the Society took the whole building.",
  look="Neoclassical, faced in Bedford limestone, with a broad Ionic colonnaded portico on Library Mall. Inside are mosaic floors, marble stairs and the large reading room on the second floor, where anyone may use the books.",
  accn="The Society's headquarters at 816 State Street, on Library Mall. The library is free and open to the public; the archives ask researchers to register with a photo ID. No parking of its own; city buses stop a block away. Hours from the Society's library page, which said hours were adjusted for its new history centre project until 2027 and to call before visiting.",
  links=[W('Wisconsin Historical Society'),BH,L('Wisconsin Historical Society: the library','https://www.wisconsinhistory.org/Records/Article/CS68'),NR('72000049','State Historical Society of Wisconsin')],brick='no',hours='Library: Mon to Wed 8 a.m. to 5 p.m., Thu 8 a.m. to 7 p.m., Fri 8 a.m. to 5 p.m., Sat 9 a.m. to 4 p.m.; closed Sundays',arch='Ferry & Clas',archw='Wikipedia, Bascom Hill; National Register list'),
N('uw-memorial-union-madison','Memorial Union','Madison','wi','civic','standing',43.07652,-89.40030,'exact','open','walk','','1926–1928',
  "The university's student union, built 1926 to 1928 and opened in October 1928 as the campus's \"living room\". Arthur Peabody's office designed the Italian Renaissance Revival main wing to match the oldest campus buildings; Leon Pescheret designed the interior and Eugene Hausler painted the Rathskeller murals. A theatre wing followed later, and the building was renovated in stages after a 2006 vote. It was listed on the National Register in 2015.",
  look="Bedford limestone walls and a green tile roof, the Rathskeller beer hall with its murals, the Great Hall and lounges, and the stone Terrace on Lake Mendota designed by Peabody's daughter Charlotte, with its sunburst chairs and summer music.",
  accn="Run by the Wisconsin Union at 800 Langdon Street. The union says it welcomes the Madison community as well as students and staff, and it has a campus visitor desk on the first floor. Building hours from the union's own page, for January 19 to December 1, 2026; it gives holiday changes there.",
  links=[W('Memorial Union (University of Wisconsin–Madison)'),BH,L('Wisconsin Union: Memorial Union','https://union.wisc.edu/visit/memorial-union/'),NR('15000255','University of Wisconsin Memorial Union')],brick='no',hours='Mon to Thu 7 a.m. to 11 p.m., Fri 7 a.m. to midnight, Sat 8 a.m. to midnight, Sun 8 a.m. to 11 p.m.',arch='Arthur Peabody',archw='Wikipedia, Bascom Hill and Memorial Union'),
N('uw-carillon-tower-madison','Carillon Tower','Madison','wi','landmark','standing',43.07612,-89.40505,'exact','public','walk','','1934–1936',
  "A freestanding bell tower paid for by classes from 1917 on, who first wanted to rebuild Bascom Hall's burned dome with chimes in it. Warren Laird and Paul Cret designed the 85-foot sandstone tower. Wikipedia dates the tower 1934 and the dedication concert 1936; a 2017 university news story says the tower was finished nearly a year before its first 25 bells arrived in 1936. Wikipedia gives 56 bells today.",
  look="A square sandstone tower with a balustrade echoing Bascom Hall's. The bells ring on the hour, and a carillonneur plays recitals; the 2017 news story said the inside of the tower was not open to the public.",
  accn="Owned by the University of Wisconsin–Madison, at 1160 Observatory Drive northwest of Bascom Hall, on open campus ground. Listen from Observatory Drive across from Bascom Hall, as the university suggests. Recital times from the School of Music's event listings (December 2025).",
  links=[BH,L('UW news: Music returns to the carillon (2017)','https://news.wisc.edu/music-returns-to-the-carillon-with-sunday-concerts/'),L('UW School of Music: Memorial Carillon recital','https://music.wisc.edu/?p=24480')],conf='mixed',brick='no',hours='Recitals some Sundays at 3 p.m.; check the School of Music calendar',arch='Warren Powers Laird; Paul Cret',archw='Wikipedia, Bascom Hill'),
N('uw-agriculture-hall-madison','Agriculture Hall','Madison','wi','civic','standing',43.07571,-89.41029,'exact','view','walk','','1901–1903',
  "The main building of the university's College of Agriculture, designed by J. T. W. Jennings and built from 1901 to 1903. The first department of agricultural economics in the United States was founded in it in 1909, and what became the first department of genetics in 1910.",
  look="A symmetric Beaux Arts front 200 feet wide: limestone basement, red brick above with stone quoins and cornice, a two-storey portico on four fluted Ionic columns, marble medallions in fruit-and-vegetable wreaths by the door, and a red tile roof. An octagonal auditorium is behind. Interior not checked.",
  accn="University building at 1450 Linden Drive, facing Henry Mall: seen from the campus walks.",
  links=[W('Agriculture Hall (Madison, Wisconsin)'),NR('85000571','Agriculture Hall')],brick='yes',bcol='red',hours='',arch='J. T. W. Jennings',builder='T. C. McCarthy',archw='Wikipedia, Agriculture Hall (Madison, Wisconsin)'),
N('hiram-smith-hall-madison','Hiram Smith Hall','Madison','wi','civic','standing',43.07601,-89.41158,'exact','view','walk','','1891–1892',
  "A Queen Anne building put up for the university's dairy school, which the Register list calls the first permanent dairy school in the western hemisphere. Wikipedia's list says it was built in 1891 to George B. Ferry's design, the Agriculture Hall article dates it 1892, and the Park Service record names Ferry & Clas; an annex designed by Arthur Peabody was added in 1909.",
  look="A Queen Anne hall of cream brick and rough stone with half-timbered gables, tall chimneys and red roofs, and its 1909 annex, on Observatory Drive. Interior not checked.",
  accn="University building at 1545 Observatory Drive: seen from the street.",
  links=[NR_LIST,NR('85000573','Hiram Smith Hall and Annex'),W('Agriculture Hall (Madison, Wisconsin)')],conf='mixed',brick='no',bcol='buff',hours='',arch='Ferry & Clas',archw='National Register record (Ferry & Clas); the Wikipedia list names George B. Ferry'),
N('uw-field-house-madison','Wisconsin Field House','Madison','wi','civic','standing',43.06864,-89.41269,'exact','view','walk','','1929–1930',
  "The university's arena, dedicated in 1930 to replace the Red Gym for basketball, designed by William F. Stevens and John Knudsen under state architect Arthur Peabody. It held 8,000 at first and more after later work; the basketball teams left for the Kohl Center in 1998 and volleyball is played there now. It was listed on the National Register in 1998.",
  look="Renaissance Revival, faced in Madison sandstone with dressed and carved limestone and a red clay tile gable roof, just south of Camp Randall Stadium.",
  accn="University arena at 1450 Monroe Street: seen from the street; inside for ticketed games and events. Event times not checked.",
  links=[W('Wisconsin Field House'),NR('98000829','University of Wisconsin Field House')],brick='no',hours='',arch='William F. Stevens; John Knudsen',archw='Wikipedia, Wisconsin Field House'),
N('madison-masonic-temple','Madison Masonic Temple','Madison','wi','civic','standing',43.07750,-89.38667,'exact','view','walk','','1923–1925',
  "A fraternal hall for Madison's Masonic bodies, designed by James R. and Edward J. Law in 1915, redrawn after the First World War and built from 1923 to 1925, with J. H. Findorff & Son as builders. It was listed on the National Register in 1990. Its auditorium of more than 1,200 seats is used for public rehearsals and performances.",
  look="Neoclassical in limestone: three storeys, four colossal columns across the front with the three entrances set back behind them, and a wide flight of steps up from Wisconsin Avenue. Interior not checked.",
  accn="At 301 Wisconsin Avenue, at East Johnson Street, two blocks north of the Capitol: seen from the street; the auditorium opens for events held there.",
  links=[W('Madison Masonic Temple (Madison, Wisconsin)'),NR('90001456','Madison Masonic Temple')],brick='no',hours='',arch='Law & Law',builder='J. H. Findorff & Son',archw='National Register record and form'),
N('orpheum-theater-madison','Orpheum Theater','Madison','wi','civic','standing',43.07520,-89.38874,'exact','open','walk','','1925–1927',
  "A movie palace designed by Rapp & Rapp of Chicago and opened in 1927 as the New Orpheum. Its Register form, of 2008, calls it Madison's best surviving movie palace, since the older Capitol Theater nearby was cut down when the Overture Center was built round it and keeps only its Moorish tower outside. It is now a venue for concerts and shows.",
  look="An Art Deco front of tan brick and smooth limestone on State Street with a canopy marquee the form thinks original and a tall ORPHEUM sign on the roof (once NEW ORPHEUM); the side wall is dark red brick; inside, a French Renaissance auditorium.",
  accn="At 216 State Street, a block from the Capitol. Open for ticketed shows; dates and door times are on the theatre's own calendar. The street front can be seen at any time.",
  links=[W('Orpheum Theater (Madison, Wisconsin)'),NR('07001460','Orpheum Theater'),L('Orpheum Theater','https://madisonorpheum.com/')],brick='some',bcol='mixed',hours='?',arch='Rapp & Rapp',archw='National Register record and form'),
N('barrymore-theatre-madison','Barrymore Theatre (Eastwood Theater)','Madison','wi','civic','standing',43.09306,-89.35227,'exact','open','drive','','1929',
  "Built on the east side as the Eastwood Theater, designed by Frederic J. Klein and H. C. Alford, ground broken April 30, 1929, opened December 27, 1929. A 1967 remodelling sealed off the dome and stripped the Spanish arcades from the auditorium; reopened in 1987 as the Barrymore, it has been owned by a nonprofit since 1992 and is a music venue.",
  look="Yellow brick, with an Italian Renaissance octagonal dome under green tile on the corner of Atwood Avenue and storefronts attached; the auditorium was Spanish colonial with tiled arches before 1967.",
  accn="At 2090 Atwood Avenue, in the Schenk-Atwood neighbourhood. Open for ticketed shows listed on the theatre's own page; the front can be seen at any time.",
  links=[W('Barrymore Theatre'),L('Barrymore Theatre','https://www.barrymorelive.com/')],brick='no',bcol='buff',hours='?',arch='Frederic J. Klein; H. C. Alford',archw='Wikipedia, Barrymore Theatre'),
N('garver-feed-mill-madison',"Garver Feed Mill (U.S. Sugar Company beet factory)",'Madison','wi','industry','standing',43.09473,-89.33483,'exact','open','drive','','1905–1906',
  "Built in 1905 and 1906 for the U.S. Sugar Company as a sugar beet factory, which ran until 1924. James R. Garver bought it in 1930 and Law, Law and Potter remodelled it as the feed mill and office of Garver's Supply Company. It stood empty for decades before a $20 million restoration finished in 2019; it is now a food hall with shops and event space. It was listed on the National Register in 2017.",
  look="Tan brick in an industrial Romanesque Revival style: the Register form describes the five-storey centre with a projecting arched entry under a crenellated tower, arched ground-floor openings and corbelled brick cornices, and a boiler house with a brick chimney.",
  accn="At 3241 Garver Green, next to Olbrich Botanical Gardens, with a parking lot on Garver Green; the Capital City State Trail passes. Its own page says it is open daily; each business keeps its own hours.",
  links=[W('Garver Feed Mill'),NR('100001445',"Garver's Supply Company Factory and Office"),L('Garver Feed Mill','https://www.garverfeedmill.com/')],th=[43.09524,-89.33560],thn='Garver Green parking lot',brick='no',bcol='buff',hours='Open daily; each business keeps its own hours',arch='Law, Law and Potter',archw='National Register record (1929-1931 remodelling)'),
]

PIN_NOTES={
 'bascom-hall-madison':'OpenStreetMap building for Bascom Hall, 500 Lincoln Drive; looked at on the aerial.',
 'uw-music-hall-madison':'OpenStreetMap building for Music Hall, 925 Lathrop Drive; looked at on the aerial.',
 'uw-science-hall-madison':'OpenStreetMap building for Science Hall, 550 North Park Street; agrees with the Wikipedia point within 10 m.',
 'uw-red-gym-madison':'OpenStreetMap building for the Armory and Gymnasium, 716 Langdon Street; looked at on the aerial.',
 'wisconsin-historical-society-headquarters-madison':'OpenStreetMap library point for the Society at 816 State Street; looked at on the aerial.',
 'uw-memorial-union-madison':'OpenStreetMap building for Memorial Union, 800 Langdon Street; looked at on the aerial.',
 'uw-carillon-tower-madison':'OpenStreetMap tower point for the Carillon Tower, 1160 Observatory Drive; looked at on the aerial.',
 'uw-agriculture-hall-madison':'OpenStreetMap building for Agricultural Hall, 1450 Linden Drive; agrees with the Wikipedia point.',
 'hiram-smith-hall-madison':'OpenStreetMap building for Hiram Smith Hall, 1545 Observatory Drive; looked at on the aerial.',
 'uw-field-house-madison':'OpenStreetMap feature for the Field House, 1450 Monroe Street; looked at on the aerial.',
 'madison-masonic-temple':'Wikipedia article coordinate for 301 Wisconsin Avenue; looked at on the aerial.',
 'orpheum-theater-madison':'OpenStreetMap theatre point, 216 State Street; looked at on the aerial.',
 'barrymore-theatre-madison':'OpenStreetMap theatre point, 2090-2098 Atwood Avenue; looked at on the aerial.',
 'garver-feed-mill-madison':'OpenStreetMap point for Garver Feed Mill; the parking point is the mapped lot on Garver Green.',
}
