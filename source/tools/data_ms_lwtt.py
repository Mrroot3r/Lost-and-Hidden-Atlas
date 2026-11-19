# November 19, 2026: the Mississippi River country of Claiborne and Jefferson counties, Mississippi (Port Gibson, Grand
# Gulf, Rodney, Alcorn, Church Hill, Rocky Springs) and the south end of the Natchez Trace Parkway into Adams County
# (Washington and Natchez). Drawn at random by tools/choose.py (region ms); start.py found one Atlas place within 40 km
# of Port Gibson (Windsor Ruins) and none round Natchez. Sources were opened in this session: Wikipedia as raw text
# (tools/wiki_raw.py); HMdb.org marker pages (positions and inscriptions); National Park Service pages for the Natchez Trace
# Parkway (places pages, the milepost 0-131 accessibility page, Mount Locust news releases); the Grand Gulf Military Park
# pages (grandgulfpark.ms.gov); SAH Archipedia entries; MDAH's Historic Jefferson College page; Natchez Pilgrimage Tours;
# the Rodney History and Preservation Society (archived copies, 2025); natchez.org; the Natchez Democrat (2024);
# EPConnection (2017); the American Battlefield Trust.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'ms_lwtt','label':'Mississippi river country: Port Gibson, Grand Gulf, Rodney and the Natchez Trace','added':'2026-11-19 00:56'}

def HM(n,t): return L('HMdb: '+t,'https://www.hmdb.org/m.asp?m=%d'%n)
GG=L('Grand Gulf Military Park','https://www.grandgulfpark.ms.gov/about')
GGT=L('Grand Gulf Military Park: park tour','https://www.grandgulfpark.ms.gov/tour')
NPSMOB=L('NPS: Natchez Trace Parkway, accessibility, milepost 0 to 131','https://home.nps.gov/natr/planyourvisit/mobility-0-to-131.htm')
NPSHRS=L('NPS: Natchez Trace Parkway, operating hours','https://www.nps.gov/natr/planyourvisit/hours.htm')
RHPS=L('Rodney History and Preservation Society: Rodney Presbyterian (archived 2025-09-06)','https://rodneyhistory.org/rodney-presbyterian')
NATORG=L('natchez.org: Rodney Presbyterian Church undergoing repairs','https://natchez.org/news/rodney-presbyterian-church-undergoing-repairs')
GG_ACC=('Grand Gulf Military Park, a state park run by its own commission, about eight miles northwest of Port Gibson off US 61 '
  'on Grand Gulf Road. The park page gives office hours of 9 a.m. to 4:30 p.m. every day, closed on Mississippi state holidays; '
  'admission is paid at the museum (fee not stated on the page). There is a campground.')
TRACE_ACC=('Natchez Trace Parkway, National Park Service. The parkway is open all the time; no hours are given for the roadside '
  'stops (the NPS hours page lists only the Tupelo visitor center). No fee.')

PLACES=[
# ---- Grand Gulf ----
N('grand-gulf-military-park','Grand Gulf Military Park and the lost town of Grand Gulf','Port Gibson','ms','town','traces',32.03000,-91.05317,'site','public','walk','','1828–1863',
  'Grand Gulf began as a small British settlement in the 18th century and was incorporated in 1833, named for a whirlpool where the Mississippi struck a rock bluff. By the late 1830s it was a river port of about 1,000 people on 76 city blocks. Yellow fever in 1843, a tornado in 1853 and then the river itself, which carried away 55 blocks between 1855 and 1860, ruined it; by 1860 only 158 people were left. Confederate batteries here drove off Union gunboats in April 1863, and Federal troops and gunboats destroyed what was left of the town. The park opened in May 1962.',
  'The earthworks of Fort Wade, including an ammunition magazine dug out in the late 1970s, the Grand Gulf cemetery, a 75-foot observation tower over the river, a museum of town and Civil War finds, and old buildings: the Spanish House (late 1790s, pegged cypress and pine, one of two buildings left of the old town by the park\'s account), a dog-trot house and water wheel, and the Sacred Heart church moved from Rodney. The marker for the town says only a few antebellum buildings survive on what were its outskirts.',
  'A river port the Mississippi ate, then left behind.',
  GG_ACC,
  [W('Grand Gulf Military State Park'),GG,GGT,HM(105720,'Town of Grand Gulf'),HM(104093,'Fort Wade'),HM(103935,'The Spanish House')],brick='?'),
N('fort-cobun-grand-gulf','Fort Cobun','Port Gibson','ms','fort','traces',32.04270,-91.05178,'site','public','walk','forts','1863',
  'Confederates laid out Fort Cobun in March 1863 on a ledge 40 feet above the river, with a parapet nearly 40 feet thick and four big guns of the 1st Louisiana Heavy Artillery. It fired on Farragut\'s squadron on March 31, and on April 29 dueled for more than five hours with seven of Porter\'s gunboats, disabling the Tuscumbia. Porter, after the town was taken, called Grand Gulf the strongest place on the Mississippi.',
  'The earthwork of the battery, in woods at the north end of Grand Gulf Road, with markers for the fort, the Point of Rock, the whirlpool and the site of a hot-shot furnace.',
  'The battery that outlasted Porter\'s ironclads.',
  GG_ACC+' Fort Cobun is about a mile north of the museum, at the end of Grand Gulf Road (HMdb).',
  [W('Grand Gulf Military State Park'),GG,HM(105777,'Fort Cobun')],brick='no'),
N('sacred-heart-church-grand-gulf','Sacred Heart Church (moved from Rodney)','Port Gibson','ms','worship','standing',32.03058,-91.05244,'exact','public','walk','','1868',
  'A small Carpenter Gothic Catholic church built in Rodney in 1868, the year before a fire burned most of that town. Its congregation was among the poorest in the diocese; by 1937 seven people came to services and it closed. The diocese deeded it to the Rodney Foundation in 1969, the foundation gave it to the state, and in 1983 the whole building was moved to Grand Gulf and restored.',
  'The white frame church with its pointed windows, now a non-denominational chapel; the park\'s tour invites visitors to walk its aisle. Which of its fittings are original was not checked.',
  'A church carried off from a ghost town to save it.',
  GG_ACC,
  [W('Sacred Heart Roman Catholic Church (Port Gibson, Mississippi)'),L('Grand Gulf Military Park: the church','https://www.grandgulfpark.ms.gov/church'),GGT,HM(104103,'Rodney Sacred Heart Roman Catholic Church')],brick='no'),
# ---- Rodney ----
N('rodney-ms','Rodney','Lorman','ms','town','ruins',31.86128,-91.19983,'site','view','drive','','1828–1930s',
  'Rodney was incorporated in 1828 and became the port for the cotton country round it; in 1817 it had been three votes short of becoming the state capital. By 1860 it had banks, newspapers, a hotel, Mississippi\'s first opera house and over 35 stores, with Oakland College nearby. After the war the river moved away (it is now about two miles off), a fire in 1869 destroyed most of the town, and the railroad went through Fayette instead. The 1938 state guide called it a ghost river town.',
  'A ruined cemetery and Confederate earthworks on the bluff behind the town; below, the 1832 brick Presbyterian church, the frame Mount Zion (Rodney) Baptist Church of 1851, abandoned and weakened by floods, Alston\'s Grocery (about 1840) at the old Commerce Street corner, a two-story brick former store on Batchelor Street, the remains of a wooden drugstore and a few houses, all in various states of disrepair.',
  'Three votes from being the capital; now the river floods it.',
  'Most buildings are private and abandoned: look from the road and do not go in. A few people still live here. Wikipedia and the preservation society both say the town floods often; the HMdb markers stand on Muddy Bayou Road north of Rodney Road. Road conditions were not checked: go only when the river is down.',
  [W('Rodney, Mississippi'),HM(120395,'Old Town of Rodney - Structures'),L('Rodney History and Preservation Society: Mount Zion / Rodney Baptist (archived 2025-04-23)','https://rodneyhistory.org/rodney-baptist%2Fmt-zion'),NATORG],brick='some'),
N('rodney-presbyterian-church','Rodney Presbyterian Church','Lorman','ms','worship','standing',31.86278,-91.19984,'exact','view','drive','','1829–1832',
  'Work on the brick church began in 1829. The date of dedication differs between sources: January 1, 1832 by the preservation society and Wikipedia, January 1, 1831 by a 1990 Colonial Dames marker. On September 13, 1863 a Confederate cavalry party captured the captain and eighteen crew of the Union gunboat Rattler at Sunday service here; the gunboat shelled the town until the Confederates threatened to hang the prisoners. The last full-time pastor left in 1923. The Rodney History and Preservation Society bought the church in 2018 and has been repairing its failing south wall.',
  'A Federal-style red brick church with fanlights over the doors and a replica cannonball set in the front above the balcony windows where the shell struck. Wikipedia says there is a gallery for enslaved worshippers at the rear, reached by a narrow winding stair. Whether the public can go in, and when, was not checked: interior not checked.',
  'The church where a Sunday service ended in a gunboat\'s shelling.',
  'Owned by the Rodney History and Preservation Society (since 2018). Look from Muddy Bayou Road, where the markers stand. The town around it floods; go only when the river is down.',
  [L('Wikipedia: Rodney Presbyterian Church','https://en.wikipedia.org/wiki/Rodney_Presbyterian_Church'),W('Rodney, Mississippi'),RHPS,NATORG,HM(118341,'Old Rodney Presbyterian Church'),HM(244212,'Rodney Presbyterian Church')],brick='yes',conf='mixed'),
# ---- Alcorn and the Bruinsburg road ----
N('oakland-memorial-chapel','Oakland Memorial Chapel','Lorman','ms','worship','standing',31.87602,-91.13997,'exact','view','drive','','1838',
  'Built in 1838 (the campus marker gives 1840–51) for Oakland College, a Presbyterian school for the white children of the region founded in 1828 by Jeremiah Chamberlain, who was murdered in 1851 by a supporter of slavery. The college closed in the Civil War, and in 1871 the state bought the campus for Alcorn, the first land-grant college founded for Black students. The chapel is the best preserved of the three Oakland buildings left and was made a National Historic Landmark in 1976. It also served as the Alcorn basketball team\'s home gym.',
  'A three-story brick Greek temple on a raised basement, with a six-column portico and a two-stage wooden tower. The cast-iron stair in front and its six balustrade panels came from Windsor after that mansion burned in 1890. Interior not checked.',
  'The college chapel that inherited Windsor\'s iron stair.',
  'On the Alcorn State University campus, on the southwest side of ASU Drive (state highway 552 leads to the campus). It is a working university: look from the drive and ask the university before going inside.',
  [W('Oakland Memorial Chapel'),HM(119851,'The Chapel'),HM(118257,'Oakland Memorial Chapel')],brick='?'),
N('bethel-presbyterian-church-alcorn','Bethel Presbyterian Church','Alcorn','ms','worship','standing',31.90586,-91.12947,'exact','view','drive','','1840s',
  'Members of the old Bayou Pierre church formed the Bethel congregation (1824 by one state marker, 1826 by the church\'s own marker and Wikipedia) under Jeremiah Chamberlain, the founder of Oakland College. The present Greek Revival building went up in the mid-1840s, about three miles south of Windsor.',
  'Pilasters and simple hood moulds outside; inside there is no ornament at all, by the marker\'s account. The slave gallery has been removed and a tornado took the tall pointed steeple. Interior not checked.',
  'A plain country church on Grant\'s road to Port Gibson.',
  'At the corner of state highway 552 and Russum Westside Road. Whether a congregation still meets here was not checked: look from the road.',
  [W('Bethel Presbyterian Church (Alcorn, Mississippi)'),HM(105784,'Bethel Church'),HM(70394,'Bayou Pierre Presbyterian Church')],brick='?'),
# ---- Port Gibson ----
N('first-presbyterian-port-gibson','First Presbyterian Church (the hand pointing to heaven)','Port Gibson','ms','worship','standing',31.95969,-90.98178,'exact','view','drive','','1859–1860',
  'A Romanesque Revival church of 1859–60, among the earliest of its style in Mississippi, for a congregation that began as the Bayou Pierre church in 1807 and moved into town in 1828. The spire ends in a gilded hand pointing upward, after the long-time pastor Zebulon Butler, who pointed heavenward as he preached. The first hand, carved in wood by young Daniel Foley, was replaced by a metal one in 1909; it was taken down, restored and regilded and put back in August 2017, 147 feet above the ground.',
  'Stuccoed brick with round-arched openings, buttresses and stained glass. Inside (SAH Archipedia) a barrel-vaulted wooden ceiling, a raised pulpit, a gallery on carved brackets and chandeliers from the steamboat Robert E. Lee, installed in 1882. Whether visitors can go in outside services was not checked.',
  'A ten-foot gold hand points straight up over US 61.',
  'An active church at Church Street (US 61) and Walnut Street. Look from the street; interior visits were not checked.',
  [HM(104345,'First Presbyterian Church'),L('SAH Archipedia: First Presbyterian Church, Port Gibson','https://sah-archipedia.org/buildings/MS-02-ND73'),L('EPConnection: golden hand back atop Port Gibson church (2017)','https://epconnection.org/2017/08/23/iconic-golden-hand-back-atop-port-gibson-miss-epc-church/'),W('Port Gibson, Mississippi')],brick='no'),
N('temple-gemiluth-chessed','Temple Gemiluth Chessed','Port Gibson','ms','worship','standing',31.95908,-90.98263,'exact','view','drive','','1891–1892',
  'Port Gibson\'s Jewish community came from the German states and Alsace-Lorraine in the 1840s; the Hebrew Benevolent Society was incorporated in 1870 and the synagogue was built in 1891–92 for $7,000. At its peak about 50 to 60 families belonged. The congregation closed in 1986 and gave its Torah to the Museum of the Southern Jewish Experience; the building, threatened with demolition, was bought and kept by new owners who are not Jewish.',
  'Red brick, with a Moorish keyhole doorway under a Russian-style onion cupola and keyhole windows in the turret: the only Moorish Revival building in the state by Wikipedia\'s account. Inside, coloured-glass keyhole panels and a horseshoe arch round the ark niche (Wikipedia); whether the public can go in was not checked.',
  'Mississippi\'s oldest synagogue, with an onion dome on Church Street.',
  'Privately owned, at 706 Church Street (US 61). Look from the street.',
  [W('Temple Gemiluth Chessed'),HM(104343,'Temple Gemiluth Chassed')],brick='yes'),
N('samuel-gibson-house','Samuel Gibson House','Port Gibson','ms','civic','standing',31.95079,-90.98579,'exact','view','drive','','c. 1805',
  'A four-room brick house thought to have been built about 1805 for Samuel Gibson, who founded Port Gibson, with a dairy in the basement and a separate outbuilding. It was moved to this spot on Church Street in 1980.',
  'The small brick house and its dependency beside US 61 at the south end of town, with several markers on the Vicksburg campaign beside it. What it is used for now, and whether it opens, was not checked.',
  'The town founder\'s house, moved to the highway.',
  'At 1601 Church Street (US 61). Look from the roadside; use and hours not checked.',
  [HM(137975,'Samuel Gibson House')],brick='?'),
N('shaifer-house','Shaifer House (Holly Hill)','Port Gibson','ms','civic','standing',31.94815,-91.03601,'site','public','drive','','by 1863',
  'A planter\'s cottage four miles west of Port Gibson where Grant\'s army, marching inland after crossing the Mississippi at Bruinsburg, met Confederate pickets just after midnight on May 1, 1863: the first shots of the Battle of Port Gibson. The house served as a field hospital for weeks, and Charles Dana wrote of the pile of amputated limbs in its yard. In the 1870s and later Union veterans came back to meet its owner, the former Confederate Abram Keller Shaifer.',
  'A one-and-a-half-story cottage with a full-width gallery and one central chimney, joined by an open breezeway to a galleried kitchen wing, above a road worn deep into the loess; a monument marks where the first shot was fired. The porch that once wrapped to the rear was taken off in a 1981–82 renovation. Interior not checked.',
  'Where the Vicksburg campaign\'s first battle began, at midnight.',
  'Owned by the Mississippi Department of Archives and History; SAH Archipedia says it is open to the public. On Shaifer Road, about 1.5 miles west of Bessie Weathers Road. The American Battlefield Trust says most of the battlefield around it is private: keep to the house grounds and the road. Hours not checked.',
  [L('SAH Archipedia: Shaifer House (Holly Hill)','https://sah-archipedia.org/node/86793'),HM(143999,'Field Surgery on the Porch'),HM(143320,'From This Site'),L('American Battlefield Trust: Port Gibson Battlefield','https://battlefields.org/visit/heritage-sites/port-gibson-battlefield')],brick='?'),
# ---- Natchez Trace Parkway ----
N('rocky-springs-ms','Rocky Springs town site','Port Gibson','ms','town','ruins',32.08977,-90.81348,'exact','public','walk','','1790s–1930s',
  'A watering place on the old Natchez Trace by a spring and a rock outcrop, settled from the 1790s. A Methodist church went up in 1837 and an academy in 1838; by 1860 the district held 2,616 free people and about 2,000 enslaved. Yellow fever, the Civil War and then the boll weevil emptied it; the post office closed in 1932 and the last store in the 1930s. The church held services until 2010.',
  'The 1837 Methodist church and its graveyard on the hill, two rusting safes (one from the post office) and several old cisterns along a short loop trail with NPS signs. The spring no longer flows.',
  'A town of 2,600 reduced to a church and two safes.',
  TRACE_ACC+' Rocky Springs is at milepost 54.8, with a free first-come campground, restrooms and a picnic area; Wikipedia says the town site is open in daylight. NPS: the spur to the church has crushed rock, roots and several flights of steps.',
  [W('Rocky Springs, Mississippi'),L('NPS: Rocky Springs Town Site','https://www.nps.gov/places/rocky-springs-town-site.htm'),L('NPS: Rocky Springs picnic area and trailhead','https://www.nps.gov/places/rocky-springs-picnic-area-and-trailhead.htm'),NPSMOB],brick='?',th=[32.08893,-90.81322],thn='Rocky Springs parking (Old Port Gibson Road)'),
N('sunken-trace-ms','Sunken Trace','Port Gibson','ms','landmark','traces',31.97060,-90.95604,'exact','public','walk','','1700s–1800s',
  'The Old Natchez Trace began as animal and American Indian paths; in the late 1700s and early 1800s boatmen walking home from Natchez and New Orleans, riders and wagons wore it into a road. In the soft loess here the traffic cut it down into a deep sunken lane.',
  'A short walk down a stretch of the old road sunk well below the ground on either side, under trees. NPS: a compacted-earth path about three feet wide, with steep parts and roots.',
  'A road worn into a trench by feet and hooves.',
  TRACE_ACC+' Milepost 41.5, with parking for about a dozen cars.',
  [L('NPS: Sunken Trace, Milepost 41.5','https://www.nps.gov/places/sunken-trace-milepost-41-5.htm'),NPSMOB],brick='no',th=[31.97013,-90.95543],thn='Sunken Trace parking (milepost 41.5)'),
N('mount-locust-ms','Mount Locust','Natchez','ms','hotel','standing',31.68687,-91.18920,'site','public','walk','','1784',
  'William and Paulina Ferguson bought Mount Locust in 1784 and built the house, one of the oldest standing in the region. As boatmen walked home up the Trace they turned it into a stand, a crude inn: corn mush, milk and a place on the porch for 25 cents. It grew into a cotton plantation worked by enslaved people, perhaps from 12 to 16 cabins. The Ferguson-Chamberlain family lived here for five generations; the NPS took it over in 1938. It is the only stand left on the parkway.',
  'The frame house on the hill above the information center, with framing of oak and sassafras and poplar clapboards; the Ferguson-Chamberlain cemetery, the cemetery of 43 enslaved people, the site of the kiln where enslaved workers made bricks for parts of the house, and a piece of the old Trace on the walking path. In September 2017 the NPS closed the house itself until it could be stabilized, leaving the grounds open; whether it has reopened was not checked.',
  'The last inn of the Natchez Trace.',
  TRACE_ACC+' Milepost 15.5, with an information center (rangers in open hours) and restrooms. NPS releases of 2017 gave hours of 9 a.m. to 4:30 p.m., at times four or six days a week and later daily for the grounds; current hours not checked.',
  [L('NPS: Mount Locust Historic House','https://www.nps.gov/places/mount-locust-historic-house.htm'),L('NPS news, September 2017: historic home temporarily closed','https://www.nps.gov/natr/learn/news/historic-home-temporarily-closed-along-the-natchez-trace-parkway.htm'),HM(87276,'Mount Locust'),NPSMOB],brick='?'),
N('elizabeth-female-academy','Elizabeth Female Academy ruins','Washington','ms','civic','ruins',31.57471,-91.29422,'exact','public','walk','','1818–1845',
  'The first school for women chartered in Mississippi (1819), founded by the Methodists in 1818 on land given by Elizabeth Roach. Its course ran to Latin, chemistry, botany and natural philosophy, and John James Audubon taught drawing here in 1822. It closed in 1845, after the capital moved from Natchez to Jackson and yellow fever struck the district. A fire in the late 1870s left it in ruins.',
  'Part of a brick wall is all that remains, reached by a paved, level path of about 450 feet from a small lot with interpretive signs.',
  'The first women\'s college in Mississippi, down to one wall.',
  TRACE_ACC+' NPS gives milepost 5.1; Wikipedia says 4.1. About ten parking spaces.',
  [W('Elizabeth Female Academy'),L('NPS: Elizabeth Female Academy, Milepost 5.1','https://www.nps.gov/places/elizabeth-female-academy.htm'),NPSMOB],brick='yes',conf='mixed',th=[31.57392,-91.29330],thn='Elizabeth Female Academy parking loop'),
N('jefferson-college-ms','Historic Jefferson College','Washington','ms','civic','standing',31.58111,-91.30000,'site','view','drive','','1811–1964',
  'Chartered in 1802 by the Mississippi Territory and opened in 1811, the first college in the territory; its first brick buildings were finished in 1820. It was for most of its life a preparatory and then a military boarding school, and closed in 1964. The Mississippi Department of Archives and History now runs it and is rehabilitating its eight buildings as an interpretive center and a field school for preservation trades; digging found the brick footings of the 1812 Methodist meeting house beside it.',
  'A campus of early brick buildings in the old territorial capital of Washington. MDAH says the campus is closed to visitors during the work; interior not checked.',
  'Mississippi\'s first college, being taught to mend itself.',
  'Owned by MDAH. Closed to visitors during rehabilitation (MDAH page, read November 2026): look from the public road in Washington and check the MDAH page before going.',
  [W('Jefferson College (Mississippi)'),L('MDAH: Historic Jefferson College','https://mdah.ms.gov/explore-mississippi/historic-jefferson-college')],brick='yes'),
# ---- Natchez and Church Hill ----
N('longwood-natchez','Longwood','Natchez','ms','civic','standing',31.53680,-91.40525,'exact','open','drive','','1859–1861',
  'An octagonal mansion designed by the Philadelphia architect Samuel Sloan in 1859 for the cotton planter Haller Nutt and built in part by enslaved people. Work stopped in 1861 when the Pennsylvania craftsmen left for the Union army; only nine rooms of the basement floor, of 32 planned, were ever finished, and the family lived in them. Nutt died in 1864. On July 4, 1867 more than 9,000 freed people held a picnic on the grounds. Given to the Pilgrimage Garden Club in 1968 on condition that it never be finished, it is the largest octagonal house in the country.',
  'The onion dome over an eight-sided shell; inside, the finished basement floor with original furnishings and, above it, the bare, unfinished upper floors, with the builders\' tools still there by the tour company\'s account.',
  'A mansion frozen the day its builders went to war.',
  'Pilgrimage Garden Club museum house at 140 Lower Woodville Road, open for tours all year (Natchez Pilgrimage Tours; tickets online, usable any day). Hours and fees not checked on the page.',
  [W('Longwood (Natchez, Mississippi)'),L('Natchez Pilgrimage Tours: year-round tours','https://natchezpilgrimage.com/year-round/')],brick='yes'),
N('christ-church-church-hill','Christ Church, Church Hill','Church Hill','ms','worship','standing',31.71500,-91.23806,'site','view','drive','','1857–1858',
  'Home of the first Episcopal congregation in Mississippi, which began in a log church under Adam Cloud, whom the Spanish had expelled for preaching. Its second church on this site (1826 by the Natchez Democrat, 1829 by Wikipedia) gave its bricks to the present Gothic Revival building of 1857–58 by J. Edward Smith. Union soldiers occupied it in 1864.',
  'Brick under stucco scored to look like stone, with lancet windows between buttresses and a rose window in the front. SAH Archipedia says the pews, chairs, marble font and pipe organ are original; a restoration finished in 2024 redid the floor, walls and all 54 pews and repaired the stained glass. The public can go in at services; other times not checked.',
  'Mississippi\'s oldest Episcopal congregation, in a church of recycled brick.',
  'An active Episcopal church on state highway 553 in Church Hill. Look from the road, or go at a service.',
  [W('Christ Church (Church Hill, Mississippi)'),L('SAH Archipedia: Christ Church, Church Hill','https://sah-archipedia.org/node/86728'),L('Natchez Democrat (2024): restoration at Christ Episcopal Church','https://www.natchezdemocrat.com/2024/09/20/major-restoration-work-at-christ-episcopal-church-to-be-revealed-sunday/')],brick='no',conf='mixed'),
]

WK='The coordinate is Wikipedia\'s.'
HMD='The coordinate is the HMdb marker\'s.'
PIN_NOTES={
 'grand-gulf-military-park':HMD+' (Grand Gulf Military Park marker, by the museum).',
 'fort-cobun-grand-gulf':HMD+' (Fort Cobun), in woods; neither the aerial nor the LiDAR picked out the parapet at this scale.',
 'sacred-heart-church-grand-gulf':HMD+' (Rodney Sacred Heart Roman Catholic Church).',
 'rodney-ms':WK,
 'rodney-presbyterian-church':HMD+' (Rodney Presbyterian Church, beside the church).',
 'oakland-memorial-chapel':HMD+' (Oakland Memorial Chapel).',
 'bethel-presbyterian-church-alcorn':HMD+' (Bethel Church).',
 'first-presbyterian-port-gibson':'The HMdb markers stand on the street; on the aerial the pin was moved 36 m east onto the large church building with tools/pix.py.',
 'temple-gemiluth-chessed':HMD+' (Temple Gemiluth Chassed).',
 'samuel-gibson-house':HMD+' It falls on a clump of trees beside US 61; the house is not clear under them on the aerial.',
 'shaifer-house':HMD+' (Field Surgery on the Porch); the house shows in a clearing about 20 m west of it on the aerial.',
 'rocky-springs-ms':'OpenStreetMap point for Rocky Springs Methodist Church (tools/nom.py).',
 'sunken-trace-ms':'OpenStreetMap point for the Sunken Trace (tools/nom.py).',
 'mount-locust-ms':'The HMdb marker, moved 11 m onto the house roof seen among trees on the aerial (tools/pix.py).',
 'elizabeth-female-academy':'OpenStreetMap ruins point (tools/nom.py), 28 m west of Wikipedia\'s; it falls in the trees beside a loop drive and the wall itself is hidden on the aerial and the LiDAR. The parking point is the loop at the end of the drive, picked off the aerial with tools/pix.py.',
 'jefferson-college-ms':WK,
 'longwood-natchez':'OpenStreetMap building for Longwood (tools/nom.py); Wikipedia\'s point fell on the lawn 60 m east, and the octagon is plain on the aerial at the new pin.',
 'christ-church-church-hill':WK+' It falls on highway 553; a long dark-roofed building about 70 m northwest may be the church but was not confirmed, so the pin stays on the road.',
}
