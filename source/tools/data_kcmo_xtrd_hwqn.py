# November 24, 2026: downtown Kansas City, the Crossroads and the West Side, Jackson County, Missouri.
# Part of filling in the Kansas City area on purpose for a local researcher. Earlier batches took the big downtown towers;
# these are Register-listed buildings in the Crossroads and the Power and Light district that the Atlas lacked.
# Facts come from the linked pages only: Wikipedia read as raw text (tools/wiki_raw.py) and Clio entries and a KCUR story read
# with tools/page.py. The National Register forms for all of these are not on line (NPGallery's copies are placeholders), so
# nothing here comes from a form. Hours were not found on pages that would open.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_xtrd', 'label': 'Kansas City: Crossroads and downtown (second pass)', 'added': '2026-11-24 13:56'}

PLACES = [
N('mainstreet-theater-kc', 'Mainstreet Theater (Empire Theater), Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.0971, -94.5836, 'site', 'view', 'drive', '', '1921',
  'The Mainstreet opened on October 30, 1921, as a 3,200-seat vaudeville and movie house designed by the Chicago firm Rapp and Rapp, the only Kansas City theatre they designed. It was renamed the RKO Missouri in 1941 and the Empire in 1960, when AMC bought it. A second theatre was built in its balcony in 1967 and it closed in 1985. '
  'The city bought it in 2004, when trees were growing from its roof, and it reopened in 2009 as part of the Power and Light District, later run by Alamo Drafthouse and then by B&B Theatres. B&B announced in March 2026 that it was leaving, and Wikipedia describes it as vacant.',
  look='A big downtown movie palace at 1400 Main Street with a mix of neoclassical and French Second Empire styling outside and a French Baroque interior, with a domed lobby ringed by round windows (Wikipedia). The 2008 renovation split the auditorium into smaller screening rooms, so how much of the original interior shows was not checked. A tunnel to the President Hotel said to have served bootleggers does not appear on the 1939 fire insurance map.',
  accn='Owned by The Cordish Companies and vacant since March 2026, so look from the street at Main and 14th. No hours. Street and garage parking downtown. Whether the building will reopen was not checked.',
  links=[W('Mainstreet Theater')], conf='mixed', hours='', brick='?'),

N('twa-headquarters-kc', 'TWA Corporate Headquarters Building (Barkley building), Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.09238, -94.58449, 'exact', 'view', 'drive', '', '1955–1956',
  'The three-storey L-shaped office building at 1735 Baltimore Avenue was built in 1955 and 1956 for Trans World Airlines, to a design by Raymond Bales Jr. and Morris Schechter. Its steel frame was raised first and the concrete floor slabs were poured on the ground and jacked up into place. '
  'TWA moved its executive offices to New York in 1964, but accounting, ticketing and cargo stayed here until 1969 and flight attendants trained here after that. It stood vacant for years, was restored from 2005 and has housed the advertising agency Barkley since 2006. It joined the National Register in 2002.',
  look='A flat modern office block clad in aluminium panels and corrugated concrete panels, once painted in TWA red and white. A 22-foot rocket, the TWA Moonliner II, stood on the roof corner; the original was sold off in 1962 and now sits at the TWA Museum at the downtown airport, while a replica was put back on the roof in 2006 (Wikipedia). Interior not checked.',
  accn='A working office building, so look from the sidewalk at 18th and Baltimore. Not open to the public. Street parking and garages in the Crossroads. Whether Barkley still leases it after 2015 was not checked.',
  links=[W('TWA Corporate Headquarters Building')], hours='', brick='no'),

N('jenkins-music-building-kc', 'Jenkins Music Company Building, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.09944, -94.58139, 'area', 'view', 'drive', '', '1911–1932',
  'The Jenkins Music Company, founded in 1878, made guitars and mandolins and published sheet music. Its six-storey fireproof building at 1217 Walnut Street, designed by Smith, Rea and Lovitt, was finished in 1912, and an eight-storey addition by Charles A. Smith followed in 1931 and 1932. '
  'The eighth floor held Steinway Hall, a recital room for about 240, and the fifth floor had a small broadcasting studio. The company hosted summer conferences of new music here in the late 1940s and 1950s, employed nearly 700 people in the 1950s and went bankrupt in 1971. The building joined the National Register in 1979.',
  look='A tall commercial building on Walnut Street that mixes late Gothic Revival and Art Deco detail, with step-backs at the eighth storey on the west front (Wikipedia, from the Register nomination). Wikipedia says a Kansas City developer owned it and planned apartments and shops; current use and interior were not checked.',
  accn='Private commercial property; look from Walnut Street. Downtown street and garage parking. No hours.',
  links=[W('Jenkins Music Company Building')], conf='mixed', hours='', brick='?'),

N('midwest-hotel-kc', 'Midwest Hotel, Kansas City', 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.08953, -94.58338, 'exact', 'view', 'drive', 'hotels', '1915',
  'The five-storey Midwest Hotel at 1925 Main Street opened in 1915, designed by Smith, Rea and Lovitt, and was the largest of the cheap hotels built south of downtown after Union Station opened in 1914. It had 75 rooms and housed single workers and travelling salesmen. '
  'The US War Department leased it for military police in the Second World War. It shut in 2005 after county prosecutors sued over drugs and prostitution, stood empty for years, and was restored as the amenity building of a 283-unit apartment block, City Club Apartments, opened in 2020. It joined the National Register in 2004.',
  look='A two-part commercial block of reinforced concrete and brick with terra cotta tiles framed by rosettes on the second to fifth floors and black Vitrolite glass tiles round the front. The restoration left the terra cotta front and exposed brick in place and the original structure shows inside (Clio). Interior not open to the public.',
  accn='Part of a private apartment complex, so look from Main Street; the Kansas City streetcar runs past on Main. Street parking and garages in the Crossroads. No visiting hours.',
  links=[W('Midwest Hotel'), ['Clio: Midwest Hotel Building', 'https://theclio.com/entry/141900']], hours='', brick='some'),

N('monroe-hotel-kc', 'Monroe Hotel, Kansas City', 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.09167, -94.58389, 'area', 'view', 'drive', 'hotels', '1920–1971',
  'The five-storey Monroe Hotel at 1904 Main Street was designed by Raymond Sanneman in 1920 and opened in 1921 as a cheap hotel for workers and travelling salesmen near Union Station. The political boss Tom Pendergast bought it in 1924 and had Sanneman design the two-storey Jackson County Democratic Club beside it as his headquarters, with a door from his office into the hotel. '
  'A federal court ordered the door sealed after Pendergast came out of prison in 1939. The hotel closed in 1971 and was later made into condominiums. The sources differ slightly on the date: Wikipedia gives 1920 for the building and Clio gives 1921 for the opening.',
  look='A five-storey Commercial-style building of reinforced concrete and brick, with terra cotta on the two lower floors, and a large marquee over the entrance that still reads Monroe Hotel (Clio). Interior not checked.',
  accn='Now private condominiums (Hotel Monroe), so look from Main Street. Street parking and garages nearby. No hours.',
  links=[W('Monroe Hotel'), ['Clio: Monroe Hotel Building', 'https://theclio.com/entry/141829']], conf='mixed', hours='', brick='some'),

N('webster-school-kc', 'Webster School (Webster House), Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.09306, -94.58611, 'site', 'view', 'drive', '', '1885–1932',
  'Webster School at 1644 Wyandotte Street was built in 1885 and opened in 1886, one of the oldest public school buildings still standing in Kansas City and one of the few Richardsonian Romanesque buildings left in the city. Manuel Diaz, the school board\'s first architect, designed it; Charles Mumma was the carpenter. '
  'It closed as a school in 1932, was leased to the state for Social Security offices, then housed the Midland Radio School from 1945. The Historic Kansas City Foundation bought it in 1978, it stood vacant from 1977 until the late 1990s, and a philanthropist paid for its restoration. It was a restaurant and antique shop from 2002 to 2020. In 2021 plans were announced to make it the Kansas City Symphony\'s headquarters. The sources give 1885 and 1886 for the opening.',
  look='A two-storey Victorian school with Romanesque and Italianate detail, unlike the plainer schools that came later. Red brick walls with stone trim, a corner tower and steep roofs (a Commons photograph opened for this entry). Whether the Symphony conversion went ahead, and what the inside looks like now, was not checked.',
  accn='Check who uses it now before going: it was announced as the Symphony\'s headquarters in 2021 and was a restaurant until 2020. Look from Wyandotte Street. Street parking in the Crossroads. No hours found.',
  links=[['Clio: Webster House, formerly the Webster School', 'https://theclio.com/entry/156425']], conf='mixed', hours='', brick='yes'),

N('guadalupe-center-kc', 'Guadalupe Center (Guadalupe Centers), Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.08578, -94.59694, 'site', 'view', 'drive', '', '1919',
  'A Catholic women\'s club opened a volunteer school and clinic in 1919 for Mexican immigrants who had settled on Kansas City\'s West Side, and named it for Mexico\'s patron saint. Clio calls it one of the first social service agencies for Latinos in the country. '
  'The agency, now Guadalupe Centers, still works on the West Side, and its building at 1015 Avenida Cesar Chavez is on the National Register of Historic Places (listed 2003 per Wikipedia\'s list). The date of the present building was not read from a source and is not given here.',
  look='A two-storey Spanish-style building of white stucco with a red tile roof and an outside stair, on the West Side (a Commons photograph opened for this entry). What can be seen inside was not checked.',
  accn='A working community centre, so look from the street and ask at the centre about visiting. Street parking on the West Side. No hours found.',
  links=[['Clio: Guadalupe Centers', 'https://theclio.com/entry/64119']], conf='mixed', hours='', brick='no'),

N('our-lady-of-guadalupe-shrine-kc', 'Our Lady of Guadalupe Shrine, Kansas City', 'Kansas City', 'kcmo', 'worship', 'standing',
  39.0856, -94.59492, 'exact', 'view', 'drive', '', '1922',
  'Our Lady of Guadalupe Parish opened here in 1922 and is described as the first Mexican Catholic church in Kansas City. The diocese threatened to close it in 1990 and the congregation persuaded it to rededicate the church as a shrine in 1991, merging with Sacred Heart parish, whose church on Madison Avenue is now the main building. '
  'A 2024 story says the stone building is falling apart and the congregation was raising up to $900,000 for repairs, with the stairs, ceiling and some outside stones fixed that summer.',
  look='A large church of gray stone on the West Side with a spire that shows over the trees from Southwest Boulevard and stained glass windows showing the apparition of Our Lady of Guadalupe, with a white statue of Juan Diego and Our Lady outside (KCUR). Mass is held there only now and then.',
  accn='A parish-run shrine at 2300 Madison Avenue. When it is open was not found; the main parish church is Sacred Heart Guadalupe, on Madison Avenue. Street parking. No hours found.',
  links=[['KCUR: Kansas City Latinos rally to save a crumbling, century-old Catholic shrine', 'https://www.kcur.org/history/2024-08-05/our-lady-guadalupe-shrine-kansas-city-westside-latino-catholic']], hours='', brick='no'),
]

PIN_NOTES = {
  'mainstreet-theater-kc': 'The coordinate is from Wikipedia and the Register list for 1400 Main Street.',
  'twa-headquarters-kc': 'The coordinate is from Wikipedia for 1735 Baltimore Avenue.',
  'jenkins-music-building-kc': 'The coordinate is from the Wikipedia infobox for 1217 to 1223 Walnut Street. On the aerial the building could not be picked out with certainty, so the pin marks the block.',
  'midwest-hotel-kc': 'The coordinate is from OpenStreetMap for 1925 Main Street.',
  'monroe-hotel-kc': 'The coordinate is from Wikipedia for 1904 Main Street. On the aerial the building could not be picked out with certainty, so the pin marks the block.',
  'webster-school-kc': 'The coordinate is from the Register list for 1644 Wyandotte Street.',
  'guadalupe-center-kc': 'The coordinate is from the Register list for the Guadalupe Center.',
  'our-lady-of-guadalupe-shrine-kc': 'The coordinate is from OpenStreetMap for the shrine at 2300 Madison Avenue.',
}
