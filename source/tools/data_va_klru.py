# November 22, 2026: Virginia, a third scatter across the state (it had 32 places, the fewest of any state or province
# nobody else held; claimed with tools/choose.py --thinnest). Fifteen places from the Eastern Shore to Big Stone Gap:
# two colonial courthouses, a church of 1706, house museums from 1797 to the 1890s, an ironworks, a rebuilt
# Washington mill, an 18th-century tavern, a stone shot tower and an iron-furnace village on the New River, the largest
# fort in the United States, and a president's camp in the Blue Ridge.
# Sources read in this session: Wikipedia articles (tools/wiki_raw.py) and the pages of whoever runs each place
# (tools/page.py): the Northampton Historic Preservation Society, the Eastern Shore of Virginia Historical Society,
# Cople Parish, Belle Grove, Inc., the American Civil War Museum and the National Park Service (Richmond, Shenandoah),
# Mount Vernon, the City of Alexandria, Virginia State Parks (Shot Tower, New River Trail, Southwest Virginia Museum),
# the Fort Monroe Authority, the Smithfield Times (1750 Courthouse), Glencoe Mansion and the Danville Museum.
# Nothing was checked on the ground. Interiors were not visited by any source opened unless the entry says so.
from data_b import N
from data_ma import W
BATCH={'key':'va_klru','label':'Virginia: a third scatter, Eastern Shore to Big Stone Gap','added':'2026-11-22 10:25'}

PLACES=[
N('eastville-court-green','Eastville Court Green (the 1731 courthouse, clerk\'s office and debtors\' prison)','Eastville','va','civic','standing',37.35278,-75.94667,'site','open','walk','','1731–1814',
  'Northampton County\'s courthouse of 1731, a small Flemish-bond brick building about 35 by 23 feet, was built by a John Marshall for 50,000 pounds of tobacco. It served until 1795, then spent more than a century as a storehouse let for a dollar a year, until the county bought it back in 1913 and Preservation Virginia moved it beside the old clerk\'s office. With the debtors\' prison of 1814 the group was repaired in the 1950s; the county\'s records here go back to 1632.',
  'Three small early buildings on the court green: the 1731 brick courthouse, the clerk\'s office (about 1800) with its battened doors and odd paving stones, and the debtors\' prison of about 1814. The Northampton Historic Preservation Society runs a self-guided tour with exhibits in all three and an overview exhibit in the 1899 courthouse, now the county administration building; the 1907 jail is being restored as a fifth stop.',
  'The Eastern Shore\'s colonial courthouse, a storehouse for a hundred years.',
  'Owned by Northampton County; the exhibits are run by the Northampton Historic Preservation Society. The three historic buildings are open April to October, Monday to Friday, except holidays (the society\'s page, read November 22, 2026); clock times were not given. A small lot is mapped just north-west of the green, off U.S. 13 Business in Eastville.',
  [W('Northampton County Courthouse Historic District'),['Northampton Historic Preservation Society: the Court Green','https://northamptonhistoricpreservationsociety.com/historic-court-green']],
  th=[37.35320,-75.94722],thn='Lot beside the court green',brick='yes',hours='April to October: Monday to Friday, except holidays (times not given)'),

N('ker-place-onancock','Ker Place','Onancock','va','landmark','standing',37.71284,-75.74693,'exact','open','walk','','1799',
  'A two-storey, five-bay Federal house built in 1799 for John Shepherd Ker, son of a Scottish settler, with a pedimented pavilion projecting front and back and a wing that began as the kitchen, joined by a hyphen. The Eastern Shore of Virginia Historical Society bought it with two acres in 1960, made it its headquarters, and shows it as a house museum of the early 1800s.',
  'The Federal house in the Onancock Historic District, with its centre pavilions and cross-gabled roof. Volunteer docents give tours of the interior and exterior when one is on duty; otherwise the office staff point visitors to the society\'s Shore History app for a self-guided tour. Interior details were not checked beyond the society\'s mention of exhibits.',
  '',
  'Run by the Eastern Shore of Virginia Historical Society, 69 Market Street. Call (757) 787-8012 before a Saturday visit to be sure a docent is there; closed Sundays and holidays (shorehistory.org, read November 22, 2026). Street parking and small lots are mapped along Market Street and Crockett Avenue.',
  [W('Ker Place'),['Eastern Shore of Virginia Historical Society: Visit','https://www.shorehistory.org/visit']],
  brick='yes',hours='Monday to Friday 11 a.m. to 3 p.m.; Saturday 11 a.m. to 3 p.m. when a docent is scheduled; closed Sundays and holidays'),

N('yeocomico-church','Yeocomico Church','Kinsale','va','worship','standing',38.06239,-76.59696,'exact','open','drive','cemeteries','1706',
  'A wooden church was built here in 1655 for Cople Parish; it was replaced in 1706 by the present T-shaped church of locally fired brick, dated by a brick in its south-east wall, and parts of the first building may have been reused in it. Like most Anglican churches in Virginia it was left empty after the Revolution, used as barracks by local tradition, and repaired in 1788, the 1820s and 1830s, and 1928. It is the fourth oldest church in the state, a National Historic Landmark since 1970, and still the main church of Cople Parish.',
  'A T-shaped brick church whose walls mix Flemish, English and irregular bond, with glazed headers, a moulded water table and walls 19 inches thick; the bricks are said to have been dug and fired about a hundred yards north-east of the church. The east end has a large 16-over-16 window under a round one. The churchyard holds the graves of several bishops and of the writer John Dos Passos. Interior not checked.',
  'Brick church of 1706 still holding Sunday services.',
  'The working church of Cople Parish (Episcopal), on Old Yeocomico Road near Kinsale, Westmoreland County. Services every Sunday at 11 a.m. (copleparish.com, read November 22, 2026). No parking lot is mapped; parking was not checked.',
  [W('Yeocomico Church'),['Cople Parish','https://www.copleparish.com/']],
  brick='yes',hours='Sunday service 11 a.m.'),

N('belle-grove-middletown','Belle Grove (Isaac Hite\'s house)','Middletown','va','landmark','standing',39.02088,-78.30377,'exact','open','walk','','1794–1797',
  'A large Federal-style house of limestone quarried on the place, built in 1794–1797 for Major Isaac Hite Jr., a Revolutionary veteran and James Madison\'s brother-in-law. General Philip Sheridan made it his headquarters at the Battle of Cedar Creek in 1864. Little altered since, it was opened as a house museum in 1967 by its owner, the National Trust for Historic Preservation, and is still a working farm; since 2002 it has been part of Cedar Creek and Belle Grove National Historical Park.',
  'The limestone manor house with its pedimented Tuscan portico, the only front laid in finished stone, and fine woodwork inside that moves from Georgian to Federal. The guided tour (one hour, at most 12 people) goes inside. On the grounds: an 1815 ice house and smokehouse, a cemetery of the enslaved, the foundations of the "Old Hall" of about 1750 beside the smokehouse, an exhibit on the archaeology of the enslaved quarter, and the trailhead for the 19th Corps Entrenchment Trail.',
  'A Federal stone house that was Sheridan\'s headquarters at Cedar Creek.',
  'Owned by the National Trust for Historic Preservation and run by Belle Grove, Inc. Adults $15, students $6, children 5 and under free; no pets. Hours for 2026: guided tours Monday to Saturday 10 a.m. to 4 p.m. and Sunday 1 to 5 p.m. from March 21 to October 31; Saturday and Sunday only in November; daily with candlelight evenings in December; closed from December 31 to March 19, 2027 (bellegrove.org, read November 22, 2026). A small parking lot is at the house; the one seen on the aerial is about 100 m north of it, by the outbuildings.',
  [W('Belle Grove Plantation (Middletown, Virginia)'),['Belle Grove: Tours and hours','https://www.bellegrove.org/visit/tours']],
  th=[39.02177,-78.30413],thn='Belle Grove parking',brick='no',hours='March 21 to October 31: Monday to Saturday 10 a.m. to 4 p.m., Sunday 1 to 5 p.m.; November weekends only; closed January to mid-March'),

N('tredegar-iron-works','Tredegar Iron Works','Richmond','va','industry','standing',37.53537,-77.44581,'site','open','walk','','1837',
  'Richmond businessmen opened the ironworks in 1837 beside the James River, with furnaces and rolling mills built by Welsh ironworkers from Tredegar in Wales. In the Civil War it was the biggest ironworks in the Confederacy, making about half its artillery and the iron plate for the ironclad CSS Virginia. It escaped the fire when Richmond was evacuated in 1865, went on making iron and munitions into the mid-20th century, and its surviving buildings were restored from the 1960s. It is a National Historic Landmark district and the home of the American Civil War Museum.',
  'The restored brick works buildings on Tredegar Street: the gun foundry, which holds the National Park Service visitor centre for Richmond National Battlefield Park (it moved there from the pattern building in 2019), and the American Civil War Museum. A Wikipedia photograph shows the red-brick pattern building with roofless brick walls of the old works beside it. A statue of Abraham Lincoln and his son Tad marks their visit to the burnt city in April 1865. Interior of the works buildings beyond the exhibits not checked.',
  'The Confederacy\'s cannon foundry, beside the James.',
  'Run by the American Civil War Museum, with the National Park Service visitor centre on the same plaza at 500 Tredegar Street. The museum charges admission (acwm.org, read November 22, 2026); the park grounds are open sunrise to sunset, and visitor centre hours vary by season (nps.gov). Lots are mapped along Tredegar Street; the Belle Isle lot is a short walk west.',
  [W('Tredegar Iron Works'),['American Civil War Museum: Visit','https://acwm.org/visit/'],['National Park Service: Tredegar move, 2019','https://www.nps.gov/rich/learn/news/a-new-future-at-tredegar-for-the-national-park-service.htm']],
  brick='yes',hours='Museum daily 10 a.m. to 5 p.m.'),

N('washington-gristmill-distillery','George Washington\'s Gristmill and Distillery','Mount Vernon','va','industry','standing',38.71327,-77.12987,'site','open','walk','','1771–c. 1850; mill rebuilt 1933',
  'In 1771 George Washington had a large stone gristmill built on Dogue Run, three miles west of Mount Vernon, to replace his father\'s mill of the 1730s; its flour was shipped to the West Indies and Europe. His farm manager James Anderson talked him into building a whiskey distillery beside it; the distillery burned in 1814 and the mill was gone by about 1850. The state rebuilt the mill in 1933 on archaeological evidence, and the Mount Vernon Ladies\' Association rebuilt the distillery on its excavated foundations; both work again today.',
  'Reconstructions, not originals, on the original sites: a sandstone mill with a pitch-back water wheel turning two millstones (some timbers from a mill at Front Royal; most of the machinery replaced 1997–2002), and a stone distillery that makes whiskey, built on foundations up to three feet thick that archaeologists uncovered. Tours go inside.',
  'Washington\'s whiskey, made again where he made it.',
  'Run by Mount Vernon, 5513 Mount Vernon Memorial Highway, 2.7 miles from the estate\'s main entrance. Included with a Mount Vernon grounds pass, or $10 alone (mountvernon.org, read November 22, 2026). Parking lot beside the site.',
  [W("George Washington's Gristmill"),['Mount Vernon: Distillery and Gristmill','https://www.mountvernon.org/the-estate-gardens/distillery-gristmill']],
  th=[38.71394,-77.13022],thn='Distillery and Gristmill parking',brick='no',hours='April to October: Friday to Sunday 10 a.m. to 5 p.m.'),

N('gadsbys-tavern-alexandria','Gadsby\'s Tavern','Alexandria','va','hotel','standing',38.80562,-77.04365,'exact','open','walk','hotels','c. 1785–1878',
  'Two taverns at the corner of North Royal and Cameron streets: a tavern of about 1785 and the City Tavern and Hotel of 1792, with an 1878 addition. John Gadsby ran them from 1796 to 1808 and gave them his name. George Washington often came, and John Adams, Thomas Jefferson, James Madison, James Monroe and Lafayette (in 1824) were guests; Jefferson was given a banquet in the ballroom in 1801. In 1917 the Metropolitan Museum of Art bought the ballroom woodwork, which is still shown in New York.',
  'The two tavern buildings in Old Town, with Gadsby\'s Tavern Museum, a restaurant serving in the 1792 City Tavern dining room, and an American Legion post. The ballroom upstairs has a reproduction of the woodwork that went to the Metropolitan Museum. A National Historic Landmark since 1963.',
  '',
  'Gadsby\'s Tavern Museum is run by the City of Alexandria (Office of Historic Alexandria), 134 North Royal Street, telephone 703-746-4242. Closed Wednesdays all year, and Mondays and Tuesdays in fall and winter (alexandriava.gov, read November 22, 2026); clock times were not on the page read. Street and garage parking in Old Town; not checked.',
  [W("Gadsby's Tavern"),['City of Alexandria: Gadsby\'s Tavern Museum','https://www.alexandriava.gov/go/1743']],
  brick='yes',hours='Closed Wednesdays, and Mondays and Tuesdays in fall and winter (times not given)'),

N('jackson-ferry-shot-tower','Jackson Ferry Shot Tower','Austinville','va','industry','standing',36.87019,-80.87032,'exact','public','walk','','1807',
  'A 75-foot tower for making lead shot, begun by Thomas Jackson after the Revolution and finished in 1807. Lead from the Austinville mines was melted at the top and poured through a sieve; the drops fell through the tower and a 75-foot shaft dug into the cliff below it, a 150-foot fall, into a kettle of water. Unlike most shot towers it is built of limestone, with walls two and a half feet thick, and it stands on a cliff over the New River.',
  'The square limestone tower at the edge of the bluff over the New River, with signs on its use; visitors could climb it on scheduled summer days, but the New River Trail State Park page now says tours are unavailable during renovations. One of few shot towers left in the United States.',
  'A stone shot tower with a 75-foot shaft dug below it.',
  'Shot Tower Historical State Park (Virginia State Parks). Grounds open dawn to dusk; the state parking fee applies ($7 a car at New River Trail), and the tower itself is free when open. From I-77 exit 24, north on U.S. 52 for two miles (dcr.virginia.gov, read November 22, 2026). The two state pages disagree on tower tours: the Shot Tower page says it opens on scheduled summer days, the New River Trail page says tours are unavailable due to renovations. Lot beside the tower.',
  [W('Jackson Ferry Shot Tower'),['Virginia State Parks: Shot Tower','https://www.dcr.virginia.gov/state-parks/shot-tower'],['Virginia State Parks: New River Trail','https://www.dcr.virginia.gov/state-parks/new-river-trail']],
  conf='mixed',th=[36.86989,-80.87017],thn='Shot Tower lot',brick='no',hours='Grounds dawn to dusk'),

N('foster-falls-village','Foster Falls village and iron furnace','Foster Falls','va','town','standing',36.88361,-80.85556,'site','public','walk','','1880s',
  'An iron-making and rail village on the New River, mostly industrial and commercial buildings of the late 19th century: the iron furnace stack, the rail bed and its frame passenger station of about 1887, a general store, a combined grist and saw mill, and the Foster Falls Hotel, a late-Victorian brick building that became an orphanage in 1938. It was listed on the National Register as a district in 2009 and is now the headquarters of New River Trail State Park.',
  'Twelve old buildings, two sites and three structures: look for the furnace stack, the depot (now the park gift shop), the store, the mill and the brick hotel, which runs again as the Inn at Foster Falls. No cars are allowed in the historic village; the rail bed is the New River Trail. Whether the furnace stack can be walked up to was not checked.',
  'An iron furnace and railroad village on the New River Trail.',
  'New River Trail State Park (Virginia State Parks), 116 Orphanage Drive, Max Meadows. Trails and day-use area open daily dawn to dusk; parking $7 a car, self-pay when the contact station is unstaffed (dcr.virginia.gov, read November 22, 2026). The inn is run by a private operator. Lot on Orphanage Drive.',
  [W('Foster Falls Historic District'),['Virginia State Parks: New River Trail','https://www.dcr.virginia.gov/state-parks/new-river-trail']],
  th=[36.88423,-80.85469],thn='Orphanage Drive lot',brick='some',hours='Dawn to dusk'),

N('fort-monroe-hampton','Fort Monroe and the Casemate Museum','Hampton','va','fort','standing',37.00207,-76.30919,'site','open','walk','forts','1819–1834',
  'Begun in 1819 under President Monroe\'s plan for coastal forts and finished in 1834, the six-sided stone-and-brick bastion fort at Old Point Comfort is the largest fort by area ever built in the United States: 63 acres inside a moat, with walls up to ten feet thick. Robert E. Lee helped build it. In the Civil War it stayed in Union hands and became a place of freedom for escaped slaves under the contraband policy; afterwards Jefferson Davis was held here for two years. The Army left in 2011, and it is now Fort Monroe National Monument.',
  'The moat and walls of the fort, its gates and the barbette tier on top; the Casemate Museum inside the walls, which includes the casemate cell where Jefferson Davis spent his first months, and among the original buildings Quarters 1, the commander\'s house.',
  'The largest fort ever built in the United States.',
  'Managed by the Fort Monroe Authority, the National Park Service and the City of Hampton. The Casemate Museum is free and self-guided with timed tickets (first at 10 a.m., last at 3:30 p.m.); seasonal hours on the page also list the visitor centre Wednesday to Sunday 9:30 a.m. to 4:30 p.m. (fortmonroe.org, read November 22, 2026). OpenStreetMap maps several small lots inside and beside the fort; which one visitors are sent to was not checked.',
  [W('Fort Monroe'),['Fort Monroe Authority: Casemate Museum','https://fortmonroe.org/things-to-do/casemate-museum/']],
  brick='some',hours='Museum April to October Tuesday to Sunday, November to March Wednesday to Sunday, 10 a.m. to 4:30 p.m.'),

N('rapidan-camp','Rapidan Camp (President Hoover\'s camp)','Shenandoah National Park','va','inst','standing',38.49075,-78.41992,'site','public','hike','','1929–1933',
  'Herbert and Lou Henry Hoover built this retreat in the Blue Ridge while he was president, 1929 to 1933, on a trout stream at the head of the Rapidan; the Marines built thirteen buildings, including a lodge, mess halls and cabins, and the President\'s cabin was called the Brown House. It was the forerunner of Camp David. In 2004 Shenandoah National Park restored the three cabins left, the Brown House, the Prime Minister\'s Cabin and the Creel, to how they looked in Hoover\'s time.',
  'Three restored cabins in the woods by the stream: the Brown House, furnished as in Hoover\'s day, and the Prime Minister\'s Cabin, which holds exhibits. Wikipedia says an interpretive guide stays at the camp through much of spring, summer and autumn; the park page says the camp has exhibits on the Hoovers.',
  'Hoover\'s Camp David before Camp David.',
  'Shenandoah National Park. A four-mile round trip (moderate, 870 feet of climb, about 2 hours 45 minutes, three stream crossings) from the Milam Gap parking area at mile 52.8 of Skyline Drive: cross the Drive, take the Appalachian Trail a few feet, turn left on the blue-blazed Mill Prong Trail, and at the second stream crossing stay right on the yellow-blazed Mill Prong Horse Trail down to the camp. Dogs on a leash of six feet at most (nps.gov, read November 22, 2026). The park entrance fee and Skyline Drive closures were not checked.',
  [W('Rapidan Camp'),['National Park Service: Rapidan Camp trailhead','https://www.nps.gov/places/rapidan-camp.htm']],
  th=[38.50035,-78.44564],thn='Milam Gap parking, Skyline Drive mile 52.8',brick='no'),

N('southwest-virginia-museum','Southwest Virginia Museum (the Ayers house)','Big Stone Gap','va','landmark','standing',36.86369,-82.78003,'exact','open','walk','','1888–1895',
  'A house built from 1888 to 1895 for Rufus A. Ayers, a former Attorney General of Virginia, designed and built by Charles A. Johnson, with outside walls of limestone and sandstone from local quarries and red oak lining the rooms; a small moat once surrounded it. The state bought it in 1946 from a foundation run by C. Bascom Slemp, and it is now a museum of the region, run as a state park.',
  'The stone house, with red-oak walls and ceilings inside; exhibits on the coal boom of the 1890s, the history of Big Stone Gap, and the pioneers who went west by the Wilderness Road, and the Southwest Virginia Walk of Fame.',
  '',
  'Southwest Virginia Museum Historical State Park (Virginia State Parks), 10 West 1st Street North. Accessible parking at the rear of the museum (dcr.virginia.gov, read November 22, 2026).',
  [W('Southwest Virginia Museum Historical State Park'),['Virginia State Parks: Southwest Virginia Museum','https://www.dcr.virginia.gov/state-parks/southwest-virginia-museum']],
  brick='no',hours='Tuesday to Friday 10 a.m. to 4 p.m., Saturday 10 a.m. to 5 p.m., Sunday 1 to 5 p.m.; also Mondays 10 to 4 from Memorial Day to Labor Day'),

N('isle-of-wight-courthouse-1750','1750 Isle of Wight Courthouse','Smithfield','va','civic','standing',36.98197,-76.63208,'exact','open','walk','','1750–1751',
  'William Rand built the county courthouse in 1750–51 with a semicircular apse and a conical roof like those of English churches and the Capitol at Williamsburg. It was the county\'s court until 1800, then was turned into a house, its arcade blocked and its roof made a gable. Preservation Virginia bought it with the clerk\'s office of 1799 in 1938 and restored it by 1959; a second restoration in the late 1990s, with Colonial Williamsburg craftsmen, made the inside look like a courthouse of the period again. It is one of four arcaded colonial courthouses left. Historic Smithfield took it over in 2013, and in 2024 it was deeded to the 1750 Courthouse of Isle of Wight County, Inc.',
  'The brick courthouse with its round apse and reopened arcade on Main Street, and beside it the small brick clerk\'s office of 1799. The courthouse group interprets the building to visitors (Smithfield Times, May 2024). The interior is a 1990s re-creation, not original fittings.',
  'One of four arcaded colonial courthouses left in Virginia.',
  'Owned and run by the 1750 Courthouse of Isle of Wight County, Inc., 130 Main Street in the Smithfield Historic District. Opening days and hours were not found on any page that could be read; the Smithfield tourism page for it answered 404. Street parking on Main Street; not checked.',
  [W('Old Isle of Wight Courthouse'),['Smithfield Times: the courthouse\'s new owner, May 2024','https://www.smithfieldtimes.com/2024/05/14/smithfield-historic-jewel-celebrates-a-new-chapter/']],
  brick='yes',hours='?'),

N('glencoe-mansion-radford','Glencoe Mansion (General Gabriel Wharton\'s house)','Radford','va','landmark','standing',37.13235,-80.58044,'exact','open','walk','','1870s',
  'A large two-storey, five-bay Second Empire brick house built in the 1870s for Gabriel C. Wharton, a Confederate brigadier general; it first appears on Radford\'s tax rolls in 1876 and once had a barn, smokehouse and ice house on wide grounds. The family kept it until 1996, when, after standing empty for 30 years, it was given to the city. It is now a museum and art gallery.',
  'The Victorian house with period rooms, exhibits on Radford (Native American finds, Mary Draper Ingles, local industry, the railroad and the river), an art gallery, and the town visitor information desk. Free guided tours of 45 to 90 minutes any time it is open, or a self-guided tour.',
  '',
  'Run by the Radford Heritage Foundation, 600 Unruh Drive. Admission free; free parking on site (glencoemuseum.org, read November 22, 2026).',
  [W('Glencoe Museum'),['Glencoe Mansion: Plan your visit','https://glencoemuseum.org/visit']],
  brick='yes',hours='Wednesday to Saturday 10 a.m. to 4 p.m., Sunday 1 to 4 p.m.'),

N('sutherlin-mansion-danville','Sutherlin Mansion (the last capitol of the Confederacy)','Danville','va','landmark','standing',36.58094,-79.40011,'exact','open','walk','','1857–1858',
  'An Italian Villa house built in 1857–58 for Major William T. Sutherlin. Jefferson Davis stayed here from April 3 to 10, 1865, signed his last proclamation as Confederate president here on April 4, and learned at dinner on April 10 of the surrender at Appomattox. The city bought it and ran it as a whites-only public library from 1928 to 1972; a sit-in by Black students in 1960 led the city to close it rather than integrate, until it reopened that fall. It is now the Danville Museum of Fine Arts and History.',
  'A two-storey stuccoed house with a wooden porch, a heavy bracketed cornice and a square cupola, on Main Street in the Old West End ("Millionaires\' Row"). The museum is open for self-guided tours of the mansion and its exhibits; group guided tours by arrangement.',
  'Where the Confederate government spent its last week.',
  'Owned by the City of Danville and run by the Danville Museum of Fine Arts and History, 975 Main Street. Closed New Year\'s Day, Thanksgiving and Christmas (danvillemuseum.org, read November 22, 2026). Parking not checked.',
  [W('William T. Sutherlin Mansion'),['Danville Museum: Visit','https://danvillemuseum.org/visit/']],
  brick='no',hours='Thursday to Saturday 10 a.m. to 4 p.m., Sunday noon to 4 p.m.'),
]

PIN_NOTES={
 'eastville-court-green':'Wikipedia coordinate for the historic district; on the aerial it falls on the green among small buildings, but which one is the 1731 courthouse was not told apart. Parking is the lot mapped north-west of the green.',
 'ker-place-onancock':'OpenStreetMap building mapped as Ker Place.',
 'yeocomico-church':'OpenStreetMap point for the church.',
 'belle-grove-middletown':'Moved onto the manor house seen on the aerial, where OpenStreetMap maps Belle Grove Plantation; the Wikipedia coordinate was about 160 m south, in a field. Parking is the lot seen on the aerial north of the house.',
 'tredegar-iron-works':'OpenStreetMap building mapped as Tredegar Iron Works.',
 'washington-gristmill-distillery':'OpenStreetMap point for the Distillery and Gristmill; parking is the mapped lot beside it.',
 'gadsbys-tavern-alexandria':'OpenStreetMap point for Gadsby\'s Tavern, 138 North Royal Street.',
 'jackson-ferry-shot-tower':'OpenStreetMap point for the tower.',
 'foster-falls-village':'Wikipedia coordinate for the historic district.',
 'fort-monroe-hampton':'OpenStreetMap point for the Casemate Museum; on the aerial it falls on the fort wall beside the moat, where the casemates are.',
 'rapidan-camp':'Wikipedia coordinate for the camp. Trees hide it on the aerial; the bare-ground LiDAR shows a level spot where two streams meet. Parking is the mapped Milam Gap pull-off beside Skyline Drive.',
 'southwest-virginia-museum':'OpenStreetMap point for the museum.',
 'isle-of-wight-courthouse-1750':'OpenStreetMap point for the 1750 Isle of Wight Courthouse, 130 Main Street.',
 'glencoe-mansion-radford':'OpenStreetMap building mapped as Glencoe Museum.',
 'sutherlin-mansion-danville':'OpenStreetMap point for the Sutherlin Mansion.',
}
