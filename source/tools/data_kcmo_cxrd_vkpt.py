# November 25, 2026: older office, warehouse and factory buildings in downtown Kansas City, the Crossroads and Hyde Park, Jackson County, Missouri.
# Part of filling in the Kansas City area on purpose for a local researcher. The Atlas had none of these buildings.
# Ground note: the ground first drawn was Lee's Summit and the country south of it, but three earlier batches had already taken
# every Register listing there that is worth a visit, so the session went to the Register listings in downtown Kansas City that no batch had added.
# Facts from the linked sources only: the Clio walking-tour pages and entries (each cites the Register form it was written from),
# the Jackson County Historical Society's article on Janssen Place, and Wikipedia read as raw text. The Register forms themselves
# could not be opened (the state's copies answer 404). Coordinates are the Register list's, checked on the aerial.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_cxrd_vkpt', 'label': 'Kansas City: older commercial and industrial buildings', 'added': '2026-11-25 11:51'}

PLACES = [
N('gumbel-building-kc', 'Gumbel Building, 801 Walnut Street', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.104302, -94.581592, 'exact', 'view', 'drive', '', '1904',
  'Built in 1904 to a design by the Kansas City architect John W. McKecknie, the Gumbel Building is described by Clio as one of the first buildings in the country built of reinforced concrete. It was office space for most of its life and was converted to a Hampton Inn, a project that began in 2014 and finished the next year. It was added to the National Register of Historic Places in 1979.',
  look='A front of square pilasters with terra-cotta decoration, topped by Roman eagles, rounded piers carved as fasces (bundles of rods) and a shield-and-wreath ornament at the top, all from Clio\'s description. Inside is now a hotel; what of the old offices survives was not checked.',
  accn='Private; a working hotel at 801 Walnut Street. Look from the sidewalk. Downtown street and garage parking. The hotel lobby is for guests; hours not checked.',
  links=[['Gumbel Building (Clio)', 'https://theclio.com/entry/157233']],
  hours='?', brick='?'),

N('baker-vawter-building-kc', 'Baker-Vawter Building (Sosland Building), 915 Wyandotte Street', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.103087, -94.585286, 'exact', 'view', 'drive', '', '1920',
  'The Baker-Vawter Company, a maker of steel filing cabinets, ledgers and loose-leaf systems, hired the Kansas City firm of Hoit, Price and Barnes in 1920 to design its western office and factory here. Remington-Rand bought the company in 1935 and stayed about fifteen years. In 1950 the Sosland family bought the building for its envelope, printing and flour-trade publishing businesses, and it was known as the Sosland Building. A 2005 renovation turned it into lofts.',
  look='Architectural historians call it a mix of commercial and industrial styles: industrial windows and doors under a terra-cotta front that was unusual for a working factory. Clio says the Baker-Vawter name is still on the side of the building.',
  accn='Private; apartment lofts ("Lofts at 917"). Look from Wyandotte Street. Downtown street and garage parking.',
  links=[['Baker-Vawter Building (Clio walking tour, stop 19)', 'https://theclio.com/tour/2310/19']],
  hours='', brick='?'),

N('dierks-building-kc', 'Dierks Building (Grand Boulevard Lofts), Grand Boulevard', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.1023, -94.5808, 'site', 'view', 'drive', '', '1909',
  'Clio says the Dierks Building was built in 1909 as an office building and enlarged upward three times, until it reached seventeen storeys. It shows how fast demand for office space grew in Kansas City and how high-rise design changed in the early twentieth century. It is on the National Register of Historic Places and is now a residential building, the Grand Boulevard Lofts.',
  look='A U-shaped brick tower with pilasters running the full height, a glass and black-aluminium shopfront nearly three storeys tall, and Art Deco ornament on the 15th to 17th floors (Clio). The pin is the Register list\'s point for the building.',
  accn='Private; apartments. Look from Grand Boulevard. Downtown street and garage parking.',
  links=[['Dierks Building (Clio downtown walking tour, stop 10)', 'https://theclio.com/tour/251']],
  hours='', brick='?'),

N('insurance-building-spalding-college-kc', 'Kansas City Insurance Building (Spalding\'s Commercial College)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.102392, -94.579256, 'site', 'view', 'drive', '', '1905',
  'Built in 1905 for Spalding\'s Commercial College, which James F. Spalding had founded in 1865 and which moved here to be near the city\'s leading businesses. Clio says more than 1,200 students attended and that Harry Truman studied there in 1901. Insurance companies took the building later, and in 1944 the Consumers Cooperative Association moved in and rebuilt the interior. Union and public-service offices followed. It is on the National Register of Historic Places.',
  look='A Chicago-style front with multi-sash windows, vertical piers and terra-cotta trim (Clio). The pin is the Register list\'s point; the exact street address was not read.',
  accn='Private; current use not checked. Look from the street. Downtown street and garage parking.',
  links=[['Kansas City Insurance Building (Clio downtown walking tour, stop 7)', 'https://theclio.com/tour/251']],
  hours='', brick='?'),

N('firestone-building-kc', 'Firestone Building (Abdiana Building), Grand Boulevard', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.088889, -94.580833, 'site', 'view', 'drive', '', '1915',
  'The Firestone Tire and Rubber Company put up this building in 1915 for $300,000, its largest investment up to then. Harvey Firestone chose Kansas City because of its farming trade and the growing use of motor vehicles on farms. Clio credits the architects Smith, Rea and Lovitt. Firestone stayed until at least 1986, the year it was listed on the National Register of Historic Places. It held a furniture store from 1997 to 2003 and is now lofts with businesses and an event space.',
  look='Reinforced concrete with terra-cotta piers and Gothic-inspired ornament; Clio calls the design conservative enough to look modern. The old Firestone sign on top was replaced by the owner\'s. The ground-floor event space keeps the Firestone logo inside.',
  accn='Private (the owner is named as Abdiana Properties in Clio). Look from Grand Boulevard. Event-space hours not checked.',
  links=[['Firestone Building (Clio)', 'https://theclio.com/entry/156437']],
  hours='', brick='?'),

N('twenty-twenty-grand-building-kc', '2020 Grand Building (Hotel Indigo)', 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.0885, -94.582, 'site', 'view', 'drive', 'hotels', '1922',
  'Built in 1922, the 2020 Grand Building shows the commercial growth in the Crossroads after Union Station opened in 1914. It is a typical two-part commercial building, with shops on the ground floor and offices above. It was added to the National Register of Historic Places in 2012 and is now a hotel, the Hotel Indigo Crossroads.',
  look='A restrained front with Prairie School touches, such as diamond shapes at the top of the pilasters. At the back is a sheltered loading dock that once stood beside the railway tracks (Clio). Inside is a hotel; the interior was not checked.',
  accn='Private; a working hotel on Grand Boulevard. Look from the sidewalk. Hours not checked.',
  links=[['2020 Grand Building (Clio Crossroads walking tour, stop 4)', 'https://theclio.com/tour/2305']],
  hours='?', brick='?'),

N('land-bank-building-kc', 'Land Bank Building, 10th Street', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.102093, -94.583686, 'exact', 'view', 'drive', '', '1924',
  'A cornerstone of the Financial District, finished in 1924 for the Kansas City Joint Stock Land Bank, the fifth bank in the country chartered under the 1916 Federal Farm Loan Act, which guaranteed loans to farmers. The business district gave the building its 1924 Gold Medal for architecture. Rothschild\'s department store stood east of it and the New England National Bank still stands to the west, with the former First National Bank (now the Central Library) across the street. It is on the National Register of Historic Places.',
  look='A 1920s bank front on 10th Street. What the inside holds, and what the building is used for now, were not checked.',
  accn='Private; look from the sidewalk. Downtown street and garage parking.',
  links=[['Land Bank Building (Clio walking tour, stop 3)', 'https://theclio.com/tour/2310']],
  hours='', brick='?'),

N('ra-long-building-kc', 'R. A. Long Building', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.102372, -94.581088, 'exact', 'view', 'drive', '', '1906',
  'Robert Alexander Long built it in 1906 as the headquarters of the Long-Bell Lumber Company, then one of the largest lumber firms in the country. Henry Hoit designed the Italian Renaissance building, which Clio calls the first steel-frame tower in Kansas City. After Long-Bell merged with International Paper in 1956, the building was bought two years later by what is now UMB Financial, which still uses it for offices. It was added to the National Register of Historic Places in 2003.',
  look='A masonry office tower in the Italian Renaissance style. The interior was not checked.',
  accn='Private; working bank offices. Look from the sidewalk. Downtown street and garage parking.',
  links=[['R. A. Long Building (Clio downtown walking tour, stop 11)', 'https://theclio.com/tour/251']],
  hours='', brick='?'),

N('stine-mcclure-undertaking-building-kc', 'Stine & McClure Undertaking Company Building', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.1025, -94.5786, 'site', 'view', 'drive', '', '1912',
  'Finished in 1912 for the Stine and McClure Undertaking Company, this is the only Egyptian Revival commercial building left in downtown Kansas City, according to Clio. It was designed by the prolific local architect John McKecknie, who also designed the Gumbel Building. The front takes its look from ancient Egyptian tombs, which suited a funeral business. It is on the National Register of Historic Places.',
  look='An Egyptian-style front of the kind that swept the United States in the nineteenth and early twentieth centuries. The pin is the Register list\'s point; the street address was not read.',
  accn='Private; current use not checked. Look from the street. Downtown street and garage parking.',
  links=[['Stine & McClure Undertaking Company Building (Clio downtown walking tour, stop 6)', 'https://theclio.com/tour/251']],
  hours='', brick='?'),

N('corrigan-building-kc', 'Thomas Corrigan Building (Corrigan Station)', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.0906, -94.5828, 'site', 'view', 'drive', '', '1921',
  'Named for the nineteenth-century businessman who built Kansas City\'s streetcar empire, this ten-storey reinforced-concrete building was finished in 1921 as an investment of Thomas Corrigan\'s four daughters. Keene and Simpson designed it for offices, light manufacturing and warehousing. It stayed in the Corrigan family until 1977. The Gateway Station post office was the main tenant from 1921 to 1931, the Donnelly Garment Company from 1935 to 1947, and the Veterans Administration until 1958. A 2015 renovation made it Corrigan Station, with shops below and offices above, close to the Main Street streetcar line.',
  look='A tall concrete loft building in the Crossroads. The interior was not checked.',
  accn='Private; offices and shops. Look from the street. Street and garage parking in the Crossroads.',
  links=[['Thomas Corrigan Building (Clio Crossroads walking tour, stop 10)', 'https://theclio.com/tour/2305']],
  hours='', brick='?'),

N('belger-cartage-building-kc', 'Belger Cartage Service building and Belger Arts Center, Walnut Street', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.08764, -94.5829, 'site', 'open', 'drive', '', '1919',
  'The brick building is the national headquarters of Belger Cartage Service, a warehousing and heavy-hauling company founded in Kansas City in 1919. Since 2000 it has also held the Belger Arts Center, which Clio says has put on more than 100 contemporary art shows drawn from the Belger Collection and from other artists.',
  look='A brick warehouse-style building in the Crossroads. Clio says the arts center is open to the public by appointment, with free guided tours; what the old building shows inside was not checked.',
  accn='The company owns the building. The arts center is open by appointment only, so write or call ahead (its own page was not opened, so the contact details are not given here). Street parking in the Crossroads.',
  links=[['Belger Cartage Service and Belger Arts Center (Clio Crossroads walking tour, stop 5)', 'https://theclio.com/tour/2305']],
  hours='?', brick='?'),

N('janssen-place-kc', 'Janssen Place, Hyde Park', 'Kansas City', 'kcmo', 'town', 'standing',
  39.06, -94.578056, 'site', 'view', 'drive', '', '1897–1917',
  'Arthur Stilwell, who founded the railroad that became the Kansas City Southern, laid out Janssen Place as an exclusive street in Hyde Park. He planted the trees, built the street and curbs and filed the plat with Westport in 1897; Westport was annexed by Kansas City later that year. Nineteen mansions went up between 1897 and 1917, built by fifteen contractors in the Queen Anne, Georgian Revival and other styles. The first two (nos. 27 and 48) were built as speculation to get the street started. The street is on the National Register of Historic Places (1976).',
  look='A short street of large early-twentieth-century houses with deep front porches. The houses are lived in, so look from the street. The Historical Society also says an annual Hyde Park homes tour is held; whether the Janssen Place houses are on it in any year was not checked.',
  accn='Private homes on a residential street, with street parking nearby. Do not go onto the lots. Whether the street itself is public or private was not checked.',
  links=[['Janssen Place (Jackson County Historical Society article)', 'https://www.jchs.org/jchs-e-journal/janssenplace']],
  hours='', brick='?'),

N('jensen-salsbery-laboratories-kc', 'Jensen-Salsbery Laboratories building', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.08778, -94.59083, 'site', 'view', 'drive', '', '1918',
  'A laboratory building of 1918 that was added to the National Register of Historic Places in 1985. Wikipedia says two Atlas figures, representing Biology and Chemistry, were carved by the Kansas City sculptor Jorgen Dreyer in 1918 and set on the third floor above the entry doors.',
  look='The two stone Atlas figures above the entrance, in a building Wikipedia classes as Prairie School. Current use and the condition of the carvings were not checked.',
  accn='Private; look from the street. The pin is the Register list\'s point and the street address was not read.',
  links=[W('Jensen-Salsbery Laboratories')],
  hours='', brick='?'),
]

PIN_NOTES = {
  'gumbel-building-kc': 'Register list coordinate for the building at 801 Walnut Street (the address Clio gives).'+' On the aerial the pin sits on a building of the right size in the right block.',
  'baker-vawter-building-kc': 'Register list coordinate; Clio gives the address as 915 to 917 Wyandotte Street.'+' On the aerial the pin sits on a building of the right size in the right block.',
  'dierks-building-kc': 'Register list coordinate.'+' On the aerial the pin sits on a building of the right size in the right block.',
  'insurance-building-spalding-college-kc': 'Register list coordinate.'+' On the aerial the pin sits on a building of the right size in the right block.',
  'firestone-building-kc': 'Register list coordinate; the Janssen Place article places the building at 2001 Grand.'+' On the aerial the pin sits on a building of the right size in the right block.',
  'twenty-twenty-grand-building-kc': 'Register list coordinate; the address is 2020 Grand Boulevard by its name.'+' On the aerial the pin sits on a building of the right size in the right block.',
  'land-bank-building-kc': 'OpenStreetMap and the Register list agree within about 20 metres.'+' On the aerial the pin sits on a building of the right size in the right block.',
  'ra-long-building-kc': 'Register list coordinate.'+' On the aerial the pin sits on a building of the right size in the right block.',
  'stine-mcclure-undertaking-building-kc': 'Register list coordinate.'+' On the aerial the pin sits on a building of the right size in the right block.',
  'corrigan-building-kc': 'Register list coordinate.'+' On the aerial the pin sits on a building of the right size in the right block.',
  'belger-cartage-building-kc': 'OpenStreetMap coordinate of the Belger Arts Center, 2100 Walnut Street.'+' On the aerial the pin sits on a building of the right size in the right block.',
  'janssen-place-kc': 'Register list coordinate for the district; OpenStreetMap puts the street about 300 metres south. On the aerial the pin sits on the tree-lined street with large houses either side.',
  'jensen-salsbery-laboratories-kc': 'Register list coordinate.'+' On the aerial the pin sits on a building of the right size in the right block.',
}
