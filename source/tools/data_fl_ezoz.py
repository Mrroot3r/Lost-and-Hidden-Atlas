# November 21, 2026: a first scatter across Florida outside St. Augustine. Florida was the state with the fewest places
# that nobody held (tools/choose.py --thinnest). Thirteen places spread from Pensacola to Key West: brick forts
# of the Third System, coquina and limestone sugar-mill ruins, a tabby plantation, lighthouses, a utopian colony's
# settlement and two standing houses.
# Sources read in this session: Wikipedia articles (tools/wiki_raw.py), and the managing bodies' own pages read with
# tools/page.py: National Park Service pages for Timucuan Preserve, Dry Tortugas and Gulf Islands; the Florida State
# Parks system guide booklet (a PDF on floridastateparks.org; the park web pages themselves answer 403); the U.S. Fish
# and Wildlife Service's St. Marks refuge pages; Volusia County's Sugar Mill Ruins page; Bok Tower Gardens' own FAQ; the
# City of Palatka's facility page. Nothing was checked on the ground. Interiors are as the sources say, else not checked.
from data_b import N
from data_ma import W
BATCH={'key':'fl_ezoz','label':'Florida: first scatter, Pensacola to Key West','added':'2026-11-21 16:24'}

FSP=['Florida State Parks system guide (PDF; hours where it gives them)','https://www.floridastateparks.org/sites/default/files/media/file/FSPSystemGuide_Booklet_ForReview-1.pdf']
SPH=' Florida state parks are open from 8 a.m. to sunset every day of the year according to Wikipedia; the park\'s own web page refused the tool (HTTP 403), so the hours were not read from the operator and are not given as hours.'

PLACES=[
N('kingsley-plantation','Kingsley Plantation','Jacksonville (Fort George Island)','fl','landmark','standing',30.43833,-81.43806,'site','open','drive','','1797–1798',
  'A plantation at the north tip of Fort George Island, at the mouth of the St. Johns River, begun under British rule in 1765 and held longest by Zephaniah Kingsley, who lived there about 25 years with his wife Anna Madgigine Jai, a former slave, and their family. Buying, training and selling enslaved people was its main business; cotton came second. The state bought it in 1955 and the National Park Service took it over in 1991, as part of the Timucuan Ecological and Historic Preserve.',
  'The owner\'s house, built probably in 1797–1798 and called the oldest plantation house standing in Florida, with its kitchen house and barn, and the remains of 25 slave cabins set out in an arc, built of tabby (lime burned from old Timucua shell middens, mixed with sand and shell). The cabins are among the best preserved in the United States. The planter\'s house opens only on days the park calendar lists; interior not checked.',
  'Tabby slave cabins in an arc, the best preserved anywhere in the country.',
  'National Park Service, Timucuan Ecological and Historic Preserve. Admission free (NPS visiting page). The grounds are open Wednesday to Sunday, 9 a.m. to 5 p.m.; all NPS areas of the preserve close on Thanksgiving, December 25 and January 1 (NPS hours page). The planter\'s house opens on the days the park calendar gives. Park in the lot on Palmetto Avenue by the house.',
  [W('Kingsley Plantation'),['NPS: Timucuan Preserve hours','https://www.nps.gov/timu/planyourvisit/hours.htm'],['NPS: Visiting Kingsley Plantation','https://home.nps.gov/timu/learn/historyculture/kp_visiting.htm']],
  th=[30.43885,-81.43743],thn='Kingsley Plantation lot, Palmetto Avenue',hours='Wednesday to Sunday 9 a.m. to 5 p.m.; closed Thanksgiving, December 25 and January 1',brick='?'),

N('fort-clinch','Fort Clinch','Fernandina Beach','fl','fort','standing',30.70469,-81.45446,'exact','open','drive','forts','1847',
  'A pentagonal brick fort of the Third System at the north end of Amelia Island, guarding the mouth of the St. Marys River and Cumberland Sound, where Spain first fortified the point in 1736. The United States began it in 1847. Confederate forces seized it early in 1861; Union troops took it back and used it as a base for the rest of the war. It went to caretaker status in 1869, was garrisoned again in 1898, and was restored by the Civilian Conservation Corps in the 1930s.',
  'Inner and outer walls of almost five million bricks, corner bastions with embrasures, and buildings in the courtyard including a two-storey barracks, restored to the Civil War years. Daily tours with reenactors in period dress, and on the first weekend of every month a garrison fires cannon and shows other skills (Florida State Parks guide).',
  'A Civil War brick fort kept as if the garrison never left.',
  'Fort Clinch State Park (Florida Department of Environmental Protection), 2601 Atlantic Avenue. A vehicle entrance fee and a separate fort entrance fee apply (the park\'s 2025 group-tour form gives both).'+SPH+' Park at the lots by the fort.',
  [W('Fort Clinch'),FSP,['Fort Clinch State Park tour form (fees)','https://www.floridastateparks.org/sites/default/files/media/file/Tour%20Request%20Fort%20Clinch%20web4-24-25_0.pdf']],
  th=[30.70357,-81.45318],thn='Fort Clinch lot, Fort Clinch Road',hours='?',brick='yes'),

N('yulee-sugar-mill-ruins','Yulee Sugar Mill Ruins','Homosassa','fl','industry','ruins',28.78368,-82.60758,'site','public','drive','','1851–1864',
  'The steam sugar mill of David Levy Yulee, Florida\'s first United States senator of Jewish heritage, at the centre of a plantation of about 5,000 acres worked by about 1,000 enslaved people who grew sugarcane, citrus and cotton. The mill ran from 1851 to 1864 and made sugar, syrup and molasses; it supplied Confederate troops. Union forces burned Yulee\'s house in May 1864 but missed the mill, which was abandoned and fell to ruin.',
  'The masonry foundation, a well and a 40-foot chimney (the state park guide calls it limestone masonry), with iron gears, a cane press and other machinery, and interpretive panels round the mill. The masonry was stabilised after a 1997 survey. A pavilion stands across the street.',
  '',
  'Yulee Sugar Mill Ruins Historic State Park, State Road 490 (West Yulee Drive), Homosassa.'+SPH+' The parking lot was not found on the map and not checked.',
  [W('Yulee Sugar Mill Ruins Historic State Park'),FSP],hours='?',brick='no'),

N('new-smyrna-sugar-mill-ruins','New Smyrna Sugar Mill Ruins (Cruger and DePeyster mill)','New Smyrna Beach','fl','industry','ruins',29.00918,-80.94067,'exact','public','walk','burned','1830–1835',
  'A steam sugar mill and sawmill built in 1830 for the New York merchants William DePeyster and Henry Cruger, worked by enslaved people under an overseer. On Christmas Day 1835, early in the Second Seminole War, Seminoles burned the mills; the walls stood, and the West Point Foundry machinery inside was taken to the Dunlawton mill. For years the ruins were wrongly said to be a Spanish mission, a story that still circulates.',
  'Coquina walls of the crushing house, with its chimney and big arched door and window openings, at 600 Old Mission Road. Soldiers stationed there afterwards altered the site.',
  'Long passed off as a Spanish mission; it was a sugar mill burned in 1835.',
  'Volusia County park, 600 Old Mission Road. Open daily, sunrise to sunset (county page). Parking at the site was not checked.',
  [W('New Smyrna Sugar Mill Ruins'),['Volusia County: Sugar Mill Ruins','https://www.volusia.org/services/community-services/parks-recreation-and-culture/parks-and-trails/park-facilities-and-locations/historical-parks/sugar-mill-ruins.stml']],
  hours='Daily, sunrise to sunset',brick='no'),

N('koreshan-unity-settlement','Koreshan Unity Settlement','Estero','fl','town','standing',26.43356,-81.81213,'site','open','drive','','1882–1920',
  'The "New Jerusalem" of the Koreshan Unity, a celibate communal sect led by Cyrus Teed, who called himself Koresh and taught that people live on the inside of a concave earth. The group moved here from Chicago in 1894; Teed dreamed of a city of ten million. After his death in 1908 the colony declined, and its last members gave the land to the state in 1961. Hedwig Michel, the last member, lived in the Planetary Court until she died in 1982.',
  'Eleven historic buildings dating from 1882 to 1920, among them the Founder\'s House, the Planetary Court (the women\'s ruling council), the bakery, machine shops and Art Hall, set in the colony\'s gardens of imported trees on the Estero River (Wikipedia; Florida State Parks guide). Which buildings open inside was not checked.',
  'A concave-earth utopia\'s village, kept by the state.',
  'Koreshan State Park, 3800 Corkscrew Road at U.S. 41, Estero (Florida State Parks). Campground, boat ramp and trails.'+SPH+' Parking was not checked: the mapped lot by U.S. 41 did not plainly show as a lot on the aerial.',
  [W('Koreshan State Historic Site'),W('Koreshan Unity'),FSP],
  hours='?',brick='?'),

N('cape-florida-light','Cape Florida Light','Key Biscayne','fl','light','standing',25.66659,-80.15596,'site','open','drive','','1825',
  'A brick lighthouse built in 1825 at the south tip of Key Biscayne, where enslaved people and Black Seminoles had boarded boats for the Bahamas. Seminoles attacked it on July 23, 1836, and the fire shattered the lens; it was rebuilt and relit in 1847, raised and relit again in 1856, put out by Confederate sympathisers in 1861, and taken out of service in 1878. Later owners sank a new foundation under it, and it rode out the 1926 hurricane. It was restored and relit in 1996.',
  'The tower, the oldest standing structure in Miami-Dade County (state park guide), with a museum in a 1970 replica of the keeper\'s cottage and kitchen. Guided tours of the lighthouse and cottage twice a day, Thursday to Monday (Florida State Parks guide); times not checked.',
  'Burned in a Seminole attack in 1836 and still standing.',
  'Bill Baggs Cape Florida State Park, 1200 S. Crandon Boulevard, Key Biscayne. Park entrance fee charged (not checked).'+SPH+' Park at the lot north of the lighthouse.',
  [W('Cape Florida Light'),FSP],th=[25.66948,-80.15592],thn='Bill Baggs park lot, Cape Florida Park Boulevard',hours='Lighthouse tours twice a day, Thursday to Monday',brick='?'),

N('fort-zachary-taylor','Fort Zachary Taylor','Key West','fl','fort','standing',24.54775,-81.81041,'exact','open','drive','forts','1845',
  'A Third System brick fort at the south-west end of Key West, begun in 1845 and named in 1850 for President Zachary Taylor. The Army leased enslaved men to build it. Union troops occupied it in January 1861 and held it through the war. In 1898 it was cut down to two storeys and new concrete batteries were put inside. Civil War guns buried in its abandoned parts were dug out from 1968 by volunteers led by Howard S. England; the state opened it to the public in 1985.',
  'Brick walls (made by Raiford and Abercrombie of Pensacola) cut down to two levels, with the 1898 Battery Osceola and Battery Adair inside, and a large collection of Civil War cannon. Guided tours of the fort are given daily (Florida State Parks guide).',
  '',
  'Fort Zachary Taylor Historic State Park, 601 Howard England Way, reached through the Truman Annex.'+SPH+' Parking inside the park was not checked.',
  [W('Fort Zachary Taylor'),FSP],hours='?',brick='yes'),

N('fort-pickens','Fort Pickens','Pensacola Beach (Santa Rosa Island)','fl','fort','standing',30.327,-87.2907,'exact','open','drive','forts','1829–1834',
  'The largest of four forts built to guard Pensacola Bay and its navy yard: a five-sided brick fort of 21.5 million bricks, built from 1829 to 1834, much of it by enslaved people. Lieutenant Slemmer held it for the Union in January 1861 and it never fell. Geronimo and several of his warriors were imprisoned there from October 1886 to May 1887. On June 20, 1899 a fire reached the magazine in Bastion D and the blast destroyed that bastion. The Army used the site until 1947.',
  'The brick fort with the wrecked Bastion D, the concrete Battery Pensacola built inside the walls in the 1890s, and ruins of later batteries east and west of it, including Battery Langdon of 1923. Ranger tours or a self-guided tour; a park store is inside the fort (NPS).',
  'Where Geronimo was held, and a bastion blown apart in 1899.',
  'Gulf Islands National Seashore (National Park Service), Fort Pickens Area at the west end of Fort Pickens Road. Entrance fee (NPS). Storms close the road at times; NPS posts closures. Opening hours were not read on any NPS page.',
  [W('Fort Pickens'),['NPS: Fort Pickens Area','https://nps.gov/guis/planyourvisit/fort-pickens-area.htm'],['NPS: Fort Pickens history','https://nps.gov/guis/learn/historyculture/fort-pickens.htm']],
  th=[30.3303,-87.29273],thn='Beach lot on Fort Pickens Road, about 400 m from the fort',hours='?',brick='yes'),

N('san-marcos-de-apalache','San Marcos de Apalache','St. Marks','fl','fort','ruins',30.15194,-84.21083,'site','open','drive','forts','1679',
  'A Spanish post at the meeting of the Wakulla and St. Marks rivers: a wooden stockade from 1679, and from 1759 a stone fort built to stand up to ships\' guns. The British, the Spanish again, Andrew Jackson in 1818 (the Arbuthnot and Ambrister affair took place there) and the Confederates, who called it Fort Ward, all held it. In 1859 the federal government built a marine hospital from the fort\'s stones, and the site was abandoned after 1865.',
  'Small pieces of the stone fort, including a bombproof wall, and a museum built on the foundation of the 1859 hospital, with pottery and tools dug near the fort and a large-screen video. A stone well and a retaining wall are reconstructions. A self-guided trail runs round the site.',
  'Six flags over one stone fort, carted off to build a hospital.',
  'San Marcos de Apalache Historic State Park, 148 Old Fort Road, St. Marks (Florida State Parks). Open 9 a.m. to 5 p.m., Thursday to Monday, except Thanksgiving, Christmas and New Year\'s Day (state park guide). A lot on Old Fort Road.',
  [W('San Marcos de Apalache Historic State Park'),FSP],th=[30.15202,-84.20975],thn='Lot on Old Fort Road',
  hours='Thursday to Monday 9 a.m. to 5 p.m.; closed Thanksgiving, Christmas and New Year\'s Day',brick='no'),

N('st-marks-light','St. Marks Light','St. Marks National Wildlife Refuge','fl','light','standing',30.07397,-84.17958,'exact','open','drive','','1831, rebuilt 1842',
  'A lighthouse on Apalachee Bay first built in 1829–1831; the inspector refused it at first because its walls were hollow. Erosion forced a new tower farther inland in 1842, re-using the lantern. Confederate troops were stationed by it in 1865. A fourth-order Fresnel lens was lit in 1867, and the tower was raised ten feet in 1883 to its present focal plane of 82 feet. The tower and keeper\'s house were renovated in 2017–2018.',
  'The tower (the refuge page says the first tower was of brick and stone) and the keeper\'s quarters, which open on Friday, Saturday and Sunday from 11 a.m. to 3 p.m. No climbing the tower at present (refuge pages). Interior beyond that not checked.',
  '',
  'U.S. Fish and Wildlife Service, St. Marks National Wildlife Refuge, at the end of Lighthouse Road. The refuge is open year-round in daylight hours; the visitor center Monday to Friday 8 a.m. to 4 p.m., weekends 10 a.m. to 5 p.m.; an entrance fee applies, America the Beautiful passes honoured (refuge visit page). Lot at the end of Lighthouse Road.',
  [W('St. Marks Light'),['USFWS: Historic St. Marks Lighthouse','https://www.fws.gov/refuge/st-marks/historic-st-marks-lighthouse'],['USFWS: St. Marks refuge, visit us','https://fws.gov/refuge/st-marks/visit-us']],
  th=[30.07421,-84.18012],thn='Lighthouse Road lot',hours='Keeper\'s quarters Friday to Sunday 11 a.m. to 3 p.m.; refuge open in daylight hours',brick='?'),

N('bok-singing-tower','Bok Tower (the Singing Tower)','Lake Wales','fl','landmark','standing',27.93533,-81.5775,'exact','open','drive','','1927–1929',
  'A 205-foot Gothic Revival carillon tower built in 1927–1929 on Iron Mountain, one of the highest points of peninsular Florida, as the centre of the sanctuary garden the editor Edward Bok gave to the nation. Its 60 bells were cast by John Taylor and Company of Loughborough, England. The gardens are a National Historic Landmark, and the 1930–1932 Pinewood Estate (El Retiro) mansion stands in them.',
  'Pink Etowah and grey Creole marble from Georgia and coquina stone, with ceramic mosaics and eight 35-foot grilles near the top, mirrored in a reflecting pool; the marble Exedra of 1930 north of it. Daily visitors cannot go inside the tower (Bok Tower Gardens). El Retiro is shown by tour, Tuesday to Sunday, for an extra fee.',
  'A marble carillon tower on the highest ground of peninsular Florida.',
  'Bok Tower Gardens, a private non-profit garden; admission charged. Open from 8 a.m. daily, last admission 5 p.m., closed Thanksgiving and Christmas Day; El Retiro tours Tuesday to Sunday from 10 a.m. (garden FAQ; closing time not given in the lines read). Visitor lot on Bok Tower Road.',
  [W('Bok Tower Gardens'),['Bok Tower Gardens: questions and answers','https://boktowergardens.org/faq']],
  th=[27.93694,-81.57494],thn='Bok Tower Gardens lot, Bok Tower Road',hours='Daily from 8 a.m., last admission 5 p.m.; closed Thanksgiving and Christmas Day',brick='no'),

N('bronson-mulholland-house','Bronson–Mulholland House (Sunny Point)','Palatka','fl','landmark','standing',29.65041,-81.6282,'exact','open','walk','','1854',
  'A columned house built in 1854 by Judge Isaac H. Bronson, one of Palatka\'s founders, at the centre of a citrus plantation he called Sunny Point. After the Civil War Charlotte White ran a school there for freed people, and Mary Mulholland, a teacher and former Union nurse, took the house over in 1904. It later became apartments and was sold to the city, which runs it as a museum.',
  'Grand columns and wide porches of the antebellum house, in a small park at 100 Madison Street. Tours and programmes are held through the year (City of Palatka); the rooms were not checked.',
  '',
  'City of Palatka, 100 Madison Street; admission free (city facility page, which gave no hours). The Clio site lists Thursday to Monday noon to 5 p.m., closed Tuesday and Wednesday, but that is a directory, so it is not given as hours. Parking not checked.',
  [W('Bronson–Mulholland House'),['City of Palatka: Bronson-Mulholland House','https://palatka-fl.gov/Facilities/Facility/Details/BronsonMulholland-House-9'],['Clio: Bronson-Mulholland House','https://www.theclio.com/entry/21376']],
  hours='?',brick='?'),

N('gamble-plantation-mansion','Gamble Plantation mansion','Ellenton','fl','landmark','standing',27.5222,-82.5266,'site','open','drive','','1840s',
  'The house of Major Robert Gamble, headquarters of one of the sugar plantations opened along the Manatee River after the Second Seminole War ended in 1842. Enslaved workers built it over five or six years, of tabby, with two-foot-thick walls and columns. It decayed badly and the state finished restoring it in 1927. The state park is named as a Confederate memorial to Judah P. Benjamin.',
  'The Greek Revival mansion, its columns and walls of tabby, a 40,000-gallon covered cistern beside it, and the 1872 frame Patten House. The brick ruins of the plantation\'s sugar mill, bought by the state in 2002 and fenced, stand half a mile north on State Road 683. Whether the house is open is not settled: Wikipedia says it was closed to the public in 2014 for termite and water damage, and also that guided tours are given; the state park guide says it is furnished as a plantation home.',
  '',
  'Judah P. Benjamin Confederate Memorial at Gamble Plantation Historic State Park, 3708 U.S. Highway 301, Ellenton (Florida State Parks). The visitor center is open Thursday to Monday, 9 a.m. to 11:45 a.m. and 12:45 to 5 p.m., except Thanksgiving, Christmas and New Year\'s Day (state park guide). Parking at the park was not checked.',
  [W('Judah P. Benjamin Confederate Memorial at Gamble Plantation Historic State Park'),FSP],
  conf='mixed',hours='Visitor center Thursday to Monday 9 to 11:45 a.m. and 12:45 to 5 p.m.; closed Thanksgiving, Christmas, New Year\'s Day',brick='some'),
]

PIN_NOTES={
 'kingsley-plantation':'Wikipedia infobox coordinate, in the wooded plantation grounds; on the aerial the house and the cabin arc were not picked out under the trees, so site precision. The lot tile shows a sandy clearing on Palmetto Avenue.',
 'fort-clinch':'Wikipedia infobox coordinate; on the aerial and LiDAR it is in the parade ground of the pentagonal fort.',
 'yulee-sugar-mill-ruins':'OpenStreetMap ruins feature (nom.py). Aerial shows only tree canopy and the LiDAR shows no plain structure, so site precision.',
 'new-smyrna-sugar-mill-ruins':'Moved 54 m with pix.py from the Wikipedia coordinate onto the rectangular coquina ruin visible in a clearing on the aerial.',
 'koreshan-unity-settlement':'OpenStreetMap building "Planetary Court" (nom.py).',
 'cape-florida-light':'Wikipedia infobox coordinate, on the shore at the tip of the key; the tower itself was not picked out for certain on the aerial (a long shadow lies across the sand beside the pin), so site precision.',
 'fort-zachary-taylor':'OpenStreetMap fort feature (nom.py); on the aerial it is on the fort\'s west curtain inside the moat.',
 'fort-pickens':'Wikipedia infobox coordinate; on the aerial it is on the fort itself.',
 'san-marcos-de-apalache':'Wikipedia infobox coordinate; on the aerial it is on the museum building at the river point.',
 'st-marks-light':'The Wikipedia coordinate fell in the bay; moved with pix.py onto the red-roofed keeper\'s house and tower at the end of Lighthouse Road, seen on the lot tile.',
 'bok-singing-tower':'Wikipedia infobox coordinate for the gardens; on the aerial it falls on the tower and its shadow at the head of the lawn.',
 'bronson-mulholland-house':'OpenStreetMap museum at 100 Madison Street (nom.py); on the aerial a house in Mulholland Park, the city park that holds it.',
 'gamble-plantation-mansion':'Wikipedia infobox coordinate, on trees inside the state park grounds north of U.S. 301; the mansion was not picked out for certain on the aerial, so site precision.',
}
