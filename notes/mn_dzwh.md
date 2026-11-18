# mn_dzwh: Washington County, Minnesota: St. Croix lumber towns, Stillwater and Scandia
state: Minnesota
region: mn
date: 2026-11-18
places: 14
file: data_mn_dzwh.py

## What this batch is
Fourteen places in Washington County, Minnesota, the first real pass in the state: the Marine Mill ruins and the 1872 stone township hall at Marine on St. Croix, Arcola Mills (1847 house and sawmill chimney), the St. Croix Boom Site, Stillwater's Warden's House (with the territorial prison's story), Isaac Staples' sawmill powerhouse, the 1870 courthouse, the Lift Bridge, the NYA overlook built of prison stone, the 1932 Log Cabin roadhouse, the 1863/65 stone arch on the Point Douglas military road, the 1873 Gateway Trail iron bridge, the Hay Lake School with the Erickson log house, and Gammelgården's 1856 log church. Sources were read with wiki_raw.py and page.py: Wikipedia, the Washington County Historical Society's pages, MNHS's Marine Mill pages, DNR trail and wayside pages, MnDOT's historic bridge and roadside pages, the county's courthouse page, Gammelgården's own pages, the Arcola Mills foundation's page and HMdb marker texts. Not checked: anything on the ground; hours for Marine Mill (MNHS's hours page shows none), the Stone House Museum, the Boom Site, the overlook, the two trails and the shops/restaurant; whether the Warden's House closes in winter; admission at Gammelgården. Arcola Mills says it is closed for habitat work (ask first). The Point Douglas bridge is private and view-only from Brown's Creek State Trail; its builder and year differ between Wikipedia (Willim, 1865) and the DNR panel (Hanly and Curtis, 1863), both given. No parking point for Marine Mill, Arcola, the two bridges on trails, the overlook, the Log Cabin or Gammelgården. Brick from pictures opened with brick.py look (courthouse and Hay Lake School red brick; Staples limestone; Log Cabin one brick chimney) or from the sources' words; the Boom Site left '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Grey Cloud Lime Kiln | Cottage Grove, MN (44.798406, -92.978055) | Mortarless limestone kiln of about 1850 by the Mississippi; Wikipedia says it collapsed in June 2014 and the property owner blamed heavy rain | Whether anything stands, and any public view; private land |
| Soo Line High Bridge (Arcola High Bridge) | Stillwater Township, MN (45.1231, -92.7442) | 1910–11 steel deck arch by C.A.P. Turner over the St. Croix (Wikipedia) | A public place to see it from, and whether the line is still active; the NPS paddling map for "High Bridge to Boom Site Landing" answered 404 |
| St. Croix Boom Company house and barn | Stillwater Township, MN (45.086468, -92.784972) | About 1885, the only buildings left of the boom (Register list) | Owner and whether visible from Highway 95 or the wayside |
| Marine Village Hall | Marine on St. Croix, MN | 1888; a 2017 marker calls it the oldest town hall in Minnesota still used for government | A coordinate and its own source; could join the Stone House entry |
| Cushing Hotel and Afton Greek Revival houses | Afton, MN (44.900893, -92.78276) | 1867 hotel, 1856 Bolles and 1864 Gilbert houses on the Register list | Present use and public view; all look private |
| John T. Cyphers House | Lakeland, MN (44.958208, -92.766406) | 1858 house of mortared unsplit boulders (Register list) | Present owner; private house, view only at best |

## Tips
- publish.sh's check refuses an email address anywhere in a data file, even a public contact address from a managing body's page: write "its contact is on the visit page" instead.
- MNHS's Marine Mill hours page (mnhs.org/marinemill/visit/hours) comes back through page.py with the "Hours" heading empty; the hours are probably drawn by script.
- washingtoncountymn.gov/3089/Tours answers 404; the courthouse's public hours are on washingtoncountymn.gov/3472.
- wiki_raw.py strips {{convert}} templates, so lengths and heights vanish from the text ("a  stone chimney"); take numbers from HMdb or MnDOT instead.
- places_test.js fails only on onesquethaw-valley ("18th century" under "Standing, from before 1800"); this batch changes nothing it reads.
