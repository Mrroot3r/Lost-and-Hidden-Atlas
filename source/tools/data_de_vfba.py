# November 22, 2026: Delaware, third pass, spread over all three counties. Ground taken with tools/choose.py --thinnest
# (Delaware had 35 places, the fewest of any state or province free).
# Facts from the linked sources only, read in this session: Wikipedia articles read as raw text, the Kent and Sussex
# county Register lists, and the pages of whoever runs each place: the Delaware Division of Historical and Cultural
# Affairs (history.delaware.gov, woodburn.delaware.gov), the Delaware Public Archives' marker pages, the Delaware Forest
# Service, the Historic Odessa Foundation, the Seaford Historical Society, the parish of All Saints' and St. George's,
# Philadelphia Yearly Meeting, the National Park Service, HMdb.org and Lighthousefriends.com.
from data_b import N
from data_ma import W

HCA='https://history.delaware.gov'
STATE_SITES=['Delaware Historical and Cultural Affairs: other historic sites owned by the state',HCA+'/historic-sites/']

BATCH={'key':'de_vfba','label':'Delaware: Kent, Sussex and southern New Castle','added':'2026-11-22 19:26'}

PLACES=[
# ---------------- Kent County ----------------
N('belmont-hall-smyrna','Belmont Hall','Smyrna','de','landmark','standing',39.2945,-75.5959,'site','open','drive','','1773 (older rear wings)',
  'Thomas Collins, later a Continental brigadier general and the eighth president of Delaware, added this brick Georgian front about 1773 to an older house on land William Penn had granted in 1684. In 1777 a British party trying to capture him shot a sentry posted on the widow\'s walk, who died in the room below; Collins died here in 1789. The Cloak family farmed it from 1827 (Belmont brand canned tomatoes were sold in the late 1800s), and the state bought it in 1987 when the Route 13 bypass was built.',
  'A five-bay, three-storey brick front one room deep, with a flattened gable that makes a widow\'s walk reached by a stair tower. The finest woodwork is in the entrance hall and the west parlor; a plaque from the Daughters of the American Revolution in the front hall remembers the sentry. A fire in 1922 gutted the third floor, and the dormers date from the repairs.',
  'The sentry shot on the widow\'s walk in 1777.',
  'Owned by the State of Delaware. The state\'s list of its historic sites says Belmont Hall is open for tours by appointment, for historical events and for rentals; no regular hours were found. The house faces US 13 on the south side of Smyrna; a state notice of 2013 gives its address as 713 Smyrna-Leipsic Road. Parking at the house not checked.',
  [STATE_SITES,['Delaware Historical and Cultural Affairs: Belmont Hall (2013)',HCA+'/history.delaware.gov/2013/11/25/history-was-made-here-belmont-hall'],W('Belmont Hall (Smyrna, Delaware)')],
  brick='yes',hours='By appointment, and at events'),

N('christ-church-dover','Christ Church, Dover','Dover','de','worship','standing',39.15474,-75.52186,'site','view','walk','cemeteries','1734',
  'Founded in 1704 as a mission of the Society for the Propagation of the Gospel, the parish built this church in 1734 on one of the two squares Dover\'s town plan of 1717 set aside for houses of worship. It was remodelled in 1859 and 1887. The churchyard holds a cenotaph to Caesar Rodney, signer of the Declaration of Independence, whose actual grave is unknown.',
  'The original brick nave of 1734 with later brick additions round it, and the churchyard beside it. Still an Episcopal parish. Interior not checked.',
  'Caesar Rodney\'s cenotaph, in a churchyard of the 1700s.',
  'An active Episcopal parish at 501 South State Street, in the Dover Green Historic District, a few streets south of the Old State House. The parish\'s own page could not be read when this was written, so no service times are given. Street parking.',
  [['Episcopal Diocese of Delaware: churches in Delaware','https://delaware.church/episcopal-churches-in-delaware/'],W('Christ Church (Dover, Delaware)')],
  brick='yes',hours='?'),

N('woodburn-governors-house-dover','Woodburn, the Governor\'s House','Dover','de','landmark','standing',39.16139,-75.52303,'site','view','walk','','1790',
  'Charles Hillyard III built this house in 1790 on land he had bought at a sheriff\'s sale. Governor Jacob Stout leased it in 1820, the first time a Delaware governor lived here. The Quaker Daniel Cowgill, who owned it from 1825, freed his family\'s slaves and let them meet in the great hall. The state bought it in 1965, and it has been the official residence of Delaware\'s governors since 1966.',
  'A two-storey house of Flemish-bond brick with a Dutch door under a fanlight, its original wrought-iron strap hinges and lock box, sandstone window blocks and dog-head shutters. Interior not checked.',
  'Where Delaware\'s governors live, in a house of 1790.',
  'Owned by the State of Delaware and lived in. Its own page says tours are not offered to the public at present and to watch for public events; look from the street. In the north part of downtown Dover.',
  [['Woodburn: visiting','https://woodburn.delaware.gov/visiting-woodburn'],W('Delaware Governor\'s Mansion')],
  brick='yes',hours='?'),

N('camden-friends-meetinghouse','Camden Friends Meetinghouse','Camden','de','worship','standing',39.1143,-75.54781,'exact','open','walk','cemeteries','1805',
  'Built in 1805 for a meeting set up in 1795 in the Quaker town Daniel Mifflin laid out in 1783, and still the meeting house of the only active Quaker meeting in Kent County. Members worked in the Underground Railroad, among them John Hunn, its "Chief Engineer" in Delaware, who lies in the burial ground with his son, Governor John Hunn Jr.',
  'A two-storey gambrel-roofed brick meeting house, unusual among Quaker houses for its gambrel roof and its lack of porches. The upstairs school room (1805 to 1882) keeps its original desks, benches and blackboard and a ten-plate stove from Wrightsville, Pennsylvania; a panel between the meeting room and the stair drops into a groove to seat an overflow on the steps. The burial ground has tall stones and a memorial to the abolitionist Warner Mifflin. A modern hall of 2009 stands behind.',
  'An 1805 school room with its desks still in it, above a meeting of abolitionists.',
  'Camden Friends Meeting, 122 East Camden-Wyoming Avenue (Delaware Route 10). Anyone may attend meeting for worship; times from Philadelphia Yearly Meeting\'s page for the meeting. The page says the house is not wheelchair accessible.',
  [['Philadelphia Yearly Meeting: Camden Friends Meeting','https://www.pym.org/meetings/meeting/camden-friends-meeting/'],W('Camden Friends Meetinghouse')],
  brick='yes',hours='Meeting for worship Sunday 10 a.m. and Wednesday 5 p.m.'),

N('old-stone-tavern-little-creek','Old Stone Tavern (Nowell House)','Little Creek','de','landmark','standing',39.16406,-75.44694,'site','view','drive','','about 1829',
  'A two-storey, five-bay stone house in the Georgian style built about 1829, with a brick cornice and a brick kitchen wing. Local people long called it a tavern, but records show it was always a dwelling. It is also known as the Nowell House, the Bell House and the Old Stone House.',
  'A rare stone house in a county of brick and frame. Look from the road; interior not checked.',
  'The "tavern" that never was one.',
  'The federal public-land map marks this lot as state land under the name Stone Tavern; who manages it and whether it ever opens was not checked. View from Main Street in Little Creek only.',
  [W('Old Stone Tavern (Little Creek, Delaware)')],
  brick='some'),

N('parson-thorne-mansion-milford','Parson Thorne Mansion (Silver Hill)','Milford','de','landmark','standing',38.91374,-75.43495,'site','open','walk','','1730–1735',
  'A brick Georgian house built between 1730 and 1735 and remodelled in 1879 with a steep cross-gabled roof. It was the home of Governor William Burton and the boyhood home of the statesman John M. Clayton. The Milford Historical Society was given the house and grounds in 1961.',
  'A two-storey, five-bay brick centre-hall house with one-storey wings and a frame rear wing. It stands across from the Mill House. Interior not checked.',
  'A governor\'s house of the 1730s in the middle of Milford.',
  'Owned by the Milford Historical Society (Milford, Delaware). Kent County\'s visitor bureau lists open-house tours on the second Saturday of each month from 10 a.m. to 2 p.m. and tours at other times by telephone; the society\'s own page was not found, so those hours are not checked. A news report of 2026 said the house was being renovated. Parking not checked.',
  [['Kent County Tourism: Parson Thorne Mansion','https://visitcentraldelaware.com/directory/parson-thorne-mansion/'],W('Parson Thorne Mansion')],
  brick='yes',hours='?'),

# ---------------- Sussex County ----------------
N('highball-signal-delmar','Highball Signal','Delmar','de','rail','standing',38.45641,-75.578,'exact','public','walk','stations','1840s type; at Delmar since 1959',
  'One of the last of the ball signals railroads used before semaphores: a white ball hoisted to the top of a pole told a train the track was clear, and "highball" came to mean full speed ahead. This one served the New Castle and Frenchtown Railroad, then Hurlock, Maryland, and was moved to Delmar for the town\'s centennial in 1959.',
  'The ball on its pole beside the tracks, an old crossing guard shack, and a state marker, in Delmar\'s Railroad Park.',
  'Where the word "highball" comes from.',
  'A public display in Railroad Park, Delmar, beside the railroad on the Delaware–Maryland line. Keep off the active tracks. Parking not checked.',
  [['HMdb: Highball Signal marker','https://www.hmdb.org/m.asp?m=39780'],W('Highball Signal')],
  brick='no'),

N('st-georges-chapel-harbeson','St. George\'s Chapel','Harbeson','de','worship','standing',38.68448,-75.219,'exact','open','drive','cemeteries','1794 (first chapel 1719)',
  'The first chapel here was built in 1719 and burned in 1792; this brick one replaced it in 1794. Its furnishings were taken out in 1850 and the roof was rebuilt steep in 1882; it was restored in 1966, and the brick tower was added in 1955. It is one parish with All Saints\' in Rehoboth Beach.',
  'A one-storey brick chapel, 42 by 32 feet, with a restored Palladian window. Interior not checked.',
  'A chapel of 1794 on a site used since 1719.',
  'An active Episcopal chapel near Angola and Harbeson, in the Indian River Hundred; service times from the parish\'s own page. Parking not checked.',
  [['All Saints\' and St. George\'s: worship','https://allsaintsandstgeorges.org/gather'],W('St. George\'s Chapel, Lewes')],
  brick='yes',hours='Sunday 8:15 a.m. (Eucharist) and 10 a.m. (choral Eucharist)'),

N('cool-spring-presbyterian-church','Cool Spring Presbyterian Church','Lewes','de','worship','standing',38.73712,-75.23899,'exact','view','drive','cemeteries','1854 (congregation about 1726)',
  'The congregation was founded about 1726 and named for the branch that runs along the north-west side of the ground; Governor Thomas Penn granted the churchyard in 1737. This plain Greek Revival frame church of 1854, dedicated in January 1855, is the third on the site.',
  'A one-storey frame church on a brick foundation with a portico of two Doric columns. The churchyard holds Revolutionary War veterans, a member of the Continental Congress and a congressman of the mid-1800s. Interior not checked.',
  'A country church and churchyard granted by a Penn in 1737.',
  'An active congregation at 28842 Log Cabin Hill Road, west of Lewes. No service times were read. Look from the road or the churchyard; parking not checked.',
  [['Delaware Public Archives: Cool Spring Presbyterian Church marker','https://archives.delaware.gov/delaware-historical-markers/cool-spring-presbyterian-church/'],W('Cool Spring Presbyterian Church')],
  brick='some',hours='?'),

N('redden-forest-lodge','Redden Forest Lodge, stable and forester\'s house','Redden','de','landmark','standing',38.74107,-75.40826,'site','public','walk','','1900–1902',
  'Built in 1900–1902 as a hunting retreat for Frank Graham Thompson, heir to the Pennsylvania Railroad, with its own rail siding at Redden Crossroads. It fell out of use in the Depression; the state bought it in the 1930s, the Civilian Conservation Corps used it, and in 1937 it became the heart of Redden State Forest.',
  'Three Shingle-style buildings on cypress frames. The lodge is a shallow V, with a lobby under an open roof and two big brick fireplaces, a dining room panelled (it is said) from an 18th-century Long Island house, and its original Mission furniture; its south wing was rebuilt after a lightning fire in 1970. The T-shaped stable has an arched carriage door and an octagonal cupola. The lodge is rented out and the education centre is used for classes, so the insides are not open at set times.',
  'A railroad heir\'s hunting lodge in a state forest.',
  'Redden State Forest, Delaware Forest Service (Department of Agriculture), north of Georgetown. The forest is open to the public for hiking, riding, picnicking and permitted hunting; it has no after-hours or weekend security, and hunting seasons apply. The lodge is rented to groups. Park at the mapped lot on Redden Forest Drive by the stable and forester\'s house; the lodge is about 1,400 feet east of them.',
  [['Delaware Forest Service: camping and state forest rules','https://agriculture.delaware.gov/?p=6493'],['Delaware Forest Service: Lodge rules','https://agriculture.delaware.gov/wp-content/uploads/sites/108/2025/05/Lodge-packet.pdf'],W('Redden Forest Education Center')],
  th=[38.7403,-75.41272],thn='Lot on Redden Forest Drive',brick='?'),

N('de-vries-monument-lewes','De Vries Monument (Zwaanendael colony site)','Lewes','de','curio','marker',38.78628,-75.15856,'site','view','walk','','1631; monument 1909',
  'Dutch settlers under David Pietersz. de Vries landed near here in 1631 to set up a whaling station and farm, Zwaanendael, the first European settlement on Delaware Bay. The monument to it was dedicated on September 22, 1909, and the site is on the National Register as the De Vries Palisade.',
  'The 1909 monument and a state marker on a small site above Roosevelt Inlet, given a patio, seating and native planting in a redesign. Nothing of the settlement can be seen.',
  'Where Delaware began, in 1631.',
  'On Pilottown Road about 0.1 mile south of College Drive, by the University of Delaware\'s Lewes campus (marker address 660 Pilottown Road); HMdb says Delaware Historical and Cultural Affairs erected the marker. Who owns the ground was not checked: see it from Pilottown Road. Parking not checked.',
  [['HMdb: The De Vries Monument','https://www.hmdb.org/m.asp?m=38631'],['The DeVries Monument undergoes redesign','https://www.einpresswire.com/article/936587190/the-devries-monument-undergoes-redesign'],W('De Vries Palisade')],
  brick='?'),

N('governor-ross-mansion-seaford','Governor Ross Mansion','Seaford','de','landmark','standing',38.65734,-75.61855,'site','open','drive','','1855–1860',
  'William Henry Harrison Ross, governor of Delaware from 1851 to 1855, built the large Italianate addition between 1855 and 1860. He helped bring the railroad to southern Delaware, but he was also a slave owner who sided with the Confederacy and left for England during the Civil War. The Seaford Historical Society bought the house in 1976 and has restored and furnished it.',
  'A complete Victorian Italianate house, furnished, and 20 acres with a granary, stable, smokehouse, corn cribs, a pattern-book "Honeymoon Cottage", and what the society calls the only documented log slave quarter in Delaware. Guided tours only.',
  'A Confederate governor\'s mansion with Delaware\'s only documented log slave quarter.',
  'Seaford Historical Society, 23669 Ross Station Road. $7 for adults, free for children 12 and under; a combined ticket with the Seaford Museum is $12. Allow 1.5 to 2 hours. Free parking on site; ground floor wheelchair accessible. Hours from the society\'s page.',
  [['Seaford Historical Society: Gov. Ross Mansion','https://www.seafordhistoricalsociety.com/visit/gov-ross-mansion/']],
  brick='?',hours='Saturday and Sunday 1 to 4 p.m. (guided tours only)'),

# ---------------- New Castle County ----------------
N('corbit-sharp-house-odessa','Corbit–Sharp House','Odessa','de','landmark','standing',39.45384,-75.65717,'exact','open','walk','','1772–1774',
  'William Corbit, a tanner with business ties to Philadelphia, built this house in 1772–74; it is counted among the finest brick Georgian houses in the Mid-Atlantic and is a National Historic Landmark. It stayed in the family until 1938, when Rodney Sharp bought it and restored it with other buildings in Odessa (his work did away with Corbit\'s tannery). It has been a museum since 1940.',
  'A two-and-a-half-storey brick house with a hipped roof and balustrade, a Doric doorway, and rich original woodwork in the hall, parlor and dining room, with panelling round the fireplaces; furnished as in the late 1700s. Tours also take in the Wilson–Warner House of 1769 and the Collins–Sharp House.',
  'One of the finest Georgian houses of the Mid-Atlantic, still with its woodwork.',
  'Historic Odessa Foundation, 118 Main Street; tickets and guided tours start from its visitor center. Open March to December; holiday tours begin in November and regular tours resume on March 1. Last tour at 3 p.m. Hours from the foundation\'s own page.',
  [['Historic Odessa: plan your visit','https://historicodessa.org/plan-your-visit'],W('Corbit–Sharp House')],
  brick='yes',hours='March to December: Tuesday to Saturday 10 a.m. to 4 p.m., Sunday 1 to 4 p.m.; last tour 3 p.m.'),

N('new-castle-ice-piers','New Castle Ice Piers','New Castle','de','landmark','ruins',39.65778,-75.56083,'area','view','walk','','1803–1882',
  'Stone piers in the Delaware River off New Castle that turned drifting ice away from ships, so that vessels could shelter here when ports upriver froze. The first two were finished in 1795, paid for by a lottery of 1794, and the federal government paid for four more in 1802, the first federally funded transport project in Delaware. Wikipedia counts seven piers built between 1803 and 1882; the National Park Service says the early ones do not survive intact and that four hexagonal piers of the 1870s and a rectangular one of the 1850s remain.',
  'Weathered stone piers standing off the shore: granite shells filled with rubble on timber cribs. A National Historic Civil Engineering Landmark.',
  'Granite islands built to fend off river ice.',
  'Seen from the New Castle waterfront (Battery Park and the foot of Delaware Street); the piers are out in the river and are reached only by water. A mapped lot at the foot of Delaware Street is about 70 m west.',
  [['National Park Service: Ice commerce and the making of New Castle\'s harbor','https://home.nps.gov/articles/000/ice-commerce-and-the-making-of-new-castle-s-harbor.htm'],W('New Castle Ice Piers')],
  th=[39.65789,-75.56162],thn='Lot at the foot of Delaware Street',conf='mixed',brick='no'),

N('coochs-bridge-historic-site','Cooch\'s Bridge battlefield and homestead','Newark','de','fort','standing',39.64007,-75.73641,'area','open','drive','forts','1777',
  'The only Revolutionary War battle on Delaware soil was fought here on September 3, 1777: about 700 Americans under General William Maxwell ambushed the British and Hessian advance, then ran out of ammunition and fell back. Cornwallis made the Cooch house his headquarters for a week. The claim that the Stars and Stripes were first carried in battle here rests on circumstantial evidence and has been questioned. The Cooch family lived on the land for seven generations, and it is now becoming a state historic site.',
  'The Cooch homestead with its carriage house, granary, chicken house, icehouse and smokehouse, and the Cooch–Dayett mill. The bridge of 1777 is gone. Monuments and signs stand in the Pencader Heritage Museum lot and on Dayett Mills Road just south of Old Baltimore Pike.',
  'The only Revolutionary battle fought in Delaware.',
  'Cooch\'s Bridge Historic Site, Delaware Division of Historical and Cultural Affairs. The site is closed except for free tours booked ahead; tours are outdoors and there is no access to the house or the mill. Groups of eight or more can arrange a private tour through the site\'s page. Limited parking on site for tours; the roadside monuments on Dayett Mills Road can be seen any time.',
  [['Delaware Historical and Cultural Affairs: Cooch\'s Bridge Historic Site',HCA+'/coochs-bridge-historic-site'],W('Cooch\'s Bridge')],
  th=[39.64103,-75.73234],thn='Monuments on Dayett Mills Road',brick='?',hours='By booked tour only (grounds)'),

N('liston-range-rear-light','Liston Range Rear Light','Port Penn','de','light','standing',39.52381,-75.63961,'site','view','drive','','1877; moved here 1906',
  'A 120-foot wrought-iron skeleton tower by the Kellogg Bridge Company of Buffalo, first lit in 1877 as the Port Penn Rear Range Light and moved here in 1904–06 when the channel was realigned. It works with a low front light by the river to mark the longest navigable range in the United States. It is the tallest lighthouse in Delaware, about three miles inland.',
  'The tapering iron frame round a cylindrical stair tower that climbs to the watch room and lantern; it is the only range light on the Delaware River that keeps its Fresnel lens, a second-order lens from Paris first lit here in 1906. Still an active aid to navigation.',
  'Delaware\'s tallest lighthouse, three miles from the water.',
  'Privately owned; grounds, keeper\'s dwellings and tower closed. From US 13 at Biddles Corner turn east on Port Penn Road; the tower is on the left after about half a mile, across from Hickory Grove Cemetery. Look from the road only.',
  [['Lighthousefriends.com: Liston Rear Range Lighthouse','https://lighthousefriends.com/light.asp?ID=463'],W('Liston Range Rear Light')],
  brick='no'),
]

PIN_NOTES={
 'belmont-hall-smyrna':'From the Wikipedia article; on the house on the aerial.',
 'christ-church-dover':'Moved onto the church building beside its churchyard, seen on the aerial; the Wikipedia point was on the lawn about 45 m away.',
 'woodburn-governors-house-dover':'Address lookup of 151 Kings Highway SW, the address OpenStreetMap gives for Woodburn; on the house among its gardens on the aerial.',
 'camden-friends-meetinghouse':'Address lookup of 122 East Camden-Wyoming Avenue (a point on the address); on the meeting house on the aerial.',
 'old-stone-tavern-little-creek':'OpenStreetMap point for the Old Stone Tavern on Main Street, Little Creek; on a house on the aerial.',
 'parson-thorne-mansion-milford':"Moved onto the house in the middle of its lawn, seen on the aerial, about 65 m from OpenStreetMap's point for the grounds; the Wikipedia point was on the lawn.",
 'highball-signal-delmar':'From the Wikipedia article; beside the tracks in Railroad Park (the federal public-land map names the park at this point); the signal itself was not made out on the aerial.',
 'st-georges-chapel-harbeson':'Moved onto the chapel beside its graveyard on Beaver Dam Road, seen on the aerial; it matches the address lookup of 20274 Beaver Dam Road and the HMdb marker. The Wikipedia point fell in a pond about 130 m north.',
 'cool-spring-presbyterian-church':'OpenStreetMap church building north of Log Cabin Hill Road, beside its churchyard on the aerial; the address lookup fell on the road.',
 'redden-forest-lodge':"OpenStreetMap building for the Redden Forest Lodge; the lodge is under trees on the aerial. The parking point is by the stable and forester's house.",
 'de-vries-monument-lewes':'From the Wikipedia article; on Pilottown Road above the inlet on the aerial, where HMdb puts the monument; the monument itself was not made out.',
 'governor-ross-mansion-seaford':'Address lookup of 23669 Ross Station Road (a point on the address); on the house on the aerial.',
 'corbit-sharp-house-odessa':'Address lookup of 118 Main Street, Odessa (a point on the address); on the house on the aerial.',
 'new-castle-ice-piers':'From the Wikipedia article; in the river off Battery Park, with the stone piers visible on the aerial round it. The pin stands for the group.',
 'coochs-bridge-historic-site':'From the Wikipedia article, on Old Baltimore Pike by the creek; the parking point is the monument spot on Dayett Mills Road that Wikipedia gives.',
 'liston-range-rear-light':'From the Wikipedia article (Lighthousefriends.com gives the same point); among the buildings of the light station on the aerial; the thin tower was not made out.',
}
