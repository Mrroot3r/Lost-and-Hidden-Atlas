# November 22, 2026: the edges of region conf (Cohoes, Waterford, Watervliet), drawn at random by
# tools/choose.py --state ny. Seven earlier batches had worked Cohoes, Waterford, Watervliet and Green Island closely
# (data_conf_simf, _biei, _kovn, _edvk, _fmbb, _aunk, _fvsv), so this batch takes what they left in Cohoes and Waterford
# and then the old canal hamlet of Vischer Ferry, up the Mohawk in Clifton Park, which start.py listed as an old town
# centre with no Atlas place in it. The Clifton Park places are filed under sar, as earlier conf batches filed Halfmoon.
# Sources were opened in this session: Wikipedia as raw text (tools/wiki_raw.py); HMdb marker pages; the Town of Clifton
# Park's page on the Vischer Ferry marker; the draft National Register form for School No. 5 on parks.ny.gov.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]

BATCH={'key':'conf_ngwx','label':'Vischer Ferry and the edges of Cohoes and Waterford','added':'2026-11-22 08:42'}

HM=lambda n,t: L('HMdb: '+t,'https://www.hmdb.org/m.asp?m=%d'%n)
CPMARK=L('Town of Clifton Park: New historic marker for Vischer Ferry Historic District','https://cliftonparkny.gov/new-historic-marker-for-vischer-ferry-historic-district')

PLACES=[
N('vischer-ferry-hamlet','Vischer Ferry hamlet (Vischer Ferry Historic District)','Clifton Park','sar','town','standing',42.79712,-73.82848,'area','view','walk','canal','1735–1900s',
  'A ferry crossing on the Mohawk that grew into an Erie Canal hamlet. Nicholas Vischer built a house by the river about 1735 and his son Eldert began a rope ferry about 1790; Benjamin Mix kept a tavern by 1788, and the church built in 1802 gave the place its first name, Amity. The canal came through in 1822, and the boat carpenters of the two dry docks beside it built many of the Greek Revival houses that still line the streets. When canal traffic fell off about 1900 the hamlet became a small summer resort; left aside afterwards, it kept its nineteenth-century look and was listed on the National Register in 1975, with a boundary increase in 1997.',
  'Walk Riverview Road and Vischer Ferry Road: Greek Revival and Victorian houses of the canal years, among them the 1844 house of Shephard Wheeler and the 1850 house of Matthias Peters, both ships\' carpenters (Wikipedia\'s pictures), the Amity Reformed Church of 1888 and the Vischer homestead on Ferry Drive (see those places). The town counts 600 acres in the district, the canal preserve with Lock 19 and the dry docks included (see Vischer Ferry: Erie Canal Lock 19). Markers stand at Riverview and Vischer Ferry Roads and in a kiosk at the end of Ferry Drive. The 1797 inn on the site of the firehouse burned in 1947. The houses are private; interiors not checked.',
  'An Erie Canal village of boat carpenters that the twentieth century passed by.',
  'Town roads; the houses are private, so look from the road. The Town of Clifton Park has a small parking area with a kiosk at the end of Ferry Drive, and the Vischer Ferry Nature and Historic Preserve has its own lots on Riverview Road.',
  [W('Vischer Ferry Historic District'),W('Vischer Ferry, New York'),CPMARK,HM(171665,'Hamlet of Vischer Ferry'),HM(136461,'Vischer Ferry')],
  th=[42.79442,-73.83116],thn='Ferry Drive parking area',brick='?'),
N('amity-reformed-church-vischer-ferry','Amity Reformed Church and its burying ground, Vischer Ferry','Clifton Park','sar','worship','standing',42.79638,-73.82610,'site','view','drive','','1802; church 1888',
  'Families of Dutch descent on the north shore of the Mohawk had crossed the river to worship at Niskayuna until, in 1802, they were allowed a church of their own and built one that June, giving the hamlet the name Amity. Canal-era growth called for a larger church in 1871; it burned at Christmas 1886, and the present church went up in 1888. Its churchyard holds at least five veterans of the Revolutionary War, buried about 1812 to 1840.',
  'The 1888 church on Riverview Road, with the cemetery behind. The congregation\'s own history, quoted on the HMdb page, describes half-circle seating, a wainscoted ceiling, chandeliers and stained-glass windows. Markers for the church (1802 and 1888) and for the Patriot burials stand by the road. Service times not checked; interior not checked.',
  '',
  'An active church at 335 Riverview Road (the marker\'s address); look from the road, or attend a service. No page of the congregation\'s own could be found to give service times.',
  [HM(59690,'Amity Reformed Church'),HM(271946,'Patriot Burials'),HM(171665,'Hamlet of Vischer Ferry')],
  hours='?',brick='?'),
N('ferry-drive-vischer-homestead-vischer-ferry','Ferry Drive, Vischer Ferry: the Vischer homestead, the mill foundation and the 1900 bridge abutments','Clifton Park','sar','landmark','ruins',42.79437,-73.83127,'area','view','drive','','about 1740; mill gone about 1950; bridge 1900–1902',
  'Nicholas Vischer and his wife Annetie settled here after their marriage in 1734 and built a small brick house; about 1806 their son Eldert added a large two-story Federal front, and the town marker calls the house the oldest in Clifton Park. Eldert ran the rope ferry across the river in front of it from about 1790 and built a grist mill across the road; the mill in old photographs was probably the third on the site and was taken down about 1950. A toll bridge built here in 1900 lost two spans to ice in 1901 and was carried away whole by the spring flood of 1902; the ferry ran again until about 1924.',
  'From the end of Ferry Drive: the homestead, its old brick wing behind the Federal front. The town marker says the mill\'s foundation and millstones can still be found in the woods across Ferry Drive from the house, and that the stone abutments of the 1900 bridge remain on both banks of the Mohawk. Neither was checked on the ground or on the aerial; the pin is the parking area, not the ruins. Red brick: not checked (the marker says brick, not its colour).',
  'A ferry, a mill and a bridge that the river took, at the end of one short road.',
  'The parking area and kiosk at the end of Ferry Drive carry the Town of Clifton Park and Mohawk Towpath Byway markers; who owns the lot was not checked. The homestead is a private house, and the owner of the woods with the mill foundation is not known: look from the road and do not go onto the land without permission.',
  [HM(171540,'The Vischer Family'),HM(171541,'The Vischer Ferry Bridge'),HM(171491,'Ferry'),W('Vischer Ferry, New York')],
  conf='mixed',brick='?'),
N('abraham-best-house-clifton-park','Abraham Best House','Clifton Park','sar','landmark','standing',42.81201,-73.82572,'exact','view','drive','','about 1815',
  'A two-story, five-bay Federal brick house built about 1815 by Abraham and Harriet Best, who came from Claverack in Columbia County; Abraham Best died in 1871 at 81. It was renovated in the 1940s and was listed on the National Register in 2011.',
  'From Vischer Ferry Road: the brick front block on a limestone foundation, with a side-gable roof, chimneys inside each end wall and a Palladian window over the front door, and a rear kitchen wing; a barn of about 1900 stands on the property. A town marker of 1976 stands by the road. Private home; interior not checked. Red brick: not checked.',
  '',
  'Private home at 113 Vischer Ferry Road; look from the road and do not stop in the driveway.',
  [W('Abraham Best House'),HM(34759,'Best House')],
  brick='?'),
N('school-no-5-clifton-park','School No. 5, "the Little Red Schoolhouse"','Clifton Park','sar','civic','standing',42.84025,-73.79424,'exact','view','drive','','1903–1953',
  'A one-room brick district school that replaced an 1860s schoolhouse in 1903 and taught all grades in one classroom until 1953, when the district joined the new Shenendehowa central school district. It is now the Clifton Park Nursery School, whose records begin about 1957. It has been nominated to the National Register; the draft form is on the state\'s site.',
  'From Moe Road: a one-story, front-gabled brick schoolhouse on a stone foundation, its brick painted red, with wide white eaves; a vestibule was added about 1970. The nomination says the classroom keeps its original window trim, wainscoting, baseboards and chair rails. It is a working preschool, so the inside is not open to visitors.',
  '',
  'In use as the Clifton Park Nursery School at 344 Moe Road; look from the road, and keep clear of drop-off times.',
  [L('National Register nomination (draft): School No. 5, "The Little Red Schoolhouse" (parks.ny.gov)','https://www.parks.ny.gov/documents/shpo/national-register/SchoolNo5TheLittleRedSchoolhouseCliftonParkSaratogaCo.pdf')],
  brick='no'),
N('imperial-avenue-houses-cohoes','Imperial Avenue: the Dickey and Lackman houses','Cohoes','conf','landmark','standing',42.77128,-73.70586,'exact','view','walk','','1890 and 1895',
  'Two neighbouring Queen Anne houses on Imperial Avenue, one of the first streets laid out after Cohoes became a city in 1869, along the top of a sharp rise a mile west of downtown, where the city\'s managers built. William J. Dickey, superintendent of a textile mill, built his in 1890 at the highest point of the street; J. Leonard Lackman, a gunsmith and locksmith, built the other about 1895, and his descendants still lived there in 2009. Both were listed on the National Register in 1998.',
  'From the street: the Dickey house is a two-story frame house with a jerkin-headed front gable, a wraparound porch and Stick-style work under the front gable, and a round-arched stained-glass stair window on the north side. The Lackman house has a clapboarded first story and a shingled second, a corner turret with a conical spire over the porch, carved swags under the gables, and its own round-topped stained-glass stair window. The Register forms say both interiors keep their original plaster and woodwork; private homes, interiors not open.',
  '',
  'Private homes; look from Imperial Avenue.',
  [W('William J. Dickey House'),W('J. Leonard Lackman House')],
  brick='?'),
N('northside-district-waterford','Northside Historic District, Waterford','Waterford','conf','town','standing',42.78515,-73.69697,'area','view','walk','','1828–1900s',
  'The part of Waterford across the old Champlain Canal from the village, where mill owners built mansions beside their workers\' houses from 1828 on. The 60-acre district was listed on the National Register in 1975 with 125 contributing buildings, mostly Greek Revival and late Victorian houses. Its best-known houses are two Greek Revival mansions of about 1830: Hugh White\'s, now the Waterford Historical Museum, and William Mansfield\'s.',
  'Walk the streets round the museum for mill owners\' houses and smaller workers\' houses of the canal and mill years. Hugh White, the marker at his house says, helped develop the water power of Cohoes, built railroads, sat in Congress and was the brother of Canvass White, an engineer of the Erie Canal (see the Waterford Historical Museum). Which house is the Mansfield house was not checked. Most houses are private; interiors not checked.',
  '',
  'Village streets; the houses are private, so look from the sidewalk. The Waterford Historical Museum has its own hours and parking (see that place).',
  [W('Northside Historic District (Waterford, New York)'),HM(11532,'White Homestead')],
  brick='?'),
]

PIN_NOTES={
 'vischer-ferry-hamlet':'HMdb\'s position for the district marker at Riverview and Vischer Ferry Roads, in the middle of the hamlet; Wikipedia gives 42.79472, -73.82 for the district.',
 'amity-reformed-church-vischer-ferry':'The ArcGIS address point for 335 Riverview Road, the address HMdb gives for the church marker.',
 'ferry-drive-vischer-homestead-vischer-ferry':'HMdb\'s position for the Vischer Family marker in the parking area at the end of Ferry Drive. The pin is that lot, not the house, the mill foundation or the bridge abutment.',
 'abraham-best-house-clifton-park':'The ArcGIS address point for 113 Vischer Ferry Road; Wikipedia gives 42.81222, -73.82611 and the HMdb marker 42.8124, -73.8266.',
 'school-no-5-clifton-park':'The ArcGIS address point for 344 Moe Road, the address on the Register nomination.',
 'imperial-avenue-houses-cohoes':'Between the Wikipedia points of the two houses (42.77139, -73.70583 and 42.77118, -73.70589), which stand side by side.',
 'northside-district-waterford':'Moved from the Wikipedia point (42.785, -73.69278), which the aerial shows on open ground by a large mill building at the edge of the district, onto a street among the houses about 350 m west. The pin marks the district as a whole, not one building.',
}
