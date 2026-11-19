# November 17, 2026: Washington County, New York (region "Upper Hudson & Washington Co."), a first close pass.
# Mostly the stone of the old Champlain Canal, which the 1915 Barge Canal left beside it: the junction lock and
# Lock 15 at Fort Edward, Lock 13 and the Moses Kill aqueduct near Fort Miller, the combined locks at Fort Ann and
# the original canal walls at Whitehall; the unfinished 1837 railroad piers in the Hudson at Hudson Falls; and the
# best of what stands: the Old Fort House, the Old Stone House Library at Fort Ann, Skene Manor, and two of the
# county's covered bridges over the Batten Kill.
# Facts come from the linked sources only. The American Canal Society's Champlain Canal index (revised 2011, with a
# condition note and a coordinate for each old lock) was read as text from its PDF; so was the 2023 Old Fort Edward
# Junction Locks Trail Extension feasibility report (Barton & Loguidice for the A/GFTC and the village). Wikipedia
# articles through tools/wiki_raw.py; HMdb marker pages, the village, museum and trail pages through tools/page.py;
# the TrailLink page only as a
# web-search excerpt (it says where the Fort Ann trail ends). Where sources disagree the text gives both; where a source is silent it says "not checked".
# Pins: the canal society's coordinate, an OpenStreetMap feature (the leads layer), an HMdb marker position or a
# Wikipedia coordinate, as each pin note says; every pin was looked at with tools/pincheck.py --lidar.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'washco','label':'Washington County, New York: old Champlain Canal locks and covered bridges','added':'2026-11-17 17:38'}
ACS=L('American Canal Society: Champlain Canal index and structures (PDF, revised 2011)','https://americancanalsociety.org/wp-content/uploads/2019/08/Champlain-Canal2.pdf')
FEJ=L('Old Fort Edward Junction Locks Trail Extension, final feasibility report (A/GFTC, November 2023, PDF)','https://public.warrencountyny.gov/gis/PlanLibrary/2023%20Old%20Fort%20Edward%20Junction%20Locks%20Trail%20Extension.pdf')
BIKE=L('Bike It or Hike It: Champlain Canalway Trail, Fort Edward to Whitehall (trail write-up, 2025)','https://bikeitorhikeit.org/champlain_canalway_trail_fort_edward_fort_ann_whitehall.htm')
TLFA=L('TrailLink: Champlain Canalway Trail, Fort Ann','https://www.traillink.com/trail/champlain-canalway-trail-fort-ann')
MULLEN=L('Village of Fort Edward: Mullen Park','https://villageoffortedward.gov/attractions/mullenpark')
WCF=L('Washington County tourism: Fort Miller listings (Old Canal Lock 13 Heritage Site)','https://washingtoncounty.fun/single-location/fort-miller')
PLACES=[
# ---- Fort Edward ----
N('fort-edward-junction-lock','Old Fort Edward junction lock and towpath arch','Fort Edward','wash','canal','ruins',43.26335,-73.57955,'site','view','walk','canal','',
  'A concrete lock that joined the Champlain Canal to the Glens Falls Feeder Canal at Fort Edward. A 2023 trail study for the village describes walls about 8 feet tall and in good condition, 19 feet apart at the south end and 42 to 50 feet apart where the structure meets Bond Creek, with some steel tie-off straps and valve doors still in place. A dry-stacked stone arch carries the old towpath over Bond Creek about 400 feet north of Argyle Street; the study says record documents date it to 1830. The canal society\'s 2011 list calls the lock half buried.',
  'The concrete lock walls running north from Argyle Street to the south end of Canal Street, mowed at the Bond Creek end and overgrown beyond it, with dumped curb stones and rubble inside. The stone arch over Bond Creek, with retaining walls along the creek; one has fallen in. Not checked on the ground.',
  '',
  'The corridor from Argyle Street (Route 197) to Canal Street is owned by the Village of Fort Edward (2023 study). The study names a gravel parking area on Argyle Street just east of Broadway and a path from it up onto the old towpath, but it is a study for a future trail, not a trail that is open, so this entry is look-from-the-street. The study quotes a 2022 structural check calling the stone arch "unsafe for public access": do not stand on it. Hours not checked.',
  [FEJ,ACS],conf=''),
N('old-champlain-lock-15-fort-edward','Old Champlain Canal Lock 15 and dry dock','Fort Edward','wash','canal','ruins',43.27070,-73.58378,'site','view','walk','canal','about 1862–1918',
  'Lock 15 of the old Champlain Canal at Fort Edward, at the south end of the canal\'s summit level (canal society list). A trail write-up says it was built around 1862 for the enlarged canal, that this stretch was kept after the canal closed in 1918 to reach the Glens Falls Feeder Canal, and that a large dry dock from the first canal of 1822 lies beside the lock, next to the mouth of the old Fort Edward feeder. The same writer says the site is wooded and overgrown and that he had not been in to look.',
  'Remains of the lock and dry dock in woods beside Mullen Park. Not confirmed: neither source describes what is left, and the trail writer had not checked it.',
  '',
  'Beside Mullen Park (formerly McIntyre Park), a Village of Fort Edward park, through which the paved Champlain Canalway Trail runs; the trail write-up gives a small parking area and trailhead at the end of Wing Street, off East Street. Whether the lock itself is on village land was not checked, so treat it as look-only from the trail and the park. Hours not checked.',
  [BIKE,ACS,MULLEN],conf='mixed',th=[43.26977,-73.58069],thn='Wing Street trailhead (Mullen Park)'),
N('old-fort-house-fort-edward','Old Fort House','Fort Edward','wash','landmark','standing',43.26111,-73.58083,'site','open','drive','forts','1772–',
  'One of the oldest wooden frame buildings in northern New York, built in 1772 by Patrick Smyth from timbers salvaged from Fort Edward. Both armies used it as a headquarters during the Revolution, and Baroness Riedesel called it "the Red House" in her memoirs. Solomon and Anne Northup first kept house here in the early 1830s. Twelve local businessmen bought it in 1949, and it opened to the public as a museum on July 12, 1953.',
  'The two-storey gambrel-roofed house on Lower Broadway, the centre of a museum campus that the Fort Edward Historical Association runs, with an 1840 toll keeper\'s house, the Riverside School House and the 1853 A. Dallas Wait law office among its buildings.',
  '',
  'Owned by the Fort Edward Historical Association and open as a museum, 29 Broadway. Its spring 2024 newsletter gave tours from 1 pm daily from June 1 to July 31 and an adult fee of $10; the town\'s page gives 1 to 5 pm with the last tour at 4. The 2026 season was not checked. Lakes to Locks Passage says the campus is open all year by appointment for school and coach tours (518-747-9600).',
  [W('Old Fort House (Fort Edward, New York)'),L('Old Fort House Museum: spring 2024 newsletter (PDF)','https://www.oldforthousemuseum.com/wp-content/uploads/2024/06/Newsletter-2024-Spring.pdf'),L('Town of Fort Edward: Old Fort House Museum','https://fortedward.net/organizations/museums'),L('Lakes to Locks Passage: Old Fort House Museum campus','https://passageport.org/?p=4583')]),
# ---- Fort Miller and the Moses Kill ----
N('old-champlain-lock-13-fort-miller','Old Champlain Canal Lock 13, Fort Miller','Fort Miller','wash','canal','ruins',43.16440,-73.57950,'site','view','walk','canal','',
  'Lock 13 of the old Champlain Canal, at the hamlet of Fort Miller, lifted boats about 9.5 feet on their way north. The American Canal Society\'s 2011 list calls it intact but overgrown. The county tourism office lists it as the Old Canal Lock 13 Heritage Site. Lakes to Locks Passage notes that remnants of the old canal still show along the east side of Route 4 here.',
  'The stone lock in brush beside Route 4. What the heritage site has in the way of signs or a path was not checked.',
  '',
  'Who owns the lock was not checked, so look from the road. Route 4 is a fast highway. The nearest mapped parking is at the modern canal\'s Lock C6 on Lock Road, a quarter mile south, which is lock ground: whether the public may park there was not checked.',
  [ACS,WCF,L('Lakes to Locks Passage: The Hamlet of Fort Miller','https://passageport.org/the-hamlet-of-fort-miller/')],conf='mixed'),
N('moses-kill-aqueduct','Moses Kill aqueduct of the old Champlain Canal','Fort Edward','wash','canal','ruins',43.20312,-73.57902,'site','view','drive','canal','',
  'The old Champlain Canal crossed the Moses Kill on a two-span aqueduct 74 feet long, numbered 3 in the canal society\'s list. The American Canal Society\'s 2011 list says its pier and abutments are intact. The next lock north, Lock 14 at Moses Hill, is on private property, the same list says.',
  'A stone pier and two abutments where the old canal crossed the creek, beside Route 4. Not checked on the ground or in any second source.',
  '',
  'Who owns the ground was not checked: look from the road only. No parking is mapped nearby, and Route 4 is a fast highway. Lock 14, to the south, is on private land.',
  [ACS],conf='mixed'),
# ---- Hudson Falls ----
N('hudson-falls-railroad-piers','Unfinished railroad piers in the Hudson, Hudson Falls','Hudson Falls','wash','rail','ruins',43.30271,-73.58994,'site','view','walk','','1837–',
  'Large stone piers set in the Hudson in 1837 to carry the Saratoga and Whitehall Railroad across the river. The panic of 1838 stopped the work and the bridge was never finished. The Town of Kingsbury\'s 1999 marker says the only use the piers ever had was for the Hudson Falls fire department to string lines for its alarm boxes, until the mid-1970s.',
  'The stone piers in the river below the marker. How many still stand was not checked.',
  '',
  'Seen from the roadside marker on Route 254 in Hudson Falls; the piers are in the river and are not a place to go. Hours do not apply.',
  [L('HMdb: Railway Bridge Piers (Town of Kingsbury marker, 1999)','https://www.hmdb.org/m.asp?m=129541')],conf='mixed'),
# ---- Fort Ann ----
N('fort-ann-locks-16-18','Old Champlain Canal locks 16, 17 and 18, Fort Ann','Fort Ann','wash','canal','ruins',43.41326,-73.48662,'site','public','walk','canal','',
  'At Fort Ann the old Champlain Canal came down off its summit level through Locks 16 and 17, a combined pair, and then Lock 18, which lowered it into Halfway Creek, soon joining Wood Creek. The canal society\'s 2011 list calls all three intact. A Lakes to Locks marker in the village says the canal\'s opening in 1823 made Fort Ann an inland port; the town\'s history marker dates the Fort Edward to Whitehall stretch to 1819. The county lists the locks as a canal heritage site.',
  'The stone chambers of the combined Locks 16 and 17, which the Champlain Canalway Trail passes through on the old towpath just before it reaches Ann Street, and Lock 18 a little north. Signs at the trail end.',
  '',
  'Who owns the towpath was not checked; it is open to the public as the Champlain Canalway Trail (part of the Empire State Trail; TrailLink and the trail write-up), a stone-dust path on the old towpath from Baldwin Corners Road north to Ann Street. The trail write-up puts a parking lot with a gazebo, picnic tables and a map board across Ann Street beside the modern canal (the village docks); the federal land map shows that lot on Champlain Canal land. An active railroad runs beside the trail: stay off it. Hours not checked.',
  [ACS,BIKE,TLFA,L('HMdb: Fort Ann Through History','https://www.hmdb.org/m.asp?m=147599'),L('HMdb: Lakes to Locks Passage marker, Fort Ann','https://www.hmdb.org/m.asp?m=147600')],th=[43.41434,-73.48539],thn='Fort Ann docks lot, Ann Street'),
N('old-stone-house-library-fort-ann','Old Stone House Library','Fort Ann','wash','canal','standing',43.412327,-73.488279,'site','open','drive','canal','about 1825–',
  'A stone house built about 1825, which Wikipedia\'s list of the county\'s Register listings calls one of the few buildings left intact from the years the Champlain Canal was being built. George Knapp gave it to the town as a library in 1922, the town\'s history marker says. It was listed on the National Register in 2013.',
  'The stone house in the village of Fort Ann, near the canal locks.',
  '',
  'A library: the outside can be seen from the street. Opening hours were not checked.',
  [L('Wikipedia: Register listings in Washington County, New York','https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Washington_County,_New_York'),
   L('HMdb: The Old Stone House Library (Pomeroy marker)','https://www.hmdb.org/m.asp?m=89708'),L('HMdb: Fort Ann Through History','https://www.hmdb.org/m.asp?m=147599')]),
# ---- Whitehall ----
N('whitehall-original-canal-walls','Original Champlain Canal walls, Whitehall','Whitehall','wash','canal','traces',43.55588,-73.40173,'area','public','walk','canal','1819–',
  'The Champlain Canal reached Lake Champlain at Whitehall, which grew from a small port into a busy transfer point, with lumberyards, icehouses and shipyards along the waterfront, and stables that wintered hundreds of canal mules. The canal society\'s list says the old canal\'s last three locks, a combined flight that lowered it into the lake, lie buried in the street just west of the modern Lock 12.',
  'The state canal marker at Main and Division Streets tells walkers to follow the towpath past the stone walls of the original canal to the Whitehall Urban Cultural Park visitor centre. The buried locks show nothing.',
  '',
  'In the village of Whitehall, on the towpath along the waterfront, which the state canal marker sends walkers along; who owns it was not checked. There is parking on Skenesborough Drive. Hours do not apply; the visitor centre\'s hours were not checked.',
  [L('HMdb: Traveling Along the Canal (Whitehall)','https://www.hmdb.org/m.asp?m=89796'),L('HMdb: The Champlain Canal (Whitehall)','https://www.hmdb.org/m.asp?m=109349'),ACS],th=[43.55401,-73.40260],thn='Skenesborough Drive lot'),
N('skene-manor','Skene Manor','Whitehall','wash','landmark','standing',43.55583,-73.39944,'exact','public','drive','','1874–',
  'A Victorian mansion of grey sandstone quarried from its own site at Whitehall, built in 1874, with a mansard roof and two towers; the central tower once held a large clock, since removed. It was later a restaurant. It is now open for tours; its website says Whitehall Skene Manor Preservation restored and keeps it. It is on the National Register as the Judge Joseph Potter House.',
  'The stone mansion and its towers on the hill above the village.',
  '',
  'Run by Whitehall Skene Manor Preservation, 8 Potters Terrace. Its site, read on November 17, 2026, said the 2026 season ended on December 12 and the house reopens in May 2027; days and times were not checked.',
  [W('Skene Manor'),L('Skene Manor','https://www.skenemanor.org/')]),
# ---- The Batten Kill ----
N('shushan-covered-bridge','Shushan Covered Bridge','Shushan','wash','landmark','standing',43.09123,-73.34543,'exact','open','drive','','1858–',
  'A two-span Town lattice covered bridge, about 161 feet long, built over the Batten Kill in 1858 by the brothers Milton and James Stevens. The county gave it up as a road bridge in 1962 and it stood in disrepair for more than ten years; a leaking roof nearly brought it down in 1974. The Shushan Covered Bridge Association saved it and made it a museum. It is one of four covered bridges left in Washington County.',
  'The two-span covered bridge beside the County Route 61 road bridge, with the museum\'s displays inside.',
  '',
  'A seasonal museum, free (donations), run by volunteers of the Shushan Covered Bridge Association; the New York State Covered Bridge Society says the bridge is owned and maintained by the town. The Town of Salem\'s page gives hours of 1 to 4 pm: weekends and holidays from Memorial Day to July 4, daily except Monday and Tuesday to Labor Day, weekends and holidays to Columbus Day, and by appointment (518-677-8251). Parking was not checked: the nearest lot OpenStreetMap maps is at a road junction among houses 300 m away.',
  [W('Shushan Bridge'),L('Town of Salem: Shushan Covered Bridge Museum','https://townofsalemny.gov/shushan-covered-bridge-museum/'),
   L('NY State Covered Bridge Society: Shushan','https://www.nycoveredbridges.org/?p=208')]),
N('rexleigh-covered-bridge','Rexleigh Covered Bridge','Jackson','wash','landmark','standing',43.13476,-73.35568,'exact','public','drive','','1874–',
  'A single-span Howe truss covered bridge of 107 feet over the Batten Kill, built in 1874 by Reuben Comins, a Troy man, and George Wadsworth. Its truss joints sit in cast-iron bearing blocks stamped "R. Comins, Troy, N.Y.", and Wikipedia calls it a rare survivor of a prefabricated kind of bridge. The state marker says it is the third bridge on the site and was rehabilitated in 2007.',
  'The covered bridge on Rexleigh Road, still open to traffic.',
  '',
  'Owned and maintained by the county and carrying traffic, the New York State Covered Bridge Society says. Mapped parking at Camp Road by the bridge. The society notes that summer crowds come to swim at the bridge; the river and its banks were not checked for ownership.',
  [W('Rexleigh Bridge'),L('NY State Covered Bridge Society: Rexleigh','https://www.nycoveredbridges.org/?p=204'),L('HMdb: Rexleigh Covered Bridge','https://www.hmdb.org/m.asp?m=58531')],th=[43.13474,-73.35609],thn='Camp Road, by the bridge'),
]
PIN_NOTES={
 'fort-edward-junction-lock':'American Canal Society coordinate for the Fort Edward junction lock (43°15\'48.05"N 73°34\'46.39"W). The LiDAR sheet shows the two parallel lock walls running north-west from the pin; the aerial shows only trees and a building by Broadway inside the ring.',
 'old-champlain-lock-15-fort-edward':'OpenStreetMap feature "Old Champlain Canal Lock 15" (the leads layer); the canal society gives 43°16\'14.68"N 73°35\'01.35"W, about 70 m away. The aerial shows woods; the LiDAR shows a walled channel inside the ring. Which part is the lock and which the dry dock was not worked out.',
 'old-fort-house-fort-edward':'Wikipedia coordinate for the Old Fort House. On the leaf-off aerial it falls among trees on the west side of Broadway, north of a large building and its parking lot; the house itself could not be picked out, so the pin is site, not exact.',
 'old-champlain-lock-13-fort-miller':'American Canal Society coordinate for Lock 13 (43°09\'51.84"N 73°34\'46.21"W); OpenStreetMap maps "Old Champlain Lock 13" about 20 m away. The tile came from Esri satellite with leaves on and shows brush between the canal and an industrial yard; the LiDAR shows a narrow channel along the east bank at the pin but no lock chamber that could be picked out.',
 'moses-kill-aqueduct':'American Canal Society coordinate for the Moses Kill aqueduct (43°12\'11.23"N 73°34\'44.47"W). The leaf-off aerial shows woods over the creek; the LiDAR shows the old canal bank crossing the creek at the pin with a block-shaped mass where the abutment should be.',
 'hudson-falls-railroad-piers':'Moved on November 17, 2026 (washco2 pass) from the HMdb marker position on Route 254 about 150 m west onto the middle one of a row of rectangular stone piers that crosses the Hudson on a slant, read off the aerial with look.py (Esri satellite; the state leaf-off tile was cut by its edge).',
 'fort-ann-locks-16-18':'OpenStreetMap feature "Old Champlain Canal Locks 16-17" (the leads layer); Lock 18 is mapped about 130 m north. The aerial and the LiDAR both show the long lock chamber along the trail inside the ring.',
 'old-stone-house-library-fort-ann':'Coordinate from the Wikipedia list of Register listings in Washington County. The ring is on a building among trees on the village street.',
 'whitehall-original-canal-walls':'HMdb position of the Traveling Along the Canal marker at Main and Division Streets; the walls are along the towpath from there. The pin is on the street by the canal; the LiDAR shows walls along the canal edge north and south of it, but which are the original canal\'s was not worked out, hence area.',
 'skene-manor':'Wikipedia coordinate for Skene Manor. The ring is on the mansion on the hill.',
 'shushan-covered-bridge':'Moved 35 m east from the Wikipedia coordinate, which sat on the road west of the river, onto the covered bridge seen on the leaf-off aerial (tools/pix.py).',
 'rexleigh-covered-bridge':'Wikipedia coordinate for the Rexleigh Bridge. The ring is on the bridge.',
}
