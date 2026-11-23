# November 23, 2026: Elgin, Illinois, from the names in one walk-through video of the town's old buildings.
# The video was only a list of names to look up; every fact here comes from a source opened while writing:
# Wikipedia read as raw text, the Elgin Heritage Commission's plaque pages (historicelgin.com), the Elgin History
# Museum's own visit page, St. John's Lutheran Church's own pages, the Unitarian Universalist Church of Elgin's
# history page, and the 2014 National Register form for the Elgin Downtown Commercial District.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
HE='Elgin Heritage Commission: '
DT=L('National Register form: Elgin Downtown Commercial District (2014)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/14001067_text')

BATCH={'key':'elgin_abst','label':'Elgin, Illinois','added':'2026-11-23 08:39'}

PLACES=[
N('old-main-elgin-academy','Old Main, Elgin Academy (Elgin History Museum)','Elgin','il','civic','standing',42.04117,-88.27784,'exact','open','walk','','1855–1856',
  'The Elgin Academy was chartered by the Illinois legislature in 1839, four years after the town was founded, as a school open to students of every denomination. Its first building, Old Main, was finished in 1856 at a cost of $19,000, to a Greek Revival design by J. Quigley, an architect from Buffalo, New York; the principal\'s family lived in the east wing and boarders in the west. The academy sold it to the city for $1 in the early 1970s, and after a rehabilitation in the late 1980s it became the Elgin History Museum. The academy itself closed in 2024.',
  'A three-story brick and limestone building with a low gabled roof, pediments, a portico of free-standing Doric columns and a domed bell tower; the museum compares its look to Illinois\'s third state capitol. Inside are the museum\'s exhibits on three floors, reached by an elevator. Two Union cannons on the grounds carry the names of 153 Civil War veterans connected with the academy.',
  'An 1856 Greek Revival schoolhouse that is now the town\'s history museum.',
  'Elgin History Museum, 360 Park Street. Adult admission $5; under 18s, teachers with identification and members free (museum page, read November 2026). The museum shares a parking lot with the academy grounds, with marked spaces closest to the building. The back entrance is step-free: ring the bell or call 847-742-4248.',
  [W('Elgin Academy (Elgin, Illinois)'),L('Elgin History Museum: plan your visit','https://elginhistory.org/hours-and-location/')],
  brick='?',hours='Wednesday to Saturday 11 a.m. to 4 p.m.'),

N('fire-barn-5-elgin','Fire Barn No. 5','Elgin','il','civic','standing',42.02581,-88.2695,'exact','open','walk','','1903–1991',
  'Elgin\'s fifth fire station, finished in 1903 for $6,262 to a Classical Revival design by the local architect Smith Hoag, at Arlington Avenue and St. Charles Street. Horses and the engine were kept downstairs, the men slept upstairs and slid down a brass pole, and hay was stored in the third-floor loft. It closed in the Great Depression, when the sculptor Trygve Rovelstad briefly used it as a studio, reopened in 1939 and served until 1991, the year it was listed on the National Register.',
  'Blond brick with red brick at the lintels and corners, a hipped roof with a domed octagonal wooden cupola that held the bell, a bay window over the apparatus door (the door itself was replaced for bigger engines) and a half-round stained glass window on the east side. It is now a fire museum; Wikipedia says it holds a Silsby steam engine used at the Great Chicago Fire of 1871. Interior not checked.',
  'A horse-era fire barn with its sliding pole and hayloft, now a fire museum.',
  'Elgin Fire Barn No. 5 Museum, 533 St. Charles Street. No page of the museum\'s own could be read when this was written, so opening days were not checked: ring ahead or look for a current notice before going. Parking was not checked.',
  [W('Fire Barn 5 (Elgin, Illinois)')],
  brick='some',hours='?'),

N('first-universalist-church-elgin','First Universalist Church (the watch church)','Elgin','il','worship','standing',42.03586,-88.28043,'site','view','walk','','1892',
  'Built in 1892 for a Universalist congregation whose first church, Unity Hall, stood on the same lot from 1866. The design is credited to George Hunter, a church member and one of the watchmakers who had come west to start the Elgin watch factory, who meant the building to look like a pocket watch: the many-sided body is the case, the roof the cover, the choir loft the hinge and the tower the stem, with the pulpit where twelve o\'clock would be. The congregation sold the building in 1979 and now meets elsewhere in Elgin.',
  'A two-story Richardsonian Romanesque church of sixteen sides under a tent-shaped roof, with a round tower and conical roof on a triangular lot at Villa and DuPage Streets. The arched windows hold their original stained glass. It is listed on the National Register (1980). Who uses it now, and whether it ever opens, was not checked; look from the street.',
  'A church built to look like a pocket watch, in the watch-factory town.',
  'At 55 Villa Street, on the triangle where Villa and DuPage Streets meet. The congregation that built it sold it in 1979 (its own history page); the present owner was not checked, so look from the public sidewalk.',
  [W('First Universalist Church (Elgin, Illinois)'),L('Unitarian Universalist Church of Elgin: history','https://uuce.org/about/uuce-history/')],
  brick='?',hours=''),

N('elgin-tower-building','Elgin Tower Building (Home Banks Building)','Elgin','il','civic','standing',42.03751,-88.2843,'exact','view','walk','','1925–1929',
  'Elgin\'s first and tallest skyscraper, built for the Home National Bank on Fountain Square, where the bank\'s older building had stood, to an Art Deco design by the St. Louis architect Wilbert G. Knoebel. It was finished in May 1929, months before the stock market crash; the Register form gives the building dates as March 1925 to May 1929. It fell on hard times again after the watch factory closed in 1965, was restored by its owner William R. Stickling, lost its wood-lined elevator to arson in 2014, and was turned into apartments after a sale in 2016.',
  'A fifteen-story stepped tower of reinforced concrete faced in limestone and granite, with two-story wings along Grove and Douglas Avenues, zigzag Art Deco detail and carving on the limestone base. The height is given as 186 feet by Wikipedia and 168 feet by the Register form. It is listed on the National Register (2002) and stands in the downtown historic district. Now apartments, so the inside is private.',
  'A 1929 Art Deco bank tower that opened just before the crash.',
  'At 100 East Chicago Street, on Fountain Square downtown. Private apartments: look from the street. A parking lot is mapped on OpenStreetMap about 100 m south on South Grove Avenue; who may use it was not checked.',
  [W('Elgin Tower Building'),L(HE+'Elgin Tower Building','https://historicelgin.com/elgin-tower-building'),DT],
  brick='?',hours='',conf='mixed'),

N('lords-park-pavilion-elgin','Lords Park Pavilion','Elgin','il','inst','standing',42.03893,-88.26171,'exact','public','walk','','1898',
  'Lords Park began in 1892 with land given by George P. and Mary Lord. Its first pavilion, put up in 1896 and 1897, burned in a fire a few months after it opened, and the present pavilion was built in a similar style and opened in 1898. It was renovated in 1993. The statue of a boy and girl under an umbrella by the fountain was first given in 1897 by workers at the David C. Cook Publishing Company and was restored with its fountain in 1998.',
  'A two-story Victorian pavilion by the park\'s lagoons and fountains, still used for receptions and public events. The park also holds a small zoo and the Elgin Public Museum, a natural history museum begun in 1906 to hold the Lords\' collections. Interior not checked.',
  'A park pavilion rebuilt in 1898 after the first one burned.',
  'In Lords Park, a City of Elgin park, at 100 Oakwood Boulevard (OpenStreetMap). The grounds are open park; the pavilion is let for events, so the inside may be closed. Park hours and parking were not checked.',
  [L(HE+'Lords Park Pavilion','https://historicelgin.com/lords-park-pavilion'),L(HE+'Lords Park','https://historicelgin.com/lords-park')],
  brick='?',hours=''),

N('old-gail-borden-library-elgin','Old Gail Borden Public Library','Elgin','il','civic','standing',42.03825,-88.28263,'site','view','walk','','1870s; library 1894–1968',
  'David Scofield\'s house of the 1870s, bought in 1892 by Alfred B. and Samuel M. Church, stepsons of Gail Borden, the inventor of condensed milk, and turned into the town\'s library in his memory. The architect W. W. Abell kept the brick house and added two wings, finishing in 1894 at a cost of $15,000. The library moved out in 1968; Ackemann\'s department store used the building until 1985, when it became a restaurant. The heritage commission calls it the only building left from that era of Elgin\'s public buildings.',
  'A two-story Richardsonian Romanesque brick building with terra cotta at the cornice, a terra cotta laurel swag and copper banding, and the words "Gail Borden Public Library" in terra cotta on the east side. The commission says it has been little altered since 1894. Its present use was not checked; look from the street.',
  'A library made out of a mansion, named for the man who invented condensed milk.',
  'At 50 North Spring Street, in the downtown historic district. Private: look from the street. Parking not checked.',
  [L(HE+'50 N. Spring Street','https://historicelgin.com/50-n-spring-street'),W('Gail Borden Public Library District'),DT],
  brick='?',hours=''),

N('david-c-cook-mansion-elgin','David C. Cook Mansion','Elgin','il','landmark','standing',42.03882,-88.27569,'site','view','walk','','1885',
  'A twelve-room Chateauesque house built in 1885 for $10,000 for David C. Cook, whose Sunday school papers grew into the David C. Cook Publishing Company, the country\'s largest interdenominational religious publisher; he moved the firm from Chicago to Elgin, and in 1901 to the Fox River at 850 North Grove. The Cook family lived here until 1945. The house later served for many years as a health center, and the heritage commission\'s page describes it as standing empty.',
  'Elaborate dormers and roof shapes and many of the original stained glass windows survive, with later additions the commission calls unsympathetic. A 2013 photograph shows the house painted white with a green roof. Private: look from the street.',
  'The publisher\'s chateau, empty for years.',
  'At 105 North Gifford Street, a private house. Look from the public sidewalk. Its present owner and condition were not checked.',
  [L(HE+'105 N. Gifford Street','https://historicelgin.com/105-n-gifford-street')],
  brick='no',hours=''),

N('selz-schwab-shoe-factory-elgin','Congdon Avenue Shoe Factory (Selz, Schwab and Company)','Elgin','il','industry','standing',42.05725,-88.26641,'exact','view','walk','','1891',
  'A shoe factory built in 1891 for $32,000 by W. W. Wright for George Ludlow and George Keep, who moved their works from Chicago. The firm failed after the hard times of 1893, and from 1897 the Chicago shoemakers Selz, Schwab and Company ran it for 32 years, carrying on even after the Palm Sunday tornado of 1920 tore off the roof; they closed after the crash of 1929. A chair maker, a metal shop and a state highway sign shop followed, and in 1999 the building was made into lofts.',
  'A long masonry factory with a center gable and two matching wings, a hipped center roof with four dormers, and double-hung windows in groups under soldier-course lintels. The grand front stair seen in old photographs is gone. Private lofts: look from the street.',
  'An 1891 shoe factory that survived a tornado, now lofts.',
  'At 618 to 644 Congdon Avenue, now private homes. Look from the street. The pin is on the long factory building.',
  [L(HE+'618-644 Congdon Avenue','https://historicelgin.com/618-644-congdon-avenue')],
  brick='?',hours=''),

N('elgin-watch-observatory','Elgin National Watch Company Observatory','Elgin','il','industry','standing',42.03024,-88.27379,'exact','view','walk','','1910',
  'Built in 1910 by the Elgin National Watch Company, two blocks east of its factory, to take time from the stars to a tenth of a second so that its watches could be set true; from 1926 it also sent time signals by short-wave radio. The company gave it to the local school district in 1960, which added a planetarium in 1963. The vast watch factory itself was pulled down in the 1960s, and this is one of the few buildings of the company left. It is listed on the National Register (1994).',
  'A two-story domed octagon of concrete covered in sheet metal, with a slit and half-ton steel shutters for the transit telescope, and a small office wing where the astronomers slept. Wikipedia says the clock vault, a Warner & Swasey transit instrument and a 1947 radio transmitter are still inside, with the 1963 planetarium at the back. Whether the school district opens it to the public was not checked.',
  'Where the watch company read the time from the stars.',
  'At 312 Watch Street; School District U-46 owns it. Look from the street unless the district\'s page says it is open. A lot about 125 m west on Raymond Street is mapped on OpenStreetMap; who may use it was not checked.',
  [W('Elgin National Watch Company Observatory')],
  brick='?',hours=''),
]

PIN_NOTES={
 'old-main-elgin-academy':'OpenStreetMap point for the Elgin History Museum, 360 Park Street; on the aerial it sits on the building on the hilltop grounds.',
 'fire-barn-5-elgin':'OpenStreetMap point for the Elgin Fire Barn Number 5 Museum, 533 St. Charles Street.',
 'first-universalist-church-elgin':'OpenStreetMap address point for 55 Villa Street. On the aerial it falls at the road edge by the triangle where Villa and DuPage Streets meet; the church itself could not be picked out with certainty, so the pin marks the site.',
 'elgin-tower-building':'OpenStreetMap point for the Elgin Tower Building, 100 East Chicago Street.',
 'lords-park-pavilion-elgin':'OpenStreetMap building mapped as Lords Park Pavilion, 100 Oakwood Boulevard.',
 'old-gail-borden-library-elgin':'OpenStreetMap address point for 50 North Spring Street. On the aerial it falls on the street in front of the block; which roof is the library could not be told, so the pin marks the site.',
 'david-c-cook-mansion-elgin':'OpenStreetMap address point for 105 North Gifford Street. On the aerial it falls on the street edge in front of the house; the pin marks the site.',
 'selz-schwab-shoe-factory-elgin':'Started from the OpenStreetMap address point for 630 Congdon Avenue, then moved about 38 m north onto the long building with a center block and two wings seen on the aerial, which matches the heritage commission\'s description.',
 'elgin-watch-observatory':'OpenStreetMap building mapped as the Elgin National Watch Company Observatory, 312 Watch Street.',
}
