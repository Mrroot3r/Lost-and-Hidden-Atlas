# Kansas City, Missouri: 18th and Vine and the east side (Historic Northeast, Scarritt Point, Swope Park), November 24, 2026.
# Part of filling in the Kansas City area on purpose for a local researcher. The Atlas had none of these places.
# Facts from the linked sources only: two National Register forms read as text (Independence Boulevard Christian Church,
# Edward A. Stevens House), Wikipedia read as raw text, the African American Heritage Trail of Kansas City, Clio entries,
# the city parks pages, KCUR, the Pitch, and the pages of the Black Archives and the American Jazz Museum for hours.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_evnk', 'label': 'Kansas City: 18th and Vine and the east side', 'added': '2026-11-24 22:58'}

PLACES = [
N('independence-boulevard-christian-church-kc', 'Independence Boulevard Christian Church, Kansas City', 'Kansas City', 'kcmo', 'worship', 'standing',
  39.10570, -94.54638, 'exact', 'view', 'drive', '', '1904–1919',
  'A large Beaux-Arts church of stone at the corner of Independence and Gladstone boulevards, built in two stages (1904–1905 and 1909–1910) with a bell tower added in 1919. Henry Hoit was the architect. '
  'The congregation traces back to 1886, and the lumber baron R. A. Long paid much of the cost of the 1905 building. It was listed on the National Register of Historic Places in 2015.',
  look='A symmetrical front with colonnaded pediments and classical ornament, an east dome sheathed in copper, and a bell tower. The Register form says the inside is just as rich, with mosaic floors, fine woodwork and stained-glass windows in the sanctuary made by Tiffany studios. '
       'The form does not say when visitors may go in.',
  accn='A working church at 606 Gladstone Boulevard, on the corner with Independence Boulevard. Look from the sidewalk. The church\'s page names a weekly meal and community programme and room hire but gives no service times or visiting hours, so ask the church before planning to go inside. Street parking.',
  links=[['National Register form (National Park Service)', 'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/14001158_text'], ['Independence Boulevard Christian Church (own page)', 'https://ibcckc.org']],
  brick='?', conf='mixed'),

N('edward-stevens-house-scarritt-point-kc', 'Edward A. Stevens House, Gladstone Boulevard, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.11522, -94.54194, 'exact', 'view', 'drive', '', '1902',
  'A Colonial Revival house on the Missouri River bluff at Scarritt Point, designed and built in 1902 by Loren Grant Middaugh for Edward A. Stevens, who died within weeks of the family moving in. '
  'Its widow later refused a neighbour, the lumber baron Robert A. Long, who wanted the lot for the gardens of his own mansion, Corinthian Hall. The house and its carriage house count toward the Scarritt Point North historic district (1997) and were listed on their own in 2016.',
  look='A tall columned portico in the Greek or Palladian manner, tan brick walls with natural rock and rusticated limestone, and a red clay tile roof. The Register form says the outside has changed very little. Inside, it describes a grand hall with a coffered ceiling, fluted pilasters and a large stained-glass window of Stevens\'s daughter Aileen as a goddess. '
       'A detached carriage house was built to hold both horses and motor cars. The house stands just east of the approach to Cliff Drive and the Kansas City Museum (Corinthian Hall).',
  accn='Private property at 3223 Gladstone Boulevard; look from the public sidewalk on the boulevard. Interior not open as far as the form says. Street parking; the Kansas City Museum and North Terrace Park are close.',
  links=[['National Register form (National Park Service)', 'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/16000736_text']],
  brick='no'),

N('gem-theater-18th-vine-kc', 'Gem Theater, 18th and Vine, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.09092, -94.56263, 'exact', 'view', 'drive', '', '1912',
  'Built in 1912 as the Star Theater by the Shriner and Powellson Amusement Company, to a design by George Carman, as a silent-movie house for Kansas City\'s Black community. It became the Gem in 1913 and was remodelled in 1924 to seat 1,238. It stopped showing films in 1960. '
  'When 18th and Vine was revived in the 1980s the Gem was the centrepiece, and in the 1990s the inside was rebuilt as a modern theatre behind the old front.',
  look='The restored 1912 front on East 18th Street is what is left of the old building; the Heritage Trail and a Clio entry say the original interior was largely removed in the 1990s. Behind it is a 500-seat performing-arts hall that runs concerts and plays.',
  accn='Part of the American Jazz Museum complex at 1615 East 18th Street. The theatre is open for ticketed events; no set visiting hours were found, so look at the front from the street. The museum next door has its own hours (see the American Jazz Museum\'s page). Street parking.',
  links=[['African American Heritage Trail: Gem Theater', 'https://aahtkc.org/gemtheater'], ['Clio: Gem Theater', 'https://theclio.com/tour/2171/6'], ['American Jazz Museum: Gem Theater', 'https://americanjazzmuseum.org/gem-theater']],
  brick='?'),

N('eblon-theater-facade-18th-vine-kc', 'Eblon Theater facade (Cherry Blossom Club), Vine Street, Kansas City', 'Kansas City', 'kcmo', 'civic', 'ruins',
  39.09027, -94.56357, 'exact', 'view', 'drive', '', '1923–1984',
  'Kansas City\'s first movie theatre owned by a Black man, built by Homer "Jap" Eblon in 1923 as a two-storey Spanish-style brick building with about 1,000 seats. Count Basie played its organ for silent films. '
  'In 1933 it became the Cherry Blossom Club, where Basie led his first band; later it was the Roby Theater, a bowling alley and the Chez Paree club, and it stood empty from 1960. A fire in 1984 destroyed the auditorium. Only the front wall was saved.',
  look='A Spanish Colonial front wall with a red doorway, still standing on Vine Street among other old storefronts that were dressed as film sets for a 1990s movie. KCUR reported in 2016 that plans for this block would keep the facades. Whether that work was done, and what stands behind the wall now, was not checked.',
  accn='Public street (Vine Street at 18th). Look from the sidewalk; the building is closed. Street parking.',
  links=[['African American Heritage Trail: Eblon Theater', 'https://aahtkc.org/eblontheater'], ['Clio: Eblon Theater and Cherry Blossom Club', 'https://theclio.com/entry/150328'], ['KCUR: historic buildings near 18th and Vine (2016)', 'https://www.kcur.org/arts-life/2016-06-06/historic-buildings-near-18th-and-vine-may-get-the-memphis-facade-treatment']],
  brick='?', conf='mixed'),

N('black-archives-parade-park-building-kc', 'Parade Park Maintenance Building (Black Archives of Mid-America), Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.09216, -94.56119, 'exact', 'open', 'drive', '', '1912',
  'A limestone park building of 1912 at the southeast corner of Parade Park, designed by Arthur L. Sparks. It held the parks department\'s horses, wagons, a repair shop and storage, and was first built as a rectangle round a courtyard. It served the parks system into the 1960s. '
  'It was listed on the National Register of Historic Places in 2008, and the Black Archives of Mid-America moved in from a nearby fire station in 2012. Only the north and west wings are left of the original plan.',
  look='A two-storey Mission Revival building of local limestone, with a historical marker on its east side. Inside is the Black Archives\' permanent exhibit, "With My Eyes No Longer Blind", on African Americans in Kansas City from the Lewis and Clark era to the 1990s.',
  accn='The archives are at 1722 East 17th Terrace (the Horace M. Peterson III Building), in the 18th and Vine district; hours are from the archives\' own visit page, but another listing says visits are by appointment, so call 816-221-1600 first. Street parking.',
  links=[['Clio: Parade Park Maintenance Building marker', 'https://theclio.com/entry/158312'], W('Parade Park Maintenance Building'), ['Black Archives: plan a visit', 'https://blackarchives.org/plan-a-visit/'], ['African American Heritage Trail: Black Archives', 'https://aahtkc.org/blackarchivesofmidamerica']],
  hours='Monday to Friday 9 a.m. to 5 p.m.; Saturday and Sunday by appointment (call 816-221-1600; one listing says appointment only)', brick='no'),

N('swope-park-shelter-5-kc', 'Swope Park Shelter No. 5 ("Watermelon Hill"), Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.00783, -94.53086, 'site', 'public', 'drive', '', '1940s',
  'A plain picnic shelter of rough stone pillars under a shingled roof, built in the early 1940s (one account says between 1940 and 1942) as part of a parks building plan. '
  'For about the first fifteen years it was the only shelter in all of Swope Park that Black residents could use, because the park was segregated, and the grassy slope round it got the name "Watermelon Hill", which many remember with mixed feelings.',
  look='A low, open shelter with six picnic tables on Zoo Drive, between Starlight Theatre and the Kansas City Zoo. There is nothing grand to see; the interest is the story, which the African American Heritage Trail tells on its page. The sources do not say whether a sign marks it.',
  accn='City park land (Kansas City Parks and Recreation), at 6700 Zoo Drive. Free to look at; parking in the zoo and Starlight lots, which may charge on event days and are not the park\'s alone.',
  links=[['African American Heritage Trail: Swope Park Shelter No. 5', 'https://aahtkc.org/swope-park-shelter-5'], ['Clio: Swope Park Shelter No. 5', 'https://theclio.com/tour/2384/11']],
  hours='?', brick='?'),

N('thomas-swope-memorial-swope-park-kc', 'Thomas H. Swope Memorial, Swope Park, Kansas City', 'Kansas City', 'kcmo', 'curio', 'standing',
  39.00157, -94.51671, 'exact', 'public', 'drive', '', '1918',
  'A colonnade of Bethel white granite on a hill in Swope Park that is also the tomb of Thomas H. Swope, who gave Kansas City about 1,300 acres in 1896. He died in 1909 and lay in a holding vault until the memorial was finished; his remains were placed here on April 8, 1918. '
  'It appears to follow a design George Kessler drew in 1915, and the lions and bronze work are by Charles Keck.',
  look='A U-shaped Greek Doric colonnade of twelve 14-foot columns round a stone court, with the inscription "Reader, if you would see his monument, look about you" in Latin, eight bronze medallions of the park\'s trees, and two big recumbent lions at the stairs. West of it, on the bluff edge, a balustrade and a fountain in a half-round pool were added later (1923, says Clio).',
  accn='City park land (Kansas City Parks and Recreation), 6900 Swope Memorial Drive, beside the golf course. The parks page gives its hours as "when the golf course is open".',
  links=[['Kansas City Parks: Thomas H. Swope Memorial', 'https://kcparks.org/?p=7085'], ['Clio: Thomas H. Swope Memorial', 'https://theclio.com/tour/2384/14']],
  hours='When the golf course is open', brick='no'),

N('tiffany-castle-pendleton-heights-kc', 'Tiffany Castle, Garfield Avenue, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.11382, -94.55765, 'exact', 'view', 'drive', '', '1908–1909',
  'A Tudor-style stone castle on the Missouri River bluff, built for the eye doctor Flavel B. Tiffany, who had seen castles in England and Scotland. Wikipedia gives both 1908 and 1909 as the year it was finished. '
  'Its floors and roof are reinforced concrete and the walls solid stone from a quarry at Second and Lydia. Tiffany also founded Tiffany Springs in Platte County, planned as a rival to Excelsior Springs.',
  look='A castle front with battlements and a tower, seen best from Garfield Avenue and from the bluff trails below; it can be seen for miles from the bottoms. The inside was not checked.',
  accn='A private home at 100 Garfield Avenue (ownership has changed several times; Wikipedia lists sales and a 2013 news report of it for sale). Look from the public street only. The house sometimes appears on the neighbourhood\'s holiday home tour; the neighbourhood association announces dates.',
  links=[W('Tiffany Castle'), W('Pendleton Heights, Kansas City')],
  brick='no'),

N('cliff-drive-kessler-park-kc', 'Cliff Drive and Kessler Park, Kansas City', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.11401, -94.55351, 'area', 'public', 'walk', '', '1900s',
  'A 4.3-mile scenic road along the limestone bluffs above the Missouri River bottoms, laid out by the landscape architect George Kessler as part of the city\'s park and boulevard plan on land bought from the estate of the Rev. Nathan Scarritt about 1900. '
  'It was named a Missouri State Scenic Byway on June 2, 2000, the only one in an urban area. It is now closed to motor vehicles.',
  look='A paved road through woods and wildflowers, with the bluff on one side and old mansions of the Historic Northeast on the other, running from The Paseo near Independence Avenue east to Indian Mound at Gladstone and Belmont boulevards. North Terrace Lake and a fountain sit by the west end. Rock climbers use the bluffs.',
  accn='City park (Kansas City Parks and Recreation). The parks page says it is closed to motor vehicles and gives its hours as 5 a.m. to midnight every day. A 2014 news story said it was gated to cars only on weekends, so the parks page is the later word. Park at North Terrace Park or on nearby streets.',
  links=[['Kansas City Parks: Cliff Drive', 'https://kcparks.org/?p=7395'], ['KCUR: Cliff Drive began with an aristocratic Kansas City family', 'https://www.kcur.org/post/cliff-drive-began-aristocratic-kansas-city-family']],
  hours='5 a.m. to midnight daily; closed to motor vehicles', brick='?'),

N('heim-fire-station-20-east-bottoms-kc', 'Heim Fire Station No. 20, East Bottoms, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.11920, -94.54914, 'exact', 'view', 'drive', '', '1903',
  'A firehouse built in 1903 by the Heim Brewing Company, then the biggest brewer in Kansas City, for its own brewery district in the East Bottoms; the city fire department later took it as Station No. 20. It was listed on the National Register of Historic Places in 2024. '
  'Boulevard Brewing\'s founder bought it in 2013 and, with a contractor, turned it into the headquarters of Bottoms Up Collective, an effort to revive the East Bottoms.',
  look='The Pitch reported in 2015 that the fire pole is still in the second-floor office. The Heim bottling plant (built in 1901) stands near the railroad tracks on Montgall Avenue and has its own entry. What the outside looks like was not checked in a source.',
  accn='A private building at Guinotte and Montgall avenues; look from the street. Its use today was not checked after the 2015 article.',
  links=[['The Pitch: In the East Bottoms, John McDonald sets out to brew the future (2015)', 'https://www.thepitchkc.com/?p=1961']],
  brick='?', conf='mixed'),

N('pendleton-heights-historic-neighborhood-kc', 'Pendleton Heights historic neighborhood, Kansas City', 'Kansas City', 'kcmo', 'town', 'standing',
  39.11000, -94.55444, 'area', 'public', 'drive', '', '19th century',
  'Kansas City\'s first developed suburb and, after Quality Hill, its second-oldest neighbourhood planned for houses, platted in the late 1800s from the 200-acre Jones farm. Wikipedia says it has the most true Victorian houses in the city. '
  'It also holds the original city reservoir and part of Cliff Drive, and was named one of the best old-house neighbourhoods in the Midwest by This Old House in 2013.',
  look='Streets of Italianate, Queen Anne, Eastlake, Richardsonian Romanesque, Beaux-Arts and Craftsman houses between The Paseo and Chestnut Trafficway. Look for Tiffany Castle on the bluff, the Philip E. Chappell house at 1836 Pendleton Avenue (listed in 1990), and three small parks. '
       'The neighbourhood\'s home tour is the first Saturday of December, with some houses open that day.',
  accn='City streets (public right of way), with private houses; look from the sidewalk. Street parking. Check the neighbourhood association\'s page for the December tour.',
  links=[W('Pendleton Heights, Kansas City')],
  brick='?', conf='mixed'),

N('eighteenth-vine-historic-district-kc', '18th and Vine Historic District, Kansas City', 'Kansas City', 'kcmo', 'town', 'standing',
  39.08889, -94.56111, 'area', 'public', 'drive', '', '20th century',
  'The old hub of Kansas City\'s Black community, where covenants and deed restrictions kept Black residents from moving south of 27th Street for the first half of the 1900s, so that more than 600 businesses, hotels, theatres and restaurants grew up here. '
  'It was also the birthplace of Kansas City jazz in the 1920s and 1930s. The National Register listed a historic district of 35 contributing buildings in 1991.',
  look='A few blocks of surviving buildings: the Gem Theater front, the facade of the Eblon Theater on Vine Street, the Kansas City Call at 1715 East 18th Street, the Mutual Musicians Foundation, and the Black Archives nearby. Film facades from a 1990s movie stayed on some old buildings for years. Each has its own entry or a sign.',
  accn='City streets (public right of way); look from the sidewalk. The American Jazz Museum (1616 East 18th Street) and the Black Archives are open at set times; see their entries. Street parking.',
  links=[W('18th and Vine'), ['African American Heritage Trail: 18th and Vine', 'https://aahtkc.org/18thandvine'], ['American Jazz Museum: plan a visit', 'https://americanjazzmuseum.org/visit']],
  brick='?', conf='mixed'),
]

PIN_NOTES = {
 'independence-boulevard-christian-church-kc': 'From an address lookup that fell on the building, matching the Register list point; checked on the aerial.',
 'edward-stevens-house-scarritt-point-kc': 'The Register list\'s point, checked on the aerial.',
 'gem-theater-18th-vine-kc': 'From an address lookup for 1615 East 18th Street; checked on the aerial.',
 'eblon-theater-facade-18th-vine-kc': 'From an address lookup for 1822 Vine Street; checked on the aerial.',
 'black-archives-parade-park-building-kc': 'Wikipedia\'s point for the building; checked against an address lookup for 1722 East 17th Terrace and the aerial.',
 'swope-park-shelter-5-kc': 'From an address lookup for 6700 Zoo Drive. The shelter itself could not be picked out on the aerial, which shows a lawn beside the zoo parking lot there, so the pin marks the site and not the roof.',
 'thomas-swope-memorial-swope-park-kc': 'From an address lookup for 6900 Swope Memorial Drive; checked on the aerial.',
 'tiffany-castle-pendleton-heights-kc': 'Wikipedia\'s point, matching an address lookup for 100 Garfield Avenue; checked on the aerial.',
 'cliff-drive-kessler-park-kc': 'A point in North Terrace Park near the west end of the drive, moved there from a first guess that fell on houses; the byway runs about 4 miles, so the pin marks a general area.',
 'heim-fire-station-20-east-bottoms-kc': 'The Register list\'s point, matching an address lookup for 2701 Guinotte Avenue; checked on the aerial.',
 'pendleton-heights-historic-neighborhood-kc': 'Wikipedia\'s point for the neighbourhood; the pin marks a general area.',
 'eighteenth-vine-historic-district-kc': 'Wikipedia\'s point for 18th and Vine; the pin marks a general area.',
}
