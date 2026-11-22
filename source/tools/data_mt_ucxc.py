# Helena, Montana: buildings named in a walking-tour video, each checked against the Montana Historical Society's
# National Register sign texts (Historic Montana), Wikipedia and the owners' own pages.
from data_b import N
from data_ma import W

def HM(n, label): return [label + ' (Historic Montana, Montana Historical Society)', 'https://historicmt.org/items/show/%d' % n]

BATCH={'key':'mt_ucxc','label':'Helena, Montana: courthouse, jail, temples, hotel, kilns and Reeder\'s Alley','added':'2026-11-22 15:59'}

PLACES=[
N('lewis-clark-courthouse-helena','Lewis and Clark County Courthouse','Helena','mt','civic','standing',46.58588,-112.03647,'exact','public','drive','','1885–',
  'A granite courthouse in the Romanesque Revival style of H. H. Richardson, drawn by the St. Paul architects Hodgson and Stem. Besides the county, it housed Montana\'s territorial capitol (1887 to 1888) and then the state capitol until 1902; word of statehood came here in 1889 and the first governor, J. K. Toole, was sworn in the same day. The 1935 earthquakes brought down its Norman clock tower, and the tower, the fourth-floor gables and the heavy stone cornice were never put back.',
  'Granite walls with Bayfield brownstone trim from Wisconsin, now without the clock tower and gables seen in old photographs. It stands at 228 East Broadway, with the old county jail on the same block (see the Myrna Loy). What is inside today and whether visitors may walk in was not checked.',
  'The building that served as Montana\'s capitol, cut down a storey by the 1935 earthquakes.',
  'A county building on a public street in downtown Helena; look from Broadway and Ewing Street. Street parking. Current offices and opening times not checked.',
  [HM(721,'Lewis and Clark County Courthouse'),W('Helena Historic District (Helena, Montana)')],
  conf='', th=None, thn=None, brick='no', hours=''),

N('myrna-loy-old-county-jail-helena','Old Lewis and Clark County Jail (the Myrna Loy)','Helena','mt','civic','standing',46.58578,-112.03559,'exact','open','drive','','1890–',
  'The county jail of 1890, built of local granite in a brooding Romanesque style to plans by the Helena firm of Paulson and McConnell, working for the Detroit Safe and Lock Company. It held prisoners until the early 1980s. After it closed, the building was renovated inside and opened at the start of the 1990s as an arts centre, the Myrna Loy, which grew out of the Helena Film Society of 1976.',
  'Heavy granite with thick stone lintels, deep arches and a corner tower that lost its battlements in the 1935 earthquakes. Now a cinema and stage: films and performances most days. What is left of the cells inside was not checked.',
  'A medieval-looking 1890 jail that now shows films.',
  'Owned and run as the Myrna Loy arts centre, 15 North Ewing Street. Box office hours from the Myrna Loy\'s own page, read November 2026; showtimes by phone (406-443-0287) or on its page. Street parking.',
  [HM(722,'Lewis and Clark County Jail'),['The Myrna Loy','https://www.themyrnaloy.com/'],['The Old County Jail becomes a Centerpiece for the Arts (Southwest Montana)','https://southwestmt.com/blog/the-old-county-jail-becomes-a-centerpiece-for-the-arts-in-helena-montana/']],
  conf='', th=None, thn=None, brick='no', hours='Box office Monday to Friday noon to 7:30 p.m., weekends 2 to 7:30 p.m.'),

N('algeria-shrine-temple-helena','Algeria Shrine Temple (Helena Civic Center)','Helena','mt','civic','standing',46.59485,-112.0405,'exact','view','drive','','1920–',
  'A Moorish Revival hall built by the Shriners for their own meetings and for public events, designed by George Carsley and Charles Haire. Wikipedia gives 1920 for the building; the state\'s sign gives 1921 as the year it was finished. Its auditorium, when new, was the ninth-largest in the country. The 1935 earthquakes damaged it more than the Shriners could pay to repair, and the City of Helena bought it in 1938; it became the Civic Center and held city offices until 1979.',
  'A minaret seventeen storeys high over a six-storey front of patterned brick (the state sign\'s figures), and a 1939 fire station addition in the same colours. Inside, an auditorium (1,925 seats, Wikipedia says; 2,608 when new, the sign says) and a ballroom; the city hires them out for shows, dances and conventions.',
  'A Shriners\' mosque-style hall the earthquake bankrupted, saved by the city.',
  'Owned by the City of Helena, 340 Neill Avenue. Open inside only for events booked there; look from Neill Avenue and Park Avenue the rest of the time. Street parking.',
  [HM(816,'Algeria Shrine Temple'),W('Algeria Shrine Temple')],
  conf='mixed', th=None, thn=None, brick='?', hours=''),

N('temple-emanu-el-helena','Temple Emanu-El','Helena','mt','worship','standing',46.58983,-112.03246,'exact','ask','drive','','1890–1891',
  'The first synagogue built between St. Paul and Portland. Governor J. K. Toole laid the cornerstone in 1890; the Helena architects Heinlein and Mathias designed it in a Romanesque and Moorish style, with keyhole windows and onion domes on the two front towers. By the 1930s the congregation had dwindled, and the State of Montana took the building, removed most religious symbols, put in a second floor and used it for offices; the Catholic Diocese of Helena bought it in 1981. In 2022 the Montana Jewish Project bought it back as a centre for Montana\'s Jews.',
  'Granite, porphyry and sandstone walls, keyhole windows and stained glass; the domes are gone. The Hebrew year 5651 is still cut in the cornerstone. The meeting space is on the upper floor, up stairs.',
  'A frontier synagogue that lost its domes and found its people again.',
  'Owned by the Montana Jewish Project, 515 North Ewing Street. Its page offers tours by appointment through its contact page (read November 2026); otherwise look from the street. Not wheelchair accessible, the page says.',
  [HM(819,'Temple Emanu-El'),W('Temple Emanu-El (Helena, Montana)'),['Montana Jewish Project: tours','https://www.montanajewishproject.com/contact'],['Montana Jewish Project buys Helena temple (NBC Montana, 2022)','https://nbcmontana.com/news/local/montana-jewish-project-buys-helena-temple-built-in-1891']],
  conf='', th=None, thn=None, brick='no', hours=''),

N('placer-hotel-helena','Placer Hotel','Helena','mt','hotel','standing',46.58938,-112.03884,'exact','view','drive','','1912–1913',
  'A seven-storey hotel opened with a ball on April 12, 1913, when it was the largest hotel between the Twin Cities and the Pacific coast. It was paid for almost entirely by public subscription, and named for the placer gold washed out of the gravel when its foundation was dug. George Carsley designed it with Cass Gilbert, architect of the Woolworth Building, and it is built of reinforced concrete and brick from the Western Clay Manufacturing Company. It has since been turned into condominiums.',
  'Wrought-iron balconies, deep eaves and a wide cornice, with 172 former guest rooms around a U-shaped plan so that every room had a window outside. It stands at the corner of Last Chance Gulch and Grand Street.',
  '',
  'Private condominiums at 21 North Last Chance Gulch; look from the street. Street and public parking downtown.',
  [HM(735,'Placer Hotel'),['Placer Hotel (Helena History)','https://helenahistory.org/placer_hotel.htm']],
  conf='', th=None, thn=None, brick='yes', hours=''),

N('reeders-alley-helena','Reeder\'s Alley','Helena','mt','town','standing',46.58482,-112.04327,'site','public','walk','','1870s–1884',
  'A lane of small brick and stone tenements on the steep hillside at the south-west corner of downtown, built by Louis Reeder, a brick mason from Pennsylvania, as lodgings for single miners; he took an existing log cabin into the largest building. The state\'s sign dates the building to 1875 to 1884 and the Montana Heritage Commission to 1872 to 1884; it was known as Reeder\'s Alley by the time he died in 1884. Pensioners still lived here in 1961 when local women began saving the buildings from demolition. The owners gave the alley to the Montana Heritage Commission in 2001.',
  'The town\'s most complete block from the territorial period: about thirty former one-room units of brick and stone in a narrow alley against Mount Helena, a stone house that held four tiny apartments, and the log Yee Wau cabin of about 1870, the last trace of Helena\'s Chinatown. Today a barbershop, small businesses, offices and the Visit Helena office are in the buildings.',
  'Thirty one-room miners\' flats in a lane nobody demolished.',
  'Owned by the Montana Heritage Commission (state of Montana); the alley at 101 to 206 Reeder\'s Alley, off South Park Avenue, is open to walk through, and the businesses keep their own hours. Small lots on South Park Avenue and Howie Street.',
  [HM(9,'Reeder\'s Alley'),HM(749,'Stone House at Reeder\'s Alley'),HM(757,'Yee Wau Cabin'),['Reeder\'s Alley (Montana Heritage Commission)','https://prod-reedersalley.mt.gov/index']],
  conf='mixed', th=None, thn=None, brick='?', hours=''),

N('federal-building-helena','Federal Building (City-County Building)','Helena','mt','civic','standing',46.58988,-112.04071,'exact','open','drive','','1904–',
  'A Renaissance Revival federal building of 1904 by James Knox Taylor, the federal government\'s supervising architect, built round a steel frame. It held the federal court, the U.S. Marshals and the post office; plain side wings and a rear addition followed in 1931. The City of Helena and Lewis and Clark County bought it together in 1978 and use it as their government building.',
  'Rusticated stone on the ground floor, smooth sandstone above, arched windows with Corinthian capitals, and a frieze of red diamond-shaped stone tiles under deep eaves on heavy timber brackets.',
  '',
  'City and county offices at 316 North Park Avenue. The county Clerk of District Court\'s office in it gives the hours shown (the county\'s page for that office, read November 2026); other offices were not checked. Street parking.',
  [HM(2218,'Federal Building'),['Clerk of District Court (Lewis and Clark County)','https://lccountymt.gov/Government/Clerk-of-District-Court']],
  conf='', th=None, thn=None, brick='no', hours='Monday to Friday 8 a.m. to 5 p.m. (Clerk of District Court)'),

N('masonic-temple-helena','Masonic Temple','Helena','mt','civic','standing',46.58667,-112.03859,'exact','view','drive','','1885–',
  'A business block with a Masonic lodge on top, designed by the Helena architects Heinlein and Matthias, who won a $250 prize for the design and oversaw its building from 1885. The Masons met on the third floor from 1886 to 1942; the U.S. Post Office and the State Publishing Company were tenants below.',
  'A lavish front in an Italian Renaissance manner. Its tall windows, lost in a remodelling, were rebuilt when the front was restored in 1979.',
  '',
  'Private, at 104 East Broadway in downtown Helena; look from the street.',
  [HM(724,'Masonic Temple, Helena')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('ywca-building-helena','YWCA Building','Helena','mt','civic','standing',46.59221,-112.03973,'exact','view','drive','','1918–',
  'Built in 1918 as a home for young working women by the Helena chapter of the Young Women\'s Christian Association, Independent, founded seven years earlier by women of most of the town\'s churches and synagogues; the chapter never joined the national body. It gave safe rooms and classes from typing to astronomy. The organisation still runs it, now as shelter for women moving from homelessness to permanent housing.',
  'Designed by Chester Kirk and built of brick from the Kessler brickyard, with brick quoins at the corners, a soldier course, belt courses and stacked brick window surrounds; 43 bedrooms upstairs.',
  '',
  'Private, a women\'s shelter at 501 North Park Avenue (Historic Montana gives Park Street): look from the street only.',
  [HM(826,'YWCA Building'),W("Young Women's Christian Association (Independent)"),['Empowering Women: The Helena YWCA (Montana Historical Society)','https://montanawomenshistory.mt.gov/News/news-articles/Empowering-Women-The-Helena-YWCA']],
  conf='', th=None, thn=None, brick='?', hours=''),

N('power-block-helena','Power Block','Helena','mt','civic','standing',46.58892,-112.03899,'exact','view','drive','','1889–',
  'A granite business block of 1889 built for T. C. Power, a merchant who controlled much of territorial Montana\'s trade. Willetts and Ashley of Chicago drew it in a Romanesque Revival manner moving towards the Chicago School. Power\'s American National Bank was here from 1892 into the 1920s; the Power Block West, matching it, was added in 1914.',
  'Rough granite walls and a rounded north-east corner where the number of openings on each floor matches the floor\'s number.',
  'Count the windows on the corner.',
  'Private, at Sixth Avenue and North Last Chance Gulch; look from the street.',
  [HM(737,'Power Block & Power Block West')],
  conf='', th=None, thn=None, brick='no', hours=''),

N('grizzly-gulch-lime-kilns-helena','Grizzly Gulch Lime Kilns','Helena','mt','industry','ruins',46.57677,-112.05383,'site','view','drive','','late 1860s–c.1910',
  'The kilns that made lime for mortar for the whole region. Joseph O\'Neill built the first in the late 1860s; limestone was blasted from the hill behind, brought down on handcars or tumbled down the bank, and burnt for days over pine fires. Each kiln could make about twenty tons every eight hours. James McKelvey, who later owned them, supplied the mortar for the State Capitol. With no railway they closed about 1910, though one ran again briefly in the 1930s.',
  'Kilns with hewn timbers, hand-forged iron braces and fire brick shipped from the East, and a state sign beside them. They are part of the Helena West Main Street Historic District.',
  '',
  'Seen from Grizzly Gulch Drive near Oro Fino Gulch Drive, where the state marker stands. Who owns the kilns was not found, so stay on the road. The McKelvey Trail lot of the city\'s trail network is about 200 m south-west.',
  [HM(790,'Grizzly Gulch Lime Kilns'),['Grizzly Gulch Lime Kilns marker (HMdb)','https://www.hmdb.org/m.asp?m=187580']],
  conf='', th=None, thn=None, brick='?', hours=''),

N('helena-railroad-depot-district','Helena Railroad Depot and Sixth Ward','Helena','mt','rail','standing',46.60013,-112.01497,'site','public','drive','stations','1883–',
  'The Northern Pacific reached Helena on June 13, 1883, a mile from downtown, and a railway neighbourhood, the Sixth Ward, grew up round the yards. Charles Reed of Reed and Stem designed the present depot in 1903, and A. O. Von Herbulis, architect of the cathedral, drew St. Mary\'s Church nearby in 1910. Trolley tracks were set in brick paving in 1915 and Beattie Park was laid out in 1930. Passenger trains no longer call.',
  'The 1903 depot, with newer brick on its west end where the 1935 earthquakes damaged it; false-fronted wooden shops of the early 1880s on Railroad Avenue; St. Mary\'s Church; trolley rails in the brick pavement; Beattie Park.',
  '',
  'A historic district of public streets round Railroad and Helena Avenues and North Sanders and North Harris Streets; the buildings are private. The pin is on the depot.',
  [HM(69,'Helena Railroad Depot Historic District'),HM(760,'Beattie Memorial Park')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('st-charles-hall-carroll-college','St. Charles Hall, Carroll College','Helena','mt','inst','standing',46.60087,-112.03915,'area','view','drive','','1909–1910',
  'The first building of Mount St. Charles College, the Catholic college founded by Bishop John Patrick Carroll. President William Howard Taft helped lay its cornerstone on September 27, 1909, and classes began in September 1910. The college was renamed Carroll College in 1932. The 1935 earthquakes damaged the top of the hall\'s south gable and many of its large stones fell; the roof was rebuilt lower and flatter.',
  'A large stone hall, still a residence hall of the college. Interior not checked.',
  'Taft laid the first stone.',
  'A private college campus on North Benton Avenue; look from the campus roads. Parking and visitor rules not checked. The pin is the college\'s point on Wikipedia, not yet placed on the hall itself.',
  [W('Carroll College'),['History of Carroll College (Carroll College)','https://catalog.carroll.edu/node/718'],['Carroll College (Helena History)','https://helenahistory.org/carroll_college.htm']],
  conf='', th=None, thn=None, brick='?', hours=''),
]

PIN_NOTES={
 'lewis-clark-courthouse-helena':'Pin is the Historic Montana point for the courthouse.',
 'myrna-loy-old-county-jail-helena':'Pin is the Historic Montana point for the jail.',
 'algeria-shrine-temple-helena':'Pin is the Historic Montana point for the temple.',
 'temple-emanu-el-helena':'Pin is the Historic Montana point for the temple.',
 'placer-hotel-helena':'Pin is the Historic Montana point for the hotel.',
 'reeders-alley-helena':'Pin is the Historic Montana point for Reeder\'s Alley.',
 'federal-building-helena':'Pin is the Historic Montana point for the building.',
 'masonic-temple-helena':'Pin is the Historic Montana point for the building.',
 'ywca-building-helena':'Pin is the Historic Montana point for the building.',
 'power-block-helena':'Pin is the Historic Montana point for the block.',
 'grizzly-gulch-lime-kilns-helena':'Pin is the HMdb position of the state marker; the aerial shows a small structure beside Grizzly Gulch Drive at the foot of the pale quarried slope.',
 'helena-railroad-depot-district':'The Historic Montana point for the district fell on a large white-roofed building south of the tracks; moved 66 m onto the long red-roofed building beside the tracks, taken to be the depot from the aerial (not confirmed by a source).',
 'st-charles-hall-carroll-college':'Pin is the Wikipedia point for Carroll College, on a campus lawn; which of the red-roofed halls round it is St. Charles Hall was not settled, so the pin stays at area precision.',
}
