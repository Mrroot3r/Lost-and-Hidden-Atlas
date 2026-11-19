# November 19, 2026: northern Saratoga County (Moreau, Northumberland, Corinth, Hadley) and the gaps left in downtown
# Saratoga Springs, drawn at random by tools/choose.py (region sar). The Atlas had nothing in South Glens Falls,
# Gansevoort or the village of Corinth, and in Saratoga Springs it had the spa, the park and the lost hotels but not the
# standing churches, the post office or the track. This batch adds the Parks-Bentley Place museum, the Gansevoort
# Mansion, International Paper's 1905 office at Corinth, the Spier Falls dam, the Lynwood church at Hadley, and in
# Saratoga Springs the Batcheller Mansion, Universal Preservation Hall, the post office and city hall corner, High Rock
# Park, Franklin Square and the race course.
# Sources were opened in this session: Wikipedia as raw text (tools/wiki_raw.py); HMdb marker pages (tools/page.py);
# the Register form for the International Paper building from NPGallery; the Village of South Glens Falls, the Town of
# Moreau, Hudson River Valley Greenway and Saratoga TODAY pages for Parks-Bentley Place; NYRA's ticket and guest-services
# pages; Universal Preservation Hall's visit page; the Batcheller Mansion Inn's history page; WNYT on city hall;
# nnywaterfalls.com for the Spier Falls view.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'sar_defo','label':'Saratoga County: Moreau, Corinth and downtown Saratoga Springs','added':'2026-11-19 15:21'}
def HM(n,t): return L('HMdb: '+t,'https://www.hmdb.org/m.asp?m='+n)
PLACES=[
N('parks-bentley-place-south-glens-falls','Parks-Bentley Place (Historical Society of Moreau and South Glens Falls)','South Glens Falls','sar','landmark','standing',43.30012,-73.62362,'exact','open','drive','','1773–1840s',
  'Daniel Parks Jr., a French and Indian War veteran whose father had settled at Wing\'s Falls in 1766, moved his family into a log cabin here in 1773 (Hudson River Valley Greenway). Wikipedia dates the log part to the 18th century and the brick house beside it to about 1840; Daniel and Sheldon Benedict bought the farm in 1820 and Cornelius Bentley in 1866. The Glens Falls Portland Cement Company gave it to the new historical society in 1986, and it was put on the National Register in 1994.',
  'A two-storey brick house of about 1840, late Federal to Greek Revival, on a hand-dressed limestone foundation, with the original one-room log dwelling of the late 1700s joined to it, a summer kitchen behind, a one-room schoolhouse and a tool shed (Wikipedia). Inside: a keeping room with a beehive fireplace, a space the society believes hid people escaping slavery, a library and a room of local school photographs (Greenway page). Free tours in open hours; donations asked (Saratoga TODAY, 2026).',
  'The one house in South Glens Falls old enough to have a log cabin inside it, and you can walk in.',
  'Owned and run by the Historical Society of Moreau and South Glens Falls, 53 Ferry Boulevard (Town of Moreau page). The hours given differ by source: the society\'s 2026 notice in Saratoga TODAY gives Saturdays noon to 4 p.m. from May 16 to mid-September; the Village of South Glens Falls page gives Saturdays 1 to 3 p.m. or by appointment; an older Greenway sheet gives Thursdays 1 to 4 p.m. Park on the street; parking not checked on the ground.',
  [W('Parks-Bentley House'),L('Town of Moreau: historical society','https://townofmoreau.org/historical_society.asp'),L('Village of South Glens Falls: Moreau Historical Society','https://villageofsgfny.gov/moreau-historical-society/'),L('Hudson River Valley Greenway: the Parks-Bentley Place','https://www.hudsonrivervalley.org/the-parks-bentley-place'),L('Saratoga TODAY: Parks-Bentley 2026 season','https://saratogatodaynewspaper.com/beginning-may-16-parks-bentley-celebrates-250-years-for-the-us-moreau-and-for-the-parks-bentley-house/')],
  conf='mixed',brick='yes',hours='Saturdays noon to 4 p.m., mid-May to mid-September (2026 notice); the village page says Saturdays 1 to 3 p.m. or by appointment'),
N('gansevoort-mansion','Gansevoort Mansion','Gansevoort','sar','landmark','standing',43.19667,-73.65361,'site','view','drive','','1813',
  'Herman Gansevoort, son of the Revolutionary general Peter Gansevoort and uncle of Herman Melville, built this house in 1813 (Wikipedia). The state\'s 1942 marker in front says General Gansevoort was given the tract in 1783 after it was confiscated from Hugh Munro, a Tory. The house was once used as a Masonic lodge and was put on the National Register in 1976.',
  'A two-storey, five-bay house with a gable roof, a central door and a front verandah on fluted Doric columns (Wikipedia). The state marker stands at Wilton Gansevoort Road (County Route 32) and Catherine Street. Wikipedia says the house is now an inn and cafe; no current page for one was found, so its use and whether it opens are not checked. Interior not checked.',
  'Melville\'s uncle\'s house, on land taken from a Tory.',
  'Private; see it from Catherine Street and County Route 32. Its present use was not confirmed in this session.',
  [W('Gansevoort Mansion'),HM('144990','Gansevoort Mansion')],conf='mixed',brick='some'),
N('international-paper-office-corinth','International Paper Administration Building and Time Office','Corinth','sar','industry','standing',43.24727,-73.81956,'exact','view','drive','','1904–1905',
  'Built in 1904–05 for the Palmer Falls pulp and paper mill on the Hudson, which the Register form says was thought the largest of its kind in the country in 1900 and became International Paper\'s. The upper floor held the superintendent\'s and directors\' offices; below were the time office and a waiting room for the mill hands, so the building split management from labour floor by floor. The mill around it is gone; the form (listed 2017) calls this the last piece of it left, and gave its use then as vacant.',
  'A T-shaped masonry building: Flemish-bond brick with burnt headers over a basement of rough grey-blue stone, a high hipped roof, a projecting entrance pavilion with a big arch of header bricks and oval windows, and a stepped parapet with terra-cotta panels. Inside, the form describes the superintendent\'s room with its period woodwork and a Neoclassical brick fireplace, and the low vaults of the fireproof floor over the time office. Behind it is the open ground where the mill stood. Interior not open; present use not checked.',
  'All that is left of what was called the biggest paper mill in America.',
  'Private (the form names no public use); see it from Pine Street at the head of Heath Street, Village of Corinth. The address is given as both 15 and 17 Pine Street in the form.',
  [L('Register form: International Paper Administration Building & Time Office','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/100001489_text'),W('Corinth, New York'),HM('150079','Jessup\'s Landing')],brick='?'),
N('spier-falls-dam','Spier Falls Dam','Moreau / Corinth','sar','water','standing',43.2345,-73.7568,'exact','view','drive','','1900–1903',
  'The Hudson River Water Power Company built this dam between 1900 and 1903, with up to 1,500 men at a time, for about $3 million; Wikipedia says it was then the fourth largest dam in the world and the largest power dam. It is concrete with a rubble core faced in granite quarried nearby, and sent power to Saratoga, Schenectady, Glens Falls, Troy and Albany. It is named for William E. Spier of the Glens Falls Paper Company. The building holding the turbines and generators had a major fire on September 14, 2024.',
  'The granite-faced dam across the Hudson with its powerhouse below. Most of the time little or no water goes over the crest, which hides a natural fall at its foot (nnywaterfalls.com). Whether the powerhouse has been repaired since the 2024 fire was not checked.',
  'In 1903 the largest power dam in the world; filling it ran the Hudson dry at Fort Edward for a day.',
  'Working hydro plant (Brookfield Power owned it in 2013, says Wikipedia). nnywaterfalls.com says it can be seen from the side of Spier Falls Road just north of the plant\'s parking area; do not go onto the plant grounds. Moreau Lake State Park land lies along the same road.',
  [W('Spier Falls Dam'),L('Northern New York Waterfalls: Spier Falls','https://nnywaterfalls.com/hudsonriver/spierfalls')],brick='?'),
N('lynwood-baptist-church-hadley','Lynwood Baptist Church and cemetery','Hadley','sar','worship','standing',43.30149,-73.90857,'site','view','drive','','1869',
  'The Town of Hadley\'s 1999 marker says the Baptist church here was organized in 1842, the present building put up in 1869, and the cemetery begun in 1844. This rests on that one marker.',
  'The 1869 church and its cemetery on South Shore Road (County Route 7), near the Sacandaga. Whether it still holds services, and what survives inside, were not checked.',
  '',
  'View from South Shore Road. Owner and use not checked; the cemetery is next to the church.',
  [HM('136229','Lynwood Church')],conf='mixed',brick='?'),
N('batcheller-mansion-saratoga','Batcheller Mansion','Saratoga Springs','sar','hotel','standing',43.07516,-73.78537,'exact','open','walk','','1873',
  'George Sherman Batcheller, born in Batchellerville in 1837, had the Albany firm of Nichols & Halcott build this house in 1873 for $100,000 and named it Kaser-el-Nouzha, "palace of pleasure"; he later sat for years as a judge on the international courts in Egypt (inn\'s history page). His daughter sold it in 1916. It was empty by 1937, a rooming house by 1942, cut into a 28-unit retirement home in 1952, and from 1966 to 1973 was wrecked by vandals until the city condemned it in November 1973; a restoration followed, and it is now an inn.',
  'A High Victorian mix of French Renaissance, Italianate and Egyptian motifs, on the corner of Circular Street and Whitney Place facing Congress Park (inn\'s page). Seen from the street; inside is for the inn\'s guests. Interior not checked.',
  'Saved from the wrecking ball after vandals had it for seven years.',
  'A working bed-and-breakfast inn at 20 Circular Street; the outside is seen from the public sidewalk. Downtown street and garage parking.',
  [L('Batcheller Mansion Inn: history','https://www.batchellermansioninn.com/history/')],brick='?',hours='?'),
N('universal-preservation-hall','Universal Preservation Hall (First Methodist Episcopal Church)','Saratoga Springs','sar','worship','standing',43.08033,-73.78754,'exact','open','walk','','1871',
  'Built in 1871 as the First Methodist Episcopal Church to designs by E. Boyden & Son, and used for the Methodists\' annual regional meetings, where William Jennings Bryan, Henry Ward Beecher and Frederick Douglass spoke (Wikipedia). The Methodists sold it in 1976 to the Universal Baptist Church, a historically African-American congregation; it decayed and was condemned in 2000. Townspeople and the church rebuilt it: a new sanctuary for the Baptists was finished in 2004, and the hall reopened as a 700-seat performance venue on February 29, 2020, run with Proctors.',
  'High Victorian Gothic in rose-coloured brick with light Ohio sandstone arches and bands. Inside, two walnut and ash staircases lead up to the main hall, 45 feet to the ceiling, with a balcony on three sides on Gothic-arched supports and tall Tiffany-inspired stained-glass windows (Wikipedia). See the inside at a show or event; the Baptist congregation worships in its own part of the building on Sundays.',
  'A Gothic church where Frederick Douglass spoke, condemned in 2000 and now a concert hall.',
  'Performance and events venue at 25 Washington Street; inside only with a ticket to an event. Its visit page lists downtown garages and lots (Woodlawn garage, the Putnam Street lot) and street parking; garage parking is charged from Memorial Day to Labor Day.',
  [W('Universal Preservation Hall'),L('Universal Preservation Hall: plan your visit','https://universalpreservationhall.org/about-us/plan-your-visit')],brick='yes',hours='?'),
N('saratoga-springs-post-office-city-hall','U.S. Post Office and City Hall, Broadway and Church Street','Saratoga Springs','sar','civic','standing',43.08354,-73.78514,'exact','open','walk','','1871–1916',
  'Four landmarks meet at this corner (Wikipedia): the Classical Revival post office, built in 1910 to designs by James Knox Taylor with one of the most elaborate post office lobbies in the state, the Italianate city hall across Broadway, the Ainsworth Building, and the 1916 marble Adirondack Trust Company. City hall opened as the town hall on December 28, 1871, with about 2,400 people at the ceremony, and became city hall when the village and town merged into a city in 1915 (WNYT).',
  'Post office: yellow pressed Roman brick on granite, marble and limestone trim, an arched entrance on polished veined-marble Doric columns. In the lobby, a 14-foot coffered plaster ceiling with a leaded-glass skylight, green marble wainscoting, and on either side of the vestibule Guy Pène du Bois\'s 1930s murals "Saratoga in the Racing Season" (Wikipedia). The lobby has been altered somewhat. City hall interior not checked.',
  'Race-track murals in a 1910 post office lobby, across from the hall the town built in 1871.',
  'Working post office at 475 Broadway, open in its counter hours (not checked here; see USPS); city hall is the working seat of the city. Downtown street and garage parking.',
  [W('United States Post Office (Saratoga Springs, New York)'),W('Broadway Historic District (Saratoga Springs, New York)'),L('WNYT: City Hall\'s 150th anniversary','https://wnyt.com/archive/saratoga-springs-city-hall-celebrating-150th-anniversary')],brick='?',hours='?'),
N('high-rock-park-spring','High Rock Spring and High Rock Park','Saratoga Springs','sar','water','standing',43.08695,-73.78020,'site','public','walk','','1771–',
  'The city\'s markers here say the Mohawks drank at High Rock for centuries and brought Sir William Johnson to it in 1771, and that settlement began around the spring. Clarke and White first bottled its water in 1848 inside a round brick building; in 1865–66 McCaffery and Ainsworth put up a Gothic pavilion with a gilded eagle, which bankrupted them. William Fargo\'s company ran the spring from 1872 to 1904; it stopped flowing by 1911, the state took the springs that year, the city got the cone in 1968, and the spring was drilled again in 2015.',
  'The mineral cone of High Rock under a pavilion, the exposed rock face of the Saratoga fault, the Governor spring of 1908 and a fountain piped from the Peerless spring, with markers telling the story (HMdb). Whether the present pavilion is the 1860s one was not checked.',
  'Where Saratoga began: a rock cone of spring water Sir William Johnson was carried to in 1771.',
  'City park on High Rock Avenue, open ground. Parking on the street and in the city lots near Henry Street.',
  [HM('131582','The Story Starts Here'),HM('131583','High Rock in the 1800\'s'),HM('131584','Creation of the Park'),HM('131579','Highrock Park')],brick='?'),
N('franklin-square-saratoga','Franklin Square','Saratoga Springs','sar','town','standing',43.08193,-73.78861,'area','view','walk','','1830s–',
  'The railroad\'s station at Division and Franklin streets made this square (first Marvin Square) the one upscale neighbourhood on the city\'s working-class West Side, with large Greek Revival houses (Wikipedia). The 1984 marker says it is ringed by buildings from as early as the 1830s, many owned by the Marvin family of the United States Hotel, that it became a centre of health hotels and homes, declined in the early 1900s and is being restored as shops and houses. It was a Register district of its own from 1973 and is now part of the West Side Historic District.',
  'Greek Revival townhouses and former hotels round a small square; the marker says it looks much as it did around 1900. Private houses and shops: from the street.',
  '',
  'Public streets; the buildings are private. The pin is the marker, not a single building.',
  [W('West Side Historic District (Saratoga Springs, New York)'),HM('131744','Franklin Square')],brick='?'),
N('saratoga-race-course','Saratoga Race Course','Saratoga Springs','sar','amuse','standing',43.07391,-73.76957,'exact','open','drive','','1863–',
  'John Morrissey ran the first thoroughbred meet on what is now the Oklahoma Training Track in August 1863, then bought 125 acres across Union Avenue and opened the main grandstand there in 1864 (Wikipedia). It is often called the oldest major sporting venue of any kind in the country, and the Travers Stakes has been run here since 1864. The grandstand was extended in the 1960s, doubling the seating.',
  'The grandstand and clubhouse, the paddock and backyard under the trees, and across Union Avenue the Oklahoma Track, where the 1863 meet was held, with its 2013 Whitney Viewing Stand. Which parts of the grandstand date from which years was not checked.',
  'The country\'s oldest major sporting venue still in use, since 1863.',
  'Run by the New York Racing Association. Open on racing days of the summer meet (2026: July 3 to September 7, per Wikipedia). NYRA: gates usually open at 11 a.m.; free early access from 7 a.m. to claim picnic tables, cleared before 11; general admission from $7, children 12 and under free; no cash for admission or parking in 2026. Free general parking in the Oklahoma lot off Union Avenue, with a shuttle to Gates A and B.',
  [W('Saratoga Race Course'),L('NYRA: Saratoga tickets','https://www.nyra.com/saratoga/tickets/'),L('NYRA: guest services','https://www.nyra.com/saratoga/visit/guest-services')],brick='?',hours='Racing days of the summer meet (July to Labor Day); gates usually 11 a.m., early access 7 a.m.'),
]
PIN_NOTES={
 'parks-bentley-place-south-glens-falls':'ArcGIS geocoder PointAddress for 53 Ferry Boulevard (the Town of Moreau page gives the address).',
 'gansevoort-mansion':'Wikipedia coordinate; the HMdb marker is about 90 m east at Catherine Street and County Route 32.',
 'international-paper-office-corinth':'ArcGIS geocoder PointAddress for 15 Pine Street, Corinth (the address in the form\'s description).',
 'spier-falls-dam':'Wikipedia coordinate; on the leaf-off aerial it falls on the dam crest.',
 'lynwood-baptist-church-hadley':'HMdb marker on South Shore Road, moved 27 m onto the red building beside it on the leaf-off aerial (taken to be the church; the cemetery rows are across the road).',
 'batcheller-mansion-saratoga':'ArcGIS geocoder PointAddress for 20 Circular Street.',
 'universal-preservation-hall':'ArcGIS geocoder PointAddress for 25 Washington Street.',
 'saratoga-springs-post-office-city-hall':'ArcGIS geocoder PointAddress for 475 Broadway (the post office).',
 'high-rock-park-spring':'HMdb marker positions round the High Rock cone.',
 'franklin-square-saratoga':'HMdb marker position (Franklin Square Associates, 1984).',
 'saratoga-race-course':'OpenStreetMap building "Saratoga Race Course Grandstand" (osmnear.py); the Wikipedia coordinate fell in the infield pond.',
}
