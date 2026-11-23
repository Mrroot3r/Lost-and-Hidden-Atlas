# November 23, 2026: downtown Kansas City, Missouri, from the names in one walking-and-postcard video about the city's
# old buildings. The video was only a list of names to look up; every fact here comes from the linked sources: Wikipedia
# read as raw text, Clio entries, the Kansas City Public Library's and the National WWI Museum's own pages, Flatland KC and
# KCTV news pages. National Register forms for the Scarritt, Old New England and Grand Avenue Temple buildings could not
# be opened.
from data_b import N
from data_ma import W

DTKC = 'Downtown Kansas City; street parking and public garages.'

BATCH = {'key': 'kcvid_yufk', 'label': 'Kansas City, Missouri: downtown towers and halls', 'added': '2026-11-23 20:42'}

PLACES = [
N('new-york-life-building-kc', 'New York Life Building (20 West Ninth)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.10371, -94.58407, 'exact', 'view', 'drive', '', '1887–1889',
  'New York Life Insurance Company bought the corner of Ninth Street and Baltimore Avenue in 1886 and finished this office block in August 1889, to a design by Frederick Elmer Hill of McKim, Mead & White. It was Kansas City\'s tallest building and the first in the city with elevators. '
  'It changed hands several times, stood empty for much of the 1990s after a failed apartment scheme, and was renovated in 1996 as the headquarters of the utility UtiliCorp (later Aquila). It is on the National Register of Historic Places.',
  look='An H-shaped block: two pairs of 10-storey wings joined by a 12-storey centre, the Ninth Street and Baltimore Avenue fronts in brick and brownstone with tiers of arched windows. Wikipedia describes a marble lobby with a barrel-vaulted ceiling, wood decoration and mosaic-tiled corridors inside; whether the public may go in was not checked.',
  accn='Private office building at 20 West Ninth Street, on the northeast corner of Ninth and Baltimore. Seen from the street. ' + DTKC,
  links=[W('New York Life Building (Kansas City, Missouri)')],
  hours='', brick='?'),

N('scarritt-building-kc', 'Scarritt Building and Arcade', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.1036, -94.5811, 'exact', 'view', 'drive', '', '1906–1907',
  'The Scarritt Estate Company built this 11-storey office tower and the four-storey arcade beside it in 1906 and 1907 for about $750,000, to a design by Root & Siemens. Clio and the Kansas City Public Library call it the finest Chicago School skyscraper in the city. It has been on the National Register since 1971. '
  'In 2022 Flatland KC reported it mostly empty and bought by a developer who planned a 193-room hotel; whether that has been done was not checked.',
  look='A grey terra cotta base of two storeys, an H-shaped shaft in light brick, and terra cotta ornament round the second-floor windows and in the cornice. The arcade, entered from 819 Walnut Street, has an ornate terra cotta ground floor and a skylight. Interior not checked.',
  accn='Private building at 818 Grand Boulevard with the arcade at 819 Walnut Street, Ninth Street corner. Seen from the street. ' + DTKC,
  links=[W('Scarritt Building and Arcade'), ['Clio: Scarritt Building and Arcade', 'https://theclio.com/entry/157238'],
         ['Flatland KC (2022): hotel plan', 'https://flatlandkc.org/news-issues/historic-scarritt-building-and-arcade-slated-to-become-50m-luxury-hotel/']],
  conf='mixed', hours='', brick='no'),

N('kcpl-building-kc', 'Kansas City Power and Light Building', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.09755, -94.58472, 'exact', 'view', 'drive', '', '1931',
  'Joseph F. Porter, president of Kansas City Power and Light, built this Art Deco tower in 1931, partly to make work downtown. Hoit, Price and Barnes designed it. At 34 storeys it was the tallest habitable building in Missouri for decades from 1931, and Wikipedia says the tallest west of the Mississippi until 1962. '
  'Its conversion to apartments began in 2014, and the lobby became an event space.',
  look='The crown is an Art Deco lantern of prismatic glass panels hiding red-orange lights that glow from sunset; the setbacks were once lit with coloured floodlights to look like flames, and LED floodlights now change colour. Interior not checked.',
  accn='Private apartment building at 1330 Baltimore Avenue, facing the Power & Light District. Seen from the street; the lantern shows best after dark. ' + DTKC,
  links=[W('Kansas City Power and Light Building')],
  hours='', brick='?'),

N('muehlebach-hotel-kc', 'Hotel Muehlebach', 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.09941, -94.58488, 'exact', 'open', 'drive', 'hotels', '1915',
  'George E. Muehlebach, of the brewing family, bought the site of the First Baptist Church in 1914, took the church down and built a 12-storey, 144-foot brown brick hotel to a design by Holabird & Roche, opened in May 1915 at a cost of $2 million. Presidents stayed here, Harry S. Truman among them. A 17-storey annex was added in 1952. '
  'The lower floors are now a wing of the Kansas City Marriott Downtown; the upper guest floors were gutted and stood empty for years, and in 2025 a developer announced plans for 152 apartments in them.',
  look='The restored 1915 lobby and ballrooms are used by the Marriott for banquets and meetings, and a plaque in the lobby marks the 1938 meeting that began the Barbershop Harmony Society. A lounge opened on the ground floor in 2023. Upper floors empty.',
  accn='Part of a working hotel at Twelfth Street and Baltimore Avenue (Kansas City Marriott Downtown), so the lobby is open to guests and people visiting the bar; ask at the desk. ' + DTKC + ' Hours: the hotel\'s own page would not open.',
  links=[W('Muehlebach Hotel')],
  hours='?', brick='?'),

N('midland-theatre-kc', 'Midland Theatre (Loew\'s Midland)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.09883, -94.58348, 'exact', 'open', 'drive', '', '1927',
  'Marcus Loew built this 3,000-seat movie palace for $4 million, finished in 1927 to a design by Thomas W. Lamb of New York with the Boller Brothers of Kansas City. It was called Loew\'s Midland until 1961 and has had many names since; the NCAA had its offices in the building from the 1950s to 1971. '
  'It was listed on the National Register in 1977, renovated after 2007, and is a concert and stage hall today.',
  look='A Renaissance Revival front in cream glazed terra cotta with pilasters, winged figures, swags and urns, and a four-storey arched window above a marquee restored to its 1927 look. Wikipedia describes the inside as French and Italian Baroque; seen only by going to a show.',
  accn='Working theatre at 1228 Main Street, run as a concert hall; you go in with a ticket for a show. ' + DTKC + ' Hours: the theatre\'s page would not open.',
  links=[W('Midland Theatre')],
  hours='?', brick='no'),

N('fidelity-bank-909-walnut-kc', 'Fidelity National Bank and Trust Building (909 Walnut)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.1031, -94.5816, 'exact', 'view', 'drive', '', '1931',
  'Fidelity National Bank and Trust bought this site, then a two-storey post office and federal building, in 1904, razed it in 1930 and in 1931 put up a 35-storey, 471-foot tower for about $2.85 million. Its twin spires copy those of the old federal building it replaced. It later held federal offices. '
  'It stood empty until 2000 and was then turned into apartments and offices. It was listed on the National Register in 1997.',
  look='An Art Deco and Gothic Revival tower with twin spires. Interior not checked.',
  accn='Private apartment building at 909 Walnut Street. Seen from the street. ' + DTKC,
  links=[W('909 Walnut')],
  hours='', brick='?'),

N('old-new-england-building-kc', 'Old New England Building', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.1038, -94.5852, 'exact', 'view', 'drive', '', '1886–1887',
  'Built for the Kansas City office of a Boston insurance company, the New England Safe Deposit and Trust Company, at the northeast corner of Ninth and Wyandotte. Sources give 1886 (Wikipedia) or 1886 to 1887 (KC Yesterday). It is a Renaissance Revival office building and was listed on the National Register in 1973.',
  look='A Renaissance Revival office front at 112 West Ninth Street, across from the New York Life Building. What is left inside was not checked.',
  accn='Private building at 112 West Ninth Street. Seen from the street. ' + DTKC,
  links=[W('Old New England Building'), ['KC Yesterday: the Old New England Building', 'https://kcyesterday.substack.com/p/the-old-new-england-building']],
  conf='mixed', hours='', brick='?'),

N('grand-avenue-temple-kc', 'Grand Avenue Temple and Grand Avenue Temple Building', 'Kansas City', 'kcmo', 'worship', 'standing',
  39.10328, -94.58028, 'exact', 'view', 'drive', '', '1911',
  'A Methodist congregation founded on this corner in 1866 built a Greek Revival church and, beside it, a 12-storey office building in 1911, to designs by the Kansas City architect John McKecknie (Clio spells him McKenzie). The rents were to pay the church\'s debts and missions, so it could stay downtown when others moved south. '
  'It held its last service in June 2021. Both buildings have been on the National Register together since 1985.',
  look='The temple front has fluted Ionic columns, two pilasters and arched stained glass windows. The office building has rusticated granite at the bottom, lion-head cartouches on the 11th floor, terra cotta panels on the 12th and an ornate cornice. Interior not checked.',
  accn='At 205 East Ninth Street and 903 Grand Boulevard. The congregation closed in 2021 and no source read says who uses the church now, so it is seen from the street. ' + DTKC,
  links=[['Clio: Grand Avenue Temple and Office Building', 'https://theclio.com/entry/157103'],
         ['Flatland KC: last service', 'https://flatlandkc.org/news-issues/grand-avenue-temple-closes-downtown-sanctuary-since-1912/']],
  hours='', brick='?'),

N('liberty-memorial-kc', 'Liberty Memorial (National WWI Museum and Memorial)', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.08028, -94.58611, 'exact', 'open', 'drive', '', '1926',
  'Kansas City people raised the money for this memorial to the First World War soon after it ended; it was dedicated on November 11, 1926, by President Coolidge. Decay made it an embarrassment by the 1990s, and city voters passed a sales tax in 1998 to restore it. Congress named the museum beneath it the country\'s official World War I museum in 2004.',
  look='An Egyptian Revival limestone tower, 217 feet, crowned by four Guardian Spirits, with a flame effect of lit steam at night. Two winged sphinxes, Memory and Future, sit between the tower and Exhibition and Memory halls. An elevator and 45 steps reach an open-air deck on top. The museum is below.',
  accn='Run by a nonprofit with the Kansas City parks board, at 2 Memorial Drive, across from Union Station. The grounds are open; the museum and tower charge admission, and the last elevator up the tower is at 4:15 p.m. (the museum\'s visit page). The tower may shut in bad weather.',
  links=[W('National World War I Museum and Memorial'), ['National WWI Museum: visit', 'https://www.theworldwar.org/visit']],
  hours='Labor Day to Memorial Day Wed to Mon 10 a.m. to 5 p.m., closed Tue; summer daily 10 a.m. to 5 p.m.', brick='no'),

N('central-library-first-national-bank-kc', 'Central Library (First National Bank Building)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.10258, -94.58388, 'exact', 'open', 'drive', '', '1906',
  'Wilder & Wight designed this building for the First National Bank in 1906. The Kansas City Public Library remodelled it and moved its Central Library here in 2004.',
  look='The restored 1906 banking hall is the first room you see inside. One of the bank vaults is now a 28-seat film room with free films. The Missouri Valley Room holds the library\'s local history collection.',
  accn='Public library at 14 West Tenth Street, at Baltimore Avenue. Free parking in the library\'s garage (the library\'s page). Hours from the library\'s page; closed on some holidays.',
  links=[W('Central Library (Kansas City, Missouri)'), ['Kansas City Public Library: Central', 'https://kclibrary.org/locations/central']],
  hours='Sun 1 to 5 p.m.; Mon to Wed 9 a.m. to 7 p.m.; Thu to Sat 9 a.m. to 5 p.m.', brick='?'),

N('mark-twain-tower-kc', 'Kansas City Athletic Club building (Mark Twain Tower, Continental Hotel)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.1010, -94.5844, 'site', 'view', 'drive', '', '1923',
  'In 1923 the Kansas City Athletic Club took over an unfinished 22-storey building at Eleventh Street and Baltimore Avenue and had Hoit, Price & Barnes complete it as its clubhouse. In the Depression, in 1932, the Continental Hotel Company took over all but the top six floors. '
  'It was remodelled as an office building named Mark Twain Tower in 1982 and bought by a historic-property developer in 2016. It is on the National Register as the Continental Hotel.',
  look='A 22-storey tower at Eleventh and Baltimore. What is left of the club and hotel inside was not checked.',
  accn='Private building at Eleventh Street and Baltimore Avenue. Seen from the street. ' + DTKC,
  links=[W('Kansas City Athletic Club')],
  hours='', brick='?'),

N('aladdin-hotel-kc', 'Aladdin Hotel', 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.09948, -94.58526, 'exact', 'view', 'drive', 'hotels', '1925',
  'The Armour Building Company built this 16-storey hotel in 1925, the tallest building in Kansas City when it opened, according to Clio. Clio names the architect both as Phillip T. Drotts and as Weaver. '
  'The hotel later closed; Clio gives both 2020 and 2022. The new owners turned it into 122 apartments, and people began moving in in September 2026 (KCTV).',
  look='Italian Romanesque: white limestone on the first three floors with arches and terra cotta, ten-storey brick pilasters topped by life-size terra cotta female figures, five arched windows on the 16th floor and a pyramid roof. KCTV says original details were kept inside.',
  accn='Private apartment building at 1215 Wyandotte Street. Seen from the street. ' + DTKC,
  links=[['Clio: Aladdin Hotel', 'https://theclio.com/entry/156615'],
         ['KCTV (2026): move-ins begin', 'https://kctv5.com/2026/10/14/move-ins-begin-historic-aladdin-hotel-downtown-kansas-city'],
         W('District I (Hotels in Downtown Kansas City TR)')],
  conf='mixed', hours='', brick='?'),

N('oak-tower-bell-telephone-kc', 'Oak Tower (Bell Telephone Building)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.1012, -94.5789, 'exact', 'view', 'drive', '', '1919–1929',
  'Built for the Bell telephone company as a 14-storey, 185-foot tower, finished in 1919 or 1920 (sources differ). In 1929 it was raised to 28 storeys, the first big job built with a new lightweight concrete made in Kansas City, which allowed more floors on the old frame. '
  'On January 11, 1964, a small plane flew into its 28th floor in a snowstorm and four people died. It was sold in 2021 and holds a data centre.',
  look='The original terra cotta front was covered in white stucco in 1974, so what shows today is the 1970s skin. Interior not checked.',
  accn='Private building at 324 East Eleventh Street, Oak Street corner. Seen from the street. ' + DTKC,
  links=[W('Oak Tower')],
  conf='mixed', hours='', brick='no'),
]

PIN_NOTES = {
 'new-york-life-building-kc': 'Position from the National Register list for Downtown Kansas City; on the aerial it falls on a downtown building of that size, though the exact one could not be told from above.',
 'scarritt-building-kc': 'Position from the National Register list for Downtown Kansas City; on the aerial it falls on a downtown building of that size, though the exact one could not be told from above.',
 'kcpl-building-kc': 'Position from the National Register list for Downtown Kansas City; on the aerial it falls on a downtown building of that size, though the exact one could not be told from above.',
 'muehlebach-hotel-kc': 'Position from Wikipedia\'s article on the hotel; on the aerial it falls on a downtown building of that size, though the exact one could not be told from above.',
 'midland-theatre-kc': 'Position from the National Register list for Downtown Kansas City; on the aerial it falls on a downtown building of that size, though the exact one could not be told from above.',
 'fidelity-bank-909-walnut-kc': 'Position from the National Register list for Downtown Kansas City; on the aerial it falls on a downtown building of that size, though the exact one could not be told from above.',
 'old-new-england-building-kc': 'Position from the National Register list for Downtown Kansas City; on the aerial it falls on a downtown building of that size, though the exact one could not be told from above.',
 'grand-avenue-temple-kc': 'Position of the church as mapped in OpenStreetMap at 205 East Ninth Street; on the aerial it falls on a downtown building of that size, though the exact one could not be told from above.',
 'liberty-memorial-kc': 'Position from Wikipedia\'s article on the museum and memorial; on the aerial it falls on the memorial deck south of the museum lawn.',
 'central-library-first-national-bank-kc': 'Position of the library as mapped in OpenStreetMap at 14 West Tenth Street; on the aerial it falls on a downtown building of that size, though the exact one could not be told from above.',
 'mark-twain-tower-kc': 'Position from the National Register list for Downtown Kansas City (Continental Hotel). On the aerial it falls on a tall building on Eleventh Street, but a photograph placed at that spot on Wikimedia Commons shows the Fairfax Building across the street, so the pin marks the corner and not a building.',
 'aladdin-hotel-kc': 'Position of the building as mapped in OpenStreetMap at 1215 Wyandotte Street; on the aerial it falls on a downtown building of that size, though the exact one could not be told from above.',
 'oak-tower-bell-telephone-kc': 'Position from Wikipedia\'s article on Oak Tower; on the aerial it falls on a downtown building of that size, though the exact one could not be told from above.',
}
