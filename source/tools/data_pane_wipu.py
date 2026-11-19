# November 19, 2026 (UTC): Northeast Pennsylvania & the Poconos (region pane, drawn at random by tools/choose.py), first pass:
# Carbon County round Jim Thorpe (old Mauch Chunk), the Lehigh Gorge, Weissport and Lehighton, Nesquehoning and Lansford,
# with Eckley Miners' Village just over the line in Luzerne County. Coal-baron mansions, the Molly Maguire jail, an Upjohn
# church, the opera house and railroad station; the Switchback gravity railroad; the Lehigh Canal's locks; the tannery
# town burned out in 1875; Fort Allen and the Gnadenhuetten massacre of 1755; a covered bridge; a coal mine and a patch town.
# Facts come from the linked sources only. Wikipedia articles were read as raw text (tools/wiki_raw.py); HMdb marker pages,
# DCNR, PHMC, Carbon County, museum and church pages, the Switchback Gravity Railroad Foundation's trail notes, Times News
# articles and the National Register form for the Nesquehoning grotto were read with tools/page.py.
# Where sources disagree the text gives both; where a source is silent it says "not checked".
# Pins: an OpenStreetMap feature, an HMdb marker position or a Wikipedia/Register coordinate, as each pin note says, then
# looked at on the pin check (aerial and LiDAR sheets).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
JAIL=L('The Old Jail Museum (tours and hours)','https://www.theoldjailmuseum.com/')
APM=L('Asa Packer Mansion Museum: tour information','https://asapackermansion.letartliveon.com/tour')
STM=L('Episcopal Parish of St. Mark and St. John: tours','https://www.stmarkandjohn.org/tours')
MCOH=L('Mauch Chunk Opera House: about','https://www.mcohjt.com/about')
LGSRY=L('Lehigh Gorge Scenic Railway','https://www.lgsry.com/')
HPM=L('Discover NEPA: The Harry Packer Mansion','https://discovernepa.com/listing/harry-packer-mansion/')
SB_NOTES=L('Switchback Gravity Railroad Foundation: trail notes','https://switchbackgravityrr.org/sbtnotes.htm')
MCLP=L('Carbon County: Mauch Chunk Lake Park trails','https://www.carboncountypa.gov/services/mauch_chunk_lake_park/biking__hiking/trails.php')
HM_LOCK1=L('HMdb: Lock No. 1, Lehigh Canal Upper Division','https://www.hmdb.org/m.asp?m=252155')
HM_DAM1=L('HMdb: Dams Made the Lehigh Canal','https://www.hmdb.org/m.asp?m=138500')
LG_HIST=L('DCNR: Lehigh Gorge State Park history','https://www.pa.gov/agencies/dcnr/recreation/where-to-go/state-parks/find-a-park/lehigh-gorge-state-park/history')
LG_PARK=L('DCNR: Lehigh Gorge State Park','https://www.pa.gov/agencies/dcnr/recreation/where-to-go/state-parks/find-a-park/lehigh-gorge-state-park')
HM_LOCK22=L('HMdb: Engineering Marvel (Lock 22)','https://www.hmdb.org/m.asp?m=153403')
HM_LOCKS=L('HMdb: A Revolution in Canal Technology','https://www.hmdb.org/m.asp?m=153402')
HM_TANNERY=L('HMdb: River Ran Black (Lehigh Tannery)','https://www.hmdb.org/m.asp?m=114628')
HM_FAWELL=L('HMdb: Fort Allen Well (PHMC marker)','https://www.hmdb.org/m.asp?m=86879')
HM_FA=L('HMdb: Fort Allen (1947 marker)','https://www.hmdb.org/m.asp?m=86877')
HM_FRANKLIN=L("HMdb: Franklin's Week in Weissport",'https://www.hmdb.org/m.asp?m=252095')
HM_GNADEN=L('HMdb: Site of the Gnaden Huetten Massacre','https://www.hmdb.org/m.asp?m=252108')
TN_LG14=L('Times News: Covered bridge to open soon (November 2014)','https://www.tnonline.com/20141107/covered-bridge-to-open-soon')
TN_LGBARS=L('Times News: Work to repair covered bridge in Lower Towamensing','https://www.tnonline.com/?p=225960')
NO9_LV=L('Lehigh Valley Passport to History: No. 9 Coal Mine and Museum','https://lvhistory.org/historic-sites/no-9-coal-mine-and-museum/')
NO9_UM=L('Underground Miners: Lansford No. 9 Mine','https://undergroundminers.com/lansford-no-9-mine/')
ECK_HRS=L('Eckley Miners\' Village Museum: hours','https://eckleyminersvillage.com/hours/')
ECK_ADM=L('Eckley Miners\' Village Museum: admission and tours','https://eckleyminersvillage.com/admission/')
ECK_PHMC=L('PHMC: Eckley Miners\' Village','https://www.pa.gov/agencies/phmc/historic-sites-and-museums/industrial-heritage-trail/eckley-miners')
GROTTO_NR=L('National Register form: The Grotto, Our Lady of Lourdes Shrine (11000923)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/11000923_text')
PLACES=[
# ---- Jim Thorpe (Mauch Chunk) ----
N('old-jail-jim-thorpe','Old Jail Museum (Carbon County Jail)','Jim Thorpe','pane','civic','standing',40.86393,-75.74652,'exact','public','walk','','1869–1995',
  'The Carbon County jail, a two-storey fortress of rusticated stone with a square guard turret over the door, built in 1869–1870. Suspected "Molly Maguires" were held here while awaiting trial in 1875–1876, and several were hanged. The prisoners left for a new county prison in Nesquehoning on 23 January 1995; Thomas and Betty Lou McBride bought the building from the county for $160,000 and opened it as a museum. Wikipedia names the builder Harry Bowman under architect Edward Haviland; the National Register list gives John Haviland and Henry Bowman.',
  'Guided tours only (about 30 to 35 minutes) through the cell blocks and the basement, used for solitary confinement until 1980. Cell 17 has the handprint said to have been left by Alexander Campbell, hanged in 1877, which legend says no one has managed to remove.',
  'The handprint in cell 17.',
  'Privately owned museum at 128 West Broadway. Guided tours only; the museum page (read November 2026) gives November weekend tours from 12 to a last tour at 4, closed every Wednesday, and open until late November or early December if the weather allows. Tours sell out; buy tickets on arrival for a later slot. Fees and the spring opening date not checked. Park in the borough lots and walk.',
  [JAIL,W('Carbon County Jail')],conf='mixed',brick='no'),
N('asa-packer-mansion','Asa Packer Mansion','Jim Thorpe','pane','landmark','standing',40.86454,-75.73835,'exact','public','walk','','1861–',
  'The house of Asa Packer (1805–1879), the coal and railroad magnate behind the Lehigh Valley Railroad and the founder of Lehigh University, finished in 1861 on a terrace above the Lehigh River. An Italianate villa of three storeys and 18 rooms built over a cast-iron frame for $14,000, attributed to Samuel Sloan. The Jim Thorpe Lions Club opened it for tours on Memorial Day 1956, and it became a National Historic Landmark in 1985.',
  'Wikipedia counts it among the best-preserved Italianate villas in the country: original Victorian furnishings, woodwork and carved panelling, Gothic trefoil details, a cupola and a two-storey porch with lacework balustrades. Seen inside only on a docent-led tour of up to 45 minutes.',
  'A coal baron\'s house left with its furniture still in it.',
  'House museum on Packer Hill above the town centre. The museum page (read November 2026) gives: main season Wednesday to Monday (closed Tuesdays) from 11 am, last tour at 3; April and May weekends only; listed days in November and the first weekends of December, 11 am to 4:15 pm. Wikipedia says open seven days from Memorial Day to October 31; the museum\'s own page is the one to trust. Tours can sell out. Fees not checked.',
  [APM,W('Asa Packer Mansion')],brick='no'),
N('harry-packer-mansion','Harry Packer Mansion','Jim Thorpe','pane','landmark','standing',40.86487,-75.73771,'exact','view','walk','','1874–',
  'A red-brick Italianate house built in 1874 to designs by Addison Hutton, given by Asa Packer to his son Harry Eldred Packer as a wedding present. It stands next door to the Asa Packer Mansion on Packer Hill, with a verandah of green Vermont sandstone and a bell tower on its two-storey wing. Wikipedia says its exterior inspired the Haunted Mansion ride at Walt Disney World.',
  'The brick house, sandstone verandah and tower from Packer Hill. It is now an inn with guest rooms; Discover NEPA says it holds guided tours and murder-mystery weekends. Interior not checked.',
  'The house said to have inspired Disney\'s Haunted Mansion.',
  'Private inn (bed and breakfast) at 19 Packer Hill. Look from the street; the inside is for guests and for the inn\'s own tours, whose times were not checked.',
  [HPM,W('Harry Packer Mansion')],brick='yes'),
N('jim-thorpe-cnj-station','Jim Thorpe station (Central Railroad of New Jersey)','Jim Thorpe','pane','rail','standing',40.86307,-75.73763,'site','public','drive','','1888–',
  'A red-brick Queen Anne station with a round corner tower, designed by Wilson Brothers & Company of Philadelphia and built in 1888 by the Central Railroad of New Jersey. The Lehigh Valley Railroad had its own station across the river. Wikipedia lists it among stations closed in 1976.',
  'The brick station and its tower at the foot of Broadway. It is the Lehigh Gorge Scenic Railway\'s ticket office and excursion station, and a visitor centre; restrooms are inside. What original fittings survive inside was not checked.',
  '',
  'Owned by the Lehigh Gorge Scenic Railway, at Susquehanna Street. Same-day train tickets are sold only at the booth here (railway page, read November 2026); station opening hours not checked. Borough and county pay lots beside it.',
  [LGSRY,W('Central Railroad of New Jersey Station (Jim Thorpe, Pennsylvania)')],th=[40.86258,-75.73795],thn='Railroad Station lot, Susquehanna Street',brick='yes'),
N('st-marks-jim-thorpe','St. Mark\'s Episcopal Church','Jim Thorpe','pane','worship','standing',40.86301,-75.73907,'site','public','walk','','1867–1869',
  'A Gothic Revival church by Richard Upjohn, one of his last, consecrated on 25 October 1869 for a congregation that counted eight coal and railroad millionaires. It replaced a first church of 1848, torn down in 1867. Built of local grey stone trimmed with red stone, it climbs a terraced hillside on Race Street in three levels, the sanctuary on the top. A National Historic Landmark since 1987; the parish is now St. Mark and St. John.',
  'Inside: windows by Louis Comfort Tiffany and Charles Gibson, English Minton tile, black walnut, and a Caen stone reredos. The parish runs guided tours in season.',
  'Tiffany glass bought with coal money.',
  'Working Episcopal church at 21 Race Street. The parish tours page (read November 2026) gives tours from mid-May 2026, Thursday to Sunday 12 to 5 from May 28, and Mondays on holiday weekends; $10 adults, $5 children over 10, under 10 free; no reservation needed. When the tour season ends was not checked: call 570-325-2241. Race Street is steep and narrow; park in the borough lots.',
  [STM,W("St. Mark's Episcopal Church (Jim Thorpe, Pennsylvania)")],brick='no'),
N('mauch-chunk-opera-house','Mauch Chunk Opera House','Jim Thorpe','pane','amuse','standing',40.86463,-75.74189,'exact','view','walk','','1881–',
  'A concert hall built in 1881–1882 to designs by Addison Hutton, next to "Millionaires\' Row": a 900-seat hall over a farmers\' market on the ground floor. It was one of the early vaudeville houses, later the Capitol Theater; the historical society remodelled it and reopened it for its centennial in 1981.',
  'The front on West Broadway. It is a working concert venue of about 450 seats, renovated in stages (new seats, roof, lobby); how much of the 1881 interior survives was not checked.',
  '',
  'Privately run concert hall at 14 West Broadway. Inside for ticketed shows only; look from the street otherwise.',
  [MCOH,W('Mauch Chunk Opera House')],brick='?'),
N('switchback-gravity-railroad','Mauch Chunk Switchback Railway (Switchback Railroad Trail)','Jim Thorpe','pane','rail','traces',40.86944,-75.74972,'area','public','hike','inclines','1827–1932',
  'A gravity railroad built in 1827 by the Lehigh Coal & Navigation Company to carry coal from Summit Hill down to the Lehigh Canal at Mauch Chunk: the second railroad in the United States, and the first over five miles long. Loaded cars ran down by gravity; mules first hauled the empties back up, later two inclined planes up Mount Pisgah and Mount Jefferson did. Freight ended in 1872, and it ran as a tourist ride for 60 more years until the Depression closed it in 1932; the property was sold to a scrapper.',
  'The roadbed is now the Switchback Railroad Trail. Local trail notes kept by the Switchback Gravity Railroad Foundation say: the base of the Mount Pisgah plane is filled in and used as a recreation area, with a small concrete foundation on the line of the plane and the plane itself mostly clear up the mountain; at Summit Hill the top of a wrought-iron fence that followed the track still sticks out of the ground; on the Jefferson plane a drainage culvert survives; and a stairway of 122 stones, built by two miners after the blizzard of 1888, crosses the ridge east of the Mauch Chunk Lake dam. The notes are trail users\' "local knowledge"; not checked on the ground.',
  'The first long railroad in America, then its first roller coaster.',
  'Carbon County maintains the trail for hiking and biking; it can be joined near the main entrance of Mauch Chunk Lake Park (county page, read November 2026), and leads to the Mount Pisgah overlook. The Mount Jefferson plane and much of the Back Track trail between Five Mile Tree and the base of the Jefferson plane are on private property: keep off posted land. Park hours not checked. The Hacklebernie cave-in, where a trestle once crossed, means a ledge or a steep scramble round it.',
  [SB_NOTES,MCLP,W('Mauch Chunk Switchback Railway')],conf='mixed',brick='no'),
N('lehigh-canal-lock-1-jim-thorpe','Lehigh Canal Lock No. 1 (Upper Division)','Jim Thorpe','pane','canal','ruins',40.86816,-75.73513,'area','view','walk','canal','1827–1931',
  'The first lock of the Lehigh Canal\'s Upper Division at Mauch Chunk, built in 1827–1829 by the Lehigh Coal & Navigation Company: about 22 by 100 feet, room for two canal boats one behind the other, with log cribbing weighted with boulders on its downstream side. Mauch Chunk was where the slackwater locks and dams of the Upper Division met the dug canal of the Lower Division to Easton. It worked until October 1931.',
  'Remnants of the lock walls and wood cribbing beneath the PA 903 bridge, near the east bank of the Lehigh River (PennDOT marker, 2024). A second marker on the Mansion House footbridge says the entrance to the lock, Guard Lock 1, has been partly stabilised beside the bridge\'s east end, and that timber cribs of Dam No. 1 dug up when the bridge was built came from hemlocks that began growing about 1547.',
  '',
  'The markers stand on US 209 (Lehigh Avenue) south of PA 903 and on the Mansion House pedestrian bridge, which carries the D&L Trail across the river from the station. Who owns the riverbank under the bridge was not checked: look from the trail and the bridges. The pin is at the east end of the PA 903 bridge, as the marker describes, not on a wall seen on the aerial.',
  [HM_LOCK1,HM_DAM1,W('Lehigh Canal')],th=[40.86258,-75.73795],thn='Railroad Station lot, Susquehanna Street',brick='?'),
# ---- Lehigh Gorge ----
N('lehigh-canal-lock-22-mud-run','Lehigh Canal Lock 22 at Mud Run','Kidder Township','pane','canal','ruins',40.98763,-75.71353,'site','public','hike','canal','1835–1862',
  'One of the 29 high-lift locks of the Lehigh Canal\'s Upper Grand Section, built in 1835–1838 by Josiah White\'s Lehigh Coal & Navigation Company between Mauch Chunk and White Haven, with 20 dams and five and a half miles of dug canal. The locks, designed by Edwin A. Douglas, lifted boats from 10 to as much as 30 feet. The great flood of 1862 destroyed the system and the railroads replaced it.',
  'The ruin of Lock 22: lock walls about 20 feet high of stone fitted without mortar, and the arched conduit that let water in without throwing boats against the gates. Visitors can stand inside the empty lock. Interpretive markers stand at its north end beside the trail.',
  'Stand where the water was, inside a lock with 20-foot walls.',
  'Lehigh Gorge State Park (DCNR), on the Lehigh Gorge Trail (D&L Trail), about 3 miles north-east of the Rockport access area (HMdb). The park is open every day, sunrise to sunset, and the trail is closed to motor vehicles (DCNR page, read November 2026). Walk or bike in from the Rockport lot.',
  [HM_LOCK22,HM_LOCKS,LG_HIST,LG_PARK],th=[40.96635,-75.75502],thn='Lehigh Gorge State Park Rockport Access, Rockport Road',brick='no'),
N('lehigh-tannery-ruins','Lehigh Tannery ruins','Kidder Township','pane','industry','ruins',41.03787,-75.76130,'area','public','walk','burned','1860s–1875',
  'In the 1860s the second-largest tannery in the United States stood on the Lehigh River here, curing as many as 50,000 hides a year with tannic acid from the bark of the gorge\'s hemlocks; its waste turned the river black. Over 100 families lived in the village of Lehigh Tannery, with two railroads, an ice house, a steam sawmill, a hotel and a school. A forest fire in 1875 swept the gorge and destroyed the tannery for good.',
  'The marker beside the trail says the ruins of the tannery and the village are in the woods next to the river. What can be seen of them was not checked; the LiDAR sheet is worth a look before going.',
  'The river ran black from here.',
  'Lehigh Gorge State Park (DCNR), at the Lehigh Tannery access off PA 534 and Tannery Road, where parking is very limited and boat launching is not allowed. The park is open every day, sunrise to sunset (DCNR page, read November 2026). The marker is on the trail just south of the trailhead. The pin is the marker, not a ruin seen on the aerial.',
  [HM_TANNERY,LG_HIST,LG_PARK],th=[41.03834,-75.76178],thn='D&L Trail Lehigh Tannery Trailhead',brick='?'),
# ---- Weissport and Lehighton ----
N('fort-allen-well-weissport','Fort Allen well','Weissport','pane','fort','traces',40.82949,-75.70230,'site','public','walk','forts','1756–',
  'A stockade fort built in January 1756 by the Province of Pennsylvania under Benjamin Franklin\'s own supervision, one of a chain of frontier defences of the French and Indian War, raised after the Gnadenhuetten settlement across the river was attacked in November 1755. Franklin spent about a week here while it went up and later wrote of sleeping on the floor.',
  'The fort\'s well, restored, is the only part left (1971 PHMC marker), "directly behind houses opposite" the marker on Franklin Street. Two more markers stand nearby, one of them a 1947 marker at Bridge Street and the D&L Trail.',
  'Ben Franklin built a fort here and slept on its floor.',
  'Weissport borough, Franklin Street at Bridge Street. The mapped well point falls in Weissport Borough Park on the federal public-land map; park hours not checked. Parking at the D&L Trail lot by the Lehigh Canal in North Weissport.',
  [HM_FAWELL,HM_FA,HM_FRANKLIN],th=[40.83140,-75.70072],thn='D&L Trail parking, Lehigh Canal Park',brick='?'),
N('gnaden-huetten-massacre-site','Gnaden Huetten massacre site','Lehighton','pane','town','marker',40.82538,-75.71483,'area','public','drive','','1746–1755',
  'Gnadenhuetten, a Moravian mission settlement founded in 1746, was the first settlement in what is now Carbon County. On 24 November 1755 it was attacked; ten people were killed, five of them in the flames of their house. The attack set off the building of Fort Allen across the river the following January.',
  'A roadside marker; nothing of the settlement stands. The marker says the dead are buried in the Lehighton cemetery on the hill to the north.',
  '',
  'Marker at South 4th Street and Bridge Street, Lehighton, on public road. The cemetery was not located from a source.',
  [HM_GNADEN,HM_FRANKLIN],brick='?'),
N('little-gap-covered-bridge','Little Gap Covered Bridge','Lower Towamensing Township','pane','landmark','standing',40.83141,-75.52244,'exact','public','drive','','c. 1860–',
  'A 73-foot Burr-truss covered bridge with elements of the Howe truss, built about 1860 over Buckwha Creek near Little Gap. A hit-and-run driver damaged it in 2011. Carbon County had it renovated in 2014 (new steel deck, sandblasting and paint) and reopened it to vehicles that November; the clearance bars at its ends have since been hit and repaired again.',
  'The timber truss and covered span on Covered Bridge Road, still carrying traffic; a nearby restaurant takes its name from it.',
  '',
  'County-owned road bridge (county bridge 17) on Covered Bridge Road, open to traffic. Respect the clearance bars and look from the road shoulders; nowhere to park was found from a source.',
  [TN_LG14,TN_LGBARS,W('Little Gap Covered Bridge')],brick='no'),
# ---- Panther Valley and Nesquehoning ----
N('no-9-mine-lansford','No. 9 Mine and Museum','Lansford','pane','industry','standing',40.82863,-75.89692,'exact','public','drive','','1855–1972',
  'An anthracite deep mine of the Panther Valley, opened in 1855 and closed in 1972; Underground Miners calls it the world\'s oldest continuously operated deep anthracite mine. The museum is in the mine\'s original wash shanty of 1912.',
  'A guided underground tour of about an hour: a ride by mine car into the mountain (1,600 feet, says the 2019 Visit PA listing), then on foot past the 900-foot shaft, along the mule-way and into a miners\' hospital cut from the rock. The wash-shanty museum holds one of the region\'s largest collections of mining objects.',
  'Into a coal mine that worked for 117 years.',
  'Museum on Dock Street, Lansford. Mine tours every hour from 11 am to 3 pm; $10 adults, $7 children 5 to 10 (Lehigh Valley Passport to History page, read November 2026). The 2019 Visit PA listing gave Friday to Sunday in April, October and November and Wednesday to Sunday from May to September; the museum\'s own site did not open, so the season is not checked. The mine is cool all year: bring a jacket.',
  [NO9_LV,NO9_UM],conf='mixed',th=[40.82867,-75.89747],thn='West Ridge Street lot',brick='?'),
N('grotto-nesquehoning','The Grotto, Our Lady of Lourdes Shrine','Nesquehoning','pane','worship','standing',40.8691,-75.8152,'site','view','drive','','1941–1945',
  'A copy of the grotto at Lourdes built single-handed by a local coal miner, Placidio Guido LaRizzio, on a knoll beside Our Lady of Mount Carmel Church in New Columbus, the Italian-American neighbourhood of Nesquehoning, and finished in 1945. It was dedicated to the servicemen and women of the Second World War. The rocks came from a quarry at the end of town and the mountain, with stones, shells and coral that local soldiers brought home from more than a hundred places. The diocese long opposed its listing on the National Register and withdrew its objection in 2019.',
  'The stone grotto with Our Lady of Lourdes in the centre, a kneeling Bernadette, an angel on top and a water trough fed from the rocks; look for the shells, coral and stones from abroad set into its face. Veterans hold services here on Memorial Day and Veterans Day (2011 Register form).',
  'A miner\'s war memorial built from stones of a hundred countries.',
  'Church property (Diocese of Allentown, St. Joseph Parish of the Panther Valley in 2019) at 15 East Garibaldi Avenue. It stands outdoors; visiting rules and hours not checked: treat it as a place of prayer and look respectfully.',
  [GROTTO_NR],brick='no'),
# ---- Luzerne County edge ----
N('eckley-miners-village','Eckley Miners\' Village','Foster Township','pane','town','standing',40.99333,-75.86278,'site','public','walk','','1854–',
  'A coal patch town begun in 1854 by Sharpe, Leisenring and Company for the Council Ridge Colliery, on a shingle-making settlement called Shingletown; first named Fillmore, its first miners were mostly English and Welsh. The 1969 filming of "The Molly Maguires" saved it from demolition, and the Pennsylvania Historical and Museum Commission has owned and run it as a museum since 1970. The wooden coal breaker seen in the film was built as a prop.',
  'Two rows of frame company houses and the museum\'s buildings: Immaculate Conception Church (1861), St. James Episcopal Church (1859), slate pickers\' houses and laborers\' double houses (1854), mine bosses\' houses (1860), the doctor\'s office (1874) and the Sharpe House (1861), with the film\'s breaker. The Catholic church, a miners\' double house and the Episcopal church open inside in season when staff allow.',
  'The patch town Hollywood saved.',
  'PHMC museum at Eckley, near Weatherly. Museum open Wednesday to Sunday, 10 am to 4 pm; the village buildings are closed inside from Labor Day to Memorial Day and in bad weather; guided tours on summer Saturdays for $2 on top of admission (museum pages, read November 2026). Admission price not checked. Allow two hours or more.',
  [ECK_HRS,ECK_ADM,ECK_PHMC,W("Eckley Miners' Village")],th=[40.99516,-75.85587],thn='Eckley museum lot',brick='?'),
]
PIN_NOTES={
 'old-jail-jim-thorpe':'OpenStreetMap museum point for the Old Jail Museum on West Broadway; the NRHP list point is 70 m east.',
 'asa-packer-mansion':'OpenStreetMap museum point for the Asa Packer Mansion, 11 Packer Hill.',
 'harry-packer-mansion':'OpenStreetMap guest-house point for the Harry Packer Mansion, 19 Packer Hill.',
 'jim-thorpe-cnj-station':'OpenStreetMap heritage point for Jim Thorpe Station, Susquehanna Street. On the aerial the point is on the street beside the station block; which roof is the station was not settled, so precision is site.',
 'st-marks-jim-thorpe':'National Register list coordinate (40.86278, -75.73917) fell in the woods behind Race Street; moved 27 m north with tools/pix.py onto the cross-gabled roof on the south side of Race Street seen on the 2021-23 leaf-off aerial. Which roof is the church was judged from the aerial only.',
 'mauch-chunk-opera-house':'OpenStreetMap theatre point, 14 West Broadway.',
 'switchback-gravity-railroad':'Wikipedia article coordinate at the Jim Thorpe end of the line; the trail runs west to Summit Hill.',
 'lehigh-canal-lock-1-jim-thorpe':'East end of the PA 903 bridge over the Lehigh, where the PennDOT marker places the lock remnants, placed with tools/pix.py on the bridge end seen on the aerial; no wall shows under the trees. The marker itself is at 40.86737, -75.73712 on US 209.',
 'lehigh-canal-lock-22-mud-run':'HMdb position of the "Engineering Marvel" marker at the north end of the Lock 22 ruins.',
 'lehigh-tannery-ruins':'HMdb position of the "River Ran Black" marker on the trail south of the Lehigh Tannery trailhead.',
 'fort-allen-well-weissport':'OpenStreetMap "Fort Allen Well" memorial point on Franklin Street; the PHMC marker is 35 m north-west.',
 'gnaden-huetten-massacre-site':'HMdb position of the marker at South 4th and Bridge Streets, Lehighton.',
 'little-gap-covered-bridge':'OpenStreetMap covered-bridge way on Covered Bridge Road.',
 'no-9-mine-lansford':'OpenStreetMap museum point, 9 Dock Street, Lansford.',
 'grotto-nesquehoning':'National Register list coordinate for the Grotto, East Garibaldi Avenue.',
 'eckley-miners-village':'Wikipedia article coordinate in the village street, between the rows of company houses on the aerial. The parking point was moved from an empty field (the OpenStreetMap lot point) to the paved lot by the museum building seen on the 2021-23 aerial, with tools/pix.py.',
}
BATCH={'key':'pane_wipu','label':'Carbon County and the Lehigh Gorge, Pennsylvania','added':'2026-11-19 00:16'}
