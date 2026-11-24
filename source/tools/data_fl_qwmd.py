# November 24, 2026: a fourth scatter across Florida (Florida was the state with the fewest places that nobody held).
# Seven places the earlier Florida batches lack, from Palm Beach and Miami up to Pensacola: two Gilded Age estates, two
# pioneer and winter houses, a plantation house on a hill, a Spanish mission site and a brick fort.
# Sources read in this session: Wikipedia articles (tools/wiki_raw.py); the operators' own pages read with tools/page.py
# (Stranahan House, Bonnet House, Mission San Luis, the Tampa Bay History Center's Chinsegut Hill page, the National Park
# Service's Fort Barrancas Area page); for Whitehall and Vizcaya the operators' own sites would not open, so their hours come
# from what a web search quoted of them. Nothing was checked on the ground.
from data_b import N
from data_ma import W
BATCH={'key':'fl_qwmd','label':'Florida: seven more, Palm Beach to Pensacola','added':'2026-11-24 14:30'}

PLACES=[
N('whitehall-flagler-museum','Whitehall (Henry Morrison Flagler Museum)','Palm Beach','fl','landmark','standing',26.71402,-80.04345,'exact','open','drive','','1902',
  'A 75-room Gilded Age mansion that Henry Flagler, a founder of Standard Oil and the builder of Florida\'s east-coast railroad and hotels, built as a winter home for his third wife, Mary Lily Kenan. It was designed by Carrère and Hastings, who had done his Ponce de Leon Hotel in St. Augustine, and the couple moved in on February 6, 1902. Flagler died in 1913 after a fall on a marble stair in the house. Later owners added a 300-room, ten-storey hotel on its west side that wiped out Flagler\'s offices; a granddaughter saved the house from demolition in 1959, it opened as a museum in 1960, and the upper ten storeys of the hotel were taken down in 1963. It is a National Historic Landmark.',
  'A neoclassical Beaux Arts palace, open as a museum. Which rooms and furnishings survive from 1902 was not checked.',
  'A palace left standing after its hotel wing was cut away.',
  'Run as a museum by the Henry Morrison Flagler Museum, One Whitehall Way. Hours and the adult ticket price ($28) are from a web search result that quoted the museum\'s visitor page; the museum\'s own pages would not open when this was written, so check before going. Free parking in the museum lot during opening hours (same source).',
  [W('Whitehall (Henry M. Flagler House)'),['Flagler Museum','https://flaglermuseum.us']],
  hours='Tuesday to Saturday 10 a.m. to 5 p.m., Sunday noon to 5 p.m.; closed Mondays, Thanksgiving, Christmas and New Year\'s Day',brick='?'),

N('vizcaya-museum-gardens','Vizcaya Museum and Gardens','Miami (Coconut Grove)','fl','inst','standing',25.74432,-80.21046,'exact','open','drive','','1914–1923',
  'The winter villa of James Deering of the International Harvester fortune, on Biscayne Bay. It was built mostly between 1914 and 1922 at a cost of $15 million, with its Italian Renaissance gardens and a village of outbuildings finished in 1923. F. Burrall Hoffman was the architect, Paul Chalfin the design director and Diego Suarez the landscape architect. Deering used it as his winter home from 1916 until his death in 1925. Miami-Dade County now owns it and runs it as a museum. It is a National Historic Landmark.',
  'A Mediterranean Revival villa with Baroque touches, formal gardens and woodland, and a village compound of outbuildings. What the house holds inside was not checked.',
  'A $15 million Italian villa on Biscayne Bay.',
  'Owned by Miami-Dade County, 3251 South Miami Avenue. Hours are from a web search result that quoted the museum\'s site; vizcaya.org would not open when this was written. The same results gave the gardens a later closing time than the house; check before going. Parking was not checked.',
  [W('Vizcaya Museum and Gardens'),['Vizcaya Museum and Gardens','https://vizcaya.org/']],
  hours='Wednesday to Monday from 9:30 a.m., last admission 4:30 p.m.; closed Tuesdays',brick='?'),

N('stranahan-house-fort-lauderdale','Stranahan House','Fort Lauderdale','fl','landmark','standing',26.11814,-80.13801,'site','open','walk','','1901',
  'Built in 1901 by Frank Stranahan as a trading post on the New River, with a community hall upstairs, and turned into the home of Frank and Ivy Stranahan in 1906. It is the oldest surviving structure in Broward County. Ivy lived here until her death in 1971; the Fort Lauderdale Historical Society bought the house in 1975, and it has been a house museum since. It was listed on the National Register in 1973.',
  'A two-storey frame house on the river with bay windows added in 1906. Inside it was set up with a staircase and wiring in 1913. Which rooms are shown was not checked.',
  'The trading post where Fort Lauderdale began.',
  'Run as a museum by Stranahan House, 335 SE 6th Avenue. Its visit page says guided tours must be booked ahead and are not offered to walk-ins (adult ticket $13 on that page). Wikipedia says tours run at 1, 2 or 3 p.m. most Tuesdays to Fridays, which the page did not repeat. Parking not checked.',
  [W('Stranahan House'),['Stranahan House: tickets and admission','https://www.stranahanhouse.org/visit']],
  hours='Guided tours by advance booking only; no walk-in tours',brick='?'),

N('bonnet-house-fort-lauderdale','Bonnet House','Fort Lauderdale','fl','inst','standing',26.13514,-80.10447,'site','open','drive','','1919–1953',
  'The estate of the artist Frederic Clay Bartlett and his wives, on land the Chicago lawyer Hugh Taylor Birch gave Bartlett and his daughter Helen as a wedding present in 1919. Bartlett built a plantation-style house and an art studio and wintered here; after Helen died in 1925 he married Evelyn Fortune Lilly, who kept the house until her death in 1997 and left it to the public. It is listed on the National Register (1984) and has stood on the National Trust\'s most endangered list (2008).',
  'The main house, an art studio, a music studio and a guest house, on grounds with five habitats, from beach dunes to mangrove and maritime forest. House tours are timed; gardens-only tickets are sold.',
  'An artist\'s winter estate on the last wild stretch of Fort Lauderdale beach.',
  'Run by Bonnet House Museum & Gardens, 900 N. Birch Road. Hours from its visit page; a self-guided house ticket and a cheaper gardens-only ticket are sold, and guided tours run on set mornings. Parking not checked.',
  [W('Bonnet House'),['Bonnet House: hours and admission','https://www.bonnethouse.org/visit']],
  hours='Tuesday to Sunday from 11 a.m., last admission 4 p.m., grounds close 5 p.m.; closed Mondays, Thanksgiving, Christmas, New Year\'s Day',brick='?'),

N('mission-san-luis-tallahassee','Mission San Luis de Apalachee','Tallahassee','fl','town','traces',30.4487,-84.3201,'site','open','drive','','1656–1704',
  'A Spanish Franciscan mission built in 1656 at the Apalachee capital, two miles west of today\'s Capitol; by 1675 more than 1,400 Apalachee and several hundred Spaniards lived under its rule, and its Council House, which held 2,000 to 3,000 people, was the largest known historic Indian building in the Southeast. The Spanish evacuated and destroyed it in 1704 as Creek and South Carolina forces approached. It became a National Historic Landmark in 1966, the state bought the land in 1983, and since 1998 some buildings have been rebuilt from the archaeology.',
  'The reconstructed Apalachee Council House, Franciscan church, Spanish houses and fort, on the site of the original mission; the 1656 buildings themselves are gone. Run as a living-history museum.',
  'A Spanish mission and a 3,000-seat Apalachee council house, rebuilt on the spot.',
  'Mission San Luis, 2100 West Tennessee Street, a state-owned site. Adults $5, seniors $3, children 6 to 17 $2 (its visit page). Parking not checked.',
  [W('Mission San Luis de Apalache'),['Mission San Luis: visit','https://www.missionsanluis.org/visit']],
  hours='Tuesday to Sunday 10 a.m. to 4 p.m.; closed Mondays, New Year\'s Day, Easter, Thanksgiving, Christmas Eve and Christmas Day',brick='?'),

N('chinsegut-hill-manor','Chinsegut Hill Manor House','Brooksville','fl','landmark','standing',28.61899,-82.36467,'exact','open','drive','','1852–1854',
  'A plantation house on one of the highest hills in peninsular Florida (269 feet). Francis Ederington, who came from South Carolina in 1852 with his family and 30 enslaved people, built the present house in 1852–1854 around an earlier cabin; it is believed to be the oldest house left in Hernando County. From 1904 the Robins family, active in progressive causes, entertained Thomas Edison, Helen Keller and J.C. Penney here; in 1932 they gave the land to the federal government, and in 1954 the house and 114 acres passed to the University of Florida, which leased them to the University of South Florida from 1958 to 2008. It is on the National Register (2003).',
  'A three-storey frame house, little changed since the 1850s (Wikipedia), with a 114-acre preserve round it. The history centre\'s weekend tours go through the house; what survives inside was not checked.',
  'A hilltop plantation house that hosted Edison and Helen Keller.',
  'Hernando County, in partnership with the Tampa Bay History Center, which runs the tours (22495 Chinsegut Hill Road). The History Center\'s page gives the tour times; tour tickets are sold there. No lot was found on the map: park as signed at the entrance.',
  [W('Chinsegut Hill Manor House'),['Tampa Bay History Center: Chinsegut Hill','https://www.tampabayhistorycenter.org/chinsegut/']],
  hours='Weekend tours Saturday and Sunday at 10 a.m., noon and 2 p.m.',brick='?'),

N('fort-barrancas-pensacola','Fort Barrancas','Pensacola (Naval Air Station Pensacola)','fl','fort','standing',30.3478,-87.2976,'exact','open','drive','forts','1839–1844',
  'A hilltop fort over Pensacola Bay, where the Spanish built Fort San Carlos de Barrancas in the 1780s. From 1839 to 1844 the United States rebuilt and greatly enlarged the old Spanish fort in brick, joined to a water battery (the Spanish Water Battery, 1787) at the foot of the bluff. The army deactivated it in 1947; it became a National Historic Landmark in 1960 and passed to the National Park Service in 1971. The Advanced Redoubt, the last fort finished under the Third System, stands nearby.',
  'The brick fort with its Civil War history, the Spanish Water Battery below it, the Advanced Redoubt and two short trails; the visitor center has exhibits. Visitors must pass the security check at Naval Air Station Pensacola to reach it.',
  'A brick fort on an active naval air station.',
  'Gulf Islands National Seashore (National Park Service); enter the base by the West Gate, with photo identification (Wikipedia and a search result; the NPS page says to enter by the West Gate). No entrance fee (NPS page). The NPS page says the site closes for the 2026 season from November 30 and reopens in 2027. Park at the mapped fort lot on Taylor Road.',
  [W('Fort Barrancas'),['NPS: Fort Barrancas Area','https://www.nps.gov/guis/planyourvisit/fort-barrancas-area.htm']],
  th=[30.34928,-87.29835],thn='Fort Barrancas parking, Taylor Road',hours='Wednesday to Sunday 9 a.m. to 4 p.m., last entry 3:30; closed from November 30, 2026 until 2027',brick='yes'),
]

PIN_NOTES={
'whitehall-flagler-museum':'OpenStreetMap\'s outline of the museum; the geocoder\'s point was 400 m east on a golf course.',
'vizcaya-museum-gardens':'Wikipedia\'s point fell in the bay; moved onto the villa seen on the aerial.',
'stranahan-house-fort-lauderdale':'Moved onto the small house on the river bank seen on the aerial; Wikipedia\'s point agrees.',
'bonnet-house-fort-lauderdale':'ArcGIS geocoder\'s point for the museum, checked on the aerial; the pin marks the estate.',
'mission-san-luis-tallahassee':'ArcGIS geocoder\'s point for the mission, checked on the aerial; the pin marks the site.',
'chinsegut-hill-manor':'Wikipedia\'s point fell on grass; moved onto the manor seen on the aerial.',
'fort-barrancas-pensacola':'ArcGIS geocoder\'s point for the fort; the lot is the mapped Fort Barrancas parking.',
}
