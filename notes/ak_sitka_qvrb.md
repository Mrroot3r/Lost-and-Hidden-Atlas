# ak_sitka_qvrb: Alaska: Sitka
state: Alaska
region: ak
date: 2026-11-24
places: 14
file: data_ak_sitka_qvrb.py

## What this batch is
Fourteen places in Sitka, Alaska, which had two (St. Michael's Cathedral and the Russian Bishop's House): Castle Hill, the Old Sitka redoubt site, the Second World War batteries of Fort Rousseau on Makhnati Island (the Sitka Naval Operating Base lead from ak_nwfc, now done), Sitka National Historical Park's Totem Trail and 1804 fort site, Russian-American Building No. 29, St. Peter's by-the-Sea, the Alaska Native Brotherhood Hall, the Sheldon Jackson Museum and the Sheldon Jackson School campus, the Pioneers' Home, the old Post Office and Court House (City Hall), Sitka National Cemetery, Princess Maksoutoff's grave in the Lutheran cemetery, and the Sitka Woman's Club cottage (Register 2024). Chosen from the Wikipedia Register list for Sitka (22 rows).

How the sources were read: this session's machine could not reach Wikipedia, Wikimedia Commons, the ArcGIS geocoder or image services, OpenStreetMap or any managing body's page from the shell (every host refused by the network proxy), so `wiki_raw.py`, `page.py`, `nom.py`, `geo.py`, `parking.py`, `pincheck.py` and `photo_find.py` could not run. Every page was read instead with the web fetch tool (Wikipedia articles, Alaska State Parks, the National Park Service, Alaska State Museums, the St. Peter's parish site, the VA, HMdb, Visit Sitka, SAH Archipedia, the Living New Deal, the Sitka Sentinel). Pins were looked at on the same Esri World Imagery the pin check uses, one 300 m square per pin (900 m for Makhnati Island, 600 m for the national park), opened in a cloud browser at the export address in `tools/ortho.py`, with the pin at the centre pixel; five were moved with `pix.py move` (Castle Hill, ANB Hall, Pioneers' Home, the national cemetery) or given a parking point (the national park). No LiDAR sheet, no `land:` line and no parking lots from OpenStreetMap.

Not checked: anything on the ground; every interior; the Sheldon Jackson Museum's current hours (the state page carries an undated closure notice and was last updated in 2020); City Hall's hours; whether the Sheldon Jackson campus grounds may be walked; who owns the Woman's Club cottage now; the exact spot of the batteries on Makhnati Island and of the 1804 battle field; which roof is Building No. 29 and which is St. Peter's church as against the See House. Red brick: 'no' from what the sources say each is built of (log, wood, stone, concrete, stucco); '?' for the two burial grounds. No pictures were chosen: Commons could not be reached, so there is no pics file; twelve places link a Wikipedia article whose picture the app may show by itself.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Sitka Lutheran Church and the Russian Orthodox cemetery | Sitka, AK | Visit Sitka and Lonely Planet name a Russian cemetery; Sitka Lutheran Church has a Wikipedia article | Not read: what stands, owner, hours |
| US Coast and Geodetic Survey Seismological and Geomagnetic House | 210 Seward Street, Sitka, AK (57.05063, -135.33582, Register list) | On the Register since 1986 | Article not read; present use |
| Cable House and Station | 2 Lincoln Street, Sitka, AK (57.04866, -135.33911, Register list) | On the Register since 1979 | Article not read |
| Fort Babcock | Near Sitka, AK (57.0142, -135.6366, federal names file) | Named in the federal names file as an old military site | Any source on what is left and how to reach it |

## Tips
- The network proxy of a cloud session can refuse every host the tools need (Wikipedia, Commons, ArcGIS, OpenStreetMap, nps.gov, dnr.alaska.gov): check with `curl -s -o /dev/null -w '%{http_code}' https://en.wikipedia.org/` before starting. The web fetch tool still read every page, and the Esri export address in `tools/ortho.py`, opened in a browser with a 300 m box round the pin in Web Mercator, stood in for the pin check's aerial tile.
- `tools/start.py "Sitka, Alaska"` answered "Could not find"; a latitude and longitude worked.
- Alaska State Parks pages (`dnr.alaska.gov/parks/aspunits/southeast/...`) give access and fees but no hours for the Sitka units.
- The Sitka National Historical Park brochure page (`nps.gov/sitk/planyourvisit/park-brochure.htm`) and the 2025 compendium give the current hours; the park's news releases about winter hours are old and disagree with them.
- A pull request opened as a draft does not merge by itself when it is later marked ready: `check.yml` runs on `pull_request` with GitHub's default event types (opened, synchronize, reopened), so marking it ready starts no new run, and the run made while it was a draft skipped the merge job. The merge job runs again on the next push to the branch.
