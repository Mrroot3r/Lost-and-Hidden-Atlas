# mt_ucxc: Helena, Montana: courthouse, jail, temples, hotel, kilns and Reeder's Alley
state: Montana
region: mt
date: 2026-11-22
places: 13
file: data_mt_ucxc.py

## What this batch is
Thirteen standing places in Helena, worked from the names in one Old World Exploration video (the record is `source/videos/20230619_hiKWVW73DRU.md`; 58 names, 13 added, 2 already on the Atlas, 16 gone, 14 not checked, 13 elsewhere or not a building). Added: the Lewis and Clark County Courthouse, the old county jail (now the Myrna Loy), the Algeria Shrine Temple, Temple Emanu-El, the Placer Hotel, Reeder's Alley, the Federal Building, the Masonic Temple, the YWCA, the Power Block, the Grizzly Gulch lime kilns, the Northern Pacific depot district and St. Charles Hall at Carroll College. Facts come mostly from the Montana Historical Society's National Register sign texts on Historic Montana (historicmt.org), with Wikipedia (wiki_raw.py), helenahistory.org, the Montana Heritage Commission's Reeder's Alley page, the Myrna Loy's and the Montana Jewish Project's own pages and the county's Clerk of District Court page. Pins are Historic Montana's points, looked at on the aerial; the depot pin was moved onto the depot, and St. Charles Hall stays at area precision on the college's Wikipedia point. Not checked: who owns the lime kilns (they are given as seen from Grizzly Gulch Drive), what is inside the courthouse today and its hours, the Civic Center's event schedule, Carroll College's visitor rules, and red brick for most places (only the Placer Hotel, from a photograph, and the stone buildings, from sources, are set).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Hawthorne School | Helena, MT, 430 Madison Avenue | helenahistory.org: a school on the site since 1879, stuccoed and cut down a storey after the 1935 earthquakes, closed by the school board in 2025 | Which parts are of the 1890s building, and what happens to it now |
| Helena High School of 1935 (Helena Middle School) | Helena, MT, 1025 North Rodney Street | helenahistory.org: a PWA school dedicated September 1935 and about three-quarters wrecked by the October 1935 earthquakes, repaired, now Helena Middle School | A second source and a pin |
| First Presbyterian Church | Helena, MT | Named in the video; no register text or church history page was found | A source for its date and builder |
| St. Joseph's Orphanage and the orphans' homes | Helena, MT | Named in the video only | Whether any building stands |

## Tips
- Historic Montana (historicmt.org) answers `?output=mobile-json` on any item (`/items/show/<n>?output=mobile-json`) and on a search (`/items/browse?search=<words>&output=mobile-json`): the sign text, address and a latitude and longitude for every National Register sign, which is quicker than the HTML pages (one HTML page, item 9, answered HTTP 500 while its JSON worked).
- helenahistory.org has a page for almost every lost Helena building, with demolition years; its school, hospital and hotel index pages list them.
- `photo_find.py look` with several ids ran past ten minutes; run it in the background one id at a time and read its output file.
- check.py refuses an e-mail address in a place list, even an organisation's: point to its contact page instead.
