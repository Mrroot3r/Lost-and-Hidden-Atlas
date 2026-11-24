# November 24, 2026: West Virginia, a third scatter (it had 50 places, none in Hancock, Ritchie, Tyler, Doddridge, Barbour,
# Brooke, Greenbrier's pavilion country or the Monroe and Pocahontas back roads). Ground claimed with tools/choose.py
# --thinnest (wv). Fourteen places in twelve counties.
# Sources read: Wikipedia articles (tools/wiki_raw.py) and the National Register lists by county; with tools/page.py the
# General Commission on Archives and History of the United Methodist Church (Rehoboth Church). Web search results quoted the
# Greenbrier Historical Society (Blue Sulphur Springs Pavilion), a Hancock County park description (Peter Tarr Furnace) and
# the Forest Service background for Cheat Summit Fort. The pages of the Ritchie County Historical Society and the Swiss
# Historical Village would not open from here, so hours for those are recorded as not found. Interiors were not visited by any
# source opened unless the entry says so.
from data_b import N
from data_ma import W
BATCH={'key':'wv_hqmn','label':'West Virginia: a third scatter across the state','added':'2026-11-24 09:36'}

PLACES=[
N('peter-tarr-furnace-weirton','Peter Tarr Furnace','Weirton','wv','industry','ruins',40.4374,-80.5728,'area','public','drive','','1790s–1840',
  'Called the first iron furnace west of the Alleghenies. A man named Grant built it in the 1790s on land of the pioneer James Campbell beside Kings Creek; Peter Tarr bought the business soon after, and with a partner formed Connell, Tarr and Company. Fuelled with local timber, it made about two tons of iron a day, mostly cooking pots and grates, and in the War of 1812 its iron was cast into cannonballs said to have been used at the 1813 Battle of Lake Erie. It ran until 1840, and in 1968 the shell was rebuilt as a permanent landmark.',
  'A stone furnace stack rebuilt in 1968 (Wikipedia), in a small roadside park with markers telling its story. What is original and what was rebuilt was not checked in any source opened.',
  'The first iron furnace west of the mountains, rebuilt as a monument.',
  'A small roadside park along Kings Creek Road in northern Hancock County, described in a search result as kept up by Hancock County and open to the public; the county\'s own page was not read. No hours or fees found. Parking not checked.',
  [W('Peter Tarr Furnace Site')],
  brick='?'),

N('old-stone-house-pennsboro','Old Stone House (Webster-Martin-Ireland House)','Pennsboro','wv','landmark','standing',39.28472,-80.97222,'exact','open','drive','','c. 1810',
  'A historic inn and boarding house, built about 1810 as a stone building five bays wide and two deep with a gable roof, with a two-story frame addition. It was listed on the National Register in 1978. The Ritchie County Historical Society opens it as a historic house and local history museum.',
  'A stone house with a one-story porch across the front (Wikipedia). Museum rooms inside; what they hold was not checked.',
  'A stone inn from about 1810, now the county museum.',
  'Run as a museum by the Ritchie County Historical Society, at 310 West Myles Avenue (search result). The society\'s page would not open from here; one listing says limited hours, with no times given. Parking not checked.',
  [W('Old Stone House (Pennsboro, West Virginia)'),['WV Tourism: Stone House Museum','https://wvtourism.com/company/stone-house-museum']],
  brick='no',hours='?'),

N('wells-inn-sistersville','Wells Inn (Hotel Wells)','Sistersville','wv','landmark','standing',39.56309,-80.99674,'exact','open','drive','','1894–1895',
  'A two-story brick hotel with a two-story verandah, built in 1894 and 1895 in the Ohio River oil and gas boom town of Sistersville. It was listed on the National Register in 1972. A search result says Charles and Kim Winslow bought it in 2010 and have run it as an inn since.',
  'Interior decor of the 1890s: a mosaic tile floor, oak furnishings and a tiled fireplace (Wikipedia, which describes the hotel as undergoing renovation in 2010). A search result says there is a restaurant and rooms; the present state of the interior was not checked.',
  'An 1895 boom-town hotel with its tile floor and fireplace.',
  'A working inn at 316 Charles Street; the town\'s page says it is open. Telephone 304-652-1312 (federal fire directory). The inn\'s own page was not read, so no hours are recorded. Street parking not checked.',
  [W('Wells Inn'),['WV Tourism: Wells Inn','https://wvtourism.com/company/wells-inn/']],
  brick='?',hours='?'),

N('rehoboth-church-union','Rehoboth Church','Union','wv','worship','standing',37.59,-80.50667,'exact','open','drive','','1785–1786',
  'A log Methodist church built in 1785 on land given by Edward Keenan, and dedicated in 1786 by Francis Asbury, the first Methodist bishop in the United States. Asbury came back at least three times in the next ten years to lead annual conferences here. Wikipedia calls it the oldest existing church building in West Virginia. Repairs began in 1927 and it is on the National Register (1974).',
  'A log building with a raised timber pulpit, galleries on three sides reached by a steep fixed ladder and held up by two big log pillars, and pews made of half-sawn logs (Wikipedia). The church\'s own listing says visitors see the original structure and furnishings, and an altar believed to be Asbury\'s is kept. A museum stands beside it.',
  'The oldest church building in West Virginia, log pews and all.',
  'Run as a church and museum, listed by the United Methodist Church\'s history commission (page read November 24, 2026). The way in is a gravel road from a marker on Route 3, about two miles east of Union. Visits at other times by calling the resident director. Parking not checked.',
  [W('Rehoboth Church'),['United Methodist Church history commission: Rehoboth Church and Museum','https://gcah.org/landmarks/rehoboth-church-and-museum/']],
  brick='no',hours='April 1 to October 31, Thursday to Saturday from 11 a.m. (end time not read); other times by appointment'),

N('locust-creek-covered-bridge','Locust Creek Covered Bridge','Hillsboro','wv','landmark','standing',38.07944,-80.25028,'exact','public','drive','','1870',
  'The only covered bridge left in Pocahontas County. R. N. Bruce was hired in 1870 to build it for $1,250, as a Warren double-intersection truss. The first bridge burned in 1888 and was replaced; in 1904 W. M. Irvine rebuilt it again, replacing the supports, trusses, siding and roof. The state bypassed it with a concrete span in 1990, and in 2002 it became a foot crossing. It is on the National Register (1981).',
  'A roofed wooden truss bridge about 114 feet long, closed to cars (Wikipedia). Walk across it; the road now goes round.',
  'The county\'s last covered bridge, now a footbridge.',
  'Kept up by the West Virginia Division of Highways (Wikipedia). On a county road about six miles from Hillsboro; pedestrians only. No hours. Parking not checked.',
  [W('Locust Creek Covered Bridge (West Virginia)')],
  brick='no'),

N('old-stone-tavern-moorefield','Old Stone Tavern','Moorefield','wv','landmark','standing',39.06111,-78.96972,'exact','view','drive','','1788',
  'A fieldstone tavern and home built in 1788 by Thomas Parsons, one of the earliest buildings in Moorefield. Frame sections were added about 1840, 1860 and 1900, and a cinder block apartment in the 1950s. It was listed on the National Register in 1979.',
  'The 1788 fieldstone core with its later frame wings and a front porch (Wikipedia). Whether it is open to visitors, and what is inside, was not checked.',
  'Moorefield\'s oldest stone building, a tavern from 1788.',
  'Ownership and use not checked; treat it as private and look from the street. Parking not checked.',
  [W('Old Stone Tavern (Moorefield, West Virginia)')],
  brick='no'),

N('old-main-bethany-college','Old Main, Bethany College','Bethany','wv','civic','standing',40.20578,-80.56031,'exact','view','drive','','1858–1871',
  'The main building of Bethany College, put up from 1858 to 1871 to a Gothic Revival design by James Keys Wilson of the Cincinnati firm of Walter and Wilson. Faculty member William Kimbrough Pendleton oversaw construction and chose its site on the hill. The college was the headquarters of Alexander Campbell, a founder of the Christian Church (Disciples of Christ). It is a National Historic Landmark (1990), and John F. Kennedy spoke in its Commencement Hall in 1960.',
  'A large Gothic Revival building with an arcade on the back (Wikipedia). It is still in use as classrooms, laboratories and the Commencement Hall. Visitor hours and what the public may enter were not checked.',
  'A working college hall in a village built round Alexander Campbell.',
  'Owned by Bethany College and in daily use; look from the campus roads and ask the college about going in. Parking not checked.',
  [W('Old Main (Bethany College)')],
  brick='?'),

N('center-point-covered-bridge','Center Point Covered Bridge','Center Point','wv','landmark','standing',39.38944,-80.63444,'exact','public','drive','','1888–1890',
  'A Long truss covered bridge ordered by the county court and built between 1888 and 1890 over Pike\'s Fork of McElroy Creek. The masons T. C. Ancell and E. Underwood charged $976.54 for the abutments; the carpenters John Ash and S. H. Smith charged $230. In 1983 it was one of only 17 covered bridges left in West Virginia. It is on the National Register (1983).',
  'A roofed wooden bridge on stone abutments (Wikipedia). Whether it still carries traffic or is closed to it was not checked.',
  'One of the 17 covered bridges West Virginia had left in 1983.',
  'On a county road near Center Point in Doddridge County; the managing body was not found. No hours. Parking not checked.',
  [W('Center Point Covered Bridge')],
  brick='no'),

N('fairfax-stone-thomas','Fairfax Stone','Thomas','wv','curio','marker',39.195,-79.4875,'exact','public','drive','','1746',
  'A boundary stone at the source of the North Branch of the Potomac River, set on October 23, 1746 to settle a dispute over the Fairfax land grant of Virginia and Maryland. It marks the corner where Grant, Preston and Tucker counties meet. The original stone, likely a plain rock, was moved by Virginia in 1833; the present marker is a later one. The four-acre state park around it dates from 1957, and the site is on the National Register (1970).',
  'A monument stone in a clearing at the end of a road, with a few picnic tables, where the river starts from beneath the stone (Wikipedia). No buildings or restrooms.',
  'The stone that fixed the western corner of Lord Fairfax\'s land.',
  'A West Virginia state park run by the Division of Natural Resources, about six miles north of Thomas (Wikipedia). Hours and fees not checked. Parking not checked.',
  [W('Fairfax Stone Historical Monument State Park')],
  brick='no'),

N('ralphsnyder-decagonal-barn','Ralphsnyder Decagonal Barn','Masontown','wv','curio','standing',39.5528,-79.7631,'site','view','drive','','1890',
  'A ten-sided barn built in 1890, a frame building with an unusual steeple-shaped cupola. It is the only 10-sided barn known to have been built in West Virginia. It was moved to its present site in 1981, which meant replacing parts of the structure and roof. It was listed on the National Register in 1985.',
  'The barn\'s ten sides and cupola, from the road (Wikipedia). A search result says the 1985 form listed it as privately owned and used for farming and as a museum; the present owner and any opening were not found.',
  'The only ten-sided barn in West Virginia.',
  'Probably private; look from the public road and do not enter the property. The Register point may be off the barn. Parking not checked.',
  [W('Ralphsnyder Decagonal Barn')],
  conf='mixed',brick='no'),

N('helvetia-swiss-village','Helvetia Village Historic District','Helvetia','wv','landmark','standing',38.7053,-80.2030,'area','open','drive','','1869–1939',
  'A village founded in 1869 and 1870 by Swiss settlers. Its 26 historic buildings in the village centre include early log houses and later frame buildings, several in Carpenter Gothic style. The district is on the National Register (1978).',
  'The Church (1882), Huber Inn (about 1880), the log Swiss Museum (about 1869), the Star Band Hall, the Cheese Haus, an original cabin of 1870, the Community Hall (1939) and Rudolph\'s Carpenter Shop (Wikipedia). Which of these are open to visitors was not checked.',
  'A Swiss mountain village in log and Carpenter Gothic.',
  'A living village of private homes and businesses along its roads; stay on the roads and ask before entering any building. The Swiss Historical Village\'s page would not open from here, so no museum hours are recorded. The pin is the middle of the district, not one building. Parking not checked.',
  [W('Helvetia Village Historic District')],
  conf='mixed',brick='?',hours='?'),

N('cheat-summit-fort','Cheat Summit Fort (Fort Milroy)','Huttonsville','wv','fort','traces',38.62444,-79.87667,'site','public','hike','','1861–1862',
  'The highest Union camp of the Civil War, on White Top, a spur of Cheat Mountain. Construction began on July 16, 1861, and it was named for Brigadier General Robert H. Milroy. It overlooked the Staunton–Parkersburg Turnpike. Snow came in August, horses froze in September, and the fort was given up in April 1862. It is on the National Register (1990).',
  'Earthworks, cabin sites and mounds over collapsed chimneys remain; a search result says the Forest Service interprets the site with signs, a trail and an overlook. Depressions said to be graves lie just south, though Wikipedia notes that statement has no source.',
  'A Union fort on a freezing mountaintop.',
  'On Monongahela National Forest land, which the Forest Service bought in 1987 (search result). Reached from U.S. Route 250 south of Huttonsville. Federal law protects the earthworks and artifacts: look, leave everything. Parking not checked.',
  [W('White Top')],
  conf='mixed',brick='no'),

N('blue-sulphur-springs-pavilion','Blue Sulphur Springs Pavilion','Blue Sulphur Springs','wv','landmark','standing',37.82831,-80.63917,'exact','public','drive','','1834',
  'The one building left of the Blue Sulphur Springs resort, built in 1834 by George Washington Buster to shelter the sulphur spring. The resort had a three-story, 200-room hotel and a bath house, and counted Henry Clay and Presidents Andrew Jackson and Martin Van Buren among its 1840s guests. It closed in 1859. The pavilion is a Greek Revival temple of twelve plastered brick columns, 32 feet 10 inches square, and was listed on the National Register in 1992.',
  'An open pavilion on a brick foundation faced with stone, with twelve plastered brick Doric columns and a marble basin where the spring flows in (Wikipedia). The Greenbrier Historical Society says it was rededicated July 1, 2023.',
  'A Greek Revival spring house, all that is left of a 200-room resort.',
  'The Greenbrier Historical Society\'s page (seen in a search result) says it owns the pavilion and that it is open to the public for viewing from 8 a.m. to 5 p.m. daily; another source names a different owner, so ownership is not settled. Address 8010 Blue Sulphur Springs Road. Parking not checked.',
  [W('Blue Sulphur Springs Pavilion'),['Greenbrier Historical Society: Blue Sulphur Springs Pavilion','https://greenbrierhistorical.org/preservation/blue-sulphur-springs-pavillion/']],
  conf='mixed',brick='no',hours='Open for viewing daily, 8 a.m. to 5 p.m. (Greenbrier Historical Society, seen in a search result)'),

N('valley-furnace-barbour','Valley Furnace (Fanny Furnace)','Valley Furnace','wv','industry','ruins',39.19611,-79.8675,'site','public','drive','','1847–1855',
  'A stone blast furnace built about 1847 by George W. Bryan, who named it Fanny for his wife, after John Johnson found iron ore here in 1835. It made pig iron with charcoal from ore nodules dug in nearby surface mines, and a steam-driven blast replaced the water-driven one about 1850. Bryan died in 1853, and the furnace stopped about 1855. Twenty to thirty houses once stood near it. It was listed on the National Register in 2023.',
  'A rough, sloping stone stack, its upper part fallen into rubble; the wooden buildings and houses are gone (Wikipedia). A state marker and roadside rest area stand beside it on Route 38 (search result).',
  'A ruined iron furnace beside the highway.',
  'An undeveloped park of about half an acre, given to the Barbour County Commission (Wikipedia gives 2002 in one place and December 2020 in another for the transfer). Visible from Route 38. Parking not checked.',
  [W('Valley Furnace')],
  conf='mixed',brick='no'),
]

PIN_NOTES={
 'peter-tarr-furnace-weirton':'The point is the Register list point, beside Kings Creek Road; the furnace itself could not be made out under the trees on the aerial or LiDAR, so the pin marks the area.',
 'old-stone-house-pennsboro':'The point is the Register list point; checked on the aerial.',
 'wells-inn-sistersville':'The point is the street address 316 Charles Street, found with the ArcGIS geocoder; the Register point fell on a park.',
 'rehoboth-church-union':'The point is the Register list point; checked on the aerial.',
 'locust-creek-covered-bridge':'The point is the Register list point; checked on the aerial.',
 'old-stone-tavern-moorefield':'The point is the Register list point; checked on the aerial.',
 'old-main-bethany-college':'The point is the Register list point; checked on the aerial.',
 'center-point-covered-bridge':'The point is the Register list point; a roofed structure over the creek is under it on the aerial.',
 'fairfax-stone-thomas':'The point is the Register list point; checked on the aerial.',
 'ralphsnyder-decagonal-barn':'The point is the Register list point; checked on the aerial.',
 'helvetia-swiss-village':'The point is the middle of the district; it marks the village, not one building.',
 'cheat-summit-fort':'The point is the Register list point; checked on the aerial and LiDAR.',
 'blue-sulphur-springs-pavilion':'The Register point fell in woods about 220 m west; the pavilion was found on the aerial beside the road and the pin put on it.',
 'valley-furnace-barbour':'The point is the Wikipedia point; checked on the aerial and LiDAR.',
}
