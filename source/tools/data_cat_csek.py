# November 19, 2026: Sullivan County, New York, the Upper Delaware and the D&H Canal country (region cat, drawn at
# random by tools/choose.py --claim, which offered Windsor, Narrowsburg and Bovina Center; the Atlas had one place within
# 25 km of Narrowsburg). Roebling's aqueduct and the Minisink battleground at Minisink Ford, the D&H Canal linear park in
# Mamakating, Narrowsburg, Tusten, Cochecton and Callicoon on the river, the county's stone arch and covered bridges, and
# the Borscht Belt synagogues and theatre round Woodridge, South Fallsburg and Livingston Manor.
# Sources opened in this session: Wikipedia as raw text (tools/wiki_raw.py, including the Sullivan County Register list),
# the Callicoon Downtown Historic District form through NPGallery, and through tools/page.py the National Park Service's
# Upper Delaware pages, Sullivan County's park pages and brochures, HMdb markers, the Town of Cochecton's railroad
# history page, the NY State Covered Bridge Society, gribblenation.org, the River Reporter, the Pike County Courier,
# Spectrum News and the Times Hudson Valley. Most Register forms here are NPGallery placeholders.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
def NP(r): return ['National Register form (NPGallery)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/'+r+'_text']
def HM(m,t): return ['HMdb: '+t,'https://www.hmdb.org/m.asp?m='+m]
NPSH=L('NPS: Upper Delaware operating hours','https://www.nps.gov/upde/planyourvisit/hours.htm')
SCP=L('Sullivan County parks brochure (2024)','https://www.sullivanny.gov/sites/default/files/departments/Parks/2024%20Sullivan%20County%20Parks%20Brochure.pdf')

BATCH={'key':'cat_csek','label':'Sullivan County, NY: Roebling\'s aqueduct, the D&H Canal, the river hamlets and the Catskill bridges','added':'2026-11-19 16:01'}

PLACES=[
N('roebling-delaware-aqueduct','Roebling\'s Delaware Aqueduct and toll house','Minisink Ford, Town of Highland','cat','canal','standing',41.48257,-74.98441,'exact','public','walk','canal','1847–1849',
  'Begun in 1847 and opened in 1849, this carried the Delaware & Hudson Canal over the Delaware River in a water-filled trough hung from wire cables, so canal boats no longer crossed by rope ferry in the path of the timber rafts. John A. Roebling, later engineer of the Brooklyn Bridge, designed it with Russell F. Lord. After the canal closed in 1898 it was drained and made a road bridge, a toll bridge until 1979. The National Park Service bought it in 1980, rebuilt the superstructure to Roebling\'s plans in 1986 and put back the icebreakers, towpaths and trough walls in 1995. It is the oldest existing wire suspension bridge in the United States.',
  'The NPS says almost all the ironwork (cables, saddles, suspenders) is what was installed when it was built. Walk across on the pedestrian paths on either side; one lane of cars uses the old trough. On the New York end the Roebling Bridge Toll House has self-guided exhibits on the aqueduct and the canal, and a gravel and grass D&H Towpath Trail of a quarter mile starts at the New York lot. The Minisink battleground is a mile up County Route 168.',
  'Walk the oldest wire suspension bridge in the country, built to carry a canal over a river.',
  'Upper Delaware Scenic and Recreational River (National Park Service). Park in the New York lot by the toll house (4225 State Route 97, Barryville), where the towpath trail starts. Per the NPS hours page the bridge is open year-round, 24 hours a day, though the walkways may close in snow; the towpath trail is open dawn to dusk and may close after high water. Pets allowed; restrooms. The bridge carries traffic: keep to the walkways.',
  [W('Roebling\'s Delaware Aqueduct'),L('NPS: Roebling\'s Delaware Aqueduct','https://www.nps.gov/places/roeblings-delaware-aqueduct.htm'),NPSH,HM('20596','Roebling\'s Delaware Aqueduct')],
  th=[41.48350,-74.98373],thn='NPS lot by the toll house, State Route 97',brick='?',
  hours='Bridge open all year, 24 hours; toll house exhibits daily 9 a.m. to 4 p.m.; towpath trail dawn to dusk'),

N('minisink-battleground-park','Minisink Battleground Park','Minisink Ford, Town of Highland','cat','fort','marker',41.48858,-74.97045,'site','public','hike','','1779; monument 1879',
  'On July 22, 1779 militia from Goshen, Warwick and Sussex County who had followed Joseph Brant\'s raiders up the Delaware from the Minisink settlements were caught on the hillside above Minisink Ford; by the end of the day between forty-five and fifty of them were dead. It was the only Revolutionary War battle in the upper Delaware valley. The Minisink Valley Historical Society set the ground aside in the 1890s to stop bluestone quarrying there, and the county keeps it as a 57-acre park.',
  'Nothing from 1779 stands (Wikipedia). The Battleground Trail climbs from the interpretive center to the bluestone Minisink Battle Monument, capped with a glacial boulder and dedicated in 1879 on the "last stand" site, and to Sentinel Rock and Hospital Rock, where the county brochure says the wounded were sheltered inside the militia\'s square. The Old Quarry Trail passes the park\'s bluestone workings (not checked on the ground).',
  'A Revolutionary battlefield saved from the bluestone quarrymen.',
  'Sullivan County park, 58 County Road 168, about a mile northeast of State Route 97 at Minisink Ford. Parking, restrooms and the interpretive center by the lot; picnic pavilion by fee. Seasons differ between the county\'s own pages: its 2025 park brochure says open Mother\'s Day weekend to Columbus Day, its park page "open daily 8:00 am - Dusk". The Delaware Company runs programs here under contract.',
  [W('Battle of Minisink'),L('Sullivan County: Battle of Minisink Park brochure (2025)','https://sullivanny.gov/sites/default/files/departments/Parks/Battle%20of%20Minisink%20Park%20Brochure%202025.pdf'),L('Sullivan County: Minisink Battleground Park','https://sullivanny.gov/Departments/ParksRecreation/Minisink'),HM('20509','Minisink Battle Monument'),SCP],
  th=[41.48714,-74.96977],thn='Park lot on County Route 168',brick='no',
  hours='Mother\'s Day weekend to Columbus Day (brochure); 8 a.m. to dusk'),

N('dh-canal-linear-park-mamakating','D&H Canal Linear Park: locks, dry dock and the Boothroyd house','Phillipsport to Wurtsboro, Town of Mamakating','cat','canal','ruins',41.63231,-74.45307,'site','public','walk','canal','1828–1898',
  'The Delaware & Hudson Canal ran 108 miles from Honesdale, Pennsylvania to Kingston with 108 locks, carrying anthracite from 1828 until 1898; Wurtsboro takes its name from the Wurts brothers who planned it. Sullivan County began buying the canal here in 1969 (Locks 42, 43 and 44) and now has over 83 acres, five locks and a dry dock along about three and a half miles of towpath between Wurtsboro and Phillipsport.',
  'Stone lock chambers, a dry dock and waste weirs along the towpath, with signs explaining them. At the Bova Road access stand the white 1850s canal-side house of the Boothroyd family, who ran a boatyard on the north side of the property (closed; the county invites visitors to look in the windows), the remains of the boatyard and a lock, and the 2011 interpretive center.',
  'Walk a canal towpath past the locks of the coal canal that named Wurtsboro.',
  'Sullivan County park beside State Route 209. Three accesses: the D&H Canal Interpretive Center lot at 16 Bova Road between Summitville and Phillipsport (pin), the Summitville access by Ferguson Road, and Hornbeck\'s Basin (3346 Route 209, half a mile north of Wurtsboro). Free. Leashed dogs; no motor vehicles or horses; respect the adjoining private land. The county page gives the park as open dawn to dusk on one line and 8 a.m. to dusk on another; the interpretive center is closed for the 2026 season.',
  [L('Sullivan County: D&H Canal Interpretive Center and Linear Park','https://sullivanny.gov/Departments/ParksRecreation/DelawareHudson'),SCP,W('Delaware and Hudson Canal')],
  th=[41.63247,-74.45262],thn='Bova Road parking area',brick='no',
  hours='Trails all year, dawn to dusk (county page also says 8 a.m. to dusk); interpretive center closed for 2026'),

N('van-tran-flat-bridge','Van Tran Flat (Livingston Manor) Covered Bridge','Livingston Manor, Town of Rockland','cat','landmark','standing',41.91472,-74.83194,'exact','public','drive','','1860',
  'John Davidson built this single-span covered bridge over Willowemoc Creek in 1860, first called the Motts Flats Bridge; it is the oldest surviving covered bridge in Sullivan County. It was closed and abandoned in 1972 and restored by the county from 1984, reopening the next year with laminated arches added for strength.',
  'A wooden Town lattice truss with a laminated arch, open slots under the eaves and four buttresses at each end. Its length is disputed: Wikipedia gives 117 feet (the state covered bridge society\'s figure), 98 feet from two older accounts, and the county 103 feet. It leads into the county\'s covered bridge park, where people fish the Willowemoc.',
  '',
  'Sullivan County\'s Livingston Manor Covered Bridge Park, 130 Covered Bridge Road, about a mile outside Livingston Manor. Parking by the bridge; picnic areas and portable toilets. Grounds open daily 8 a.m. to dusk; facilities May to October (county page).',
  [W('Van Tran Flat Bridge'),L('Sullivan County: Livingston Manor Covered Bridge Park','https://sullivanny.gov/Departments/ParksRecreation/LivingstonManor'),SCP],
  conf='mixed',th=[41.91406,-74.83155],thn='Covered bridge park lot',brick='no',hours='Grounds daily 8 a.m. to dusk; facilities May to October'),

N('beaverkill-covered-bridge','Beaverkill Covered Bridge','Beaverkill Campground, Town of Rockland','cat','landmark','standing',41.98156,-74.83617,'exact','public','drive','','1865',
  'Built in 1865 as one of the first crossings of the Beaver Kill in what was still a barely settled part of the Catskills, this hemlock lattice-truss bridge now stands inside the Beaverkill State Campground, the second public campground in the Catskill Park. In 1948 the town planned to replace it with a metal bridge and gave up the idea after local opposition. Which of three men built it is disputed.',
  'A 98-foot hemlock lattice truss with extra diagonals at the ends, an unusual variant of Ithiel Town\'s design, on dry-laid fieldstone abutments now faced in concrete (Wikipedia). It carries Conklin Road across the river.',
  '',
  'In the state\'s Beaverkill Campground on Campsite Road (County Route 30), north of Roscoe; the bridge carries a town road. No parking lot is mapped here; campground rules, fees and seasons were not checked (DEC page not read).',
  [W('Beaverkill Bridge')],brick='no'),

N('halls-mills-covered-bridge','Halls Mills Covered Bridge','Halls Mills, Town of Neversink','cat','landmark','standing',41.89012,-74.58985,'exact','public','walk','','1906–1912',
  'A single-span Town lattice covered bridge over the Neversink River, begun in 1906 and finished in 1912 by David Benton with helpers; it was taken out of road use in 1963. The Town of Neversink owns it and shares its upkeep with the county. One dry-stacked stone abutment was badly damaged in the 2011 floods of Irene and Lee.',
  'About 119 feet of bridge on stone abutments, beside the abandoned stretch of Hunter Road. Sources disagree on whether you may walk through it: Wikipedia says it is now posted closed to pedestrians, the state covered bridge society that it carries foot traffic. Look from the bank or the old road if it is posted.',
  '',
  'Town of Neversink. From Curry on State Route 55 take County Route 19 north almost 3 miles, turn left on Hunter Road for about 0.3 miles, park, and take the abandoned road on the left to the bridge (NY State Covered Bridge Society). No mapped lot; parking is along Hunter Road. Do not cross if posted closed.',
  [W('Halls Mills Bridge (New York)'),L('NY State Covered Bridge Society: Halls Mills','https://www.nycoveredbridges.org/?p=168')],
  conf='mixed',brick='no'),

N('stone-arch-bridge-kenoza-lake','Stone Arch Bridge Historical Park','Kenoza Lake, Town of Delaware','cat','landmark','standing',41.74806,-74.95417,'exact','public','drive','','1873 or 1880–1882',
  'A three-arched bridge of hand-cut stone over the East Branch of Callicoon Creek, built by the Swiss immigrants Henry and Philip Hembt and restored by the county in 1980–81. Its date is not settled: Wikipedia gives 1873, the county\'s park brochure 1880 and its park page 1882.',
  'The three stone arches carry an arched roadway; the county keeps the 20 acres round it as a park with a walk on the Worthington Trail, fishing in the creek, a playground and a picnic area. No swimming.',
  '',
  'Sullivan County park, 25 Stone Arch Road, Kenoza Lake (off State Route 52). Free. Grounds open daily 8 a.m. to dusk; facilities May to October (county page). No lot is mapped; park at the county park.',
  [W('Stone Arch Bridge (Kenoza Lake, New York)'),L('Sullivan County: Stone Arch Bridge Historical Park','https://sullivanny.gov/Departments/ParksRecreation/StoneArchBridge'),SCP],
  conf='mixed',brick='no',hours='Grounds daily 8 a.m. to dusk; facilities May to October'),

N('tusten-stone-arch-bridge','Tusten Stone Arch Bridge and the lost Tusten settlement','Tusten','cat','landmark','standing',41.55611,-75.01944,'exact','public','walk','','1896',
  'A two-arched stone bridge of 1896, about 51 feet long, over the Tenmile River just above its mouth on the Delaware. It served the settlement of Tusten, named for Lt. Col. Benjamin Tusten, the Goshen surgeon killed at Minisink while tending the wounded; a state marker of 2020 says homes, stores and mills stood here by about 1875, shipping bluestone by the Erie and rafting lumber down the river. Since 1927 the land has belonged to the Greater New York Councils of the Boy Scouts as the Ten Mile River scout camps, and the hamlet is gone.',
  'The stone bridge itself; a local historian quoted in the River Reporter says that from the bridge there is little else of the village to be seen. The 1856 Ten Mile River Baptist Church stands near by on Route 97.',
  'A hamlet\'s stone bridge left standing inside a scout reservation.',
  'Owned by the Boy Scouts\' Greater New York Councils. Gribblenation (2020) says that by an agreement with the National Park Service the bridge is open to the public along the start of the Tusten Mountain Trail; the NPS says that trailhead is beside its Ten Mile River Access on Crawford Road (about 10 cars, seasonal toilet). NPS river accesses are closed 10 p.m. to 5 a.m. Keep to the trail; the rest is scout camp.',
  [W('Tusten Stone Arch Bridge'),L('Gribblenation: Tusten Stone Arch Bridge','https://gribblenation.org/2020/11/tusten-stone-arch-bridge-new-york.html'),L('NPS: Ten Mile River Access','https://www.nps.gov/places/ten-mile-river-access.htm'),L('River Reporter: Finding Tusten village','https://www.riverreporter.com/stories/funding-tusten-village,58276'),HM('167262','Ten Mile River')],
  th=[41.553348,-75.017845],thn='NPS Ten Mile River Access lot',brick='no',hours='NPS river access closed 10 p.m. to 5 a.m.'),

N('ten-mile-river-baptist-church','Ten Mile River (Tusten) Baptist Church','Tusten','cat','worship','standing',41.55997,-75.01641,'site','view','drive','','1856',
  'A small frame meeting house of 1856 with modest Greek Revival detail, built for the Tusten settlement on the Tenmile River. Its bell tower and spire are a reconstruction. The churchyard holds the grave of Gustavus A. Neumann, founding editor of the New Yorker Staats-Zeitung.',
  'The white frame church and its old cemetery. Interior not checked.',
  '',
  'On State Route 97 at the Cochecton Turnpike. Whether it holds services or opens was not found; view from the road and the cemetery. Owner not checked.',
  [W('Ten Mile River Baptist Church'),L('River Reporter: Finding Tusten village','https://www.riverreporter.com/stories/funding-tusten-village,58276')],brick='no'),

N('arlington-hotel-narrowsburg','Arlington Hotel (Delaware Valley Arts Alliance)','Narrowsburg','cat','hotel','standing',41.60842,-75.06111,'exact','open','drive','','1894',
  'A four-story frame hotel built in 1894 above the Big Eddy of the Delaware, first run by J. G. Gutheil, that put up river travellers and explorers in the 1890s. In the 1920s George Oellrich bought it for a general store. It now houses the Delaware Valley Arts Alliance, the arts council for Sullivan County.',
  'Five bays wide with a second-story porch across the south front; the upper floors are clapboard, the ground floor modern siding and permastone. Inside are the alliance\'s two galleries and shop. Narrowsburg\'s Main Street round it carries the Tusten Historical Society\'s numbered building markers.',
  '',
  'Delaware Valley Arts Alliance, 37 Main Street, Narrowsburg. Street parking. Hours are from a Pike County Courier notice of 2026, not the alliance\'s own site, which refused the page tool.',
  [W('Arlington Hotel (Narrowsburg, New York)'),HM('120712','Arlington Hotel'),L('Pike County Courier: DVAA\'s first exhibits of 2026','https://www.pikecountycourier.com/entertainment/dvaa-s-first-exhibits-of-2026-LE5512049')],
  brick='no',hours='Gallery and shop Thursday to Sunday 11 a.m. to 4 p.m., and by appointment (2026 notice)'),

N('cochecton-railroad-station','Cochecton Erie Railroad station','Cochecton','cat','rail','standing',41.71735,-75.04481,'area','view','drive','stations','c. 1850',
  'Built about 1850 by the Erie as a freight house, this is said to be the oldest surviving railroad station in New York State; when the line opened in 1851 Cochecton had a passenger station as well, later pulled down. A trucking business that used it for storage meant to demolish it in 1992, so the Cochecton Preservation Society took it apart, stored the pieces and re-erected the hand-hewn frame on donated land about a mile and a half up the track.',
  'A large one-and-a-half-story frame building with Greek Revival cornice, frieze, windows and doors restored, and the ticket office bay window rebuilt from a 1910 photograph. The town says the interior was still being restored; interior not checked.',
  '',
  'Cochecton Preservation Society, on State Route 97 just north of Cochecton. Opening times not found: view from the road. The railroad beside it is active: keep off the tracks.',
  [W('Cochecton station'),L('Town of Cochecton: Railroad history','https://townofcochectonny.org/our-community/arts-culture/railroad-history/')],
  brick='no'),

N('callicoon-downtown','Callicoon: the Erie depot, the Western Hotel and Main Street','Callicoon, Town of Delaware','cat','town','standing',41.76629,-75.05774,'site','public','drive','stations','1848–1948',
  'Callicoon Depot grew round the Erie Railroad\'s station after the line reached the mouth of Callicoon Creek in 1848, and German families came to settle the hills behind it. The first depot burned in 1899 and was replaced by the present Shingle Style station. The commercial streets along the tracks were rebuilt after a fire with two-story frame stores, and the hamlet\'s core was listed as a historic district in 2016.',
  'The 1899 depot with its broad hipped roof on braced eaves; the Western Hotel, whose 1852 core is said to be the oldest commercial building in the hamlet, enlarged in 1885 with an opera house wing and a mansard roof; the Delaware House, a three-story hotel opposite the depot; the 1948 Quonset-hut movie theatre with its Art Deco front; and up the hill the 1871 Methodist church and 1889 parsonage. The district form describes it all; current uses not checked.',
  '',
  'Public streets of the hamlet on State Route 97 and the river; street parking. The Erie line through Callicoon is an active railroad (Norfolk Southern): keep off the tracks.',
  [NP('16000390'),HM('121835','Erie Train Station')],brick='?'),

N('st-josephs-seraphic-seminary','St. Joseph\'s Seraphic Seminary (Delaware Valley Job Corps)','Callicoon','cat','inst','standing',41.77026,-75.05755,'site','view','drive','','1904–1972',
  'A Franciscan minor seminary of the Holy Name Province, founded in 1904 and dedicated by Cardinal Farley in 1911; boys came in the ninth grade for a six-year classical course in Latin and Greek before the novitiate. It closed in 1972, was sold to the federal government in 1977 and since 1979 has been the Delaware Valley Job Corps Center. The Romanesque seminary, its church and farm buildings were listed as a historic district in 1993.',
  'The Romanesque main building of 1904 on the hill above Callicoon. Interior not checked; materials not checked.',
  '',
  'A residential federal Job Corps center on Seminary Road; not open to visitors as far as found. View from the road only.',
  [W('St. Joseph\'s Seraphic Seminary')],brick='?'),

N('bloomingburg-reformed-dutch-church','Bloomingburg Reformed Protestant Dutch Church','Bloomingburg','cat','worship','standing',41.55614,-74.44293,'exact','view','drive','','1821',
  'An ornate Federal-style wooden church of 1821, one of the oldest in the county, with an 80-foot bell tower that is a landmark from afar. Long out of use as a church, it has been looked after since 1977 by the Bloomingburg Restoration Foundation as a local history museum; the Town of Mamakating has owned it since 1999. In 2018 voters defeated, 550 to 31, the town\'s plan to sell it to another congregation, and the town supervisor called it an eyesore for its cracks, leaning steeple and broken steps.',
  'White clapboard on heavy timber framing, with the tower rising in stages above the front gable and a painted clock face traditionally set at 11:07. Inside, Wikipedia says the box pews were turned into slips and the galleries extended in the mid-19th century, and some furnishings were stolen in a period of neglect. A 2022 article says a restoration was under way; present condition not checked.',
  'A town fought its own government to keep its 1821 church.',
  'Owned by the Town of Mamakating, 112 Main Street (County Route 171). Wikipedia says the foundation opens it as a museum by appointment; no current page of the foundation was read, so view from Main Street.',
  [W('Bloomingburg Reformed Protestant Dutch Church'),L('Spectrum News (2018): group fights for control of former church','https://spectrumlocalnews.com/nys/hudson-valley/news/2018/09/19/community-group-fights-town-officials-to-maintain-control-of-historic-former-church'),L('Times Hudson Valley (2022): Falling houses of God','https://www.timeshudsonvalley.com/stories/falling-houses-of-god,36229')],
  brick='no'),

N('rivoli-theatre-south-fallsburg','Rivoli Theatre','South Fallsburg','cat','civic','standing',41.70932,-74.62877,'exact','open','drive','','1923',
  'Built in 1923 and remodelled in the late 1930s, the Rivoli was a main source of films and live shows in the years of the Jewish summer resorts of the Catskills, and it has changed little since. The Sullivan County Dramatic Workshop owns it, stages plays there each summer, and began showing films again in 2012.',
  'A front block with the foyer and lobby and a one-story auditorium behind; concrete block faced in buff brick with red brick coursing and trim, and a three-sided neon marquee hung on chains. Inside is seen at performances; interior details not checked.',
  'A Borscht Belt picture house still showing films.',
  'Owned by the Sullivan County Dramatic Workshop; open for its shows and films. Street parking. No schedule page was read, so hours are not given.',
  [W('Rivoli Theatre (South Fallsburg, New York)')],brick='some',hours='?'),

N('ohave-shalom-woodridge','Ohave Shalom Synagogue (the Woodridge Shul)','Woodridge','cat','worship','standing',41.71061,-74.57257,'exact','view','drive','','1930',
  'An Orthodox synagogue built in 1930 by a group that split from what was then Woodridge\'s only congregation, which it later absorbed. It is the one synagogue in Sullivan County whose religious wall paintings survive. In 2020 the congregation appealed for money to keep up and restore the building.',
  'A one-story building on a raised basement, its painted concrete block given a golden brick veneer in the 1950s, with a pedimented portico, stained glass along the sides and over the ark (sunbursts and Stars of David), a wooden ark and bimah, and the ark topped by Lions of Judah holding the Ten Commandments. Some of the painting, including the ceiling, was painted over (Wikipedia). Whether visitors are let in was not found.',
  '',
  '14 Maurice Rose Street, Woodridge. An active congregation; service times not found. View from the street.',
  [W('Ohave Shalom Synagogue (Woodridge, New York)')],brick='no'),

N('agudas-achim-livingston-manor','Agudas Achim Synagogue','Livingston Manor','cat','worship','standing',41.89975,-74.82265,'area','view','drive','','1920s',
  'A congregation founded in 1913 by the Jews of Livingston Manor built this stucco-sided wooden synagogue in the 1920s for a community that swelled each summer with resort visitors from New York. It mixes Eastern European synagogue features with the lancet windows of the local Protestant churches. The congregation became Reform after the resorts declined and, per Wikipedia, holds monthly services year-round.',
  'Austere inside, with a barrel-vaulted ceiling, a paneled ark and bimah, an iron chandelier and lanterns, and three Star of David windows over the ark at the west end; the building is architecturally intact from its construction (Wikipedia). Interior seen only at services.',
  '',
  'Rock Avenue, Livingston Manor. An active congregation; no page of its own was read for service times. View from the street.',
  [W('Congregation Agudas Achim (Livingston Manor, New York)')],brick='no'),
]

PIN_NOTES={
'roebling-delaware-aqueduct':'Wikipedia\'s point, on the bridge; the lot is the OpenStreetMap "Museum Parking" lot on Route 97 by the toll house (4225 Route 97 geocodes 40 m from it).',
'minisink-battleground-park':'HMdb\'s position of the Minisink Battle Monument marker; lot is the OpenStreetMap park lot on County Route 168 (58 County Road 168 geocodes 70 m from it).',
'dh-canal-linear-park-mamakating':'ArcGIS PointAddress for 16 Bova Road, the interpretive center; the lot is the mapped Bova Road parking area on county park land. The canal runs about 4.5 miles south to Wurtsboro.',
'van-tran-flat-bridge':'Wikipedia\'s point; 130 Covered Bridge Road geocodes 80 m southeast, by the mapped park lot.',
'beaverkill-covered-bridge':'Wikipedia\'s point on the bridge.',
'halls-mills-covered-bridge':'Wikipedia\'s point on the bridge.',
'stone-arch-bridge-kenoza-lake':'Wikipedia\'s Register point; the park address geocodes (interpolated) about 200 m south.',
'tusten-stone-arch-bridge':'Wikipedia\'s Register point; lot is the NPS Ten Mile River Access coordinate from the NPS page.',
'ten-mile-river-baptist-church':'Moved with pix.py from Wikipedia\'s rounded Register point (41.56, -75.01667) 22 m into the clearing beside the railroad, taken to be the churchyard; the church building itself could not be picked out on the aerial and OpenStreetMap had no church by name, so not confirmed.',
'arlington-hotel-narrowsburg':'ArcGIS PointAddress for 37 Main Street, 5 m from HMdb\'s Arlington Hotel marker.',
'cochecton-railroad-station':'ArcGIS POI "Cochecton Station" on Route 97, 120 m east of Wikipedia\'s Register point (which falls in a field by the tracks). The building could not be picked out on the aerial: area pin.',
'callicoon-downtown':'HMdb\'s position of the Erie Train Station marker at the depot.',
'st-josephs-seraphic-seminary':'ArcGIS POI for the Delaware Valley Job Corps Center, 30 m from Wikipedia\'s point.',
'bloomingburg-reformed-dutch-church':'OpenStreetMap\'s mapped church at 112 Main Street (nom.py), 40 m from Wikipedia\'s point.',
'rivoli-theatre-south-fallsburg':'OpenStreetMap\'s mapped Rivoli Theater on Laurel Avenue (nom.py); Wikipedia\'s point is about 1.4 km southwest, away from the hamlet.',
'ohave-shalom-woodridge':'ArcGIS PointAddress for 14 Maurice Rose Street, 5 m from Wikipedia\'s point.',
'agudas-achim-livingston-manor':'Wikipedia\'s point fell on a house among houses; moved to ArcGIS\'s point for Rock Avenue itself, 180 m southeast, since the source names only the street. The building is not identified: area pin, look along Rock Avenue.',
}
