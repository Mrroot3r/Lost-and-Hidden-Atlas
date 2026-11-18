# il_jasy: Illinois: Elsah, Grafton, Alton and Edwardsville
state: Illinois
region: il
date: 2026-11-18
places: 19
file: data_il_jasy.py

## What this batch is
Nineteen places on the Illinois side of the Mississippi above St. Louis, the first real batch for Illinois (region drawn by choose.py; Elsah drawn at random from six towns): Elsah village and its ice house ruin, the Principia College Maybeck campus, Pere Marquette State Park Lodge and the Smith-Duncan House and Eastman Barn, Grafton's Main Street with its ice house and 1846 wharf, the Ruebel Hotel, the Jersey County Courthouse, the Alton prison wall, McPike Mansion, the Lyman Trumbull House, the Yakel house and Union Brewery, the Godfrey Memorial Chapel, the Clifton Terrace terraces and wine cellar, the Old Chain of Rocks Bridge, the Stephenson House and LeClaire's Nelson factory in Edwardsville, the Kamp Store at Kampsville and Salem Baptist Church. Mostly standing places; three ruins (Elsah ice house, Alton prison wall, Clifton Terrace). Sources: Wikipedia read with wiki_raw.py (the Register list pages for Jersey, Calhoun and Madison counties gave the names), HMdb marker texts read with page.py, IDNR park and lodge pages, the NPS Route 66 page, Principia's campus page, stephensonhouse.org, historic-leclaire.org, the SIUE Madison Historical encyclopedia, the Village of Godfrey parks page and the Great Rivers & Routes / greatriverroad.com listings. Not checked: nothing was seen on the ground; hours for the Alton prison site, the courthouse, the Godfrey chapel, LeClaire campus and Pere Marquette park gates; the Kamp Store's hours (two listings disagree); who owns the Elsah ice house ruin and Salem Baptist Church; whether the Smith-Duncan buildings may be walked up to. Pins that are not on the thing: Principia (middle of the campus district), Grafton (middle of the district, not the ice house or wharf), Smith-Duncan and McPike (under trees, area), Clifton Terrace (on the terraces seen on LiDAR; the cellar not seen). Brick was set from Wikipedia photographs for the Ruebel Hotel, Stephenson House, Yakel house, McPike Mansion (all yes) and Salem Baptist (no); the Godfrey chapel, Principia and Grafton are left '?' (Wikimedia answered 429).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Alton Gas & Electric Power House | Alton, IL (38.8942, -90.1963) | 1913-14 substation for the Keokuk hydro plant, closed 1937, Abbott Machine Company since 1950 (Wikipedia) | Left out for room; a private works, view-only from West Broadway |
| Paris Mason Building | Grafton, IL (38.97139, -90.45028) | c. 1840 rock-faced limestone house and warehouse of the founder's brother (Wikipedia) | Owner and whether it can be seen from the street |
| New Piasa Chautauqua | Chautauqua, IL (38.9658, -90.3847) | 1885 Methodist summer resort, 200 cottages, private and semi-gated (Wikipedia) | What can be seen from Route 100 without entering |
| Cahokia Mounds and the Brooks Catsup Bottle | Collinsville, IL | Both on the Madison County Register list | Outside this batch's ground; IDNR hours for Cahokia |
| Lock and Dam 26 Confederate cemetery (HMdb) | Alton riverfront | Marker says graves of the prison's smallpox island were unearthed in 1935 | The marker number and what can be seen |

## Tips
- choose.py gave a whole state (Illinois, 1 place); a random draw among a few towns picked the ground inside it.
- The greatriversgreenway.org page for the Chain of Rocks Bridge hours (?p=12689) is 404 with no archived copy; the NPS page `nps.gov/places/chain-of-rocks-bridge.htm` gives parking and "open daily".
- A Mississippi bridge pin from OpenStreetMap can fall on the Missouri side of the state line: check.py refuses it for reg il. Pin the Illinois bank end.
- HMdb's nearby list for Elsah, Grafton and Alton gave the Elsah ice house ruin and the Clifton Terrace winery, which no Register list names; find the marker numbers by searching the cached page for `inscription<number>`.
- The Clifton Terrace stone terraces show plainly on the LiDAR sheet and not at all on the aerial.
