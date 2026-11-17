# November 17, 2026: the country round Syracuse, New York (Onondaga County, with Brewerton and Great Bear just over the
# line in Oswego County). A second pass at Central New York after data_cny.py: the stone aqueducts and lime kilns of the
# old Erie Canal east of the city, Lock 51 and the Jordan Aqueduct to the west, Clinton's Ditch at Camillus, two locks
# of the old Oswego Canal, the earthworks of Fort Brewerton, the mill ruins on the Charlie Major Nature Trail, and one
# vanished trolley park (Long Branch).
# Facts come from the linked sources only. Wikipedia articles were read as raw text (tools/wiki_raw.py); the state parks
# page, the Onondaga County Parks pages (their ?ajax=1 copies, which tools/page.py can read), the Town of Skaneateles,
# Town of Volney, eriecanal.org, HMdb and Pomeroy Foundation marker pages, and the draft Old Erie Canal waterfront plan
# (PDF) through tools/page.py. Where sources disagree the text gives both; where a source is silent it says "not checked".
# Pins: an OpenStreetMap feature (tools/nom.py), a marker position from HMdb or the Pomeroy Foundation, or a Wikipedia
# coordinate, as each pin note says; every pin was looked at on the pin check, aerial and LiDAR
# (research/pincheck_syracuse_*.jpg).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'syracuse','label':'Round Syracuse: canal aqueducts, locks and kilns, Fort Brewerton, Skaneateles Creek mills','added':'2026-11-17 08:27'}
OEC=L('NYS Parks: Old Erie Canal State Historic Park (hours)','https://parks.ny.gov/parks/olderiecanal/details.aspx')
OECMAP=L('NYS Parks: Old Erie Canal trail map 1, DeWitt section (PDF)','https://parks.ny.gov/documents/parks/OldErieCanalTrailMap1-DeWittSection.pdf')
ECO=L('eriecanal.org: traces in Old Erie Canal State Historic Park','https://eriecanal.org/OECSHP.html')
LWRP=L('Old Erie Canal corridor waterfront plan, Fayetteville section (2021 draft, PDF)','https://sarah-krisch.squarespace.com/s/2_Fayetteville_2021-03-25_DRAFT-OLD_ERIE_CANAL_LWRP_SectionII_Review-DRAFT.pdf')
OLP=L('Onondaga County Parks: Onondaga Lake Park trails and hours','https://onondagacountyparks.com/parks/onondaga-lake-park/trails/?ajax=1&m=1729814072')
PLACES=[
# ---- East of the city: the Old Erie Canal ----
N('butternut-creek-aqueduct','Butternut Creek Aqueduct','DeWitt','cny','canal','ruins',43.04357,-76.05022,'exact','public','walk','canal','1856–1917',
  'A three-span stone aqueduct, 80 feet long, that carried the enlarged Erie Canal over Butternut Creek; it was finished in 1856 and stands at the western end of Old Erie Canal State Historic Park. Its wooden trough rotted away and was replaced by a narrow concrete channel, which still feeds water into the canal. In 2012 the aqueduct breached, draining a long stretch of the canal and flooding the creek; it was mended by plugging the breach with gravel.',
  'The stone towpath arches and the piers that held the trough, seen from the towpath and, eriecanal.org says, from above on Kinne Road near Butternut Drive. A feeder from Jamesville Reservoir joined the canal just west of the aqueduct.',
  'Where the 36-mile canal park begins: an 1856 aqueduct that burst in 2012.',
  'Old Erie Canal State Historic Park (New York State Parks), open year-round from sunrise to sunset by the park page. The state trail map marks parking on Burdick Drive at Marsh Drive and the Butternut Creek Recreation Area and Ryder Park beside the trail at the aqueduct; which lot is nearest was not checked on the ground. Stay on the towpath above the creek.',
  [OEC,OECMAP,L('eriecanal.org: Butternut Creek Aqueduct','https://eriecanal.org/ButternutCreek.html'),W('Butternut Creek (Limestone Creek tributary)'),ECO]),
N('limestone-creek-aqueduct','Limestone Creek Aqueduct','Manlius','cny','canal','ruins',43.04406,-76.01040,'exact','public','walk','canal','1856–1917',
  'The enlarged Erie Canal crossed Limestone Creek here on a three-span stone aqueduct, 79 feet 10 inches long, completed in 1856. Its wooden trough is gone; a narrow concrete channel now carries canal water across between two concrete dams, and the stone arches still hold up the towpath, which is the Erie Canalway Trail.',
  'From the towpath: the arches under the trail, the trough piers and the end walls, some topped with concrete buttresses that hold the modern channel. eriecanal.org also photographed the arches from the creek bed.',
  'An aqueduct you ride across without noticing.',
  'Old Erie Canal State Historic Park (New York State Parks), open year-round from sunrise to sunset. The Fayetteville waterfront plan names the Limestone Feeder trail, about a mile long, from Canal Landing Park in Fayetteville to the aqueduct; parking at the park itself was not checked.',
  [OEC,L('eriecanal.org: Limestone Creek Aqueduct','https://eriecanal.org/LimestoneCreek.html'),W('Limestone Creek (Chittenango Creek tributary)'),LWRP,ECO]),
N('fayetteville-lime-kilns','Fayetteville lime kilns and the Limestone Feeder','Fayetteville','cny','industry','ruins',43.03174,-76.01330,'area','view','walk','canal','1800s',
  'Fayetteville grew on quarries and cement: its limestone burned into a lime that made cement that set under water, which the canal builders needed for locks and aqueducts. A navigable feeder canal from Limestone Creek linked the village to the Erie Canal and was lined with a sawmill, lime kilns, a grist mill and other works. The sources disagree on its age: the waterfront plan web page says the state dug it in 1826, while the plan itself gives 1852, with the enlarged canal, as its earliest record.',
  'The waterfront plan web page says that walking or riding south on the Feeder trail you see the remains of the old lime kilns on your left. OpenStreetMap has an information board titled "Lime Kilns, Cement, Fayetteville\'s History" on Feeder Street, which is where the pin is; the kilns themselves were not located, and what is left of them was not checked.',
  'The lime that made the canal\'s underwater cement.',
  'The Limestone Feeder trail (a one-mile path from Canal Landing Park in the Village of Fayetteville to the Old Erie Canal towpath) and Feeder Street are public; who owns the ground the kilns stand on was not checked, so look from the trail. Trail hours not checked.',
  [L('Old Erie Canal corridor plan: Fayetteville things to see (lime kiln remnants)','https://sarah-krisch.squarespace.com/fayetteville-1'),LWRP]),
# ---- West of the city ----
N('clintons-ditch-camillus','Clinton\'s Ditch remains, Camillus Erie Canal Park','Camillus','cny','canal','traces',43.05220,-76.29954,'site','public','walk','canal','1825–1840s',
  'Camillus Erie Canal Park, a town park, keeps seven miles of the enlarged Erie Canal. Beside it lies a stretch of the first canal of 1825, Clinton\'s Ditch, which the enlargement replaced; the park also holds the remnants of an earlier lock and aqueduct used from 1825 to the mid-1840s, a waste weir, a feeder, Culvert 59, and the lower seven feet of the gates of Lock 50 (Gere\'s Lock), dug from the mud and put on show. A sign marks the midpoint of the original canal between Albany and Buffalo.',
  'The bed of Clinton\'s Ditch, seen from a nature trail (Wikipedia); the Lock 50 gate bottoms and the replica Sims\' Store at the park centre on Devoe Road. Where exactly the 1825 lock and aqueduct remnants lie was not checked.',
  'Two Erie Canals side by side: the 1825 ditch and its 1840s replacement.',
  'Camillus Erie Canal Park (Town of Camillus), 5750 Devoe Road; Sims\' Store is a museum and gift shop. The park\'s own site (eriecanalcamillus.com) refused the connection, so hours and rules were not checked. The Nine Mile Creek Aqueduct, already in the Atlas, is in the same park.',
  [W('Camillus Erie Canal Park'),L('eriecanal.org: Camillus Erie Canal Park','https://eriecanal.org/Camillus.html'),L('eriecanal.org: Lock 50 (Gere\'s Lock)','https://eriecanal.org/Lock50.html'),L('Camillus Erie Canal Park','https://www.eriecanalcamillus.com/')],
  th=[43.05258,-76.30299],thn='Sims\' Store, Devoe Road'),
N('erie-lock-51-jordan','Enlarged Erie Canal Lock 51','Elbridge','cny','canal','ruins',43.06687,-76.49560,'exact','public','walk','canal','1847–1917',
  'A double lock of the enlarged Erie Canal, built in 1847 about two miles west of Jordan to replace the village lock; it lowered boats 5.7 feet to the west. Its south chamber was later made double length (the marker says the locks were lengthened in 1884). The lock tender\'s house stood here until it was moved to the Jordan-Elbridge school about 1990 (1988 by the HMdb marker at its new site).',
  'Both stone chambers, with door recesses and stairs at the west end; eriecanal.org photographed them from the towpath and the heelpath in 2007 and 2009. An interpretive sign stands in the rest area.',
  'A double lock in the woods at the county line.',
  'Lock 51 Park, an Onondaga County park of about three quarters of an acre on the north side of Route 31, with parking for three or four cars. It is on the Jordan Level Trail (Erie Canalway Trail), which can also be joined at the village park in Jordan, Laird Road and McDonald Road. Park hours were not given on the county page.',
  [L('Onondaga County Parks: Lock 51 Park','https://onondagacountyparks.com/parks/lock51/?ajax=1&m=1776244566'),L('eriecanal.org: Lock 51','https://eriecanal.org/Lock51.html'),L('HMdb: The Canalway Trail, Elbridge/Lock 51','https://www.hmdb.org/m.asp?m=153837'),L('HMdb: Jordan Lock 51','https://www.hmdb.org/m.asp?m=109249'),L('HMdb: Locktender\'s House','https://www.hmdb.org/m.asp?m=153650')]),
N('jordan-aqueduct','Jordan Aqueduct','Jordan','cny','canal','ruins',43.06627,-76.47234,'site','public','walk','canal','1841–1917',
  'The enlarged Erie Canal crossed Skaneateles Creek in the middle of Jordan on a four-span aqueduct, 105 feet 6 inches long, built in 1841–45. It was abandoned at the close of the 1917 season. In 1932 the old canal through the village was made into a garden park, a WPA project, with the aqueduct remains as its centrepiece; the Village of Jordan keeps the gardens and the stonework.',
  'The four towpath arches, which carry the canal trail, and the piers that held the trough; a modern footbridge spans the creek from pier to pier. Fill has buried the bottom of the two eastern piers.',
  'A canal aqueduct turned into a village garden in 1932.',
  'Jordan Canal Park, kept by the Village of Jordan, on the Erie Canalway Trail where it crosses Main Street (Route 317). Hours and parking were not checked.',
  [L('eriecanal.org: Jordan Aqueduct','https://eriecanal.org/JordanAqueduct.html'),W('Jordan Canal Park'),L('CNY Hiking: Old Erie Canal Trail, Pump Road to Jordan','https://cnyhiking.com/OldErieCanalJordan.htm')]),
N('charlie-major-trail-mills','Mill and dam ruins on the Charlie Major Nature Trail','Skaneateles','cny','industry','ruins',42.96810,-76.44231,'area','public','walk','','1840–1981',
  'The Charlie Major Nature Trail follows the bed of the Skaneateles Short Line, a railroad that ran in one form or another from 1840 to 1981 between Skaneateles and Skaneateles Junction. It served the mills that Skaneateles Creek powered: paper mills, grist mills, distilleries and woodworking mills. Passenger trains stopped in 1932; the tracks from Skaneateles Falls to Skaneateles were abandoned in 1970, Stauffer Chemical bought the railroad in 1974, and it stopped running on July 15, 1981.',
  'The town says that along the trail you see remains of the railroad, dams and mill buildings; the trail crosses the creek on three bridges. Which ruin stands where was not checked: the pin is a trail bridge about halfway along.',
  'A rail trail through the ruins of the mills it was built to serve.',
  'Town of Skaneateles trail, carry in and carry out. Parking at both ends: in Mottville at Crow Hill Road and Frost Street (with a playground), and north of Skaneateles near 4144 Mill Road by the Old Seneca Turnpike. Hours not given on the town page.',
  [L('Town of Skaneateles: Charlie Major Nature Trail','https://www.townofskaneateles.gov/departments/parks/charlie-major-nature-trail/'),L('CNY Hiking: Charlie Major Nature Trail','https://cnyhiking.com/CharlieMajorNatureTrail.htm')],
  th=[42.97314,-76.44426],thn='Crow Hill Road bridge, Mottville (trail\'s north end)'),
# ---- North: Onondaga Lake and the Oswego Canal ----
N('mud-lock-5-liverpool','Mud Lock (Oswego Canal Lock 5)','Liverpool','cny','canal','ruins',43.12358,-76.24964,'site','public','walk','canal','1828–early 1900s',
  'Lock 5 of the Oswego Canal, which opened in 1828–29 from Lake Ontario to the Erie Canal in Syracuse. It was called the Mud Lock for the shifting, quicksand-like ground. It was rebuilt and enlarged several times; in 1887 Garnet D. Baltimore, the first Black graduate of Rensselaer Polytechnic Institute, helped lengthen it for longer boats. The Barge Canal made it redundant in the early 1900s.',
  'The Pomeroy Foundation says the stone lock walls were still standing in 2025; its marker (2025) stands beside them at the Cold Springs end of Onondaga Lake Park. On the leaf-off aerial and the LiDAR a narrow walled chamber runs north and south just west of the marker, which is where the pin is.',
  'A canal lock rebuilt by one of the first Black civil engineers in America.',
  'Onondaga Lake Park (Onondaga County), open April to October 6 am to half an hour after sunset and November to March 6 am to sunset; the park closes at 4:30 pm during Lights on the Lake. The marker\'s address is 77 Cold Springs Trail, Liverpool.',
  [L('Pomeroy Foundation: Mud Lock 5 marker','https://www.wgpfoundation.org/historic-markers/mud-lock-5/'),OLP]),
N('guard-lock-2-fulton','Guard Lock 2, Oswego Canal','Fulton','cny','canal','ruins',43.26169,-76.36596,'site','public','hike','canal','about 1858–early 1900s',
  'A guard lock on the old Oswego Canal, built about 1858 to replace an earlier one near the horseshoe dam across the Oswego River. Guard locks usually stood open and were closed in floods to keep the river out of the canal. The Barge Canal, which turned the river itself into the waterway in the early 1900s, made it unnecessary.',
  'The stone lock in the woods by the river; the Pomeroy page says paddlers can still go through it. A Pomeroy marker stands at it.',
  'An old canal lock you can paddle through.',
  'Great Bear Recreation Area, owned by the City of Fulton and the Town of Volney, open dawn to dusk and free (Town of Volney). Walk the River\'s Landing loop (yellow) to the lock. CNY Hiking puts a small parking area off County Route 57 across from the junction with Great Bear Road; the Pomeroy page says the lots were free in 2022 and volunteers keep the path.',
  [L('Pomeroy Foundation: Guard Lock 2 marker','https://www.wgpfoundation.org/historic-markers/guard-lock-2/'),L('Town of Volney: Great Bear Trails hours','https://townofvolney.gov/faqs/what-can-i-do-at-great-bear-trails-and-what-are-its-operating-hours'),L('CNY Hiking: Great Bear Recreation Area','https://www.cnyhiking.com/GreatBearRecArea.htm')],
  th=[43.26601,-76.35218],thn='Great Bear lot, County Route 57 opposite Great Bear Road'),
N('fort-brewerton','Fort Brewerton earthworks','Brewerton','cny','fort','traces',43.24222,-76.14139,'exact','view','drive','forts','1759–1768',
  'A British fort built in 1759 on the north bank of the Oneida River near Oneida Lake to guard the route from Albany to Oswego. It was an eight-pointed star of earth walls with log palisades and a moat, holding four log blockhouses. Fort Wiki says it was dismantled and abandoned under a treaty with the Mohawks, giving both 1767 and 1768. The site was listed on the National Register in 1973.',
  'A 1932 state marker calls what is here the original earthworks of the 1759 fort; Fort Wiki also says some of the earthworks remain. Beside them is the Oliver Stevens Blockhouse, a log reconstruction of a later blockhouse, now the historical society\'s museum. On the state\'s bare-ground LiDAR the whole eight-pointed star shows clearly at the pin, just south of Route 11 and west of the road to the bridge, and it can be made out on the leaf-off aerial too; how it looks on the ground was not checked.',
  'A star-shaped British fort from the French and Indian War.',
  'Fort Brewerton Historical Society, 9 US Route 11, Brewerton. Wikipedia says the museum is open noon to 4 pm on the third Saturday of each month from April to December, and for events and private tours by request; the society\'s own hours were not checked. Who owns the grounds and whether they are open outside museum days was not checked: look from Route 11 or come on an open day.',
  [W('Fort Brewerton'),L('HMdb: Fort Brewerton marker','https://www.hmdb.org/m.asp?m=84165'),L('HMdb: Strategic Crossroads','https://www.hmdb.org/m.asp?m=253242'),L('Fort Wiki: Fort Brewerton','https://www.fortwiki.com/Fort_Brewerton')],
  conf='mixed'),
N('long-branch-park','Long Branch amusement park','Geddes','cny','amuse','gone',43.11777,-76.25002,'area','view','drive','trolleyparks,amusements','1882–1938',
  'Ben and George Maurer opened Long Branch on the north shore of Onondaga Lake in 1882, named for its chestnut trees. It had a dance pavilion, a restaurant, an arcade, bowling, billiards, boating, ice boating and rides, and Wikipedia lists a trolley among its features. Badly damaged in 1912 and rebuilt, it closed in 1938, done in by the polluted lake, the end of the trolleys and the car. Its carousel stayed until 1941, went to Roseland Park in Canandaigua, and now turns at Destiny USA.',
  'Nothing of the amusement park was found in the sources. The ground is a county picnic park; the "Resort Era" sign at the West Shore Trail lot across Long Branch Road tells the story of the lake\'s resorts.',
  'Syracuse\'s trolley park, and a carousel that outlived it.',
  'Long Branch Park is part of Onondaga Lake Park (Onondaga County) and is a reserved-use area only: the county says to contact the Griffin Visitor Center to reserve it. The West Shore Trail lot on Long Branch Road is open to trail users.',
  [L('Onondaga County Parks: Long Branch Park','https://onondagacountyparks.com/parks/onondaga-lake-park/long-branch-at-onondaga-lake-park/?ajax=1&m=1725797439'),W('Long Branch Park'),L('HMdb: The Resort Era','https://www.hmdb.org/m.asp?m=144419'),OLP]),
]
PIN_NOTES={'butternut-creek-aqueduct': 'OpenStreetMap feature "Butternut Creek Aqueduct" (tools/nom.py); on the leaf-off aerial and the LiDAR the pin sits on the aqueduct where the canal crosses the creek beside Interstate 481.',
 'limestone-creek-aqueduct': 'OpenStreetMap aqueduct bridge "Limestone Creek Aqueduct" (tools/nom.py); the aerial shows the pin on the structure, with the concrete dams on each side.',
 'fayetteville-lime-kilns': 'OpenStreetMap information board "Lime Kilns, Cement, Fayetteville\'s History" on Feeder Street; the aerial shows a paved lot by the feeder, and the LiDAR the feeder channel just west. The kilns themselves were not located.',
 'clintons-ditch-camillus': 'OpenStreetMap derelict canal "Clinton\'s Ditch" (tools/nom.py); the LiDAR shows a narrow channel and bank north of and parallel to the watered enlarged canal at the pin. Trailhead is the Sims\' Store position in the Canalway Water Trail guidebook; the aerial shows the store and its lot.',
 'erie-lock-51-jordan': "Moved about 46 m west-northwest from the HMdb position of the rest-area sign (43° 4.004' N, 76° 29.704' W) onto the double lock chamber, which shows on the aerial and the LiDAR north of Route 31 (tools/look.py, tools/pix.py).", 'jordan-aqueduct': 'Wikipedia coordinate for Jordan Canal Park; the aerial shows it on the creek crossing with the footbridge among the aqueduct piers.',
 'charlie-major-trail-mills': "An OpenStreetMap bridge of the Charlie Major Nature Trail, about halfway along; no single ruin was located. Trailhead is the OpenStreetMap Crow Hill Road bridge at the trail's north end, a public road; the lot itself was not made out on the aerial.", 'mud-lock-5-liverpool': 'Moved 16 m west-southwest from the Pomeroy Foundation marker position (43.123678, -76.249497) onto a narrow walled chamber that shows on the leaf-off aerial and the LiDAR (tools/pix.py).',
 'guard-lock-2-fulton': 'Pomeroy Foundation marker position on the yellow towpath trail (43.26169, -76.36596); the LiDAR shows a walled structure on the river bank at the pin. Trailhead is the parking lot OpenStreetMap maps on County Route 57 (tools/parking.py), about 1.2 km north-east of the lock: the aerial shows a gravel lot with cars at the junction with Great Bear Road, as CNY Hiking describes, on land the public-land map calls Great Bear Recreational Area.',
 'fort-brewerton': 'Wikipedia coordinate for Fort Brewerton; the LiDAR shows the eight-pointed star earthwork centred on the pin.',
 'long-branch-park': 'OpenStreetMap park "Long Branch Park" (tools/nom.py); the aerial shows picnic grounds and paths, nothing of the amusement park.'}
