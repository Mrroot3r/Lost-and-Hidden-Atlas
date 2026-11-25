# November 25, 2026: leftovers of the Kansas City area that earlier batches did not reach: Liberty and
# Smithville (Clay County), and Independence. The Atlas already holds nearly every listing
# on the National Register in Jackson, Clay, Platte and Cass counties, so this batch is small. Sources: Wikipedia read as raw text, the
# pages of Missouri State Parks, KCUR, Kansas City magazine, KSHB and Northeast News, and web search results that quote them.
from data_b import N
from data_ma import W

BATCH = {'key': 'mo_hgxr', 'label': 'Kansas City area: Liberty, Smithville, Independence, Platte County', 'added': '2026-11-25 02:51'}

PLACES = [
N('englewood-theater-independence-mo', 'Englewood Theater, Winner Road, Independence', 'Independence', 'kcmo', 'civic', 'standing',
  39.08753, -94.44877, 'exact', 'view', 'drive', '', '1949',
  'The Englewood opened with a gala on July 7, 1949, when Winner Road was newly part of Independence; the first picture shown was the western Colorado Territory. It later held the KC Opry country music show (1978–1989 according to Cinema Treasures), then stood empty for about twenty years. A nonprofit, Friends of Englewood Theater, bought it in 2025, and news reports say it has been approved for or placed on the National Register of Historic Places. Local reporting calls it the last Art Deco theater in the Kansas City area.',
  look='A neighbourhood cinema with a marquee on Winner Road, in the Englewood Arts District. Inside, backstage walls carry hundreds of signatures left by KC Opry performers. Northeast News reported that the owners gave their first public tours during the district\'s Third Friday event on March 20 and would repeat them at each Third Friday until interior renovation begins; confirm on the owners\' pages before going. The exact register listing date was not confirmed.',
  accn='Privately owned by the nonprofit Friends of Englewood Theater, 10917 E. Winner Road. Look from the street; street parking along Winner Road. Interior only on the occasional Third Friday tours described above.',
  links=[['KSHB: placed on the National Register', 'https://www.kshb.com/news/local-news/missouri/jackson-county/englewood-theater-placed-on-national-historic-register-as-nonprofit-ownership-begins-renovation-plans'], ['Kansas City magazine: back in community hands', 'https://kansascitymag.com/the-historic-englewood-theater-is-back-in-community-hands-and-set-to-become-a-cultural-hub-for-eastern-jackson-county/'], ['Northeast News: public tours', 'https://northeastnews.net/pages/historic-theater-re-envissioned-offers-public-tours/'], ['Cinema Treasures', 'https://cinematreasures.org/theaters/1464']],
  hours='', brick='?', conf='mixed'),

N('liberty-arsenal-site-liberty-mo', 'Liberty Arsenal (Missouri Depot) site, Liberty', 'Liberty', 'kcmo', 'fort', 'gone',
  39.19906, -94.40650, 'area', 'view', 'drive', '', '1837–1861',
  'The federal government bought ten acres near Liberty in 1837 for an arsenal on the western frontier, finished in 1839. By 1841 it had officers\' and men\'s quarters, a storehouse, a magazine, workshops, an armory, gun sheds and laboratories. Pro-slavery men seized it in 1855 during the Kansas troubles and again early in the Civil War, in April 1861.',
  look='No standing building is reported: Fortwiki says no visible remains and Legends of America says nothing remains. On the aerial the pin falls on the edge of an active quarry. A marker placed in 2012 at the highway junction names the depot as lying on the bluffs a quarter mile to the southwest. One KCUR photo caption calls what is visible there the only remains of the depot; that may mean the marker. Wikipedia places the site west of the junction of Route 291 and old 210 Highway.',
  accn='The arsenal site and more than 100 acres around it belong to private family trusts and have been closed to the public for over a century; KCUR reported in 2018 that the owners refused a history group access. Look only from the public highway at the marker. The pin is Wikipedia\'s coordinate for the site and marks the general area.',
  links=[W('Liberty Arsenal'), ['KCUR: a public park on the hilltop?', 'https://www.kcur.org/arts-life/2018-06-15/history-lovers-renew-hope-for-a-public-park-on-a-storied-hilltop-in-clay-county'], ['Fortwiki: Liberty Arsenal', 'https://fortwiki.com/Liberty_Arsenal']],
  hours='', brick='?', conf='mixed'),

N('aker-cemetery-smithville-mo', 'Aker Cemetery, Smithville', 'Smithville', 'kcmo', 'burial', 'traces',
  39.41111, -94.54556, 'area', 'view', 'drive', '', '1835–1882',
  'Aker Cemetery is a small family burying ground begun about 1835 by the Aker family, who came from Kentucky. The Register says it is the only remaining evidence of the first settlers in the area. It holds 25 graves, ten of them marked, dated 1835 to 1882, and was listed on the National Register of Historic Places in 1974.',
  look='A half-acre plot in woods with little undergrowth. The federal public-land map puts the pin inside the Smithville Recreation Area at Smithville Lake, on a wooded point with a paved loop beside it (aerial, bare trees). The 1974 nomination described it as in poor condition with stones lying on the ground; its present condition was not checked.',
  accn='No page read says who owns the plot, whether the public may visit, or where to park. It lies northeast of Smithville off Route W. Treat it as view only from the road and ask the Clay County or Smithville historical societies before going on to any private land. The pin is the Wikipedia coordinate and was not confirmed on the ground.',
  links=[W('Aker Cemetery'), ['National Park Service listing 74001071', 'https://npgallery.nps.gov/AssetDetail/NRIS/74001071']],
  hours='', brick='?', conf='mixed'),

N('west-liberty-courthouse-square-district-liberty-mo', 'West Liberty Courthouse Square Historic District (three Italianate shops), Liberty', 'Liberty', 'kcmo', 'civic', 'standing',
  39.24639, -94.42056, 'area', 'view', 'walk', '', '1877–1885',
  'Three adjoining commercial buildings on the west side of the courthouse square in Liberty, built between 1877 and 1885, form this small district. Wikipedia calls them representative examples of Italianate commercial architecture. It was listed on the National Register of Historic Places in 1992.',
  look='Look at the upper fronts: Italianate shopfronts of that period usually carry bracketed cornices and tall arched windows, but the detail of these three was not read in a source. The pin sits in the middle of the square; which three buildings they are was not checked. Whether they are brick was not checked.',
  accn='Ordinary shops and offices around the courthouse square; look from the sidewalk. Street parking around the square. Business hours are the businesses\' own.',
  links=[W('West Liberty Courthouse Square Historic District')],
  hours='', brick='?', conf='mixed'),

N('woodson-sawyer-house-independence-mo', 'Woodson-Sawyer House (Araby West), Independence', 'Independence', 'kcmo', 'landmark', 'standing',
  39.08722, -94.43444, 'site', 'view', 'drive', '', 'c. 1866',
  'A historical marker, as quoted in web search results, says this brick Italianate house was built about 1866 by Samuel Hughes Woodson, a lawyer, congressman and land developer. It is also known as Araby West. It was listed on the National Register of Historic Places in 1986; the Park Service record gives significant years of 1865 and 1881, so the building date is approximate.',
  look='A two-story brick Italianate house, four bays wide and six deep according to the National Register form as summarised in search results. The porch may have been added about 1910 by the Woodsons\' daughter; the form only suggests this. Interior not checked.',
  accn='A private house at 1604 W. Lexington Avenue; look from the public sidewalk and do not enter the grounds. Street parking nearby. The marker text and the Register form could not be opened directly when this was written, so these details come from search-result quotations.',
  links=[['National Register listing 86000457 (History Pointer)', 'https://historypointer.com/nris/resource/86000457'], ['Historical Marker Database: Woodson-Sawyer House', 'https://www.hmdb.org/m.asp?m=144554']],
  hours='', brick='yes', conf='mixed'),
]

PIN_NOTES = {
  'englewood-theater-independence-mo': 'Address lookup for 10917 E. Winner Road.',
  'liberty-arsenal-site-liberty-mo': 'Wikipedia coordinate for the arsenal; the land is private so the pin marks the general area.',
  'aker-cemetery-smithville-mo': 'Wikipedia and National Register coordinate, about 39 deg 24 min 40 sec N, 94 deg 32 min 44 sec W.',
  'west-liberty-courthouse-square-district-liberty-mo': 'Wikipedia coordinate, in the courthouse square.',
  'woodson-sawyer-house-independence-mo': 'Wikipedia list coordinate for the house at 1604 W. Lexington; the aerial shows a large wooded lot on Lexington Avenue and the house was not picked out under the trees, so the pin marks the site.',
}
