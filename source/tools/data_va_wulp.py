# November 20, 2026: Virginia, a first scatter across the state (the state had one place, Belle Isle in Richmond).
# Region claimed with tools/choose.py --thinnest (va). Fifteen places from the Tidewater and the Eastern Shore to the
# Alleghany Highlands and the Pocahontas coalfield, standing and ruined, 1665 to the 1900s.
# Sources read in this session: Wikipedia articles (tools/wiki_raw.py) and the pages of the bodies that run each place
# (tools/page.py): Preservation Virginia (Bacon's Castle), NOVA Parks (Aldie Mill), the City of Petersburg (Blandford
# Church), Barboursville Vineyards, the Corporation for Jefferson's Poplar Forest, the National Park Service (Historic
# Jamestowne hours and fees, Appomattox Court House hours, Mabry Mill), the US Forest Service (Roaring Run day use area and
# loop trail, Elizabeth Furnace recreation area), Virginia Energy (Pocahontas Exhibition Mine), the US Fish and Wildlife
# Service (an Assateague Lighthouse climbing day) and Visit Alleghany Highlands (Humpback Bridge). The pages of Historic
# St. Luke's (HTTP 403) and the Prestwould Foundation (connection reset) could not be read. Interiors were not visited by
# any source opened unless the entry says so.
from data_b import N
from data_ma import W
BATCH={'key':'va_wulp','label':'Virginia: a first scatter across the state','added':'2026-11-20 02:20'}

GWJ='George Washington and Jefferson National Forests (US Forest Service). '

PLACES=[
N('barboursville-ruins','Barboursville ruins (James Barbour\'s mansion)','Barboursville','va','landmark','ruins',38.16237,-78.28069,'site','open','walk','','c. 1822–1884',
  'The house of James Barbour, governor of Virginia, US senator and Secretary of War, built from designs by his friend Thomas Jefferson and finished about 1822 in a Neo-Palladian style, with a Roman Doric portico on the entrance front and an octagonal drawing room projecting into a second portico on the garden front, as at Monticello. It burned on Christmas Day 1884; only the outer brick walls, the inner masonry partitions and the portico columns survived. The ruin has been stabilised and stands on the grounds of Barboursville Vineyards.',
  'The roofless brick shell on a knoll, with the columns of the porticoes standing. The vineyard invites visitors to walk to the "Landmark Ruins" on their own. Two service buildings north of the house, believed to date from about 1790, where Barbour lived until the house was finished, are now an inn for the vineyard\'s guests (Wikipedia). Library 1821 in the old winery building shows Barbour papers and household china (vineyard page).',
  'A Jefferson house that burned on Christmas Day and was left standing as a ruin.',
  'Private: on the grounds of Barboursville Vineyards, which opens the estate every day and asks guests to stroll the grounds and see the ruins on their own; no reservation is needed. A wine tasting costs $20; the page names no charge for walking to the ruins (vineyard tasting-room page, read November 20, 2026). Parking at the winery; the mapped lot point on Mansion Road was on the road on the aerial, so none is given.',
  [W('Barboursville (James Barbour)'),['Barboursville Vineyards: tasting room and ruins','https://www.bbvwine.com/tour-tasting/tasting-room']],
  brick='yes',
  hours='Estate and tasting room: Monday to Saturday 10 a.m. to 5 p.m., Sunday 11 a.m. to 5 p.m.; shorter on December 24 and 31'),

N('blandford-church-petersburg','Blandford Church and its Tiffany windows','Petersburg','va','worship','standing',37.22583,-77.38778,'exact','open','drive','cemeteries','1736',
  'An Anglican church built in 1736 on Well\'s Hill, the highest point in Petersburg, also called St. Paul\'s or "The Brick Church". It was abandoned in 1806 and became an ivy-covered shell; in the Civil War it served as a telegraph station and as a field hospital after the Battle of the Crater in 1864. The city repaired it in 1882, and from 1901 the Ladies\' Memorial Association made it a memorial chapel for the Confederate dead buried in Blandford Cemetery around it, many unidentified in mass graves. It is now a city museum.',
  'Fifteen stained-glass windows designed and installed by Louis Comfort Tiffany\'s studio between 1901 and 1912 (the city page; Wikipedia gives 1904 to 1912), paid for by the former Confederate states and others: each large window shows a saint, one was given by Tiffany himself, and the half-round window over the door carries the only Confederate flag Tiffany is known to have made (Wikipedia). The pulpit and 34 pews were paid for between 1889 and 1905. The interior is shown by guided tour. Blandford Cemetery round it holds 18th- to 20th-century gravestones, sculpture and iron fences.',
  'An abandoned colonial church turned into a Tiffany memorial chapel.',
  'Run by the City of Petersburg as the Blandford Church Museum, 111 Rochelle Lane. Admission is charged; the church is wheelchair accessible; the cemetery is open every day (city page, read November 20, 2026). Parking was not checked on the ground; no mapped lot lies near the church.',
  [W('Blandford Church'),['City of Petersburg: Blandford Church Museum & Cemetery','https://www.petersburgva.gov/2328']],
  brick='yes',hours='Thursday to Saturday 10 a.m. to 4 p.m., Sunday 1 to 4 p.m.; Monday to Wednesday by appointment; cemetery every day'),

N('bacons-castle','Bacon\'s Castle (Arthur Allen\'s brick house)','Surry','va','landmark','standing',37.10903,-76.72238,'exact','open','drive','','1665',
  'The oldest documented brick dwelling in the United States, built in 1665 for the merchant Arthur Allen in a high Jacobean (Carolean) style. In September 1676 followers of Nathaniel Bacon seized and fortified it during Bacon\'s Rebellion and held it for about four months, which gave it its name; Bacon himself is not known ever to have been there. Preservation Virginia bought it at auction in the 1970s and restored and furnished it in the 1980s.',
  'Triple-stacked chimneys and shaped Flemish gables outside, and carved compass roses on the cross beams of many rooms (Wikipedia). The grounds hold a reconstructed 17th-century English formal garden, an 1830 slave dwelling, an 1820s smokehouse and a barn dated to about 1700 (Preservation Virginia). The inside is seen on a 45-minute guided tour; Preservation Virginia says the house is in a two-year restoration and some furnishings are off view, with tours going on as scheduled.',
  'The house the rebels held, and the oldest brick house in the country.',
  'Owned and run by Preservation Virginia, 465 Bacons Castle Trail, Surry. Interior tours March to December: $15, seniors, AAA and military $12, students $10, under 6 free; a self-guided phone tour covers the grounds and garden; ample parking on site (Preservation Virginia page, read November 20, 2026).',
  [W('Bacon\'s Castle'),['Preservation Virginia: Bacon\'s Castle','https://preservationvirginia.org/historic-sites/bacons-castle/']],
  brick='yes',hours='March to December: Friday and Saturday 10 a.m. to 5 p.m., Sunday noon to 5 p.m.; Thursday 10 a.m. to 5 p.m. in June, July and August'),

N('humpback-covered-bridge','Humpback Covered Bridge','Covington','va','landmark','standing',37.80059,-80.04701,'exact','public','drive','','1857',
  'The oldest covered bridge left in Virginia, built in 1857 over Dunlap Creek on the James River and Kanawha Turnpike, after three earlier uncovered bridges at about the same spot were lost to floods in 1837 and 1842 and to wear in 1856. It is 109 feet long and built 4 feet higher in the middle than at the ends, a shape few covered bridges have. Traffic moved to a steel bridge for US 60 just to the north in 1929; a farmer stored hay in it into the early 1950s, and in 1954 a five-acre wayside park opened round it.',
  'The arched timber bridge across the creek, which can be walked; the wayside has parking, restrooms, picnic tables and access to Dunlap Creek (Wikipedia, Visit Alleghany Highlands).',
  'A covered bridge built with a hump, the oldest in the state.',
  'A public wayside park beside US 60 west of Covington, opened in 1954 by the Virginia Highway Department and local groups (Wikipedia). Hours were not found on any page read.',
  [W('Humpback Covered Bridge'),['Visit Alleghany Highlands: Humpback Bridge','https://visitalleghanyhighlands.com/listings/humpback-bridge/']],
  th=[37.80022,-80.04746],thn='Humpback Bridge wayside lot',brick='no'),

N('roaring-run-furnace','Roaring Run Furnace','Eagle Rock','va','industry','ruins',37.70813,-79.89281,'site','public','walk','','c. 1832',
  'An iron furnace built about 1832 on Roaring Run in what is now the Jefferson National Forest near Eagle Rock, at the north-east corner of the Hoop Hole wild area. It worked before the Civil War and stands for the iron industry that spread through the Virginia mountains in the 1800s. It was listed on the National Register in 1983.',
  'The furnace stack beside the Woodland Trail, the return half of the 1.5-mile Roaring Run loop: most walkers go up the Streamside Trail past stone bridges to Roaring Run Falls and come back past an overlook and the furnace to the picnic area (Forest Service trail page). Wikipedia\'s photographs show a stone stack with an arched opening, on a stone-walled base.',
  'A furnace stack on the way back from a waterfall.',
  GWJ+'Roaring Run Day Use Area, Eastern Divide Ranger District: open all year, sunrise to sunset, no fee, vault toilets, no drinking water; dogs on a leash no longer than 6 feet. From Eagle Rock take Craig Creek Road (SR 615) 5.5 miles, then Roaring Run Road (SR 621) 1 mile; the entrance is on the left (Forest Service pages, read November 20, 2026).',
  [W('Roaring Run Furnace'),['USFS: Roaring Run Day Use Area','https://www.fs.usda.gov/r08/gwj/recreation/roaring-run-day-use-area'],['USFS: Roaring Run Loop Trail','https://www.fs.usda.gov/r08/gwj/recreation/trails/roaring-run-loop-trail-forest-trail-264']],
  th=[37.70638,-79.89319],thn='Roaring Run Day Use Area lot',brick='no',hours='All year, sunrise to sunset'),

N('elizabeth-furnace-fort-valley','Elizabeth Furnace','Fort Valley','va','industry','ruins',38.93139,-78.32306,'area','public','walk','','1836–1888',
  'A blast furnace on Passage Creek that made pig iron from 1836 to 1888, using the creek for water power and ore mined nearby. The iron was hauled over Massanutten Mountain to the South Fork of the Shenandoah and on to Harpers Ferry for forging; hikers on the Massanutten Trail still use that road. The site is now the Elizabeth Furnace Recreation Area of the George Washington National Forest.',
  'Much of the original stone furnace still stands (Wikipedia). The Pig Iron and Charcoal Trail explains how iron was mined and smelted here, and a swinging bridge crosses to a restored 1830s cabin by the campground (Forest Service page).',
  'Iron hauled over a mountain on a road hikers still walk.',
  GWJ+'Elizabeth Furnace Recreation Area, Lee Ranger District: day use open all year from sunrise to sunset, no fee for day use, limited amenities in winter; alcohol prohibited; dogs on a leash. From Strasburg take VA 55 east 5 miles to Waterlick, then SR 678 about 3.5 miles (Forest Service page, read November 20, 2026).',
  [W('Elizabeth Furnace'),['USFS: Elizabeth Furnace Recreation Area','https://www.fs.usda.gov/r08/gwj/recreation/elizabeth-furnace-recreation-area']],
  th=[38.92775,-78.32946],thn='Pig Iron Interpretive Trail lot',brick='no',hours='Day use all year, sunrise to sunset'),

N('aldie-mill','Aldie Mill','Aldie','va','industry','standing',38.97523,-77.64103,'site','open','drive','','1807–1809',
  'A merchant mill on the Little River, built between 1807 and 1809 by William Cooke for Charles F. Mercer, on a site where Mercer\'s father had run a tub mill from about 1764; the village that grew round it was named Aldie in 1810. Its first machinery was Oliver Evans\'s patented system. John Moore bought it in 1835 and his descendants ran it for six generations, until 1971.',
  'A two-storey brick mill with two loft levels, driven by two overshot water wheels set one after the other; much of the machinery and the wheels were replaced at the start of the 1900s, and the restored metal wheels turn the machinery again. A two-storey brick miller\'s house stands behind it between the river and the race (Wikipedia). NOVA Parks says it is the only mill with tandem overshot wheels open to the public in Virginia; guided tours of the mill on spring to autumn weekends.',
  'Two water wheels, one behind the other, still turning a mill.',
  'Aldie Mill Historic Park, run by NOVA Parks (Northern Virginia Regional Park Authority), on US 50 in Aldie. The grounds and the village can be visited all year; the mill opens for guided tours on weekends from April 1 to November 1 (NOVA Parks page, read November 20, 2026).',
  [W('Aldie Mill Historic District'),['NOVA Parks: Aldie Mill Historic Park','https://novaparks.com/parks/aldie-mill-historic-park']],
  brick='yes',hours='April 1 to November 1: Saturday and Sunday 11 a.m. to 4 p.m.; closed November 2 to March 30'),

N('prestwould-clarksville','Prestwould','Clarksville','va','landmark','standing',36.64972,-78.56417,'site','open','drive','','1795–1797',
  'A stone plantation house built for Sir Peyton Skipwith, who moved his family here from Elm Hill in 1797. Wikipedia calls it the most intact and best documented plantation left in Southside Virginia. The Prestwould Foundation has run it as a historic site since 1963; it became a National Historic Landmark in 2003.',
  'A seven-bay stone house with a hipped roof, a pair of interior chimneys and Doric porches on three sides, on a hill above the upper end of Kerr Reservoir. The complex has eight buildings, all from before 1830 and most from the 1780s; the outbuildings, among them an office, are of wood frame (Wikipedia). Interior not checked.',
  '',
  'Owned and run by the Prestwould Foundation, about a mile north of Clarksville off US 15. Wikipedia says it is open for tours from April to October or by appointment; the foundation\'s own page (prestwould.org) could not be read in this session, so hours were not checked. No mapped parking lot is near the house; parking not checked.',
  [W('Prestwould'),['Prestwould Foundation','https://www.prestwould.org/']],
  brick='no',hours='?'),

N('jamestown-church-tower','Jamestown Church tower and Memorial Church','Jamestown','va','worship','standing',37.20853,-76.77839,'exact','open','walk','cemeteries','1639–1700 (tower); 1907',
  'The brick church tower at Jamestown, added in two stages some time between 1639 and 1700 to an earlier church, is the last structure standing above ground from the years when Jamestown was the capital of Virginia. The church fell to ruin by the 1790s, when its bricks went into the graveyard wall. In 1907 the National Society of the Colonial Dames of America built the Memorial Church against the old tower, just outside the foundations of the 1617 and 1639 churches. Preservation Virginia owns it; the tower was repaired with about 5,000 new handmade bricks in 2013 and 2014.',
  'The old tower, and inside the 1907 church the cobblestone and brick foundations of the 1617 church, visible under glass in the floor (Wikipedia). The brick-walled graveyard of the 1790s is beside it. Whether the church is open at a given time was not checked.',
  'The only thing left standing of the first capital.',
  'Historic Jamestowne, run jointly by Preservation Virginia and the National Park Service (Colonial National Historical Park) at the west end of the Colonial Parkway. An entrance pass is required for every visitor (NPS hours and fees pages, read November 20, 2026). The Island Drive lot is the parking given here.',
  [W('Jamestown Church'),['NPS: Historic Jamestowne hours','https://www.nps.gov/jame/planyourvisit/hours.htm'],['NPS: Historic Jamestowne fees','https://www.nps.gov/jame/planyourvisit/fees.htm'],['Historic Jamestowne: plan your visit','https://historicjamestowne.org/visit/plan-your-visit/']],
  th=[37.21159,-76.7766],thn='Island Drive lot, Historic Jamestowne',brick='yes',
  hours='Daily 9 a.m. to 5 p.m. (entrance gate from 8:45 a.m.); closed Thanksgiving, December 25 and January 1'),

N('st-lukes-church-smithfield','St. Luke\'s Church (Old Brick Church)','Smithfield','va','worship','standing',36.94057,-76.58548,'exact','open','drive','','1632 or 1682',
  'A brick church at Benns Church near Smithfield, called the oldest church in Virginia and the oldest brick church in British North America. Local tradition dates it to 1632; other evidence points to 1682, and the date is disputed. It became a National Historic Landmark in 1966. A private non-profit, Historic St. Luke\'s, has kept the 100-acre site since 1954 without government money.',
  'A single room with a tower at the west end that is part of the first build, the only original tower known on a colonial church in Virginia; brick laid in Flemish bond, buttresses on the north and south walls (no other standing church has them), Y-tracery windows, crow-stepped gable ends and a great east window of round- and pointed-headed lights in tiers. The original glass was replaced in the 1800s; the Victorian windows remain, and the glass over the altar was made in Germany (Wikipedia). Interior not checked.',
  'A church old enough that nobody agrees within fifty years when it was built.',
  'Owned and run by Historic St. Luke\'s, a private non-profit, on Benns Church Boulevard (VA 10) near Smithfield. Its pages (stlukesmuseum.org) answered HTTP 403 in this session, so hours, fees and parking were not checked.',
  [W('St. Luke\'s Church (Smithfield, Virginia)'),['Historic St. Luke\'s: hours and tours','https://stlukesmuseum.org/hours-schedule/']],
  brick='yes',hours='?'),

N('assateague-light','Assateague Lighthouse','Chincoteague','va','light','standing',37.91118,-75.35603,'exact','public','walk','','1867',
  'A 142-foot conical lighthouse built in 1867 on Assateague Island to replace a 45-foot tower of 1833, painted in bands of red and white. It stands in the Chincoteague National Wildlife Refuge, owned by the US Fish and Wildlife Service and kept by the Coast Guard as a working aid to navigation. The island has grown about five miles south since the first light was placed at its tip. A $1.5 million repair was finished in 2013.',
  'The tower, the keeper\'s house and the oil house; the keeper\'s quarters house refuge staff and volunteers. The first-order Fresnel lens is in the Museum of Chincoteague Island (Wikipedia). Wikipedia says the tower is open for climbs on summer Saturdays; a Fish and Wildlife Service event page gave climbing hours of 10 a.m. to 3:30 p.m. for one such day in May 2025. Current climbing days not checked.',
  '',
  'Chincoteague National Wildlife Refuge (US Fish and Wildlife Service), reached by road from Chincoteague across the Assateague Channel; the Lighthouse Trail leads to it. Refuge hours and entrance fees were not checked: the refuge\'s visit page answered HTTP 404.',
  [W('Assateague Light'),['USFWS: Assateague Lighthouse climbing day','https://www.fws.gov/event/assateague-lighthouse-birds-eye-view-refuge']],
  th=[37.91041,-75.35382],thn='Refuge lot on Beach Road',brick='no'),

N('poplar-forest','Thomas Jefferson\'s Poplar Forest','Forest','va','landmark','standing',37.34802,-79.26456,'exact','open','drive','','1806',
  'The retreat house Thomas Jefferson designed and began building in 1806, while president, on land he inherited in 1773; he came here every year from 1810 to 1823. The brick house has an octagonal plan, a square dining room at the centre with elongated octagonal rooms round it, and may have been the first octagonal house built in the United States. A fire in 1845 led the Cobbs and Hutter families to rebuild it in the Greek Revival style with an attic storey. It has been open to visitors since 1986, and a restoration to Jefferson\'s design was completed in April 2023.',
  'The restored octagonal brick villa, seen on docent tours at 10:30 a.m., noon, 1 p.m. and 2:30 p.m. when a docent is free, or with the Poplar Forest app. Archaeologists still work on the site, including the Wingo quarter where enslaved people lived from about 1790 to 1812 (Wikipedia). The walking trails are free; admission is needed for the rest of the grounds (Poplar Forest page).',
  'Jefferson\'s octagon, rebuilt after a fire and restored back.',
  'Run by the Corporation for Jefferson\'s Poplar Forest, a non-profit, at Forest near Lynchburg. Tickets are needed for the house and grounds; tours cannot be guaranteed a docent unless booked privately (Poplar Forest tickets page, read November 20, 2026).',
  [W('Poplar Forest'),['Poplar Forest: tickets and hours','https://www.poplarforest.org/tickets/']],
  th=[37.34699,-79.2657],thn='Lot on Poplar Forest Parkway',brick='yes',
  hours='Daily mid-January to December 30, except Easter, Thanksgiving and December 24–25; last admission 4:30 p.m. (March to November), 3:30 p.m. (December to February)'),

N('mabry-mill','Mabry Mill','Meadows of Dan','va','industry','standing',36.75088,-80.406,'exact','public','drive','','1903–1910',
  'A mill at milepost 176.2 of the Blue Ridge Parkway, built by Edwin Boston Mabry, who came home to Floyd County in 1903. It began as a blacksmith and wheelwright shop, then a sawmill, and was grinding grain by 1905; by 1910 the front part was finished with lathes, a planer and a jigsaw. He and his wife Lizzy ground corn, sawed lumber and did blacksmithing here for three decades. It is now kept by the National Park Service.',
  'The gristmill, Mabry\'s original sawmill and blacksmith shop, and Matthew\'s Cabin, moved here by the Parkway\'s designers, on the half-mile Mabry Mill (Mountain Industry) Trail. The insides of the buildings open seasonally, with craft demonstrations on summer and early autumn weekends and Sunday afternoon music (NPS page, Wikipedia). Wikipedia\'s photograph shows weathered board buildings and an overshot wheel over the millpond.',
  '',
  'Blue Ridge Parkway (National Park Service), milepost 176, 3 miles north of Meadows of Dan off US 58. Parking for cars and buses on site; pets allowed; seasonal restrooms (NPS pages, read November 20, 2026).',
  [W('Mabry Mill'),['NPS: Mabry Mill, Milepost 176','https://nps.gov/blri/planyourvisit/mabry-mill-mp-176.htm'],['NPS: Mabry Mill (place)','https://www.nps.gov/places/mabry-mill.htm']],
  th=[36.74976,-80.40515],thn='Mabry Mill lot on the Parkway',brick='no'),

N('pocahontas-exhibition-mine','Pocahontas Exhibition Coal Mine','Pocahontas','va','industry','standing',37.30806,-81.34972,'area','open','drive','','1882',
  'Pocahontas Mine No. 1, the "Baby Mine", opened in 1882 as the first mine in the Pocahontas coalfield, in a 13-foot seam; it was worked for 73 years, until mining in Pocahontas stopped in 1955. Its coal was turned to coke on the site and sent by rail to Norfolk, and in both world wars it supplied much of the Navy\'s coal. In 1938 it became the first exhibition coal mine in the country, and until 1970 visitors could drive their cars through it. It became a National Historic Landmark in 1994.',
  'Guided trips underground into the old workings. The spoil pile covers the place where the beehive coke ovens stood; three oven ruins are left, overgrown with trees (Wikipedia).',
  'The first coal mine opened to tourists, which once let them drive through.',
  'Run with the Town of Pocahontas, 215 Shop Hollow Road; Virginia Energy inspects it for safety. Groups of 12 or more can book a tour through December by telephone or email (Virginia Energy page, read November 20, 2026). The mapped lot on Shop Hollow Road beside the mine\'s street address is given as its parking; not checked on the ground.',
  [W('Pocahontas Exhibition Coal Mine'),['Virginia Energy: Pocahontas Exhibition Mine','https://energy.virginia.gov/public/Pocahontas-Exhibition-Mine.shtml']],
  th=[37.3074,-81.34594],thn='Lot on Shop Hollow Road, by 215 Shop Hollow Road',brick='no',hours='April to September: Thursday to Saturday 10 a.m. to 5 p.m., Sunday noon to 4 p.m.'),

N('appomattox-court-house-village','Appomattox Court House village','Appomattox','va','town','standing',37.3775,-78.796,'area','open','walk','','1840s',
  'The village of Clover Hill on the Richmond to Lynchburg stage road became the county seat of Appomattox County in the 1840s. Here, in the McLean House, Lee surrendered the Army of Northern Virginia to Grant on April 9, 1865. The railroad passed it by in 1854, and after the courthouse burned in 1892 the county seat moved to Appomattox Depot; the McLean House was taken down. The National Park Service rebuilt the McLean House, which reopened in 1949, and the courthouse, and restored the village.',
  'Original 19th-century buildings, among them the Clover Hill Tavern, where about 30,000 parole passes were printed in 26 hours after the surrender, stand beside the rebuilt McLean House and courthouse (Wikipedia, NPS). The visitor centre is in the rebuilt courthouse. The McLean House is open and staffed daily in the warm season and may keep shorter hours in winter (NPS).',
  'The war ended in a parlour, and the parlour was rebuilt from nothing.',
  'Appomattox Court House National Historical Park (National Park Service), on VA 24 north-east of the town of Appomattox (NPS hours page, read November 20, 2026). The fees page was read but gave no entrance fee for this park.',
  [W('Appomattox Court House National Historical Park'),['NPS: Appomattox Court House hours','https://www.nps.gov/apco/planyourvisit/hours.htm']],
  th=[37.3759,-78.79722],thn='Lot on Back Lane, Appomattox Court House NHP',brick='some',
  hours='Daily 9 a.m. to 5 p.m. (9 a.m. to 2 p.m. on December 24); closed Thanksgiving, December 25 and January 1'),
]

PIN_NOTES={
 'barboursville-ruins':'Wikipedia coordinate for the ruin.',
 'blandford-church-petersburg':'Wikipedia coordinate; the ArcGIS geocoder put 111 Rochelle Lane 100 m north.',
 'bacons-castle':'Wikipedia coordinate; the ArcGIS geocoder\'s point for 465 Bacons Castle Trail is 5 m away.',
 'humpback-covered-bridge':'OpenStreetMap bridge "Humpback Covered Bridge" (nom.py), the same as the Wikipedia coordinate; on the aerial it is on the bridge over the creek. The wayside lot was read off the aerial with pix.py (no lot is mapped).',
 'roaring-run-furnace':'OpenStreetMap point "Roaring Run Furnace" (historic=ruins, nom.py), 50 m from the Wikipedia coordinate; the LiDAR shows a mound at the pin beside the stream junction, taken to be the stack. The day-use lot is 155 m south.',
 'elizabeth-furnace-fort-valley':'Wikipedia coordinate for the furnace; on the aerial it is in trees and on the LiDAR it sits on a track along Passage Creek with no stack picked out. Pin marks the area; the Pig Iron Interpretive Trail lot, 500 m south-west, is given as parking.',
 'aldie-mill':'OpenStreetMap point "Historic Aldie Mill" (tourism=attraction, nom.py); the Wikipedia article gives no coordinate.',
 'prestwould-clarksville':'Wikipedia coordinate.',
 'jamestown-church-tower':'Wikipedia coordinate.',
 'st-lukes-church-smithfield':'The Wikipedia coordinate fell on grass 43 m east of a long dark-roofed building, taken to be the church; moved onto it with pix.py.',
 'assateague-light':'OpenStreetMap lighthouse "Assateague Light" (nom.py), matching the Wikipedia coordinate.',
 'poplar-forest':'The Wikipedia coordinate fell in trees; moved 44 m with pix.py onto the white octagonal house seen on the aerial.',
 'mabry-mill':'OpenStreetMap watermill "Mabry Mill" (nom.py), matching the Wikipedia coordinate.',
 'pocahontas-exhibition-mine':'Wikipedia coordinate, in woods on the aerial; the mine mouth was not picked out. The ArcGIS geocoder put 215 Shop Hollow Road 340 m east, beside the mapped lot given as parking. Pin marks the area.',
 'appomattox-court-house-village':'Wikipedia coordinate for the park, in the village.',
}
