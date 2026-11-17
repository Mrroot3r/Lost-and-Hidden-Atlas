# November 17, 2026: Washington County, New York, more. Added on top of the "washco" batch (pull request 48), which a
# second session researched at the same time: these are the six places that session did not add. The Feeder Canal at
# Hudson Falls and Glens Falls (Lock 12 and the Kenyon Lumber site, the Martindale boat basin, the 1906 coal silos, the
# lime-kiln ruins), the old canal and trolley bed in the Denton Sanctuary, and the Eagleville covered bridge.
# Facts come from the linked sources only. The American Canal Society's index of Champlain Canal structures (revised
# 2011, a 4-page PDF) and the 2023 Fort Edward junction-lock feasibility study were read as text from their PDFs
# (tools/page.py); HMdb marker pages were fetched whole and their inscriptions read; Wikipedia as raw text
# (tools/wiki_raw.py); The Nature Conservancy, the Empire State Trail, Washington County tourism (washingtoncounty.fun),
# Skene Manor and the bikeitorhikeit.org trail guide through tools/page.py; feedercanal.org's walking tour through the web
# fetch tool, which answered set questions about it. Where sources disagree the text gives both; where a source is
# silent it says "not checked". Nothing was checked on the ground.
# Pins: an OpenStreetMap feature (tools/nom.py), an HMdb marker position, the canal index's GPS figure, or a spot read off
# the state leaf-off aerial and LiDAR, as each pin note says. Every pin was looked at with tools/pincheck.py --lidar.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'washco2','label':'Washington County, more: the Feeder Canal, the Denton Sanctuary canal and Eagleville bridge','added':'2026-11-17 17:47'}
ACS=L('American Canal Society: Champlain Canal structures index (PDF, rev. 2011)','https://americancanalsociety.org/wp-content/uploads/2019/08/Champlain-Canal2.pdf')
BIKE=L('Bike It or Hike It: Champlain Canalway Trail and Feeder Canal Trail','https://bikeitorhikeit.org/champlain_canalway_trail_fort_edward_fort_ann_whitehall.htm')
EST=L('Empire State Trail: Fort Edward to Fort Ann','https://empiretrail.ny.gov/albany-whitehall/fort-edward-fort-ann')
JLOCK=L('A/GFTC: Old Fort Edward Junction Locks Trail Extension study (PDF, Nov. 2023)','https://public.warrencountyny.gov/gis/PlanLibrary/2023%20Old%20Fort%20Edward%20Junction%20Locks%20Trail%20Extension.pdf')
FCA=L('Feeder Canal Alliance: walking tour','https://feedercanal.org/?p=435')
CANALS=L('Washington County tourism: canals of Washington County','https://washingtoncounty.fun/canals-of-washington-county/')
PLACES=[
N('denton-sanctuary-canal','Old Champlain Canal and trolley bed, Denton Sanctuary','Greenwich','wash','canal','traces',43.13678,-73.58397,'site','public','walk','canal','1822–1917',
  'The Nature Conservancy\'s 350-acre Denton Sanctuary lies on the east bank of the Hudson north of Schuylerville, on a strip that carried the old Champlain Canal and later an electric trolley. The canal here opened in 1822 and was given up when the present canal opened in 1917. The Conservancy calls the trolley the Greenwich-Schuylerville line; a Lakes to Locks Passage page says it ran from Troy to Lake George. Shale was dug on the land into the 1970s.',
  'From the Route 4 entrance the path crosses the old canal bed, filling in with plants, between the road and an old shale pit; the Yellow loop follows the old trolley bed for part of its 1.4 miles. The Conservancy says granite blocks that lined one of the old locks can be seen from the road about 0.7 mile north of the entrance, on the right going north; the canal index lists Bassett\'s Lock (No. 12) beside Route 4 near there. What is left of the lock was not checked.',
  'A canal bed and a trolley bed side by side in the woods above the Hudson.',
  'A Nature Conservancy preserve, open dawn to dusk all year; park on the side of Route 4 at the entrance (about five spaces, no facilities). No camping, fires or collecting; the Conservancy runs a hunting program by written permission and keeps the preserve open in the fall hunting season. Trails are narrow, up to 3 feet wide, with short steep pitches. The pin, on the canal bed, falls just outside the preserve outline in the federal protected-areas map while the parking point falls inside it; the strip along Route 4 was not checked against a parcel map (Washington County is not in the state parcel file).',
  [L('The Nature Conservancy: Denton Sanctuary','https://www.nature.org/en-us/get-involved/how-to-help/places-we-protect/denton-sanctuary/'),
   L('Lakes to Locks Passage: Denton Wildlife Sanctuary','https://passageport.org/?p=4687'),ACS],conf='mixed',th=[43.13675,-73.58445],thn='Denton Sanctuary parking, Route 4 shoulder'),
N('feeder-lock-12-kenyon','Feeder Canal Lock 12 and the Kenyon Lumber site','Hudson Falls','wash','canal','ruins',43.30009,-73.572,'site','public','walk','canal','1852–1926',
  'The Glens Falls Feeder Canal, dug from 1824 to keep the summit of the Champlain Canal in water, drops through thirteen masonry locks east of Hudson Falls. Kenyon Lumber was built beside Lock 12 in 1852 and at its peak had over 100 workers; log rafts a quarter mile long were floated down the canal from the feeder dam to the mill. Griffin Lumber, at Lock 13 on Pearl Street, bought it in 1926, moved the plant across the street and used the old site for storage.',
  'The walking tour passes Locks 12 and 11 before the Burgoyne Avenue bridge; OpenStreetMap maps Lock 12 as a ruin. What is left of the lock and of the mill site was not checked.',
  '',
  'On the Feeder Canal trail; the canal is maintained by the New York State Canal Corporation and the trail by the Feeder Canal Alliance with the towns. Parking at Feeder Canal Park on Burgoyne Avenue. Hours not checked.',
  [L('HMdb: Kenyon Lumber','https://www.hmdb.org/m.asp?m=131747'),FCA,BIKE,W('Glens Falls Feeder Canal')],conf='mixed',th=[43.29782,-73.56971],thn='Feeder Canal Park, Burgoyne Avenue'),
N('feeder-coal-silos','Feeder Canal coal silos','Hudson Falls','wash','industry','standing',43.30215,-73.57688,'site','view','walk','canal','1906',
  'Griffin Lumber built these silos beside the Feeder Canal in the fall of 1906, each holding a different grade of coal. They are made of cement blocks that, by the marker, Griffin Lumber itself invented.',
  'The silos beside the canal, seen from the trail just east of Maple Street. Their state was not checked.',
  '',
  'On Maple Street (Route 196) at the Feeder Canal, across from the highway department; the trail guide says to look for them from the towpath after crossing Maple Street. Who owns them was not checked: look from the trail.',
  [L('HMdb: Coal Silos','https://www.hmdb.org/m.asp?m=131688'),BIKE],conf='mixed'),
N('martindale-boat-basin','Martindale Boat Basin','Hudson Falls','wash','canal','traces',43.30607,-73.58086,'site','public','walk','canal','1824–1928',
  'One of six basins on the Feeder Canal where boats, about 90 by 14 feet, could pull over to pass or turn, and where cargo was loaded from wagons. The stone-lined basin was 200 feet wide and held six boats. The last boat passed in 1928; the Martindale Avenue bridge was then lowered and its limestone blocks pushed into the basin. They were pulled out in 1990 and now form a three-tier wall down to a boat dock.',
  'The stone embankments of the basin, the reset bridge blocks and interpretive signs, in a small park with picnic tables.',
  '',
  'A pocket park on the Feeder Canal trail with water access for small boats; parking from Martindale Avenue. Owner and hours not checked.',
  [L('HMdb: Martindale Boat Basin','https://www.hmdb.org/m.asp?m=131746'),L('Washington County tourism: Martindale Boat Basin Park','https://washingtoncounty.fun/directory/martindale-boat-basin-park/'),FCA]),
N('feeder-lime-kilns','Lime kiln ruins on the Feeder Canal','Glens Falls','wash','industry','ruins',43.30796,-73.62628,'area','public','walk','canal','1832–',
  'Lime was burned at Glens Falls from 1820, and the Feeder Canal let it be shipped to Albany and New York. The Sherman Lime Company kilns here began in 1832; once there were more than 83 kilns along the canal, fired with scrap wood from the sawmills, each holding 250 to 300 barrels. Jointa Lime, nearby, dates back almost to the canal\'s beginning.',
  'East of the Shermantown Road bridge the walking tour points out the stonework and ruins of a series of kilns beside the towpath. How much stands was not checked.',
  'Ruins of a lime-burning row that once had more than eighty kilns.',
  'On the Feeder Canal trail (Canal Corporation canal); the pin falls on a state-owned parcel in the state tax-parcel file; the Feeder Canal Alliance says cars may be parked on Shermantown Road, off Warren Street (Route 32), where there is also a canoe dock. Industry still works along this stretch of canal: keep to the towpath.',
  [L('HMdb: Lime Kiln Site','https://www.hmdb.org/m.asp?m=185976'),FCA,L('Feeder Canal Alliance: paddling the canal','https://feedercanal.org/?p=431'),BIKE,W('Glens Falls Feeder Canal')],conf='mixed'),
N('eagleville-covered-bridge','Eagleville Covered Bridge','Salem','wash','landmark','standing',43.08324,-73.31371,'exact','public','drive','','1858',
  'A Town lattice truss covered bridge over the Batten Kill, built in 1858 by local builder Ephraim Clapp. A flood damaged it in 1977; it was stabilized and put back into use for cars. It is one of four covered bridges left in Washington County.',
  'The bridge on Eagleville Road. Whether it still carries cars was not checked.',
  '',
  'On Eagleville Road, a public road, on the line between the towns of Jackson and Salem. Watch for traffic.',
  [W('Eagleville Bridge')]),
]
PIN_NOTES={
 'denton-sanctuary-canal':'Moved 39 m east of the mapped parking area (the trailhead point) onto the old canal bed, which shows on the state LiDAR as a channel running beside Route 4; under trees on the leaf-off aerial.',
 'feeder-lock-12-kenyon':'OpenStreetMap ruin "Glens Falls Feeder Canal Lock #12"; the Kenyon marker is about 30 m east.',
 'feeder-coal-silos':'HMdb position of the Coal Silos marker on Maple Street.',
 'martindale-boat-basin':'Moved 25 m from the OpenStreetMap park point (which fell on a building) to the canal edge beside the Martindale Avenue bridge; the basin walls are not clear on the aerial.',
 'feeder-lime-kilns':'HMdb position of the Lime Kiln Site marker, which falls on the Shermantown Road bridge over the canal; the walking tour puts the kiln ruins beside the towpath east of the bridge. They were not picked out on the aerial, hence area.',
 'eagleville-covered-bridge':'OpenStreetMap bridge "Eagleville Covered Bridge".',
}
