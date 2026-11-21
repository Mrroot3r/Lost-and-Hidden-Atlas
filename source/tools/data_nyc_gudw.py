# November 21, 2026: the North Fork of Long Island (the Town of Southold: Cutchogue, Mattituck, Southold, Greenport,
# Stirling, Orient) and Shelter Island, with one boat-only ruin in Gardiners Bay. Region drawn at random by
# tools/choose.py --state ny (nyc), which offered Orient and Southold; tools/start.py showed no Atlas place in the Town
# of Southold or on Shelter Island.
# Sources read in this session: Wikipedia articles and the Register lists for the towns of Southold and Shelter Island
# (tools/wiki_raw.py), and the pages of the bodies that run the places (Cutchogue-New Suffolk Historical Council,
# Southold Historical Museum, First Presbyterian Church of Southold, Railroad Museum of Long Island, Village of
# Greenport, Congregation Tifereth Israel, Peconic Landing, Oysterponds Historical Society, Shelter Island Historical
# Society, Sylvester Manor Educational Farm, Union Chapel in the Grove, NYS Parks), all read with tools/page.py.
from data_b import N
from data_ma import W
BATCH={'key':'nyc_gudw','label':'Long Island: Southold, Greenport, Orient and Shelter Island','added':'2026-11-21 19:46'}

CNSHC=['Cutchogue-New Suffolk Historical Council','https://www.cutchoguenewsuffolkhistory.org/']
SHM=['Southold Historical Museum: visit','https://southoldhistorical.org/visit']

PLACES=[
N('old-house-cutchogue','The Old House and the Cutchogue Village Green','Cutchogue','nyc','landmark','standing',41.00798,-72.48638,'site','open','drive','','1698–1699 (or 1649)',
  'A two-storey timber-frame house about 36 by 20 feet with three-part casement windows, a great brick chimney between its four rooms and a kitchen fireplace over nine feet wide; the National Park Service called it one of the most distinguished surviving examples of English domestic building in America, and it was made a National Historic Landmark in 1961. Its age is argued over. The old story is that John Budd built it about 1649 and that it was moved to Cutchogue as a wedding gift to his daughter Anna and Benjamin Horton in 1658; tree-ring studies say its timbers were felled in 1698 (Wikipedia puts the first study in 2003 and gives about 1699; the Historical Council puts it in 2008 and gives 1698; a 2017–2018 study agreed). Joseph Wickham bought it in 1699, and the Loyalist Parker Wickham lived in it. The 1938 hurricane stripped the trees that hid it, and it was restored in 1940 and 1968.',
  'On the Village Green with it stand the Wickham Farmhouse (a one-storey Cape with a central chimney, moved here in 1965; the Council dates it to 1704, its own text to the mid-18th century), the Old Schoolhouse of about 1840, Cutchogue\'s first district school, used until 1903, a Victorian red barn, a carriage house, and the library in the 1862 Independent Congregational Church. Inside the Old House the Council has refurnished the rooms as a wealthy tanner\'s house of 1698 with reproductions and antiques, and shows "poppet" dolls found in the 1940 restoration, witch bottles and a horseshoe hung against witches. The Green itself was cleared of brush and two ruined house foundations in about 1960.',
  'A house whose builders may have known the first settlers of Long Island, and the tree rings that argue the date.',
  'Owned by the Cutchogue-New Suffolk Historical Council, which gives guided tours in summer (Wikipedia); the Council\'s own pages read in November 2026 gave no tour days or times. GPS address 27320 Main Road (Route 25), on the south side of the road as you reach the business area. Parking was not checked on the ground.',
  [W('Old House (Cutchogue)'),CNSHC,['Council: the Old House, 1698 origin story','https://www.cutchoguenewsuffolkhistory.org/timeline/the-old-house-1698/'],['Council: the Wickham Farmhouse','https://www.cutchoguenewsuffolkhistory.org/timeline/the-wickham-farmhouse-1704/']],
  conf='mixed',brick='no',hours='?'),

N('old-cutchogue-burying-ground','Old Cutchogue Burying Ground','Cutchogue','nyc','burial','standing',41.02154,-72.47702,'site','public','drive','','1717',
  'The burying ground of Cutchogue\'s settlers, dated by the Cutchogue-New Suffolk Historical Council to 1717. It was a town ground, not a churchyard, so burials were of any denomination; the headstones face west and the footstones east. The Council bought it from the Cutchogue Presbyterian Church for one dollar in 1960 and has cared for it since.',
  'Old headstones and footstones in rows. A conservator surveyed every stone in 2014, and since 2015 volunteers have cleaned off lichen and reset, repaired and re-joined broken stones in yearly workshops; the inscriptions are recorded on BillionGraves.',
  '',
  'Cared for by the Cutchogue-New Suffolk Historical Council, which allows full public access (its "About us" page). At 32770 Main Road, on the corner of Harbor Lane, on the south side of Route 25 about a mile east of the Village Green. Parking was not checked on the ground.',
  [CNSHC,['Council: Old Cutchogue Burying Ground','https://www.cutchoguenewsuffolkhistory.org/timeline/old-burying-ground-1717/'],['Council: about us','https://www.cutchoguenewsuffolkhistory.org/about-us/']],
  brick='?',hours=''),

N('horton-point-light-southold','Horton Point Lighthouse','Southold','nyc','light','standing',41.08511,-72.44567,'exact','open','drive','','1857',
  'A lighthouse on a bluff about 60 feet above Long Island Sound, on land that was part of Barnabas Horton\'s 1640 grant. Building began on May 19, 1857 under William Sinclair, who became its first keeper; 150,000 bricks came by schooner, and the light, a third-order Fresnel lens burning sperm-whale oil, was first lit on October 15, 1857. It was dark from 1933, when an automatic light on a steel tower took over, until 1990. Stella Prince Terry, acting keeper in 1903–1904, was added to the Coast Guard\'s list of women keepers in 2023.',
  'A square tower 58 feet high joined to the keeper\'s house: granite foundation, brick walls under stucco, a black lantern and copper dome (Wikipedia). The house holds the Southold Historical Museum\'s Nautical Museum. The light still works, a green flash every ten seconds.',
  'A whale-oil lighthouse on a bluff, and the woman keeper the records forgot.',
  'The lighthouse and its grounds are under the Southold Park District (Wikipedia); the Nautical Museum inside is run by the Southold Historical Museum, 3575 Lighthouse Road. Parking in the Park District lot costs $5 for non-residents; street parking is by Town permit only (museum page, read November 2026, when the museum was closed for the season).',
  [W('Horton Point Light'),SHM,['Southold Historical Museum: history of Horton Point Lighthouse','https://www.southoldhistorical.org/hortonpointhistory']],
  th=[41.0855,-72.44467],thn='Southold Park District lot, Lighthouse Road',brick='?',hours='Memorial Day weekend to September 20: Saturday and Sunday 11:30 a.m. to 4 p.m. (Nautical Museum)'),

N('southold-historical-museum-maple-lane','Southold Historical Museum, Maple Lane campus','Southold','nyc','landmark','standing',41.06577,-72.42316,'site','open','drive','','c. 1750–1900',
  'A museum village grown from the home of its founder, Ann Hallock Currie-Bell, left to the museum in 1964; other old buildings of the town were bought or given and moved to the site. Eleven buildings on the campus open to the public.',
  'The Thomas Moore House, built about 1750 by Samuel Landon (on the Register, as the Samuel Landon House); the Joseph N. Hallock House of 1900, a late Victorian house with the paintings of Thomas Currie-Bell (also on the Register); the Bay View School of 1822, used until 1925; the Gagen Blacksmith Shop of 1842, where blacksmiths still demonstrate; a print shop of 1840 brought from Riverhead with a working press; an 18th-century barn of hand-hewn beams holding sleighs and carriages; the round brick Bay View icehouse of 1875 with its conical roof, rare on the North Fork; and an 1875 corncrib (museum page).',
  '',
  'Run by the Southold Historical Museum, 55200 Main Road; private group tours by appointment. The museum\'s offices and shops are in the Henry W. Prince Building at 54325 Main Road. Parking was not checked on the ground (museum pages read November 2026, when the campus was closed for the season).',
  [SHM,['Southold Historical Museum: Maple Lane campus','https://www.southoldhistorical.org/historic-buildings']],
  brick='?',hours='Memorial Day weekend to September 20: Saturday and Sunday 1 to 4 p.m.'),

N('first-presbyterian-southold','First Presbyterian Church of Southold and the Old Burying Ground','Southold','nyc','worship','standing',41.06274,-72.43046,'exact','open','drive','','1640; church 1803',
  'The congregation was founded in 1640 as the First Church of Christ in Southold under the Rev. John Youngs from Southwold, England. Its first meeting house stood near the Founders\' Monument and its second, of 1684, across Main Street; the present church was built in 1803, 40 by 60 feet for four hundred people, with the steeple added in 1808, a bell in 1855 and the town clock in 1884. Its cemetery\'s northwest corner is the Old Burying Ground, the acre the Puritan settlers set aside.',
  'The church keeps the 1855 iron triangle once rung to call people to worship. The Old Burying Ground has about twenty graves of the 17th century, among them the box tomb of William Wells, dated 1671, which the church calls the oldest colonial grave on Long Island; slate and sandstone stones carved by New England stonecutters from about 1680 to 1810 show winged death\'s heads (the earliest 1687) and soul effigies. About a thousand stones have been cleaned and many reset. A brochure for a self-guided walk is in a holder on an entrance pillar on Main Road; the Southold library runs guided visits. Interior not checked.',
  'The oldest English graves on Long Island, carved with death\'s heads.',
  'First Presbyterian Church of Southold, 53100 Main Road (address from OpenStreetMap). The church\'s pages give Sunday worship and the cemetery\'s self-guided brochure; for a docent tour call the Southold Free Library. Parking was not checked on the ground.',
  [['First Presbyterian Church of Southold','https://jan-falkowski.squarespace.com/'],['FPC Southold: history','https://jan-falkowski.squarespace.com/history'],['FPC Southold: the Old Burying Ground','https://jan-falkowski.squarespace.com/old-burying-ground']],
  brick='?',hours='Sunday worship 10 a.m.'),

N('greenport-station-railroad-museum','Greenport station and the Railroad Museum of Long Island','Greenport','nyc','rail','standing',41.09972,-72.36361,'site','open','drive','stations','1844; buildings 1892',
  'The eastern end of the Long Island Rail Road\'s main line, opened on July 29, 1844. The station was burned in the town\'s Fourth of July festivities in 1870 and rebuilt that October, and replaced by the present building in 1892 (some sources say 1894). Steam ended on June 5, 1955, mail in 1965, and trains ran onto the dock until 1978. The station, its freight house and turntable were listed on the Register in 1989 as a historic district.',
  'The 1892 station and the 1892 freight house, which the Railroad Museum of Long Island has restored as its Greenport museum, with railroad exhibits and the LIRR wooden caboose No. 14; the turntable is in the same yard of about 3.4 acres, by the Shelter Island ferry. The museum gives a self-guided walk of the yard. The station still serves trains.',
  '',
  'The museum (Railroad Museum of Long Island) was closed for the 2026 season when read in November 2026 and reopens May 29, 2027; admission $9 for adults, $5 for children 5 to 12. It sits across the parking lot from the west end of the train platform. Its main site and restoration shop are in Riverhead.',
  [W('Greenport station'),['RMLI: Greenport hours','https://rmli.org/greenport/'],['RMLI: visiting us','https://rmli.org/visit/'],['RMLI: about us','https://rmli.org/about-us/']],
  brick='?',hours='From May 29, 2027, 10:30 a.m. to 4:30 p.m. (season days not given); closed for the 2026 season'),

N('greenport-antique-carousel','Greenport\'s antique carousel, Mitchell Park','Greenport','nyc','amuse','standing',41.10162,-72.36103,'exact','open','drive','amusements','',
  'A carousel about a hundred years old, given to the village by the Grumman Aircraft Corporation, turning in the Jess Owen Carousel House in Mitchell Park on Greenport\'s waterfront (Village of Greenport page).',
  'The carousel in its carousel house; single rides $3, fifteen for $30. Its maker and date were not checked.',
  '',
  'Owned and run by the Village of Greenport, in Mitchell Park off Front Street; last ride 15 minutes before closing. Village lots nearby; parking was not checked on the ground.',
  [['Village of Greenport: the carousel','https://villageofgreenport.org/carousel-greenport-village.php']],
  conf='mixed',brick='?',hours='School closing to Labor Day: Sunday to Friday 11 a.m. to 7 p.m., Saturday to 8 p.m.; then weekends 11 a.m. to 5 p.m. and school holidays'),

N('tifereth-israel-greenport','Congregation Tifereth Israel synagogue','Greenport','nyc','worship','standing',41.10087,-72.36486,'exact','open','drive','','1903–1904',
  'A small Victorian vernacular synagogue at 519 Fourth Street; its cornerstone was laid on December 28, 1903 and it was dedicated on January 11, 1904. The congregation began Orthodox, became Conservative and is now egalitarian Conservative. It was listed on the Register in 2006.',
  'The 1903 front-gabled building with its low projecting entrance; a large addition stands behind. Inside, the upper balcony was the women\'s section while the congregation was Orthodox, and seating became mixed when it joined the Conservative movement (Wikipedia). Interior fabric not checked beyond that.',
  '',
  'Congregation Tifereth Israel, 519 Fourth Street; the congregation\'s page gives its regular Friday night and Shabbat morning services. Street parking; not checked on the ground.',
  [W('Congregation Tifereth Israel (Greenport, New York)'),['Congregation Tifereth Israel','https://tiferethisraelgreenport.org/']],
  brick='no',hours='Friday 7:30 to 8:30 p.m.; Shabbat morning 9:30 to 11:30 a.m.'),

N('brecknock-hall-greenport','Brecknock Hall','Stirling, Greenport','nyc','landmark','standing',41.11725,-72.36215,'site','view','drive','','1857',
  'An Italianate mansion of square-cut ashlar stone built in 1857 for David Gelston Floyd, a whaling entrepreneur and grandson of General William Floyd, signer of the Declaration of Independence. It has a central projecting gable and a one-room cupola on the roof; a 19th-century barn, an early 20th-century greenhouse and a caretaker\'s house stand with it. Peconic Landing says it is one of the largest mid-19th-century stone mansions built on Long Island. The Brecknock Hall Foundation restored it in 2008.',
  'The stone house at the entrance to the Peconic Landing campus, with its lawns running toward the Sound. Interior not checked.',
  '',
  'On the grounds of Peconic Landing, a retirement community on 144 acres, which hires the hall out for weddings and events; the Brecknock Hall Foundation holds educational programs and events open to the public there, such as the yearly end-of-summer fireworks. Not open at set times: see it at a public event or from the drive. Parking was not checked.',
  [W('Brecknock Hall'),['Peconic Landing: Brecknock Hall','https://peconiclanding.org/brecknock-hall']],
  brick='no',hours=''),

N('orient-historic-district-oysterponds','Orient village and the Oysterponds Historical Society','Orient','nyc','town','standing',41.13829,-72.30352,'site','open','drive','','1730–late 19th century',
  'Orient\'s Register historic district of 120 contributing buildings, put up from the late 18th to the late 19th century, most of them Cape Cod houses of one and a half storeys in shingle or clapboard, with Italianate and other 19th-century styles among them. Its focal point is Orient Wharf, begun in 1740. The Oysterponds Historical Society keeps a campus of old buildings on Village Lane.',
  'Walk Village Lane from the monument on Main Road to the wharf; the society\'s campus is on the left about 500 yards down. Which of its buildings are which, and what is inside, was not checked.',
  '',
  'Oysterponds Historical Society, 1555 Village Lane: its buildings and exhibitions were closed for the season when read in November 2026; staff may open the doors for a tour on weekdays if you call the office. Admission $10 for non-member adults. Suffolk County Transit bus S92 and the Hampton Jitney stop at Orient village. Parking was not checked on the ground.',
  [W('Orient Historic District'),['Oysterponds Historical Society: address, hours and directions','https://oysterpondshistoricalsociety.org/address-hours-directions/']],
  brick='?',hours='Seasonal (closed when read in November 2026); weekday tours by arrangement through the office'),

N('orient-point-light','Orient Point Lighthouse ("the Coffee Pot")','Orient','nyc','light','standing',41.16344,-72.22361,'exact','boat','boat','','1899',
  'A cast-iron "sparkplug" lighthouse on a reef in Plum Gut, the narrow channel between Orient Point and Plum Island. A daymark was put there in 1855 and a stone beacon in 1874, which ice carried away in 1896. The caisson tower was begun in October 1898 and lit on November 10, 1899. It was automated in 1954 or on April 5, 1958 (Wikipedia gives both); the Coast Guard\'s 1970 plan to pull it down was dropped after a public outcry. Sold at auction in 2013, it belongs to the sculptor Randy Polumbo, who has made part of it an artist\'s residency.',
  'A tower 45 feet tall with six decks, on a riprap island built up after 1899. Wikipedia quotes the owner that part of the base is missing.',
  'The Coffee Pot at the very tip of the North Fork, sold to an artist.',
  'Private, standing in the water: seen from boats in Plum Gut (the ferries to New London pass close) and from shore. NYS Parks says it is one of four lighthouses visitors can see from Orient Beach State Park (40000 Main Road; vehicle fee in season; hours on its page).',
  [W('Orient Point Light'),['NYS Parks: Orient Beach State Park','https://parks.ny.gov/parks/106']],
  conf='mixed',brick='no',hours=''),

N('gildersleeve-octagon-mattituck','Andrew Gildersleeve Octagonal Building','Mattituck','nyc','landmark','standing',40.9913,-72.53411,'area','view','drive','','1854',
  'An eight-sided building put up in 1854 by Andrew Gildersleeve, a master carpenter, as his family\'s home and a store. It was listed on the Register on August 19, 1976.',
  'The octagon at the corner of Main Road (Route 25) and Love Lane, Mattituck\'s little shopping street. Its present use and interior were not checked.',
  '',
  'Not known to open to visitors; owner and present use not checked: see it from Main Road and Love Lane. Street parking on Love Lane, not checked on the ground.',
  [W('Andrew Gildersleeve Octagonal Building')],
  brick='some',hours=''),

N('havens-house-shelter-island','Havens House (James Havens Homestead)','Shelter Island','nyc','landmark','standing',41.06411,-72.33096,'exact','open','drive','','1743',
  'A large shingled farmhouse built in 1743 and enlarged in the early to mid 19th century, with a broad gabled roof, a wraparound porch and rear wings. It was listed on the Register in 1986 and is owned by the Shelter Island Historical Society as a house museum, beside its Shelter Island History Center.',
  'The house and the society\'s exhibits; its 2026 exhibit was "Havens House: Witness the American Revolution". The society runs a farmers\' market on the grounds from late May to early September. Interior fabric not checked.',
  '',
  'Shelter Island History Museum (Shelter Island Historical Society), 16 South Ferry Road; tours of Havens House in its open hours, and by appointment (631-749-0025). Parking was not checked on the ground.',
  [W('James Havens Homestead'),['Shelter Island Historical Society','https://www.shelterislandhistorical.org/']],
  brick='some',hours='Fall: Tuesday to Friday 10 a.m. to 2 p.m.; second and fourth Wednesdays 10 a.m. to 7:30 p.m.'),

N('sylvester-manor-shelter-island','Sylvester Manor','Shelter Island','nyc','landmark','standing',41.08039,-72.34111,'site','public','walk','','1652; house 1737',
  'Nathaniel Sylvester acquired the land, some 8,000 acres of the island, in the 17th century; he and his brother owned plantations in Barbados and over 200 enslaved Africans, and when he died in 1680 his heirs inherited the estate with 23 enslaved people. The manor house was built in 1737 for his grandson Brinley Sylvester by enslaved Africans and European indentured servants; the last enslaved person here was freed in 1820. The grounds hold a burying ground of unmarked graves of the enslaved. It is now a 236-acre nonprofit educational farm, listed on the Register in 2015.',
  'The house seen from the grounds, the gateway, three walking trails (Creekside, Woodlands and Farm) and the farm, with the windmill nearby. The manor house is closed to visitors while it is readied for rehabilitation (manor page, November 2026).',
  'A 17th-century plantation on Long Island, and the people who were enslaved on it.',
  'Sylvester Manor Educational Farm. Trails and grounds open March to October, every day, sunrise to sunset; closed November to February for the Town of Shelter Island\'s deer hunt (obey the trail-closed signs). Maps at the kiosk by the front entrance and by the parking area; leashed dogs allowed, no bicycles. The farmstand at 21 Manwaring Road opens Friday to Sunday, 9 a.m. to 5 p.m., May to November.',
  [W('Sylvester Manor'),['Sylvester Manor: plan your trip','https://www.sylvestermanor.org/plan-your-trip/']],
  brick='?',hours='Grounds and trails March to October, daily sunrise to sunset; closed November to February; house closed'),

N('shelter-island-windmill','Shelter Island Windmill','Shelter Island','nyc','industry','standing',41.07658,-72.3361,'site','public','walk','','1810',
  'A windmill built in 1810 by the master millwright Nathaniel Dominy V as the "Old Red Mill" at the mouth of Jockey Creek in Southold. Joseph Congdon bought it in 1840 and moved it to the middle of Shelter Island; it ground grain until before 1879, when Lillian Horsford bought it to keep it, ran again in 1917–1918 for wartime flour, and was moved to Sylvester Manor in 1926 by Cornelia Horsford.',
  'The windmill on the Sylvester Manor farm, north of Manwaring Road. The Historical Society says the "Devil\'s Footprint" rock lies in the back farm field behind it: ask the farm first.',
  'A Dominy windmill that crossed Peconic Bay by ox team and barge.',
  'On the Sylvester Manor Educational Farm, whose grounds and trails are open March to October, sunrise to sunset, and closed November to February for the deer hunt.',
  [W('Shelter Island Windmill'),['Sylvester Manor: plan your trip','https://www.sylvestermanor.org/plan-your-trip/']],
  brick='no',hours='Grounds March to October, daily sunrise to sunset'),

N('union-chapel-shelter-island-heights','Union Chapel in the Grove','Shelter Island Heights','nyc','worship','standing',41.08389,-72.35889,'exact','open','drive','','1875',
  'A shingled wood-frame chapel built in 1875, the most important surviving building of the Shelter Island Heights Grove and Camp Meeting Association, a Methodist camp begun in 1872. Its front has a two-and-a-half-storey bell tower with a double door at the base under a small porch. It was listed on the Register in 1984.',
  'The chapel among the trees of the Grove. It is now a summer community chapel with no members: trustees bring in guest preachers and local musicians, and services are followed by a reception outdoors. Interior not checked.',
  '',
  'Union Chapel in the Grove: interfaith services open to all on Sunday mornings in summer (in 2026 the last was at the end of August). Parking was not checked on the ground.',
  [W('Union Chapel (Shelter Island Heights, New York)'),['Union Chapel in the Grove','https://unionchapelinthegrove.org/']],
  brick='no',hours='Summer: Sundays 10:30 a.m.'),

N('gardiners-point-the-ruins','"The Ruins": Fort Tyler on Gardiners Point Island','Gardiners Bay','nyc','fort','ruins',41.14137,-72.14619,'site','boat','boat','forts','1855–1924',
  'Once a peninsula of Gardiners Island, cut off by a storm in 1888. A lighthouse stood on it from 1855. During the Spanish–American War Congress paid for a fort here, Fort Tyler, with Battery Edmund Smith for two 8-inch disappearing guns and two 5-inch guns; records say it was never armed. Shifting sand dogged it, and it was abandoned in 1924. In World War II it was used for bombing practice, and with erosion it was reduced to a speck of fort foundations, known locally as "The Ruins".',
  'What is left of the fort\'s foundations on a speck of island (Wikipedia; the pin check shows what the aerial sees). It is part of the Long Island National Wildlife Refuge Complex.',
  'A coast fort that was never armed, bombed and eroded to a concrete speck in the bay.',
  'Seen only from a boat. Wikipedia says the island is treated as a navigational hazard because of possible unexploded ordnance; no source read says landing is allowed. It lies in the Town of East Hampton, north of Gardiners Island, which is private.',
  [W('Gardiners Point Island')],
  brick='?',hours=''),
]

PIN_NOTES={
 'old-house-cutchogue':'ArcGIS address point for 27320 Main Road, the Council\'s GPS address for the Village Green; Wikipedia\'s point is 25 m away.',
 'old-cutchogue-burying-ground':'ArcGIS address point for 32770 Main Road, the address the Council gives; OpenStreetMap maps the cemetery at the same spot.',
 'horton-point-light-southold':'ArcGIS address point for 3575 Lighthouse Road; Wikipedia\'s point is 10 m away.',
 'southold-historical-museum-maple-lane':'ArcGIS address point for 55200 Main Road, the museum\'s address for the campus.',
 'first-presbyterian-southold':'OpenStreetMap place of worship, 53100 Main Road (tools/nom.py).',
 'greenport-station-railroad-museum':'Wikipedia\'s point for the station.',
 'greenport-antique-carousel':'OpenStreetMap building tagged attraction=carousel, "Antique Carousel", 115 Front Street (tools/osmnear.py).',
 'tifereth-israel-greenport':'ArcGIS address point for 519 Fourth Street.',
 'brecknock-hall-greenport':'Moved with tools/pix.py 67 m north onto the large house the aerial shows at the head of the drive; the Register list point was on the lawn south of it.',
 'orient-historic-district-oysterponds':'ArcGIS address point for 1555 Village Lane, the Oysterponds Historical Society.',
 'orient-point-light':'Wikipedia\'s point, on the reef in Plum Gut.',
 'gildersleeve-octagon-mattituck':'ArcGIS street intersection of Love Lane and Main Road, the corner Wikipedia names. The Register list point was 880 m east, on a building in a lawn by a pond, not at Love Lane; which corner the octagon stands on was not settled from the aerial.',
 'havens-house-shelter-island':'ArcGIS address point for 16 South Ferry Road; Wikipedia\'s point is 60 m away.',
 'sylvester-manor-shelter-island':'Wikipedia\'s point for the manor.',
 'shelter-island-windmill':'Moved with tools/pix.py 95 m north-west from Wikipedia\'s point (in the middle of the farm fields) onto a small tower casting a long shadow at the head of the fields, taken to be the windmill; not certain.',
 'union-chapel-shelter-island-heights':'Wikipedia\'s point for the chapel.',
 'gardiners-point-the-ruins':'Wikipedia\'s point for the island.',
}
