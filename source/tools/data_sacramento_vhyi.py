# Sacramento, California: buildings named in a walk-through video of old photographs and postcards, each checked
# against Wikipedia, the National Register, the Diocese of Sacramento's archives and, for opening times, the page of
# whoever runs the place. Downtown and Old Sacramento first, then midtown.
from data_b import N
from data_ma import W

BATCH={'key':'sacramento_vhyi','label':'Sacramento: Sutter\'s Fort, Old Sacramento, the Cathedral, Crocker, City Hall and downtown landmarks','added':'2026-11-24 07:31'}

PLACES=[
N('sutters-fort-sacramento','Sutter\'s Fort','Sacramento','ca','fort','standing',38.57247,-121.47122,'site','open','walk','forts','1841–',
  'The walled trading post at the heart of John Sutter\'s colony of New Helvetia, the first non-Indigenous settlement in the Central Valley, begun in 1839; the fort itself was started in 1841. Its two-storey adobe main building, put up between 1841 and 1843 by Indigenous forced labour, is where James Marshall showed Sutter the gold from Sutter\'s Mill in January 1848. The city of Sacramento grew up round it. When the city meant to tear it down in 1891, the Native Sons of the Golden West bought and rebuilt it, and it passed to California State Parks in 1947.',
  'The adobe central building is the one original structure; the walls and the rooms round them were rebuilt. The rooms hold exhibits on early California and on the Nisenan, Miwok and Hawaiian people who worked here. A National Historic Landmark since 1961.',
  'The adobe where Sutter first saw the gold.',
  'Sutter\'s Fort State Historic Park, run by California State Parks, between K and L streets and 26th and 28th streets in midtown. Entry fee ($5 adults, $3 youth, under 6 free, as read November 2026). No parking on park grounds: metered street parking and paid lots nearby. Dogs on the grounds only, service animals inside. Hours from the park\'s page.',
  [W('Sutter\'s Fort'),['California State Parks: Sutter\'s Fort SHP','https://www.parks.ca.gov/?page_id=485']],
  conf='', th=None, thn=None, brick='no', hours='Daily 10 a.m. to 5 p.m.; closed Thanksgiving, Christmas and New Year\'s Day'),

N('old-sacramento-historic-district','Old Sacramento and its raised streets','Sacramento','ca','town','standing',38.58485,-121.50497,'area','open','walk','','1849–',
  'The 1850s riverfront business district that grew up between Sutter\'s Fort and the Sacramento River. Floods came often before the levees, so the city raised its streets a storey; most old sidewalks and shopfronts were filled in, but hollow sidewalks and spaces below the street remain. By the 1960s the district was run down, and it was restored as a historic district, some buildings moved in or rebuilt. It became a National Historic Landmark in 1965 and holds more than 50 historic buildings; California State Parks runs about a third of it.',
  'The 1853 B. F. Hastings Building (western end of the Pony Express and first home of the California Supreme Court), the 1855 Big Four Building and the Eagle Theater. The Sacramento History Museum\'s underground tours, about an hour, show hollow sidewalks, sloped alleys and two spaces left below the raised streets; photographs are not allowed underground. The California State Railroad Museum is here too.',
  'Walk under the streets a whole city jacked up out of the floods.',
  'Public streets; the state historic park is free to enter. The underground tours leave from the Sacramento History Museum, 101 I Street (the pin), and are ticketed ($30 adults, $25 ages 6 to 17, under 6 free, as read November 2026); closed-toe shoes advised. Metered street parking and the Old Sacramento garage at 2nd and I streets.',
  [W('Old Sacramento State Historic Park'),['California State Parks: Old Sacramento SHP','https://www.parks.ca.gov/?page_id=497'],['Sacramento History Museum: underground tours','https://sachistorymuseum.org/underground-tours/']],
  conf='', th=None, thn=None, brick='?', hours='Underground tours daily from the Sacramento History Museum; state park museum 10 a.m. to 5 p.m.'),

N('cathedral-blessed-sacrament-sacramento','Cathedral of the Blessed Sacrament','Sacramento','ca','worship','standing',38.57903,-121.49198,'exact','open','walk','','1887–1889',
  'The cathedral of the Catholic Diocese of Sacramento at 11th and K streets, begun in 1887 under Bishop Patrick Manogue, a gold-rush miner turned priest, and completed in June 1889. When finished no cathedral west of the Mississippi was as large. It is Italian Renaissance outside and Victorian inside, and has held the funeral Masses of California governors.',
  'A large restoration cleaned and re-leaded the big stained glass windows, painted the walls and ceiling and rebuilt the 110-foot inner dome, blocked from view for about seventy years. A Reuter organ installed then reuses pipes of the earlier instrument. Free docent tours on Sundays.',
  'The biggest cathedral in the West when it opened, its dome uncovered again after seventy years.',
  'An active cathedral; visitors welcome in the hours the parish page gives (enter by the left side gate ramp). Free Sunday docent tours meet by the baptismal font (English 9 and 11 a.m., Spanish 1 p.m., as read November 2026). Street and garage parking downtown.',
  [W('Cathedral of the Blessed Sacrament (Sacramento, California)'),['Cathedral parish page','https://www.cathedralsacramento.org/']],
  conf='', th=None, thn=None, brick='?', hours='Open daily 10 a.m. to 4 p.m.; Mass Monday to Friday 12:10 p.m., Sunday 8, 10 a.m., 12, 2, 4 and 6 p.m.'),

N('st-francis-assisi-church-sacramento','St. Francis of Assisi Church','Sacramento','ca','worship','standing',38.57384,-121.47251,'exact','view','walk','','1908–1910',
  'The Franciscan friars came to Sacramento in 1894 at Bishop Manogue\'s invitation, bought the southwest corner of 26th and K streets that December and built a first church and friary. Within ten years it was too small. Brother Adrian Wiewer, a friar, drew the present church; its cornerstone was laid in the fall of 1908 and it was dedicated on October 18, 1910, by the diocesan archives\' account.',
  'The 1910 church on 26th Street, two blocks from Sutter\'s Fort. Its foundation, columns and roof were strengthened about 2004. Interior not checked.',
  'A friar-designed church two blocks from Sutter\'s Fort.',
  'An active parish church at 1066 26th Street. Mass times not checked: the parish\'s own pages could not be opened when this was written. Street parking in midtown.',
  [['Diocese of Sacramento archives: the Franciscan friars in Sacramento (PDF)','https://www.scd.org/sites/default/files/2017-06/Vol_2_No_42_Franciscan_Friars_in_Sacramento.pdf'],['Pacific Coast Architecture Database','https://pcad.lib.washington.edu/building/3066/']],
  conf='', th=None, thn=None, brick='?', hours=''),

N('sacramento-city-hall-1909','Sacramento City Hall (1909)','Sacramento','ca','civic','standing',38.58213,-121.49344,'site','view','walk','','1908–1909',
  'Designed in 1908 by the local architect Rudolph A. Herold and finished in 1909 at 915 I Street, facing the city plaza. It was restored from 2003 to 2005 for about $11 million as the cornerstone of a new civic centre, which joined it to a modern wing; together they hold the city\'s main offices.',
  'The 1909 building on I Street, with its columns and carved capitals, stands in front of the newer wing. Interior not checked.',
  'The city\'s 1909 hall, restored as the face of a new civic centre.',
  'Working city offices at 915 I Street, across from Cesar Chavez Plaza; look from the street. Street and garage parking downtown.',
  [W('Sacramento City Hall')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('crocker-art-museum-sacramento','Crocker Art Museum (the Crocker mansion and gallery)','Sacramento','ca','civic','standing',38.5771,-121.50607,'exact','open','walk','','1874–',
  'Judge Edwin B. Crocker and Margaret Crocker gathered paintings and drawings in Europe from 1869 to 1871 and built a gallery beside their house at Third and O streets; the mansion and gallery, finished in 1874, are counted the best work of the architect Seth Babson. Margaret Crocker lent the gallery for a public exhibition in 1885, the year the museum dates from; it is the oldest art museum in the western United States. A large modern wing opened in 2010.',
  'The 1874 Italianate gallery and the Crocker mansion, with the 2010 addition behind. The mansion\'s front was restored in 1989 with a modern gallery inside. The collection runs from Gold Rush paintings to Old Master drawings and ceramics.',
  'The oldest art museum in the West, still in the judge\'s 1874 gallery.',
  'A museum at 216 O Street. Admission charged ($15 adults, as read November 2026). Street parking, lots and public garages nearby; light rail stops at 7th and Capitol and at 8th and K.',
  [W('Crocker Art Museum'),['Crocker Art Museum: plan your visit','https://www.crockerart.org/visit']],
  conf='', th=None, thn=None, brick='?', hours='Wednesday to Sunday 10 a.m. to 5 p.m., Thursday to 9 p.m.; closed Monday and Tuesday'),

N('elks-tower-sacramento','Elks Tower','Sacramento','ca','civic','standing',38.58019,-121.4917,'exact','view','walk','','1926–',
  'A fourteen-storey Italian Renaissance tower of brick and steel at 11th and J streets, dedicated in June 1926 as the home of Sacramento Elks Lodge No. 6, with about a hundred hotel rooms and a shop as well. From 1968 radio stations broadcast from its thirteenth floor. It was designed by Starks and Flanders, who also drew the Federal Building and the Sutter Club.',
  'The tall lodge tower beside the cathedral. It is now hired out for weddings and parties. Interior not checked.',
  'A fraternal lodge built as a skyscraper.',
  'Private; an event venue at 921 11th Street. Look from the street.',
  [W('Elks Tower'),W('Federal Building (Sacramento)')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('governors-mansion-sacramento','California Governor\'s Mansion','Sacramento','ca','landmark','standing',38.58012,-121.4849,'exact','view','walk','','1877–',
  'A thirty-room, three-storey Second Empire and Italianate house built in 1877 for the hardware merchant Albert Gallatin, sold in 1887 to Joseph Steffens, father of the journalist Lincoln Steffens, and bought by the state in 1903 as the governor\'s home. Governors lived here from 1903 to 1967 and again from 2015 to 2019; since 1967 California State Parks has kept it as a historic house museum.',
  'Furnishings left by past governors (a 1902 Steinway piano, Hiram Johnson\'s chairs and sofas, Persian rugs bought by Earl Warren\'s wife) are inside, but the house is shut to visitors: look from 16th and H streets.',
  'Lincoln Steffens\'s boyhood home, then the governors\' for sixty years.',
  'Governor\'s Mansion State Historic Park, California State Parks, at 16th and H streets. The park\'s page says it is closed to the public (November 2026). Look from the street.',
  [W('Governor\'s Mansion State Historic Park'),['California State Parks: Governor\'s Mansion SHP','https://www.parks.ca.gov/?page_id=498']],
  conf='', th=None, thn=None, brick='?', hours=''),

N('travelers-hotel-sacramento','Travelers\' Hotel','Sacramento','ca','hotel','standing',38.58184,-121.50052,'exact','view','walk','hotels','1914–',
  'A six-storey hotel at 5th and J streets that opened in May 1914 as one of the finest on the Pacific Coast. Its E-shaped plan gave all 226 rooms an outside window. It was designed by Cuff and Diggs and built with a steel and concrete frame faced in locally made brown brick. It was listed on the National Register in 1978.',
  'The long lobby with Alaskan marble pillars and white tile floors and a basement banquet room with a marble dance floor were described as little altered in 1978. Whether they survive now was not checked.',
  'The 1914 hotel where every room had a window.',
  'Private building at 428 J Street, next to Old Sacramento; look from the street.',
  [['National Register nomination (PDF)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/78000744_text']],
  conf='', th=None, thn=None, brick='?', hours=''),

N('sutter-club-sacramento','Sutter Club','Sacramento','ca','civic','standing',38.57783,-121.49642,'exact','view','walk','','1930–',
  'One of the oldest social clubs in California, formed in 1889 for Sacramento merchants and professional men. Its present clubhouse at 1220 9th Street, in a Spanish and Mediterranean style by Dean and Dean with Starks and Flanders, opened in 1930. It became a city landmark in 1982 and was listed on the National Register in 2017.',
  'The 1930 Spanish-style clubhouse a block from the Capitol. Interior not checked.',
  'A private club of 1889 in its 1930 Spanish house.',
  'A private members\' club; look from the street.',
  [W('Sutter Club')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('federal-building-sacramento','U.S. Post Office, Courthouse and Federal Building','Sacramento','ca','civic','standing',38.58235,-121.49483,'exact','view','walk','','1933–',
  'Finished in 1933 to designs by the local firm Starks and Flanders, in a simplified Renaissance Revival style. It held the post office, the federal court for northern California until 1966, and government offices. The post office moved out in July 2012. It was listed on the National Register in 1980.',
  'The 1933 federal building at 8th and I streets. Federal offices now; interior not checked.',
  'The New Deal-era post office and court that replaced the old one.',
  'A federal office building at 801 I Street; look from the street.',
  [W('Federal Building (Sacramento)')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('sacramento-city-library-carnegie','Sacramento City Library (Carnegie building)','Sacramento','ca','civic','standing',38.58175,-121.49514,'site','view','walk','','1918–',
  'The three-storey Italian Renaissance Revival central library on I Street between 8th and 9th, designed by Loring P. Rixford and paid for largely by a $100,000 Carnegie grant. It opened in 1918 and replaced an 1872 library a block west. It was listed on the National Register in 1992.',
  'The outside keeps much of its 1918 look; the inside has been much modernised. It faces Cesar Chavez Plaza beside City Hall.',
  'Sacramento\'s Carnegie library, still the central branch.',
  'The Central Library of Sacramento Public Library, 828 I Street. Opening hours not checked: the library\'s own page could not be opened when this was written.',
  [W('Sacramento City Library')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('sacramento-valley-station','Sacramento Valley Station (Southern Pacific depot)','Sacramento','ca','rail','standing',38.58418,-121.50061,'exact','view','walk','stations','1926–',
  'The Southern Pacific Railroad\'s depot of 1926 at 4th and I streets, designed by Bliss and Faville of San Francisco in the Renaissance Revival style and opened in February 1926 on the site of China Slough. It is still a working station, one of the busiest Amtrak stops in the West and the end of a light rail line.',
  'Inside, the waiting room keeps a mural by John A. MacQuarrie of the 1863 groundbreaking in Sacramento for the first transcontinental railroad. The ticket and baggage offices were moved into the old station restaurant in a recent renovation.',
  'A working 1926 depot with its waiting-room mural.',
  'A working Amtrak and light rail station at 401 I Street; the waiting room is open to travellers. Station hours not checked.',
  [W('Sacramento Valley Station')],
  conf='', th=None, thn=None, brick='?', hours=''),
]

PIN_NOTES={
 'sutters-fort-sacramento':'Wikipedia\'s point for the fort, inside its walls.',
 'old-sacramento-historic-district':'Address lookup of the Sacramento History Museum, 101 I Street, where the underground tours begin; the district spreads round it.',
 'cathedral-blessed-sacrament-sacramento':'Address lookup of 1017 11th Street, on the cathedral.',
 'st-francis-assisi-church-sacramento':'Address lookup of 1066 26th Street, on the church at 26th and K.',
 'sacramento-city-hall-1909':'Address lookup of 915 I Street; the aerial shows the old hall and the newer wing joined, so the pin marks the site.',
 'crocker-art-museum-sacramento':'Address lookup of 216 O Street.',
 'elks-tower-sacramento':'Address lookup of 921 11th Street.',
 'governors-mansion-sacramento':'Address lookup of 1526 H Street.',
 'travelers-hotel-sacramento':'Address lookup of 428 J Street.',
 'sutter-club-sacramento':'Address lookup of 1220 9th Street.',
 'federal-building-sacramento':'Address lookup of 801 I Street.',
 'sacramento-city-library-carnegie':'Wikipedia\'s point, on the I Street side of the block; the address lookup of 828 I Street fell 10 m south on the newer library tower behind the 1918 building. The pin marks the site.',
 'sacramento-valley-station':'Address lookup of 401 I Street.',
}
