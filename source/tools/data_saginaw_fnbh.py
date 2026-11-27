# November 27, 2026: Saginaw, Michigan. A "videos" session (PROMPTS.md job 9): the names came from one video's tour of
# old Saginaw buildings (the record is source/videos/20250314_zoxXyf3DM4o.md); the video is a tip and nothing here rests
# on it. Sources read: Wikipedia (each article named in the links), SAH Archipedia (Buildings of Michigan, 2012), the
# Castle Museum of Saginaw County History's own articles, the Michigan Stained Glass Census, and the Public Libraries of
# Saginaw's branch page for the library's hours. Pins are OpenStreetMap features or address points, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'saginaw_fnbh','label':'Michigan: old Saginaw','added':'2026-11-27 03:42'}

DT=' Downtown parking is in city lots, ramps and on the street; their hours and fees were not checked.'
SAH='https://sah-archipedia.org/buildings/MI-01-'

PLACES=[

N('bearinger-building-saginaw','Bearinger Building','Saginaw','mi','civic','standing',43.43395,-83.93717,'exact','view','walk','','1893',
  'A six-storey store and office block built in 1893 by Isaac Bearinger, an Ontario-born lumberman who rose from cook\'s helper to timber baron. Saginaw architects W. T. Cooper and Frederick Beckbissinger designed it, and it was billed as the first fireproof building on Saginaw\'s east side. The Bearinger family kept it until 1972; it was emptied in 2008, foreclosed on in 2013, bought by the Saginaw Economic Development Corporation in 2015 and by the City of Saginaw in 2022. On the National Register since 1982.',
  'A Chicago-style block of brick and steel faced with red brick, with ribbon windows on the sixth floor; the decorative cornice that once crowned it is gone, and limestone now covers the ground floor. Empty when the latest source read was written; inside not checked.',
  '',
  'Owned by the City of Saginaw (2022, Wikipedia); 124 North Franklin Street downtown, seen from the street. Not open to visitors.'+DT,
  [W('Bearinger Building')],
  brick='yes',bcol='red'),

N('saginaw-armory','Saginaw Armory','Saginaw','mi','civic','standing',43.43139,-83.94061,'exact','view','walk','','1909–1910',
  'A National Guard armory built in 1909 and 1910 with state money from Michigan\'s new armory fund and city money on top, to the design of William T. Cooper; the earth dug for it was dumped by the river to make a park and parade ground. Company B of the Michigan National Guard stayed until 1983. The building was then sold several times and taken over by businesses, and renovated in 2009. On the National Register since 2002.',
  'A three-storey castle-like brick armory on a high basement, with five-sided towers at the corners, a round-arched entrance bay with a small corbelled turret, and a row of round attic windows. The parapet was battlemented until, it is thought, the 1950s, when the battlements were taken off. Inside not checked.',
  '',
  'Privately owned and used by businesses (Wikipedia); 234 South Water Street, seen from the street.'+DT,
  [W('Saginaw Armory')],
  brick='?'),

N('potter-street-station-saginaw','Potter Street Station (Flint and Pere Marquette depot)','Saginaw','mi','rail','standing',43.44068,-83.93265,'site','view','walk','stations','1881',
  'The Flint and Pere Marquette Railroad\'s East Saginaw depot, built in 1881 to the design of the New York architect Bradford Lee Gilbert and used for passengers until 1950. The Chesapeake and Ohio, which had taken over the line, planned to pull it down in 1955, and in the late 1980s city officials ordered the railroad of the day to demolish it; it survived both, was damaged by arson in April 1991, and given a new roof with a state grant in 1993. On the National Register since 1996; Wikipedia says it stands empty and is owned by the Saginaw Depot Preservation Corporation.',
  'A long two-storey depot of red brick trimmed with stone, 285 feet by 40, with hip roofs, broad round-arched dormers, darker brick bands, terra-cotta panels and an iron-bracketed canopy all round; a two-storey boiler house stands beside it. The Register description gives a pyramid-roofed central tower; whether the tower still stands was not checked. Not open inside.',
  '',
  'Owned by a preservation group (Wikipedia, date not given); 501 Potter Street, seen from the street. Parking was not checked: the lots nearby belong to businesses.',
  [W('Saginaw Potter Street station')],
  brick='yes',bcol='red'),

N('hoyt-library-saginaw','Hoyt Public Library','Saginaw','mi','civic','standing',43.43045,-83.93568,'exact','open','walk','','1887–1890',
  'Built in 1887 to 1890 with a bequest from Jesse Hoyt, a New York investor in Saginaw timberland, who left East Saginaw a site and $100,000 for a library and books. H. H. Richardson, McKim, Mead and White and Van Brunt and Howe all sent plans; the trustees chose Van Brunt and Howe\'s, laid out on the advice of the Chicago librarian Frederick Poole, and Richardson\'s rejected design went to New Orleans instead. A porch and reference room came in 1920 and 1921, a beige brick addition in 1959 to 1960, and a renovation in 1994.',
  'A round corner tower, arches and gables in rough grey-white Bay Port limestone trimmed with red Lake Superior sandstone. Inside the old building is finished in oak, staircase included. The beige brick wing of 1959 to 1960 is in a plainer style. Still the main library, open to anyone in its hours.',
  '',
  'The main library of the Public Libraries of Saginaw, 505 Janes Avenue; the hours are from the library\'s own branch page.'+DT,
  [W('Hoyt Library'),['SAH Archipedia: Hoyt Public Library',SAH+'SA5'],['Public Libraries of Saginaw: Hoyt Main','https://www.saginawlibrary.org/branch/hoyt-main']],
  brick='no',bcol='buff',hours='Monday to Thursday 9 a.m. to 8 p.m.; Friday and Saturday 9 a.m. to 5 p.m.; closed Sunday'),

N('temple-theatre-saginaw','Temple Theatre','Saginaw','mi','civic','standing',43.43473,-83.93911,'exact','open','walk','','1927',
  'A 1927 theatre and three-storey clubhouse built for the Elf Khurafeh Shriners, meant to follow the Academy of Music, which burned in 1917. Osgood and Osgood of Grand Rapids designed it; W. S. Butterfield ran it as a film and stage house for fifty years until it closed in 1977. Samuel and Peter Shaheen restored it from 2002, gave it to the city in 2010 with an endowment, and it is now run by TempleArts and is home to the Saginaw Bay Symphony Orchestra.',
  'A working 1,750-seat theatre whose interior decoration, by Tuttle and Clark of Detroit, was repaired and repainted in the restoration, with some original painting uncovered from under later paint; the organ was restored in 2011 and a new vertical marquee, modelled on the first, went up in 2016. Seen inside by buying a ticket to a show.',
  '',
  'A performing arts centre at 201 North Washington Avenue; the theatre\'s own pages could not be opened when this was written, so box office hours were not checked. A mapped lot is on Johnson Street, about 70 m north.'+DT,
  [W('Temple Theatre (Saginaw, Michigan)'),['SAH Archipedia: Temple Theatre',SAH+'SA19']],
  th=[43.43537,-83.93902],thn='Lot on Johnson Street',
  brick='?',hours='?'),

N('forest-lawn-chapel-saginaw','Forest Lawn Cemetery Chapel and Receiving Vault','Saginaw','mi','worship','standing',43.39681,-83.95577,'area','public','walk','cemeteries','1899–1900',
  'A chapel and winter receiving vault built in 1899 and 1900 for Saginaw\'s Forest Lawn Cemetery to plans by Haug and Scheurmann, with Anson Hobson as builder. Its domed shape was inspired by Byzantine churches, the Hagia Sophia above all. The cemetery\'s grounds were laid out by Joseph Earnshaw of Cincinnati and reworked in 1909 by O. C. Simonds, who moved the South Washington Avenue entrance drive; Frantz and Spence repaired and refitted the chapel in 1947.',
  'A domed building of Bay Port limestone, 48 by 41 feet and 56 feet high, topped by a cupola, with four minaret-like pinnacles on the corner buttresses and a gabled portico facing the entrance; a Bay Port stone retaining wall of 1947 stands in front. Inside, marble, pressed brick, red sandstone and stained glass, and two rows of crypts in the vault. Whether the chapel is still used, and whether it can be seen inside, was not checked.',
  '',
  'Forest Lawn Cemetery, 3210 South Washington Avenue, run by the City of Saginaw; the chapel faces the cemetery entrance. The cemetery\'s gate hours were not found on any page of the city\'s.',
  [['SAH Archipedia: Forest Lawn Cemetery Chapel and Receiving Vault',SAH+'SA15']],
  conf='mixed',brick='no'),

N('saginaw-water-works','Saginaw Water Works','Saginaw','mi','water','standing',43.41221,-83.95488,'exact','view','walk','','1926–1929',
  'Saginaw\'s water treatment plant, built in 1926 to 1929 to the design of Victor Andre Matteson, a Chicago architect known for water plants, with Hoad, Decker, Shoecraft and Drury as engineers; a wing was added in the late 1960s. It drew from the Saginaw River until 1949 and since then from an intake at Whitestone Point on Lake Huron. Matteson built copies of it at Cedar Rapids, Iowa and Fort Wayne, Indiana.',
  'Three joined buildings in Collegiate Gothic dress, more like a college than a waterworks, in the middle of Ezra Rust Park near a small lake. A buttressed central tower hides a 125,000-gallon steel tank; behind its vaulted lobby, the filter gallery has operating tables of green serpentine and black Belgian marble. A working plant: seen from the park, inside not open as far as any source read says.',
  '',
  'A working city water plant at 522 Ezra Rust Drive, seen from Ezra Rust Park. A mapped lot is on South Washington Avenue in Hoyt Park, about 240 m east.',
  [['SAH Archipedia: Saginaw Water Works',SAH+'SA14']],
  th=[43.4126,-83.95196],thn='Lot on South Washington Avenue (Hoyt Park)',
  brick='?'),

N('first-congregational-church-saginaw','First Congregational Church','Saginaw','mi','worship','standing',43.42887,-83.93728,'exact','view','walk','','1867–1868',
  'The congregation gathered in 1857; the church was begun in 1867 and dedicated on June 14, 1868, to plans by the Detroit architect Gordon W. Lloyd, and altered in 1926 and 1927 by Frantz and Spence of Saginaw. Fire gutted the main part on June 3, 1973, and it stood roofless through a winter; at first it was called past saving, but the congregation rebuilt it and returned to the restored sanctuary in October 1974. The Castle Museum calls its style Italian villa; other accounts call it Romanesque Revival.',
  'A church that looks hardly changed since 1868, though it was added to many times and rebuilt inside after 1973. The Michigan Stained Glass Census records Tiffany Studios windows (The River Jordan, the Crucifixion, The Church in the World) and windows by Alfred Timler; the sanctuary ceiling was painted by the Saginaw artist Russell Thayer after the fire. Interior otherwise not checked.',
  '',
  'A working church of the United Church of Christ at 403 South Jefferson Avenue; its own page could not be opened when this was written, so service times were not checked.'+DT,
  [['Castle Museum: A Restored Church and New Ceiling','https://www.castlemuseum.org/post/a-restored-church-and-new-ceiling-first-congregational-church'],['Michigan Stained Glass Census: First Congregational Church','https://michiganstainedglass.org/collections/building.php/id=208-792-1211/']],
  conf='mixed',brick='?',hours='?'),

N('schuch-hotel-saginaw','Schuch Hotel','Saginaw','mi','hotel','standing',43.41833,-83.96175,'exact','view','walk','','1868',
  'A three-storey brick Italianate hotel of 1868 in old Saginaw City, now the west side, near where Fort Saginaw stood. It opened as the Brockway House and was renamed the Benson House and then the Crowley House before taking the Schuch name. It stands in the Saginaw City Historic Business District, on the National Register since 1982.',
  'A three-storey Italianate brick front at 301 North Hamilton Street. A restaurant and bar used the building in recent years; whether it is open now, and the inside, were not checked.',
  '',
  'Private, at 301 North Hamilton Street in Old Town Saginaw on the west side; seen from the street. Street parking.',
  [W('Saginaw City Historic Business District')],
  brick='?'),

N('jeffers-fountain-saginaw','Jeffers Memorial Fountain','Saginaw','mi','curio','standing',43.43139,-83.93456,'site','public','walk','','1906',
  'A memorial drinking fountain in Jeffers Park, a small triangle of downtown that the heirs of Michael Jeffers, an Irish-born early settler and one of East Saginaw\'s biggest landlords, gave to the city after his death; it had been covered with commercial buildings. Roy Merriam of Saginaw designed the fountain, Anson Hobson made it, and the Henry-Bonnard Bronze Company of New York cast the bust of Jeffers and the lion masks. It was dedicated at the end of the Memorial Day parade on May 30, 1906; park and fountain were restored by a committee formed in 2003 and rededicated in June 2013.',
  'The fountain with a bronze bust of Michael Jeffers on top and bronze lion masks, in the middle of the little park between East Genesee, Federal and Warren, beside the Castle Museum. Water once came from a deep well and was cooled by pipes run through ice in a vault beneath.',
  '',
  'A city park downtown, beside the Castle Museum; open ground.'+DT,
  [['Castle Museum: A Small Park with a Story, Jeffers Park','https://www.castlemuseum.org/post/a-small-park-with-a-story-jeffers-park']],
  brick='?'),

]

PIN_NOTES={
 'bearinger-building-saginaw':'OpenStreetMap\'s outline of the Bearinger Fireproof Building, checked on the aerial.',
 'saginaw-armory':'Address point for 234 South Water Street, checked on the aerial.',
 'potter-street-station-saginaw':'Address point for 501 Potter Street, beside the tracks north of Potter Street. The summer aerial did not show the depot\'s hip roofs clearly, so the pin marks the site and not the building.',
 'hoyt-library-saginaw':'OpenStreetMap\'s Hoyt Public Library, checked on the aerial.',
 'temple-theatre-saginaw':'OpenStreetMap\'s Temple Theatre, checked on the aerial.',
 'forest-lawn-chapel-saginaw':'Address point for the cemetery, 3210 South Washington Avenue, at the edge of the cemetery on South Washington Avenue. The chapel could not be picked out under the trees on the summer aerial, so the pin marks the cemetery entrance area; the chapel faces that entrance.',
 'saginaw-water-works':'OpenStreetMap\'s Saginaw Water Works and Treatment Facility, checked on the aerial.',
 'first-congregational-church-saginaw':'OpenStreetMap\'s First Congregational Church, checked on the aerial.',
 'schuch-hotel-saginaw':'Address point for 301 North Hamilton Street, checked on the aerial.',
 'jeffers-fountain-saginaw':'OpenStreetMap\'s Jeffers Park; the fountain is in its middle.',
}
