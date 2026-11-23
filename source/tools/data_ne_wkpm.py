# November 23, 2026: a third scatter across Nebraska, the state with the fewest places on the map (45 before this batch,
# 29 of them in Omaha and the Missouri River towns of the southeast). Claimed with tools/choose.py --thinnest (ne).
# Sources read in this session: National Register and National Historic Landmark forms from NPGallery (read as text with
# page.py) for Fort Atkinson, the William Jennings Bryan House, the Picotte hospital, the Genoa Indian school, the Midwest
# Theater, the Harold Lloyd birthplace, the Pawnee County Courthouse, the Bell Bridge and the Red Cloud depot; the Museum of
# the Fur Trade's own visit page (hours, address, admission); the Friends of Fort Atkinson's page; Wikipedia for outlines
# only. history.nebraska.gov and outdoornebraska.gov answer 403 to page.py, so most hours of state sites were not read and
# say so. Pins are the Register or Wikipedia points, checked on the aerial.
# Red brick: the Genoa shop building is 'some' (red brick painted cream on three sides, by its Register form); the Pawnee
# County Courthouse is 'no' (tan brick on limestone, by its form); the Picotte hospital, the Lloyd house, the Red Cloud depot
# are wood frame ('no'); the Bell Bridge is steel ('no'); the rest are '?'.
from data_b import N
from data_ma import W

BATCH={'key':'ne_wkpm','label':'Nebraska: a third scatter across the state','added':'2026-11-23 21:28'}

NPG=lambda ref,label: ['National Register form: '+label,'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/'+ref+'_text']
NHL=lambda ref,label: ['National Historic Landmark form: '+label,'https://npgallery.nps.gov/NRHP/GetAsset/NHLS/'+ref+'_text']
NGPC='Nebraska Game and Parks Commission'

PLACES=[
N('fort-atkinson-fort-calhoun','Fort Atkinson','Fort Calhoun','ne','fort','standing',41.4533,-96.0122,'site','open','drive','forts','1819–1827',
  'The first U.S. Army post west of the Missouri River, begun in 1819 on the bluff where Lewis and Clark had met the Oto and Missouria in 1804. More than 1,000 people lived in and around it; scurvy killed over 200 of the 1,120 soldiers in the first winter (Wikipedia). The army left in 1827. The state took the site in 1963 and rebuilt the fort in the 1980s and 1990s.',
  'The log barracks quadrangle with its two corner bastions and the powder magazine are reconstructions on the original ground; the original fort is under the grass and was dug in the 1950s to 1980s. The Register form describes the site as little disturbed apart from those digs. A military museum is on site. Interior not checked.',
  'The first fort on the far side of the Missouri, rebuilt on its own footings.',
  'A state historical park of the '+NGPC+' about a mile east of Fort Calhoun; a Nebraska park entry permit is normally needed for a vehicle. The Friends of Fort Atkinson hold living-history days (Wikipedia says the first weekend of each month, May to October; the Friends\' own page lists a two-day event on October 3 and 4, 2026). Ordinary hours were not read: outdoornebraska.gov refuses automated requests.',
  [W('Fort Atkinson (Nebraska)'),NHL('66000454','Fort Atkinson'),['Friends of Fort Atkinson','https://www.fortatkinsononline.org']],brick='?',hours='?'),
N('genoa-indian-school','Genoa U.S. Indian Industrial School','Genoa','ne','inst','standing',41.44955,-97.72413,'area','open','drive','','1884–1934',
  'The fourth boarding school the federal government opened away from the reservations, built in 1884 on the former Pawnee reservation to teach Native children European-American ways. It grew from 74 pupils to as many as 599 and more than 30 buildings, and closed in 1934 (the Register form says 1933). At least 86 children died there; researchers have since named more than a hundred.',
  'The 1907 shop building, a two-storey brick block of 34 by 90 feet, now the museum. Its red brick was painted or stained cream on the south, east and west sides (Register form). The big dormitories, dining hall and classrooms are gone; farm and industrial buildings remain in farm country. Museum exhibits include a classroom and banners from the tribes whose children attended. Interior not checked.',
  'A boarding school where children were taken from forty tribal nations, and what is left of it.',
  'The museum is run by the Genoa U.S. Indian School Foundation; other surviving buildings are on private ground, so look from the road. Its hours and the exact street address were not found in a page that could be read. Parking not checked.',
  [W('Genoa Indian Industrial School'),NPG('78001706','Genoa U.S. Indian Industrial School'),['Genoa Indian School Digital Reconciliation Project','https://www.genoaindianschool.org']],brick='some',hours='?',conf='mixed'),
N('bordeaux-trading-post-chadron','Bordeaux Trading Post (Museum of the Fur Trade)','Chadron','ne','industry','standing',42.82364,-102.92812,'site','open','drive','','1837–1876',
  'A trading post set up beside Bordeaux Creek in the fall of 1837 for the American Fur Company, run by James Bordeaux, who traded buffalo robes with the Brule Sioux. The ruins were gone by the time homesteaders came in 1885. Wikipedia gives its building as 1845–46 and its founding as 1837; the sources differ, so the dates here are loose.',
  'A reconstruction of the post, built in 1956 on the original foundation stones: hand-hewn timber walls follow the old lines, and the hearthstones and threshold stones are the originals found in place (Wikipedia, from the Register nomination). It is the centre of the Museum of the Fur Trade, with more than 6,000 objects, including an old point blanket dated 1775. Photography is allowed inside.',
  'A fur-trade post rebuilt on its own postholes.',
  'Museum of the Fur Trade, 6321 U.S. Highway 20, three miles east of Chadron; a private non-profit museum. Admission $6 for adults 18 and over, children free with an adult (its own visit page, read November 2026). Parking at the museum.',
  [W('Bordeaux Trading Post'),['Museum of the Fur Trade: visit','https://www.furtrade.org/visit']],brick='no',
  hours='May 1 to Oct 31: daily 8 a.m. to 5 p.m.; Nov 1 to Apr 30: by appointment only',conf='mixed'),
N('bryan-house-fairview-lincoln','William Jennings Bryan House (Fairview)','Lincoln','ne','landmark','standing',40.79581,-96.65164,'exact','view','drive','','1902–1903',
  'Fairview, the home of William Jennings Bryan from 1902 to 1921, built in 1902–03 for $17,000 on a hilltop east of Lincoln. In 1921 Bryan gave the house and ten acres to the Methodist Conference for a hospital, and it became a nurses\' home. The Junior League and the State Historical Society restored it in the early 1960s to open to the public.',
  'A large Classical Revival and Queen Anne house with a turret and varied rooflines. In 1908 the Bryans closed in the porch as a reception room. A 1964 hospital wing rises just beside the west wall (National Historic Landmark form, 1960s). Wikipedia says the ground floor has Bryan exhibits and the upper floors house the Bryan Institute. Interior not checked.',
  '',
  'On the Bryan Health campus at 52nd and A Streets; the hospital grounds are private. Whether it opens to visitors now, and when, was not found on a page that could be read: ask at the hospital before going. Parking not checked.',
  [W('William Jennings Bryan House (Lincoln, Nebraska)'),NHL('66000947','William Jennings Bryan House')],brick='?',hours='?'),
N('picotte-hospital-walthill','Susan La Flesche Picotte Memorial Hospital','Walthill','ne','civic','standing',42.152,-96.49544,'site','view','drive','','1912–1945',
  'The hospital Dr. Susan La Flesche Picotte, a physician of the Omaha tribe and among the first Native women to earn a medical degree, founded in 1913 as the first privately funded hospital on a reservation. The frame Craftsman building went up in 1912–13 to the plans of William Steele of Sioux City. It closed in 1945 and reopened in 1989 as a heritage site.',
  'A one-and-a-half-storey wooden building with a long recessed porch, 42 by 78 feet, on a hill above the village; its wood siding is now covered with asbestos shingles. The ward plan is little changed. In 1992 three ground-floor rooms held a small museum on church missions and the Omaha and Winnebago peoples. Interior not checked.',
  '',
  'At 505 Matthewson Street, on the Omaha reservation. Whether it is open to visitors now was not found on a page that could be read; ask before going. Look from the street. Parking not checked.',
  [W('Susan La Flesche Picotte'),NHL('88002762','Susan LaFlesche Picotte Memorial Hospital')],brick='no',hours='?'),
N('midwest-theater-scottsbluff','Midwest Theater','Scottsbluff','ne','civic','standing',41.863611,-103.662222,'exact','view','drive','','1946',
  'A downtown movie house that opened May 3, 1946, built by the company that ran dance halls and cinemas in Scottsbluff, Morrill and Bridgeport from the 1920s. The owners later gave it to the Oregon Trail Community Foundation to run as a performing-arts and entertainment centre.',
  'Streamline Moderne: a two-storey brick building 140 by 50 feet on a reinforced-concrete base, with a stucco front and tower and satin aluminum handrails that curve with the stairs (Register form, 1997). Interior and events not checked.',
  '',
  'At 1707 Broadway, in the middle of downtown Scottsbluff. It is a working venue run by a foundation; its show times and tours were not read, so check its own page before going. Street parking nearby; not checked.',
  [NPG('97000728','Midwest Theater')],brick='?',hours='?'),
N('harold-lloyd-birthplace-burchard','Harold Lloyd Birthplace','Burchard','ne','landmark','standing',40.14966,-96.34921,'site','view','drive','','1893',
  'A small frame house in the village of Burchard where the silent-film comedian Harold Lloyd was born in 1893. The family left in 1897.',
  'A one-storey vernacular frame house with a shed, a privy and a garage whose dates are not known (Register form, 1993). Interior not checked.',
  '',
  'Private property as far as the sources say; look from the street. Whether it opens to visitors was not found. Parking not checked.',
  [NPG('93001403','Harold Lloyd Birthplace')],brick='no',hours='?'),
N('pawnee-county-courthouse-pawnee-city','Pawnee County Courthouse','Pawnee City','ne','civic','standing',40.108056,-96.153333,'exact','view','drive','','1911–1912',
  'The county courthouse on the square at Pawnee City, built in 1911–12 to the design of Nebraska architect William P. Gernandt, who designed ten courthouses between 1910 and 1923. It is a "county citadel" of the type with a flat roof and raised basement, and shares features with the Merrick County Courthouse.',
  'Classical Revival: tan brick walls over a raised ashlar limestone basement, a portico of four colossal stone columns on the north front reached by twin stone stairways, stone balustrades, and a third storey hidden behind a tall brick parapet (Register form). Interior not checked.',
  '',
  'A working county building on the courthouse square; look from the public street. Hours not checked. Street parking round the square; not checked.',
  [W('Pawnee County Courthouse (Nebraska)'),NPG('89002232','Pawnee County Courthouse')],brick='no',hours='?'),
N('bell-bridge-valentine','Bell Bridge','Valentine','ne','landmark','standing',42.895,-100.322222,'site','public','drive','','1902–1903',
  'A pin-connected steel Pratt through-truss bridge over the Niobrara River, ordered by the Cherry County commissioners in 1902 from the Canton Bridge Company of Ohio and finished in November 1903 on steel rolled by Cambria. It was one of only four truss bridges in the county left standing after the flood of February 1916.',
  'The truss itself, which still carries traffic and is little altered except for repairs (Register form).',
  '',
  'The bridge carries a county road (the Register form calls it a county road bridge) about 12 miles northeast of Valentine, so the road is public; the land beside it is not mapped as public and may be private, so stay on the road and park without blocking it. Parking not checked.',
  [NPG('92000752','Bell Bridge')],brick='no',hours='?',conf='mixed'),
N('burlington-depot-red-cloud','Burlington Depot','Red Cloud','ne','rail','standing',40.07737,-98.52174,'exact','view','drive','stations','1897',
  'A combination passenger and freight station on the Burlington line, whose two-storey part was built in 1897 with the agent\'s rooms upstairs. Eight passenger trains a day once stopped here. Willa Cather knew this building in her last years in Red Cloud. It was moved less than 300 feet to a spot just south-southwest of its first site, in the mid-1960s, so that it would not be taken down.',
  'A wood-frame depot about 25 by 100 feet. Most of the west wing has gone, leaving a stub for the coal room and a truncated gable (Register form, 1981). Interior not checked.',
  '',
  'In Red Cloud on the old railroad ground south of the business district; who owns and opens it now was not found. Look from the public way. Parking not checked.',
  [W('Burlington Depot (Red Cloud, Nebraska)'),NPG('81000376','Burlington Depot')],brick='no',hours='?',conf='mixed'),
N('ash-hollow-garden-county','Ash Hollow and Windlass Hill','Lewellen','ne','landmark','traces',41.29806,-102.12,'area','public','drive','','1855',
  'A spring and cave used by people for some 1,500 years, then a hard drop on the Oregon and California trails, where wagons were let down Windlass Hill at about 25 degrees. In September 1855 U.S. troops attacked a Brule Sioux camp near here, killing 86 people (Wikipedia, which cites a state marker). The cave is a National Historic Landmark.',
  'Wagon ruts are visible on Windlass Hill; the cave is at the park too, and a visitor center (built 1978) looks over the canyon. The two sites are 2.5 miles apart. Not checked: what is open or staffed now.',
  '',
  'Ash Hollow State Historical Park, about 5 miles south of Lewellen, run by the '+NGPC+'; a state park entry permit is normally needed. Hours and the trail to the ruts were not read: outdoornebraska.gov refuses automated requests. The pin is the Register point for the cave, not the hill.',
  [W('Ash Hollow State Historical Park')],brick='no',hours='?',conf='mixed'),
]

PIN_NOTES={
'fort-atkinson-fort-calhoun':'Moved from Wikipedia\'s point, which fell in the open field north-west, onto the walled reconstruction seen on the aerial.',
'genoa-indian-school':'The Register point for the school grounds, checked on the aerial.',
'bordeaux-trading-post-chadron':'The street-address point for the museum at 6321 U.S. 20; the Wikipedia point fell in a field and on the railroad.',
'bryan-house-fairview-lincoln':'Wikipedia point for the house, checked on the aerial.',
'picotte-hospital-walthill':'The street-address point for 505 Matthewson Street; the Landmark list\'s point fell in a field.',
'midwest-theater-scottsbluff':'Register point on Broadway, checked on the aerial.',
'harold-lloyd-birthplace-burchard':'Register point, checked on the aerial.',
'pawnee-county-courthouse-pawnee-city':'Register point on the square, checked on the aerial.',
'bell-bridge-valentine':'Register point over the Niobrara, checked on the aerial.',
'burlington-depot-red-cloud':'OpenStreetMap\'s point for the depot on Seward Street; the Register point fell on the railroad yard.',
'ash-hollow-garden-county':'The Register point for Ash Hollow Cave; Windlass Hill is 2.5 miles away.',
}
