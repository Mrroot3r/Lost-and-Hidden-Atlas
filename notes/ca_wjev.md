# ca_wjev: California: Downieville, Sierra City and the Henness Pass Road
state: California
region: ca
date: 2026-11-19
places: 22
file: data_ca_wjev.py

## What this batch is
22 places in Sierra County, California, the first batch in California beyond Sutro Baths: the gold-rush business block of Downieville (museum in the 1852 Old Slate Store, the Craycroft, Mackerman and Hirshfeldter buildings, the 1855 foundry, the 1858 Catholic church, the 1864 Masonic hall, the 1885 gallows, the Hospital and Jersey truss bridges), Goodyears Bar (1862 schoolhouse, St. Charles Hotel), Sierra City (Kentucky Mine and stamp mill, Busch Building, Miner's Hotel, Sierra Buttes lookout), Forest City (the Forest Service townsite and its dance hall), Alleghany (Sixteen to One Mine) and the Henness Pass Road country to the east (Webber Lake Hotel, Kyburz Flat petroglyph and More's Station, Wheeler sheep camp oven, Sierraville School). Sources: HMdb marker pages read with `page.py --all` (most pins are HMdb marker positions), National Register forms from NPGallery, Wikipedia via `wiki_raw.py`, the Sierra County Historical Society (Kentucky Mine page and The Sierran, Winter 2019), Truckee Donner Land Trust pages, The Mountain Messenger, NoeHill, the National Forest Foundation. Not checked: anything on the ground; interiors; hours for the Downieville Museum (season only), Downieville Foundry, Forest City dance hall, Goodyears Bar schoolhouse and the Alleghany museum; Tahoe National Forest's own pages for Kyburz Flat and the Sierra Buttes lookout (404), so season and rules there are not checked; mountain-road and winter access for Forest City, Alleghany, Kyburz Flat and Webber Lake. Pins that are a marker and not the building itself: Sixteen to One Mine (prec area), the gallows (marker beside the courthouse). The Sierra Buttes trailhead point is an OpenStreetMap lot, not confirmed as the Packer Lake Road trailhead. The Sierraville School pin was moved off the highway onto the building taken to be the school. Red brick is '?' for most buildings: no picture was opened.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Sierra City School | Sierra City, CA (39.5671, -120.6302, Register list) | One-room school of 1883, listed on the National Register January 2024 (Wikipedia, Sierra City article) | The NPGallery text (100009718) is a placeholder and the state's draft PDF read only 726 characters; owner, use and a pin check |
| Durgan Bridge | Downieville, CA (39.559714, -120.8294) | 1938 one-lane Pratt through truss, 140 ft, on Nevada Street over the North Yuba, by Judson Pacific (nomination 12000398) | Left out only to keep the town from being all bridges; could be added from the form |
| Hansen Bridge | Downieville, CA (39.56313, -120.82517) | 1935 Pratt pony truss, 80 ft, over the Downie River (nomination 12000399) | As above |
| 1872 California-Nevada boundary marker | near Verdi, NV (HMdb 94295, 39.524581, -120.002033) | Cast-iron pylon 8 ft tall, one of four set by Von Schmidt in 1872-73 (nomination 81000387; HMdb) | Exact spot of the pylon, which side of the line it is reached from, and land owner |
| Plum Valley House site | Ridge Road, near Alleghany (HMdb 65932, 39.448417, -120.960683) | 1854 log toll house on the Henness Pass Road, California Historical Landmark 695; only a marker now | Whether anything remains beside the marker |
| Mountain House site | Mountain House Road and Henness Pass Road (HMdb 65960) | 1860 three-storey roadhouse, torn down in the 1920s | Gone; only worth adding if traces are found |

## Tips
- HMdb nearby lists (3-mile radius) at five points gave nearly every place in this county with a position; the grep in GUIDE section 16 for the cached list worked as written. For a marker's full text, cut `page.py --all` output between "Inscription." and "Erected".
- NPGallery `_text` worked for every Sierra County form tried except Sierra City School (100009718, placeholder).
- Tahoe National Forest recreation pages: guessed addresses under `fs.usda.gov/r05/tahoe/recreation/...` all answered 404, and web search did not turn up a Kyburz Flat or Sierra Buttes page.
- Most web search results in this run gave titles and links only, no quoted text, so hours could not be taken from search results.
- `publish.sh` stopped once because app files changed on main during the session; `resync.sh`, rebuild, and a new branch name worked.
