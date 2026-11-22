# nyc_fiff: Long Island: Stony Brook, Setauket, Port Jefferson and Kings Park
state: New York
region: nyc
date: 2026-11-22
places: 17
file: data_nyc_fiff.py

## What this batch is
Seventeen places on the North Shore of central Suffolk County, drawn at random by `choose.py --state ny` (region `nyc`, which offered Port Jefferson); `start.py` showed only three Atlas places within 15 km, none in these villages. Nearly all standing. Three Villages: the Stony Brook Grist Mill (c. 1751), the Hawkins-Mount House, Thompson House (1709), Sherwood-Jayne Farm, Brewster House (1665), Caroline Church (1729) and Setauket Presbyterian Church with their burying grounds, Frank Melville Memorial Park, and Old Field Point Light (now the village hall). Port Jefferson: the Bayles Shipyard buildings, the Mather House Museum, the First National Bank. Miller Place: the William Miller House (1720). Town of Smithtown: the empty Kings Park Psychiatric Center with York Hall (Nissequogue River State Park), the St. James General Store, the Blydenburgh farm and New Mill (dam failed August 2024), and the Wyandanch Club in Caleb Smith State Park Preserve. Sources: the Brookhaven and Smithtown Register lists and Wikipedia (`wiki_raw.py`), and the managing bodies' pages read with `page.py` (NYS Parks, Suffolk County Parks, NYS DEC, the Ward Melville Heritage Organization, Preservation Long Island, the Long Island Museum, the Village of Old Field, the Port Jefferson historical society, Frank Melville Park, the two churches), with TBR News Media and Clio for a few details. Not checked: nothing on the ground; no interior; hours for Thompson House, the Mount House, the William Miller House and the St. James General Store (`hours='?'`); whether the Blydenburgh New Mill survived the 2024 dam failure and whether the park's New Mill Road entrance has reopened; the Blydenburgh resident-only rule (from Clio, not the county page). Pins: the William Miller House and the First National Bank are area pins (address lookup on the road; turreted bank not picked out on the aerial); Kings Park marks York Hall only. Brick is `?` for most places (no source gave the colour); the two churches are `no` (wood shingles).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Chandler Estate ruins | Mount Sinai, NY (OpenStreetMap ruin lead 40.95553, -73.02072) | TBR News Media (tbrnewsmedia.com/?p=161827): an upscale resort above Mount Sinai Harbor that burned, leaving foundations in brush on a trail; Port Jefferson Rotary clears the 44-acre Chandler Estate Preserve (tbrnewsmedia.com/?p=127829) | Who owns the preserve (town or county), where to park, dates of the resort and the fire from a source better than a resident's memory |
| Old Bethel Cemetery and Bethel AME Church | Setauket, NY (40.93157, -73.13307) | Register listing (2017) with the Bethel–Christian Avenue–Laurel Hill district, a 19th-century African-American neighbourhood | The Wikipedia article had no usable text; needs the Register form or the church's own page, and access to the cemetery |
| Hulse House, Old Field Club | East Setauket, NY | Register rows in the Brookhaven list | Owner and whether anything can be seen from the road |

## Tips
- `wmho.org` (Ward Melville Heritage Organization) lists the Grist Mill's hours on `/properties/`; its event pages and `/brewster-house/` answered 404 or a 400 KB page with no hours. Thompson House is now shown by the WMHO, not Preservation Long Island.
- The old Miller Place-Mount Sinai Historical Society address `mpmshistoricalsociety.org/?p=2016` answered 404 with no archived copy.
- `photo_find.py look` on two places hung for over five minutes after writing both sheets' JSON; the candidates could be read from `research/photofind_<id>.json` and `set` worked while it hung.
- `publish.sh` stopped because `app.js`, `boot.js`, `sw.js`, `make.py` and `places_test.js` changed on main during the hour; `resync.sh` caught up cleanly.
