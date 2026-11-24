# November 24, 2026: a fourth Mississippi scatter (batch ms_rkvq), claimed with tools/choose.py --thinnest.
# Sources opened: Wikipedia as raw text (articles and National Register lists), the Mississippi Department of Archives
# and History's Old Capitol Museum page, Rowan Oak's visit page, the Natchez Pilgrimage page.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'ms_rkvq','label':'Mississippi: Jackson, Vicksburg, Natchez, Biloxi and more','added':'2026-11-24 13:30'}

PLACES=[
N('king-edward-hotel-jackson','King Edward Hotel (Edwards Hotel)','Jackson','ms','hotel','standing',32.29987,-90.19073,'exact','view','drive','','1923',
'A 12-story Beaux-Arts hotel designed by the New Orleans architect William Nolan and opened as the Edwards Hotel on December 29, 1923, on a corner where two earlier hotels stood. '
'For over forty years it was the centre of Jackson society and politics. Okeh Records used a room here for blues recording sessions in December 1930. '
'The hotel stood closed and empty for nearly 40 years before work began in 2006; it was restored in 2007 to 2009 and reopened in December 2009 as apartments and a Hilton Garden Inn.',
look='A tall beige brick building with Beaux-Arts detail on the corner of Capitol and Mill Streets, and a restored lobby with a grand staircase. Whether a visitor may walk through the lobby was not checked.',
accn='Private; a working hotel. Look from the street. Hours not checked. It is a National Register property (1976) and a Mississippi Landmark (1990).',
links=[W('King Edward Hotel (Jackson, Mississippi)')],
brick='no',hours='?'),

N('mcraven-house-vicksburg','McRaven House (Bobb House)','Vicksburg','ms','landmark','standing',32.34607,-90.87194,'site','open','drive','','c. 1797–1849',
'A house built in three parts. The oldest, a kitchen with one room over it, was put up around 1797 by Andrew Glass and was a way station for travellers on the Natchez Trace; Sheriff Stephen Howard added a middle section in the Empire style in 1836, and John Bobb built the rest in Greek Revival after 1849. '
'In the 1863 siege of Vicksburg it served as a Confederate field hospital and camp and was hit by shells from both sides. It is listed on the National Register as the Bobb House and is run today as a tour home.',
look='Three visibly different building periods from frontier through Empire to Greek Revival. It is billed as haunted; that is local belief, not a fact. Interior not checked.',
accn='A private tour home at 1445 Harrison Street. Hours differ between listings (a Visit Vicksburg listing gave daily 12:00 to 4:30 p.m.; another gave 10 a.m. to 4:30 p.m. most days) and the home\'s own page could not be read, so hours are not confirmed. Street parking not checked.',
links=[W('McRaven House')],
conf='mixed',brick='?',hours='?'),

N('magnolia-hotel-biloxi','Magnolia Hotel (Mardi Gras Museum)','Biloxi','ms','hotel','standing',30.39460,-88.88934,'exact','open','drive','','1847',
'Built in 1847 for John Hahn, who ran a coffeehouse in New Orleans, and thought to be the oldest surviving hotel on the Mississippi Gulf Coast. '
'After the Civil War it filled with winter guests from the North. Hahn\'s descendants ran it until it closed in World War II. Hurricane Camille damaged it in 1969; the city bought it in 1972 and moved it about 100 yards north to higher ground, turning it to face east, and restored it. It needed more repair after Hurricane Katrina in 2005.',
look='A two-and-a-half-story wood-frame building with plastered walls, originally 54 feet on a side, with a hall through the middle of each floor. It now holds the Mardi Gras museum. Interior not checked.',
accn='Owned by the City of Biloxi, which lists it among its museums (119 Rue Magnolia). No hours could be read from the city page, so hours are not checked.',
links=[W('Magnolia Hotel (Biloxi, Mississippi)'),L('City of Biloxi: museums','https://www.biloxi.ms.us/museums/mardigras/')],
brick='no',hours='?'),

N('old-fort-house-columbus','Old Fort House (Themerlaine)','Columbus','ms','landmark','standing',33.50016,-88.42611,'site','view','drive','','1844',
'A planter\'s mansion built in 1844 for the Fort family. After Elias Fort died in 1834 his widow Martha Williams Battle Fort lived here with their four children and shaped the house as it stands; she stayed until her death in 1876. '
'It has been on the National Register since 1985. It combines Greek Revival, Gothic Revival and Italianate detail.',
look='A large antebellum house, seen from the street. Interior and any tour days not checked.',
accn='Private as far as the sources show; look from the public street. The listed coordinate is the Register\'s and was not checked against the house beyond the aerial.',
links=[W('Old Fort House (Columbus, Mississippi)')],
conf='mixed',brick='?',hours='?'),

N('old-water-electric-plant-holly-springs','Old Water and Electric Light Plant','Holly Springs','ms','industry','standing',34.76917,-89.44722,'area','view','drive','','1897–1898',
'Built in 1897 and 1898 to bring business to Holly Springs. By 1899, after water pipes were laid, 100 houses had running water. '
'It later served as the city police headquarters and is now listed as unused. It has been on the National Register since 1982.',
look='A late Victorian utility building near the courthouse square. Its condition and what survives inside were not checked.',
accn='City-owned as far as the sources show; look from the street. Ownership and hours not checked.',
links=[W('Old Water and Electric Light Plant')],
conf='mixed',brick='?',hours='?'),

N('brookhaven-union-station','Illinois Central Union Station and Godbold Transportation Center','Brookhaven','ms','rail','standing',31.57934,-90.44289,'exact','view','drive','','1890; 1907',
'Brookhaven was a junction of four railroads. In 1907 the Illinois Central built the Tudor-revival brick Union Station and freight house, designed by F. D. Chase; it has been on the National Register since 1980 and now holds the Military Memorial Museum. '
'Next to it the Amtrak stop, the Godbold Transportation Center (2011), is built into the town\'s old 1890 power plant, whose tall smokestack was kept.',
look='The depot is a Tudor-revival brick building at 125 South Whitworth Avenue. In the transportation centre the waiting-room benches came from the old depot, and the power-plant chimney still stands. Museum hours not checked.',
accn='Public street, and Amtrak\'s City of New Orleans stops at the centre. The museum\'s hours were not checked.',
links=[W('Godbold Transportation Center')],
brick='?',hours='?'),
N('brandon-hall-washington-ms','Brandon Hall','Washington','ms','landmark','standing',31.61485,-91.25329,'site','view','drive','','1809–1856',
'A Greek Revival plantation house finished in 1856 for Gerard Brandon III and Charlotte Hoggatt Brandon, built on land granted by the Spanish crown in 1788. '
'William Lock Chew bought the land in 1809 and put up a three-room brick house; Wikipedia says that house still survives as the basement of the present one. '
'The Brandon and Hoggatt families held the place for 81 years until 1914, and it was completely renovated in 1987.',
look='A large Greek Revival house on the old Natchez Trace road country, with an earlier brick dwelling built into its base. Interior and any tours not checked.',
accn='Private as far as the sources show; look from the public road. Ownership and visiting rules not checked.',
links=[W('Brandon Hall (Washington, Mississippi)')],
conf='mixed',brick='some',hours='?'),

N('rosalie-natchez','Rosalie','Natchez','ms','landmark','standing',31.55899,-91.40886,'exact','open','drive','','1823',
'A three-story brick mansion built in 1823 by enslaved people for Peter Little, a cotton broker, on the bluff over the Mississippi River. '
'It influenced many later Greek Revival mansions in Natchez. In the Civil War Union forces took it over as a headquarters, and General Grant used it; Union officers stored the owners\' furniture in the attic under guard. '
'The Mississippi State Society of the Daughters of the American Revolution has run it as a house museum for more than seventy years.',
look='A cubical brick house with a low hipped roof ringed by a balustrade. Interior not checked.',
accn='A house museum on the bluff in Natchez. The Natchez Pilgrimage site lists year-round home tours, but no hours for Rosalie could be read, so hours are not checked.',
links=[W('Rosalie Mansion'),L('Natchez Pilgrimage Tours','https://www.natchezpilgrimage.com/')],
brick='?',hours='?'),
]
PIN_NOTES={
'king-edward-hotel-jackson':'ArcGIS address lookup (235 West Capitol Street), checked on the aerial.',
'mcraven-house-vicksburg':'ArcGIS address lookup (1445 Harrison Street); the Wikipedia point was in woods nearby.',
'magnolia-hotel-biloxi':'ArcGIS address lookup (119 Rue Magnolia).',
'old-fort-house-columbus':'Register point moved 18 m north onto the house shown on the aerial; the match to this house is from the Register point only.',
'old-water-electric-plant-holly-springs':'Wikipedia coordinate; the aerial shows small buildings at the pin and which one is the plant could not be told, so the pin marks the area.',
'brookhaven-union-station':'ArcGIS address lookup (125 South Whitworth Avenue).',
'brandon-hall-washington-ms':'Moved from the Wikipedia point to the house seen on the aerial, about 50 m west.',
'rosalie-natchez':'ArcGIS address lookup (100 Orleans Street).',
}
