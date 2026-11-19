# November 19, 2026: South County (Washington County), Rhode Island, fourth Rhode Island pass. Drawn at random by
# tools/choose.py (region risouth). Mostly standing places the earlier passes left out (the oldest churches and houses
# round Wickford and Saunderstown, Watch Hill, working mills, lighthouses, a railroad station) and one ruin, the
# Windswept carriage house at Black Point.
# Facts come from the linked sources only. Wikipedia was read as raw text (tools/wiki_raw.py); museum, fire-district,
# preservation and magazine pages through tools/page.py. Where sources disagree the text gives both; where none says,
# it says "not checked". Pins: the Wikipedia or Register coordinate, or an OpenStreetMap feature, each looked at on the
# March 2026 state aerial with tools/pincheck.py (research/pincheck_risouth_kchn_*.jpg), as each pin note says.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'risouth_kchn','label':'South County, Rhode Island (fourth pass)','added':'2026-11-19 04:41'}
WHFD_C=L('Watch Hill Fire District: Flying Horse Merry-Go-Round','https://watchhillfiredistrict.org/merry-go-round/')
WHFD_L=L('Watch Hill Fire District: Lighthouse and Museum','https://watchhillfiredistrict.org/the-watch-hill-lighthouse-and-museum/')
BSH=L('Babcock-Smith House Museum: visit','https://babcocksmithhouse.org/visit/')
BSH0=L('Babcock-Smith House Museum','https://babcocksmithhouse.org/')
NEL_PJ=L('New England Lighthouses: Point Judith','https://www.nelights.com/exploring/rhode_island/point_judith_lighthouse.html')
VRI_PJ=L('Visit Rhode Island: Point Judith Lighthouse','https://www.visitrhodeisland.com/listing/point-judith-lighthouse/8467/')
RIWPS_BP=L('RI Wild Plant Society: Malcolm Grant Trail (2018)','https://riwps.org/on-the-trail/malcolm-grant-trail-narragansett-ri/')
PJ_BP=L('PattyJ.com: the ruins at Scarborough Beach (2020)','https://pattyj.squarespace.com/full-blog/2020/5/22/4yxj1kfeax3ymu16z80ihj10h5pcbt')
A360_BP=L('Abandoned in 360: Windswept Mansion','https://abandonedin360.com/abandoned-residential-properties/windswept-mansion/')
SAH_ONC=L('SAH Archipedia: Old Narragansett Church','https://sah-archipedia.org/buildings/RI-01-NK21')
SORI_ONC=L('South of Rhode Island: Faith Restored (Old Narragansett Church)','https://sorhodeisland.com/stories/faith-restored-preserving-old-narragansett-church-in-wickford,36812')
SC_H=L("Smith's Castle: location and hours",'https://smithscastle.org/hours')
SC_V=L("Smith's Castle: visit",'https://www.smithscastle.org/visit/')
GSM=L('Gilbert Stuart Museum: visit','https://gilbertstuartmuseum.org/visit-our-museum')
HNE_C=L('Historic New England: Casey Farm','https://www.historicnewengland.org/property/casey-farm/')
YK_PM=L('Yankee: Perry Grist Mill','https://newengland.com/yankee-magazine/travel/samuel-e-perry-grist-mill/')
PC_PM=L('Progressive Charlestown: Perryville grist mill (2012)','https://www.progressive-charlestown.com/2012/10/perryville-grist-mill-same-as-it-ever.html')
LHF_PB=L('Lighthouse Friends: Plum Beach','https://www.lighthousefriends.com/light.asp?ID=402')
USLSS=L('US Life-Saving Service Heritage: Narragansett Pier','https://uslife-savingservice.org/station-buildings/narragansett-pier-station-house/')
URM=L('National Register form: Upper Rockville Mill','http://www.preservation.ri.gov/pdfs_zips_downloads/national_pdfs/hopkinton/hopk_canonchet-road-332_upper-rockville-mill.pdf')

PLACES=[
# ---- Westerly and Watch Hill ----
N('flying-horse-carousel-watch-hill','Flying Horse Carousel','Westerly','risouth','amuse','standing',41.30912,-71.85818,'exact','public','walk','amusements','c.1876–',
  'A small carousel whose twenty wooden horses hang on chains from sweeps and swing outward as it turns, which gives it its name. Its age rests on inference: Wikipedia, after the landmark nomination, gives about 1876 and says a travelling carnival left it at Watch Hill in 1879; the Watch Hill Fire District says it has run since 1867. It was horse-powered, then water-powered from 1897 and electric from about 1914. The 1938 hurricane threw the horses into the dunes; they were dug out and it ran again, short three chariots. National Historic Landmark 1987.',
  'The horses are carved wood with their original agate eyes; manes, reins and other trappings are replacements. It turns inside a ten-sided, hip-roofed wooden pavilion of the early 1900s at the end of Bay Street, behind a low picket fence. Only children under 12 may ride, and a brass-ring arm comes down halfway through the ride.',
  'The oldest carousel in the country whose horses fly out on chains.',
  'Kept by the Watch Hill Fire District with the Watch Hill Memorial Library and Improvement Society. Wikipedia says it runs from June to Labor Day; tickets are sold in the building to its right, and the fire district points to the carousel\'s own site for hours (not read). Parking: the Larkin Road lot about 150 m north-east (whether it charges was not checked).',
  [W('Flying Horse Carousel'),WHFD_C],conf='mixed',th=[41.30942,-71.85715],thn='Larkin Road lot, Watch Hill',brick='no'),
N('watch-hill-lighthouse','Watch Hill Lighthouse','Westerly','risouth','light','standing',41.30389,-71.85842,'exact','view','walk','','1856–',
  'A beacon and watchtower stood here from 1745. The first lighthouse, of 1807, had to be given up to erosion, and the present 45-foot tower was lit in 1856 further back from the bluff. Its keeper won the Congressional Gold Medal for the rescue after the steamer Metis sank off Watch Hill in 1872, and his widow became the first woman keeper here in 1879. The light was automated in 1986 and leased to the Watch Hill Lightkeepers Association.',
  'The 1856 tower and the buildings round it, from the outside: the fire district says the lighthouse and its neighbouring buildings are closed to the public, but a museum there opens in summer. What the tower is built of and what is in the museum were not checked.',
  '',
  'Managed by the Watch Hill Lighthouse Keepers Association for the Coast Guard. The Watch Hill Fire District says it is reached on foot by a private road, open 8 a.m. to sunset all year; only disabled visitors and senior citizens may drive down. Museum hours not checked (see the association\'s site). Parking in Watch Hill village, such as the Larkin Road lot about 700 m north.',
  [W('Watch Hill Light'),WHFD_L],th=[41.30942,-71.85715],thn='Larkin Road lot, Watch Hill',brick='?'),
N('babcock-smith-house-westerly','Babcock-Smith House','Westerly','risouth','landmark','standing',41.371111,-71.820278,'site','public','drive','','c.1734–',
  'A Georgian mansion of about 1734, the home first of the Babcocks, among them the colonial doctor Joshua Babcock, and later of the Smiths, whose family ran a granite business. A volunteer museum since 1972, it tells two stories: the colonial house and the Westerly granite industry.',
  'The house is furnished for the Babcock years, the Victorian Smith years and a colonial restoration of 1928. On the grounds are a carriage house, Joshua\'s Store and a granite exhibit, with granite records and local history books for researchers. Which details are original to the house was not checked.',
  '',
  'Babcock-Smith House Museum, 124 Granite Street, with parking behind the museum. The museum\'s page gives: from the Saturday of Memorial Day weekend to October 31, Saturdays 2–5 p.m. with a guided tour at 3; in July, August and September, Thursday to Sunday 2–5; closed July 4; tours by appointment all year. Suggested donation $10 for adults, children under 12 free, cash only. The house has two steps in and stairs to the upper floor.',
  [BSH,BSH0],brick='?'),
# ---- Narragansett ----
N('point-judith-lighthouse','Point Judith Lighthouse','Narragansett','risouth','light','standing',41.36103,-71.48139,'exact','view','drive','','1856–',
  'Three lights have stood on Point Judith, where two busy waterways meet in cold, dangerous water. A tower of 1810 fell to the 1815 hurricane; its stone replacement of 1816 gave way to the present octagonal granite tower in 1856. The top half is painted brown so that sailors can tell it apart by day. Automated 1954; on the National Register since 1988.',
  'The octagonal granite tower, white below and brown above, beside a working Coast Guard station. The tower is not open.',
  '',
  'Coast Guard property. The sources disagree on the grounds: Visit Rhode Island says visitors are welcome on the grounds with the lighthouse and station off limits; New England Lighthouses says the grounds are no longer open and the light is seen from a small park before the gate, with no-trespassing signs at the residence. Parking: the lot on Ocean Road about 140 m north. Hours not checked.',
  [W('Point Judith Light'),VRI_PJ,NEL_PJ],conf='mixed',th=[41.3623,-71.48136],thn='Ocean Road lot by the gate',brick='no'),
N('coast-guard-house-narragansett','Narragansett Pier Life-Saving Station (Coast Guard House)','Narragansett','risouth','civic','standing',41.43021,-71.45534,'exact','view','walk','','1888–',
  'A life-saving station built in 1888 to designs by McKim, Mead and White, when Narragansett Pier was a fashionable resort. It served until 1946 and became a restaurant in the 1960s, when a large dining room was added and the boat-room floor levelled. Fire damaged the south end of the upper floor in 1975. An earlier station house of 1872 stood somewhere nearby and is gone.',
  'An oblong block, rounded at its north end, under a steep slate roof that curves with that end. The restaurant additions run to the south and east. Interior not checked.',
  '',
  'The Coast Guard House restaurant, 40 Ocean Road; open as a restaurant in 2026 by its listings in search results, hours not checked. Seen from Ocean Road and the sea wall walk; a mapped lot on the sea wall walk is close by to the north.',
  [W('Narragansett Pier Life Saving Station'),USLSS],brick='?'),
N('windswept-carriage-house-black-point','Windswept carriage house ruins, Black Point','Narragansett','risouth','landmark','ruins',41.39538,-71.46703,'site','public','walk','burned','1895–',
  'Edmund Davis, grandson of the maker of Perry Davis\'s Vegetable Pain Killer, built a summer estate here in 1895 with a large mansion and a stone carriage house above what is now Scarborough Beach. By a 2020 local write-up, citing a newspaper, the estate was later sold and run as a restaurant, which burned; the state then took over the land.',
  'The stone shell of the carriage house at the south end of the Black Point trails, near the north edge of Scarborough State Beach. Nothing else of the estate was checked. These are ruins: keep out of the walls.',
  '',
  'State land: the Black Point Fishing Area, Department of Environmental Management (the Malcolm Grant Trail, named for the official who helped buy Black Point). Park in the Black Point lot across from 655 Ocean Road and walk the main trail south, about four miles of trails in all. Hours not checked. Watch for poison ivy and cliffs.',
  [RIWPS_BP,PJ_BP,A360_BP],conf='mixed',th=[41.39992,-71.46467],thn='Black Point Fishing Area lot, Ocean Road',brick='?'),
# ---- North Kingstown: Wickford and Saunderstown ----
N('old-narragansett-church','Old Narragansett Church','North Kingstown','risouth','civic','standing',41.5725,-71.44972,'site','view','walk','','1707–',
  'Built in 1707 about five miles from here for the Anglican parish of St. Paul\'s, and believed the oldest Episcopal church building in the Northeast. Where it first stood is given differently: Pendar Road (Wikipedia), Shermantown Road (Buildings of Rhode Island) and Tower Hill (a 2020s magazine). In 1800 it was hauled to Wickford. Gilbert Stuart was baptised in it in 1756. After the plaster barrel vault fell in from ice-dam damage in 2019 it was restored.',
  'A plain five-bay clapboard meeting house with round-arched windows, a segmental pediment over the double door and a plastered barrel-vault ceiling. Inside, the pulpit stands on the long wall; the gallery dates from 1723 and the pews from about 1800, many with names and drawings scratched in by parishioners, kept on purpose in the restoration. It has no electricity or heat; the parish holds services here in summer. Opening times for visitors not checked.',
  '',
  'St. Paul\'s Episcopal Church, Wickford, 60 Church Lane. Public parking off Main Street, about 350 m east. Seen from Church Lane at any time; when it is open to visitors was not checked.',
  [W('Old Narragansett Church'),SAH_ONC,SORI_ONC],conf='mixed',th=[41.5722,-71.44568],thn='Main Street public lot, Wickford',brick='no'),
N('smiths-castle-cocumscussoc','Smith\'s Castle (Cocumscussoc)','North Kingstown','risouth','landmark','standing',41.58343,-71.455,'site','public','drive','','1678–',
  'Near the trading post Roger Williams opened in 1637, Richard Smith built a fortified house, the "castle". His son let colonial militias use it in King Philip\'s War; it was burned after the Great Swamp Fight and rebuilt in 1678 as a saltbox, later altered. About 40 soldiers were buried on the land. It was a dairy farm into the 1900s before it became a museum; the site is a National Historic Landmark for what digs have found.',
  'One of the oldest houses in the state, shown by docent-led tours; the grounds and trails are open for walking. What original fabric survives inside was not checked.',
  '',
  'House museum at 55 Richard Smith Drive, off Route 1. Its page gives tours in season Friday to Sunday 11:30–4:30 and office hours off season Monday to Friday 10–1; the tour season had ended for 2026 when read. Parking not checked.',
  [W("Smith's Castle"),SC_H,SC_V],brick='?'),
N('gilbert-stuart-birthplace','Gilbert Stuart Birthplace and snuff mill','North Kingstown','risouth','industry','standing',41.52027,-71.44434,'site','public','drive','','1751–',
  'The painter Gilbert Stuart was born here in 1755 in a house of 1751, where his father ground snuff with a water-powered mill in the basement. The mill and wheel were later lost. Norman Isham restored the house in 1930 and it opened as a museum in 1931, with an English snuff mill of the 1730s brought in and a new wheel on the side of the house turned by Carr Pond. A grist mill of 1757 stands on the grounds; it ran again from 2007.',
  'Much of the original wooden walls and beams and the four corner fireplaces survive; the furnishings are of the period but none is the Stuarts\'. Tours show both mills working and the fish ladder. Trails on the 23 acres pass the Hammond burial ground and the foundation of a colonial fulling mill.',
  '',
  'Gilbert Stuart Birthplace & Museum, 815 Gilbert Stuart Road, Saunderstown. Its page: open late April through October, Wednesday to Sunday 10–4; call ahead for a guided tour. Admission not checked.',
  [W('Gilbert Stuart Birthplace'),GSM],brick='?'),
N('casey-farm-saunderstown','Casey Farm','North Kingstown','risouth','landmark','standing',41.51333,-71.42444,'area','public','drive','','c.1725–',
  'A 300-acre farm across the whole neck between the Narrow River and the West Passage, never divided in three centuries. Daniel Coggeshall built the house about 1725–50; it passed to the Caseys by marriage, and the family kept it, often with tenant farmers, until giving it to what is now Historic New England in 1955. General Silas Casey and Thomas Lincoln Casey, engineer of the Washington Monument, are buried here.',
  'The farmhouse, farmyard and family cemetery, where six generations of Caseys lie; the guided tour takes in the farmyard and cemetery. Organic vegetables are still grown here. Interior not checked.',
  '',
  'Historic New England, 2325 Boston Neck Road (Route 1A). Wikipedia says a farmers market runs Saturday mornings mid-May through October. Historic New England\'s page refused this session\'s reader, so tour days and fees were not checked.',
  [W('Casey Farm'),HNE_C],brick='?'),
N('plum-beach-lighthouse','Plum Beach Lighthouse','North Kingstown','risouth','light','standing',41.5303,-71.4052,'exact','boat','boat','','1899–',
  'A sparkplug lighthouse on Plum Beach Shoal in the West Passage, sunk in place on a pneumatic caisson from 1896 after steamer captains had pleaded for it for years; its builder called it the stormiest place they had ever worked. Lit in 1899, it was put out in 1941 when the first Jamestown Bridge opened and stood derelict until the Friends of Plum Beach Lighthouse took it over in 1999, restored the outside in 2003 and relit it.',
  'The cast-iron tower on its caisson, with the granite base added in 1922. Not open; seen from the water.',
  '',
  'Owned by the Friends of Plum Beach Lighthouse. Out on the shoal; a shore viewpoint was not checked.',
  [W('Plum Beach Light'),LHF_PB],brick='?'),
N('six-principle-baptist-church','Six Principle Baptist Church (Old Baptist Meeting House)','North Kingstown','risouth','civic','standing',41.59278,-71.49139,'site','view','drive','cemeteries','c.1703–',
  'The land was deeded for a meeting house about 1703, and the congregation probably dates from after 1664. It is one of the last congregations of the Six Principle Baptists, an offshoot of the First Baptist Church in Providence. The meeting house was remade in Greek Revival style in 1842; its 1700s frame is believed to survive inside.',
  'The Greek Revival meeting house on Stony Lane and its old cemetery. Interior not checked.',
  '',
  'An active church; as of 2009 Wikipedia gave Sunday service at 10:30 a.m. Seen from Stony Lane; when else it is open was not checked.',
  [W('Six Principle Baptist Church')],brick='?'),
# ---- South Kingstown ----
N('kingston-station-ri','Kingston railroad station','South Kingstown','risouth','rail','standing',41.484,-71.5607,'site','public','drive','stations','1875–',
  'The New York, Providence and Boston Railroad built this station in 1875 at West Kingston, a village that grew up round the line after it opened in 1837 and missed Kingston itself. It has been in use ever since. The Narragansett Pier Railroad left from here for Peace Dale and the Pier until passenger trains ended in 1952; its bed is now the William C. O\'Neill Bike Path.',
  'The 1875 station building beside the Northeast Corridor, still a stop for Amtrak Northeast Regional trains. Inside not checked.',
  '',
  'Amtrak station with a parking lot by the platform. Waiting-room hours not checked. Stay off the tracks: trains pass at high speed.',
  [W('Kingston station (Rhode Island)'),W('Narragansett Pier Railroad')],th=[41.48326,-71.56129],thn='Station lot',brick='?'),
N('perry-carpenter-grist-mill','Perry-Carpenter Grist Mill','South Kingstown','risouth','industry','standing',41.39222,-71.57694,'exact','view','drive','','c.1703 or c.1716–',
  'A small water-powered corn mill at Perryville, said to be the oldest working corn mill in Rhode Island. Its dates are given two ways: Wikipedia, after the Register listing, says James Perry built it about 1716 and it was moved here before 1789; Yankee and a 2012 local article say 1703, and the 2012 article says the Watsons moved it about 500 feet in 1825. A turbine replaced the wheel between 1850 and 1860. Bob and Diane Smith bought it in 1985 and grind Rhode Island whitecap flint corn into jonnycake meal.',
  'A single-storey wood-frame mill on a granite foundation by the east side of Moonstone Beach Road, with its head race and tail race from Perry\'s Mill Pond. On grinding days the owners show it working.',
  '',
  'Private, a working business at 364 Moonstone Beach Road. Seen from the road. Grinding days are announced in the local paper (Yankee); the 2012 article says parking is in the yard just south and across the road. Ask before going in.',
  [W('Perry-Carpenter Grist Mill'),YK_PM,PC_PM],conf='mixed',brick='no'),
N('fayerweather-blacksmith-shop','George Fayerweather blacksmith shop','South Kingstown','risouth','industry','standing',41.48038,-71.52018,'exact','view','drive','','1820–',
  'The home and smithy of George Fayerweather, an African-American blacksmith, and his wife Sarah Harris Fayerweather, on the edge of Kingston village. The shop was built in 1820. The Kingston Improvement Association keeps it.',
  'The homestead and shop at 1859 Mooresfield Road, restored after a 1940 survey photograph showed it run down. It now houses the Fayerweather Craft Guild and the Kingston Garden Club. Interior not checked.',
  '',
  'Kingston Improvement Association. Seen from Mooresfield Road (Route 138); when it is open was not checked.',
  [W('George Fayerweather Blacksmith Shop')],brick='?'),
# ---- Hopkinton ----
N('upper-rockville-mill','Upper Rockville Mill','Hopkinton','risouth','industry','standing',41.52026,-71.76027,'site','view','drive','','1844–',
  'A 3½-storey stone textile mill of 1844–45 with a two-storey building added in the 1860s, built by the Rockville Manufacturing Company, for much of the 1800s the main employer and landowner round Rockville. Textile firms ran it until 1953, when the Boy Scouts bought it for the water rights that mattered to Camp Yawgoog, kept the rights and sold the rest.',
  'The Greek Revival stone mill and its 1860s neighbour at 332 Canonchet Road, the site of a third building, Wincheck Pond and what is left of the raceway. Interior not checked.',
  '',
  'Private. Seen from Canonchet Road.',
  [W('Upper Rockville Mill'),URM],brick='?'),
]

PIN_NOTES={
 'flying-horse-carousel-watch-hill':'Moved about 45 m from the Wikipedia coordinate (which fell on the beach) onto the round-roofed pavilion at the foot of Bay Street seen on the March 2026 aerial, with tools/pix.py.',
 'watch-hill-lighthouse':'Wikipedia coordinate; on the March 2026 aerial it sits on the lighthouse buildings at the tip of Watch Hill Point.',
 'babcock-smith-house-westerly':'Register list coordinate; on the aerial it falls on a street corner among houses, so which building is the museum was not picked out (prec site).',
 'point-judith-lighthouse':'Wikipedia coordinate; on the aerial it is on the lawn at the tip of Point Judith, beside the red-roofed Coast Guard buildings.',
 'coast-guard-house-narragansett':'Moved about 35 m from the Wikipedia coordinate (on Ocean Road) onto the building on the sea side of Ocean Road just south of The Towers, seen on the aerial, with tools/pix.py.',
 'windswept-carriage-house-black-point':'OpenStreetMap point "Windswept Mansion" (building=ruins) on the Black Point main trail; the March 2026 aerial shows a small roofless structure in the scrub at the ring, above the north end of Scarborough Beach.',
 'old-narragansett-church':'Wikipedia coordinate; on the aerial it falls among village buildings off Church Lane; the church itself was not picked out (prec site).',
 'smiths-castle-cocumscussoc':'Moved about 50 m from the Wikipedia coordinate (on the mudflat of the cove) onto the nearer of two buildings on the shore, seen on the aerial; which of them is the house was not certain.',
 'gilbert-stuart-birthplace':'Moved about 70 m from the Wikipedia coordinate (in woods) onto the buildings by the stream and dam south-west of it on the aerial; the Register list gives a point about 700 m north.',
 'casey-farm-saunderstown':'Wikipedia coordinate; on the aerial it falls in a field of the farm, with farm buildings to the south and north; the house was not picked out, so prec area.',
 'plum-beach-lighthouse':'Wikipedia coordinate; on the aerial the ring is on the tower in the West Passage (no LiDAR over water).',
 'six-principle-baptist-church':'Wikipedia coordinate; on the aerial it falls on a parking lot west of Stony Lane beside buildings; the meeting house was not picked out (prec site).',
 'kingston-station-ri':'Wikipedia coordinate; on the aerial it is at the drop-off beside the platform; the 1875 building was not picked out from the newer ones (prec site).',
 'perry-carpenter-grist-mill':'Wikipedia coordinate; on the aerial the ring is on a small building on the east side of Moonstone Beach Road.',
 'fayerweather-blacksmith-shop':'Register list coordinate; on the aerial it is on a building on the north side of Mooresfield Road.',
 'upper-rockville-mill':'Wikipedia coordinate; on the aerial it is on a large mill building on Canonchet Road.',
}
