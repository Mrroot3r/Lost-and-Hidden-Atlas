# November 17, 2026: Utah, first close pass: the Tintic Mining District round Eureka (Juab County, with the Tintic mill
# just over the line in Utah County) and three Pony Express stations in the West Desert.
# Facts come from the linked sources, opened in this session: the 1979 National Register forms for the Tintic Mining District
# (read as text from NPGallery), the Utah Division of State History markers filed on HMdb.org, Wikipedia, the National Park
# Service's Pony Express pages, the BLM byway map and a BLM monograph, Eureka City's own pages, and two recent visits:
# the Mining History Association's field trip of June 9, 2024 and a Deseret News piece of June 3, 2024.
# The Register forms are from 1977-79; where only a form says something still stands, the text says so.
# Every pin was looked at on the Esri World Imagery aerial with tools/look.py; four were moved with tools/pix.py.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'ut_tkty','label':'Utah: the Tintic Mining District and the Pony Express stations','added':'2026-11-17 20:53'}
MRA=L('National Register nomination: Tintic Mining District, Multiple Resource Area (1979, NPGallery)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/64000875_text')
MHA2=L('Mining History Association: Tintic field trip, June 9, 2024 (gallery 2)','https://mininghistoryassociation.org/ParkCityTinticTour2.htm')
MHA3=L('Mining History Association: Tintic field trip, June 9, 2024 (gallery 3)','https://mininghistoryassociation.org/ParkCityTinticTour3.htm')
MHA1=L('Mining History Association: Tintic field trip, June 9, 2024 (gallery 1)','https://mininghistoryassociation.org/ParkCityTinticTour1.htm')
DN24=L('Deseret News (June 3, 2024): How to visit Utah ghost towns','https://www.deseret.com/utah/2024/06/03/how-to-visit-utah-ghost-towns/')
HMTIN=L('HMdb: Tintic Mining District marker','https://www.hmdb.org/m.asp?m=75338')
THS=L('Eureka City: Tintic Historical Society and museum','https://eureka.utah.gov/tintic-historical-society')
PXMON=L('BLM: The Pony Express Stations of Utah in Historical Perspective, appendix 1 (station ownership)','https://npshistory.com/publications/blm/cultresser/ut/2/app1.htm')
PXBLM=L('BLM: Pony Express National Backcountry Byway map (PDF)','https://www.blm.gov/sites/blm.gov/files/uploads/BLMUtahPonyExpressNationalBackcountryBywayMap.pdf')
MINES='Old shafts, adits and mine dumps all over the district: keep out of every opening and off the dumps. Eureka was an EPA Superfund cleanup for lead and arsenic in mine waste.'
PLACES=[
# ---- Eureka ----
N('bullion-beck-headframe-eureka','Bullion Beck headframe','Eureka','ut','industry','standing',39.95008,-112.12515,'exact','view','drive','','c. 1890',
  'The Bullion Beck, found by John Beck in 1871, was one of Eureka\'s Big Four mines with the Gemini, the Eureka Hill and the Centennial-Eureka (Blue Rock). Its headframe went up about 1890 and was once housed inside a frame building some 70 feet high. The state marker calls it the only remnant of the company. The mine dumps round it were part of the EPA Superfund cleanup; the 2024 Mining History Association tour says the headframe is all that was kept of the mine.',
  'A 65-foot wooden A-frame (Montana-type) headframe on the north side of US 6 at the west edge of town, with a state marker on a stone monument. The dumps round it are capped with fresh grey rock from the cleanup.',
  'The last of Eureka\'s Big Four standing over its shaft, beside the highway.',
  'Seen from West Main Street (US 6); the marker is on the roadside, about 0.3 miles west of Church Street. Who owns the headframe ground now was not checked: in 1979 it was U.V. Industries. '+MINES,
  [L('HMdb: The Bullion Beck & Champion Mining Company Headframe (Division of State History marker)','https://www.hmdb.org/m.asp?m=75433'),MHA2,
   L('Waymarking: Bullion Beck and Champion Mining Company Headframe','https://www.waymarking.com/waymarks/WM7TYP_Bullion_Beck_and_Champion_Mining_Company_Headframe')]),
N('eureka-historic-district-ut','Eureka Main Street and the historic district','Eureka','ut','town','standing',39.95528,-112.11528,'area','view','walk','','1885–1910s',
  'Eureka was the centre of the Tintic Mining District, organised on December 13, 1869, and by the turn of the century the Big Four mines kept well over 5,000 people here. The district was listed on the National Register in 1979. About 660 people lived here at the 2020 census; it is a living town, not a ghost town.',
  'Stone and brick commercial blocks along Main Street (US 6): the Elks block of 1909-10, the old post office of about 1894, the McCornick bank, City Hall of 1899 and the 1891 county courthouse and jail on Church Street. St. Patrick\'s Catholic Church on North Church Street was built in 1885, and the state marker calls it one of the oldest Catholic churches in Utah. Each of these has a state marker.',
  'A mining town that never quite emptied: the downtown of a camp that was once Utah\'s ninth city.',
  'Public streets; the buildings are private, churches and city offices. Look from the sidewalk. Mobile phone service is limited or absent in Eureka, says the city.',
  [W('Eureka, Utah'),HMTIN,L('HMdb: St. Patrick\'s Catholic Church','https://www.hmdb.org/m.asp?m=75432'),
   L('HMdb: B.P.O.E. Block, Elk Lodge #711','https://www.hmdb.org/m.asp?m=75428'),L('HMdb: Juab County Courthouse','https://www.hmdb.org/m.asp?m=75431'),
   L('National Register nomination: Eureka Historic District (1979, NPGallery)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/79002514_text'),DN24,
   L('WorldAtlas: 6 old-timey mining towns in Utah','https://www.worldatlas.com/cities/6-old-timey-mining-towns-in-utah.html')]),
N('tintic-mining-museum-eureka','Tintic Mining Museum (Union Pacific depot and City Hall)','Eureka','ut','rail','standing',39.95443,-112.11993,'site','open','walk','stations','1899, 1926',
  'The Union Pacific built this wood-frame depot in Eureka in 1926. In 1954 it was moved out to the Dragon Mine at Silver City, and the 1979 Register form says it was to be moved back to Eureka in 1978; it now holds the Tintic Mining Museum. Next door, City Hall was built in 1899 for the court, mayor, sheriff and fire department, and part of its upper floor holds more of the museum.',
  'Ore specimens from the district\'s mines, mine models, an assay office and a mock mine office inside. Behind the museum is the historical society\'s yard of mine cages, ore buckets and machinery. The old jail stands behind City Hall.',
  '',
  'Run by the Tintic Historical Society, 241 West Main Street. The city\'s page gives no set hours: call a society member for an appointment, or ask at the convenience store across the street, which can call for you. Parking on Main Street, or the lot on Hatfield Avenue a block west.',
  [THS,L('HMdb: Eureka City Hall','https://www.hmdb.org/m.asp?m=75426'),L('HMdb: Union Pacific Railroad Depot','https://www.hmdb.org/m.asp?m=75372'),
   L('National Register nomination: Union Pacific Railroad Depot, Tintic district (1979, NPGallery)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/79003480_text'),MHA1,MHA2],
  th=[39.95371,-112.12175],thn='Parking lot, Hatfield Avenue'),
N('eagle-blue-bell-mine-eureka','Eagle and Blue Bell Mine','Eureka','ut','industry','ruins',39.94722,-112.11667,'site','ask','drive','','early 1900s–1949',
  'A big surface plant on the hill above the Chief Consolidated mine, just south of Eureka. Its shaft went down 2,016 feet, and the Chief Consolidated company held it as an asset into the 1990s. The 2024 tour says the mine closed in 1949. The 1979 Register form lists a wooden A-frame headframe, frame buildings, ore bins and a huge cone-shaped dump.',
  'On the 2024 visit: the concrete hoist house, with the flat-rope hoist and the big engine foundations inside; two cages at the shaft collar; massive ore bins; and the ruins of the office, the change house (the dry) and other buildings. The tour photos do not show a headframe, and the city\'s slideshow has a picture captioned "Collapse of Eagle Blue Bell"; whether the headframe stands was not checked. Down the hill the Chief Consolidated office still stands on the reclaimed yard; the Chief headframe was lost in the cleanup and a stake marks its place.',
  '',
  'Private mining ground, not on mapped public land; the 2024 visit was a guided tour. Ask the owner before going up; in 1979 it was Chief Consolidated Mining, and the owner now was not checked. Open shaft. '+MINES,
  [L('National Register nomination: Eagle and Blue Bell Mine (1979, NPGallery)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/79003482_text'),MHA3,THS,
   L('Utahrails.net: Tintic, Eagle & Blue Bell Mine','https://utahrails.net/mining/tintic-eagle-blue-bell.php')],conf='mixed'),
N('knightsville-school-foundation','Knightsville school foundation','Knightsville','ut','town','ruins',39.95434,-112.09938,'site','ask','drive','','1896–1940',
  'Jesse Knight, a Latter-day Saint who struck rich ore at his Humbug Mine against expert advice, built Knightsville about 1896 as a company town for his miners on the north slope of Godiva Mountain. It had some 65 homes, boarding houses, stores and churches, and was known as the mining camp without a saloon. The school went up in 1909. By 1924 only two mines were working and the operation closed by 1940.',
  'A concrete foundation about 40 feet square, made, says the Register form, of gravel and rock from the Mayday Mine dump. The Register form and Wikipedia say nothing else of the town remains but scattered debris.',
  'A model town with no saloon, and all that is left is the school.',
  'Not on mapped public land. In 1979 the Anaconda Company owned it; the owner now was not checked. Dirt tracks run past it east of Eureka. Ask before going on. '+MINES,
  [W('Knightsville, Utah'),W('Knightsville School Foundation'),
   L('National Register nomination: Knightsville School Foundation (1979, NPGallery)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/79003485_text'),
   L('NV Expeditions: Knightsville','https://beyond.nvexpeditions.com/utah/juab/knightsville.php')],conf='mixed'),
# ---- Silver City, Mammoth and Diamond ----
N('tintic-smelter-site','Tintic Smelter and Knight-Dern mill site','Silver City','ut','industry','ruins',39.91699,-112.14042,'site','ask','drive','','1908–1915, then the mill',
  'Jesse Knight built the Tintic Smelter at Silver City in 1908 to beat the high rates charged by the Salt Lake Valley smelters, and it brought them down. It was taken apart in 1915 and replaced that year by the Tintic Mill, built by Knight with George Dern, later governor of Utah, to roast ores from across the West. Silver City itself was the district\'s centre in the 1870s and 1880s and faded by 1930.',
  'Slag and tailings dumps and long concrete foundations of the smelter and mill, about five acres (the Register form). On the aerial the foundations show as long parallel concrete walls west of the old road. The Deseret News found building foundations at Silver City in 2024.',
  '',
  'Not on mapped public land; the Anaconda Company owned it in 1979 and the owner now was not checked. Look from the road and ask before walking in. Slag and tailings: lead and arsenic. '+MINES,
  [W('Silver City, Utah'),L('National Register nomination: Tintic Smelter Site (1979, NPGallery)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/79003472_text'),DN24],conf='mixed'),
N('silver-city-cemetery-ut','Silver City Cemetery','Silver City','ut','burial','traces',39.90216,-112.13404,'site','view','drive','cemeteries','1870s–',
  'The burial ground of Silver City, the mining camp at the mouth of Dragon Canyon that grew up after the 1869 strikes and was the district\'s centre in the 1870s and 1880s. The Register listed it in 1979 as the only remaining evidence of the town.',
  'A fenced plot of about an acre with graves; the Deseret News photographed them in May 2024. Mine holes and tailings piles are what else is left of the town.',
  '',
  'About half a mile east of US 6 south of Eureka, on a dirt road. Not on mapped public land; the 1979 form found no recorded owner. Owner and any rules not checked: look from the gate and treat it as a burial ground. '+MINES,
  [W('Silver City Cemetery (Utah)'),W('Silver City, Utah'),L('National Register nomination: Silver City Cemetery (1979, NPGallery)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/79003472_text'),DN24]),
N('mammoth-historic-district-ut','Mammoth','Mammoth','ut','town','standing',39.92808,-112.1219,'area','view','drive','','1870–',
  'Named for the Mammoth Mine, found in 1870, which worked for about 75 years. The camp peaked about 1900-1910 with 2,500 to 3,000 people, four large hotels and a school; it incorporated in 1910 and gave up its charter in 1929. Water had to be bought at ten cents a gallon. The Register form of 1979 counted about 35 people still living here.',
  'One long street up Mammoth Canyon to the mine, with frame houses mostly built between 1892 and 1910. The brick fire station of about 1930 has a state marker; at Gold Street another marks the site of the Tintic Hospital (1902-1933), whose building was destroyed about 1935.',
  'A semi-ghost town where people still live in miners\' houses.',
  'People live here: stay on the public road and look. Mine ground above the town is private and some small-scale mining goes on. '+MINES,
  [W('Mammoth, Utah'),L('National Register nomination: Mammoth Historic District (1979, NPGallery)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/79003468_text'),
   L('HMdb: Mammoth Fire Station','https://www.hmdb.org/m.asp?m=75443'),L('HMdb: Site of the Tintic Hospital','https://www.hmdb.org/m.asp?m=75442'),MHA2]),
N('diamond-cemetery-ut','Diamond townsite and cemetery','Diamond','ut','burial','traces',39.88099,-112.10837,'site','view','drive','cemeteries','1870–1890',
  'One of the earliest camps in the district, named for quartz crystals first taken for diamonds. It grew to about 900 people with saloons, stores and a school, but the mines struck water and the last residents left in 1890. The post office may have stayed open until 1906, and the last house was moved away in 1923.',
  'Mine tailings and a small cemetery west of the townsite. Little of the cemetery is left; the Register form names one intact grave still visited by family, and Wikipedia says at least one grave is still kept. On the aerial the cemetery is a clump of trees in a small square enclosure.',
  '',
  'Not on mapped public land; in 1979 it was probably owned by the Weir Company, and the owner now was not checked. A dirt road passes just north. Look from the road. '+MINES,
  [W('Diamond, Utah'),L('National Register nomination: Diamond Cemetery (1979, NPGallery)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/79003476_text'),HMTIN],conf='mixed'),
# ---- Tintic Valley and Goshen ----
N('knight-grain-elevator','Knight Grain Elevator','Knight','ut','industry','standing',39.94267,-112.19545,'exact','view','drive','','1915',
  'A 50,000-bushel concrete grain elevator built in 1915 by the Union Grain and Elevator Company for Jesse Knight\'s dry farm in the Tintic Valley, one of the largest farms in the valley. The Register form says it shows Knight\'s hand in every side of the district, from mines and smelters to railroads and farming. It is nearly all that is left of the place called Knight.',
  'The concrete elevator between Utah Route 36 and the railroad, west of Eureka.',
  '',
  'Private (in 1979 J. G. Bennett owned it; not checked since). Look from SR 36. Do not cross the railroad.',
  [W('Knight Grain Elevator'),L('National Register nomination: Knight Grain Elevator (1979, NPGallery)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/79003470_text')]),
N('tintic-standard-reduction-mill','Tintic Standard Reduction Mill (closed)','Genola','ut','industry','ruins',39.95772,-111.85506,'exact','view','drive','','1920–1925',
  'Built in 1920 to raise the metal content of Tintic ores before shipping, it was the only American mill using the Augustin acid-brine process in the early 1920s. It handled up to 200 tons a day but the process went out of date and the mill closed in 1925. The Division of Wildlife Resources took over the land in 1986 as part of the Goshen Warm Springs Wildlife Management Area. In 2002 state tests found high lead and arsenic, and the state closed the site.',
  'Concrete foundations of the water tanks, crushers, roasters and leaching tanks stepping down the west slope of Warm Springs Mountain, covered in graffiti; parts have collapsed. It shows from the road as you come into Genola.',
  'A concrete castle on a hill that the state will fine you for walking into.',
  'CLOSED. The mill is on the Goshen Warm Springs Wildlife Management Area and the Division of Wildlife Resources has closed it because of lead, arsenic and collapsing concrete; it is fenced and posted and officers write trespassing citations (2019 news reports; the division\'s own pages were not read). Look from the public road only.',
  [W('Tintic Standard Reduction Mill'),
   L('Deseret News (August 27, 2019): DWR to cite trespassers at old Tintic Mill','https://www.deseret.com/2019/8/27/20835566/keep-out-dwr-officials-to-issue-citations-to-trespassers-on-old-tintic-mill-site-near-goshen/'),
   L('KSL (2019): Officers to issue citations to Tintic Mill trespassers','https://www.ksl.com/article/news/outdoors/officers-to-issue-citations-to-tintic-mill-trespassers-amid-growing-cases/46626723'),
   L('Utah Outdoor Activities: Harold Mill / Goshen Warm Springs','https://utahoutdooractivities.com/harold-mill-goshen-warm-springs.html')]),
# ---- West Desert: Pony Express stations ----
N('boyd-pony-express-station','Boyd Pony Express Station','Callao','ut','landmark','ruins',39.84381,-113.5533,'site','public','drive','','c. 1855–c. 1900',
  'Also called Butte Station and the Half-way House. George Washington "Bid" Boyd is said to have built it about 1855, though the rider Howard Egan wrote that it was not there yet when he passed in 1860. It became a Pony Express relay station in 1860, with gunports in its stone walls. Boyd is said to have lived on here alone until about 1900, which is probably why the stone was not carried off. The BLM dug and stabilised it in 1974 and 1975.',
  'Stabilised stone walls of a one-room, partly dug-out station with gunports, behind a fence, with a BLM kiosk. The NPS says the old trail shows on the ground heading northwest toward Willow Springs.',
  'One of the best-kept Pony Express stations in Utah, alone in the desert.',
  'BLM land (Fillmore Field Office), open to the public with a roadside pullout. On Pony Express Road, 14 miles west of Fish Springs National Wildlife Refuge; keep right where Granite Ranch Road splits off; the site is on the north side. A long gravel road with no services named on the BLM or NPS pages; the BLM map warns it is muddy when wet. Do not move or take anything: it is a federal offence.',
  [L('NPS: Boyd Station (Pony Express National Historic Trail)','https://www.nps.gov/places/boyd-station.htm'),
   L('BLM: Pony Express Trail includes Boyd Station','https://www.blm.gov/visit/pony-express-trail-includes-boyd-station'),PXBLM,PXMON,
   L('BLM: The Pony Express Stations of Utah, Fish Springs to Willow Springs','https://npshistory.com/publications/blm/cultresser/ut/2/sec2d.htm')]),
N('canyon-round-station-pony-express','Canyon (Round) Station','Ibapah','ut','fort','ruins',40.04456,-113.8042,'exact','public','drive','','1861–1863 and after',
  'The first Canyon Station, at the mouth of Overland Canyon, was a Pony Express and Overland Stage stop with a dugout, a stable and perhaps a log house. Goshute warriors attacked it on August 8, 1863, in revenge for the destruction of a Goshute village by soldiers, killing at least five men and burning it. Within months the stage company rebuilt at the other end of the canyon, about 3.5 miles southeast, on ground easier to defend.',
  'Stone outlines of the 1863 station and the low round stone fort behind it, with rifle ports, which probably never had a roof; a BLM interpretive shelter. A hollow south of the parking area marks the likely corral and blacksmith shop. The 1863 burned site has a stone monument 3.5 miles up the road.',
  'The Pony Express trail\'s round stone fort.',
  'BLM land in the Deep Creek Mountains Wilderness Study Area, open to the public. On Pony Express Road (Deep Creek Mountains Road) about 13 miles northwest of Callao; the interpretive site entrance is on the left. Remote gravel road; no services named on the BLM or NPS pages.',
  [L('NPS: Canyon Station (Pony Express National Historic Trail)','https://www.nps.gov/places/canyon-station.htm'),PXBLM,PXMON]),
N('willow-springs-pony-express-station','Willow Springs Pony Express Station','Callao','ut','landmark','standing',39.90028,-113.71419,'site','view','drive','','',
  'Local tradition places it on the Willow Springs Ranch at Callao, and a wood-clad adobe building at the ranch headquarters is said to be the original station. A BLM study of the stations says the site is disputed: it found a foundation where an 1882 survey put the stable, and the Kearney boarding house still standing nearby.',
  'A 1939 monument at the ranch entrance on East Pony Express Road. The ranch buildings, and a huge cottonwood said to date from the Pony Express years, are on private land.',
  '',
  'Private ranch: the NPS says the owners\' permission is needed to visit the station. The 1939 monument at the ranch entrance is open to the public.',
  [L('NPS: Willow Springs Station','https://www.nps.gov/places/willow-springs-station.htm'),
   L('BLM: The Pony Express Stations of Utah, Fish Springs to Willow Springs','https://npshistory.com/publications/blm/cultresser/ut/2/sec2d.htm'),PXMON],conf='mixed'),
# ---- cemetery ----
N('eureka-city-cemetery-ut','Eureka City Cemetery','Eureka','ut','burial','standing',39.945,-112.14611,'site','public','drive','cemeteries','1894–',
  'Eureka\'s cemetery has been at this spot west of town since 1894. The Register listed it in 1979, an exception for a cemetery, because its stones show the many nationalities of the mining district, when disease and accidents struck, and the separate plots of the fraternal lodges that buried their members.',
  'About ten acres of graves in a grid of lanes, with lodge plots.',
  '',
  'Owned by Eureka City (1979 form). West of town off US 6. Hours and rules not checked.',
  [W('Eureka City Cemetery (Utah)'),L('National Register nomination: Eureka City Cemetery (1979, NPGallery)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/79003470_text')]),
]
PIN_NOTES={
 'bullion-beck-headframe-eureka':'HMdb marker position (39° 57.005′ N, 112° 7.509′ W); the aerial shows the A-frame headframe\'s shadow in the ring.',
 'eureka-historic-district-ut':'Wikipedia\'s Register-list coordinate for the district, on Main Street (US 6); the aerial shows the downtown blocks round it.',
 'tintic-mining-museum-eureka':'HMdb marker position for the depot, beside City Hall on West Main Street; not moved. Parking point is an OpenStreetMap lot (tools/parking.py).',
 'eagle-blue-bell-mine-eureka':'Wikipedia\'s Register-list coordinate (the 1979 form\'s own figure, 39° 54′ 48″, is off by two minutes); the aerial shows a group of ruined buildings on a big grey dump in the ring and a second structure about 80 m south.',
 'knightsville-school-foundation':'Moved 12 m with tools/pix.py onto a walled square about 13 m across beside the dirt tracks, which matches the 40-foot foundation; started from the Wikipedia coordinate. The Register form\'s own figure (112° 04′ 50″) is 1.6 km east, on bare hillside, and was not used.',
 'tintic-smelter-site':'Moved 83 m west with tools/pix.py from the Wikipedia coordinate onto the long concrete foundations seen on the aerial.',
 'silver-city-cemetery-ut':'OpenStreetMap cemetery outline (tools/nom.py); the aerial shows the fenced plot with lanes in the ring.',
 'mammoth-historic-district-ut':'HMdb position of the Mammoth Fire Station marker on Main Street; the aerial shows houses along the road.',
 'diamond-cemetery-ut':'Read off the pin-check sheet with tools/pix.py onto the tree-filled square enclosure, 13 m from the OpenStreetMap cemetery point (tools/nom.py); the dirt road passes about 70 m north.',
 'knight-grain-elevator':'Moved 111 m west with tools/pix.py from the Wikipedia coordinate onto the elevator, which shows with its long shadow between SR 36 and the railroad.',
 'tintic-standard-reduction-mill':'OpenStreetMap ruin point (tools/nom.py); the aerial shows the round tank foundations in the ring.',
 'boyd-pony-express-station':'OpenStreetMap ruin point, 3 m from the NPS interpretive-turnout coordinate, about 40 m north of Pony Express Road at the Granite Ranch Road fork. Neither the aerial nor the LiDAR picks out the walls clearly at this scale. The BLM page\'s own coordinate (39.8418, -113.316) is 20 km east and was not used.',
 'canyon-round-station-pony-express':'OpenStreetMap ruin point (tools/nom.py, "Canyon Station (Pony Express)"); the aerial shows the round enclosure in the ring and the shelter and loop road beside it.',
 'willow-springs-pony-express-station':'NPS coordinate for the monument at the ranch entrance; the aerial shows the road junction there. The station building is in the ranch yard to the east and was not pinned.',
 'eureka-city-cemetery-ut':'Wikipedia coordinate; the aerial shows the grid of cemetery lanes in the ring.',
}
