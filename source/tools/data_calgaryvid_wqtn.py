# November 27, 2026: downtown Calgary, Alberta, from the names in one video of old photographs of the city. The video was
# only a list of names to look up; every fact here comes from the linked sources: the Canadian Register of Historic
# Places statements (historicplaces.ca), the City of Calgary's Historic Downtown and Connaught-Beltline heritage walking
# tours, the City's historical research report on James Short Park, Wikipedia read as raw text, the Confluence's and
# Knox United Church's own pages, and a CTV News report.
from data_b import N
from data_ma import W

DT = 'Downtown Calgary; street parking and public parkades nearby. The City Hall and Centre Street CTrain stations are a short walk.'
HDT = ['City of Calgary: Historic Downtown Calgary walking tour (PDF)', 'https://www.calgary.ca/PDA/pd/Documents/Heritage-planning/heritage-walking-tours/heritage-historic-dwtn-calgary-brochure.pdf']
def R(n, t): return ['Canadian Register of Historic Places: ' + t, 'https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=' + n]

BATCH = {'key': 'calgaryvid_wqtn', 'label': 'Calgary: the sandstone city, its churches, bank, courthouse and bridge', 'added': '2026-11-27 00:32'}

PLACES = [
N('confluence-fort-calgary', 'The Confluence (Fort Calgary site)', 'Calgary', 'ab', 'fort', 'traces',
  51.04528, -114.04556, 'site', 'open', 'walk', 'forts', '1875–1914',
  'The North-West Mounted Police built a post here, where the Elbow River meets the Bow, in 1875; first called Fort Brisebois, it was renamed Fort Calgary in 1876. The palisade came down in 1882 and the police used the enlarged barracks until 1914, when the ground was sold to the Grand Trunk Pacific Railway and the police buildings were demolished for a rail terminal. '
  'It was named a National Historic Site in 1925, bought by the city in 1975 and opened as Fort Calgary Historic Park in 1978; it took its present name, The Confluence Historic Site and Parkland, in 2024.',
  look='None of the original fort stands. On the site are reconstructions of the stables and wagon shed (1990s) and a replica of the 1888 two-storey barracks (2000), an interpretive centre, and open parkland on the two rivers. The Deane House (1906), built for the post\'s superintendent and later moved, and Hunt House are on the grounds too.',
  accn='Run by The Confluence Historic Site & Parkland at 750 9 Avenue SE. Admission charged for the cultural centre; the parkland and a free audio tour are open to walk. Its own pay parking lot is on 9 Avenue SE (Calgary Parking zone 8345); the visit page, read November 2026, warned of road work in front and of a closure of the cultural centre for exhibit work, so check before going. Hours from theconfluence.ca/visit.',
  links=[W('The Confluence Historic Site & Parkland'), ['The Confluence: plan your visit', 'https://www.theconfluence.ca/visit']],
  brick='?', hours='Summer (from May 16) Tuesday to Sunday 10 a.m. to 5 p.m.; winter (from October 13) Thursday to Sunday 11 a.m. to 4 p.m.'),

N('imperial-bank-of-canada-calgary', 'Imperial Bank of Canada building', 'Calgary', 'ab', 'civic', 'standing',
  51.04573, -114.06282, 'exact', 'view', 'walk', '', '1886–1887, 1909–1911',
  'The I. G. Baker Company and the businessmen John Lineham and Matthew Dunn put up two matching sandstone buildings here in 1886 and 1887, just after the fire of 1886, when the town ruled that public buildings be of fire-proof brick or sandstone. The Imperial Bank of Canada, the first chartered bank to open in Calgary, bought one of them in 1892. '
  'Between 1909 and 1911 the architects Darling and Pearson of Toronto, with Hodgson, Bates and Beatty, remade it as a Neoclassical bank. It has been a Provincial Historic Resource since 1977.',
  look='A two-storey building of rough-faced sandstone on the Stephen Avenue pedestrian mall: a cornice on block modillions, a balustered parapet, carved shields, and the words IMPERIAL BANK OF CANADA. The Register notes that the columned entrance and pediment have since been altered or removed. Interior not checked.',
  accn='Private building at 102 8 Avenue SE (the walking tour gives 100), on Stephen Avenue, a pedestrian street. Seen from the street. ' + DT,
  links=[R('8081', 'Imperial Bank of Canada'), HDT],
  brick='no', hours=''),

N('hudsons-bay-store-calgary', "Hudson's Bay Company store (The Bay), Stephen Avenue", 'Calgary', 'ab', 'civic', 'standing',
  51.04575, -114.06609, 'site', 'view', 'walk', '', '1911–1913, 1929, 1957',
  "The Hudson's Bay Company's fourth store in Calgary. The first part, along 1 Street SW and 7 Avenue, opened in 1913, one of the largest city stores of its day to sell by departments; the 8 Avenue front with its colonnade was added in 1929 and a west wing in 1957. "
  'The store has closed. CTV News reported in April 2026 that the building is to be turned into condominiums.',
  look='A Chicago Commercial block with Edwardian Classical touches, of steel, concrete and brick faced entirely in cream glazed terra cotta, with a colonnade along Stephen Avenue (8 Avenue SW). Interior not checked.',
  accn='Private building at 200 8 Avenue SW, filling the block between 1 and 2 Street SW. Seen from the street; works may be under way. ' + DT,
  links=[HDT, ['CTV News (April 2026): building to become condos', 'https://www.ctvnews.ca/calgary/article/historic-hudsons-bay-building-being-converted-into-condos/']],
  brick='no', hours=''),

N('central-united-church-calgary', 'Central United Church (Central Methodist Church)', 'Calgary', 'ab', 'worship', 'standing',
  51.04628, -114.06504, 'exact', 'view', 'walk', '', '1905',
  'Built for the Central Methodist congregation, successor to the Methodist church Reverend John McDougall began in Calgary in 1875. Fund-raising for it began in 1898 and the design came from Badgley and Nicklas of Cleveland, Ohio; it was dedicated in February 1905. It became Central United Church in 1925. '
  'The chimes in its tower were given in 1927 by R. B. Bennett, later Prime Minister, in memory of his mother.',
  look='A stone church with a square corner tower, as a recent photograph shows. Interior not checked.',
  accn='Active church at 131 7 Avenue SW. Service times were not found on a page of the congregation\'s own; seen from the street. ' + DT,
  links=[HDT],
  brick='no', hours='?'),

N('knox-united-church-calgary', 'Knox United Church', 'Calgary', 'ab', 'worship', 'standing',
  51.04807, -114.07111, 'exact', 'open', 'walk', '', '1912–1913',
  "Home of Calgary's oldest Protestant congregation, founded as Knox Presbyterian in 1883. Its first wooden church was followed in 1886 by the first large stone building in the town, enlarged in 1905, and then by this church, built in 1912 and 1913 to a design by the Calgary architects Lawson and Fordyce with Allen and Collens of Boston. "
  'The congregation joined the United Church of Canada in 1925. The church, called "the cathedral of the west", was long the tallest building in Calgary and is a Provincial Historic Resource.',
  look='A large Gothic Revival church of local Paskapoo sandstone in the English Perpendicular manner: a square bell tower with a crenellated parapet, big traceried windows and a corner courtyard among the towers. Inside, by the Register: extensive stained glass including 37 memorial windows and a First World War window, a Casavant organ of 4,355 pipes, the baptismal font and an oak communion table.',
  accn='Active church at 506 4 Street SW. Sunday worship is open to all. The church\'s page names the Barclay Centre Parkade at 615 3 Street SW (cheap on Sundays) and free street parking on Sundays. Hours from kxcalgary.com.',
  links=[W('Knox United Church (Calgary)'), R('5183', 'Knox United Church'), ['Knox United Church', 'https://kxcalgary.com/']],
  brick='no', hours='Sunday worship 10:30 a.m.'),

N('first-baptist-church-calgary', 'First Baptist Church', 'Calgary', 'ab', 'worship', 'standing',
  51.04042, -114.07195, 'exact', 'view', 'walk', '', '1912',
  'The First Baptist congregation began with seven members in 1888 and met in rented rooms until its first church, on 6 Avenue and 2 Street SW, was built in 1890. A second followed in 1900 on 7 Avenue and 1 Street SW, across from the Central Methodist church; this, its third, was finished in 1912 to a design by D. S. McIlroy. '
  'Thomas Underwood, a church member and one of the busiest builders of the boom years, built all three.',
  look='A red brick church with a tall spire, seen across Central Memorial Park, as a photograph shows. Interior not checked.',
  accn='Active church at 1301 4 Street SW (the City tour gives 1311). Service times were not found on a page of the congregation\'s own; seen from the street. Street parking in the Beltline.',
  links=[['City of Calgary: Connaught-Beltline heritage walking tour (PDF)', 'https://www.calgary.ca/PDA/pd/Documents/Heritage-planning/heritage-walking-tours/heritage-connaught-beltline-heritage-walk-tour.pdf']],
  brick='yes', bcol='red', hours='?'),

N('calgary-courthouse-no-2', 'Calgary Courthouse No. 2', 'Calgary', 'ab', 'civic', 'standing',
  51.0472, -114.07322, 'exact', 'view', 'walk', '', '1912–1914',
  'The Supreme Court of Alberta sat on this block from the late 1880s. This larger courthouse was designed by the provincial architect Allan M. Jeffers; his successor Richard P. Blakey reworked the plans, and it cost so much that the province stopped building new public buildings for a time. '
  'The court moved in in 1914 and stayed until 1962. The Glenbow museum used it from 1964 to 1975, and it was an appeal court again from 1986 to 2001. It is a Provincial Historic Resource.',
  look='A two-storey Neoclassical block of smooth sandstone on a base of rough granite, with plain wings either side of an ornamented entrance and the provincial crest carved over the door. The Register says it was the last major building in Calgary to use local sandstone, and that the foyer, marble staircase and parts of the terrazzo floor survive inside. Present use and whether the public may go in were not checked.',
  accn='Building at 530 7 Avenue SW, at 5 Street SW. Seen from the street. ' + DT,
  links=[R('9082', 'Calgary Courthouse No. 2'), HDT],
  brick='no', hours=''),

N('centre-street-bridge-calgary', 'Centre Street Bridge', 'Calgary', 'ab', 'landmark', 'standing',
  51.05299, -114.06255, 'exact', 'public', 'walk', '', '1915–1916',
  'The city built this bridge over the Bow River in 1915 and 1916 for $375,000, to replace a steel truss bridge of 1907 put up by a land company and wrecked by the flood of 1915. It was designed by the Minnesota bridge engineer John F. Greene and for much of its early life carried two streetcar lines as well as cars and people. '
  'It was protected as a Municipal Historic Resource in 1992.',
  look='A reinforced concrete bridge of four arched spans about 396 m long, with an upper deck on arches and a lower deck below. Each end has a pair of kiosks topped by big concrete lions modelled on those in Trafalgar Square, with buffalo heads, a maple leaf, rose, shamrock and thistle; the sculptures were first carved by the Calgary artist James L. Thomson. Classical balustrades and balconies line the sidewalks.',
  accn='A City of Calgary street bridge (built by the city, by Wikipedia and the Register) between Chinatown (Riverfront Avenue) and Crescent Heights, with sidewalks on the upper deck. The Bow River Pathway passes under it. Street parking in Chinatown.',
  links=[W('Centre Street Bridge (Calgary)'), R('9275', 'Centre Street Bridge')],
  brick='no', hours=''),

N('calgary-fire-hall-no-1', 'Calgary Fire Hall No. 1', 'Calgary', 'ab', 'civic', 'standing',
  51.04762, -114.06077, 'exact', 'view', 'walk', '', '1911',
  'Built in 1911 to replace the city\'s first fire headquarters of 1887, to a design by Lang and Major, with the fire chief James "Cappy" Smart taking part in the planning. Smart led the brigade from here until he retired in 1933, and it stayed a fire hall until 1973. '
  'It is a Provincial Historic Resource.',
  look='A two-storey red brick fire hall with sandstone trim, set at an angle to the street corner: five wide truck doors, FIRE HEADQUARTERS lettered in the pediment, and a square hose tower with a copper-covered cupola (a reconstruction of the original). Present use not checked.',
  accn='Private building at 140 6 Avenue SE, at 1 Street SE. Seen from the street. ' + DT,
  links=[R('11820', 'Calgary Fire Hall No. 1'), HDT],
  brick='yes', bcol='red', hours=''),

N('calgary-public-building', 'Calgary Public Building', 'Calgary', 'ab', 'civic', 'standing',
  51.04518, -114.06008, 'exact', 'view', 'walk', '', '1930–1931',
  'The federal government\'s main office building in Calgary until 1979, and the city\'s main post office from 1931 to 1961. It stands where the first federal building and post office stood from 1894 until it was pulled down in 1913. Planned in 1919 but built only in 1930 and 1931, it is an eight-storey office block in a classical dress. '
  'It became part of the city\'s performing arts centre in 1985 and has been a Municipal Historic Resource since 1996.',
  look='Eight storeys of Tyndall limestone with giant Ionic columns on the north and west fronts at the east end of Stephen Avenue. The Register describes a two-storey lobby of Quebec marble and polished brass, and attendant-run passenger elevators that it called the last known in Alberta in 2007. Interior not checked.',
  accn='Building at 205 8 Avenue SE (the Register gives 201); in 2008 the Register said it held City of Calgary offices and a performing arts centre. Seen from the street; whether the lobby is open to walk into was not checked. ' + DT,
  links=[R('9286', 'Calgary Public Building'), HDT],
  brick='no', hours=''),

N('central-school-cupola-calgary', 'Central School cupola, James Short Park', 'Calgary', 'ab', 'curio', 'standing',
  51.0492, -114.06353, 'site', 'public', 'walk', '', '1904–1905',
  'Central School, a sandstone public school built in 1904 and 1905 and opened on May 24, 1905, stood on this block. It was renamed James Short School in 1938, after a former principal, closed in 1967 and was demolished in 1969, and a bus depot took its place. '
  'Its cupola was kept and set up in James Short Park, dedicated in 1991 over a new parkade; the clockwork from the tower of the Burns Block, pulled down in 1965, was put in it.',
  look='The school\'s cupola, set on a base in a small downtown park, with a clock in it; OpenStreetMap and a photograph on Wikimedia Commons give the park the name Harmony Park. Nothing else of the school is left.',
  accn='City of Calgary park (the City\'s own parks report covers it) on top of the James Short Parkade at 115 4 Avenue SW, between Centre Street and 1 Street SW. Open ground; parking in the parkade below.',
  links=[['City of Calgary: James Short Park historical research (PDF)', 'https://www.calgary.ca/content/dam/www/csps/parks/documents/locations/james-short/james-short-historical-research.pdf']],
  brick='?', hours=''),
]

PIN_NOTES = {
 'confluence-fort-calgary': 'Wikipedia\'s coordinate for the historic site; on the aerial it falls on open grass inside a ring of paths, with the buildings to the east. The address 750 9 Avenue SE geocodes about 120 m to the southeast.',
 'imperial-bank-of-canada-calgary': 'OpenStreetMap\'s outline of the Imperial Bank of Canada building on 8 Avenue SE.',
 'hudsons-bay-store-calgary': 'The address 200 8 Avenue SW, geocoded as a point address; the store fills the block.',
 'central-united-church-calgary': 'OpenStreetMap\'s point for Central United Church, 131 7 Avenue SW.',
 'knox-united-church-calgary': 'OpenStreetMap\'s point for Knox United Church, 506 4 Street SW.',
 'first-baptist-church-calgary': 'OpenStreetMap\'s point for First Baptist Church, 1301 4 Street SW.',
 'calgary-courthouse-no-2': 'OpenStreetMap\'s outline of Courthouse No. 2, 530 7 Avenue SW.',
 'centre-street-bridge-calgary': 'OpenStreetMap\'s bridge feature over the Bow River.',
 'calgary-fire-hall-no-1': 'OpenStreetMap\'s outline of Fire Hall No. 1, 140 6 Avenue SE. On the aerial the ring is on the low building at the corner beside the curved glass tower, and a street photograph on Wikimedia Commons taken 3 m from the pin shows the fire hall there beside that tower.',
 'calgary-public-building': 'OpenStreetMap\'s outline of the Calgary Public Building, 205 8 Avenue SE.',
 'central-school-cupola-calgary': 'The park\'s address, 115 4 Avenue SW, geocoded; it falls in the small park, but which object on the aerial is the cupola could not be told.',
}
