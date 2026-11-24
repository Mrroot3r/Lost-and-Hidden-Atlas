# fl_qwmd: Florida: seven more, Palm Beach to Pensacola
state: Florida
region: fl
date: 2026-11-24
places: 7
file: data_fl_qwmd.py

## What this batch is
Seven places in Florida that earlier batches lacked, from Palm Beach to Pensacola: Whitehall (Flagler Museum), Vizcaya, the Stranahan House, Bonnet House, Mission San Luis, Chinsegut Hill Manor and Fort Barrancas. Facts come from Wikipedia (wiki_raw.py) and, where they opened, the operators' own pages read with page.py (Stranahan House, Bonnet House, Mission San Luis, the Tampa Bay History Center's Chinsegut page, the National Park Service's Fort Barrancas page). Whitehall's and Vizcaya's own sites would not open, so their hours and Whitehall's price come from web search results that quoted them; the access notes say so. Not checked: anything on the ground, interiors, parking for all but Fort Barrancas, red brick for all but Fort Barrancas (Wikipedia says its brick). Pins: Whitehall, Vizcaya, the Stranahan House and Chinsegut Hill were moved off the Wikipedia or geocoder point onto the building seen on the aerial. Mission San Luis is mostly reconstruction on the site of the 1656 mission, and is marked as such.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Prospect Bluff Historic Sites (Negro Fort and Fort Gadsden) | Sumatra, FL (29.93, -85.02 on Wikipedia; OpenStreetMap "Prospect Bluff" 29.825, -85.017) | National Historic Landmark in Apalachicola National Forest; ruins of two forts, 1814 and 1818; Forest Service page shows a closure order | Whether the site has reopened and its hours; which of the two coordinates is the fort |
| Egmont Key (Fort Dade ruins, lighthouse) | Tampa Bay, FL (27.586, -82.761) | State park and refuge reached only by boat; Wikipedia | Ferry operator and hours from a page |
| Deering Estate at Cutler | Miami, FL (25.616, -80.306) | Richmond Cottage and Stone House on 444 acres; Wikipedia | Hours and access from the estate's own page |
| Ybor City Museum State Park | Tampa, FL (27.962, -82.439) | Former Ferlita Bakery in Ybor City Historic District | Hours; park pages answer 403, try the system guide PDF |

## Tips
- Whitehall's Wikipedia and ArcGIS points both fell about 400 m east on a golf course; OpenStreetMap's museum outline (osmnear.py ... buildings -g 'Flagler') was right.
- Vizcaya's Wikipedia point is in the bay.
- tools/app_smoke.js tests android-app/www, not dist/web; run against dist/web it times out on "Start a field log".
- vizcaya.org, flaglermuseum.us/visit and deeringestate.org/visit would not open with page.py; a web search quoted the hours.
