# November 19, 2026: Lincoln County, New Mexico: the Lincoln County War town of Lincoln, Fort Stanton, the gold camp of
# White Oaks, the Jicarilla Mountains, Carrizozo, Ruidoso and the Hondo valley. Region drawn at random by
# tools/choose.py (nm); the county chosen inside it.
# Sources read in this session: National Register nomination forms (NPGallery "_text" PDFs, read with tools/page.py:
# Lincoln 66000477, White Oaks 70000403, Fort Stanton 73001142, Jicarilla Schoolhouse 83001623, Old Dowlin Mill
# 13000768, Carrizozo Woman's Club 03000995, Paden Drugstore 05000204; the Monjeau Lookout form 87002483 is a scan with no
# text layer and was not read), Wikipedia (tools/wiki_raw.py), HMdb marker pages (texts and positions), fortstanton.org,
# the Lincoln National Forest pages, Clio, Discover Ruidoso, Legends of America, New Mexico Ghost Towns and the Hurd
# gallery's own page. The New Mexico Historic Sites pages (nmhistoricsites.org) came back as the same generic text for
# every address, so Lincoln's hours are from the Clio entry and the Los Alamos Daily Post, not from the state's page.
from data_b import N
BATCH={'key':'nm_lincoln_drpx','label':'New Mexico: Lincoln, Fort Stanton and White Oaks','added':'2026-11-19 00:23'}

def NR(ref,label):
    return [label+' (National Register nomination)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/%s_text'%ref]
def HM(m,label):
    return ['HMdb: '+label,'https://www.hmdb.org/m.asp?m=%d'%m]
LINC_NR=NR('66000477','Lincoln Historic District')
LINC_W=['Wikipedia: Lincoln Historic District','https://en.wikipedia.org/wiki/Lincoln_Historic_District_(Lincoln,_New_Mexico)']
LINC_CLIO=['Clio: Lincoln Historic Site Courthouse Museum','https://www.theclio.com/entry/77677']
LINC_ACC=('Lincoln Historic Site, run by New Mexico Historic Sites (state Department of Cultural Affairs); the 1974 nomination says the courthouse, the Tunstall store and other buildings are state-owned. Hours not checked on the state\'s own page, which did not open: '
          'the Clio entry gives 9 a.m. to 5 p.m. daily, closed New Year\'s Day, Easter, Thanksgiving and Christmas, and a Los Alamos Daily Post notice (read in an archived copy of April 12, 2026) gives an opening time of 10 a.m.; '
          'check before you go. Admission fee not checked. Lincoln is one street along U.S. 380; park along the street or at the visitor centre, as signed (parking not checked on the ground). '
          'Many other houses in the village are private homes.')
WO_NR=NR('70000403','White Oaks Historic District')
WO_W=['Wikipedia: White Oaks, New Mexico','https://en.wikipedia.org/wiki/White_Oaks,_New_Mexico']
WO_RUI=['Discover Ruidoso: White Oaks Ghost Town','https://www.discoverruidoso.com/info/white-oaks-ghost-town']
WO_ROAD='White Oaks is about 3 miles off U.S. 54 on State Road 349, north-east of Carrizozo. Most of the old town is private property: keep to the roads. Parking not checked on the ground.'
FS_ACC=['Fort Stanton Inc.: hours and admission','https://fortstanton.org/information']

PLACES=[
N('lincoln-county-courthouse-lincoln-nm','Old Lincoln County Courthouse (Murphy-Dolan Store)','Lincoln','nm','civic','standing',33.49372,-105.39068,'site','public','walk','','1874',
  'Built in 1874 as the store and home of L. G. Murphy & Co., the headquarters of the Murphy-Dolan side in the Lincoln County War of 1878. The firm failed and the building became the county courthouse in 1880, serving as the county\'s government and court until 1913. Billy the Kid broke out of the jail here in April 1881, killing his two guards.',
  'A two-storey, L-shaped building of stuccoed adobe brick with a hipped shingle roof and a two-storey porch across the front (1974 nomination). It is a museum of the state historic site. Interior fabric not checked.',
  'The building Billy the Kid shot his way out of in 1881.',
  LINC_ACC,
  [LINC_NR,LINC_W,LINC_CLIO,HM(119775,'Murphy-Dolan Store')],brick='no'),
N('tunstall-store-lincoln-nm','Tunstall Store','Lincoln','nm','civic','standing',33.49277,-105.38705,'site','public','walk','','1877–1878',
  'The store of the Englishman John H. Tunstall and the lawyer Alexander McSween, rivals of the Murphy-Dolan store; Tunstall\'s killing in February 1878 set off the Lincoln County War, and McSween was killed in the July battle. The marker gives the building as 1877, the nomination as 1878. The store was looted in the war but went on trading, notably under John M. Penfield.',
  'A single-storey U-shaped building of plastered adobe with a gable roof and a porch the length of the south front; a later addition forms the west arm (nomination). A photograph caption in the Los Alamos Daily Post shows a store interior open to visitors. Interior fabric not checked.',
  '',
  LINC_ACC+' The store was closed for a time in early 2026 after bats got into the attic, and reopened (Los Alamos Daily Post).',
  [LINC_NR,HM(45991,'Tunstall-McSween Store'),['Los Alamos Daily Post: Tunstall Store opens (archived copy)','https://ladailypost.com/tunstall-store-to-open-this-weekend/']],conf='mixed',brick='no'),
N('torreon-lincoln-nm','The Torreon','Lincoln','nm','fort','standing',33.49256,-105.38604,'exact','public','walk','','1850s',
  'A round stone defence tower from the first years of La Placita del Rio Bonito, the village that became Lincoln in 1869; the settlers\' huts stood round a plaza with the tower in it, as a refuge from Apache raids. In the Lincoln County War Murphy\'s sharpshooters were posted in it. The Chaves County Historical Society restored it from 1937; the nomination says it was reconstructed.',
  'A circular stone tower with a second floor on vigas and an open top (nomination). Stands beside U.S. 380 at milepost 97.8.',
  '',
  'Owned by the State of New Mexico (1974 nomination). Seen from U.S. 380 in the middle of Lincoln. '+LINC_ACC,
  [LINC_NR,HM(45990,'Torreon')],brick='no'),
N('san-juan-church-lincoln-nm','San Juan Bautista Church','Lincoln','nm','civic','standing',33.49218,-105.38607,'site','view','walk','','1887',
  'La Iglesia de San Juan Bautista, Lincoln\'s adobe church, dedicated in 1887, just after the years of the Lincoln County War. New Mexico State Monuments restored it in 1984.',
  'A rectangular adobe building (nomination), beside the Torreon on U.S. 380. Whether it is open and what survives inside was not checked.',
  '',
  'In Lincoln\'s historic district, on U.S. 380; who owns it now and whether it is open was not checked: see it from the road.',
  [LINC_NR,HM(45970,'San Juan Church')],brick='no'),
N('fort-stanton-nm','Fort Stanton','Fort Stanton','nm','fort','standing',33.4952,-105.5255,'site','public','walk','','1855–1896',
  'An Army post founded in 1855 against the Mescalero Apaches; Confederates held it in 1861, and Kit Carson, John J. Pershing and Buffalo Soldiers of the 9th Cavalry served here. The Army left in 1896, and in 1899 it became the country\'s first federal tuberculosis sanatorium; in the Second World War German seamen from the liner Columbus were held here. It is now a state historic site.',
  'Stone buildings round the parade ground: the nomination says a dozen or more predate 1896 and several keep walls from the 1850s, with one adobe building of the fort period. The museum is in an 1855 barracks that became the hospital\'s administration building. The Fort Administration Building marker says most buildings began in 1855 as single-storey stone; it was raised a storey for the hospital and had a theatre upstairs.',
  'A frontier fort that became a TB hospital and a wartime internment camp.',
  'Fort Stanton Historic Site, 104 Kit Carson Road, on NM 220 off U.S. 380 between Capitan and Lincoln. Its own page gives Thursday to Monday, 10 a.m. to 4 p.m., closed Tuesday and Wednesday; $7 for adults, free for 16 and under. Parking not checked on the ground. The land round it is the Bureau of Land Management\'s Fort Stanton–Snowy River Cave National Conservation Area.',
  [NR('73001142','Fort Stanton'),['Wikipedia: Fort Stanton','https://en.wikipedia.org/wiki/Fort_Stanton_(New_Mexico)'],FS_ACC,['Fort Stanton Inc.: the museum','https://www.fortstanton.org/museum'],HM(85802,'Fort Administration Building')],brick='no'),
N('hoyle-house-white-oaks-nm','Hoyle House ("Hoyle\'s Castle")','White Oaks','nm','town','standing',33.74819,-105.73515,'exact','view','drive','','1893',
  'A two-storey Victorian house built in 1893 by Watt Hoyle, an owner of the Old Abe Mine, for a fiancée who never came; it was called Hoyle\'s Folly and, by the account in Legends of America, its inside was never finished. It is one of the few buildings left of the gold camp of White Oaks.',
  'Steep gables and a sharp roof; Discover Ruidoso mentions a widow\'s walk. Sources disagree on the walls: the 1970 nomination calls it the stone Hoyle house, Legends of America a brick home. Interior not checked.',
  'A gold-boom mansion built for a bride who never came.',
  'Private: see it from the road only. '+WO_ROAD,
  [WO_NR,['Legends of America: White Oaks','https://www.legendsofamerica.com/nm-whiteoaks/'],WO_RUI],conf='mixed',brick='?'),
N('white-oaks-schoolhouse-nm','White Oaks Schoolhouse','White Oaks','nm','civic','standing',33.75184,-105.73764,'exact','view','walk','','1895–1947',
  'The large brick school of the White Oaks gold camp, first used in 1895 and closed as a school in 1947, according to New Mexico Ghost Towns, which gives its cost as $10,000. It is now a museum of the town\'s history.',
  'The 1970 nomination names it among the brick and stone buildings that outlasted the town. A 2022 visitor\'s blog says the museum opens only at weekends. Interior not checked.',
  '',
  'A museum (Discover Ruidoso); who runs it and its hours were not checked; a 2022 blog says weekends only. '+WO_ROAD,
  [WO_NR,['New Mexico Ghost Towns: White Oaks','https://newmexicoghosttowns.net/white-oaks-nm'],WO_RUI,['Off Center & Not Even: Another Old School (2022)','https://offcenternoteven.com/2022/09/09/another-old-school/']],brick='?'),
N('cedarvale-cemetery-white-oaks-nm','Cedarvale Cemetery','White Oaks','nm','burial','standing',33.74128,-105.74603,'site','view','walk','cemeteries','1880s',
  'The burying ground of White Oaks. Susan McSween Barber, widow of the Lincoln County War\'s Alexander McSween, moved to White Oaks in 1902 and was buried here in 1931; so was William C. McDonald, New Mexico\'s first governor after statehood, once a White Oaks lawyer and bank president. The 1970 nomination says its many old gravestones were unvandalized and well kept.',
  'Old headstones on a hillside south-west of the town; a state marker on State Road 349 names it.',
  '',
  'Ownership not checked; visitors are named by Discover Ruidoso. Keep to the cemetery and respect the graves. '+WO_ROAD,
  [WO_NR,WO_W,HM(280155,'White Oaks')],brick='?'),
N('no-scum-allowed-saloon-white-oaks-nm','No Scum Allowed Saloon','White Oaks','nm','civic','standing',33.7503,-105.73643,'exact','public','drive','','',
  'The one saloon of the old gold camp still open, in a building Discover Ruidoso calls a hundred years old and made of brick. Its date of building was not found in any source opened.',
  'A brick building on the main road through White Oaks; inside not checked.',
  '',
  'A privately owned working bar, open to customers when it trades (hours not checked). '+WO_ROAD,
  [WO_W,WO_RUI],brick='?'),
N('jicarilla-schoolhouse-nm','Jicarilla Schoolhouse','Jicarilla','nm','civic','standing',33.86111,-105.65444,'area','view','drive','','1907',
  'A one-room school of 1907 for the mining and homesteading families of the Jicarilla Mountains, built by the neighbours of squared pine logs hewn about a mile away on Ancho Peak. It was the biggest building in the mountains and served also as meeting hall, church and Saturday-night dance hall; the community lasted into the 1940s.',
  'Squared log walls with dovetailed corners chinked with split strips, a wide central door and three big windows a side; inside, tongue-and-groove boards on walls and ceiling (1983 nomination). Interior not checked.',
  'A hewn-log school in the gold hills, built by its own families.',
  'On State Road 349 in the Lincoln National Forest (Wikipedia, nomination). Whether it is open was not checked: see it from outside. A long gravel drive; road condition not checked.',
  [NR('83001623','Jicarilla Schoolhouse'),['Wikipedia: Jicarilla Schoolhouse','https://en.wikipedia.org/wiki/Jicarilla_Schoolhouse']],brick='no'),
N('monjeau-lookout-nm','Monjeau Lookout','Alto','nm','landmark','standing',33.43082,-105.73158,'exact','public','drive','','1936–1940',
  'A fire lookout of the Lincoln National Forest, first built in 1936 and rebuilt in 1940 by the Civilian Conservation Corps (Forest Service). Wikipedia describes it as a native stone tower with living quarters, topped by a metal-framed cab.',
  'The stone tower on the summit, with wide views. The National Register form is a scan with no text and was not read. Interior not checked.',
  '',
  'Lincoln National Forest, Smokey Bear Ranger District. The Forest Service says the dirt road up is steep in places and closes in winter with snow; visit in summer. No water; restroom information not available. Wikipedia says the last mile of the road is sometimes gated, and then you walk up. A mapped lot is just below the summit.',
  [['Lincoln National Forest: Monjeau Lookout','https://www.fs.usda.gov/r03/lincoln/recreation/monjeau-lookout'],['Wikipedia: Monjeau Lookout','https://en.wikipedia.org/wiki/Monjeau_Lookout']],th=[33.43142,-105.73097],thn='Lot on Monjeau Lookout Road (OpenStreetMap)',brick='no'),
N('old-dowlin-mill-ruidoso-nm','Old Dowlin Mill','Ruidoso','nm','industry','standing',33.32377,-105.65063,'site','view','drive','','1868',
  'Ruidoso\'s oldest building, a water mill built in 1868 by Capt. Paul Dowlin, a Civil War veteran who had served at Fort Stanton, after his first mill down the hill was washed away. It was also a store, blacksmith shop and post office, and the town grew round it. The 2013 nomination calls it the only water-powered gristmill still working on its first site in New Mexico.',
  'A long adobe-block building, an 18-foot wooden flume 79 feet long, and a 16-foot overshot wheel on stone footings that turns 18-inch flint millstones inside (2013 nomination). The nomination gave its use then as a museum and gallery; whether the public can go in now was not checked.',
  'The water wheel that started Ruidoso.',
  'Privately owned, at 641 Sudderth Drive (nomination). The wheel and flume are seen from the street. Parking not checked.',
  [NR('13000768','Old Dowlin Mill'),['Wikipedia: Old Dowlin Mill','https://en.wikipedia.org/wiki/Old_Dowlin_Mill']],brick='no'),
N('carrizozo-womans-club-nm','Carrizozo Woman\'s Club','Carrizozo','nm','civic','standing',33.6425,-105.878611,'site','view','drive','','1939',
  'A Pueblo Revival clubhouse of adobe built in 1939 as a Works Progress Administration project, for the town\'s woman\'s club. A bad crack in an adobe wall put it on New Mexico\'s list of ten most endangered places in 2002, which led to its listing.',
  'An L-shaped building with exposed vigas and a portal; inside, a circular meeting room, the Round Room, with exposed beams carried by trusses above the ceiling (2003 nomination). Interior not checked.',
  '',
  'At 908 Eleventh Street; a club building, not open as a museum: see it from the street. Street parking; not checked on the ground.',
  [NR('03000995','Carrizozo Woman\'s Club'),['Wikipedia: Carrizozo Woman\'s Club','https://en.wikipedia.org/wiki/Carrizozo_Woman%27s_Club']],brick='no'),
N('padens-drug-store-carrizozo-nm','Paden\'s Drug Store','Carrizozo','nm','civic','standing',33.64114,-105.87828,'exact','view','drive','','1909',
  'A drugstore and soda fountain on Carrizozo\'s main street: the front building went up in 1909 and was raised a storey in 1917 by the local builder D. B. Tennis. The Paden name stayed on the pharmacy until 1954; from 1977 Roy Dow ran a gift shop and ice-cream parlour in it. It was sold in 2022.',
  'Plate-glass shop windows between brick pilasters, a corner entrance and a wooden awning; the 2005 nomination says the ground floor still felt like an early 1900s pharmacy and soda fountain. Whether it is open now and what survives inside was not checked.',
  '',
  'Private, at 1200 Central Avenue (U.S. 54) per OpenStreetMap; see it from the street. Street parking; not checked on the ground.',
  [NR('05000204','Paden Drugstore Complex'),['Wikipedia: Paden\'s Drug Store','https://en.wikipedia.org/wiki/Paden%27s_Drug_Store']],brick='?'),
N('hurd-house-san-patricio-nm','Peter and Henriette Wyeth Hurd House','San Patricio','nm','landmark','standing',33.403675,-105.329725,'area','view','drive','','1930s',
  'The ranch house and studios of the painters Peter Hurd and Henriette Wyeth Hurd, who lived and painted here from the 1930s until their deaths in 1984 and 1997. Hurd bought 40 acres and an adobe hacienda here in the early 1930s. It was listed in 2014 and made a National Historic Landmark in 2024; their son Michael Hurd keeps the house and runs the Hurd–La Rinconada gallery beside it.',
  'A house round a placita, an open courtyard in the manner of the old New Mexico ranchos (Wikipedia). The family gallery, of exposed stabilized adobe, opened in 1986 on the corner of the polo field. Interior of the house not checked.',
  '',
  'Private ranch. The gallery is open to the public (its own page); its hours and whether the house can be seen were not checked. On U.S. 70 at San Patricio.',
  [['Wikipedia: Peter and Henriette Wyeth Hurd House','https://en.wikipedia.org/wiki/Peter_and_Henriette_Wyeth_Hurd_House'],['Hurd–La Rinconada Gallery: visit','https://hurdgallery.com/visit'],['KLAQ: national historic landmark','https://klaq.com/new-mexico-artists-national-historic-landmark/']],brick='?'),
]

PIN_NOTES={
 'lincoln-county-courthouse-lincoln-nm':'HMdb position of the Murphy-Dolan Store marker on U.S. 380; checked on the aerial.',
 'tunstall-store-lincoln-nm':'HMdb position of the Tunstall-McSween Store marker; checked on the aerial.',
 'torreon-lincoln-nm':'OpenStreetMap tower "Torreon"; agrees with the HMdb marker position.',
 'san-juan-church-lincoln-nm':'HMdb position of the San Juan Church marker; checked on the aerial.',
 'fort-stanton-nm':'Moved with pix.py from the OpenStreetMap park point (on the road, 200 m east) onto the open parade ground ringed by the old buildings, as seen on the aerial.',
 'hoyle-house-white-oaks-nm':'OpenStreetMap building "Hoyle House", 950 Pine Street.',
 'white-oaks-schoolhouse-nm':'OpenStreetMap museum "White Oaks Schoolhouse Museum".',
 'cedarvale-cemetery-white-oaks-nm':'OpenStreetMap cemetery "Cedarvale Cemetery".',
 'no-scum-allowed-saloon-white-oaks-nm':'OpenStreetMap bar "No Scum Allowed Saloon".',
 'jicarilla-schoolhouse-nm':'National Register list coordinate. The aerial shows a clearing at a fork of the gravel road among pinon and juniper, but no building could be picked out at the ring, so area only.',
 'monjeau-lookout-nm':'OpenStreetMap tower "Monjeau Lookout"; agrees with Wikipedia.',
 'old-dowlin-mill-ruidoso-nm':'OpenStreetMap "Old Mill" point, which agrees with the ArcGIS geocoder\'s point address for 641 Sudderth Drive; the National Register list coordinate fell on the road 280 m east.',
 'carrizozo-womans-club-nm':'National Register list coordinate; checked on the aerial.',
 'padens-drug-store-carrizozo-nm':'OpenStreetMap historic building "Paden\'s Drug Store".',
 'hurd-house-san-patricio-nm':'Wikipedia / National Register coordinate; ranch ground, so area only.',
}
