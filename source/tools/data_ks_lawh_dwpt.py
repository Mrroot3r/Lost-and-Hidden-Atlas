# November 24, 2026: more of Lawrence and Douglas County, Kansas (houses, a Carnegie library, a mansion, a farmstead).
# Part of filling in the Kansas City area on purpose for a local researcher.
# Facts from the National Register nominations that have a text layer on the National Park Service's NPGallery (read whole)
# and the Kansas Historical Society's register listings for Douglas County (read as pages, summaries only for the newer
# listings whose nominations could not be read). Nothing was checked on the ground.
from data_b import N

KS_LIST = ['Kansas Historical Society: National and State Registers, Douglas County', 'https://www.kansashistory.gov/natreg/natreg_listings/search/county:DG/records:all']
NPG = 'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/'

BATCH = {'key': 'ks_lawh_dwpt', 'label': 'Lawrence and Douglas County, Kansas (second pass)', 'added': '2026-11-24 23:54'}

PLACES = [
N('old-lawrence-library-ks', 'Old Lawrence City Library (1904 Carnegie library)', 'Lawrence', 'ks', 'civic', 'standing',
  38.96778, -95.2375, 'exact', 'view', 'walk', '', '1903–1904',
  'Lawrence\'s public library from its opening on December 26, 1904 until a new library opened in 1972. Congressman J. D. Bowersock obtained $25,000 of Carnegie money for it, and the building and its fittings cost $27,412. '
  'The 1975 nomination says contemporary newspapers reported it as the first building in Kansas faced with grey terra cotta, made by the Northwestern Terra Cotta Company of Chicago. A buff-brick addition was built in 1937.',
  look='A one-storey Neo-Classical building of pressed buff brick on a Warrensburg stone foundation, set back from the corner of Ninth and Vermont. A portico with two Corinthian columns on each side shelters a round-arched entrance, and a terra-cotta pediment above it carries the date 1904 and the words "Lawrence City Library". '
  'The 1975 nomination says the front is nearly unaltered except for the replaced doors. Interior not checked, and what the building is used for now was not found.',
  accn='Present owner and use not checked: the 1975 nomination says the city was then planning to use it for the arts. Look from the sidewalk at the corner of Ninth and Vermont; there is parking on the downtown streets and in the lots nearby (West 9th Street lot, about 60 m).',
  links=[['National Register nomination (1975), read in full', NPG + '75000709_text'], KS_LIST],
  conf='mixed', brick='no', hours=''),

N('castle-tea-room-roberts-house-lawrence-ks', 'The Castle (John N. Roberts House, Castle Tea Room), 1307 Massachusetts Street', 'Lawrence', 'ks', 'landmark', 'standing',
  38.95967, -95.23633, 'exact', 'view', 'walk', '', '1893–1894',
  'A fifteen-room Romanesque mansion of ashlar limestone with a three-storey corner tower, built for Lawrence manufacturer John N. Roberts during the financial panic of 1893 to 1894 and finished in the autumn of 1894. Roberts made much of his money from patents on wooden butter and lard containers and served as Kansas adjutant general in 1889. '
  'The nomination says the seventeen-year-old English visitor Sidney Endacott carved the mantels, newel posts and other interior woodwork over three months. The Roberts family left in 1919; from 1947 the house was the home of Libuse Kriz, who ran a restaurant in it, the Castle Tea Room. '
  'The Lawrence Journal-World reported in 2019 that the nonprofit that owns it would lease it out, and in 2020 that an agency would put its offices in part of it; who owns it and what it is used for now were not checked.',
  look='A towering stone house with carved porches and entries, a slate-and-lead hipped roof and several tall stone chimneys; the 1974 nomination says the outside looked unchanged from an 1898 photograph. '
  'Inside it describes five first-floor fireplaces, a third-floor ballroom with stained glass and a hidden staircase, and each room finished in a different wood. Interior not checked now. The neighbouring house at 1313 Massachusetts, also listed (Roberts-Luther-Mitchell House), was Roberts\'s as well.',
  accn='Owned by a nonprofit foundation per 2019 and 2020 press reports; present use and any opening hours not checked. Look from the sidewalk on Massachusetts Street at 13th; park on the street. Do not assume the interior is open.',
  links=[['National Register nomination (1974), read in full', NPG + '74000831_text'], ['Lawrence Journal-World, local history: the Castle Tea Room (2020)', 'https://www2.ljworld.com/living/2020/aug/12/local-history-a-few-stories-of-the-castle-tea-room-and-its-number-loving-parrot'], KS_LIST],
  conf='mixed', brick='no', hours=''),

N('morse-house-lawrence-ks', 'Dr. Frederic D. Morse House, 1041 Tennessee Street', 'Lawrence', 'ks', 'landmark', 'standing',
  38.96444, -95.23889, 'exact', 'view', 'walk', '', '1888–1889',
  'A two-storey Queen Anne house built about 1888 to 1889 for Dr. Frederic D. Morse (1838 to 1931), who came to Lawrence in 1868, practised medicine here for decades and lectured on the history of medicine at the University of Kansas. He saw patients at home from 1915. '
  'He and his wife lived in it until their deaths, and the house changed hands nine times between 1932 and 1988. The Kansas Historical Society lists it as Second Empire in style, where the 1991 nomination calls it Queen Anne.',
  look='A frame house on a rusticated limestone foundation with a cross-gabled hipped roof, fish-scale shingles and half-timbered gable ends, spindlework on the entry porch, and art-glass windows. The nomination notes the original limestone steps and paving to the curb, two limestone hitching posts and, along this block, patches of original brick sidewalk. '
  'It says the inside keeps its original plan, with oak woodwork, an Eastlake-style staircase, pocket doors and Minton-tiled fireplace hearths. This is the 1991 description; interior not checked since.',
  accn='A private house in the Oread neighbourhood; look from Tennessee Street. Street parking only, and not described as open to visitors. Owner not checked.',
  links=[['National Register nomination (1991), read in full', NPG + '91000469_text'], KS_LIST],
  conf='mixed', brick='some', hours=''),

N('benedict-house-lawrence-ks', 'Benedict House, 923 Tennessee Street', 'Lawrence', 'ks', 'landmark', 'standing',
  38.9664, -95.2397, 'exact', 'view', 'walk', '', 'about 1869–1890',
  'A small frame cottage built about 1869 as a four-room house, enlarged in seven stages up to 1927, and given its Stick-style look by the addition of 1882 and the foyer of 1890. The 1991 nomination was written to certify a rehabilitation that took off the later rear additions, '
  'put a metal-clad addition behind the old house and built two cottages on the lot to the south; the work was finished in August 1990. The Kansas Historical Society lists the builder as James Bell.',
  look='A cross-gabled, shingled and weatherboarded cottage with decorated gable trusses, overhanging eaves, varied wood siding and a one-storey porch. The metal-clad addition of 1989 to 1990 behind it echoes the old form but is plainly modern. Interior not checked.',
  accn='Private; the 1991 nomination lists it as a multiple dwelling. Look from Tennessee Street; street parking only. Present owner not checked.',
  links=[['National Register nomination (1991), read in full', NPG + '91001978_text'], KS_LIST],
  conf='mixed', brick='no', hours=''),

N('griffin-house-645-connecticut-lawrence-ks', 'A. J. and Mary Carrol Griffin House, 645 Connecticut Street', 'Lawrence', 'ks', 'landmark', 'standing',
  38.97151, -95.23272, 'exact', 'view', 'walk', '', '',
  'A Queen Anne house in East Lawrence listed on the National Register in March 2022, designed according to the Kansas Historical Society by the mail-order architect George F. Barber. The listing calls it a Queen Anne house of superb quality that keeps its distinctive features, '
  'and takes 1901 to 1916, the years the Griffins owned it, as its period. Only the Society\'s short summary was read: the nomination itself was not available, so the building date and what changed are not confirmed.',
  look='A Queen Anne house of the kind the Society calls superb quality, with its original features kept. A Wikimedia Commons photographer\'s caption says all the masonry walls are twice-pressed brick. Only the Society\'s summary was read, so what else changed is not confirmed. Interior not checked.',
  accn='A private house; look from Connecticut Street. Street parking only. Owner and use not checked.',
  links=[KS_LIST], conf='mixed', brick='yes', hours=''),

N('john-kelly-stone-building-lawrence-ks', 'John Kelly Stone Building and farmstead, 777 N 1750 Road', 'Lawrence', 'ks', 'landmark', 'standing',
  38.99152, -95.35816, 'area', 'view', 'drive', '', '',
  'A single-storey limestone building on a historic farmstead west of Lawrence that also has Oregon-California Trail ruts, listed on the Kansas State Register in November 2021. According to the Kansas Historical Society it was in severe disrepair in 2013 and was taken down and rebuilt stone by stone, '
  'with matching mortar, with the help of stone masons and architecture students. The date it was first built, and the story of John Kelly, were not found in what was read.',
  look='A side-gabled limestone building with a wooden addition and an open-timber roof, now in good condition per the Society. The pin is the mapped address; the farmstead\'s other buildings and the trail ruts were not located. Interior not checked.',
  accn='Private farmstead on a county road west of Lawrence; look only from the road, and nothing read says the public may enter. Owner not checked.',
  links=[KS_LIST], conf='mixed', brick='no', hours=''),

N('barnes-hoskinson-farmstead-vinland-ks', 'Barnes-Hoskinson Farmstead (William Barnes farm), Vinland', 'Vinland', 'ks', 'landmark', 'standing',
  38.84031, -95.18214, 'site', 'view', 'drive', '', '1885–1891',
  'A farm that William Elliot Barnes bought in 1856 and lived on until 1920. A businessman and horticulturalist, he began what is believed to be the first vineyard in Kansas. He had the Queen Anne farmhouse built in 1885 and a vernacular bank barn in 1891. '
  'The farm was listed on the National Register in 2023 as the Barnes-Hoskinson Farmstead. Only the Kansas Historical Society\'s summary was read, so what else stands on it is not confirmed. The nearby Barnes Apple Barn is a separate listing.',
  look='A Queen Anne farmhouse and a bank barn on a rural road near Vinland. Which other farm buildings survive was not read. Interior not checked.',
  accn='Private farm on East 1728 Road; look from the road. Nothing read says the public may go in. Owner not checked.',
  links=[KS_LIST], conf='mixed', brick='?', hours=''),

N('chi-omega-house-ku-lawrence-ks', 'Chi Omega Sorority House, 1345 West Campus Road', 'Lawrence', 'ks', 'landmark', 'standing',
  38.9592, -95.25144, 'exact', 'view', 'walk', '', '',
  'A Tudor Revival sorority house on the University of Kansas campus, listed on the Kansas State Register in January 1983 and designed, according to the Kansas Historical Society, by Walter Glover. '
  'OpenStreetMap maps a Chi Omega house at this address. Only the Society\'s entry was read; its date, history and what survives inside were not found.',
  look='A Tudor Revival house on the campus edge. Interior not checked.',
  accn='A working private chapter house; look from West Campus Road. Campus parking rules apply and nothing says visitors may go in.',
  links=[KS_LIST], conf='mixed', brick='?', hours=''),

N('breezedale-historic-district-lawrence-ks', 'Breezedale Historic District (2301–2401 Massachusetts Street)', 'Lawrence', 'ks', 'town', 'standing',
  38.9417, -95.2358, 'site', 'public', 'walk', '', '1909–1910',
  'Charles E. Sutton developed the Breezedale Addition and the streetcar line to the south end of Massachusetts Street, and built five similar houses there in 1909 and 1910. According to the Kansas Historical Society it was the first attempt in Lawrence to create an identifiable suburb. '
  'The district was listed in 2008 with fourteen contributing and five non-contributing buildings, and is Bungalow and Craftsman in style.',
  look='A short run of early twentieth-century bungalows and Craftsman houses along both sides of Massachusetts Street. The Society\'s summary was the only source read, so which houses are the five Sutton built is not stated here. Look from the public sidewalk; the houses are private.',
  accn='Massachusetts Street is a public city street of Lawrence (the federal public-land map does not show city streets); the houses are private homes, so view them from the sidewalk and stay off the lawns. Street parking.',
  links=[KS_LIST], conf='mixed', brick='?', hours=''),
]

PIN_NOTES = {
  'old-lawrence-library-ks': 'Register list coordinate for the old library at Ninth and Vermont.',
  'castle-tea-room-roberts-house-lawrence-ks': 'OpenStreetMap building named for General John Roberts Castle at 1307 Massachusetts.',
  'morse-house-lawrence-ks': 'Register list coordinate for 1041 Tennessee Street.',
  'benedict-house-lawrence-ks': 'Register list coordinate for 923 Tennessee Street.',
  'griffin-house-645-connecticut-lawrence-ks': 'Address lookup in OpenStreetMap for 645 Connecticut Street.',
  'john-kelly-stone-building-lawrence-ks': 'Address lookup in OpenStreetMap for 777 North 1750 Road; the pin marks the farm address, not the stone building itself.',
  'barnes-hoskinson-farmstead-vinland-ks': 'Address lookup in OpenStreetMap for 715 East 1728 Road fell in a field north of the road; the pin was moved about 70 m to the farmhouse seen on the 2024 aerial just south of it. Which building is which was not confirmed.',
  'chi-omega-house-ku-lawrence-ks': 'OpenStreetMap map point for the Chi Omega house at 1345 West Campus Road.',
  'breezedale-historic-district-lawrence-ks': 'Register list coordinate for the middle of the district.',
}
