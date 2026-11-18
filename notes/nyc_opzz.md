# nyc_opzz: Staten Island, New York City
state: New York
region: nyc
date: 2026-11-18
places: 17
file: data_nyc_opzz.py

## What this batch is
The first 17 places in region `nyc` (drawn at random by `choose.py`), all on Staten Island. Standing: the Conference House (c. 1680), the Voorlezer's House and St. Andrew's Church at Historic Richmond Town, the Billiou–Stillwell–Perine House (c. 1662), Battery Weed and Fort Tompkins at Fort Wadsworth, Snug Harbor's Temple Row, the Alice Austen House, the Seguine Mansion, the Kreischer House, the Staten Island Range Light, the Prince's Bay Lighthouse at Mount Loretto (with the orphanage bulkhead on the beach), the Reformed Church at Port Richmond and Woodrow Methodist Church. Ruins: the New York City Farm Colony, the Witte Marine boat graveyard on the Arthur Kill and Swinburne Island's quarantine station. Sources: Wikipedia read with `wiki_raw.py`; hours from the managing bodies' own pages read with `page.py` (NPS Gateway Fort Wadsworth page and Staten Island FAQ, Historic House Trust pages for the Conference House, Alice Austen House and Seguine Mansion, Historic Richmond Town's visit page, Snug Harbor's visit page, NYS DEC's Mount Loretto page), HMdb 155238, and news/history pages for the Farm Colony (6sqft, JLC Online) and the boat graveyard (Forgotten New York, Freshkills Park). Every pin was looked at on the leaf-off aerial and LiDAR; seven were moved (see pin notes). Not checked: anything on the ground; how far the Farm Colony's "Landmark Colony" redevelopment (approved 2016) has gone; whether the boat graveyard can be seen from Arthur Kill Road; the Billiou house's opening schedule on the society's own pages; church interiors and opening times; admission fees at Richmond Town, Alice Austen and Snug Harbor's indoor sites; street parking. The Seguine Mansion was marked "temporarily closed" on the Historic House Trust page. Brick is `?` for most places: no picture was opened, and sources say "brick" without a colour for the Reformed Church and Snug Harbor.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Historic stone chimney, New Springville | Staten Island, NY (40.59683, -74.15429) | Mapped in OpenStreetMap as a ruin, "Historic Stone Chimney", on Ashworth Avenue by Willowbrook Park | Any written source; the NYC Parks Willowbrook Park history page does not mention it |
| Pellman Cottage ruin | Staten Island, NY (40.51028, -74.2225) | Mapped in OpenStreetMap as a ruin on Cunningham Road, just west of Mount Loretto | Any written source and the owner |
| Seaview Hospital historic district | Willowbrook, Staten Island (40.59167, -74.13278) | 1905–1938 tuberculosis hospital, 37 contributing buildings; part reopened as a city nursing home (Wikipedia) | Which buildings stand empty and what can be seen from public streets |
| Sandy Ground Historic Archeological District | Rossville/Woodrow, Staten Island | Register-listed, address restricted (Register list) | A source that says what can be visited (the Sandy Ground museum and the AME Zion church cemetery were not researched) |
| New Dorp Light | New Dorp, Staten Island (40.58083, -74.12) | 1856 range light, now a private residence, not open (Wikipedia) | Left out because the pin would be a private house; could go in as view-only if a public viewpoint is found |
| Fort Wadsworth's Endicott batteries (Battery Duane, Barbour, Turnbull, Bacon, Catlin, Hudson and others) | Fort Wadsworth (OSM fort-site points 40.598–40.607, -74.054 to -74.061) | Mapped in OpenStreetMap; on NPS land | A source for each battery's dates and what is left |

## Tips
- The NYC Parks pages under `php1-84.nycgovparks.org` that search results return answer 401 to `page.py`; the same path on `www.nycgovparks.org` reads.
- The Historic House Trust (`historichousetrust.org/houses/<name>/`) gives owner, operator and hours for every city-owned historic house in one short page; it was the best access source on Staten Island.
- `nps.gov/places/fort-wadsworth.htm` is a 404; Fort Wadsworth's hours are on `nps.gov/gate/learn/historyculture/fort-wadsworth.htm`.
- `osmnear.py <lat> <lon> 300 buildings` gives Snug Harbor's lettered buildings (`ref=A` to `E`, Building C tagged Main Hall), which put the pin on the right building.
