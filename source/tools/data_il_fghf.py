# November 22, 2026: a first statewide scatter for Illinois, then the state with the fewest places on the map (23).
# Region il claimed with choose.py --thinnest. Spread from Galena and Chicago in the north to Cairo and the Shawnee
# National Forest in the south. Facts come only from sources opened in this session: Wikipedia read as raw text
# (tools/wiki_raw.py), the National Park Service's Pullman pages, the Forest Service's Illinois Iron Furnace page,
# Glessner House's own tour pages, the Diocese of Belleville's parish directory and the Institute of Christ the King's
# Cahokia page, and a Southeast Missourian article on Magnolia Manor. The Illinois DNR historic-sites pages could not be
# read (every address tried served the page for another site), so no state historic site here has hours on record.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
IDNR='The Illinois Department of Natural Resources runs it as a state historic site; its page could not be read when this was written, so hours were not checked: ring ahead or look at the state historic sites page.'
SHS=L('Illinois State Historic Sites','https://dnrhistoric.illinois.gov/experience/sites.html')

BATCH={'key':'il_fghf','label':'Illinois: Galena to Cairo','added':'2026-11-22 05:37'}

PLACES=[
N('holy-family-log-church-cahokia','Church of the Holy Family log church','Cahokia Heights','il','worship','standing',38.57012,-90.18851,'site','open','walk','','1786–1799',
  'The parish was founded in 1699 by missionaries from Quebec and is said to be the oldest continuously active Catholic parish in the United States. The log church was begun about 1786 and consecrated on September 24, 1799, and is called the oldest church building west of the Allegheny Mountains. A stone church replaced it in 1891 and the log church became a parish hall until it was restored in 1949 to 1951.',
  'A little-altered French colonial church in poteaux-sur-sol ("post on sill") building: heavy hewn walnut timbers set upright into a wooden sill on stone slabs, the gaps filled with rubblestone and clay, the walls leaning slightly inward and braced with diagonal timbers. Some rotted members were replaced in 1949 to 1951. Wikipedia says visitors are welcome for guided tours in summer; the inside can be seen at the Sunday Mass. Interior fittings not checked.',
  'A church of 1799 still used for Sunday Mass.',
  'Holy Family Parish, 116 Church Street, at the corner of East 1st and Church Streets, beside the 1891 stone church and the parish house. The Diocese of Belleville\'s parish directory and the Institute of Christ the King, which says the Mass, both give a 9 a.m. Sunday Latin Mass in the log church; the parish\'s other Masses are in the newer church. Parking on the street; a lot was not checked.',
  [W('Church of the Holy Family (Cahokia Heights, Illinois)'),L('Diocese of Belleville: Holy Family, Cahokia Heights','https://dio-bell.solutiosoftware.com/directory/parishes/holy-family-cahokia'),L('Institute of Christ the King: Holy Family Log Church','https://institute-christ-king.org/cahokia-home')],
  brick='no',hours='Sunday 9 a.m. Latin Mass in the log church'),

N('cahokia-courthouse','Cahokia Courthouse','Cahokia Heights','il','civic','standing',38.57092,-90.19204,'site','open','walk','','c. 1740 (rebuilt 1930s)',
  'A French colonial log house of about 1740, built with its logs standing upright, that later served as a courthouse. In 1904 promoters of the St. Louis World\'s Fair bought it, took it apart and rebuilt it at the fair, and afterwards it was rebuilt again in Jackson Park, Chicago. Cahokia people lobbied in the 1920s to have it brought home, and it was rebuilt a third time on its first site.',
  'A poteaux-sur-sol log building interpreted as a frontier courthouse of about 1800. Each move replaced much of the old wood, and Wikipedia calls the third rebuilding mostly a new building; the state says it holds some timber from the first. A visitor center stands just south on Elm Street. Interior not checked.',
  'The courthouse that went to the World\'s Fair and to Chicago before coming home.',
  'Historic Cahokia Courthouse, 107 Elm Street at West 1st Street. '+IDNR+' The Church of the Holy Family log church is a short walk east.',
  [W('Old Cahokia Courthouse'),SHS],brick='no',hours='?'),

N('fort-de-chartres','Fort de Chartres and its powder magazine','Prairie du Rocher','il','fort','ruins',38.08472,-90.15833,'site','open','drive','','1750s',
  'The seat of French rule in the Illinois Country. The first log forts of 1718 to 1720 were spoiled by Mississippi floods, and a limestone fort with walls 15 feet high was built in the 1750s. The river took the south wall in 1772, people carted the stone away, and by 1900 only the powder magazine was left. The state bought the ruins in 1913 and restored the magazine in 1917.',
  'The stone powder magazine, thought to be the oldest building standing in Illinois. Around it: the gateway and two stone buildings rebuilt by the WPA in the 1920s and 1930s (one, the Guards House, has a chapel furnished in the style of the 1750s), a museum built in 1928 on an old foundation, walls partly rebuilt on their foundations in 1989, other buildings\' cellars and foundations laid open, a bake oven and a kitchen garden. Large reenactments in summer.',
  'The last original piece of a French stone fort on the Mississippi.',
  'State historic site four miles west of Prairie du Rocher, Randolph County. '+IDNR,
  [W('Fort de Chartres'),SHS],brick='no',hours='?',th=[38.08746,-90.15924],thn='Lot off Stringtown Road (OpenStreetMap)'),

N('pierre-menard-house','Pierre Menard House','Ellis Grove','il','landmark','standing',37.96318,-89.9083,'site','open','drive','','1802–',
  'The home of Pierre Menard, a fur trader from near Montreal who became the first lieutenant governor of Illinois in 1818. Building began in 1802 below the bluffs at Kaskaskia. The rest of old Kaskaskia, the first state capital, has been washed away by floods, and the house is the one thing left standing there in its first place.',
  'A French colonial (Creole) house with a broad gallery, or porch. Behind it are a period stone kitchen, a privy, a rebuilt smokehouse and springhouse, and a herb and vegetable garden; the museum has a film. Wikipedia notes that the house says nothing of the people enslaved on the place. Interior not checked.',
  'All that stands of the first capital\'s town.',
  'Pierre Menard Home State Historic Site, Randolph County. '+IDNR,
  [W('Pierre Menard House'),SHS],brick='?',hours='?'),

N('illinois-iron-furnace','Illinois Iron Furnace','Rosiclare','il','industry','standing',37.49911,-88.32823,'site','public','walk','','1837–1883',
  'A charcoal blast furnace built between 1837 and 1839 for Chalon Guard and Leonard White, smelting local ore into pig iron that went by wagon to Elizabethtown on the Ohio. It stood idle from 1861 to 1868 and closed for good in 1883, the end of the iron industry in Illinois. Road building in the 1930s badly damaged it, and the Forest Service\'s Golconda Job Corps Center rebuilt it in 1967.',
  'The rebuilt stack: big limestone blocks from near Cave-In-Rock, dry-laid on a limestone foundation, with wrought iron binders through the stonework (Forest Service). It is the only iron furnace left in Illinois. A picnic area surrounds it, and a half-mile trail from the back of the picnic area follows Big Creek.',
  'The last iron furnace in Illinois.',
  'Shawnee National Forest picnic site, run by the Forest Service: open all year, daily 6 a.m. to 10 p.m., no fee, no overnight parking, no trash cans (pack it out). The furnace stands in the picnic area; from Harrisburg take Illinois 34/145 south.',
  [W('Illinois Iron Furnace'),L('Forest Service: Illinois Iron Furnace Historic Site','https://fs.usda.gov/r09/shawnee/recreation/illinois-iron-furnace-historic-site')],
  brick='?',hours='Daily 6 a.m. to 10 p.m., all year'),

N('shawneetown-bank','Shawneetown Bank','Old Shawneetown','il','civic','standing',37.69667,-88.13528,'site','view','walk','','1839–1841',
  'Old Shawneetown was a salt-trade town and the seat of a federal land office from 1812, and Illinois chartered its first banks there in 1816. This Greek Revival bank was begun on August 3, 1839 and opened in 1841, the oldest building in Illinois put up as a bank, and banks used it into the 1900s.',
  'A brick building with a limestone front at Main and Washington Streets. Some restoration was done in the 1970s; in 2009 it was on Landmarks Illinois\'s list of the ten most endangered places, and it was not open for tours as of 2017 (Wikipedia). Interior not checked.',
  'A Greek Revival bank in a nearly empty river town.',
  'State historic site, seen from Main Street and Washington Street. Wikipedia says it was not open for tours as of 2017; whether that has changed was not checked.',
  [W('Shawneetown Bank State Historic Site'),SHS],brick='some'),

N('magnolia-manor-cairo','Magnolia Manor','Cairo','il','landmark','standing',37.00937,-89.18247,'exact','open','walk','','1869',
  'Charles A. Galigher, a Cairo businessman and friend of Ulysses S. Grant from Grant\'s time in command at Cairo, built this house in 1869. Grant was feted here after his presidency. The Cairo Historical Association formed in 1952 to restore it and has run it as a house museum since.',
  'A 14-room red brick Victorian house with double walls and ten-inch air spaces against the damp. Inside are many original nineteenth-century furnishings (Wikipedia). Every year it opens its Holiday House on Thanksgiving Day (Southeast Missourian).',
  'Grant\'s friend\'s house in a fading river town.',
  'Cairo Historical Association, 2700 Washington Avenue. Its own hours page was not found, so hours were not checked; a Southeast Missourian article says the house has opened for tours since 1952 and charges admission.',
  [W('Magnolia Manor (Cairo, Illinois)'),L('Southeast Missourian: Magnolia Manor Holiday House opens','https://www.semissourian.com/news/magnolia-manor-holiday-house-opens-thursday-2811317')],brick='yes',hours='?'),

N('cairo-historic-district','Cairo Historic District','Cairo','il','town','standing',37.00556,-89.17417,'area','public','walk','','1800s–1890',
  'Cairo, where the Ohio meets the Mississippi, was a river trade town and the southern end of the Illinois Central Railroad. It lost most of its people in the 1900s, and by the 1970s parts of the district were said to be beginning to look like a ghost town. The district, put on the National Register in 1979, takes in most of the city built by 1890: about 980 buildings.',
  'Commercial and residential streets of the 1800s, bounded roughly by Park, 33rd, Sycamore, 21st, Cedar and 4th Streets and the Ohio River. Magnolia Manor is on Washington Avenue at the north end. Which buildings still stand and which are empty was not checked.',
  'A once-busy river city, now half empty.',
  'Public streets; the buildings are seen from the street, and many are private. The pin is the middle of the district from the Register list, not one building.',
  [W('Cairo Historic District'),W('Cairo, Illinois')],conf='mixed',brick='?'),

N('mount-pulaski-courthouse','Mount Pulaski Courthouse','Mount Pulaski','il','civic','standing',40.00905,-89.28495,'site','open','walk','','1847–1855',
  'Mount Pulaski won the Logan County seat in 1848 by raising $2,700 of the $3,000 for a brick courthouse. It was the county seat until 1855. Abraham Lincoln argued cases here on the Eighth Circuit, and it is one of only two of that circuit\'s courthouses left. The town gave it to the state in 1936, and the state restored it in 1936 to 1939.',
  'A two-story Greek Revival brick courthouse on the public square, with pediments and corner pilasters. Guided tours show the recreated county offices and the courtroom upstairs.',
  'A courtroom Lincoln practised in.',
  'On the public square, Mount Pulaski. '+IDNR,
  [W('Mount Pulaski Courthouse State Historic Site'),L('HMdb: Mt. Pulaski Court House','https://www.hmdb.org/m.asp?m=12327'),SHS],brick='yes',hours='?'),

N('metamora-courthouse','Metamora Courthouse','Metamora','il','civic','standing',40.79178,-89.36241,'site','open','walk','','1845',
  'Built in 1845 by David Irving as the Woodford County courthouse and an Eighth Circuit court. Lincoln handled more than 70 cases here from 1845 to 1858, among them two murders and two cases of people who had fled slavery. It is the other of the two Eighth Circuit courthouses that survive, and has been a museum since 1921.',
  'A Greek Revival courthouse. The first floor is a museum of local history and frontier law; the second floor is restored to its 1850s look as the courtroom and judges\' chambers. Interior details beyond that not checked.',
  'The other surviving Lincoln circuit courthouse.',
  'Metamora, Woodford County. '+IDNR,
  [W('Metamora Courthouse State Historic Site'),SHS],brick='?',hours='?'),

N('jubilee-college','Jubilee College','Brimfield','il','inst','standing',40.82557,-89.80026,'site','open','drive','','1839–1862',
  'Bishop Philander Chase, who had founded Kenyon College in Ohio, founded Jubilee College in 1839, one of the earliest colleges in Illinois, out in the country away from the temptations of towns. Its chapel and schoolhouse were consecrated in 1840, and the college ran until 1862. The Civilian Conservation Corps repaired the building in the 1930s, the state restored it in the 1970s, and the historic site, shut in 2008 and 2009, reopened in September 2022.',
  'The two-story Gothic Revival chapel and schoolhouse of native sandstone, L-shaped after an Anglican chapel near London, which held the chapel, classrooms and dormitory. One wing has a recreated schoolmaster\'s office and library, exhibits and a film. Wikipedia says the state offers guided tours of it only from time to time.',
  'A frontier bishop\'s stone college in the woods.',
  'The 90-acre historic site sits inside Jubilee College State Park (3,100 acres, Illinois DNR), about six miles west of Peoria. '+IDNR,
  [W('Jubilee College State Park'),SHS],brick='no',hours='?'),

N('bishop-hill-colony','Bishop Hill Colony','Bishop Hill','il','town','standing',41.2003,-90.1189,'area','public','walk','','1846–1861',
  'Swedish religious dissenters led by Eric Janson founded Bishop Hill on the prairie in 1846 and ran it as a commune until 1861. Many of the first emigrants died on the way, and the first winter was spent in dugouts; brick houses followed, and by 1849 there were a flour mill, two sawmills and a three-story church. It is a National Historic Landmark.',
  'Colony buildings scattered through the village. The state shows four: the 1848 frame Greek Revival Colony Church with its museum, the three-story stuccoed brick Colony Hotel, the frame Boys\' Dormitory, and the colony barn moved behind the hotel. A brick museum holds Olof Krans\'s folk paintings of colony life, and the state owns the village park.',
  'A Swedish commune on the prairie, still standing.',
  'Public village streets, Henry County, about two miles north of US 34. The four state buildings are a state historic site: its page could not be read when this was written, so hours were not checked. Other colony buildings are privately owned.',
  [W('Bishop Hill Colony'),W('Bishop Hill State Historic Site'),SHS],brick='?'),

N('nauvoo-historic-district','Nauvoo Historic District','Nauvoo','il','town','standing',40.5407,-91.39318,'area','public','walk','','1839–1846',
  'Nauvoo was the headquarters of the Latter Day Saints from 1839 to 1846 and for a short time the largest city in Illinois. Most of the Saints left by 1848; the temple burned that year and a tornado levelled its ruins in 1865. From the 1950s members of the Church of Jesus Christ of Latter-day Saints bought and restored many of the old houses and shops; in 2024 the church also bought the Joseph Smith Historic Site from the Community of Christ.',
  'Restored 1840s homes and shops on a broad street grid: the Brigham Young and Heber C. Kimball houses, the Joseph Smith Homestead and Mansion House, the Red Brick Store, the Times and Seasons printshop, the Webb blacksmith shop, the Scovil bakery, the Seventies Hall and others; the site of the first temple and the Smith family cemetery. Some contributing houses are private homes. Which buildings open and when was not checked.',
  'A whole 1840s city restored on the Mississippi.',
  'Public streets. The pin is the Red Brick Store on Water Street (OpenStreetMap), in the old lower town; the restored buildings are run by the Church of Jesus Christ of Latter-day Saints, and their hours were not checked.',
  [W('Nauvoo Historic District'),W('Nauvoo, Illinois')],brick='some'),

N('grant-home-galena','Ulysses S. Grant Home','Galena','il','landmark','standing',42.41126,-90.42439,'exact','open','walk','','1859–1860',
  'An Italianate house built in 1859 and 1860 to William Dennison\'s design for Alexander J. Jackson. Galena Republicans, Elihu Washburne among them, bought it and gave it to General Grant in 1865 for his war service. The Grants lived here during the 1868 campaign and at times afterwards, and Grant last came in 1880. It has been kept as his memorial since 1904.',
  'Rooms furnished as they looked in the middle 1860s, many with the Grants\' own furniture; an exhibit building next door. Outside: low roof, balustraded balconies over covered porches, deep eaves.',
  'The house a town gave a general.',
  'U.S. Grant Home State Historic Site, 500 Bouthillier Street, across the Galena River from downtown. '+IDNR,
  [W('Ulysses S. Grant Home'),SHS],brick='?',hours='?'),

N('galena-historic-district','Galena: Main Street and the old town','Galena','il','town','standing',42.41662,-90.42780,'area','public','walk','','1820s–1900',
  'Galena grew rich on lead mining, and by the 1830s it had more people than Chicago. Fires in the 1850s led the city to ban new wooden buildings, so the downtown is brick and stone. When the town declined its buildings stood empty; it passed one of the first preservation ordinances in Illinois in 1965, and the district, about 85 percent of the city with over a thousand pre-1900 buildings, went on the National Register in 1969.',
  'Three tiers up the hill: Main Street by the river, lined with red brick commercial buildings of two to four stories in the plain style of the 1840s; Bench Street with the churches and fraternal halls whose steeples crown the town; and Prospect Street with houses and the old high school\'s clock tower, joined by stairs. The DeSoto House, St. Rose Academy, the Flatiron Building and the Dowling House of 1827 are named by Wikipedia. The 1845 Old Market House is the welcome centre.',
  'A lead-mining boomtown kept whole in brick.',
  'Public streets; most buildings are shops and private houses seen from the street. The pin is on Main Street. Parking on the streets and in the lots along the levee was not checked.',
  [W('Galena Historic District'),W('Old Market House (Galena, Illinois)')],brick='yes'),

N('lockport-historic-district','Lockport: the canal town and the Gaylord Building','Lockport','il','canal','standing',41.59088,-88.05794,'site','public','walk','','1836–1848',
  'Lockport was platted in 1836 as the Illinois and Michigan Canal was begun and became the canal\'s headquarters two years later. The canal, finished in 1848, joined the Great Lakes to the Illinois River; its busiest year was 1882 and it was used until 1933. The downtown runs beside it, and the stretch of locks and towpath from Lockport to LaSalle is a National Historic Landmark.',
  'The Gaylord Building of 1838 on the canal bank, of yellow limestone with an Italianate addition of 1859, restored from 1983 on and one of the National Trust\'s historic sites. Nearby in the 59-building district: the Canal Office of 1838 (the Will County Historical Society), the Norton warehouse and store, and the canal itself beside the street. Interiors not checked.',
  'Headquarters of the canal that made Chicago.',
  'Public streets and the canal-side path. The pin is the Gaylord Building, 200 West 8th Street (OpenStreetMap); what is open inside was not checked.',
  [W('Lockport Historic District'),W('Gaylord Building'),W('Illinois and Michigan Canal')],brick='no'),

N('pullman-chicago','Pullman','Chicago','il','town','standing',41.69524,-87.60854,'exact','open','walk','','1880–',
  'George Pullman built a town for the workers of his sleeping-car works, then outside Chicago, from 1880. It had the factory, the Hotel Florence (opened 1881) and red brick row houses with indoor plumbing. A plan of 1960 to clear it for an industrial park led residents to save it; it went on the National Register in 1969. A fire in 1998 destroyed much of the factory\'s clock tower building, which was restored and opened as the national park visitor center on September 6, 2021.',
  'Streets of red brick row houses for workers and managers, the Hotel Florence, the administration building with its clock tower, and the A. Philip Randolph Pullman Porter Museum. Part of the grounds is still a state historic site.',
  'A company town that started a national strike.',
  'Pullman National Historical Park (National Park Service); the visitor center is on South Cottage Grove Avenue by the clock tower (OpenStreetMap). The park gives daily tours at 1 p.m. from the visitor center, which may be cancelled for staffing, events or weather; the state historic site grounds are open dawn to dusk, no motor vehicles, pets leashed. The visitor center\'s own hours are drawn by script on the park\'s page and were not read. Most houses are private homes.',
  [W('Pullman National Historical Park'),L('National Park Service: Pullman basic information','https://www.nps.gov/pull/planyourvisit/basicinfo.htm')],
  brick='yes',hours='Tours daily at 1 p.m. from the visitor center; state historic site grounds dawn to dusk'),

N('glessner-house-chicago','Glessner House','Chicago','il','landmark','standing',41.85772,-87.62145,'exact','open','walk','','1885–1887',
  'Henry Hobson Richardson designed this house on Prairie Avenue for John J. Glessner in 1885 and 1886, and it was finished in late 1887. Its plain fortress-like front puzzled the neighbours of Chicago\'s richest street. The family gave it to the Armour Institute in 1937; threatened with demolition in the 1960s, it opened for tours in 1971 and is a National Historic Landmark.',
  'Rooms restored to their first look, with nearly all the artifacts original and in place, including William Morris wallpapers and textiles (Glessner House). The 75-minute tour runs from the coach house to the courtyard. The house is not accessible by wheelchair, and children under five are not taken.',
  'The Richardson house that taught Sullivan and Wright.',
  'Glessner House, on Prairie Avenue at 18th Street; enter through the green door on 18th Street. Tickets $20 for adults on its own page, advance tickets recommended. Its pages disagree on January: one says it is closed all January, the other that it is open all year except holidays.',
  [W('John J. Glessner House'),L('Glessner House: full house tour','https://glessnerhouse.org/house-tours'),L('Glessner House: closed days','https://glessnerhouse.org/closed-days')],
  brick='?',hours='Tours Wednesday, Friday and Saturday at 11:30 a.m., 1 p.m. and 2:30 p.m.; closed some holidays'),

N('chicago-water-tower','Chicago Water Tower','Chicago','il','water','standing',41.89717,-87.62442,'exact','public','walk','','1869',
  'William W. Boyington designed the 182-foot tower in 1869 to house a standpipe for the pumps of the Chicago Avenue Pumping Station, which drew water from cribs in Lake Michigan. It was the only public building in the burned district to survive the Great Chicago Fire of 1871. It is the second-oldest water tower in the United States, after Louisville\'s.',
  'A castellated tower of yellowing Lemont limestone in Jane M. Byrne Plaza on Michigan Avenue, with the pumping station across the street. Inside is a city art gallery run by the Chicago Office of Tourism; its hours were not checked.',
  'The building the Great Fire spared.',
  'City park on Michigan Avenue at Chicago Avenue; seen from the plaza at any time. The city\'s gallery page answered 404 when this was written.',
  [W('Chicago Water Tower')],brick='no'),
]

PIN_NOTES={
 'holy-family-log-church-cahokia':'Wikipedia article coordinate.',
 'cahokia-courthouse':'OpenStreetMap point for the historic courthouse building, which is under trees on the aerial.',
 'fort-de-chartres':'Wikipedia article coordinate.',
 'pierre-menard-house':'OpenStreetMap point for the historic site; a small building stands beside it under trees near the railroad. The Wikipedia coordinate is about 180 m north in woods.',
 'illinois-iron-furnace':'Moved about 115 m west from the Forest Service coordinate, which fell in woods, onto the picnic-area loop where the furnace stands; the stack itself is not seen under the trees.',
 'shawneetown-bank':'Wikipedia (Register) coordinate.',
 'magnolia-manor-cairo':'OpenStreetMap point for the house.',
 'cairo-historic-district':'Register list coordinate for the district: the middle of an area, not a building.',
 'mount-pulaski-courthouse':'HMdb markers for the courthouse, on the west side of the square; the building is under trees on the aerial. The Wikipedia coordinate fell on a house a block west.',
 'metamora-courthouse':'Wikipedia (Register) coordinate.',
 'jubilee-college':'Moved about 230 m onto the one large building in the clearing north of the park road, taken to be the college building; the Wikipedia coordinate fell on an open lawn. Not confirmed from a source.',
 'bishop-hill-colony':'Wikipedia coordinate for the state historic site, on a village crossroads; it marks the village, not one building.',
 'nauvoo-historic-district':'OpenStreetMap point for the Red Brick Store.',
 'grant-home-galena':'OpenStreetMap point for the museum.',
 'galena-historic-district':'On the Main Street commercial blocks, picked on the aerial; the pin marks the district, not one building.',
 'lockport-historic-district':'OpenStreetMap point for the Gaylord Building.',
 'pullman-chicago':'OpenStreetMap building for the Pullman Administration Building (the clock tower); the Wikipedia coordinate fell on the railroad.',
 'glessner-house-chicago':'OpenStreetMap point for the museum.',
 'chicago-water-tower':'Wikipedia (Register) coordinate.',
}
