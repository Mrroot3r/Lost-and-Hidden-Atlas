# November 23, 2026: a second scatter across Mississippi (batch ms_ihap), claimed with tools/choose.py --thinnest when
# Mississippi had 36 places. It fills ground the first two batches left empty: the northeast corner (Corinth, Jacinto,
# Tupelo), the Natchez Trace at French Camp, Natchez town itself, the Delta (Greenwood, Clarksdale, Rosedale), the
# central hills (Oxford's country, Winston County, Raymond, Hazlehurst) and the Meridian country.
# Sources were opened in this session: Wikipedia as raw text, the National Register lists by county, SAH Archipedia
# (Buildings of Mississippi), National Park Service pages (Natchez National Historical Park hours and fees, the
# Natchez Trace's French Camp page, Shiloh's Verandah House page), the American Battlefield Trust, HMdb.org marker
# pages, the Elvis Presley Birthplace's own site, the Delta Blues Museum's visitor page, the Register nomination for
# Stuckey's Bridge, Hill Country History (Jacinto) and Mississippi Preservation (Hopewell).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'ms_ihap','label':'Mississippi: Natchez, the northeast hills, the Delta and the Trace','added':'2026-11-23 02:23'}

PLACES=[
# ---- Northeast corner ----
N('verandah-curlee-house-corinth','Verandah-Curlee House','Corinth','ms','landmark','standing',34.937,-88.52094,'site','open','drive','','1857',
'A Greek Revival house built in 1857 by Hamilton Mask, a surveyor and one of the founders of Corinth, and later home to the '
'Curlee family, clothing manufacturers. In the Civil War no fewer than five generals made it their headquarters, among them '
'Braxton Bragg, Henry Halleck and John B. Hood. It is one of four Corinth houses drawn in an artist\'s sketchbook of 1860 that '
'still stand.',
look='Wraparound verandas on three sides with three porticos of slender chamfered columns, stuccoed walls and a parapet; a small '
'1850s wooden cottage stands beside it. Inside, the drawing room has pilasters carrying a decorated entablature. The house is '
'kept as a museum with Audubon prints, antiques and a display of replica soldiers\' furnishings (American Battlefield Trust). '
'Interior not checked.',
accn='705 Jackson Street (a Commons photograph gives 711). SAH Archipedia (Buildings of Mississippi, 2021) says it is open as a house museum; no page of the '
'house\'s own could be read (the web address that sources give for it now carries unrelated pages), so hours were not checked. '
'Street parking.',
links=[L('SAH Archipedia: Mask-Curlee House (Verandah House)','https://sah-archipedia.org/node/86845'),
       L('NPS: Verandah House (Corinth tour stop)','https://www.nps.gov/places/corinth-tour-1-stop-5-verandah-house.htm'),
       L('American Battlefield Trust: The Verandah-Curlee House','https://www.battlefields.org/visit/heritage-sites/verandah-curlee-house')],
brick='some',hours='?'),

N('jacinto-courthouse','Jacinto Courthouse','Rienzi','ms','civic','standing',34.76099,-88.42853,'site','view','drive','','1854',
'The red-brick Federal courthouse of old Tishomingo County, built in 1854 for just under $7,000 to designs of J. J. Blythe. '
'Jacinto, founded in 1836 at the middle of the huge county, lost the county seat in 1870 when the county was split in three, '
'and the railroad went to Corinth and Iuka instead; the town dwindled to a crossroads (52 people in 2020). The courthouse '
'was a school until 1908 and a church until 1960, decayed and lost its cupola, and was restored from 1969 by the Jacinto '
'Historic Foundation.',
look='A two-story red-brick building with a hipped roof of cypress shingles, a rebuilt cupola, wooden window lintels with corner '
'blocks and twelve-over-twelve sash. SAH Archipedia says the interiors are largely intact, the second-floor courtroom included. '
'Round the square: a wooden store of about 1900 (now a museum and store), a small early log building, a doctor\'s office of '
'about 1873 moved from Alabama, and the 1930 Jacinto School.',
accn='Jacinto Historic Foundation, at Mississippi Highway 364 and 360. Wikipedia says the courthouse is open to visitors, but no '
'page of the foundation with days or hours was found, so it is marked look-from-the-road. Parking by the square.',
links=[W('Jacinto, Mississippi'),L('SAH Archipedia: Jacinto Courthouse','https://sah-archipedia.org/node/86827'),
       L('Hill Country History: Jacinto Courthouse (1854)','https://hillcountryhistory.org/2018/04/09/jacinto-courthouse-1854/')],
brick='yes'),

N('elvis-presley-birthplace-tupelo','Elvis Presley Birthplace','Tupelo','ms','landmark','standing',34.25997,-88.67996,'site','open','drive','','1934–1935',
'The two-room shotgun house built by Vernon Presley with his father and brother, where Elvis Presley was born on January 8, '
'1935; his twin brother was stillborn. The family lost the house for lack of payment when Elvis was a few years old. A tornado '
'in 1936 that killed hundreds near Tupelo spared it. The 15-acre park round it also holds the plain frame Assembly of God '
'church where the family worshipped, moved here, a museum and a chapel.',
look='The small frame house on its original lot, the moved wooden church (with a multimedia re-creation of a 1940s service), the '
'museum, the chapel and two statues of the young Elvis. On the Mississippi Blues Trail. Interior of the house not checked.',
accn='Elvis Presley Birthplace, 306 Elvis Presley Drive. Tickets at the welcome '
'center only: all three buildings $25, any one $12, children 7 to 12 from $5; the ticket office closes at 3 p.m. The grounds '
'are open 24 hours. Hours and prices from the birthplace\'s own site, read November 2026. Parking on the grounds.',
links=[W('Elvis Presley Birthplace'),L('Elvis Presley Birthplace (official site)','https://www.elvispresleybirthplace.com')],
brick='?',hours='Monday to Saturday 9 a.m. to 4 p.m., Sunday 1 to 4 p.m. (ticket office closes 3 p.m.); grounds open 24 hours'),

# ---- Natchez Trace ----
N('french-camp-historic-village','French Camp Historic Village','French Camp','ms','town','standing',33.29525,-89.3997,'site','view','walk','','c. 1840–1855 (buildings); stand c. 1812',
'Louis LeFleur kept a stand, a trading post and inn, on the Natchez Trace here from about 1812; his nationality gave the place '
'its name, and his son Greenwood Leflore, a Choctaw chief and state senator, gave his to Greenwood and Leflore County. The '
'village by the Parkway was put together from 1975: old log and frame buildings of Choctaw County and its neighbours moved '
'onto one site.',
look='The Huffman log cabin (about 1840), a double-pen dogtrot with dovetailed corners moved here in 1975; the Colonel James '
'Drane House (about 1846), a two-story dogtrot I-house moved in 1981, with Federal-style woodwork inside and its brick end '
'chimneys rebuilt; the board-and-batten French Camp post office of 1848 to 1964; a saddle-notched log barn; a sorghum mill; '
'and a hewn-timber house of about 1855 used as a museum. A boardwalk links them (SAH Archipedia). Interiors not checked.',
accn='Natchez Trace Parkway milepost 180.7, where the National Park Service has a parking area and a panel on the LeFleur stand. '
'Who owns the village and when its buildings open was not found on a page read for this entry, so it is marked look-only.',
links=[L('NPS: French Camp (Natchez Trace Parkway)','https://www.nps.gov/places/french-camp.htm'),
       L('SAH Archipedia: French Camp Historic Village','https://sah-archipedia.org/node/86678'),W('French Camp, Mississippi')],
brick='some'),

# ---- Natchez ----
N('melrose-natchez','Melrose','Natchez','ms','landmark','standing',31.54309,-91.38306,'site','open','drive','','begun after 1840',
'A 15,000-square-foot Greek Revival mansion that the lawyer and planter John T. McMurran, who held enslaved people, began '
'planning after the great tornado of 1840, to designs of the Maryland architect Jacob Byers. Grief and Civil War losses made '
'him sell it, with its furniture, in 1865. Because each owner sold the house furnished, it was one of the most intact '
'antebellum estates in the South when the National Park Service bought the 80-acre estate in 1990.',
look='The house is furnished for the years just before the Civil War, many second-floor bedrooms with their original '
'furniture. On the grounds: a two-story kitchen and a dairy, octagonal cistern houses, a smokehouse, a privy, a barn, a '
'carriage house, and one of the last slave quarters left in Natchez. A National Historic Landmark.',
accn='Natchez National Historical Park (National Park Service). Grounds, outbuildings and '
'gardens are free. House tours must be booked on Recreation.gov: the hours page says $11, the fees page $10 for adults plus '
'a $1 booking fee; 17 and under free. Closed Thanksgiving, Christmas and New Year\'s Day. From nps.gov, read November 2026. '
'Parking on the estate.',
links=[W('Melrose (Natchez, Mississippi)'),L('NPS: Natchez NHP hours','https://nps.gov/natc/planyourvisit/hours.htm'),
       L('NPS: Natchez NHP fees','https://www.nps.gov/natc/planyourvisit/fees.htm')],
conf='mixed',brick='?',hours='Daily 8:30 a.m. to 5 p.m.; house tours 10 and 11 a.m., 2, 3 and 4 p.m. (book on Recreation.gov)'),

N('william-johnson-house-natchez','William Johnson House','Natchez','ms','landmark','standing',31.56004,-91.40578,'site','open','walk','','1840–1841',
'The town house of William Johnson, a free Black man known as the Barber of Natchez, built in 1840 with bricks salvaged from '
'buildings the tornado of that year had destroyed. It is part of Natchez National Historical Park.',
look='A brick house at 210 State Street downtown. The first-floor visitor center and exhibit hall reopened on September 1 '
'(the park page does not give the year); the family\'s rooms on the second floor were still closed when the page was read.',
accn='Natchez National Historical Park (National Park Service), 210 State Street. Free. Closed Thanksgiving, Christmas and New '
'Year\'s Day. Hours from the park\'s hours page, read November 2026. Street parking downtown.',
links=[W('William Johnson House (Natchez, Mississippi)'),L('NPS: Natchez NHP hours','https://nps.gov/natc/planyourvisit/hours.htm')],
brick='yes',hours='Daily 8:30 a.m. to 5 p.m. (first floor only; second floor closed)'),

N('kings-tavern-natchez','King\'s Tavern','Natchez','ms','hotel','standing',31.5602,-91.3992,'exact','view','walk','','1769 or c. 1798',
'Counted among the oldest buildings in Natchez, though its date is not settled: Wikipedia gives 1769 and says it began as a '
'blockhouse for the British fort, built partly of timbers from broken-up ships and flatboats; SAH Archipedia gives about 1798, '
'when Richard King bought the lot, and says he took his first tavern licence in 1799. The Pilgrimage Garden Club bought and '
'restored it in 1970, and it has been a tavern and restaurant under several owners since.',
look='A side-gabled frame building with beaded siding, an outside brick chimney, chamfered gallery posts and board-and-batten '
'doors; a raised basement was put under it when the street was cut down. Wikipedia said in 2022 that it was closed and for '
'sale; whether it is open now was not checked.',
accn='Private, 613 Jefferson Street. Look from the street; whether it now serves the public was not checked. Street parking.',
links=[W("King's Tavern"),L('SAH Archipedia: King\'s Tavern','https://sah-archipedia.org/node/87128')],
conf='mixed',brick='?'),

# ---- Delta ----
N('fort-pemberton-greenwood','Fort Pemberton','Greenwood','ms','fort','traces',33.53067,-90.23415,'area','public','walk','','1863',
'In March 1863 Confederate troops under W. W. Loring stopped Grant\'s Yazoo Pass expedition here, on a neck of land where the '
'Tallahatchie bends east. The fort was thrown up of cotton bales and logs covered with earth, and the old steamer Star of the '
'West was sunk in the channel. Union ironclads attacked on March 11, 14, 16 and 23 and were driven off, ending that route to '
'Vicksburg.',
look='Fort Pemberton Memorial Park takes in part of the fort. A county marker of 1958 said some of the original breastworks '
'could easily be recognized there; whether they still show was not checked. A state marker of 1976 at the park is missing, '
'its post left standing (HMdb).',
accn='Fort Pemberton Memorial Park, on US 49E at Levee Road west of Greenwood (HMdb). Leflore County put up the 1958 marker; '
'Wikipedia and HMdb call it Fort Pemberton Memorial Park, a public memorial park; who owns and runs it now and its hours were not checked. Parking was not checked.',
links=[W('Fort Pemberton (Mississippi)'),L('HMdb: Fort Pemberton Park','https://www.hmdb.org/m.asp?m=77329'),
       L('HMdb: Fort Pemberton (missing marker)','https://www.hmdb.org/m.asp?m=132320')],
conf='mixed',brick='no'),

N('delta-blues-museum-clarksdale','Delta Blues Museum (Clarksdale passenger depot)','Clarksdale','ms','rail','standing',34.20024,-90.57327,'site','open','drive','','1926',
'The Yazoo and Mississippi Valley (Illinois Central) passenger depot of 1926, listed on the National Register in 1995, now '
'houses the Delta Blues Museum. Clarksdale grew as a hub where Highways 61 and 49 met and several railroads kept depots.',
look='The museum holds blues instruments and memorabilia, art, and the cabin from Stovall Plantation where Muddy Waters is said '
'to have lived as a young man, rebuilt inside. A Mississippi Blues Trail marker stands outside. Original fabric of the depot '
'not checked.',
accn='Delta Blues Museum, in the old depot. Adults (17 and over) $15, 6 and under free; closed on New Year\'s, Martin Luther King Day, '
'Memorial Day, July 4, Labor Day, Thanksgiving, Christmas Eve and Christmas. From the museum\'s visitor page, read November '
'2026. Parking by the depot.',
links=[W('Delta Blues Museum'),L('Delta Blues Museum: visitor info','https://www.deltabluesmuseum.org/visitor-info.aspx')],
brick='?',hours='Monday to Saturday 10 a.m. to 5 p.m., last admission 4:30 p.m.'),

N('grace-episcopal-rosedale','Grace Episcopal Church','Rosedale','ms','worship','standing',33.86026,-91.02753,'site','view','drive','','1879',
'A Carpenter Gothic church built in 1879 for a congregation founded in 1875 under Bishop William M. Green. It is the oldest '
'church still standing in Bolivar County, with much of its original detail intact; the state put up a marker in 1987.',
look='The wooden Gothic church at 203 Main Street, in the Rosedale Historic District. Interior not checked.',
accn='Episcopal parish. No page with service times was found. Look from Main Street; street parking.',
links=[W('Grace Episcopal Church (Rosedale, Mississippi)')],
brick='no'),

# ---- Central hills ----
N('hinds-county-courthouse-raymond','Hinds County Courthouse, Raymond','Raymond','ms','civic','standing',32.26028,-90.42333,'site','view','drive','','1857–1859',
'Built in 1857 to 1859 by the Weldon Brothers with skilled enslaved labour, and praised in 1858 as "a triumph of their skill." '
'After the Battle of Raymond in May 1863 Union troops took down the Confederate flags on the cupola and raised their own, and '
'the courthouse served as a hospital for Confederate wounded. It still works as a chancery and tax office for the south and '
'west of the county.',
look='A plain Greek Revival block with four porticos of simplified Doric columns, iron balconies over the doors, stucco scored '
'to look like stone over brick walls, and an octagonal cupola rebuilt in 1949. The second-floor courtroom survives. An early '
'iron picket fence with two stepped stiles rings the square; the bronze Confederate soldier is of 1908. Opposite, St. Mark\'s '
'Episcopal Church (1854 to 1855).',
accn='Hinds County, 127 West Main Street. A working county office: its office hours were not checked. Look from the square; '
'street parking.',
links=[W('Hinds County Courthouse (Raymond, Mississippi)'),L('SAH Archipedia: Hinds County Courthouse, Raymond','https://sah-archipedia.org/node/86804'),
       L('American Battlefield Trust: Raymond Courthouse','https://www.battlefields.org/visit/heritage-sites/raymond-courthouse')],
brick='no'),

N('hazlehurst-depot','Illinois Central Railroad Passenger Depot (Hazlehurst Depot Museum)','Hazlehurst','ms','rail','standing',31.86113,-90.39444,'site','view','drive','','1925',
'The Illinois Central passenger depot of 1925, listed on the National Register. Amtrak\'s City of New Orleans still stops at a '
'small shelter beside it, and the old depot holds the Hazlehurst Depot Museum.',
look='The 1925 depot by the tracks in downtown Hazlehurst. Original fabric and the museum\'s rooms not checked.',
accn='Museum in the depot; no page of its own with hours was found, so it is marked look-from-the-street. The tracks are an '
'active main line: stay off them. Street parking.',
links=[W('Hazlehurst station')],
brick='yes'),

N('stuckeys-bridge-ms','Stuckey\'s Bridge','Meridian','ms','landmark','standing',32.25556,-88.85528,'site','view','drive','','1901 (crossing from about 1850)',
'A single-span iron through truss, 112 feet long, over the Chunky River southwest of Meridian, put up in 1901 by the Virginia '
'Bridge and Iron Company where a bridge had stood since about 1850 (a contract of 1847 survives). The Register form calls its '
'truss rare, fitting no known type but close to the Fink and Stearns patterns. A legend tells of an innkeeper named Stuckey '
'who robbed and killed his guests and was hanged from the bridge, and the river is said to be haunted.',
look='The iron truss on the county road over the Chunky River. A Mississippi Landmark (1984) and on the National Register (1988). '
'Whether it is still open to cars was not checked.',
accn='Lauderdale County road. Look from the road or the bridge approach; parking room was not checked.',
links=[W("Stuckey's Bridge"),L('National Register nomination (NPS)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/88002415_text')],
brick='no'),

N('zion-baptist-collinsville','Zion Baptist Church','Collinsville','ms','worship','standing',32.60889,-88.88139,'site','view','drive','','1910–1911',
'A Carpenter Gothic country church of 1910 to 1911, put on the National Register in 2002 for the quality of its detail and how '
'little it has changed. It replaced an earlier church on the site.',
look='The frame church on a six-acre lot with a cemetery holding immigrants from England, Scotland and Ireland from about 1860 '
'on; a separate African-American cemetery tied to the church lies outside the listed ground. Interior not checked.',
accn='Church property; no page with service times was found. Look from the road.',
links=[W('Zion Baptist Church (Collinsville, Mississippi)')],
brick='no'),

N('baptist-church-of-christ-sardis','The Baptist Church of Christ at Sardis','Louisville','ms','worship','standing',33.05528,-88.85361,'site','view','drive','','1917',
'A one-room country church built in 1917 for the Baptist Church of Christ, a denomination now nearly gone. Its timber was cut in '
'the neighbourhood and milled on the spot. It was put on the National Register in 2011 and is kept as a historic site and '
'family-history centre with its cemetery.',
look='A one-room frame church with two front doors set side by side; the pews and pulpit are original, as is most of the '
'building. Cemetery beside it. Interior not checked.',
accn='Owner not checked; no page with opening times was found. Look from the road.',
links=[W('The Baptist Church of Christ at Sardis')],
brick='no'),


N('hopewell-presbyterian-oxford','Hopewell Presbyterian Church','Oxford','ms','worship','standing',34.39361,-89.41139,'site','view','drive','','c. 1849',
'A plain gable-front frame church built about 1849 to replace a log church that burned that year. Its members included white '
'families and enslaved Black people. The congregation was dissolved in 1981, and the church stands on the grounds of Camp '
'Hopewell, set up on the property in 1951.',
look='Listed in 1999 because it keeps its original framing, weatherboards, windows and paired front doors. Interior not checked.',
accn='Camp Hopewell grounds, private. Ask the camp before going in; otherwise look from the public road if it can be seen.',
links=[W('Hopewell Presbyterian Church (Oxford, Mississippi)'),
       L('Preservation in Mississippi: Hopewell Presbyterian Church','https://misspreservation.com/2015/04/21/suzassippis-mississippi-hopewell-presbyterian-church-in-lafayette-county/')],
brick='no'),
]

PIN_NOTES={
'verandah-curlee-house-corinth':'OpenStreetMap point for the Verandah Curlee House museum.',
'jacinto-courthouse':'ArcGIS geocoder point for the Jacinto Courthouse, on the square; which of the buildings there is the courthouse was not told apart on the aerial.',
'elvis-presley-birthplace-tupelo':'Wikipedia coordinate, in the park among trees; the small house was not picked out on the aerial.',
'french-camp-historic-village':'OpenStreetMap point for French Camp Historic Village.',
'melrose-natchez':'Wikipedia coordinate.',
'william-johnson-house-natchez':'ArcGIS geocoder point for the museum and its address, 210 State Street; the Wikipedia coordinate is about 1.3 km east, in woods.',
'kings-tavern-natchez':'Wikipedia coordinate.',
'fort-pemberton-greenwood':'Position of the missing 1976 state marker from HMdb, at the park; on the aerial the point is on US 49E beside the woods by the river, and no earthwork can be seen.',
'delta-blues-museum-clarksdale':'ArcGIS geocoder point for the Delta Blues Museum; the Wikipedia coordinate falls on the tracks east of it.',
'grace-episcopal-rosedale':'ArcGIS geocoder point for 203 Main Street; the Wikipedia coordinate is about 450 m south.',
'hinds-county-courthouse-raymond':'Wikipedia coordinate.',
'hazlehurst-depot':'ArcGIS geocoder point for the Hazlehurst Depot Museum, by the tracks.',
'stuckeys-bridge-ms':'Wikipedia coordinate, on the river; the bridge itself is hidden by trees on the aerial.',
'zion-baptist-collinsville':'Wikipedia coordinate.',
'baptist-church-of-christ-sardis':'Wikipedia coordinate.',
'hopewell-presbyterian-oxford':'Wikipedia coordinate.',
}
