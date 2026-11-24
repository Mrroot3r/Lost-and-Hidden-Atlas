# November 24, 2026: Kalamazoo, Michigan. A "videos" session (PROMPTS.md job 9): the names came from one video's tour of
# old Kalamazoo buildings (the record is source/videos/20240830_CSmQNVkUKRA.md); the video is a tip and nothing here
# rests on it. Sources read: Wikipedia (each article named in the links), SAH Archipedia (Buildings of Michigan, 2012),
# Second Wave Media (First Baptist Church, 2021), news results on the Hilton Garden Inn in the Masonic Temple, Amtrak's
# station page, and for hours the pages of the City of Kalamazoo, First Baptist and First Presbyterian.
# Pins are address points from the ArcGIS geocoder or Register points, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'kalamazoo_bnds','label':'Michigan: old Kalamazoo','added':'2026-11-24 21:33'}

DT=' Downtown parking is in city ramps, lots and street meters; their hours and fees were not checked.'
SAH='https://sah-archipedia.org/buildings/MI-01-'

PLACES=[

N('ladies-library-association-kalamazoo','Ladies Library Association Building','Kalamazoo','mi','civic','standing',42.28905,-85.58690,'exact','view','walk','','1878–1879',
  'Said to be the first building in the United States put up as a women\'s club, and the first owned by a women\'s organisation. The Ladies\' Library Association, begun in 1852 from a reading circle, raised the money and built it in 1878 and 1879 to the design of the Chicago architect Henry Lord Gay; a kitchen wing followed in 1913. The association still owns and uses it, and finished a restoration in 2013. On the National Register since 1970 and a Michigan State Historic Site.',
  'A small High Victorian Gothic building of orange-red brick with limestone trim, decorative tiles, a steep slate roof and an odd shed-dormered tower over the entrance porch, with a gargoyle spout. Inside are a library and meeting room below and a lecture hall with a stage above, with stained-glass windows of scenes from Milton, Shakespeare, Burns, Cooper, Longfellow and Hawthorne; it opens to the public only at events, and no regular hours were found.',
  '',
  'Owned and used by the Ladies\' Library Association, at 333 South Park Street on the south side of Bronson Park; seen from the street.'+DT,
  [W('Ladies Library Association Building'),['SAH Archipedia: Ladies Library Association Building',SAH+'KZ4']],
  brick='yes'),

N('lawrence-chapin-building-kalamazoo','Lawrence and Chapin Building (Vermeulen Furniture Building)','Kalamazoo','mi','industry','standing',42.29284,-85.58489,'exact','view','walk','','1870–1872',
  'A rare survivor of Kalamazoo\'s years as an iron-making town: the iron works of William S. Lawrence and Dr. L. C. Chapin, built from 1870 to 1872 on the site of an earlier iron-implement factory, to the design of Lemuel Dwight Grosvenor. After Chapin died and Lawrence lost his fortune it was sold about 1900 and held, in turn, a mission, a skating rink and an interurban railway station before the Vermeulen Furniture Company used it for over 50 years. Restored in the 1990s as part of the Arcadia Creek project; on the National Register since 1983.',
  'A big brick Second Empire block with a slate mansard roof, dormers and a central tower-pavilion, its upper windows hooded and grouped in threes between tall pilasters with paired brackets. The two lower floors were altered in the 1960s. Offices; the inside was not checked.',
  '',
  'A private building at 201 North Rose Street, on the corner of Water Street downtown; seen from the street.'+DT,
  [W('Lawrence and Chapin Building'),['SAH Archipedia: Vermeulen Furniture Company Building',SAH+'KZ5']],
  brick='?'),

N('masonic-temple-kalamazoo','Masonic Temple Building (Hilton Garden Inn)','Kalamazoo','mi','civic','standing',42.29396,-85.58493,'exact','open','walk','','1913–1915',
  'Built from 1913 to 1915 by eleven local Masonic bodies to replace their 1868 hall, to the design of Spier and Rohns of Detroit, with three auditoriums stacked inside for lodge ceremonies and public events. The Masons sold it in 1963; the county bought it in 1975, and it later became the Rose Street Market, offices and shops. After a developer bought it in 2015 it was turned into a hotel, the Hilton Garden Inn Kalamazoo Downtown, which opened in late 2020. On the National Register since 1980.',
  'A six-storey cube with brown brick on the two street fronts and yellow brick on the other two, white terra-cotta trim, a metal cornice and tall round-arched window groups; the hotel\'s best rooms look out through the old round windows over Rose Street. How much of the old interior survives was not checked.',
  '',
  'A working hotel at 309 North Rose Street (the hotel gives 303); anyone may walk into the lobby, and no opening hours apply.'+DT,
  [W('Masonic Temple Building (Kalamazoo, Michigan)'),['SAH Archipedia: Rose Street Market (Kalamazoo Masonic Temple)',SAH+'KZ6'],['PlazaCorp: Downtown Kalamazoo Hilton Garden Inn','https://www.plazacorp.net/project/hilton-garden-inn']],
  brick='no',hours='?'),

N('michigan-central-depot-kalamazoo','Michigan Central Depot (Kalamazoo Transportation Center)','Kalamazoo','mi','rail','standing',42.29542,-85.58410,'exact','open','walk','stations','1887',
  'The Michigan Central Railroad\'s station, built in 1887 to the design of the New York architect Cyrus L. W. Eidlitz in place of an earlier one; passenger trains had run between Kalamazoo and Detroit since 1846. Renovated in 2005 and 2006, when a bus station was added beside it, it is now the Kalamazoo Transportation Center, the city\'s bus hub and one of Michigan\'s busiest Amtrak stations. On the National Register since 1975.',
  'Richardsonian Romanesque: massive round arches of rock-faced red Lake Superior sandstone, a conical turret and a heavy red tile roof with deep eaves, with red brick. Still a working station; the waiting room is inside.',
  '',
  'A working Amtrak and bus station at 459 North Burdick Street, run with the city; Amtrak\'s station page gave no hours, so the hours are not checked. Parking was not checked.',
  [W('Kalamazoo Transportation Center'),['SAH Archipedia: Kalamazoo Transportation Center',SAH+'KZ7'],['Amtrak: Kalamazoo station','https://www.amtrak.com/stations/kal']],
  brick='some',hours='?'),

N('old-central-high-school-kalamazoo','Old Central High School','Kalamazoo','mi','civic','standing',42.28466,-85.59008,'exact','view','walk','','1912–1923',
  'Kalamazoo\'s high school site since its first Union School went up here in 1857 and 1858; later schools on the spot were razed or burned. What stands is a block-long building of two parts: a 1912 gymnasium and manual-training wing and the main front section with its auditorium of 1923, by the local architect Rockwell A. LeRoy. The high school left for a new building in 1972; the old one now holds adult education, a math and science magnet school and the Chenery Auditorium. On the National Register since 1983.',
  'A four-storey Tudor Revival school of red brick with limestone trim and an E-shaped front on South Westnedge Avenue. The Chenery Auditorium inside is used for concerts; the rest is a working school.',
  '',
  'A Kalamazoo Public Schools building at 714 South Westnedge Avenue; seen from the street, and the auditorium is entered for concerts and events.',
  [W('Old Central High School (Kalamazoo, Michigan)')],
  brick='yes'),

N('state-theatre-kalamazoo','State Theatre','Kalamazoo','mi','civic','standing',42.28850,-85.58333,'exact','open','walk','','1927',
  'A Spanish-styled atmospheric movie palace designed by John Eberson and built in 1927 for W. S. Butterfield Theatres, when it seated 1,300 under a ceiling meant to look like a night sky over a Spanish courtyard. It still runs, now with live shows. On the National Register since 2021.',
  'Buff tapestry brick and ornate terra cotta outside; inside, the auditorium, lobby and mezzanine are dressed as a Mediterranean courtyard with pottery, wrought iron, statues and paintings. Its original Barton theatre organ is still played for special events. Go in for a show.',
  '',
  'A working theatre at 404 South Burdick Street; the theatre\'s own site could not be opened, so show times and box-office hours were not checked.'+DT,
  [W('State Theatre (Kalamazoo, Michigan)')],
  brick='no',hours='?'),

N('state-hospital-water-tower-kalamazoo','Kalamazoo State Hospital Water Tower','Kalamazoo','mi','water','standing',42.27917,-85.60444,'area','view','walk','','1895',
  'A 175-foot water tower built in 1895 for the Michigan Asylum for the Insane, designed by William B. Stratton of Detroit to look like the keep of a medieval castle and match the asylum\'s buildings. The asylum opened in 1859; its early buildings are gone. The state meant to pull the tower down in 1974, but a local committee raised the money to save it, and it was restored in 1975 and 1976. On the National Register since 1972.',
  'A tall red brick cylinder on a base of big stone blocks, with a crenellated yellow brick parapet jutting out on brackets at the top, where the water tanks are, and a copper roof.',
  '',
  'On the grounds of the Kalamazoo Psychiatric Hospital, a working state hospital on Oakland Drive between Wheaton Avenue and Howard Street; look from the public streets.',
  [W('Kalamazoo State Hospital Water Tower'),['SAH Archipedia: Water Tower, Kalamazoo Psychiatric Hospital',SAH+'KZ21'],W('Kalamazoo Regional Psychiatric Hospital')],
  brick='yes'),

N('state-hospital-gatehouse-kalamazoo','State Hospital Gatehouse','Kalamazoo','mi','inst','standing',42.28139,-85.60000,'area','view','walk','','c. 1879',
  'A small carpenter Gothic cottage built about 1879 as a lodge at the entrance to the Michigan Asylum for the Insane, its details taken from a pattern book of 1873; a matching entrance gate is gone. It is unclear that a gatekeeper ever lived there: by 1885 it housed some women patients, and later staff families. It was restored in the early 1960s as a museum. On the National Register since 1983.',
  'A two-storey cottage with board-and-batten siding, a steep gabled roof and Swiss and Eastlake trim on the gables, porch and bay window. Whether the museum inside still opens was not found.',
  '',
  'At 1006 Oakland Drive, at the entrance to the Kalamazoo Psychiatric Hospital, a working state hospital; look from Oakland Drive. No opening hours were found.',
  [W('State Hospital Gatehouse'),W('Kalamazoo Regional Psychiatric Hospital')],
  brick='no'),

N('kalamazoo-city-hall','Kalamazoo City Hall','Kalamazoo','mi','civic','standing',42.28955,-85.58582,'exact','open','walk','','1931',
  'Kalamazoo\'s finest Art Deco building, dedicated in September 1931 in place of the older Corporation Hall, to the design of Weary and Alford of Chicago. Its plan is classical, its ornament of its own time. It stands on Bronson Park in the Bronson Park Historic District.',
  'Granite and Indiana limestone walls with fluted pilasters and relief panels of floral and geometric designs and local history scenes; dark cast-aluminium window frames. Inside is a three-storey skylit atrium finished in black and gold marble and travertine, with aluminium fountains, stair rails, grilles, lanterns and a letter box cast with carp, birds and pond lilies; the commission chambers were painted in peach, aqua and gold by the Kalamazoo artist Otto Stauffenberg.',
  '',
  'The working city hall at 241 West South Street, facing Bronson Park; the public hours are from the City of Kalamazoo\'s page.'+DT,
  [['SAH Archipedia: Kalamazoo City Hall',SAH+'KZ2'],['City of Kalamazoo: City Hall','https://kalamazoocity.org/Government/Locations-Hours/City-Hall'],W('Bronson Park Historic District')],
  brick='no',hours='Monday to Friday 8 a.m. to 4:30 p.m.'),

N('first-baptist-church-kalamazoo','First Baptist Church','Kalamazoo','mi','worship','standing',42.29129,-85.58638,'exact','open','walk','','1853',
  'Built in 1853 for a congregation that marked its 190th anniversary in 2026. A 2021 news report calls it one of the oldest structures in Kalamazoo County, and the congregation calls it the oldest public building in Kalamazoo. It stands on the old Church Square, north of Bronson Park. When the congregation could no longer afford its upkeep, a coalition of local nonprofits took it over in April 2021 to keep it from being torn down; the church still worships there as a tenant.',
  'A white-painted church with a square clock tower and pointed windows, on the corner of West Michigan Avenue and Church Street, part of the Bronson Park Historic District. Go in at the Sunday service; the inside was not checked.',
  '',
  'Owned since 2021 by the Kalamazoo Nonprofit Advocacy Coalition, with First Baptist as tenant, at 315 West Michigan Avenue; the service time is from the church\'s own page.'+DT,
  [['First Baptist Church of Kalamazoo','https://fbckazoo.org'],['Second Wave Media: New nonprofit owners of First Baptist Church (2021)','https://secondwavemedia.com/new-nonprofit-owners-of-first-baptist-church-dream-plan-future-as-anchor-in-downtown-ka-050621/'],W('Bronson Park Historic District')],
  brick='no',hours='Sunday 9:30 a.m. Bible study, 10:30 a.m. worship'),

N('first-presbyterian-church-kalamazoo','First Presbyterian Church','Kalamazoo','mi','worship','standing',42.28934,-85.58642,'exact','open','walk','','1928–1930',
  'A Late Gothic Revival church built from 1928 to 1930 after the congregation\'s 1885 brick church burned in 1926. It was designed by Charles Z. Klauder of Philadelphia, the architect of the Cathedral of Learning in Pittsburgh, and built by a father-and-son firm from the congregation. The congregation\'s founding is given as 1834 by one source and 1835 by another.',
  'Cut limestone over a steel and concrete frame, with a French flamboyant Gothic rose window high over the arched entrance on South Street. Inside, a lofty English open-truss nave with low arcaded side aisles and blue, purple and red glass by the Willett Studios of Philadelphia in the rose and chancel windows. Go in at the Sunday service.',
  '',
  'A working church at 321 West South Street, facing Bronson Park; the service time is from the church\'s own page.'+DT,
  [['SAH Archipedia: First Presbyterian Church',SAH+'KZ3'],['First Presbyterian Church of Kalamazoo','https://fpckzoo.org']],
  brick='no',hours='Sunday 10 a.m.'),

N('east-hall-wmu-kalamazoo','East Hall (Heritage Hall), Western Michigan University','Kalamazoo','mi','civic','standing',42.28628,-85.59689,'exact','view','walk','','1905',
  'The first building of the Western State Normal School, now Western Michigan University, finished in 1905 on Prospect Hill above the city; two wings were added by 1909. The university moved most of its work to a new campus from the late 1940s. In the 2010s North Hall and the side wings came down, the original part was kept, and it reopened in 2015 as Heritage Hall, the alumni centre, with North Hall\'s portico set up just north of it. On the National Register since 1978, and in the Western State Normal School Historic District.',
  'The original red brick block on the hilltop of East Campus, with the saved columned portico of North Hall beside it; the inside was not checked.',
  '',
  'Western Michigan University\'s alumni centre on East Campus, Prospect Hill, reached from Oakland Drive; seen from the campus grounds. Parking on campus was not checked.',
  [W('East Campus (Western Michigan University)')],
  brick='yes'),

]

PIN_NOTES={
 'ladies-library-association-kalamazoo':'ArcGIS address point for 333 South Park Street; on the building on the aerial.',
 'lawrence-chapin-building-kalamazoo':'ArcGIS street-address point for 201 North Rose Street, checked on the aerial.',
 'masonic-temple-kalamazoo':'ArcGIS street-address point for 309 North Rose Street, checked on the aerial.',
 'michigan-central-depot-kalamazoo':'ArcGIS address point for 459 North Burdick Street, checked on the aerial.',
 'old-central-high-school-kalamazoo':'ArcGIS address point for 714 South Westnedge Avenue, checked on the aerial.',
 'state-theatre-kalamazoo':'ArcGIS address point for 404 South Burdick Street, checked on the aerial.',
 'state-hospital-water-tower-kalamazoo':'Wikipedia article coordinate, in a courtyard of the hospital buildings. The tower could not be picked out with certainty on the aerial, so the pin marks the hospital grounds only.',
 'state-hospital-gatehouse-kalamazoo':'Wikipedia article coordinate, on the west side of Oakland Drive in trees; the address point fell on the road, and the cottage could not be picked out under the trees, so the pin marks the hospital entrance area only.',
 'kalamazoo-city-hall':'OpenStreetMap building for City Hall at 241 West South Street; on the building on the aerial.',
 'first-baptist-church-kalamazoo':'ArcGIS address point for 315 West Michigan Avenue, checked on the aerial.',
 'first-presbyterian-church-kalamazoo':'OpenStreetMap building for First Presbyterian Church; on the building on the aerial.',
 'east-hall-wmu-kalamazoo':'OpenStreetMap building named Heritage Hall; the Register point fell in the trees east of it.',
}
