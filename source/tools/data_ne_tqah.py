# November 19, 2026: the old Missouri River towns of southeast Nebraska: Brownville and Auburn (Nemaha County) and
# Nebraska City (Otoe County). Region drawn at random by tools/choose.py (ne).
# Sources read in this session: the 1970 National Register nomination for the Brownville Historic District (NPGallery
# "_text" PDF, text layer read with tools/page.py), HMdb marker pages (inscriptions and positions), SAH Archipedia's
# Bailey House entry, the Wikipedia articles (tools/wiki_raw.py), the Brownville visitor site (brownville-ne.com), the
# Nemaha County tourism museum page, the Nebraska City Museum Association's museum page, Arbor Day Farm's Arbor Lodge
# page, Wildwood Historic Center's own pages, the Mayhew Cabin Foundation's page, a June 2026 KOLN news report on the
# cabin's reopening, and the Kregel Windmill Factory Museum's own page. No interior was seen by this session.
# Red brick: St. Benedict's, the Otoe County Courthouse and the G.A.R. hall are red brick in the Wikimedia photographs
# their articles name (tools/brick.py look); Arbor Lodge (painted white) and the dredge (a steel boat) are not. The
# others say brick in a source without the colour, or were not looked at, and are '?'.
from data_b import N
from data_ma import W
BATCH={'key':'ne_tqah','label':'Nebraska: Brownville, Auburn and Nebraska City','added':'2026-11-19 10:53'}

def NR(ref,label):
    return [label+' (National Register nomination)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/%s_text'%ref]
def HM(m,label):
    return ['HMdb: '+label,'https://www.hmdb.org/m.asp?m=%s'%m]
BDIST=NR('70000374','Brownville Historic District')
BVIS=['Brownville visitor site','https://www.brownville-ne.com/']
NEMT=['Nemaha County Tourism: museums','https://enjoynemahacounty.org/?p=1895']
NCMA=['Nebraska City Museum Association: our museums','https://NebraskaCityMuseums.org/museums']
BHS_HOURS=('The Nemaha County tourism page gives the Brownville Historical Society museums\' season as late April to mid-October, '
           '1 to 4 p.m. on Saturdays and Sundays. ')
BTOWN='Street parking in the village; parking was not checked on the ground. '
NCTOWN='Street parking in town; parking was not checked on the ground. '

PLACES=[
N('brownville-historic-district','Brownville Historic District','Brownville','ne','town','standing',40.397363,-95.657283,'area','public','walk','','1854–1880s',
  'A Missouri River steamboat town founded by Richard Brown in 1854, which ran a ferry, a U.S. land office (where Daniel Freeman filed what Congress later recognised as the first homestead claim) and Nebraska\'s first telegraph link to the east. It may have passed 2,000 people by the early 1870s, then emptied after the Panic of 1873, a failed railroad bond and the loss of the county seat to Auburn in 1885. The 1970 nomination found most of its buildings dated from before 1875, mostly brick houses, with few later buildings among them.',
  'Brick houses of the 1850s to 1870s scattered over the bluffs, a handful of museums run by the Brownville Historical Society, the repertory theatre in a 1903 frame church moved here in 1966, the 1854 Didier log cabin (moved into Boettner Park in 2008) and the state marker in the park on Main Street. Most of the old commercial blocks on Main Street are gone (1970 nomination); many of the houses are private homes.',
  'The Nebraska territorial river town that the railroad passed by and so kept its 1860s houses.',
  'A village with public streets; most of the historic buildings are private homes, to be seen from the street. '+BHS_HOURS+'The pin is the state marker in Boettner Park on Main Street (HMdb). '+BTOWN,
  [BDIST,HM('177299','Brownville marker'),BVIS,NEMT,['SAH Archipedia: Bailey House (town history)','https://sah-archipedia.org/node/16203']],brick='?'),
N('brownville-methodist-church','Brownville Methodist Church','Brownville','ne','worship','standing',40.396083,-95.661282,'site','view','walk','','1859',
  'Built in 1859 for the Congregationalists led by the Rev. Thomas W. Tipton, a Brownville man who sat in the U.S. Senate from 1867 to 1875; the Methodists have used it since 1861. The 1970 nomination calls it one of Nebraska\'s oldest churches and a rare Greek Revival church in the state. It was recorded by the Historic American Buildings Survey in 1934.',
  'A brick church under a frame cupola added about 1870; the nomination found few other changes outside. The mason Abbott Gates, who helped build it, built the similar Gates House nearby. Interior not checked.',
  '',
  'A working church at 423 Water Street; the village visitor site gives the Sunday service at 10 a.m. Outside of services, see it from the street. '+BTOWN,
  [BDIST,BVIS],brick='?'),
N('brown-carson-house-brownville','Brown-Carson House','Brownville','ne','landmark','standing',40.39728,-95.65823,'site','public','walk','','1860–c.1880',
  'A one-storey brick house built in 1860 for Richard Brown, the town\'s founder, who added a two-storey frame wing in 1861 and sold it in 1864 to the banker John L. Carson. Carson added a frame second storey to the old part about 1880. The Carson family gave the house and its carriage house to the Brownville Historical Society in 1966.',
  'The 1970 nomination says the Italianate house, with its furnishings and basement kitchen, was hardly changed since the 1880s, and the carriage house south of it was built before 1880. It is shown as a house museum. Interior not checked by this session.',
  '',
  'Owned by the Brownville Historical Society (1970 nomination) and run as the Carson House Museum, 231 Main Street. '+BHS_HOURS+BTOWN,
  [BDIST,NEMT,BVIS],brick='?'),
N('furnas-house-brownville','Governor Furnas House','Brownville','ne','landmark','standing',40.395819,-95.662889,'site','view','walk','','1868',
  'A brick house probably built in 1868 by and for Andrew J. Berry, and from 1878 until his death in 1905 the home of Robert W. Furnas, newspaper editor, Civil War officer and governor of Nebraska. The nomination calls him Nebraska\'s third state governor and the village visitor site its second; the visitor site says he lived here after leaving the governorship and is buried in Walnut Grove Cemetery under an unusual monument.',
  'A two-and-a-half-storey brick house mixing Gothic Revival and Italianate (nomination); now the Governor Furnas House Museum. Interior not checked.',
  '',
  'Listed by the Nemaha County tourism page as the Governor Furnas House Museum, 230 South 6th Street; who owns it now and its hours were not found on any page opened, so see it from the street unless it is open. '+BTOWN,
  [BDIST,BVIS,NEMT],brick='?'),
N('muir-house-brownville','Muir House','Brownville','ne','landmark','standing',40.398456,-95.656653,'site','view','walk','','1868–1872',
  'An Italianate mansion begun in 1868 for Robert V. Muir, a Scot who ran a sawmill, a flour business and a ferry, published the Nebraska Advertiser, and ran for governor for the Prohibition Party. The marker gives the building years as 1868 to 1870; the 1970 nomination says it was finished about 1872. The nomination calls it one of Nebraska\'s finest Italianate houses.',
  'Two storeys of native Nebraska brick; the marker says the panelling inside is butternut, bird\'s-eye maple and black walnut cut at Muir\'s own sawmill across the river. In 1970 its owner had furnished it and opened it to tours; whether it is open now was not checked. Interior not checked.',
  '',
  'Private property as far as any source opened shows: see it from Atlantic Street. The marker stands beside the driveway at Atlantic and North 2nd Streets (HMdb); the pin is the marker. '+BTOWN,
  [HM('183305','Muir House'),BDIST],conf='mixed',brick='?'),
N('bailey-house-brownville','Captain Bailey House','Brownville','ne','landmark','standing',40.397834,-95.66072,'site','public','walk','','1877',
  'A Gothic Revival brick house of Captain Benson M. Bailey, a Civil War veteran. The visitor site says it first stood near the Missouri River and was taken down and moved brick by brick in 1877 when the river threatened it; the nomination calls that story "purportedly". Its bricks came from one of Brownville\'s three early brickyards (visitor site).',
  'A one-and-a-half-storey brick I-house with three steep gables, pointed-arch windows rising into them and a full-width porch (SAH Archipedia). It is the Captain Bailey Museum of the Brownville Historical Society. Interior not checked.',
  '',
  'Run by the Brownville Historical Society as a museum. The county tourism page gives the address as 412 Main Street; SAH Archipedia gives 402 Main Street. '+BHS_HOURS+BTOWN,
  [['SAH Archipedia: Bailey House','https://sah-archipedia.org/node/16203'],BDIST,BVIS,NEMT],brick='?'),
N('captain-meriwether-lewis-dredge','Dredge Captain Meriwether Lewis','Brownville','ne','landmark','standing',40.39488,-95.6506,'exact','public','walk','','1931–1932',
  'A side-wheel steam dustpan dredge launched in 1931 for the U.S. Army Corps of Engineers and finished in 1932, used to keep the Missouri River channel open. It is 269 feet long and had a working crew of 52. Given to the Nebraska State Historical Society in 1976, it was brought to Brownville the next year and set on dry land by the river; it is a National Historic Landmark.',
  'The whole vessel on dry ground beside the river, with its 25-foot paddle wheels; the Museum of Missouri River History, opened in 1981, is in rooms on the boiler deck (Wikipedia). Interior not checked.',
  'A 1930s river dredge, paddle wheels and all, beached for good beside the river it dug.',
  'In Brownville Riverside Park, inside Brownville State Recreation Area on the federal land map. The county tourism page lists it as the Meriwether Lewis Dredgeboat & Missouri River Museum; its own site would not open, and its season and hours were not checked. Parking: the mapped lot about 100 m west, on the recreation-area road.',
  [W('Captain Meriwether Lewis (dustpan dredge)'),NEMT,BVIS],th=[40.39478,-95.65178],thn='Lot in Brownville State Recreation Area',brick='no'),
N('brownville-bridge','Brownville Bridge','Brownville','ne','landmark','standing',40.39917,-95.65167,'site','view','drive','','1939',
  'A cantilevered Warren through-truss bridge carrying U.S. 136 over the Missouri River to Missouri, built in 1939 by Atchison County, Missouri, as a toll bridge with Public Works money. It is narrow, one 8-foot lane each way and no shoulders; the main span is about 420 feet. It was repaired in 2009 and 2010 and closed for 216 days in 2019 after the floods.',
  'The steel truss over the river, best seen from the riverfront park at Brownville. A 1939 Public Works plaque is on the east abutment on the Missouri side (HMdb).',
  '',
  'An open highway bridge maintained by the Missouri Department of Transportation (Wikipedia); there is no walkway named in any source, so see it from the riverfront. Parking: the lot in Brownville State Recreation Area.',
  [W('Brownville Bridge'),HM('216754','Brownville Bridge plaque')],th=[40.39478,-95.65178],thn='Lot in Brownville State Recreation Area',brick='no'),
N('nemaha-county-courthouse-auburn','Nemaha County Courthouse','Auburn','ne','civic','standing',40.3857,-95.84472,'site','view','drive','','1899–1900',
  'The courthouse of the county seat that left Brownville: an 1883 vote moved it to Auburn, a town made in 1882 from the villages of Sheridan and Calvert. The Richardsonian Romanesque building was designed by George A. Berlinghof; the cornerstone was laid in May 1900 with former governor Furnas present, and the county moved in that December.',
  'A symmetrical building with two main entrances and corner towers. The marker says its stone was quarried about five miles west of Auburn and its brick made at a local brickyard. Interior not checked.',
  '',
  'In use as the county courthouse, 1824 N Street; public hours not checked. '+NCTOWN,
  [HM('140410','Nemaha County Courthouse'),W('Nemaha County Courthouse (Nebraska)')],brick='?'),
N('arbor-lodge-nebraska-city','Arbor Lodge','Nebraska City','ne','inst','standing',40.680496,-95.881525,'exact','public','walk','','1855–1903',
  'The home of J. Sterling Morton, who started Arbor Day in 1872 and was Grover Cleveland\'s Secretary of Agriculture. It began in 1855 as a four-room frame house on 160 acres and was enlarged several times, last in 1903, into a 52-room neo-colonial mansion, later the summer home of his son Joy Morton, founder of Morton Salt. It is a National Historic Landmark.',
  'The mansion with Morton family furnishings and a Tiffany skylight in the sun parlour (Wikipedia), and a 72-acre park with an arboretum, an Italian terraced garden, a log cabin, a carriage house, walking trails and more than 200 kinds of lilac (Arbor Day Farm).',
  'Where Arbor Day was dreamed up: a four-room cabin grown into a 52-room mansion.',
  'Owned by the Nebraska Game and Parks Commission and run by the Arbor Day Foundation (Nebraska City Museum Association). Arbor Day Farm\'s page says the grounds are open daily with no admission or park permit needed; the mansion tour costs $9 for adults and $7 for children 3 to 12; the mansion\'s hours were not read. OpenStreetMap maps two Arbor Lodge parking lots by the mansion; the one tried showed on the aerial as a drive by a building, so parking was not settled.',
  [W('Arbor Lodge State Historical Park and Arboretum'),['Arbor Day Farm: Arbor Lodge','https://www.arbordayfarm.org/attractions/arbor-lodge.cfm'],NCMA,NR('69000135','Arbor Lodge')],brick='no'),
N('wildwood-ware-house-nebraska-city','Wildwood (Jasper A. Ware House)','Nebraska City','ne','landmark','standing',40.673876,-95.878335,'area','public','walk','','1869',
  'A ten-room Gothic-style country house built in 1869 for Jasper and Ellen Ware, set "amidst the wild wood" on the west side of Nebraska City. The city now runs it as the Wildwood Historic Center.',
  'The house furnished as a well-off Victorian home, shown on guided tours by docents in period dress, with the family\'s Steinway piano in the parlour, a Victorian garden behind and an art gallery and gift shop (Wildwood and the museum association).',
  '',
  'Open daily from Arbor Day (the last Friday in April) to the end of October: Monday to Saturday 10 a.m. to 5 p.m., Sunday 1 to 5 p.m., last tour at 4; house tours $5 for adults and $2 for children 12 and under; the garden and shop are free (Wildwood\'s own pages). 420 Steinhart Park Road. Parking: the Steinhart Park lot about 100 m north-east; not checked on the ground.',
  [['Wildwood Historic Center: plan your visit','https://wildwoodhistoriccenter.org/visit-us'],['Wildwood Historic Center','https://wildwoodhistoriccenter.org/'],NCMA],th=[40.67468,-95.87779],thn='Steinhart Park lot',brick='?'),
N('mayhew-cabin-nebraska-city','Mayhew Cabin and John Brown\'s Cave','Nebraska City','ne','landmark','standing',40.674331,-95.87075,'site','public','walk','','1855',
  'A cottonwood-log cabin built in 1855 by Allen and Barbara Mayhew. Her brother John Henry Kagi lived with them before joining John Brown in Kansas; in 1859 Kagi helped Brown lead escaped slaves from Missouri through Nebraska City to Iowa, and he was killed at Harpers Ferry that October. It is on the National Park Service\'s Underground Railroad Network to Freedom.',
  'The furnished cabin, moved a short way north in the 1930s for a new highway and set on a new cellar lined with its old foundation stones. The "cave" and tunnel to the ravine were dug then by the owner for visitors (the marker calls the cave recreated). The cabin was restored in 2005 and again after the 2019 flood, which closed the site for seven years until it reopened on Juneteenth 2026 (KOLN).',
  '',
  'Owned by the Mayhew Cabin Foundation, 2012 4th Corso (Nebraska Highway 2). The museum association lists it as open by appointment; current hours were not checked. '+NCTOWN,
  [['Mayhew Cabin Foundation: the cabin today','https://mayhewcabin.org/history/mayhew-cabin/'],HM('177269','Mayhew Cabin, 1855'),HM('177270','Mayhew Cabin and the Underground Railroad'),W('Mayhew Cabin'),['KOLN: site reopens after seven-year closure (June 2026)','https://www.wowt.com/2026/06/19/underground-railroad-site-reopens-after-7-year-closure-nebraska-city/'],NCMA],brick='no'),
N('kregel-windmill-factory-nebraska-city','Kregel Windmill Factory','Nebraska City','ne','industry','standing',40.67698,-95.86383,'exact','public','walk','','1902–1991',
  'The cousins Louis and George Kregel began making windmills in Nebraska City in 1879 and moved into this one-storey factory, built in 1902 (the museum association says 1903). The company made Eli windmills until 1941, when steel rationing turned it mostly to sales and repair, and it ran until Art Kregel died in 1991. The marker calls it the last intact historic windmill factory in the United States.',
  'The factory floor kept as the workers left it, with its machinery, shown as a museum since 2013 with video kiosks; an Eli windmill stands outside (HMdb).',
  'A windmill factory left as if the crew had gone to lunch in the 1940s.',
  'A nonprofit museum at 1416 Central Avenue (the museum\'s page; the museum association gives 1423). Its page gives winter hours of Tuesday to Saturday 10 a.m. to 5 p.m. and admission of $8 for adults and $5 for students. '+NCTOWN,
  [['Kregel Windmill Factory Museum','https://www.kregelwindmillfactorymuseum.org/node/31'],HM('251358','The Kregel Windmill Factory'),NCMA],brick='?'),
N('gar-memorial-hall-nebraska-city','Grand Army of the Republic Memorial Hall','Nebraska City','ne','civic','standing',40.675957,-95.856921,'exact','public','walk','','1894–1895',
  'A Richardsonian Romanesque hall built in 1894 and 1895 by the architects Fisher & Lawrie for William Baumer Post No. 24 of the Grand Army of the Republic, the Union veterans\' society, one of 354 posts in Nebraska. The museum association calls it one of the last GAR halls left in the state.',
  'Restored as the Civil War Veterans Museum, with weapons, uniforms, medals and art from both sides. Interior not checked.',
  '',
  'A museum at 910 1st Corso (the museum association); its hours on that page could not be matched to it with certainty, so hours not checked. '+NCTOWN,
  [W('Grand Army of the Republic Memorial Hall (Nebraska City, Nebraska)'),HM('195041','G.A.R. Memorial Hall'),NCMA],brick='yes'),
N('otoe-county-courthouse-nebraska-city','Otoe County Courthouse','Nebraska City','ne','civic','standing',40.676201,-95.858302,'exact','view','walk','','1865',
  'A two-storey courthouse built in 1865 by William R. Craig and F. W. Wood for $22,500, before which the county used rooms in stores and once a cabin. A wing was added in 1882 and a matching one in 1936. Its marker and Wikipedia call it the oldest public building in Nebraska.',
  'The 1865 block with its two wings; Wikipedia mentions a mural of the town\'s history outside the courtrooms. Interior not checked.',
  '',
  'In use as the county and city courthouse, 1021 Central Avenue; public hours not checked. '+NCTOWN,
  [W('Otoe County Courthouse'),HM('272934','Otoe County Courthouse')],brick='yes'),
N('st-benedicts-church-nebraska-city','St. Benedict\'s Catholic Church','Nebraska City','ne','worship','standing',40.669664,-95.841003,'exact','view','walk','','1856–1861',
  'The parish was founded in 1856 and its church finished in 1861; Wikipedia calls it the oldest brick church in Nebraska. In 1948 its walls were found to be spreading, and they were taken down, reinforced and rebuilt mostly with the original brick.',
  'A brick vernacular Romanesque church with buttresses and an entry tower. Interior not checked.',
  '',
  'A working parish church at 411 5th Rue; see it from the street outside services. '+NCTOWN,
  [W("St. Benedict's Catholic Church (Nebraska City, Nebraska)"),NR('83001100',"St. Benedict's Catholic Church")],brick='yes'),
N('first-methodist-church-nebraska-city','First United Methodist Church (1855 wall)','Nebraska City','ne','worship','standing',40.677226,-95.858688,'site','view','walk','','1855–1856',
  'The Methodist mission at Nebraska City began a church here in 1855 and dedicated it in November 1856. The Nebraska Methodist Conference was organised in the town in 1861, and in 1936 the conference named this the "Mother Church of Methodism in Nebraska".',
  'Part of the first church survives as the south end of the present sanctuary, and a plaque marks a wall of the 1855 building (HMdb). Interior not checked.',
  '',
  'A working church at 11th Street (U.S. 75) and 1st Avenue; see the old wall from the street. '+NCTOWN,
  [HM('66936','Mother Church of Methodism in Nebraska'),HM('66938','Original 1855 wall')],brick='?'),
N('russell-majors-waddell-house-nebraska-city','Russell, Majors & Waddell House (Old Freighters Museum)','Nebraska City','ne','landmark','standing',40.679814,-95.863037,'exact','public','walk','','1858',
  'Built by the U.S. Army in 1858 for its quartermaster and sold in 1859 to Russell, Majors & Waddell, the freighting firm that hauled army supplies west and later ran the Pony Express. It was the firm\'s office, with Alexander Majors\'s family upstairs for a time. A marker records that six people Majors held enslaved escaped from his household in 1860 by the Underground Railroad and were never caught.',
  'The house, a private home from 1865 until it became the Old Freighters Museum in 1985, with exhibits on the freighting trade and the westward trails and a surviving piece of the 1860s "Steam Wagon" (museum association). Interior not checked.',
  '',
  'Run by the Nebraska City Historical Society, 407 North 14th Street. The museum association\'s page appears to give Thursday to Sunday, noon to 4 p.m., from Arbor Day to October 31 or by appointment, but its layout makes the match uncertain. '+NCTOWN,
  [HM('254117','Russell, Majors & Waddell House'),HM('251936','Alexander Majors Residence'),NCMA],brick='?'),
]

PIN_NOTES={
 'brownville-historic-district':'The HMdb position of the state marker in Boettner Park on Main Street; the district covers much of the village.',
 'brownville-methodist-church':'ArcGIS geocoder PointAddress for 423 Water Street, Brownville.',
 'brown-carson-house-brownville':'OpenStreetMap point "Brown-Carson Historic House" on Main Street (tools/nom.py).',
 'furnas-house-brownville':'ArcGIS geocoder PointAddress for 230 South 6th Street, Brownville, the address the county tourism page gives. The aerial shows only trees here; the LiDAR sheet shows a building-sized platform at the pin.',
 'muir-house-brownville':'HMdb position of the Muir House marker beside the driveway at Atlantic and North 2nd Streets.',
 'bailey-house-brownville':'ArcGIS geocoder PointAddress for 412 Main Street, Brownville (the county tourism page\'s address).',
 'captain-meriwether-lewis-dredge':'OpenStreetMap building "Captain Meriwether Lewis", mapped as a ship (tools/nom.py).',
 'brownville-bridge':'Wikipedia coordinate for the bridge, on the Nebraska half of the river.',
 'nemaha-county-courthouse-auburn':'Moved 76 m with tools/pix.py from the HMdb marker position at North and 19th Streets onto the courthouse in the middle of its square, which the aerial shows plainly.',
 'arbor-lodge-nebraska-city':'ArcGIS geocoder PointAddress for 2600 Arbor Avenue; OpenStreetMap puts the museum point 30 m away.',
 'wildwood-ware-house-nebraska-city':'ArcGIS geocoder StreetAddress (interpolated) for 420 Steinhart Park Road. On the aerial the pin is on the park road among trees with no house in the ring, so it is marked area.',
 'mayhew-cabin-nebraska-city':'ArcGIS geocoder PointAddress for 2012 4th Corso; the HMdb markers are 100 m south on the road. The aerial shows grass and trees in the ring and no cabin plainly; it may be under the trees.',
 'kregel-windmill-factory-nebraska-city':'ArcGIS geocoder PointAddress for 1416 Central Avenue; the HMdb marker is 15 m away.',
 'gar-memorial-hall-nebraska-city':'ArcGIS geocoder PointAddress for 910 1st Corso.',
 'otoe-county-courthouse-nebraska-city':'ArcGIS geocoder PointAddress for 1021 Central Avenue.',
 'st-benedicts-church-nebraska-city':'ArcGIS geocoder PointAddress for 411 5th Rue.',
 'first-methodist-church-nebraska-city':'HMdb position of the plaque on the 1855 wall at 11th Street and 1st Avenue.',
 'russell-majors-waddell-house-nebraska-city':'ArcGIS geocoder PointAddress for 407 North 14th Street.',
}
