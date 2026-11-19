# November 17, 2026: Central Pennsylvania, first close pass: Huntingdon County (with Etna Furnace just over the line in
# Blair County). Iron furnaces, canal and railroad remains, the Broad Top coal country and a few standing survivors.
# Facts come from the linked sources only. Wikipedia articles were read as raw text (tools/wiki_raw.py); the DCNR park
# pages, the National Park Service page on Mt. Etna, the Penn State forest brochure and public-use page, the Friends of
# the East Broad Top museum page and the HMdb marker texts were read with tools/page.py. The National Register forms for
# this county (npgallery) are scans with no text layer and were not read. Where sources disagree the text gives both;
# where a source is silent it says "not checked".
# Pins: an OpenStreetMap feature, a Wikipedia/Register coordinate, an HMdb marker position or an address lookup, as each
# pin note says, then looked at on the pin check (aerial and LiDAR sheets) and moved with tools/pix.py where the thing
# could be seen.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
DCNR_GW=L('DCNR: Greenwood Furnace State Park','https://www.pa.gov/agencies/dcnr/recreation/where-to-go/state-parks/find-a-park/greenwood-furnace-state-park')
DCNR_TC=L('DCNR: Trough Creek State Park','https://www.pa.gov/agencies/dcnr/recreation/where-to-go/state-parks/find-a-park/trough-creek-state-park')
DCNR_TCH=L('DCNR: History of Trough Creek State Park','https://www.pa.gov/agencies/dcnr/recreation/where-to-go/state-parks/find-a-park/trough-creek-state-park/history.html')
DCNR_WD=L('DCNR: Whipple Dam State Park','https://www.pa.gov/agencies/dcnr/recreation/where-to-go/state-parks/find-a-park/whipple-dam-state-park')
HM=lambda t,n: L('HMdb: '+t,'https://www.hmdb.org/m.asp?m=%d'%n)
GW_NEAR=L('HMdb: markers at Greenwood Furnace (An Undeniable Presence, An Industry in Ruins, Greenwood Furnace)','https://www.hmdb.org/nearbylist.asp?nearby=yes&Latitude=40.6505&Longitude=-77.754&Miles=1&MilesType=1')
PSU_SVF=L('Penn State: Stone Valley Forest brochure','https://ecosystems.psu.edu/about/facilities/fmo/pdfs/svf-brochure/@@download/file/SVFbrochure.pdf')
PSU_USE=L('Penn State Forestland Management Office: public use','https://ecosystems.psu.edu/about/facilities/fmo/public-use')
NPS_ETNA=L('National Park Service: Mt. Etna Furnace','https://www.nps.gov/alpo/learn/historyculture/mtetna.htm')
RTTC=L('Rails to Trails of Central Pennsylvania (Lower Trail)','https://www.rttcpa.org/')
FEBT=L('Friends of the East Broad Top: Robertsdale Museum','https://febt.org/robertsdale-museum/')
EBT=L('East Broad Top Railroad (official site)','https://eastbroadtop.com/')
PGC_DIGEST=L('Pennsylvania Game Commission: 2026-27 Hunting and Trapping Digest (orange rule for non-hunters on game lands)','https://lawrencecountypa.gov/getmedia/ed8e94c5-f0aa-4e12-9fd1-79217f8a0ce0/PA-Game-Hunting-and-Trapping-Digest-26-27.pdf')
PLACES=[
# ---- Iron furnaces ----
N('greenwood-furnace-stacks','Greenwood Furnace stacks','Jackson Township','pac','industry','ruins',40.65180,-77.75342,'site','public','walk','','1834–1904',
  'An ironmaking village grew up here around two charcoal furnaces. The park panels say the first furnace was fired in 1834 and ran until 1880, and the second went into blast in 1867 and ran until 1904, one of the largest cold-blast charcoal furnaces built and one of the last in Pennsylvania. The dates of the second stack are not agreed: a plaque on it says it was erected in 1860, and an older state marker says the works were built about 1837. After 1904 the buildings were pulled down and the woods came back; the Civilian Conservation Corps stabilized stack 2 in 1936, and archaeologists dug at stack 1 about forty years later.',
  'Two stone stacks: stack 2, rebuilt in the 1930s, standing, and stack 1 beside it as a lower ruin, with interpretive panels. The historic district round them keeps the ironmaster\'s mansion, the company store, the Methodist church and the blacksmith shop, and a walking tour takes in parts of the town, the tramway, old roads and charcoal hearths.',
  'The last fire in a Pennsylvania charcoal iron village went out here in 1904.',
  'Greenwood Furnace State Park (DCNR), on PA 305 about 5 miles west of Belleville. Open every day sunrise to sunset; day-use areas close at dusk. The park office (8 to 4, Monday to Friday) has a visitor center on the ironworks and a free guide to the historic district. Parking by the park office and along Greenwood Road. Hours from the DCNR park page, read November 2026.',
  [DCNR_GW,GW_NEAR,W('Greenwood Furnace State Park')],conf='mixed',th=[40.65036,-77.75511],thn='Greenwood Road lot by the park office'),
N('paradise-furnace','Paradise Furnace (Mary Ann Furnace)','Todd Township','pac','industry','ruins',40.31083,-78.12611,'site','public','drive','','1830s–1869',
  'Reuben Trexler and Jacob Lesher built Trough Creek Furnace in the gorge after Trexler\'s 1818 bloomery. John Savage leased it in 1832 and renamed it Mary Ann Furnace; DCNR says that in 1835, for about a month, good iron was made here with coke as fuel, a first in the United States. Charcoal smelting went on into the 1850s or 1860s; Horatio Trexler renamed it Paradise Furnace and fired it again in 1865, and it went out of blast for good in 1869. The Civilian Conservation Corps camp that built Trough Creek State Park, opened in 1936, was named Camp Paradise Furnace.',
  'The furnace stack, about 28 feet square and 15 to 20 feet tall, of coursed rubble stone, with the 1830s stone ironmaster\'s mansion and an 18th-century two-storey log house that became the park visitor center in 1982 (Register description). Whether the visitor center still opens there was not checked.',
  '',
  'Trough Creek State Park (DCNR), along PA 994 east of Entriken. Open every day sunrise to sunset; contact the park office for facility seasons. Parking on Trough Creek Drive beside the furnace. Hours from the DCNR park page, read November 2026.',
  [DCNR_TCH,DCNR_TC,W('Paradise Furnace'),W('Trough Creek State Park')],th=[40.31051,-78.12727],thn='Trough Creek Drive lot'),
N('monroe-furnace','Monroe Furnace','Barree Township','pac','industry','ruins',40.69600,-77.89354,'exact','public','walk','','1840s–1860s',
  'General James Irvin built a charcoal furnace at the foot of Tussey Mountain in the 1840s, with a village of workers\' houses and a store. The sources disagree on its dates: Wikipedia gives 1846 to 1849 for its building and says it ran until 1863, while Penn State\'s forest brochure says it was built in 1845 and closed in 1870 because of its poor location, small size and lack of money. The land is now Penn State\'s Stone Valley Forest.',
  'The stone furnace stack, which Penn State calls all that remains of the settlement; the Register listing also counts the visible foundations of fourteen workers\' houses round it. Charcoal hearths are scattered through the forest.',
  '',
  'Penn State\'s Stone Valley Forest, which Penn State says is open to the public year-round by public roads; camping needs a free university permit. The Ironstone Trail passes the furnace beside Route 26. Hunting is allowed in the forest. Hours were not checked. Where to park nearest the furnace was not checked: the lot OpenStreetMap maps on Rybacki Road just south of it looked like open meadow on the aerial.',
  [PSU_SVF,PSU_USE,W('Monroe Furnace')],conf='mixed'),
N('huntingdon-furnace','Huntingdon Furnace','Franklin Township','pac','industry','standing',40.65815,-78.11506,'site','view','drive','','1796–1880s',
  'An iron furnace that, per Wikipedia, began in 1796 and was moved to this site in 1805 from its first site a mile upstream, then worked until the 1880s. Its village survives: an office, the ironmaster\'s mansion (1851), a log worker\'s house, a farm manager\'s house, a stone grist mill (1808) and the miller\'s house.',
  'The furnace, about 30 feet square and 30 feet high, with the mill and houses of the old ironworks, on Huntingdon Furnace Road (Register description; what stands now was not checked).',
  '',
  'Private land; look from Huntingdon Furnace Road and do not enter without the owner\'s leave. Who owns it now was not checked.',
  [W('Huntingdon Furnace')]),
N('barree-furnace','Barree Forge and Furnace','Porter Township','pac','industry','ruins',40.58833,-78.10111,'site','ask','drive','','c.1797–1880s',
  'An ironworks on the Juniata whose forge was built about 1797; the stone furnace stack is dated 1864, and the works closed in the 1880s. The United Methodist Church bought the property in 1963 for a church camp, Greene Hills.',
  'The furnace stack, 30 feet square and 6 to 15 feet high in coursed limestone, the 1830s ironmaster\'s mansion (brick, painted white), a barn and the forge site (Register description; not checked on the ground).',
  '',
  'A private church camp. Ask the camp before visiting; how it handles visitors was not checked.',
  [W('Barree Forge and Furnace')]),
N('juniata-iron-works','Juniata Iron Works (Hatfield Iron Works)','Porter Township','pac','industry','standing',40.54248,-78.08586,'area','view','drive','','1840s–1870s',
  'An ironworks first built on the south side of the Frankstown Branch of the Juniata and moved to the north bank in the late 1840s. It closed in the mid-1870s and its machinery was taken out. What is left is the works\' village: two ironmaster\'s mansions (1841 and 1867), a store and post office, a grist mill (1856) and two workers\' houses.',
  'Brick mansions, the mill and the store; Wikipedia says the store houses a bed and breakfast. No furnace remains are described.',
  '',
  'Private houses; look from the road. Ownership was not checked.',
  [W('Juniata Iron Works')]),
N('pennsylvania-furnace-pa','Pennsylvania Furnace','Franklin Township','pac','industry','standing',40.70172,-77.99935,'area','view','drive','','c.1810–1888',
  'An iron works set up about 1810, first making charcoal iron and later using coke; iron was made here as late as 1888 (state marker, 1947). The ironmaster\'s mansion is listed on the National Register.',
  'The state marker says the remaining buildings were part of the iron works; which ones stand now was not checked.',
  '',
  'Private land. The marker stands at Spruce Creek Road and Johnson Road; look from the road.',
  [HM('Pennsylvania Furnace',91028)],conf='mixed'),
N('etna-furnace','Etna Furnace and the Lower Trail canal works','Catharine Township','pac','industry','ruins',40.52334,-78.17934,'site','ask','walk','canal','1805–1875',
  'An iron village that grew from 1805 round a furnace of 1808 and prospered with the Pennsylvania Main Line Canal, which ran past it from 1832 to 1875, when a flood wrecked it and the railroad shut it. The Register district counts the stone furnace, canal locks, a lock keeper\'s house site, an aqueduct (rebuilt 1848), charcoal house ruins, tenant houses, a store and paymaster\'s office, a church of 1860 and a cemetery. The Park Service says the ironmaster\'s mansion was gutted by arson.',
  'From the Lower Trail the Park Service says you can see the mansion at about the trail\'s midpoint, the foundation of a lock tender\'s house marked by a sign upstream, cut-stone bridge abutments, an old railroad bridge on the piers of a canal aqueduct, and, about two miles downstream, the abutments and part of the guard lock at Willow Dam. Whether the furnace stack itself can be seen from public ground was not checked.',
  '',
  'The Lower Trail, owned by Rails to Trails of Central Pennsylvania, is open free to walkers, cyclists and riders; no motor vehicles. Parking at the Mount Etna trail lot on Fox Run Road. The furnace and mansion are on land whose owner was not checked: ask first. Trail hours were not checked.',
  [NPS_ETNA,RTTC,W('Etna Furnace (Williamsburg, Pennsylvania)'),W('Lower Trail')],th=[40.52044,-78.17188],thn='Mount Etna trail lot, Fox Run Road'),
# ---- Canal, rail and bridges ----
N('corbin-bridge','Corbin Bridge','Juniata Township','pac','landmark','standing',40.45472,-77.98306,'site','public','drive','','1937',
  'A one-lane suspension bridge over the Raystown Branch of the Juniata, built in 1937 by Reading Steel Products, 322 feet long with a 12.5-foot deck. It is the only road suspension bridge in Huntingdon County.',
  'The steel towers and cables carrying Corbin Road over the river. The Bridgemeister inventory listed it in use in 2021; whether it is open today was not checked.',
  '',
  'A county road bridge (Township Road 428, Corbin Road). Drive or walk across; one lane.',
  [W('Corbin Bridge'),L('Bridgemeister: Corbin\'s','https://bridgemeister.com/bridge.php?bid=187')]),
N('huntingdon-1850-arch','Pennsylvania Railroad 1850 stone arch, Huntingdon','Huntingdon','pac','rail','standing',40.48140,-78.00377,'site','view','walk','','1850',
  'This stone arch carried the first single-track Pennsylvania Railroad line into Huntingdon in 1850; the engine "Henry Clay" arrived on June 6. After the 1889 flood destroyed much of the canal, the railroad bought the canal bed and moved its tracks to it, nearer the river, so this bridge over Standing Stone Creek was left behind. The Huntingdon Rotary Club restored it.',
  'The restored arch over Standing Stone Creek with the Rotary Club\'s marker; the present railroad bridge follows the line of the old canal aqueduct.',
  '',
  'In the borough of Huntingdon; the marker stands on Penn Street. Look from the street. Who owns the arch was not checked.',
  [HM('Transition From Canal Era To Railroads At Huntingdon, PA',177102)]),
N('st-marys-covered-bridge','St. Mary\'s Covered Bridge','Cromwell Township','pac','landmark','standing',40.20589,-77.87811,'exact','view','drive','','1889',
  'A Howe truss covered bridge on cut stone abutments over Shade Creek, built in 1889. It is the only covered bridge left in Huntingdon County.',
  'The covered bridge itself. Whether it still carries traffic was not checked.',
  '',
  'Look from the road. Ownership and whether the bridge is open were not checked.',
  [W("St. Mary's Covered Bridge")]),
# ---- Broad Top coal country ----
N('east-broad-top-rockhill','East Broad Top Railroad, Rockhill Furnace','Rockhill Furnace','pac','rail','standing',40.24146,-77.89900,'site','open','drive','stations','1871–1956',
  'A three-foot-gauge coal railroad that ran from 1871 to 1956 and was kept whole afterwards: Wikipedia calls it one of the oldest and best preserved narrow-gauge lines in America. Tourist trains ran until 2011; a non-profit foundation bought it in February 2020 and trains returned in 2021. It was made a National Historic Landmark in 1964.',
  'The station on Meadow Street and the original shops, with a pair of Babcock and Wilcox boilers, a 19th-century stationary steam engine and overhead line shafts; all six of the line\'s last narrow-gauge steam engines are still on site, with the 1927 M-1 motor car and more than 150 hoppers.',
  'A whole railroad that simply stopped in 1956 and was never broken up.',
  'Owned and run by the non-profit EBT Foundation since 2020 (Wikipedia); the station is at 421 Meadow Street. Train days, shop tours and fares were not checked (the railroad\'s own site refused the page reader): see eastbroadtop.com.',
  [W('East Broad Top Railroad and Coal Company'),HM('East Broad Top Railroad',32389),EBT]),
N('robertsdale-pa','Robertsdale coal town','Wood Township','pac','town','standing',40.18252,-78.11496,'site','view','drive','stations','1872–1956',
  'A company town founded in 1872 by the Rockhill Iron and Coal Company as the first terminus and mining headquarters of the East Broad Top. The deep mines closed by the early 1950s (Mine No. 1 in 1951), and the coal company shut down in 1956 with the railroad. The town is a Register historic district of 102 buildings dating from about 1873 to the 1920s.',
  'The company store (1873-74), the coal company office (1914), the post office, the 1914 East Broad Top depot, a hotel, the 1948 Reality Theatre and miners\' houses. The Friends of the East Broad Top run a free museum in the old company post office and the station, with walking tours of the EBT yard and mine area and rail-bike rides on a mile of restored track; the Broad Top Area Coal Miners Museum is in the former Methodist church.',
  '',
  'Public streets through a lived-in village: the houses are private. The Friends\' museum (570 South Main Street) was open Saturdays May to October, 10 to 5, in its 2025 season, with walking tours at 11, 1 and 3; admission free (Friends of the East Broad Top page, read November 2026). The coal miners\' museum\'s hours were not checked.',
  [FEBT,W('Robertsdale, Pennsylvania'),W('Robertsdale Historic District'),W('Broad Top Area Coal Miners Museum')]),
N('minersville-coke-ovens','Minersville coke ovens','Carbon Township','pac','industry','ruins',40.21760,-78.18333,'site','ask','walk','','1875–1920s',
  'A coal and coke works founded in 1875 east of Coalmont. In 1925 it had ninety beehive ovens and sixty-seven unfinished Mitchell ovens. The Register listing covers the oven rows, the pillars of the tipple, the foundations of the supply house, engine and power house, substation, hoist house and blacksmith shop, the railroad beds and the Gordon Mine.',
  'Rows of beehive oven ruins and mine-works foundations (Register description). A 2017 blog visit found only part of the site on State Game Lands and the rest posted as private.',
  '',
  'Partly State Game Lands 67 (Pennsylvania Game Commission) and partly private, posted land: stay on the game lands and do not cross posted ground. A mapped parking spot on the game lands is just north-east of the ovens off PA 913. Non-hunters must wear fluorescent orange on game lands from October 1 to January 31 and April 20 to May 31 (Game Commission digest 2026-27). Where the game-land boundary runs through the ovens was not checked.',
  [W('Minersville Coke Ovens'),L('Discovery PA blog: Minersville Coke Ovens (2017)','https://discoverypa.blogspot.com/2017/05/minersville-coke-ovens.html'),PGC_DIGEST],conf='mixed',th=[40.21882,-78.18288],thn='State Game Lands 67 parking'),
# ---- Lumber era ----
N('whipple-dam','Whipple Dam','Jackson Township','pac','water','standing',40.68304,-77.86581,'area','public','walk','','1860s–',
  'Osgood M. Whipple built a dam here in the lumber boom to power his sawmill; he left the business in 1897 and locals kept using the pond. The state Department of Forests and Waters rebuilt the dam in 1928, and the land became Whipple Dam State Park. Before the lumbermen, this ground belonged to the Monroe iron works.',
  'The dam and its lake. Wikipedia says remnants of the iron-ore mines can be seen in the park. On the aerial used for the pin check (date not known) the lake bed lay empty; whether the lake is full now was not checked.',
  '',
  'Whipple Dam State Park (DCNR), off PA 26 about 12 miles south of State College, run from the Greenwood Furnace office. Open every day sunrise to sunset; day-use areas close at dusk. Hours from the DCNR park page, read November 2026.',
  [DCNR_WD,W('Whipple Dam State Park')]),
]
PIN_NOTES={
 'greenwood-furnace-stacks':'HMdb position of the "An Industry in Ruins" panel, which stands in front of the two stacks (an OpenStreetMap information board is mapped at the same spot on Broad Mountain Road). The stacks are under tree cover on the aerial; the LiDAR shows a raised block beside the pin.',
 'paradise-furnace':'Wikipedia/Register coordinate, on the open ground by Trough Creek Drive; the stack itself was not picked out on the aerial or LiDAR.',
 'monroe-furnace':'OpenStreetMap historic=ruins point "Monroe Furnace" on the Ironstone Trail; the 1 m LiDAR shows a raised mound right under the pin.',
 'huntingdon-furnace':'OpenStreetMap historic=ruins point "Huntingdon Furnace"; the LiDAR shows a tall square mass at the pin, in a yard about 80 m from the road.',
 'barree-furnace':'Wikipedia/Register coordinate, in trees by a road junction; the LiDAR shows a small raised ring at the pin, perhaps the stack (not certain).',
 'juniata-iron-works':'The Register coordinate fell in a ploughed field with no buildings; moved about 40 m onto the public road that runs past the farm buildings to the west. Which buildings are the iron works was not picked out, so area.',
 'pennsylvania-furnace-pa':'HMdb position of the 1947 state marker at Spruce Creek and Johnson roads, on the road junction on the aerial; the Register coordinate for the mansion (40.7036, -78.0131) is about a kilometre west, so area.',
 'etna-furnace':'OpenStreetMap historic=ruins point "Etna Furnace" on Etna Furnace Road; the LiDAR shows a mound against the hillside at the pin.',
 'corbin-bridge':'Wikipedia/Register coordinate; it falls on the bridge deck on the aerial.',
 'huntingdon-1850-arch':'HMdb position of the Rotary Club marker beside the arch on Penn Street; the Register coordinate, about 100 m south-west, fell at the creek mouth.',
 'st-marys-covered-bridge':'Moved about 20 m from the Register coordinate onto the grey-roofed covered span seen on the aerial beside US 522 and the church.',
 'east-broad-top-rockhill':'ArcGIS address lookup of 421 Meadow Street; it falls on the red-roofed station, with the roundhouse visible to the south-west.',
 'robertsdale-pa':'ArcGIS address lookup of 570 South Main Street, the Friends of the East Broad Top museum; it falls on Main Street beside the building.',
 'minersville-coke-ovens':'The Register coordinate is in woods with nothing to see; moved about 125 m north-east onto a long straight double bench on the 1 m LiDAR, read as a bank of ovens (an interpretation, not confirmed). It shows again at the edge of the game-lands parking tile.',
 'whipple-dam':'The DCNR park GPS point was on a road in the woods; moved about 120 m to where the lake bed narrows at its downstream end on the aerial, read as the dam. Not certain, so area.',
}
BATCH={'key':'pac_eclm','label':'Huntingdon County, Pennsylvania','added':'2026-11-17 21:05'}
