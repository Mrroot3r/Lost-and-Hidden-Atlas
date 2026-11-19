# November 19, 2026 (UTC): Northeast Pennsylvania & the Poconos (region pane, drawn at random by tools/choose.py).
# The first places in the Lehigh Valley: Northampton County round Nazareth, Bethlehem and Easton, with the Coplay cement
# kilns just over the line in Lehigh County. Moravian Nazareth and Bethlehem (Whitefield House, Nazareth Hall, the 1741
# Gemeinhaus, the Colonial Industrial Quarter, the Sun Inn), the Henry gun works at Boulton, the Bethlehem Steel blast
# furnaces, the Lehigh Canal at Hugh Moore Park and the Chain Bridge piers, the Lehigh Gap toll house, a Dentzel carousel,
# the county's last covered bridge and the Parsons-Taylor House in Easton.
# Facts come from the linked sources only. Wikipedia articles were read as raw text (tools/wiki_raw.py); the managing
# bodies' pages, HMdb markers, SAH Archipedia, the Lehigh Valley Passport to History pages and the toll-house survey were
# read with tools/page.py. Where sources disagree the text gives both; where a source is silent it says "not checked".
# Pins: an OpenStreetMap feature, an address point, an HMdb marker or a Wikipedia/Register coordinate, as each pin note
# says, then looked at on the pin check (aerial and LiDAR sheets).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
MHS_VISIT=L('Moravian Historical Society: visit','https://www.moravianhistory.org/visit')
MHS_ABOUT=L('Moravian Historical Society: about the site','https://www.moravianhistory.org/about')
LV_MHS=L('Lehigh Valley Passport to History: Moravian Historical Society','https://lvhistory.org/historic-sites/moravian-historical-society/')
SAH_NH=L('SAH Archipedia: Nazareth Hall, Manor House','https://sah-archipedia.org/node/18411')
SAH_SS=L("SAH Archipedia: Single Sisters' House, Nazareth",'https://sah-archipedia.org/node/18412')
DCNR_JB=L('DCNR: Jacobsburg Environmental Education Center history','https://www.pa.gov/agencies/dcnr/recreation/where-to-go/state-parks/find-a-park/jacobsburg-environmental-education-center/history')
LV_JHS=L('Lehigh Valley Passport to History: Jacobsburg Historical Society','https://lvhistory.org/historic-sites/jacobsburg-historical-society/')
JHS=L('Jacobsburg Historical Society','https://www.jacobsburghistory.com/')
KCB=L('Kreidersville Covered Bridge Association','https://kreidersvillecoveredbridge.org/')
WEONA=L('Pen Argyl Borough: Weona Park','https://penargylborough.com/departments/weona-park/')
TOLL=L('C. T. Evans: Lehigh Water Gap Chain Bridge Toll House','https://slatington.ctevans.net/Tollhouse/Tollhouse.html')
TOLL_D=L('C. T. Evans: toll house physical description (PDF)','https://www.ctevans.net/Slatington/Tollhouse/Description.pdf')
HM_SCHOEFER=L('HMdb: The Schoefer Kilns','https://www.hmdb.org/m.asp?m=85448')
HM_COPLAY=L('HMdb: Coplay Made Cement: Cement Made Coplay','https://www.hmdb.org/m.asp?m=85452')
HBMS_MM=L('Historic Bethlehem Museums & Sites: Moravian Museum of Bethlehem','https://historicbethlehem.org/visit-us/museums-sites/moravian-museum-of-bethlehem/')
LV_HBMS=L('Lehigh Valley Passport to History: Historic Bethlehem Museums & Sites','https://lvhistory.org/historic-sites/historic-bethlehem-museums-sites/')
SUN=L('The Sun Inn (Sun Inn Preservation Association)','https://suninnbethlehem.org')
AQ_HMT=L('ArtsQuest: Hoover Mason Trestle','https://www.artsquest.org/?p=1469')
NCM=L('National Canal Museum: notice of reduced 2026 schedule','https://canals.org/?p=10204')
HM_LC=L('HMdb: The Lehigh Canal (PHMC marker)','https://www.hmdb.org/m.asp?m=29601')
HM_HMP=L('HMdb: From Brownfields to Greenfields','https://www.hmdb.org/m.asp?m=157270')
HM_LOCKT=L("HMdb: It's a Short Commute",'https://www.hmdb.org/m.asp?m=109560')
LV_PT=L('Lehigh Valley Passport to History: Parsons-Taylor House','https://lvhistory.org/historic-sites/parsons-taylor-house/')
PLACES=[
# ---- Nazareth ----
N('whitefield-house-nazareth','Whitefield House and Gray Cottage','Nazareth','pane','landmark','standing',40.74213,-75.30674,'exact','open','walk','','1740–',
  'Moravians who had left their failed mission in Georgia began both buildings in 1740 on the Ephrata Tract. The stone Whitefield House (56 by 35 feet) was begun for the evangelist George Whitefield as a school for orphaned slaves, but after a dispute only its foundation was laid for him; the Moravians bought his 5,000 acres, which became Nazareth, and finished the house in 1743 for 32 couples arriving from England. From 1756 to 1758 a stockade 236 by 170 feet with sentry boxes stood round it, and by January 1756 it sheltered 253 refugees from the Gnadenhütten and Northampton massacres, Moravian Lenape among them. Since then it has been a place of worship, a boarding school, a nursery, the Moravian Theological Seminary and housing for missionaries on leave; the Moravian Historical Society, founded in 1857, owns both buildings.',
  'The 1740–1743 stone Whitefield House holds the society\'s museum: paintings by John Valentine Haidt, early American textiles and pottery, early gunmaking and historic musical instruments (the society\'s page), and uniforms from Nazareth Hall (Wikipedia). Admission includes a docent-led tour. The exhibition galleries are upstairs, by stairs only. The 1740 Gray Cottage stands beside it; whether it is shown inside was not checked.',
  'The house Whitefield ordered and the Moravians finished.',
  'Owned by the Moravian Historical Society, on its 3-acre site on East Center Street. The society\'s pages (read November 2026) give open daily 1 to 4 p.m. except major holidays, or by appointment; admission includes a guided tour. The Passport to History page gives $10 adults, $8 students and seniors; free for children under 5. Parking not checked.',
  [MHS_VISIT,MHS_ABOUT,LV_MHS,W('Whitefield House and Gray Cottage')],brick='no',hours='Daily 1 to 4 p.m., except major holidays; or by appointment'),
N('nazareth-hall','Nazareth Hall and the Single Sisters\' House','Nazareth','pane','civic','standing',40.74342,-75.31361,'site','view','walk','','1755–',
  'A large Moravian manor house of limestone rubble, about 46 by 98 to 100 feet under a lofty mansard (gambrel) roof, built in 1755–1756 in the hope that Count Zinzendorf would come back from Europe and settle here; he never did. From 1759 it was the boarding school for Moravian boys, later a well-known classical academy and the forerunner of Moravian College, with military drill from the Civil War years; it closed in 1928–1929. SAH Archipedia says it later served as a military academy, children\'s home and finally apartments. In 1841 it was plastered over, the cupola replaced and the dormers changed, and an addition extended it four bays east. The three-storey limestone Single Sisters\' House of 1784 stands just east of it. The dates differ: SAH gives 1755, Wikipedia 1754 and 1756.',
  'From Center and Green streets: the plastered manor house with its double-pitched roof and rows of dormers and its entrances at either end, the 1784 Single Sisters\' House, and the rest of the Register tract (an 1840 stuccoed stone church, a brick parsonage of the 1870s, the 1819 principal\'s house). Interior not checked.',
  'The house built for a count who never came back.',
  'The buildings are private (apartments, per SAH Archipedia); who owns each was not checked. Look from Center and Green streets in the borough.',
  [SAH_NH,SAH_SS,W('Nazareth Hall'),W('Nazareth Hall Tract')],conf='mixed',brick='some'),
# ---- Jacobsburg ----
N('boulton-historic-site','Boulton Historic Site (Henry Homestead, Pennsylvania Longrifle Museum)','Bushkill Township','pane','landmark','standing',40.77426,-75.28736,'site','open','walk','','1812–',
  'The estate of the Henry family of gunmakers on the Bushkill Creek. William Henry II moved his shop from Christian Springs to Jacobsburg in 1792 and built a forge there; in 1812 a larger gun works went up at Boulton to fill government contracts, and three more generations made rifles here until the late 1800s, for every war from the Revolution to the Civil War and for John Jacob Astor\'s American Fur Company. The gun works itself is gone. The Henry Homestead of 1812 holds the Pennsylvania Longrifle Museum, and the John Joseph Henry house of 1832 was home to five generations of the family. DCNR says only foundations remain of the colonial village of Jacobsburg and of Henry\'s Forge.',
  'The longrifle museum in the Henry Homestead, with Henry guns made here; the 1832 house museum with two centuries of family furniture, an 1868 Chickering piano, clothing and toys; the summer kitchen, carriage and sleigh barns still holding the family\'s vehicles; and the Nicholas Hawk gunshop, moved here timber by timber from Gilbert, Monroe County, and rebuilt in 2008. DCNR also describes a self-guided trail about the gun works. The foundations of Jacobsburg village and Henry\'s Forge were not located in this session.',
  'Rifles for the fur trade, made by hand in a creek valley.',
  'Run by the Jacobsburg Historical Society inside Jacobsburg Environmental Education Center (a DCNR state park), 402–403 Henry Road. The Passport to History page (not the society\'s own) says the museum season opens in May and the site opens for special living-history events, $10 adults; the society\'s own page did not give hours. Henry Road lots in the park are about 250 m north.',
  [DCNR_JB,LV_JHS,JHS,W('Jacobsburg Environmental Education Center')],th=[40.77655,-75.28595],thn='Henry Road lot, Jacobsburg Environmental Education Center',brick='?',hours='?'),
# ---- north of Nazareth ----
N('kreidersville-covered-bridge','Kreidersville Covered Bridge','Allen Township','pane','landmark','standing',40.72375,-75.49281,'exact','public','drive','','1839–',
  'A wooden Burr-truss covered bridge 116 feet long over the Hokendauqua Creek, built in 1839 and the last covered bridge left in Northampton County. When the state planned in 1959 to replace it with a concrete bridge, local people formed the Theodore Burr Covered Bridge Society of Pennsylvania to save it; the state restored it and the county took it over, and it was rededicated in 1961, then called Solt\'s Bridge (also Hummel\'s and Koch\'s, after families who lived nearby).',
  'The Burr arches inside the covered span. Whether cars still cross it was not checked.',
  '',
  'The bridge and Covered Bridge Park are owned and kept by Allen Township (association page, read November 2026), at Covered Bridge Road. No parking lot is mapped; park in Covered Bridge Park (not checked on the ground).',
  [KCB,W('Kreidersville Covered Bridge')],brick='?'),
N('weona-park-carousel','Weona Park Carousel','Pen Argyl','pane','amuse','standing',40.86999,-75.24652,'area','open','walk','','1917–',
  'A Dentzel menagerie carousel built in 1917 and set up in Weona Park in 1923, in a wooden pavilion 80 feet across with 24 sections. Its 44 animals and two sleighs stand three abreast; they were hand-carved and painted in the 1890s, about 1905 and about 1917. Listed on the National Register in 1999.',
  'The carved animals and the round wooden pavilion. Rides cost $2, cash only; photographs are allowed while it runs for the public, but not staged shoots.',
  '',
  'Weona Park is the Borough of Pen Argyl\'s, open dawn to dusk. The borough page (read November 2026) gives the carousel\'s 2026 hours: Fridays 3 to 9 p.m. and weekends 1 to 9 p.m. from late May to Labor Day, then weekends 1 to 8 p.m. to October 3; weather permitting, and festival days vary. Parking not checked.',
  [WEONA,W('Weona Park Carousel')],brick='no',hours='Late May to Labor Day: Fridays 3 to 9 p.m., weekends 1 to 9 p.m. September to early October: weekends 1 to 8 p.m. (2026 season)'),
N('lehigh-gap-toll-house','Lehigh Water Gap Chain Bridge Toll House','Lehigh Township','pane','landmark','standing',40.7822,-75.6051,'site','view','drive','','c. 1826–',
  'A fieldstone toll house built into the bank at Weider\'s Crossing, about half a mile below the Lehigh Gap, for a chain bridge across the Lehigh River put up about 1826. The bridge carried the road from the lower valley north through Slatington towards the anthracite country; it burned in 1926, was rebuilt, and was taken down in 1933 when the highway bridge came. The toll house and the east abutment survive and were listed on the National Register in 2020.',
  'The toll house in the Pennsylvania German style (thick fieldstone walls, steep gable, small irregular windows, a later brick chimney), the stone abutment joined to its south-west corner, and, from the west, the remains of two of the bridge\'s piers in the river. Interior not checked.',
  'A toll house left standing when its bridge went.',
  'Ownership not checked: look from the access road off Riverview Drive or from the Appalachian Trail parking at Weiders Crossing, about 130 m away. Do not go onto the property.',
  [TOLL,TOLL_D],th=[40.78293,-75.60392],thn='Appalachian Trail parking, Weiders Crossing',brick='some'),
N('coplay-cement-kilns','Coplay Cement Company Kilns (Saylor Park)','Coplay','pane','industry','ruins',40.67649,-75.49614,'site','public','walk','','1892–1904',
  'Nine Schoefer vertical kilns of red brick, built by David Saylor\'s Coplay Cement Company in 1892–1893 (an HMdb panel says by 1894) to burn Portland cement; Saylor had taken out the first American patent for it in 1871. The kilns once stood inside a great plant building and ran day and night, but the rotary kiln, first built across the river at Northampton, made them obsolete, and they went out in 1904. The company gave the kilns and land to Lehigh County in 1975; the county owns the site and the Lehigh County Historical Society teaches there.',
  'The row of tall brick kilns, shorter now than when working, with the doors where cement-rock bricks were loaded and the coal-firing level below. Interpretive panels stand round them (one reported missing on HMdb). The rest of the plant is gone.',
  'The kilns that made Lehigh Valley cement famous.',
  'Saylor Park, a Lehigh County park at 245 North 2nd Street, Coplay. The county\'s page would not open from here, so park hours were not checked. A county lot is on North 2nd Street, about 80 m away.',
  [HM_SCHOEFER,HM_COPLAY,W('Coplay Cement Company Kilns')],conf='mixed',th=[40.67586,-75.49569],thn='Saylor Park lot, North 2nd Street',brick='yes'),
# ---- Bethlehem ----
N('colonial-industrial-quarter-bethlehem','Colonial Industrial Quarter (1762 Waterworks and 1761 Tannery)','Bethlehem','pane','industry','standing',40.61917,-75.38333,'site','public','walk','','1741–',
  'The Moravians\' workshop quarter on the Monocacy Creek, begun in 1741 and called the country\'s earliest industrial park: by 1747 some 35 trades worked here off a spring and the creek. The limestone Waterworks of 1762, by the Danish millwright Hans Christoph Christensen, is believed to be the oldest pump-powered public water supply in the United States and is a National Historic Landmark. The 1761 limestone Tannery, three storeys and an attic, handled 1,000 to 2,000 hides a year in the 1760s. The quarter is part of the Moravian Bethlehem World Heritage Site, inscribed in 2024.',
  'Standing: the Waterworks (restored in 1972 from the original craftsmen\'s drawings, with a replica waterwheel restored again in 2009 after Hurricane Ivan), the Tannery, the 1869 Luckenbach Mill, the Gristmiller\'s House, and a springhouse and smithy rebuilt on their old foundations. Ruins: the 1749 Pottery (a wall fragment and foundations on Main Street west of Central Moravian Church), and remains of the 1752 Butchery, 1765 Oil Mill and 1771 Dye House. Wikipedia says the Waterworks is shown on guided tours; their times were not checked.',
  'Water pumped uphill by a waterwheel in 1762.',
  'The buildings and ruins are the City of Bethlehem\'s, leased to Historic Bethlehem Museums & Sites (459 Old York Road for the Tannery and Luckenbach Mill). The grounds along the creek are open ground; tour times for the buildings were not checked on the museum\'s own pages (its quarter page answers 404). Park in the downtown garages.',
  [LV_HBMS,W('Colonial Industrial Quarter'),W('Bethlehem Waterworks'),W('The Tannery (Bethlehem, Pennsylvania)')],brick='no'),
N('moravian-museum-gemeinhaus','Moravian Museum of Bethlehem (1741 Gemeinhaus)','Bethlehem','pane','landmark','standing',40.61893,-75.38108,'exact','open','walk','','1741–',
  'The oldest building in Bethlehem: a log house of white oak begun in 1741 and finished in 1743, where the whole first community of about 80 people lived, worshipped and taught. The Saal on the second floor was their first place of worship; the Old Chapel of 1751 was built into its north-east end. Its logs were stuccoed in 1777 and clapboarded in 1868, and it housed single and widowed women until 1966, when it became the museum. It is thought to be the largest 18th-century log building in continuous use in the country; a National Historic Landmark, also for the mycologist Lewis David de Schweinitz, born here.',
  'Docent-led visits through the Saal and rooms whose plan is almost unchanged since 1743, with remnants of the 1777 scored stucco under the south-west porch, herringbone double doors and the steep kicked roof. The complex beside it holds the 1744–1772 Single Sisters\' House, the 1746 Bell House and the 1751 Old Chapel (seen on the museum\'s World Heritage tour).',
  'A log house that has stood since 1741.',
  'Run by Historic Bethlehem Museums & Sites at 66 West Church Street. Its page (read November 2026) gives the regular hours below, with longer Christmas-season hours (11 a.m. to 6 p.m., some days closed) from mid-November to January 1. Adults $12 plus a fee; free on the first Sunday of the month from February to November. Park in the downtown garages.',
  [HBMS_MM,W('Lewis David de Schweinitz Residence'),W('Historic Moravian Bethlehem District')],brick='no',hours='Mon, Thu and Sun 11 a.m. to 4 p.m.; Fri and Sat 11 a.m. to 5 p.m.; Tue and Wed custom tours only. Longer hours mid-November to January 1'),
N('sun-inn-bethlehem','Sun Inn','Bethlehem','pane','hotel','standing',40.62192,-75.38173,'exact','open','walk','','1758–',
  'The Moravians\' inn for outsiders, a two-storey stone building of 1758 on Main Street, licensed under George III. Its guests included the Penns, General Gage, Sir William Johnson, and on the patriot side George and Martha Washington, Hamilton, Franklin, Lafayette, Pulaski, John Paul Jones and, on 22 September 1777, John Adams, Samuel Adams, John Hancock and other members of the Continental Congress. The Sun Inn Preservation Association runs it today.',
  'A small museum with a self-guided tour of the inn as it was in 1758, and a restaurant (Tavern at the Sun Inn) with a micro-distillery selling colonial-style spirits. No rooms to stay in. Which original fittings survive inside was not checked.',
  'The inn where the Continental Congress stopped in 1777.',
  'Run by the Sun Inn Preservation Association at 564 Main Street. Its page (read November 2026) says the museum is open during restaurant hours. Park in the downtown garages.',
  [SUN,W('Moravian Sun Inn')],brick='no',hours='Museum open during restaurant hours: Wednesday to Saturday, noon to 9 p.m.'),
N('bethlehem-steel-blast-furnaces','Bethlehem Steel blast furnaces and the Hoover-Mason Trestle','Bethlehem','pane','industry','ruins',40.61494,-75.3666,'site','public','walk','','1913–1995',
  'The five rusted blast furnaces of Bethlehem Steel\'s Bethlehem plant, the oldest at the west end dating from 1913. The company grew from the Saucona Iron Company of 1857; its first blast furnace here was lit in 1863. Steel made here went into the Golden Gate and George Washington bridges and more than 1,000 ships in World War II. The plant closed in 1995. The furnaces were left standing as the backdrop of SteelStacks, an arts campus, and the 46-foot-high trestle that once carried ore, coke and limestone to them by narrow-gauge railway (built about 1905) became a 1,650-foot elevated walkway in 2015.',
  'Walk the trestle alongside the furnaces at their mid-height. The rest of the plant here is now venues, a casino and plazas.',
  'Walk beside five blast furnaces on the old ore trestle.',
  'The trestle is a free public walkway on the SteelStacks campus, listed by ArtsQuest, which runs the campus; who owns the furnaces themselves was not checked. It is reached from the Bethlehem Visitor Center and both ends of the Gas Blowing Engine House (Wind Creek lot or the PBS39 end). ArtsQuest (read November 2026): Sunday to Wednesday 10 a.m. to 8 p.m., Thursday to Saturday 10 a.m. to 9 p.m.; closed in bad weather or for events, and the elevator was out of service.',
  [AQ_HMT,W('Hoover-Mason Trestle'),W('Bethlehem Steel')],brick='?',hours='Trestle: Sunday to Wednesday 10 a.m. to 8 p.m.; Thursday to Saturday 10 a.m. to 9 p.m.'),
# ---- Easton ----
N('hugh-moore-park-lehigh-canal','Lehigh Canal at Hugh Moore Park (Locktender\'s House, Guard Lock 8)','Easton','pane','canal','standing',40.65795,-75.24407,'site','public','walk','canal','1827–1942',
  'The Lehigh Canal ran 47 miles from Mauch Chunk to Easton, built 1827–1829, and met the Delaware and Morris canals here; it carried anthracite and fed the anthracite iron industry, fully working until 1932 and partly for ten years more. In 1962 Hugh Moore, founder of the Dixie Cup Company, paid for six miles of canal and land along the Lehigh, and this section was restored in 1976. The City of Easton\'s park holds three operating locks and the last locktender\'s house built by the Lehigh Coal and Navigation Company, beside Guard Lock No. 8, among nineteenth-century industrial ruins.',
  'The only fully restored stretch of towpath canal in Pennsylvania and New Jersey (city panel), the locks, the Locktender\'s House Museum and the mule-drawn canal boat Josiah White II, which runs in season. Whether the boat and house are open in 2026: see below.',
  '',
  'City of Easton park, run with the National Canal Museum, 2750 Hugh Moore Park Road. The museum\'s page (read November 2026) says the Glendon Hill Road bridge into the park is closed, and the museum, heritage-corridor offices and archives are closed for the rest of 2026; the museum was closed for the season. Whether the park and towpath can be reached on foot from the D&L Trail was not checked.',
  [NCM,HM_LC,HM_HMP,HM_LOCKT,W('National Canal Museum')],th=[40.66212,-75.23973],thn='Hugh Moore Park Road lot',brick='?'),
N('chain-bridge-easton','Chain Bridge piers (Lehigh Canal change bridge)','Easton','pane','canal','ruins',40.6538,-75.2485,'site','view','hike','canal','1856–1857',
  'A suspension "change bridge" of 1856–1857 that carried the Lehigh Canal\'s towpath, and the mules, across the Lehigh River at Pool No. 8: before 1857 boats were poled across more than a mile upstream. A causeway reached the west end of the island and a towpath of nearly a mile ran along its south shore to the bridge, hung from iron wire rope over three stone piers about 30 feet high. In 1972 the piers and the cable were still there; the National Canal Museum now says only the stone abutments remain.',
  'Stone piers standing in the river below the island (Island Park), seen from the shore.',
  'A bridge built only for canal mules.',
  'In the Hugh Moore Park and Lehigh Canal Register district (City of Easton). The nearest lot is on Hugh Moore Park Road, over a kilometre away, and the park\'s Glendon Hill Road bridge was closed in 2026 (National Canal Museum). The path to a viewpoint was not checked: look from public ground only.',
  [NCM,W('Chain Bridge (Easton, Pennsylvania)')],conf='mixed',th=[40.66212,-75.23973],thn='Hugh Moore Park Road lot',brick='no'),
N('parsons-taylor-house','Parsons-Taylor House','Easton','pane','landmark','standing',40.68974,-75.21088,'exact','open','walk','','1757–',
  'A two-and-a-half-storey stone house in the Georgian style built in 1757 by the Surveyor-General William Parsons and later rented by George Taylor, ironmaster and signer of the Declaration of Independence, until he died in 1781. The George Taylor Chapter of the Daughters of the American Revolution has owned it since 1906.',
  'Inside, a three-part circular stair (Passport to History page); the Kressler Garden of native plants is next door. The first floor only is accessible.',
  'Home of a signer of the Declaration.',
  'Owned by the DAR chapter. The Passport to History page (not the chapter\'s own) gives docent-led tours by appointment, free, and open house on Easton\'s Heritage Day in July; it gives the address as 40 Ferry Street, OpenStreetMap as 56 South 4th Street. Park in the downtown garages.',
  [LV_PT],conf='mixed',brick='no',hours='?'),
]
PIN_NOTES={
 'whitefield-house-nazareth':'OpenStreetMap museum point for Whitefield House on East Center Street; the Wikipedia point is about 140 m south-west.',
 'nazareth-hall':'Wikipedia coordinate for the Nazareth Hall Tract; on the aerial it falls on a large building in the tract, taken to be Nazareth Hall.',
 'boulton-historic-site':'ArcGIS PointAddress for 402 Henry Road; lot is the mapped Henry Road lot in the park.',
 'kreidersville-covered-bridge':'OpenStreetMap bridge way on Covered Bridge Road.',
 'weona-park-carousel':'OpenStreetMap point for Weona Park, on the ball field; the carousel pavilion could not be picked out with certainty on the aerial, so the pin marks the park. The Register point, about 200 m north-west, falls on houses in town.',
 'lehigh-gap-toll-house':'Register list coordinate; on the aerial it falls on a small building between the rail line and the river, taken to be the toll house. Lot is the mapped Appalachian Trail parking at Weiders Crossing.',
 'coplay-cement-kilns':'OpenStreetMap point for Saylor Park; HMdb gives the kiln panel at 40.67688, -75.49617.',
 'colonial-industrial-quarter-bethlehem':'Wikipedia coordinate for the Bethlehem Waterworks, in trees by the Monocacy Creek on the aerial; the building is not clear under the trees.',
 'moravian-museum-gemeinhaus':'OpenStreetMap heritage point for the Gemeinhaus, 66 West Church Street.',
 'sun-inn-bethlehem':'OpenStreetMap point for The Sun Inn, 564 Main Street.',
 'bethlehem-steel-blast-furnaces':'OpenStreetMap footway of the Hoover-Mason Trestle, beside the furnaces.',
 'hugh-moore-park-lehigh-canal':'OpenStreetMap museum point for the Locktender\'s House.',
 'chain-bridge-easton':'OpenStreetMap ruin point "Lehigh Canal Chain Bridge", on a pier in the river on the aerial; the Wikipedia point is 40 m west.',
 'parsons-taylor-house':'OpenStreetMap building point for the Parsons-Taylor House.',
}
BATCH={'key':'pane_jmkq','label':'Nazareth, Bethlehem and Easton (Lehigh Valley), Pennsylvania','added':'2026-11-19 21:09'}
