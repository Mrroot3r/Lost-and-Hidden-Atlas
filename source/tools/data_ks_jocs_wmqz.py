# November 24, 2026: Johnson County, Kansas, third pass (Overland Park, Merriam, Shawnee, Spring Hill).
# The register lists for the county had been used by two earlier batches, so these come from the Clio walking tour of
# Olathe, Overland Park and Shawnee, the Wikipedia articles read with tools/wiki_raw.py, the Overland Park Historical
# Society's visit page, the City of Spring Hill's pages and the Kansas Historical Society's register search.
from data_b import N
from data_ma import W
KSNR='https://www.kansashistory.gov/natreg/natreg_listings/search/page:%d/county:JO/records:all/submit:SEARCH'
CLIO='https://theclio.com/tour/1012/%d'
BATCH={'key':'ks_jocs_wmqz','label':'Johnson County, Kansas (third pass)','added':'2026-11-24 04:49'}
PLACES=[
N('strang-carriage-house-overland-park-ks','Strang Carriage House','Overland Park, Kansas','ks','landmark','standing',38.98260,-94.67188,'site','open','drive','','1915',
  'William B. Strang Jr., who laid out Overland Park in 1906 and ran the interurban line that served it, built this limestone carriage house in 1915 for his carriages and cars, with rooms upstairs for his chauffeurs. Clio calls it one of the oldest buildings standing in Overland Park. Since 1990 it has been the home of the Overland Park Historical Society, which keeps a small museum of local objects in it.',
  'A rough limestone building with a clay tile roof and its original wooden doors; the society has heavily renovated the inside. Small collections of local artifacts. Opening times were not found.',
  'What is left of the man who made Overland Park, a few blocks from his car barn.',
  'Home of the Overland Park Historical Society on Santa Fe Drive in the old downtown (the address lookup gave 8045 Santa Fe Drive). Street parking is free in the district. No page read gives opening times for this building: the society\'s visit page describes its other museum, Discover O.P., and does not mention the carriage house. Check with the society before going.',
  [W('Strang Carriage House'),['Clio: Strang Carriage House',CLIO%17],['Overland Park Historical Society: plan your visit','https://ophistorical.org/hours-and-locations.html']],
  hours='?',brick='no'),
N('strang-depot-overland-park-ks','Strang Depot (Discover O.P.)','Overland Park, Kansas','ks','rail','standing',38.98383,-94.67193,'site','open','drive','','1905–1906',
  'Construction of this interurban depot began in 1905 for William B. Strang Jr.\'s Missouri and Kansas Interurban Railway, known as the Strang Line. Clio calls it the first commercial building in what became Overland Park; the first interurban car arrived in March 1906. Later it was enlarged and remodeled with the old walls covered. The Overland Park Historical Society bought it and opened some of the walls again.',
  'The society pulled back later walls to show the 1906 stone walls, original wainscoting and lap siding. It plans a museum with a trolley car, exhibits and an archive. The Society\'s visit page describes a museum in downtown called Discover O.P., with changing exhibits on the area from Native Americans through Strang and the post-war suburbs.',
  'The first building of a suburb, with its 1906 stone showing again.',
  'Clio gives the depot site as 8001 Santa Fe Drive. The society\'s visit page does not give a street address, so that Discover O.P. is this building is likely but not confirmed from the page itself. Free parking on site; free street parking in the downtown. Hours below are those the society\'s page gives for Discover O.P.; it also opens for downtown events.',
  [['Clio: Strang Depot',CLIO%18],['Overland Park Historical Society: plan your visit','https://ophistorical.org/hours-and-locations.html']],
  hours='Wednesday to Friday noon to 5 p.m.; Saturday 9 a.m. to 2 p.m. (Discover O.P., per the society)',brick='?',conf='mixed'),
N('strang-line-car-barn-overland-park-ks','Strang Line Car Barn','Overland Park, Kansas','ks','rail','standing',38.98595,-94.67162,'site','open','drive','','1906–1940',
  'Built in 1906 at the end of the Strang Line to store and repair the interurban cars and to power the track. A fire in 1925 destroyed much of it and it was rebuilt. The line closed in 1940 and the rails were taken up. Clio says the car barn, the carriage house and a small artificial lake nearby are all that remain of Strang\'s original works.',
  'The limestone exterior is original, and a plaque tells the history of the line. A furniture store uses the building. Inside is a shop; what survives of the barn\'s inner structure was not checked.',
  'The one building left from the trolley line that built a suburb.',
  'Clio gives the address as 7400 W. 79th Street, Overland Park, a working furniture store. Walk in during shop hours or look from the sidewalk; shop hours were not read.',
  [['Clio: Strang Line Car Barn',CLIO%20],W('Missouri and Kansas Interurban Railway')],
  hours='?',brick='no',conf='mixed'),
N('aztec-theater-shawnee-ks','Aztec Theater (Mission Theater)','Shawnee, Kansas','ks','civic','standing',39.02265,-94.71534,'exact','open','drive','','1927',
  'The Mission Theater opened on September 5, 1927 with 500 seats, designed by the Kansas City firm Boller Brothers in Spanish Mission style with Art Deco touches. Dickinson Theaters renamed it the Aztec in the 1940s, and it closed in the 1970s. After decades as bank storage it was bought in 2017, repaired from July 2019 with a $250,000 city grant, and reopened in 2020 as a music venue.',
  'The restored 1927 auditorium and lobby, the original ticket booth and door (salvaged from a dumpster) and a 1949 popcorn machine. It mostly hosts live music, with one classic film a month from May to October. Interior open for shows.',
  'A 1927 movie palace brought back after 46 years dark.',
  'On Johnson Drive in downtown Shawnee (11119 Johnson Drive per Clio). A private venue, open for events and shows, so there are no regular hours; see its schedule.',
  [['Clio: The Aztec Theater',CLIO%25]],
  hours='Shows and events only; one classic film a month May to October (no regular hours read)',brick='?'),
N('campbell-home-merriam-ks','Campbell Home','Merriam, Kansas','ks','landmark','standing',39.02187,-94.69588,'exact','view','drive','','1860–1893',
  'David Gee Campbell built the house in Shawnee in 1860 and moved it to what is now Merriam in 1864, after raiders burned Shawnee. He gave land to the railroad, and the town took the name Merriam from the railroad\'s secretary. The house burned in 1890; it was rebuilt in 1893 in the same design on the 1864 foundation, which had survived. Clio calls it the oldest home in the town.',
  'A house on an 18-inch stone foundation and basement made of stone hauled from the Turkey Creek basin, with a historical marker. Clio says the present house is the 1893 rebuild, so the visible structure dates from then.',
  'The first house of a railroad town, rebuilt on its own foundation.',
  'At 9503 Johnson Drive, Merriam. Who owns it and whether it opens were not checked: look from the street.',
  [['Clio: Campbell Home',CLIO%23],['HMdb: Campbell Home','https://www.hmdb.org/m.asp?m=51344']],
  brick='?',conf='mixed'),
N('strengthen-arm-liberty-overland-park-ks','Strengthen the Arm of Liberty statue','Overland Park, Kansas','ks','curio','standing',39.02159,-94.67336,'site','view','drive','','1950s',
  'A replica of the Statue of Liberty placed by the Boy Scouts of America in its 1950s Strengthen the Arm of Liberty campaign, the theme of the Scouts\' fortieth anniversary in 1950. About 200 such replicas went up across the country. This one is on the west side of Shawnee Mission North High School.',
  'A statue of Liberty on a base, set on the school grounds. The exact year it was put up was not found.',
  'One of about 200 Scout-made Statues of Liberty.',
  'On school grounds at Shawnee Mission North High School. A school is not open to wander at will: look from the public side and ask the school. Who owns the statue was not checked.',
  [W('Strengthen the Arm of Liberty Monument (Overland Park, Kansas)')],
  brick='?',conf='mixed'),
N('spring-hill-historic-district-ks','Spring Hill Historic District (South Main Street)','Spring Hill, Kansas','ks','town','standing',38.74391,-94.81718,'site','public','drive','','1900s',
  'The 100 block of South Main Street is a Kansas State Register district (listed December 9, 2000). The city says the Kansas Historical Society designated it as Johnson County\'s first historic district. The city asks owners to keep the buildings\' historic look and sends exterior work to the Society for review.',
  'A block of old commercial buildings along South Main, with downtown murals nearby (the city publishes a mural guide). Which buildings are the oldest was not read: the city points to the Spring Hill Historical Society and the Johnson County Library for each building\'s history.',
  'Johnson County\'s first designated historic district, one block long.',
  'City streets in downtown Spring Hill; look from the sidewalk. Shops and offices inside keep their own hours. The city\'s page gives no opening hours for the district.',
  [['City of Spring Hill: Historic District','https://springhillks.gov/169/Historic-District'],['City of Spring Hill: history','https://springhillks.gov/253/Spring-Hill-History'],['Kansas Historical Society register summary',KSNR%4]],
  brick='?',conf='mixed'),
]
PIN_NOTES={
'strang-carriage-house-overland-park-ks':'ArcGIS address lookup for 8045 Santa Fe Drive, near the Wikipedia point. On the aerial the pin falls in a small park beside the road and no single building can be picked out, so it marks the spot within about 60 m (Commons photographs of the building are taken 26 to 60 m from it).',
'strang-depot-overland-park-ks':'ArcGIS address lookup for 8001 Santa Fe Drive, the address Clio gives for the depot site.',
'strang-line-car-barn-overland-park-ks':'ArcGIS address lookup for 7400 W. 79th Street, the address Clio gives.',
'aztec-theater-shawnee-ks':'ArcGIS address lookup for 11119 Johnson Drive, the address Clio gives; the pin is on a building in the downtown block on the aerial.',
'campbell-home-merriam-ks':'ArcGIS address lookup for 9503 Johnson Drive, the address Clio gives.',
'strengthen-arm-liberty-overland-park-ks':'Wikipedia coordinates; the article places it on the west side of Shawnee Mission North High School.',
'spring-hill-historic-district-ks':'ArcGIS address lookup for 100 S. Main Street, the start of the 100 block named by the city; the pin is on the first building of the row on the aerial. The streets are the city\'s, which is why access is public.',
}
