# November 19, 2026: a first scatter of places across Indiana, which had one place on the map (Rose Island).
# State taken with tools/choose.py --thinnest. Spread from Lake Michigan to the Ohio River on purpose.
# Sources read in this session: Wikipedia articles (tools/wiki_raw.py), the Indiana State Museum and Historic Sites
# "plan your visit" pages, Indiana DNR park pages and the DNR Brough's Folly brochure, the Grouseland, Indiana Landmarks,
# Michigan City Historical Society, Elkhart County Parks, Indiana Medical History Museum and Rotary Jail Museum pages,
# the NPS Bailly/Chellberg trail page, an HMdb marker and an Inside INdiana Business article. Hours are as those pages gave
# them in November 2026. Interiors were not visited by any source unless the entry says so.
from data_b import N
from data_ma import W
BATCH={'key':'in_gcvh','label':'Indiana: a first scatter, Lake Michigan to the Ohio','added':'2026-11-19 20:16'}

ISM='Indiana State Museum and Historic Sites'
def ISMP(site,slug):
    return [ISM+': '+site+', plan your visit','https://www.indianamuseum.org/historic-sites/%s/plan-your-visit/'%slug]

PLACES=[
N('corydon-old-capitol-in','Old Capitol (first Indiana State Capitol)','Corydon','in','civic','standing',38.21147,-86.126,'exact','open','walk','','1814–1816',
  'A two-storey Federal limestone building put up as the Harrison County Courthouse, which served as the capitol of the Indiana Territory and then as the first state capitol from 1816 to 1825, when the government moved to Indianapolis. Dennis Pennington, speaker of the territorial lower house, supervised its building. It is now part of the Corydon Capitol State Historic Site in the middle of the Corydon Historic District.',
  'The two-storey limestone capitol on its public square, with the Old Treasury Building, Governor Hendricks\' Headquarters, the Constitution Elm memorial and the Posey House nearby in the same district. Indoor visits are by timed guided tour. Interior details not checked.',
  'Indiana\'s statehood began in a county courthouse.',
  'Owned by the state and run by '+ISM+'. Its plan-your-visit page gives timed guided tours Wednesday to Sunday at 10 a.m., noon, 2 and 4 p.m. (and, for a summer 2026 offer, Wednesdays and Sundays only), with an admission fee; it asks visitors to call to confirm tour availability. Parking on the historic downtown square or at the Harrison County visitors bureau (same page).',
  [ISMP('Corydon Capitol','corydon-capitol-historic-site'),W('Corydon Historic District')],brick='no',
  hours='Guided tours Wednesday to Sunday 10 a.m., noon, 2 and 4 p.m.; call to confirm'),

N('indiana-territorial-capitol-vincennes','Indiana Territorial Capitol','Vincennes','in','civic','standing',38.68538,-87.52519,'exact','open','walk','','1800–1805',
  'A plain two-storey frame building that was the seat of government of the Indiana Territory from 1800 to 1813, before the capital moved to Corydon. It was built between 1800 and 1805 and moved to its present site in 1949. It stands in a row of buildings across from Vincennes University and is part of the Vincennes State Historic Sites.',
  'The two-storey frame capitol in the state historic site row. Indoor tours of the buildings need a ticket; interior details not checked.',
  '',
  'Run by '+ISM+'. Its page gives indoor tours Wednesday to Sunday 10 a.m. to 4 p.m. with admission, and free self-guided outdoor visits Wednesday to Sunday. Parking on Scott Street or in the "Historic Sites" spaces of the Vincennes University lot on First Street (same page).',
  [ISMP('Vincennes State Historic Sites','vincennes-state-historic-site'),W('Indiana Territorial Capitol')],brick='no',
  hours='Indoor tours Wednesday to Sunday 10 a.m. to 4 p.m.'),

N('grouseland-vincennes','Grouseland, William Henry Harrison\'s house','Vincennes','in','landmark','standing',38.68549,-87.52601,'site','open','walk','','1802–1804',
  'The two-storey Federal house William Henry Harrison built while he was the first governor of the Indiana Territory, finished in 1804 of bricks made near Vincennes; it is believed to have been the first brick building in the town and the territory. The Harrisons left in 1812. The Francis Vigo Chapter of the Daughters of the American Revolution raised money to save it from demolition (it had a limited deed by 1916), restored it and still owns it; the Grouseland Foundation runs it.',
  'Red brick on a limestone basement, with a high roof and dormers. Inside, the first floor has a parlor used as a council chamber, a dining room and a library at the rear; the DAR furnished it to Harrison\'s time with a few Harrison family possessions (Wikipedia).',
  'A frontier governor\'s brick mansion where treaties were talked over.',
  'Owned by the local DAR chapter and run by the Grouseland Foundation, whose page gives its hours as noon to 4 p.m. Eastern, Tuesday to Saturday. It stands at Park and Scott streets in the Vincennes Historic District, near the Territorial Capitol; parking not checked.',
  [['Grouseland: FAQs (hours)','https://grouseland.org/faqs'],W('Grouseland')],brick='yes',
  hours='Tuesday to Saturday noon to 4 p.m. Eastern'),

N('lanier-mansion-madison-in','Lanier Mansion','Madison','in','landmark','standing',38.73529,-85.38591,'exact','open','walk','','1840–1844',
  'The Greek Revival house the banker James F. D. Lanier had built by the Madison architect Francis Costigan, finished in 1844 for $25,000. Lanier left for New York after seven years. The state opened it as a house museum in the 1920s, and it is a National Historic Landmark (1994).',
  'A brick house painted yellow ochre on a raised blue limestone base, with a two-storey river-side portico of four 30-foot fluted wooden Corinthian columns behind iron railings. Inside: a 10-foot entrance hall, Ionic-columned doorways with egg-and-dart moulding, a library ceiling in gold leaf, red and blue, and a self-supporting staircase that winds up to the cupola. The gardens below the portico are recreated; the carriage house was rebuilt in 2003 on its old foundation (Wikipedia).',
  '',
  'Run by '+ISM+'. Its page says Wednesday to Sunday, 10 a.m. to 5 p.m.; all guided tours start at the visitor center just west of the house (entrance on Vine Street), and the grounds can be walked all day. Parking near the Lanier-Madison Visitor Center (same page).',
  [ISMP('Lanier Mansion','lanier-mansion-historic-site'),W('Lanier Mansion')],brick='no',
  hours='Wednesday to Sunday 10 a.m. to 5 p.m., guided tours from the visitor center; grounds all day'),

N('broughs-tunnel-clifty-falls','Brough\'s Tunnel (Brough\'s Folly), Clifty Falls State Park','Madison','in','rail','ruins',38.75888,-85.43018,'area','public','hike','','1852–1854',
  'A railroad tunnel left unfinished in Clifty Creek canyon. John Brough bought the Madison and Indianapolis Railroad in 1852 and set about 700 men to build a gentler line out of the Ohio valley up the canyon, with two tunnels, cutting limestone with gunpowder and hand drills. Debt and hard rock stopped the work, and the line was abandoned at a cost the DNR puts at about $300,000. Brough went on to be governor of Ohio in 1864.',
  'A 600-foot tunnel on Trail 5 driven through a shale band, more than 6 feet high at the south end and about 4.5 feet at the north, so no train could ever have used it. Retaining walls and limestone abutments for a trestle are along Trails 1, 3, 4 and 5; the second tunnel was dynamited shut. The DNR says the tunnel itself is closed because rock falls at both ends, and it is now winter habitat for bats.',
  'A railroad tunnel too low for a train.',
  'Clifty Falls State Park, Indiana DNR; OpenStreetMap maps a lot named Brough\'s Tunnel about 55 m from the pin. The DNR\'s Brough\'s Folly brochure puts the tunnel on Trail 5 and says it is CLOSED to visitors (falling rock; bat habitat): see it from the trail. Park entrance fee and hours not checked. The pin is the trail point mapped in OpenStreetMap as Brough\'s Tunnel.',
  [['Indiana DNR: Brough\'s Folly brochure','https://www.in.gov/dnr/state-parks/files/sp-CliftySP-BroughsFollyBrochure.pdf'],W('Clifty Falls State Park')],th=[38.75933,-85.42991],thn='Brough\'s Tunnel parking, Clifty Falls State Park',brick='no'),

N('duck-creek-aqueduct-metamora','Duck Creek Aqueduct, Whitewater Canal','Metamora','in','canal','standing',39.44616,-85.12998,'exact','public','walk','canal','1846',
  'A covered wooden aqueduct carrying the Whitewater Canal over Duck Creek at the east edge of Metamora, the only one of its kind left in the United States. The first aqueduct (1839–1843) washed out in a flood and this one was built in 1846; it was strengthened in 1868 and repaired in 1901. It is a National Historic Landmark (2014) in the Whitewater Canal State Historic Site.',
  'A single-span Burr truss about 90 feet long that looks like a covered bridge, with an oak trough holding 2 to 3 feet of water, valves and a spillway at the west end; the metal roof is 20th-century (Wikipedia). The site\'s gristmill nearby grinds at 11 a.m., 1:30 and 3 p.m. in season.',
  'A covered bridge that carries a canal instead of a road.',
  'Part of the Whitewater Canal State Historic Site, which '+ISM+' runs (its page; the federal land map does not hold it, and the owner of record was not checked). Its page says the grounds can be toured on your own all day; the site is Wednesday to Sunday 10 a.m. to 5 p.m. in season, and in winter closed except the last weekend in November and the first three weekends of December. Parking is opposite the Metamora Grist Mill (same page).',
  [ISMP('Whitewater Canal','whitewater-canal-historic-site'),W('Duck Creek Aqueduct')],brick='no',
  hours='Grounds all day; site Wednesday to Sunday 10 a.m. to 5 p.m. in season; winter weekends late November to December only'),

N('laughery-creek-bridge-in','Laughery Creek Bridge (the Triple Whipple)','Aurora','in','landmark','standing',39.02472,-84.88583,'site','view','walk','','1868',
  'An iron bridge of 1868 by the Wrought Iron Bridge Company over Laughery Creek on the Dearborn and Ohio county line, the only known triple-intersection Whipple truss. It closed to traffic in the 1970s and decayed until federal money and both counties restored it for people on foot.',
  'A single pin-connected through truss nearly 300 feet long on stone abutments, its members crossing three times; the concrete deck is not original (Wikipedia). The HMdb marker says it is rehabilitated for pedestrians.',
  'The only triple Whipple truss in the world.',
  'Closed to vehicles and rehabilitated for walkers (HMdb marker); Wikipedia says the two counties paid for the work, but who owns it now was not checked, so it is marked view. OpenStreetMap maps a small lot on Old State Road 56 about 130 m southeast; not checked on the ground.',
  [W('Laughery Creek Bridge'),['HMdb: Laughery Creek Bridge marker','https://www.hmdb.org/m.asp?m=66899']],conf='mixed',th=[39.02368,-84.88523],thn='Lot on Old State Road 56',brick='no'),

N('cannelton-cotton-mill','Cannelton Cotton Mill','Cannelton','in','industry','standing',37.91146,-86.7452,'exact','view','drive','','1849–1851',
  'A sandstone cotton mill built 1849 to 1851 to the design of the Rhode Island architect Thomas Alexander Tefft, once the largest industrial building west of the Alleghenies. Hamilton Smith of Louisville meant it to rival Lowell with steam power from local coal. It employed about 400 workers at first, mostly women and girls. A National Historic Landmark since 1991, it now holds homes.',
  'The long sandstone mill on Adams Street. It is lived in; interior not checked.',
  'A Lowell-style mill on the Ohio.',
  'Residences (Wikipedia): see it from the street.',
  [W('Cannelton Cotton Mill')],brick='no'),

N('hindostan-falls-mill-rock','Hindostan Falls: the lost town and its mill holes','Shoals','in','town','traces',38.62412,-86.8538,'area','public','walk','','1816–1828',
  'A town founded in 1816 at the falls of the East Fork of the White River on the stage road from New Albany to Vincennes. By 1820 about 1,200 people lived there, many on houseboats, and it was the county seat; an epidemic of yellow fever or cholera that year emptied it, and by 1824 less than half remained. The county seat moved in 1828 and the site became farmland.',
  'No buildings. Square holes drilled in a large flat rock along the river held up a mill owned by Frederick Shulz; a few pioneer cemeteries and a restored church are nearby. A marker on State Road 550 stands about half a mile north of the town site (Wikipedia). The holes were not located on the aerial.',
  'A frontier boomtown that a fever wiped out.',
  'A state public fishing area (Wikipedia; the DNR lists Hindostan Falls Public Fishing Area ramps). The pin is just north of ramp 1 (38.6239, -86.8538), 3851 Falls Lane, Shoals, as How\'s Your River gives it from the DNR list. Hours not checked. The river is a whitewater run at high water.',
  [W('Hindostan Falls, Indiana'),['How\'s Your River: Hindostan Falls Public Fishing Area ramp 1','https://www.howsyourriver.com/access_sites/hindostan-falls-public-fishing-area-ramp-1']],brick='no'),

N('spring-mill-gristmill-in','Spring Mill gristmill and Pioneer Village','Mitchell','in','industry','standing',38.7352,-86.4267,'area','open','walk','','1817',
  'An industrial village grew up in the early 1800s round cave springs whose water never froze, driving gristmills, a wool mill, a sawmill and a distillery. Its centrepiece is a three-storey limestone gristmill of 1817 that still grinds cornmeal. The village was restored in Spring Mill State Park, founded in 1927.',
  'The stone mill fed by a race from the cave spring, with about 20 historic buildings in the Pioneer Village; the DNR\'s mill page tells of a flume replacement during which the mill was shut while the village stayed open. Hamer Cemetery is south of the village (Wikipedia).',
  '',
  'Spring Mill State Park, Indiana DNR. The park page gives the Pioneer Village 9 a.m. to 4:30 p.m., weekends from March 15 to April 14 (weather allowing) and daily April 15 to the last full weekend of October. Park entrance fee not checked. Pin is at the end of the mapped mill race; the mill itself was not seen on the aerial.',
  [['Indiana DNR: Spring Mill State Park','https://www.in.gov/dnr/state-parks/parks-lakes/spring-mill-state-park/'],['Indiana DNR: Spring Mill grist mill FAQ','https://WWW.IN.GOV/dnr/state-parks/files/sp-spring-mill-grist-mill-faq.pdf'],W('Spring Mill State Park')],brick='no',
  hours='9 a.m. to 4:30 p.m.: weekends March 15 to April 14, daily April 15 to last full weekend of October'),

N('west-baden-springs-hotel','West Baden Springs Hotel','West Baden Springs','in','hotel','standing',38.56722,-86.61806,'site','open','walk','hotels','1902',
  'A spa hotel whose 200-foot atrium dome was the largest in the world from 1902 to 1913. It closed in June 1932 after the crash, became a Jesuit seminary until 1964 and then a business school campus until 1983, and was shut as unsafe in 1989. An affiliate of the Historic Landmarks Foundation of Indiana bought it in 1996 with an anonymous donor\'s money; the Cook family stabilised and restored it for almost $100 million, and it reopened as a hotel on June 23, 2007.',
  'The domed atrium with its great fireplace, marble wainscotting from the 1920s remodel and brick columns wrapped in canvas painted to look like marble; the Jesuits made the lobby a chapel with stained glass. The sunken garden was recreated. The Jesuit cemetery is nearby (Wikipedia).',
  'From grand hotel to seminary to ruin and back.',
  'A working hotel, part of French Lick Resort. Indiana Landmarks runs tours: 2 and 4 p.m., Wednesday to Saturday from January to May and Tuesday to Saturday from June to December, with tickets, plus twilight and behind-the-scenes tours on some days (its tours page). Parking not checked.',
  [['Indiana Landmarks: French Lick and West Baden Springs hotel tours','https://www.indianalandmarks.org/?p=1257'],W('West Baden Springs Hotel')],brick='?',
  hours='Indiana Landmarks tours 2 and 4 p.m.: Wednesday to Saturday January to May, Tuesday to Saturday June to December'),

N('mansfield-roller-mill','Mansfield Roller Mill','Mansfield','in','industry','standing',39.67702,-87.10151,'exact','open','drive','','1880',
  'A mill on Big Raccoon Creek begun in 1821 as a log mill on sandstone bedrock by a ford. Jacob Rohm bought it in 1875, tore it down in 1880 and rebuilt it, put in roller stands in place of millstones in 1884 and two water turbines in 1886 and 1889. The state restored it from the 1990s to 2005, and Raccoon State Recreation Area now runs it as a state historic site.',
  'Much of the original water-powered equipment still works, and the 1886 Rodney Hunt turbine drives demonstrations at festivals and events (Wikipedia). Interior not checked.',
  '',
  'Owned by Indiana DNR and run from Raccoon State Recreation Area. The DNR\'s mill page answered 404, so hours were not checked; Wikipedia says demonstrations are given for festivals and special events. It stands at Mansfield Road and Big Raccoon Creek, southeast of Rockville.',
  [W('Mansfield Roller Mill')],brick='?',hours='?'),

N('rotary-jail-crawfordsville','Rotary Jail (Montgomery County Jail and Sheriff\'s Residence)','Crawfordsville','in','civic','standing',40.04389,-86.90178,'exact','open','walk','','1882',
  'The county jail and sheriff\'s house of 1882, whose cell block is a rotary jail: a turning drum of cells, the only one of its type in Indiana and one of two left in the United States. It is now a local history and prison museum, a National Historic Landmark since 2023.',
  'Red brick and limestone in a mix of Italianate, Gothic Revival and Romanesque Revival (Wikipedia). Interior not checked.',
  'A jail that turned its prisoners round.',
  'Run as the Rotary Jail Museum. Its page gives the 2026 season as Wednesday to Saturday, 10 a.m. to 3 p.m. in spring and autumn and to 5 p.m. from June 3 to September 5, last entry an hour before closing, closed holiday weeks and from December 17 for the winter; admission charged. Parking not checked.',
  [['Rotary Jail Museum','https://rotaryjailmuseum.org'],W('Montgomery County Jail and Sheriff\'s Residence')],brick='yes',
  hours='March to mid-December, Wednesday to Saturday 10 a.m. to 3 p.m. (to 5 p.m. June 3 to September 5)'),

N('indiana-medical-history-museum','Indiana Medical History Museum (Old Pathology Building)','Indianapolis','in','inst','standing',39.77117,-86.21473,'exact','open','walk','','1895',
  'The pathology building of 1895 on the grounds of the Central Indiana Hospital for the Insane (later Central State Hospital), the oldest surviving pathology laboratory in the United States. Two medical colleges taught neurology and psychiatry in it from 1900 to 1908.',
  'A two-storey brick building with a 150-seat teaching amphitheater, autopsy room, anatomical museum, library, laboratories and a photography room (Wikipedia). Seen by guided tour.',
  '',
  'The museum\'s page gives Wednesday to Saturday 10 a.m. to 4 p.m., with guided tours on the hour from 10 a.m. to 3 p.m., at 3270 Kirkbride Way; it says the old entrance is closed and names two ways onto the former hospital grounds. Parking not checked.',
  [['Indiana Medical History Museum: visit','https://www.imhm.org/visit'],W('Indiana Medical History Museum')],brick='?',
  hours='Wednesday to Saturday 10 a.m. to 4 p.m., guided tours on the hour 10 a.m. to 3 p.m.'),

N('levi-coffin-house-fountain-city','Levi and Catharine Coffin House','Fountain City','in','landmark','standing',39.95782,-84.91857,'site','open','walk','','c. 1838–1839',
  'The Federal brick house of the Quaker abolitionists Levi and Catharine Coffin, called the "Grand Central Station" of the Underground Railroad because three escape routes met there; Wikipedia says they may have helped as many as 2,000 people escape while they lived in Indiana (1826 to 1847). It was apartments after 1911, was restored in the 1960s and opened in 1970; it was the first Indiana property on the National Register (1966).',
  'A two-storey, eight-room house painted red, with original fireplaces, doors, floors and some woodwork restored, built-in bookcases original to the south room, some original window panes, and changes inside that could have hidden people (Wikipedia). Seen only by guided tour.',
  'The house where escape routes met.',
  'Run by '+ISM+'. Its page says a guided tour is needed to see the house: Wednesday to Sunday at 10:30 a.m., 1:30 and 3:30 p.m., admission charged. Parking not checked.',
  [ISMP('Levi and Catharine Coffin','levi-and-catharine-coffin-state-historic-site'),W('Levi Coffin House')],brick='no',
  hours='Guided tours Wednesday to Sunday 10:30 a.m., 1:30 and 3:30 p.m.'),

N('huddleston-farmhouse-cambridge-city','Huddleston Farmhouse','Cambridge City','in','hotel','standing',39.81217,-85.18725,'site','view','drive','','1841',
  'A three-storey brick farmhouse built in 1841 by the Huddleston family, who lodged and fed travellers on the National Road. Indiana Landmarks restored it as a museum and office, then sold the farmstead to a family who meant to live there and farm it, saying they hoped one day to make it an educational site (Inside INdiana Business).',
  'The brick house (Wikipedia says 125,000 bricks), with a barn, carriage shed and smokehouse. Private home; interior not checked.',
  '',
  'Privately owned since Indiana Landmarks sold it (Inside INdiana Business). Indiana Landmarks\' older page said tours were by appointment; that is out of date. See it from the National Road; the pin is the Wikipedia coordinate.',
  [W('Huddleston Farmhouse'),['Inside INdiana Business: Historic Huddleston farmstead acquired','https://www.insideindianabusiness.com/articles/historic-huddleston-farmstead-acquired']],brick='?'),

N('old-michigan-city-light','Old Michigan City Lighthouse','Michigan City','in','light','standing',41.72268,-86.90602,'exact','open','walk','','1858',
  'The harbor light of 1858, which replaced an 1837 light and was the second at the site. In 1904 its lantern, lens and light were moved to the new light at the end of the extended pier and the old station was remodelled. Seven keepers and fourteen assistants served from 1837 to 1940. It is now the Old Lighthouse Museum in Washington Park.',
  'A fourth-order Fresnel lens is shown inside (Wikipedia). Interior not otherwise checked.',
  '',
  'Run by the Michigan City Historical Society, whose page gives the 2027 season as April 1 to October 31, Wednesday to Sunday 1 to 4 p.m. Central, with off-season tours by appointment. Free museum parking, not for beach parking (same page).',
  [['Michigan City Historical Society: visit','https://mchistorical.org/visit'],W('Old Michigan City Light')],brick='?',
  hours='April to October, Wednesday to Sunday 1 to 4 p.m. Central'),

N('bailly-homestead-porter','Joseph Bailly Homestead','Porter','in','landmark','standing',41.62306,-87.09417,'site','public','walk','','1834',
  'The homestead of Joseph Bailly, a fur trader and one of the first permanent white settlers of northwest Indiana, begun in 1834; he came to the lake shore in 1822. It stayed in the family until 1917 and the National Park Service bought it in 1971. A National Historic Landmark (1962) in Indiana Dunes National Park.',
  'A 2.5-storey house of hewn cedar and oak logs under weatherboards; a two-storey log storehouse from an older trading building; a kitchen rebuilt as a chapel by 1874; a brick house southwest of the main house; and the family cemetery three-quarters of a mile north on a sand ridge (Wikipedia). Interior not checked.',
  'One of the last traces of the Calumet fur trade.',
  'Indiana Dunes National Park. The NPS trail page starts the walk at the Bailly/Chellberg parking lot (paved, with year-round restrooms) and gives the area\'s hours as 6 a.m. to 11 p.m. daily. Whether the house opens inside was not checked.',
  [['NPS: Bailly Homestead, Chellberg Farm and trails','https://www.nps.gov/places/bailly-homestead-chellberg-farm-little-calumet-river-mnoke-prairie-trails.htm'],W('Joseph Bailly Homestead')],brick='?',
  hours='Grounds 6 a.m. to 11 p.m. daily'),

N('bonneyville-mill-in','Bonneyville Mill','Bristol','in','industry','standing',41.71931,-85.76512,'site','open','drive','','1832',
  'A gristmill of 1832 in York Township, a heavy timber frame on a stone foundation about 40 feet square with shed additions. It went to electric power in 1919, was restored in the 1970s after its last private owner, and is now in an Elkhart County park, where it grinds stone-ground flour in season.',
  'The frame mill on its stone foundation; flour is sold at the mill in season (Elkhart County Parks). Interior not checked.',
  '',
  'Elkhart County Parks. Its page gives the mill as open April 14 to November 15, Tuesday to Sunday 10 a.m. to 5 p.m., and the park open daily from 9 a.m. (closing time by season).',
  [['Elkhart County Parks: Bonneyville Mill','https://elkhartcountyparks.org/parks/bonneyville-mill'],W('Bonneyville Mill')],brick='no',
  hours='Mill April 14 to November 15, Tuesday to Sunday 10 a.m. to 5 p.m.'),
]

PIN_NOTES={
 'corydon-old-capitol-in':'OpenStreetMap building point for Corydon Capitol State Historic Site (nom.py).',
 'indiana-territorial-capitol-vincennes':'OpenStreetMap building mapped as Indiana Territorial Capitol (nom.py).',
 'grouseland-vincennes':'Wikipedia coordinate.',
 'lanier-mansion-madison-in':'OpenStreetMap building point for Lanier Mansion (nom.py).',
 'broughs-tunnel-clifty-falls':'OpenStreetMap footway named Brough\'s Tunnel (nom.py); the tunnel is under trees.',
 'duck-creek-aqueduct-metamora':'OpenStreetMap bridge feature Duck Creek Aqueduct (nom.py).',
 'laughery-creek-bridge-in':'Wikipedia coordinate.',
 'cannelton-cotton-mill':'OpenStreetMap building point for Cannelton Cotton Mill (nom.py).',
 'hindostan-falls-mill-rock':'Moved 25 m north off the water (pix.py) from the DNR fishing-area ramp 1 as How\'s Your River lists it; the mill holes are along the river nearby and were not located.',
 'spring-mill-gristmill-in':'Near the lower end of the OpenStreetMap mill race in Spring Mill State Park (osmnear.py); the mill building was not pinned exactly.',
 'west-baden-springs-hotel':'Wikipedia coordinate.',
 'mansfield-roller-mill':'OpenStreetMap watermill point (nom.py).',
 'rotary-jail-crawfordsville':'OpenStreetMap museum point (nom.py).',
 'indiana-medical-history-museum':'OpenStreetMap museum point (nom.py).',
 'levi-coffin-house-fountain-city':'OpenStreetMap building mapped as Levi Coffin House (nom.py); the aerial shows trees over it, so precision is site.',
 'huddleston-farmhouse-cambridge-city':'Wikipedia coordinate.',
 'old-michigan-city-light':'OpenStreetMap museum point (nom.py).',
 'bailly-homestead-porter':'Wikipedia coordinate.',
 'bonneyville-mill-in':'Wikipedia coordinate fell on the road bridge; moved 36 m west-southwest onto the mill building seen on the aerial (pix.py).',
}
