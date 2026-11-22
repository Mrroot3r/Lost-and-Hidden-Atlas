# tacoma_zudq: Tacoma: old downtown and Stadium District
state: Washington
region: wa
date: 2026-11-22
places: 16
file: data_tacoma_zudq.py

## What this batch is
Sixteen standing places in Tacoma, Washington, from the names in one walk-through video about the city's old buildings (Old World Exploration, July 2025; the record is source/videos/20250704_wKD_l_i6dkk.md). The video was used only as a list of names. Added: Old City Hall, the Northern Pacific Office Building, the Bostwick, the Pantages and Rialto theatres, the Elks Temple (McMenamins), the Perkins and Sprague buildings, the 1908 armory, the Carnegie main library, Urban Grace (First Baptist) church, Stadium and Lincoln high schools, the closed Holy Rosary church, the Rust mansion, and Wright Park with the Seymour Conservatory. Sources: Wikipedia as raw text and its Pierce County Register list; the City of Tacoma Register of Historic Places PDF (updated January 5, 2026), which gives address, year and architect for every city landmark; HistoryLink and Tales of Tacoma for the armory; Seattle Met for the Bostwick; the city's Prairie Line Trail page for the Sprague; Lee & Associates and the developer's page for Old City Hall's conversion. Pins are ArcGIS PointAddress results for each street address, all looked at on the aerial; the armory's was on the street and was moved to the building OpenStreetMap names Armory. Red brick was settled from the sources or from a Commons picture of each building; the Carnegie library, the Perkins (dark brown brick) and the armory stay '?'. Not checked: anything on the ground; whether Old City Hall's first phase has opened; the Pantages, Rialto and Seymour Conservatory hours (their pages refused automated reading); the library's hours on days other than Tuesday and Thursday; the armory's current owner; parking (downtown lots from OpenStreetMap only, owners and fees unknown). Year disagreements are given in the text: Holy Rosary (1920 on Wikipedia, 1929 on the city register), the armory (1908 HistoryLink, 1909 register), Urban Grace (1924 or 1925), Wright Park (1886 or 1890).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Masonic Temple and Temple Theater | Tacoma, WA (47.262081, -122.444189) | 1927 Art Deco lodge and theatre by Ambrose J. Russell, city landmark at 47 St. Helens Avenue (city register; Register list) | A page saying when the theatre is open, and a read of its history |
| Pythian Temple | Tacoma, WA (47.254858, -122.439639) | 1906 lodge by Frederick Heath at 924-926 Broadway (city register; Register list) | Whether the lodge rooms can be seen, and a fuller source |
| U.S. Post Office and Federal Building, downtown | Tacoma, WA (47.253044, -122.436222) | Built 1910, on the National Register (Wikipedia list) | Read its article and current use |
| St. Luke's Memorial Church | 3615 North Gove Street, Tacoma, WA | City landmark, dates 1883 and 1936 (city register) | Why two dates (moved or rebuilt?), service times |
| Job Carr Cabin Museum | Tacoma, WA | Museum named for Job Carr; its own site is jobcarrmuseum.org | Whether the cabin is the 1865 original or a replica, and hours (page not read) |

## Tips
- The City of Tacoma Register of Historic Places PDF (cms.tacoma.gov, "publication landmarks register" with the date) reads in full with `page.py --all -n 200000` and gives address, built year and architect for about 200 landmarks: the fastest way to settle Tacoma names.
- parkstacoma.gov (Metro Parks Tacoma) and tacomaartslive.org answer HTTP 403 to `page.py` and `hours.py`, with no archived copy; web searches for them returned links only.
- The Register list coordinate for the Perkins Building is the Tacoma Building's (47.2628, -122.434797, shared by both rows); the address lookup of 1101 A Street is right.
- `wiki_raw.py --rows ... | grep -i tacoma` misses most Tacoma rows (the town column is blank); filter by latitude instead.
