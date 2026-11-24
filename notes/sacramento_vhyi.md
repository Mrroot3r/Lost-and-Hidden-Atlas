# sacramento_vhyi: Sacramento: Sutter's Fort, Old Sacramento, the Cathedral, Crocker, City Hall and downtown landmarks
state: California
region: ca
date: 2026-11-24
places: 13
file: data_sacramento_vhyi.py

## What this batch is
A "videos" session (PROMPTS.md job 9). The names came from one video, "Old World Sacramento California" by Old World Exploration (https://www.youtube.com/watch?v=MiaBTHqM8v4); the record of all 40 names is source/videos/20241129_MiaBTHqM8v4.md. The video was a tip only: no fact here rests on it. Added 13 standing places, the first in Sacramento beside the State Capitol: Sutter's Fort, Old Sacramento and its raised streets (with the underground tours), the Cathedral of the Blessed Sacrament, St. Francis of Assisi Church, City Hall (1909), the Crocker Art Museum, the Elks Tower, the Governor's Mansion, the Travelers' Hotel, the Sutter Club, the 1933 Federal Building, the Carnegie city library and the Southern Pacific depot (Sacramento Valley Station). Facts come from Wikipedia (read with wiki_raw.py), the National Register form for the Travelers' Hotel, and the Diocese of Sacramento's archive leaflet on the Franciscans for St. Francis. Hours and fees come from California State Parks pages (page_id 485 Sutter's Fort, 497 Old Sacramento, 498 Governor's Mansion, which says the house is closed to the public), crockerart.org, cathedralsacramento.org and the Sacramento History Museum's tour page. Pins are street-address lookups (all PointAddress) and Wikipedia points, each looked at on the aerial. Not checked: St. Francis Mass times (the parish site answers 403), the Central Library's hours (its page moved: 404), the station's hours, interiors of the City Hall, Elks Tower, Sutter Club, Federal Building and Travelers' Hotel, and red brick for every place but Sutter's Fort (adobe). Nothing was checked on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Sacramento names from the video left "not checked" | Sacramento, CA | 22 rows in source/videos/20241129_MiaBTHqM8v4.md: the State Fair buildings, the old courthouse and Hall of Records, the Windsor Hotel, People's Savings Bank, the Buffalo brewery, the Bee building and several schools and churches | Whether each still stands, and a source |
| Stanford Mansion and other Register listings | Sacramento, CA | The Register list for Sacramento County has about 80 rows in the city (Leland Stanford Mansion, Westminster Presbyterian, Tower Bridge, I Street Bridge, Masonic Temple, Memorial Auditorium, Hotel Senator, Libby cannery) | Not reached in this batch; none is on the Atlas yet |

## Tips
- parks.ca.gov pages read in full with `page.py --all https://www.parks.ca.gov/?page_id=<n>`: 485 Sutter's Fort, 497 Old Sacramento, 498 Governor's Mansion.
- stfrancisparish.com and amtrak.com answer 403 to `page.py` and the web fetch tool; saclibrary.org/locations/central is 404. The Diocese of Sacramento's archive PDFs on scd.org read well.
- The ArcGIS lookup gave a PointAddress on the building for all 13 downtown addresses; only the Carnegie library's fell on the newer tower behind it.
