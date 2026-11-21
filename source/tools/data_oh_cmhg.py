# November 21, 2026: a first scatter of places across Ohio, away from Licking County (the only ground worked before):
# the Lake Erie shore and the northeast (Squire's Castle, Marblehead, Zoar, Mansfield), the northwest (Providence on the
# Maumee, the Deep Cut at Spencerville), the west and southwest (Bear's Mill, the Piatt castle, the Golden Lamb, Fort
# Ancient) and the southeast (Marietta, Hope Furnace, Buckeye Furnace).
# Region taken by tools/choose.py --thinnest (oh, 20 places).
# Sources read in this session: Wikipedia articles (tools/wiki_raw.py), and the visitor pages of Cleveland Metroparks,
# the Ohio State Reformatory Preservation Society, the Zoar Community Association, the Marblehead Lighthouse Historical
# Society, the Golden Lamb, the Mac-A-Cheek Foundation, the Northwest Territory Museum Society (Campus Martius),
# Metroparks Toledo and the Hopewell Ceremonial Earthworks partnership (tools/page.py). The Ohio History Connection's
# pages (ohiohistory.org) answered HTTP 403, Bear's Mill's own site reset the connection, and Mill Creek MetroParks
# and the Johnny Appleseed park district would not open or came back drawn by script.
from data_b import N
from data_ma import W
BATCH={'key':'oh_cmhg','label':'Ohio: a first scatter from Lake Erie to the Ohio River','added':'2026-11-21 20:26'}

OHC='The Ohio History Connection owns it; its pages answered HTTP 403 in this session, so hours were not checked: look on ohiohistory.org before going.'

PLACES=[
N('squires-castle-willoughby-hills',"Squire's Castle",'Willoughby Hills','oh','landmark','ruins',41.58,-81.41917,'exact','public','walk','','1895–1897',
  "About 1890 Feargus B. Squire, a Standard Oil executive, bought 525 acres of forest east of Cleveland for an English-style country estate he called River Farm. He began the gatekeeper's house about 1895 and finished it about 1897, in Romanesque Revival style, of locally quarried Euclid bluestone, with no electricity, gas or running water. The manor house was never built; Squire used the gatehouse as an occasional weekend home and sold the estate in 1922, and the Cleveland park board bought most of it in 1925.",
  "The stone shell of the three-storey gatehouse, open to the sky inside: the park removed the upper floors and filled in the basement, and vandals took the leaded glass and nearly every interior detail. The lawns in front are a picnic ground.",
  "The gatehouse of a mansion that was never built.",
  "Cleveland Metroparks, North Chagrin Reservation, off Chagrin River Road. Reservations are open 6 a.m. to 11 p.m. (the Metroparks FAQ page). Parking: the Squire's Castle lot just north of the building.",
  [W("Squire's Castle"),["Cleveland Metroparks: Squire's Castle",'https://www.clevelandmetroparks.com/parks/visit/parks/north-chagrin-reservation/squire-s-castle'],
   ['Cleveland Metroparks: FAQs (park hours)','https://www.clevelandmetroparks.com/about/cleveland-metroparks-organization/faqs']],
  th=[41.58126,-81.41875],thn="Squire's Castle lot, North Chagrin Reservation",brick='no',hours='Daily 6 a.m. to 11 p.m. (the reservation)'),

N('ohio-state-reformatory-mansfield','Ohio State Reformatory','Mansfield','oh','inst','standing',40.78446,-82.50241,'exact','open','drive','','1886–1990',
  "A reformatory for young first offenders, meant as the step between the boys' school at Lancaster and the state penitentiary in Columbus. It went up from 1886 to 1910, slowed by lack of money, to designs by Levi T. Scofield of Cleveland, mixing Victorian Gothic, Richardsonian Romanesque and Queen Anne; the field had been a Civil War training camp, Camp Mordecai Bartley. A federal court order closed it in December 1990. The Shawshank Redemption (1994) was filmed here, and a preservation society formed in 1995 runs it as a historic site.",
  "The castle-like front block of brick and concrete, the warden's quarters and the great cell blocks. Self-guided and guided tours go inside; the society's tours page says that from August 31 to mid-November a haunted-house setup closes solitary, the ground levels of the cell blocks and the showers.",
  "Shawshank's prison, empty since 1990.",
  "Owned and run as a museum by the Ohio State Reformatory Preservation Society. Its FAQ page: open every day of the year 10 a.m. to 4 p.m., closed on major holidays and December 23 to January 1; self-guided tour $30, guided tours $40. Parking: the lot north of the old building, seen on the aerial.",
  [W('Ohio State Reformatory'),['Ohio State Reformatory: FAQs','https://www.mrps.org/faqs/'],['Ohio State Reformatory: Tours','https://www.mrps.org/tours/']],
  th=[40.78506,-82.50167],thn='Reformatory visitor lot',brick='?',hours='Daily 10 a.m. to 4 p.m.; closed major holidays and December 23 to January 1'),

N('zoar-village','Zoar Village','Zoar','oh','town','standing',40.61397,-81.42308,'site','open','walk','','1817–1898',
  "German Radical Pietists, the Society of Separatists of Zoar, founded the village in 1817 and held everything in common, with farms, shops and mills run by elected trustees. At its height in the 1850s the society owned more than 10,000 acres; it voted to disband in 1898 and divided the property among its 222 members. Much of the village plan and many society buildings survive; it is a National Historic Landmark district (2016). A failing 1936 flood levee on the Tuscarawas threatened the village until the Army Corps of Engineers finished a $14 million repair in 2023.",
  "A street plan and German-style society buildings, ten of them restored as museum buildings, and the central garden laid out after the Book of Revelation (its great central tree is gone). The Zoar Community Association runs guided tours inside the museum buildings, April to October. Interior details not checked.",
  "A communal village that kept its shape after the commune ended.",
  "The village streets are public. The museum buildings are owned by the Ohio History Connection and shown by the Zoar Community Association: its hours page gives guided tours $12 an adult and self-guided tours $10 (May to September, Wednesday and Thursday 11 a.m. to 3 p.m.); closed major holidays. Parking in the village, not checked.",
  [W('Zoar, Ohio'),['Historic Zoar Village: museum hours','https://historiczoarvillage.com/?p=24']],
  brick='?',hours='April–May and October Sat 11–4, Sun 12–4; June–September Wed–Sat 11–4, Sun 12–4'),

N('marblehead-lighthouse-oh','Marblehead Lighthouse','Marblehead','oh','light','standing',41.53644,-82.71172,'exact','open','drive','','1821–',
  "Built in 1821 by William Kelly with two local men, a 50-foot tower of native limestone at the tip of the Marblehead Peninsula, lit in 1822: the oldest lighthouse in continuous use on the American side of the Great Lakes. Its first keeper was Benajah Wolcott, a Revolutionary War veteran; fifteen keepers followed, two of them women. A Fresnel lens came in 1858, the 1821 stone keeper's house was replaced by the present frame house in 1880, the Coast Guard took over in 1946 and automated it in 1958. Ohio's natural resources department has held the grounds since 1972 and the tower since 1998.",
  "The limestone tower (25 feet across at the base, walls 5 feet thick), the 1880 frame keeper's house, now a museum with a Fresnel lens, and a replica lifesaving station with a restored Coast Guard boat. Tower tours in season.",
  "The oldest working light on the American Great Lakes.",
  "Marblehead Lighthouse State Park (Ohio Department of Natural Resources); the Marblehead Lighthouse Historical Society runs the museums and tower tours. Its visit page: the park is open all the time and the buildings shut in winter; tower tickets $5 (age 6 and up), sold only at the tower, a limited number each day. Parking: the lot on Lighthouse Road, as mapped; not checked.",
  [W('Marblehead Light (Ohio)'),['Marblehead Lighthouse Historical Society: visit','https://www.marbleheadlighthouseohio.org/']],
  th=[41.53689,-82.71419],thn='Lighthouse Road lot',brick='no',hours='Memorial Day weekend to Labor Day daily noon–4; September and first October weekend Sat–Sun noon–4; grounds always'),

N('golden-lamb-lebanon','Golden Lamb','Lebanon','oh','hotel','standing',39.43361,-84.20833,'site','open','drive','','1803–',
  "Ohio's oldest hotel, opened in 1803 as a licensed log tavern on Lebanon's main street, on the road between Cincinnati and Columbus. A brick inn replaced the log house in 1815, and the present four-storey building grew around it; it took its name from the lamb on its signboard. Twelve presidents stayed or ate here, from William Henry Harrison to George W. Bush, and so did Charles Dickens, Mark Twain and Harriet Beecher Stowe. It was refurnished with Shaker furniture in 1927 and listed on the National Register in 1978.",
  "A working inn and restaurant in the 1815 building, furnished with Shaker pieces. Interior otherwise not checked.",
  "Where Dickens, Twain and twelve presidents stopped.",
  "A private hotel and restaurant (the Portman family); the public may dine and stay. Its home page gave no opening hours that this session could read. Parking in downtown Lebanon, not checked.",
  [W('Golden Lamb Inn'),['The Golden Lamb','https://www.goldenlamb.com/']],
  brick='?',hours='?'),

N('hope-furnace-lake-hope','Hope Furnace','Zaleski','oh','industry','ruins',39.33194,-82.34028,'site','public','walk','','1854–1874',
  "A sandstone blast furnace shaped like a cut-off pyramid, one of two iron furnaces left in Vinton County. It smelted iron from 1854 to 1874 with coal or charcoal, and at its height a community of at least three hundred people lived round it. When it closed the workers left and every building was lost. It was listed on the National Register in 1973.",
  "The square sandstone stack beside State Route 278, with slag still scattered over the ground. Nothing is left of the furnace town.",
  "An iron furnace whose town walked away.",
  "Lake Hope State Park (Ohio Department of Natural Resources), on SR 278 about 5 miles northeast of Zaleski. Parking: the small lot on SR 278 beside the furnace, as mapped (the land map puts it in Zaleski State Forest). Park hours not checked.",
  [W('Hope Furnace')],
  th=[39.33149,-82.33983],thn='SR 278 lot by the furnace',brick='no'),

N('buckeye-furnace-jackson','Buckeye Furnace','Wellston','oh','industry','standing',39.05639,-82.45722,'site','open','drive','','1852–1894',
  "A charcoal iron furnace of the Hanging Rock Iron Region, which made Ohio a leading iron state for the Union in the Civil War. It ran from 1852 to 1894 on a 270-acre tract, with the village of Buckeye as its company town. Like other furnaces of its day it has a lower level for the furnace and an upper one for storing charcoal. The Ohio Historical Society bought it in 1935 and from the 1960s rebuilt the site's buildings from what former furnace workers remembered.",
  "The stone furnace stack, with reconstructed site buildings round it. Tours, per Wikipedia; times not checked.",
  "A Civil War iron furnace with its buildings put back from memory.",
  "A state historic site owned by the Ohio History Connection. "+OHC+" No parking lot is mapped; not checked.",
  [W('Buckeye Furnace')],
  brick='?',hours='?'),

N('piatt-castle-mac-a-cheek','Piatt Castle Mac-A-Cheek','West Liberty','oh','landmark','standing',40.25103,-83.72681,'site','open','drive','','1864–1871',
  "Abram S. Piatt began this three-storey Gothic house in 1864, the same year his brother Donn began Mac-O-Chee about three-quarters of a mile away; Mac-A-Cheek was finished in 1871 and Mac-O-Chee in 1879. Both have towers, painted ceilings and intricate woodwork. Tours of Mac-A-Cheek began in 1912; the family sold Mac-O-Chee in 2019 to pay for Mac-A-Cheek's restoration. Both are on the National Register (1982).",
  "The towered house of pale stone, with red brick chimneys (Commons photograph), set back from the road, with painted ceilings and woodwork; visits are self-guided past family artifacts and exhibits.",
  "Two brothers, two castles, three-quarters of a mile apart.",
  "Run by the Mac-A-Cheek Foundation for the Humanities, one mile east of West Liberty. Its home page (2026 season): adults $15, youth $8, seniors $12. Mac-O-Chee, the other castle, is privately owned and not open. Parking at the house.",
  [W('Piatt Castles'),['Piatt Castle Mac-A-Cheek','https://www.piattcastles.org/']],
  brick='some',hours='2026: April 4–May 24 Sat–Sun 10–4; May 25–Sept 7 daily 10–5; Sept 8–Oct 25 Sat–Sun 10–4'),

N('rufus-putnam-house-marietta','Rufus Putnam House (Campus Martius Museum)','Marietta','oh','landmark','standing',39.42125,-81.46111,'exact','open','walk','','1788–',
  "General Rufus Putnam of the Ohio Company of Associates began this house soon after he arrived in 1788, as part of Campus Martius, Marietta's fortification for its settlers. The walls were framed on the ground from hewn oak timbers four inches thick, pinned with wooden dowels, and fitted with planks numbered in Roman numerals. It is the only part of the fort left, and is called the oldest building in Ohio. The museum building was raised around it, and holds the Ohio Company Land Office too.",
  "The post-and-plank house of 1788, enclosed inside the museum; its second floor is not wheelchair accessible.",
  "The oldest building in the Northwest Territory, inside a museum.",
  "Owned by the Ohio History Connection and run by the Northwest Territory Museum Society, 601 2nd Street (State Route 7). Its visit page: adults $10, students $5; free parking behind the museum and on the street.",
  [W('Rufus Putnam House'),W('Campus Martius Museum'),['Campus Martius Museum: plan your visit','https://mariettamuseums.org/campus-martius/plan-a-visit/']],
  brick='?',hours='Mon–Sat 9:30–5, Sun 12–5; closed New Year’s Day, Easter, Thanksgiving, Christmas Eve and Day'),

N('mound-cemetery-marietta','Mound Cemetery and the Great Mound','Marietta','oh','burial','standing',39.42,-81.45194,'site','public','walk','','1801–',
  "The town's founders kept the Great Mound, or Conus, an Adena burial mound, from being dug away by laying out the city cemetery round it in 1801. Archaeologists put the mound at about 100 BC to AD 500; it is part of the Marietta Earthworks. The cemetery holds more Revolutionary War officers than any other in the country, among them Generals Rufus Putnam and Benjamin Tupper, Commodore Abraham Whipple and Colonel William Stacy.",
  "The conical mound in the middle of the cemetery, and the gravestones of the founders round it.",
  "A town cemetery laid out to save a 2,000-year-old mound.",
  "A city cemetery; hours not checked. Street parking nearby, not checked.",
  [W('Mound Cemetery (Marietta, Ohio)')],
  brick='no'),

N('bears-mill-greenville',"Bear's Mill",'Greenville','oh','industry','standing',40.10667,-84.54194,'exact','open','drive','','1849–',
  "A water-powered gristmill on Greenville Creek, built in 1849 by Manning Hart and bought before it was finished by Gabriel Bear of Pennsylvania. When his local millstones proved poor, Bear went to France for better ones. It ground at full capacity for well over a century, slowing only in the late 1970s, and is the oldest industrial building in Darke County. The Friends of Bear's Mill, a non-profit, run it as a working mill and milling museum.",
  "A wooden mill on a stone foundation, with a metal roof, still grinding. Interior not checked.",
  "A working 1849 mill with French millstones.",
  "Owned and run by the Friends of Bear's Mill, 6450 Arcanum Bears Mill Road; its own site reset the connection in this session, so hours were not checked. Parking: OpenStreetMap maps a lot at the mill itself, on Arcanum Bears Mill Road; not checked.",
  [W("Bear's Mill")],
  brick='no',hours='?'),

N('providence-lock-44-ludwig-mill','Lock 44 and the Isaac Ludwig Mill, Providence Metropark','Grand Rapids','oh','canal','standing',41.41583,-83.85861,'site','open','walk','','1866–',
  "Providence was a canal town on the Miami and Erie Canal, which carried boats 249 miles between Toledo and Cincinnati. Metroparks Toledo keeps more than a mile of the original canal and towpath here, with Lock 44, one of the last working nineteenth-century limestone locks, and the Isaac Ludwig Mill, built over two years to 1866 as a water-wheel sawmill and changed to a turbine gristmill in the 1880s. The Providence Dam across the Maumee was built to keep the canal full.",
  "The limestone lock, which still works for the mule-drawn reproduction boat The Volunteer; the working saw and grist mill; the old canal and towpath, now part of the Buckeye Trail; WPA buildings and bridges in the park.",
  "Ohio's last working canal lock.",
  "Metroparks Toledo. Park open 7 a.m. to dark every day; the canal boat and mill run May through October (2026 tickets: adults $12). Parking and tickets at 13205 S. River Road.",
  [W('Providence Metropark'),['Metroparks Toledo: Canal Experience','https://metroparkstoledo.com/canal-experience'],['Metroparks Toledo: Providence','https://metroparkstoledo.com/explore-your-parks/providence']],
  th=[41.41623,-83.85752],thn='Canal Experience lot, South River Road',brick='?',hours='Park daily 7 a.m. to dark; mill May–Oct, e.g. Jun–Aug Wed–Sun 11–4 (2026)'),

N('miami-erie-canal-deep-cut','Miami and Erie Canal Deep Cut','Spencerville','oh','canal','traces',40.6875,-84.36528,'area','public','walk','','1825–1845',
  "To carry the Miami and Erie Canal over the ridge between the St. Marys and Auglaize rivers without locks, workers dug the bed up to 52 feet into blue clay, far deeper than the canal's own 5 feet of water. The 6,600-foot cut was one of the canal's major works; the line from Cincinnati to Toledo was built between 1825 and 1845. It is a National Historic Landmark.",
  "The long, deep, dry canal trench beside State Route 66, with trails and a picnic area.",
  "A canal dug 52 feet into a ridge.",
  "Owned by the state and run by Johnny Appleseed Metroparks and the Heritage Trails Park District as Deep Cut Historical Park, two miles south of Spencerville on SR 66. The park district's pages would not open here; hours not checked. Parking: the lot off SR 66 at the south end, as mapped.",
  [W('Miami and Erie Canal Deep Cut')],
  th=[40.68397,-84.36498],thn='SR 66 lot',brick='no'),

N('fort-ancient-earthworks','Fort Ancient Earthworks','Oregonia','oh','landmark','traces',39.40778,-84.09025,'area','open','walk','','',
  "The largest prehistoric hilltop enclosure in the country: three and a half miles of earthen walls round a 100-acre bluff 270 feet above the Little Miami River, built by the Hopewell culture in at least three stages over about 400 years. Evidence points to a ceremonial gathering place, not a fort. The state bought it in 1891 as Ohio's first state park, and in 2023 it became part of the Hopewell Ceremonial Earthworks World Heritage Site.",
  "Earthen walls, some up to 23 feet high, along miles of trails, and a museum of 9,000 square feet.",
  "The biggest hilltop earthwork in North America.",
  "Owned by the Ohio History Connection, 6123 State Route 350. The World Heritage partnership's page: admission charged; guided tours on the 1st and 3rd Fridays at 1 p.m.; closed on many holidays. Parking at the museum, not checked.",
  [W('Fort Ancient (Lebanon, Ohio)'),['Hopewell Ceremonial Earthworks: Fort Ancient','https://hopewellearthworks.org/fort-ancient/']],
  brick='no',hours='Wed–Sat 10–5, Sun 12–5; admissions end 4 p.m.'),
]

PIN_NOTES={
 'squires-castle-willoughby-hills':'Wikipedia coordinate; checked on the aerial.',
 'ohio-state-reformatory-mansfield':'The Wikipedia coordinate fell in a field about 200 m west-northwest; moved with pix.py onto the centre tower of the long old reformatory block, south of the fenced modern prison (Mansfield Correctional) on the aerial.',
 'zoar-village':'The Wikipedia village coordinate fell on a house; moved with pix.py about 75 m north onto the edge of the central garden, plain on the aerial.',
 'marblehead-lighthouse-oh':'Wikipedia coordinate; checked on the aerial.',
 'golden-lamb-lebanon':'Wikipedia coordinate; checked on the aerial.',
 'hope-furnace-lake-hope':'Wikipedia coordinate; checked on the aerial.',
 'buckeye-furnace-jackson':'Wikipedia coordinate; checked on the aerial.',
 'piatt-castle-mac-a-cheek':'Wikipedia coordinate for the Piatt Castles; it lands on a large house in the trees, and two Commons photographs titled Mac-A-Cheek Castle were taken 16 m from it.',
 'rufus-putnam-house-marietta':'Wikipedia coordinate; checked on the aerial.',
 'mound-cemetery-marietta':'Wikipedia coordinate; checked on the aerial.',
 'bears-mill-greenville':'Wikipedia coordinate; checked on the aerial.',
 'providence-lock-44-ludwig-mill':'Wikipedia coordinate for Providence Metropark; checked on the aerial.',
 'miami-erie-canal-deep-cut':'Wikipedia coordinate; prec area along the cut.',
 'fort-ancient-earthworks':'Wikipedia coordinate; prec area.',
}
