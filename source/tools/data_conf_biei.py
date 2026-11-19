# November 18, 2026: Watervliet, Green Island, the Cohoes Juncta and the Watervliet Shakers. Drawn at random by
# tools/choose.py --state ny (region conf). Waterford and downtown Cohoes were worked earlier the same day
# (data_conf_simf.py), so this batch goes south: the City of Watervliet, Green Island and the old Juncta, with the
# two Colonie places that carry the old Town of Watervliet's name (the Shaker settlement and the 1817 Dutch church at
# Latham) filed under albco like the Pruyn House.
# Sources were opened in this session: Wikipedia as raw text (tools/wiki_raw.py); the Arsenal's National Historic
# Landmark form (66000503), the Shaker Heritage Society's visit and buildings pages, NPS, HMdb markers, the Spindle
# City Historic Society's canal brochure, Industrial Scenery (blog, November 2025), St. Nicholas parish history and
# bulletin, The Evangelist, army.mil (archived copies) and Clio, through tools/page.py.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'conf_biei','label':'Watervliet, Green Island and the Watervliet Shakers','added':'2026-11-18 23:41'}
NHL=L('National Historic Landmark nomination: Watervliet Arsenal (66000503)','https://npgallery.nps.gov/NRHP/GetAsset/NHLS/66000503_text')
SHV=L('Shaker Heritage Society: Plan your trip','https://home.shakerheritage.org/visit/')
SHB=L('Shaker Heritage Society: surviving structures','https://virtual.shakerheritage.org/existing.html')
PLACES=[
N('watervliet-shaker-church-family','Watervliet Shakers: 1848 Meeting House, Church Family and Ann Lee\'s grave','Colonie','albco','town','standing',42.74106,-73.81111,'exact','public','walk','','1776–1920s',
  'The first Shaker settlement in America was founded here in 1776, in what was then the Town of Watervliet; Mother Ann Lee, the Shakers\' founder, is buried in its cemetery. At its height the community had about 350 members in four "families". The last members left in the 1920s and Albany County bought the Church Family\'s land; Albany International Airport was later built over the Shakers\' herb fields. The site is a National Register district (1973).',
  'The 1848 Meeting House, the third at Watervliet, which the Shaker Heritage Society calls the most intact of the large Shaker meeting houses in the country; it holds the society\'s museum and shop. Around it: nine Shaker buildings of the Church Family in all (among them a dwelling with an 1822 date stone left by its master masons, and a workshop the county remodelled in the Colonial Revival style about 1930), the ruins of the grist mill, the herb garden, orchard and barnyard, the Shaker Cemetery with Ann Lee\'s grave, and trails round the Ann Lee Pond preserve. Whether the Meeting House keeps its original benches and woodwork was not checked.',
  'America\'s first Shaker village, next to the airport runway.',
  'Shaker Heritage Society, 25 Meeting House Road, off Heritage Lane by Albany International Airport. Its own page (read November 2026): April 1 to October 8, Tuesday to Saturday 10 a.m. to 4 p.m.; October 13 to December 18, Tuesday to Sunday 10 a.m. to 4 p.m.; closed Mondays, July 4 and Thanksgiving. The Church Family grounds, cemetery and preserve trails are open to the public; fees were not checked. Parking at the Meeting House Road lot. The land under the Heritage Lane lot is mapped as the Ann Lee Pond Nature and Historic Preserve.',
  [SHV,SHB,W('Watervliet Shaker Historic District')],
  th=[42.74106,-73.81174],thn='Meeting House Road lot',brick='?'),
N('reformed-dutch-church-latham','Reformed Dutch Church of Rensselaer in Watervliet (1817)','Latham','albco','worship','standing',42.74805,-73.75896,'exact','view','drive','','1817',
  'A country church of 1817 in a plain Greek Revival style, built for the Dutch Reformed congregation of the old Town of Watervliet. It was a church until 1886 and since then has been a feed store, a public hall, a chapel, an architect\'s office and a theater. It was listed on the National Register in 1985.',
  'Pedimented gable front with corner pilasters, a deep channelled cornice and a square cupola with a single bell on the roof. OpenStreetMap names the building at this address (210 Old Loudon Road) "Chapel of Praise", so it may be a church again; its present use and the interior were not checked.',
  '',
  'Privately owned building on Old Loudon Road in Latham; see it from the road. Whether it is open to visitors was not checked.',
  [W('Reformed Dutch Church of Rensselaer in Watervliet')],
  conf='mixed',brick='?'),
N('watervliet-arsenal','Watervliet Arsenal from Broadway','Watervliet','conf','fort','standing',42.71844,-73.70268,'area','view','walk','forts','1813–',
  'Founded on July 14, 1813, for the War of 1812, the Watervliet Arsenal is the oldest arsenal in continuous use in the United States and still makes cannon, mortar and tank-gun barrels. It grew through the 1820s to 1840s into the Army\'s main maker of artillery carriages; most buildings of 1824 to 1847 were of stone, and from 1829 the arsenal walled its land and both banks of the Erie Canal. The Iron Building, a prefabricated cast-iron storehouse of 1859 by the Architectural Iron Works of New York, held the arsenal museum until the Army closed it in October 2013. National Historic Landmark since 1966.',
  'From Broadway only: the Landmark form says the Broadway side is closed by a wrought-iron picket fence, with the officers\' quarters and offices in the north-east part of the post behind it; the north and south sides have rubble sandstone walls of the 1830s with stone piers, and a long stretch of the arsenal wall follows the line of the old Erie Canal. The site of the first arsenal of 1813–24, in the north-east corner on Broadway, is now playing fields. The Iron Building is inside the post and is not open; whether it can be seen from outside was not checked. Red brick: not checked.',
  'The Army\'s oldest working arsenal, and the cast-iron museum nobody may enter.',
  'An active U.S. Army installation behind a fence: no public access, and the museum is closed (Clio; army.mil, archived copy of June 2026). Look from the public sidewalk of Broadway (NY 32). The pin is the Broadway frontage, not one building.',
  [NHL,W('Watervliet Arsenal'),W('Iron Building (Watervliet Arsenal)'),L('Clio: Watervliet Arsenal Museum (closed)','https://www.theclio.com/entry/31331'),L('army.mil: History departs historic arsenal (2013; archived copy)','https://www.army.mil/article/117177/History_departs_historic_arsenal/')],
  brick='?'),
N('st-nicholas-ukrainian-watervliet','St. Nicholas Ukrainian Catholic Church','Watervliet','conf','worship','standing',42.73455,-73.70305,'exact','public','walk','','1906–1908',
  'Ukrainian immigrants in South Troy, West Troy (Watervliet) and Cohoes first worshipped in a frame former Methodist church in Troy from 1897. In 1906 the parish bought a lot at Fourth Avenue and 24th Street in Watervliet, chosen as central to all three; the cornerstone was laid on May 30, 1907, and after the Panic of 1907 ran the money out, a loan through the Roman Catholic bishop of Albany let the church be finished in early 1908. Bernhardt Noack designed it. National Register.',
  'Onion-domed towers and round-arched windows on a front of buff brick in common bond with limestone trim. Inside, the walls were replastered and new icons painted in the late 1940s; the slate roof was replaced in copper, and in the 1950s and 1960s the central dome was taken off. It is still a parish church: the November 2025 bulletin lists Sunday Divine Liturgies at 9 and 11 a.m. with a rosary at 10:30, and weekday liturgies at 9 a.m.',
  'Onion domes two blocks from the old Erie Canal.',
  'Active parish church at 2410 Fourth Avenue (parish office 518-273-6752). Visitors can go in for the liturgies; other times not checked. Street parking.',
  [W('St. Nicholas Ukrainian Catholic Church'),L('St. Nicholas parish history (cerkva.com)','https://www.cerkva.com/wp-content/uploads/2017/09/history.pdf'),L('St. Nicholas parish bulletin, November 16–23, 2025','https://www.cerkva.com/wp-content/uploads/2025/11/Nov-16_-23-2025.pdf')],
  brick='no'),
N('ohio-street-methodist-watervliet','Ohio Street Methodist Episcopal Church (St. Ann Maronite)','Watervliet','conf','worship','standing',42.73107,-73.70277,'exact','view','walk','','c. 1850',
  'A brick Methodist church built about 1850 and remodelled about 1895, with a brick parish house of about 1880; it is also known as the Third Avenue Methodist Church. Listed on the National Register in 2005. In 2013 the Maronite Catholic parish of St. Ann, about a hundred years old and until then on Fourth Street in Troy, took over the vacant church (Wikipedia says from the City of Watervliet) and renamed it St. Ann Maronite Catholic Church.',
  'Two brick buildings on stone foundations, the church and its parish house, at 1921 Third Avenue. The Evangelist reported the Maronites planned classrooms, a gathering space, offices and a rectory in the Watervliet buildings. The colour of the brick, the interior and service times were not checked.',
  '',
  'Church of the St. Ann Maronite parish; see it from Third Avenue. Whether and when visitors may go in was not checked. Street parking.',
  [W('Ohio Street Methodist Episcopal Church Complex'),L('The Evangelist: Maronites prepping shrine and new church','https://evangelist.org/news/2018/apr/06/maronites-prepping-shrine-and-new-church')],
  conf='mixed',brick='?'),
N('meneely-bell-foundry-site','Meneely Bell Foundry site','Watervliet','conf','industry','marker',42.72652,-73.70019,'site','public','walk','','1826–1950s',
  'Andrew Meneely, a Scot who had worked in Julius Hanks\'s foundry in Troy, started a bell foundry in West Troy (now Watervliet) that his sons Edward and George ran after his death in 1851, and the family went on casting for about a hundred years; more than 65,000 bells carried the Meneely name. The markers disagree on the dates: one gives 1826 to 1951, the other says the plant opened in 1829, heads its panel "1826 – 1950" and says the foundry closed in 1954.',
  'Nothing of the foundry stands: the Leo O\'Brien Municipal Center, with the Watervliet Public Library and senior center (1501 Broadway), is on its site. Two markers stand on Broadway in front of it, and a "City of the Bells" marker on Third Avenue near Sixth Street. Meneely bells hang in churches across the region; HMdb lists several, among them the United Methodist Church bell in Watervliet.',
  'The city of bells, and the library on the foundry floor.',
  'Public sidewalk on Broadway (NY 32) in front of the municipal center; parking there was not checked.',
  [L('HMdb: Meneely Bell Foundry','https://www.hmdb.org/m.asp?m=182363'),L('HMdb: Meneely Foundry','https://www.hmdb.org/m.asp?m=40322'),L('HMdb: Watervliet – City of the Bells','https://www.hmdb.org/m.asp?m=303576')],
  conf='mixed',brick='?'),
N('tilley-ladders-watervliet','John S. Tilley Ladders Company factory','Watervliet','conf','industry','standing',42.70825,-73.70871,'exact','view','walk','','1916',
  'John S. Tilley founded his ladder company in 1855, and it became the oldest ladder maker in the country, turning out ladders and scaffolds for houses, builders and fruit picking. Its factory in the Port Schuyler part of Watervliet was built in 1916 and added to again and again until it covered much of a city block. It was listed on the National Register and has since been made into apartments.',
  'The 1916 factory and its additions on Second Street, now apartments. The materials and what is left of the factory inside were not checked.',
  '',
  'Private apartment building at 122 Second Street; look from the street.',
  [L('National Park Service: John S. Tilley Ladders Company','https://www.nps.gov/places/john-s-tilley-ladders-company.htm')],
  brick='?'),
N('federal-dam-troy-lock','Federal Dam and the Troy Lock','Green Island','conf','canal','standing',42.75143,-73.68732,'site','view','walk','canal','1916',
  'The U.S. Army Corps of Engineers built this dam across the Hudson between Green Island and Troy, with a single lock at its east end opened in 1916 (one Army photo caption says 1915); it marks the head of the tide, the upper end of the Hudson estuary, at river mile 153. The lock lifts boats about 14 feet and is the first that boats meet going up from New York toward the Erie and Champlain canals, though it is not a state canal lock. It is the second dam at Green Island; the first, the State Dam of 1823, had powered the island\'s early mills.',
  'The dam and its spillway across the river and, at the Troy end, the lock chamber, still run by the Corps. A marker on the Empire State Trail on Green Island, just south of the bridge to Van Schaick Island, faces the dam a few hundred yards away. Red brick: not checked.',
  'Where the tide stops.',
  'Federal works of the U.S. Army Corps of Engineers; no access to the dam or the lock walls was found. Look from the Empire State Trail on Green Island (the HMdb marker is at 42.76017, -73.68769) or from the Troy bank. The pin is the dam crest.',
  [W('Federal Dam (Troy)'),L('army.mil: Hudson River\'s Troy Lock & Dam, 100 years (archived copy, December 2016)','https://www.army.mil/article/172897'),L('HMdb: Water Fire Iron / .7 Sq. Mi. / Age of Rail (Green Island)','https://www.hmdb.org/m.asp?m=256004')],
  conf='mixed',brick='?'),
N('juncta-champlain-lock2-cohoes','The Juncta and Old Champlain Canal Lock 2','Cohoes','conf','canal','ruins',42.76365,-73.69898,'exact','view','drive','canal','1823–1915',
  'The Juncta, near Main and Saratoga Streets, was where the original Champlain Canal met the Erie, at the foot of the flight of locks round the Cohoes Falls; it opened in 1823, held the first settlement of Cohoes and its first post office, and grew into a busy trading place. The Champlain locks were numbered north from the junction (the later "New Juncta"). Lock 1 is now under a road; of Lock 2 the American Canal Society lists one wall visible.',
  'A state marker (2000, re-erected by the city in December 2007) on the east side of Saratoga Street (NY 32) just north of Spring Street. About 70 m to the north-east, between Saratoga Street and Route 787, the stone chamber of Lock 2: a November 2025 photo essay shows the west wall mostly intact with one gate recess at its lower end, two blocks pushed out of place, and the wall nearest the highway partly broken with its rubble piled in the chamber. A 2008 HMdb note says the lock was to be part of a planned interpretive park.',
  'Where the Erie met the Champlain, and one lock wall left.',
  'The marker is on the public roadside. Who owns the ground round Lock 2 was not checked, so treat the lock as view-only from Saratoga Street. Parking was not checked; the nearest mapped lot is on Alexander Street, 470 m south-west.',
  [L('HMdb: Juncta (state marker)','https://www.hmdb.org/m.asp?m=6161'),L('American Canal Society: Champlain Canal index sheet','https://americancanalsociety.org/wp-content/uploads/2019/08/Champlain-Canal2.pdf'),L('Industrial Scenery: Champlain Canal Lock 2 in Cohoes (November 2025)','https://industrialscenery.blogspot.com/2025/11/champlain-canal-lock-2-in-cohoes-ny.html'),L('Spindle City Historic Society: Erie Canal brochure (2023)','https://www.spindlecity.net/Brochures/Erie%20Canal%20brochure%202023.pdf')],
  conf='mixed',brick='no'),
N('cohoes-savings-bank','Cohoes Savings Bank building','Cohoes','conf','civic','standing',42.775,-73.70108,'site','view','walk','','1905, 1923, 1950',
  'The Cohoes Savings Institution was chartered in 1851 with the mill owner Egbert Egberts as its first president and opened its first building on Oneida Street in 1853. It bought the corner of Remsen and Seneca Streets in 1904 and finished a Beaux Arts bank there in 1905, adding to it on the next lot, 75 Remsen Street, after 1923. Renamed the Cohoes Savings Bank in 1922, it merged with the Mechanics Savings Bank of Cohoes in 1933.',
  'The 1905 Beaux Arts front and its 1923 addition. In 1950 the office of the Albany architect Marcus T. Reynolds remodelled the banking hall, with murals by David Cunningham Lithgow of Native American legends and the Cohoes Falls, Henry Hudson\'s voyage, the birth of Cohoes industry and the finding of the Cohoes Mastodon. Whether the murals survive was not checked. OpenStreetMap lists a jewelry shop at 75 Remsen Street; the present use of the banking hall was not checked.',
  'A banking hall painted with the mastodon.',
  'Privately owned; see it from Remsen Street. Whether the public can see the hall inside was not checked. Downtown street parking and the mapped lot on Remsen Street.',
  [L('Spindle City Historic Society: Historic Downtown Cohoes self-guided tour (2023)','https://www.spindlecity.net/Brochures/downtown%20sites%20brochure%202023.pdf')],
  conf='mixed',brick='?'),
]
PIN_NOTES={
 'cohoes-savings-bank':'OpenStreetMap address point for 75 Remsen Street (the tour\'s address); the 1905 corner building is at Remsen and Seneca Streets.',
 'watervliet-shaker-church-family':'OpenStreetMap building "Shaker Meeting House" (25 Meeting House Road); parking is the mapped lot on Meeting House Road.',
 'reformed-dutch-church-latham':'OpenStreetMap place of worship at 210 Old Loudon Road, the church\'s address in Wikipedia; Wikipedia\'s own point is 60 m east.',
 'watervliet-arsenal':'On Broadway (NY 32) in front of the post, between the two OpenStreetMap road points for Broadway; a wide leaf-off aerial shows the post\'s car parks and buildings just west. It marks where to look from, not one building.',
 'st-nicholas-ukrainian-watervliet':'OpenStreetMap address point for 2410 Fourth Avenue, the parish address in its bulletin.',
 'ohio-street-methodist-watervliet':'OpenStreetMap address point for 1921 Third Avenue; OpenStreetMap has St. Ann Maronite church at the same spot.',
 'meneely-bell-foundry-site':'HMdb position of the Meneely Foundry marker in front of the Watervliet Public Library (1501 Broadway).',
 'tilley-ladders-watervliet':'OpenStreetMap address point for 122 Second Street, the address on the NPS page.',
 'federal-dam-troy-lock':'Read off a wide leaf-off aerial onto the middle of the dam crest, where the spill shows; OpenStreetMap\'s dam point is 120 m west, on the Green Island bank.',
 'juncta-champlain-lock2-cohoes':'American Canal Society coordinate for Lock 2, which on a close leaf-off aerial falls on the narrow stone chamber between Saratoga Street and Route 787 (42°45\'49.14", 73°41\'56.34"); the Juncta marker (HMdb) is 70 m south-west at 42.76321, -73.69973.',
}
