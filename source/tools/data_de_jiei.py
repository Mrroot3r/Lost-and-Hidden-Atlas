# November 18, 2026: Delaware, New Castle County, first pass (region drawn at random by tools/choose.py).
# Facts from the linked sources only, read in this session: Wikipedia articles through tools/wiki_raw.py, National
# Register nomination forms through tools/page.py (npgallery text layers), Delaware State Parks pages (destateparks.com),
# Delaware Public Archives marker pages, HMdb marker pages, and the Hagley and county pages named in each access note.
# Where a source is old (the 1971 and 1972 Register forms for the Brandywine mills) the text says so.
from data_b import N
from data_ma import W

DSP='https://destateparks.com'
NCC_RULES=['New Castle County park rules (county trail guide PDF): all county parks open year-round, dawn to dusk','https://delawaregreenways.org/wp-content/uploads/2021/02/Rockwood-Map.pdf']

PLACES=[
N('eastburn-jeanes-lime-kilns','Eastburn–Jeanes lime kilns','Pike Creek','de','industry','ruins',39.7415,-75.71601,'area','view','drive','','',
  'Marble from three quarries in the Pike Creek valley was burned here to make quicklime for fertilizer and mortar, and the lime went out over Limestone Road to Pennsylvania, Maryland and southern Delaware. The Jeanes and Eastburn families built the kilns and the stone buildings around them. The 1976 Register form says the industry stopped in the first decade of the 1900s.',
  'The 1976 form counted eight lime kilns and two abandoned quarries. The state marker says the kilns, houses, shops, springhouses and the ruin of the stone Eastburn barn remain. Not checked on the ground.',
  'A row of old lime kilns along a suburban road.',
  'State historical marker NC-83 gives the address as 535 Upper Pike Creek Road, Newark. Who owns the kilns was not checked; the pin is not on mapped public land, so look from the road and ask before stepping off it.',
  [['Delaware Public Archives: Eastburn-Jeanes Mining Complex marker','https://archives.delaware.gov/?p=28876'],
   ['National Register nomination (1976)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/77000389_text'],
   W('Eastburn–Jeanes Lime Kilns Historic District')],conf='mixed',brick='?'),

N('auburn-valley-mills-yorklyn','Auburn Valley mills (NVF and Marshall paper mill)','Yorklyn','de','industry','ruins',39.80751,-75.67652,'area','public','walk','','',
  'The Marshall family made paper and then vulcanized fibre beside the Red Clay Creek at Yorklyn. Their National Vulcanized Fiber plant polluted the creek with zinc. After NVF went bankrupt in 2008 most of the plant was torn down and the state bought the land; Auburn Valley State Park opened on November 9, 2018.',
  'The state park page says the park takes in the Marshall Brothers Paper Mill and the NVF plant. The National Register district inside the park lists the Auburn Mill, the Insulite Mill of 1900 and the piers of a trolley line trestle. Which mill buildings still stand, and in what state, was not confirmed from an official source.',
  'A ruined fibre-mill town turned into a state park.',
  'Auburn Valley State Park (Delaware State Parks), 3000 Creek Road, Yorklyn. The park page gives the park as open daily, 8 a.m. to sunset, and notes a closure from December 1 to March 1 without saying clearly what it covers. The Marshall Estate grounds keep shorter weekday hours. Fees not checked.',
  [['Delaware State Parks: Auburn Valley',DSP+'/History/AuburnValley'],W('Auburn Valley State Park'),W('Yorklyn, Delaware')],conf='mixed',
  th=[39.80751,-75.67652],thn='Parking lot on Yorklyn Road, on the former NVF site (state land)',brick='?'),

N('garrett-snuff-mill-yorklyn','Garrett Snuff Mill','Yorklyn','de','industry','standing',39.80861,-75.67389,'site','view','drive','','1846–1954',
  'The Garrett family made snuff on the Red Clay Creek from mills begun in the early 1730s. The complex at Yorklyn has fourteen buildings put up between 1846 and 1901, and made snuff until 1954, latterly as the George W. Helme Company.',
  'Red brick mill buildings, each one dated, and two older stone mills. A 2016 newsletter of the Friends of Auburn Heights says floods in 1999 and 2003 closed the shops that had moved in, fire destroyed the big No. 5 mill and another building, and several buildings were being restored. A 2009 state planning paper names one as Dew Point Brewing.',
  'A whole red brick snuff mill, dated building by building.',
  'Private property, partly in business use. See it from Yorklyn Road and from the Auburn Valley trail across the creek. The pin is not on mapped public land.',
  [W('Garrett Snuff Mill'),['National Register nomination (1978)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/78000913_text'],
   ['Friends of Auburn Heights newsletter, May 30, 2016: The Snuff Mills of Yorklyn','https://d8e7jbdw4fu0e.cloudfront.net/8331/0ae36900-0f41-11ed-b6ac-539b50ede322-vUViLEu.full.pdf'],
   ['DNREC: 2009 Yorklyn design guidelines','https://documents.dnrec.delaware.gov/parks/planning/auburn-valley/2016-master-plan/2009-Yorklyn-Design-Guidelines.pdf']],
  brick='yes'),

N('brandywine-springs-park','Brandywine Springs amusement park','Faulkland','de','amuse','ruins',39.7446,-75.6391,'area','public','walk','amusements,trolleyparks','1886–1923',
  'A mineral spring resort with a four-storey hotel opened here in 1826. In the late 1800s it became an amusement park along Hyde Run, with rides, a theatre and a trolley line from Wilmington. The park closed after the 1923 season. It became Delaware\'s first state park in the 1950s and passed to New Castle County in 1970.',
  'Low foundations of the park buildings along a crushed-stone path over and around Hyde Run. The Friends of Brandywine Springs have dug out foundations with archaeologists for over twenty years and put up signs at some of them. The concrete footings of the Caterpillar ride are among the sites they describe.',
  'One of the few amusement parks anyone has dug up like an archaeological site.',
  'Brandywine Springs Park, a New Castle County park, 3300 Faulkland Road. County parks are open year-round from dawn to dusk (county park rules). The county\'s own page for the park would not open.',
  [W('Brandywine Springs'),['SAH Archipedia: Brandywine Springs Park','https://archipediavm.upress.virginia.edu/buildings/DE-01-MC5'],
   ['Delaware Public Media: Brandywine Springs amusement park sites (2016)','https://www.delawarepublic.org/delaware-headlines/2016-10-28/history-matters-a-sample-of-brandywine-springs-amusement-park-sites'],
   ['Delaware Historical and Cultural Affairs: Brandywine Springs through the years','https://history.delaware.gov/2024/11/14/brandywine-springs-through-the-years/'],
   ['Friends of Brandywine Springs','http://www.fobsde.org/'],NCC_RULES],
  th=[39.74606,-75.64164],thn='Brandywine Springs Park lot, Faulkland Road',brick='?'),

N('fort-delaware','Fort Delaware','Pea Patch Island','de','fort','standing',39.58952,-75.5675,'site','boat','boat','forts','',
  'A granite and brick harbour fort designed by Joseph Totten on Pea Patch Island in the Delaware River. In the Civil War the Union held Confederate prisoners of war and others here. A concrete three-gun battery was built inside the fort in the 1890s, when it became one of three forts guarding the river with Fort Mott and Fort DuPont.',
  'The fort is gneiss, granite and brick: over two million bricks went into its casemates, magazines, barracks and ovens, and Confederate prisoners\' names are still carved into the brick of small rooms. Sandstone remnants of an earlier star fort, burned in 1831, can still be seen.',
  'A Civil War prison fort you can only reach by ferry.',
  'Fort Delaware State Park (DNREC). Ferry only, from the ticket office and dock at 45 Clinton Street, Delaware City; advance tickets online. The park page says the fort closed for the 2026 season and reopens on April 24, 2027. Wear closed-toe shoes.',
  [['Delaware State Parks: Fort Delaware',DSP+'/History/FortDelaware'],W('Fort Delaware')],
  th=[39.57844,-75.58881],thn='Lot on Clinton Street, Delaware City, near the ferry office at 45 Clinton Street',brick='some'),

N('fort-dupont-batteries','Fort DuPont gun batteries','Delaware City','de','fort','ruins',39.57197,-75.58224,'site','public','walk','forts','1897–1942',
  'Fort DuPont guarded the river with Fort Delaware and Fort Mott from 1900 to 1942. Its first works were a Civil War battery; the Endicott-era gun and mortar batteries came in 1897 to 1904. After World War II the state took over the post, and part of it became Fort DuPont State Park in 1992.',
  'The Riverview Trail along the river loops past three of the old batteries, Elder, Read and Gibson, according to the park page. The rest of the post is being redeveloped.',
  '',
  'Fort DuPont State Park (DNREC), Delaware City; the park page puts the batteries on its Riverview Trail. Open daily, 8 a.m. to sunset. The Riverview Trail is packed earth and dogs are allowed.',
  [['Delaware State Parks: Fort DuPont',DSP+'/History/FortDupont'],W('Fort DuPont')],
  th=[39.57320,-75.58078],thn='Park lot on Old Battery Lane',brick='?'),

N('delaware-city-canal-lock','Eastern lock of the Chesapeake and Delaware Canal','Delaware City','de','canal','ruins',39.57873,-75.5875,'exact','public','walk','canal','1829–1927',
  'The first Chesapeake and Delaware Canal opened in 1829 with its eastern lock here; the lock was rebuilt and enlarged in 1851 to 1854. When the sea-level canal opened without locks in 1927 every other lock was destroyed, but this one survived because the new canal entered the river two miles south at Reedy Point.',
  'A stone lock chamber without its gates. The short stretch between the lock and the river was filled in for parking, and the old canal west of the lock is a branch channel for small boats. The iron diving bell used to repair the lock stands in Battery Park.',
  'The last lock of the old canal, in a town park.',
  'Battery Park, the public riverfront park at the foot of Clinton Street, Delaware City; the diving bell plaque credits the Delaware City Community Park District with restoring the bell in 1961. Who runs the park now and its hours were not checked.',
  [['National Register nomination (1975)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/75000543_text'],
   ['SAH Archipedia: Delaware Tide Lock','https://sah-archipedia.org/node/10525'],['Delaware City: history','https://delawarecity.com/history']],
  th=[39.57844,-75.58881],thn='Lot on Clinton Street, Delaware City',brick='no'),

N('hagley-powder-yards','Hagley powder yards','Wilmington','de','industry','standing',39.78056,-75.575,'area','public','walk','','1802–1921',
  'E. I. du Pont founded black powder mills on the Brandywine in 1802 and the works became the largest black powder factory in the world. They closed in 1921. The Hagley Museum opened on the site in 1957.',
  'Restored stone powder mills along the creek, a 19th-century machine shop, a workers\' community and the first du Pont house. A narrated bus runs the Powder Yard Trail and is the only way to the house.',
  '',
  'Hagley Museum and Library, a nonprofit museum, 200 Hagley Creek Road. Admission charged ($22 for adults from February 1, 2026). Open 10 a.m. to 5 p.m. six days a week, closed Wednesdays, last admission at 4 (hours page as quoted in a search result; an older copy gives 10 to 4 after daylight saving time ends). In January only the exhibition is open and walking on the grounds is not allowed. Free parking at the visitor center.',
  [W('Hagley Museum and Library'),['Hagley: hours and tickets','https://www.hagley.org/hours-tickets'],['Hagley: plan a visit','https://www.hagley.org/visit']],
  th=[39.77494,-75.5784],thn='Hagley visitor center parking',brick='?'),

N('brecks-mill','Breck\'s Mill','Wilmington','de','industry','standing',39.77058,-75.57941,'site','view','drive','','1813–1854',
  'A mill on the Brandywine rebuilt in 1813 and rebuilt again within six weeks after a fire in 1846. It stopped working in 1854 and by the 1890s was a community house for the DuPont workers of Henry Clay village.',
  'A three-storey random stone mill with brick arches over the windows and a stone bell tower whose top storey is brick (the 1971 Register form). A 2020 magazine article says it now houses a post office, an art gallery and a studio. Walker\'s Mill stands opposite across the dam.',
  '',
  'Private, in business use, at the foot of Breck\'s Lane. Look from the lane and from the Rising Sun Lane bridge.',
  [['National Register nomination (1971)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/71000230_text'],['SAH Archipedia: Breck\'s Mill','https://sah-archipedia.org/node/10288'],
   ['The Hunt, Summer 2020, p. 37','https://digital-editions.todaymediacustom.com/hunt/summer-2020/files/basic-html/page37.html'],W("Breck's Mill Area")],
  brick='some'),

N('walkers-mill','Walker\'s Mill and Walker\'s Bank','Wilmington','de','industry','standing',39.77068,-75.57849,'site','view','drive','','1813–',
  'Joseph B. Sims built a cotton spinning mill and workers\' houses here at Rising Sun in 1813 to 1815. It took the name Walker\'s Mill in the late 1840s, and a fire in 1848 destroyed much of it before it was rebuilt.',
  'A big whitewashed stone mill beside the dam, with a tower that is stone below and brick above, and a brick arch where the race ran back into the creek (the 1972 Register form). Walker\'s Bank, the 1813 row of workers\' houses, stands beside it. A 2020 magazine article says the mill is an office building.',
  '',
  'Private. See it from Rising Sun Lane and its bridge over the Brandywine.',
  [['National Register nomination (1972)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/72000296_text'],['Walker\'s Mill history (jlmeek.com)','https://jlmeek.com/walker/brief_history.htm'],
   ['The Hunt, Summer 2020, p. 37','https://digital-editions.todaymediacustom.com/hunt/summer-2020/files/basic-html/page37.html']],
  brick='some'),

N('iron-hill-ore-pits','Iron Hill ore pits','Newark','de','industry','traces',39.63905,-75.75635,'area','public','hike','','to 1891',
  'Iron ore was dug from open pits on Iron Hill and nearby Chestnut Hill for about two hundred years, and Native Americans quarried jasper here before that. The last operator, Whitaker, sent the ore by rail to Principio Furnace in Maryland, and mining stopped in 1891. New Castle County protected about 300 acres as a park for the Bicentennial.',
  'The county\'s marker in the park says the ore pits remain clearly visible. A local magazine names the Whitaker Ore Pit, a hand-dug mine and the old jasper quarry among the park\'s remains. The pin is the marker beside the trail lot, not a pit.',
  '',
  'Iron Hill Park, a New Castle County park, reached by road from Old Baltimore Pike (Robert L. Melson Lane is blocked at Whitaker Road). County parks are open year-round from dawn to dusk. The Iron Hill Museum next door is a separate place, not part of the park.',
  [W('Iron Hill (Delaware)'),['HMdb: Historic Iron Ore Mining','https://www.hmdb.org/m.asp?m=158219'],['HMdb: Iron Hill marker','https://www.hmdb.org/m.asp?m=155424'],NCC_RULES],
  th=[39.63856,-75.75592],thn='Iron Hill Park trail lot',brick='no'),

N('lums-mill-house','Lum\'s Mill House','Kirkwood','de','landmark','standing',39.55095,-75.7131,'site','view','walk','','about 1713',
  'A two-storey, three-bay brick house built about 1713, also called the Clement House, the Samuel Davies House and the Lum House. It stands in Lums Pond State Park.',
  'The brick house. Whether it can be visited inside was not checked.',
  '',
  'Lums Pond State Park (DNREC): open daily, 8 a.m. to sunset; state park entrance fees apply in season (not checked for this park).',
  [W("Lum's Mill House"),['Delaware State Parks: Lums Pond',DSP+'/Lums']],
  th=[39.55274,-75.71244],thn='State park lot off the Little Jersey Trail',brick='yes'),

N('old-brick-store-smyrna','Old Brick Store','Smyrna','de','landmark','standing',39.322,-75.57234,'site','view','drive','','about 1764',
  'A two- to three-storey brick store built about 1764 near Smyrna, also known as the Old Brick Hotel and The Granary.',
  'The brick building. Its present use and owner were not checked.',
  '',
  'Ownership not checked; look from the road. The federal land map puts the pin inside a state-owned area called the Fox-Brickstore Landing District, so the building may be on state land, but no page saying so was found.',
  [W('Old Brick Store')],conf='mixed',brick='yes'),

N('appoquinimink-friends-meetinghouse','Appoquinimink Friends Meetinghouse','Odessa','de','civic','standing',39.45733,-75.6638,'site','view','walk','','1785',
  'A tiny Quaker meetinghouse built by David Wilson about 1785 in the village then called Cantwell\'s Bridge, now Odessa. It may be the smallest brick house of worship in the United States, and it was used as a station on the Underground Railroad.',
  'The small brick meetinghouse, restored in 1938, with a burial ground behind it whose stones run from early fieldstones to modern markers.',
  '',
  'On Main Street, Odessa. See it from the street; whether it opens was not checked.',
  [W('Appoquinimink Friends Meetinghouse')],brick='yes'),

N('ashland-covered-bridge','Ashland Covered Bridge','Ashland','de','landmark','standing',39.79827,-75.65788,'exact','public','drive','','about 1860',
  'A Town lattice truss covered bridge built about 1860 that still carries Barley Mill Road over the Red Clay Creek. Oversized trucks ignoring the signs damaged it in 2011 and 2014, and a snow plough hit it in 2017.',
  'The covered bridge, on a public road.',
  '',
  'A public road bridge on Barley Mill Road near Brackenville Road (who maintains it was not checked). Obey the height and weight signs. Parking not checked.',
  [W('Ashland Covered Bridge')],brick='?'),
]

PIN_NOTES={
 'eastburn-jeanes-lime-kilns':'Pin is a point on Upper Pike Creek Road (OpenStreetMap) about 60 m from the Register list coordinate, which fell on a house with a pool. No kiln could be picked out on the aerial or the LiDAR; the marker address, 535 Upper Pike Creek Road, geocodes about 150 m to the south-east.',
 'auburn-valley-mills-yorklyn':'Pin is the mapped parking lot on Yorklyn Road on the former NVF site (tools/parking.py); the mill remains are around it.',
 'garrett-snuff-mill-yorklyn':'Wikipedia infobox coordinate; on the aerial it sits among the mill buildings.',
 'brandywine-springs-park':'Wikipedia coordinate for the park, in the woods by Hyde Run; no foundation could be picked out on the aerial or the LiDAR.',
 'fort-delaware':'Moved about 1.5 km onto the pentagon of the fort on Pea Patch Island, read off a wide aerial with tools/pix.py; the Wikipedia coordinate fell in the island marsh.',
 'fort-dupont-batteries':'Moved 134 m east from the Wikipedia coordinate (a road circle on the old post) onto a battery that shows as concrete blocks on the LiDAR by the river (tools/pix.py). Which of the three batteries it is was not settled.',
 'delaware-city-canal-lock':'Waymarking position for the lock in Battery Park (N 39 34.724, W 75 35.250); the narrow lock chamber shows beside it on the aerial and the LiDAR.',
 'hagley-powder-yards':'Wikipedia infobox coordinate for the museum grounds, in woods above the creek; the parking point is the visitor center lot.',
 'brecks-mill':'Moved onto the building on the west bank beside the dam, opposite Walker\'s Mill, on the aerial (tools/pix.py); the district coordinate fell among houses on Breck\'s Lane.',
 'walkers-mill':'Register list coordinate; on the aerial it sits on the big mill on the east bank by the dam.',
 'iron-hill-ore-pits':'Position of the Historic Iron Ore Mining marker from Waymarking (N 39 38.343, W 75 45.381), at the trail lot. The LiDAR shows a large hollow about 100 m north-east of it that may be one of the pits; not confirmed, so the pin stays at the marker.',
 'lums-mill-house':'Register list coordinate; on the aerial it sits on the house beside the park road.',
 'old-brick-store-smyrna':'Register list coordinate; on the aerial it sits on a building at a farm lane bend.',
 'appoquinimink-friends-meetinghouse':'Register list coordinate; on the aerial it is among trees and buildings off Main Street, and the small meetinghouse could not be picked out for sure.',
 'ashland-covered-bridge':'Wikipedia infobox coordinate; on the aerial it sits on the road crossing of the creek.',
}

BATCH={'key':'de_jiei','label':'Delaware: New Castle County','added':'2026-11-18 04:16'}
