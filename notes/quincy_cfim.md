# quincy_cfim: Quincy, Illinois
state: Illinois
region: il
date: 2026-11-24
places: 10
file: data_quincy_cfim.py

## What this batch is
Ten standing buildings in Quincy, Illinois, the first places on the map there, from the names in one Old World Exploration video (record: `source/videos/20241115_6QjIVfd5HwM.md`; the video was a list of names only). Added: the Dick Brothers Brewery, the 1888 public library (now the History Museum on the Square), the 1887 U.S. Post Office and Courthouse, State Savings Loan and Trust, the Hotel Quincy, B'nai Sholom Temple, St. Francis Solanus Church, Francis Hall at Quincy University, Salem Evangelical Church and the 1899 stone arch bridge in South Park. Sources: Wikipedia read as raw text (`wiki_raw.py`, including the Downtown Quincy and South Side German district articles), the Historical Society of Quincy and Adams County's articles and museum pages, the churches' own pages (stfrancissolanus.com, salemquincy.org), the brewery district's museum page, St. Louis Public Radio, Saint Louis Patina, the visitors' bureau's architecture guide and the Quincy Park District. Pins are ArcGIS address lookups or OpenStreetMap features, each looked at on the aerial. Not checked: the History Museum's days and times (its page gives none that could be read; `hours='?'`), whether the post office lobby is open, what B'nai Sholom is used for since its sale, whether the South Park bridge on South Eighth Street is the 1899 arch (marked `conf='mixed'`), and every interior except the two churches, whose fittings come from their own pages. Red brick: yes for the brewery (Saint Louis Patina and a Commons picture) and Salem (Commons picture), no for the stone library, the limestone post office and the stone bridge, `?` for the rest.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Illinois Veterans Home (Soldiers' and Sailors' Home) and All Wars Museum | Quincy, IL, 1707 North 12th Street | Dedicated 1886, the state's first and largest veterans' home (state page; HSQAC article); has an All Wars Museum | Which 1880s buildings survive the 2025 rebuilding; the museum's own page (quincyivh.org) answered HTTP 509 |
| St. Mary's (Immaculate Conception) Church, now Blessed Sacrament | Quincy, IL, 1119 South 7th Street (gcatholic) | Parish of 1867 for south-side Germans; merged into Blessed Sacrament | The building's date and a parish page with Mass times |
| Chaddock (Chaddock College, Chaddock Boys' School) | Quincy, IL | Methodist academy of 1853, Chaddock College 1878, boys' school 1899 (search results only) | Which old building stands and a page read in full; chaddock.org/about/history is 404 |

## Tips
- `geo.py` searches New York only; outside it call the ArcGIS `findAddressCandidates` address directly with `SingleLine=` (PointAddress hits landed on every Quincy building).
- HMdb answered 403 to `page.py` again (November 24, 2026); the South Park and St. Boniface markers could not be read.
- A web search for "History Museum on the Square hours" returned Springfield, Missouri's museum of the same name: check the town before taking hours.
- dickbrothersbrewery.com: `/museum` reads; `/tunnels` and `/tunnel-tours` are 404.
