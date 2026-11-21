# November 21, 2026: what was still missing in Cohoes, Watervliet and Waterford, and two places just south of Watervliet
# in Colonie (Menands), filed under albco like the other Colonie places. Drawn at random by tools/choose.py --state ny
# (region conf, which six earlier batches had already worked closely). Sources were opened in this session: HMdb
# markers and nearby lists, Wikipedia as raw text (tools/wiki_raw.py), the Town of Colonie's parks page, the Erie
# Canalway's heritage-award page and the Edison Tech Center (School Street hydro), the Spindle City Historic
# Society's three 2023 tour brochures, troyirish.org (Watervliet churches) and the City of Watervliet's historian
# page (the last two through the web fetch tool).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'conf_aunk','label':'Cohoes, Watervliet and Waterford: what was left','added':'2026-11-21 20:45'}
SCHS=L('Spindle City Historic Society: Historic Downtown Cohoes self-guided tour (2023)','https://www.spindlecity.net/Brochures/downtown%20sites%20brochure%202023.pdf')
SCHE=L('Spindle City Historic Society: The Erie Canal in Cohoes self-guided tour (2023)','https://www.spindlecity.net/Brochures/Erie%20Canal%20brochure%202023.pdf')
def H(n,t): return L('HMdb: '+t,'https://www.hmdb.org/m.asp?m=%d'%n)
PLACES=[
N('schuyler-house-burying-ground-colonie','Schuyler Flatts: the Schuyler house site and the Old Schuyler Burying Ground','Colonie','albco','burial','traces',42.70654,-73.70902,'site','public','walk','cemeteries','1640s–1962',
  'The Flatts, the river plain north of Albany, were farmed by the 1640s and bought by Philip Pieterse Schuyler in 1672; the farm was the early home of Pieter Schuyler, the first mayor of Albany, and the family held the farm for more than two and a half centuries. The house, whose foundations a 1957 tablet says were believed to date from 1649, burned in 1962. North of the farm lane the family kept a burying ground: records of 1874 count more than 50 burials, most from the epidemic years of the 1830s and 1840s, and in 1920 the family moved a number of the stones to Albany Rural Cemetery. The whole site is a National Historic Landmark and, since 2002, a Town of Colonie park.',
  'The town\'s marker panels along the footpath tell the story. The marker for the burying ground says Colonel Philip Schuyler\'s gravestone of 1758, a stone tablet set on pillars, is the earliest and grandest of the stones that remain; how many others are left was not checked. OpenStreetMap maps the foundations of the Colonel Philip Schuyler house about 60 m south-east of the burying-ground marker; whether anything of them shows above ground was not checked. The 1957 house tablet is now by the parking area off Broadway. Red brick: not checked.',
  'A Dutch farm of the 1640s, a mayor\'s birthplace and a family graveyard, in a town park beside Route 32.',
  'Schuyler Flatts Cultural Park, a 43-acre Town of Colonie park at 595 Broadway between Menands and Watervliet. The town\'s parks page says it opens daily and closes at dusk; HMdb puts the park\'s parking area off Broadway (NY 32) by the 1957 tablet (the lot was not picked out on the aerial), then a footpath of about 0.1 mile to the burying-ground marker. The neighbouring African burial site of the Schuyler farm is a separate Atlas entry.',
  [W('Schuyler Flatts'),H(268621,'The Old Schuyler Burying Ground'),H(268883,'Schuyler Flatts (1957 tablet, rededicated 2002)'),L('Town of Colonie: parks and facilities (Schuyler Flatts Cultural Park)','https://www.colonie.org/parks/parks/')],
  conf='mixed',brick='?',hours='Daily to dusk'),
N('north-reformed-church-watervliet','North Reformed Dutch Church (Watervliet Historical Society) and its Meneely bells','Watervliet','conf','worship','standing',42.72606,-73.70126,'exact','open','drive','','1839–2001',
  'The congregation of the first church in what is now Watervliet built a second church north of the Arsenal in 1839, at First Avenue and 15th Street. A storm in 1854 brought the steeple down with its Meneely bell, and a fire in 1900 started in the steeple by the wiring of the bell, then used as the city fire alarm, destroyed the second bell; troyirish.org adds a fire in 1924. The church joined First Baptist in 1968 as Christ Church, which closed in 2001. The Watervliet Historical Society and its museum now use the church; troyirish.org says it is the church hall of 1865.',
  'Two Meneely bells stand at the front steps: the North Reformed Church\'s third bell, whose inscription records the 1900 fire, and the 1906 bell of the demolished St. Patrick\'s Church, brought down in 2013 and put in a ground-level pavilion (the society\'s marker gives about 11,000 pounds mounted, troyirish.org 6,800 pounds; both are given here). troyirish.org says the sanctuary windows are the only memorials of the church that remain. Interior not checked. Red brick: not checked.',
  'Bells from the city that cast 65,000 of them, on the doorstep of a closed church.',
  'The Watervliet Historical Society, 1501 First Avenue at 15th Street, behind the Watervliet Public Library; street parking. The City of Watervliet\'s historian page (last changed 2021) gives the museum\'s hours and the telephone 518-272-0715; the bells can be seen from the sidewalk at any time.',
  [L('troyirish.org: North Reformed Dutch Church, 1501 First Ave, Watervliet','https://troyirish.org/?p=486'),L('troyirish.org: St. Patrick\'s, Watervliet','https://troyirish.org/?p=1456'),H(185074,'North Dutch Reformed Church Bell'),H(70628,'Saint Patrick\'s Church Bell'),L('City of Watervliet: City Historian (historical society and museum hours)','https://watervlietny.gov/historian/')],
  conf='mixed',brick='?',hours='Wednesday to Friday 11 a.m. to 4 p.m. (city page of 2021)'),
N('school-street-hydro-cohoes','School Street hydroelectric station and the Lower Gatehouse','Cohoes','conf','industry','standing',42.78486,-73.70794,'exact','view','walk','','1915',
  'Built in 1915 beside the Harmony Mills, the School Street plant took over the dam, upper gatehouse and power canal of the Cohoes Company\'s 1800s water-power system; the lower canals were given up and filled. A 4,500-foot canal brings water from the pond above the Cohoes Company dam to the Lower Gatehouse, from which five steel penstocks run down the face of the gorge to the powerhouse. It still runs, with five units of 38,800 kilowatts in all; Brookfield Renewable Power, its owner in 2008, renewed the federal licence in 2007 and repaired the masonry.',
  'From Overlook Park and Falls View Park: the powerhouse at the foot of the gorge below the falls, the penstocks on the gorge wall, and the Lower Gatehouse at the head of them. The heritage corridor\'s marker by the overlook explains the system. A working plant: interior not open. Red brick: yes; the 2020 Commons photograph from the north-west shows red brick powerhouse buildings beside the penstocks.',
  'A 1915 power plant still running on the Cohoes Company\'s old power canal.',
  'Private, working power plant behind fences: view it from the city\'s Overlook Park on School Street and from Falls View Park across the footbridge (see the Cohoes Falls entries for their hours). Where to park was not settled: the lot OpenStreetMap maps on Cataract Street did not show plainly as a lot on the aerial, so use street parking.',
  [L('Erie Canalway National Heritage Corridor: School Street Hydro, 2008 Heritage Award','https://eriecanalway.org/find-resources/case-studies/school-street-hydro'),H(280758,'Water for Power'),L('Edison Tech Center: Cohoes Falls Power Plant','https://edisontechcenter.org/cohoes/')],
  brick='yes'),
N('cohoes-lock-17','Enlarged Erie Lock 17 and the locktender\'s house','Cohoes','conf','canal','ruins',42.78268,-73.71003,'site','view','walk','canal','1836–1842',
  'One of the ten double-chamber limestone locks, numbered 9 to 18, built in Cohoes for the enlarged Erie Canal of 1836 to 1842 to carry boats about 112 feet up around the Cohoes Falls. Each had a 10-foot lift, and the run of locks was so slow that passing them could take nearly a day. Lock 17 is one of the units of the Enlarged Erie Canal Historic District, listed in 2004.',
  'The historic society\'s canal tour lists Lock 17 among the easiest to reach: by John and Erie Streets, with a well-preserved stretch of the canal prism to the north of the lock and, west of it, a house once lived in by locktenders, now a private home. Red brick: none in the sources; it is a stone lock.',
  '',
  'By John and Erie Streets, in a wooded strip behind the houses; the locktender\'s house is a private home. Who owns the ground round the lock was not checked (Wikipedia says the locks on city-owned land are in the 2004 district), so look from the street. Street parking.',
  [SCHE,W('Enlarged Erie Canal Historic District')],
  conf='mixed',brick='no'),
N('egberts-bailey-finishing-building-cohoes','Egberts and Bailey finishing building (the Salvation Army building), 300 Ontario Street','Cohoes','conf','industry','standing',42.77417,-73.70163,'exact','view','walk','','1844',
  'Built in 1844 as a supplementary building for the Egberts and Bailey knitting mill, the first mill built for power knitting: here the knit goods were sewn together and made ready to ship. It became a store in 1859. It stands at Remsen and Ontario Streets, next to the 1864 Troy Manufacturing mill, which has the ghost of the vanished Egberts and Bailey mill on its side.',
  'A building of two and a half storeys whose gable roof was later taken off and replaced with a third storey and a flat roof, so the 1844 building is the lower part. The 2023 tour calls it the Salvation Army building; current use and interior not checked. Red brick: not checked.',
  '',
  'Private building on public streets; look from the sidewalk. Street parking in downtown Cohoes.',
  [SCHS],
  brick='?'),
N('mohawk-street-houses-cohoes','Mohawk Street: the Van Auken and Clarke houses, the 1849 Claxton building and 2–4 White Street','Cohoes','conf','landmark','standing',42.77381,-73.69981,'site','view','walk','','1840s–1873',
  'The stretch of Mohawk Street up to Oneida Street was where many of the men who built Cohoes lived in the 1800s. The historic society\'s downtown tour picks out four survivors: the brick Second Empire house built in 1873 for David Van Auken, engineer of the Cohoes Company and architect of Harmony Mill No. 3; the house of Joshua R. Clarke, who came from Pawtucket in 1831 and built the first Harmony Company building and the Egberts and Bailey mill; the last of three identical buildings put up in 1849 by F. S. Claxton, agent of the Cohoes Company; and an 1840s Federal frame house on White Street, among the oldest houses in the city.',
  'At 115 Mohawk Street the Van Auken house, brick Second Empire with Eastlake detail; across the street at 112 the Clarke house, later home of H. S. Bogue, the third mayor; at 113 the Claxton building, long the office of Dr. Edward Vandercar, city historian and a founder of the Hudson-Mohawk Industrial Gateway; and round the corner at 2–4 White Street the 1840s frame house. All private; interiors not checked. Red brick: the tour calls the Van Auken house brick but does not give the colour; the others not checked.',
  '',
  'Private houses on public streets; look from the sidewalk. Street parking. Cohoes City Hall, the former St. John\'s Church and the William Moore House are on the same street.',
  [SCHS],
  brick='?'),
N('button-fire-engine-works-waterford','Button Fire Engine Works site (Button Park)','Waterford','conf','industry','marker',42.78768,-73.67975,'exact','public','walk','','1850–1891',
  'Lysander Button began as a machinist in John Rogers\' fire-engine shop on the King\'s Canal in Waterford, became its sole owner in the 1840s and later moved to a steam-powered building on Third Street. His hand pumpers and, later, Button steamers were sold across the world, about 750 of them; a Button steamer won the Centennial Award at Philadelphia in 1876. He sold the works in 1882 to Holroyd & Company of Waterford, and in 1891 the Button Fire Engine Works was folded into the American Fire Engine Company.',
  'A marker in Button Park on the waterfront, about 100 feet north-north-west of the Waterford Harbor Visitor Center, gives 1850 for the manufactory on this site. Nothing of the works is said to remain. Wikipedia says the Waterford Historical Museum obtained an original Button & Blake hand pumper, the "Converse", in 2005; whether it is on show was not checked. Red brick: none; a marker in a park.',
  'Fire engines from a canal village sold around the world.',
  'Button Park is public waterfront by the Waterford Harbor Visitor Center at 1 Tugboat Alley; street parking; the lot OpenStreetMap maps on Tugboat Alley was not plain on the aerial.',
  [H(115392,'Button Park'),W('Lysander Button')],
  brick='no'),
N('troy-steel-iron-furnace-site-menands','Troy Steel and Iron Company blast furnace site (Hillhouse Island)','Colonie','albco','industry','marker',42.70252,-73.70534,'area','public','walk','','',
  'The Troy Steel and Iron Company\'s blast furnace stood here on an island in the Hudson called Beeaker or Hillhouse Island. The marker sets it among the iron works of the Mohawk-Hudson area, with Erastus Corning\'s Albany Iron Works, the Rensselaer Iron Works and the Burden Iron Company across the river. The tidal channels that made the islands along the west shore were mostly filled in the 1960s when Interstate 787 was built, and the island is gone.',
  'Only the marker, on the Empire State Trail beside the river, about half a mile south of the trailhead at Broadway and Fourth Street in Watervliet. Across the river is the mouth of the Wynants Kill and the Burden works. Red brick: none; a marker.',
  '',
  'On the Empire State Trail (Mohawk-Hudson bike-hike trail), the state\'s public trail for walkers and cyclists; not reachable by car. Park at the trail lot in Watervliet and walk south about half a mile.',
  [H(226374,'Troy Steel & Iron Co.')],
  th=[42.70953,-73.70491],thn='Mohawk-Hudson Bike-Hike Trail lot, Watervliet',brick='no'),
]
PIN_NOTES={
 'schuyler-house-burying-ground-colonie':'HMdb position of the Old Schuyler Burying Ground marker (268621), which stands on the lane with the burying ground to its north; OpenStreetMap maps the house foundations at 42.70619, -73.70856.',
 'north-reformed-church-watervliet':'ArcGIS PointAddress for 1501 1st Avenue, Watervliet; the bell markers (HMdb 185074, 70628) are at 42.72617, -73.70105.',
 'school-street-hydro-cohoes':'OpenStreetMap building "School Street Hydro-Station" (alt name Cohoes Falls Power Plant); the Lower Gatehouse is mapped at 42.78463, -73.70834.',
 'cohoes-lock-17':'OpenStreetMap ruin "Enlarged Erie Canal Lock 17" from the Atlas leads layer; the LiDAR sheet shows the double lock chamber under the pin, in trees behind the houses.',
 'egberts-bailey-finishing-building-cohoes':'ArcGIS PointAddress for 300 Ontario Street, Cohoes.',
 'mohawk-street-houses-cohoes':'ArcGIS PointAddress for 115 Mohawk Street (the Van Auken house); 112 and 113 are beside it and 2 White Street is about 150 m south (42.77253, -73.70020).',
 'button-fire-engine-works-waterford':'HMdb position of the Button Park marker (115392).',
 'troy-steel-iron-furnace-site-menands':'HMdb position of the Troy Steel & Iron Co. marker (226374) on the Empire State Trail; the island itself was filled in, so this is the marker, not a ruin.',
}
