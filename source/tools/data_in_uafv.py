# November 22, 2026: a second scatter of places across Indiana, still the thinnest state on the map (21 places).
# State taken with tools/choose.py --thinnest. Spread from the Calumet to the Ohio and the Wabash on purpose, adding nothing
# that tools/start.py or the first batch (data_in_gcvh.py) already lists.
# Sources read in this session: Wikipedia articles (tools/wiki_raw.py); the managing bodies' own pages read with tools/page.py
# (Indiana State Museum and Historic Sites plan-your-visit pages, the Old Sheriff's House Foundation, Howard County Museum,
# Eugene V. Debs Foundation, Indiana University Libraries for Wylie House, the Sisters of St. Benedict of Ferdinand,
# Carroll County Wabash and Erie Canal, Inc., Parke County's coveredbridges.com, Indiana Landmarks); HMdb markers; the
# Chicago Sun-Times and FOX 32 on City Methodist Church; Islands.com on the Medora bridge; Inside INdiana Business on Bridgeton.
# Hours are as those pages gave them in November 2026. Interiors were not visited by any source unless the entry says so.
from data_b import N
from data_ma import W
BATCH={'key':'in_uafv','label':'Indiana: a second scatter, Calumet to the Ohio','added':'2026-11-22 02:22'}

ISM='Indiana State Museum and Historic Sites'
def ISMP(site,slug):
    return [ISM+': '+site+', plan your visit','https://www.indianamuseum.org/historic-sites/%s/plan-your-visit/'%slug]

PLACES=[
N('city-methodist-church-gary','City Methodist Church','Gary','in','worship','ruins',41.60043,-87.33843,'exact','view','walk','','1925–1975',
  'Once the largest Methodist church in the Midwest. Pastor William Grant Seaman got U.S. Steel to give the site and almost half the cost, and the nine-storey complex (the sanctuary, a 1,000-seat theatre called Seaman Hall, offices, a gymnasium and a dining hall) was built in 21 months for $800,000; the first service was held on October 3, 1926. The congregation dwindled as the city emptied and the last service was in 1975. A plan to make it an open-air ruins garden found no money for the $4.2 million stabilization, and in September 2026 the Northwest Indiana Regional Development Authority gave Homrich Wrecking a $5.3 million contract to demolish it (Chicago Sun-Times, FOX 32).',
  'The sanctuary and the tall office and theatre block behind it, on Washington Street at Sixth Avenue in downtown Gary. Whether demolition had begun by late November 2026 was not checked: the news in September said it would start once the contract was signed, and Indiana Landmarks expected the building to come down within a year.',
  'Once the largest Methodist church in the Midwest, empty since 1975 and now set to come down.',
  'Owned by the City of Gary. The building is closed and unsafe; Wikipedia says permits are now required to go in, and this entry gives no way in: look from the street. Street parking and downtown lots round Adams and Jefferson streets (OpenStreetMap). If demolition has started the block may be fenced.',
  [['Chicago Sun-Times: City Methodist Church slated for demolition (Sept. 2026)','https://chicago.suntimes.com/real-estate/2026/09/05/city-methodist-church-largest-midwest-gary-demolition'],
   ['FOX 32: City Methodist Church slated for demolition','https://www.fox32chicago.com/news/century-old-city-methodist-church-gary-slated-demolition'],W('City Methodist Church')],
  conf='mixed',brick='?'),

N('gary-union-station','Gary Union Station','Gary','in','rail','ruins',41.60566,-87.33639,'exact','view','walk','stations','1910–',
  'The union station U.S. Steel\'s new city got in 1910, four years after Gary was founded, set between the raised lines of the Lake Shore and Michigan Southern and the Baltimore and Ohio. It has stood empty for about fifty years. It was listed on the National Register in 2019, and in 2023 the City of Gary, the Decay Devils and Digital Equity LLC broke ground on turning it into a fibre network centre and community space, but the project was paused indefinitely in 2024 (Wikipedia).',
  'A Beaux-Arts station of cast-in-place concrete scored to look like stone, facing west on Broadway and almost hidden until you are next to it because it sits between two raised rail lines. A painted "No Parking Cabs Only" on a front pillar is the only sign left; a cobblestone drive leads to a south door, and a tunnel on the north side ran under the tracks to the platform stairs (Wikipedia). Interior not checked.',
  'A concrete station tucked between two railroad embankments.',
  'Owned by the City of Gary (Wikipedia names the city as a partner in the paused project; ownership not otherwise checked). Closed: look from Broadway. The tracks on either side are active railroads; keep off them. Parking not checked.',
  [W('Gary Union Station')],brick='no'),

N('lake-county-sheriffs-house-crown-point','Lake County Sheriff\'s House and Jail','Crown Point','in','civic','standing',41.41562,-87.36364,'exact','open','walk','','1882–1974',
  'A two-storey Second Empire brick house and jail built in 1882 for Lake County, with a three-storey tower and a mansard roof; the Tuscan-columned porch was added about 1890. It was the sheriff\'s home until 1958 and the county jail until 1974. It is the jail John Dillinger escaped from, the foundation\'s tour ending at "public enemy number one\'s cell". Listed on the National Register in 1989, in the Crown Point Courthouse Square district.',
  'The towered, mansard-roofed house on South Main Street, a block from the old courthouse square. The guided tour goes from the sheriff\'s rooms through the workings of the jail to Dillinger\'s cell, with several staircases to climb (foundation\'s page).',
  'The jail John Dillinger walked out of.',
  'Owned and run by the Old Sheriff\'s House Foundation. Its tours page gives tours on Thursdays and Saturdays from early May to late September, or on request with at least five business days\' notice; the tour is not recommended for anyone who has trouble walking. Night tours and paranormal investigations are booked separately. Parking not checked.',
  [['Old Sheriff\'s House Foundation: house and jail tours','https://oldsheriffshouse.org/historic-house-and-jail-tours.html'],W('Lake County Sheriff\'s House and Jail')],
  brick='?',hours='Tours Thursday and Saturday, early May to late September; other times on request'),

N('copshaholm-south-bend','Copshaholm (Oliver Mansion)','South Bend','in','landmark','standing',41.67531,-86.26226,'exact','open','walk','','1895–1896',
  'A 38-room Romanesque Queen Anne mansion built in 1895 and 1896 for Joseph D. Oliver of the Oliver Chilled Plow Works, designed by Charles Alonzo Rich of Lamb and Rich in New York, and named after the family\'s Scottish home village. The Olivers lived in it for 72 years, and its furnishings on all three floors are their own. It is now shown as part of the History Museum in South Bend.',
  'Basement and first two storeys of Indiana fieldstone. Inside: oak, cherry and mahogany woodwork, leaded glass windows, 14 fireplaces and the family\'s furniture, porcelain, silver and bronzes. Round it are 2.5 acres of gardens with a tea house, an Italian sunken garden by Alice E. Neale, a rose garden, a pergola, a tennis lawn and a fountain (Wikipedia).',
  'A plow maker\'s mansion with everything still in it.',
  'Owned and shown by the History Museum, South Bend. Its own page for the mansion (historymuseumsb.org/see-do/historic-house) refused this session (HTTP 403), so hours, tour times and fees were not checked: look them up before going. Parking not checked.',
  [W('Joseph D. Oliver House'),['The History Museum: the Oliver Mansion','https://historymuseumsb.org/see-do/historic-house']],
  brick='?',hours='?'),

N('limberlost-cabin-geneva','Limberlost Cabin (Gene Stratton-Porter\'s home)','Geneva','in','landmark','standing',40.58968,-84.95987,'exact','open','walk','','1894–1895',
  'The fourteen-room, two-storey log house the writer and naturalist Gene Stratton-Porter designed with an architect and lived in from 1895 to 1913, on the edge of Geneva near the Limberlost Swamp. She worked from it on her field studies, photographs and books, writing The Song of the Cardinal here and using the Limberlost as the setting for Freckles, A Girl of the Limberlost and Laddie. It was listed on the National Register in 1974 and is now the Limberlost State Historic Site.',
  'A Queen Anne-style rustic log house at 200 East Sixth Avenue, shown on timed indoor tours with the visitor centre. Interior details not checked. The Limberlost Swamp and Loblolly Marsh nature preserves nearby are open dawn to dusk (ISM page).',
  'Where "A Girl of the Limberlost" was written, on the edge of the swamp itself.',
  'Run by '+ISM+'. Its page gives the site Wednesday to Sunday 10 a.m. to 5 p.m., with timed indoor tours of the cabin at 11 a.m. and 2 p.m., booked online or by calling; walk-up tickets subject to availability; admission charged. Parking not checked.',
  [ISMP('Limberlost','limberlost-state-historic-site'),W('Gene Stratton Porter Cabin (Geneva, Indiana)')],
  brick='?',hours='Wednesday to Sunday 10 a.m. to 5 p.m.; cabin tours 11 a.m. and 2 p.m.'),

N('monon-high-bridge-delphi','Monon High Bridge','Delphi','in','rail','standing',40.58910,-86.64266,'exact','public','walk','','1891',
  'The Monon Railroad\'s trestle over Deer Creek east of Delphi, built in 1891 and crossing the creek 65 feet up, the second highest in Indiana (HMdb marker). CSX vacated the line in the late 1980s, and in 2017 it gave the bridge and almost half a mile of approach to Indiana Landmarks, which repaired a badly damaged pier; decking and railings went on in 2022, and the 1.5-mile Monon High Bridge Trail along the old roadbed was dedicated in September 2023 (Indiana Landmarks).',
  'The trestle high over Deer Creek at the end of the trail; new decking and steel railing cover the west quarter of the bridge for walkers (Indiana Landmarks). Along the trail are the 1916 Centennial Monument, a Bicentennial Plaza and the Freedom Bridge (HMdb). How far out the decked part reaches today was not checked: stay on the decking.',
  'A railroad trestle you can walk out on, 65 feet over a creek.',
  'The bridge belongs to Indiana Landmarks and the trail was built with the City of Delphi and Indiana DNR (Indiana Landmarks). The trail runs from Samuel Milroy Road to the bridge (HMdb marker); trail hours not checked. The trailhead point is a small lot OpenStreetMap maps on Old State Route 25 by the trail\'s west end, about 1.3 km west of the high bridge as the crow flies; the truss over State Road 25 beside that lot is not the High Bridge.',
  [['Indiana Landmarks: Monon High Bridge Trail to be dedicated (2023)','https://www.indianalandmarks.org/2023/09/new-monon-high-bridge-trail-to-be-dedicated-september-6/'],
   ['HMdb: Monon High Bridge Trail','https://www.hmdb.org/m.asp?m=312647']],
  th=[40.59483,-86.65607],thn='Lot on Old State Route 25 (OpenStreetMap)',brick='?'),

N('wabash-erie-canal-delphi','Wabash and Erie Canal Park','Delphi','in','canal','water',40.59174,-86.68052,'site','public','walk','canal','1840s',
  'About a mile of the Wabash and Erie Canal at Delphi, rewatered by Carroll County Wabash and Erie Canal, Inc., founded in 1974; it calls it the longest stretch of the canal open for recreation in Indiana. The canal bed was restored to its old shape and given a constant water supply, and three miles of towpath trail border it (HMdb marker). Beside it is a village of old buildings brought together, among them the 1844 Reed Case House, and an 1874 bowstring arch iron bridge moved here from Paint Creek near Camden in 1999.',
  'The watered canal with its towpath, the 1844 Reed Case House with its canal-era parlour, the 1874 bowstring iron bridge, a 54-foot replica canal boat, the Delphi, and the site of three lime kilns of 1857 near the north dock (HMdb, canal group\'s page). The museum is indoors.',
  'A mile of a canal you can still see water in.',
  'Run by Carroll County Wabash and Erie Canal, Inc. Its visit page: trails open all year dawn to dusk, the park closed at night; the canal museum Monday to Friday 10 a.m. to 4 p.m. (March to December) and Saturday 1 to 4 p.m. in canal season; the Pioneer Village, Reed Case House and public boat rides Saturdays 1 to 4 p.m., late May to mid-September. The pin is the address of the museum, 1030 North Washington Street; parking not checked on the ground.',
  [['Wabash and Erie Canal Park: visit','https://wabashanderiecanal.org/visit/'],['HMdb: Welcome to Canal Park','https://www.hmdb.org/m.asp?m=163280'],W('Wabash and Erie Canal')],
  brick='?',
  hours='Trails dawn to dusk; museum Mon to Fri 10 a.m. to 4 p.m. (March to Dec); village and boat Saturdays 1 to 4 p.m., late May to mid-Sept'),

N('seiberling-mansion-kokomo','Seiberling Mansion (Howard County Museum)','Kokomo','in','landmark','standing',40.48682,-86.14422,'exact','open','walk','','1889–1891',
  'The house Monroe Seiberling of Akron built after he came to Kokomo in 1887 to start a strawboard works and then the Diamond Plate Glass Company. He began it in October 1889 for $50,000 and it was finished within two years, in a mix of Queen Anne and Romanesque Revival. Listed on the National Register in 1972, it belongs to the Howard County Historical Society and holds the Howard County Museum.',
  'The mansion in the Old Silk Stocking Historic District, seen on a self-guided tour; the second and third floors are reached by stairs only, with a video of them on the first floor (museum page). Interior details not checked.',
  'A plate-glass maker\'s mansion, now the county museum.',
  'Owned by the Howard County Historical Society. Its plan-your-visit page: Tuesday to Sunday 1 to 4 p.m., admission charged; guided tours booked at least a month ahead. Free parking behind the museum, entered from West Walnut Street (same page).',
  [['Howard County Museum: plan your visit','https://howardcountymuseum.org/explore/plan-your-visit'],W('Seiberling Mansion')],
  brick='?',hours='Tuesday to Sunday 1 to 4 p.m.'),

N('debs-house-terre-haute','Eugene V. Debs House','Terre Haute','in','landmark','standing',39.4719,-87.4055,'exact','open','walk','','1890',
  'The two-storey frame house the union leader and presidential candidate Eugene V. Debs and his wife Kate built in 1890. James Whitcomb Riley and Carl Sandburg were visitors, and 5,000 people came to the funeral sermon given at the house in 1926. It later had several owners and was a fraternity house from 1948 to 1961. It is a National Historic Landmark (1966) on the Indiana State University campus, kept as a museum by the Eugene V. Debs Foundation.',
  'Original fittings include the cobalt blue porcelain tile fireplace from Italy, the mahogany dining and parlour furniture and the whole set of Haviland china; one room is the Riley bedroom and another is covered in murals of Debs\'s life (Wikipedia).',
  'A labour leader\'s house, china and all.',
  'Run by the Eugene V. Debs Foundation. Its hours page: Tuesday to Saturday noon to 5 p.m., closed on major holidays; group tours and after-hours visits by arrangement. The museum has its own visitor parking on the south side of the house (same page).',
  [['Eugene V. Debs Foundation: hours and directions','https://debsfoundation.org/index.php/landing/visit-the-museum/museum-hours'],W('Eugene V. Debs Home')],
  brick='?',hours='Tuesday to Saturday noon to 5 p.m.'),

N('bridgeton-mill-in','Bridgeton Mill and covered bridge','Bridgeton','in','industry','standing',39.64931,-87.17664,'exact','open','walk','','1871',
  'A gristmill on Big Raccoon Creek at a site milled since about 1823; it bills itself as the oldest continually operating mill in Indiana. The mill before it burned in 1869, and James Rea rebuilt it in 1871; the concrete dam was finished in 1916. Mike and Karen Roe bought it in 1995 and restored it, and it now runs on electric power and grinds more than 20 products. The double-span covered bridge of 1868 by J. J. Daniels just above the dam was burned by an arsonist in 2005; the bridge there now is a 2006 copy built by volunteers.',
  'The working mill beside its 225-foot concrete dam, with the 2006 copy of the covered bridge over the mill pond (it is not the 1868 bridge). Nearby are the 1878 miller\'s house, the Case Cabin, and an office and the Bridgeton Country Store, both of 1868 (Parke County page).',
  'Indiana\'s oldest working mill, below a covered bridge that had to be built twice.',
  'A private working mill that welcomes visitors. Parke County\'s visitor page says the mill is open every day from April to November, and the 1878 House and Case Cabin every weekend from late April to November; daily times not checked. OpenStreetMap maps small lots in the village (Bridgeton Road, Searing Street).',
  [['Parke County: Bridgeton Mill, dam and covered bridge','https://www.coveredbridges.com/things-to-do-1/bridgeton-mill-dam-covered-bridge'],
   ['Inside INdiana Business: Bridgeton Mill to mark 200 years','https://www.insideindianabusiness.com/articles/bridgeton-mill-to-mark-200-years'],W('Bridgeton Covered Bridge')],
  brick='?',hours='Every day April to November (times not checked)'),

N('wylie-house-bloomington','Wylie House','Bloomington','in','landmark','standing',39.16171,-86.53092,'exact','open','walk','','1835',
  'The house Andrew Wylie, first president of Indiana University, built in 1835 on a 20-acre tract near the college; he, his wife Margaret and ten of their children lived here until his death in 1851. From 1859 it was the home of Theophilus Wylie, a professor and early photographer, whose family stayed until 1913. Indiana University Libraries runs it as a house museum, shown as it would have looked before 1860.',
  'A two-storey brick house with a Flemish bond front, with historic gardens and an education centre behind (Wikipedia, museum page). Free guided tours go through the house; the second floor is up stairs only. Interior details not checked.',
  '',
  'Owned and run by Indiana University Libraries. Its page: free guided tours Friday and Saturday 10 a.m. to 4 p.m., on the hour, the last at 3 p.m.; closed on major holidays and during university breaks. Free Wylie House spaces behind the museum off the alley, and two-hour street parking on Second Street (same page).',
  [['IU Libraries: Wylie House Museum','https://libraries.indiana.edu/wylie-house-museum'],W('Wylie House')],
  brick='?',hours='Friday and Saturday 10 a.m. to 4 p.m., tours on the hour (last 3 p.m.); closed university breaks'),

N('tc-steele-house-studio','T. C. Steele House and Studio (House of the Singing Winds)','Nashville','in','landmark','standing',39.13177,-86.34801,'exact','open','drive','','1907–1926',
  'The hilltop home and studio of the Hoosier Group painter Theodore Clement Steele and his second wife Selma, who named it the House of the Singing Winds. They enlarged the house in 1911 when they bought land to bring it to 211 acres, adding gardens, a barn-sized studio and gallery and outbuildings. Selma gave it all to the state shortly before her death in 1945; it was listed on the National Register in 1973 as the Theodore Clement Steele House and Studio.',
  'The house and the large studio, where Steele\'s paintings are seen only on the guided indoor tour; lily ponds and formal, hillside and perennial gardens; a two-storey log cabin of about 1875 that Selma moved here in the early 1930s to save it; five trails; and the family cemetery (Wikipedia, ISM page).',
  'A painter\'s studio on a Brown County ridge, with his pictures still on the walls.',
  'Run by '+ISM+'. Its page: Wednesday to Sunday 10 a.m. to 5 p.m.; indoor tours of the house and studio at 10:15 a.m., 1:15 and 3:15 p.m., bookable online; grounds, gardens and trails need a ticket bought on site. Parking lots on the site (OpenStreetMap).',
  [ISMP('T.C. Steele','tc-steele'),W('T. C. Steele State Historic Site')],
  th=[39.12982,-86.34946],thn='T.C. Steele State Historic Site lot',brick='?',
  hours='Wednesday to Sunday 10 a.m. to 5 p.m.; house and studio tours 10:15 a.m., 1:15 and 3:15 p.m.'),

N('medora-covered-bridge','Medora Covered Bridge','Medora','in','landmark','standing',38.818497,-86.148029,'exact','public','walk','','1875',
  'The longest historic covered bridge in the United States: J. J. Daniels built it in 1875 in nine months for $18,142, a three-span Burr arch truss with 431 feet between the abutments and a roof 461 feet long. It carried U.S. 50 until 1935 and State Road 235 until 1972, when a new bridge alongside replaced it. Set for demolition in 1968, it was saved by Governor Whitcomb in 1971, and the original truss is still in place with repairs. It is on the National Register.',
  'The three-span covered bridge over the East Fork of the White River, beside the modern State Road 235 bridge about a mile east of Medora; Indiana\'s last three-span covered bridge (HMdb marker). Restored in 2010, closed to cars since 1972 and open to walkers (Islands.com).',
  'The longest historic covered bridge in the country.',
  'Owner not checked. Islands.com says pedestrians may walk across, and that a small access road on the west side of the river leads to parking, a picnic area and the river; that lot is not mapped in OpenStreetMap and the pin check\'s aerial was used to look for it. No hours known.',
  [W('Medora Covered Bridge'),['HMdb: Medora Covered Bridge','https://www.hmdb.org/m.asp?m=74047'],
   ['Islands.com: Medora Covered Bridge','https://www.islands.com/1834254/medora-covered-bridge-longest-historic-america-indiana-timeless-midwest-riverfront-charm']],
  brick='no'),

N('monastery-immaculate-conception-ferdinand','Monastery Immaculate Conception (the Castle on the Hill)','Ferdinand','in','worship','standing',38.22501,-86.85538,'exact','open','walk','','1883–1924',
  'The monastery of one of the largest communities of Benedictine women in the United States, on a hill east of Ferdinand called Mount Tabor. The quadrangle where the sisters live was built from 1883 to 1888, with a large addition in 1903; the domed Romanesque Revival chapel, by the St. Louis architect Viktor Klutho, was begun in 1915 and its interior finished in 1924. It was listed on the National Register in 1983 as the Convent Immaculate Conception Historic District.',
  'Inside the chapel: a Gothic high altar with statues from Munich of the Immaculate Conception, St. Benedict and St. Scholastica, pews hand-carved by German craftsmen, Stations of the Cross carved in Munich, 47 Munich stained glass windows, and 89 angels in glass, statues and carvings (Wikipedia). Grounds open dawn to dusk.',
  'A domed convent church with 47 Munich windows above a small German town.',
  'The Sisters of St. Benedict of Ferdinand. Their page: grounds open dawn to dusk; guided tours Tuesday to Friday at 10 a.m., 11 a.m., 1 and 2 p.m. and Saturday and Sunday at 1 and 2 p.m., not on dates the page lists (including November 26 to 29 and December 24 to 31, 2026); visitors welcome at the Liturgy of the Hours and Mass. Parking not checked.',
  [['Sisters of St. Benedict: at the monastery','https://www.thedome.org/at-the-monastery/'],W('Monastery Immaculate Conception')],
  brick='?',hours='Tours Tue to Fri 10 a.m., 11 a.m., 1 and 2 p.m., Sat and Sun 1 and 2 p.m.; Mass Sunday 10:30 a.m.; grounds dawn to dusk'),

N('community-house-no-2-new-harmony','Community House No. 2, New Harmony','New Harmony','in','town','standing',38.13036,-87.93478,'exact','open','walk','','1822',
  'A three-storey brick dormitory the Harmonists built in 1822 for their single members, later used by Robert Owen\'s community for its gatherings and a school. The Harmonist and Owenite buildings of 1814 to 1867 make up a National Register district that takes in sixteen National Historic Landmarks. The state runs Community House No. 2, Thrall\'s Opera House (Community House No. 4, 1824), the Fauntleroy House, the Mattias Scholle House, the Harmonist Cemetery and the Harmonist Labyrinth (Wikipedia, 2012).',
  'Community House No. 2 at 410 Main Street can be seen on a self-guided visit; the 90-minute guided Historic Properties tour starts there and goes partly outdoors across several buildings. Nearby are the walled Harmonist cemetery (no gravestones, its wall built of brick from the second Harmonist church), part of the old rope walk, and the Labyrinth, replanted in 1939 near its first site (Wikipedia). Interior details not checked.',
  'The dormitory of a celibate German utopia on the Wabash.',
  'Run by '+ISM+'. Its page: Wednesday to Sunday 10 a.m. to 5 p.m.; self-guided visits to Community House No. 2 from 10 a.m. to 4:40 p.m. Central; guided Historic Properties tours Wednesday to Sunday at 11 a.m., 1 and 3:30 p.m. Central; admission charged; no photography on tours. Parking not checked.',
  [ISMP('New Harmony','new-harmony-historic-site'),W('New Harmony Historic District')],
  brick='?',hours='Wednesday to Sunday 10 a.m. to 5 p.m.; guided tours 11 a.m., 1 and 3:30 p.m. Central'),

N('fort-knox-ii-vincennes','Fort Knox II site','Vincennes','in','fort','traces',38.72503,-87.50572,'site','public','walk','forts','1803–1813',
  'A frontier army fort built in 1803 at Petit Rocher, a landing on the Wabash about three miles north of Vincennes, when the War Department set aside $200 for a new post. Late in 1811 William Henry Harrison mustered his regulars and militia here before marching on Prophetstown and the Battle of Tippecanoe. In 1813 the army judged it too far to protect the town, and the fort was taken apart, floated down the river and put up again near the first Fort Knox (Wikipedia). The site is a state historic site and on the National Register (1982).',
  'Nothing of the fort stands: its outline is marked with short posts, with interpretive signs in a park setting above the river (Wikipedia, Vincennes tourism page); a photograph on Wikimedia Commons shows them as a low wall of upright logs, described as reconstructed palisades.',
  'The field where Harrison gathered the army that fought at Tippecanoe.',
  'Part of the Vincennes State Historic Sites run by '+ISM+'; its plan-your-visit page says self-guided outdoor visits to Fort Knox II and Sugarloaf Mound are free, Wednesday to Sunday 10 a.m. to 5 p.m. Near Ouabache Trails Park on the north side of Vincennes. Parking not checked.',
  [ISMP('Vincennes State Historic Sites','vincennes-state-historic-site'),W('Forts of Vincennes, Indiana'),
   ['Visit Vincennes: Fort Knox II','https://visitvincennes.org/attractions/fort-knox-ii/']],
  brick='no',hours='Wednesday to Sunday 10 a.m. to 5 p.m. (self-guided, free)'),

N('culbertson-mansion-new-albany','Culbertson Mansion','New Albany','in','landmark','standing',38.28637,-85.81272,'exact','open','walk','','1867–1869',
  'The 25-room Second Empire mansion of William Culbertson, once the richest man in Indiana, designed by the local architect James T. Banes, begun in 1867 for $120,000 and finished in November 1869. After his death his third wife sold the house and contents in 1899 for $7,100; it later belonged to the American Legion, which altered it, and was nearly torn down for a gas station in the 1960s before it was saved. It is now a state historic site.',
  'Three storeys and about 20,000 square feet: hand-painted and frescoed ceilings and walls, a carved rosewood-grained staircase, hand-painted floors, marble fireplaces and crystal chandeliers; the first tin roof came from Scotland. The tour takes in the parlours, dining rooms, bedrooms, kitchen and laundry (Wikipedia). Interior as restored now not checked.',
  'The house of the richest man in Indiana, saved from a gas station.',
  'Run by '+ISM+'. Its page: Wednesday to Sunday 10 a.m. to 5 p.m.; guided tours start at the front door, at East Main and East 10th streets (ring the bell); walk-up tickets subject to availability; admission charged. Parking not checked.',
  [ISMP('Culbertson Mansion','culbertson-mansion-historic-site'),W('Culbertson Mansion State Historic Site')],
  brick='?',hours='Wednesday to Sunday 10 a.m. to 5 p.m., guided tours'),
]

PIN_NOTES={
 'city-methodist-church-gary':'Wikipedia coordinate, on the church block at Washington Street and Sixth Avenue; checked on the aerial.',
 'gary-union-station':'ArcGIS geocoder point for the named station, beside Wikipedia\'s coordinate (41.60564, -87.33696); checked on the aerial.',
 'lake-county-sheriffs-house-crown-point':'ArcGIS PointAddress for 226 South Main Street, Crown Point.',
 'copshaholm-south-bend':'ArcGIS PointAddress for 808 West Washington Street, South Bend.',
 'limberlost-cabin-geneva':'ArcGIS PointAddress for 200 East Sixth Avenue (geocoded as E 6th St), Geneva; OpenStreetMap\'s Limberlost State Historic Site area is 20 m away.',
 'monon-high-bridge-delphi':'OpenStreetMap names a truss over State Road 25 the Monon High Bridge (40.59407, -86.65476), but that is the trail\'s crossing of the highway; the pin is moved with tools/pix.py onto the rail bridge over Deer Creek, where OpenStreetMap maps the abandoned line named High Bridge, seen on the aerial.',
 'wabash-erie-canal-delphi':'ArcGIS PointAddress for 1030 North Washington Street, the canal museum address; the canal runs beside it.',
 'seiberling-mansion-kokomo':'OpenStreetMap museum point at 1200 West Sycamore Street (tools/nom.py).',
 'debs-house-terre-haute':'OpenStreetMap museum point at 451 North Eighth Street (tools/nom.py).',
 'bridgeton-mill-in':'OpenStreetMap building named Bridgeton Mill (tools/nom.py).',
 'wylie-house-bloomington':'OpenStreetMap museum point at 307 East Second Street (tools/nom.py).',
 'tc-steele-house-studio':'ArcGIS PointAddress for 4220 T.C. Steele Road.',
 'medora-covered-bridge':'Position of the HMdb Medora Covered Bridge marker, by the bridge.',
 'monastery-immaculate-conception-ferdinand':'ArcGIS PointAddress for 802 East Tenth Street fell on the lawn; moved with tools/pix.py onto the domed chapel seen on the aerial.',
 'community-house-no-2-new-harmony':'OpenStreetMap point for the building named Community House 2 on Main Street (tools/nom.py); the geocoder\'s interpolated point for 410 Main Street fell in the street 70 m south.',
 'fort-knox-ii-vincennes':'The National Register list point (38.724167, -87.506667) fell in an open field; moved with tools/pix.py about 130 m north-east onto the rectangular post outline seen on the aerial, beside the ArcGIS point for Fort Knox II (38.7252, -87.5058).',
 'culbertson-mansion-new-albany':'OpenStreetMap building for the Culbertson Mansion State Historic Site, 914 East Main Street (tools/nom.py).',
}
