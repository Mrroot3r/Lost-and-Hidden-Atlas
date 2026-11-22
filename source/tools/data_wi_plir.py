# November 22, 2026: a first scatter of places across Wisconsin beyond the lead region (which wi_axaz covered): the
# Lake Superior shore and the Gogebic iron range in the north, the Mississippi and St. Croix on the west, Portage on the
# Fox-Wisconsin portage in the middle, the Fox River at Kaukauna, the Door peninsula, and Ozaukee, Sheboygan and Milwaukee
# counties in the east. Region wi drawn by choose.py --thinnest (Wisconsin had 21 places).
# Facts come only from sources opened in this session: Wikipedia read as raw text (tools/wiki_raw.py, including the
# Register list rows for each county), the Plummer Mine Register form (NPGallery), HMdb, and the pages of whoever runs
# each place: the Wisconsin Historical Society (Villa Louis, and its 2026 Wade House season release as carried by Urban
# Milwaukee), the National Park Service, the Door County Maritime Museum, Door County, the Door County Historical Society,
# the Wisconsin DNR, Marquette University, the City of Kaukauna, the Historic Indian Agency House, the Fort Winnebago
# Surgeons Quarters, the Mabel Tainter Center for the Arts, the Hudson octagon house museum, the La Crosse County
# Historical Society, Hurley's chamber page for the Plummer headframe friends, Travel Wisconsin and TMJ4.
# Most of these places are seasonal and were closed for the winter when read; the hours given are the season's.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]

BATCH={'key':'wi_plir','label':'Wisconsin: a first scatter from Lake Superior to Lake Michigan','added':'2026-11-22 01:27'}

IR_NR=W('National Register of Historic Places listings in Iron County, Wisconsin')
BA_NR=W('National Register of Historic Places listings in Bayfield County, Wisconsin')
DG_NR=W('National Register of Historic Places listings in Douglas County, Wisconsin')
DN_NR=W('National Register of Historic Places listings in Dunn County, Wisconsin')
CO_NR=W('National Register of Historic Places listings in Columbia County, Wisconsin')
OZ_NR=W('National Register of Historic Places listings in Ozaukee County, Wisconsin')
DO_NR=W('National Register of Historic Places listings in Door County, Wisconsin')
SH_NR=W('National Register of Historic Places listings in Sheboygan County, Wisconsin')
SC_NR=W('National Register of Historic Places listings in St. Croix County, Wisconsin')
OU_NR=W('National Register of Historic Places listings in Outagamie County, Wisconsin')
LC_NR=W('National Register of Historic Places listings in La Crosse County, Wisconsin')

PLACES=[
# ---- The north: the iron range and Lake Superior ----
N('plummer-mine-headframe-pence','Plummer Mine Headframe','Pence','wi','industry','standing',46.40755,-90.29269,'exact','public','walk','','1904–1924',
  'The steel headframe over the shaft of the Plummer iron mine on the Gogebic Range, worked from 1904 to 1924. Miners were lowered from it into a shaft that follows the ore vein down at an angle to 2,367 feet. It is called the last headframe still standing in Wisconsin.',
  'A riveted steel truss about 80 feet tall on a concrete base, triangular in profile, topped by two big sheave wheels in a boxy frame (the Register form). Remnant tailing piles are noted at the site. It stands in the Plummer Mine Headframe Interpretive Park, with markers on the Penokee Iron Range Trail.',
  'The last headframe in Wisconsin.',
  'Plummer Mine Headframe Interpretive Park, on Plummer Road about a quarter mile south of State Highway 77 (HMdb). An interpretive park dedicated to the iron miners (the HMdb marker). A friends group raises money for its restoration (the Hurley area chamber page); who owns the park was not checked, and no hours were found. No parking lot is mapped; park along Plummer Road where the aerial shows room.',
  [W('Plummer Mine Headframe'),L('Register nomination form (NPGallery)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/97001141_text'),L('HMdb: Penokee Iron Range Trail, Plummer Mine','https://www.hmdb.org/m.asp?m=45418'),L('Hurley area chamber: Friends of the Plumer Mine Headframe','https://www.hurleywi.com/?p=8236'),IR_NR],brick='no'),
N('hokenson-fishery-little-sand-bay','Hokenson Brothers Fishery','Little Sand Bay','wi','industry','standing',46.9467,-90.8916,'site','public','walk','','1927',
  'Leo, Roy and Eskel Hokenson ran a family commercial fishery at Little Sand Bay on Lake Superior for more than 30 years from 1927. Their dock was built on crib piers in 1927, and Roy\'s house in 1940. It is now kept by the Apostle Islands National Lakeshore.',
  'You can walk the grounds and see the twine shed (where nets were made, mended and stored, and which also served as workshop and smithy), the pile driver, the dock and the herring shed (the Park Service pages). The restored fish tug Twilite and other outdoor exhibits are beside the seasonal visitor centre. Interior not checked.',
  'Three brothers, one dock, thirty years of Lake Superior fish.',
  'Apostle Islands National Lakeshore (National Park Service), Little Sand Bay Road, Town of Russell. The visitor centre is staffed in season only; opening days and hours not checked. Parking at the Little Sand Bay lots.',
  [L('NPS: Historic Hokenson Brothers Fishery','https://www.nps.gov/articles/000/historic-hokenson-brothers-fishery-apis.htm'),L('NPS: Little Sand Bay','https://www.nps.gov/places/little-sand-bay.htm'),W('Hokenson Fishing Dock'),BA_NR],
  th=[46.94573,-90.88983],thn='Little Sand Bay lot',brick='?'),
N('ss-meteor-superior','SS Meteor, the last whaleback','Superior','wi','industry','standing',46.72274,-92.06356,'exact','open','walk','','1896',
  'Built in Superior in 1896 as the Frank Rockefeller, one of 44 whalebacks, a cigar-shaped freighter design of Captain Alexander McDougall meant to carry the most cargo on the least draft. She hauled ore, coal and grain, was later an oil tanker as the Meteor, and sailed until 1969. As the last whaleback left anywhere she was brought back to Superior in 1971 and berthed on Barkers Island as a museum ship.',
  'The whole ship can be toured from the pilot house to the cargo holds, with exhibits on the main deck (Travel Wisconsin). Wikipedia says the hull was rusting and the interiors needed repair around 2000, and that by 2016 restoration had brought much of the ship back to good condition.',
  'The only whaleback left in the world.',
  'Superior Public Museums (Wikipedia), 200 Marina Drive on Barkers Island. Seasonal hours: the museum\'s own page did not open in this session, so days and times were not checked. Parking on North Marina Drive.',
  [W('SS Meteor (1896)'),L('Travel Wisconsin: SS Meteor Whaleback Ship','https://www.travelwisconsin.com/things-to-do/culture-arts/museums-history/ss-meteor-whaleback-ship'),DG_NR],
  th=[46.72149,-92.06520],thn='North Marina Drive lot',brick='no',hours='?'),
# ---- The west: Menomonie, Hudson, La Crosse, Prairie du Chien ----
N('mabel-tainter-menomonie','Mabel Tainter Memorial Building','Menomonie','wi','civic','standing',44.87679,-91.92814,'exact','open','walk','','1889',
  'A theatre, library and meeting hall that the lumberman Andrew Tainter and his wife built in 1889 in memory of their daughter Mabel, who died in 1886 at 19. Designed in Richardsonian Romanesque in the Minneapolis office of L. S. Buffington (Wikipedia names Harvey Ellis or Edgar Joraleman), it opened its library in 1891. A nonprofit arts centre owns and runs it.',
  'Dunnville sandstone outside. Inside, hand-stencilled walls and ceilings, a marble staircase, stained and leaded glass, carved white-pine arches, walnut and oak woodwork, brass fixtures, and the original Steere and Turner tracker organ of 1,597 pipes, once water-powered and now electric. The 269-seat theatre is shown on guided tours.',
  'A lumber baron\'s memorial to his daughter, organ and all.',
  'Mabel Tainter Center for the Arts, 205 Main Street East. Guided historic tours Friday and Saturday, noon to 3 p.m., last tour 2:30, no reservation; tours can be cancelled for shows and private events (its tours page). Street parking downtown.',
  [W('Mabel Tainter Memorial Building'),L('Mabel Tainter: Visits and tours','https://mabeltainter.org/visits-tours'),DN_NR],brick='no',hours='Guided tours Friday and Saturday, noon to 3 p.m. (last tour 2:30); cancelled on some show days'),
N('octagon-house-hudson','Octagon House (John S. Moffat House)','Hudson','wi','landmark','standing',44.98066,-92.75521,'exact','open','walk','','1854–1855',
  'An eight-sided house built by John Moffat, a land-office clerk and later a county judge, who came to Hudson from Ithaca, New York with his wife Nancy. The Register list gives 1854 and Wikipedia 1855. It was built Greek Revival and later restyled Italianate. A local historical society bought it in 1964 and shows it as a house museum.',
  'Stucco-walled octagon furnished in mid-1800s style; the museum page speaks of the Moffat-Hughes family\'s things and decorations at Christmas. A second museum building on the grounds holds Hudson-area tools, furniture and railroad items.',
  'An octagon on the St. Croix.',
  'Octagon House Museum, 1004 Third Street. Wikipedia names the owner as the Hudson Area History Connection; the museum\'s own page is headed St. Croix County Historical Society. Its tours page gives "Saturday and Sunday, 11 a.m. to 4 p.m." for the house and "Friday to Sunday, 11 to 4, May through October" for the second building, plus Christmas tours the first three weekends of December. Admission charged. Street parking.',
  [W('John S. Moffat House'),L('Octagon House Museum: tours','https://hudsonoctagonhouse.org/tours-experiences'),SC_NR],conf='mixed',brick='no',hours='Saturday and Sunday, 11 a.m. to 4 p.m. (the page also gives Friday to Sunday, May to October); Christmas tours first three December weekends'),
N('hixon-house-la-crosse','Hixon House','La Crosse','wi','landmark','standing',43.81585,-91.24715,'exact','open','walk','','1859',
  'The home of Gideon Hixon, a lumberman who later founded and led the La Crosse National Bank and sat in the state legislature. Begun in 1859 and added to in 1870 and the early 1880s. The La Crosse County Historical Society owns it and restored it from 2004, reopening it in 2005.',
  'A two-storey clapboard Italianate house with wide eaves and carved brackets; the plain outside hides a richly furnished interior full of the family\'s things from their travels. Original floor and wall coverings were cleaned or copied in the restoration, and Mrs. Hixon\'s "Turkish Nook" survives (the society\'s page).',
  'A lumberman\'s house with its Turkish Nook intact.',
  'La Crosse County Historical Society, 429 7th Street North. Closed for the season when read (November 2026); holiday tours December 4 (4:30 to 6:30 p.m.), 5 (11 a.m. to 3 p.m.) and 6 (noon to 4 p.m.); summer hours were not on the page. Street parking.',
  [W('Gideon C. Hixon House'),L('La Crosse County Historical Society: Hixon House','https://www.lchshistory.org/hixon-house'),LC_NR],brick='no',hours='Seasonal; closed November 2026, holiday tours December 4 to 6 (summer hours not given)'),
N('villa-louis-prairie-du-chien','Villa Louis','Prairie du Chien','wi','landmark','standing',43.05637,-91.1585,'exact','open','walk','','1871',
  'The Dousman family estate on St. Feriole Island by the Mississippi. The ground holds a mound later used by Fort Shelby, built by the Americans in 1814 and taken by the British that year in the only War of 1812 battle in Wisconsin, and then by Fort Crawford. The fur trader Hercules Dousman built a brick house on the mound in 1843; his son Louis built the present Italianate mansion, designed by E. Townsend Mix, in 1871. Louis\'s daughters began restoring it in the 1930s and gave it to the city; the Wisconsin Historical Society runs it.',
  'The mansion is restored to 1893–98 from old photographs, with many of the family\'s own furnishings. The 25-acre site has more than a dozen historic buildings, including a fur-trade warehouse that is now a museum, the foundations of Fort Crawford and the 1812 battlefield on the lawn (the society\'s site). Shown on guided tours.',
  'A Victorian mansion on a mound, a fort and a battlefield.',
  'Wisconsin Historical Society, 521 North Villa Louis Road. The 2026 season had ended when read, and the site reopens for general admission in May 2027; the 2025 season ran from May 21 into November with tours (the society\'s release). Days and times not checked. Tickets at the visitor centre. Parking off North Villa Louis Road.',
  [W('Villa Louis'),L('Wisconsin Historical Society: Villa Louis','https://villalouis.wisconsinhistory.org/'),L('Wisconsin Historical Society: Villa Louis 2025 season','https://wisconsinhistory.org/Records/Article/CS17353')],
  th=[43.05733,-91.15749],thn='North Villa Louis Road lot',brick='?',hours='Seasonal, May to about November; reopens May 2027 (days and times not checked)'),
# ---- Portage: the Fox-Wisconsin portage ----
N('indian-agency-house-portage','Historic Indian Agency House','Portage','wi','landmark','standing',43.559167,-89.437222,'site','open','walk','','1832',
  'A Federal-style house built in 1832 for John Kinzie, the government\'s Indian subagent to the Ho-Chunk (Winnebago), and his wife Juliette, beside Fort Winnebago at the portage between the Fox and Wisconsin rivers. Wikipedia calls it the only known Indian agency still on its original site. The Colonial Dames of America in Wisconsin have run it as a museum since 1932.',
  'The 1832 house, shown by docent-led tours of about an hour; begin at the visitor centre by the lot (its tours page). What original fabric survives inside is not described in the sources read (interior not checked).',
  'Where the Kinzies kept the agency at the portage.',
  'National Society of the Colonial Dames of America in Wisconsin, 1490 Agency House Road, off State Highway 33 by the Portage Canal. May 15 to October 15: Wednesday to Saturday 10 a.m. to 4 p.m., Sunday noon to 5; guided tours free, donations welcome; free parking (its tours page).',
  [W('Fort Winnebago'),L('Historic Indian Agency House: tours','https://agencyhouse.org/tours'),CO_NR],
  th=[43.55955,-89.43688],thn='Agency House Road lot',brick='no',hours='May 15 to October 15: Wednesday to Saturday 10 a.m. to 4 p.m., Sunday noon to 5 p.m.'),
N('fort-winnebago-surgeons-quarters','Fort Winnebago Surgeons Quarters','Portage','wi','fort','standing',43.55428,-89.43327,'site','open','walk','','1816–1828',
  'A log house that a fur trader built at the portage and sold to the army, which used it as the home of Fort Winnebago\'s surgeons; it is the only building of the fort (1828–1845) left. The dates differ: its own site says built between 1816 and 1819 and sold to the army in 1828, Wikipedia says built in 1824 by Francois Le Roi and Therese L\'Ecuyer, and the Register list says between 1818 and 1828.',
  'Hand-hewn log house, called one of the oldest French colonial log homes in Wisconsin still on its first foundation, furnished with early 1800s things, medical tools among them. The Garrison School, a one-room school used until 1960, was moved beside it.',
  'The last building of Fort Winnebago.',
  'Wisconsin Society Daughters of the American Revolution, W1824 State Highway 33. Walk-in guided tours May to October; closed for the season when read and reopening May 2027 (its home page). Days and times not checked: the visit page answered 404. Parking by the house.',
  [W('Fort Winnebago'),L('Fort Winnebago Surgeons Quarters','https://www.fortwinnebagosurgeonsquarters.org/'),CO_NR],conf='mixed',
  th=[43.55497,-89.43381],thn='State Highway 33 lot',brick='no',hours='May to October, guided tours (days and times not checked)'),
# ---- The Fox River ----
N('grignon-mansion-kaukauna','Charles A. Grignon Mansion','Kaukauna','wi','landmark','standing',44.28568,-88.25304,'site','open','walk','','1836–1837',
  'A Federal and Greek Revival house that Charles Grignon built as a wedding gift for his wife Mary Elizabeth Meade, known to travellers as "the Mansion in the Woods". The Register list gives 1836 and Wikipedia and the city 1837. It served as inn, church, trading post and Indian meeting place, on ground by the Fox River that held a trading post from as early as 1760 (the city\'s page).',
  'Restored to 1837–62, when Charles lived there, and shown on guided tours. Interior not checked.',
  'The mansion in the woods by the Fox.',
  'City of Kaukauna, 1313 Augustine Street, with the Friends of the Grignon Mansion. Open on set weekends for guided tours, 11 a.m. to 3 p.m. (July 25 and 26, August 9, 22 and 23, September 19 in 2026), Christmas tours in December, private tours by arrangement; admission charged (the city\'s page). Parking in Grignon Park.',
  [W('Charles A. Grignon House'),L('City of Kaukauna: Grignon Mansion','https://kaukauna.gov/grignon-mansion/'),OU_NR],
  th=[44.28512,-88.25522],thn='Augustine Street lot, Grignon Park',brick='no',hours='Set summer weekends, 11 a.m. to 3 p.m.; December Christmas tours; dates on the city page'),
# ---- Door County ----
N('cana-island-lighthouse','Cana Island Lighthouse','Baileys Harbor','wi','light','standing',45.08819,-87.04792,'exact','open','walk','','1869–1870',
  'Built in 1869 and lit in 1870 to replace the Baileys Harbor light, and still a working aid to navigation. The tower and keeper\'s house were of cream city brick; the tower\'s brick wore so badly that it was sheathed in steel in 1902. The light used lard, then kerosene, acetylene and from 1945 electricity. A storm on August 9, 2025 felled about 30 percent of the island\'s trees.',
  'The steel-clad tower, which can be climbed in season, with its third-order Fresnel lens, and the keeper\'s house, privy and grounds (Door County Maritime Museum). Reached by a short walk across a causeway.',
  'A brick tower in a steel coat.',
  'Cana Island Lighthouse County Park, owned by Door County and run with the Door County Maritime Museum. The island is open from half an hour before sunrise to half an hour after sunset; the lighthouse and tower May 1 to October 31, 10 a.m. to 5 p.m., last climb 4:30 (the museum\'s hours page); a fee for the island and another for the tower (the county page). Parking at the Cana Island lot on East Cana Island Road.',
  [W('Cana Island Light'),L('Door County: Cana Island Lighthouse','https://co.door.wi.gov/556/Cana-Island-Lighthouse'),L('Door County Maritime Museum: hours','https://dcmm.org/explore/hours-admissions/'),DO_NR],
  th=[45.09091,-87.05201],thn='Cana Island Lighthouse parking',brick='no',hours='May 1 to October 31: 10 a.m. to 5 p.m. (last tower climb 4:30); island sunrise to sunset'),
N('eagle-bluff-lighthouse','Eagle Bluff Lighthouse','Fish Creek','wi','light','standing',45.16868,-87.23662,'exact','open','walk','','1868',
  'A brick light station of 1868 on a 33-foot bluff over the Strawberry Channel, automated in 1926. The Door County Historical Society restored it from 1960 and opened it in 1963 or 1964 (Wikipedia gives both). It is furnished to the time of the Duclon family, keepers from 1883 to 1918.',
  'Square 44-foot tower joined to the keeper\'s house, with the oil house and privy restored and the barn and summer kitchen rebuilt; some of the Duclons\' own things are on show. Unusually for Door County it has two basements. Shown by guided tour.',
  'The Duclons\' lighthouse, with their belongings.',
  'In Peninsula State Park (Wisconsin DNR); the Door County Historical Society gives tours from mid-May to mid-October for a fee (the DNR page). For 2025 it gave daily tours, 11 a.m. to 3 p.m., $6 (the society\'s opening notice); 2026 hours not checked. A state park sticker is needed. Parking on Shore Road by the lighthouse.',
  [W('Eagle Bluff Light'),L('Wisconsin DNR: Eagle Bluff Light Station','https://dnr.wisconsin.gov/topic/parks/peninsula/lighthouse'),L('Door County Historical Society: Eagle Bluff opens','https://doorcountyhistoricalsociety.org/?p=3310'),DO_NR],
  th=[45.16798,-87.23634],thn='Shore Road lot',conf='mixed',brick='?',hours='Mid-May to mid-October; in 2025 daily 11 a.m. to 3 p.m.'),
# ---- Ozaukee County ----
N('cedarburg-covered-bridge','Covered Bridge (Red Bridge), Cedarburg','Cedarburg','wi','landmark','standing',43.33767,-88.00495,'exact','public','walk','','1876',
  'Built in 1876 over Cedar Creek after farmers petitioned for a bridge that would not wash out like those before it; Wisconsin once had about 40 covered bridges and this is one of the last. A centre support was added in 1927. Ozaukee County took over its care in 1940, bought it with the land around in 1960, and in 1962 shifted it about 50 feet east and closed it to all but walkers, with a new road bridge beside it.',
  'A 120-foot lattice-truss bridge of pine with oak lattices, sided in board and batten, on fieldstone abutments with a concrete centre pier. A 1955 Daughters of the American Revolution plaque calls it the "last covered bridge in Wisconsin".',
  'Wisconsin\'s last old covered bridge.',
  'Covered Bridge County Park, Ozaukee County, on Covered Bridge Road north of Cedarburg. Footbridge, open to walkers; park hours not checked. Parking in the park.',
  [W('Covered Bridge (Cedarburg, Wisconsin)'),OZ_NR],th=[43.33745,-88.00344],thn='Covered Bridge County Park lot',brick='no'),
N('grafton-lime-kilns','Milwaukee Falls Lime Company kilns, Lime Kiln Park','Grafton','wi','industry','ruins',43.30544,-87.95557,'site','public','walk','','1890–1926',
  'Quarrying began here in 1845. The Milwaukee Falls Lime Company, formed in 1890, built five wood-fired kilns by 1893 to burn the dolomite into quicklime, and a concrete dam in 1915 whose turbine drove the drills, a tramway and a crusher. The works closed in 1926. The village bought the site in the 1960s for a park; the dam came out in 2010 and the old quarry was listed on the Register in 2012.',
  'The kilns, the quarry and the mill race, which was left when the dam was removed; a steel truss bridge moved from Bridge Street in 1996 also stands in the park. A TMJ4 report (undated) says the village fenced three kilns after masonry fell and then repaired them.',
  'Five kilns that burned the riverbank into lime.',
  'Lime Kiln Park, Village of Grafton, on Green Bay Road by the Milwaukee River (Wikipedia). Park hours not checked; keep off the kilns if they are fenced. Parking off Green Bay Road.',
  [W('Milwaukee Falls Lime Company'),L('TMJ4: repairs to the Lime Kiln Park kilns','https://www.tmj4.com/news/ozaukee-county/grafton-residents-park-visitor-welcome-repairs-to-preserve-19th-century-lime-kilns'),OZ_NR],
  th=[43.30554,-87.95529],thn='Green Bay Road lot',brick='?'),
# ---- Sheboygan County ----
N('wade-house-greenbush','Wade House','Greenbush','wi','hotel','standing',43.77668,-88.08488,'exact','open','walk','','c.1849–1850',
  'Sylvanus and Betsey Wade\'s stagecoach inn, halfway along the plank road between Fond du Lac and Sheboygan; the Register list says built around 1849 and the Wisconsin Historical Society calls it the original 1850 inn. The society runs it as a historic site.',
  'A two-and-a-half-storey Greek Revival inn with a ballroom in the attic (the Register list), shown on tours, with blacksmithing and horse-drawn carriage rides on the grounds. Interior otherwise not checked.',
  'A plank-road stagecoach inn.',
  'Wisconsin Historical Society, W7965 State Road 23. 2026 season May 23 to November 1, Wednesday to Sunday, admission 9:30 a.m. to 4:30 p.m.; adults $15; parking included (the society\'s release, April 2026). Closed for the winter when read.',
  [W('Wade House'),L('Wisconsin Historical Society: Wade House 2026 season (Urban Milwaukee)','https://urbanmilwaukee.com/pressrelease/all-roads-lead-to-wade-house-2026-season-kicks-off-may-23/'),SH_NR],conf='mixed',brick='no',hours='Late May to early November: Wednesday to Sunday, 9:30 a.m. to 4:30 p.m.'),
# ---- Milwaukee ----
N('st-joan-of-arc-chapel-milwaukee','St. Joan of Arc Chapel','Milwaukee','wi','worship','standing',43.03764,-87.93104,'exact','open','walk','','15th century',
  'A medieval chapel built over generations in Chasse-sur-Rhône, south of Lyon in France, abandoned after the French Revolution and left to ruin. It was taken down and rebuilt on Long Island, New York, then moved again to Marquette University and dedicated to Joan of Arc on May 26, 1966. A sign at the old site in France says Joan may have prayed there on March 9, 1429.',
  'The stone the legend says Joan stood and prayed on lies behind the altar. Old Christian pieces older than the chapel are shown inside, among them Spanish tapestries and crucifixes. The stained glass is not original: the New York owner had it made by Connick (Wikipedia).',
  'A French chapel Joan of Arc may have prayed in, now in Milwaukee.',
  'Marquette University, on the south side of campus west of the Raynor Memorial Libraries. Open Monday to Saturday 10 a.m. to 4 p.m., Sunday noon to 4; closed Saturdays November 21 and 28, 2026; Mass when classes are in session, Monday, Wednesday and Friday at noon and Tuesday and Thursday at 10 p.m. (the chapel\'s visitor page). Parking in the 16th Street parking structure.',
  [W('St. Joan of Arc Chapel'),L('Marquette: Visiting St. Joan of Arc Chapel','https://marquette.edu/st-joan-of-arc-chapel/visitor-information.php')],brick='?',hours='Monday to Saturday 10 a.m. to 4 p.m., Sunday noon to 4 p.m.; Mass in term Monday, Wednesday, Friday noon, Tuesday, Thursday 10 p.m.'),
]

PIN_NOTES={
 'plummer-mine-headframe-pence':'OpenStreetMap point for the headframe (nom.py), 50 m from the HMdb marker position and 60 m from the Register list point.',
 'hokenson-fishery-little-sand-bay':'Register list point for the Hokenson Fishing Dock; the fishery buildings stand by it on the shore, so site precision.',
 'ss-meteor-superior':'OpenStreetMap point for the SS Meteor attraction on Barkers Island (nom.py), 60 m from the Wikipedia coordinate.',
 'mabel-tainter-menomonie':'OpenStreetMap point for the Mabel Tainter theatre, 205 Main Street East (nom.py).',
 'octagon-house-hudson':'OpenStreetMap point for the Octagon House museum, 1004 Third Street (nom.py).',
 'hixon-house-la-crosse':'OpenStreetMap point for the Historic Hixon House Museum, 429 7th Street North (nom.py).',
 'villa-louis-prairie-du-chien':'Moved with pix.py 45 m from the OpenStreetMap museum point, which fell in trees, onto the large house on the raised ground the LiDAR shows (the mound); the aerial was taken in a flood.',
 'indian-agency-house-portage':'Register list point for the Old Indian Agency House; the OpenStreetMap park point is 160 m away.',
 'fort-winnebago-surgeons-quarters':'OpenStreetMap point for the Surgeons Quarters historic site, W1824 State Highway 33 (nom.py); small buildings stand beside it on the aerial and which is the log house is not certain, so site precision.',
 'grignon-mansion-kaukauna':'OpenStreetMap point for the C. A. Grignon Mansion (nom.py); the Register list point is 220 m west. On the aerial the pin is in a clump of trees in the park and the house is not clearly seen, so site precision.',
 'cana-island-lighthouse':'OpenStreetMap point for the lighthouse (nom.py).',
 'eagle-bluff-lighthouse':'OpenStreetMap point for the lighthouse (nom.py).',
 'cedarburg-covered-bridge':'OpenStreetMap path named Covered Bridge (nom.py); a close aerial (look.py) shows the roofed bridge just east of the road bridge at the pin.',
 'grafton-lime-kilns':'Moved with pix.py from the OpenStreetMap park point onto the row of square masonry structures the aerial shows beside the Green Bay Road lot, taken to be the kilns (74 m from the park point).',
 'wade-house-greenbush':'OpenStreetMap building point for the Sylvanus Wade House (nom.py), beside the Register list point.',
 'st-joan-of-arc-chapel-milwaukee':'OpenStreetMap point for Saint Joan of Arc Chapel (nom.py).',
}
