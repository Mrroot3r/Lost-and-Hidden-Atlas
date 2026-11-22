# November 22, 2026: a first scatter across Arkansas, the state with the fewest places on the map when this session began
# (22). Region claimed with tools/choose.py --thinnest (ar). The batch is spread over the corners the map lacked: the
# northwest Ozarks (Monte Ne, Eureka Springs, the Buffalo River), Fort Smith, Petit Jean Mountain, Hot Springs, Camden,
# the Delta (Helena, Dyess, Lake Village, Rohwer, Arkansas Post, Pine Bluff), the northeast river towns (Jacksonport,
# Powhatan, Mammoth Spring) and North Little Rock.
# Sources read in this session: Wikipedia articles and county Register lists (tools/wiki_raw.py), and the pages of whoever
# runs each place (Arkansas State Parks, the National Park Service, Arkansas State University Heritage Sites, the City of
# North Little Rock, the Ouachita County Historical Society, the Department of Arkansas Heritage, Explore Pine Bluff), the
# Encyclopedia of Arkansas (Monte Ne, Helena Depot), read with tools/page.py. Nothing was checked on the ground.
from data_b import N
from data_ma import W
BATCH={'key':'ar_tsiw','label':'Arkansas: a first scatter across the state','added':'2026-11-22 03:21'}

ASP='https://www.arkansasstateparks.com/parks/'
EOA='https://encyclopediaofarkansas.net/entries/'

PLACES=[
N('monte-ne-resort-ruins','Monte Ne resort (Coin Harvey\'s drowned resort)','Monte Ne','ar','hotel','water',36.285556,-94.069722,'area','public','walk','hotels,drowned','1901–1920s',
  'A health resort and planned town that William Hope "Coin" Harvey ran from 1901 into the 1920s, with hotels, an indoor pool, its own bank, post office and rail line. Harvey then spent his money on a terraced concrete amphitheater meant as the foot of a 130-foot "Pyramid" that was never built; the 1931 Liberty Party convention that nominated him for president met there. He died at Monte Ne in 1936 and was buried in a concrete vault. Beaver Lake, made by a dam in the 1960s, flooded nearly all of it.',
  'Most of the time very little. The amphitheater and old bridges show only when Beaver Lake is very low (1977, 2006). The Corps of Engineers demolished the last Oklahoma Row hotel tower in February 2023 (Wikipedia); the Encyclopedia of Arkansas says the Corps began removing Oklahoma Row in 2023 and still lists parts of two hotels and Harvey\'s tomb as visible, so what stands today was not confirmed. Wikipedia says the tomb is on private land and seen from the Monte Ne boat launch.',
  '',
  'The flooded resort is on U.S. Army Corps of Engineers land at Beaver Lake; Harvey\'s tomb is on private land: look from the launch. Parking: the Monte Ne lakeside launch (Encyclopedia of Arkansas); no lot was found on the map and the launch was not checked on the aerial. Corps rules and hours not checked. Do not climb on what is left: the Corps took the tower down over safety.',
  [W('Monte Ne'),['Encyclopedia of Arkansas: Monte Ne',EOA+'monte-ne-benton-county-334/']],conf='mixed',brick='?'),

N('crescent-hotel-eureka-springs','Crescent Hotel','Eureka Springs','ar','hotel','standing',36.4083,-93.7374,'site','open','drive','hotels','1886',
  'A resort hotel built in 1886 at 75 Prospect Avenue to designs by the St. Louis architect Isaac S. Taylor, with electricity and elevators from the start. It struggled as a hotel, became the Crescent College and Conservatory for Young Women in 1908, a summer hotel again after 1934, and from 1937 the "hospital" of the fraudulent cancer-cure promoter Norman Baker. It was restored and is a working hotel again, a member of Historic Hotels of America.',
  'The hotel on its hill above the town, with its basement spa restored. The hotel\'s own page says guided tours and activities are planned every day; times and the parts of the building shown were not checked. Interior otherwise not checked.',
  '',
  'Privately owned working hotel (Wikipedia names Elise Roenigk as owner). Parking not checked.',
  [W('Crescent Hotel (Eureka Springs, Arkansas)'),['Crescent Hotel','https://crescent-hotel.com/']],brick='?',hours='?'),

N('parker-hickman-farmstead-erbie','Parker–Hickman Farmstead','Erbie','ar','landmark','standing',36.070993,-93.222466,'site','public','drive','','1840s–1980s',
  'A farm on the Buffalo River bottomlands begun by the Parker brothers, who came from Tennessee in the 1830s. Its house was built of local red cedar logs dated to the 1840s, which the Park Service calls the oldest log structure in the Buffalo National River. Nine owners lived on it for about 130 years, the last the Hickmans in the early 1980s.',
  'The log house with its later additions and the outbuildings and farm buildings set roughly in a rectangle round it; a panel on site maps the farm and says what each building was for. Interior not checked.',
  '',
  'National Park Service, Buffalo National River (Upper District), near Erbie Campground. The Park Service page lists auto parking and exhibits at the site. Hours not checked.',
  [['NPS: Parker-Hickman Farmstead','https://www.nps.gov/places/parker-hickman-farmstead.htm'],W('Parker–Hickman Farm Historic District')],brick='no'),

N('fort-smith-national-historic-site','Fort Smith National Historic Site','Fort Smith','ar','fort','standing',35.38821,-94.42983,'site','open','walk','forts','1817–1871',
  'The Army built the first Fort Smith here in 1817 and a second fort near its ruins from 1838; the second was used until 1871. From 1872 the federal court for the Western District of Arkansas, with jurisdiction over all of Indian Territory, sat in the old barracks, best known for Judge Isaac C. Parker\'s two decades on the bench.',
  'The barracks, courthouse and jail building (now the visitor center and museum), the commissary of about 1838, the foundation remains of the first fort of 1817 to 1824, a reconstruction of the court\'s gallows, and a riverside trail with Trail of Tears exhibits.',
  '',
  'National Park Service, visitor center at 301 Parker Avenue. Hours from the park\'s hours page (winter hours shown, in effect November 14, 2026 to March 31, 2027); closed New Year\'s Day, Thanksgiving and Christmas. Parking not checked.',
  [W('Fort Smith National Historic Site'),['NPS: Fort Smith hours','https://www.nps.gov/fosm/planyourvisit/hours.htm']],brick='?',
  hours='Winter: visitor center Tue–Sat 9 a.m.–5 p.m.; gallows and commissary Tue–Sat 9:15–4:45; grounds daily 30 min before sunrise to 11 p.m.'),

N('mather-lodge-petit-jean','Mather Lodge, Petit Jean State Park','Morrilton','ar','hotel','standing',35.11722,-92.93833,'site','open','drive','hotels','1935',
  'The lodge of Arkansas\'s first state park, built in 1935 by a Civilian Conservation Corps crew in the Rustic style. The CCC also built the park\'s trails, roads, bridges and cabins from 1933 out of native log and stone.',
  'Log and stone CCC work in the lodge and across the park. Still a working lodge with a restaurant. Interior not checked.',
  '',
  'Arkansas State Parks. Hours from the park\'s page; visitor center daily 8 a.m. to 5 p.m. Parking not checked.',
  [W('Mather Lodge'),['Arkansas State Parks: Petit Jean',ASP+'petit-jean-state-park']],brick='?',
  hours='Lodge open all year, 24 hours; restaurant daily 7 a.m.–9 p.m. March–November, 8 a.m.–8 p.m. December–February'),

N('fordyce-bathhouse-hot-springs','Fordyce Bathhouse, Bathhouse Row','Hot Springs','ar','hotel','standing',34.51372,-93.05347,'exact','open','walk','','1914–1962',
  'The grandest bathhouse on Bathhouse Row, built in 1914 and 1915 to designs by George Mann and Eugene John Stern and open from 1915 to 1962, the first on the Row to close. It stood empty until it reopened in 1989 as the visitor center of Hot Springs National Park.',
  'Cream-coloured brick with terra cotta, on a Batesville limestone base. Inside, free to walk through: the marble lobby and bath halls, stained glass in the Men\'s Bath Hall ceiling and the third-floor Music Room, dressing rooms, a gymnasium, the only bowling alley on the Row, and in the basement the Fordyce Spring and the original Otis elevator machinery (Park Service page).',
  '',
  'National Park Service, 369 Central Avenue. Free self-guided tour. The park\'s hours page lists the other bathhouses but gave no hours for the Fordyce; hours not checked. Parking not checked.',
  [W('Bathhouse Row'),['NPS: Fordyce Bathhouse','https://home.nps.gov/hosp/planyourvisit/fordyce-bathhouse.htm']],brick='no',hours='?'),

N('mccollum-chidester-house-camden','McCollum–Chidester House','Camden','ar','landmark','standing',33.584722,-92.842222,'site','open','drive','','1847',
  'A wood-frame house built in 1847 by Peter McCollum and sold ten years later to Colonel John T. Chidester. The Ouachita County Historical Society runs it as a museum, with the Leake-Ingham Building, a law office, behind it.',
  'The house and the Leake-Ingham Building behind it. Interior not checked.',
  '',
  'Ouachita County Historical Society, 926 Washington Street NW. Hours from the society\'s page, which warns that a small nonprofit\'s hours can be shorter. Street parking; not checked.',
  [W('McCollum-Chidester House'),['Ouachita County Historical Society','https://ouachitacountyhistoricalsociety.org']],brick='no',
  hours='Tours Wednesday–Saturday 9 a.m.–4 p.m.'),

N('helena-depot-delta-cultural-center','Helena Depot (Delta Cultural Center)','Helena-West Helena','ar','rail','standing',34.5219,-90.5858,'site','open','walk','stations','1912',
  'A Missouri Pacific depot of about 1912, on the site of an Arkansas Midland Railroad depot (the Encyclopedia of Arkansas says it first appears on a 1914 map and was finished by 1918). In 1990 it became the first building of the Delta Cultural Center, a state museum of the Arkansas Delta.',
  'Red brick with reddish mortar and rounded brick edges, a two-storey front under a hipped roof with big eaves on knee braces, limestone trim; the old breezeway between its two parts was bricked in. Inside is the museum.',
  '',
  'Department of Arkansas Heritage, 95 Missouri Street. Free. Hours from its page ("unless specified"). Street parking; not checked.',
  [W('Delta Cultural Center'),['Encyclopedia of Arkansas: Helena Depot',EOA+'helena-depot-7736/'],['Delta Cultural Center','https://www.arkansasheritage.com/delta-cultural-center']],brick='yes',
  hours='Tuesday–Saturday 9 a.m.–5 p.m.'),

N('dyess-colony-administration-building','Dyess Colony: administration building and Johnny Cash boyhood home','Dyess','ar','town','standing',35.59007,-90.21469,'site','open','drive','','1934',
  'A New Deal farm colony founded in 1934 by the Federal Emergency Relief Administration, with about 500 farms of 20 or 40 acres for poor families. Johnny Cash grew up here, in a farm house of 1934. Arkansas State University bought the house in 2011 and runs it with the colony\'s administration building as a museum.',
  'The colony\'s administration building, now a museum, with the visitor center beside it; the Cash boyhood home is about 3 km west on the tour. Interior not checked.',
  '',
  'Arkansas State University Heritage Sites. Tours begin at the Dyess Colony visitor center; admission charged (from $25 for the boyhood home tour). Closed December 24 to 26 and December 31 to January 2. Parking not checked.',
  [W('Dyess, Arkansas'),W('Johnny Cash Boyhood Home'),['A-State: Plan a Visit','https://www.astate.edu/outreach/history-and-heritage/heritage-sites/dyess-cash/visit.html']],brick='?',
  hours='Boyhood home tours Monday–Saturday, hourly 9 a.m.–3 p.m.'),

N('lakeport-plantation','Lakeport Plantation','Lake Village','ar','landmark','standing',33.25740,-91.15516,'site','open','drive','','about 1859',
  'A Greek Revival plantation house built about 1859 by Lycurgus Johnson on a cotton plantation his father Joel Johnson began in 1831 with enslaved labour; by 1860 Johnson held more than 155 people in slavery. The family kept it until 1927. Arkansas State University restored it from 2003 to 2008 and opened it as a museum in 2007.',
  'The restored house, with exhibits on the lives and labour of the people enslaved there. Guided or self-guided tours from the visitor center. Interior not checked beyond that.',
  '',
  'Arkansas State University Heritage Sites, 601 Highway 142. Admission $15 guided, $10 self-guided. The museum warns that maps may route you onto the unpaved levee road. Closed November 26 and 27, 2026 and December 19, 2026 to January 3, 2027. Parking not checked.',
  [W('Lakeport Plantation'),['A-State: Plan a Visit','https://www.astate.edu/outreach/history-and-heritage/heritage-sites/lakeport-plantation-museum/visit.html']],brick='?',
  hours='Monday–Friday 9 a.m.–3:30 p.m.'),

N('rohwer-relocation-center-cemetery','Rohwer Relocation Center cemetery and camp site','Rohwer','ar','burial','traces',33.766389,-91.280278,'site','public','drive','cemeteries','1942–1945',
  'One of two camps in the eastern half of the country where Japanese Americans were held during the Second World War: more than 8,000 people were confined at Rohwer from 1942 to 1945. The people held there designed and built the cemetery in 1943 and 1944, one of only three such camp cemeteries left in the country, now a National Historic Landmark.',
  'The cemetery: two historic concrete monuments, one to Japanese American soldiers killed in Europe, 24 low concrete headstones, entrance markers, posts and a bench carved with a sun and moon, all made by the incarcerees, and cherry trees planted in 1994. A memorial, panels and audio kiosks tell the camp\'s story. The rest of the camp is farmland again; Wikipedia names the old high school gym as the largest structure left.',
  '',
  'An Arkansas State University heritage site with a memorial and kiosks; the federal land map shows no public land here and who owns the cemetery ground was not checked. The aerial shows a farm track to it. The camp land around it is farmed: stay at the cemetery. The museum for the camp is in McGehee. Hours and parking not checked.',
  [W('Rohwer War Relocation Center'),['NPS: Rohwer Relocation Center Memorial Cemetery','https://www.nps.gov/places/rohwer-relocation-center-memorial-cemetery.htm'],['A-State: Rohwer','https://www.astate.edu/outreach/history-and-heritage/heritage-sites/rohwer/']],brick='?'),

N('arkansas-post-national-memorial','Arkansas Post National Memorial','Gillett','ar','fort','traces',34.020833,-91.348333,'area','public','walk','forts','1686–1863',
  'The trading post Henri de Tonti founded for France in 1686 to trade with the Quapaw, moved more than once along the lower Arkansas River, later Spanish and then American, and the first capital of Arkansas Territory from 1819 to 1821. The French and Spanish forts at this site, and the Confederate Fort Hindman taken in 1863, are gone into the river: erosion took them and left no trace of the old waterfront.',
  'Parts of the Confederate road, trenches and artillery positions; an early 1800s well and cistern; the site of the town, where archaeologists found the French colonial village; partial reconstructions the Park Service made in 1964. A state museum stands on the rest of the grounds.',
  '',
  'National Park Service, 1741 Old Post Road. Hours from the superintendent\'s compendium; the visitor center is closed Thanksgiving, Christmas and New Year\'s Day. The Menard-Hodges Mounds in the Osotouy Unit are closed to the public. Parking not checked.',
  [W('Arkansas Post'),['NPS: Superintendent\'s compendium','https://www.nps.gov/arpo/learn/management/arpo-superintendent-s-compendium.htm']],brick='?',
  hours='Grounds daily 7 a.m. to sunset; visitor center Thursday–Monday 8:30 a.m.–5 p.m.'),

N('union-station-pine-bluff','Union Station','Pine Bluff','ar','rail','standing',34.22611,-92.00167,'site','view','walk','stations','1906',
  'A station built in 1906 by the Iron Mountain Railroad at the junction of the Cotton Belt and the Iron Mountain. It holds the Pine Bluff/Jefferson County Historical Museum.',
  'A one-storey brick building under a hip roof whose long eaves rest on iron columns and half-truss brackets. Interior not checked.',
  '',
  'The museum\'s page (Explore Pine Bluff) says it is temporarily closed after winter weather damage and gives its usual hours as Thursday to Saturday 10 a.m. to 2 p.m., free; look from the street until it reopens. Parking not checked.',
  [W('Union Station (Pine Bluff, Arkansas)'),['Explore Pine Bluff: the museum','https://www.explorepinebluff.com/pine-bluff-jefferson-co-museum']],brick='?'),

N('old-mill-north-little-rock','The Old Mill (T. R. Pugh Memorial Park)','North Little Rock','ar','landmark','standing',34.79167,-92.24917,'site','public','walk','','1933',
  'A re-creation of a water-powered grist mill built in 1933 by the developer Justin Matthews as a draw for his Park Hill and Lakewood subdivisions. The concrete was worked by the sculptor Dionicio Rodriguez to look like wood, iron and steel. The mill appears in the opening scenes of Gone with the Wind.',
  'Faux bois concrete throughout the mill, bridges and park. Inside is an iron grist mill dated 1828 from the Cagle family mill in Pope County.',
  '',
  'City of North Little Rock Parks and Recreation. Hours from the city\'s page; no pets. Parking not checked.',
  [W('T. R. Pugh Memorial Park'),['North Little Rock: The Old Mill','https://nlr.ar.gov/departments/parks-and-recreation/parks/old-mill/']],brick='?',
  hours='Daily 8 a.m. to sunset'),

N('jacksonport-courthouse','Jacksonport Courthouse','Jacksonport','ar','civic','standing',35.63934,-91.31157,'area','open','walk','','1872',
  'The courthouse of 1872 of a steamboat town at the meeting of the White and Black rivers, the county seat from 1852 (the park says) and home of county government until 1892. The Jackson County Historical Society bought the derelict building in 1961 and it opened as a museum in 1976.',
  'The restored red brick courthouse with a gazebo on its lawn (Commons photograph), furnished with exhibits. The park\'s museum steamboat, the Mary Woods No. 2, sank at its moorings in January 2010 (Wikipedia); whether anything of it is still there was not checked. Interior not checked.',
  '',
  'Arkansas State Parks, Jacksonport State Park, 111 Avenue Street. Admission free. Hours from the park\'s page; closed New Year\'s Day, Thanksgiving, Christmas Eve and Christmas Day. Parking at the state park lot on Adams Street.',
  [W('Jacksonport State Park'),['Arkansas State Parks: Jacksonport',ASP+'jacksonport-state-park']],brick='yes',th=[35.63894,-91.31080],thn='Jacksonport State Park lot, Adams Street',
  hours='March–November Wed–Sat 8 a.m.–5 p.m., Sun 1–5; December–February Wed–Fri 8–5, Sat–Sun 1–5'),

N('powhatan-courthouse','Powhatan Courthouse and village','Powhatan','ar','civic','standing',36.08214,-91.11879,'site','open','walk','','1873–1888',
  'A Black River steamboat town and the seat of Lawrence County from 1869 to 1968. Its two-storey brick courthouse on a stone foundation dates from 1888. The railroad crossed the river at Black Rock instead in 1883, and the town declined.',
  'The courthouse, now the visitor center and museum, free. Guided tours of the other buildings on their original sites: the 1873 limestone jail (the only building left from the first courthouse\'s time), a log house, the Male and Female Academy, the Methodist church and the one surviving commercial building of the 1880s.',
  '',
  'Arkansas State Parks, Powhatan Historic State Park, 4414 Highway 25. Hours from the park\'s page; closed New Year\'s Day, Thanksgiving, Christmas Eve and Christmas Day. Park lot on Highway 25.',
  [W('Powhatan Historic State Park'),['Arkansas State Parks: Powhatan',ASP+'powhatan-historic-state-park']],brick='?',th=[36.08216,-91.11919],thn='State park lot, Highway 25',
  hours='Courthouse museum Wednesday–Saturday 8 a.m.–5 p.m., Sunday 1–5 p.m.'),

N('frisco-depot-mammoth-spring','Frisco depot, Mammoth Spring','Mammoth Spring','ar','rail','standing',36.49572,-91.53300,'area','open','walk','stations','1885–1886',
  'A Victorian depot of the Kansas City, Fort Scott and Memphis Railroad, later the Frisco, that linked the spring town to the railway. The state park gives 1886 as its year, and Wikipedia gives both 1886 and 1885; it was restored in 1971 and is a railroad museum.',
  'A long one-storey red brick depot under a grey hipped roof (Commons photograph of the depot). Inside, railroad memorabilia and a restored caboose. Interior not checked.',
  '',
  'Arkansas State Parks, Mammoth Spring State Park. Hours from the park\'s page: the depot museum is closed from December 14 to March 1. Park gates 8 a.m. to dusk. The state park lot on Frisco Lane is at the pin.',
  [W('Mammoth Spring State Park'),['Arkansas State Parks: Mammoth Spring',ASP+'mammoth-spring-state-park']],conf='mixed',brick='yes',
  hours='March–mid-December: Wednesday–Saturday 8 a.m.–5 p.m., Sunday 1–5 p.m.'),

N('mammoth-spring-dam','Mammoth Spring dam and mill remains','Mammoth Spring','ar','water','standing',36.49520,-91.53476,'site','public','walk','','1887–1972',
  'The Mammoth Spring Improvement and Water Power Company built a 198-foot limestone dam in 1887 across the outflow of one of the largest springs in the country, making Spring Lake. It first drove a flour mill, a cotton mill and a cotton gin; from 1925 the Arkansas-Missouri Power Company ran a hydroelectric plant here until 1972, then gave the property to the state.',
  'The limestone dam with its spillway and a walkway across, Spring Lake behind it, and a small red brick power house at the end of the dam (Commons photographs); the park interprets the mill and hydroelectric remnants.',
  '',
  'Arkansas State Parks, Mammoth Spring State Park, which the park page says holds the mill and power plant remnants (the federal land map does not draw the park over the dam); gates open 8 a.m. to dusk. Lot on U.S. 63 by the visitor center.',
  [W('Mammoth Spring State Park'),['Arkansas State Parks: Mammoth Spring',ASP+'mammoth-spring-state-park']],brick='some',th=[36.49599,-91.53529],thn='State park lot, U.S. 63',
  hours='Park gates 8 a.m. to dusk'),
]

PIN_NOTES={
 'monte-ne-resort-ruins':'Register list coordinate for the Oklahoma Row Hotel Site (Wikipedia); on the aerial it is a grassy point at the shore of Beaver Lake in the Corps recreation area. Nothing of the resort could be seen, so area only.',
 'crescent-hotel-eureka-springs':'Wikipedia article coordinate; on the aerial it is on the large hotel building on the hilltop.',
 'parker-hickman-farmstead-erbie':'Coordinate given on the National Park Service page; on the aerial it is a clearing in the woods with small buildings.',
 'fort-smith-national-historic-site':'Wikipedia article coordinate; on the aerial it is on the long building in the park, the barracks.',
 'mather-lodge-petit-jean':'Wikipedia article coordinate; on the aerial it is at the lodge buildings beside the lot.',
 'fordyce-bathhouse-hot-springs':'OpenStreetMap point for the Fordyce Bathhouse Visitor Center (tools/nom.py); on the aerial it is on a red-tiled building on Bathhouse Row.',
 'mccollum-chidester-house-camden':'Register list coordinate (Wikipedia); on the aerial it is on a house on Washington Street.',
 'helena-depot-delta-cultural-center':'Register list coordinate for the Helena Depot (Wikipedia); on the aerial it is on the long red-roofed building beside the tracks.',
 'dyess-colony-administration-building':'OpenStreetMap point for the Dyess Colony Administration Building (tools/nom.py); on the aerial it is on the building in the middle of the circle.',
 'lakeport-plantation':'Wikipedia coordinate fell in a field; moved 82 m north onto the cluster of buildings at the end of the farm road on the aerial. Which roof is the house was not settled from the aerial.',
 'rohwer-relocation-center-cemetery':'Register list coordinate for the memorial cemetery (Wikipedia); on the aerial a clump of trees with pale monuments at the end of a farm track among fields.',
 'arkansas-post-national-memorial':'Register list coordinate for the memorial (Wikipedia); it falls in woods inside the memorial on the aerial. No parking lot is mapped within 4 km and the visitor center was not found on the aerial, so area only.',
 'union-station-pine-bluff':'Wikipedia article coordinate; on the aerial it is on the long red-roofed building beside the tracks.',
 'old-mill-north-little-rock':'Register list coordinate (Wikipedia); on the aerial it is in the trees by the pond in the park; the mill itself is hidden by leaves.',
 'jacksonport-courthouse':'Register list coordinate for the state park fell in a field by the levee; moved about 560 m west onto the large hip-roofed building beside the state park lot on Adams Street. Not confirmed as the courthouse, so area only.',
 'powhatan-courthouse':'Wikipedia article coordinate for the state park; on the aerial it is on the building on the hill beside the park lot.',
 'frisco-depot-mammoth-spring':'Register list coordinate fell on a ball field; moved 120 m west to the state park lot on Frisco Lane (parking.py) and the long building beside it on the aerial, which may be the depot. Not confirmed, so area only.',
 'mammoth-spring-dam':'Register list coordinate fell on the U.S. 63 bridge; moved about 160 m east onto the white spillway at the outlet of Spring Lake seen on the aerial, beside a small building.',
}
