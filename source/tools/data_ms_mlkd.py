# November 21, 2026: a first scatter across Mississippi outside the river country round Port Gibson and Natchez (batch
# ms_lwtt): the Gulf Coast (Biloxi, Pascagoula), the Delta (Money, Sumner, Dockery), Vicksburg, Grenada,
# Meridian, the Tombigbee country (Columbus, Waverley), Oxford, Holly Springs and Tishomingo in the northeast corner.
# Mississippi was the region with the fewest places (21) when tools/choose.py --thinnest claimed it.
# Sources were opened in this session: Wikipedia as raw text (tools/wiki_raw.py); National Park Service pages (Ship Island, kept for the lead in the note,
# Fort Massachusetts, Emmett Till and Mamie Till-Mobley National Monument, Vicksburg fees); the City of Biloxi's lighthouse
# page; visitbeauvoir.org; rowanoak.com; oldcourthouse.org; mdwfp.com (Tishomingo State Park and its trail brochure);
# MDAH (Dockery Farms landmark news); SAH Archipedia (Dockery Farms); the Mississippi Gulf Coast National Heritage Area and
# lapointekrebs.org; WLOX (June 2026); the American Battlefield Trust (Waverley, Grenada Lake); HMdb.org marker pages
# (Bryant's Grocery, Grenada's Confederate fort); NPR (2019 and 2023); the Meridian Star (2017).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'ms_mlkd','label':'Mississippi: a first scatter from the Gulf Coast to the Delta and the northeast hills','added':'2026-11-21 23:25'}

PLACES=[
# ---- Gulf Coast ----
N('biloxi-lighthouse','Biloxi Lighthouse','Biloxi','ms','light','standing',30.39442,-88.90122,'exact','open','drive','','1848',
'A cast-iron tower bolted together from plates made in Baltimore and lined with brick, lit in 1848 on the beach at Biloxi. '
'It was kept by women for longer than any other American lighthouse; Mary Reynolds took it over in 1854. The keeper\'s house '
'was destroyed by Hurricane Camille in 1969; the tower came to the City of Biloxi after 1968, was damaged by Katrina in 2005 and '
'relit after a $400,000 restoration in 2010.',
look='The tower stands in the median of Beach Boulevard (US 90). Inside, painted lines mark the heights of past storm surges, '
'Katrina\'s highest at 21.5 feet. The city runs guided tours; its page said in November 2026 that tours to the top were '
'temporarily stopped for repairs to the upper deck.',
accn='City of Biloxi. Guided tours daily 9 to 10 a.m., weather permitting; $5 from age 12, $2 ages 6 to 11, under 6 free; '
'no reservation except groups ((228) 374-3105). Hours and the note that the climb is closed for repairs from the city\'s page, '
'read November 2026. Parking on Beach Boulevard beside it.',
links=[W('Biloxi Lighthouse'),L('City of Biloxi: Biloxi Lighthouse','https://biloxi.ms.us/visitor-info/museums/lighthouse/')],
th=[30.39407,-88.90113],thn='Beach Boulevard lot',brick='no',
hours='Guided tours daily 9 to 10 a.m., weather permitting (climb to the top closed for repairs, November 2026)'),

N('beauvoir-biloxi','Beauvoir (Jefferson Davis home)','Biloxi','ms','landmark','standing',30.3925,-88.97083,'site','open','drive','','1848–1852',
'A raised Gulf Coast cottage built by planter James Brown from 1848 and finished in 1852. Jefferson Davis lived here from '
'1877 until his death in 1889 and wrote his memoir in a cottage on the grounds. From 1903 to 1957 it was a Confederate '
'veterans\' home, with barracks, a hospital and a cemetery behind the house; the house has been a museum since 1941. Katrina '
'tore off its porches and part of the roof in 2005 and destroyed the library pavilion and other outbuildings; the house '
'reopened restored in June 2008.',
look='The house faces the Gulf across US 90, with red-brick piers under the raised main floor and six brick fireplaces at its '
'core. Guided tours of the house run on the hour; the grounds hold the veterans\' cemetery with the Tomb of the Unknown '
'Confederate Soldier, a newer presidential library building and a museum.',
accn='Owned and run by the Mississippi Division of the Sons of Confederate Veterans, 2244 Beach Boulevard. House tour $12, '
'grounds pass $7, under 6 free (visitbeauvoir.org, read November 2026). The page gives tour times but not the days open. '
'Parking on the grounds.',
links=[W('Beauvoir (Biloxi, Mississippi)'),L('Beauvoir: visit','https://www.visitbeauvoir.org/')],
brick='some',hours='Guided house tours on the hour, 10 a.m. to 4 p.m. (days not given on the page)'),

N('lapointe-krebs-house','LaPointe-Krebs House (the "Old Spanish Fort")','Pascagoula','ms','landmark','standing',30.38028,-88.55806,'site','open','drive','','1757',
'Neither a fort nor Spanish: a French colonial house on Krebs Lake whose oldest room has timbers dated by tree rings to 1757, '
'with additions dated 1762 and 1772. It is Mississippi\'s oldest standing building and its only French colonial one. The '
'oldest walls are oyster-shell concrete (tabby) on longleaf pine framing; the west addition is bousillage of clay and Spanish '
'moss. The Krebs family lived here for more than a century.',
look='The low house of tabby and bousillage walls, recently given its largest restoration; a museum building beside it serves '
'as the interpretive centre (the old museum was wrecked by Katrina in 2005). The Krebs cemetery is next to it.',
accn='Owned and run by the LaPointe-Krebs Foundation, 4602 Fort Street, Pascagoula, (228) 471-5126. WLOX reported in June 2026 '
'that the house and museum are open seven days a week except holidays; the foundation\'s own page read gives no hours. '
'Parking on the grounds not checked.',
links=[W('Old Spanish Fort (Pascagoula, Mississippi)'),L('Mississippi Gulf Coast National Heritage Area: LaPointe-Krebs House','https://msgulfcoastheritage.ms.gov/historic/historic-homes/lapointe-krebs-house/'),
 L('LaPointe-Krebs Foundation','https://www.lapointekrebs.org/'),L('WLOX: Mississippi\'s oldest structure endures (June 2026)','https://www.wlox.com/2026/06/29/coast-life-like-america-mississippi-oldest-structure-endures/')],
brick='?',hours='?'),

# ---- The Delta ----
N('bryants-grocery-money','Bryant\'s Grocery and Meat Market ruins','Money','ms','civic','ruins',33.65246,-90.20893,'site','view','drive','','1955',
'The country store in Money where Emmett Till, fourteen and visiting from Chicago, was accused in August 1955 of offending '
'the white shopkeeper Carolyn Bryant. Days later her husband Roy Bryant and his half-brother J. W. Milam abducted him; he was '
'beaten and shot, and both men were acquitted at Sumner. The killing drew attention around the world and is credited with '
'sparking the civil rights movement.',
look='What is left of the store stands beside the highway along the railroad in Money: NPR in 2019 described it in ruins, '
'overtaken by trees and vines, and in 2023 as crumbling. A Mississippi Freedom Trail marker stands at the site.',
accn='Look from the roadside only; the building is unsafe and its owner was not checked. No parking lot is mapped: pull off '
'where the shoulder allows. The marker here has been vandalised before.',
links=[L('HMdb: Bryant\'s Grocery marker','https://www.hmdb.org/m.asp?m=77418'),
 L('NPR: Telling the Emmett Till story in Mississippi (2019)','https://www.npr.org/2019/08/28/755024458/why-don-t-y-all-let-that-die-telling-the-emmett-till-story-in-mississippi'),
 L('NPR: Civil rights tourism may protect Mississippi history (2023)','https://www.npr.org/2023/03/14/1161501882/civil-rights-tourism-preserve-mississippi-history')],
brick='?'),

N('tallahatchie-courthouse-sumner','Tallahatchie County Second District Courthouse','Sumner','ms','civic','standing',33.97028,-90.36944,'exact','open','drive','','1910',
'A two-storey brick Romanesque Revival courthouse of 1910 with a four-storey corner tower. In September 1955 the men accused of '
'murdering Emmett Till were tried and acquitted here. It was restored to its look at the time of the trial and in July 2023 '
'became part of the Emmett Till and Mamie Till-Mobley National Monument.',
look='The courthouse on the square at 108 Main Street, with its tower. The Emmett Till Interpretive Center and the national '
'monument\'s Sumner visitor center are across the street, with a self-guided tour app for the other Till sites. Interior not '
'checked.',
accn='Tallahatchie County courthouse, part of the Emmett Till and Mamie Till-Mobley National Monument (NPS); a passport stamp '
'is kept at the courthouse. The NPS hours page carried no hours when read (November 2026). Parking on East Court Street.',
links=[W('Tallahatchie County Courthouse'),L('NPS: Tallahatchie County Courthouse','https://www.nps.gov/places/tallahatchie-county-courthouse.htm')],
th=[33.97068,-90.36938],thn='East Court Street',brick='?',hours='?'),

N('dockery-farms','Dockery Farms','Cleveland','ms','landmark','standing',33.72951,-90.61638,'site','view','drive','','1895',
'A cotton plantation and sawmill begun in 1895 by Will Dockery on the Sunflower River, which grew to more than 2,000 workers '
'with its own store, post office, school and rail terminal. Charley Patton lived here from about 1900, and Robert Johnson, '
'Howlin\' Wolf, Son House and Pops Staples played round it: it is widely called the birthplace of the Delta blues. It is still '
'a working farm.',
look='Eight original buildings designed and built by Will Dockery and his workers: a cypress-framed seed house, a '
'corrugated-metal cotton gin behind it, a cotton shed, hay barn, commissary storage, a mule trough and, on Highway 8, the '
'clapboard Moderne service station of about 1935 with its red-striped canopy. A Mississippi Blues Trail marker.',
accn='Private working farm; the site is managed by the Dockery Farms Foundation (MDAH). Look from Highway 8. Tours are by '
'arrangement only (Wikipedia: a small number of private tours); the foundation\'s web address no longer carries its own '
'pages (November 2026). No parking lot is mapped.',
links=[W('Dockery Plantation'),L('MDAH: Blues site named a Mississippi Landmark','https://mdah.ms.gov/news/blues-site-named-mississippi-landmark'),
 L('SAH Archipedia: Dockery Farms','https://sah-archipedia.org/node/86841')],
brick='?'),

# ---- Vicksburg and Grenada ----
N('old-warren-county-courthouse-vicksburg','Old Warren County Courthouse (Old Court House Museum)','Vicksburg','ms','civic','standing',32.35205,-90.87862,'exact','open','drive','','1858–1860',
'Built on one of Vicksburg\'s highest bluffs from 1858 to 1860 by the Weldon brothers of Rodney, it was a main Union target in '
'the 47-day siege and took only one serious hit; the Stars and Stripes went up over it on July 4, 1863. In December 1874 it '
'was where the Vicksburg massacre began, when Black citizens tried to reinstate Sheriff Peter Crosby. Left empty after a new '
'courthouse opened in 1939, it has been a museum since 1948.',
look='The original iron doors and shutters survive, and the second-floor courtroom where Holt Collier was tried and acquitted '
'in 1867. Four former cistern houses are attached to the building. Museum of local history inside.',
accn='Vicksburg and Warren County Historical Society, 1008 Cherry Street. Adults $10, seniors $9, students $5 '
'(oldcourthouse.org, read November 2026). Parking on Adams and Cherry streets.',
links=[W('Old Warren County Courthouse'),L('Old Court House Museum','https://www.oldcourthouse.org/')],
th=[32.35203,-90.87732],thn='Adams Street lot',brick='?',
hours='Monday to Saturday 8:30 a.m. to 4:30 p.m. (to 5 p.m. during daylight saving time)'),

N('uss-cairo-vicksburg','USS Cairo gunboat','Vicksburg','ms','fort','ruins',32.37583,-90.86667,'site','open','drive','','1861–1862',
'A Union ironclad river gunboat built by James Eads at Mound City, Illinois, in 1861. She fought at Fort Pillow and Memphis and '
'on December 12, 1862 became the first ship sunk by a mine set off by hand, going down in twelve minutes in the Yazoo River '
'with no one killed. Found in 1956, she was raised in three pieces in 1964, reassembled on a concrete base in the military park '
'from 1977, and has been shown under a shelter since 1980.',
look='The partly rebuilt hull, armour and engines of the gunboat under a fabric roof, with a museum of what was recovered from '
'the mud: weapons and naval stores. Near the Vicksburg National Cemetery.',
accn='National Park Service, Vicksburg National Military Park. Entrance fee, valid seven days, for everyone 16 and over '
'(standard pass $10 to $20, nps.gov fees page read November 2026). The NPS hours page gave no times when read. Parking on '
'Cairo Museum Circle.',
links=[W('USS Cairo'),L('NPS: Vicksburg fees','https://www.nps.gov/vick/planyourvisit/fees.htm')],
th=[32.37599,-90.86732],thn='Cairo Museum Circle lot',brick='no',hours='?'),

N('grenada-confederate-fort','Confederate fort at Grenada Lake','Grenada','ms','fort','traces',33.78832,-89.76805,'area','public','walk','forts','1862',
'Eight forts were built round Grenada in the winter of 1862 to guard its two railroads on Pemberton\'s Yalobusha River line '
'against Grant\'s advance down the Mississippi Central. Van Dorn\'s raid on Grant\'s depot at Holly Springs that December '
'turned Grant back, so no battle came. This fort guarded the Grenada to Graysport road that Van Dorn used for the raid.',
look='Earthwork walls of the fort; the American Battlefield Trust says two of the forts are on Army Corps of Engineers land '
'at Grenada Lake and open to the public, and one has been restored. An HMdb marker stands at the roadside. A 2019 Commons photograph '
'taken about 90 m from the pin shows high earth walls in pine woods with a wooden stair over them and a shelter by the old road.',
accn='U.S. Army Corps of Engineers, Grenada Lake, off Scenic Route 333 (marker at or near 2088 Scenic Route 333). '
'The American Battlefield Trust says two of the forts are on Corps land and open to the public; the federal land map does not show the pin as public land, so check the signs on arrival. Hours not checked. Five more forts are on private land and are not open.',
links=[L('HMdb: Confederate Fort','https://www.hmdb.org/m.asp?m=89894'),L('American Battlefield Trust: Grenada Lake','https://battlefields.org/visit/heritage-sites/grenada-lake')],
brick='no'),

# ---- East Mississippi ----
N('highland-park-dentzel-carousel','Highland Park Dentzel Carousel','Meridian','ms','amuse','standing',32.37685,-88.71861,'exact','open','drive','amusements','1896–1909',
'A two-row menagerie carousel made about 1896 by the Dentzel company of Philadelphia, sold to Meridian and running in the '
'same place in Highland Park since 1909. It is the only two-row stationary Dentzel menagerie left in the world, and its '
'house is the only surviving carousel building built from a Dentzel plan; both are a National Historic Landmark.',
look='Twenty-eight hand-carved animals, two abreast (twenty horses, a lion, a tiger, deer, antelope and giraffes), two chariots, '
'and oil paintings round the top crown, all restored. The original shelter building houses it.',
accn='City of Meridian Parks and Recreation, Highland Park. The city\'s own carousel page was not found; the Meridian Star '
'(December 2017) gave Saturday 1 to 5 p.m. and said hours vary by season. Parking beside the shelter on 19th Street.',
links=[W('Highland Park Dentzel Carousel and Shelter Building'),L('Meridian Star: carousel back in operation (2017)','https://meridianstar.com/?p=201555')],
th=[32.37690,-88.71830],thn='19th Street lot, Highland Park',brick='?',hours='?'),

N('waverley-mansion','Waverley','West Point','ms','landmark','standing',33.57094,-88.50041,'site','open','drive','','1838–1852',
'A plantation house over the Tombigbee built for Colonel George Hampton Young of Georgia (begun 1838 by one account; 1852 is '
'the accepted completion), named after Scott\'s novel. It is unique among Mississippi mansions for its huge octagonal cupola. '
'The plantation had its own brick kiln, gin, ice house and pool, and the house fell into disrepair after the Youngs.',
look='An H-shaped two-storey Greek Revival house with a two-storey octagonal cupola; inside, four rooms on each floor open onto '
'the central octagon, with the original gas chandelier hanging in it. The American Battlefield Trust says the restored house is '
'open for tours.',
accn='Private house shown by tour, on Waverly Mansion Road off Highway 50 between West Point and Columbus. No owner\'s page with '
'hours or fees was found; hours not checked. The nearest mapped lot, on Waverly Mansion Road, is about 400 m south of the pin.',
links=[W('Waverley (West Point, Mississippi)'),L('American Battlefield Trust: Waverley','https://www.battlefields.org/visit/heritage-sites/waverley-plantation-mansion')],
conf='mixed',brick='?',hours='?'),

N('friendship-cemetery-columbus','Friendship Cemetery','Columbus','ms','burial','standing',33.48083,-88.43056,'site','public','walk','cemeteries','1849',
'Laid out by the Odd Fellows in 1849 as three interlocking circles, their emblem, and owned by the City of Columbus since 1957. '
'More than 2,000 Confederate soldiers and 40 to 150 Union soldiers were buried here when Columbus was a hospital town after '
'Shiloh. On April 26, 1866 the women of Columbus decorated the graves of both sides alike, which inspired the poem The Blue '
'and the Gray and is counted among the beginnings of Memorial Day.',
look='Some 22,000 graves over 70 acres, still in use, with the Confederate monument of 1873. The Union dead were moved to '
'Corinth National Cemetery in 1867.',
accn='City of Columbus cemetery (the city acquired it in 1957, Wikipedia). Daylight visits; hours not checked. Drive in on the cemetery lanes.',
links=[W('Friendship Cemetery')],
brick='?'),

# ---- North Mississippi ----
N('rowan-oak-oxford','Rowan Oak (William Faulkner\'s house)','Oxford','ms','landmark','standing',34.3598,-89.5247,'exact','open','walk','','1844',
'A plain Greek Revival house built in 1844 for Robert Sheegog, an Irish settler. William Faulkner bought it run down in 1930 '
'and lived here until his death in 1962, adding plumbing, brick terraces, a porte-cochère and an office. The University of '
'Mississippi has owned and run it since 1972.',
look='The cedar avenue of the 1840s up to the front, a circle garden, a post oak barn and a dwelling of the enslaved survive '
'on the grounds. Inside, Faulkner wrote the plot outline of his novel A Fable on the walls of his office. Bailey Woods trail '
'from the grounds.',
accn='University of Mississippi Museum. House $10 cash, free for children 12 and under; grounds and the Bailey Woods trail '
'open daily dawn to dusk (rowanoak.com, read November 2026). Parking on Old Taylor Road not checked; the nearest mapped lots '
'are on the campus.',
links=[W('Rowan Oak'),L('Rowan Oak: hours and admission','https://www.rowanoak.com/visit/hours-admission/')],
brick='?',hours='House Tuesday to Saturday 10 a.m. to 4 p.m. (to 5 p.m. June 1 to July 31); grounds daily dawn to dusk'),

N('montrose-holly-springs','Montrose','Holly Springs','ms','landmark','standing',34.77187,-89.44076,'area','view','drive','','1858',
'A Greek Revival mansion of red brick with white Corinthian columns, finished in 1858 for Alfred Brooks as a wedding present '
'for his daughter. It later became the home of the Holly Springs Garden Club, with an arboretum on its grounds.',
look='The two-storey red-brick front and columns at 335 East Salem Avenue; inside, a circular staircase with a niche. The house '
'is shown during the town\'s annual pilgrimage and home tour.',
accn='Holly Springs Garden Club. Look from East Salem Avenue; open inside only during the annual pilgrimage (dates not '
'checked). Whether the arboretum is open at other times not checked.',
links=[W('Montrose (Holly Springs, Mississippi)')],
brick='yes'),

N('tishomingo-state-park-ccc','Tishomingo State Park CCC works and swinging bridge','Tishomingo','ms','inst','standing',34.60515,-88.17963,'area','public','walk','','1935–1939',
'Built by Civilian Conservation Corps Company 3497 from April 1935 and opened in May 1939 among the sandstone bluffs of Bear '
'Creek canyon. Unlike most Mississippi CCC parks, which were built of wood, Tishomingo used a great deal of stone. Many '
'of the CCC works survive: roads, buildings, trails, cabins, picnic tables and the pond the men used.',
look='The suspended footbridge over Bear Creek, built by CCC workers in 1938; the CCC pond; about 98 stone steps down to the '
'creek on one trail; and the site of the CCC camp on the CCC Camp Trail. The nature centre has CCC memorabilia.',
accn='Mississippi Department of Wildlife, Fisheries and Parks, at milepost 304 of the Natchez Trace Parkway. The park page '
'lists $2.00 per person (5 and under free) at the gatehouse; park hours not checked. Park at the Swinging Bridge area. The pin '
'is the footbridge as OpenStreetMap maps it on the Outcroppings Trail.',
links=[W('Tishomingo State Park'),L('MDWFP: Tishomingo State Park','https://mdwfp.com/parks-destinations/park/tishomingo-state-park'),
 L('MDWFP: Tishomingo trails brochure','https://mdwfp.com/sites/default/files/2024-07/tishomingo_trails_brochure_for_web_201506.pdf')],
brick='no'),
]

PIN_NOTES={
'biloxi-lighthouse':'OpenStreetMap lighthouse point (nom.py); checked on the aerial.',
'beauvoir-biloxi':'Wikipedia infobox coordinate; checked on the aerial.',
'lapointe-krebs-house':'Wikipedia infobox coordinate, beside the Krebs Cemetery that OSM maps; checked on the aerial.',
'bryants-grocery-money':'OpenStreetMap mapped-ruin point from the leads layer; checked on the aerial.',
'tallahatchie-courthouse-sumner':'Wikipedia infobox coordinate; checked on the aerial.',
'dockery-farms':'OpenStreetMap tourism point for Dockery Farms on Highway 8 (nom.py); checked on the aerial.',
'old-warren-county-courthouse-vicksburg':'Wikipedia infobox coordinate; checked on the aerial.',
'uss-cairo-vicksburg':'Wikipedia infobox coordinate, beside the Cairo Museum Circle lot; checked on the aerial.',
'grenada-confederate-fort':'HMdb marker position (33 47.299 N, 89 46.083 W), about 90 m from the OpenStreetMap fort point. The aerial shows only woods there, about 250 m from Scenic Route 333, and no lot or wall could be seen, so the pin is area only. Commons photographs of the fort and of the old Grenada to Graysport road are geotagged 80 to 100 m from it.',
'highland-park-dentzel-carousel':'Wikipedia infobox coordinate; checked on the aerial.',
'waverley-mansion':'The Wikipedia coordinate fell in woods about 350 m away; moved to the ArcGIS point of interest "Waverly Mansion", where the aerial shows a large house with angled roofs among trees. Not confirmed as the mansion itself, hence site precision.',
'friendship-cemetery-columbus':'Wikipedia infobox coordinate; checked on the aerial.',
'rowan-oak-oxford':'Wikipedia infobox coordinate; checked on the aerial.',
'montrose-holly-springs':'ArcGIS address point for 335 Salem Avenue, which falls on the street; the aerial does not show which of the houses beside it is Montrose, so the pin is left on the road and marked area.',
'tishomingo-state-park-ccc':'OpenStreetMap footbridge on the Outcroppings Trail, which the park brochure says begins at the Swinging Bridge; checked on the aerial (woods over the creek). Commons photographs of the bridge are geotagged 27 to 58 m from it.',
}
