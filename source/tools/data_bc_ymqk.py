# November 24, 2026: a third scatter of places across British Columbia, claimed with tools/choose.py --thinnest (bc had
# 52 places). Eleven places: Kinsol Trestle and Craigflower Schoolhouse (Vancouver Island), Victoria's Emily Carr House,
# Helmcken House and the E&N Roundhouse, Hatley Castle in Colwood, Hastings Mill Store in Vancouver, Irving House in New
# Westminster, the Walhachin hall on the Thompson, the sternwheeler Sicamous at Penticton, and the ghost town of Anyox.
# Sources read in this session: Wikipedia (tools/wiki_raw.py), the Cowichan Valley Regional District's Kinsol page and the
# Old Hastings Mill Store Museum's home page. The Register of Historic Places, Parks Canada and most operators' pages would
# not open, so hours come only from what a web search quoted from the operator's page, and each entry says so. Nothing was
# checked on the ground.
from data_b import N
from data_ma import W
BATCH={'key':'bc_ymqk','label':'British Columbia: a third scatter','added':'2026-11-24 17:35'}

PLACES=[
N('kinsol-trestle','Kinsol Trestle','Shawnigan Lake','bc','rail','standing',48.66843,-123.69382,'exact','public','walk','','1920–1979',
  'A curved wooden railway trestle over the Koksilah River, 44 m high and 188 m long, started by the Canadian Northern Pacific in 1911 and finished in 1920 under Canadian National. It was built for the forest industry, not for the small copper mine its station was named after. The last train crossed in 1979 and fire damaged it in 1988. It was restored and reopened to walkers on July 28, 2011.',
  'The whole timber structure from the trail: Douglas fir members, the seven-degree curve and the river far below. You can walk, cycle or ride across it on the Cowichan Valley Trail, which follows the old rail grade.',
  'The tallest wooden trestle in the Commonwealth, brought back from a burned wreck.',
  'Managed by the Cowichan Valley Regional District as part of the Cowichan Valley Trail (the federal land map does not show it as public land; the district page is the basis for open access). Its page says the trail is open to walkers, cyclists and riders, with toilets open year round. By car, go through Shawnigan Lake to Glen Eagles Road; a public lot is on the right about 550 m along, and the trestle is about 1.2 km on foot from it. Opening hours and any fee not checked. No parking point is given on the map: use the lot on that page.',
  [W('Kinsol Trestle'),['Cowichan Valley Regional District: Kinsol Trestle','https://www.cvrd.ca/1147/Kinsol-Trestle']],
  brick='no', hours='?'),

N('walhachin-hall','Walhachin Soldiers Memorial Hall','Walhachin','bc','town','standing',50.75303,-120.98601,'site','view','drive','','1908–1920',
  'Walhachin was a failed English orchard colony on the Thompson River. A company began selling irrigated orchard lots in 1908, English settlers came, and a large town hall was built in 1912. Most of the young men left in 1914 for the war. The wooden flumes that carried the water were unreliable, the orchards decayed, and fruit shipments stopped by 1919. The hotel was pulled down in 1920. A small community stayed on, and Wikipedia describes the hall as still in use in the 1960s and 1970s.',
  'A hall mapped in OpenStreetMap as the community centre, on Central Avenue. Whether it is the 1912 building, and what survives of the flumes and orchard terraces, was not checked. The article names a Weber piano once played by Paderewski that stood in the hall until 1961.',
  'An English "Little England" orchard colony that died of its own irrigation flume.',
  'On the south bank of the Thompson, off Highway 1 about 28 km east of Cache Creek. Who owns the hall and whether it can be entered was not checked: look from the road. Treat the pin as the community hall, not as the old townsite or the flumes.',
  [W('Walhachin')], conf='mixed', brick='?', hours=''),

N('emily-carr-house','Emily Carr House','Victoria','bc','landmark','standing',48.4138,-123.37,'exact','open','walk','','1863',
  'An Italianate villa built in 1863 for the family of Richard Carr, designed by Wright and Sanders, who also built the Fisgard Lighthouse. It was the childhood home of the painter and writer Emily Carr, born 1871. After a private owner used it as a rental, a member of parliament saved it from demolition in 1964; the province bought it in 1976 and returned it to its original look. It is a National Historic Site.',
  'A well-preserved Victorian house with its original exterior colours restored from period photographs. Most furnishings are replicas or period pieces; a few original items were recovered. Inside: not checked beyond that.',
  'Where Emily Carr grew up, on the same street that she wrote about.',
  'Owned by the Province of British Columbia and run by the Carr House Community Society at 207 Government Street, near Beacon Hill Park. Its own page would not load. A web search quoted the society\'s listing as Thursday to Saturday 10 a.m. to 4 p.m. from September 1 to December 20 with tours on Fridays and Saturdays, by donation, but other listings differ: ask before going. Street parking, not checked.',
  [W('Emily Carr House'),['Carr House Community Society','https://www.carrhouse.org/']],
  brick='?', hours='?'),

N('helmcken-house','Helmcken House','Victoria','bc','landmark','standing',48.42,-123.3665,'site','open','walk','','1852',
  'Built in 1852 by Dr. John Sebastian Helmcken, a Hudson\'s Bay Company surgeon and Victoria\'s first doctor, after he married Cecilia Douglas, the governor\'s daughter. Wikipedia calls it one of the oldest houses in British Columbia still on its original site. It is a museum in Thunderbird Park.',
  'A small early colonial house kept as a museum; his medical kit is among the objects on show. Inside: not checked.',
  'One of the oldest houses in the province, still where it was built.',
  'Run by the Royal BC Museum beside Thunderbird Park in downtown Victoria. The museum page opened but no opening times could be read from it, so hours are not checked; the house has been closed to the public at times. Street and parkade parking, not checked. The pin is from Wikipedia and was checked on the aerial only.',
  [W('Helmcken House'),['Royal BC Museum: Helmcken House','https://www.royalbcmuseum.bc.ca/visit/helmcken-house']],
  conf='mixed', brick='?', hours='?'),

N('esquimalt-nanaimo-roundhouse','Esquimalt and Nanaimo Railway Roundhouse','Victoria','bc','rail','standing',48.42993,-123.38123,'site','view','walk','','1913',
  'A steam-era railway roundhouse in Victoria West, finished in 1913 for the Esquimalt and Nanaimo Railway and made a National Historic Site in 1992. Wikipedia says it has been virtually unchanged since it was built and that it still stands among railway shops and outbuildings of the steam age.',
  'The roundhouse and the old shops round it, seen from the public paths on the Victoria West waterfront. Who owns it now, what has been done to it since 1992, and whether it can be entered were not checked.',
  'A 1913 steam roundhouse in the middle of Victoria.',
  'Ownership and public access not checked; treat it as look-from-the-street. The pin is from Wikipedia and sits close to the mapped Westsong Walkway; the aerial check says whether it is on the building.',
  [W('Esquimalt and Nanaimo Railway Roundhouse')],
  conf='mixed', brick='?', hours=''),

N('hatley-castle','Hatley Castle (Hatley Park)','Colwood','bc','inst','standing',48.4343,-123.4724,'exact','view','drive','','1908–1913',
  'A 40-room Scottish baronial mansion built for James Dunsmuir, the province\'s Lieutenant Governor, to a design by Samuel Maclure, with formal gardens laid out by Boston designers. The family held it until 1937 and Canada bought it in 1939; it was a military college from the 1940s to 1995 and has housed Royal Roads University since then. The estate is a National Historic Site (1995) and the castle a Classified Federal Heritage Building.',
  'The castle from its approach drive and the formal gardens (Japanese, Rose and Italian gardens are the showcase areas), on a 565-acre campus with farmland and old forest. The university charged for the main gardens from 2006; the present fee and hours were not checked. Interior not checked.',
  'A Dunsmuir castle that became a military college and a university.',
  'Owned and managed by Royal Roads University on University Drive, Colwood. The estate\'s own page would not open. Visitor parking lots are mapped on University Drive; pay and permit rules not checked. Treat the castle as view-only unless the university says otherwise.',
  [W('Hatley Park National Historic Site')],
  brick='?', hours=''),

N('hastings-mill-store','Old Hastings Mill Store Museum','Vancouver','bc','landmark','standing',49.27281,-123.18581,'exact','open','walk','','1860s',
  'The company store of the Hastings Mill sawmill on Burrard Inlet, the first commercial operation round which Vancouver grew (Wikipedia dates the mill from 1865, with lumber cutting from 1867). The store was moved to Alma Street in 1930 and opened as a museum in 1932. The museum calls it Vancouver\'s oldest surviving building.',
  'A wooden store building holding the city\'s first council table, a lifeguard\'s oil lamp, a full-size Hansom cab, items from the steamer Beaver and Indigenous baskets and carvings (museum home page). The main floor accessibility was not checked.',
  'The oldest building left in Vancouver, carried here on a barge in 1930.',
  'Run by the museum society in Hastings Mill Park, 1575 Alma Street, by the Seaside Greenway. A web search quoted its contact page as open Saturdays and Sundays 1 to 4 p.m., by donation, but also said the schedule is seasonal and has changed: check before going. Street parking, not checked.',
  [W('Hastings Mill'),['Old Hastings Mill Store Museum','https://hastingsmillmuseum.ca/']],
  brick='?', hours='?'),

N('irving-house-new-westminster','Irving House','New Westminster','bc','landmark','standing',49.20781,-122.90627,'exact','open','walk','','1865',
  'Built in 1865 by the steamship captain William Irving for his wife and five children, soon after the Royal Engineers left New Westminster. Wikipedia calls it the oldest house in the Lower Mainland still completely intact and still on its original site. It housed three generations of the family until 1950, then the city made it a museum. Restoration since 2011 included the original gold wallpapers (2018).',
  'A one-and-a-half-storey Victorian house at Royal Avenue and Merivale Street, kept as a house museum. Its interior is part of the museum; details not checked.',
  'The oldest house in the Lower Mainland, on its original corner.',
  'Run by the City of New Westminster. A web search quoted the city\'s page as seasonal: Wednesday to Sunday noon to 5 p.m. in summer, Saturday and Sunday noon to 4 p.m. September to November, weekends 3:30 to 7:30 p.m. in December, by donation. The page is undated, so confirm. Street parking and parkades downtown, not checked.',
  [W('Irving House')],
  brick='?', hours='?'),

N('craigflower-schoolhouse','Craigflower Schoolhouse','Saanich','bc','civic','standing',48.45265,-123.42162,'exact','open','walk','','1850s',
  'Built by the Hudson\'s Bay Company for the children of its Craigflower Farm workers, as the third school in the colony of Vancouver Island, and first called Maple Point School. It is a two-storey Georgian Revival building with one schoolroom and rooms for the teacher and boarders, and a school bell salvaged from the wreck of the Major Tompkins. A National Historic Site, 200 m across the Gorge Waterway from Craigflower Manor.',
  'The schoolhouse with its bell, and a shell midden on the site left by earlier peoples. Inside: not checked.',
  'The third school in the colony, still beside the water.',
  'Wikipedia says it opens in summer for special presentations. A web search listing gave May to September, Wednesday to Sunday 1 to 5 p.m., but another page of the same site called it temporarily closed, and no operator page was read: check before going. Street parking on Admirals Road, not checked.',
  [W('Craigflower Manor and Schoolhouse')],
  conf='mixed', brick='?', hours='?'),

N('ss-sicamous-penticton','S.S. Sicamous','Penticton','bc','landmark','standing',49.50184,-119.61099,'exact','open','walk','','1914–1936',
  'A four-decked sternwheeler built for the Canadian Pacific Railway and launched May 19, 1914, to carry passengers and freight on Okanagan Lake. It was retired in 1936 and sat at Okanagan Landing until the Penticton Gyro Club bought it in 1951 and brought it to Penticton, where it is beached as a museum and restoration site.',
  'The big wooden ship itself on the lakeshore, with a heritage park holding other lake boats. Inside: not checked.',
  'A 1914 lake steamer beached in the middle of Penticton.',
  'Run by the S.S. Sicamous society at 1099 Lakeshore Drive West. A web search quoted its page as $10 adults and $8 seniors, and a notice that it was closed until May 18, 2026; current hours were not read. Check sssicamous.ca. A lot is mapped on Lakeshore Drive West next to the ship.',
  [W('Sicamous (sternwheeler)'),['S.S. Sicamous hours and admission','https://sssicamous.ca/hours-of-operation']],
  brick='no', hours='?'),

N('anyox-ghost-town','Anyox','Anyox','bc','town','ruins',55.417,-129.833,'area','boat','boat','burned','1912–1935',
  'A company copper-mining town on Granby Bay, Observatory Inlet, built from 1912 by Granby Consolidated, which had moved its mining here from Phoenix. At its peak it held about 3,000 people with a hospital, curling rink and golf course. Fire hit it in 1923, the mine closed in 1935 and the town was abandoned. Salvage in the 1940s took most steel and machinery, and forest fires in 1942 and 1943 burned the wooden buildings.',
  'The ruins of a large smelter and company town in regrown forest: what survives of the concrete and slag was not checked in this research. There is no road to it.',
  'A 3,000-person copper town with no road, left to the forest.',
  'There is no land link; it is about 60 km south of Stewart on the inlet. Land ownership and any rules or tours were not checked. Treat it as boat-only and do not go without a local guide or operator who knows the site. The pin is the town\'s position from Wikipedia and OpenStreetMap and marks the general area only.',
  [W('Anyox')],
  conf='mixed', brick='?', hours=''),
]

PIN_NOTES={
'kinsol-trestle':'Coordinate from Wikipedia; on the aerial the pin is on the rail grade where it crosses the river gap under trees.',
'walhachin-hall':'Point is the OpenStreetMap community centre, Walhachin Soldiers Memorial Hall; the town centre, not the flumes.',
'emily-carr-house':'Wikipedia coordinate, checked on the aerial.',
'helmcken-house':'Wikipedia coordinate, checked on the aerial.',
'esquimalt-nanaimo-roundhouse':'Wikipedia coordinate, checked on the aerial.',
'hatley-castle':'Wikipedia coordinate for the castle, checked on the aerial.',
'hastings-mill-store':'OpenStreetMap building named Hastings Mill Park Museum at 1575 Alma Street.',
'irving-house-new-westminster':'Wikipedia coordinate, checked on the aerial.',
'craigflower-schoolhouse':'OpenStreetMap and Wikipedia coordinates agree; checked on the aerial.',
'ss-sicamous-penticton':'Wikipedia coordinate; the ship is beached beside Lakeshore Drive West.',
'anyox-ghost-town':'Position of the town from Wikipedia and OpenStreetMap, area only; the aerial tile shows only forest and a track, no buildings, so the pin is not on any ruin.',
}
