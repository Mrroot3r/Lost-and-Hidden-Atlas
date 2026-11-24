# November 24, 2026 (UTC): Scranton, Lackawanna County, Pennsylvania (region pane), names taken as leads from one
# Old World Exploration video about the city and checked one by one. Standing buildings of the anthracite and iron
# city: the courthouse, city hall, the Albright library, the armory, the Masonic temple, the Lackawanna station,
# the Hotel Jermyn, the old Central High School, the county prison, Scranton Prep, four churches, the iron furnace
# stacks and the Lake Scranton dam.
# Facts come from the linked sources only: SAH Archipedia (George E. Thomas, Buildings of Pennsylvania), the City of
# Scranton's landmark-buildings guide (Historical Architectural Review Board, May 2016), Wikipedia read as raw text,
# and the pages of the library system, the Anthracite Heritage Museum, the Pennsylvania Historical and Museum
# Commission, the cathedral and Elm Park church. Where a source is silent the text says "not checked".
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
def SAH(n,t): return L('SAH Archipedia: '+t,'https://sah-archipedia.org/buildings/PA-02-LK'+n)
HARB=L('City of Scranton: Downtown Scranton landmark buildings (2016, PDF)','https://scrantonpa.gov/docs/HARB/Historic%20Scranton-Downtown%20Scranton%20Landmark%20Buildings%20and%20Historic%20Districts.pdf')

BATCH={'key':'scranton_prsl','label':'Scranton, Pennsylvania','added':'2026-11-24 12:33'}

DT='Street parking and public lots in downtown Scranton; fees not checked.'

PLACES=[

N('lackawanna-county-courthouse-scranton','Lackawanna County Courthouse','Scranton','pane','civic','standing',41.40813,-75.66243,'site','public','drive','',
  '1881–1884, enlarged 1896',
  'Lackawanna County was split from Luzerne County in 1878, and the Lackawanna Iron and Coal Company gave the ground for its courthouse, once a swampy lowland called the Lily Pond. Isaac G. Perry designed it (finished 1884), and in 1896 B. T. Lacey added a third story and rebuilt the roof. The first session of the commission that settled the 1902 anthracite coal strike sat here.',
  look='A Romanesque and Victorian Gothic pile of yellowish West Mountain stone trimmed with Onondaga limestone, with a five-story clock tower, Flemish gables and a tile roof. A wing was added in 1964, and the interior has been much altered. On the square: the 1924 John Mitchell Monument (a bronze of the mine workers\' leader in a granite niche with reliefs of anthracite life) and the 1899 Soldiers and Sailors Monument. Interior not checked.',
  hook='',
  accn='Courthouse Square is an open public square in the middle of downtown, at North Washington Avenue and Spruce Street. The courthouse is a working county building; its opening hours were not checked. '+DT,
  links=[W('Lackawanna County Courthouse'),SAH('1','Lackawanna County Courthouse'),HARB],
  conf=None,th=None,thn=None,brick='no',hours=''),

N('scranton-city-hall','Scranton City Hall (Municipal Building)','Scranton','pane','civic','standing',41.41009,-75.66093,'site','view','drive','',
  '1888–1893',
  'Edwin L. Walter, who also drew the county prison, designed the Municipal Building in 1888 in a spiky Victorian Gothic. It still holds the mayor\'s and city offices. A small covered bridge from its second story crosses to the fire headquarters on Mulberry Street, built in the same style; the two were listed together on the National Register in 1981.',
  look='Limestone ashlar with sandstone trim, tall towers and pinnacles, at North Washington Avenue and Mulberry Street. Inside, the council chamber is a double-height room with stencilled decoration and large stained glass windows (SAH Archipedia). Whether visitors may see the chamber was not checked.',
  hook='',
  accn='A working city hall, 340 North Washington Avenue: look from the street. Office hours not checked. '+DT,
  links=[W('Scranton City Hall'),SAH('19','City Hall'),HARB],
  conf=None,th=None,thn=None,brick='no',hours=''),

N('albright-memorial-library-scranton','Albright Memorial Library','Scranton','pane','civic','standing',41.41123,-75.65959,'exact','open','drive','',
  '1890–1893',
  'The Albright family gave the site of their Scranton home for a public library, and the Buffalo architects Green and Wicks built it in 1890–1893, modelled on the Hotel de Cluny in Paris. It opened in May 1893 as the Scranton Public Library and is still the city\'s main library. Frederick Law Olmsted planned the original grounds.',
  look='A French Gothic and Renaissance building of Indiana limestone and Medina stone with a tile roof, owls and gargoyles, wrapped round a courtyard. Inside: reading rooms with oak woodwork and beamed ceilings off a stair hall, a barrel-vaulted reading room upstairs, and stained glass windows by Edwin Ford and Frederick Brooks of Boston showing famous bookbinders\' work.',
  hook='',
  accn='A public library of the Lackawanna County Library System, 500 Vine Street at North Washington Avenue; free to walk in during opening hours (from the library system\'s page). The system lists paid street parking by app. '+DT,
  links=[W('Albright Memorial Building'),SAH('21','Albright Memorial Library'),L('Lackawanna County Library System: Albright Memorial Library','https://www.lclshome.org/albright-memorial-library/'),HARB],
  conf=None,th=None,thn=None,brick='no',hours='Monday to Thursday 9 a.m. to 8 p.m.; Friday and Saturday 9 a.m. to 5 p.m.; Sunday 1 to 5 p.m.'),

N('lackawanna-college-central-high-scranton','Lackawanna College Administration Building (Central High School)','Scranton','pane','civic','standing',41.41145,-75.65904,'exact','view','drive','',
  '1895–1896, addition 1923',
  'Built as Scranton\'s Central High School to designs by Little and O\'Connor, and meant to sit well with the Albright Library across Vine Street. Edward Langley\'s 1923 addition, which matches the old part closely, holds the auditorium now called the Mellow Theater. It is now the main building of Lackawanna College.',
  look='A Beaux-Arts front with Gothic details in colourful West Mountain stone and limestone, with ironwork at the main door, at North Washington Avenue and Vine Street. The auditorium is the finest room inside (SAH Archipedia); interior not checked.',
  hook='',
  accn='A working college building, 501 Vine Street: look from the street. '+DT,
  links=[SAH('22','Administration Building, Lackawanna College (Central High School)'),W('Lackawanna College'),HARB],
  conf=None,th=None,thn=None,brick='no',hours=''),

N('scranton-cultural-center-masonic-temple','Scranton Cultural Center (Masonic Temple and Scottish Rite Cathedral)','Scranton','pane','civic','standing',41.41074,-75.66000,'exact','open','drive','',
  '1927–1930',
  'Raymond Hood, who won the Chicago Tribune tower competition, designed this long, massive temple for the city\'s Masons, finished in 1930. It held a Scottish Rite cathedral and lodge rooms beside a theatre and ballroom meant for public use. It is now a performing arts centre run by the Scranton Cultural Center, which hosts touring Broadway shows, concerts and events.',
  look='Indiana limestone over a steel frame in a mix of Gothic and Romanesque with Art Deco touches, with a finely carved entrance arch. Inside: travertine halls, themed meeting rooms, a 1,600-seat theatre whose ceiling shows two-headed eagles and whose stage opens into a ballroom, and a smaller fourth-floor theatre. Roof and masonry repairs began in spring 2025.',
  hook='',
  accn='420 North Washington Avenue. Open for shows and events, and for building tours: Wikipedia says visitors can take a tour of the building, but the centre\'s tour page could not be opened when this was written, so book through its page or by telephone. '+DT,
  links=[W('Scranton Cultural Center'),SAH('20','Scranton Cultural Center (Masonic Temple and Scottish Rite Cathedral)'),L('Scranton Cultural Center','https://www.scrantonculturalcenter.org/'),HARB],
  conf=None,th=None,thn=None,brick='no',hours='?'),

N('lackawanna-station-scranton','Lackawanna Station (Delaware, Lackawanna and Western Railroad Station)','Scranton','pane','rail','standing',41.40553,-75.66135,'exact','open','drive','',
  '1907–1908',
  'The Lackawanna Railroad\'s owners gave Scranton this French Renaissance station and office building in 1907–1908, designed by Kenneth Murchison as a larger cousin of his Hoboken terminal. Passenger service ended and the station closed in 1970. It was rescued and reopened as a hotel in 1983, and keeps its clocks, stairs, fountains and ceilings.',
  look='An Indiana limestone front over brick and steel, with eagles round an eight-foot bronze clock on the central tower. The Grand Lobby, two and a half stories high, has a mosaic tile floor, a barrel-vaulted Tiffany stained-glass ceiling, Siena marble walls and 36 Grueby faience tile panels of scenes along the railroad; the old waiting room is a restaurant.',
  hook='',
  accn='A working hotel, 700 Lackawanna Avenue, next to Steamtown National Historic Site; the lobby is the hotel\'s public space. Opening hours for non-guests were not checked. '+DT,
  links=[W('Radisson Lackawanna Station Hotel'),SAH('11','Radisson Lackawanna Station Hotel (Delaware, Lackawanna and Western Railroad Station)'),HARB],
  conf=None,th=None,thn=None,brick='no',hours='?'),

N('scranton-iron-furnaces','Scranton Iron Furnaces','Scranton','pane','industry','ruins',41.40402,-75.66240,'site','public','walk','',
  '1840s–1902',
  'Scranton, Grant and Company began making iron here in 1840, and the four stone blast furnaces were built between 1848 and 1857. Rails for the Erie Railroad were made here in 1847, and by 1865 the works, later the Lackawanna Iron and Coal Company, had the largest iron capacity in the country. In 1902 the company took the plant apart and moved it to Lackawanna, New York.',
  look='Four huge stone furnace stacks, the only part of the plant left, in a small historic park on Cedar Avenue, with an arch of brick among the stonework (the city guide gives stone and brick).',
  hook='',
  accn='Owned by the Pennsylvania Historical and Museum Commission and run with the Anthracite Heritage Museum, 159 Cedar Avenue. The museum\'s page gives the grounds as open dawn to dusk all year (the state page gives the same hours worded "dusk to dawn"). Tours and group visits through the Anthracite Heritage Museum. Street parking on Cedar Avenue; not checked.',
  links=[W('Scranton Iron Furnaces'),SAH('12','Lackawanna Iron and Coal Company Furnaces'),L('Anthracite Heritage Museum: Iron Furnaces','http://www.anthracitemuseum.org/explore/iron-furnaces/'),L('Pennsylvania Historical and Museum Commission: Scranton Iron Furnaces','https://www.pa.gov/agencies/phmc/historic-sites-and-museums/industrial-heritage-trail/scranton-iron')],
  conf=None,th=None,thn=None,brick='?',hours='Grounds daily, dawn to dusk, all year'),

N('st-peters-cathedral-scranton','Cathedral of Saint Peter','Scranton','pane','worship','standing',41.41059,-75.66363,'exact','open','drive','',
  '1865–1867, enlarged 1883–1884',
  'Joel Amsden built it in 1865–1867 as the parish church of St. Vincent de Paul. In 1883–1884 Edwin Forrest Durang enlarged it behind a new Baroque front with twin bell towers, and it was consecrated in 1884 as the cathedral of the Diocese of Scranton. The rectory beside it dates from 1908; the whole complex was listed on the National Register in 1976.',
  look='A pedimented front between two bell towers on Wyoming Avenue. Inside: stained glass from the 1883 work, by Durang and later the German designer Frank Mayer, with 15 large windows on the life of Christ, and a 1979 Casavant organ.',
  hook='',
  accn='The cathedral of the Diocese of Scranton, 315 Wyoming Avenue. Mass times from the cathedral\'s own page; confession Saturdays 10:30 to 11:30 a.m. '+DT,
  links=[W("St. Peter's Cathedral (Scranton, Pennsylvania)"),SAH('16',"St. Peter's Cathedral"),L('Cathedral of Saint Peter: Mass and confession','https://stpeterscathedral.org/services'),HARB],
  conf=None,th=None,thn=None,brick='?',hours='Mass Monday to Friday 6:30 a.m. and 12:10 p.m.; Saturday 6:30 a.m. and 5:30 p.m.; Sunday 6:30 a.m., 10 a.m., 12:15 p.m. and 5 p.m.'),

N('elm-park-church-scranton','Elm Park United Methodist Church','Scranton','pane','worship','standing',41.40717,-75.65991,'exact','open','drive','',
  '1891–1893',
  'Building began in September 1891 to designs by Weary and Kramer of Akron, known for their Akron-plan Protestant churches. Fires in December 1892 and March 1893 left only the tower standing, and the church was finished in December 1893. Its size earned it the name "Cathedral of Methodism of Northeastern Pennsylvania".',
  look='A block-long Richardsonian Romanesque church of West Mountain stone at 712 Linden Street. The church\'s page speaks of the sanctuary\'s soaring architecture and its organ; interior otherwise not checked.',
  hook='',
  accn='An active Methodist church, 712 Linden Street. Service times from the church\'s own page. '+DT,
  links=[SAH('25','Elm Park United Methodist Church'),L('Elm Park United Methodist Church','https://www.elmparkumchurch.org/'),HARB],
  conf=None,th=None,thn=None,brick='no',hours='Sunday 8:30 a.m. (chapel), 10 a.m. (sanctuary) and 1 p.m. (Swahili service)'),

N('covenant-presbyterian-church-scranton','Covenant Presbyterian Church (First Presbyterian)','Scranton','pane','worship','standing',41.40997,-75.65484,'site','view','drive','',
  '1902–1904',
  'The First Presbyterian congregation bought the old reservoir lots at Madison Avenue and Olive Street in 1894, and built this church after selling its old church on Washington Avenue in 1902. The cornerstone was laid in 1903 and the church, designed by Lansing C. Holden of New York, was dedicated in 1904. It was later called Westminster and is now Covenant Presbyterian.',
  look='A Victorian Gothic church of limestone with flying buttresses and a turret. The city guide notes nine Tiffany windows; interior not checked.',
  hook='',
  accn='An active church, 550 Madison Avenue: look from the street. No page of its own giving service times was found. Street parking; not checked.',
  links=[HARB],
  conf=None,th=None,thn=None,brick='no',hours=''),

N('st-matthews-lutheran-church-scranton','St. Matthew\'s Lutheran Church (Second Presbyterian Church)','Scranton','pane','worship','standing',41.40972,-75.65788,'site','view','drive','',
  '1885–1886',
  'Built in 1886 on Jefferson Avenue as the Second Presbyterian Church, to designs by James C. Cady, at a cost of about $60,000; Tiffany studios did much of the original interior. The Presbyterians moved in 1926 and St. John\'s Lutheran Church bought it. A later merger of two Lutheran congregations gave it its present name; it was renovated in 2000.',
  look='A Victorian Romanesque church. Two original Tiffany windows and Tiffany lamps survive inside (city guide); interior not checked.',
  hook='',
  accn='An active Lutheran church, 425 Jefferson Avenue: look from the street. No page of its own giving service times was found. Street parking; not checked.',
  links=[HARB],
  conf=None,th=None,thn=None,brick='?',hours=''),

N('scranton-armory','Scranton Armory (Watres Armory)','Scranton','pane','civic','standing',41.41549,-75.65272,'exact','view','drive','',
  '1900–1901',
  'The Lackawanna Iron and Coal Company gave the land and building began in August 1900 to designs by Lansing C. Holden; it was named for Colonel Louis A. Watres of the National Guard regiment. The Guard used it until 2012, when it moved to a new reserve centre. The building is now zoned for commercial use and has served as an art storage warehouse.',
  look='A four-story Romanesque castle of brick and stone, 20 by 26 bays, with crenellated towers either side of a stone arched entrance, at 901 Adams Avenue. It held a drill hall with a high arched ceiling and a swimming pool later filled in for target practice. Not open to visitors.',
  hook='',
  accn='Private, 901 Adams Avenue: look from Adams and Jefferson avenues. Street parking; not checked.',
  links=[W('Scranton Armory'),HARB],
  conf=None,th=None,thn=None,brick='?',hours=''),

N('hotel-jermyn-scranton','Hotel Jermyn','Scranton','pane','hotel','standing',41.40869,-75.66556,'exact','view','drive','',
  '1894–1896',
  'The coal operator John Jermyn bought the Forest House of 1855, pulled it down and built this seven-story hotel in its place in 1894–1896 to designs by John A. Duckworth, with 200 fireproof rooms of stone and steel. More than 10,000 people came to see it when it opened in 1896, and President Eisenhower stayed here. It became the Jermyn Motor Inn and is now the Jermyn Apartments, with 85 apartments.',
  look='A seven-story Romanesque front of pale stone, at the corner of Spruce Street, 139 Wyoming Avenue, facing the courthouse side of downtown. Now apartments; interior not open.',
  hook='',
  accn='Private apartments, 139 Wyoming Avenue: look from the street. '+DT,
  links=[HARB],
  conf=None,th=None,thn=None,brick='no',hours=''),

N('lackawanna-county-prison-scranton','Lackawanna County Prison','Scranton','pane','inst','standing',41.42295,-75.64829,'site','view','drive','',
  '1886',
  'Edwin L. Walter, who also designed City Hall, drew this castle-like jail, and the prisoners were moved in from the old building on Center Street in January 1887. It opened with 108 cells for men and 22 for women. It is still the county prison: a large expansion in 1999 raised its capacity to about 1,200.',
  look='A Victorian Gothic castle front of sandstone and brownstone (West Mountain stone), at 1371 North Washington Avenue. A working prison; nothing to see beyond the outside.',
  hook='',
  accn='A working county prison: look only from North Washington Avenue, do not photograph people and do not try to go in. Street parking; not checked.',
  links=[HARB],
  conf=None,th=None,thn=None,brick='no',hours=''),

N('scranton-preparatory-school','Scranton Preparatory School (International Correspondence Schools building)','Scranton','pane','civic','standing',41.41833,-75.65389,'site','view','drive','',
  '1921',
  'Built in 1921 to designs by W. Scott Collins as the second headquarters of the International Correspondence Schools, the mail-order school founded in Scranton; its Wikipedia article calls it the Women\'s Institute building. The Jesuit high school Scranton Prep, opened in 1944, moved here after 1961, and wings were added in 2005–2007.',
  look='A crenellated Tudor Revival tower modelled on Hampton Court\'s, in buff brick, at Wyoming Avenue and Ash Street. A working school; interior not open.',
  hook='',
  accn='A private school, 1000 Wyoming Avenue: look from the street. Street parking; not checked.',
  links=[SAH('35','Scranton Preparatory School (International Correspondence School)'),W('Scranton Preparatory School')],
  conf=None,th=None,thn=None,brick='no',hours=''),

N('lake-scranton-dam','Lake Scranton Dam','Roaring Brook Township (by Scranton)','pane','water','standing',41.37959,-75.63310,'site','public','walk','',
  '1898',
  'William Walker Scranton built the dam in 1898, forming the Burned Bridge Reservoir, which everyone calls Lake Scranton. It still holds drinking water for Scranton and belongs to Pennsylvania American Water.',
  look='The dam\'s big stonework at the south end of the reservoir, seen from the paved 3.57-mile walking loop round the lake. The gatehouse was not checked.',
  hook='',
  accn='Pennsylvania American Water land. The paved loop is open to walkers and runners, closed to cars and bicycles, and dogs are not allowed, to protect the water supply (Discover NEPA, the county visitors\' bureau). Parts near the dam have been closed for maintenance in some years. Free parking at the trailhead lot on PA 307; the dam is about 1.4 km round the loop.',
  links=[W('Lake Scranton'),L('Discover NEPA: Lake Scranton Walking Trail','https://discovernepa.com/listing/lake-scranton-walking-trail/')],
  conf=None,th=[41.38885,-75.62171],thn='Lake Scranton trail parking, PA 307',brick='?',hours=''),

]

PIN_NOTES={
 'lackawanna-county-courthouse-scranton':'From the City of Scranton landmark guide\'s coordinate for the courthouse.',
 'scranton-city-hall':'From the City of Scranton landmark guide\'s coordinate for the Municipal Building.',
 'albright-memorial-library-scranton':'From the City of Scranton landmark guide\'s coordinate for the library.',
 'lackawanna-college-central-high-scranton':'From the City of Scranton landmark guide\'s coordinate for the old Central High School.',
 'scranton-cultural-center-masonic-temple':'From the City of Scranton landmark guide\'s coordinate for the Masonic Temple.',
 'lackawanna-station-scranton':'From the City of Scranton landmark guide\'s coordinate for the station.',
 'scranton-iron-furnaces':'From the City of Scranton landmark guide\'s coordinate for the furnaces; the National Register point is about 50 m north.',
 'st-peters-cathedral-scranton':'From the City of Scranton landmark guide\'s coordinate for the cathedral.',
 'elm-park-church-scranton':'From the City of Scranton landmark guide\'s coordinate for Elm Park church.',
 'covenant-presbyterian-church-scranton':'From the City of Scranton landmark guide\'s coordinate for the church.',
 'st-matthews-lutheran-church-scranton':'From the City of Scranton landmark guide\'s coordinate for the church.',
 'scranton-armory':'From the City of Scranton landmark guide\'s coordinate for the armory.',
 'hotel-jermyn-scranton':'From the City of Scranton landmark guide\'s coordinate for the hotel.',
 'lackawanna-county-prison-scranton':'From the City of Scranton landmark guide\'s coordinate for the prison.',
 'scranton-preparatory-school':'From the Wikipedia article\'s coordinate for the school.',
 'lake-scranton-dam':'The dam as mapped on OpenStreetMap.',
}
