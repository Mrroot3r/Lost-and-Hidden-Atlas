# November 24, 2026: Virginia, a fourth scatter (it had 47 places, the fewest of any state or province nobody else held;
# claimed with tools/choose.py --thinnest). Twelve places from Hampton Roads to the Shenandoah Valley and the New River:
# a president's birthplace manse, a general's house, a Quaker mill village, an 1891 pottery turned railway depot,
# an 18th-century tavern, a moved tavern, an earthwork fort of 1623, and two old-town districts.
# Sources read in this session: Wikipedia articles (tools/wiki_raw.py) and the pages of whoever runs each place
# (tools/page.py): the Woodrow Wilson Presidential Library, the Stonewall Jackson House, the Waterford Foundation,
# the National Park Service (Booker T. Washington), the Strasburg Museum, the Fairfax County Park Authority (Sully),
# Michie Tavern, Hanover Tavern and Historic Isle of Wight. Nothing was checked on the ground.
from data_b import N
from data_ma import W
BATCH={'key':'va_dnqe','label':'Virginia: a fourth scatter, Hampton Roads to the Shenandoah','added':'2026-11-24 02:30'}

PLACES=[
N('wilson-birthplace-staunton','Woodrow Wilson Birthplace (the Manse)','Staunton','va','landmark','standing',38.15008,-79.06886,'exact','open','walk','','1846',
  'The Manse, a 12-room Greek Revival house with 12 fireplaces, was built in 1846 by Staunton\'s First Presbyterian Church as its minister\'s home, for about $4,000. Woodrow Wilson was born in its "birth room" on December 28, 1856, and the family left in 1858. After his death in 1924 a foundation was formed, in 1938, to turn the house into a museum; it was restored to its 1850s look, opened in 1941, and made a National Historic Landmark in 1964.',
  'The birthplace house itself, reached by a scheduled guided tour, with a museum, a research library and a gift shop on the same campus. Furnishings were not checked beyond the restoration to the 1850s.',
  '',
  'Run by the Woodrow Wilson Presidential Library Foundation at 230 East Frederick Street. Open every day 10 a.m. to 5 p.m.; closed New Year\'s Day, Easter, Thanksgiving, Christmas Eve and Christmas Day; the last tickets are sold at 4:30 p.m. Tickets are $20 for adults, with lower prices for seniors, military, students and children (woodrowwilson.org, read November 24, 2026). Parking was not checked.',
  [W('Woodrow Wilson Presidential Library'),['Woodrow Wilson Presidential Library: hours and directions','https://www.woodrowwilson.org/hours-directions'],['Woodrow Wilson Presidential Library: tickets and tours','https://www.woodrowwilson.org/visit']],
  brick='yes',hours='Daily 10 a.m. to 5 p.m.; closed New Year\'s Day, Easter, Thanksgiving, Christmas Eve and Day; last tickets 4:30 p.m.'),

N('stonewall-jackson-house-lexington','Stonewall Jackson House','Lexington','va','landmark','standing',37.78472,-79.44139,'exact','open','walk','','1800–1861',
  'A two-storey brick house with a large stone addition at the back, built in 1800 by Cornelius Dorman and enlarged by Dr. Archibald Graham in 1845 to hold his medical practice. Major Thomas J. Jackson, then a professor at the Virginia Military Institute, bought it on November 4, 1858 for $3,000; it was the only house he ever owned, and he lived here until the Civil War began in 1861. It served as Stonewall Jackson Memorial Hospital from 1907 to 1954, became a museum, and was restored to the Jacksons\' time in 1979.',
  'A house museum in the Lexington Historic District with its garden. The brick front and the stone rear addition show the two building periods; interior rooms were not checked beyond the 1979 restoration.',
  '',
  'Owned and run as a museum by a nonprofit (stonewalljackson.org). Its home page gives Monday to Saturday 9 a.m. to 5 p.m. and Sunday 1 to 5 p.m. in a holiday-hours notice (read November 24, 2026), so the regular schedule may differ. On East Washington Street in the town centre; street parking was not checked.',
  [W('Stonewall Jackson House'),['Stonewall Jackson House','https://www.stonewalljackson.org']],
  brick='yes',hours='Monday to Saturday 9 a.m. to 5 p.m.; Sunday 1 to 5 p.m. (as given in a holiday-hours notice)'),

N('waterford-village-loudoun','Waterford (the Quaker mill village)','Waterford','va','town','standing',39.18667,-77.61,'area','public','walk','','1733–',
  'Amos Janney, a Quaker from Pennsylvania, bought land on Catoctin Creek about 1733 and built a grist mill and a saw mill in the 1740s; the settlement, first called Janney\'s Mill, took the name Waterford by the 1790s. Its Quaker population stayed loyal to the Union in the Civil War and helped slaves escape north. The village declined early in the 20th century; the Waterford Foundation was formed in 1944 to save it, and it became a National Historic Landmark District in 1970.',
  'A whole village of 18th- and 19th-century buildings on small streets. Named stops on the Foundation\'s page are Waterford Mill, the John Wesley Community Church (built in 1891 by and for the African American Methodist congregation), and the Second Street School, the one-room Black schoolhouse built in 1867 and used until 1957. A farm trail runs behind the mill and the school. Most houses are private homes.',
  '',
  'The streets are public; the houses are private homes, so look from the street. The Waterford Foundation (offices at the Old School, 40222 Fairfax Street, open Tuesday to Friday 10 a.m. to 2 p.m.) runs scheduled walking tours at $20 a person (waterfordfoundation.org, read November 24, 2026). The pin marks the middle of the village.',
  [W('Waterford, Virginia'),['Waterford Foundation: Visit','https://www.waterfordfoundation.org/visit']],
  th=[39.18778,-77.61000],thn='Waterford Old School, 40222 Fairfax Street',brick='?'),

N('booker-t-washington-birthplace','Booker T. Washington National Monument','Hardy','va','landmark','standing',37.11961,-79.73151,'site','open','drive','','1856–',
  'The monument keeps part of the 207-acre tobacco farm where Booker T. Washington was born into slavery on April 5, 1856. Congress paid for the site through a commemorative half dollar, the first United States coin to show an African American, minted from 1946 to 1951; the coins did not cover the cost and the state of Virginia made up the rest. It became a National Monument on April 2, 1956.',
  'Farm buildings, gardens, crafts and animals used to show 1850s tobacco farming and slavery, with a visitor center. Whether each building is original or rebuilt was not checked.',
  '',
  'Run by the National Park Service in rural Franklin County. The visitor center is open Wednesday to Sunday 10 a.m. to 4 p.m.; grounds and restrooms 9 a.m. to 5 p.m. every day; buildings closed Thanksgiving, December 25 and January 1, and the park closes at 2 p.m. on December 24 (nps.gov, read November 24, 2026). Phone (540) 682-0173 in bad weather. A parking lot is mapped on Plantation Trail inside the monument.',
  [W('Booker T. Washington National Monument'),['National Park Service: hours and seasons','https://www.nps.gov/bowa/planyourvisit/hours.htm']],
  th=[37.11773,-79.73300],thn='Lot on Plantation Trail',brick='?',hours='Visitor center Wednesday to Sunday 10 a.m. to 4 p.m.; grounds daily 9 a.m. to 5 p.m.'),

N('strasburg-museum-pottery-depot','Strasburg Museum (the Steam Pottery and Southern Railway depot)','Strasburg','va','industry','standing',38.98741,-78.35586,'exact','open','walk','stations','1891',
  'A two-storey, ten-bay brick factory with a slate hipped roof and a small raised monitor, built in 1891 for the Strasburg Stone and Earthenware Manufacturing Company to make earthenware. In 1913 it was turned into a station and depot for the Southern Railway, and a one-storey roof was added along its side. The Strasburg Museum opened in it in 1970; it is on the National Register of Historic Places (1979).',
  'The building itself, with museum displays of railroad artifacts and a model railroad, Strasburg pottery, Native American artifacts, period rooms and Civil War items. A model train display runs on Saturdays. Interiors beyond that list were not checked.',
  '',
  'Run by the Strasburg Museum. Open May to October, Friday to Sunday 10 a.m. to 4 p.m.; adults $5; the museum\'s page showed "Closed for the Season" when read on November 24, 2026 (strasburgmuseum.org). No cards at the gift shop. Parking was not checked.',
  [W('Strasburg Stone and Earthenware Manufacturing Company'),['Strasburg Museum','https://strasburgmuseum.org']],
  brick='?',hours='May to October: Friday to Sunday 10 a.m. to 4 p.m. (closed for the season in winter)'),

N('sully-historic-site','Sully Historic Site','Chantilly','va','landmark','standing',38.90769,-77.43086,'site','open','drive','','1794',
  'Richard Bland Lee built the main house in 1794 on land his family had held since 1725. After William Swartwort bought it in 1838 it was a home, a working farm, or both under a series of owners. The federal government took it in 1958 when land was cleared for Dulles Airport, and the Fairfax County Park Authority now runs it with a focus on the Lee family, with talks on the people enslaved here.',
  'The 1794 house and its grounds, shown on ticketed tours. Outbuildings and interior were not checked.',
  '',
  'Run by the Fairfax County Park Authority. The visitor center is open Saturday and Sunday 11 a.m. to 4 p.m., with ticketed tours at 11 a.m., 1 p.m. and 3 p.m.; the grounds are open dawn to dusk (fairfaxcounty.gov, read November 24, 2026; the page also carried a 2022 notice, so check before going). Parking was not checked.',
  [W('Sully Historic Site'),['Fairfax County Park Authority: Sully Historic Site','https://www.fairfaxcounty.gov/parks/sully-historic-site']],
  brick='no',hours='Visitor center Saturday and Sunday 11 a.m. to 4 p.m.; tours 11, 1 and 3; grounds dawn to dusk'),

N('michie-tavern-charlottesville','Michie Tavern (moved to its present site in 1927)','Charlottesville','va','hotel','standing',38.00870,-78.46369,'site','open','drive','','1784',
  'William Michie of Scotland took out a licence for an ordinary here in 1784, in Earlysville, to feed and house travellers. It stopped working as a tavern between 1830 and 1850 and stayed a private house; in 1927 it was bought by Josephine Henderson and moved 17 miles to its present place near Monticello. Another family ran it from 1968, and it was sold in 2026 to a local businessman. The Meadow Run Mill, moved from Augusta County, was rebuilt on the grounds in 1976.',
  'A group of old buildings that includes a pub and a restaurant, with a tavern shop. Because the tavern was moved, the building is old but not on its first site. Interior not checked.',
  '',
  'A working business, now under new ownership. On its page (michietavern.com, read November 24, 2026) the tavern shop is open 11 a.m. to 4 p.m. daily and the 1784 Pub Wednesday to Saturday 3:30 to 7:30 p.m.; tour times were not found. A parking area for the tavern is mapped just north-west on Thomas Jefferson Parkway.',
  [W('Michie Tavern'),['Michie Tavern: plan your visit','https://michietavern.com/plan-your-visit']],
  th=[38.00895,-78.46430],thn='Michie Tavern parking area',brick='some',hours='Tavern shop daily 11 a.m. to 4 p.m.; 1784 Pub Wednesday to Saturday 3:30 to 7:30 p.m.'),

N('lee-hall-mansion-newport-news','Lee Hall Mansion','Newport News','va','landmark','standing',37.19972,-76.57556,'site','open','drive','','1848–1859',
  'A brick plantation house built between 1848 and 1859 for Richard Decatur Lee, a local planter (no line to General Robert E. Lee has been traced). In 1862, during the Peninsula Campaign, it was headquarters for Confederate generals Joseph E. Johnston and John B. Magruder. It was listed on the National Register in 1972; the main house is open to the public and the former kitchen is used as offices.',
  'The main house, which is shown on guided tours. Nearby is Endview Plantation. Interior not checked.',
  '',
  'Run by the City of Newport News on Yorktown Road, near U.S. 60 and Route 238. No page of the managers that gave hours could be read, so hours are not checked: call the site before going. Parking was not checked.',
  [W('Lee Hall Mansion'),['City of Newport News: Lee Hall Mansion','https://newport-news.org/visitors/things-to-do/attractions-and-museums/3/lee-hall-mansion']],
  brick='?',hours='?'),

N('dayton-historic-district','Dayton Historic District','Dayton','va','town','standing',38.41611,-78.94083,'area','public','walk','','1880s–1930',
  'A town centre and its streets of 154 contributing buildings, mostly of the late 1800s and early 1900s, added to the National Register in 1984. Named buildings include the Carpenter Store (1888), the Bank of Dayton (1911), the Ruebush-Kieffer Printing Company, Dayton Drug Company, a college Administration Building (1910), the Kieffer Alumni Gymnasium (1930) and Methodist, Presbyterian and United Brethren churches.',
  'Brick and frame commercial buildings, houses and churches along the main streets. Which survive in what condition was not checked.',
  '',
  'The streets are public roads; who owns each building was not checked, and houses are private, so look from the street. The pin marks the centre of the district. Parking was not checked.',
  [W('Dayton Historic District (Dayton, Virginia)')],
  brick='?'),

N('christiansburg-institute','Christiansburg Institute','Christiansburg','va','civic','standing',37.13377,-80.38897,'site','view','drive','','1866–1966',
  'A school for African American students, founded in 1866 by Captain Charles S. Schaeffer, a Union soldier and Baptist minister, to educate freed slaves; it began with twelve students in a rented room. Booker T. Washington became an adviser in 1896 and it turned to trades teaching, with a trades building finished in 1902 and about 14 buildings by the 1940s. It was the only secondary school for Black students in Montgomery County until it closed in 1966 with integration.',
  'One of the old buildings is now a museum. Which buildings stand was not checked.',
  '',
  'The museum\'s own page could not be read, so its hours and whether it is open to walk-in visitors are not checked. The pin is on the address of the Institute, 125 Arrowhead Trail. Ask before going. Parking was not checked.',
  [W('Christiansburg Institute')],
  brick='?'),

N('fort-boykin-isle-of-wight','Fort Boykin (earthworks of 1623 to 1862)','Smithfield','va','fort','traces',37.03445,-76.61935,'site','public','drive','forts','1623–1862',
  'A fort was ordered here in 1623, after the attack of 1622, and built by Captain Roger Smith as a triangular earthwork with a ditch and a palisade. It was enlarged in the Revolution and renamed for Major Francis Boykin, possibly reshaped as a five-point star in 1812, and doubled in size by the Confederates between June 1861 and May 1862. Union gunboats fired on it on May 8, 1862; the garrison spiked its guns and left, and Union marines blew up the powder magazine on May 17. The remains, mostly Civil War, are in a public park.',
  'Earthen walls and gun positions on a bluff over the James River. A guided walk is offered on set dates.',
  '',
  'A park of Isle of Wight County at 7410 Fort Boykin Trail, open March to October 8:30 a.m. to 7:30 p.m. and November to February 8:30 a.m. to 5 p.m. (Historic Isle of Wight, read November 24, 2026). Guided tours: Isle of Wight County Museum, (757) 356-1223. A parking lot is mapped on Fort Boykin Trail, about 180 m south-east of the earthworks.',
  [W('Fort Boykin'),['Historic Isle of Wight: Fort Boykin','https://historicisleofwight.com/fort-boykin.html']],
  th=[37.03381,-76.61751],thn='Lot on Fort Boykin Trail',brick='no',hours='March to October 8:30 a.m. to 7:30 p.m.; November to February 8:30 a.m. to 5 p.m.'),

N('hanover-tavern','Hanover Tavern','Hanover','va','hotel','standing',37.76249,-77.36759,'exact','open','drive','','1733–',
  'A tavern was licensed on this spot in 1733 and has served without a break since; Patrick Henry helped his father-in-law John Shelton run it in the 1750s and 1760s, and Lafayette, Rochambeau, Washington, Chief Justice John Marshall and Charles Dickens are said to have stopped here. The present building, restored by the Hanover Tavern Foundation, dates from 1791 with early 19th-century and late 20th-century additions. It is a community centre, theatre and tavern beside the courthouse of Hanover County.',
  'A long colonial building with a covered portico. Interior not checked beyond the foundation\'s restoration.',
  '',
  'Run by the Hanover Tavern Foundation, at Hanover Courthouse Road, Hanover. Closed Monday and Tuesday; Wednesday to Saturday 11 a.m. to 9 p.m.; Sunday 11 a.m. to 8 p.m. (hanovertavern.org/hours, read November 24, 2026). Parking was not checked.',
  [W('Hanover Tavern'),['Hanover Tavern: hours','https://hanovertavern.org/hours/']],
  brick='some',hours='Wednesday to Saturday 11 a.m. to 9 p.m.; Sunday 11 a.m. to 8 p.m.; closed Monday and Tuesday'),
]

PIN_NOTES={
 'wilson-birthplace-staunton':'Wikipedia coordinates for the Manse; to be checked on the aerial.',
 'stonewall-jackson-house-lexington':'Wikipedia coordinates for 8 East Washington Street; to be checked on the aerial.',
 'waterford-village-loudoun':'The middle of the village, from Wikipedia.',
 'booker-t-washington-birthplace':'Wikipedia coordinates for the monument.',
 'strasburg-museum-pottery-depot':'The ArcGIS geocoder and OpenStreetMap agree on 440 East King Street, about 40 m from Wikipedia\'s point.',
 'sully-historic-site':'Wikipedia\'s point fell on the highway; moved onto the house seen on the aerial.',
 'michie-tavern-charlottesville':'Wikipedia\'s point fell in woods; the ArcGIS geocoder\'s match for 683 Thomas Jefferson Parkway is used.',
 'lee-hall-mansion-newport-news':'Wikipedia coordinates for the house.',
 'dayton-historic-district':'The middle of the district, from Wikipedia.',
 'christiansburg-institute':'A street-address match (125 Arrowhead Trail) from the ArcGIS geocoder.',
 'fort-boykin-isle-of-wight':'Wikipedia\'s point was at the fort\'s edge; moved to the middle of the earthworks seen on the bare-ground aerial.',
 'hanover-tavern':'Wikipedia\'s point fell in a parking lot; moved onto the long building beside it seen on the aerial.',
}
