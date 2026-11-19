# November 18, 2026: Windham County, Connecticut (region cte, drawn at random by choose.py): Pomfret, Brooklyn, Canterbury,
# Woodstock, Scotland, Willimantic (Windham), Killingly, Putnam, Plainfield and Eastford.
# Facts come only from sources opened in this session: Wikipedia read as raw text (tools/wiki_raw.py), the managers' own pages
# (CT DEEP / ctparks.com for Mashamoquet Brook and Old Furnace, CT DECD for the Prudence Crandall Museum, roselandcottage.org,
# huntingtonhomestead.org, oldtrinity.net), the Killingly Conservation Commission's Old Furnace page and walk leaflet, the
# Connecticut Office of Tourism listings (ctvisit.com) for the Mill Museum and the Huntington Homestead, the Local Historic
# Districts of Connecticut page for the Stone Road Historic Trail, and colonialmeetinghouses.com for Trinity Church.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]

BATCH={'key':'cte_jqlk','label':'Windham County, Connecticut: Pomfret to Plainfield','added':'2026-11-18 13:54'}

MASH=L('ctparks.com: Mashamoquet Brook State Park','https://ctparks.com/parks/mashamoquet-brook-state-park')
KCC=L('Killingly Conservation Commission: Old Furnace State Park','https://www.killinglyconservation.org/old-furnace-state-park-ross-cliffs')
KCCPDF=L('Killingly Conservation Commission: Old Furnace walk leaflet (PDF)','https://killinglyconservation.org/_files/ugd/f1f6b2_e011d001a1e243b7befc3159fb8071d3.pdf')
CRAN=L('CT DECD: Prudence Crandall Museum, plan your visit','https://portal.ct.gov/decd/content/historic-preservation/04_state_museums/prudence-crandall-museum/plan-your-visit')

PLACES=[
# ---- Pomfret: Mashamoquet Brook State Park ----
N('brayton-grist-mill-pomfret','Brayton Grist Mill','Pomfret','cte','industry','standing',41.86074,-71.98240,'site','public','drive','','c.1890',
  'A four-storey timber grist mill on Mashamoquet Brook, built about 1890 by William Brayton from the materials of older mills on the same spot. It is the last of several mills that once lined the brook. Brayton died in 1928 and the state bought the property in 1930 to enlarge the state park. It is counted among the best-kept 19th-century country grist mills in Connecticut.',
  'A clapboarded post-and-beam mill beside the park entrance road. Inside (from Wikipedia) the 19th-century turbine still sits in a wooden frame in the basement, the gearing is on the second level and milling machines patented in 1888 and 1890 on the third; it also holds the Marcy blacksmith collection. Wikipedia says the museum is open by appointment; the Pomfret Historical Society, which looks after the mill, gives no visiting hours on its pages. Interior hours not checked.',
  'A turbine-driven grist mill with its machinery still in place.',
  'Mashamoquet Brook State Park (CT DEEP), 276 Mashamoquet Road, Pomfret, just south of US 44 on the west side of the park entrance road. The park page gives "Open Daily, 8:00 a.m. to sunset" (read November 2026). The mill is cared for by the Pomfret Historical Society; whether and when the inside is open was not checked.',
  [W('Brayton Grist Mill'),MASH,L('Pomfret Historical Society','https://pomfret-historical-society.org/?p=319')],brick='no'),
N('putnam-wolf-den-pomfret','Israel Putnam Wolf Den','Pomfret','cte','landmark','traces',41.84163,-71.98491,'exact','public','walk','','1742',
  'A cleft in a gneiss ledge where, in 1742, the young Israel Putnam is said to have crawled in by torchlight and shot the wolf that had killed some seventy of his sheep, Connecticut\'s last known wolf, and was hauled out by a rope tied to his ankles. The story was set down in a 1788 biography and has likely grown in the telling, but most of his biographers accept the cave and the wolf. Putnam went on to be a general in the Revolution. The Daughters of the American Revolution bought the den in 1899 and it joined the state park in 1925; it is on the National Register.',
  'The den is a natural fissure that runs about 20 feet into the rock; fill has closed whatever chamber may once have been at the back. It looks much as it did when the tale was written down. The park\'s blue-blazed Mashamoquet Brook Trail passes it, along with the Table Rock and Indian Chair rock formations.',
  'Crawl in after Old Put\'s wolf.',
  'Mashamoquet Brook State Park (CT DEEP), open daily 8 a.m. to sunset by the park page (read November 2026). Park at the lot off Wolf Den Drive near the Wolf Den campground; the den is a short walk on the trail. The park page says the Indian Chair area remains closed.',
  [W('Israel Putnam Wolf Den'),W('Mashamoquet Brook State Park'),MASH],conf=None,th=[41.84353,-71.98633],thn='Lot off Wolf Den Drive, Mashamoquet Brook State Park',brick='no'),
# ---- Brooklyn ----
N('trinity-church-brooklyn-ct','Old Trinity Church','Brooklyn','cte','worship','standing',41.80015,-71.92416,'exact','view','drive','','1771',
  'Finished in April 1771, little changed since, and the oldest Anglican (Episcopal) church building standing in Connecticut. Godfrey Malbone paid for most of it to escape paying for a new Congregational meeting house, and it was built in part with the labour of people he enslaved. It was closed during the Revolution. The congregation now meets in a newer church in Brooklyn centre and keeps this one for special services.',
  'A clapboarded wood-frame church with a hip roof, round-arched upper windows and a pedimented doorway; much of the siding is original, still held by hand-cut nails. Inside (from Wikipedia) the original box pews with wrought-iron hinges, the original pulpit and reading desk. The church opens for occasional historical services from the 1789 Book of Common Prayer, open to all (one was held on Trinity Sunday, May 31, 2026, by oldtrinity.net); otherwise seen from outside.',
  'Box pews that have seen 250 years of Anglican services.',
  'On the east side of Church Street near Brown Road, east of Brooklyn centre. Owned by the Trinity Church parish; seen from the road and the churchyard. Parking at the church not checked.',
  [W('Trinity Church (Brooklyn, Connecticut)'),L('Old Trinity Church: historical services','https://oldtrinity.net/historic-anglican-services/'),L('Colonial Meetinghouses: Trinity Church, Brooklyn','https://www.colonialmeetinghouses.com/mh_trinity_brooklyn.shtml')],brick='no'),
N('unitarian-meetinghouse-brooklyn-ct','Unitarian Meetinghouse','Brooklyn','cte','worship','standing',41.78768,-71.95021,'exact','view','drive','','1771–1774',
  'The meeting house on Brooklyn green, built in 1771-74 after years of opposition from local Anglicans (who built Trinity Church in the meantime). In the early 1800s the congregation split and the Unitarians kept the building. It was restyled in 1845, with a new entrance tower and a full second floor, and those changes were undone in the late 20th century, using unusually full records, to bring it back to its first form.',
  'One of the few pre-Revolutionary church buildings left in the state. Restored to the old plan, with the main door on the long side and the pulpit facing it; the bell tower with its steeple is at one short end. Owned by the Unitarian Universalist Society in Brooklyn. Interior and visiting times not checked.',
  'A meeting house turned back to 1771.',
  'At the junction of Routes 169 and 6 in Brooklyn village centre. Owned by the Unitarian Universalist Society; seen from the green and the road. Parking not checked.',
  [W('Unitarian Meetinghouse')],brick='no'),
# ---- Canterbury ----
N('prudence-crandall-museum','Prudence Crandall Museum','Canterbury','cte','inst','standing',41.69792,-71.97194,'exact','open','drive','','1805',
  'A house of 1805 on Canterbury green where Prudence Crandall ran a girls\' boarding school from 1831. When she admitted one Black student the white parents withdrew their daughters; in 1833 she reopened it for "young Ladies and little Misses of color". The town fought the school in court and then with violence, and she closed it in 1834 for the students\' safety and left Connecticut. She is the state heroine, and the house is a National Historic Landmark and a state museum.',
  'A "Canterbury type" house: a gable-on-hip roof with twin chimneys, a pediment over a projecting centre with a Palladian window, a carved doorway, and a cornice with modillions and a Greek fret, on dressed stone foundations. A 1981 study found about 95% of the building unaltered since Crandall\'s day. The tour covers five rooms of the first floor; the second floor is closed to the public.',
  'The school a town shut down in 1834.',
  'State museum (CT Department of Economic and Community Development) at Routes 14 and 169. By the museum\'s page (read November 2026): timed guided tours only, Sundays at 11:30 and 3:00 from November 8, 2026 to April 18, 2027, about an hour each; Monday to Thursday for booked groups; closed Friday and Saturday. Adults $10, 65 and over $8, youth $5. Parking at the museum, with overflow across Route 169 behind the church.',
  [W('Prudence Crandall Museum'),CRAN],brick='?'),
# ---- Woodstock ----
N('roseland-cottage-woodstock','Roseland Cottage','Woodstock','cte','landmark','standing',41.94931,-71.97628,'exact','open','drive','','1846',
  'A Gothic Revival summer house of 1846 built for the publisher Henry Chandler Bowen, laid out on the ideas of Andrew Jackson Downing. From 1870 Bowen held huge Fourth of July celebrations here, and four presidents came as his guests: Grant, Hayes, Benjamin Harrison and McKinley. It is a National Historic Landmark, owned by Historic New England and run as a museum.',
  'Known locally as the Pink House, it is painted coral pink. Wikipedia counts it among the best-kept Gothic summer houses in the country, with its original Gothic furniture and embossed Lincrusta wall covering. The grounds keep a boxwood parterre garden in its 1850 pattern, an icehouse, a garden house and a carriage barn with what Wikipedia calls the oldest surviving indoor bowling alley in the country. The house is seen on a guided tour only.',
  'Four presidents and a bowling alley in a pink Gothic cottage.',
  'Historic New England, on Route 169 on Woodstock Hill. By roselandcottage.org (read November 2026): every visitor to the house is taken on a guided tour; the gardens and grounds are open dawn to dusk; parking on the grounds, behind the barn. Tour days and fees are on Historic New England\'s page, which refused this session (HTTP 403): not checked.',
  [W('Roseland Cottage'),L('Roseland Cottage: visitor information','https://roselandcottage.org/info/'),L('Historic New England: Roseland Cottage','https://www.historicnewengland.org/property/roseland-cottage')],brick='some'),
# ---- Scotland ----
N('huntington-homestead-scotland','Huntington Homestead','Scotland','cte','landmark','standing',41.69889,-72.08517,'exact','open','drive','','early 1700s',
  'A saltbox farmhouse built in the first quarter of the 18th century, birthplace and boyhood home of Samuel Huntington (1731-1796), a signer of the Declaration of Independence, Governor of Connecticut and the first presiding officer of the Congress of the Confederation. It is a National Historic Landmark and a museum run by the Governor Samuel Huntington Trust.',
  'Two and a half storeys, five bays, with a big central chimney and the long rear roof of a saltbox; a 19th-century kitchen wing on the east. Inside, a Georgian central-chimney plan with a narrow winding stair in front of the chimney; Wikipedia says the woodwork and plaster are almost all original.',
  'Where a president of the Congress grew up.',
  '36 Huntington Road (Route 14), Scotland. The trust\'s page and the state tourism listing (read November 2026) give the museum as open the first and third Saturdays, May to October, 11 a.m. to 3 p.m.; admission free, donations asked. Parking not checked.',
  [W('Samuel Huntington Birthplace'),L('The Huntington Homestead','https://huntingtonhomestead.org/visit-1'),L('CT Office of Tourism: Huntington Homestead','https://ctvisit.com/listings/huntington-homestead')],brick='some',hours='May to October: first and third Saturdays, 11 a.m. to 3 p.m.'),
# ---- Willimantic (Windham) ----
N('mill-museum-willimantic','Windham Textile and History Museum and the thread mills','Willimantic','cte','industry','standing',41.71101,-72.20566,'exact','open','drive','','1824–1985',
  'Willimantic was a thread town. The Jillsons built a mill here in 1824; Hartford investors bought it in 1854 and formed the Willimantic Linen Company, which never made linen. It rebuilt the mills from 1880, added the last in 1910, passed to the American Thread Company in 1898, and closed in 1985 when the work went south. Mill 4 burned in 1995. The museum, known as the Mill Museum, is in the company\'s former store, which the state tourism listing calls its former headquarters.',
  'The museum shows a manager\'s office, a boarding-house room of the 1880s and a room of old sewing machines; tours take in the outside of the mill property, which is mostly private (apartments now use part of it). Nearby the 1857 stone arch bridge over the Willimantic River is planted as the Garden on the Bridge. The mill chimney was taken down between 2012 and 2014.',
  'A thread empire told from its own company store.',
  'Windham Textile and History Museum, 157 Union Street (OpenStreetMap). The state tourism listing (read November 2026) gives adults $10, seniors and students $7, children under 5 free, and a 1 to 1.5 hour tour; the museum\'s own pages are drawn by script and could not be read, so hours not checked. The mill buildings are private: seen from the street.',
  [W('Windham Textile and History Museum'),W('Jillson Mills'),L('CT Office of Tourism: Windham Textile and History Museum','https://ctvisit.com/listings/windham-textile-and-history-museum')],brick='?'),
# ---- Killingly ----
N('old-furnace-killingly','Old Furnace State Park iron furnace','Killingly','cte','industry','traces',41.77678,-71.86431,'area','public','walk','','1700s or 1831',
  'An iron furnace gave this state park its name; bog ore, charcoal from the woods and a flux of limestone or gabbro were smelted here with air blown by water wheels. The sources disagree on its dates: Wikipedia has it working from before the Revolution (making iron for horseshoes for the Continental Army) to the mid-1800s, while the Killingly Conservation Commission dates it to the 1830s and 1840s, with the furnace built in 1831 and furnace and forge both at work in 1833. The town made it a park in 1909 and the state took it over in 1918.',
  'The Conservation Commission says remnants of the stone furnace can still be seen beside Fall Brook (Wikipedia calls the stream Furnace Brook), but the landscaping that made it a park destroyed many features; Wikipedia speaks of foundations and stone walls in second-growth woods. The blue-blazed Old Furnace Trail crosses the brook and passes man-made ponds on the way up to the views from Ross Cliffs. The exact place of the furnace remains was not found.',
  'What is left of a furnace that may have shod the Continental Army.',
  'Old Furnace State Park (CT DEEP), 539 South Frontage Road off Route 6, about half a mile east of I-395 exit 91, by the Killingly Conservation Commission. Park at the lot by the road; the trail to the top of the cliffs is about 2 miles. Open year round for hiking, hunting and fishing (Wikipedia); daily hours not checked: the DEEP page read gives none. Hunting is allowed: wear orange in season.',
  [W('Old Furnace State Park'),KCC,KCCPDF],conf='mixed',brick='no'),
N('daniels-village-killingly','Daniel\'s Village mill site','Killingly','cte','industry','ruins',41.88284,-71.85044,'site','view','drive','','1720s–1861',
  'A mill village on the Five Mile River at Putnam Road. A grist mill stood here from the 1720s; in 1814 local men and Rhode Island investors built one of the first cotton mills in Connecticut, Howe\'s Factory, bought by the Daniels family in 1845. By then the village had a store, a smithy, three mill buildings and at least nine workers\' houses. The mills burned in 1861 and were never rebuilt, and by the early 1900s the rest was in ruins. It is on the National Register as an archaeological site and a town historic district, the Stone Road Historic Trail.',
  'Wikipedia names the early 19th-century stone dam and the stone house at the corner of Putnam and Stone Roads, built after 1814, as what can be seen. Stone Road itself is kept as part of the district.',
  'A cotton village that burned in 1861 and was never rebuilt.',
  'Private: the whole site was bought in 2015 by a single owner (Wikipedia). See it from Putnam Road and Stone Road only; do not go onto the land without asking. Road-shoulder parking not checked.',
  [W('Daniel\'s Village Archeological Site'),L('Local Historic Districts of Connecticut: Stone Road Historic Trail','https://lhdct.org/district/stone-road-historic-trail')],brick='no'),
N('peep-toad-mill-killingly','Elliottville Lower Mill (Peep Toad Mill)','Killingly','cte','industry','standing',41.83917,-71.84250,'site','view','drive','','c.1850',
  'A small cotton mill of about 1850 on Whetstone Brook in East Killingly, built by the Elliottville Manufacturing Company (Thomas Pray and Henry Westcott) to spin and prepare warps for its larger upper mill upstream. Some local histories say it began as a saw and grist mill, but its building methods match the upper mill. It is a rare survivor of the many wood-frame textile mills that burned or were swallowed by later growth, and is on the National Register.',
  'A mill of stone and wood framing, with its dam, pond and head race across the road, and a rubble-stone arch bridge carrying Peep Toad Road over the brook. In the 20th century the mill became a private home and art studio.',
  'A wooden mill that never burned.',
  'Private home. Seen from Peep Toad Road, which crosses the brook on the stone bridge; do not go onto the property. Parking not checked.',
  [W('Elliottville Lower Mill')],brick='no'),
# ---- Putnam ----
N('cargill-falls-mill-putnam','Cargill Falls Mill','Putnam','cte','industry','standing',41.91500,-71.91167,'site','view','drive','','1806–1950',
  'One of Connecticut\'s oldest mill complexes, at the falls of the Quinebaug opposite downtown Putnam. Rhode Island investors including Oziel Wilkinson, Samuel Slater\'s father-in-law, founded the Pomfret Manufacturing Company here in 1806 and built a four-storey wooden mill whose foundation still carries a later building. Grist, saw and fulling mills had used the drop in the 18th century. It is on the National Register.',
  'Twenty joined buildings, the oldest of 1824 and the newest of 1950, up to five storeys; most are brick with timber framing inside, one is coursed rubble stone and one is wood. Seen from Pomfret Street (US 44) and across the river. Its present use was not checked.',
  'Slater\'s family mill at the falls of the Quinebaug.',
  'Private, 52-58 Pomfret Street. Seen from the street and the river bank downtown. Parking not checked.',
  [W('Cargill Falls Mill')],brick='yes'),
# ---- Plainfield ----
N('packerville-bridge-plainfield','Packerville Bridge and dam','Plainfield','cte','water','standing',41.66716,-71.94834,'exact','view','drive','','1886',
  'A stone arch bridge over Mill Brook, built in 1886 after a flood carried off most of the town\'s bridges. Stone was chosen because a bridge just below a mill dam was at most risk from a dam failure. It is one of fewer than twenty 19th-century stone arch bridges left in the state, and on the National Register. Just upstream is the Packerville Dam, all that survives of a 19th-century mill.',
  'A cut-stone barrel arch with rubble spandrels; the stone came from near Westerly, Rhode Island. The stone guard rails were replaced with metal in the 20th century. Look upstream for the old mill dam.',
  'A flood-proof arch below a mill dam.',
  'Carries Packerville Road just north of Lowes Way; a public road. Watch for traffic; parking not checked. The dam and banks: ownership not checked, so view from the road.',
  [W('Packerville Bridge')],brick='no'),
N('glen-falls-bridge-moosup','Glen Falls Bridge','Moosup (Plainfield)','cte','landmark','standing',41.71702,-71.86139,'exact','view','drive','','1886',
  'A wrought-iron lenticular pony truss made by the Berlin Iron Bridge Company in 1886, one of a dwindling number of the hundreds of these lens-shaped bridges once in Connecticut. It carried the main east-west road over the Moosup River until Route 14 was moved in 1940. Some truss members and the portal posts were replaced in the 20th century; it stands on concrete abutments. On the National Register since 1999.',
  'The curved top and bottom chords of a lenticular truss, low over the river, beside a former 19th-century mill complex on the north bank east of the bridge. Wikipedia says it has been closed to cars and walkers for many years.',
  'A lens-shaped iron bridge left in place.',
  'Closed to all traffic. Seen from the two dead-end spurs of Brunswick Avenue, south of North Main Street (Route 14) on the east side of Moosup. Do not cross it. Parking not checked.',
  [W('Glen Falls Bridge')],brick='no'),
# ---- Eastford ----
N('natchaug-lumber-shed-eastford','Natchaug Forest CCC lumber shed','Eastford','cte','civic','standing',41.83933,-72.08392,'site','view','drive','','1934',
  'The Civilian Conservation Corps had a camp in Natchaug State Forest from 1933 to 1941 and built its roads and trails and a workshop, garage, oil house, barn, sawdust shed and three lumber sheds. When this shed was listed on the National Register in 1986, three of the buildings were left and two had been much altered; this is the best kept.',
  'A post-and-beam shed with vertical board siding and five equipment bays with double wooden doors on its north front, at the south end of the forest maintenance yard, which is the old CCC camp site. The forest\'s CCC Loop trail recalls the camp.',
  'What is left of a CCC camp.',
  'Natchaug State Forest (CT DEEP), maintenance yard on the east side of Kingsbury Road near the middle of the forest. A working yard: seen from the road. A mapped lot for the CCC Trail is about 700 m west. Forest hours not checked.',
  [W('Natchaug Forest Lumber Shed'),W('Natchaug State Forest')],th=[41.84066,-72.09257],thn='CCC Trail lot, Natchaug State Forest',brick='no'),
]

PIN_NOTES={
 'brayton-grist-mill-pomfret':'Wikipedia list coordinate, west of the park entrance road south of US 44; the mill could not be picked out under the trees on the aerial, so prec is site.',
 'putnam-wolf-den-pomfret':'OpenStreetMap point for the Wolf Den rock (nom.py).',
 'trinity-church-brooklyn-ct':'Wikipedia infobox coordinate.',
 'unitarian-meetinghouse-brooklyn-ct':'Wikipedia list coordinate (41.787679, -71.950214) at Routes 169 and 6.',
 'prudence-crandall-museum':'Wikipedia infobox coordinate at Routes 14 and 169.',
 'roseland-cottage-woodstock':'Moved 53 m with pix.py from the Wikipedia coordinate (on the lawn) onto the house beside the boxwood parterre seen on the aerial.',
 'huntington-homestead-scotland':'ArcGIS geocoder PointAddress for 36 Huntington Road, 40 m north-east of the Wikipedia coordinate, which fell at the road edge.',
 'mill-museum-willimantic':'OpenStreetMap point for the museum, 157 Union Street (nom.py).',
 'old-furnace-killingly':'Pin is the park lot on South Frontage Road (parking.py); the furnace remains are said to be beside Fall Brook near the park but were not placed.',
 'daniels-village-killingly':'Moved 41 m with pix.py from the Wikipedia coordinate (on a private house) to the dam at the pond outlet, seen on the LiDAR sheet beside Putnam Road.',
 'peep-toad-mill-killingly':'Wikipedia infobox coordinate on Peep Toad Road at Whetstone Brook.',
 'cargill-falls-mill-putnam':'Wikipedia infobox coordinate on Pomfret Street at the river.',
 'packerville-bridge-plainfield':'OpenStreetMap bridge (nom.py) on Packerville Road.',
 'glen-falls-bridge-moosup':'Wikipedia infobox coordinate over the Moosup River.',
 'natchaug-lumber-shed-eastford':'Moved 46 m with pix.py from the Wikipedia coordinate (in trees) onto the southern building of the maintenance yard on the aerial; which shed is the listed one was not confirmed.',
}
