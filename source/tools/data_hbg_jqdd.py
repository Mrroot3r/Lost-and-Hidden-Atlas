# November 26, 2026: Harrisburg, Pennsylvania, and the river just above it: the buildings and bridges named in one
# video about the city, each looked up and written from sources opened for this batch (Wikipedia read as raw text,
# SAH Archipedia's Buildings of Pennsylvania entries, FortWiki, the Department of General Services' news page,
# Amtrak's Great American Stations page and the cathedral parish's own page). The video itself is not a source.
from data_b import N
from data_ma import W

NRHP = ['Wikipedia: National Register listings in Dauphin County, Pennsylvania', 'https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Dauphin_County,_Pennsylvania']
BRIDGES = ['SAH Archipedia: Susquehanna River Bridges, Harrisburg', 'https://sah-archipedia.org/buildings/PA-02-DA8']

PLACES = [
N('harrisburg-state-hospital', 'Harrisburg State Hospital (Pennsylvania State Lunatic Hospital)', 'Harrisburg', 'pac', 'inst', 'standing',
  40.28429, -76.87659, 'site', 'view', 'drive', '', '1851–2006',
  'Pennsylvania\'s first public hospital for the mentally ill, set up in 1845 after lobbying by Dorothea Dix and opened in 1851 in a Kirkbride-plan main building by John Haviland. '
  'Between 1893 and 1912 it was rebuilt on the cottage plan by Addison Hutton and John A. Dempwolf; at its height it held more than 70 buildings and over 2,000 patients and was called the "City on the Hill". It closed on January 27, 2006.',
  look='A campus of separate old hospital buildings on the hill north of the city, mostly standing empty. One, the Cherrywood building, burned in December 2024 and was pulled down. In August 2024 the state announced a laboratory complex for the grounds: site work from early 2025, new building from 2026, with only the Administration Building, the Chapel, the Dix Museum and Dixmont Cottage to be restored. Expect demolition and construction; how much else still stands was not confirmed.',
  accn='State property (Department of General Services), on Cameron Street and Arsenal Boulevard. It is a construction site and not open: look from the public roads round it. Listed on the National Register in 1986 as the Pennsylvania State Lunatic Hospital.',
  links=[W('Harrisburg State Hospital'), ['Department of General Services: lab plans for the former hospital (August 2024)', 'https://www.pa.gov/agencies/dgs/newsroom/dgs-unveils-final-joint-laboratory-plans-for-former-harrisburg'], NRHP],
  brick='?'),

N('rockville-bridge', 'Rockville Bridge', 'Rockville', 'pac', 'rail', 'standing',
  40.3334, -76.9103, 'site', 'view', 'drive', '', '1900–1902',
  'The longest stone masonry arch railroad viaduct ever built: 48 arches of 70 feet, 3,820 feet in all, crossing the Susquehanna about 2 miles above Harrisburg between Rockville and Marysville. '
  'The Pennsylvania Railroad built it between April 1900 and March 1902, after a wooden bridge of 1849 and an iron one of 1877 on the same line. It still carries Norfolk Southern freight and Amtrak\'s Pennsylvanian.',
  look='The whole stone viaduct, still in use, seen from the river banks at either end.',
  hook='Forty-eight stone arches across a mile-wide river, still carrying trains.',
  accn='Owned and used by Norfolk Southern; an active main line. Stay off the tracks and the bridge and look from public roads near the Rockville and Marysville ends. Listed on the National Register in 1975 and named a National Historic Civil Engineering Landmark in 1979.',
  links=[W('Rockville Bridge'), NRHP],
  brick='no'),

N('marysville-bridge-piers-dauphin-narrows', 'Marysville Bridge piers and the Dauphin Narrows Statue of Liberty', 'Dauphin', 'pac', 'rail', 'ruins',
  40.35829, -76.92978, 'site', 'view', 'drive', '', '1858–1903',
  'The Northern Central Railway crossed the Susquehanna here, at the Dauphin Narrows between Marysville and Dauphin, on a covered bridge finished in 1858. Once the Pennsylvania Railroad took over the line in 1875 the trains went over the Rockville Bridge instead, and this one decayed and was taken down in 1902 or 1903. '
  'On July 2, 1986 a replica of the Statue of Liberty made of venetian blinds was put up on one of the old piers; after a windstorm destroyed it six years later, local people raised $25,000 for a 25-foot replica of wood, metal, glass and fiberglass.',
  look='Several of the old bridge piers stand above the water; others are under it or washed away. The Statue of Liberty replica stands on one of them in midstream.',
  hook='A covered railroad bridge gone for a century, and Lady Liberty on what is left of it.',
  accn='In the river. Seen from US 22/322 on the Dauphin side and from the Marysville bank; whether there is a place to pull off the highway was not confirmed, so do not stop on the highway shoulder.',
  links=[W('Marysville Bridge')], conf='mixed',
  brick='?'),

N('pennsylvania-state-arsenal-harrisburg', 'Pennsylvania State Arsenal', 'Harrisburg', 'pac', 'fort', 'standing',
  40.27700, -76.86700, 'site', 'view', 'drive', 'forts', '1874',
  'The state\'s first arsenal in Harrisburg went up in 1817 on Capitol Hill. In 1874 a bigger one was built here, at 18th and Herr Streets, away from the Capitol on higher ground: a tall central tower in front of a two-storey building, both with mansard roofs. '
  'In 1914 the building behind the tower was replaced by the present three-storey one, with crenellated parapets that give it the look of a fortress.',
  look='The 1874 tower and the 1914 building, both now without their mansard roofs, with a state roadside marker on Herr Street in front.',
  accn='State property, used as the Department of General Services\' public works complex. Not open to visitors: look from Herr Street and 18th Street.',
  links=[['FortWiki: Pennsylvania State Arsenal', 'https://www.fortwiki.com/Pennsylvania_State_Arsenal']], conf='mixed',
  brick='?'),

N('mulberry-street-bridge-harrisburg', 'Mulberry Street Bridge', 'Harrisburg', 'pac', 'landmark', 'standing',
  40.26121, -76.87506, 'site', 'public', 'walk', '', '1909',
  'A long concrete arch bridge that carries Mulberry Street over Cameron Street, Paxton Creek and the railroad, joining downtown Harrisburg to Allison Hill. It replaced an iron bridge with a wooden deck, put up in 1891, that was prone to fire. '
  'The concrete bridge of 1909 was designed by James Fuertes and is, in SAH Archipedia\'s words, still one of the largest concrete bridges in the country.',
  look='The row of concrete arches, best seen from Cameron Street below.',
  accn='A public street bridge: walk or drive across it, or look up at it from Cameron Street. Eligible for the National Register, not listed.',
  links=[W('Mulberry Street Bridge'), BRIDGES],
  brick='no'),

N('cathedral-st-patrick-harrisburg', 'Cathedral of Saint Patrick', 'Harrisburg', 'pac', 'worship', 'standing',
  40.26371, -76.88664, 'exact', 'open', 'walk', '', '1904–1907',
  'The cathedral of the Catholic Diocese of Harrisburg, on State Street a few blocks from the Capitol. The parish\'s first church here was begun in 1826; this one, designed by George I. Lovatt of Philadelphia, was begun in 1904 and finished on March 1, 1907.',
  look='Rough North Carolina granite with limestone trim and a copper-clad dome. Inside: granite columns along the nave, 44 stained glass windows from Munich, marble wainscoting and frescoes of the four Western Fathers of the Church under the dome. The altar was simplified in 1949–50.',
  accn='An active cathedral at 212 State Street. The main doors face State Street up steps; a ramp is on the Church Street side. Street parking (metered Monday to Saturday) and the South Street garage, free with validation on weekends for Mass. Mass times from the parish\'s own page, November 2026. A contributing building in the Harrisburg Historic District.',
  links=[W('Cathedral of Saint Patrick (Harrisburg, Pennsylvania)'), ['SAH Archipedia: St. Patrick\'s Roman Catholic Cathedral', 'https://sah-archipedia.org/buildings/PA-02-DA19'], ['Cathedral Parish of St. Patrick', 'https://stpatrickcathedral.com/']],
  brick='no', hours='Mass Monday to Friday 12 p.m.; Saturday 5:30 p.m.; Sunday 7:30 a.m., 9:30 a.m. and 12:15 p.m.'),

N('harrisburg-transportation-center', 'Harrisburg station (Pennsylvania Railroad station and train shed)', 'Harrisburg', 'pac', 'rail', 'standing',
  40.26205, -76.87774, 'exact', 'open', 'walk', 'stations', '1885–1887',
  'The third Pennsylvania Railroad station on this site, designed by the railroad\'s architect W. Bleddyn Powell and built in 1885–87, with the tracks of the main line between Philadelphia and Pittsburgh running under two train sheds behind it. '
  'An earlier station here, of 1857 by Joseph Hoxie, is the one in the photographs of Abraham Lincoln\'s funeral train. The building was restored in 1985–86 and is still the city\'s railroad and bus station.',
  look='A long red brick front with heavy brownstone lintels and deep brackets under the shelter roof; inside, a waiting room panelled in golden oak. It is one of the few American stations that still has a train shed over the tracks. The preserved electric locomotive PRR 4859 stands on one track.',
  accn='Owned by Amtrak and run by the Harrisburg Redevelopment Authority, at 4th and Chestnut Streets. Amtrak, intercity buses and Capital Area Transit use it. Paid parking. Waiting room hours from Amtrak\'s Great American Stations page, November 2026.',
  links=[W('Harrisburg Transportation Center'), ['SAH Archipedia: Harrisburg Transportation Center', 'https://sah-archipedia.org/buildings/PA-02-DA24'], ['Amtrak Great American Stations: Harrisburg', 'https://www.greatamericanstations.com/stations/HAR']],
  brick='yes', hours='Waiting room Monday to Friday 4:30 a.m. to 11:59 p.m.; Saturday and Sunday 6:45 a.m. to 11:45 p.m.'),

N('east-shore-ymca-harrisburg', 'YMCA building, North Front Street', 'Harrisburg', 'pac', 'civic', 'standing',
  40.26413, -76.88936, 'site', 'view', 'walk', '', '1931',
  'A big YMCA on the riverfront at 701 North Front Street, designed in 1931 by the Harrisburg architects Lawrie and Green in a Lombard Romanesque manner, after the Philadelphia firm Zantzinger, Borie and Medary\'s YWCA of 1913 in the city.',
  look='Dark red brick and terra-cotta, facing the river.',
  accn='A working YMCA branch, open to its members; look from Front Street and Riverfront Park. Hours were not read from the YMCA\'s own page.',
  links=[['SAH Archipedia: North Front Street', 'https://sah-archipedia.org/buildings/PA-02-DA5']],
  brick='yes'),
]

PIN_NOTES = {
  'harrisburg-state-hospital': 'OpenStreetMap\'s outline of the Administration Building; on the leaf-off aerial the pin is on a building among the old hospital blocks. The grounds spread about 400 m round it.',
  'rockville-bridge': 'OpenStreetMap\'s point for the bridge, over the river; on the aerial the pin is on the viaduct, with old piers of an earlier bridge showing in the water upstream.',
  'marysville-bridge-piers-dauphin-narrows': 'OpenStreetMap\'s point for the Statue of Liberty replica, on one of the piers in the river; the aerial shows the pin on a pier, with more piers in a line across the river.',
  'pennsylvania-state-arsenal-harrisburg': 'FortWiki\'s coordinate for 18th and Herr Streets; on the aerial it falls on a large building at that corner. Which part is the 1874 tower could not be told from above.',
  'mulberry-street-bridge-harrisburg': 'OpenStreetMap\'s line for the Mulberry Street Bridge, over Cameron Street; the aerial shows the pin on the bridge deck.',
  'cathedral-st-patrick-harrisburg': 'OpenStreetMap\'s point for the cathedral at 212 State Street; the aerial shows the pin on the domed church.',
  'harrisburg-transportation-center': 'OpenStreetMap\'s outline of the station building; on the aerial the pin is on the train shed roof beside the station.',
  'east-shore-ymca-harrisburg': 'ArcGIS address lookup of 701 North Front Street; on the aerial it falls on a large building on Front Street by the river. The building itself was not told apart from above.',
}

BATCH = {'key': 'hbg_jqdd', 'label': 'Harrisburg, Pennsylvania (from a video)', 'added': '2026-11-26 02:33'}
