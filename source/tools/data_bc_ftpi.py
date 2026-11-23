# November 23, 2026: a second scatter of places across British Columbia, claimed with tools/choose.py --thinnest (bc had
# 36 places). Spread from the west coast of Vancouver Island to the Rockies and the far north-west: Victoria, Shirley,
# West Vancouver, Richmond, Mission, Harrison Mills, Hope, Keremeos, Kelowna, Vernon, Greenwood, Rossland, Castlegar,
# Yoho National Park and Atlin.
# Sources read in this session: Wikipedia (tools/wiki_raw.py), the Canadian Register of Historic Places where its pages
# opened (historicplaces.ca refused most requests this session after the first few), the Parks Canada Directory of Federal
# Heritage Designations, and the managing bodies' own pages where they opened (BC Parks, BC Hydro, Kilby Historic Site,
# the Sheringham Point Lighthouse Preservation Society, the Rossland Museum, the Greenwood Museum, the City of Greenwood,
# the Historic O'Keefe Ranch, the Province of British Columbia news release on Point Ellice House, the Anglican Diocese of
# New Westminster). Where a page would not open, the entry says what the hours rest on. Nothing was checked on the ground.
from data_b import N
from data_ma import W
BATCH={'key':'bc_ftpi','label':'British Columbia: a second scatter, Vancouver Island to Atlin','added':'2026-11-23 05:46'}

def CR(i,label):
    return [label+' (Canadian Register of Historic Places)','https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=%d'%i]

PLACES=[
N('christ-church-hope','Christ Church','Hope','bc','worship','standing',49.3808,-121.44569,'exact','view','drive','','1861',
  'An Anglican parish church built in 1861 under Bishop George Hills, with the Royal Engineers, at the height of the Fraser River gold rush. It is one of about fourteen such churches put up in the colony between 1859 and 1866, and Parks Canada calls it the oldest church in British Columbia still on its original foundation. It was made a National Historic Site in 1994 and is still a parish church.',
  'A small Gothic Revival church of wood: a clapboard nave and a lower chancel under separate gable roofs, a side entrance porch with a pointed doorway, square-headed windows and a bell tower, on a big lot among tall firs. Inside, a chancel rail and a chancel raised three steps above the nave (Register statement). Interior not checked in person.',
  'The oldest church in BC on its first foundation, built in a gold-rush camp.',
  'An active Anglican parish (Diocese of New Westminster) at 681 Fraser Avenue, at the corner of Park Street, one block west of the Trans-Canada Highway. The diocese page says the parish holds weekly services but gives no times; view from the street otherwise. Parking on the street, not checked.',
  [CR(12564,'Christ Church National Historic Site of Canada'),['Parks Canada: Christ Church National Historic Site','https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=828'],['Anglican Diocese of New Westminster: Christ Church Hope','https://vancouver.anglican.ca/yale/christ-church-hope']],
  brick='no', hours='?'),

N('kilby-historic-site','Kilby General Store and Historic Site','Harrison Mills','bc','civic','standing',49.23593,-121.95713,'exact','open','drive','','1906–1977',
  'Thomas and Eliza Kilby opened the T. Kilby Hotel and General Store on August 14, 1906, beside the Canadian Pacific line, to serve the company town of the Rat Portage sawmill at Harrison Mills, near where the Harrison River joins the Fraser. Their son Acton ran it from 1922. The Encyclopedia of BC says the province bought it in 1972 and made it a museum of a 1920s country store; other accounts say the family ran it until 1977. The Kilby Heritage Society runs it now.',
  'The general store with its stock laid out as in the 1920s, a heritage post office, the Manchester House hotel and a farm, beside the railway (British Columbia Magazine). Inside the store is the museum; a café and gift shop are on the site.',
  'A 1906 country store, hotel and post office kept as the family left it.',
  'Run by the Kilby Heritage Society at 215 Kilby Road, Harrison Mills. 2026 admission $16 adults, $13 seniors, $11 youth and students, children 5 and under free, $42 family; last admission 30 minutes before closing (Kilby hours page, read November 2026). Closed from December 14 until spring 2027. OpenStreetMap maps a lot on Kilby Road beside the store; the next-door Kilby Park campground is open all year.',
  [['Kilby Historic Site: hours and fees','https://kilby.ca/visit/hours-fees/'],['British Columbia Magazine: Exploring the Kilby Historic Site','https://www.bcmag.ca/exploring-the-kilby-historic-site/'],['Encyclopedia of BC: Kilby General Store','https://knowbc.com/limited/Books/Encyclopedia-of-BC/K/Kilby-General-Store']],
  conf='mixed', th=[49.23612,-121.95575], thn='Lot on Kilby Road', brick='no',
  hours='2026: Apr 2 to Jun 21 Thu–Sun 11–4; Jun 25 to Sep 7 Thu–Mon 10–4; Sep 10 to Nov 1 Thu–Sun; Nov 7 to Dec 13 Sat–Sun (museum 11–4); closed to spring'),

N('stave-falls-powerhouse','Stave Falls Powerhouse','Mission','bc','industry','standing',49.22869,-122.35462,'exact','open','drive','','1911–2000',
  'The first generator at Stave Falls went on line in December 1911, and the plant grew to five generators by 1925; it was once British Columbia\'s largest source of hydroelectric power and is a National Historic Site. The dam was raised in 1925. A new powerhouse replaced the old one between 1995 and 2000, and the original building became BC Hydro\'s visitor centre.',
  'A walk through the 100-year-old powerhouse with historical displays and electricity demonstrations (BC Hydro); the old penstocks are beside it (Wikipedia). Guided tours drop-in; audio tours in several languages.',
  'Walk through what was once BC\'s biggest power plant.',
  'BC Hydro visitor centre at 31338 Dewdney Trunk Road, Mission. Closed for the winter; reopening March 1, 2027 (BC Hydro page, read November 2026). Free parking for cars, RVs and buses; fully wheelchair accessible; only guide and service dogs. Groups of ten or more must book. Hours may change without notice.',
  [W('Stave Falls Dam and Powerhouse'),['BC Hydro: the Powerhouse at Stave Falls','https://www.bchydro.com/community/recreation_areas/visitor-centres/stave-falls-visitor-centre.html']],
  brick='?', hours='Mar 1 to Jun 21 daily; Jun 22 to Sep 9 closed Tue and Wed; Sep 10 to Oct 12 daily; 10 a.m. to 4 p.m. (2027 season); closed in winter'),

N('britannia-shipyards','Britannia Shipyards','Richmond','bc','industry','standing',49.12085,-123.1702,'site','open','walk','','1889–1980',
  'The Britannia Cannery opened here on the Steveston Channel of the Fraser in 1889, one of more than a dozen canneries on Steveston\'s Cannery Row. Canning stopped in 1917 and the main building became a boat repair yard; part of the site was leased to the Murakami boatworks in 1918, until the family was interned in 1942. It stayed a working shipyard until 1980, was given to the City of Richmond and became a National Historic Site in 1991.',
  'Cannery and shipyard buildings, workers\' houses and stores linked by the original wooden boardwalks over the tidal flats, run as an open-air museum (Wikipedia).',
  'A whole cannery-and-boatyard community on stilts over the Fraser.',
  'City of Richmond heritage park at 5180 Westwater Drive, Steveston; admission has been free (City of Richmond release, 2021). Hours not checked from a page of the city\'s own: a city release of 2021 gives summer hours of daily 10 a.m. to 5 p.m., and a tourism listing gives winter hours of noon to 5 p.m. Parking not checked: the lot OpenStreetMap maps on Westwater Drive could not be made out on the aerial.',
  [W('Britannia Shipyard'),['City of Richmond: Britannia Shipyards','https://www.richmond.ca/culture/sites/britanniashipyards.htm']],
  brick='?', hours='?'),

N('point-atkinson-lighthouse','Point Atkinson Lighthouse','West Vancouver','bc','light','standing',49.33039,-123.26459,'exact','public','walk','','1875; 1914',
  'A wooden lighthouse with a keeper\'s house first shone on Point Atkinson, at the mouth of Burrard Inlet, on March 17, 1875; a fog alarm followed in 1889 at the demand of Canadian Pacific Steamships. The present reinforced-concrete tower went up on the granite shore in 1914, and was thought new in design at the time. It is automated, still in use, and a National Historic Site.',
  'A white six-sided concrete tower on the rocks, seen from the viewpoints of Lighthouse Park; the tower itself is not open. The park\'s old-growth forest is the walk in.',
  'A 1914 concrete light at the door of Vancouver harbour.',
  'In Lighthouse Park, a District of West Vancouver park, on Beacon Lane off Marine Drive. The district\'s page refused this tool; as quoted in a search result it says the park is open 7 a.m. to 10 p.m. daily and the lot is pay parking all year. The lot is small and fills at weekends. OpenStreetMap maps the lot about 800 m north of the lighthouse, under trees on the aerial.',
  [W('Point Atkinson Lighthouse'),['District of West Vancouver: Lighthouse Park','https://westvancouver.ca/parks-recreation/parks-trails/lighthouse-park']],
  brick='no', hours='Park 7 a.m. to 10 p.m. daily'),

N('craigdarroch-castle','Craigdarroch Castle','Victoria','bc','landmark','standing',48.42263,-123.34376,'exact','open','drive','','1887–1890',
  'A Scottish baronial mansion of 37 rooms built between 1887 and 1890 for the coal baron Robert Dunsmuir and his wife Joan; Robert died in 1889, before it was finished. It was later a military hospital, a college, offices and a music conservatory, and has been a museum since 1979, run by a non-profit society. It is a National Historic Site.',
  'Walls of grey stone under red roofs and turrets (photographs on Wikimedia Commons). The whole house, with 17 fireplaces and a tower reached by 87 steps (Wikipedia), shown by self-guided tour.',
  'A coal baron\'s castle on a Victoria hill.',
  'Run by the Craigdarroch Castle Historical Museum Society at 1050 Joan Crescent. The castle\'s own page is drawn by script and could not be read; the hours here are as a search result quotes it, with adult tickets at $23.50 and seniors at $21. The ticket office closes 15 minutes before the castle. Parking not checked.',
  [W('Craigdarroch Castle'),['Craigdarroch Castle: plan your visit','https://thecastle.ca/plan/plan-your-visit']],
  brick='no', hours='Wednesday to Sunday 10 a.m. to 5:30 p.m.; closed December 25, 26 and January 1'),

N('point-ellice-house','Point Ellice House','Victoria','bc','landmark','standing',48.43608,-123.37727,'exact','view','drive','','1861–62',
  'One of Victoria\'s oldest houses, built in 1861–62 above the Gorge Waterway for Charles Wentworth Wallace and Catherine Wallace, daughter of the Hudson\'s Bay Company chief factor John Work. Peter and Caroline O\'Reilly moved in in 1867 and the family lived there until 1975, when they sold the house, land and the family\'s household collection to the province. It became a National Historic Site in 1966 and a provincial heritage site in 1975.',
  'The house and its gardens on the waterway. It closed to the public on August 21, 2026, and the province took it over on September 2 to look after the house and its collection; it says it is looking at how to reopen it.',
  'A gold-rush-era house left with the family\'s things in it.',
  'Owned by the Province of British Columbia at 2616 Pleasant Street. Closed to visitors since August 21, 2026 (province news release of August 4, 2026); view from the street. Parking not checked.',
  [W('Point Ellice House'),['BC Gov News: Point Ellice House closes to public','https://news.gov.bc.ca/releases/2026TACS0034-000893']],
  brick='?', hours=''),

N('sheringham-point-lighthouse','Sheringham Point Lighthouse','Shirley','bc','light','standing',48.37676,-123.92108,'exact','public','walk','','1912',
  'Built in 1912 on the south-west coast of Vancouver Island after the wreck of the SS Valencia in 1906, to guide ships into the Strait of Juan de Fuca. It was kept by keepers for 77 years and automated in 1989. The federal government named it a heritage lighthouse in 2015 and gave the tower and two hectares round it to a local preservation society, which reopened the site in 2016.',
  'A six-sided reinforced-concrete tower with six flaring buttresses that hold up the gallery against the wind (Wikipedia), on the point above the strait, with a volunteer visitor centre open now and then.',
  'A buttressed concrete light built after one of the coast\'s worst wrecks.',
  'Owned by the Sheringham Point Lighthouse Preservation Society. The society\'s page: the site is open every day; drive about 1.7 km down Sheringham Point Road (next left after the Shirley fire hall) to the lot at its end, then walk Jennie\'s Trail, about 200 m, to the lighthouse gate. No legal access or parking on Seaside Drive or Lighthouse Road. No vehicles on the trail except service vehicles and mobility scooters. Toilet at the lot. The site may close in bad weather. The page\'s closing times did not read cleanly.',
  [W('Sheringham Point Light'),['Sheringham Point Lighthouse Preservation Society: visit','https://sheringhamlighthouse.ca/the-lighthouse-2/visit-the-lighthouse-site/']],
  brick='no', hours='Daily from 9 a.m.; closing time varies by season'),

N('grist-mill-keremeos','Grist Mill at Keremeos','Keremeos','bc','industry','standing',49.21391,-119.80751,'site','open','drive','','1877',
  'A flour mill driven by a water wheel, built in 1877 by Barrington Price in the Similkameen valley. The site, now owned by the Province of British Columbia, keeps the mill with its old milling machinery, a general store and house, and an apple house and root cellar, with newer and replica buildings round them.',
  'A weathered log and plank mill with a large wooden water wheel and its flume (photographs on Wikimedia Commons). The working mill and its machinery, the store, the house and the gardens (Wikipedia). Interior not checked in person.',
  'A working 1877 water-wheel flour mill.',
  'Provincial heritage site at 2691 Upper Bench Road, just north of the junction of Highways 3 and 3A. Hours not checked from a page of the mill\'s own: a tourism listing gives 10 a.m. to 4 p.m. from mid-April to mid-October, and in 2026 the site was under new management. OpenStreetMap maps a lot on Upper Bench Road beside it.',
  [W('Grist Mill (Keremeos)'),CR(1674,'Grist Mill at Keremeos'),['The Grist Mill and Gardens','https://oldgristmill.ca/contact/']],
  th=[49.21430,-119.80685], thn='Lot on Upper Bench Road', brick='no', hours='?'),

N('myra-canyon-trestles','Myra Canyon trestles (Kettle Valley Railway)','Kelowna','bc','rail','standing',49.79168,-119.31191,'site','public','walk','','1914–1973',
  'The Kettle Valley Railway crossed Myra Canyon, south-east of Kelowna, on 18 wooden trestles and through two tunnels between Myra and June Springs stations. Trains stopped on the section in May 1973 and the line was abandoned in 1978. The 2003 Okanagan Mountain Park fire burned 14 of the 18 trestles; the province rebuilt them, and the trail is open again, the trestles kept up by a non-profit society. The section is a National Historic Site.',
  'Rebuilt timber trestles and old tunnels strung round the canyon on the old rail bed, now a walking and cycling trail. The pin is on OpenStreetMap\'s Trestle 18, about 1 km from the Myra Station lot.',
  'Eighteen trestles round one canyon, rebuilt after a forest fire.',
  'In Myra-Bellevue Park (BC Parks). Start from the Myra Station parking lot; no parking beyond it, and no motor vehicles past it. The trail is very busy in summer. Hazards from the 2003 fire remain in the area. BC Parks offers a free trestle map and guide. Hours not checked.',
  [W('Kettle Valley Railway'),['BC Parks: Myra-Bellevue Park','https://bcparks.ca/myra-bellevue-park/']],
  th=[49.80108,-119.31291], thn='Myra Station parking lot', brick='no', hours='?'),

N('okeefe-ranch','Historic O\'Keefe Ranch','Vernon','bc','landmark','standing',50.36477,-119.28072,'site','view','drive','','1867',
  'Cornelius O\'Keefe pre-empted bottom land at the head of Okanagan Lake in June 1867 and built up a ranch and a store here. He lived in his ranch house until his death, and the family kept it until 1977; it was sold on to the City of Vernon for $1 to be run as a historic site. St. Ann\'s church on the ranch was built in 1889 and is one of the earliest churches still standing in the North Okanagan.',
  'The O\'Keefe mansion, St. Ann\'s church and cemetery, the Balmoral schoolhouse and other 19th-century ranch buildings (Wikipedia). In October 2026 the ranch said its historic buildings are closed until further notice, though visitors may walk the grounds and see the animals; the City of Vernon\'s plans could close the site for good.',
  'A cattle ranch of 1867 with its mansion and wooden church.',
  'Owned by the City of Vernon and run by the Historic O\'Keefe Ranch & Interior Heritage Society on Highway 97 about 12 km north of Vernon. Historic buildings closed until further notice; grounds open to walk (ranch home page, read November 2026). Parking not checked.',
  [W("O'Keefe Ranch"),['Historic O\'Keefe Ranch','https://okeeferanch.ca/']],
  brick='?', hours='?'),

N('greenwood-smelter-stack','BC Copper Company smelter stack and slag','Greenwood','bc','industry','ruins',49.07925,-118.68922,'site','view','drive','','1901–1918',
  'The British Columbia Copper Company, a New York firm that bought the Mother Lode mine in 1898, built a smelter at the mouth of Copper Creek, at Anaconda just south of Greenwood; the first furnace was blown in on February 18, 1901. Ore ran short from 1912, the plant worked on and off through the First World War, and it closed for good on November 26, 1918. The site was later given to the City of Greenwood as Lotzkar Memorial Park.',
  'The brick smokestack, 36 m (121 ft) high, standing over a huge black slag pile at the edge of town (Greenwood Museum); the superintendent\'s house still stands nearby.',
  'A lone 36-metre smelter stack over a black slag mountain.',
  'Lotzkar Memorial Park, City of Greenwood, on Everett Avenue in Anaconda. A search result quotes the city\'s site as saying the smelter ruins project is under construction and not open for touring, so look from the park\'s edge and the road. The Greenwood Museum & Visitor Centre arranges heritage walking tours. Parking not checked.',
  [['Greenwood Museum: mining history','https://sites.google.com/charnleyvanwyk.com/greenwoodmuseumvisitorcentre/history/mining-history'],['City of Greenwood: heritage and history','https://www.greenwoodcity.com/community-events/heritage-history/'],W('Greenwood, British Columbia')],
  brick='?', hours=''),

N('rossland-court-house','Rossland Court House','Rossland','bc','civic','standing',49.07713,-117.79572,'exact','view','drive','','1898–1901',
  'Rossland\'s third court house, designed by John J. Honeyman and built by James Lawn for $38,500; work began in 1898 and it opened in May 1901, when Rossland was a boom town of gold-copper mines. It has served as a court house ever since and became a National Historic Site in 1980.',
  'A buff-brick building on a cut-stone basement with a tower at each corner, three under steep tiled pyramid roofs, behind stone retaining walls and an entrance stair. Inside, a wood-panelled court room with a timber ceiling inlaid with cedar and a great stained-glass window with the provincial arms flanked by the arms of Begbie and Douglas (Register statement). Interior not checked in person.',
  'A fortress-like gold-rush court house with its court room intact.',
  'A working court house at 2288 Columbia Avenue, at Monte Cristo Street; view from the street. Whether the public may look in outside court business not checked. Parking on the street, not checked.',
  [CR(7838,'Rossland Court House National Historic Site of Canada'),['Rossland Museum: Court House','https://rosslandmuseum.ca/court-house']],
  brick='no', hours=''),

N('doukhobor-suspension-bridge','Doukhobor Suspension Bridge','Castlegar','bc','landmark','standing',49.3173,-117.62957,'exact','public','walk','','1913',
  'Doukhobor settlers built this suspension bridge over the Kootenay River in eight months of 1913, with their own labour and money at the call of their leader Peter Verigin, to join their communities of Brilliant and Ootischenia. A new highway bridge replaced it in 1966 and it was abandoned. Restoration began in the early 1990s, it became a National Historic Site in 1995, and it reopened as a footbridge in 2010.',
  'Reinforced-concrete towers 14.6 m high on piers set in the rock of both banks, four steel cables, a deck 100.9 m long hung on steel rods with a steel frame and wood planking, and a date cut in one tower (Register statement).',
  'A bridge a utopian community built by hand in 1913.',
  'The centre of Brilliant Bridge Regional Park, run by the Regional District of Central Kootenay, at Brilliant Road in rural Castlegar. Hours and parking not checked: the district\'s page read gave neither.',
  [CR(7818,'Doukhobor Suspension Bridge National Historic Site of Canada'),W('Brilliant Suspension Bridge'),['Regional District of Central Kootenay: Brilliant Bridge Regional Park','https://rdck.ca/community-services/brilliant-bridge-regional-park/']],
  brick='no', hours='?'),

N('twin-falls-tea-house','Twin Falls Tea House','Yoho National Park','bc','hotel','standing',51.54583,-116.5275,'area','view','hike','','1908',
  'A log rest house for hikers and trail riders near Twin Falls in the Little Yoho Valley, first built about 1908 by the Canadian Pacific Railway or an outfitter working with it. A two-storey chalet-style cabin was added about 1923 and joined to it between 1925 and 1928. Parks Canada proposed pulling it down in 1969; the woman who ran it led a letter-writing campaign that saved it. It became a National Historic Site in 1992 and was extensively renovated in 2005.',
  'Two log buildings of unusually massive peeled logs, the later one with a balcony looking at Twin Falls; no running water or electricity, a wood-burning stove and kerosene lamps (Wikipedia).',
  'A 1908 log tea house at the end of a mountain trail.',
  'In Yoho National Park (Parks Canada), run by a private operator under a Parks Canada licence. It is a long day hike from the Takakkaw Falls parking lot at the end of the Yoho Valley Road; a search result quotes Parks Canada as giving 8.5 km. The Parks Canada page could not be opened, so the season and whether it is open now were not checked. Park pass needed. OpenStreetMap maps the lot by the Takakkaw Falls campground.',
  [W('Twin Falls Tea House'),['Parks Canada: Twin Falls Tea House National Historic Site','https://parks.canada.ca/pn-np/bc/yoho/culture/twin']],
  th=[51.49743,-116.48414], thn='Takakkaw Falls lot', brick='no', hours='?'),

N('tarahne-atlin','M.V. Tarahne','Atlin','bc','landmark','standing',59.57325,-133.70622,'exact','view','walk','','1916 or 1917',
  'A lake boat built at Atlin by the White Pass and Yukon Route; the sources differ on the year, 1916 or 1917. It carried passengers and freight between Atlin and Scotia Bay until 1936, bringing tourists who came up the Inside Passage to the company\'s Atlin Inn. It now rests on the lakeshore and belongs to the Atlin Historical Society.',
  'The white-painted boat hauled out on the shore of Atlin Lake (photograph on Wikimedia Commons), in the gold-rush town; in 2021 a concert series was filmed aboard. The Atlin courthouse, built 1900 and now an art gallery, and the museum in the old schoolhouse are in the same town (Wikipedia).',
  'A 1910s lake boat beached in BC\'s far north-west gold town.',
  'Owned by the Atlin Historical Society, a volunteer charity. Atlin is reached only by the Atlin Road from the Yukon. Whether visitors can go aboard, and when, not checked: the society\'s page could not be opened. Parking not checked.',
  [W('Atlin, British Columbia')],
  conf='mixed', brick='no', hours=''),
]

PIN_NOTES={
 'christ-church-hope':'OpenStreetMap point for Christ Church at 681 Fraser Avenue.',
 'kilby-historic-site':'OpenStreetMap point for the Kilby General Store museum.',
 'stave-falls-powerhouse':'OpenStreetMap building mapped as Stave Falls Powerhouse.',
 'britannia-shipyards':'OpenStreetMap point for the Britannia Shipyards National Historic Site, on the tidal marsh between the shipyard buildings on the aerial; the pin marks the site.',
 'point-atkinson-lighthouse':'OpenStreetMap lighthouse point; the parking point is the OpenStreetMap Lighthouse Park lot.',
 'craigdarroch-castle':'OpenStreetMap point for the castle building.',
 'point-ellice-house':'OpenStreetMap point for Point Ellice House.',
 'sheringham-point-lighthouse':'OpenStreetMap lighthouse point on Jennie\'s Trail.',
 'grist-mill-keremeos':'Address point for 2691 Upper Bench Road from the ArcGIS geocoder; on the aerial it falls in an open field of the grounds, south of the lot and the trees along the creek, and the mill building could not be picked out. The pin marks the site.',
 'myra-canyon-trestles':'OpenStreetMap abandoned railway way named Trestle 18, on the old grade on the aerial; the parking point is the OpenStreetMap Myra Station lot, which shows parked cars.',
 'okeefe-ranch':'OpenStreetMap point for O\'Keefe Ranch museum; Wikipedia\'s coordinate is about 5 km away to the north-west.',
 'greenwood-smelter-stack':'OpenStreetMap ruins point for Lotzkar Memorial Park; on the aerial it falls on the black slag pile. The stack itself could not be picked out, so the pin marks the site.',
 'rossland-court-house':'OpenStreetMap courthouse point.',
 'doukhobor-suspension-bridge':'OpenStreetMap way for the Old Brilliant Bridge.',
 'twin-falls-tea-house':'Wikipedia coordinate, on a bend of the creek in forest; the building could not be seen on the aerial, so the pin marks only the general area.',
 'tarahne-atlin':'OpenStreetMap point for the MV Tarahne.',
}
