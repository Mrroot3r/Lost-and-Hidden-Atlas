# November 18, 2026: Philadelphia & southeast Pennsylvania (region pae, drawn at random by tools/choose.py), first pass:
# northern Chester County, the old iron country of the French Creek and Brandywine valleys, with Hopewell Furnace just over
# the line in Berks County. Iron furnaces and forges, the Revolutionary powder works and army hospital, an 18th-century
# custom mill, covered bridges, a Quaker meetinghouse, a church and a stone railroad viaduct.
# Facts come from the linked sources only. Wikipedia articles were read as raw text (tools/wiki_raw.py); the National Park
# Service visitor-center page, the Mill at Anselma, Historic Yellow Springs, WeConservePA, TrailLink, the Iron & Steel
# Heritage pages and a West Chester University park plan were read with tools/page.py. No National Register form was read.
# Where sources disagree the text gives both; where a source is silent it says "not checked".
# Pins: an OpenStreetMap feature or a Wikipedia/Register coordinate, as each pin note says, then looked at on the pin check
# (aerial and LiDAR sheets).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
NPS_HOFU=L('National Park Service: Hopewell Furnace visitor center (hours)','https://www.nps.gov/hofu/planyourvisit/visitorcenter.htm')
WCP_BENTLEY=L('WeConservePA: French and Pickering Creeks Conservation Trust opens new preserve','https://weconservepa.org/blog/french-and-pickering-creeks-conservation-trust-opens-new-preserve/')
WCP_CANNON=L('WeConservePA: Trust unearths four Revolutionary War era cannons','https://weconservepa.org/blog/french-pickering-creeks-conservation-trust-unearths-four-revolutionary-war-era-cannons/')
ISH_POWDER=L('Iron & Steel Heritage: Continental Powder Works','https://ironandsteelheritage.org/SE/powder_works.cfm')
TL_FCT=L('TrailLink: French Creek Trail','https://www.traillink.com/trail/french-creek-trail')
ANSELMA=L('The Mill at Anselma: Plan your visit','https://anselmamill.org/Visit')
HYS_RUINS=L('Historic Yellow Springs: Timeline of the Hospital Ruins (Washington Hall)','https://yellowsprings.org/timeline-of-the-hospital-ruins-washington-hall-at-yellow-springs/')
HYS_VISIT=L('Historic Yellow Springs: Visit','https://yellowsprings.org/visit/')
ISH_HIB=L('Iron & Steel Heritage: Hibernia County Park','https://ironandsteelheritage.org/SE/hibernia_park.cfm')
WCU_HIB=L('West Chester University: Hibernia County Park natural resource plan (2020, PDF)','https://www.wcupa.edu/business-PublicManagement/geographyPlanning/GIS/documents/HiberniaNRMP_PlanningStudioSpring2020.pdf')
MYC_HIB=L('MyChesCo: Hibernia County Park','https://www.mychesco.com/a/lifestyle/outdoor-recreation/hibernia-county-park-where-chester-county-still-hears-the-fiddles/')
PLACES=[
# ---- Iron ----
N('hopewell-furnace-elverson','Hopewell Furnace','Elverson','pae','industry','standing',40.20538,-75.77407,'exact','open','walk','','1771–1883',
  'An iron plantation built round a charcoal-fired, cold-blast furnace. Ironmaster Mark Bird founded it about 1771; it did best between 1820 and 1840, had a short revival in the Civil War, and blew out for the last time on 15 June 1883, beaten by anthracite-fired mills. It became one of the first historic sites in the National Park System in 1938, and the furnace, water wheel, blast machinery, cast house, blacksmith shop, barn and tenant houses were rebuilt and restored by 1952.',
  'The furnace group (stack, water wheel, blast machinery, cast house, charcoal house), the ironmaster\'s house, the company store, the blacksmith shop, a barn and workers\' houses: 14 restored buildings in 848 mostly wooded acres. Which buildings are open inside on a given day was not checked. The park\'s trails join those of French Creek State Park, which surrounds it on three sides.',
  'The furnace that outlived the charcoal-iron age by half a century.',
  'Hopewell Furnace National Historic Site (National Park Service), on Hopewell Road near Elverson, in Berks County just over the Chester County line. Visitor center and grounds open Wednesday to Sunday, 9 am to 5 pm, closed New Year\'s Day, Thanksgiving and Christmas; on closed days the buildings, parking lot and visitor center are shut but the trails stay open. It is a working farm: keep dogs away from the livestock. Hours from the NPS visitor-center page, read November 2026; fees not checked.',
  [NPS_HOFU,W('Hopewell Furnace National Historic Site')],th=[40.20690,-75.77346],thn='Hopewell Furnace visitor parking, Hopewell Road',brick='?',hours="Wednesday to Sunday, 9 a.m. to 5 p.m.; closed New Year's Day, Thanksgiving and Christmas. The trails stay open on closed days"),
N('warwick-furnace-ruins','Warwick Furnace ruins','Warwick Township','pae','industry','ruins',40.15010,-75.74014,'site','public','walk','','1737–1867',
  'An early iron furnace on the South Branch of French Creek, owned by Anna Rutter Nutt, widow of Samuel Nutt, and managed by George Taylor when the first Franklin stoves were cast here. The 1910 county marker says it was built in 1737 and the Wikipedia infobox gives 1738; the marker says it made shot and cannon for the Revolution and its last iron in 1867, and Wikipedia says it supplied iron for the USS Monitor. In 2015 the French & Pickering Creeks Conservation Trust protected the farm, and the trust later found four Revolutionary cannon cast here buried in the fields by the creek, hidden in 1777 from the advancing British.',
  'The ruins of the furnace, reached by a one-mile loop trail in the Thomas P. Bentley Nature Preserve, with the 1910 Chester County Historical Society marker. How much of the stack stands was not checked.',
  'Cannon cast here lay buried in the field next door for almost 250 years.',
  'Thomas P. Bentley Nature Preserve (French & Pickering Creeks Conservation Trust), on Warwick Furnace Road. Open dawn to dusk, with a one-mile loop trail to the furnace (WeConservePA report of the 2019 opening; the trust\'s own page was not read). The farm round the preserve is private: keep to the trail.',
  [WCP_BENTLEY,WCP_CANNON,W('Warwick Furnace Farms')],conf='mixed',th=[40.14986,-75.73935],thn='Bentley Preserve lot, Warwick Furnace Road',brick='?'),
N('hibernia-iron-works','Hibernia iron works and mansion','West Caln Township','pae','industry','standing',40.02924,-75.84211,'exact','public','walk','','1794–',
  'Samuel Downing built the first forge here on the West Branch of the Brandywine in 1794, to turn pig iron into bar iron. Charles Brooke bought the works in 1821 and became its most prosperous ironmaster; by 1850 Hibernia had two forges, two heating furnaces, a rolling mill, a grist mill, the mansion and workers\' houses. When the iron works closed was not checked. The ironmaster\'s mansion was remodelled in the early 20th century to look like an English country house, and the estate is now a county park of about 900 acres round Chambers Lake.',
  'The ironmaster\'s mansion, open for tours, and ruins of the iron works scattered through the park; the Forge and Forest Hill trails pass stone walls and foundations. The sources do not say which ruin was which building.',
  '',
  'Hibernia County Park (Chester County Parks), off Wagontown Road northwest of Coatesville. Walking tours of the mansion run from Memorial Day to Labor Day (Iron & Steel Heritage page). Park hours not checked: the county\'s park page was not found. Parking by the mansion and at the Forge Trail lot.',
  [ISH_HIB,WCU_HIB,MYC_HIB],th=[40.02961,-75.84193],thn='lot by Hibernia Mansion',brick='?'),
# ---- Revolution ----
N('continental-powder-works-french-creek','Continental Powder Works at French Creek','East Pikeland Township','pae','industry','ruins',40.13810,-75.55315,'site','public','walk','','1776–1777',
  'Built on French Creek early in 1776 to supply the Continental Army, the only powder mill and gun factory commissioned by the Continental Congress. It was meant to make two tons of powder a week and had a dam, mill race, powder and graining mills, a saltpeter house, four drying houses, a magazine, the superintendent\'s house and barracks for the militia guard. British troops burned it in September 1777; the site went on as a mill into the 1800s.',
  'Mostly ruins (Wikipedia; the site was listed on the National Register in 2015). French Creek Heritage Park, on the French Creek Trail, commemorates it. TrailLink says the trail by Rapps Dam Road reaches the ruins of Snyder\'s Mill and the site of Jacob Rudy\'s Powder Mill; how these relate to the Continental works was not checked, nor what can be seen of each.',
  'Washington\'s army got its powder and muskets from this creek until the British burned it.',
  'French Creek Heritage Park, on the French Creek Trail; the best parking is on either side of Rapps Dam Road just south of the covered bridge, where a paved, wheelchair-usable mile of trail begins (TrailLink). Who manages the park and its hours not checked.',
  [W('Continental Powder Works at French Creek'),ISH_POWDER,TL_FCT],conf='mixed',brick='?'),
N('washington-hall-yellow-springs','Washington Hall hospital ruins, Yellow Springs','Chester Springs','pae','civic','ruins',40.10063,-75.62162,'exact','public','walk','','1777–1781',
  'Congress had a general hospital built at the Yellow Springs spa after Washington saw the place; Washington Hall went up in 1777 and 1778, inoculated soldiers against smallpox and took most of the sick and wounded from Valley Forge. Congress ordered the hospital closed in September 1781. The later Yellow Springs village was a Civil War soldiers\' orphan school, then from 1916 to 1951 the country school of the Pennsylvania Academy of the Fine Arts, then a film studio, and since 1978 Historic Yellow Springs. When Washington Hall fell to ruin was not checked.',
  'The ruins of Washington Hall in the village, which Historic Yellow Springs keeps; the village\'s other old buildings (the Lincoln and Washington buildings) stand round it. What survives of the walls was not checked.',
  '',
  'Kept by Historic Yellow Springs, Inc., 1685 Art School Road, Chester Springs (who owns each piece of the land was not checked; the federal land map does not hold it). Grounds open dawn to dusk every day; office Monday to Friday 9 am to 4 pm. Parking in front of the Lincoln building and in the paved lot by the Washington building. Hours from the Historic Yellow Springs pages, read November 2026.',
  [HYS_RUINS,HYS_VISIT,W('Yellow Springs, Chester County, Pennsylvania')],th=[40.10063,-75.61915],thn='Historic Yellow Springs lot',brick='?'),
# ---- Mill ----
N('mill-at-anselma','Mill at Anselma (Lightfoot Mill)','Chester Springs','pae','industry','standing',40.08119,-75.64406,'exact','open','drive','','c. 1747–1982',
  'Samuel Lightfoot built this small custom grist mill about 1747 to grind for the farmers of Pikeland, the first of eight grist mills in the township. It later ground feed for the dairy farms and stayed at work until 1982. It is probably the only mill in the United States with its colonial-era power transmission still intact, and was made a National Historic Landmark in 2005.',
  'The mill with its colonial gearing, which is run on demonstration days, and the miller\'s house, on 22 acres of grounds. Open inside on weekend tours (below).',
  '',
  'The Mill at Anselma, outside Chester Springs. Open weekends April to December: Saturday 10 am to 2 pm and Sunday 1 pm to 4 pm, tours on the hour; on the second Saturday of the month (Demo Day) 10 am to 4 pm with the mill running. Adults $10, seniors and ages 5 to 14 $5, under 5 free. The grounds are open dawn to dusk unless a private event is on. From the mill\'s own visit page, read November 2026.',
  [ANSELMA,W('Lightfoot Mill')],th=[40.08160,-75.64350],thn='Mill at Anselma lot',brick='?',hours='April to December: Saturday 10 a.m. to 2 p.m., Sunday 1 to 4 p.m., tours on the hour; the second Saturday of the month 10 a.m. to 4 p.m.'),
# ---- Covered bridges ----
N('rapps-covered-bridge','Rapps Covered Bridge','East Pikeland Township','pae','landmark','standing',40.13838,-75.55274,'exact','public','drive','','1866',
  'A Burr-truss covered bridge built in 1866 by Benjamin F. Hartman across French Creek on Rapps Dam Road, one of three covered bridges over the creek. It was renovated in 1978 and in 2011; a tractor-trailer badly damaged it on April 29, 2014, and it reopened in October 2015.',
  'The covered bridge on fieldstone abutments, with horizontal siding and boxed cornices at the portals. The French Creek Trail passes it.',
  '',
  'A public road bridge: it carries Rapps Dam Road. Park on either side of Rapps Dam Road just south of the bridge (TrailLink).',
  [W('Rapps Bridge'),TL_FCT],brick='no'),
N('kennedy-covered-bridge','Kennedy Covered Bridge','Kimberton','pae','landmark','standing',40.14065,-75.57660,'exact','public','drive','','1856',
  'A Burr-truss covered bridge over French Creek built in 1856, damaged in an 1884 flood and repaired, and reinforced in 1936. Listed on the National Register in 1974.',
  'The wooden covered bridge. What its abutments are built of and whether it still carries cars were not checked.',
  '',
  'A public road bridge on West Seven Stars Road, near Kimberton. No parking lot is mapped at the bridge; pull off only where it is legal.',
  [W('Kennedy Bridge (Kimberton, Pennsylvania)')],brick='?'),
N('halls-covered-bridge','Hall\'s (Sheeder-Hall) Covered Bridge','East and West Vincent Townships','pae','landmark','standing',40.14784,-75.62048,'exact','public','drive','','1850',
  'Built in 1850, a two-span Burr-truss covered bridge over French Creek just below Birch Run, the oldest covered bridge in Chester County. Listed on the National Register in 1973.',
  'The two-span wooden covered bridge. What its abutments are built of and whether it still carries cars were not checked.',
  '',
  'A public road bridge, where Hollow Road crosses French Creek (OpenStreetMap). No parking lot is mapped nearby; pull off only where it is legal.',
  [W('Hall\'s Bridge')],brick='?'),
N('larkin-covered-bridge','Larkin Covered Bridge','Eagle','pae','landmark','standing',40.08248,-75.68558,'exact','public','walk','','1854',
  'Built in 1854 over Marsh Creek beside Jesse Larkin\'s grist mill at Milford Mills, and rebuilt in 1881. The state moved it north in 1972 before Milford Mills was cleared for Marsh Creek Lake, and in 2006 Upper Uwchlan Township took it down and set it up again on a trail by Graphite Mine Road. It now spans a dry ditch.',
  'The Burr-truss covered bridge, now a footbridge on the township trail.',
  '',
  'Upper Uwchlan Township trail, next to the entrance of the Byers Station development on Graphite Mine Road near Eagle. Trail hours not checked. No parking lot is mapped at the bridge.',
  [W('Larkin Covered Bridge (Chester Springs, Pennsylvania)')],brick='?'),
# ---- Standing ----
N('uwchlan-meetinghouse','Uwchlan Meetinghouse','Lionville','pae','worship','standing',40.05444,-75.66028,'site','view','drive','','1756',
  'Welsh Quakers built this rubble-fieldstone meetinghouse in 1756 to replace two log buildings. In the winter of 1777–78 it was a hospital for the Continental Army at Valley Forge, and the dead were buried behind it; in the Civil War it was offered as a hospital again, and soldiers scratched their names and regiments on the walls of the balcony. It was later the area\'s first library and a school, then a Grange hall from 1920 and a women\'s club from 1963, and was sold to the Uwchlan Conservation Trust.',
  'The 1756 stone meetinghouse and the burial ground behind it. The soldiers\' graffiti is in the balcony; whether and when the inside can be seen was not checked.',
  '',
  'On North Village Avenue (PA 113) in Lionville, owned by the Uwchlan Conservation Trust (Wikipedia). See it from the road; opening times not checked.',
  [W('Uwchlan Meetinghouse')],brick='no'),
N('st-marys-episcopal-warwick','Old St. Mary\'s Episcopal Church, Warwick','Elverson','pae','worship','standing',40.16583,-75.78111,'site','view','drive','','1806',
  'The Rev. Levi Bull founded the parish in 1805 and the first church was built in 1806; Julius Sachse of the Historical Society of Pennsylvania thought it the first church built in Pennsylvania after the Revolution. Bull replaced it in 1843 with the present Gothic Revival church of stuccoed fieldstone, 50 by 70 feet, and served here almost fifty years. The congregation fell to about ten in the 1970s and revived in the 1990s.',
  'The 1843 church in its graveyard, with burials from 1806, among them the Revolutionary officer and ironmaster Samuel Van Leer. Interior not checked.',
  '',
  'On Warwick Road, Warwick Township. A working church: see it from the road and the churchyard; service times not checked.',
  [W('St. Mary\'s Episcopal Church (Elverson, Pennsylvania)')],brick='no'),
N('coatesville-high-bridge','Coatesville High Bridge','Coatesville','pae','rail','standing',39.98389,-75.82750,'site','view','drive','','1902–1904',
  'The Pennsylvania Railroad built this stone-arch viaduct of ten arches in 1902 to 1904 to carry four tracks of its Main Line across the Brandywine water gap at Coatesville. The first bridge here, of 1832, was a single wooden track on stone piers, followed by cast-iron (1867) and wrought-iron (1890) spans. President A. J. Cassatt chose stone here though the railroad had built in steel since the 1880s. The bridge passed to Penn Central in 1968 and to Amtrak in 1976.',
  'The ten masonry arches over the West Branch of the Brandywine, the old Wilmington and Northern line and PA 82.',
  '',
  'Amtrak\'s Main Line, in use: see it from PA 82 and the streets below, never from the tracks.',
  [W('High Bridge (Coatesville, Pennsylvania)')],brick='no'),
]
PIN_NOTES={
 'hopewell-furnace-elverson':'The furnace building as mapped in OpenStreetMap; the trailhead point is the visitor parking lot OpenStreetMap maps on Hopewell Road.',
 'warwick-furnace-ruins':'The furnace ruin as mapped in OpenStreetMap (historic=ruins), inside the Bentley Preserve; the leaf-off aerial shows a roofless stone ruin under the ring and the LiDAR a mound round it. The trailhead point is the preserve lot OpenStreetMap maps 70 m east, by a small building at the road; the lot itself is hard to make out on the aerial.',
 'hibernia-iron-works':'Hibernia Mansion as mapped in OpenStreetMap; the aerial shows the house under the ring and the lot just north; the forge ruins are spread along the Forge and Forest Hill trails and were not pinned.',
 'continental-powder-works-french-creek':'The National Register coordinate (Wikipedia), at the south end of Rapps covered bridge on Rapps Dam Road; the ruins themselves were not pinned and are not visible under the trees on the aerial. The LiDAR shows a long straight channel running southwest from the pin beside the creek, perhaps a race; not confirmed.',
 'washington-hall-yellow-springs':'Washington Hall as mapped in OpenStreetMap in the Chester Springs historic district; the leaf-off aerial and the LiDAR both show a roofless rectangular outline under the ring. The trailhead point is the paved lot OpenStreetMap maps 210 m east, seen on the aerial.',
 'mill-at-anselma':'The watermill as mapped in OpenStreetMap, on the mill building on the aerial; the trailhead point is the lot it maps 66 m northeast.',
 'rapps-covered-bridge':'The Rapps Dam Road bridge over French Creek as mapped in OpenStreetMap, 16 m from the Wikipedia coordinate; the aerial shows the covered bridge under the ring.',
 'kennedy-covered-bridge':'The West Seven Stars Road bridge over French Creek as mapped in OpenStreetMap, 41 m from the Register coordinate; the aerial shows the roofed bridge under the ring.',
 'halls-covered-bridge':'The Hollow Road bridge over French Creek as mapped in OpenStreetMap, 48 m from the Register coordinate; the aerial shows the bridge under the ring.',
 'larkin-covered-bridge':'The covered bridge as mapped in OpenStreetMap by Graphite Mine Road; the aerial shows the roofed bridge beside the road under the ring.',
 'uwchlan-meetinghouse':'The Register coordinate (Wikipedia), on North Village Avenue in Lionville; it falls on a lawn among buildings and which building is the meetinghouse was not settled on the aerial, so the pin is kept as site.',
 'st-marys-episcopal-warwick':'The Register coordinate (Wikipedia), on trees at the west edge of the graveyard north of Warwick Road; the church is probably the large roof at the graveyard\'s south edge about 60 m away, but that was not certain, so the pin is kept as site.',
 'coatesville-high-bridge':'The Register coordinate (Wikipedia), on the viaduct as the aerial shows.',
}
BATCH={'key':'pae_ievd','label':'Northern Chester County, Pennsylvania','added':'2026-11-18 11:40'}
