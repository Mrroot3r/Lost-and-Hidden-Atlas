# November 26, 2026: Midtown, Hyde Park, the Country Club District and the east side, Kansas City, Missouri.
# Part of filling in the Kansas City area on purpose for a local researcher. Facts come from the linked sources only: Clio's
# "Historic Homes of Kansas City" tour and its Walt Disney tour, the Midtown KC Post, the R. A. Long Historical Society, the Kansas
# City Magazine and KC Yesterday pieces, Wikipedia read as raw text, and the Park Service's record pages. The National Register
# forms themselves could not be read (the state's copies are gone and the Park Service holds only a one-page stand-in), so what
# each entry says of the building comes from the other sources. Coordinates are the Register's points, checked on the aerial.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_mtwn_tjwe', 'label': 'Kansas City: Midtown, Hyde Park and the Country Club District', 'added': '2026-11-26 01:52'}

CLIO = ['Clio: Historic Homes of Kansas City, Midtown to Ward Parkway', 'https://theclio.com/tour/3153']

PLACES = [
N('volker-house-roselawn-kc', 'William Volker House (Roselawn)', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.06002, -94.6055, 'exact', 'view', 'drive', '', '1889',
  "William Volker, who made a fortune in picture frames, window shades and home furnishings, bought this house at 3717 Bell Street in 1889, the first home in a new suburb, and lived in it until he died in 1947. Clio and Wikipedia say he stayed in it while others of his means built large estates, which earned him the nickname \"Mr. Anonymous of Bell Street\" for his private giving. "
  "He gave away most of his fortune from 1911 and bought the Walter Dickey mansion that became the first building of the University of Kansas City. The house is on the National Register (1993).",
  look="A large Victorian house on Bell Street in the Volker neighbourhood. What the exterior is built of and whether anything of the interior survives were not checked, and no source read says whether the public can go in.",
  accn="Look from Bell Street. Who owns it now and whether it is open were not found in any source read, so it is marked view only. Street parking.",
  links=[CLIO, ['Clio: Roselawn, the estate of William Volker', 'https://theclio.com/tour/3153/7'], W('William Volker'), ['Park Service record, NRIS 93000408', 'https://npgallery.nps.gov/AssetDetail/NRIS/93000408']],
  conf='mixed', brick='some'),

N('shelley-house-hyde-park-kc', 'William Francis Shelley House', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.06177, -94.58667, 'exact', 'view', 'drive', '', '1887–1889',
  "One of the oldest houses in the Hyde Park neighbourhood, built from 1887 to 1889, before Kansas City annexed Hyde Park. The neighbourhood's plan barred businesses and required houses to cost more than $15,000. "
  "William Shelley's family was close to people such as General William Tecumseh Sherman, and his brother George Shelley was twice mayor in the late 1880s. It is on the National Register (1978).",
  look="A large late-Victorian house on its own lot at the Hanover Place end of Hyde Park. The exterior materials and the interior were not checked.",
  accn="Private; look from the public street. Street parking.",
  links=[CLIO, ['Clio: William Francis Shelley House', 'https://theclio.com/tour/3153/4'], ['Park Service record, NRIS 78001662', 'https://npgallery.nps.gov/AssetDetail/NRIS/78001662']],
  conf='mixed', brick='yes'),

N('knight-house-hyde-park-kc', 'William Baker and Mary Knight House', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.0622, -94.58493, 'exact', 'view', 'drive', '', '1890',
  "Completed in summer 1890 for the railway and canal engineer William Baker Knight, who died that year at 42 of injuries from a train crash, and his wife Mary. Clio calls it a Queen Anne house with masonry and half-timbering, both unusual for that style, and says it had voice tubes for talking between rooms and floors. "
  "It was one of the first grand houses in Hyde Park. It is at 3534 Walnut Street and on the National Register (2003).",
  look="A Victorian Queen Anne house with masonry and half-timbered work. The interior was not checked.",
  accn="Private house on Walnut Street; look from the public sidewalk. Street parking.",
  links=[CLIO, ['Clio: William Baker and Mary Knight House', 'https://theclio.com/tour/3153/3'], ['Park Service record, NRIS 03001054', 'https://npgallery.nps.gov/AssetDetail/NRIS/03001054']],
  brick='?'),

N('mcintire-house-armour-blvd-kc', 'Levi McIntire House, Armour Boulevard', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.06376, -94.57588, 'exact', 'view', 'drive', '', '1911',
  "A single-family house of 1911 at 710 East Armour Boulevard, one of the few left on a street that filled with mansions and then apartment hotels by the 1920s. Its first resident, Levi McIntire, worked in real estate; the architects were Keene and Simpson. "
  "Some real-estate listings give 1908; the National Register record and Clio give 1911. It was listed in 1983.",
  look="A 1911 house among the apartment blocks of Armour Boulevard. Exterior materials and interior were not checked.",
  accn="Private; look from the sidewalk. Street parking along Armour Boulevard.",
  links=[CLIO, ['Clio: Levi McIntire House', 'https://theclio.com/tour/3153/1'], ['Park Service record, NRIS 83001011', 'https://npgallery.nps.gov/AssetDetail/NRIS/83001011']],
  conf='mixed', brick='?'),

N('loose-mansion-armour-blvd-kc', 'Jacob and Ella Loose House (Loose Mansion)', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.06351, -94.5844, 'exact', 'open', 'drive', '', '1911',
  "Built in 1911 for Jacob and Ella Loose, whose Loose-Wiles Biscuit Company made Sunshine crackers and the Hydrox cookie. Clio says Ella chose George Oakley Totten, who had designed several legation buildings in Washington, and the four-storey house took two years to finish. "
  "Ella later gave nearly eighty acres for Loose Park. Clio says the house is now an event space and bed and breakfast. It is on the National Register (1983).",
  look="A four-storey mansion built for large parties at 101 East Armour Boulevard. The house's own website was not read, so what is kept inside and the opening times are not given.",
  accn="Run as an event venue and bed and breakfast, so the public goes in by booking or at its events; its own page was not read and no hours are given. Look from Armour Boulevard. Street parking.",
  links=[CLIO, ['Clio: Jacob and Ella Loose House', 'https://theclio.com/tour/3153/2'], ['Park Service record, NRIS 83001008', 'https://npgallery.nps.gov/AssetDetail/NRIS/83001008']],
  conf='mixed', brick='yes', hours='?'),

N('christian-church-hospital-kc', 'Christian Church Hospital (Robinson Memorial Hospital)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.08085, -94.5651, 'exact', 'view', 'drive', '', '1916',
  "The lumber baron Robert A. Long gave $200,000 toward this hospital, which opened in April 1916 just west of Troost Park; church members raised another $150,000 so a third of the beds would go to charity patients. Long meant it as part of a plan to make Kansas City the national home of the Christian Church, with buildings by the architect Henry Hoit. "
  "In 1926 it became a veterans' hospital for disabled World War I soldiers, then a neurological clinic, then Robinson Memorial Hospital. It was listed on the National Register in 2004.",
  look="A Classical Revival hospital block. The Long Historical Society says it was being rehabilitated for senior housing; whether that is finished, and what survives inside, were not checked.",
  accn="Look from the public street. The Register record gives the address as 2524 West Paseo; the pin is the Register's point. Street parking.",
  links=[['R. A. Long Historical Society: Christian Church Hospital', 'https://ralonghistoricalsociety.org/christian-church-hospital'], ['Park Service record, NRIS 04001161', 'https://npgallery.nps.gov/AssetDetail/NRIS/04001161']],
  conf='mixed', brick='?'),

N('montgomery-ward-warehouse-tension-kc', 'Montgomery Ward warehouse (Tension Envelope building), 19th Street', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.08974, -94.57345, 'exact', 'view', 'drive', '', '1910–1911',
  "A nine-storey brick warehouse at 819 East 19th Street, built as Montgomery Ward's Kansas City merchandise warehouse and finished in two phases by 1911 to designs by John McKecknie, a pioneer of reinforced concrete. Kansas City Magazine says Ward's earlier Kansas City home was in the West Bottoms and its later one on St. John Avenue in the Northeast. "
  "Tension Envelope bought it, and its \"Tension Envelopes\" sign went up in 1959. It is on the National Register (2010), under three names: Montgomery Ward, Tension Envelope and Southwest Warehouse. The Register points to a period of 1908 to 1960.",
  look="A tall brick Classical Revival warehouse with the lit Tension Envelopes sign on the Crossroads skyline. Sources differ on whether the first part was built in 1908 or 1910.",
  accn="Headquarters of the Tension Corporation, a working company, so look from the street. Street parking in the Crossroads.",
  links=[['KC Yesterday: Tension Envelopes', 'https://kcyesterday.substack.com/p/tension-envelopes'], ['Kansas City Magazine: the Ward building on St. John', 'https://kansascitymag.com/kansas-city-once-home-to-largest-building-west-of-mississippi/'], ['Crossroads Arts District: Tension Corporation', 'https://kccrossroads.org/explore-the-crossroads/tension-envelope'], ['Park Service record, NRIS 10000461', 'https://npgallery.nps.gov/AssetDetail/NRIS/10000461']],
  conf='mixed', brick='yes'),

N('vanderslice-hall-marburg-kcai-kc', 'Vanderslice Hall (Marburg, the August Meyer house), Kansas City Art Institute', 'Kansas City', 'kcmo', 'inst', 'standing',
  39.04691, -94.58276, 'exact', 'view', 'drive', '', '1896',
  "A 35-room, three-storey Queen Anne mansion called Marburg, designed by Van Brunt and Howe and finished in 1896 for August Meyer, the first president of the park board, whose plans shaped the city's parks and boulevards. "
  "It stood on an eight-acre estate with a Japanese garden and koi pond. Howard Vanderslice bought it in 1927 and gave it to the Kansas City Art Institute, which uses it for offices. Clio says it is built mainly of brick and limestone, with an auditorium added in 1930, and that the entrance hall, grand staircase and first-floor fireplaces survive; the exterior stonework was cleaned by hand and the art-glass windows restored in 2016. National Register 1982.",
  look="Triple windows on the upper floors and a gabled pavilion over the stair. Inside, Clio says the entrance hall, grand staircase and fireplaces are intact.",
  accn="An administrative building of the Kansas City Art Institute campus on Warwick Boulevard; no public hours were found, so look from the campus green and the street. Street parking.",
  links=[['Clio: Vanderslice Hall', 'https://theclio.com/tour/3153/15'], W('Kansas City Art Institute'), ['Park Service record, NRIS 82003146', 'https://npgallery.nps.gov/AssetDetail/NRIS/82003146']],
  conf='mixed', brick='yes'),

N('the-walnuts-wornall-kc', 'The Walnuts (apartment buildings at 51st and Wornall)', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.03596, -94.59075, 'site', 'view', 'drive', '', '1929–1931',
  "Three Jacobean-style luxury apartment buildings, built from 1929 to 1931 on a ten-acre site at 5049 Wornall Road across from Loose Park, now condominiums. They replaced a stone country house also called the Walnuts, built about 1909 for the railway manager W. W. Sylvester and later home to the Wallace Robinson family, whose great hall had a pipe organ. "
  "The mansion was torn down in 1929. Ella Loose took a penthouse; Clio says an English garden sits above the underground parking.",
  look="Three Tudor-looking towers with a garden between them. Clio says the garden is landscaped; whether any of the old mansion's trees remain was not checked.",
  accn="Private condominiums; look from Wornall Road and the Loose Park side. Street parking, and Loose Park is across the road.",
  links=[['Clio: The Walnuts', 'https://theclio.com/entry/204812'], ['Midtown KC Post: Walnuts Apartments replaced the mansion of the same name', 'https://midtownkcpost.com/walnuts-apartments-replaced-famous-mansion-of-the-same-name/']],
  conf='mixed', brick='?'),

N('hunter-gary-house-ward-parkway-kc', 'Hunter Gary House', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.02693, -94.60586, 'site', 'view', 'drive', '', '1922',
  "Built in 1922 for Hunter L. Gary, president of the Kansas City Telephone Company, which became Southwestern Bell. The architect John Van Brunt took the English Georgian brick house from Washington's Mount Vernon and gave it a two-storey white portico on eight columns. "
  "Gary sold it in 1941 to the bank president Harry Abernathy. Clio says later owners added to it but kept the interior largely original, including walnut-panelled rooms, and that a dining room was added in 1928. National Register 2008.",
  look="A brick Georgian mansion with a tall white portico copied from Mount Vernon, raised on a terrace once used for croquet.",
  accn="Private estate off 56th Street near Ward Parkway; look from the public road. Street parking.",
  links=[CLIO, ['Clio: Hunter Gary House', 'https://theclio.com/tour/3153/29'], ['Park Service record, NRIS 08000022', 'https://npgallery.nps.gov/AssetDetail/NRIS/08000022']],
  conf='mixed', brick='yes'),

N('nicholson-house-ward-parkway-kc', 'George E. Nicholson House', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.0244, -94.60188, 'area', 'view', 'drive', '', '1917–1918',
  "A Neo-Classical Revival mansion built in 1917 and 1918 for George Nicholson, who owned cement plants, brick kilns, zinc mines and gas companies and led the group that bought the Kansas City Gas Company. Wight and Wight, who designed the Nelson-Atkins Museum and City Hall, were the architects. "
  "The deed made the three houses round the 58th Street parklet face each other, so the front door faces 58th Street although the lot fronts Ward Parkway. Clio says later owners kept the interior in near-original condition, with Italian marble floors and plasterwork. National Register 2005.",
  look="A three-storey classical house whose entrance faces 58th Street. Clio says the original library, sunroom and dining room finishes survive.",
  accn="Private; look from 58th Street and Ward Parkway. The pin marks the junction round which the house stands, not the house itself. Street parking.",
  links=[CLIO, ['Clio: George E. Nicholson House', 'https://theclio.com/tour/3153/31'], ['Park Service record, NRIS 05001325', 'https://npgallery.nps.gov/AssetDetail/NRIS/05001325']],
  conf='mixed', brick='?'),

N('katz-house-ward-parkway-kc', 'Michael H. and Rose Katz House', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.01976, -94.60271, 'site', 'view', 'drive', '', '1928–1929',
  "A French Norman-style house at 5930 Ward Parkway, built in 1928 and 1929 for Michael Katz, who ran the Katz drugstore chain with his brother Isaac, and his wife Rose. The architect was Robert Gornall, who designed the Uptown Theater. "
  "The house was used for charity events, and Clio notes the 1930s kidnapping of Michael Katz as one of the city's best-known crimes. National Register 2004.",
  look="A large Norman-style house on Ward Parkway. Exterior materials and the interior were not checked.",
  accn="Private; look from Ward Parkway. Street parking is limited.",
  links=[CLIO, ['Clio: Michael H. and Rose Katz House', 'https://theclio.com/tour/3153/32'], ['Park Service record, NRIS 04000212', 'https://npgallery.nps.gov/AssetDetail/NRIS/04000212']],
  conf='mixed', brick='some'),

N('tromanhauser-house-roanoke-kc', 'Norman Tromanhauser House', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.06197, -94.60148, 'site', 'view', 'drive', '', '1914–1915',
  "A Prairie School house at 3603 West Roanoke Drive designed by Louis Curtiss, the Kansas City architect, for the businessman Norman Tromanhauser. The Park Service record gives 1915 as its date and 1900 to 1924 as its period, and the National Register listing came in 2001. "
  "Other sources say it was built for friends of Curtiss and has later additions; the nomination itself could not be read.",
  look="A Prairie School house by Curtiss. The materials and the additions were not checked.",
  accn="Private house on Roanoke Drive; look from the street. Street parking.",
  links=[['Park Service record, NRIS 01000014', 'https://npgallery.nps.gov/AssetDetail/NRIS/01000014']],
  conf='mixed', brick='?'),

N('walt-disney-family-home-bellefontaine-kc', "Walt Disney's family home, 3028 Bellefontaine", 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.07006, -94.5474, 'exact', 'view', 'drive', '', '1905',
  "The Disney family lived here from 1914 to November 1921. Clio says it was here that Walt first took to entertaining and cartooning, and that he set up a makeshift studio in the garage with a borrowed film camera and made the first Laugh-O-gram shorts. "
  "The house and garage were listed on the National Register in 1978 (Clio says 1977). Clio calls it a plain wood cottage of 1905 and says the garage's wood walls were replaced with cinder block.",
  look="A two-storey frame house and the small garage behind it. A 2014 KCUR story found the family of its present occupant still living there and visitors stopping to photograph it from the street.",
  accn="A private home, not open to the public (Clio). Look from the sidewalk on Bellefontaine Avenue and respect the residents. Street parking.",
  links=[['Clio: Walt Disney\'s family home', 'https://theclio.com/tour/544/1'], ['KCUR: living in Walt Disney\'s childhood home', 'https://www.kcur.org/community/2014-05-09/what-its-like-to-live-in-walt-disneys-childhood-home-in-kansas-city'], ['Park Service record, NRIS 78001654', 'https://npgallery.nps.gov/AssetDetail/NRIS/78001654']],
  conf='mixed', brick='no'),
]

PIN_NOTES = {
'volker-house-roselawn-kc': 'Address lookup for 3717 Bell Street, checked on the aerial; the Register point is about 40 metres away.',
'shelley-house-hyde-park-kc': 'National Register point, checked on the aerial.',
'knight-house-hyde-park-kc': 'Address lookup for 3534 Walnut Street; the Register point is about 200 metres north, on a modern building.',
'mcintire-house-armour-blvd-kc': 'Address lookup for 710 East Armour Boulevard, checked on the aerial.',
'loose-mansion-armour-blvd-kc': 'National Register point; OpenStreetMap puts the mansion about 20 metres away.',
'christian-church-hospital-kc': 'Moved about 50 metres from the Register point onto the hospital building seen east of the road on the aerial; the Register point matched the address it gives, 2524 West Paseo.',
'montgomery-ward-warehouse-tension-kc': 'Address lookup for 819 East 19th Street, then moved about 30 metres onto the large warehouse roof seen on the aerial; the Register point is about 200 metres north, in a parking lot.',
'vanderslice-hall-marburg-kcai-kc': 'National Register point for the mansion on the Art Institute campus, checked on the aerial.',
'the-walnuts-wornall-kc': 'Address lookup for 5049 Wornall Road, checked on the aerial; the pin marks the site.',
'hunter-gary-house-ward-parkway-kc': 'National Register point, checked on the aerial; the pin marks the estate.',
'nicholson-house-ward-parkway-kc': 'National Register point, which falls at the junction of Ward Parkway and 58th Street where three houses face each other; the aerial does not show which one is the Nicholson house, so the pin marks the area.',
'katz-house-ward-parkway-kc': 'Address lookup for 5930 Ward Parkway; the Register point is about 290 metres north.',
'tromanhauser-house-roanoke-kc': 'Address lookup for 3603 West Roanoke Drive; the Register point is on the road.',
'walt-disney-family-home-bellefontaine-kc': 'Address lookup for 3028 Bellefontaine Avenue, checked on the aerial.',
}
