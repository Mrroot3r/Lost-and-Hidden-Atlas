# November 22, 2026: New Mexico, a second scatter across the state (34 places before this batch, none in the north-west,
# the far east, Albuquerque, Taos town or the south-west corner). Chosen with tools/choose.py --thinnest (nm).
# From Clayton and Raton in the north-east to Gallup in the west and Mesilla and Shakespeare in the south: gold and silver
# camps, Route 66 survivors, adobe churches, a flour mill, a narrow-gauge rail yard and two old theatres.
# Sources read in this session: Wikipedia (tools/wiki_raw.py), National Park Service pages (nps.gov/places), HMdb.org
# marker texts, the City of Albuquerque's KiMo pages, the Shuler Theater's own pages, the Cleveland Roller Mill Museum,
# Hotel Eklund, the Basilica of San Albino, Shakespeare Ghost Town, the Santuario de Chimayo, Sierra County Recreation &
# Tourism, the New Mexico Tourism Department, New Mexico Magazine, the Albuquerque Journal, Atlas Obscura, HistoryNet and
# newmexicoghosttowns.net.
from data_b import N
from data_ma import W
BATCH={'key':'nm_qvzr','label':'New Mexico: mining camps, Route 66 and adobe churches across the state','added':'2026-11-22 17:35'}

def HM(n,label):
    return ['HMdb: '+label,'https://www.hmdb.org/m.asp?m=%d'%n]
SIERRA='https://sierracountynewmexico.info/cool-places/'

PLACES=[
# ---- North-east ----
N('elizabethtown-nm','Elizabethtown ("E-Town")','Elizabethtown','nm','town','ruins',36.61917,-105.28444,'area','view','drive','','1866–1917',
  'A gold camp begun in 1866 and named for Elizabeth Moore, daughter of a Fort Union commander; it was the first incorporated town in New Mexico. In 1869 it may have held 5,000 to 9,000 people, the largest place in the territory, and in 1870 it became the first seat of Colfax County. By 1872 about 100 people were left and the county seat went to Cimarron. Mining picked up again in the 1890s, but a fire in 1903 burned most of the wooden town, and by 1917 few lived there.',
  'Today a scatter of ranch homes stands on the old townsite. Wikipedia names the stone wall of a boarding house as the one remnant of the original town, and a large cemetery on the hill above. Exactly where the wall stands was not checked.',
  'The biggest town in New Mexico in 1869, now one stone wall and a hillside cemetery.',
  'Just off NM 38 between Eagle Nest and Red River (Wikipedia). The homes on the townsite are lived in: look from the road and do not walk into yards. Who owns the wall and the cemetery, and whether visitors may walk to them, was not checked.',
  [W('Elizabethtown, New Mexico')],brick='?'),

N('st-james-hotel-cimarron-nm','St. James Hotel','Cimarron','nm','hotel','standing',36.50472,-104.92058,'exact','open','drive','','1872 (hotel by 1880)',
  'Henri Lambert, who had been a cook to President Lincoln, came west for gold, then opened a saloon in Cimarron in 1872 at Lucien Maxwell\'s urging. By 1880 it had grown into the two-storey adobe St. James Hotel. Lawmen and outlaws stayed and fought here; Wikipedia names Wyatt Earp, Jesse James and Buffalo Bill among its guests. It closed in September 2024 and reopened under new owners that December.',
  'The National Park Service says the bar, once part of the present dining room, still has bullet holes in its pressed tin ceiling, and the Albuquerque Journal (December 2024) shows the holes in the restaurant ceiling and an old register in Lambert\'s Restaurant. Rooms are named for famous guests. The building is in the Cimarron Historic District.',
  'Henri Lambert\'s saloon and hotel, bullet holes still in the ceiling.',
  'A working hotel and restaurant at Collinson Avenue (NM 21) and 17th Street in old town Cimarron, owned and run by Chad and Alyse Mantz since December 2024 (Albuquerque Journal). The NPS page says it is on the chamber of commerce walking tour. Restaurant hours not checked.',
  [['NPS: St. James (Don Diego) Hotel','https://www.nps.gov/places/st-james-don-diego-hotel-cimarron.htm'],['Albuquerque Journal: the hotel reopens (Dec. 2024)','https://www.abqjournal.com/lifestyle/to-keep-that-history-going-is-really-important-to-us-iconic-new-mexico-hotel-reopens/398120'],W('St. James Hotel (Cimarron, New Mexico)')],
  brick='no',hours='?'),

N('shuler-theater-raton-nm','Shuler Theater','Raton','nm','civic','standing',36.90293,-104.43901,'exact','open','drive','','1915',
  'Raton\'s municipal auditorium, built while Dr. J. J. Shuler, the Santa Fe railroad\'s surgeon, was mayor. Its first show, the touring musical comedy The Red Rose, opened on April 27, 1915. After Shuler died in 1919 the city named it for him. His daughter Evlyn led its restoration from the 1960s, and a nonprofit restoration commission has looked after it since 1974.',
  'Three of the original drop curtains survive and are still used, among them the fire curtain painted with the Palisades of Cimarron. The restored box seats beside the stage are in use, and the lobby holds eight WPA murals of 1934 by Manville Chapman showing Raton\'s history (the theater\'s own pages). Open for performances; daytime visiting not checked.',
  '',
  'Owned and kept by the City of Raton, 131 North 2nd Street downtown; the Shuler offices take bookings on 575-445-4746 (the theater\'s own page). Performance dates and any tour times not checked.',
  [['Shuler Theater: history','https://shulertheater.com/?p=33'],['Shuler Theater: about','https://shulertheater.com/?p=31']],
  brick='?',hours='?'),

N('eklund-hotel-clayton-nm','Hotel Eklund','Clayton','nm','hotel','standing',36.45179,-103.18484,'exact','open','drive','','1892',
  'The oldest part, now the saloon, was built in 1892 as a saloon and gambling hall. Carl Eklund bought it in 1894 and enlarged it in stages into a hotel. It was listed on the National Register in 2002. Two architects who restore old buildings bought it in 2011 and run it.',
  'A working hotel with 24 rooms (remodelled in 2004), two dining rooms and the old bar (the hotel\'s own page). It faces the Luna Theater, also on the Register (Wikipedia). Interior fabric not checked.',
  '',
  'A working hotel, restaurant and saloon at 15 Main Street, Clayton, run by its owners (hotel page). Restaurant hours not checked.',
  [['Hotel Eklund: about us','https://hoteleklund.com/about-us'],W('Eklund Hotel')],
  brick='?',hours='?'),

N('cleveland-roller-mill-nm','Cleveland Roller Mill','Cleveland','nm','industry','standing',35.98574,-105.35874,'site','open','drive','','1890s–1940',
  'The last of the Mora Valley\'s flour mills to be built, and one of the largest in northern New Mexico. Joseph Fuss, a Mora merchant and rancher, began it in the 1890s; most of the machinery was put in from 1897, brought by train to Las Vegas and by wagon to Cleveland. A water wheel drove it until 1916, then a steam engine, whose boiler blew up in 1919 and killed a worker. Fuss sold the mill in 1913 and it closed in 1940 (museum and National Park Service).',
  'A three-storey adobe water-powered flour mill. The original roller-mill machinery is intact and restored so that it can be run for demonstrations (museum page). The museum inside tells the story of farming and milling in the Mora Valley.',
  'The only mill of its size in north-eastern New Mexico restored to running order.',
  'A museum run by the Cleveland Roller Mill Museum. Its page says it is closed for the 2026 season and opens again May 29 to October 31, 2027; days and times not checked. On NM 518 in Cleveland, west of Mora (address lookup).',
  [['Cleveland Roller Mill Museum','https://clevelandrollermillmuseum.org/'],['NPS Fort Union: Cleveland Roller Mill talk (2015)','https://www.nps.gov/foun/learn/news/august-20-2015-glimpses-of-the-past-cleveland-roller-mill-feeding-the-mora-valley.htm']],
  brick='no',hours='May 29 to October 31, 2027 (closed for 2026); days and times not checked'),

# ---- North ----
N('kit-carson-house-taos-nm','Kit Carson House','Taos','nm','landmark','standing',36.40701,-105.57212,'exact','open','walk','','1825',
  'A one-storey adobe house of 1825, a U round a courtyard, a short way east of the Taos plaza. The frontiersman Kit Carson bought it in 1843 when he married Josefa Jaramillo, and it was their main home until 1868. The Masonic lodge Carson had founded bought it in 1910; after years of decay a foundation restored it from 1952. It became a National Historic Landmark in 1963.',
  'The front three rooms and the next room north are the oldest part. The house is shown as a museum of Carson\'s life, with guided tours and a gift shop (Wikipedia). Interior fabric not checked.',
  '',
  'A house museum at 113 Kit Carson Road, Taos, owned by the Masonic lodge and run by the Kit Carson Memorial Foundation (Wikipedia). The museum\'s own site and the town tourism page could not be opened when this was written: hours and fees not checked.',
  [W('Kit Carson House')],
  brick='no',hours='?'),

N('santuario-de-chimayo-nm','El Santuario de Chimayó','Chimayó','nm','worship','standing',35.98908,-105.93192,'exact','open','walk','','1813–1816',
  'Bernardo Abeyta built a small chapel to the Christ of Esquipulas here about 1810. In 1813 he asked leave to build a larger church, permission came in 1814, and by 1816 the present church had replaced the chapel. In 1929 the Spanish Colonial Arts Society bought it and gave it to the Archdiocese of Santa Fe. It is a National Historic Landmark (1970) and draws close to 300,000 pilgrims a year.',
  'An adobe church entered through a walled courtyard, with a bell tower each side and walls over three feet thick; the tower caps and metal roof came after 1917. Inside are doors carved by Pedro Domínguez, a six-foot crucifix of the Christ of Esquipulas, five reredoses and other folk art, and the little room called el pocito with its pit of holy earth (Wikipedia, NPS).',
  'The pilgrimage church of the holy dirt, 1816.',
  'Run by the Santuario under the Archdiocese of Santa Fe; its own page says the church and chapels hold weekly Masses and tours and welcome visitors, but its schedule page showed nothing when this was written. Small lots at the church on County Road 94C and Santuario Lane (OpenStreetMap).',
  [['El Santuario de Chimayó','https://www.holychimayo.us'],['NPS: El Santuario de Chimayó','https://www.nps.gov/places/el-santuario-de-chimayo.htm'],W('El Santuario de Chimayo')],
  th=[35.98900,-105.93226],thn='Lot on County Road 94C',brick='no',hours='?'),

N('chama-railyard-nm','Chama rail yard and depot (Cumbres & Toltec)','Chama','nm','rail','standing',36.90258,-106.57870,'site','open','walk','','1880–1924',
  'The Denver & Rio Grande\'s narrow-gauge San Juan Extension reached Chama in late 1880 on its way to Durango and Silverton. The line ran until traffic faded in the late 1960s; in 1970 Colorado and New Mexico bought the 64 miles between Antonito and Chama, and it runs as the Cumbres & Toltec Scenic Railroad, a National Historic Landmark since 2012. The depot is the second on the spot; the first burned in 1899 with the wooden roundhouse.',
  'In the yard (HMdb markers): the water tank of 1897, the coal tipple and the sand house of 1924, the last two stalls of the brick roundhouse, the machine shop, boiler room and oil house of 1899, and the passenger depot of 1899. The tipple is the only one left of three built on the line in 1924 and is worked for demonstrations.',
  'The last coal tipple of the Rio Grande narrow gauge.',
  'Owned and run by the Cumbres & Toltec Scenic Railroad. Trains run from Chama to Antonito, Colorado; its own page gives the 2027 season as May 29 to October 17, with a Santa train from Chama in winter. The yard is a working railroad: stay off the tracks. Parking on 4th Street by the depot (OpenStreetMap).',
  [HM(280854,'The Chama Railyard'),HM(280864,'Coal Tipple'),HM(280909,'D&RG depot, Chama'),['Cumbres & Toltec Scenic Railroad','https://cumbrestoltec.com/'],W('Cumbres and Toltec Scenic Railroad')],
  th=[36.90351,-106.57845],thn='4th Street lot',brick='some',hours='Trains May 29 to October 17, 2027; winter Santa trains (railroad page)'),

# ---- West ----
N('el-rancho-hotel-gallup-nm','El Rancho Hotel','Gallup','nm','hotel','standing',35.52957,-108.72814,'exact','open','drive','','1936–1937',
  'Built on Route 66 by Joe Massaglia for R. E. "Griff" Griffith, brother of the film director D. W. Griffith, as a base for film crews and stars working on westerns round Gallup; the staff were trained by the Fred Harvey Company. The National Park Service gives 1936 for its building and opening, Wikipedia 1937 for the opening. After Interstate 40 it declined; Armand Ortega bought it at a bankruptcy auction and restored it.',
  'A rambling Rustic building of brick, random stone and rough-hewn wood, with intentionally wavy brickwork, a shake roof, brick and stone chimneys and a plantation-style portico. The square lobby has a balcony round it, a brick and stone fireplace and twin log stairways; rooms in the main building carry the names of film-star guests (NPS, Wikipedia).',
  'Where the stars of the westerns slept.',
  'A working hotel at 1000 East Highway 66 (NPS). Lobby and restaurant hours not checked.',
  [['NPS: El Rancho Hotel','https://www.nps.gov/places/el-rancho-hotel.htm'],W('El Rancho Hotel & Motel')],
  brick='some',hours='?',conf='mixed'),

# ---- Albuquerque ----
N('san-felipe-de-neri-albuquerque-nm','San Felipe de Neri Church','Albuquerque','nm','worship','standing',35.09667,-106.67006,'exact','view','walk','','1793',
  'The church on the north side of Old Town Plaza. The first church, of the town\'s founding in 1706, fell in the winter of 1792–93, and the governor ordered a new one built at once; begun in 1793, it is the one building in Old Town proven to date from Spanish rule. Under Bishop Lamy in the 1850s and 1860s it took on a pitched roof and Gothic Revival spires, and the inside was redone again in 1916. It is still a parish church.',
  'A cross-shaped adobe church with thick walls, vigas and carved corbels from the 1790s under a skin of Victorian trim, a pressed tin ceiling of 1916 and an altar and pulpit painted to look like marble. Beside it are the two-storey rectory of about 1890 on the site of the 1790s convent, the Jesuits\' school of 1878 and the convent of 1881, said to be the first two-storey adobe in Old Town (Wikipedia).',
  '',
  'An active Catholic parish of the Archdiocese of Santa Fe on North Plaza Street, Old Town (Wikipedia). The parish site would not open when this was written: Mass and visiting times not checked.',
  [W('San Felipe de Neri Church')],
  brick='no',hours='?'),

N('kimo-theatre-albuquerque-nm','KiMo Theatre','Albuquerque','nm','civic','standing',35.08482,-106.65256,'exact','open','walk','','1927',
  'A picture palace on Central Avenue, opened on September 19, 1927, in the Pueblo Deco style: Pueblo Revival forms with Native motifs and the soaring lines of Art Deco. The city later offered to buy it cheaply or condemn and pull it down; it bought it instead and has restored it in stages, and it is back in use for shows.',
  'The auditorium seats 650 after restoration (Wikipedia). The city runs free Meet The KiMo tours on set dates (city page). It was built with no lift and has no room for one.',
  '',
  'Owned and run by the City of Albuquerque at 423 Central Avenue NW, downtown. The box office opens two hours before ticketed events and stays open for 30 minutes after the start (city page).',
  [['City of Albuquerque: KiMo tours','https://www.cabq.gov/artsculture/kimo/kimo-tours'],['City of Albuquerque: KiMo contact','https://www.cabq.gov/artsculture/kimo/contact-us'],W('KiMo Theater')],
  brick='?',hours='Box office 2 hours before ticketed events; free Meet The KiMo tours on set dates (city page)'),

N('golden-nm','Golden: San Francisco church and mining ruins','Golden','nm','town','standing',35.26965,-106.21320,'site','view','drive','','1820s–1928',
  'Placer gold was found on Tuerto Creek in 1825, years before the California rush, and two small camps grew up in the late 1820s; the San Francisco Catholic Church was built about 1830. Golden was formed in 1879 as the centre of a new mining district, with saloons, a school and even a stock exchange. By 1928 so few were left that the post office closed. The general store of 1918 is the one business still open.',
  'The church, Golden\'s most photographed building, was restored in 1960 by the priest and historian Fray Angélico Chávez; it has a cemetery. West of the church, across the highway, are the ruins of another large building and mining remains (Wikipedia). Whether the church opens was not checked.',
  '',
  'On NM 14, the Turquoise Trail Scenic Byway, about ten miles north of the Sandia Park junction, between Cedar Crest and Madrid (Wikipedia). Who owns the church and the ruins was not checked: look from the road and the church grounds\' edge. New homes stand among the old ones; do not walk into yards.',
  [W('Golden, New Mexico')],brick='?'),

# ---- East ----
N('cuervo-nm','Cuervo','Cuervo','nm','town','ruins',35.03051,-104.40873,'area','view','drive','','1901',
  'A railroad town founded in 1901, with a post office from 1902, later a supply centre for ranches and from 1926 a stop on Route 66. Interstate 40 split it in two. The post office closed in 2011.',
  'Nearly every building is abandoned and badly fallen; in 2011 the shell of an old stone schoolhouse and a stone church still stood, and both appeared to be under restoration (Wikipedia). A few homes are lived in.',
  'A Route 66 town cut in half by the interstate.',
  'Off I-40 about 17 miles east-north-east of Santa Rosa, on streets either side of the interstate (Wikipedia). The buildings are private: look from the public streets.',
  [W('Cuervo, New Mexico')],brick='no'),

N('blue-swallow-motel-tucumcari-nm','Blue Swallow Motel','Tucumcari','nm','hotel','standing',35.17202,-103.71641,'exact','open','drive','','1939–1942',
  'A Route 66 motel begun by the carpenter W. A. Huggins. Wikipedia has it open with a café by July 1941; the National Park Service says the rancher Ted Jones opened it in 1942. Floyd Redman bought it in 1958 for his wife Lillian, who ran it for decades and became a figure of Route 66 lore, taking belongings in trade when guests could not pay.',
  'An L-shaped court with pink stucco walls decorated with shells, a stepped parapet, an office and manager\'s home, and garages between the rooms; Wikipedia counts 12 units, the NPS 14. The neon sign promises "TV" and "100% Refrigerated Air".',
  'The swallow sign of Tucumcari.',
  'A working motel at 815 East Route 66 Boulevard, run by its owners (NPS). The motel\'s own page could not be opened when this was written: office hours not checked.',
  [['NPS: Blue Swallow Motel','https://www.nps.gov/places/blue-swallow-motel.htm'],W('Blue Swallow Motel')],
  brick='no',hours='?',conf='mixed'),

N('glenrio-nm','Glenrio','Glenrio','nm','town','ruins',35.17902,-103.04320,'site','view','drive','','1930s',
  'A Route 66 town on the Texas line. The State Line Bar and motel of the 1930s were built on the New Mexico side because the Texas county was dry, and the post office of about 1935 was in New Mexico too. Interstate 40 passed it by. The east side is governed by Texas.',
  'What is left (Wikipedia): the courtyard motel, the Texas Longhorn Café and Phillips 66 station, the post office, a diner and Texaco station, the old Route 66 roadbed and the bed of the Rock Island railroad, its rails lifted in the 1980s. OpenStreetMap marks the abandoned post office and the Little Juarez Café, whose lines were used in the film Cars, and the State Line Bar as under reconstruction.',
  'Half in New Mexico, half in Texas, all of it Route 66.',
  'On the old Route 66 roadbed off I-40 at the state line; the New Mexico welcome centre on I-40 opened in 2008 (Wikipedia). The buildings are private: look from the old road. At least one business near the bar is open (OpenStreetMap).',
  [W('Glenrio, New Mexico and Texas')],brick='?'),

N('hotel-clovis-nm','Hotel Clovis','Clovis','nm','hotel','standing',34.39981,-103.20504,'exact','view','drive','','1931',
  'A ten-storey Art Deco hotel by the architect Robert Merrell, opened on October 20, 1931, and listed on the National Register in 1984. It closed in 1983. Work to turn it into apartments began in 2011, and Wikipedia says Hotel Clovis Lofts were lived in by January 2020.',
  'The tower stands on Main Street downtown. Wikipedia said in 2017 the street-floor shops were empty and unfinished. Interior not checked.',
  '',
  'Now apartments (Hotel Clovis Lofts, address lookup): look from the street.',
  [W('Hotel Clovis')],brick='?'),

# ---- South ----
N('kelly-nm','Kelly ghost town','Kelly','nm','town','ruins',34.08315,-107.20508,'site','view','drive','','1866–1947',
  'Silver was found here about 1866 and the townsite laid out about 1879; Kelly boomed on silver, then on zinc carbonate for paint from 1903, and once held about 3,000 people with banks, churches and saloons. Magdalena grew three miles north as the railroad terminus. When the zinc gave out in the 1930s the town died; the last residents left in 1947 and many houses were hauled down to Magdalena.',
  'St. John the Baptist church still stands and holds festivals. Up the hill is the Kelly Mine headframe of 1906, bought in kit form from the Traylor Engineering Company of New York and 121 feet high over the Tri-Bullion shaft, nearly 1,000 feet deep (New Mexico Tourism Department). newmexicoghosttowns.net shows the Tri-Bullion smelter remains, the Traylor shaft and ore bin and a rusted safe.',
  'A 121-foot steel headframe over a 1,000-foot shaft.',
  'About 2.5 to 3.5 miles south of Magdalena: the sources disagree on the road (NM 114 per newmexicoghosttowns.net; the state tourism page says to ask locally). Atlas Obscura says to park at the church. Who owns the mine ground was not checked; the shafts are deep and closed: keep to the road and look from the church.',
  [['New Mexico Tourism Department: Kelly','https://www.newmexico.org/places-to-visit/ghost-towns/kelly'],HM(280237,'Kelly'),['newmexicoghosttowns.net: Kelly','https://www.newmexicoghosttowns.net/kelly-nm'],['Atlas Obscura: Kelly','https://atlasobscura.com/places/kelly-ghost-town']],
  brick='?',conf='mixed'),

N('pioneer-store-chloride-nm','Pioneer Store Museum','Chloride','nm','civic','standing',33.33875,-107.68113,'exact','open','drive','','1880–1923',
  'Chloride grew from Henry Pye\'s silver find of 1879 into a town of eight saloons and about 500 people by 1881, and nearly 3,000 in 1890; the silver crash of the 1890s emptied it. The Pioneer Store was built in 1880 and traded until 1923, when the owners closed it with its stock sealed inside. A retired couple bought it more than sixty years later, found it full, including most of the town records of 1880 to 1923, and opened it as a museum in 1998.',
  'The store\'s own fittings and stock reinstalled after a four-year restoration, with cash registers, clothing, dental instruments and minerals (Sierra County tourism). Some of Chloride\'s other old buildings remain and are kept up (Wikipedia).',
  'A general store shut in 1923 with everything left on the shelves.',
  'A museum on Wall Street, Chloride, off NM 52 on the Geronimo Trail byway; 575-743-2736. Hours as given by Sierra County Recreation & Tourism; the museum\'s own page was not read.',
  [['Sierra County Recreation & Tourism: Pioneer Store Museum',SIERRA+'pioneer-store-museum/'],W('Chloride, New Mexico')],
  brick='?',hours='Thursday to Monday 10 a.m. to 4 p.m. (county tourism page)'),

N('kingston-nm','Kingston: Percha Bank and the ghost-town museum','Kingston','nm','town','standing',32.91702,-107.70614,'site','open','drive','','1882',
  'Silver was found at what became the Solitaire Mine in 1882, and Percha City, soon renamed Kingston, grew to some 1,800 people; Lillian Russell performed here. A fire in 1890 destroyed its saloons, hotels, church and opera house (New Mexico Magazine), and the panic of 1893 ended the boom. Mining came back briefly in the Second World War and had mostly stopped by 1952.',
  'Wikipedia shows the former Percha Bank (now a museum), the Black Range Lodge, the former Victorio Hotel and the assay office. The Kingston Ghost Town Museum opened in 2024 in an early adobe house where Territorial Governor George Curry wrote his autobiography in the 1940s, with artifacts such as the Victorio Hotel\'s first register (New Mexico Magazine, Sierra County tourism). Percha Bank hours not checked.',
  '',
  'On NM 152 in the Black Range. The Kingston Ghost Town Museum is at 28 Kingston Main Street, 575-895-5501; hours as given by Sierra County Recreation & Tourism. Most of the old buildings are private homes or businesses: look from the street.',
  [['Sierra County Recreation & Tourism: Kingston Ghost Town Museum',SIERRA+'kingston-ghost-town-museum/'],['New Mexico Magazine: Kingston Ghost Town Museum (2024)','https://www.newmexicomagazine.org/blog/post/kingston-ghost-town-museum/'],W('Kingston, New Mexico')],
  brick='?',hours='Museum: Saturday 10:30 a.m. to 4 p.m., Sunday noon to 4 p.m., weekdays by appointment (county tourism page)'),

N('shakespeare-nm','Shakespeare ghost town','Shakespeare','nm','town','standing',32.32479,-108.73856,'site','open','drive','','',
  'A stage stop called Mexican Springs, renamed Grant after the Civil War, then Ralston City when silver was found, and finally Shakespeare; it was abandoned when the mines closed in 1929. In 1881 the outlaws "Russian Bill" Tattenbaum and Sandy King were lynched here. It is part of a private ranch.',
  'Wikipedia shows the Stafford Hotel building with its dining room and kitchen (2023 photographs). Seen only on a guided tour.',
  'A silver camp on a working ranch, shown by its owners.',
  'Private property on Ghost Town Road near Lordsburg. The owners\' page says tours only, guided: no walk-through visits, and entering without a guide is trespass. $15 adults, $7 ages 6 to 12, under 6 free, $30 minimum, plus tax; call ahead on 575-542-9034. It warns of rattlesnakes, open mine shafts and dust storms on I-10.',
  [['Shakespeare Ghost Town: tours','https://shakespeareghostown.com/tours'],W('Shakespeare, New Mexico')],
  brick='?',hours='Daily tours at 10 a.m., noon and 3 p.m. Mountain time when a guide is available; call ahead (owners\' page)'),

N('basilica-san-albino-mesilla-nm','Basilica of San Albino','Mesilla','nm','worship','standing',32.27489,-106.79596,'exact','open','walk','','1906 (parish 1852)',
  'The Mexican government ordered a church for Mesilla in 1852, and the first was built on the south side of the plaza. A later church in the French style rose on the north side, and its first bell was ordered in 1876. The present church on that site dates from 1906 (Wikipedia also gives 1908). It is in the Diocese of Las Cruces.',
  'A fired-brick church with a bell tower at each front corner, on the north side of Mesilla Plaza inside a low stone wall. Plaster was taken off inside and out in the 1960s, leaving the brick showing (Wikipedia). A memorial to parishioners killed in war stands by the door.',
  '',
  'The parish church at 2280 Calle Principal, Mesilla; office Monday to Friday 9 a.m. to 4 p.m., 575-526-9349 (parish page). The cemetery is open daily 7 a.m. to 5 p.m.',
  [['Basilica of San Albino','https://sanalbino.org/'],W('Basilica of San Albino')],
  brick='yes',hours='Mass Saturday 4:30 p.m.; Sunday 8 a.m. (Spanish), 9:30 and 11 a.m.; Monday to Friday 9 a.m. (parish page)',conf='mixed'),
]

PIN_NOTES={
 'elizabethtown-nm':'Wikipedia coordinate for the townsite; the boarding-house wall and the cemetery were not found on the aerial.',
 'st-james-hotel-cimarron-nm':'OpenStreetMap point for the St. James Hotel.',
 'shuler-theater-raton-nm':'OpenStreetMap point for the Shuler, 131 North 2nd Street.',
 'eklund-hotel-clayton-nm':'OpenStreetMap point for the Eklund Hotel, 15 Main Street.',
 'cleveland-roller-mill-nm':'Address lookup point for the Cleveland Roller Mill Museum.',
 'kit-carson-house-taos-nm':'OpenStreetMap point for the Kit Carson House; on a building on the aerial. The federal land map labels the spot Taos Pueblo land, which the sources read do not say.',
 'santuario-de-chimayo-nm':'OpenStreetMap point for the Santuario.',
 'chama-railyard-nm':'HMdb position of the National Historic Landmark marker on the depot.',
 'el-rancho-hotel-gallup-nm':'OpenStreetMap point for the El Rancho Hotel.',
 'san-felipe-de-neri-albuquerque-nm':'OpenStreetMap point for the church.',
 'kimo-theatre-albuquerque-nm':'OpenStreetMap point for the KiMo, 423 Central Avenue NW.',
 'golden-nm':'OpenStreetMap church building beside the San Francisco church cemetery.',
 'cuervo-nm':'OpenStreetMap point for the hamlet, which fell on the I-40 embankment; moved 75 m south onto the town\'s open ground south of the interstate. The school and church were not singled out.',
 'blue-swallow-motel-tucumcari-nm':'OpenStreetMap point for the Blue Swallow Motel.',
 'glenrio-nm':'OpenStreetMap State Line Bar building, on the New Mexico side of the line; the aerial shows open ground there, perhaps taken before the rebuilding.',
 'hotel-clovis-nm':'Address lookup point for Hotel Clovis Lofts.',
 'kelly-nm':'OpenStreetMap St. John the Baptist church, where visitors park; the headframe is up the hill.',
 'pioneer-store-chloride-nm':'OpenStreetMap point for the Pioneer Store Museum.',
 'kingston-nm':'OpenStreetMap point for the Percha Bank.',
 'shakespeare-nm':'OpenStreetMap point for the Shakespeare Ghost Town tours.',
 'basilica-san-albino-mesilla-nm':'Address lookup point for 2280 Calle Principal; on the twin-towered church on the aerial.',
}
