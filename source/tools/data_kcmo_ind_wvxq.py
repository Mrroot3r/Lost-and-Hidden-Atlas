# November 23, 2026: Independence, Jackson County, Missouri, about ten miles east of downtown Kansas City.
# Part of filling in the Kansas City area on purpose for a local researcher. The Atlas had no place in Independence itself.
# Facts from the linked sources only: Wikipedia read as raw text, the City of Independence's visitor pages, the National Park
# Service pages for the Truman site and the trail park, the Jackson County Historical Society's visit page, the Vaile Mansion's
# and the Bingham-Waggoner Estate's own visit pages, MillPictures.com, and web search results that quote the Truman Library's
# pages. The National Register forms could not be read (NPGallery gives only a placeholder page for the older ones).
from data_b import N
from data_ma import W

NRHP = ['Wikipedia: National Register listings in Jackson County, Missouri', 'https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Jackson_County,_Missouri']
HOMES = ['City of Independence: historic home tours', 'https://www.independencemo.gov/visitors/our-history-and-culture/book-tour-historic-homes-independence-mo']

PLACES = [
N('vaile-mansion-independence-mo', 'Vaile Mansion', 'Independence', 'kcmo', 'landmark', 'standing',
  39.10764, -94.41710, 'exact', 'open', 'drive', '', '1871–1881',
  'Harvey Vaile, a lawyer and mail-route contractor who settled in Independence in 1870, had this Second Empire mansion built; work began about 1871 and it was finished in 1881 at a reported cost of $150,000. '
  'It stood in a 630-acre estate with a vineyard and orchard, now cut down to about 5.6 acres. Wikipedia calls it the first house in Jackson County with indoor plumbing.',
  look='A 31-room house of hand-pressed red brick with limestone trim, a tall central tower and mansard roofs. Inside, according to Wikipedia, the original paintwork, nine marble fireplaces and two of the three original chandeliers remain; the furniture is a later refurnishing, not the Vailes\'. The City of Independence also names a 48,000-gallon wine cellar and a black walnut staircase. Shown by guided tour.',
  accn='A house museum run by a nonprofit, the Vaile Victorian Society, at 1500 North Liberty Street. Tickets are bought at the door ($10 for adults in the regular season, per its visit page); no reservations needed for individuals. Group tours Monday to Wednesday by request. Hours were read from the mansion\'s own visit page in November 2026.',
  links=[W('Vaile Mansion'), ['Vaile Mansion: visit', 'https://vailemansion.org/visit'], HOMES],
  brick='yes', hours='April 1 to October 31: Thursday to Saturday 10 a.m. to 4 p.m., Sunday 1 to 4 p.m. Holiday tours November 28 to December 30 (closed December 23 to 25), same hours'),

N('bingham-waggoner-estate-independence-mo', 'Bingham-Waggoner Mansion and Estate', 'Independence', 'kcmo', 'landmark', 'standing',
  39.08560, -94.41883, 'site', 'open', 'drive', '', 'before 1861',
  'The artist George Caleb Bingham lived here until the Civil War began. The Waggoner family, millers from Pennsylvania who made Queen of the Pantry flour, bought it later. '
  'The City of Independence describes the house as Italianate and says original wagon swales (trail ruts) can still be seen and felt on the property; it lay on the way from the courthouse square to the Santa Fe, California and Oregon trails.',
  look='An Italianate mansion with a park of about 19 acres around it, a carriage house gift shop, and the trail swales on the grounds (the National Park Service puts the swales in line with those in Santa Fe Trail Park, half a mile south). Shown by tour. Which parts of the house are Bingham\'s and which the Waggoners\' was not checked.',
  accn='A house museum at 313 West Pacific Avenue; free parking lot off Pacific Avenue, and the grounds may be explored. The estate\'s own page says walk-in tours are available and gives Thursday to Saturday, 10 a.m. to 3 p.m.; web search results for other pages list different weekday hours, so call ahead. Hours read November 2026.',
  links=[['Bingham-Waggoner Estate: plan your visit', 'https://bwestate.squarespace.com/visit'], HOMES, ['National Park Service: Santa Fe Trail Park', 'https://www.nps.gov/places/000/santa-fe-trail-park.htm'], NRHP],
  conf='mixed', brick='?', hours='Thursday to Saturday, tours 10 a.m. to 3 p.m.; call to confirm'),

N('jackson-county-1859-jail-independence-mo', 'Jackson County 1859 Jail and Marshal\'s Home', 'Independence', 'kcmo', 'civic', 'standing',
  39.09333, -94.41528, 'exact', 'open', 'drive', '', '1859–1933',
  'A. B. Cross designed the county jail, built in 1859 with the jailer\'s house at the front and twelve limestone cells behind. It was replaced in 1933 and later restored as a museum. '
  'A brick block was added behind the jail in 1907 to house chain gangs doing road and sewer work. In the Civil War up to twenty prisoners were held in a cell meant for three.',
  look='Six cells upstairs and six downstairs behind two-foot limestone walls, each six by nine feet, and the jailer\'s kitchen where his wife cooked for the family and the prisoners. The 1907 brick addition is at the back.',
  accn='Museum of the Jackson County Historical Society at 217 North Main Street; free parking across the street and along the street. Admission $6 for adults. Hours from the Society\'s visit page, read November 2026; the page says it also opens on weekends in December.',
  links=[W('Jackson County Jail and Marshal\'s House'), ['Jackson County Historical Society: plan your visit', 'https://www.jchs.org/plan-your-visit'], HOMES],
  brick='some', hours='April to October: Tuesday to Saturday 10 a.m. to 4 p.m., closed Sunday and Monday; weekends in December'),

N('truman-home-independence-mo', 'Truman Home and Noland Home, Harry S Truman National Historic Site', 'Independence', 'kcmo', 'landmark', 'standing',
  39.09333, -94.42306, 'site', 'open', 'drive', '', '1867–1885',
  'Bess Truman\'s grandfather George Porterfield Gates built the house between 1867 and 1885. Harry and Bess Truman lived here after their 1919 marriage; it was the family\'s "Summer White House" during his presidency and his office after he retired in 1953. '
  'Across the street, at 216 North Delaware, the Noland Home belonged to his uncle and aunt and his cousins, where he stayed while courting Bess.',
  look='The Truman Home is shown by a ranger-led tour of about 30 minutes, much as the family left it; the second floor has never been open. The first floor of the Noland Home has exhibits and can be entered without a tour.',
  accn='Run by the National Park Service. Free, but every visitor on a Truman Home tour needs a ticket: tours hold eight people, tickets are given out the same day, first come, first served, at the visitor center at 223 North Main Street, not at the house. Hours read from the Park Service pages, November 2026.',
  links=[W('Harry S. Truman National Historic Site'), ['NPS: operating hours', 'https://www.nps.gov/hstr/planyourvisit/hours.htm'], ['NPS: plan your visit', 'https://www.nps.gov/hstr/planyourvisit/index.htm'], HOMES],
  brick='?', hours='Wednesday to Sunday; Truman Home tours same-day tickets at 223 N. Main; Noland Home first floor 8:30 a.m. to 4:30 p.m.',
  th=[39.0926, -94.4195], thn='National Park Service visitor center area, North Main Street'),

N('truman-courthouse-independence-mo', 'Jackson County Courthouse (Truman Courthouse), Independence Square', 'Independence', 'kcmo', 'civic', 'standing',
  39.09247, -94.41643, 'exact', 'ask', 'drive', '', '1836–1933',
  'Jackson County\'s first permanent courthouse here was brick, built in 1836; sources agree that the present building was rebuilt around that core, in a remodel begun in 1933 and dedicated in 1933 or 1934 (the sources differ). Harry Truman was presiding judge of the county court in these years. '
  'The Jackson County Historical Society now keeps its offices and archives here, and the grounds hold statues of Truman and Andrew Jackson and markers for the Santa Fe, California and Oregon trails.',
  look='Truman\'s restored office and courtroom are in the building, and parts of the 1836 building remain in a second-floor courtroom and the attic, as a web search result quoting the Historical Society puts it. Not checked in person.',
  accn='Owned by Jackson County, on Independence Square. Park on the square\'s streets. Tours are by request through the Jackson County Historical Society (its site has a Request a Tour page); no set hours were found, so none are given.',
  links=[W('Jackson County Courthouse (Independence, Missouri)'), ['Jackson County Historical Society: plan your visit', 'https://www.jchs.org/plan-your-visit'], HOMES],
  conf='mixed', brick='?'),

N('truman-depot-independence-mo', 'Truman Depot (Missouri Pacific Depot)', 'Independence', 'kcmo', 'rail', 'standing',
  39.08674, -94.42955, 'site', 'view', 'drive', '', '1913',
  'The Missouri Pacific Railroad built the station in 1913. It is called the Truman Depot because it was the last stop of Harry Truman\'s 1948 whistle-stop campaign, and 8,500 people welcomed him back in January 1953 after he left office. It was listed on the National Register in 1979.',
  look='Still an Amtrak station. Whether the waiting room is open and what original fittings survive inside was not checked.',
  accn='Owned by the City of Independence (its Parks and Recreation pages list the depot) at 1111 West Pacific Avenue; a National Park Service record gives a different address, 600 South Grand. Look from the street or platform; no hours were found.',
  links=[W('Independence station'), ['City of Independence: Truman Depot', 'https://www.independencemo.gov/visitors/our-history-and-culture/harry-s-truman/truman-depot'], NRHP],
  brick='?'),

N('trinity-episcopal-church-independence-mo', 'Trinity Episcopal Church', 'Independence', 'kcmo', 'worship', 'standing',
  39.09500, -94.41685, 'exact', 'view', 'drive', '', '1881',
  'Wikipedia dates the church at 409 North Liberty Street to 1881 (a Truman Library records note gives 1878, so the year is not settled); it was listed on the National Register in 1979. '
  'Harry Truman married Bess Wallace here on June 28, 1919, and their daughter Margaret was married here on April 21, 1956. Bess began attending the church between 1901 and 1903.',
  look='A Victorian church of 1881 on the edge of the Truman neighborhood. Interior and surviving glass or woodwork not checked.',
  accn='An active Episcopal parish. Look from the street; no page of the parish was read, so service times are not given. Street parking.',
  links=[W('Trinity Episcopal Church (Independence, Missouri)'), ['Truman Library: Trinity Episcopal Church', 'https://www.trumanlibrary.gov/education/student-resources/places/independence/trinity-episcopal-church'], NRHP],
  conf='mixed', brick='?'),

N('stone-church-independence-mo', 'Stone Church (Community of Christ)', 'Independence', 'kcmo', 'worship', 'standing',
  39.0915, -94.4282, 'exact', 'view', 'drive', '', '1884–1888',
  'The Reorganized Church of Jesus Christ of Latter Day Saints began this limestone church in 1884 and dedicated it on April 6, 1888, at 1012 West Lexington Avenue. From the early 1900s until the Auditorium opened in 1958 it was the church\'s headquarters building.',
  look='A limestone church across the street from the Temple Lot and the Independence Temple. It is still a congregation\'s meeting place. Interior not checked.',
  accn='Owned by the Community of Christ. Look from the street; no page of the congregation was read, so service times are not given.',
  links=[W('Stone Church (Independence, Missouri)'), W('Temple Lot')],
  brick='no', hours=''),

N('waggoner-gates-mill-independence-mo', 'Waggoner-Gates Mill remnant', 'Independence', 'kcmo', 'industry', 'standing',
  39.08666, -94.41916, 'site', 'view', 'drive', '', '1830–1967',
  'John Overfelt built a first mill by a spring here in 1830. Peter Waggoner bought it in 1867, his son William rebuilt it as a flour mill in 1875 with George Gates (Bess Truman\'s grandfather), and it became Waggoner-Gates Milling in 1883, known for Queen of the Pantry flour. '
  'It closed in 1957 and an explosion and fire in 1967 left rubble and one long two-story brick storage building, which was made into the National Frontier Trails Center in 1989.',
  look='The surviving long brick building and a water tower beside the Pacific Avenue railroad tracks, with a restored Chicago and Alton depot moved behind it (as MillPictures.com reported in 2008). The City of Independence now places the National Frontier Trails Museum inside the Truman Memorial Building, 416 West Maple; a search result quoting the Historical Society says the Missouri Model Railroad Museum took over the mill building, which was not checked.',
  accn='Pacific Avenue, Independence, between South Pleasant and South Osage streets. Look from the street; whether the building is open to visitors now was not checked, so no hours are given.',
  links=[['MillPictures: Waggoner-Gates Milling Co.', 'https://www.millpictures.com/mills.php?millid=722'], ['City of Independence: National Frontier Trails Museum', 'https://www.independencemo.gov/government/city-departments/parks-rec/national-frontier-trails-museum']],
  conf='mixed', brick='yes'),

N('santa-fe-trail-park-ruts-independence-mo', 'Santa Fe Trail Park wagon ruts', 'Independence', 'kcmo', 'curio', 'traces',
  39.06655, -94.42362, 'area', 'public', 'drive', '', '1820s–1860s',
  'The park keeps about a quarter mile of Oregon, California and Santa Fe trail ruts in the middle of Independence. The National Park Service says they line up with the ruts at the Bingham-Waggoner Estate half a mile north, and that the roads between the two places show that the trails\' importance did not end when wagon traffic did.',
  look='Grassed-over ruts, called swales, with interpretive signs; the Park Service lists restrooms, picnic tables and a playground. The pin is the park, not a surveyed spot on the ruts: where exactly the ruts run was not checked.',
  accn='Managed by City of Independence Parks and Recreation, 2900 South Santa Fe Road. Open park; park hours were not checked.',
  links=[['National Park Service: Santa Fe Trail Park', 'https://www.nps.gov/places/000/santa-fe-trail-park.htm'], HOMES],
  conf='mixed', brick='no'),

N('andrew-drumm-institute-independence-mo', 'Andrew Drumm Institute (Drumm Farm)', 'Independence', 'kcmo', 'inst', 'standing',
  39.06333, -94.39389, 'area', 'view', 'drive', '', '1929',
  'The cattleman Andrew Drumm left money in his will for a home, school and farm for orphaned or poor boys; he died in 1919 and the institute opened in 1929 on a 370-acre working farm. '
  'The historic district has 10 contributing buildings, mainly living quarters and classrooms (National Register, 2006). Many farm buildings were lost later, and a golf course now covers 209 acres of the land. It is now the Drumm Farm Center for Children.',
  look='A working children\'s center: look only from public roads. Which buildings are visible from the road was not checked, and the pin is approximate.',
  accn='Private and in use by Drumm Farm Center for Children; not open to visitors as far as the sources say. Ask the center before going on the grounds.',
  links=[W('Andrew Drumm Institute'), NRHP],
  conf='mixed', brick='?'),
]

PIN_NOTES={
'vaile-mansion-independence-mo':'Coordinate from the Wikipedia infobox, then moved about 50 m south onto the mansion as the aerial shows it.',
'bingham-waggoner-estate-independence-mo':'The National Register list coordinate fell on the parking lot; moved about 85 m northeast onto the mansion as the aerial shows it.',
'jackson-county-1859-jail-independence-mo':'Coordinate from Wikipedia and the National Register list for 217 North Main Street; checked on the aerial.',
'truman-home-independence-mo':'Coordinate from Wikipedia for the Truman Home; the Noland Home is across the street. Parking point is near the visitor center on Main Street.',
'truman-courthouse-independence-mo':'Coordinate from Wikipedia for the courthouse on Independence Square; checked on the aerial.',
'truman-depot-independence-mo':'Coordinate from Wikipedia for the station; checked on the aerial.',
'trinity-episcopal-church-independence-mo':'OpenStreetMap places the church at 409 North Liberty Street; the Wikipedia coordinate fell on a parking lot, so the pin is on the church building seen on the aerial.',
'stone-church-independence-mo':'Coordinate from Wikipedia for 1012 West Lexington Avenue; checked on the aerial.',
'waggoner-gates-mill-independence-mo':'Coordinate is an OpenStreetMap address match for 318 West Pacific Avenue; checked on the aerial.',
'santa-fe-trail-park-ruts-independence-mo':'The pin is the park as OpenStreetMap maps it, not the ruts; the park may need a better spot once the ruts can be seen.',
'andrew-drumm-institute-independence-mo':'Coordinate from the National Register list; the pin marks the institute area only.',
}

BATCH={'key':'kcmo_ind_wvxq','label':'Independence, Missouri','added':'2026-11-23 11:48'}
