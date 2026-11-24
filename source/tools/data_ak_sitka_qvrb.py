# November 24, 2026: Sitka, Alaska (City and Borough of Sitka). Alaska had 51 places, two of them in Sitka
# (St. Michael's Cathedral and the Russian Bishop's House). Ground: Alaska drawn with tools/choose.py --state ak.
# Sources read in this session: the Wikipedia Register list for Sitka and the articles named in each entry; the pages
# of Alaska State Parks (Fort Rousseau Causeway, Old Sitka, Baranof Castle), the National Park Service (Sitka National
# Historical Park brochure and 2025 compendium, the Totem Trail, the park history, and the "places" pages for the
# landmarks), Alaska State Museums (Sheldon Jackson Museum), Sitka Fine Arts Camp, the parish of St. Peter's
# by-the-Sea, the Department of Veterans Affairs (Sitka National Cemetery), HMdb, Visit Sitka, the Society of
# Architectural Historians, the Living New Deal and the Daily Sitka Sentinel. Nothing was checked on the ground.
from data_b import N
from data_ma import W
BATCH={'key':'ak_sitka_qvrb','label':'Alaska: Sitka','added':'2026-11-24 01:02'}

def NR(ref,label):
    return [label+' (National Register nomination)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/%s_text'%ref]
ASP_FR=['Alaska State Parks: Fort Rousseau Causeway State Historical Park','https://dnr.alaska.gov/parks/aspunits/southeast/ftrousseau.htm']
ASP_OS=['Alaska State Parks: Old Sitka State Historical Park','https://dnr.alaska.gov/parks/aspunits/southeast/oldsitkaahp.htm']
ASP_BC=['Alaska State Parks: Baranof Castle State Historic Site','https://dnr.alaska.gov/parks/aspunits/southeast/baranofcastle.htm']
NPS_NOB=['National Park Service: Sitka Naval Operating Base and U.S. Army Coastal Defenses','https://home.nps.gov/places/sitka-naval-operating-base-and-us-army-coastal-defenses.htm']
NPS_BC=['National Park Service: Baranof Castle State Historic Site','https://www.nps.gov/places/baranof-castle-state-historic-site.htm']
NPS_B29=['National Park Service: Russian-American Building No. 29','https://www.nps.gov/places/russian-american-building-no-29.htm']
NPS_ANB=['National Park Service: Alaska Native Brotherhood Hall','https://www.nps.gov/places/alaska-native-brotherhood-hall.htm']
NPS_SJ=['National Park Service: Sheldon Jackson School','https://www.nps.gov/places/sheldon-jackson-school.htm']
NPS_TT=['National Park Service: Take the Totem Trail','https://www.nps.gov/thingstodo/sitk-totem-trail.htm']
NPS_PH=['National Park Service: Sitka National Historical Park history','https://www.nps.gov/sitk/learn/historyculture/park-history.htm']
NPS_BR=['National Park Service: Sitka National Historical Park brochure (hours)','https://www.nps.gov/sitk/planyourvisit/park-brochure.htm']
VS_B29=['Visit Sitka: Building 29','https://visitsitka.org/member/building-29']
VS_ANB=['Visit Sitka: ANB Hall','https://visitsitka.org/?p=608']
VS_PMG=['Visit Sitka: Princess Maksoutoff\'s grave','https://visitsitka.org/?p=693']
SJM_H=['Alaska State Museums: Sheldon Jackson Museum hours and admission','https://museums.alaska.gov/sheldon_jackson/sjhours.html']
SJM_HI=['Alaska State Museums: Sheldon Jackson Museum history','https://museums.alaska.gov/sheldon_jackson/sjhistory.html']
SFAC=['Sitka Fine Arts Camp: the historic campus','https://www.fineartscamp.org/historic-campus.html']
STP=['St. Peter\'s by-the-Sea Episcopal Church','https://stpeters-sitka.org/']
STP2=['St. Peter\'s by-the-Sea: church happenings (service times)','https://stpeters-sitka.org/church-happenings']
SAH_PH=['Society of Architectural Historians (SAH Archipedia): Sitka Pioneers\' Home','https://sah-archipedia.org/buildings/AK-01-SE050']
LND_PH=['Living New Deal: Sitka Pioneers\' Home','https://livingnewdeal.org/projects/sitka-pioneers-home/']
LND_CH=['Living New Deal: City Hall (old federal building), Sitka','https://livingnewdeal.org/projects/city-hall-old-federal-building-sitka-ak/']
VA_SNC=['Department of Veterans Affairs: Sitka National Cemetery','https://www.cem.va.gov/cems/nchp/Sitka.asp']
HMDB_PM=['HMdb: In Appreciation (Lutheran cemetery, Sitka)','https://www.hmdb.org/m.asp?m=308264']
SENT_WC=['Daily Sitka Sentinel: Woman\'s Club building listed on National Register','https://sitkasentinel.com/2012-05-10-22-08-10/24890-woman-s-club-building-listed-on-national-register']
HP_WC=['HistoryPointer: Sitka Woman\'s Club Building','https://historypointer.com/nris/resource/100010895']

PLACES=[
N('sitka-naval-operating-base-fort-rousseau','Sitka Naval Operating Base and Fort Rousseau (Makhnati Island)','Sitka','ak','fort','ruins',57.0395,-135.3896,'area','boat','boat','forts','1939–1944',
  'The Navy built an air station on Japonski Island, across the channel from Sitka, from 1939; it was commissioned on October 1, 1939. In March 1941 the Army began coastal batteries on Makhnati Island, at the end of a causeway that runs from Japonski through a string of small islands (8,100 feet long, the National Park Service says). Fort Rousseau held two 6-inch guns, two 155 mm guns, magazines and a command post, but the batteries were finished only after Attu and Kiska were retaken, never fired in war, and the Army left Sitka in spring 1944. The bases are a National Historic Landmark district (1986), and the Makhnati end is Fort Rousseau Causeway State Historical Park, made in 2008 by the state park page (about 2007 by the National Park Service).',
  'Alaska State Parks lists ammunition magazines, lookouts, gun emplacements and the headquarters command centre on the island; Wikipedia calls the Army sites little more than foundations and concrete structures. The Navy hangars, ramps, control tower and piers on Japonski are gone. The pin marks Makhnati Island; the single batteries were not placed. Not checked on the ground.',
  'A Second World War coastal fort that never fired a shot, on an island you reach only by boat.',
  'Alaska State Parks manages the 60-acre state historical park. Its page says there is no road access: the island lies west of the airport runway and is reached by a short boat ride or kayak, and the park is undeveloped, with no visitor facilities. No page read gives hours, fees or the state of the old concrete.',
  [W('Sitka Naval Operating Base and U.S. Army Coastal Defenses'),ASP_FR,NPS_NOB],conf='mixed',brick='no'),
N('old-sitka-redoubt-st-michael','Old Sitka (Redoubt St. Archangel Michael site)','Sitka','ak','fort','marker',57.12955,-135.37342,'area','public','walk','forts','1799–1802',
  'In 1799 the Russian-American Company under Alexander Baranov built log buildings inside a palisade here, the Redoubt of St. Archangel Michael. Tlingit warriors attacked and destroyed it in 1802, and when the Russians came back in 1804 they settled on Castle Hill, in today\'s Sitka, instead. The ground was dug by archaeologists in 1934–35, named a National Historic Landmark in 1962 and made a state park in 1966.',
  'Nothing of the redoubt stands; Wikipedia says the site is now of archaeological interest and has been partly damaged by erosion and building. The state park has interpretive panels, a boat launch and dock, and two trails: the Forest Muskegs trail, 1.25 miles, barrier-free with a self-guiding brochure, and the Mosquito Cove trail, 1.5 miles through spruce and hemlock.',
  '',
  'Alaska State Parks, Old Sitka State Historical Park, on Halibut Point Road about seven miles north of downtown Sitka (milepost 7.5 on the state page, mile 6.9 by Wikipedia), within walking distance of the state ferry terminal and Starrigavan Campground. Toilets and trails are listed as accessible. The pin is the park\'s loop by the boat launch, where you park. The state page gives no hours; the boat launch has a fee on a page not read here. Hours not checked.',
  [W('Old Sitka Site'),ASP_OS],conf='mixed',brick='no'),
N('castle-hill-baranof-castle-sitka','Castle Hill (Baranof Castle State Historic Site)','Sitka','ak','fort','marker',57.04870,-135.33803,'exact','public','walk','forts','1804–1867',
  'The rock hill above the harbour was the Tlingit site Noow Tlein before Alexander Baranov took it in 1804 (the Tlingit gave it up formally in 1804 by Wikipedia, in 1805 by the National Park Service), and from then until 1867 it was the seat of the Russian-American Company and of Russian America. A two-storey brick governor\'s house with a cupola, built in 1836, stood on top until it burned in 1894. Alaska was handed over to the United States in a ceremony on the hill in 1867, and the first 49-star flag in Alaska was raised here in 1959. It became a National Historic Landmark in 1962.',
  'The rock, about 60 feet high, with a flat top reached by a walkway; a stone parapet of 1965, six cannons, a flagpole and interpretive panels. Nothing of the Russian buildings stands. Fill laid in 1968 set the hill back from the water.',
  'Where Russia handed Alaska to the United States.',
  'Alaska State Parks state historic site, downtown at Harbor Road and Lincoln Street. The state page says a fully accessible walkway leads to the top and there is no fee; it gives no hours. Parking not checked.',
  [W('Castle Hill (Sitka, Alaska)'),ASP_BC,NPS_BC],conf='mixed',brick='no'),
N('russian-american-building-29-sitka','Russian-American Building No. 29 (Tilson Building)','Sitka','ak','landmark','standing',57.04965,-135.33629,'site','view','walk','','about 1850 (sources give 1835 to 1852)',
  'A two-storey log house built by the Russian-American Company to house its workers. Its date is not settled: Wikipedia gives the 1840s and 1850, the National Park Service 1852, Visit Sitka 1835. An addition of the 1880s lengthened the gallery and roof; the house was modernised in the 1960s, partly because the logs were decaying, and rehabilitated in the mid-1980s. It became a National Historic Landmark in 1987.',
  'Hewn spruce logs squared to about 18 inches, on a stone foundation, under shiplap siding of the kind seen in early pictures, with a gallery on the east side and four dormers. The National Park Service says a section of the outside log wall is left open to show the original hand-hewn logs, nails and builders\' marks. The Park Service lists it as private and not open to the public; Visit Sitka lists a business there, the Log Cache, at 206 Lincoln Street. Interior not checked.',
  'One of the Russian-era log buildings still standing on Sitka\'s main street.',
  'Privately owned, on Lincoln Street in downtown Sitka: look from the street. Parking not checked.',
  [W('Russian-American Building No. 29'),NPS_B29,VS_B29],conf='mixed',brick='no'),
N('st-peters-by-the-sea-sitka',"St. Peter's by-the-Sea Episcopal Church",'Sitka','ak','worship','standing',57.05152,-135.32799,'site','open','walk','','1899',
  'A Gothic Revival Episcopal church designed by H. Louis Duhring Jr. of Philadelphia and built by John W. Dudley. The cornerstone was laid on June 29, 1899, the first service held on November 26, 1899, and the church consecrated on April 15, 1900. It has been on the National Register since 1978, as has the See House, the bishop\'s house behind it.',
  'Fieldstone walls and buttresses rise to about nine feet, with shingled wood framing above. The Register form describes oiled spruce inside, open roof trusses, stained-glass windows and door and a nine-panel pointed window over the altar; Wikipedia says the rose window includes a Star of David. The parish says the church is open daily for quiet reflection and prayer; it repaired the stone buttresses in 2024 and says the sanctuary needs a new roof.',
  '',
  'The parish of St. Peter\'s by-the-Sea, 611 Lincoln Street; hours from the parish\'s own pages (Wednesday noon prayer is online only). Parking not checked.',
  [W("St. Peter's by-the-Sea Episcopal Church (Sitka, Alaska)"),NR('78000538',"St. Peter's Church"),STP,STP2],brick='no',
  hours='Open daily for prayer; Sunday service 9 a.m.'),
N('alaska-native-brotherhood-hall-sitka','Alaska Native Brotherhood Hall','Sitka','ak','civic','standing',57.05070,-135.34125,'exact','view','walk','','1914',
  'The Alaska Native Brotherhood built this hall in 1914 for Sitka Camp No. 1, the organisation\'s first chapter. Wikipedia says it was probably enlarged later, with the front quarter added and the roof raised to two storeys. It is a National Historic Landmark: 1987 by Wikipedia, 1978 by the National Park Service\'s page.',
  'A two-storey wooden Craftsman hall about 40 by 60 feet, most of it standing on pilings over the water: shingles on the lower storey and the gable ends, clapboard above, exposed rafter ends and brackets. Inside, by Wikipedia and the Park Service, is an open two-storey hall with a stage over the water and a gallery round it. The Park Service says it is open to the public for social events and community activities; no times were found. Interior not checked.',
  '',
  'The Alaska Native Brotherhood and Sisterhood Grand Camp manages it (National Park Service), at 235 Katlian Street. Look from the street, or go in when it holds a public event.',
  [W('Alaska Native Brotherhood Hall'),NPS_ANB,VS_ANB],conf='mixed',brick='no'),
N('sheldon-jackson-museum-sitka','Sheldon Jackson Museum','Sitka','ak','civic','standing',57.05054,-135.32252,'site','open','walk','','1895–1897',
  'Built in 1895–97 on the Sheldon Jackson School grounds, it is Alaska\'s oldest museum and, the state says, the first concrete building in Alaska. It has been on the National Register since 1972, and the State of Alaska bought it in the mid-1980s.',
  'The 1890s concrete building still houses the museum, run by Alaska State Museums. The displays and the inside of the building were not checked here.',
  '',
  'Alaska State Museums, 104 College Drive. Admission from the state page: in summer $7, seniors $6, in winter $5 and $4, aged 18 and under free. The state pages also carried a notice, with no year, that the museum was closed "through December 1" for heating and ventilation work, and the hours page was last updated in 2020: check before you go.',
  [W('Sheldon Jackson College'),SJM_H,SJM_HI],conf='mixed',brick='no',
  hours='May 6 to Oct 3 daily 9 a.m. to 4:30 p.m.; winter Wednesday to Saturday noon to 4 p.m.; closed holidays'),
N('sheldon-jackson-school-campus-sitka','Sheldon Jackson School (college campus)','Sitka','ak','inst','standing',57.05095,-135.32372,'site','view','walk','','1884–2007',
  'A Presbyterian mission school for Alaska Native students, founded in 1878 and moved to this site in 1884; it was renamed for the Rev. Sheldon Jackson after 1910, added a high school in 1917 (closed 1967) and college classes in the 1940s, and closed as Sheldon Jackson College in 2007. The main buildings of 1910–11 were designed by Ludlow and Peabody (of New York by the Sitka Fine Arts Camp, of Boston by Wikipedia). It became a National Historic Landmark in 2001, and in 2011 the campus passed to Alaska Arts Southeast, parent of the Sitka Fine Arts Camp, which repaired failing siding and roofs.',
  'Wood-shingled Craftsman halls round a green: Stevenson Hall, North Pacific Hall, the Richard H. Allen Memorial, Whitmore Hall, Fraser Hall, and the power plant and laundry, 17 contributing buildings by the National Park Service (18 by Wikipedia). They were white at first and are brown now. Other tenants include Outer Coast College and the Sitka Sound Science Center. Interior not checked.',
  '',
  'Managed by the Sitka Fine Arts Camp, 801 Lincoln Street. No page read says whether visitors may walk the grounds: look from Lincoln Street. The Sheldon Jackson Museum on the same grounds is a separate place, open to visitors.',
  [W('Sheldon Jackson College'),NPS_SJ,SFAC],conf='mixed',brick='no'),
N('sitka-pioneer-home',"Sitka Pioneers' Home",'Sitka','ak','inst','standing',57.05009,-135.33778,'exact','view','walk','','1934–1935',
  'The state\'s home for elderly Alaskans opened here in September 1913, the oldest of Alaska\'s Pioneer Homes. The present concrete building went up in 1934–35 with Public Works Administration help, designed by Heath, Gove and Bell of Tacoma. It has been on the National Register since 1979 and is still an assisted-living home run by the state.',
  'A large building with yellow-painted stucco walls, a red-tile hip roof and a sun porch across the front (SAH Archipedia). In front stands Alonzo Victor Lewis\'s statue The Prospector, dedicated on Alaska Day 1949. Wikipedia says the free Alaska Day reception is held inside; otherwise no visiting hours were found.',
  '',
  'State of Alaska, Division of Pioneer Homes, 120 Katlian Street. People live here: see it and the statue from the street.',
  [W('Sitka Pioneer Home'),SAH_PH,LND_PH],conf='mixed',brick='no'),
N('sitka-post-office-court-house','Sitka U.S. Post Office and Court House (City Hall)','Sitka','ak','civic','standing',57.04899,-135.33855,'site','view','walk','','1936–1938',
  'A Moderne federal building of poured concrete, designed by Gilbert Stanley Underwood and built in 1936–38 by the J. B. Warrack Company, in place of a wooden building that burned in 1936. The post office used the first floor from 1963 and left in 1986; the City of Sitka has used it as City Hall since 1993. It has been on the National Register since 1997.',
  'A plain concrete block on a raised basement with simple Art Deco details; the main entrance was moved down to the basement level. Interior not checked.',
  '',
  'City of Sitka, City Hall, 100 Lincoln Street. The city offices\' opening hours were not checked.',
  [W('Sitka United States Post Office and Court House'),LND_CH],brick='no'),
N('sitka-national-historical-park-fort-site','Sitka National Historical Park: Totem Trail and the 1804 fort site','Sitka','ak','fort','marker',57.04888,-135.31596,'area','public','walk','forts','1804',
  'At the mouth of Indian River stood Shis\'kí Noow, the fort of the Kiks.ádi Tlingit, where they fought Russian fur hunters and their Aleut allies in 1804. President Benjamin Harrison set the ground aside as a park in 1890, it became a national monument in 1910 and passed to the National Park Service in 1916; it took its present name in 1972. The Park Service calls it the oldest federally designated park in Alaska.',
  'The Totem Trail, a flat crushed-gravel loop of 30 to 90 minutes through the forest, with Haida and Tlingit totem poles from several villages; the Park Service says several are new or second-generation poles, and Wikipedia says many copy originals kept in storage. Midway a grassy field, a modern pole and a marker at the Kiks.ádi Memorial mark the fort and battle site, with wayside signs. Wikipedia gives two miles of paths in 112 acres.',
  'The battleground of 1804, in a forest of totem poles.',
  'National Park Service; the park\'s address is 103 Monastery Street and the trail starts at the visitor centre. Hours from the park brochure and the 2025 compendium; older park news releases give other winter visitor-centre hours. The visitor centre lots close when the grounds close, there is no overnight parking, and the upper lot is kept for tour buses in the day from May to September. Leashed pets are allowed on the trails, not indoors. The pin is in the park near Indian River, not on the battle field itself.',
  [W('Sitka National Historical Park'),NPS_TT,NPS_PH,NPS_BR],brick='no',th=[57.04922,-135.31946],thn='Visitor centre car park (from the aerial)',
  hours='Grounds 6 a.m. to 10 p.m. May 15 to Sept 30, 7 a.m. to 8 p.m. Oct to May 14; visitor centre daily 8 a.m. to 5 p.m. mid-May to Sept'),
N('sitka-national-cemetery','Sitka National Cemetery','Sitka','ak','burial','standing',57.05440,-135.32371,'site','public','walk','cemeteries','1924',
  'The Department of Veterans Affairs says General Jefferson C. Davis laid out the burial ground in the late 1800s, and President Calvin Coolidge made it Sitka National Cemetery by executive order in June 1924. It covers 4.3 acres and has been on the National Register since 2012.',
  'Rows of graves on a slope below Mount Verstovia. The VA names among the burials Governor James Green Brady (Section R), and two cannons stand as memorials.',
  '',
  'Department of Veterans Affairs, 803 Sawmill Creek Road, at the Observatory Way junction about 1.5 miles from the airport bridge; looked after from Fort Richardson National Cemetery. Hours from the VA page.',
  [W('Sitka National Cemetery'),VA_SNC],brick='?',
  hours='Monday to Friday 8 a.m. to 5 p.m.; weekends and holidays 7 a.m. to 7 p.m.; winter dawn to dusk'),
N('princess-maksoutoff-grave-sitka',"Princess Maksoutoff's grave (Lutheran cemetery)",'Sitka','ak','burial','standing',57.05120,-135.33796,'site','public','walk','cemeteries','1840',
  'A marker at the cemetery says the Lutheran cemetery was begun in 1840. In it lies the first wife of Dimitrii Maksoutoff, the last Russian governor of Alaska; her grave marker says she was born in 1834 and died on December 18, 1862. Foster Mills found the overgrown grave in 1924 and kept it for more than 25 years, Russell and Monica Mills after him, until Sitka Lutheran Church took it over in 1992.',
  'The princess\'s grave and its marker, and a marker thanking the Mills family, in the Lutheran cemetery behind the Pioneers\' Home. The other graves were not described by any source read.',
  '',
  'On Princess Way north of Seward Street (HMdb), behind the Pioneers\' Home (Visit Sitka); in the care of Sitka Lutheran Church since 1992 by the marker. No hours found.',
  [HMDB_PM,VS_PMG],brick='?'),
N('sitka-womans-club-building',"Sitka Woman's Club Building",'Sitka','ak','civic','standing',57.0493,-135.3343,'exact','view','walk','','1897',
  'A one-storey wooden cottage of 1,176 square feet, known as the Cottage by the Sea, built in 1897 by Hans Christian Pande. The Mills family deeded it to the Sitka Woman\'s Club in 1951 for one dollar; the club leased it to the city in 1975 for the Double O senior meal programme and later let it for shops and offices. It went on the National Register in October 2024 for its place in Sitka\'s social and women\'s history, 1951 to 1975.',
  'A small wooden cottage on Harbor Drive by the water. The Sentinel says a health practitioner uses it now. Interior not checked.',
  '',
  'At 300 Harbor Drive; the Sentinel article does not say plainly who owns it now. Look from the street.',
  [SENT_WC,HP_WC],brick='no'),
]

PIN_NOTES={
'sitka-naval-operating-base-fort-rousseau':'On Makhnati Island, the wooded island at the end of the causeway on the aerial (the federal names file and OpenStreetMap give Fort Rousseau here); area only, the batteries were not placed.',
'old-sitka-redoubt-st-michael':'Register list point; on the aerial it falls on the state park\'s parking loop by the boat launch on Halibut Point Road, area only.',
'castle-hill-baranof-castle-sitka':'Register point moved 12 m west onto the summit ring of Castle Hill seen on the aerial.',
'russian-american-building-29-sitka':'Register list point, on the row of buildings on the south side of Lincoln Street west of the cathedral on the aerial; which roof is No. 29 could not be told, so site precision.',
'st-peters-by-the-sea-sitka':'Register list point for 611 Lincoln Street; on the aerial it falls on a drive between the buildings north of Lincoln Street, within about 20 m of them; the church could not be told from the See House, so site precision.',
'alaska-native-brotherhood-hall-sitka':'Register point moved 16 m west onto the long hall standing over the water off Katlian Street on the aerial.',
'sheldon-jackson-museum-sitka':'Wikipedia point; on the aerial it falls on a building beside Lincoln Street at the east side of the campus green, site precision.',
'sheldon-jackson-school-campus-sitka':'Wikipedia point, on the campus green among the halls on the aerial.',
'sitka-pioneer-home':'Register point moved 25 m west onto the middle of the large red-roofed building at Katlian and Lincoln streets seen on the aerial.',
'sitka-post-office-court-house':'Register list point, at the large flat-roofed building at the west end of Lincoln Street by Castle Hill on the aerial; site precision.',
'sitka-national-historical-park-fort-site':'Register point for the park, in the forest near Indian River on the aerial; the battle field itself was not placed, so area only. The parking point is the lot beside the building at the end of Lincoln Street, read off the aerial and not confirmed by a park page.',
'sitka-national-cemetery':'The VA page\'s map point moved 37 m north-west from the road edge onto the rows of graves seen on the aerial.',
'princess-maksoutoff-grave-sitka':'HMdb marker position on Princess Way; on the aerial a lane and grass among trees north of the Pioneers\' Home, the grave itself not visible, so site precision.',
'sitka-womans-club-building':'Register list point; on the aerial a small cottage by the water on Harbor Drive lies within about 10 m.',
}
