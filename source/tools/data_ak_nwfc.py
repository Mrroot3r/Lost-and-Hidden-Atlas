# November 21, 2026: a first scatter across Alaska beyond Juneau: Sitka, Ketchikan, Haines, Dyea, Anchorage,
# Hatcher Pass, Talkeetna, Kenai, Kodiak, the Copper River, Fairbanks, Eagle and Unalaska. Ground taken with
# tools/choose.py --thinnest (Alaska had 21 places, all but one round Juneau).
# Sources read in this session: the Wikipedia articles (tools/wiki_raw.py) and the Register list for Skagway; the pages
# of Alaska State Parks (Independence Mine, Fort Abercrombie), the National Park Service (Sitka National Historical
# Park, Klondike Gold Rush National Historical Park), the Bureau of Land Management (Fort Egbert), the Orthodox Church
# in America's parish pages (Sitka, Kenai, Unalaska), the Kodiak History Museum, the Friends of Nike Site Summit,
# the Talkeetna Historical Society, Gold Dredge 8, the City of Cordova and the Alaska DOT&PF bridge 339 page.
# No source opened was a visit to an interior unless the entry says so.
from data_b import N
from data_ma import W
BATCH={'key':'ak_nwfc','label':'Alaska: a first scatter, Sitka to Unalaska','added':'2026-11-21 22:22'}

def NR(ref,label):
    return [label+' (National Register nomination)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/%s_text'%ref]
OCA_SIT=['Orthodox Church in America: St. Michael the Archangel Cathedral, Sitka','https://www.oca.org/parishes/OCA-AK-SITSMK']
OCA_KEN=['Orthodox Church in America: Holy Assumption of the Virgin Mary Church, Kenai','https://oca.org/parishes/OCA-AK-KENDVM']
OCA_UNA=['Orthodox Church in America: Holy Ascension of Our Lord Cathedral, Unalaska','https://oca.org/parishes/OCA-AK-UNAHAK']
NPS_RBH=['National Park Service: Russian Bishop\'s House','https://nps.gov/places/russian-bishops-house.htm']
NPS_RBH2=['National Park Service: tour the Russian Bishop\'s House','https://www.nps.gov/thingstodo/tour-russian-bishops-house.htm']
NPS_DYEA=['National Park Service: Dyea','https://www.nps.gov/klgo/learn/historyculture/dyea.htm']
ASP_IM=['Alaska State Parks: Independence Mine State Historical Park','https://dnr.alaska.gov/parks/aspunits/matsu/indepmineshp.htm']
ASP_FA=['Alaska State Parks: Fort Abercrombie State Historical Park','https://dnr.alaska.gov/parks/aspunits/kodiak/fortabercrombieshp.htm']
BLM_FE=['Bureau of Land Management: Fort Egbert National Historic Site','https://www.blm.gov/visit/fort-egbert-national-historic-site']
FONSS=['Friends of Nike Site Summit','https://www.nikesitesummit.net/']
FONSS2=['Friends of Nike Site Summit: about Site Summit','https://www.nikesitesummit.net/about-site-summit.html']
KHM=['Kodiak History Museum: hours and admission','https://kodiakhistorymuseum.org/visit']
THS=['Talkeetna Historical Society and Museum','https://www.talkeetnahistoricalsociety.org/']
GD8=['Gold Dredge 8','https://golddredge8.com/']
CORD=['City of Cordova: Copper River Highway bridge','https://www.cityofcordova.net/copper-river-highway-bridge-to-childs-glacier/']
DOT339=['Alaska DOT&PF: Copper River Highway bridge 339','https://dot.alaska.gov/nreg/bridge339/']

PLACES=[
N('st-michaels-cathedral-sitka','St. Michael\'s Cathedral','Sitka','ak','worship','standing',57.05005,-135.33534,'exact','open','walk','','1844–1848; rebuilt 1966–1976',
  'The cathedral of St. Michael the Archangel was built in 1844–1848 to the design of Innocent Veniaminov, later the first Bishop of Alaska, when Sitka was the capital of Russian America; it was the seat of the Orthodox diocese for all of North America until 1872. The log church burned on the night of January 2, 1966. Townspeople in a human chain carried out most of the icons and furnishings (the parish says over 95 per cent), and a copy was built on the same spot to the same measurements in concrete and steel, consecrated again in the 1970s.',
  'The rebuilt cathedral stands in the middle of Lincoln Street, which runs round it. Inside, the parish says, the walls are still lined with sailcloth, and the nave holds the icons saved in 1966, among them the Sitka Mother of God, and a bishop\'s chair made by Veniaminov himself; Wikipedia adds that the royal doors of the iconostasis and the chandelier were saved, while the hand-made bells and the tower clock were lost. Open to visitors in the cruise season, from the parish\'s page.',
  '',
  'Active Orthodox cathedral at 240 Lincoln Street, downtown Sitka. The parish page says it is open 9 a.m. to 4 p.m. from May to September when cruise ships are in, and that tours at other times are by appointment by telephone; services are as given. Hours from the Orthodox Church in America parish page, read November 2026. Street parking downtown; parking not checked on the ground.',
  [W('St. Michael\'s Cathedral (Sitka, Alaska)'),OCA_SIT],
  brick='no',hours='May to September 9 a.m. to 4 p.m. on cruise-ship days; other times by appointment. Saturday Vespers 5 p.m.; Sunday Hours 9 a.m., Divine Liturgy 9:30 a.m.'),

N('russian-bishops-house-sitka','Russian Bishop\'s House','Sitka','ak','landmark','standing',57.05144,-135.33118,'exact','open','walk','','1841–1843',
  'A two-storey log house built for the Russian Orthodox Church by the Russian-American Company in 1841–1843 (Wikipedia; a Park Service tour page says completed in 1842), one of the few buildings left from Russian America. It was the home and office of Ivan Veniaminov (St. Innocent), the first Bishop of Alaska, and housed Orthodox bishops until 1969. The National Park Service bought it in 1973 and spent fifteen years restoring it to how it looked in 1853; it is now part of Sitka National Historical Park.',
  'The log house of nine bays under a hip roof, with clapboard on the south front. The ground floor is a museum on Russian America; the upper floor is furnished as in the nineteenth century and is seen on a ranger-led tour, and its Chapel of the Annunciation is still used for services (Park Service pages). The Park Service notes uneven floors and dim light inside, and stairs to the upper floor.',
  '',
  'National Park Service, Sitka National Historical Park, 501 Lincoln Street, a short walk from the downtown docks. The Park Service page gives the season as spring, summer and fall, in the daytime, no reservations, and points to the park\'s hours page, which gave no times when read in November 2026 (a 2022 park notice had the house closed on most weekends). Hours not checked. Street parking; not checked on the ground.',
  [W('Russian Bishop\'s House'),NPS_RBH,NPS_RBH2],
  brick='no',hours='Spring, summer and fall, daytime (the park gives no fixed times on its page)'),

N('creek-street-ketchikan','Creek Street','Ketchikan','ak','town','standing',55.34239,-131.64197,'site','public','walk','','1903–1954',
  'A boardwalk on wooden pilings up the steep east bank of Ketchikan Creek, east of downtown. In 1903 a city ordinance moved the brothels out of the town centre to this side of the creek, and it was Ketchikan\'s red-light district until about 1954. The Star was one of the largest houses; Dolly\'s House is now a museum. Creek Street was listed on the National Register in 2014.',
  'The plank boardwalk and the frame houses on stilts over the creek. Whether Dolly\'s House museum is open, and when, was not checked; interiors not checked.',
  '',
  'A public boardwalk at the edge of downtown Ketchikan, open to walk at any time. Parking not checked; downtown Ketchikan is walkable from the cruise docks.',
  [W('Creek Street (Ketchikan, Alaska)')],
  brick='?'),

N('fort-william-h-seward-haines','Fort William H. Seward (Chilkoot Barracks)','Haines','ak','fort','standing',59.22694,-135.44389,'site','view','walk','','1902–1945',
  'The last of eleven army posts built in Alaska during the gold rush years, authorised in 1898 and built in 1902–1904 as 85 frame buildings round a parade ground at Port Chilkoot, half a mile from Haines. Renamed Chilkoot Barracks in 1922, it was the only army post in Alaska between 1925 and 1940. It closed in 1945 and was sold to the Port Chilkoot Company; the buildings became homes, art galleries and lodging, and the post is a National Historic Landmark (1978).',
  'The frame buildings of the post round the parade ground, on Fort Seward Drive and Parade Grounds Road. Which are open as galleries or lodging, and when, was not checked; interiors not checked.',
  '',
  'Now part of the City of Haines: the streets round the parade ground are public, the buildings are privately owned homes and businesses. Look from the street. Parking not checked.',
  [W('Fort William H. Seward'),['Haines Sheldon Museum: historical vignettes','https://sheldonmuseum.org/Vignettes/fortwilliamseward.htm']],
  brick='no'),

N('dyea-townsite','Dyea townsite','Skagway','ak','town','ruins',59.50777,-135.35833,'area','public','walk','stations','1897–1903',
  'Dyea was a boomtown of the Klondike Gold Rush of 1897–1898, where thousands landed to start up the Chilkoot Trail; it had two wharves, warehouses and a sawmill. Before the rush the Taiya River valley was a Tlingit fishing camp and the start of the Chilkat Tlingit trade route over the pass. Once the White Pass railway was built out of Skagway in 1898 the town emptied: the post office closed in 1902, and by 1903 fewer than half a dozen people lived there. Fires and floods in the 1940s and 1950s took most of what was left.',
  'The Park Service says many ruins remain at the old townsite but are hard to identify, and it is a major archaeological site; a self-guided tour leads through it. Slide Cemetery, with the graves of the Palm Sunday 1898 avalanche, is beside the townsite (mapped in OpenStreetMap; not read about in this session). Disturb nothing.',
  '',
  'National Park Service, Klondike Gold Rush National Historical Park, which bought most of the townsite in 1978; it has a self-guided townsite tour and a campground. Dyea Road runs about 9 miles from Skagway (distance not from a source read). The parking point is the lot OpenStreetMap maps at the Slide Cemetery trail; hours not checked.',
  [NPS_DYEA,W('Klondike Gold Rush National Historical Park')],
  th=[59.51015,-135.35888],thn='Slide Cemetery trail parking (OpenStreetMap)',brick='?'),

N('oscar-anderson-house-anchorage','Oscar Anderson House','Anchorage','ak','landmark','standing',61.21857,-149.90598,'exact','open','walk','','1915',
  'Built in 1915 by Oscar Anderson, who claimed to be the eighteenth person to set foot on what became Anchorage, it was the first wood-frame house in the town. Anderson lived in it until his death in 1974. It was restored to its 1915 look between 1978 and 1982 and opened as a house museum; it was listed on the National Register in 1978.',
  'A small frame house in Elderberry Park at the start of the Tony Knowles Coastal Trail. Interior not checked.',
  '',
  'A house museum in Elderberry Park, a city park at the west end of 5th Avenue. No page of the museum\'s own could be read in this session (the Municipality\'s historic preservation page answered 404): hours not checked. Parking not checked.',
  [W('Oscar Anderson House Museum')],
  brick='no',hours='?'),

N('nike-site-summit-anchorage','Nike Site Summit','Anchorage','ak','fort','ruins',61.24817,-149.5478,'site','permit','walk','','1957–1979',
  'A Nike-Hercules anti-aircraft missile battery on a Chugach mountaintop, built in 1957–1958 and armed in 1959, one of three Nike sites that guarded Anchorage and its bases. From 1960 to 1963 it fired unarmed practice missiles once a year. It was decommissioned in 1979, with the site in Key West the last two in the nation, and the army left it in the 1980s. Listed on the National Register in 1996, it is one of the best preserved Nike-Hercules sites in the state.',
  'The battery control area, the missile launch area with its launch control building, and the magazines (Wikipedia). The Friends of Nike Site Summit have put a Nike-Hercules missile on display there and signs along the tour route. Interiors not checked.',
  '',
  'On Joint Base Elmendorf-Richardson, at the eastern edge of the old Fort Richardson beside Chugach State Park and the Arctic Valley ski area: military land, not open to wander. The Friends of Nike Site Summit run tours and hikes in summer; their page says the next year\'s dates are usually announced in late March. Tour arrangements not checked further.',
  [W('Site Summit'),FONSS,FONSS2],
  brick='?'),

N('independence-mine-hatcher-pass','Independence Mine','Hatcher Pass','ak','industry','ruins',61.79022,-149.2857,'site','open','walk','','1897–1950',
  'The second largest hard-rock gold mine in Alaska, high in the Talkeetna Mountains above Palmer. Claims were worked here from at least 1897; the Wasilla Mining Company ran the mines from 1934 to 1943 and from 1948 to 1950, with a camp of up to sixteen frame buildings joined by covered wooden passages. The company meant to come back and never did, so much of the camp and its machinery was left as it stood. The land was given to the state in 1980 and is a state historical park.',
  'The camp buildings and mining machinery, which Wikipedia says the weather has hurt badly; some buildings stand and some have fallen. Alaska State Parks lists an assay office with displays on assaying and retorting, guided history tours and a gift shop in Bunkhouse No. 2. Gold panning with pan and shovel only.',
  '',
  'Alaska State Parks, at Mile 17.3 of Hatcher Pass Road (from Palmer by the Palmer-Fishhook Road). Run under contract by Salmon Berry Travel & Tours. Daily parking fee. The gate to the upper lot is open 9 a.m. to 7 p.m.; outside those hours walk up from the lower lot (the state\'s page names the Independence Bowl parking area). Hours from the Alaska State Parks page, read November 2026.',
  [W('Independence Mines, Alaska'),ASP_IM,NR('74000440','Independence Mines')],
  brick='?',hours='Visitor centre daily June 18 to September 30; upper gate 9 a.m. to 7 p.m., tours 10 a.m. to 6 p.m.; walk-in from the lower lot outside those hours'),

N('talkeetna-historic-district','Talkeetna Historic District','Talkeetna','ak','town','standing',62.32246,-150.11388,'site','public','walk','','1916–1940',
  'Talkeetna was set up in 1916 as a construction headquarters of the Alaska Railroad and became a home for miners once the line was finished. The historic district covers a few blocks of Main Street and C and D Streets, with three buildings from the railroad\'s construction years and ten more from before 1940, most of them one or two storeys, frame or log.',
  'Among them the Fairview Inn, the town\'s first schoolhouse (now the Talkeetna Historical Society museum) and the Talkeetna Roadhouse, built as a log house in 1917 and enlarged as a roadhouse in the 1940s (Wikipedia). The museum has a walking tour app. Interiors other than the museum not checked.',
  '',
  'Public streets in the village. The Talkeetna Historical Society museum on D Street gave its winter hours on its page, and summer hours of 9 a.m. to 5 p.m. daily until September 15; read November 2026. Parking not checked.',
  [W('Talkeetna Historic District'),THS],
  brick='no'),

N('holy-assumption-church-kenai','Holy Assumption of the Virgin Mary Church','Kenai','ak','worship','standing',60.55291,-151.26771,'exact','open','walk','','1895–1896',
  'A log church in Old Town Kenai, built to replace the first church of 1849 with a grant from the Holy Synod in St. Petersburg; the parish says 1895, Wikipedia that it was completed in 1896. Wikipedia calls it the oldest standing Russian Orthodox church in Alaska. The parish was founded in 1845 by the monk Nikolai Militov, who served it for 22 years. The church, its rectory, cemetery and the 1906 St. Nicholas Chapel were made a National Historic Landmark in 1970.',
  'A log church in the Pskov style, shaped like a ship, with an elaborate iconostasis inside (Wikipedia). Across the street on the bluff over the Kenai River mouth stands the small St. Nicholas Chapel. The rectory\'s date is given two ways: 1881 by Wikipedia, 1887 by the parish; both call it the oldest building in the area.',
  '',
  'Active Orthodox parish at 1105 Mission Avenue in Old Town Kenai. Services from the Orthodox Church in America parish page, read November 2026; whether it opens outside services was not checked. Parking not checked.',
  [W('Holy Assumption of the Virgin Mary Church'),OCA_KEN,['National Park Service: Holy Assumption Orthodox Church','https://www.nps.gov/places/holy-assumption-orthodox-church.htm']],
  conf='mixed',brick='no',hours='Saturday Vigil 6 p.m.; Sunday Hours 8:40 a.m., Divine Liturgy 9 a.m.'),

N('kodiak-history-museum-erskine-house','Russian-American Magazin (Erskine House), Kodiak History Museum','Kodiak','ak','landmark','standing',57.78767,-152.40341,'exact','open','walk','','c. 1808',
  'Kodiak was founded in 1793 as Pavlovsk, the first lasting Russian settlement in North America and the capital of Russian America until 1808. This log warehouse (magazin) was built by the Russian-American Company in the first decade of the nineteenth century and is the oldest of four buildings left from Russian rule. W. J. Erskine bought it in 1911 as his home. It is a National Historic Landmark (1962) and now holds the Kodiak History Museum, run by the Kodiak Historical Society, which reopened with new exhibits in 2019.',
  'A large two-storey log building on a concrete foundation, with a partly glazed front porch (Wikipedia). Exhibits on the Kodiak islands and the Aleutians in the Russian and early American years.',
  '',
  'Kodiak History Museum, 101 East Marine Way, downtown Kodiak. Admission 10 dollars for adults, children under 18 free. Hours from the museum\'s page, read November 2026. Parking not checked.',
  [W('Kodiak History Museum'),KHM],
  brick='no',hours='Wednesday, Thursday and Saturday 10 a.m. to 4 p.m.; Friday noon to 7 p.m.'),

N('fort-abercrombie-kodiak','Fort Abercrombie','Kodiak','ak','fort','ruins',57.83111,-152.35583,'site','public','walk','forts','1941–1945',
  'A Second World War coast defence on Miller Point, north-east of Kodiak, built in 1941 and abandoned after the war without having fired in anger. It is part of the Kodiak Naval Operating Base and Forts Greely and Abercrombie National Historic Landmark. The state made it a park in 1969.',
  'Gun emplacements, underground magazines and the foundations of buildings, among cliffs, spruce forest, meadows and a trout lake (Wikipedia; Alaska State Parks). Bring a light for the magazines if they are open; whether they are was not checked.',
  '',
  'Alaska State Parks, 1400 Abercrombie Drive, off Rezanof Drive about 3.5 miles past the four-way light coming from the airport. Day use, a small tent campground (first come, first served) and two cabins; roads are narrow and rough for vehicles over 20 feet. The parking point is the lot OpenStreetMap maps on Abercrombie Drive in the park. Hours not given on the state\'s page.',
  [W('Fort Abercrombie State Historical Park'),ASP_FA],
  th=[57.83063,-152.36055],thn='Abercrombie Drive lot, Fort Abercrombie State Historical Park',brick='?'),

N('million-dollar-bridge-cordova','Million Dollar Bridge (Miles Glacier Bridge)','Cordova','ak','rail','standing',60.67305,-144.74579,'exact','boat','boat','','1909–1910',
  'A steel Pennsylvania-truss bridge of four spans, about 1,550 feet in all, built in 1909–1910 across the Copper River between Miles and Childs glaciers for the Copper River and Northwestern Railway, which carried copper ore from Kennecott to Cordova. It cost 1.4 million dollars. The railway closed in 1938; the bridge was turned into a road bridge in 1958. The 1964 earthquake knocked span 4 off its pier, and it was propped up with cables, beams and planks.',
  'The four truss spans over the river, with the dropped and patched fourth span (Wikipedia).',
  '',
  'The Copper River Highway ends at the bridge, but the state closed it at Mile 36 because bridge 339 there failed (scoured riverbed, found 2011); the City of Cordova says the closure lasts until that bridge is replaced, and the state\'s project page says the replacement was dropped for lack of money. Wikipedia: reached only by jet boat up the Copper River or by boat down from Chitina. The city says a local business holds a Forest Service permit to take people there for a fee; the Cordova Ranger District has details.',
  [W('Miles Glacier Bridge'),CORD,DOT339],
  brick='no'),

N('gold-dredge-8-fairbanks','Goldstream Dredge No. 8','Fox','ak','industry','standing',64.94157,-147.65876,'site','open','drive','','1928–1959',
  'A ladder dredge worked by the Fairbanks Exploration Company from 1928 to 1959 north of Fairbanks, on water brought in by the 90-mile Davidson Ditch. It cut a track 4.5 miles long and, by Wikipedia\'s figure, brought up 7.5 million ounces of gold. It was listed on the National Register as a historic district in 1984 and named a Historic Mechanical Engineering Landmark in 1986.',
  'The dredge itself, with a mining museum. The operator\'s two-hour tour rides a replica of the Tanana Valley Railroad, includes gold panning and a close look at the dredge.',
  '',
  'A private attraction at 1803 Old Steese Highway North, between Fairbanks and Fox. Wikipedia says tours run in summer for a fee; the operator\'s page sells tours and did not give hours when read in November 2026. The parking point is the lot OpenStreetMap maps beside it.',
  [W('Goldstream Dredge No. 8'),GD8],
  th=[64.94188,-147.65801],thn='Gold Dredge 8 parking, Old Steese Highway',brick='?',hours='?'),

N('fort-egbert-eagle','Fort Egbert','Eagle','ak','fort','standing',64.78928,-141.2133,'site','public','walk','forts','1899–1911',
  'An army post set up in 1899, during the Klondike rush, beside Eagle Bluff on the Yukon River a few miles from Canada; Eagle was under its rule until 1900. It was the first station of the Washington-Alaska Military Cable and Telegraph System, linked to Dawson City in 1900 and to Valdez in 1902, and Roald Amundsen telegraphed the news of his Northwest Passage crossing from here in 1905. The fort was left in 1911, but a Signal Corps station stayed until 1925.',
  'Five restored buildings of the fort, with exhibits and an interpretive trail (Bureau of Land Management). Part of the Eagle Historic District National Historic Landmark. Interiors not checked.',
  '',
  'Bureau of Land Management with the Eagle Historical Society and Museums; no fee for the fort, and a 12-dollar BLM campground next to it. Eagle is at the end of the Taylor Highway, 163 miles north of Tetlin Junction near Tok (BLM). Hours of the buildings not checked; the BLM Eastern Interior Field Office in Fairbanks answers questions.',
  [W('Fort Egbert'),BLM_FE,W('Eagle, Alaska')],
  brick='?'),

N('holy-ascension-cathedral-unalaska','Church of the Holy Ascension','Unalaska','ak','worship','standing',53.87547,-166.53633,'exact','open','walk','','1894–1896',
  'Unalaska\'s Orthodox cathedral, one of the oldest churches in Alaska, on a site used for a church since 1808 (parish). Ivan Veniaminov, later St. Innocent, served here for ten years from 1824 and built the 1825 chapel. The present wood-frame church is dated two ways: Wikipedia says built in 1894, its alterations 1894 to 1896, while the parish says 1896. It was restored in the 1990s (the parish says 1996, Wikipedia 1998) and is a National Historic Landmark.',
  'A cruciform frame church with a 52-foot bell tower and green onion dome, red-painted shingle roofs and red-painted floors (Wikipedia). The parish says the interior is the original, believed to keep the iconostasis of the 1808 chapel and another from the 1825 chapel, and its icons are being restored a few at a time. The bishop\'s house stands nearby. Whether it opens outside services was not checked.',
  '',
  'Active Orthodox cathedral of the Aleutian Deanery at 265 West Broadway Avenue, Unalaska (address from OpenStreetMap). Unalaska is reached by air from Anchorage or the summer ferry from Homer (parish). Services from the Orthodox Church in America parish page, read November 2026; the parish gives a telephone number for other services. Parking not checked.',
  [W('Church of the Holy Ascension'),OCA_UNA],
  conf='mixed',brick='no',hours='Saturday Vigil 6:30 p.m.; Sunday Hours and Liturgy 9:30 a.m. (8:30 a.m. in summer)'),
]

PIN_NOTES={
'st-michaels-cathedral-sitka':'OpenStreetMap place of worship at 240 Lincoln Street (nom.py), within 30 m of the Wikipedia point.',
'russian-bishops-house-sitka':'ArcGIS PointAddress for 501 Lincoln Street, Sitka; 15 m from the Register point.',
'creek-street-ketchikan':'OpenStreetMap footway named Creek Street (nom.py), on the boardwalk; the street is long, so site precision.',
'fort-william-h-seward-haines':'Wikipedia coordinate for the district, by Fort Seward Drive and Parade Grounds Road (osmnear.py).',
'dyea-townsite':'OpenStreetMap Dyea Historic Townsite Road (nom.py); the ruins are scattered and the Park Service does not map them, so area precision. Parking from parking.py.',
'oscar-anderson-house-anchorage':'OpenStreetMap building "Oscar Anderson House" (nom.py), matching Wikipedia within 20 m.',
'nike-site-summit-anchorage':'Moved with pix.py onto the missile launch area (pads and buildings plain on a 3 km aerial), 40 m from the OpenStreetMap point of the launch area ruins; the Wikipedia point fell on bare tundra 650 m north-east. The control area is on the summit about 1.3 km north-east.',
'independence-mine-hatcher-pass':'OpenStreetMap museum point "Independence Mine" on Gold Cord Road (nom.py), in the camp, 30 m from the Wikipedia point.',
'talkeetna-historic-district':'OpenStreetMap point of the Talkeetna Historical Society Museum on D Street (nom.py), inside the district.',
'holy-assumption-church-kenai':'OpenStreetMap place of worship at 1105 Mission Avenue (nom.py).',
'kodiak-history-museum-erskine-house':'OpenStreetMap museum point (nom.py), matching the Wikipedia point within 15 m.',
'fort-abercrombie-kodiak':'Wikipedia coordinate for the park on Miller Point; the batteries are spread over the point. Parking from parking.py.',
'million-dollar-bridge-cordova':'OpenStreetMap bridge "Miles Glacier Bridge" (nom.py), same as Wikipedia.',
'gold-dredge-8-fairbanks':'OpenStreetMap attraction point "Gold Dredge #8" on the Old Steese Highway (nom.py); the Wikipedia point is 500 m south. Parking from parking.py.',
'fort-egbert-eagle':'Wikipedia point fell on an open field; moved with pix.py 55 m to the row of long frame buildings south of it on the aerial, taken to be the fort\'s (which building is which not checked).',
'holy-ascension-cathedral-unalaska':'OpenStreetMap place of worship at 265 West Broadway Avenue (nom.py), same as Wikipedia within 15 m.',
}
