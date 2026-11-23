# November 23, 2026: Canton, Ohio. A "videos" session (PROMPTS.md job 9): the names came from one video's tour of
# old Canton buildings (the record is source/videos/20250117_ky7yvCYNKx8.md); the video is a tip and nothing here
# rests on it. Sources read: Wikipedia (each article named in the links), the National Register list for Stark County,
# the National Register form for the architecture of Guy Tilden in Canton, the Clio walking-tour page for the Hotel
# Courtland, a Repository article on the Masonic Temple's centenary, and for hours the pages of whoever runs each place
# (the First Ladies museum and the National Park Service, the Basilica parish and the Diocese of Youngstown, the Palace
# Theatre). Pins are ArcGIS address points or Register points, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'canton_pknj','label':'Ohio: old Canton, McKinley\'s town','added':'2026-11-23 04:32'}

DT=' OpenStreetMap maps several parking lots within a few hundred metres downtown; their owners, hours and fees were not checked.'

PLACES=[

N('stark-county-courthouse-canton','Stark County Courthouse','Canton','oh','civic','standing',40.79891,-81.37517,'exact','view','walk','','1870s; rebuilt 1895',
  'The county courthouse on Canton\'s central square. Cleveland architect George F. Hammond redesigned it in Beaux-Arts style in 1895, building around an older courthouse put up in the 1870s; part of the old building\'s corner towers was removed in the work. The courthouse and its annex are on the National Register.',
  'The clock tower carries statues of trumpeting angels. Interior and public hours not checked.',
  '',
  'Owned by Stark County, on the square at Market Avenue and Tuscarawas Street; seen from the surrounding streets and Central Plaza.'+DT,
  [W('Stark County Courthouse (Ohio)')],
  brick='?'),

N('mckinley-national-memorial','McKinley National Memorial','Canton','oh','burial','standing',40.8075,-81.39322,'exact','public','walk','','1905–1907',
  'The tomb of President William McKinley, shot in 1901, and of his wife Ida. Harold Van Buren Magonigle of New York won a competition of over sixty designs; work began on June 6, 1905, and President Theodore Roosevelt spoke at the dedication on September 30, 1907. The state took it over in 1943 and the Stark County Historical Society in 1973; it was rededicated in 1992 after five years of restoration.',
  'A domed mausoleum on a hill, reached by 108 steps in four flights, 50 feet wide, on built-up terraces. Inside, walls of Tennessee marble and the double green granite sarcophagi of the President and Ida McKinley; at the foot of the steps a 9-and-a-half-foot bronze of McKinley giving his last speech, by Charles Henry Niehaus. The long reflecting pool that once formed the sword\'s handle in the design was filled in in 1951. National Historic Landmark.',
  '',
  'Run by the Stark County Historical Society, which also runs the McKinley Presidential Library and Museum beside it, at 800 McKinley Monument Drive NW. The society\'s own page asked for a browser check and could not be read when this was written, so the memorial\'s opening hours were not checked; the nearest lot OpenStreetMap maps is about 400 m south on Elgin Avenue, at Waterworks Park.',
  [W('McKinley National Memorial')],
  brick='?',hours='?'),

N('crossroads-umc-canton','First Methodist Episcopal Church (Crossroads United Methodist)','Canton','oh','worship','standing',40.79844,-81.37636,'exact','view','walk','','1881',
  'A High Victorian Gothic church of 1881, McKinley\'s own church: he was a trustee and Sunday school superintendent, and his funeral was held here on September 19, 1901, with President Roosevelt in the second pew and McKinley\'s own pew draped in black. Renamed Church of the Savior in 1968, it became Crossroads United Methodist in 2014 when its congregation merged with St. Paul\'s. On the National Register since 1979.',
  'A Gothic church downtown, still used by its congregation. Interior not checked.',
  '',
  'An active church at 120 Cleveland Avenue SW; seen from the street. Its own page could not be opened when this was written, so service times were not checked.'+DT,
  [W('Crossroads United Methodist Church')],
  brick='?'),

N('basilica-st-john-baptist-canton','Basilica of St. John the Baptist','Canton','oh','worship','standing',40.80322,-81.37735,'exact','open','walk','','1871',
  'A Catholic church designed by James Renwick Jr., finished in 1871 and dedicated in 1872, for a parish founded in 1823 and called the oldest Catholic parish in northeastern Ohio. It was made a minor basilica on June 19, 2012. In 2024 the parish merged with St. Peter\'s nearby.',
  'A Gothic Revival church with a 79-rank pipe organ by Kegg of Hartville. Open for Mass; other visiting hours not checked.',
  '',
  'An active church at 627 McKinley Avenue NW; the parish office is at St. Peter\'s, 726 Cleveland Avenue NW, weekdays 8 a.m. to 4 p.m. Mass times are from the parish\'s own page as read in November 2026; the diocese\'s page says the Saturday and Sunday Masses move between the two churches with the seasons, so check before going.'+DT,
  [W('Basilica of St. John the Baptist (Canton, Ohio)'),['Basilica of St. John the Baptist and St. Peter Parish','https://www.sjbspcanton.org/'],['Diocese of Youngstown: the Basilica','https://doy.org/location/basilica-of-st-john-the-baptist-canton']],
  brick='?',hours='Mass Tuesday 6 p.m., Thursday noon, Saturday 4 p.m., Sunday 10:30 a.m. (the parish page, November 2026)'),

N('first-ladies-nhs-saxton-house','First Ladies National Historic Site: Saxton McKinley House','Canton','oh','landmark','standing',40.7966,-81.37558,'site','open','walk','','1841; 1865',
  'The brick Victorian house where Ida Saxton McKinley was born and grew up, built in 1841 and altered in 1865; William McKinley lived here with her for over twenty years while a Canton lawyer and congressman. Since 2000 it has been one half of a National Historic Site for all the First Ladies; the other half is the museum and visitor centre in the 1895 City National Bank Building at 205 Market Avenue South.',
  'Three floors of the house are seen on a guided tour of about 50 minutes, ranger-led, first come first served for the first 15 at each time. The bank building has three floors of exhibits open free, with a small copy of the first White House library.',
  '',
  'Run by the National First Ladies\' Library with the National Park Service. All tours start at the museum, 205 Market Avenue South, not at the house. Hours from the museum\'s page as read in November 2026; the Park Service says the site opens seasonally.'+DT,
  [W('First Ladies National Historic Site'),['First Ladies Library and Museum: visit','https://firstladies.org/visit'],['National Park Service: Saxton House tours','https://www.nps.gov/fila/planyourvisit/saxton-house-tours.htm']],
  th=[40.79759,-81.37525],thn='Museum and visitor centre, 205 Market Avenue South (tours start here)',
  brick='?',hours='Tuesday to Saturday 9 a.m. to 4 p.m.; house tours 10 a.m., noon and 2 p.m.'),

N('canton-public-library-1903','Canton Public Library (Carnegie building)','Canton','oh','civic','standing',40.79726,-81.37679,'exact','view','walk','','1903',
  'Canton\'s Carnegie library, built in 1903 to the design of Guy Tilden, who won the competition for it. It was said in 1973 to be among the Tilden designs most admired by architects. The library moved out in 1978 and the building became law offices. On the National Register since 1982.',
  'Pressed grey brick, with Greek Ionic columns either side of a recessed entrance that opens into a central rotunda. Interior not checked; offices.',
  '',
  'Private offices; seen from the street.'+DT,
  [W('Canton Public Library'),['National Register form: the architecture of Guy Tilden in Canton','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/64000606_text']],
  brick='no'),

N('hotel-courtland-entrance-canton','Hotel Courtland entrance arch','Canton','oh','hotel','ruins',40.79874,-81.37584,'site','view','walk','','1905–1992',
  'A seven-storey Classical Revival hotel of 1905 by Guy Tilden. Jim Thorpe was a regular, and it was said to be the scene of one of the meetings that led to the National Football League. Later the St. Francis Hotel and then the Stark County Office Building, it was listed on the National Register in 1987 and torn down in 1992 for an underground parking garage.',
  'Only the main entrance was left standing on the site.',
  '',
  'On the street at 209 West Tuscarawas Street, beside the courthouse square; seen from the sidewalk. Its present state was not checked on the ground.'+DT,
  [W('Hotel Courtland'),['Clio: Hotel Courtland','https://theclio.com/tour/1357/3'],['National Register form: the architecture of Guy Tilden in Canton','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/64000606_text']],
  conf='mixed',brick='?'),

N('canton-masonic-temple','Canton Masonic Temple','Canton','oh','civic','standing',40.80477,-81.37206,'exact','view','walk','','1924–1926',
  'A four-storey Masonic temple begun in 1924 and finished two years later; it was dedicated on November 9, 1924, and rededicated for its hundredth year in April 2024. Five Masonic bodies share it, among them William McKinley Lodge 431 and the Scottish Rite.',
  'A buff-coloured front with tall columns across the upper floors (Wikimedia Commons photograph). The largest room, the Cathedral room, has theatre seating for 812, and there is a grand ballroom below ground. Inside only for members\' events or rentals.',
  '',
  'Privately owned, 836 Market Avenue North; seen from the street. Rooms can be rented for events.'+DT,
  [['The Repository (via Yahoo News): Canton Masonic Temple, 100 years','https://www.yahoo.com/news/canton-masonic-temple-100-years-210954409.html']],
  brick='no'),

N('palace-theatre-canton','Canton Palace Theatre','Canton','oh','civic','standing',40.80208,-81.37361,'exact','open','walk','','1926',
  'An atmospheric movie palace by John Eberson, opened in November 1926 with money from Harry Ink, whose sore-throat remedy Tonseline had a bandaged giraffe as its sign; a giraffe went into the decoration. It held films, vaudeville and stage shows and was listed on the National Register in 1979.',
  'Brick with terracotta, a Churrigueresque front of pinnacles round a tall vertical sign and marquee. Inside, a garden-themed auditorium for 1,509 under a ceiling of stars and dawn, and a Kilgen theatre organ, restored in 1992, still played for silent films.',
  '',
  'Run as a theatre, 605 Market Avenue North; inside for shows. Box office hours from the theatre\'s page as read in November 2026.'+DT,
  [W('Palace Theatre (Canton, Ohio)'),['Canton Palace Theatre','https://cantonpalacetheatre.org/']],
  brick='?',hours='Box office opens 1 hour before a performance until 30 minutes into it, on performance days'),

N('trinity-lutheran-church-canton','Trinity Lutheran Church (former)','Canton','oh','worship','standing',40.79919,-81.37768,'exact','view','walk','','1886',
  'A sandstone church of 1886, the oldest surviving Canton design of Guy Tilden, for an English-speaking congregation founded in 1838. Its members voted to close it in late 2010, when about thirty came on a Sunday, and a developer bought it in 2012 to make a wedding chapel. On the National Register since 1985.',
  'Romanesque Revival with Gothic touches: a 60-foot stone bell tower with a steep pyramid roof, a porte-cochere, and arched stained glass windows with tracery; "A Mighty Fortress is Our God" is cut into the stone. Its present use and the interior not checked.',
  '',
  'Privately owned, 415 West Tuscarawas Street; seen from the street.'+DT,
  [W('Trinity Lutheran Church (Canton, Ohio)'),['National Register form: the architecture of Guy Tilden in Canton','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/64000606_text']],
  brick='no'),

]

PIN_NOTES={
'stark-county-courthouse-canton':'Address point for 115 Central Plaza North, on the courthouse.',
'mckinley-national-memorial':'Moved about 110 m north-west from the National Register point, which fell on the plaza at the foot of the steps, onto the domed memorial seen on the aerial.',
'crossroads-umc-canton':'Address point for 120 Cleveland Avenue SW, on the church.',
'basilica-st-john-baptist-canton':'Address point for 627 McKinley Avenue NW, on the church.',
'first-ladies-nhs-saxton-house':'Address point for 331 Market Avenue South, at the Saxton House corner; which of the small buildings by the pin is the house was not settled on the aerial. The second point is the museum where tours start.',
'canton-public-library-1903':'Address point for 236 Third Street SW, which agrees with the National Register point to within 30 m.',
'hotel-courtland-entrance-canton':'Street address point for 209 West Tuscarawas Street, not a point on the arch itself; the arch was not picked out on the aerial.',
'canton-masonic-temple':'Address point for 836 Market Avenue North, on the temple.',
'palace-theatre-canton':'Address point for 605 Market Avenue North, on the theatre.',
'trinity-lutheran-church-canton':'Address point for 415 West Tuscarawas Street, on the church.',
}
