# November 17, 2026: Washington County, New York (Fort Edward, Fort Ann, Whitehall, the Hudson at Thomson and
# Hudson Falls, Shushan) and the Knapp estate at Shelving Rock on Lake George.
# The old Champlain Canal between Fort Edward and Fort Ann first: its locks, the Fort Edward junction lock, the Moses
# Kill aqueduct; then bridge piers left in the Hudson, the burned Knapp estate (finished from LEADS.md), the hull of
# USS Ticonderoga at Whitehall, and four standing places (Skene Manor, the Old Fort House, the Shushan bridge).
# Facts come from the linked sources only. Wikipedia was read as raw text (tools/wiki_raw.py); the American Canal
# Society's Champlain Canal structures table (revised 5/28/11) and the Lakes to Locks Passage guidebook "The Northern
# Inland Passage" (2019) as text taken from their PDFs; the 2023 Old Fort Edward Junction Locks feasibility report
# (Barton & Loguidice for the Adirondack/Glens Falls Transportation Council and the village) as text from its PDF;
# the American Canal Society's Glens Falls Feeder sheet through the web fetch tool (its text layer was too thin for
# tools/page.py); HMdb marker pages, park, museum, trail and agency pages, and hobby blogs through tools/page.py.
# Where sources disagree the entry gives both; where a source is silent it says "not checked". Washington County's
# tax parcels are not in the state file tools/parcel.py reads, so no owner was looked up by parcel.
# Pins: an OpenStreetMap feature (tools/nom.py), the Canal Society's GPS position, an HMdb marker position, or a
# spot read off the aerial with tools/look.py and tools/pix.py, as each pin note says. Every pin was looked at with
# tools/pincheck.py --lidar (research/pincheck_washco_*.jpg).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'washco','label':'Washington County: old Champlain Canal locks, river piers and Whitehall','added':'2026-11-17 17:41'}
ACS=L('American Canal Society: Champlain Canal structures table (PDF, revised 2011)','https://americancanalsociety.org/wp-content/uploads/2019/08/Champlain-Canal2.pdf')
FEED=L('American Canal Society: Glens Falls Feeder (PDF)','https://americancanalsociety.org/wp-content/uploads/2019/08/Glens-Falls-Feeder.pdf')
GUIDE=L('Lakes to Locks Passage: The Northern Inland Passage, Champlain Canal guidebook (PDF, 2019)','https://passageport.org/wp-content/uploads/2021/06/Champ-Canal-Guidebook-Interior-7.pdf')
FEJL=L('Old Fort Edward Junction Locks Trail Extension, final feasibility report (PDF, 2023)','https://public.warrencountyny.gov/gis/PlanLibrary/2023%20Old%20Fort%20Edward%20Junction%20Locks%20Trail%20Extension.pdf')
EST=L('Empire State Trail: Champlain Canalway Trail, Fort Edward to Fort Ann','https://empiretrail.ny.gov/albany-whitehall/fort-edward-fort-ann')
GHOST=L('Wash Wild blog (2022): Ghost Bridges','https://wcny.blogspot.com/2022/08/ghost-bridges.html')
PLACES=[
# ---- The old Champlain Canal, Fort Edward to Fort Ann ----
N('old-champlain-lock-15-fort-edward','Old Champlain Canal Lock 15, Fort Edward','Fort Edward','wash','canal','ruins',43.27070,-73.58378,'exact','view','walk','canal','',
  'Lock 15 stood at the south end of the old Champlain Canal\'s summit level, the stretch fed with water by the Glens Falls Feeder. The canal from Fort Edward north to Lake Champlain opened in 1819 and the whole canal in 1823. When the Barge Canal took a new line through Fort Edward early in the 1900s, the feeder stayed in service through the south end of the old summit, old Lock 15 and a new junction lock at the south edge of the village. The feeder was later given up for boats; the American Canal Society calls the old canal through the village dry, its water now running north in the old bed to Smith\'s Basin.',
  'OpenStreetMap maps the lock on Canal Street with a dry dock and a waste weir beside it (the guidebook says Fort Edward had one dry dock). A Lake Champlain Maritime Museum crew walked to an abandoned lock here, with a stream running down its middle and an intact towpath on one side, then followed the old canal down Canal Street and found two more crumbling locks past the railroad; the post is undated and does not name the lock, so that it is this one is not confirmed. The museum\'s archaeologists later surveyed canal walls, a stone arch, a series of locks and an abandoned barge in the village.',
  '',
  'Who owns the lock was not checked; the American Canal Society says the feeder canal remains in state ownership. Look from Canal Street; no parking lot was confirmed on the aerial, so park on a village street where it is allowed. Not a park: no hours or rules were found for it.',
  [FEED,ACS,L('Lake Champlain Maritime Museum: Exploration in Fort Edward','https://www.lcmm.org/exploration-in-fort-edward/'),
   L('Lake Champlain Maritime Museum: MRI in Fort Edward','https://lcmm.org/mri-in-fort-edward'),GUIDE,W('Champlain Canal')],conf='mixed'),
N('fort-edward-junction-lock','Fort Edward junction lock and the towpath arch','Fort Edward','wash','canal','ruins',43.26407,-73.58012,'exact','view','walk','canal','1830 arch; lock abandoned 1940s',
  'After the Barge Canal opened, this concrete lock joined the old canal and the Glens Falls Feeder to the new Champlain Canal just above its Lock 7. It was abandoned in the 1940s. Where the lock meets Bond Creek a dry-stacked stone arch carries the old towpath over the creek; records cited in a 2023 study date the arch to 1830, as part of the first Champlain Canal; a visitor\'s note on Komoot gives 1869 for the arch, so the date is not settled.',
  'The 2023 study found the concrete lock walls about 8 feet tall and in good condition, 19 feet apart at the south end and 42 to 50 feet apart where they meet Bond Creek, with steel tie-off straps and valve doors still in place, and old curbstone, slabs and pipe dumped inside. South of the creek the ground is mowed; north of it the space between the walls is heavily overgrown. The stone arch about 400 feet north of Argyle Street was in poor condition, with failed stones in an abutment, missing and displaced stones and bulging wingwalls. The American Canal Society lists a single-span aqueduct, its floor gone, just north of the lock.',
  '',
  'The corridor from Argyle Street (Route 197) to the end of Canal Street is owned by the Village of Fort Edward, which was studying a trail through it in 2023; whether one has been built was not checked. A 2022 assessment called the stone arch unsafe for public access: stay off it and look from the ends. The study describes a gravel parking area on Argyle Street about 175 feet east of Broadway (US 4).',
  [FEJL,FEED,ACS,L('Komoot: Old Champlain Canal Junction Lock','https://www.komoot.com/highlight/6428997')],conf='mixed'),
N('fort-ann-old-canal-locks','Old Champlain Canal Locks 16, 17 and 18, Fort Ann','Fort Ann','wash','canal','ruins',43.41326,-73.48662,'exact','public','walk','canal','about 1857 (locks 16 and 17)',
  'At Fort Ann the old Champlain Canal came off its summit level: combined Locks 16 and 17 dropped boats from the summit toward Lake Champlain, and Lock 18 (Brigg\'s) lowered the canal into Halfway Creek, which soon joined Wood Creek. A Lakes to Locks Passage marker dates Locks 16 and 17 to about 1857. The canal made Fort Ann an inland port when it opened in 1823, and was later replaced by the Barge Canal.',
  'The American Canal Society lists all three locks as intact (table revised 2011); TrailLink calls them well preserved with their original stonework, and the Empire State Trail\'s gallery shows the trail running through a lock. The Old Stone House Library on George Street (US 4), built about 1825, is one of the few buildings left from the years the canal was dug.',
  '',
  'On the Champlain Canalway Trail, a public walking and cycling trail that the state lists as part of the Empire State Trail; it follows the old towpath from Baldwin Corners Road to the village. The trail\'s north end is at the locks, at South Canal Street and Ann Street; just east on Ann Street, before the bridge, a trailhead has parking, a map kiosk, a picnic shelter and a small dock. The guidebook says the towpath is kept as a snowmobile trail in winter under a Canal Corporation permit. No hours were found on the trail pages.',
  [L('TrailLink: Champlain Canalway Trail, Fort Ann','https://www.traillink.com/trail/champlain-canalway-trail-fort-ann'),
   L('HMdb: Lakes to Locks Passage, Fort Ann','https://www.hmdb.org/m.asp?m=147600'),ACS,EST,GUIDE,
   L('HMdb: Old Stone House Library','https://www.hmdb.org/m.asp?m=89708')],
  th=[43.41434,-73.48539],thn='Fort Ann trailhead and dock lot, Ann Street'),
N('moses-kill-aqueduct','Moses Kill aqueduct and trolley arch','Fort Edward','wash','canal','ruins',43.20312,-73.57902,'site','boat','boat','canal','',
  'The old Champlain Canal crossed the Moses Kill south of Fort Edward on an aqueduct of two spans, about 74 feet long; the canal boats rode in a wooden trough with a towpath beside it. The 2019 canal guidebook calls it still relatively intact. Just upstream a concrete arch carried the Hudson Valley electric trolley over the creek; a local paddler writes that it was built around 1900 and believes it stopped running after the 1927 flood.',
  'The American Canal Society lists the pier and abutments as intact and numbers it Aqueduct 3; the paddler calls it Aqueduct 4 and describes cut limestone piers, then the trolley arch a short paddle upstream. Old Lock 14, which lifted boats toward the Fort Edward level, is listed as intact on private property nearby.',
  '',
  'Seen from the water. The paddler launches from West River Road (County Route 29) in Northumberland, on Canal Corporation land, crosses the Hudson and enters the creek under the Route 4 bridge; he warns of a dangerous dam downstream (stay well above the line of buoys) and of motorboats at the Barge Canal entrance, and says the old put-in on the creek\'s north bank is overgrown. The banks along the creek, including the lock, are treated here as private: stay in the boat.',
  [ACS,L('Wash Wild blog (2021): the Moses Kill by canoe','https://wcny.blogspot.com/2021/09'),GUIDE,GHOST],conf='mixed'),
# ---- Piers left in the Hudson ----
N('saratoga-whitehall-railroad-piers','Saratoga and Whitehall Railroad piers, Hudson Falls','Hudson Falls','wash','rail','traces',43.30246,-73.59038,'exact','view','drive','','1837–',
  'Large stone piers stand in the Hudson above Baker\'s Falls, put there in 1837 for a bridge of the Saratoga and Whitehall Railroad that was never finished. The town\'s marker says work stopped in the panic of 1838; the canal guidebook says the panic of 1837, after arguments among the directors over where to cross, and that the bridge would have been 80 feet high. The railroad reached Whitehall in 1848. The only use ever made of the piers, the marker says, was to carry the Hudson Falls fire department\'s alarm lines, until the mid-1970s.',
  'A line of piers across the river, seen on the aerial. The Town of Kingsbury\'s 1999 marker stands on Route 254 by the river.',
  '',
  'In the river; look from Route 254 at the marker on the east bank. The banks were not checked for public access.',
  [L('HMdb: Railway Bridge Piers','https://www.hmdb.org/m.asp?m=129541'),GUIDE],conf='mixed'),
N('hudson-crossing-bridge-piers','Trolley and railroad bridge piers at Hudson Crossing','Thomson','wash','rail','traces',43.11689,-73.57558,'area','view','walk','','1890s–1920s',
  'Two lines of piers cross the Hudson between the Northumberland Dam and the Dix Bridge. Hudson Crossing Park says the Greenwich and Schuylerville Electric Railroad was formed in 1895 and built a trolley bridge here, powered from a dam on the Battenkill at Middle Falls; the line passed to the Hudson Valley Railway, which ran from Greenwich to Thomson until 1928. A Washington County blogger dates the laid-stone trolley piers downstream to a line abandoned in 1909, and the concrete piers just upstream to a Greenwich and Johnsonville Railway bridge first used on August 5, 1903, later shared by steam trains and trolleys; another rail historian dates that bridge to 1901. The dates do not agree.',
  'Cut-stone and concrete piers in the river, seen from the Dix Bridge, an old road bridge now for walkers and bikes; the guidebook says the trolley bridge was 900 feet long. A hiker in 2015 found trolley abutments, ties and paper mill foundations on the Thomson shore; that ground was not checked and is not part of this entry.',
  '',
  'Hudson Crossing Park, on the island made by Champlain Canal Lock 5: open every day of the year from dawn to dusk, free. Park at its lot off County Route 42 and walk to the Dix Bridge.',
  [L('Hudson Crossing Park: Hudson Valley Railway wayside','https://www.hudsoncrossingpark.org/virtual-heritage-wayside-hudson-valley-railway'),
   L('Hudson Crossing Park','https://www.hudsoncrossingpark.org/'),GHOST,
   L('Rich\'s PedalPoint (2015): Thomson pulp and paper mill ruins','https://rc-pedalpoint.blogspot.com/2015/11/thomson-pulp-and-paper-mill-ruins-part.html?m=1'),
   L('Rich\'s PedalPoint (2015): abandoned railroad and trolley bridges, Schuylerville','https://rc-pedalpoint.blogspot.com/2015/11/abandoned-railroad-and-trolley-bridges.html'),GUIDE],conf='mixed',
  th=[43.11448,-73.57741],thn='Hudson Crossing Park lot, County Route 42'),
# ---- Lake George: the Knapp estate ----
N('knapp-estate-shelving-rock','Knapp estate ruins, Shelving Rock','Fort Ann','adk','inst','ruins',43.55347,-73.60228,'area','public','hike','burned','1902–1917',
  'George Owen Knapp, a founder of Union Carbide, built an estate at Shelving Rock on the east shore of Lake George in 1902, with a private powerhouse using the water of Shelving Rock Falls. His mansion burned in 1917. The family built carriage roads across the land, now hiking trails, with a gazebo on Shelving Rock Mountain. The land passed to the state around 1941: one writer says Knapp sold it 3,200 acres that year, another that the state had 4,300 acres of the estate by then.',
  'A hiker in 2014 saw the ruins of the gardens beside the falls, on the carriage road rather than the falls path. Where the house stood and what else remains was not checked: the pin is the falls.',
  'A millionaire\'s Lake George estate, burned and given back to the woods.',
  'Lake George Wild Forest, Shelving Rock Area (NYS DEC): open year-round, free; a day use area runs along Shelving Rock Brook to the bay. From the unpaved lot up the hill past the brook crossing on Shelving Rock Road, walk back about 0.1 mile to the trail; the top of the falls is 0.3 mile in. A 2009 writer found private land and posted signs on the drive in and private houses on the point: keep to the state land and marked trails. DEC Region 5 office (518) 623-1200.',
  [L('NYS DEC: Lake George Wild Forest','https://dec.ny.gov/places/lake-george-wild-forest'),
   L('Northern New York Waterfalls: Shelving Rock Falls','https://nnywaterfalls.com/shelvingrockbrook/shelvingrockfalls/'),
   L('Shelving Rock Falls, a short hike (blog, 2014)','https://nsantasierphoto.wordpress.com/2014/07/06/shelving-rock-falls-a-short-hike-with-lots-of-water/'),
   L('Adirondack Explorer: Three great little peaks','https://www.adirondackexplorer.org/recreation/three-great-little-peaks/'),
   L('Terry Olmsted: Shelving Rock (2009)','https://sites.google.com/site/terryolmsted/index-5/chapter-220'),
   L('Crazy as a Loom (2011): Shelving Rock','https://crazyasaloom.blogspot.com/2011/08/did-i-say-simple.html'),W('George Owen Knapp')],conf='mixed'),
# ---- Whitehall ----
N('uss-ticonderoga-hull-whitehall','Hull of USS Ticonderoga and the old canal walls, Whitehall','Whitehall','wash','water','ruins',43.55357,-73.40259,'site','view','walk','canal','1814–',
  'Ticonderoga was built at Vergennes, Vermont, in 1814 as a merchant steamer, bought by the Navy, made a schooner and fought in the Battle of Plattsburgh that September. She was laid up at Whitehall after the war and sold in 1825 as not worth repairing. The wreck was found again in 1958; Wikipedia says it was raised the next year, the 1958 marker beside it says raised in 1958. Whitehall was the north end of the Champlain Canal, where lake boats and canal boats traded cargo; its last three old locks lie buried in the street west of the modern Lock 12.',
  'The wooden remains of the hull are on display outside the Skenesborough Museum. The canal marker at Main and Division streets points walkers along the towpath past the stone walls of the original canal to the visitor center.',
  'A War of 1812 warship\'s bones beside the canal she outlived.',
  'Outdoors on the waterfront by the Skenesborough Museum on Skenesborough Drive, with a lot beside it; who owns the ground and the display was not checked. The museum\'s hours were not checked either: its web site shows only history notes.',
  [W('USS Ticonderoga (1814)'),L('HMdb: U.S.S. Ticonderoga','https://www.hmdb.org/m.asp?m=89671'),
   L('HMdb: Traveling Along the Canal','https://www.hmdb.org/m.asp?m=89796'),ACS,GUIDE],conf='mixed',
  th=[43.55401,-73.40260],thn='Skenesborough Drive lot'),
N('skene-manor-whitehall','Skene Manor','Whitehall','wash','landmark','standing',43.55586,-73.39920,'exact','public','drive','','1874–',
  'A Victorian mansion of grey sandstone quarried on its own hillside, built in 1874-75 (Wikipedia says 1874) for New York Supreme Court Judge Joseph H. Potter and first called Mountain Terrace. It was renamed in 1946 for Philip Skene, who founded the town as Skenesborough in 1759. It was a restaurant for a time; a local nonprofit, Whitehall Skene Manor Preservation, now owns it, restores it and opens it for tours.',
  'Two towers, a mansard roof and three bracketed porches; the clock that was in the centre tower has been removed. A Lakes to Locks marker says the manor looks down on the northernmost lock of the Champlain Canal.',
  '',
  'Owned and run by Whitehall Skene Manor Preservation, Inc., 8 Potters Terrace. On November 17, 2026 its web site said it was closed and would reopen in May 2027; it gives no weekly hours. Off season, look from the street.',
  [W('Skene Manor'),L('Skene Manor','https://www.skenemanor.org/'),GUIDE,L('HMdb: Lakes to Locks Passage, Fort Ann','https://www.hmdb.org/m.asp?m=147600')]),
# ---- Standing places ----
N('old-fort-house-fort-edward','Old Fort House','Fort Edward','wash','fort','standing',43.26171,-73.58075,'exact','public','drive','forts','1772–',
  'One of the oldest wooden frame buildings in northern New York, built in 1772 by Patrick Smyth from timbers salvaged from Fort Edward. In 1777 both the British and the Americans used it as headquarters; Baroness Riedesel called it the Red House. Solomon and Anne Northup set up their first home here in the early 1830s.',
  'A two-story, five-bay frame house with a shallow gambrel roof, now the museum of the Fort Edward Historical Association.',
  '',
  'Old Fort House Museum, 29 Lower Broadway, owned by the Fort Edward Historical Association. Its site gives tours from 1 to 4 PM daily from June to October, Christmas tours on weekends in December, and the office open on weekdays all year, (518) 747-9600.',
  [W('Old Fort House (Fort Edward, New York)'),L('Old Fort House Museum','https://www.oldforthousemuseum.com/'),GUIDE]),
N('shushan-covered-bridge','Shushan Covered Bridge','Shushan','wash','landmark','standing',43.09128,-73.34554,'exact','view','drive','','1858–',
  'A covered bridge over the Batten Kill built in 1858 by Milton Stevens on the patented Town lattice truss. It was closed to traffic in 1962 and left abandoned for ten years before local people saved it; it is one of four old covered bridges left in Washington County.',
  'The wooden lattice bridge, now a seasonal museum.',
  '',
  'Run as a seasonal museum (Wikipedia); who runs it and its hours were not checked. Look from the roads at either end when it is shut.',
  [W('Shushan Bridge')]),
]
PIN_NOTES={
 'old-champlain-lock-15-fort-edward':'OpenStreetMap\'s "Old Champlain Canal Lock 15" ruins on Canal Street (tools/nom.py), which matches the American Canal Society\'s GPS position to within a few metres. The leaf-off aerial shows only trees and a dark channel in the ring; the LiDAR shows the walled lock chamber running through the pin. The Canal Street lot that tools/parking.py lists could not be told from the street on the aerial, so no parking point is given.',
 'fort-edward-junction-lock':'OpenStreetMap\'s "Old Champlain Canal Junction Lock" ruins; the American Canal Society gives 43.26335, -73.57955, about 70 m south-east. Trees on the aerial; the LiDAR shows the long straight lock walls running north-west through the pin, east of Broadway.',
 'fort-ann-old-canal-locks':'OpenStreetMap\'s "Old Champlain Canal Locks 16-17" ruins on South Canal Street; Lock 18 is mapped about 140 m north (43.41454, -73.48612). The aerial and the LiDAR both show the narrow chamber in the ring between South Canal Street and the railroad. The trailhead tile shows a gravel lot by the canal at the Ann Street bridge.',
 'moses-kill-aqueduct':'The American Canal Society\'s GPS position for the Moses Kill aqueduct. The aerial shows the creek in the ring under bare trees; the LiDAR shows the old canal\'s banks curving down to the creek on both sides and a block at the crossing, which fits the abutments. The piers themselves were not picked out.',
 'saratoga-whitehall-railroad-piers':'Read off the aerial with tools/look.py and tools/pix.py: the middle pier of a line of six piers crossing the river west of the HMdb marker on Route 254 (43.30208, -73.58813). The pin check shows the pier in the ring and its neighbours on the same line.',
 'hudson-crossing-bridge-piers':'The Dix Bridge, read off the aerial with tools/look.py and tools/pix.py (OpenStreetMap maps it there too); the pin check shows the bridge across the ring. The piers stand in the river upstream, between the bridge and the Northumberland Dam, and were not picked out on the aerial. The trailhead tile shows the park\'s gravel lot.',
 'knapp-estate-shelving-rock':'OpenStreetMap\'s Shelving Rock Falls (tools/nom.py); a waterfall site gives 43.55306, -73.60250. Conifers on the aerial; the LiDAR shows the brook\'s ravine. No source places the house or garden ruins exactly. OpenStreetMap maps nine numbered lots on Shelving Rock Road, but none could be seen under the trees, so no parking point is given.',
 'uss-ticonderoga-hull-whitehall':'OpenStreetMap\'s Skenesborough Museum point (tools/nom.py), on the red-roofed museum building beside the canal on the aerial; the HMdb Ticonderoga marker is about 95 m south (43.55272, -73.40277). The hull itself was not picked out. The trailhead tile shows a paved lot north of the museum.',
 'skene-manor-whitehall':'OpenStreetMap\'s Skene Manor building (tools/nom.py); the pin check shows the mansion on its wooded hillside with the drive below.',
 'old-fort-house-fort-edward':'Moved 67 m north from Wikipedia\'s coordinate (43.26111, -73.58083, on trees beside Broadway) onto the house the ArcGIS geocoder gives for the Old Fort House Museum and for 29 Broadway (43.26170, -73.58084), read off the aerial with tools/look.py and tools/pix.py.',
 'shushan-covered-bridge':'OpenStreetMap\'s Shushan Covered Bridge (tools/nom.py); the pin check shows the covered span over the Batten Kill.',
}
