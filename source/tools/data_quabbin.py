# November 17, 2026: the Quabbin and the North Quabbin, Massachusetts (region 'cmass'), first close pass.
# Chosen because region cmass held 3 places against 48 in Worcester and 15 in the Pioneer Valley next to it.
# What it holds: what is left of the Swift River valley's four lost towns outside Dana Common (already in data_ma.py):
# the Rabbit railroad bed at Gate 35, the wartime range remains at Gate 52, Webster Road in old Enfield, the
# Quabbin Park Cemetery, two buildings carried out of Prescott, the Keystone Bridge at Millington, the lost spa
# village of Coldbrook Springs in the Ware River watershed; and mill and farm ruins on Trustees reservations at
# Bear's Den, Doane's Falls and Swift River, plus the Ware-Hardwick covered bridge.
# Facts come from the linked sources only. DCR's Quabbin pages, packets, kiosk posters and event pages were read
# with the web fetch tool (mass.gov refuses tools/page.py with HTTP 403); Trustees pages and trail maps, newspaper
# articles, the Swift River Valley Historical Society site, Wachusett Greenways and the Byways page through
# tools/page.py; Wikipedia as raw text (tools/wiki_raw.py). Where sources disagree the text gives both; where a
# source is silent the entry says "not checked". Nothing here was checked on the ground.
# Pins: an OpenStreetMap feature (tools/nom.py, tools/osmnear.py), a Wikipedia or DCR coordinate, an address
# lookup, or a spot read off the aerial and LiDAR, as each pin note says. Every pin was looked at with
# tools/pincheck.py --lidar (research/pincheck_quabbin_*.jpg).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'quabbin','label':'The Quabbin and North Quabbin: lost-town traces, mill ruins, Prescott survivors','added':'2026-11-17 18:41'}
DCR_ACCESS=L('DCR: watershed public access maps and rules (Gate 30 notice)','https://www.mass.gov/info-details/dcr-watershed-public-access-maps')
DCR_PARK=L('DCR: Quabbin Park brochure (rules, hours)','https://www.mass.gov/doc/quabbin-park-brochure/download')
DCR_DETECT=L('DCR: Be a History Detective at Quabbin Reservoir','https://www.mass.gov/doc/be-a-history-detective-at-quabbin-reservoir/download')
DCR_PARKPACK=L('DCR Quabbin educational packet: Quabbin Park','https://www.mass.gov/files/documents/2017/09/25/Quabbin%20park.pdf')
DCR_G35=L('DCR Quabbin educational packet: Gate 35','https://www.mass.gov/files/documents/2017/09/25/Gate%2035.pdf')
DCR_RABBIT=L('DCR kiosk poster: the Rabbit railroad','https://www.mass.gov/doc/quabbin-reservoir-kiosk-poster-rabbit-run-railroad/download')
DCR_MILL=L('DCR event: Exploring the Road to Millington (Gate 29), Oct. 11, 2026','https://www.mass.gov/event/exploring-the-road-to-millington-gate-29-10112026-10-11-2026')
DCR_KEY26=L('DCR event: Quabbin\'s Keystone Bridge, updated (Jan. 2026)','https://www.mass.gov/event/quabbins-keystone-bridge-updated-1252026-01-25-2026')
ADN_KEY=L('Athol Daily News (Oct. 26, 2025): work begins at Keystone Bridge','https://atholdailynews.com/2025/10/26/historic-bridge-stabilization-new-salem/')
ADN_KEY0=L('Athol Daily News (Mar. 3, 2025): Friends of Quabbin want to restore the bridge','https://atholdailynews.com/2025/03/03/friends-of-quabbin-want-to-restore-new-salem-stone-arch-bridge-59725427/')
DCR_CEM=L('DCR: Quabbin Park Cemetery','https://www.mass.gov/info-details/quabbin-park-cemetery')
SRVHS=L('Swift River Valley Historical Society','https://swiftrivermuseum.org')
REC_MOVE=L('Greenfield Recorder (Aug. 9, 2020): moving days in North Quabbin','https://recorder.com/2020/08/09/moving-days-in-north-quabbin-35614016/')
PREBLE=L('Peter Preble: the Methodist Episcopal Church of Prescott (blog, 2015)','https://www.frpeterpreble.com/2015/04/new-england-churches-the-methodist-episcopal-church-of-prescott-massachusetts.html')
TT_BD=L('The Trustees: Bear\'s Den','https://thetrustees.org/place/bears-den/')
TT_BDMAP=L('The Trustees: Bear\'s Den trail map (2024)','https://thetrustees.org/wp-content/uploads/2024/05/bears-den-trail-map.pdf')
TT_DF=L('The Trustees: Doane\'s Falls','https://thetrustees.org/place/doanes-falls/')
TT_DFMAP=L('The Trustees: Doane\'s Falls trail map (2023)','https://thetrustees.org/wp-content/uploads/2024/07/doanes-falls-trail-map.pdf')
TT_SR=L('The Trustees: Swift River Reservation','https://thetrustees.org/place/swift-river-reservation/')
TT_SRMAP=L('The Trustees: Swift River Reservation trail map','https://thetrustees.org/wp-content/uploads/2020/07/SwiftRiver_TrailMap_2018.pdf')
BYWAY_CB=L('Western Mass Scenic Byways: Coldbrook Springs','https://www.bywayswestmass.com/map-markers/coldbrook-springs')
WG_CB=L('Wachusett Greenways: hike and history of the Coldbrook area','https://www.wachusettgreenways.org/wordpress/?p=5654')
WARE_RULES=L('DCR: 2023 Ware River Watershed public access summary','https://www.mass.gov/doc/2023-ware-river-watershed-public-access-management-summary/download')
QUABBIN_RULES='DCR watershed land (Division of Water Supply Protection). Dogs and other domestic animals are not allowed anywhere at Quabbin Park or on the Quabbin Reservation; no swimming, fires, camping or alcohol; do not take artifacts. Hours are those posted at each gate; DCR\'s Quabbin Park brochure says the park is open dawn to dusk.'
PLACES=[
# ---- The lost towns of the Swift River valley ----
N('rabbit-railroad-gate-35','Rabbit railroad bed and North Dana cellar holes, Gate 35','New Salem','cmass','rail','traces',42.48597,-72.27777,'site','public','hike','stations,drowned','1873–1935',
  'The road to the left inside Quabbin Gate 35 is the bed of the Springfield-to-Athol line through the Swift River valley, opened in 1873 and known as "the Rabbit" for its many stops. The Boston and Albany bought it in 1880 and the New York Central ran it from 1901. The last train ran on June 1, 1935, and the water-supply commission took up the rails at once. The DCR packet calls the line the Athol & Enfield and dates its first run to 1871; its own kiosk poster gives 1873 for the opening.',
  'DCR says the walk passes cellar holes and foundations of the buildings that stood here, an old ice pond (now a beaver pond past the power lines), patches of the old Route 21 tar and, about 1 1/3 miles in, a tower the military built in the 1940s for watching bombing practice in the valley. The road ends at the water after about 1 1/2 miles. When the reservoir is very low the foundation of the New Salem station shows on the shore about a mile south of the gate. None of this was checked on the ground.',
  'Walk the Rabbit\'s grade into a valley that was emptied for Boston\'s water.',
  'Quabbin Reservation, DCR. Park at Gate 35 at the end of Old North Dana Road, New Salem. '+QUABBIN_RULES,
  [DCR_G35,DCR_RABBIT,DCR_PARK],conf='mixed',th=[42.50420,-72.27405],thn='Gate 35 parking, Old North Dana Road'),
N('keystone-bridge-new-salem','Keystone Bridge at Millington','New Salem','cmass','landmark','standing',42.53421,-72.30267,'exact','public','hike','','1866–',
  'A dry-laid stone arch over the Middle Branch of the Swift River, built in 1866 by Adolphus Porter. The stones were cut and stacked with no mortar. It stands on the old road to Millington (so named in OpenStreetMap), a lost village of New Salem, and now carries a trail. Damage was spotted in the summer of 2021 and DCR closed Gate 30 and the road over the bridge that July. The Friends of Quabbin raised the money to stabilize it, work began in October 2025, and DCR reported the stabilization finished that fall.',
  'The single stone arch over the river, a short walk inside the gate. Whether the deck is open to walk on again was not checked: DCR\'s access page still carried its July 2021 closure notice for Gate 30 when it was read, while DCR\'s own guided walk of October 2026 went in from Gate 29 and stopped to see the bridge.',
  'A Civil War veteran\'s mortarless arch that outlived the town it served.',
  'Quabbin Reservation, DCR. Gate 30 on Route 122 has been closed since July 10, 2021; DCR recommends Gate 29, at Elm Street and Route 202 in New Salem, for this part of the reservation (limited parking; do not block the gate). Keep off the bridge if it is signed closed. '+QUABBIN_RULES,
  [ADN_KEY,ADN_KEY0,DCR_KEY26,DCR_ACCESS,DCR_MILL],conf='mixed'),
N('webster-road-enfield','Webster Road, old Enfield','Belchertown','cmass','town','traces',42.28897,-72.32669,'area','public','walk','drowned','–1938',
  'Webster Road, once called Long Hill Road, ran from the centre of Enfield towards what is now Route 9, past mostly working farms. Enfield was the largest of the four towns given up for the Quabbin; it ceased to exist on April 28, 1938. Before the buildings were destroyed every one was photographed and its place recorded, and DCR keeps those photographs at its Administration Building.',
  'DCR describes foundations, cellar holes and fields from the homesteads along a fairly level road of about 1.5 miles, with stone walls, old sugar maples that may carry tap scars, and trees grown round barbed wire. The house and land beyond the gate at the far end are private. Which cellar hole belonged to whom was not checked.',
  '',
  'Quabbin Park, DCR. The trailhead is on the park road about three quarters of a mile past Enfield Lookout, across from Hanks Meadow, where DCR asks walkers to park. The walk is about 2 miles and easy. '+QUABBIN_RULES,
  [DCR_DETECT,DCR_PARKPACK,DCR_PARK,L('DCR event: Quabbin\'s Hidden History: Webster Road','https://www.mass.gov/event/quabbins-hidden-history-webster-road-962026-09-06-2026')],th=[42.30741,-72.32391],thn='Hanks Meadow parking (OpenStreetMap: Shoreline/Enfield Lookout Trail)'),
N('quabbin-park-cemetery','Quabbin Park Cemetery','Ware','cmass','burial','standing',42.281794,-72.308542,'site','public','drive','cemeteries,drowned','1931–',
  'Built in 1931 and 1932 by the Metropolitan District Water Supply Commission on 82 acres of farm and woodland south of Route 9, outside the watershed, to take the dead of the Swift River valley. In all 7,613 graves were moved from 34 cemeteries, and 6,601 were reburied here; families chose other cemeteries for the rest. Formal cemetery groups were not kept together. It is still an active cemetery for former residents of the four towns, their direct descendants and DCR staff.',
  'The entrance columns on Route 9 are built of stones from the foundation of every church in the valley, with bronze plaques naming every cemetery that was removed. The war memorials and markers of Dana, Enfield, Greenwich and Prescott stand near the entrance. DCR\'s page has a tour of 27 stops and a web app for finding a grave.',
  'Where Dana, Enfield, Greenwich and Prescott went to be buried.',
  'Owned and run by DCR, which sets its rules (DCR\'s cemetery page). On Route 9 in Ware (557 Belchertown Road), about three miles east of the Quabbin Visitor Center. No dogs or pets; headstone rubbings only by direct descendants. Hours were not given on DCR\'s page and were not checked.',
  [DCR_CEM,DCR_PARKPACK,DCR_DETECT]),
N('quabbin-gate-52-range','Gate 52 wartime range remains','Ware','cmass','fort','ruins',42.30800,-72.31644,'area','public','walk','','',
  'DCR says the U.S. Air Force used the Quabbin valley floor for target practice with dummy bombs, often filled with flour. When is not given in the source read. The end of the road from Gate 52 was a practice shooting range, with concrete structures for storing ammunition and a helicopter landing pad.',
  'DCR\'s educational packet (posted 2017) says the remains of these structures can still be seen; what is left now and exactly where was not checked. The walk from the gate is short, about 0.3 mile each way on a hiking site\'s map.',
  '',
  'Quabbin Park, DCR. Gate 52 is on Ware Enfield Road inside the park. '+QUABBIN_RULES,
  [DCR_PARKPACK,DCR_PARK,L('MyHikes: Gate 52 Trail (map and length)','https://myhikes.org/trails/gate-52-trail')],conf='mixed',th=[42.305832,-72.314907],thn='Gate 52 (parking point from MyHikes)'),
N('prescott-church-swift-river-museum','North Prescott Methodist church (Swift River Valley Historical Society)','New Salem','cmass','town','standing',42.54079,-72.31542,'site','open','drive','drowned','1837–',
  'The Methodist Episcopal church of North Prescott stood about 20 feet inside what became the reservoir line. Prescott people bought it to save it. In 1949 it was taken down, carried in pieces to donated land in Orange and put up again as the Prescott Historical Society, which took most of a year; in 1985 it was moved in one piece, over two days, to the Swift River Valley Historical Society\'s grounds in North New Salem. A 2015 blog post gives 1837 as the year it was built; no other source read here gives a date.',
  'The church, the Whitaker-Clary House and the Carriage Shed hold the society\'s museum of Dana, Enfield, Greenwich and Prescott, including a 1929 Dana fire truck.',
  'A church that left the valley in pieces and came back to the edge of it.',
  'The society owns the museum grounds at 40 Elm Street, New Salem, just west of Route 202 (Wikipedia: the church is now the society\'s home). The society\'s site gives the museum as open Wednesdays and Sundays 1 to 4 p.m. from mid-June to mid-September, free; it listed a closing date of September 16 for 2026. The grounds outside those hours were not checked.',
  [SRVHS,REC_MOVE,W('Prescott, Massachusetts'),PREBLE]),
N('prescott-town-house-petersham','Prescott Town House','Petersham','cmass','civic','standing',42.49889,-72.18361,'area','ask','drive','drowned','1838–',
  'The town hall of Prescott, a Greek Revival building of 1838 that stood just south of Atkinson Hollow. When Prescott was given up for the Quabbin, Judge John Monroe Woolsey paid to move it to Petersham and used it as a law library and office. It was listed on the National Register in 1989.',
  'The town house on a hill above a hay meadow north of Petersham centre, off Route 32. Whether it can be seen from Route 32 was not checked.',
  'Prescott\'s town hall, carried out of the valley to be a judge\'s library.',
  'Not open to the public, according to Wikipedia\'s Prescott article; who owns it now was not checked. Do not go up to it without the owner\'s leave. The Register form is a scan with no text layer and was not read.',
  [W('Prescott Town House'),W('Prescott, Massachusetts')]),
# ---- The Ware River watershed ----
N('coldbrook-springs','Coldbrook Springs village site','Oakham','cmass','hotel','traces',42.39476,-72.04713,'area','public','walk','hotels','–1930s',
  'A village beside a sulphur spring and an iron spring, with the Cold Spring House, a hotel and boarding house for visitors with a bath house, a store, post office and billiard hall, a blacksmith, a machine shop, a box mill and at least ten houses. The state bought the hotel in 1930 and removed it and the other buildings to protect the Ware River watershed, as part of the Quabbin aqueduct system.',
  'The sources disagree: the Byways page says many foundations and remnants of the village are still there; Wachusett Greenways says the cisterns that held the spring water are still visible at the hotel site. Where the hotel and cisterns stand on the ground was not checked; the pin is the road corner where the Greenways walk began.',
  'A spa for invalids, bought and erased for Boston\'s water.',
  'DCR Ware River Watershed land: the federal public-land map puts the ground just north-west of the corner in the Ware River Watershed, and DCR names Coldbrook Road among its watershed roads. Open from one hour before sunrise to one hour after sunset; dogs must be on a leash of 6 feet or less; vehicles are allowed on Coldbrook Road in daylight only; hunting is allowed in season with a DCR permit, so wear orange. The parking spot at the corner of Route 122 and Coldbrook Road was not checked.',
  [BYWAY_CB,WG_CB,WARE_RULES,L('DCR: Ware River Watershed (hours)','https://www.mass.gov/locations/ware-river-watershed')],conf='mixed'),
# ---- Trustees reservations of the North Quabbin ----
N('williams-homestead-ruins','Williams Homestead ruins, Swift River Reservation','Petersham','cmass','town','ruins',42.46131,-72.16806,'exact','public','walk','','',
  'The Slab City tract of the Trustees\' Swift River Reservation was farmland until the late 1880s, and small mills also stripped it of trees; it has grown back to forest. The tract takes its name from the granite slabs quarried from its outcrops for local buildings. The Trustees\' trail map marks the Williams Homestead ruins.',
  'Open grass paths through cellar holes on the Slab City tract, with the Williams Homestead ruins marked on the trail map. Who the Williams family were and when the house went was not found.',
  '',
  'The Trustees of Reservations, Swift River Reservation, Slab City tract. Entrance and parking for six cars on Route 122/32, 2 miles south of the Route 122 and 32 junction, at Connor\'s Pond. Open daily sunrise to sunset, free. Dogs on leash. Hunting allowed in season except Sundays; wear orange. Lots are seldom plowed in winter.',
  [TT_SR,TT_SRMAP,W('Swift River Reservation')],th=[42.46117,-72.16545],thn='Slab City tract parking, Route 122/32'),
N('bears-den-mill-site','Bear\'s Den mill site','New Salem','cmass','industry','ruins',42.54228,-72.32627,'area','public','walk','','',
  'At Bear\'s Den the Middle Branch of the Swift River drops about 12 feet into a pool at the foot of a gorge some 70 feet deep. The river also drove a mill here. The Trustees\' trail map marks a mill site and an old dam.',
  'The foundation of the old mill beside the stream, on the right-hand path from the entrance; the falls are to the left. Age and use of the mill were not found in any source read.',
  '',
  'The Trustees of Reservations, Bear\'s Den, 18 Neilson Road, New Salem; roadside parking at the entrance, 0.5 mile along Neilson Road from Elm Street. Open daily sunrise to sunset, free. Dogs on leash. Hunting allowed in season except Sundays. Steep drops and rocky ground; land beside it is private.',
  [TT_BD,TT_BDMAP,W('Bear\'s Den')],th=[42.54154,-72.32508],thn='Bear\'s Den roadside parking, Neilson Road'),
N('doanes-falls-mill-site','Doane\'s mill site and cellar holes','Royalston','cmass','industry','ruins',42.6488,-72.2019,'area','public','walk','','19th century',
  'Amos Doane, who owned land in Royalston in the early 1800s, built a mill above the falls on Lawrence Brook, 50 feet long and more than four storeys tall, to make doors, sashes and blinds. His venture failed, but earlier mills had worked the falls with success. Wikipedia says only the foundations of these mills remain.',
  'The Trustees\' trail map marks the site of Doane\'s mill and a group of cellar holes beside the trail along the falls. The pin is the falls, not the mill site.',
  '',
  'The Trustees of Reservations, Doane\'s Falls, Athol Road, Royalston; parking for three cars at the entrance, more at the lower lot on Doane Hill Road. Open daily sunrise to sunset, free. Stay behind the safety fence: swimming, wading and going down to the water are banned after deaths and injuries. Dogs on leash. Hunting allowed on the Coddings Meadow parcel except Sundays.',
  [TT_DF,TT_DFMAP,W('Doane\'s Falls')],th=[42.64993,-72.20082],thn='Doane\'s Falls parking, Athol Road'),
N('ware-hardwick-covered-bridge','Ware-Hardwick Covered Bridge','Hardwick','cmass','landmark','standing',42.31016,-72.21214,'exact','public','drive','','1886–',
  'A single-span Town lattice covered bridge over the Ware River at Gilbertville, the woollen-mill village of Hardwick, built in 1886 and managed by a joint committee of Ware and Hardwick. It came through the flood of the 1930s that destroyed Gilbertville\'s mills. It was rebuilt in 1986-1987, closed by the state in August 2002, and reopened in October 2010. It is one of a few 19th-century covered bridges left in Massachusetts.',
  'The one-lane bridge, sided in vertical boards with a strip left open for light, between Bridge Street in Gilbertville and Old Gilbertville Road in Ware.',
  '',
  'A public road bridge that carries cars, one lane; Wikipedia says the two towns run it through a joint committee. Parking near it was not checked.',
  [W('Ware–Hardwick Covered Bridge')]),
]
PIN_NOTES={
 'rabbit-railroad-gate-35':'OpenStreetMap track named "Rabbit Run Rail Bed" south of Gate 35 (tools/osmnear.py). On the 2023 leaf-off aerial the pin is on a woods road near the shore; the LiDAR shows a raised grade there. The trailhead point is the lot OpenStreetMap maps at the end of Old North Dana Road: the aerial shows a road junction with a small clearing in woods, not a house.',
 'keystone-bridge-new-salem':'OpenStreetMap bridge on the old Orange Millington Road over the Middle Branch of the Swift River (tools/osmnear.py). The aerial shows the river and the woods road under trees; the LiDAR shows the road crossing the stream at the pin, with Route 122 about 100 m east.',
 'webster-road-enfield':'A point on the OpenStreetMap line of Webster Road in Quabbin Park; the LiDAR shows the old road and field walls round it. No source places a single cellar hole. The trailhead point is the lot OpenStreetMap maps at the Shoreline/Enfield Lookout trail, a gravel lot in a clearing on the aerial, taken to be Hanks Meadow.',
 'quabbin-park-cemetery':'Coordinate printed on DCR\'s Quabbin Park Cemetery page; on the aerial it is on Route 9 at the cemetery entrance, with the grounds to the south.',
 'quabbin-gate-52-range':'No source places the structures. Moved 65 m with tools/pix.py onto small rectangular shapes beside the end of the OpenStreetMap track from Gate 52, seen on the LiDAR only (the aerial shows bare woods); they may be the structures DCR describes, or not. The trailhead point is MyHikes\' parking point, on the park road on the aerial.',
 'prescott-church-swift-river-museum':'ArcGIS address lookup of 40 Elm Street, New Salem; the aerial shows the society\'s group of buildings at the pin.',
 'prescott-town-house-petersham':'Wikipedia coordinate (from the National Register list). On the aerial the pin is in a hay meadow, with a small building about 50 m north-east and others on the hill to the north-west; which one is the town house was not settled, so the pin is area only.',
 'coldbrook-springs':'ArcGIS lookup of the corner of Route 122 and Coldbrook Road, where the Wachusett Greenways walk began; the hotel site is not placed by any source. The LiDAR shows a few small square hollows within about 150 m of the corner, not checked as cellar holes.',
 'williams-homestead-ruins':'OpenStreetMap point "Williams Homestead Ruins" (mapped ruin), matching the ruins on the Trustees\' trail map. The LiDAR shows a sharp square hollow at the pin, in a clearing on the aerial. The trailhead point is OpenStreetMap\'s lot beside Route 122 at Connor\'s Pond, a clearing off the road on the aerial.',
 'bears-den-mill-site':'OpenStreetMap point for the Bear\'s Den reserve (tools/nom.py), in woods above the gorge on the aerial and LiDAR; the mill site on the Trustees\' map was not picked out. The trailhead point is OpenStreetMap\'s parking point on the Neilson Road shoulder.',
 'doanes-falls-mill-site':'Wikipedia coordinate for the falls, on white water on the aerial; the mill site and cellar holes are beside the falls trail on the Trustees\' map and were not picked out. The trailhead point is OpenStreetMap\'s parking at the Athol Road bridge, a road shoulder on the aerial.',
 'ware-hardwick-covered-bridge':'Wikipedia coordinate was 33 m west of the bridge in the trees; moved with tools/pix.py onto the covered bridge, which shows plainly on the 2023 aerial.',
}
