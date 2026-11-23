# November 23, 2026: a second pass over Independence, Jackson County, Missouri, for a local researcher.
# Facts from the linked sources only: Clio's Independence Heritage Trail, the City of Independence's page for the log courthouse,
# the National Park Service's hours page, Wikipedia read as raw text. The National Register forms were not read.
from data_b import N
from data_ma import W

CLIO = ['Clio: Independence Missouri Heritage Trail', 'https://www.theclio.com/tour/855']
NRHP = ['Wikipedia: National Register listings in Jackson County, Missouri', 'https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Jackson_County,_Missouri']

BATCH = {'key': 'kcmo_ind2_qfhm', 'label': 'Independence, Missouri (second pass)', 'added': '2026-11-23 23:46'}

PLACES = [
N('log-courthouse-1827-independence-mo', '1827 Log Courthouse', 'Independence', 'kcmo', 'civic', 'standing',
  39.09084, -94.41633, 'exact', 'open', 'drive', '', '1827',
  'A log building put up in 1827, the year Independence was founded, by the merchant Algernon Sidney Gilbert as his house and store, which also supplied freighters bound for the Santa Fe Trail. It was later used for Jackson County government, and Harry S. Truman held sessions of the county court here in 1932 and 1933 while the main courthouse was being enlarged. Clio says a mob destroyed part of it in 1833, when the Mormons were driven out of the county.',
  look='A small log building with a 1976 marker beside it. The City of Independence says it was the only courthouse between Independence and the Pacific for more than 40 years. Interior not checked.',
  accn='Run by the City of Independence Parks and Recreation at 107 West Kansas Avenue, a block south of the square. The city page says tours are by appointment: call 816-325-7575. Other listings say seasonal or by appointment; no set hours were found. Street parking.',
  links=[['City of Independence: 1827 Log Courthouse', 'https://independencemo.gov/visitors/our-history-and-culture/1827-log-courthouse'], ['Clio: 1827 Log Courthouse', 'https://theclio.com/entry/10673'], ['Truman Library: 1827 Jackson County Log Courthouse', 'https://www.trumanlibrary.gov/education/student-resources/places/independence/1827-jackson-county-log-courthouse']],
  brick='no', hours='By appointment: call 816-325-7575'),

N('kritser-house-independence-mo', 'Kritser House', 'Independence', 'kcmo', 'landmark', 'standing',
  39.08944, -94.41472, 'area', 'view', 'drive', '', 'about 1850',
  'A small house of about 1850 named for Martin U. Kritser, its first owner and builder, who took part in the town\'s early growth. Wikipedia calls it one of the few middle-class houses of the mid-Victorian frontier period left in Independence. It was listed on the National Register in 1985. Clio notes a modern addition at the back.',
  look='A modest house with a historical marker in front. Wikipedia gives the date as 1850 and Clio as around 1850. Interior not checked.',
  accn='Private or institutional use was not checked; look from the street. No hours found.',
  links=[W('Kritser House'), CLIO, NRHP],
  conf='mixed', brick='?'),

N('truman-visitor-center-fire-station-independence-mo', 'Truman Site Visitor Center (1928 Independence Fire Station No. 1)', 'Independence', 'kcmo', 'civic', 'standing',
  39.09360, -94.41542, 'exact', 'open', 'drive', '', '1928',
  'The visitor center of the Harry S Truman National Historic Site is in the old Independence Fire Station No. 1, built in 1928. Clio says it is a contributing building of the Harry S. Truman National Historic Landmark District.',
  look='A 1928 fire station used as the ticket and information point for the Truman Home tours. Interior not checked.',
  accn='Managed by the National Park Service at 223 North Main Street; this is where Truman Home tickets are sold. The Park Service says the site is open Wednesday to Sunday and closed Monday and Tuesday; the page read gave no hours for the center itself.',
  links=[['National Park Service: hours and seasons', 'https://www.nps.gov/hstr/planyourvisit/hours.htm'], CLIO],
  brick='?', hours='Wednesday to Sunday; closed Monday and Tuesday (daily hours not given on the page read)'),

N('temple-lot-independence-mo', 'Temple Lot', 'Independence', 'kcmo', 'worship', 'marker',
  39.09068, -94.42797, 'site', 'view', 'drive', '', '1831',
  'The first site dedicated for a temple in the Latter Day Saint movement: Joseph Smith dedicated the area on August 3, 1831, and Edward Partridge bought about 63 acres on December 19, 1831. The Saints were driven from the county before a temple was built. Wikipedia says the small Church of Christ (Temple Lot) has owned the lot itself since 1867, and the Community of Christ owns most of the surrounding ground. A court case over ownership began in 1891.',
  look='A plot of open ground, not a ruin: no temple was ever finished here. Wikipedia says the Temple Lot church tried and failed to build a temple of its own in 1929. Nearby are the Community of Christ Auditorium and its Independence Temple. What can be seen from the street was not checked.',
  accn='Private religious land. The Temple Lot church owns it; the Community of Christ owns the ground around it. Whether the lot is open to visitors, and when, was not checked: look from the public street.',
  links=[W('Temple Lot')],
  brick='no', hours=''),

N('community-of-christ-auditorium-independence-mo', 'Community of Christ Auditorium', 'Independence', 'kcmo', 'worship', 'standing',
  39.0898, -94.4283, 'site', 'view', 'drive', '', '1926–1958',
  'A domed church headquarters building on the greater Temple Lot at 1001 West Walnut. Ground was broken in 1926, building stalled in the Depression, and it was finished in 1958 at about two-thirds the planned size of its main chamber, which seats 5,800. President Truman spoke there on June 27, 1945.',
  look='A large domed building, 114 feet to the top of the dome. Wikipedia says it holds an Aeolian-Skinner organ of 113 ranks and 6,334 pipes. The article names it as a brick church; the colour and any interior access were not checked, and that article marks parts of itself as unsourced.',
  accn='Owned by the Community of Christ. Visiting hours for the building, and for the organ the church invites people to hear, were not checked: see the church\'s own visit page for the organ.',
  links=[W('Auditorium (Community of Christ)'), ['Community of Christ: organ visit page', 'https://cofchrist.org/visit-auditorium-organ']],
  conf='mixed', brick='?', hours='?'),

N('first-presbyterian-church-independence-mo', 'First Presbyterian Church', 'Independence', 'kcmo', 'worship', 'standing',
  39.09259, -94.42168, 'site', 'view', 'drive', '', '',
  'Where Harry Truman and Bess Wallace met in Sunday school in 1892; Clio quotes Truman on it. Clio adds that the Kansas City Times, before it was finished, called it the handsomest church between Chicago and Denver. The building\'s date was not given on the page read.',
  look='A church on West Lexington Avenue close to the square. Original glass and woodwork, and any hours for visitors, were not checked.',
  accn='An active church. Service times were not checked: look from the street.',
  links=[CLIO],
  conf='mixed', brick='?'),
]

PIN_NOTES = {
 'log-courthouse-1827-independence-mo': 'OpenStreetMap places the courthouse at 107 West Kansas Avenue; checked on the aerial.',
 'kritser-house-independence-mo': 'Coordinate from the Wikipedia article. On the aerial the pin falls among trees and small houses and the house itself could not be picked out, so it marks the area only.',
 'truman-visitor-center-fire-station-independence-mo': 'OpenStreetMap places the visitor center at 223 North Main Street; checked on the aerial.',
 'temple-lot-independence-mo': 'Coordinate from the Wikipedia article for the lot.',
 'community-of-christ-auditorium-independence-mo': 'Coordinate from the Wikipedia article for the Auditorium.',
 'first-presbyterian-church-independence-mo': 'OpenStreetMap place of worship on West Lexington Avenue.',
}
