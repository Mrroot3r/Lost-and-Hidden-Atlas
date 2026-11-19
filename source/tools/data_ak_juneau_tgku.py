# November 19, 2026: the City and Borough of Juneau, Alaska: downtown Juneau, Douglas, the Basin Road mines, the road
# north to Amalga Harbor and the light stations on Lynn Canal. Region drawn at random by tools/choose.py (ak).
# Sources read in this session: the Wikipedia articles (tools/wiki_raw.py) and the Register list for Juneau, the
# National Register nomination forms (NPGallery "_text" PDFs, text layers read with tools/page.py), the pages of
# Alaska State Parks, the City and Borough of Juneau (museum hours, Evergreen Cemetery, Perseverance Trail notices,
# the 2018 Treadwell Mine Historic Site and Trail Plan, the historic structures list), St. Nicholas Orthodox Church,
# the National Shrine of St. Therese, the Alaskan Hotel, Wings Airways, HMdb, the Juneau Empire, the Juneau
# Independent, KTOO, Alaska's News Source, the Seattle Times archive and Lighthouse Friends. Interiors were not visited
# by any source opened unless the entry says so.
from data_b import N
from data_ma import W
BATCH={'key':'ak_juneau_tgku','label':'Alaska: Juneau, Douglas and Lynn Canal','added':'2026-11-19 20:24'}

def NR(ref,label):
    return [label+' (National Register nomination)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/%s_text'%ref]
TOWN='Downtown Juneau: street parking and public lots; parking was not checked on the ground.'
CBJHSD=['Juneau: Historic Structures Database','https://juneau.org/community-development/hsd-list/entry/41736']

PLACES=[
N('st-nicholas-orthodox-church-juneau','St. Nicholas Russian Orthodox Church','Juneau','ak','worship','standing',58.30315,-134.40886,'exact','open','walk','','1893',
  'A small octagonal wooden church built in 1893 and consecrated early in 1894, now a parish of the Diocese of Alaska of the Orthodox Church in America. Juneau never had Russian settlers: the Orthodox church came here through Tlingit leaders, among them the Taku leader Anathahash, who was baptised in Sitka in 1890 and came back with the first Orthodox priest to serve the area. The Missionary Society in Russia sent drawings, furnishings, a full iconostasis and two hundred silver rubles for the building.',
  'A wood-frame church on an octagonal plan with a small entry porch, small cupolas on four of the eight roof panels and an onion dome with an Orthodox cross (1973 nomination). Wikipedia says the six large panels of the iconostasis are the original icons from Russia. The parish shows liturgical items shipped in 1893, a gallery of St. Nicholas art and clergy photographs in its visitor centre and shop in the rectory.',
  '',
  'Active Orthodox parish at 326 5th Street. Its page says the church is open for visitors in summer at the hours given and that winter tours are by appointment (by email through its page); visitors are welcome at services. The shop is run by volunteers and its hours vary. The parish\'s weekly schedule page gives Sunday "Hours and Divine Liturgy" at 9:40 a.m., the visitor page Divine Liturgy at 10 a.m. Hours from the parish\'s visitor page, read November 2026. '+TOWN,
  [W('St. Nicholas Russian Orthodox Church (Juneau, Alaska)'),NR('73000377','St. Nicholas Russian Orthodox Church'),['St. Nicholas Orthodox Church: visitor centre and hours','https://stnicholasjuneau.org/?p=98'],['St. Nicholas: weekly schedule','https://stnicholasjuneau.org/sunday-bulletin-weekly-schedule/']],
  brick='no',hours='Summer 2026: Monday to Saturday 9 a.m. to 7 p.m. (Vigil Saturday 5 p.m.); Sunday Divine Liturgy 10 a.m., open until 7 p.m. Winter tours by appointment'),

N('house-of-wickersham-juneau','House of Wickersham (Wickersham State Historic Site)','Juneau','ak','landmark','standing',58.30351,-134.4114,'exact','open','walk','','1898–1899',
  'The first large Victorian house on Chicken Ridge, Juneau\'s "Nob Hill", built by Frank Hammond, the owner of a mining company. James Wickersham, judge, delegate to Congress and the man Alaska State Parks credits with Home Rule, the Alaska Railroad, the University of Alaska and Denali National Park, bought it in 1928 and lived here until his death in 1939. His niece began showing it in 1958, and the state bought it in 1984. The building year is not settled: the state\'s page says 1898, Wikipedia 1899.',
  'A frame house with a view over the town and the channel; Alaska State Parks shows it as a house museum on Wickersham\'s life and Alaska\'s territorial days. Interior not checked.',
  '',
  'Alaska State Parks owns and runs it, at 213 7th Street (from South Main Street turn right on 7th). The state\'s page says only that it is open for the summer season, May through September; days and times were not on the page read in November 2026. Parking was not checked; 7th Street is a steep residential street.',
  [W('House of Wickersham (Juneau, Alaska)'),['Alaska State Parks: Wickersham State Historic Site','https://dnr.alaska.gov/parks/aspunits/southeast/wickshp.htm']],
  conf='mixed',brick='no',hours='May to September; days and times not given on the state page'),

N('juneau-douglas-city-museum','Juneau-Douglas City Museum (Juneau Memorial Library)','Juneau','ak','civic','standing',58.3018,-134.41127,'exact','open','walk','','1950–1951',
  'Built in 1950-51 as the Juneau Memorial Library, opposite the State Capitol at Fourth and Main, and the city\'s library until the 1980s, when it became the city museum. Its exhibits cover gold mining, hydropower, skiing, fishing, politics and the town\'s history.',
  'A two-storey Classical Revival building of concrete with red marble trim, its entrance recessed in a full-height opening under a pediment, with a stained glass decoration behind the big window under the northeast gable (Wikipedia). Outside stands Harnessing of the Atom, a totem pole carved by the Tlingit artist Amos Wallace in 1967.',
  '',
  'Run by the City and Borough of Juneau. Its page gives the same days and times for July to September and October to December 2026: summer admission $7 ($6 seniors, 12 and under free with an adult); free October to December. Hours from the city\'s page, read November 2026. '+TOWN,
  [W('Juneau-Douglas City Museum'),['City and Borough of Juneau: museum hours','https://juneau.org/view/museum-hours']],
  brick='no',hours='Wednesday to Saturday 11 a.m. to 4:30 p.m. (July to December 2026)'),

N('last-chance-basin-jualpa-mining-camp','Jualpa Mining Camp and Last Chance Mining Museum','Juneau','ak','industry','standing',58.30559,-134.38448,'site','open','walk','','1910s–1944',
  'The Alaska-Juneau Gold Mining Company\'s camp on the south bank of Gold Creek in Last Chance Basin, about a mile above Juneau at the end of Basin Road. It was set up between 1910 and 1913 and worked until 1944, and the mine produced more than $80 million in gold. Crews laid two miles of track through three tunnels to carry the ore to the company\'s mill on Gastineau Channel. The camp, with 21 contributing buildings and structures, was listed on the National Register in 1993.',
  'The largest building left is the 84-foot air compressor building, which still holds the company\'s compressor and is now the Last Chance Mining Museum of the Gastineau Channel Historical Society. Also left: railway pieces, a transformer house, a powder magazine and a cable hoist (Wikipedia). The Seattle Times wrote in 1993 of half a dozen camp buildings still standing and crumbling; their state now was not checked.',
  '',
  'The museum is run by the Gastineau Channel Historical Society; who owns the ground was not checked. No page of the museum\'s own was found: the Travel Juneau listing (a visitor bureau directory, not the museum) gives Thursday to Monday 2 to 5 p.m. until mid-September and a $5 cash fee. Reached by Basin Road from downtown, about two miles from the cruise docks on foot. The city has warned of avalanches and landslides along Basin Road and near the Perseverance trailhead, with slopes of unknown stability; parking at the end of the road was not checked.',
  [W('Last Chance Mining Museum'),NR('93000733','Jualpa Mining Camp'),['Seattle Times, 1993: Remains from Juneau\'s mining past crumbling','https://archive.seattletimes.com/archive/19930627/1708537/remains-from-juneaus-mining-past-crumbling'],['City and Borough of Juneau: Basin Road and Perseverance Trail hazards','https://juneau.org/newsroom-item/avalanche-and-landslide-hazards-on-basin-road-perseverance-trail-2']],
  brick='?',hours='?'),

N('treadwell-mine-ruins-douglas','Treadwell gold mine ruins','Douglas','ak','industry','ruins',58.26915,-134.3785,'site','public','walk','','1881–1922',
  'John Treadwell bought a lode claim on Douglas Island in 1881, and by 1884 a 120-stamp mill was running. Four mines made up the complex, which at its height (1911 to 1917) was the largest hard-rock gold mine in the world, with over 2,000 workers. On April 21, 1917 a cave-in at sea level flooded three of the mines; only the Ready Bullion went on, and mining ended in 1922. Fires destroyed most of the wooden buildings, among them one in 1926.',
  'A trail through the woods past the Glory Hole (the first, open-pit mine, now full of water), the foundations of dozens of machinery and housing buildings, the remains of the "New" Office Building, ties and pieces of the 1888 Treadwell Express (the city plan calls it the first railroad in Alaska), and bits of the wood-stave, steel and concrete pipes and trestles that brought the water. Interpretive signs along the way (city trail plan, 2018).',
  '',
  'The City and Borough of Juneau owns the site, cared for by the Treadwell Historic Preservation and Restoration Society under a 2009 agreement (trail plan). Park at Savikko Park (Sandy Beach) in Douglas, on Saint Ann\'s Avenue, and walk the trail east; the mapped lot is about 900 m from the pin. Hours not checked. Keep back from the edge of the Glory Hole.',
  [W('Treadwell gold mine'),['City and Borough of Juneau: Treadwell Mine Historic Site and Trail Plan (2018)','https://juneau.org/wp-content/uploads/2019/12/Treadwell-Mine-Historic-Site-Trail-Plan-2018.pdf']],
  th=[58.27417,-134.39051],thn='Savikko Park (Sandy Beach) lot, Saint Ann\'s Avenue',brick='?'),

N('alaska-juneau-mill-ruins','Alaska-Juneau gold mill ruins','Juneau','ak','industry','ruins',58.29362,-134.39538,'area','view','drive','','1917–1944',
  'The Alaska-Juneau company\'s mill on the side of Mount Roberts, where from 1917 to 1944 ore brought two miles by electric train from Silver Bow Basin was sorted, crushed and treated. HMdb\'s marker says it crushed almost 100 million tons of ore for 3.5 million ounces of gold, and that its tailings built the airport, Egan Drive and a third of downtown Juneau. The company\'s 1916 steam power plant below it, the last large AJ building on the waterfront, was being torn down at the end of 2024.',
  'What is left of the mill is its stepped foundations on the mountainside, which the marker says are visible from the Mount Roberts tram and from Gastineau Channel; the Juneau Empire photographed them in April 2024 through bare trees from Douglas Island. Not checked on the ground.',
  '',
  'Seen from a distance only: from South Franklin Street near the south cruise docks, the tram, or across the channel. Who owns the mill ground was not checked; the steam plant parcel below belongs to Alaska Electric Light & Power (Juneau Empire). Nothing read says the public may go up to the ruins. The pin is the site of the steam plant below the mill, not the mill itself.',
  [['HMdb: Alaska Juneau Mill marker','https://www.hmdb.org/m.asp?m=42823'],['Juneau Empire: the AJ steam plant comes down','https://www.juneauempire.com/news/going-goinggone-the-last-aj-mine-building-disappears']],
  conf='mixed',brick='?'),

N('alaskan-hotel-juneau','Alaskan Hotel and Bar','Juneau','ak','hotel','standing',58.30028,-134.40497,'exact','open','walk','','1913',
  'The hotel opened on September 16, 1913, built by a promoter named Caro and the brothers James and John McCloskey next to the old Central hotel, near the steamship docks; the owners give it as the oldest operating hotel in Alaska. It had steam heat and a wireless station on the roof. It was briefly condemned in the 1970s and restored after Mike and Bettye Adams bought it in 1977.',
  'A three-storey frame building with a stucco front and two big bay windows running from the eaves down to the two front entrances (1978 nomination). The owners say they have brought it back to its Victorian style, and that the bar keeps 19th-century fittings, among them a replica Tiffany lamp. Interior not checked by a visit.',
  '',
  'A working hotel and bar at 167 South Franklin Street, privately owned. Bar and front desk hours were not on the pages read. '+TOWN,
  [W('Alaskan Hotel and Bar'),NR('78000526','Alaskan Hotel'),['The Alaskan Hotel: history','https://www.thealaskanhotel.com/history/'],CBJHSD],
  brick='no',hours='?'),

N('valentine-building-juneau','Valentine Building','Juneau','ak','civic','standing',58.3007,-134.40709,'exact','view','walk','','1904–1912',
  'A two-storey wood-frame business block filling a whole five-sided city block at 202 Front Street, built in phases in 1904 and 1912 by Emery Valentine, a businessman who was mayor of Juneau six times. For the first half of the 20th century it was one of the best addresses in town.',
  'An irregular frontier commercial block with shopfronts on the ground floor (Wikipedia). Who occupies it now and the interiors were not checked.',
  '',
  'Privately owned shops and offices; see it from Front Street. '+TOWN,
  [W('Valentine Building (Juneau, Alaska)'),NR('85001275','Valentine Building')],
  brick='no'),

N('alaska-steam-laundry-juneau','Alaska Steam Laundry building','Juneau','ak','civic','standing',58.30009,-134.40511,'exact','view','walk','','1901',
  'Built in 1901 on what was then First Street, in the heart of the business district, for the Alaska Steam Laundry. The laundry stayed until 1963, when its owners, the MacKinnons, opened a new plant on Glacier Avenue (1978 nomination).',
  'A Victorian business front with a semicircular corner tower jutting out at the second storey, capped by a conical roof a storey higher; the shop front was all plate glass and the roof was laid in a parquet pattern of shingles. The 1978 nomination says the front was then almost the same as in 1901. Today\'s use and interior not checked.',
  '',
  'Privately owned, at 174 South Franklin Street; see it from the street. '+TOWN,
  [NR('78000527','Alaska Steam Laundry')],
  brick='?'),

N('bergmann-hotel-juneau','Bergmann Hotel','Juneau','ak','hotel','standing',58.30264,-134.40613,'exact','view','walk','','1913',
  'A 50-room apartment hotel that opened on December 16, 1913, built by Mrs. Bergmann, who ran leading Juneau hotels from 1896 to 1916; KTOO calls it one of Alaska\'s oldest residential buildings. City officials condemned it in March 2017. In January 2024 KTOO reported it long vacant, owned since 2019 by the D\'Amato brothers, who planned 18 apartments upstairs and a restaurant on the ground floor. Whether that work has been done was not checked.',
  'A three-storey shingled building with 66 windows over a full basement; the 1977 nomination says the front looked almost as it did when finished in 1913.',
  '',
  'Privately owned, at 434 Third Street; see it from the street. Do not go in. '+TOWN,
  [NR('77000217','Bergmann Hotel'),['KTOO, 2024: a developer wants to bring back the Bergmann','https://www.ktoo.org/2024/01/18/a-developer-wants-to-breathe-new-life-into-juneaus-historic-but-long-vacant-bergmann-hotel/']],
  brick='no'),

N('fries-miners-cabins-juneau','Fries Miners\' Cabins','Juneau','ak','landmark','standing',58.30412,-134.40527,'site','view','walk','','1913',
  'Six identical houses built in 1913 on Starr Hill as housing for workers in the nearby gold mines, of lumber from the Worthen mill on South Franklin Street; only the plumbing and wiring came from outside. They appear on the 1914 Sanborn map.',
  'A row of small Craftsman bungalows with wood-shingle walls and shake roofs on a built-up concrete base, set to take up a 15-foot fall across the lots (1988 nomination).',
  '',
  'Private houses in the 500 block of Kennedy Street; look from the street only. Parking was not checked.',
  [NR('88001347','Fries Miners\' Cabins')],
  brick='no'),

N('alaska-governors-mansion-juneau','Alaska Governor\'s Mansion','Juneau','ak','landmark','standing',58.3027,-134.41492,'exact','view','walk','','1912',
  'The territorial governor\'s house, built in the spring to autumn of 1912 to drawings signed in 1911 by James Knox Taylor, on a site reserved by presidential order in 1911. Governor Walter Clark and his family moved in on January 1, 1913 and held a public open house the next day.',
  'A two-and-a-half-storey frame house over a full cellar with concrete walls (1976 nomination, quoting the Daily Alaska Dispatch of 1913). Interior not checked.',
  '',
  'Owned by the State of Alaska and the governor\'s residence, at 716 Calhoun Avenue; see it from the street. Whether it has public tours was not checked.',
  [W('Alaska Governor\'s Mansion'),NR('76000359','Alaska Governor\'s Mansion')],
  brick='no'),

N('evergreen-cemetery-juneau','Evergreen Cemetery','Juneau','ak','burial','standing',58.30453,-134.42282,'site','public','walk','','1887',
  'Juneau\'s main burying ground from the late 1880s until the 1970s. Wikipedia says it was laid out in 1887 to replace the first cemetery on Chicken Ridge, when that ground was staked as a gold mine, and that most graves were moved here between 1889 and 1892 and the rest about 1915; the city\'s page says it became active in 1891. It was deeded to the city in 1907.',
  'An old town cemetery which the city says holds several prominent Alaskans; since 2024 it is also a certified arboretum. The city has an online map of burial records.',
  '',
  'Run by the City and Borough of Juneau Parks and Recreation at 601 Seater Street; the city describes it as open green space that people use as a park. Hours were not on the city\'s page. Parking was not checked.',
  [W('Evergreen Cemetery (Juneau, Alaska)'),['City and Borough of Juneau: Evergreen Cemetery','https://juneau.org/parks-recreation/evergreen-cemetery']],
  conf='mixed',brick='?'),

N('shrine-of-st-therese-juneau','National Shrine of St. Thérèse','Juneau','ak','worship','standing',58.47222,-134.78722,'site','open','drive','','1930s–1941',
  'A Catholic retreat on the shore of Lynn Canal, begun in the 1930s by the Jesuit Father William LeVasseur with the support of Bishop Joseph Crimont, on land first held under Forest Service permits. Volunteers with no building experience raised the stone chapel on a small island about 400 feet off the shore from the summer of 1935; the first Mass was said there in 1941. Bishop Crimont is buried in its crypt. It nearly closed in 1985, and in 2016 it was named a national shrine.',
  'The chapel, 63 by 28 feet with a 28-foot tower, has walls of beach stones gathered by volunteers. A recent renovation, the shrine says, added a metal roof, a heated floor, steel windows with granite sills and an accessible altar, and cleaned the stone. The grounds also hold a labyrinth (2001), a columbarium and gardens.',
  '',
  'Run by the shrine at 21425 Glacier Highway, north of Juneau; the shrine office is open 8 a.m. to 5 p.m. daily. No buses: the largest vehicle allowed is a 15-passenger van. Hours from the shrine\'s own pages, read November 2026.',
  [W('National Shrine of St. Thérèse, Juneau'),['Shrine of St. Therese: history','https://www.shrineofsainttherese.org/history-shrine'],['Shrine of St. Therese: visiting hours','https://www.shrineofsainttherese.org/?p=2890'],['Shrine of St. Therese: Mass times','https://shrineofsainttherese.org/shrine/mass-times']],
  th=[58.47088,-134.78337],thn='Shrine parking lot, Shrine Access Road',brick='no',
  hours='May to September 8 a.m. to 10 p.m., October to April 8 a.m. to 8 p.m.; Sunday Mass 1:30 p.m. Memorial Day to Labor Day'),

N('ernest-gruening-cabin-juneau','Ernest Gruening Cabin','Juneau','ak','landmark','standing',58.49374,-134.78678,'site','public','walk','','1947',
  'The summer cabin of Ernest Gruening, governor of Alaska Territory from 1939 to 1953 and later its senator, built in 1947 on land leased from the Forest Service by local workers including his son Hunt. Alaska State Parks says he wrote much of his statehood manifesto, "The State of Alaska", here, and entertained Adlai Stevenson, Earl Warren and many senators. It is the centre of Ernest Gruening State Historical Park.',
  'A wood-frame cabin, 24 by 28 feet, with a big fieldstone chimney and siding milled to look like logs; inside is one large room with a spiral stair to a sleeping loft (Wikipedia). Interior not checked. The park has interpretive displays on a trail, a boat launch and views across Lynn Canal.',
  '',
  'Alaska State Parks, Ernest Gruening State Historical Park: take the Glacier Highway to Amalga Harbor Road and turn right; the park is on the right. A mapped lot on Amalga Harbor Road is about 250 m south of the pin. Whether the cabin opens to visitors and the park\'s hours were not on the state page.',
  [W('Ernest Gruening Cabin'),['Alaska State Parks: Ernest Gruening State Historical Park','https://dnr.alaska.gov/parks/aspunits/southeast/ernestgrushp.htm']],
  th=[58.49162,-134.78563],thn='Amalga Harbor Road lot',brick='no'),

N('sentinel-island-light-station','Sentinel Island Light Station','Juneau','ak','light','standing',58.54625,-134.92322,'exact','boat','boat','','1902',
  'Commissioned on March 1, 1902, a few hours after Five Finger Light to the south, the second light in Southeast Alaska, built for the Klondike traffic up Lynn Canal. In August 1910 the steamship Princess May ran onto the rocks just north of it, and her passengers and crew waited in the keepers\' house. The present Art Deco concrete tower was built in 1935, and the original lantern room was moved onto it. Keepers left in 1966 and the Coast Guard burned the old house in 1971.',
  'The 1935 concrete lighthouse with the 1902 glass lantern room on top, support buildings, a tram line for heavy loads and a dock (Juneau Independent). Interior not checked.',
  '',
  'Owned by the Gastineau Channel Historical Society, which took it over from the Coast Guard (Juneau Independent). On an island in Lynn Canal about 23 miles northwest of downtown: by boat only. A tour company, Juneau Lighthouse Tours, lands groups on the island in summer (Alaska\'s News Source, 2025).',
  [W('Sentinel Island Light'),['Juneau Independent: Sentinel Island Light Station','https://www.juneauindependent.com/post/sentinel-island-light-station-adapting-to-change-over-124-years'],['Alaska\'s News Source, 2025: Sentinel Island lighthouse tour','https://www.alaskasnewssource.com/2025/06/06/roadtrippin-2025-sentinel-island-lighthouse-tour/'],['HMdb: Sentinel Island Lighthouse','https://www.hmdb.org/m.asp?m=181644']],
  brick='no'),

N('point-retreat-light-station','Point Retreat Light Station','Admiralty Island','ak','light','standing',58.41147,-134.95502,'site','boat','boat','','1904',
  'A light at the north tip of Admiralty Island, where Lynn Canal begins, first lit in 1904 from a small hexagonal wooden tower. In 1924 a combined lighthouse and fog signal building replaced it, with keepers\' houses, a wharf and a boathouse. The lantern was taken off in the 1950s and the station was unmanned in 1973.',
  'The 1924 lighthouse without its lantern, with a modern light on a post, and one keepers\' dwelling (Wikipedia; Lighthouse Friends). Not checked on the ground.',
  '',
  'Leased in 1997 to the Alaska Lighthouse Association for thirty years (Lighthouse Friends); whether it can be visited was not checked. By boat only; most people see it from cruise ships.',
  [W('Point Retreat Light'),['Lighthouse Friends: Point Retreat','https://lighthousefriends.com/light.asp?ID=827']],
  brick='?'),

N('mayflower-school-douglas','Mayflower School','Douglas','ak','civic','standing',58.27529,-134.39235,'site','view','walk','','1934',
  'Built in 1934 by the Bureau of Indian Affairs as a model school for Native children, with a library, kitchen and recreation room that served the Tlingit of Douglas as a community centre. It taught Native children only until 1940, when it joined the Juneau schools. It is the only historic Native school building left in Juneau-Douglas, and since 1994 it has housed the Juneau Montessori School.',
  'A Colonial Revival wood-frame school on a hillside in Savikko Park, with its main door on the upper level in a recessed entry flanked by fluted pilasters under a swan\'s-neck pediment (Wikipedia). Interior not checked.',
  '',
  'In use as a school at St. Ann\'s and Savikko Streets: look from outside. Savikko Park\'s lot on Saint Ann\'s Avenue is close by.',
  [W('Mayflower School (Juneau, Alaska)')],
  brick='no'),

N('taku-glacier-lodge-twin-glacier-camp','Taku Glacier Lodge (Twin Glacier Camp)','Juneau','ak','hotel','standing',58.49067,-133.94122,'site','open','boat','','1923',
  'A wilderness camp on the southeast bank of the Taku River, opened in 1923 by the Taku River Trading Company with a log lodge and eleven tents, one of the hunting and fishing camps that opened across Alaska in the 1920s. Seven buildings of 1923 to 1934 survive among thirteen.',
  'The 1923 lodge, a one-storey log and stone building 40 by 20 feet under a cross-gabled roof, is still the main building, with the camp\'s outbuildings round the edge of the clearing (1988 nomination).',
  '',
  'In the Tongass National Forest and reached by floatplane: Wings Airways flies visitors there for a meal, about 25 minutes from Juneau. Season and times were not on the page read.',
  [NR('88000556','Twin Glacier Camp'),['Wings Airways: Taku Glacier Lodge','https://wingsairways.com/blog/taku-glacier-lodge-tour/']],
  brick='no',hours='?'),
]

PIN_NOTES={
 'st-nicholas-orthodox-church-juneau':'ArcGIS PointAddress for 326 5th Street.',
 'house-of-wickersham-juneau':'ArcGIS PointAddress for 213 7th Street.',
 'juneau-douglas-city-museum':'ArcGIS PointAddress for 114 West 4th Street, at Fourth and Main.',
 'last-chance-basin-jualpa-mining-camp':'OpenStreetMap point for the Last Chance Mining Museum (Nominatim); the Register list point is 130 m southeast. The pin is on a long building in the woods on the aerial, which fits the 84-foot compressor building.',
 'treadwell-mine-ruins-douglas':'OpenStreetMap building mapped as the "New" Office Building of the Treadwell mine (Nominatim); the Glory Hole is mapped 300 m south. On the aerial the pin is on a small roofed structure in the woods. Parking is the Savikko Park lot, a paved loop on the aerial.',
 'alaska-juneau-mill-ruins':'A building mapped as ruins in OpenStreetMap beside South Franklin Street: on the aerial it is the red-roofed AJ steam plant, since torn down (2024-25). The mill foundations are on the wooded slope of Mount Roberts just above it (Juneau Empire photo caption) and could not be seen on the aerial or picked out on the LiDAR, so the pin is the area only.',
 'alaskan-hotel-juneau':'ArcGIS PointAddress for 167 South Franklin Street.',
 'valentine-building-juneau':'ArcGIS PointAddress for 202 Front Street.',
 'alaska-steam-laundry-juneau':'ArcGIS PointAddress for 174 South Franklin Street.',
 'bergmann-hotel-juneau':'ArcGIS PointAddress for 434 Third Street.',
 'fries-miners-cabins-juneau':'ArcGIS StreetAddress (interpolated) for the 500 block of Kennedy Street.',
 'alaska-governors-mansion-juneau':'ArcGIS PointAddress for 716 Calhoun Avenue; the Register list point is miles away, on another listing.',
 'evergreen-cemetery-juneau':'ArcGIS PointAddress for 601 Seater Street fell on the road at the north edge; moved 70 m south onto the open cemetery lawn seen on the aerial (tools/pix.py).',
 'shrine-of-st-therese-juneau':'Wikipedia article coordinate, on the small wooded island; the chapel is under the trees and not seen on the aerial, which shows a path from the shore. The parking point is OpenStreetMap\'s Shrine parking lot, under trees on the aerial.',
 'ernest-gruening-cabin-juneau':'Register list coordinate; the cabin is not seen under the trees on the aerial. The parking point is a large lot on Amalga Harbor Road, plain on the aerial.',
 'sentinel-island-light-station':'Register list and Wikipedia coordinate, on the island beside the light tower seen on the aerial.',
 'point-retreat-light-station':'Wikipedia coordinate, on the station buildings seen on the aerial.',
 'mayflower-school-douglas':'Register list coordinate, on the school building seen on the aerial.',
 'taku-glacier-lodge-twin-glacier-camp':'Register list coordinate, on the lodge clearing beside the buildings seen on the aerial.',
}
