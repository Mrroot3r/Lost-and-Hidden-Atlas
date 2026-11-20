# November 20, 2026: central and eastern Suffolk County, Long Island: the Town of Riverhead (Riverhead, Jamesport,
# Northville, Flanders), western Southampton (Hampton Bays, Quogue) and eastern Brookhaven (Yaphank, Ridge, Coram,
# Shoreham, Rocky Point, Mastic Beach, Center Moriches). Region drawn at random by tools/choose.py --state ny (nyc,
# which offered Riverhead); tools/start.py showed no Atlas place within 25 km of Riverhead.
# Sources read in this session: Wikipedia articles and the Register lists for the towns of Riverhead, Southampton and
# Brookhaven (tools/wiki_raw.py), and the pages of the bodies that run the places (Suffolk County Parks, the National
# Park Service, NYS DEC, Cornell Cooperative Extension, the Suffolk County Historical Society, Hallockville, the Jamesport
# Meeting House, the Ketcham Inn Foundation, the Yaphank Historical Society), HMdb and the Pomeroy Foundation's marker
# pages, and local news reports, all read with tools/page.py. Interiors were not visited by any source opened unless the
# entry says so.
from data_b import N
from data_ma import W
BATCH={'key':'nyc_efce','label':'Long Island: Riverhead, the Pine Barrens and the Moriches','added':'2026-11-20 11:40'}

WP=W
TOWN='Street parking or the public lots in town; parking was not checked on the ground.'

PLACES=[
N('big-duck-flanders','The Big Duck','Flanders','nyc','landmark','standing',40.90719,-72.62239,'exact','open','drive','','1931',
  'A 20-foot duck-shaped shop built in 1931 by the duck farmer Martin Maurer to sell ducks and eggs, the building that gave architects the word "duck" for a building shaped like what it sells. Maurer moved it to his Flanders ranch in 1937; Suffolk County later took it to Sears Bellows County Park as a gift shop, and it came back to its 1937 spot on the old Big Duck Ranch in October 2007. The Duck was put on the National Register in 1997 and the ranch in 2008.',
  'The ferrocement duck itself, white with an orange bill, standing beside Flanders Road on the ranch land; Wikipedia gives it as 20 feet tall to the top of the head. The inside is a small gift shop run as the visitor centre. The county lights it up each year in early December.',
  'The building that named a whole kind of roadside architecture.',
  'Suffolk County Parks runs the Duck and its visitor centre gift shop; the county\'s monthly notices say the park land round it is open dawn to dusk and the shop\'s days change month by month (in August 2024 it was open 10 a.m. to 5 p.m.), so call 631-852-3232 before going (Suffolk County Parks notices for April and August). A mapped lot on Flanders Road sits beside it.',
  [WP('Big Duck'),['Suffolk County Parks: Big Duck hours (August)','https://suffolkcountyny.gov/Departments/Parks/News/ArtMID/7824/ArticleID/12208/The-Big-Duck-August-Hours-of-Operation'],['Suffolk County Parks: Big Duck hours (April)','https://suffolkcountyny.gov/Departments/Parks/News/ArtMID/7824/ArticleID/13155/The-Big-Duck-April-Hours-of-Operation']],
  th=[40.9073,-72.62248],thn='Lot on Flanders Road beside the Duck',brick='no',hours='Grounds dawn to dusk; the gift shop inside changes its days monthly (10 a.m. to 5 p.m. in August 2024): call 631-852-3232'),

N('vail-leavitt-music-hall-riverhead','Vail-Leavitt Music Hall','Riverhead','nyc','civic','standing',40.91639,-72.6625,'site','view','walk','','1881',
  'A small upstairs opera house built in 1881 by the lumber dealer David F. Vail and his son George, designed by J. W. Flack, with shops on the ground floor. It ran on gas light until electricity reached Riverhead in 1888, and in 1914 Thomas Edison used it to show his kinetophone, an early try at sound film. Later it served as a restaurant, a roller rink and a betting parlour. The Town of Riverhead sold it in March 2026 for $150,000 to The Jazz Loft, which says it will restore it.',
  'Wikipedia says the horseshoe balcony and the stage proscenium survived all the conversions. News 12 calls it Long Island\'s oldest theatre. Interior not checked; it was changing hands for restoration when last reported.',
  '',
  'Owned since March 2026 by The Jazz Loft (News 12). Whether it holds performances during the restoration was not checked, so it is marked view only. In downtown Riverhead, a block off Main Street. '+TOWN,
  [WP('Vail-Leavitt Music Hall'),['News 12: The Jazz Loft purchases Vail-Leavitt Music Hall (March 2026)','https://longisland.news12.com/2026/03/18/the-jazz-loft-purchases-vail-leavitt-music-hall/DdvyGAZFULuFUcflvyGyJ']],brick='?'),

N('suffolk-county-historical-society-riverhead','Suffolk County Historical Society Museum','Riverhead','nyc','civic','standing',40.91816,-72.6681,'exact','open','walk','','1930',
  'The county historical society, founded in 1886 with Riverhead\'s Surrogate Judge James H. Tuthill as its first president, kept its first finds in a glass case in his office. Its own Colonial Revival building at West Main Street and Court Street, designed by August Galow on land given by Alice O. Perkins, opened in 1930, with wings added in 1951 and 1964.',
  'A red brick building with a pediment over the arched doorway, a balustrade and dormers (photograph on Wikipedia). A museum and research library. Wikipedia lists Native American artifacts, farm tools, whaling gear, furniture, Civil War arms and a transport hall with horse-drawn wagons, sleighs and a 1905 Curved Dash Oldsmobile; the society\'s own page names the Hulbert Flag, which some believe was carried from Fort Ticonderoga to Philadelphia in 1775.',
  '',
  'Run by the Suffolk County Historical Society at 300 West Main Street. Its page (read November 2026) gives only a holiday notice: closed November 26 to 28, 2026, reopening Wednesday, December 2, at 10 a.m.; the full weekly hours were not on the page read. Mapped lots on Railroad Avenue and Osborn Avenue are close by.',
  [WP('Suffolk County Historical Society Building'),['Suffolk County Historical Society','https://suffolkcountyhistoricalsociety.org/']],
  th=[40.91903,-72.66763],thn='Lot off Railroad Avenue',brick='yes',hours='Opens Wednesdays from 10 a.m. (full weekly hours not on its page); closed Thanksgiving week'),

N('hallockville-museum-farm-northville','Hallockville Museum Farm (Hallock Homestead)','Northville','nyc','landmark','standing',40.98288,-72.59122,'site','open','drive','','1765',
  'The Hallock family farm on Sound Avenue, now a museum farm. The farmhouse began in 1765 as a one-storey, five-bay house with a central chimney; a room was added in 1833, and in 1845 it was raised to two storeys under a broad gable roof. The Register listing of 1984 counts the house, barn, milk house, shop and woodhouse, and privy.',
  'The 1765 farmhouse and its barn and outbuildings. The museum says it offers house tours, classes, fairs and a farmers market; its country fair is in early autumn. Interior not checked.',
  '',
  'Hallockville Museum Farm, a not-for-profit, at 6038 Sound Avenue (631-298-5292). Its home page (read November 2026) lists events and markets with times but no regular opening hours; call or check its calendar.',
  [WP('Hallock Homestead'),['Hallockville Museum Farm','https://hallockville.com/']],brick='?',hours='?'),

N('jamesport-meeting-house','Jamesport Meeting House','Jamesport','nyc','worship','standing',40.95008,-72.58094,'exact','view','drive','','1731',
  'A meeting house built by Puritan settlers in 1731, which its trust calls the oldest public building on the East End. When two Congregational parishes merged it was put up for sale, and in 2008 local people bought it to save it. It is now a not-for-profit hall for concerts, plays, lectures, civic meetings and weddings.',
  'A two-storey gable-fronted building with a wing to the east and an open bell tower under a two-tiered mansard cap (Wikipedia). The trust says it has been restored and that restoration continues. Interior not checked; the way in is to go to one of its events.',
  '',
  'Owned by the Jamesport Meeting House Preservation Trust, 1590 Main Road at the corner of Manor Lane. It opens for its own events (listed on its calendar), not at set hours. Parking was not checked.',
  [WP('Jamesport Meeting House'),['Jamesport Meeting House','https://jamesportmeetinghouse.org/']],brick='?'),

N('marconi-building-radio-central-rocky-point','Marconi station building and Radio Central','Rocky Point','nyc','landmark','standing',40.93837,-72.94038,'site','view','drive','','1902',
  'The little building that housed Marconi\'s spark-gap transmitter at his ship-to-shore station and school in Babylon from 1902. In 1930 the radio pioneer Edwin Armstrong bought it and gave it to RCA\'s Radio Central at Rocky Point, the transmitting station that President Harding switched on on November 5, 1921 and that DEC calls the world\'s largest, with towers 450 feet tall. Radio Central closed in 1978; its land is now DEC\'s Rocky Point Pine Barrens State Forest, and the Marconi building passed to the Rocky Point school district.',
  'The Marconi building, kept up by the Rocky Point Historical Society, with an HMdb-listed marker beside it on Rocky Point-Yaphank Road; the radio club opens it in April and October. A DEC interpretive sign of 2021 marks the station inside the state forest, but where in the forest it stands, and what is left of the tower bases, was not checked: the Maritime Radio Historical Society says the station was bulldozed and the towers dynamited, with some remains still to be seen.',
  '',
  'The building is on Rocky Point school district land (HMdb marker, 90 Rocky Point-Yaphank Road): look from the road. The state forest needs DEC\'s free three-year Managed Land Access Permit for every visitor, and its trails close during January shotgun season; lots are on Route 25A, Rocky Point Road (bikes) and Whiskey Road (DEC page).',
  [['HMdb: Marconi','https://www.hmdb.org/m.asp?m=174035'],['NYS DEC: Rocky Point Pine Barrens State Forest','https://dec.ny.gov/places/rocky-point-pine-barrens-state-forest'],['NYS DEC: Radio Central sign unveiled (2021)','https://dec.ny.gov/news/press-releases/2021/9/rocky-point-historical-society-and-suffolk-county-commemorate-historic-role-of-decs-rocky-point-pine-barrens'],['Maritime Radio Historical Society: Rocky Point','https://radiomarine.org/radio-archaeology/rocky-point']],conf='mixed',brick='?'),

N('wardenclyffe-tesla-laboratory-shoreham','Wardenclyffe, Tesla\'s laboratory','Shoreham','nyc','industry','standing',40.9484,-72.89825,'site','view','drive','','1901–1917',
  'Nikola Tesla\'s wireless station, begun in 1901 with J. P. Morgan\'s money to send messages and power across the Atlantic. Morgan would not pay for the larger scheme, the work stopped in 1906, and the tower was dynamited for scrap in 1917. The brick laboratory by Stanford White survived 50 years as a photographic works; the Tesla Science Center bought the site in 2013 after a crowdfunding drive. A fire in November 2023 burned through the laboratory\'s roof and its later steel girders, and a new visitor centre was dedicated in July 2026.',
  'The red brick laboratory with its tall brick chimney and arched windows (a 2024 photograph on Wikimedia Commons shows its burned roof), damaged by the 2023 fire and under restoration, and the new Eugene Sayan Visitor Center, which the Riverhead News-Review says will hold historical tours. The tower is gone. Interior not checked.',
  'The last of Tesla\'s laboratories, after the fire.',
  'Owned by the Tesla Science Center at Wardenclyffe, a nonprofit. Its tours page answered 403, so tour days and times were not checked; look from the road until you have booked. A mapped lot on George Avenue is about 370 m away and was not checked.',
  [WP('Wardenclyffe Tower'),WP('Tesla Science Center at Wardenclyffe'),['Riverhead News-Review: new visitor center after the fire (July 2026)','https://riverheadnewsreview.timesreview.com/2026/07/135352/tesla-science-center-to-dedicate-new-visitor-center-after-wardenclyffe-fire/']],brick='yes'),

N('longwood-estate-ridge','Longwood Estate (Smith Estate)','Ridge','nyc','landmark','standing',40.86751,-72.90602,'area','view','drive','','c. 1790',
  'Part of the manor that William "Tangier" Smith was granted in 1693. The house was built about 1790 and enlarged in the 19th century; the Smiths kept the estate until 1968, leasing much of it to tenant farmers, and the Town of Brookhaven has owned it since 1974.',
  'The main house, a caretaker\'s cottage, barns and sheds from the late 1700s to the early 1900s, the Smith family cemetery and a small schoolhouse moved here in 1977 (Wikipedia and the Pine Barrens Commission). Interior not checked.',
  '',
  'Owned by the Town of Brookhaven (Pomeroy Foundation marker page), on Longwood Road at Smith Road. The town\'s own page for it was not found, so opening times were not checked; the Brookhaven Country Fair is held on the grounds in September.',
  [WP('Smith Estate (Ridge, New York)'),['Pomeroy Foundation: Longwood Estate marker','https://www.wgpfoundation.org/historic-markers/longwood-estate/'],['Central Pine Barrens Commission: cultural and historic resources','https://pb.state.ny.us/central-pine-barrens/cultural-and-historic-resources/']],brick='?'),

N('william-floyd-estate-mastic-beach','William Floyd Estate (Old Mastic House)','Mastic Beach','nyc','landmark','standing',40.77372,-72.82979,'site','open','walk','','1718–',
  'The Floyd family seat: by 1718 they held 4,400 acres here, and Nicoll Floyd built the Old Mastic House and ran it as a northern plantation. It passed to his son William Floyd, a signer of the Declaration of Independence, and to later generations, who made it a summer home and gave it to the National Park Service in 1975.',
  'The Old Mastic House with its exhibit, twelve outbuildings, the family cemetery and trails through 613 acres of fields and woods on the Great South Bay.',
  'A signer\'s family seat, kept for 250 years.',
  'National Park Service (Fire Island National Seashore), 245 Park Drive. Grounds April 1 to November 30, 9 a.m. to 4:30 p.m., closed December to March; the house exhibit was open May 2 to September 27, 2026, Wednesday to Sunday 9 a.m. to 4:30 p.m.: check in at the front porch for an entry time (NPS page). Parking on site.',
  [WP('William Floyd House'),['NPS: William Floyd Estate','https://www.nps.gov/fiis/planyourvisit/williamfloydestate.htm']],
  th=[40.77254,-72.83136],thn='Estate parking lot',brick='?',hours='Grounds Apr 1 to Nov 30, 9 a.m. to 4:30 p.m.; house May to late Sep (2026: May 2 to Sep 27), Wed to Sun 9 a.m. to 4:30 p.m.'),

N('terry-ketcham-inn-center-moriches','Terry-Ketcham Inn','Center Moriches','nyc','hotel','standing',40.80233,-72.78075,'exact','view','drive','','1693',
  'An inn and tavern on the old King\'s Highway. The blacksmith Samuel Terrell put up a one-room timber frame here in 1693 (now called the Summer Kitchen); a half-house followed about 1710, and a building programme in 1790 tripled it. The Ketcham Inn Foundation says Jefferson and Madison stayed in 1791 on their way to William Floyd, and that the Ketchams ran it until 1914. Neglected and damaged by fire in 1989, it was taken on by the foundation that year and has been under restoration since.',
  'A long two-storey, nine-bay frame building with a rear wing, a state historic marker at the southeast corner and an 1850s hay barn behind, where the foundation sells used books and records (Wikipedia). Interior not checked.',
  '',
  'Owned by the Ketcham Inn Foundation at 81 Main Street; Wikipedia says the state parks office protects it. No regular opening hours were found on the foundation\'s page, which lists events; view from Main Street otherwise. Parking was not checked.',
  [WP('Terry-Ketcham Inn'),['Ketcham Inn Foundation: Ketcham Inn','https://ketchaminnfoundation.org/ketcham-inn/']],brick='?'),

N('homan-gerard-house-mills-yaphank','Homan-Gerard House and Mills','Yaphank','nyc','industry','standing',40.835833,-72.915833,'area','view','drive','','1762',
  'A mill owner\'s house beside the Carmans River in Yaphank, a hamlet once called Millville for its water mills. The Brookhaven town records first note the place in 1762, when a sawmill was built on the river; the Homans added a gristmill, and Daniel Homan Jr. remodelled the house in the Federal style about 1790. Long abandoned, it was stabilised by Suffolk County from 2012 and restored by the Yaphank Historical Society and the county, finished in 2019.',
  'The gambrel-roofed house with its central chimney, attic quadrant windows that were never glazed, a late 19th-century barn and three sheds. The mills are gone above ground; Wikipedia says surveys have mapped their footprints and races along the river. The society interprets the house as it was in 1825. Interior not checked.',
  '',
  'Restored by the Yaphank Historical Society and Suffolk County Parks; the society opens it on its own tour days (Suffolk County listed holiday tours of it in December 2024, 1 to 4 p.m., for a donation). No regular hours were found. Pin is the Register point, near the house and pond, not on the house.',
  [WP('Homan-Gerard House and Mills'),['Yaphank Historical Society: Homan-Gerard House','https://yaphankhistorical.org/?p=2112'],['Suffolk County: Yaphank Historic House Tours (2024)','https://suffolkcountyny.gov/News/ArtMID/583/ArticleID/12625/evr/1/Yaphank-Historic-House-Tours']],brick='?'),

N('suffolk-county-almshouse-barn-yaphank','Suffolk County Almshouse Barn (Suffolk County Farm)','Yaphank','nyc','inst','standing',40.828056,-72.921667,'site','open','walk','','1871',
  'In 1870 Suffolk County bought 170 acres to build an almshouse for the needy and infirm, whose residents had to work its farm. The great hay barn of 1871 is the only building of the almshouse left. Later county inmates worked the farm; since 1974 Cornell Cooperative Extension has run it as an educational farm.',
  'The multi-storey shingled barn with its broad gable roof, which the farm says is still used for its first job of storing hay and straw, in the middle of a working farm with animals.',
  '',
  'Suffolk County Farm and Education Center, run by Cornell Cooperative Extension of Suffolk County; its page says it is open to the public seven days a week, 9 a.m. to 3 p.m., except Memorial Day, July 4, Labor Day, November 27 and 28 and December 25. Parking was not checked.',
  [WP('Suffolk County Almshouse Barn'),['Cornell Cooperative Extension: Suffolk County Farm, about','https://ccesuffolk.org/suffolk-county-farm/about'],['Cornell Cooperative Extension: Suffolk County Farm','https://ccesuffolk.org/suffolk-county-farm']],brick='?',hours='Daily 9 a.m. to 3 p.m.; closed Memorial Day, July 4, Labor Day, Thanksgiving and the day after, and Christmas'),

N('st-andrews-church-yaphank','St. Andrew\'s Episcopal Church','Yaphank','nyc','worship','standing',40.83677,-72.91483,'site','view','drive','','1853',
  'A Carpenter Gothic church of 1853 on East Main Street, on land once owned by James Huggins Weeks, a Yaphank man who was president of the Long Island Rail Road from 1847 to 1850. It was built to look like Old Grace Church in Massapequa.',
  'Wikipedia says that apart from an extension on the east side it is largely unchanged since 1853. Interior not checked.',
  '',
  'An Episcopal church; service times were not checked. View from East Main Street. Parking was not checked.',
  [WP('St. Andrew\'s Episcopal Church (Yaphank, New York)')],brick='?'),

N('shinnecock-canal-lock-hampton-bays','Shinnecock Canal and lock','Hampton Bays','nyc','canal','standing',40.8875,-72.50139,'area','public','walk','','1892',
  'A 4,700-foot canal across the South Fork at Canoe Place, where Native people once carried their canoes between Shinnecock Bay and Peconic Bay. The canal opened in 1892; tide gates were begun in 1918 to tame the three-foot difference in tides between the bays. Its lock, 41 feet wide and 250 feet long, is the only working navigation lock on Long Island.',
  'The lock and tide gates, with the Montauk Highway, Sunrise Highway and Long Island Rail Road bridges over the canal. Suffolk County runs the lock: a gate hinge failed in September 2024 and the county discouraged boat traffic while it was repaired (East Hampton Star).',
  '',
  'Suffolk County operates the lock. A mapped lot off Holzman Lane is inside Shinnecock Canal Park on the federal public-land map, and another serves the Shinnecock Canal County Marina on Canal Road; neither was checked on the ground. Pin is the Wikipedia point for the canal, not the lock.',
  [WP('Shinnecock Canal'),['East Hampton Star: equipment failure at the Shinnecock Canal (2024)','https://www.easthamptonstar.com/villages/2024913/equipment-failure-impacts-boat-traffic-through-shinnecock-canal']],
  th=[40.88655,-72.50206],thn='Shinnecock Canal Park lot, Holzman Lane',brick='?'),

N('quogue-life-saving-station','Quogue Life-Saving Station','Quogue','nyc','landmark','standing',40.8075,-72.59937,'exact','view','drive','','1912',
  'A shingle-style station built in 1912 by the U.S. Life-Saving Service, designed by Victor Mendelheff, replacing earlier stations on this beach (the first of 1849, then a red house of 1872 that was moved a few hundred yards east). Crews from here helped the Infanti in 1851, the Europa in 1886, the Nahum Chapin in 1897 and the Augustus Hunt in 1904. It became a Coast Guard station in 1915 and is now a private house.',
  'The gable-roofed station with its four-storey shingled lookout tower with a hipped roof, which Wikipedia calls one of the few left of its type.',
  '',
  'A private residence: look from Dune Road. Parking was not checked.',
  [WP('Quogue Life-Saving Station')],brick='?'),

N('davis-town-meeting-house-coram','Davis Town Meeting House','Coram','nyc','civic','standing',40.87153,-72.99544,'exact','view','drive','','c. 1750',
  'A house built about 1750, probably by Elijah Davis, that served as the Town of Brookhaven\'s meeting place: from about 1800 the annual April town meeting was held here more than 80 times, until 1885, when the town was split into election districts. Davis descendants owned it almost continuously until the early 2000s. Repairs begun in 2009 ended with a grand reopening on April 13, 2024.',
  'The restored house and its election room, where the town\'s ballots were counted (The Messenger). Interior not checked.',
  'Brookhaven\'s town hall for 85 years was somebody\'s front room.',
  'Kept by the Davis Town Meeting House Society at 263 Middle Country Road, at the corner of Coram-Mount Sinai Road. It opens for tours on set days (Longwood Public Library ran one on July 20, 2024); no regular hours were found. Parking was not checked.',
  [WP('Davis Town Meeting House'),['The Messenger: Historic Davis House reopens (2024)','https://messengerpapers.com/2024/04/historic-davis-house-reopens-after-years-long-renovations/'],['Longwood Public Library: Davis Town Meeting House tour','https://longwoodlibrary.org/event/lester-h-davis-town-meeting-house-tour-136471']],brick='?'),
]

PIN_NOTES={
 'big-duck-flanders':'Wikipedia coordinate; the geocoder put 1012 Flanders Road within 5 m of it.',
 'vail-leavitt-music-hall-riverhead':'Wikipedia and Register list coordinate; the street address was not taken from a source, so the pin is left at that point.',
 'suffolk-county-historical-society-riverhead':'ArcGIS PointAddress for 300 West Main Street, Riverhead.',
 'hallockville-museum-farm-northville':'ArcGIS PointAddress for 6038 Sound Avenue, the museum\'s address; the Register point for the homestead is about 450 m northeast.',
 'jamesport-meeting-house':'ArcGIS PointAddress for 1590 Main Road, Jamesport; Wikipedia\'s point is within 20 m.',
 'marconi-building-radio-central-rocky-point':'HMdb marker position for the Marconi marker (40 56.302 N, 72 56.423 W); the station site in the state forest is not pinned.',
 'wardenclyffe-tesla-laboratory-shoreham':'Wikipedia coordinate for the Tesla Science Center at Wardenclyffe.',
 'longwood-estate-ridge':'OpenStreetMap point for the Longwood Estate park (nom.py), inside Smith Estate Park on the public-land map; on the aerial it falls among trees by a clearing, with buildings to the north, so it marks the grounds, not the house. The Pomeroy marker and the Register point are 1 km apart.',
 'william-floyd-estate-mastic-beach':'ArcGIS PointAddress for 245 Park Drive, Mastic Beach (the address on the NPS page).',
 'terry-ketcham-inn-center-moriches':'ArcGIS PointAddress for 81 Main Street, Center Moriches.',
 'homan-gerard-house-mills-yaphank':'Register list coordinate; on the aerial it falls in trees east of the road beside the Carmans River pond, with houses just west, so it marks the site, not the house. The Pomeroy marker page gives a point 5 km south and was not used.',
 'suffolk-county-almshouse-barn-yaphank':'Register list coordinate for the barn; on the aerial it falls on a long building in the middle of the farm, which could not be told apart from the other barns there.',
 'st-andrews-church-yaphank':'ArcGIS point of interest "Saint Andrews Church", about 40 m east of the Wikipedia point, which fell in trees on the aerial; the church itself could not be made out under the trees, so the pin is near it, not on it.',
 'shinnecock-canal-lock-hampton-bays':'Wikipedia coordinate for the canal; on the aerial it falls on the railroad bridge over the canal, not on the lock.',
 'quogue-life-saving-station':'OpenStreetMap point for the station (nom.py), 78 Dune Road.',
 'davis-town-meeting-house-coram':'ArcGIS PointAddress for 263 Middle Country Road; Wikipedia\'s point is 1.5 km northeast, and the library page puts the house at the corner of Coram-Mount Sinai Road, which the geocoder places 60 m from this pin.',
}
