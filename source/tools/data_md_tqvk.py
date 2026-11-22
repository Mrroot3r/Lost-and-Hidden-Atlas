# November 22, 2026: Maryland, a first scatter across the state: Allegany and Garrett counties in the west, Washington
# County, Howard County and Baltimore in the middle, the Eastern Shore (Talbot, Queen Anne's, Somerset, Worcester) and
# Southern Maryland (St. Mary's, Calvert). Region taken as the thinnest on the map by tools/choose.py --thinnest (md).
# Sources read in this session: Wikipedia articles (read one at a time as raw text), National Park Service pages for the
# C&O Canal and Antietam, Maryland Department of Natural Resources park pages (Fort Frederick, Casselman River Bridge,
# Patapsco Valley, Point Lookout), Howard County's museum page, Calvert County's museums page, and the pages of Old Wye
# Mill, Furnace Town, Historic Sotterley, Third Haven Friends Meeting, Spruce Forest Artisan Village, Garrett County
# Historical Society museums, HMdb and Clio. Interiors were not visited by any source opened unless the entry says so.
from data_b import N
from data_ma import W
BATCH={'key':'md_tqvk','label':'Maryland: a first scatter, mountains to the Eastern Shore','added':'2026-11-22 16:25'}

PATAPSCO=('Patapsco Valley State Park (Maryland Park Service). The park page gives 9 a.m. to sunset; a day-use service charge is collected at the area contact stations '
          '(amount not checked). On busy weekends the Avalon, Orange Grove, Hilton, Hollofield and Daniels areas often fill to capacity and close to more cars (park page, read November 22, 2026).')
PAT_L=['Maryland DNR: Patapsco Valley State Park','https://dnr.maryland.gov/publiclands/Pages/central/patapsco.aspx']
COCH=['NPS: Paw Paw Tunnel','https://www.nps.gov/choh/planyourvisit/paw-paw-tunnel.htm']

PLACES=[
N('paw-paw-tunnel','Paw Paw Tunnel, C&O Canal','Oldtown','md','canal','standing',39.55556,-78.46278,'site','public','walk','canal','1836–1850',
  'A 3,118-foot canal tunnel through Tunnel Hill, dug so the Chesapeake and Ohio Canal could skip six miles of the Potomac\'s Paw Paw Bends. Work began in 1836 and was meant to take two years; labour fights, riots among the workers, money shortfalls and loose shale stretched it to fourteen. It is lined with an estimated six million bricks. Canal boats used it until the canal closed to commerce in 1924.',
  'The tunnel itself, walked on the old towpath with a flashlight: weep holes, rope burns worn into the timbers and rub rails by the boats\' tow lines, and brass plates every 100 feet. The two-mile Tunnel Hill Trail climbs over the top to where the builders lived and to views of the Paw Paw Bends; the Park Service calls it steep and strenuous. Bicycles must be walked inside.',
  'Six million bricks and fourteen years to save six miles.',
  'Chesapeake and Ohio Canal National Historical Park (National Park Service). Park at the Paw Paw Tunnel Campground off Route 51 and walk about half a mile up the towpath to the tunnel (NPS page, read November 22, 2026). The Park Service has had rock-fall work and detours on the towpath below the tunnel since 2020; its closure page said the tunnel was expected to stay open and the Tunnel Hill Trail was open, with short closures for repairs. Check the park\'s alerts before going.',
  [W('Paw Paw Tunnel'),COCH,['NPS: Paw Paw Tunnel closures and detours','https://www.nps.gov/choh/planyourvisit/pawpaw-closure.htm']],
  th=[39.54449,-78.46076],thn='Paw Paw Tunnel Campground parking, Route 51',brick='some'),

N('lonaconing-furnace','Lonaconing Iron Furnace','Lonaconing','md','industry','ruins',39.57028,-78.97806,'site','view','drive','','1837–1850s',
  'A stone blast furnace of the George\'s Creek Coal and Iron Company, also called Furnace No. 1, built between 1837 and 1839 and first in blast in 1839. It is remembered as the first coke-fired furnace in the country to work successfully, showing that coke and raw bituminous coal could both smelt iron. Iron-making stopped in the mid-1850s. The top house, moulding house, engine house and hot-blast stoves are all gone.',
  'The sandstone stack itself, a cut-off square pyramid about 50 feet high, 50 feet square at the base and 25 feet at the top. A historical marker beside it describes the 60-horsepower steam blowing engine and the arch that once joined the furnace top to the road so ore and fuel could be hauled across.',
  'The furnace that proved coke could make American iron.',
  'Stands in a small park beside Main Street in Lonaconing, with a historical marker; who owns the ground was not confirmed, so it is given here as seen from the street and the marker. Street parking in town; no lot was found mapped next to it.',
  [W('Lonaconing Furnace'),['HMdb: George\'s Creek Coal and Iron Company marker','https://www.hmdb.org/m.asp?m=139083']],
  brick='no'),

N('casselman-bridge-grantsville','Casselman River Bridge (Little Crossings), National Road','Grantsville','md','landmark','standing',39.69667,-79.14361,'exact','view','walk','','1813–1814',
  'A stone arch bridge built in 1813–1814 to carry the National Road over the Casselman River east of Grantsville; the first wagons crossed in 1815. Its 80-foot arch was then the longest single stone span in the United States. It carried the road until 1933 and has been a National Historic Landmark since 1964. It has also been called Casselman\'s, Castleman\'s and Little Crossings Bridge.',
  'The 354-foot bridge and its single high arch, best seen from the river banks; Stanton\'s Mill and a small 1813 National Road arch stand just beside it.',
  'The longest stone arch in America, the year the British burned Washington.',
  'Casselman River Bridge State Park (Maryland Park Service). CLOSED for now: the park page (read November 22, 2026) says the bridge and the ground round it, including a stretch of the river, are fenced off for safety while the arch, walls, abutments and deck are repaired. Look from outside the fence until the park says it has reopened; it was open to walkers before. Small lots off the National Pike and Casselman Road beside the park.',
  [W('Casselman Bridge'),['Maryland DNR: Casselman River Bridge State Park','https://dnr.maryland.gov/publiclands/pages/western/casselman.aspx']],
  brick='no'),

N('stantons-mill-grantsville','Stanton\'s Mill','Grantsville','md','industry','standing',39.69682,-79.14037,'site','open','drive','','about 1797',
  'A grist mill complex beside the Casselman River, its two-storey heavy-timber mill dating from about 1797 with an addition of 1890. With it go a stone-faced timber crib dam and race of the mid-1800s, the tailrace, a small one-span stone arch bridge built for the National Road in 1813, and a frame storehouse of about 1900. Wikipedia describes the mill as still working.',
  'The timber-framed mill, its dam and race, and the little 1813 stone arch. Interior not checked.',
  '',
  'Next to Casselman River Bridge State Park, at the Spruce Forest Artisan Village (a nonprofit), whose page says the village is open seasonally May 1 to October 31, with artists\' hours varying (read November 22, 2026). The mill\'s own days and times were not found.',
  [W('Stanton\'s Mill'),['Spruce Forest Artisan Village','https://spruceforest.squarespace.com']],
  brick='no',hours='May 1 to October 31 (the village); mill times not found'),

N('oakland-bo-station','Oakland B&O station','Oakland','md','rail','standing',39.40989,-79.40894,'exact','open','drive','stations','1884',
  'A Queen Anne brick station with a round domed tower between one-storey wings, designed by Baldwin and Pennington and built by the Baltimore and Ohio Railroad in 1884, when the railroad was selling Oakland and Garrett County as a mountain resort; its Oakland Hotel stood across the tracks and a meadow. Amtrak trains stopped again from 1976 to 1981. The town bought it in 1998.',
  'The station, tower and wings, still beside the main line. Clio describes it as the Oakland B&O Railroad Museum of the Garrett County Historical Society, with changing exhibits and a Baldwin locomotive acquired in 2018. Interior not checked.',
  '',
  'Owned by the Town of Oakland; run as a museum by the Garrett County Historical Society. The society\'s hours page gives Wednesday to Saturday 10 a.m. to 3 p.m. for its museums; that it covers the station was not confirmed. Trains still run on the line beside it: keep off the tracks.',
  [W('Oakland station (Maryland)'),['Clio: Oakland B&O Railroad Station and Museum','https://theclio.com/entry/20594'],['Garrett County museums: hours','https://garrettcountymuseums.com/hours/']],
  brick='yes',hours='?'),

N('fort-frederick-md','Fort Frederick','Big Pool','md','fort','standing',39.61028,-78.00361,'exact','open','walk','forts','1756–1757',
  'A large stone fort built by the colony of Maryland in 1756–1757, during the French and Indian War, as a refuge for frontier settlers, and named for Frederick Calvert, Lord Baltimore. It was used again in the Revolution. Its walls had decayed to as little as eight feet in places when the state took it over; the Civilian Conservation Corps rebuilt them in the 1930s. It has been a National Historic Landmark since 1973.',
  'A stone square with a bastion at each corner, each wall about 179 feet long and 17.5 feet high, the gate in the middle of the south wall, and two of the three barracks rebuilt inside. In summer staff and volunteers in period clothing work in the barracks. The C&O Canal runs through the park below.',
  'A Vauban fort in stone on the edge of the colonial frontier.',
  'Fort Frederick State Park (Maryland Park Service), 11100 Fort Frederick Road, Big Pool. The park page (read November 22, 2026) says the barracks are open Thursday to Monday from Memorial Day to Labor Day and on spring and autumn weekends; for the fort buildings and visitor center it says to call ahead (301-842-2155).',
  [W('Fort Frederick State Park'),['Maryland DNR: Fort Frederick State Park','https://dnr.maryland.gov/publiclands/Pages/western/fortfrederick.aspx']],
  th=[39.61285,-78.00714],thn='Fort Frederick State Park lot, Fort Frederick Road',brick='no',hours='Barracks Thursday to Monday, Memorial Day to Labor Day, and spring and autumn weekends; call for other buildings'),

N('dunker-church-antietam','Dunker Church, Antietam battlefield','Sharpsburg','md','worship','standing',39.47536,-77.74678,'exact','public','drive','','1852 (rebuilt 1962)',
  'A plain whitewashed meeting house built in 1852 by the German Baptist Brethren, called Dunkers, on land given by the farmer Samuel Mumma. On September 17, 1862, the Battle of Antietam was fought round it; it was hit by rifle and cannon fire, changed hands, and served Confederate troops briefly as a field hospital. Mended by 1864, it held services until it fell into disrepair, and a windstorm blew it down in 1921. It was rebuilt on its own foundation for the centennial, largely from the salvaged material, and rededicated on September 2, 1962.',
  'The small white church by the Hagerstown Pike, one of the landmarks named in the battle reports, with its rebuilt walls on the original foundation. The battlefield\'s trails and tour stops lead out from it. Interior not checked.',
  'The church at the centre of the bloodiest day in American history.',
  'Antietam National Battlefield (National Park Service), open all year; the visitor center is open every day 9 a.m. to 5 p.m., and the park and visitor center close on Thanksgiving, December 25 and January 1 (NPS hours page, read November 22, 2026). Entrance fee not checked. Parking on the park road beside the church.',
  [W('Dunker Church'),['NPS: Dunker Church','https://www.nps.gov/places/antietam-battlefield-dunker-church.htm'],['NPS: Antietam hours','https://www.nps.gov/anti/planyourvisit/hours.htm']],
  th=[39.47393,-77.7451],thn='Park road lot near the Dunker Church',brick='no',hours='Battlefield open all year; visitor center daily 9 a.m. to 5 p.m.; closed Thanksgiving, December 25, January 1'),

N('thomas-viaduct','Thomas Viaduct','Elkridge','md','rail','standing',39.22167,-76.71333,'exact','public','walk','','1833–1835',
  'An eight-arch stone railroad viaduct over the Patapsco between Relay and Elkridge, built for the Baltimore and Ohio Railroad from July 4, 1833, to July 4, 1835, and named for its first president, Philip E. Thomas. When finished it was the largest railroad bridge in the country and its first multi-span stone railroad bridge built on a curve; its piers are wedge-shaped to follow the curve. It is sometimes called the oldest multiple-arch stone railroad bridge in the world, though England\'s Sankey Viaduct is older. It still carries CSX freight and MARC Camden Line trains.',
  'The curved line of arches across the river and valley, seen from the Avalon Area\'s entrance road just west of the contact station, where an interpretive sign stands. The park warns of a blind curve on the road. The viaduct is a working railway: stay off it.',
  'Built in 1835 and still carrying trains every day.',
  PATAPSCO+' Enter the Avalon Area off U.S. Route 1 in Elkridge. The viaduct itself belongs to the railroad, CSX Transportation; it is seen from the park.',
  [W('Thomas Viaduct'),PAT_L,['Maryland DNR: Avalon Area historic sites','https://dnr.maryland.gov/publiclands/Pages/central/PatapscoValley/Avalon/Historic-Sites.aspx']],
  brick='no'),

N('patterson-viaduct-ilchester','Patterson Viaduct ruins','Ilchester','md','rail','ruins',39.24889,-76.76472,'site','public','walk','','1829',
  'One of the three stone viaducts of the first 13 miles of the Baltimore and Ohio Railroad, built from May to December 1829 to cross the Patapsco at Ilchester and named for the B&O director William Patterson. The great flood of 1868 nearly destroyed it; a Bollman iron truss replaced it in 1869 on the old west arch and wing wall, and in 1903 the line moved to a new bridge upstream when the Ilchester Tunnel opened. The ruins were listed on the National Register in 1976.',
  'The one surviving arch on the west bank, which carried a road under the railway, and the east abutment. Since 2006 a cable-stayed footbridge on the Grist Mill Trail, its design echoing a Bollman truss, crosses the river on top of them.',
  '',
  PATAPSCO+' The Grist Mill Trail crosses the river on the old abutments.',
  [W('Patterson Viaduct'),PAT_L],
  brick='no'),

N('bollman-truss-bridge-savage','Bollman Truss Railroad Bridge','Savage','md','rail','standing',39.13472,-76.82528,'exact','public','walk','','1852 or 1869',
  'A two-span, 160-foot iron through-truss bridge of the type invented by the Baltimore engineer Wendel Bollman, the first all-metal bridge design used steadily on an American railroad. It is the last of its design left standing. It carried the B&O spur to the Savage cotton mill over the Little Patuxent until the mill closed in 1947. The bridge\'s age is given two ways: its own Wikipedia article says it was built in 1852 elsewhere on the main line and moved here about 35 years later, the Savage Mill Trail article says it was built in 1869. Howard County restored it in 1983.',
  'The iron towers, trusses and rods of the bridge, which now carries the Savage Mill Trail. The decorative metal caps on the towers are replacements, put back in the 1983 restoration after vandals took the originals. The 1816–1823 Savage textile mill stands near the start of the trail.',
  'The only bridge of its kind left anywhere.',
  'Savage Park and the Savage Mill Trail (Howard County Recreation and Parks), a flat gravel trail of 0.8 mile. Park hours not checked. Parking in the lots by Savage Mill and on Fair Street.',
  [W('Bollman Truss Railroad Bridge'),W('Savage Mill Trail')],
  th=[39.13602,-76.82886],thn='Fair Street lot, Savage',brick='no',conf='mixed'),

N('ellicott-city-bo-station','B&O Ellicott City Station','Ellicott City','md','rail','standing',39.26722,-76.79528,'exact','open','drive','stations','1830 or 1831',
  'The end of the Baltimore and Ohio Railroad\'s first 13 miles from Baltimore, where passenger trains, pulled at first by horses, began running in May 1830; the Tom Thumb engine was shown off here that August. Wikipedia gives 1830 for the stone station, built of local granite against the end of the Oliver Viaduct; Howard County\'s page says it was built in 1831 as a freight depot and fitted for passengers in 1857. Passenger trains stopped in 1949 and freight in 1972. It is called the oldest railroad station left in the country.',
  'The two-storey stone station, its upper floor level with the tracks on the viaduct, under a gabled roof with a wooden cupola. Inside are a gift shop and freight agent\'s office below, and the superintendent\'s office, ticket and telegraph office, men\'s waiting room and car house above. Behind it the 1885 freight house holds a model of the first 13 miles and a restored 1927 caboose; the filled-in turntable pit still shows its granite foundations.',
  'Where American railroading started.',
  'Howard County Department of Recreation and Parks, 3711 Maryland Avenue. Admission free; guided tours by appointment. Closed January 1, Easter Sunday, Memorial Day, July 4, Labor Day, Thanksgiving and December 25 (county page, read November 22, 2026). The second floor is up a stair; there is no lift. Trains still run on the line beside it.',
  [W('Baltimore and Ohio Ellicott City Station Museum'),['Howard County: B&O Ellicott City Station Museum','https://www.howardcountymd.gov/ecborail']],
  brick='no',hours='Wednesday and Thursday 10 a.m. to 3 p.m.; Friday to Sunday 10 a.m. to 5 p.m.; closed Monday and Tuesday'),

N('wye-mill','Old Wye Mill','Wye Mills','md','industry','standing',38.94139,-76.08139,'exact','open','drive','','late 1600s',
  'A wooden water-powered grist mill on the line between Queen Anne\'s and Talbot counties, on a site milling since the late 1600s: the earliest industrial site on the Eastern Shore still in use, and called the oldest grist mill in the country that has kept working. It was one of the first mills automated with Oliver Evans\'s system, which it still uses.',
  'The frame mill with a 10-foot steel overshot wheel of the 1800s, and inside nearly all its late-1700s machinery. The mill sells its stone-ground grain products. The lower floor is wheelchair accessible.',
  'Grinding on the same spot for more than three hundred years.',
  'Old Wye Mill (a nonprofit) beside Route 662 just off U.S. Route 50. Parking beside the mill. Grain products can be bought out of season by calling 410-827-3850 (mill page, read November 22, 2026).',
  [W('Wye Mill'),['Old Wye Mill: hours, dates and location','https://www.oldwyemill.org/visit']],
  th=[38.94164,-76.08061],thn='Lot beside the mill',brick='no',hours='May 1 to October 31: Wednesday to Saturday 10 a.m. to 3 p.m.; Sunday 1 to 3 p.m.'),

N('old-wye-church','Old Wye Church','Wye Mills','md','worship','standing',38.93639,-76.08,'site','view','drive','','1717–1721',
  'An Anglican brick church built in 1717–1721, heavily altered in 1854 and put back to its 1700s appearance in 1947–1949. It is a plain Georgian parish church: one storey, a gable roof, round-arched windows and shouldered buttresses. It is listed on the National Register.',
  'The brick church with its round-arched windows and buttresses, close to the Wye Mill. Interior not checked.',
  '',
  'An Episcopal church of Wye Parish, on Route 662 in Wye Mills. Service times were not found on a page of the parish\'s own; see from the road and churchyard.',
  [W('Old Wye Church'),['Wye Parish','https://wyeparish.org/']],
  brick='?'),

N('third-haven-meeting-house','Third Haven Meeting House','Easton','md','worship','standing',38.76639,-76.07694,'exact','open','drive','','1682–1684',
  'A timber Quaker meeting house begun in 1682 on three acres bought from the merchant John Edmondson and first used for a meeting on August 14, 1684. It is generally held to be the oldest Friends meeting house standing in America. It was built framed in white oak with four wings; in 1797 the east and west wings were taken off and the building widened by ten feet, which left it a little lopsided. A brick meeting house for winter was added on the grounds in 1880.',
  'The plain frame meeting house of the 1680s and its grounds, with the 1880 brick house beside it. The meeting\'s history page says the timbers were hewn with a broadaxe. Interior not checked.',
  'The oldest Quaker meeting house in America, still used.',
  'Third Haven Friends Meeting. The entrance is on South Washington Street (Route 565) in Easton, three tenths of a mile south of the hospital. The meeting\'s page invites visitors to worship (read November 22, 2026); which of its two buildings is used was not checked.',
  [W('Third Haven Meeting House'),['Third Haven Friends Meeting','https://thirdhaven.org/'],['Third Haven: history','https://www.thirdhaven.org/history.php']],
  brick='no',hours='Meeting for worship Sundays 10 a.m. and Wednesdays 5:30 p.m.'),

N('nassawango-furnace','Nassawango Iron Furnace (Furnace Town)','Snow Hill','md','industry','ruins',38.20417,-75.46889,'site','open','drive','','1830–1849',
  'A blast furnace built in 1830 by the Maryland Iron Company to smelt the bog iron ore of the Pocomoke Forest. A hot blast, then newly invented in England, may have been added in 1837. Because the bog ore varied so much, it stopped in 1849. It now stands at the centre of Furnace Town, a 25-acre site kept by a nonprofit foundation.',
  'The brick furnace stack, with buildings of the 1800s brought to the site round it (a church, a store, houses) and artisans\' workshops; one moved house of 1869 is the information centre.',
  'An iron furnace fed by ore dug from a swamp.',
  'Furnace Town Foundation (a nonprofit), at Old Furnace Road and Millville Road off Route 12, north of Snow Hill. Admission $8 adults, $6 children 5 to 15, seniors and military, free under 5 (foundation page, read November 22, 2026).',
  [W('Nassawango Iron Furnace Site'),W('Furnace Town Living Heritage Museum'),['Furnace Town Historic Site','https://furnacetown.org/']],
  brick='?',hours='April to October: Thursday to Sunday 10 a.m. to 4 p.m.'),

N('point-lookout-light','Point Lookout Lighthouse and prison camp','Scotland','md','light','standing',38.0387,-76.3221,'exact','open','drive','forts','1830',
  'A house lighthouse first lit on September 20, 1830, at the mouth of the Potomac, built by John Donahoo; it was raised to two full storeys in 1883 and made a duplex for two keepers in 1927. Round it in the Civil War stood Hammond General Hospital and then the prison camp for Confederate soldiers, which held 20,000 at a time. How many died there is given two ways: the state park says nearly 4,000, the lighthouse article more than 3,000.',
  'The lighthouse, now a small self-guided museum with exhibits over both floors. The state park says the earthworks of a Civil War fort still stand on the river shore near Cornfield Harbor, and that the fort\'s barracks and officers\' quarters and part of the prison pen have been rebuilt.',
  'A lighthouse that kept watch over a prison of 20,000.',
  'Point Lookout State Park (Maryland Park Service), at the end of Route 5. Day-use areas open daily 7 a.m. to sunset May to September and 8 a.m. to sunset October to April (park page, read November 22, 2026); park fee not checked. The lighthouse days come from its Wikipedia article (May to September, Thursday to Monday 9 a.m. to 5 p.m., opened to the public May 15, 2025), not from a park page.',
  [W('Point Lookout Light'),W('Point Lookout State Park'),['Maryland DNR: Point Lookout State Park','https://dnr.maryland.gov/publiclands/pages/southern/pointlookout.aspx'],['Maryland DNR: Point Lookout history','https://dnr.maryland.gov/publiclands/pages/southern/ptlookout/history-ptlookout.aspx']],
  brick='?',hours='Lighthouse May to September, Thursday to Monday 9 a.m. to 5 p.m. (Wikipedia); park 7 a.m. to sunset in summer'),

N('cove-point-light','Cove Point Lighthouse','Lusby','md','light','standing',38.38625,-76.38175,'exact','open','drive','','1828',
  'A conical brick tower and keeper\'s house built in 1828 by John Donahoo, the oldest lighthouse on Chesapeake Bay that has never stopped working. Keepers stayed until 1986, when it was automated; Calvert County took it over in 2000, with much old equipment in place, and the Calvert Marine Museum runs it.',
  'The 1828 tower, the 1901 fog signal building with the old fog bell on the roof of a 1902 shed, and a visitor center; a museum interpreter is on site. The keeper\'s house is let as a vacation rental and is not part of the visit.',
  '',
  'Calvert County, run by the Calvert Marine Museum, 3500 Lighthouse Boulevard, Lusby. Admission and parking free. The county page (read November 22, 2026) says the grounds are open at set hours but does not give them; the museum allows visits in the summer months. Check with the museum before going.',
  [W('Cove Point Light'),['Calvert County: museums','https://calvertcountymd.gov/3284/Museums']],
  th=[38.3861,-76.38234],thn='Lighthouse Boulevard lot',brick='?',hours='?'),

N('teackle-mansion','Teackle Mansion','Princess Anne','md','landmark','standing',38.20333,-75.70222,'exact','open','drive','','1802–1819',
  'A Neoclassical house at 11736 Mansion Street built between 1802 and 1819 for Littleton Dennis Teackle and his wife Elizabeth Upshur Teackle. It appears in George Alfred Townsend\'s novel The Entailed Hat. It is the home of the Somerset County Historical Society and was listed on the National Register in 1971.',
  'The long Neoclassical front and its period rooms of the 1800s, shown by the historical society on free tours. Interior otherwise not checked.',
  '',
  'Somerset County Historical Society, 11736 Mansion Street. A county tourism listing names free tours by the society; their days and times were not found on a page of the society\'s own.',
  [W('Teackle Mansion'),['Visit Somerset: Teackle Mansion open for tours','https://visitsomerset.com/event/teackle-mansion-open-for-tours']],
  brick='?',hours='?'),

N('sotterley-hollywood','Historic Sotterley','Hollywood','md','landmark','standing',38.37824,-76.53487,'exact','open','drive','','1700s',
  'A plantation on the Patuxent River, once the home of George Plater, sixth governor of Maryland, and later of Herbert L. Satterlee, a New York lawyer and son-in-law of J. P. Morgan. The house is a long, low frame building of nine bays, clad in wide beaded clapboards under a wood-shingle roof. It opened to the public in 1961 and is a National Historic Landmark.',
  'The house above the river; a sawn-log quarters for enslaved people of about 1830; an 1700s brick warehouse and an early-1800s brick meat house; an early-1800s corn crib and barns of the early 1900s. Gardens and trails round the grounds.',
  'A Tidewater plantation with its slave quarters still standing.',
  'Historic Sotterley (a nonprofit), 44300 Sotterley Lane. Its page (read November 22, 2026) says the guided tour season ended October 18 and that tours, visitor center and exhibits are closed until May 2027; the grounds, gardens and trails stay open through the winter, with the restrooms shut.',
  [W('Sotterley (Hollywood, Maryland)'),['Historic Sotterley','https://www.sotterley.org/']],
  brick='?',hours='Guided tours May to mid-October (closed until May 2027); grounds and trails open in winter'),

N('phoenix-shot-tower','Phoenix Shot Tower','Baltimore','md','industry','standing',39.29072,-76.60547,'exact','view','walk','','1828–1892',
  'A round red brick tower 234 feet tall, built in under six months in 1828 from about 1.1 million bricks, without outside scaffolding; Charles Carroll of Carrollton laid its cornerstone on July 4. It was the tallest structure in the United States until 1846. Molten lead was poured through a sieve at the top and fell into a tub of water at the bottom to make musket shot. A fire gutted it in 1882 and it was rebuilt; it stopped making shot in 1892. When an oil company bought it in 1921 to clear the site for a filling station, the neighbourhood raised the money to give it to the city in 1928.',
  'The tapering brick tower, crenellated at the top, with heavy metal doors at the foot and small windows scattered up its side to light the stair. The colour of the brick changes near the top, where it was rebuilt after the 1882 fire. It is the only one left of Baltimore\'s four shot towers.',
  'The tallest building in America in 1828, built to drop lead.',
  'Owned by the City of Baltimore, at Fayette and Front streets by the Shot Tower Metro station. Seen from the street; tours are given only now and then, and no page of the city or a museum giving set hours was found.',
  [W('Phoenix Shot Tower')],
  brick='yes'),
]

PIN_NOTES={
 'paw-paw-tunnel':'Wikipedia coordinate, over the middle of the tunnel under Tunnel Hill (woods on the aerial); the portals were not placed. The parking point is the mapped lot at the Paw Paw Tunnel Campground (OpenStreetMap), about half a mile below the south end by the towpath.',
 'lonaconing-furnace':'Wikipedia coordinate, on a small tree-covered green beside Main Street; the stack itself could not be picked out on the aerial.',
 'casselman-bridge-grantsville':'Wikipedia coordinate; the aerial shows the pin on the stone bridge over the river.',
 'stantons-mill-grantsville':'OpenStreetMap point for the watermill on Casselman Road; the Wikipedia coordinate fell in an empty field.',
 'oakland-bo-station':'OpenStreetMap point for the station museum at 117 East Liberty Street; the Wikipedia coordinate fell in woods.',
 'fort-frederick-md':'Wikipedia coordinate, inside the fort walls on the aerial; parking is a mapped lot on Fort Frederick Road inside the park (OpenStreetMap).',
 'dunker-church-antietam':'Wikipedia coordinate, on the small white church on the aerial; parking is the mapped lot on the park road just south-east (OpenStreetMap).',
 'thomas-viaduct':'Wikipedia coordinate, on the viaduct over the river on the aerial.',
 'patterson-viaduct-ilchester':'Wikipedia coordinate, at the river crossing of the old line in the gorge (aerial and bare-ground shading); the arch and abutment were not picked out separately.',
 'bollman-truss-bridge-savage':'Wikipedia coordinate, on the bridge over the river on the aerial; parking is the mapped Fair Street lot (OpenStreetMap).',
 'ellicott-city-bo-station':'Wikipedia coordinate, on the station roof beside the tracks on the aerial.',
 'wye-mill':'Wikipedia coordinate, on the mill building by the road on the aerial; parking is the mapped lot beside it (OpenStreetMap).',
 'old-wye-church':'Wikipedia coordinate, in the trees of the church grounds; the building is hidden on the aerial.',
 'third-haven-meeting-house':'Wikipedia coordinate, beside a building in the trees of the meeting grounds on the aerial.',
 'nassawango-furnace':'Register list coordinate for the furnace site, in woods; the bare-ground shading shows a mound and curving channels there, but the stack was not picked out.',
 'point-lookout-light':'Wikipedia coordinate, on the lighthouse at the tip of the point on the aerial.',
 'cove-point-light':'Wikipedia coordinate, beside the tower on the aerial; parking is the mapped lot on Lighthouse Boulevard (OpenStreetMap).',
 'teackle-mansion':'Wikipedia coordinate, on a house by the road on the aerial.',
 'sotterley-hollywood':'OpenStreetMap point for Sotterley Mansion; the Wikipedia coordinate fell in trees by a field.',
 'phoenix-shot-tower':'Wikipedia coordinate, on the tower (its long shadow shows) on the aerial.',
}
