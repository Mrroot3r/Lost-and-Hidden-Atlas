# acnj_irqa: Atlantic City, New Jersey
state: New Jersey
region: njs
date: 2026-11-26
places: 13
file: data_acnj_irqa.py

## What this batch is
Thirteen standing places in Atlantic City, worked from the names in one Old World Exploration video (record: `source/videos/20240802_ih_0JqfbXbw.md`; the video is a tip, never a source). Eight are buildings the video names: Boardwalk Hall, the Dennis Hotel (now the Dennis Tower of Bally's), The Claridge, Steel Pier, the Warner Theatre's 1929 ocean front, St. Nicholas of Tolentine Church, the World War I Memorial, and the Bartlett (Guarantee Trust) Building, which is probably the "trust company" in the video. Five more stood close by and had good sources: Absecon Lighthouse, the Morris Guards Armory, the Knights of Columbus Club-Hotel (empty), the Madison Hotel (empty) and the Central Methodist Episcopal Church (Asbury UMC). Sources: Wikipedia read as raw text, the City of Atlantic City's "Historic District Draft Inventory" PDF (acnj.gov, 63 pages with a text layer: dates, architects and a description of every building in a proposed downtown district), the Claridge's history page, Absecon Lighthouse's front page and Steel Pier's contact page for hours, Jersey Digs on the Armory, WPG Talk Radio on the First Presbyterian Church. Not checked: parking for most places (public garages and street parking only), hours for Boardwalk Hall, the hotels and the Warner (`hours='?'`), St. Nicholas's Mass times (the parish site accatholic.org refused both page readers; directories disagree and were not used), red brick for most places (`'?'`), and the inside of every building. Pins are OpenStreetMap, Wikipedia or ArcGIS address points, all on their buildings on the 2020 leaf-off aerial except the Knights of Columbus point (street edge) and the Dennis point (a low roof among the Bally's buildings; the pin is marked site).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| St. Michael's Church, Ducktown | Atlantic City, NJ (10 N. Mississippi Avenue) | Italian parish founded 1904; cornerstone of church and school 1912 (Waymarking); public Sunday Masses ended September 2015 (a parishioners' petition) | A source on the building today and whether it opens |
| Atlantic City Fire Station No. 4 | Atlantic City, NJ (39.3553, -74.4444 from the Register list) | Listed on the National Register (100012757) | Any description; `tools/form.py 100012757` |
| Liberty Hotel and Segal Building | Atlantic City, NJ | Both on the National Register list, with a Wikipedia article for the Liberty | Read and add; neither is named in the video |
| Atlantic City High School of 1923 | Albany and Atlantic Avenues, Atlantic City, NJ | Opened September 17, 1923, with a 1,000-seat auditorium and organ (Wikipedia, the school's article) | Whether it still stands |
| German Presbyterian Church, Turn Verein Hall, Chelsea National Bank | Atlantic City, NJ (1316 Pacific Ave, 24 S. New York Ave, 1301 Atlantic Ave) | Described with dates in the city's Historic District Draft Inventory | Pins and a look; good for a second Atlantic City batch |

## Tips
- The City of Atlantic City's "Historic District Draft Inventory" (acnj.gov/_Content/pdf/Atlantic-City-Historic-District-Draft-Inventory.pdf) reads in full with `page.py` and gives date, architect and present state for each downtown building; search the cached copy in `research/pages/` by street address.
- accatholic.org (Parish of Saint Monica, Atlantic City) answers 403 to `page.py` and comes back empty in the web fetch tool.
- Wikipedia has no article under "Dennis Hotel" for Atlantic City (that title is St. Petersburg, Florida); the Dennis is in "Bally's Atlantic City".
- The First Presbyterian Church at Pacific and Pennsylvania Avenues was being taken down in 2025 (its sandstone went to the Smithsonian Castle), though the city's draft inventory still lists it.
