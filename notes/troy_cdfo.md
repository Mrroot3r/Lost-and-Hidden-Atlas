# troy_cdfo: The RPI hill, three old Troy churches and old Lansingburgh
state: New York
region: troy
date: 2026-11-21
places: 14
file: data_troy_cdfo.py

## What this batch is
Fourteen places in region `troy` (drawn at random by `choose.py --state ny`), on ground three earlier batches (`troy_qbqw`, `troy_odvt`, `troy_vhio`) had already worked, so this batch took what they left. The RPI hill: the 1907 Approach stair, the 1933 St. Joseph's Seminary chapel that became the Voorhees Computing Center, and the Carnegie Building (1906), Russell Sage Laboratory (1909), '87 Gymnasium (1912) and Greene Building (1931), all from the RPI Institute Archives building histories. Three former churches: Woodside Presbyterian and its Proudfit Chapel in South Troy (Wikipedia, Atlas Obscura), the old First Presbyterian church that is Russell Sage College's Julia Howard Bush Memorial Center (two HMdb markers that disagree on 1832 and 1836, so `conf='mixed'`), and the 1846 First Baptist church now a fraternity house (HMdb, Baptist News Global, Atlas Obscura). Public School No. 1 (its Register form, which gives both 1976 and 1978 as the end of school use). Old Lansingburgh from the 2023 Central Lansingburgh Historic District Register form: the 1770s gambrel houses at 524-526 First Avenue (Van Vleeck) and 499 Second Avenue (the Old Daley Inn), the 1870 J. Fox steamer firehouse, and the corner at 117th Street and Third Avenue where the form says the base of the Powers Opera House (an 1845 Baptist meetinghouse, burned 1917) survives; the Lansingburgh Historical Society's page and a 1917 Troy Times story disagree on its year. Pages read with `page.py` and `wiki_raw.py`; pins from OpenStreetMap names and ArcGIS PointAddress results, all looked at on the leaf-off aerial and on the building. Not checked: anything on the ground; interiors (none of these is open at set hours that a source gives); whether The Post Contemporary still holds events at Woodside (thepost.org did not answer); who owns and maintains the Approach today; RPI's visitor-parking rules; which part of the building at 15 117th Street is the opera house base. Red brick from pictures for Public School No. 1, Greene and Russell Sage Laboratory; granite or stone (`no`) for Woodside, the Voorhees chapel and the Approach from their sources; the rest `?`. `check.py` warns that the Powers Opera House remains read as a church but are `civic`: the entry is about the opera house and theatre it became, so the warning stands.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Firemen's Hall | Lansingburgh, Troy, NY (3 115th Street; geocoder 42.77504, -73.67804) | Central Lansingburgh Register form: 1873 central fire station and village hall, courtroom added 1892, heavily altered into apartments after a fire in the 1950s | Little original left to see by the form's account; a picture |
| Russell Armington house | Lansingburgh, Troy, NY (1 113th Street) | Central Lansingburgh Register form: shipbuilder's house of about 1795, front altered about 1890, now vinyl-sided | Worth a pin only with more story or a picture |
| Pittsburgh Building and Walker Laboratory, RPI | Troy, NY (RPI campus) | RPI Institute Archives building histories: 1912 administration building (now the Lally School), 1907 chemical laboratory | Positions and a look at the aerial; left out to keep the batch from being all RPI |

## Tips
- The RPI Institute Archives building histories (`archives.rpi.edu/institute-history/building-histories/<slug>`, index at `archives.rpi.edu/node/3563`) read in full with `page.py --all` and give year, architect, cost and later use for every campus building; slugs are the building name in lower case with hyphens (`approach`, `87-gymnasium`).
- NPGallery `GetAsset/<uuid>` PDFs for 2018-2023 Troy forms have text layers (Public School No. 1, Central Lansingburgh Historic District, 312 pages); search results name the uuid. `page.py --all` stops at 12,000 characters unless given `-n 900000`; save it to a file and grep the inventory by street address ("478 Second Avenue 1870 ...").
- The SHPO's own form PDFs at `parks.ny.gov/documents/shpo/national-register/...`, which web search still lists, answered 404 (Neemes Foundry).
- `troyirish.org` answers 403 to `page.py`; `thepost.org` (Woodside's arts centre) did not connect.
