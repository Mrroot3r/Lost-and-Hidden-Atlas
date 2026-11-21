# November 21, 2026: Fresno, California. A "videos" session (PROMPTS.md job 9): the names came from one video's list of
# Fresno buildings (the record is source/videos/20250926_hlwluCCauT4.md); the video is a tip and nothing here rests on it.
# Sources read in this session: historicfresno.org (A Guide to Historic Architecture in Fresno: its National Register and
# Local Register pages and its driving tour, adapted from the Register nominations), Wikipedia (tools/wiki_raw.py), the
# Pacific Coast Architecture Database, KVPR (May 2026) on the Bank of Italy, an ABC30 report on the Rowell Building, a
# Fresno Bee column (read on Yahoo) on the Liberty Theatre, and the own pages of the Forestiere Underground Gardens, the
# Fresno County Historical Society (Kearney Mansion) and St. John's Cathedral for hours. Pins are address lookups
# (ArcGIS PointAddress) looked at on the aerial. Interiors were not visited by any source opened unless the entry says so.
from data_b import N
from data_ma import W
BATCH={'key':'fresno_znad','label':'California: downtown Fresno, Kearney Park and the Underground Gardens','added':'2026-11-21 22:19'}

def HF(page,label):
    return ['Historic Fresno: '+label,'https://historicfresno.org/'+page]
TOUR=HF('tours/nrhp.htm','driving tour of National Register sites')
G4=[36.73369,-119.79129]
G4N='City Parking Garage 4, 1919 Tulare Street'
SP=[36.73271,-119.78753]
SPN='The Spiral Garage, 801 Van Ness Avenue'
DT=' The Downtown Fresno Partnership lists the public garages nearby: City Parking Garage 4 (1919 Tulare Street), the Van Ness Courthouse Garage (1077 Van Ness Avenue) and the Spiral Garage (801 Van Ness Avenue); their hours and fees were not checked.'
DTL=['Downtown Fresno Partnership: Bank of Italy listing (nearby public parking)','https://www.downtownfresno.org/space-available/bank-of-italy-1015-fulton-st']

PLACES=[
N('bank-of-italy-fresno','Bank of Italy Building','Fresno','ca','civic','standing',36.73389,-119.79066,'exact','view','walk','','1917–1918',
  'An eight-story bank and office tower at Fulton and Tulare streets, designed by Charles Franklin of the R. F. Felchlin Company for A. P. Giannini\'s Bank of Italy, which became the Bank of America in 1930. Historic Fresno dates it 1917 and says it was finished about August 1918; KVPR says the banking hall was enlarged along Tulare Street in 1927 and that the bank moved out by 1968. It has stood empty since the 1970s (KVPR: the mid 1970s) and was sold to a Fresno developer in 2009.',
  'A steel and concrete tower faced in sculpted white terra cotta and brick (KVPR calls the brick brown): ornate spandrel panels, belt courses, arched windows near the top and a heavy terra cotta cornice. The Register form describes a lobby with a 25-foot decorative plaster ceiling, marble floor and stair, etched brass elevator doors, a brass letter box and the original wall clock; the building is vacant and shut, so the interior is not open and was not checked.',
  'Fresno\'s banking palace, empty for about fifty years.',
  'Private, vacant and closed (owned by the Penstar Group, which lists its floors for lease): look from the Fulton Street and Tulare Street sidewalks. The address is given as 1001 Fulton Mall, 1015 Fulton Street and, in one place on the tour page, 1101 Fulton Mall; it is the corner building at Fulton and Tulare.'+DT,
  [HF('nrhp/italy.htm','Bank of Italy Building'),['KVPR, Central Valley Roots: the Bank of Italy building (May 26, 2026)','https://www.kvpr.org/podcast/central-valley-roots/2026-05-26/fresnos-historic-banking-palace-the-bank-of-italy-building'],DTL,W('Bank of Italy (Fresno, California)')],
  conf='mixed',th=G4,thn=G4N,brick='no'),
N('fresno-brewing-company-office','Fresno Brewing Company office and warehouse','Fresno','ca','industry','standing',36.72737,-119.77620,'site','view','drive','','1907 (brewery 1900–1955)',
  'The brick office and warehouse of a brewery that Ernst Eilert founded in 1900. Brewing stopped with Prohibition in 1919, when the plant bottled soft drinks as Eilert Products, and began again in 1933; the brewery was sold to Grace Bros. of Santa Rosa in 1942. The six-story brewhouse to the south was pulled down in 1955, and this building, an attached storage shed and a wood shed are all that is left of a twenty-acre works. Historic Fresno\'s Register page dates the office 1907; its tour page says 1899.',
  'A long two-story office and one-story warehouse (42 by 173 feet) all of common red brick laid in English bond, with a crenelated parapet, round-arched windows, string courses, and black fluted cast-iron columns under a tin awning over the porch and loading platforms. The Register form describes an untouched office inside: pressed-tin walls and ceilings, a cashier\'s window, a Mosler walk-in safe, an Otis elevator and a cast-iron spiral stair. The empty lot beside it is where the brewery stood. Interior not checked; no source read says the public may go in.',
  'The office outlived the brewery it served by seventy years.',
  'Private; view from M Street and Heaton Street at 100 M Street, on the southern edge of downtown (the tour page reaches it from Highway 41 by the O Street exit, Santa Clara Street and M Street). Street parking was not checked on the ground.',
  [HF('nrhp/fresbrew.htm','Fresno Brewing Company'),TOUR],
  conf='mixed',brick='yes'),
N('hotel-californian-fresno','Hotel Californian','Fresno','ca','hotel','standing',36.73334,-119.78805,'exact','view','walk','','1923',
  'A nine-story hotel at Van Ness Avenue and Kern Street, designed by H. Rafael Lake and built by R. F. Felchlin and Company in 1923 as a luxury hotel and a meeting place for the city. It was known as the best hotel between San Francisco and Los Angeles. The Register form says it now houses low-income seniors, with shops in the ground floor.',
  'An Italian Renaissance block in three parts: a two-story base of cast stone with arched second-floor windows under red brick voussoirs, a five-floor shaft of variegated red brick, and a top floor with iron-railed balconettes under a bracketed metal cornice. From Kern Street the upper floors read as two towers joined at the back, a U-shaped plan. The ground-floor storefronts were rebuilt in aluminum and glass in the 1970s. Interior not checked; it is housing.',
  '',
  'Private housing with ground-floor shops: view from the Van Ness Avenue and Kern Street sidewalks at 851 Van Ness Avenue.'+DT,
  [HF('nrhp/californ.htm','Hotel Californian'),HF('lrhr/174.htm','Hotel California (Local Register 174)'),DTL],
  th=SP,thn=SPN,brick='yes'),
N('forestiere-underground-gardens','Forestiere Underground Gardens','Fresno','ca','landmark','standing',36.80740,-119.88198,'site','open','drive','','1906–1946',
  'A hand-dug underground home and garden. Baldassare Forestiere, a Sicilian immigrant, found his Fresno land was hardpan and the summers punishing, dug a cellar to live in, and went on digging for about forty years, until his death in 1946, with hand tools and a pair of mules. He planted fruit trees and vines in chambers open to the sky. It opened to the public after his death, is run by members of his family, and is on the National Register and is California Historical Landmark 916.',
  'Almost nothing shows from the street. Below ground: rooms, passageways and courtyards with arches and vaults, some 25 feet down by the gardens\' account, and fruit trees and vines growing up through skylights, some more than ninety years old. Seen by guided walking tour only, about an hour.',
  'A man dug himself a house under the hardpan and then kept going for forty years.',
  'Run by the Forestiere family at 5021 West Shaw Avenue; admission fee, guided tours only, reservations recommended (prices not checked). The gardens\' own pages say the season is March through November, that tour days and times change through the year and are shown on its booking calendar, that it closes in extreme heat or wet weather, and that November 30 is the last day of the 2026 season. A visitor\'s review on the gardens\' site mentions free street parking in front; not checked.',
  [['Forestiere Underground Gardens','https://undergroundgardens.com/'],['Forestiere Underground Gardens: questions and answers','https://undergroundgardens.com/faq'],W('Forestiere Underground Gardens'),TOUR],
  brick='?',hours='Guided tours, March through November; days and times change, see its booking calendar. Closed December to February'),
N('hotel-fresno','Hotel Fresno','Fresno','ca','hotel','standing',36.73582,-119.79456,'exact','view','walk','','1912',
  'The oldest hotel building left in Fresno: seven stories of concrete by the architect Edward T. Foulkes, a high-rise when it was built in 1912 (the Local Register page says 1913) and once the social center of the city. Its plan, a block wrapped round a two-story glass-roofed court, is said to follow the Palace Hotel in San Francisco. It closed in 1983 and stood empty for about forty years; Wikipedia says work began in 2019 and it reopened in October 2024 as affordable housing for 79 families.',
  'Scored concrete walls with a two-story base, four plain floors of rooms and a decorated top floor: an elaborate metal cornice, iron balconettes, oval cartouches and swag panels. The Register form, written while it was empty, describes the court inside with its arcade of fourteen piers; what the renovation kept was not checked, and it is housing, not open to visitors.',
  '',
  'Private housing at 1241 to 1263 Broadway Plaza: view from the sidewalk. Streets round it were realigned, so approach on foot from Fulton Street. Parking: a lot mapped on Broadway by OpenStreetMap, not checked on the ground.',
  [HF('nrhp/hotelfresno.htm','Hotel Fresno'),HF('lrhr/166.htm','Hotel Fresno (Local Register 166)'),W('Hotel Fresno')],
  conf='mixed',th=[36.73753,-119.79545],thn='Mapped parking lot on Broadway (OpenStreetMap)',brick='no'),
N('kearney-mansion-fresno','Kearney Mansion','Fresno','ca','inst','standing',36.72384,-119.91925,'site','open','drive','','1903 (park begun 1892)',
  'The house of M. Theo Kearney (1842–1906), a promoter of Fresno County farm colonies and head of the raisin growers, at the middle of his Fruit Vale Estate seven miles west of Fresno. It was meant only as the superintendent\'s lodge: Kearney planned a far larger house, Chateau Fresno, which was never built, and at his death only this residence and the servants\' quarters stood. He left the estate to the University of California, which sold all but the park by 1949; the county leases the park, and the Fresno City and County Historical Society has run the house as a museum since 1962.',
  'Two buildings in a French Renaissance manner, with walls of two-foot-thick adobe brick under plaster and steep roofs with dormers, pinnacles and tall chimneys. Inside, by the Register form, about half the original furnishings, French wallpapers and art nouveau light fixtures; the servants\' quarters hold a gallery and the museum store. Round it, the park laid out by Rudolph Ulrich from 1892, and Kearney Boulevard, the tree-lined avenue he planted from the city.',
  'The grand house on the plans was never built; the caretaker\'s lodge became the mansion.',
  'In Kearney Park, a Fresno County park at 7160 West Kearney Boulevard; the society\'s page says a $5 per vehicle parking fee, cash only, is taken at the park entrance. Tours are guided, about an hour: adults $12, seniors $10, children 5 to 12 $8; reservations encouraged, closed on some holidays (the society\'s visiting page, read November 2026). Park hours not checked. The pin is a building mapped by OpenStreetMap at the end of the park drive; follow the park signs to the mansion.',
  [['Fresno City and County Historical Society: visit Kearney Mansion Museum','https://www.valleyhistory.org/visitkmm'],HF('nrhp/kearney.htm','Kearney Mansion'),W('Kearney Park (Fresno)')],
  brick='no',hours='Guided tours Friday, Saturday and Sunday at 12, 1:30 and 3 p.m.; twilight tours Thursdays 7 p.m., late April to late September'),
N('liberty-theatre-fresno','Liberty Theatre (Hardy\'s Theatre)','Fresno','ca','civic','standing',36.73453,-119.78848,'exact','view','walk','','1917',
  'The oldest movie theater left in Fresno, opened in 1917 as the Liberty to designs by W. D. Coates and H. B. Traver, and later called Hardy\'s and then the Mexico. A Fresno Bee column says a church bought it and, under a city permit issued in 2021 without review by the preservation commission, gutted much of the inside, the balcony included; work stopped in October 2022, and the column reports a partial roof collapse, water damage and mold since.',
  'A Renaissance Revival front on Van Ness Avenue that, by Historic Fresno, still carries signs for all three of its names; the Hardy\'s marquee dates from the 1930s. The column describes broken windows, graffiti and a boarded, padlocked entrance. Closed; the interior is largely stripped.',
  'Fresno\'s oldest picture house, gutted on a permit nobody reviewed.',
  'Private, closed and in poor repair: look from the Van Ness Avenue sidewalk at 944 Van Ness Avenue and keep out.'+DT,
  [HF('lrhr/171.htm','Liberty Theater (Local Register 171)'),['Fresno Bee column (on Yahoo): Leaky roof, a ceiling cave-in and mold','https://www.yahoo.com/news/leaky-roof-ceiling-cave-mold-172229382.html'],['Pacific Coast Architecture Database: Liberty Theatre','https://pcad.lib.washington.edu/building/7454']],
  th=SP,thn=SPN,brick='?'),
N('rowell-building-fresno','Rowell Building','Fresno','ca','civic','standing',36.73480,-119.78853,'exact','view','walk','','1911–1912',
  'A six-story office block in the form of an Italian palazzo at the southeast corner of Tulare Street and Van Ness Avenue, designed by R. F. Felchlin and finished in 1912, the year its owner, the physician and politician Chester A. Rowell, died. After a renovation it became the Fresno County District Attorney\'s office in 2021.',
  'The Renaissance Revival street fronts on Tulare and Van Ness, across from the courthouse park. It is a working county office, not a place to visit; interior not checked.',
  '',
  'A Fresno County office at 2100 Tulare Street: view from the sidewalk.'+DT,
  [HF('lrhr/170.htm','Rowell Building (Local Register 170)'),['Pacific Coast Architecture Database: Rowell Building','https://pcad.lib.washington.edu/building/25030'],['ABC30: Historic Rowell Building now home to Fresno County District Attorney\'s Office (2021)','https://abc30.com/post/rowell-building-fresno-county-district-attorney/11061983/']],
  th=SP,thn=SPN,brick='no'),
N('san-joaquin-light-and-power-building','San Joaquin Light and Power Corporation Building','Fresno','ca','civic','standing',36.73771,-119.79506,'exact','view','walk','','1923–1924',
  'The eleven-story headquarters of the San Joaquin Light and Power Corporation, a company begun in 1895 that later became part of Pacific Gas and Electric. Raymond R. Shaw of the R. F. Felchlin Company designed it, and it went up in 1923 and 1924 at Fulton and Tuolumne streets, across from the Pantages Theatre. Wikipedia gives its height as 52.8 meters, the fourth tallest building in the city.',
  'An Italian Renaissance Revival office tower that Historic Fresno calls a landmark on the skyline. What it holds now and its interior were not checked.',
  '',
  'Private offices at 1401 Fulton Street: view from the sidewalk. Parking: a lot mapped on Broadway by OpenStreetMap, not checked on the ground.',
  [TOUR,W('San Joaquin Light and Power Corporation Building')],
  th=[36.73753,-119.79545],thn='Mapped parking lot on Broadway (OpenStreetMap)',brick='?'),
N('southern-pacific-depot-fresno','Southern Pacific Depot','Fresno','ca','rail','standing',36.73229,-119.79321,'exact','view','walk','stations','1889',
  'The railroad made Fresno: the Central Pacific set a station here in 1872 with a wood-frame depot. In 1889 the Southern Pacific, which had made Fresno its main freight terminal in the valley, replaced it with this Queen Anne passenger and freight depot, one of two stations in that style in California. Freight space was added on the south side between 1914 and 1929 and offices on the north in 1930. It closed to passengers on May 1, 1971. California\'s high-speed rail station is being built beside it as an expansion of the depot, with a $20 million federal grant in 2023 toward restoring the building and a plaza.',
  'The 1889 depot at the foot of Tulare Street, beside the Union Pacific main line. Expect construction for the high-speed rail station round it; how much can be seen from the street today was not checked, and no source read says the building is open.',
  'The 1889 depot that is to become the door of a high-speed rail station.',
  'Owned for the high-speed rail project; closed. View from Tulare Street and H Street at 1713 Tulare Street. The tracks beside it are an active main line: stay off railroad property.'+DT,
  [HF('lrhr/011.htm','Southern Pacific Depot (Local Register 11)'),W('Fresno station (California High-Speed Rail)'),TOUR],
  th=G4,thn=G4N,brick='no'),
N('st-johns-cathedral-fresno','St. John the Baptist Cathedral','Fresno','ca','worship','standing',36.74061,-119.78227,'exact','open','walk','','1902–1903',
  'The mother church of the Catholic Diocese of Fresno. St. John\'s is the oldest parish in the city: its first church, of brick with a 90-foot steeple, was finished in 1880 on M Street and pulled down from 1901. The cornerstone of this one was laid in April 1902 on Mariposa Street and it was dedicated in June 1903; it became a cathedral in 1922. The architect was Thomas Bermingham.',
  'A red brick Gothic-Romanesque church (the brick from a photograph on Wikipedia) with two square towers under spires, a triple doorway and a rose window, with the rectory and St. John\'s Hall school beside it, both on the city\'s Local Register. Wikipedia mentions stained glass and statues; the interior was not checked beyond that.',
  '',
  'An active Catholic cathedral at 2814 Mariposa Street; Mass times are from the parish\'s own page (read November 21, 2026), and the rectory office keeps Tuesday to Friday hours. Street parking was not checked.',
  [['St. John\'s Cathedral (parish page)','https://stjohnsfresno.org/'],W('Saint John the Baptist Cathedral (Fresno, California)'),HF('lrhr/mariposa.htm','Local Register, Mariposa Street')],
  brick='yes',hours='Mass: Monday to Friday 8 a.m. (Spanish) and 12:10 p.m.; Saturday 4 and 5:15 p.m.; Sunday 7:30, 9, 10:30 a.m., 12 and 1:30 p.m.'),
N('mattei-building-fresno','Mattei Building','Fresno','ca','civic','standing',36.73546,-119.79262,'exact','view','walk','','1920–1921',
  'A twelve-story office tower on Fulton Street, one of several high-rises put up in Fresno in the 1920s, designed by Eugene Mathewson with Robert von Ezdorf (Historic Fresno dates it 1920, the Pacific Coast Architecture Database 1921). Guarantee Savings bought it in 1961 and remodeled it heavily, destroying some of the classical detail at street level.',
  'A neo-classical concrete tower above a remodeled base. Historic Fresno says the original classical columns and capitals can still be seen from the alley behind the building. Present use and interior not checked.',
  '',
  'Private, at 1177 Fulton Street: view from the Fulton Street sidewalk and the public alley behind.'+DT,
  [HF('lrhr/167.htm','Mattei Building (Local Register 167)'),['Pacific Coast Architecture Database: Mattei Building','https://pcad.lib.washington.edu/building/21075']],
  conf='mixed',th=G4,thn=G4N,brick='no'),
N('pantages-warnors-theatre-fresno','Pantages Theatre (Warnors Theatre)','Fresno','ca','civic','standing',36.73841,-119.79441,'exact','open','walk','','1928',
  'A 2,100-seat theater built by the vaudeville magnate Alexander Pantages to designs by B. Marcus Priteca, who designed all his houses. It opened in 1928 (Historic Fresno heads its pages 1929, the year Warner Brothers bought it and renamed it Warner\'s). It showed films until 1973, when it was sold and turned to concerts, and the name was respelled Warnors in the 1960s.',
  'A corner tower of rusticated terra cotta under a red-tiled lantern, a two-story window arcade on terra cotta pilasters, variegated brick above and a red tile roof, with the auditorium set back behind like a villa in a courtyard. Inside, by the Register form: a flattened dome with a wrought-iron chandelier, stencilled friezes and gold-leaf plaster, and the 1928 Robert Morton pipe organ of 14 ranks and 1,035 pipes. Historic Fresno says that but for a newer marquee it keeps its original look.',
  'A Pantages house with its theater organ still in place.',
  'A working concert theater at 1400 Fulton Street: the inside is seen by going to an event. The theater\'s own page would not open in this session, so event days, tours and box office hours were not checked. Parking: a lot mapped on Broadway by OpenStreetMap, not checked on the ground.',
  [HF('nrhp/warnor.htm','Pantages Theatre'),W('Warnors Theatre')],
  conf='mixed',th=[36.73753,-119.79545],thn='Mapped parking lot on Broadway (OpenStreetMap)',brick='no',hours='?'),
N('old-fresno-water-tower','Old Fresno Water Tower','Fresno','ca','water','standing',36.73920,-119.78721,'exact','public','walk','','1894',
  'The city\'s water tower, designed by the Chicago architect George Washington Maher, who was hired in 1891, and finished in 1894 at a cost of $20,000. It held 250,000 gallons and stayed in use until 1963. His plan put a library on two floors under the tank, which was never fitted. The ground floor was for years a parking-meter repair shop; in 2001 the tower was remodeled as the city and county visitors\' center, and Wikipedia says the Fresno Arts Council took over its management in 2014, with an art gallery.',
  'A 109-foot round tower in an American Romanesque style: brick, each course smaller than the one below to give a beehive profile, with a two-foot inner wall, a fourteen-inch outer wall and a passage between them. The brick is painted over. A landscaped plaza built in 2001 surrounds it. Whether the tower is open now, and when, was not checked: the Arts Council\'s gallery page gives hours for its own office on Van Ness Avenue, not for the tower.',
  'A water tower drawn up with a library inside.',
  'City property at 2444 Fresno Street, at O Street, in a public plaza: seen freely from outside. Parking: a lot mapped across Fresno Street by OpenStreetMap, not checked on the ground.',
  [HF('nrhp/wtrtwr.htm','Old Fresno Water Tower'),W('Old Fresno Water Tower')],
  th=[36.73997,-119.78723],thn='Mapped parking lot across Fresno Street (OpenStreetMap)',brick='no'),
]

AD='Address lookup (ArcGIS PointAddress) for %s; looked at on the aerial.'
PIN_NOTES={
'bank-of-italy-fresno':AD%'1015 Fulton Street',
'fresno-brewing-company-office':AD%'100 M Street'+' The aerial shows a group of industrial roofs here and did not settle which is the 1907 building.',
'hotel-californian-fresno':AD%'851 Van Ness Avenue',
'forestiere-underground-gardens':AD%'5021 West Shaw Avenue'+' The gardens are below ground.',
'hotel-fresno':AD%'1257 Broadway Plaza',
'kearney-mansion-fresno':'A building mapped by OpenStreetMap in Kearney Park, at the end of the park drive; looked at on the aerial.',
'liberty-theatre-fresno':AD%'944 Van Ness Avenue',
'rowell-building-fresno':AD%'2100 Tulare Street',
'san-joaquin-light-and-power-building':AD%'1401 Fulton Street',
'southern-pacific-depot-fresno':AD%'1713 Tulare Street',
'st-johns-cathedral-fresno':AD%'2814 Mariposa Street',
'mattei-building-fresno':AD%'1177 Fulton Street',
'pantages-warnors-theatre-fresno':AD%'1400 Fulton Street',
'old-fresno-water-tower':AD%'2444 Fresno Street',
}
