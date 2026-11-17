# November 17, 2026: Amsterdam, New York, and the country round it (Montgomery and western Schenectady counties).
# Ruins and traces reached on foot: the mill dams and the sealed power house on the North Chuctanunda Creek, the
# enlarged Erie Canal locks at Yankee Hill and Fort Hunter, a farm foundation in the county forest at Duanesburg,
# the old road through Wolf Hollow (finished from LEADS.md), and three stone houses of the Johnson era.
# Facts come from the linked sources only. Wikipedia articles were read as raw text (tools/wiki_raw.py); the state
# parks page, the county and land-conservancy pages, HMdb marker pages, the Old Fort Johnson page and one Substack
# post through tools/page.py; the county's printed creek tour ("Touring the North Chuctanunda Creek", Montgomery
# County Water Quality Committee, posted by the county tourism office in 2019, its own date not printed) as text
# extracted from the PDF. The power-house news pages were read in full; one (Mohawk Valley Compass) refused the
# fetch and is used only through a search excerpt, as the entry says. Where sources disagree the text gives both;
# where a source is silent it says "not checked".
# Pins: an OpenStreetMap feature (tools/nom.py, tools/osmnear.py), an HMdb marker position, or a spot read off the
# aerial with tools/look.py, as each pin note says. Every pin was looked at on the pin check, aerial and LiDAR
# (research/pincheck_amsterdam_*.jpg).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'amsterdam','label':'Amsterdam and the lower Mohawk: mill dams, canal locks and Johnson houses','added':'2026-11-17 06:27'}
TOUR=L('Touring the North Chuctanunda Creek (county tour guide, PDF)','https://visitmontgomerycountyny.com/wp-content/uploads/2019/03/Touring-the-Chuctanunda-Creek.pdf')
DAMS=L('HMdb: Dams and Waterfalls (Chuctanunda Creek Trail)','https://www.hmdb.org/m.asp?m=274710')
ACN=L('HMdb: The AC&N Rail Road (Chuctanunda Creek Trail)','https://www.hmdb.org/m.asp?m=275059')
SCX=L('NYS Parks: Schoharie Crossing details and hours','https://parks.ny.gov/historic-sites/schohariecrossing/details.aspx')
CNTY=L('Schenectady County: nature preserves (County Forest, Wolf Hollow)','https://schenectadycountyny.gov/nature')
PLACES=[
# ---- Amsterdam: the North Chuctanunda Creek ----
N('mohasco-power-house','Mohasco Power House','Amsterdam','mohawk','industry','standing',42.95049,-74.17835,'exact','view','walk','','about 1914–1960s',
  'A tall brick power plant with arched windows, built about 1914 beside the North Chuctanunda Creek to make power for the McCleary, Wallin and Crouse carpet mills, which merged into Mohawk Carpet Mills in 1920 and later Mohasco. A branch of the Amsterdam, Chuctanunda and Northern railroad brought coal to it from about 1915. It stopped working in the 1960s with the rest of the mill complex, when the company moved its work south. The mills themselves burned and were torn down; the city owns the power house, had it studied in 2017 with a Preservation League grant, and has since closed it off.',
  'The brick shell beside the creek, seen from outside only. The county tour guide also describes, on the path from Second Avenue, the footings of a tall railroad trestle in the creek bed, a second trestle behind the power house carrying the coal track to its upper floor, and lumps of coal below it; how much of that is still there was not checked. Upstream, the guide calls the old upper-mill ground a large brownfield.',
  'The last big building of the carpet mills that made Amsterdam the Carpet City.',
  'Owned by the City of Amsterdam and closed: a March 2022 article on 929nin.com says the city secured the building about a year earlier and nobody is allowed inside, and warns against entering. Look from the Chuctanunda Creek Trail. The county tour guide reaches it on a path along the old railroad bed from the Second Avenue bridge (behind the paint store), and warns that the bank drops steeply to the creek. The trail\'s hours and the city\'s rules for it were not checked: the city\'s own trail page (amsterdamny.gov/Chucktrail, named on the trail markers) returned "not found".',
  [L('WAMC (2017): Amsterdam seeks preservation of Mohasco Power House','https://www.wamc.org/new-york-news/2017-07-14/amsterdam-seeks-preservation-of-mohasco-power-house'),
   L('Preservation League: Gratz grant for the Mohasco Power House','https://preservenys.org/blog/gratz-grant-mohasco-power-house'),
   L('929nin.com (2022): the off-limits power house','https://929nin.com/mohasco-power-house/'),TOUR,ACN]),
N('kelloggs-dam-amsterdam','Kellogg\'s Dam and the linseed oil mill','Amsterdam','mohawk','industry','traces',42.93860,-74.17985,'site','view','walk','','1850–1948',
  'The Kellogg family moved a linseed oil business from West Galway to Amsterdam in 1850 and ran it beside the North Chuctanunda Creek as Kelloggs and Miller from 1872, pressing flax seed for oil used in paint and varnish. The county tour guide says the concrete dam below the Fourth Avenue (Pulaski Memorial) bridge was built in 1878 to give the mill power and water, and that its pond once reached Forest Avenue and Church Street before being filled for stores and parking. In 1879 the family built the Amsterdam, Chuctanunda and Northern railroad to link the mill to the New York Central. The business was sold in the 1930s and the mill closed in 1948. Across the creek stand the Sanford carpet mills, where Bigelow-Sanford stopped making carpet in Amsterdam in 1955.',
  'From the Pulaski Memorial Bridge on Fourth Avenue the guide points out the dam, the old oil mill, the railroad trestle that ran to the Sanford mills, and, on Church Street, a large brick oil storage tank. On the aerial a white spill shows on the creek at the pin. The guide\'s date is not printed, so whether each of these still stands was not checked.',
  '',
  'Seen from public streets and bridges: Willow Street, where an HMdb-listed trail marker stands at the bridge, and the Fourth Avenue bridge. The mill buildings are private (the guide says businesses use the old Sanford mills); the guide asks walkers to respect private property, and some of its streets have no sidewalk.',
  [TOUR,ACN,DAMS]),
N('stewarts-dam-amsterdam','Stewart\'s Dam and the pitted rocks','Amsterdam','mohawk','industry','traces',42.94180,-74.17710,'site','view','walk','','1866–',
  'A mill dam on the North Chuctanunda Creek off Forest Avenue. The county tour guide says it powered what was the Stewart and Carmichael mill in 1866, which became the Smeallie and Voorhees paper mill in 1907. The creek here scoured bathtub-sized potholes in the limestone below the dam, which the trail marker calls the Pitted Rocks. The marker says at least seven dams were identified on the lower creek, all but one built to hold water for the mills.',
  'The dam and falls, and the potholes below it when the water is low. The county tour guide says the dam is hard to see with the leaves out, and that from the lot of the old paper mill the footings of an old railroad trestle can be seen in the creek.',
  '',
  'The City of Amsterdam\'s Chuctanunda Creek Trail marker stands on a raised platform overlooking the dam, on Forest Avenue about 0.1 mile south of Second Avenue. Look from there. The guide mentions paths that neighbourhood children use down to the stream; who owns the banks was not checked, and the guide warns to keep back when the water is high.',
  [DAMS,TOUR]),
# ---- Amsterdam and Fort Johnson: stone houses of the Johnson era ----
N('guy-park-manor','Guy Park Manor','Amsterdam','mohawk','civic','standing',42.94701,-74.20939,'site','view','drive','canal','1774–',
  'A limestone Georgian house built in 1774 for Guy Johnson, nephew and son-in-law of Sir William Johnson, after his first house on the land burned. The state confiscated it from the Loyalist Johnsons and sold it; it served for years as a tavern and stagecoach stop on the Mohawk Turnpike, and Wikipedia notes an Erie Canal lock near it. The state bought it in 1907. The Walter Elwood Museum had just moved in when the Mohawk flood after Hurricane Irene severely damaged it in August 2011, and the museum left. Work on the canal walls began in 2016, restoration in 2022, and in 2024 the house was raised four feet against floods.',
  'The stone house by the river; on the state aerial it stands in a fenced work yard. Whether the restoration is finished and whether the house is open was not checked.',
  '',
  'Guy Park State Historic Site, owned by the State of New York. Whether the grounds or the house are open, and the hours, were not checked: look from the street or the canal side until you know.',
  [W('Guy Park'),L('HMdb: Manor House on the Mohawk','https://www.hmdb.org/m.asp?m=152505')],conf='mixed'),
N('old-fort-johnson','Old Fort Johnson','Fort Johnson','mohawk','fort','standing',42.95721,-74.2406,'exact','public','drive','forts','about 1749–',
  'A two-storey limestone house that Sir William Johnson built about 1749 and surrounded with fortifications. It was his home, office and trading post until he moved to Johnson Hall in 1763. His son Sir John kept it until 1776, when the local Committee of Safety confiscated it. It stayed in private hands until 1906, when the Montgomery County Historical Society opened it as a museum, and it was named a National Historic Landmark in 1972.',
  'The stone house at the corner of Routes 5 and 67, with a low stone retaining wall along the front and east side. Nothing of the fortifications is described as surviving: the museum says John Johnson removed the last of them about 1772.',
  '',
  'Owned and run as a museum by the Montgomery County Historical Society (Wikipedia and the museum\'s own page), at 2 Mergner Road; the federal public-land map does not show it, as expected for a private non-profit. Its site gave tour dates of June 3 to October 17 for 2025; the 2026 season and hours were not checked. Parking in the museum\'s lot at the intersection.',
  [W('Old Fort Johnson'),L('Old Fort Johnson (Montgomery County Historical Society)','https://www.oldfortjohnson.org/')]),
# ---- Fort Hunter and Yankee Hill: the enlarged Erie Canal ----
N('yankee-hill-lock-28','Yankee Hill Lock 28 and Putman\'s Canal Store','Fort Hunter','mohawk','canal','ruins',42.95274,-74.23784,'exact','public','walk','canal','1840s–early 1900s',
  'A lock of the enlarged Erie Canal, built during the enlargement of the 1840s, and beside it a canal store built in 1856 by the family of Garrett Putman, which served boats until the early 1900s. Both belong to Schoharie Crossing State Historic Site, which keeps a long stretch of the old canal between Fort Hunter and here.',
  'The stone lock chambers off Queen Anne Road, and the store, which has a small exhibit about canal stores inside (when it is open was not checked). The Empire State Trail passes beside them.',
  '',
  'Schoharie Crossing State Historic Site (NYS Parks). Yankee Hill Lock picnic area at 550 Queen Anne Road, Amsterdam, open sunrise to sunset daily; the Yankee Hill dock is open from mid-May to early November. No vehicle fee. No motor vehicles on the trails or grass.',
  [W('Schoharie Crossing State Historic Site'),SCX]),
N('empire-lock-29','Empire Lock 29','Fort Hunter','mohawk','canal','ruins',42.94582,-74.27349,'exact','public','walk','canal','1840s–',
  'A lock of the enlarged Erie Canal built in the 1840s by James Ott, called one of the best preserved of the enlarged canal\'s locks. The enlarged locks were doubled, with two chambers side by side. Lock 30, built by James Stewart in the village, was filled and paved over in 1956 for a change to Main Street. The Fort Hunter Canal Society was formed in the 1950s to save the ruins here, and the site\'s stretch of the original 1825 canal runs from Schoharie Creek to this lock.',
  'The double lock just east of East Church Street in Fort Hunter, on the site\'s trails.',
  '',
  'Schoharie Crossing State Historic Site (NYS Parks); grounds open sunrise to sunset daily, no vehicle fee. The visitor center at 129 Schoharie Street is open May 1 to October 31, Wednesday to Saturday 10 to 5 and Sunday 1 to 5.',
  [W('Schoharie Crossing State Historic Site'),SCX]),
N('queen-anne-parsonage','Queen Anne Parsonage','Fort Hunter','mohawk','fort','standing',42.94367,-74.26943,'site','view','drive','forts','1711 or 1712–',
  'The house built for the missionaries of Queen Anne\'s Chapel at Fort Hunter, the British fort of 1712 beside the Mohawk village called the Lower Castle. The chapel was torn down for the Erie Canal in the 1820s, and the parsonage is called the only surviving building of the fort. The state marker of 1935 says it was built in 1712 and that in 1775 the Rev. J. Stuart and Joseph Brant translated the Gospel of St. Mark into Mohawk here; the Schenectady Digital History Archive gives 1711.',
  'The house stands nearly a mile from the chapel site. Its present state and use were not checked.',
  '',
  'Who owns it was not checked; treat it as private. The state marker is on Queen Anne Road about 0.4 mile west of Main Street, at 187 Queen Anne Road: look from the road.',
  [L('HMdb: Queen Anne Parsonage','https://www.hmdb.org/m.asp?m=213140'),L('Schenectady Digital History Archive: Queen Anne\'s Chapel parsonage','https://schenectadyhistory.org/resources/mvgw/images/queen_anne_parsonage.html'),W('Fort Hunter, New York')],conf='mixed'),
# ---- Western Schenectady County ----
N('wolf-hollow-road','Wolf Hollow Road','Glenville','mohawk','civic','traces',42.9108,-74.0753,'site','public','walk','','1800s–2011',
  'A deep ravine on Hoffman\'s Fault, used as a footpath by the Mohawk and Mohican peoples between the river and the country to the north. Settlers in the 1800s made it a wagon road for hauling limestone cut from the Glenville hills. It is named as the route Kateri Tekakwitha took north in 1667, and as the place of the Battle of Kinquariones in 1669, when the Mohawks defeated the Mohicans. Cars used it until Hurricane Irene damaged it in 2011; since then the 1.1-mile road has been closed to traffic and open to walkers and bicycles.',
  'The old paved road down the gorge, with 100-foot cliffs of limestone and dolomite on one side and shale on the other, the Chaughtanoonda Creek beside it, a 1935 state marker at the south end and interpretive signs of the land conservancy and county by the upper lot (photographed in June 2025).',
  'A road that went back to the woods after one storm.',
  'Wolf Hollow Nature Trail on the old county road, listed and described by Schenectady County as one of its preserves (the federal public-land map does not show it); the Mohawk Hudson Land Conservancy has protected nearly 400 acres round it. Trailhead parking lot on Hoffman\'s Hill Road at the top: the county gives it as Route 5 west from I-890, right on Wolf Hollow Road, on to Hoffman\'s Hill Road, 1.1 miles to the lot. The county page gives no hours (not checked). A Union College geology page says the land on both sides of the road is private: stay on the road.',
  [CNTY,L('Mohawk Hudson Land Conservancy: Wolf Hollow Road','https://www.mohawkhudson.org/wolf-hollow-road'),L('HMdb: Wolf Hollow (1935 marker)','https://www.hmdb.org/m.asp?m=105175'),L('HMdb: History of Wolf Hollow Road','https://www.hmdb.org/m.asp?m=275916'),L('Union College: Geology of Wolf Hollow','https://minerva.union.edu/garverj/Regional_geology/Wolf_hollow.html')],
  th=[42.9172,-74.0699],thn='Wolf Hollow Nature Trail lot, Hoffman\'s Hill Road'),
N('wiggins-homestead-county-forest','Wiggins farm foundation and family cemetery','Duanesburg','mohawk','town','ruins',42.80233,-74.15658,'exact','public','hike','cemeteries','1810–1872',
  'The Schenectady County Forest Preserve is Great Lot 92 of the hundred lots into which James Duane divided his land. The Rockwells leased it; in 1810 "Jacob Nathaniel and Daniel Wiggins" (the marker\'s wording) leased Lot 93 next door, yet buried their dead here on their neighbour\'s land. The earliest stone is that of the elder Daniel Wiggins, who died in 1823. The marker gives 1872 both as the year his son Daniel took over the lease of Lot 92 and as the year he sold it, keeping the right to visit and use the burying ground. The county says the land was farmed in the 1700s and 1800s.',
  'Stone walls, an old farmhouse foundation and the small family cemetery in the woods. On LiDAR a small square hollow shows at the pin. The cemetery holds 12 graves according to the Schenectady County Historical Society, three of them fieldstones. OpenStreetMap labels the foundation on the Blue Trail as the Wiggins family homestead; no source read says whose house it was.',
  '',
  'Schenectady County Forest Preserve, 104 acres owned by the county (ECOS gives 102), joined by a trail to the Town of Duanesburg Forest. Open dawn to dusk; carry in, carry out. Limited hunting is allowed from November 15 to December 15 (see the county\'s rules). Parking for about eight cars on Lake Road; the Long Path\'s guide gives the trailhead lot at 42.80174, -74.15425.',
  [CNTY,L('HMdb: Wiggins Family Cemetery','https://www.hmdb.org/m.asp?m=211417'),L('ECOS: Schenectady County Forest','https://ecosny.org/schenectady-county-forest-2/'),L('NY-NJ Trail Conference: Long Path section 37 (parking)','https://trailconference.org/node/6528')],
  th=[42.80174,-74.15425],thn='Schenectady County Forest lot, Lake Road'),
]
PIN_NOTES={
 'mohasco-power-house':'An OpenStreetMap building tagged as ruins beside the creek, next to the Sticker Mule works on Forest Avenue. The pin check (state leaf-off aerial) shows the dark brick block inside the ring on the creek bank, and the LiDAR its footprint against the creek\'s cut bank.',
 'kelloggs-dam-amsterdam':'Read off the aerial: a white spill across the creek just below the Fourth Avenue bridge, where the tour guide puts Kellogg\'s Dam; the pin check shows the spill in the ring and the large mill buildings to the south-west. A waterfall site gives 42.93806, -74.17944 for a power dam here.',
 'stewarts-dam-amsterdam':'Read off the aerial: white water on the creek beside the HMdb position of the Dams and Waterfalls marker (42.94173, -74.17677), which says the dam is just north of it. The pin check shows the white water in the ring and the creek\'s rock gorge on the LiDAR.',
 'guy-park-manor':'OpenStreetMap\'s Guy Park State Historic Site park area, by the river. On the state leaf-off aerial the ring holds a building in a fenced work yard beside a canal lock and dam, which fits the restoration; the date of that aerial was not checked.',
 'old-fort-johnson':'OpenStreetMap\'s Old Fort Johnson museum point at 2 Mergner Road; the pin check shows the house in the ring, north of Route 5.',
 'yankee-hill-lock-28':'OpenStreetMap\'s "Old Yankee Hill Lock 28" ruins; Garret Putman\'s store is mapped 30 m north. The pin check shows the lock chambers in the ring on the aerial and on LiDAR, the store building just north.',
 'empire-lock-29':'OpenStreetMap\'s "Enlarged Erie Canal Empire Lock No. 29" ruins; the double chamber shows in the ring on the aerial and on LiDAR.',
 'queen-anne-parsonage':'The HMdb position of the 1935 state marker on Queen Anne Road; the pin sits on Queen Anne Road, with a house about 30 m north on the aerial that is presumably the parsonage (not confirmed). Left on the road on purpose: look from there.',
 'wolf-hollow-road':'The middle of the "Wolf Hollow Nature Trail" path as OpenStreetMap maps it (the old road); the trailhead is the striped lot on Hoffman\'s Hill Road seen on the aerial, about 60 m from the HMdb position of the History of Wolf Hollow Road marker. The LiDAR shows the deep gorge with the road along its floor; the aerial shows only trees.',
 'wiggins-homestead-county-forest':'OpenStreetMap\'s "Wiggins Family Homestead Foundation" ruins on the Blue Trail. The aerial shows only pines, but the LiDAR shows a small square hollow inside the ring, which fits a cellar. The cemetery marker is about 120 m north-east (HMdb 42.80293, -74.15545).',
}
