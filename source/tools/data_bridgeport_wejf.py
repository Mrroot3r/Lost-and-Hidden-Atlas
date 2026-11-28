# November 28, 2026: Bridgeport, Connecticut. A "videos" session (PROMPTS.md job 9): the names came from one video's tour
# of old Bridgeport buildings (the record is source/videos/20260130_5LQ7Pk4bYig.md); the video is a tip and nothing here
# rests on it. Sources read: Wikipedia (each article named in the links), the National Park Service record for the
# Bridgeport Downtown South Historic District, Historic Buildings of Connecticut (historicbuildingsct.com) for the Court
# Exchange Building, the Bridgeport Savings Bank and the First Baptist Church, the Barnum Museum's own page, the Cathedral
# Parish's page and St. John's own page for service times, and the Arcade's owner's page.
# Pins are address-lookup points (PointAddress) or a street corner, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'bridgeport_wejf','label':'Connecticut: old downtown Bridgeport','added':'2026-11-28 16:32'}

DT=' Downtown Bridgeport has metered street parking and pay lots; their owners and rates were not checked.'
DTS=['National Park Service record: Bridgeport Downtown South Historic District (1987)','https://npgallery.nps.gov/AssetDetail/NRIS/87001402']

PLACES=[
N('barnum-museum-bridgeport','Barnum Museum (Barnum Institute of Science and History)','Bridgeport','ctsw','civic','standing',41.17566,-73.18815,'exact','view','walk','','1893',
  'P. T. Barnum gave the land and the money for this building, which opened in February 1893 as the Barnum Institute of Science and History, home of the Bridgeport Scientific Society and the Fairfield County Historical Society. The city opened the Barnum Museum in it in 1936, used it as a city hall annex from 1946, and reopened it as a museum after a renovation in 1989. It was made a National Historic Landmark in 2023.',
  'A three-storey building of stone and terra cotta designed by Longstaff and Hurd, mixing Byzantine and Romanesque ideas, with a frieze by Henri Plasschaert along the top showing five scenes from American history. A 1989 addition and the Bridgeport Center complex are joined to it. The museum\'s page says the building has been through a tornado and two hurricanes and that the museum is working towards reopening in 2030, so it is seen from Main Street for now.',
  '',
  'Owned and run by the Barnum Museum, 820 Main Street. Closed to visitors while it is restored; its own page gives reopening in 2030 as the aim. Seen from the sidewalk.'+DT,
  [W('Barnum Museum'),['The Barnum Museum','https://barnum-museum.org/']],
  brick='?',arch='Longstaff and Hurd',archw='Wikipedia infobox, from the National Register nomination'),

N('mclevy-hall-bridgeport','McLevy Hall (old Bridgeport City Hall and county courthouse)','Bridgeport','ctsw','civic','standing',41.17662,-73.18995,'exact','view','walk','','1853–1854',
  'Bridgeport won the county seat from Fairfield by offering to pay for a courthouse and jail, and this building went up in 1853–1854 between State and Bank Streets at a cost of $75,000. It held the city hall on the ground floor, the county offices and courts on the two floors above, and a public hall, Washington Hall. The county courts moved out in 1888; it served as city hall into the 1930s and held city offices into the 1970s, and was renamed for Mayor Jasper McLevy in 1966.',
  'A Greek Revival building designed by Alexander Jackson Davis to look like a temple. News reports since 2022 describe city plans for its restoration and reuse; what has been done is not checked. Interior not checked.',
  '',
  'Owned by the City of Bridgeport, 202 State Street. Seen from State Street and McLevy Green.'+DT,
  [W('McLevy Hall'),['National Register nomination: Bridgeport City Hall (1977)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/77001387_text']],
  brick='?',arch='Alexander Jackson Davis; Joseph W. Northrop',archw='Wikipedia infobox, from the National Register nomination'),

N('fairfield-county-courthouse-bridgeport','Fairfield County Courthouse (Golden Hill Street, 1888)','Bridgeport','ctsw','civic','standing',41.18047,-73.19088,'exact','view','walk','','1888',
  'When the old city hall on State Street became too small for city and county together, Norwalk offered $100,000 to take the courthouse and a Bridgeport group that included P. T. Barnum offered $150,000. The county built here, to plans by the Bridgeport architect Warren R. Briggs, and the building opened in 1888. It is still a working state courthouse.',
  'A three-storey Richardsonian Romanesque building of brick with brownstone and terra cotta trim on a high granite base, with a six-storey tower capped by a pyramid roof in the middle of the front and crenellated turrets at the corners. Round-arched bays with granite columns flank the entrance. Interior not checked.',
  '',
  'A working state courthouse, 172 Golden Hill Street; people go in on court business, through security. Seen from Golden Hill Street.'+DT,
  [W('Fairfield County Courthouse (Bridgeport, Connecticut)')],
  brick='?',arch='Warren R. Briggs',archw='Wikipedia, from the National Register nomination'),

N('first-baptist-church-bridgeport','First Baptist Church (Washington Avenue)','Bridgeport','ctsw','worship','standing',41.17667,-73.19754,'exact','view','walk','','1893–1894',
  'The congregation was founded in 1837 with 39 members and grew into one of the city\'s largest Protestant churches. This, its third building, was designed by the local architect Joseph W. Northrop and built in 1893; a county history quoted by Historic Buildings of Connecticut says it was dedicated on October 28, 1894.',
  'A Richardsonian Romanesque church of red sandstone from East Haven, shaped like a long octagon, with a four-and-a-half-storey octagonal tower at the street corner holding the main door and lower towers at the other corners. The Register summary says the inside has changed little since a 1930 renovation and keeps its tile floor, plaster walls and oak pews. Interior not otherwise checked; no service times were found.',
  '',
  'Owned by the congregation, 126 Washington Avenue at West Avenue. No page of its own was found; seen from the street.',
  [W('First Baptist Church (Bridgeport, Connecticut)'),['Historic Buildings of Connecticut: First Baptist Church of Bridgeport (1893)','https://historicbuildingsct.com/first-baptist-church-of-bridgeport-1893/']],
  brick='no',bcol='none',hours='?',arch='Joseph W. Northrop',archw='Wikipedia and Historic Buildings of Connecticut'),

N('palace-majestic-theaters-bridgeport','Palace and Majestic Theaters and Savoy Hotel','Bridgeport','ctsw','civic','standing',41.18236,-73.19120,'exact','view','walk','','1921–1922',
  'Sylvester Z. Poli, who ran a chain of vaudeville houses across the Northeast, built two theaters and a hotel in one building in 1921–1922, to designs by the theater architect Thomas W. Lamb. The Palace seated 3,700 and the Majestic 2,600. The Majestic closed in 1971 and the Palace in 1975, and the whole building has stood empty since.',
  'A five-storey Beaux Arts building filling the block of Main Street between Congress and Arch Streets: brick and concrete made to look like granite on the front, mostly brick on the other sides. The hotel was at the front and the two auditoriums side by side behind it. Empty and decaying; the inside is shut. Seen from Main Street.',
  '',
  '1315–1357 Main Street; owner not checked. Closed and empty; look from the sidewalk only.',
  [W('Palace and Majestic Theaters')],
  brick='?',arch='Thomas W. Lamb',archw='Wikipedia, from the National Register nomination'),

N('bishop-arcade-bridgeport','Sterling Block and Bishop Arcade','Bridgeport','ctsw','civic','standing',41.17817,-73.18927,'exact','open','walk','','1841, 1850, 1889',
  'The north part of this block was built in 1841 for the Sterling Hotel, one of the oldest commercial buildings in the city, and the hotel added to it in 1850. In 1889 William D. Bishop enlarged it again and built a glass-roofed arcade through it from Main Street to the post office behind, the first indoor shopping mall in Connecticut. Its present owner calls it one of the few arcades of its time left in the country.',
  'A four-storey masonry block fifteen bays wide on Main Street, its outside much changed. The two-storey arcade inside keeps its glass roof and original iron columns, arches and scrollwork, now shops with apartments above.',
  '',
  'Privately owned (part of the City Trust Collection of shops and apartments), 993–1005 Main Street; the arcade is a shopping passage. Opening hours not checked.'+DT,
  [W('Sterling Block-Bishop Arcade'),['Time Equities: City Trust Collection, Arcade Mall','https://timeequities.com/properties/city-trust-collection-arcade-mall']],
  brick='?',hours='?'),

N('st-johns-episcopal-church-bridgeport','St. John\'s Episcopal Church (Fairfield Avenue)','Bridgeport','ctsw','worship','standing',41.17523,-73.19953,'exact','open','walk','','1873–1875',
  'The congregation began as an Anglican mission in 1738, one of the oldest Episcopal congregations in the state, and became a parish in 1784. This, its fourth church, was designed by James Renwick Jr. and built in 1873–1875; the chapel wing followed in 1886–1888, the rectory in 1903 and the parish hall in 1930.',
  'A Gothic Revival church of Greenwich granite with lighter Ohio stone trim and a slate roof banded in red slate. A square tower at the southeast corner has buttresses, a belfry and a pyramid cap with round corner turrets. The altar reredos, installed in 1913, is by the sculptor Gutzon Borglum. Interior otherwise not checked.',
  '',
  'Owned by the Episcopal parish, 768 Fairfield Avenue at Park Avenue. Sunday services in English, Spanish, and French and Creole (the parish\'s own page).',
  [W('St. John\'s Episcopal Church (Bridgeport, Connecticut)'),['St. John\'s Episcopal Church: parish ministries','https://saintjohnsbridgeport.org/parish-ministries']],
  th=[41.17524,-73.20022],thn='Lot on Fairfield Avenue',brick='no',bcol='none',hours='Sunday 8 and 10 a.m. (English), noon (Spanish), 5 p.m. (French and Creole)',arch='James Renwick Jr.',archw='Wikipedia, from the National Register nomination'),

N('united-congregational-church-bridgeport','United Congregational Church (now the Bridgeport Islamic Community Center)','Bridgeport','ctsw','worship','standing',41.17354,-73.19808,'exact','view','walk','','1926',
  'Built in 1926 for the reunited North and South Congregational churches, which had split from the town\'s 1695 congregation in the 19th century, it was one of the last churches built in the city before the Great Depression. The New York firm Allen and Collens designed it. The Bridgeport Islamic Community Center bought it in 2017.',
  'A two-storey Colonial Revival church with a cast stone portico of fluted columns and a sunburst pediment, three round-arched doorways, and a tower that rises from a brick clock stage through octagonal stages to a spire. Interior not checked.',
  '',
  'Owned by the Bridgeport Islamic Community Center, 703 State Street. Seen from the street.',
  [W('Bridgeport Islamic Community Center')],
  brick='?',arch='Allen and Collens',archw='Wikipedia, from the National Register nomination'),

N('st-augustine-cathedral-bridgeport','St. Augustine Cathedral','Bridgeport','ctsw','worship','standing',41.18024,-73.19576,'exact','open','walk','','1865–1868',
  'The parish was formed when St. James Church became too small. The cornerstone of this church was laid on August 28, 1865, and it was dedicated on St. Patrick\'s Day 1868. It became the cathedral of the new Diocese of Bridgeport in 1953.',
  'A Gothic Revival church first designed by Patrick C. Keely. A renovation finished in 2004 brought new marble floors, repainted ceilings and a new altar, and the pipe organ was rebuilt in 2014 with 42 ranks. Open for Mass; interior otherwise not checked.',
  '',
  'The cathedral of the Roman Catholic Diocese of Bridgeport, on Washington Avenue; part of the Cathedral Parish. Mass times from the parish\'s own page.',
  [W('St. Augustine Cathedral (Bridgeport, Connecticut)'),['The Cathedral Parish','https://thecathedralparish.org/']],
  th=[41.18000,-73.19764],thn='Lot on Calhoun Place',brick='?',hours='Sunday 7 and 10 a.m., 11:30 a.m. (Spanish), 2 p.m. (Vietnamese); weekdays 12:10 p.m.',arch='Patrick C. Keely',archw='Wikipedia infobox: Patrick C. Keely (original)'),

N('court-exchange-building-bridgeport','Court Exchange Building','Bridgeport','ctsw','civic','standing',41.17638,-73.19001,'exact','view','walk','','1896',
  'An office block built in 1896 by C. Barnum Seeley, a grandson of P. T. Barnum, who hired the architect George Longstaff; Historic Buildings of Connecticut says Longstaff\'s lavish plans drove the cost up. It stands beside McLevy Hall on State Street and is part of the Bridgeport Downtown South Historic District.',
  'An ornate five-bay commercial front on State Street. Interior not checked.',
  '',
  'Privately owned, 207–215 State Street. Seen from the street.'+DT,
  [['Historic Buildings of Connecticut: Court Exchange Building (1896)','https://historicbuildingsct.com/court-exchange-building-1896/'],DTS],
  brick='?',arch='George Longstaff',archw='Historic Buildings of Connecticut'),

N('bridgeport-savings-bank-1917','Bridgeport Savings Bank building (Main and State Streets)','Bridgeport','ctsw','civic','standing',41.17685,-73.18876,'site','view','walk','','1917',
  'The Bridgeport Savings Bank was chartered in 1842 and merged into People\'s Savings Bank in 1927. Its building at the corner of Main and State Streets was designed by Cass Gilbert and built in 1917. Historic Buildings of Connecticut says it is now a restaurant.',
  'A classical bank building on the corner, part of the Bridgeport Downtown South Historic District, whose National Park Service record names Cass Gilbert among its architects. Which corner and the present use are not confirmed on the ground; interior not checked.',
  '',
  'Privately owned, Main Street at State Street. Seen from the street.'+DT,
  [['Historic Buildings of Connecticut: Bridgeport Savings Bank (1917)','https://historicbuildingsct.com/?p=13358'],DTS],
  brick='?',conf='mixed',arch='Cass Gilbert',archw='Historic Buildings of Connecticut'),
]

PIN_NOTES={
 'barnum-museum-bridgeport':'Address lookup of 820 Main Street (a match on the house number).',
 'mclevy-hall-bridgeport':'Address lookup of 202 State Street (a match on the house number).',
 'fairfield-county-courthouse-bridgeport':'Address lookup of 172 Golden Hill Street (a match on the house number).',
 'first-baptist-church-bridgeport':'Address lookup of 126 Washington Avenue (a match on the house number).',
 'palace-majestic-theaters-bridgeport':'Address lookup of 1315 Main Street (a match on the house number).',
 'bishop-arcade-bridgeport':'Address lookup of 1001 Main Street (a match on the house number).',
 'st-johns-episcopal-church-bridgeport':'Address lookup of 768 Fairfield Avenue (a match on the house number).',
 'united-congregational-church-bridgeport':'Address lookup of 703 State Street fell on the street corner; moved about 30 m onto the church with the tower that the aerial shows.',
 'st-augustine-cathedral-bridgeport':'Address lookup of 399 Washington Avenue fell in a parking lot; moved about 60 m onto the large church building that the aerial shows, which is also where Wikipedia puts the cathedral.',
 'court-exchange-building-bridgeport':'Address lookup of 211 State Street (a match on the house number).',
 'bridgeport-savings-bank-1917':'The corner of Main and State Streets; the source names the corner but not which of the four buildings, so the pin marks the crossing.',
}
