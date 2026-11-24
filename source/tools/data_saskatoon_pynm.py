# November 24, 2026: Saskatoon, Saskatchewan, from a video's list of names (a stranger's tip, never a source). Every fact
# below comes from pages opened for this batch: the City of Saskatoon's heritage register (one page per place, and its
# printed register), Wikipedia read as raw text, the churches' own pages for service times, the Province of
# Saskatchewan's 2025 news release on the new city-centre school, and Ardent Mills' list of its mills. Pins are the
# ArcGIS geocoder's address points and OpenStreetMap points, each looked at on the aerial.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
def YXE(t,s): return ['City of Saskatoon heritage register: '+t,'https://saskatoon.ca/heritage-register/'+s]

BATCH={'key':'saskatoon_pynm','label':'Saskatoon: downtown, Riversdale and the mills','added':'2026-11-24 15:43'}

PLACES=[
N('king-george-hotel-saskatoon','King George Hotel','Saskatoon','sk','hotel','standing',52.13018,-106.66374,'exact','view','walk','hotels','1911–1912',
  'A five-storey brick hotel paid for by investors in London, England, designed by Brown and Vallance and opened in January 1912 as a first-class hotel for the booming town. It lost its standing when the Bessborough opened in the mid-1930s and carried on serving travellers, farmers and country merchants. A 1914 addition was made, the front was covered in green and white ceramic tile in the 1960s, and fires damaged it in 1979 and 2004.',
  'A five-storey corner building with a corner tower. The 1960s tiling took away some of the terra cotta knights and gargoyles of the first front, and the 2007 restoration could not bring the brick front back to its original state (City register). Shops on the ground floor, offices on the second, flats above; interior not checked.',
  'The 1912 luxury hotel that the Bessborough eclipsed.',
  'Privately owned, 157 2nd Avenue North, downtown. See it from the street; the ground floor holds shops. Listed on the City of Saskatoon heritage register. Downtown street parking; not checked.',
  [YXE('King George Hotel','king-george-hotel')],brick='?'),
N('albany-hotel-saskatoon','Albany Hotel (first the Iroquois Hotel)','Saskatoon','sk','hotel','standing',52.12641,-106.67212,'exact','view','walk','hotels','1906',
  'Built in 1906 by the Graham brothers as the Iroquois Hotel, one of the first large buildings west of the railway lines, with a two-tier balcony across its front over 20th Street. In 1912 the balconies came off and the building was enlarged, much altered and renamed the Albany; by 1914 it had 42 rooms with hot and cold water, steam heat, electric light and telephones. Since December 2000 it has been housing.',
  'A three-storey brick hotel on a stone basement, flat-roofed and symmetrical, on the corner of 20th Street West in Riversdale (City register). Interior not checked; it is housing and not open to visitors.',
  '',
  'Privately run housing, 265 Avenue B South at 20th Street West. See it from the street only. Listed on the City of Saskatoon heritage register.',
  [YXE('Albany Hotel','albany-hotel')],brick='?'),
N('robin-hood-mill-saskatoon','Robin Hood Mill (Saskatoon Mill and Mix Facility)','Saskatoon','sk','industry','standing',52.14275,-106.66331,'site','view','drive','','1927–1929',
  'Robin Hood bought the existing Factoria Mill here in 1926, began building in 1927, put in machinery in 1928 and added warehouses in 1929; the old Factoria section was pulled down in 1938. About $7 million went into new equipment in 1999, when it had some 140 workers. Ardent Mills lists it today as its Saskatoon Mill and Mix Facility, so it is still a working mill.',
  'The big mill and its concrete elevator tower, with the Robin Hood sign on top, a landmark of the Central Industrial neighbourhood (City register). A working plant: nothing inside is open to the public.',
  '',
  'A working flour mill run by Ardent Mills, 95 33rd Street East. Private industrial ground: see it from 33rd Street or the streets round it, and keep clear of the rail spurs and truck gates. Listed on the City of Saskatoon heritage register.',
  [YXE('Robin Hood Mill','robin-hood-mill'),L('Ardent Mills: its locations, Saskatoon Mill and Mix Facility','https://ardentmills.com/our-facilities/saskatchewan-canada/saskatoon-mill-and-mix-facility')],brick='?'),
N('great-western-brewery-saskatoon','Great Western Brewing Company (built as the Hub City brewery)','Saskatoon','sk','industry','standing',52.1365,-106.66165,'site','view','walk','','1927',
  'Designed by David Webster and built in 1927 for the Hub City Brewing Company at a cost of $500,000; it became the Western Canada Brewing Company in 1930 and Drewry\'s in 1932, and a bottling plant was added in 1948. Molson closed it in 1989, and sixteen former workers bought it and reopened it as Great Western, then the only employee-owned brewery in western Canada. The City register calls it the one large brewery left in the province, used as a brewery for its whole life.',
  'A large brewery building with arched windows and the "Great Western" mural along its 2nd Avenue North side (City register). Whether the company runs tours or a shop was not checked, because its own page could not be opened when this was written.',
  '',
  'A working brewery, privately owned, 510 1st Avenue North in City Park. See it from 1st and 2nd Avenues North. Listed on the City of Saskatoon heritage register.',
  [YXE('Great Western Brewing Company','great-western-brewing-company')],brick='?'),
N('19th-street-subway-saskatoon','19th Street Subway','Saskatoon','sk','landmark','traces',52.1243,-106.6688,'area','public','walk','','1930–1931',
  'Railway tracks once cut the west side of Saskatoon off from downtown, and crossing them was dangerous. A first underpass on 19th Street, begun in 1911, was narrow and hard to get in and out of; this one was dug by hand from December 1930 over six and a half months as relief work for the unemployed. It is kept on the City register as a reminder of the early underpasses.',
  'What is left is the roadway itself, under the shadow of two freeway approaches: it no longer has its centre pier, roof or retaining walls (City register). Do not expect a tunnel.',
  'An underpass dug by hand for relief work in the Depression.',
  'A public street, the 100 block of 19th Street East, owned by the City of Saskatoon. Walk it on the sidewalk; it carries traffic.',
  [YXE('19th Street Subway','19th-street-subway')],brick='?'),
N('king-george-school-saskatoon','King George School','Saskatoon','sk','civic','standing',52.11915,-106.68668,'exact','view','walk','','1912–1913',
  'A fourteen-room "castle school" in the Collegiate Gothic style, designed by the school board\'s architect David Webster and built in 1912–1913, on ground where a two-room frame school had been moved in 1911 and renamed for the King\'s coronation. Gordie Howe went to school here. The province announced in 2025 that a new school for King George, Pleasant Hill and Riversdale pupils was being built; the school\'s own page says the new one opens in the 2027–28 school year, and what then becomes of this building was not found.',
  'A big brick school with a central tower, castle-like turrets and Masonic symbols on the front, of Estevan brick with stone trim (City register; Wikipedia). Interior not checked; a working school.',
  '',
  'Saskatoon Public Schools, 721 Avenue K South. A working school: look from Avenue K and the streets round it, and not during school drop-off. Heritage holding bylaw (60-day delay on demolition).',
  [YXE('King George School','king-george-school'),W('King George, Saskatoon'),L('King George School: our school','https://www.spsd.sk.ca/kinggeorge/our-school'),L('Government of Saskatchewan, June 23, 2025: construction to begin on the city centre school','https://www.saskatchewan.ca/government/news-and-media/2025/june/23/construction-to-begin-on-saskatoon-city-centre-school-project')],brick='?'),
N('royal-bank-saskatoon','Royal Bank building','Saskatoon','sk','civic','standing',52.12656,-106.66543,'exact','view','walk','','1911–1913',
  'Built for the Royal Bank of Canada from 1911 and occupied in October 1913, designed by Kenneth Guscotte Rea; the bank kept the main floor until 1975. The City register calls it the only bank left in Saskatoon in the Classical and Renaissance manner from the first boom. It was renovated in the 1970s and has had other tenants since.',
  'A three-storey cut-stone front with full-height Ionic columns, a heavy cornice with dentils, a balustrade on the roofline and "Royal Bank of Canada" carved in stone over the door (City register). Interior not checked.',
  '',
  'Privately owned, 243 2nd Avenue South, downtown. See it from the street. Heritage holding bylaw (60-day delay on demolition).',
  [YXE('Royal Bank','royal-bank')],brick='?'),
N('knox-united-church-saskatoon','Knox United Church','Saskatoon','sk','worship','standing',52.13024,-106.65446,'exact','open','walk','','1912–1914',
  'Built in 1912–1914 by Saskatoon\'s founding Presbyterians to designs by Brown and Vallance of Montreal, in the Collegiate Gothic style on a cross-shaped plan; it joined the United Church of Canada in 1925. Its 1,200 seats and good sound have made it a concert hall as well as a church. Apart from an elevator added on the north side it has hardly changed.',
  'Dark red brick with stepped gables, buttresses and arched doors. Inside: four sets of stained glass, among them the "Burning Bush" window, a high oak chancel, balconies and open rafters, the pulpit from the 1900 Knox Church, and the 1914 Casavant organ (City register). Open at Sunday worship.',
  '',
  'An active United Church congregation, 838 Spadina Crescent East on the riverbank. Visitors are welcome at Sunday worship (the church\'s own page). Municipal Heritage Property since 2003 (outside only).',
  [YXE('Knox United Church','knox-united-church'),W('Knox United Church (Saskatoon)'),L('Knox United Church','https://knoxunitedchurch.ca')],
  conf=None,brick='yes',hours='Sunday worship 10:30 a.m.'),
N('st-johns-cathedral-saskatoon','Cathedral of St. John the Evangelist (St. John\'s Anglican Cathedral)','Saskatoon','sk','worship','standing',52.12984,-106.65535,'exact','open','walk','','1912–1917',
  'The Duke of Connaught laid the cornerstone in 1912, but the war and the collapse of the land boom delayed the opening until 1917; it became the cathedral of the new Anglican Diocese of Saskatoon in 1932. Designed by Thompson, Daniel and Colthurst after the Manchester architect J.S. Crowther\'s work, it is built of Alberta Redcliff brick, British Columbia timber, Saskatchewan fieldstone and Tyndall stone, with Doulton terra cotta and Carrara ware. Its spire is among the tallest of any church in western Canada.',
  'A brick cross-shaped church with a conical tower, gargoyles and fruit-and-vine terra cotta round the doors. Inside, little altered: a vaulted ceiling, stained glass over the altar, a white Carrara-ware rood screen, inscribed pillars, and the 1907 tubular chimes from the first St. John\'s; the steeple clock was added in 2003 (City register).',
  '',
  'An active Anglican cathedral, 816 Spadina Crescent East on the riverbank. Open at its services (the cathedral\'s own page). Municipal Heritage Property since 2004 (outside only).',
  [YXE('St. John\'s Anglican Cathedral','st-johns-anglican-cathedral'),W('Cathedral of St. John the Evangelist (Saskatoon)'),L('St. John\'s Cathedral Saskatoon','https://stjohnscathedralsaskatoon.ca/')],
  brick='?',hours='Sunday 8 and 10:30 a.m.; Wednesday 12:10 p.m. in the Lady Chapel'),
N('third-avenue-united-church-saskatoon','Third Avenue United Church (St. Vincent of Lerins Orthodox Church)','Saskatoon','sk','worship','standing',52.13186,-106.65984,'exact','view','walk','','1911',
  'Built in 1911 by the Westside Methodist congregation at 24th Street and 3rd Avenue, in the English Gothic style to designs by John N. Semmens, with seats for about 1,600. Besides a church it was the town\'s great hall: political meetings of thousands in the 1920s (one led to the Wheat Pool), live radio organ recitals and university convocations were held here. The City register gives its other name as St. Vincent of Lerins Orthodox Church.',
  'A stone church with two towers of unequal height, lancet windows and doors: a native limestone base and buff Tyndall stone walls with blue-grey trim. Inside: oak hammer-beam rafters, huge Gothic stained-glass windows on three sides and a Casavant organ (City register); the protection covers the outside, the rafters and the organ. Interior not checked by a visit.',
  '',
  'A church, 304 3rd Avenue North, downtown; the City register gives its other name as St. Vincent of Lerins Orthodox Church. No page of the congregation\'s own with service times was found, so see it from the street. Municipal Heritage Property since 2017.',
  [YXE('Third Avenue United Church','third-avenue-united-church')],brick='no',hours='?'),
]

PIN_NOTES={
 'king-george-hotel-saskatoon':'The geocoder\'s address point for 157 2nd Avenue North, on the building on the aerial.',
 'albany-hotel-saskatoon':'The geocoder\'s address point for 265 Avenue B South, on the building on the aerial.',
 'robin-hood-mill-saskatoon':'The geocoder\'s address point for 95 33rd Street East fell on a bare lot north of the plant; moved about 130 m south-west onto the tall mill buildings, which cast a long shadow on the aerial.',
 'great-western-brewery-saskatoon':'The geocoder\'s address point for 510 1st Avenue North; the pin marks the brewery site.',
 '19th-street-subway-saskatoon':'Placed on 19th Street East where it passes under the freeway approaches; the register gives only the block, so the pin marks the area.',
 'king-george-school-saskatoon':'OpenStreetMap\'s point for King George Community School, 721 Avenue K South.',
 'royal-bank-saskatoon':'The geocoder\'s address point for 243 2nd Avenue South.',
 'knox-united-church-saskatoon':'OpenStreetMap\'s point for Knox United Church.',
 'st-johns-cathedral-saskatoon':'The geocoder\'s address point for 816 Spadina Crescent East, moved about 20 m east onto the cross-shaped church seen on the aerial.',
 'third-avenue-united-church-saskatoon':'OpenStreetMap\'s point for St. Vincent of Lerins Orthodox Church, 304 3rd Avenue North.',
}
