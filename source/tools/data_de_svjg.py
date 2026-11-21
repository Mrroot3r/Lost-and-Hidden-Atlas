# November 20, 2026: Delaware, second pass, spread over the whole state (Wilmington and New Castle, Kent County, Sussex
# County). Ground taken with tools/choose.py --thinnest (Delaware had 16 places, the fewest of any state or province free).
# Facts from the linked sources only, read in this session: Wikipedia articles through tools/wiki_raw.py, the county
# Register lists through wiki_raw.py --rows, and the managing bodies' own pages through tools/page.py: the Delaware
# Division of Historical and Cultural Affairs (history.delaware.gov), Delaware State Parks, DelDOT, the National Park
# Service, the Delaware Nature Society, Old Swedes, Barratt's Chapel, the Overfalls foundation, the Fenwick Island
# lighthouse friends, the Delaware River and Bay Lighthouse Foundation, the Friends of Bombay Hook and the Town of Dagsboro.
from data_b import N
from data_ma import W

HCA='https://history.delaware.gov'
STATE_SITES=['Delaware Historical and Cultural Affairs: other historic sites owned by the state',HCA+'/historic-sites/']

BATCH={'key':'de_svjg','label':'Delaware: Kent, Sussex and old Wilmington','added':'2026-11-20 08:22'}

PLACES=[
N('old-swedes-church-wilmington','Holy Trinity (Old Swedes) Church','Wilmington','de','worship','standing',39.73853,-75.54056,'site','open','walk','','1698–99',
  'A congregation of the former New Sweden colony built this church in 1698 and 1699 and consecrated it on Trinity Sunday, June 4, 1699. It stands on the burial ground of Fort Christina, which goes back to 1638, and has been an Episcopal parish since 1791. It is a National Historic Landmark and part of First State National Historical Park, and the church calls itself the oldest church building in the nation still used for worship as built.',
  'Walls of local blue granite with Swedish brick that came over as ships\' ballast. The tour takes in the church, the burial ground of 1638 (the article counts over 15,000 burials) and the early 18th-century Hendrickson House. The church is still used for services.',
  'A church of 1699 on New Sweden\'s burial ground.',
  'Old Swedes Historic Site runs the tours: $12 a person, $7 for students aged 6 to 15, the military and first responders, free under 6; walking the cemetery alone is $5. Hours from its own page. No parking lot was found near the church on the aerial (the mapped one on Taylor Street is a building); street parking not checked.',
  [['Old Swedes Historic Site: hours and tours','https://oldswedes.org/hours-tours/'],W('Holy Trinity Church (Old Swedes)')],
  brick='some',hours='Thursday to Saturday 10 a.m. to 3 p.m. (tours of the church, burial ground and Hendrickson House)'),

N('fort-christina-wilmington','Fort Christina and the Rocks','Wilmington','de','fort','marker',39.73722,-75.53833,'area','public','walk','forts','1638',
  'The first Swedish settlers landed here in March 1638 from the Kalmar Nyckel and the Fogel Grip, at a stone outcrop on the Christina River called the Rocks, and built an earthwork fort round it: the first settlement of New Sweden. The Dutch took it in 1655. Under English rule the fortifications decayed and vanished entirely. The state made a park of the Rocks and the fort site in 1938, for the 300th anniversary.',
  'Nothing of the fort is left. The park holds the Rocks and a granite monument from Sweden topped by a replica of the Kalmar Nyckel, by the sculptor Carl Milles. Old Swedes Church is a few blocks west.',
  'Where New Sweden began, and what is left: a rock and a monument.',
  'Fort Christina State Park, part of First State National Historical Park; no fee. The National Park Service page says the site is open from Memorial Day weekend to Labor Day with reduced fall hours to the end of October, starting at the Kalmar Nyckel Foundation\'s tent. Parking: a mapped lot on East 7th Street about 200 m north-east (not checked).',
  [['National Park Service: Fort Christina','https://www.nps.gov/frst/planyourvisit/fort-christina.htm'],STATE_SITES,W('Fort Christina')],
  th=[39.73812,-75.53617],thn='Lot on East 7th Street',brick='no',hours='Memorial Day weekend to Labor Day; reduced hours in the fall to the end of October'),

N('new-castle-court-house','New Castle Court House','New Castle','de','civic','standing',39.65972,-75.56361,'exact','open','walk','','about 1730',
  'The first court house here, where the Pennsylvania colonial assembly met in 1700 with William Penn present, was mostly destroyed in 1729 by a fire a prisoner started trying to escape, and the court house was rebuilt on the same site within a year. Its cupola was agreed in 1750 as the centre of the 12-mile circle that makes most of the Delaware–Pennsylvania border. It was Delaware\'s first capitol until 1777, and the abolitionists Thomas Garrett and John Hunn were tried and fined here under the Fugitive Slave Act.',
  'The foundation of the earlier court house is still visible, the article says. Inside: the courtroom and an exhibit on the Underground Railroad in Delaware; guided tours on the hour. A National Historic Landmark and part of First State National Historical Park.',
  'The cupola the Delaware border is drawn from.',
  'A state museum run by the Delaware Division of Historical and Cultural Affairs; free. Hours from its page (closed Monday and Tuesday; last tour 3 p.m., Sunday 3:30). Parking: a mapped lot on West Third Street about 130 m south-west, and the streets of the old town.',
  [['Delaware Historical and Cultural Affairs: New Castle Court House Museum',HCA+'/history.delaware.gov/new-castle-court-house-museum'],['National Park Service: New Castle Court House','https://www.nps.gov/frst/planyourvisit/new-castle-court-house.htm'],W('New Castle Court House Museum')],
  th=[39.65902,-75.56488],thn='Lot on West Third Street',brick='yes',hours='Wednesday to Saturday 10 a.m. to 4 p.m. (tours on the hour); Sunday tours 1:30, 2:30 and 3:30 p.m.; free'),

N('old-state-house-dover','Old State House','Dover','de','civic','standing',39.15639,-75.52306,'exact','open','walk','','1787–1792',
  'Built between 1787 and 1792 on The Green at Dover, it was the only seat of the state government from 1792 to 1932 and the Kent County court house until 1873. It was remodelled in a Victorian style in 1873 and restored to its first appearance in 1976.',
  'A two-storey, five-bay brick building laid in Flemish bond on the front, with a fanlight, a Palladian window and an octagonal cupola; wings were added from 1836 to 1926. Inside are the old Senate chamber and the original courtroom (pictures in the article). A free museum with guided tours.',
  'Delaware\'s capitol for 140 years.',
  'A state museum run by the Division of Historical and Cultural Affairs; free. Hours from its page; Wikipedia gives older ones (Monday to Saturday). Free but limited street parking round the Green, and a mapped lot on East North Street about 150 m north-west.',
  [['Delaware Historical and Cultural Affairs: Old State House',HCA+'/old-state-house/'],W('Old State House (Dover, Delaware)')],
  th=[39.1576,-75.52375],thn='Lot on East North Street',brick='yes',hours='Wednesday to Saturday 10 a.m. to 4 p.m.; guided tours at 10, 11, 1, 2 and 3; free'),

N('john-dickinson-plantation','John Dickinson Plantation (Poplar Hall)','Dover','de','landmark','standing',39.10278,-75.44944,'site','open','drive','','1739–40',
  'Judge Samuel Dickinson built the house in 1739 and 1740 on a 13,000-acre plantation; wings followed in 1752 and 1754. It was the boyhood home of John Dickinson, the "Penman of the Revolution" and a drafter of the Articles of Confederation. A British raid in August 1781 badly damaged it and a fire nearly destroyed it in 1804. The state owns it and runs it as a museum that tells the stories of the tenant farmers, servants and enslaved people who worked there as well.',
  'An Early Georgian brick mansion facing a bend of the St. Jones River that has since been straightened. Mansion tours Thursday to Saturday (10:30, 11:30, 1:30, 2:30 and later; the page was cut there). A National Historic Landmark and part of First State National Historical Park.',
  'The farm of the man who wrote "Letters from a Farmer in Pennsylvania".',
  'Owned by the State of Delaware and run by the Division of Historical and Cultural Affairs; free. Free parking at the visitor centre on Kitts Hummock Road, 5 miles south of Dover. The page lists closed days (November 3 and 26, 2026).',
  [['Delaware Historical and Cultural Affairs: John Dickinson Plantation',HCA+'/john-dickinson-plantation/'],W('John Dickinson House')],
  th=[39.10288,-75.44936],thn='Visitor centre lot, Kitts Hummock Road',brick='?',hours='Tuesday to Saturday 10 a.m. to 4 p.m.; mansion tours Thursday to Saturday; free'),

N('barratts-chapel-frederica','Barratt\'s Chapel','Frederica','de','worship','standing',39.02467,-75.45913,'exact','open','drive','','1780',
  'Built in 1780 on land given by Philip Barratt, it is the oldest surviving church in the country built by and for Methodists. On November 14, 1784 Thomas Coke, sent by John Wesley, met Francis Asbury here; the sacraments were given for the first time by ordained Methodist clergy, and the two planned the Christmas Conference in Baltimore that founded the Methodist Episcopal Church.',
  'The outside looks much as it did in 1784; the inside was renovated several times and dates from 1842. The walls are brick (a 1982 black-and-white survey photograph in the article; the colour was not checked). A star in the floor marks where Coke and Asbury met. A museum beside it shows furniture, books and objects of Methodism on the Delmarva Peninsula, with a reconstructed 18th-century vestry.',
  'Where American Methodism became a church.',
  'Owned by the Commission on Archives and History of the Peninsula-Delaware Conference of the United Methodist Church. Hours from the chapel\'s own page, which also offers visits by appointment; Wikipedia says Saturdays and Sundays. A mapped lot beside the chapel on Bay Road (US 113).',
  [['Barratt\'s Chapel and Museum','https://www.barrattschapel.org/'],W('Barratt\'s Chapel')],
  th=[39.02477,-75.45955],thn='Chapel lot on Bay Road',brick='?',hours='Wednesday and Saturday 10 a.m. to 2 p.m.; other times by appointment'),

N('allee-house-bombay-hook','Allee House','Dutch Neck Crossroads','de','landmark','standing',39.28475,-75.50448,'exact','view','drive','','about 1753',
  'Abraham Allee, of a Huguenot family, is thought to have built this brick farmhouse about 1753 on land his father bought in 1706 and 1711. It left the family in 1828 and was sold to the United States government in 1962; it is now on Bombay Hook National Wildlife Refuge. Volunteers once showed it on spring and fall weekends, but tours stopped when sagging floors and a damaged chimney made it unsafe.',
  'One of the best-kept early brick farmhouses in Delaware: Flemish bond with some glazed headers. Inside (not open) is the parlour panelling with arched china closets. The Friends of Bombay Hook say it is closed and waiting for money to repair it.',
  'A 1750s farmhouse alone in the refuge marshes.',
  'U.S. Fish and Wildlife Service, Bombay Hook National Wildlife Refuge: the house is closed; see it from outside. OpenStreetMap places it on Dutch Neck Road. The refuge\'s own visiting page answered 404, so refuge hours and fees were not checked. No mapped parking.',
  [['Friends of Bombay Hook: The Allee House','https://www.friendsofbombayhook.org/?p=2289'],W('Allee House (Dutch Neck Crossroads, Delaware)')],
  brick='yes'),

N('octagonal-schoolhouse-cowgills-corner','Octagonal Schoolhouse','Cowgill\'s Corner','de','civic','standing',39.19556,-75.4725,'site','view','drive','','1836',
  'Delaware made public schooling free in 1829, and this eight-sided school opened in 1836, one of the first buildings of that movement. Manlove Hayes is said to have designed it. Boys and girls sat in two circles, boys facing out and girls in. It stayed a public school well into the 20th century and was then a community meeting house. The state bought it in 1967.',
  'A one-room, one-storey stuccoed stone building under a pyramid roof of shingles with a stepped stone cornice. In 2019 the state laid a gravel lane to it and cleared the brush round it, as a first step to opening it to the public. Interior not checked.',
  'An eight-sided one-room school of 1836.',
  'Owned by the State of Delaware (Division of Historical and Cultural Affairs). No source read says it opens; look from outside. No mapped parking; the state built a gravel lane to it in 2019.',
  [['Delaware Historical and Cultural Affairs: improvements at the Octagonal Schoolhouse (2019)',HCA+'/history.delaware.gov/2019/09/24/improvements-completed-at-delawares-historic-octagonal-schoolhouse'],W('Octagonal Schoolhouse (Cowgill\'s Corner, Delaware)')],
  brick='no'),

N('abbotts-mill-milford','Abbott\'s Mill','Milford','de','industry','standing',38.88611,-75.47667,'site','public','walk','','1795',
  'A sawmill was set up here in 1795 and turned into a grist mill after 1808; it ground until 1960 and is named for Ainsworth Abbott, who bought it in 1919. The present two-and-a-half-storey mill is a later 19th-century building on what is thought to be the first mill\'s foundation. The state owns it and the Delaware Nature Society runs the nature centre round it.',
  'A wooden frame mill by Abbott\'s Pond. The state found rot and insect damage in its beams and closed it; repairs were to start in summer 2026, so mill tours are on hold. Five miles of free trails, a boardwalk and a pond trail in the Milford Millponds Nature Preserve.',
  'A working grist mill being rebuilt beam by beam.',
  'Owned by the State of Delaware and run by the Delaware Nature Society as Abbott\'s Mill Nature Center, 15411 Abbotts Pond Road. Hours from the society\'s page; the state page gives the same centre hours. The parking point is the lot the aerial shows beside the nature centre buildings, about 70 m north of the pin.',
  [['Delaware Nature Society: Abbott\'s Mill Nature Center','https://www.delawarenaturesociety.org/centers/abbotts-mill-nature-center/'],['Delaware Historical and Cultural Affairs: the restoration of Abbott\'s Mill (2026)',HCA+'/2026/07/27/the-restoration-of-abbotts-mill/'],W('Abbott\'s Mill')],
  th=[38.88671,-75.47657],thn='Nature centre lot',brick='no',hours='Grounds sunrise to sunset daily; nature centre Wednesday to Friday 9 a.m. to 4 p.m.; mill tours on hold during repairs'),

N('old-christ-church-laurel','Old Christ Church (Broad Creek Chapel)','Laurel','de','worship','standing',38.56123,-75.53733,'site','view','drive','','1771–72',
  'Robert Houston built this Church of England chapel of ease for the north of Stepney Parish, Maryland, begun in 1771; the boundary was later settled so that it fell in Delaware. It became the mother church of western Sussex County. Governor Nathaniel Mitchell is buried there. The state has called it the Chesapeake region\'s only 18th-century frame church with its original interior, and it has been put forward as a National Historic Landmark.',
  'A wooden church, now painted barn red, whose inside has never been significantly altered, electrified or plumbed: high box pews with doors and chalked family names, a pulpit on the middle of the north wall, a flattened barrel-vault ceiling and a west gallery once used by enslaved and free Black worshippers. Chipman\'s Mill pond lies across the dam.',
  'A church of 1772 with no electricity and its box pews intact.',
  'At Old Christ Church Road and Chipman\'s Pond Road near Laurel. The Old Christ Church League looks after it; who owns it and when it opens were not checked (no page of its own was found). See it from outside unless it is open. A mapped lot on Chipmans Pond Road about 290 m north-west.',
  [['Delaware Historical and Cultural Affairs: Old Christ Church (2024)',HCA+'/2024/02/15/explore-the-storied-history-of-old-christ-church/'],W('Old Christ Church (Laurel, Delaware)')],
  th=[38.56309,-75.53991],thn='Lot on Chipmans Pond Road',brick='no',hours='?'),

N('prince-georges-chapel-dagsboro','Prince George\'s Chapel','Dagsboro','de','worship','standing',38.54855,-75.23893,'exact','open','drive','','1755–57',
  'Built from 1755 as a chapel of ease for St. Martin\'s Church in Worcester Parish, Maryland, and dedicated on June 30, 1757 to Prince George, later George III. A transept and chancel added about 1763 have since been removed. The state bought it in 1967, restored it and opened it as a museum.',
  'A small shingled chapel. Inside are a vaulted heart-pine ceiling and timbered pine pillars.',
  'A Maryland chapel that the border moved into Delaware.',
  'Owned by the State of Delaware; the Friends of Prince George\'s Chapel give the tours, at 32040 Chapel Lane. The hours come from an undated state notice; the state\'s list of sites says to call (302) 732-3324 for an appointment. No mapped lot at the chapel.',
  [['Delaware Historical and Cultural Affairs: free tours of Prince George\'s Chapel',HCA+'/?p=56187'],STATE_SITES,['Town of Dagsboro: Prince George\'s Chapel','https://dagsboro.delaware.gov/prince-georges-chapel/'],W('Prince George\'s Chapel')],
  brick='no',hours='Fourth Sunday of the month, April to October, 1:30 to 4:30 p.m.; other times by appointment; free'),

N('woodland-ferry','Woodland Ferry (Cannon\'s Ferry)','Woodland','de','landmark','standing',38.6,-75.65694,'site','open','drive','','1740s',
  'James Cannon began a ferry over the Nanticoke River here in the 1740s and his family ran it until the mid-1800s, when the county took it over as a free ferry; the state highway department has run it since 1935. It is one of the oldest ferries in continuous use in the country. The slave trader Patty Cannon used the crossing to ship kidnapped free Black people and escaped slaves south.',
  'A six-car cable ferry, the Tina Fallon (2008), crossing 480 feet of the Nanticoke. The National Register listing, Cannon\'s Ferry, takes in the ferry and a house of about 1810 at the landing (Cannon Hall in the Historic American Buildings Survey). Riding it is free.',
  'One of the oldest working ferries in America.',
  'Owned and run by DelDOT; no fee. Hours as DelDOT\'s page gives them; it also posts closures, so check before going. Woodland Ferry Road on both banks; no mapped parking at the landing.',
  [['DelDOT: Woodland Ferry','https://deldot.gov/Programs/woodland_ferry/index.shtml'],W('Woodland Ferry')],
  brick='?',hours='Monday to Friday 7 a.m. to 4 p.m., not 11 a.m. to noon or Thursday mornings; no weekend service'),

N('fenwick-island-lighthouse','Fenwick Island Lighthouse','Fenwick Island','de','light','standing',38.45136,-75.05495,'exact','open','drive','','1858',
  'Finished on December 29, 1858 and first lit on August 1, 1859, on the Delaware–Maryland line, it is the oldest lighthouse in Delaware. It was automated in 1940 and put out in 1978; a public campaign had it handed to the state, and it was lit again in 1982 and restored in 1997 and 1998.',
  'An 87-foot brick tower, painted white (2008 photograph in the article), with a cast-iron spiral stair, beside a white frame keeper\'s house, now among houses and shops. The base holds a small museum and shop; the tower is not open for climbing.',
  'Delaware\'s oldest lighthouse, on the state line.',
  'Owned by the State of Delaware and kept by the New Friends of the Fenwick Island Lighthouse; closed on rainy days. The state lists the address as 146th Street, Ocean City, Maryland. Mapped lots on Tunnel Avenue and Lighthouse Avenue, about 130 m away.',
  [['Fenwick Island Lighthouse: visiting hours 2026','https://fenwickislandlighthouse.org/summer-2018/'],STATE_SITES,W('Fenwick Island Light')],
  th=[38.45005,-75.05502],thn='Lot on Lighthouse Avenue',brick='no',hours='July and August Thursday to Monday 9 a.m. to 1 p.m.; June and September Friday to Sunday, April, May and October weekends 9 to noon; closed November to March'),

N('indian-river-life-saving-station','Indian River Life-Saving Station','Rehoboth Beach','de','landmark','standing',38.63353,-75.06688,'exact','open','drive','','1880',
  'The Life-Saving Service set up this station between Bethany Beach and Rehoboth Beach in 1880 to rescue shipwrecked sailors. It became a Coast Guard station in 1915 and was used until the Ash Wednesday Storm of 1962 half buried it in sand. It was moved back from the eroding shore, restored, and is now a state park museum.',
  'A board-and-batten frame station house of the 1874 design with bracketed eaves and double doors for the surfboat; the barn, stables and other outbuildings are gone.',
  'A life-saving station half buried by the 1962 storm.',
  'Delaware Seashore State Park. Hours from the park page (last admission 30 minutes before closing). A mapped lot on the Coastal Highway (Route 1) about 60 m north-west of the station.',
  [['Delaware State Parks: Indian River Life-Saving Station','https://destateparks.com/Centers/IRLifeSavingStation'],W('Indian River Life-Saving Station')],
  th=[38.63432,-75.0671],thn='Lot on the Coastal Highway',brick='no',hours='Jun–Sep Mon–Sat 8–4, Sun 8–3; Apr–May Mon–Sat 9–4, Sun 9–3; Mar and Oct Tue–Sat 9–4; Nov–Feb Wed–Sat 9–4'),

N('lightship-overfalls-lewes','Lightship Overfalls (LV-118)','Lewes','de','light','standing',38.77792,-75.14111,'exact','open','walk','','1938',
  'The last lightship built for the U.S. Lighthouse Service, made to replace one wrecked in the 1938 hurricane, and the last with a riveted hull. Renumbered WAL 539 under the Coast Guard, she stayed on station through the Second World War. A storm in December 1970 damaged her and she was retired in 1972, given to the Lewes Historical Society and painted for the Overfalls station, where she never served.',
  'A museum ship on the canal at Lewes, shown by tour. A National Historic Landmark.',
  'A lightship painted for a station she never served.',
  'The Overfalls Maritime Museum Foundation; season and days from its page, plus Veterans Day and the first Saturday of December. A mapped lot beside the ship.',
  [['Overfalls Maritime Museum Foundation','https://overfalls.org/'],W('United States lightship Overfalls (LV-118)')],
  th=[38.77796,-75.14149],thn='Lightship lot',brick='no',hours='10 a.m. to 3:30 p.m.: Thursday to Sunday from Lewes Maritime Day to Labor Day weekend, then Friday to Sunday to mid-October'),

N('delaware-breakwater-east-end-light','Delaware Breakwater East End Light','Lewes','de','light','standing',38.79724,-75.10002,'exact','boat','boat','','1885',
  'Built in 1885 on the east end of the inner Delaware Breakwater to replace the failing Cape Henlopen beacon, with a fourth-order Fresnel lens and a red sector for the Hen and Chickens Shoal. It was automated in 1950 and discontinued in 1996, and passed to the state in 1999.',
  'An iron tower about 56 feet high on the stone breakwater; the Fresnel lens is still in it. Seen across the water from Cape Henlopen State Park.',
  'A lighthouse on a breakwater you can only reach by boat.',
  'Owned by the State of Delaware and leased to the Delaware River and Bay Authority. The state says access is forbidden except on visits with Cape Water Tours; the lighthouse foundation\'s page says the same. The nearest mapped lot in Cape Henlopen State Park is about 740 m east (park fees not checked).',
  [STATE_SITES,['Delaware River and Bay Lighthouse Foundation','https://delawarebaylights.org/'],W('Delaware Breakwater East End Light')],
  th=[38.79516,-75.09186],thn='Point parking, Cape Henlopen State Park',brick='no'),

N('old-sussex-county-courthouse','Old Sussex County Courthouse','Georgetown','de','civic','standing',38.68931,-75.38526,'exact','open','walk','','1793',
  'Built in 1793 on The Circle at Georgetown, the new county seat, it was moved to its present lot in 1837 and made into a house when the present court house took its place. The state got it in 1962 and renovated it in 1974 and again in 2016.',
  'A two-storey, five-bay late Georgian frame building sheathed in cypress shingles. The 2016 work restored the outside and refurbished both floors inside.',
  'Sussex County\'s first court house, moved round the corner.',
  'Owned by the State of Delaware and leased to the Georgetown Historical Society, which opens it at times through the year. The state\'s list of sites says to call (302) 855-9660 for hours; no hours page was found. 10 South Bedford Street; a mapped lot on Strawberry Alley about 80 m south.',
  [STATE_SITES,['Delaware Historical and Cultural Affairs: restoration of the Old Sussex County Court House (2016)',HCA+'/2016/11/22/restoration-work-completed-at-old-sussex-county-court-house/'],W('Old Sussex County Courthouse')],
  th=[38.68905,-75.38542],thn='Lot on Strawberry Alley',brick='no',hours='?'),

N('zwaanendael-museum-lewes','Zwaanendael Museum','Lewes','de','civic','standing',38.77473,-75.13912,'exact','open','walk','','1931–32',
  'Built for the 300th anniversary of Zwaanendael, the Dutch settlement of 1631 that was Delaware\'s first, and finished in 1932 to designs by E. William Martin after the Statenlogement in Hoorn. It holds the history of Delaware\'s south-east coast: the wreck of HMS DeBraak, the Cape Henlopen lighthouse, the British bombardment of Lewes in 1812 and the Delaware River pilots.',
  'A copy of a Dutch town building in red brick with stone dressings (photograph in the article): stepped gable, terracotta roof tiles, carved stone and painted shutters, with a statue of David Pietersen de Vries on top. A free state museum.',
  'A Dutch town hall in a Delaware beach town.',
  'A state museum run by the Division of Historical and Cultural Affairs; free. Hours from its page. Street parking in downtown Lewes; a mapped lot on West 3rd Street beside it.',
  [['Delaware Historical and Cultural Affairs: Zwaanendael Museum',HCA+'/zwaanendael-museum/'],W('Zwaanendael Museum')],
  th=[38.77481,-75.13974],thn='Lot on West 3rd Street',brick='yes',hours='Wednesday to Saturday 10 a.m. to 4:15 p.m.; free'),
]

PIN_NOTES={
 'old-swedes-church-wilmington':'Wikipedia coordinate; checked on the aerial.',
 'fort-christina-wilmington':'Wikipedia coordinate for the park; area pin.',
 'new-castle-court-house':'Wikipedia coordinate; checked on the aerial.',
 'old-state-house-dover':'Wikipedia coordinate; checked on the aerial.',
 'john-dickinson-plantation':'Wikipedia coordinate, on the visitor centre lot; the mansion is near by but was not picked out on the aerial.',
 'barratts-chapel-frederica':'Wikipedia coordinate, which fell on the parking lot. The sample check of November 21, 2026 moved it 36 m east (tools/pix.py) onto the squarish building that stands against the cemetery on the Esri aerial, taken to be the chapel; the longer buildings north of it are taken to be the museum. Not confirmed from a second source.',
 'allee-house-bombay-hook':'OpenStreetMap building (historic=building, Allee House); checked on the aerial.',
 'octagonal-schoolhouse-cowgills-corner':'Register list coordinate, in trees by the gravel lane; the octagonal building itself could not be made out on the aerial, so site precision.',
 'abbotts-mill-milford':'Register list coordinate, at the road crossing below the pond dam where the mill stands; the parking point was read off the aerial with pix.py (a lot by the nature centre buildings), not the mapped lot 1 km west, which is a track across a field.',
 'old-christ-church-laurel':'Register list coordinate fell on Chipmans Pond Road; moved 41 m with pix.py onto the building by the junction on the aerial, taken to be the church (not confirmed from a picture).',
 'prince-georges-chapel-dagsboro':'OpenStreetMap place of worship (Prince George\'s Chapel, Ward Lane); checked on the aerial.',
 'woodland-ferry':'Register list coordinate for Cannon\'s Ferry, in the river beside the west landing pier on the aerial.',
 'fenwick-island-lighthouse':'OpenStreetMap lighthouse; checked on the aerial.',
 'indian-river-life-saving-station':'Register list coordinate fell on the highway; moved 54 m east with pix.py onto the red-roofed station house on the aerial.',
 'lightship-overfalls-lewes':'Wikipedia coordinate; checked on the aerial.',
 'delaware-breakwater-east-end-light':'Coordinate given on the state\'s historic sites page; checked on the aerial.',
 'old-sussex-county-courthouse':'OpenStreetMap courthouse (10 South Bedford Street); checked on the aerial.',
 'zwaanendael-museum-lewes':'Wikipedia coordinate; checked on the aerial.',
}
