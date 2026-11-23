# November 23, 2026: downtown Kansas City, the West Bottoms and Elmwood Cemetery, Jackson County, Missouri.
# Part of filling in the Kansas City area on purpose for a local researcher. The Atlas had none of these buildings.
# Facts from the linked sources only: Wikipedia read as raw text (tools/wiki_raw.py), the National Register forms for the
# Moline Plow, Perfection Stove and Creamery Package buildings (read from the National Park Service's copies), and Clio pages
# for the Marty and Faultless Starch buildings. The Register forms for Marty, Faultless Starch and the downtown buildings
# could not be read. Hours of the hotels and theatre were not found on pages that would open.
from data_b import N
from data_ma import W

PLACES = [
N('folly-theater-kc', 'Folly Theater (Standard Theatre)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.10194, -94.58694, 'exact', 'open', 'drive', '', '1900',
  'The Standard Theatre opened on September 23, 1900, as a vaudeville and burlesque house with 2,400 seats. Colonel Edward Butler of St. Louis built it at a reported cost of $250,000 for his son, to a design by the Kansas City architect Louis S. Curtiss. It was renamed the Century in 1902 and Shubert\'s Missouri after the Shubert brothers bought it in 1923. '
  'It was later saved by a nonprofit that raised the money to buy it, and a seven-year restoration finished in 1981. Its original colour scheme was restored in 2005. It is on the National Register of Historic Places and was recorded by the Historic American Buildings Survey.',
  look='A narrow Neo-Palladian front of Carthage limestone and red pressed brick, with a big Palladian window over three arched entrances at street level. Inside, the auditorium now seats 1,078 (Wikipedia). The Edward Hotel that stood beside it, also by Curtiss, was demolished in 1965 and an annex was built on its site. Interior beyond the auditorium was not checked.',
  accn='A working theatre in the middle of downtown, at 300 West 12th Street (the address in the survey record). You go in for a performance or an event; the theatre\'s page lists what is on. Public street and garage parking downtown. Hours: no set visiting hours were found on the pages read.',
  links=[W('Folly Theater'), ['Folly Theater (the theatre\'s page)', 'https://www.follytheater.org/']],
  hours='?', brick='some'),

N('hotel-president-kc', 'Hotel President (President Hotel)', 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.09778, -94.58417, 'exact', 'open', 'drive', 'hotels', '1925',
  'Frank A. Dudley of Niagara Falls built the President in 1925 for the United Hotels Company, in the same downtown building boom that produced the Mainstreet Theater, the Midland Theatre and the Power and Light Building. In 1928 it was headquarters of the Republican National Convention that nominated Herbert Hoover. '
  'It closed in 1980, was restored for $45.5 million and reopened in 2005 as a Hilton hotel, with more renovations in 2017.',
  look='A tall downtown hotel at 1327 to 1335 Baltimore Avenue. What of the 1925 lobby and rooms survives was not checked; Wikipedia says its Drum Room lounge once drew Frank Sinatra and Benny Goodman, and does not say whether the room still exists.',
  accn='A working hotel (Hilton President Kansas City), so the lobby is open to guests and people visiting the restaurant or bar; ask at the desk. Parking is in downtown garages or on the street. Hours: not found on a page that would open.',
  links=[W('Hotel President')],
  hours='?', brick='?'),

N('savoy-hotel-and-grill-kc', 'Savoy Hotel and Grill (Hotel Thorne)', 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.10361, -94.58667, 'exact', 'open', 'drive', 'hotels', '1888',
  'The Arbuckle Coffee Company\'s owners built it in 1888 and it opened in 1889 as the Hotel Thorne. It became the Hotel Savoy in 1894. In 1903 a west wing was added with the Savoy Grill, and the grill room was ringed with murals of the Santa Fe Trail painted by Edward Holslag. Until it closed for renovation in 2016 it was said to be the oldest continuously operating hotel west of the Mississippi. '
  'It reopened after new owners refurbished it (Wikipedia says 2018), joined Historic Hotels of America in 2019, and is on the National Register of Historic Places (1974).',
  look='The Holslag murals now surround the bar of the restaurant, Savoy at 21c, and the hotel kept some original pieces during its 1980s renovation, including the reception desk. Wikipedia says a 2014 kitchen fire damaged the old grill. How much of the 1888 building shows on the street, and what the 2016–2018 refurbishment changed, were not checked.',
  accn='A working hotel and restaurant (the 21c Museum Hotel), so the bar and dining room are open to customers. Street and garage parking downtown. Hours: not found on a page that would open.',
  links=[W('Savoy Hotel and Grill')],
  hours='?', brick='?'),

N('boley-building-kc', 'Boley Building', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.10000, -94.58222, 'exact', 'view', 'drive', '', '1909',
  'Louis Curtiss, a Canadian-born architect working in Kansas City, designed this six-story Art Nouveau building and it was finished in 1909. It is described as one of the first buildings with a curtain wall of metal and glass, and the first to use rolled-steel columns. It is on the National Register of Historic Places (1971) and is the headquarters of the publisher Andrews McMeel Universal.',
  look='The steel frame carries a thin front of glass and metal, with cantilevered floor slabs, cast-iron detail and terra cotta ornament. Wikipedia says the interior displays comic strips the company publishes, such as Calvin and Hobbes and Doonesbury; whether visitors may go in was not found.',
  accn='An office building, so look at it from the sidewalk. Street and garage parking downtown.',
  links=[W('Boley Building')],
  hours='', brick='?'),

N('hotel-phillips-kc', 'Hotel Phillips', 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.10003, -94.58460, 'exact', 'open', 'drive', 'hotels', '1931',
  'The Phillips opened in February 1931 on 12th Street, on the site of the Glennon Hotel, where Harry S. Truman had once run a haberdashery. It cost $1.6 million, had 450 rooms and at 20 stories was then the tallest hotel in Kansas City. It is on the National Register of Historic Places (1979). '
  'It was bought in 2015, renovated and joined Hilton\'s Curio Collection; it now has 217 rooms.',
  look='Wikipedia says the lobby holds an eleven-foot sculpture of the Goddess of Dawn, made in 1931 by the Kansas City sculptor Jorgen Dreyer. Whether it survived the renovation was not checked, nor was the rest of the interior.',
  accn='A working hotel across the street from the Muehlebach Hotel. The lobby and any bar or restaurant are open to guests and customers. Street and garage parking downtown. Hours: not found on a page that would open.',
  links=[W('Hotel Phillips')],
  hours='?', brick='?'),

N('rieger-hotel-kc', 'Rieger Hotel', 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.08946, -94.58391, 'site', 'open', 'drive', 'hotels', '1915',
  'Alexander Rieger, a local entrepreneur, built the hotel in 1915 at the northwest corner of 20th and Main Streets, near Union Station, for travelling businessmen. The Rieger family sold it in 1926 and it kept the name. A local story says Al Capone stayed here; Wikipedia gives it as hearsay, not a record. The upper floors became condominiums in 2003. It is on the National Register of Historic Places (2004).',
  look='A well-known corner building in the Crossroads Art District. Wikipedia says the original lobby holds a restaurant and the basement a speakeasy-style bar; neither was checked, so confirm they are still open before going.',
  accn='Upper floors are private condominiums. The ground-floor restaurant is open to customers if it still operates. Street parking in the Crossroads. Hours: not found on a page that would open.',
  links=[W('Rieger Hotel')],
  hours='?', brick='?', conf='mixed'),

N('chambers-building-kc', 'Chambers Building (Chambers Lofts)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.09977, -94.58237, 'exact', 'view', 'drive', '', '1915–1923',
  'The architect Charles A. Smith designed this twelve-story building in the Early Commercial style. The first five stories went up in 1915 and the top seven were added in 1923. It was renovated with low-income housing tax credits, is marketed as Chambers Lofts, and was listed on the National Register of Historic Places in 2001.',
  look='A steel-frame tower clad in brick and terra cotta, with a visible break in character between the 1915 base and the 1923 addition. Interior was not checked.',
  accn='Apartment building: look from the sidewalk. Street and garage parking downtown.',
  links=[W('Chambers Building (Kansas City, Missouri)')],
  hours='', brick='some'),

N('graphic-arts-building-kc', 'Graphic Arts Building (Graphic Arts Lofts)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.10242, -94.58567, 'exact', 'view', 'drive', '', '1915',
  'Samuel B. Tarbet designed this eight-story reinforced-concrete building in 1915 as a headquarters for commercial printing and related trades. Park University later used it, and after a redevelopment approved in 2005 it became Graphic Arts Lofts, with 58 apartments. It was listed on the National Register of Historic Places in 2005. Tarbet also designed the Wheeling Corrugating building, the Goodenow Textiles building and the Athenaeum.',
  look='A concrete-frame loft building built for printers. The first floor holds the leasing office for the Old Town Lofts buildings (Wikipedia). What the outside is faced with and what survives inside were not checked.',
  accn='Apartment building: look from the sidewalk. Street and garage parking downtown.',
  links=[W('Graphic Arts Building (Kansas City, Missouri)')],
  hours='', brick='?'),

N('argyle-building-kc', 'Argyle Building', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.09983, -94.57930, 'exact', 'view', 'drive', '', '1906–1925',
  'Louis Curtiss designed the Argyle in 1906 as a four-story building in the Early Commercial style. In 1924–25 the firm of Keene and Simpson enlarged it to ten stories, and the new floors were used for medical offices. It was listed on the National Register of Historic Places in 2005.',
  look='A ten-story downtown block whose upper six floors date from the 1924–25 enlargement over Curtiss\'s original four. Present use and interior were not checked.',
  accn='Look from the sidewalk; whether the public may enter was not found. Street and garage parking downtown.',
  links=[W('Argyle Building (Kansas City, Missouri)')],
  hours='', brick='?'),

N('albert-marty-building-kc', 'Albert Marty Building', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.10089, -94.60223, 'site', 'view', 'drive', '', '1886',
  'The local developer Albert Marty built this solid-brick Romanesque Revival warehouse near the rail depot in 1886; early tenants sold farm implements. The Gustin-Bacon Manufacturing Company used it from the 1910s to 1964, and later tenants included the Columbia Burlap Bag Company, a tire company and an antique dealer. Clio says it came through the Missouri River floods of 1903 and 1908. '
  'It is one of the oldest buildings left in the West Bottoms and is on the National Register of Historic Places. Sources differ on who designed it: Clio says the architect is unknown and that Van Brunt and Howe may have, while the Register form for the building next door credits Frederick B. Hamilton.',
  look='Heavy brick walls, wide doorways and arched windows. Clio says the Columbia Burlap Bag Company name is still on the building. It is part of a row Marty developed in 1884–86 along 12th Street; the Creamery Package building is its neighbour. Interior not checked.',
  accn='Private commercial building at 1412 to 1418 West 12th Street. Look from the sidewalk. Street parking in the West Bottoms.',
  links=[['Clio: Albert Marty Building', 'https://theclio.com/entry/157952'], ['National Register form, Creamery Package building (describes the Marty row)', 'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/16000764_text']],
  hours='', brick='yes', conf='mixed'),

N('creamery-package-building-kc', 'Creamery Package Manufacturing Company Building', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.10090, -94.60180, 'site', 'view', 'drive', '', '1886',
  'A four-story Romanesque Revival brick building, ready for use in 1886 and built of heavy timber inside, in the row Albert Marty developed in the West Bottoms. The Register form credits the architect Frederick B. Hamilton (an attribution) and the contractor Willis M. Prather. It housed the Flint and Walling Manufacturing Company, the Chandler Pump Company and, from 1921 to 1964, the Creamery Package Manufacturing Company. '
  'It was listed on the National Register of Historic Places in the 2010s as part of the railroad-related industrial buildings of Kansas City.',
  look='A brick front of thick piers, recessed windows on the upper floors, a heavily corbelled cornice and, on the ground floor, wooden overhead doors, over a limestone foundation. The form was written from visits in 2016. Its use today was not checked.',
  accn='Private commercial building at 1408 to 1410 West 12th Street. Look from the sidewalk. Street parking in the West Bottoms.',
  links=[['National Register form, Creamery Package Manufacturing Company Building', 'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/16000764_text']],
  hours='', brick='yes'),

N('moline-plow-building-kc', 'Moline Plow Company Building', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.10180, -94.59980, 'site', 'view', 'drive', '', '1906',
  'The Moline Plow Company first set up in the West Bottoms around 1870 at 11th and Santa Fe. This seven-story building at 1015 Mulberry Street was designed by the Kansas City firm of Root and Siemens, built by Collins Brothers Construction in 1906, and used as a warehouse and sales office for plows, tractors and cultivators. It has also been called the Moline Building and the Morewood Building. '
  'The nomination form lists it as vacant when written, and it is on the National Register of Historic Places.',
  look='A seven-story brick and stone Commercial-style block with terra cotta trim on a stone foundation. Inside, the form says the upper floors are wide open spaces with the heavy timber columns and beams showing; the second-floor columns have Composite capitals. Its use now was not checked.',
  accn='Private building, empty when the form was written: look from the sidewalk. Street parking in the West Bottoms.',
  links=[['National Register form, Moline Plow Company Building', 'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/100004065_text']],
  hours='', brick='yes'),

N('perfection-stove-building-kc', 'Perfection Stove Company Building', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.10254, -94.59844, 'site', 'view', 'drive', '', '1919',
  'The Perfection Stove Company\'s Kansas City branch opened in 1918, and this three-story brick distribution office and warehouse at 1200 Union Avenue was built in 1919. The 2014 Register form calls it an excellent, intact example of its type in the West Bottoms and notes that the district stayed a warehouse area after the old Union Depot was torn down when Union Station opened in 1914.',
  look='A flat-roofed brick building with terra cotta and limestone trim on a concrete foundation. The form lists its use as vacant when written in January 2014. Present use was not checked.',
  accn='Private building: look from the sidewalk. Street parking in the West Bottoms.',
  links=[['National Register form, Perfection Stove Company Building', 'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/14000376_text']],
  hours='', brick='yes'),

N('faultless-starch-building-kc', 'Faultless Starch Company Building', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.10540, -94.59580, 'site', 'view', 'drive', '', '',
  'The Faultless Starch Company moved into this plant at 1025 West 8th Street after the 1903 flood ruined its earlier home. The Kansas City firm Shepard and Farrar designed it, and it was added to in the 1930s and 1950s. The company later made Bon Ami cleanser as well. It is on the National Register of Historic Places (2002). '
  'Sources disagree on whether the family company still runs the plant: Clio says it does, but a search result says the family operation in the West Bottoms was sold in 2020. Neither was confirmed.',
  look='A tall red-brick plant (photographs on Wikimedia Commons show it), with a flat roof, many large windows, several entrances and loading docks. Interior was not checked.',
  accn='Private industrial property: look from the sidewalk. Street parking in the West Bottoms.',
  links=[['Clio: Faultless Starch Company/Bon Ami Building', 'https://theclio.com/tour/2558/28'], W('Bon Ami Company')],
  hours='', brick='yes', conf='mixed'),

N('elmwood-cemetery-kc', 'Elmwood Cemetery', 'Kansas City', 'kcmo', 'burial', 'standing',
  39.09611, -94.52583, 'exact', 'public', 'drive', 'cemeteries', '1872',
  'Elmwood opened on September 8, 1872, as a rural cemetery east of the city, and covers 43 acres. A nonprofit society owns it under a charter meant to run 999 years. It holds the oldest surviving Jewish cemetery in Kansas City, from two acres sold to Temple B\'nai Jehudah early on. People buried here include Kersey Coates, the real-estate developer; Tom Bass, the African American horse trainer; and Jacob Loose, whose mausoleum is here. It is on the National Register of Historic Places.',
  look='Wikipedia lists a vault and crematorium, an entrance gate and fence, the Kirkland B. Armour Chapel (1904, 1917) and a cemetery office (1925), with Victorian monuments and mausoleums. The society invites visitors to treat it as a community park, and the paved paths are used for running. Which buildings are open was not checked.',
  accn='Owned by the Elmwood Cemetery Society, at 4900 Truman Road at Van Brunt Avenue. Parking along the cemetery roads and nearby streets was not checked. Gate hours were not found on a page that would open; assume daylight and respect any posted rules.',
  links=[W('Elmwood Cemetery (Kansas City, Missouri)')],
  hours='', brick='no'),
]

BATCH = {'key': 'kcmo_dtwb_mrqx', 'label': 'Downtown Kansas City and the West Bottoms, Missouri', 'added': '2026-11-23 17:03'}

PIN_NOTES = {
 'folly-theater-kc': 'Position from Wikipedia\'s infobox for the Folly Theater; on the aerial the pin falls on a building of that kind at the spot, though the exact one could not be told apart.',
 'hotel-president-kc': 'Position from Wikipedia\'s infobox for the Hotel President; on the aerial the pin falls on a building of that kind at the spot, though the exact one could not be told apart.',
 'savoy-hotel-and-grill-kc': 'Position from Wikipedia\'s infobox for the Savoy; on the aerial the pin falls on a building of that kind at the spot, though the exact one could not be told apart.',
 'boley-building-kc': 'Position from the National Register list on Wikipedia; on the aerial the pin falls on a building of that kind at the spot, though the exact one could not be told apart.',
 'hotel-phillips-kc': 'Position from the National Register list on Wikipedia (Wikipedia\'s article gives one a few metres off); on the aerial the pin falls on a building of that kind at the spot, though the exact one could not be told apart.',
 'rieger-hotel-kc': 'Position from the National Register list on Wikipedia, which differs by about 250 m from the article\'s infobox; the pin marks the corner of 20th and Main by the aerial.',
 'chambers-building-kc': 'Position from the National Register list on Wikipedia, since the article\'s point lies a block away; on the aerial the pin falls on a building of that kind at the spot, though the exact one could not be told apart.',
 'graphic-arts-building-kc': 'Position from the National Register list on Wikipedia, since the article\'s point lies a block away; on the aerial the pin falls on a building of that kind at the spot, though the exact one could not be told apart.',
 'argyle-building-kc': 'Position from the National Register list on Wikipedia, since the article\'s point lies a block away; on the aerial the pin falls on a building of that kind at the spot, though the exact one could not be told apart.',
 'albert-marty-building-kc': 'Position from the National Register list on Wikipedia; on the aerial the pin falls on a building of that kind at the spot, though the exact one could not be told apart.',
 'creamery-package-building-kc': 'Position from the National Register list on Wikipedia; on the aerial the pin falls on a building of that kind at the spot, though the exact one could not be told apart.',
 'moline-plow-building-kc': 'Position from the National Register list on Wikipedia; on the aerial the pin falls on a building of that kind at the spot, though the exact one could not be told apart.',
 'perfection-stove-building-kc': 'Position from the National Register list on Wikipedia; on the aerial the pin falls on a building of that kind at the spot, though the exact one could not be told apart.',
 'faultless-starch-building-kc': 'Position from the National Register list on Wikipedia; on the aerial the pin falls on a building of that kind at the spot, though the exact one could not be told apart.',
 'elmwood-cemetery-kc': 'Position from Wikipedia\'s infobox for the cemetery; on the aerial the pin falls on a building of that kind at the spot, though the exact one could not be told apart.',
}
