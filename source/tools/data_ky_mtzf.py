# November 24, 2026: Kentucky, a second statewide scatter (claimed with tools/choose.py --thinnest). Earlier batches sit
# round Harrodsburg, Danville, Frankfort, Louisville and a few towns; this one goes to Northern Kentucky, the Hardin County
# river, the Knobs, the Cumberland plateau, the Appalachian east and the far west. Facts come from the linked sources only,
# read in the session: Wikipedia through tools/wiki_raw.py, National Park Service and operators' own pages through
# tools/page.py. Kentucky State Parks pages could not be read, so those two places give no hours.
from data_b import N
from data_ma import W

BATCH={'key':'ky_mtzf','label':'Kentucky: a second statewide scatter','added':'2026-11-24 01:28'}

PLACES=[
N('roebling-suspension-bridge-covington','John A. Roebling Suspension Bridge','Covington','ky','landmark','standing',39.09223,-84.50957,'exact','public','walk','','1856–1867',
  'Opened on January 1, 1867 between Covington and Cincinnati, this was the longest suspension bridge in the world, with a main span of 1,057 feet, until the Niagara Clifton Bridge passed it. John A. Roebling planned it and later built the Brooklyn Bridge on the same ideas. Pedestrians first walked it on December 1, 1866, and 166,000 people crossed in two days.',
  'Two Gothic-style towers of rough-cut sandstone, the lower 25 feet of each cased in limestone against scour and river traffic. The bridge was painted blue in 1894. A second set of cables, a wider steel deck and a longer northern approach were added in 1896, which changed its look. Wikipedia says it is a National Historic Landmark (1975) and a Historic Civil Engineering Landmark (1983). People still walk across it.',
  'The long span that taught Roebling how to build Brooklyn.',
  'A public road and footway over the Ohio River, kept by the Kentucky Transportation Cabinet (Wikipedia). The Kentucky end is at Roebling Point, with street parking and garages nearby; which lot to use was not checked.',
  [W('John A. Roebling Suspension Bridge')],
  conf='mixed',brick='no'),

N('covington-cathedral-basilica-assumption','Cathedral Basilica of the Assumption','Covington','ky','worship','standing',39.07833,-84.50806,'exact','open','walk','','1895–1910',
  'The cathedral of the Diocese of Covington, begun in 1894 to designs by the Detroit architect Leon Coquard and dedicated in 1901. Its outside follows Notre-Dame in Paris and its inside the abbey church of Saint-Denis. There was no money for stained glass until 1910, and the Madison Avenue front by David Davis was added between 1908 and 1910. The two planned towers were never built. Pope Pius XII made it a minor basilica in 1953.',
  'Wikipedia lists murals by Frank Duveneck, a high altar of Carrara marble and a stained glass window in the north transept, 67 by 24 feet, made in 1911 by Mayer and Company of Munich, which shows the Coronation of Mary above the Council of Ephesus. The 24 statues in the front niches are from 2021. The parish says it welcomes visitors and offers tours by arrangement.',
  'A Gothic cathedral with a 67-foot window from Munich, on the Ohio.',
  'Parish church at Madison Avenue, Covington. Open hours and Mass times are from the parish page; it also closes after Mass on civil holidays. Parking not checked.',
  [W('Cathedral Basilica of the Assumption (Covington, Kentucky)'),['Cathedral Basilica of the Assumption (parish page)','https://covcathedral.com/']],
  brick='?',hours='Open Mon–Fri 9 a.m.–3 p.m., Sat 10–4, Sun 8:30–5; Mass weekdays 8:15, Sat 4:30 p.m., Sun 7:30, 10, 5:30'),

N('waveland-state-historic-site','Waveland State Historic Site (Bryan House)','Lexington','ky','landmark','standing',37.97139,-84.53722,'exact','open','walk','','',
  'The Greek Revival home of Joseph Bryan, a grandson of William Bryan and Mary Boone, Daniel Boone\'s sister. His planter family ran a hemp and tobacco farm here with the labour of enslaved people, and his son Joseph Henry Bryan made it a noted horse-breeding farm. It is now a Kentucky State Parks historic site on 10 acres. The year of the house is not given in the article text read.',
  'The front door copies the north door of the Erechtheion in Athens. First-floor rooms are 14 feet high. Bryan made the bricks, lumber and ironwork on the farm; Wikipedia says the stairway rail is of flat boards and the marble-looking baseboards are painted stone. The tour also covers the brick slave quarters, smokehouse and ice house. Other farm buildings (gunsmith shop, mills) are described but their survival was not checked.',
  'A hemp planter\'s Greek Revival house with a copy of an Athens doorway.',
  'Run by Kentucky State Parks, 225 Waveland Museum Lane, Lexington. Wikipedia says tours run daily for much of the year; the Parks page that carries the days and times could not be read, so hours are not given. Phone the site first. Parking not checked.',
  [W('Waveland State Historic Site')],
  conf='mixed',brick='?',hours='?'),

N('fort-duffield-west-point','Fort Duffield','West Point','ky','fort','ruins',37.99306,-85.94194,'site','public','hike','forts','1861–1862',
  'A Union earth fort on Pearman Hill above West Point, where the Salt River meets the Ohio. The 9th Michigan Infantry built it in two months from November 3, 1861, and named it for the Rev. George Duffield, whose son led the regiment. Its 950 troops soon left for the front, and its artillery and munitions were removed in December 1862. It was never attacked. The fort\'s own site calls it Kentucky\'s largest and best-preserved Civil War earthwork.',
  'A serpentine earth wall, not a star, on a wooded hilltop nearly 300 feet above the town. Wikipedia adds that there are wooden walkways, small cabins and a lookout over the Ohio; the spring inside the fort is closed off for safety, and a Civil War cemetery lies on the west side of the hill. Reenactments and bus rides have stopped (2021).',
  'A snaking Civil War earthwork above the mouth of the Salt River.',
  'City of West Point park, 175 acres, once part of Fort Knox, given to the city in 1978 (the fort\'s own site). A lot at the foot of the hill serves the trails. Search listings, not an operator page, say it is open daily from morning to dark and free; not checked.',
  [W('Fort Duffield'),['Fort Duffield (the fort\'s site)','https://fortduffield.com/']],
  conf='mixed',brick='no'),

N('blue-heron-mining-community','Blue Heron Mining Community (Mine 18)','Strunk','ky','town','traces',36.67159,-84.54772,'site','public','walk','','1937–1962',
  'A coal camp of the Stearns Coal and Lumber Company on the Big South Fork of the Cumberland River. Its mines ran from 1937 to December 1962, when they closed as unprofitable, and hundreds of people lived here. The buildings were removed or fell down, and in the 1980s the National Park Service re-created the town as an outdoor museum.',
  'No original buildings stand (NPS says so). Open metal frames, called ghost structures, stand on the approximate sites of the train depot, company store, school, church, bathhouse, superintendent\'s house and repair shop, each with photographs and audio about the people. The tipple and its bridge are a full-size model, and a mine entrance is shown.',
  'A coal town drawn in steel outline, with the miners\' voices inside.',
  'Big South Fork National River and Recreation Area (National Park Service). A 2025 NPS release gives the address 8249 Mine 18 Road, Strunk, with free parking, and says the site can also be reached by the Big South Fork Scenic Railway from Stearns, for which tickets are needed. An older NPS page says it can be visited at any time; not checked this year.',
  [W('Blue Heron, Kentucky'),['NPS: Blue Heron','https://home.nps.gov/biso/learn/historyculture/blueheron.htm']],
  conf='mixed',brick='no',th=[36.66997,-84.54748],thn='Blue Heron lot by the tipple bridge'),

N('pine-mountain-settlement-school','Pine Mountain Settlement School','Bledsoe','ky','inst','standing',36.94861,-83.18306,'site','view','drive','','1913–',
  'A boarding school founded in 1913 in Harlan County on land that William Creech Sr. deeded for school use. Katherine Pettit and Ethel de Long ran it, with plans by the architect Mary Rockwell Hook of Kansas City. It taught grade-school children until 1930, then high school students, and now runs programmes on Appalachian culture and the environment. The campus is a National Historic Landmark District.',
  'Wikipedia names a stone reservoir and a chapel built by the stonemason Luigi Zande among the campus buildings. Their present condition and whether they can be entered were not checked.',
  'A mountain school campus where two women and a stonemason built the buildings.',
  'Private non-profit grounds at 36 Highway 510, Bledsoe. The school\'s own pages offer day hiking, workshops, events and lodging but give no hours for walking the campus: call (606) 558-3571 before coming. Parking not checked.',
  [W('Pine Mountain Settlement School'),['Pine Mountain Settlement School: Visit','https://pinemountainsettlementschool.com/visit/'],['Pine Mountain Settlement School: History','https://www.pinemountainsettlementschool.com/history/']],
  conf='mixed',brick='?'),

N('nada-tunnel-powell-county','Nada Tunnel','Slade','ky','rail','standing',37.81722,-83.68083,'site','public','drive','','1910–1911',
  'A 900-foot sandstone tunnel on Kentucky Route 77, blasted in 1910 and 1911 for the Dana Lumber Company\'s narrow-gauge railroad, the Big Woods, Red River & Lombard. Steam locomotives took logs through it to a sawmill at Clay City. After the timber was cut the rails were pulled up and it became a dirt road, now paved to one lane. It is the way in to Red River Gorge.',
  'A rough, unlit rock bore, 12 by 12 feet when built and raised to 13 feet after a log train stuck. Traffic goes one way at a time. Wikipedia says two prehistoric rock-art sites near it, Nada Tunnel 1 and 2, were listed on the Register in 1992; their positions are not given here.',
  'A logging railway tunnel that is now the one-lane door to Red River Gorge.',
  'A public state road, KY 77; the tunnel is in Daniel Boone National Forest country. Take care with the one-lane traffic and the dark. Parking not checked.',
  [W('Nada Tunnel')],
  brick='no'),

N('lincoln-birthplace-memorial-building','Lincoln Birthplace Memorial Building','Hodgenville','ky','landmark','standing',37.5311,-85.7375,'exact','open','walk','','1909–1911',
  'The Beaux-Arts memorial that John Russell Pope designed over the farm where Abraham Lincoln was born on February 12, 1809. President Theodore Roosevelt laid the cornerstone in 1909 and President Taft dedicated it on November 9, 1911. Inside is a symbolic birth cabin: the real one was taken down before 1865, and the logs here mostly date from the 1840s.',
  'A temple of 56 steps (his age at death), 16 windows and 16 ceiling rosettes (the sixteenth president). The 12-by-17-foot cabin inside is a stand-in, built from old logs after a mix-up with logs from other cabins. The sinking spring that named the farm is on the same site.',
  'A marble temple built around a stand-in for Lincoln\'s birth cabin.',
  'Abraham Lincoln Birthplace National Historical Park, 2995 Lincoln Farm Road, Hodgenville. Hours are from the park\'s own page (last updated September 2024). Parking at the visitor center.',
  [W('Abraham Lincoln Birthplace National Historical Park'),['NPS: Operating hours and seasons','https://www.nps.gov/abli/planyourvisit/hours.htm']],
  brick='?',hours='Visitor center 9–5 daily; Memorial Building 9–4:30; closed New Year\'s Day, Thanksgiving, Christmas'),

N('mayo-mansion-paintsville','Mayo Mansion','Paintsville','ky','landmark','standing',37.81639,-82.80833,'exact','view','walk','','1905–1912',
  'A 43-room, three-story mansion that the coal and timber man John C. C. Mayo built from 1905, finished in December 1912 at a cost of $250,000. Italian stonemasons from Cincinnati worked on it, the water came from its own cistern system, and the sandstone was cut across Paint Creek and carried over on a three-quarter-mile overhead tram. After Mayo died in 1914 his family moved to Ashland and took much of the marble, tile and furniture with them.',
  'A sandstone mansion with stone columns. Since 1945 it has been Our Lady of the Mountains School, so the inside is a school; the outside can be looked at.',
  'A coal baron\'s sandstone palace, now a Catholic school.',
  'It is a working school, so look from the public street; visits inside were not checked. Parking not checked.',
  [W('Mayo Mansion')],
  brick='no'),

N('wickliffe-mounds-ballard','Wickliffe Mounds','Wickliffe','ky','landmark','traces',36.97102,-89.09286,'site','open','walk','','',
  'A Mississippian town on a bluff above the Ohio River, three miles from where it meets the Mississippi: a ceremonial and administrative centre of a chiefdom, with hundreds of people at its height. Two large platform mounds and at least eight small ones stand round a central plaza. People began leaving about 1300 for the Twin Mounds site. A museum at the site is run by Kentucky State Parks.',
  'Earth mounds and a plaza on a river bluff, with a museum. The museum\'s own hours could not be read.',
  'A chief\'s town of earth mounds above the Ohio, left by about 1300.',
  'Kentucky State Parks historic site; its page could not be read, so hours and fees are not given. Search listings say it keeps a season of spring to mid-November: phone first. Parking not checked.',
  [W('Wickliffe Mounds')],
  conf='mixed',brick='no',hours='?'),
]

PIN_NOTES={
'roebling-suspension-bridge-covington':'Wikipedia coordinate for the bridge; checked on the aerial.',
'covington-cathedral-basilica-assumption':'Wikipedia coordinate; checked on the aerial.',
'waveland-state-historic-site':'Wikipedia coordinate; checked on the aerial.',
'fort-duffield-west-point':'Wikipedia coordinate for the fort; checked on the aerial and the bare-ground sheet.',
'blue-heron-mining-community':'The OpenStreetMap point named for the community; the Wikipedia coordinate fell in woods about 200 m east. The parking point is a mapped lot by the tipple bridge.',
'pine-mountain-settlement-school':'Wikipedia coordinate for the campus; checked on the aerial.',
'nada-tunnel-powell-county':'Wikipedia coordinate, on KY 77 at the tunnel; the tunnel itself cannot be seen on the aerial, so the pin marks the tunnel\'s road.',
'lincoln-birthplace-memorial-building':'Wikipedia coordinate for the park; checked on the aerial.',
'mayo-mansion-paintsville':'Wikipedia coordinate for the mansion; checked on the aerial.',
'wickliffe-mounds-ballard':'Wikipedia coordinate for the site; checked on the aerial.',
}
