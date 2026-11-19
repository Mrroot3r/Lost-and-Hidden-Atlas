# pe_bhrt: Charlottetown and Queens County, Prince Edward Island
state: Prince Edward Island
region: pe
date: 2026-11-19
places: 24
file: data_pe_bhrt.py

## What this batch is
The first places in Prince Edward Island: 8 in Charlottetown (Province House, St. Dunstan's Basilica, All Souls' Chapel at St. Peter's Cathedral, Beaconsfield, Government House, Ardgowan, the Prince Edward Battery, the sandstone CNR station) and 16 in rural Queens County and Victoria (Skmaqn–Port-la-Joye–Fort Amherst earthworks, Blockhouse Point, Point Prim, Wood Islands and Leards Range lighthouses, Orwell Corner village, the Macphail Homestead, Belfast's 1824 church and the Acadian-Scottish burial ground, Dalvay-by-the-Sea, Shaw's Hotel, the Farmers' Bank and Doucet House at Rustico, Green Gables, the ruins of Montgomery's Cavendish home and her New London birthplace). Every place has its Canadian Register of Historic Places statement, read in full with `page.py --all -n 60000`; candidates came from the Wikipedia "List of National Historic Sites of Canada in Prince Edward Island" and "List of historic places in Queens County / Charlottetown" (`{{HPC row}}` templates, read from `research/wikiraw/`). Hours came from Parks Canada's pages, the operators' own pages where they opened, and otherwise Tourism PEI's "Dates of operation" (seasons only, no times: marked "Tourism PEI; times not checked"). Not checked: anything on the ground; Province House's status (Parks Canada's two pages disagree, so `conf='mixed'`); Government House tour times (lgpei.ca 403); Beaconsfield and Orwell Corner times (peimuseum.ca 403); the Cavendish Home site's hours; owners of Blockhouse Point lighthouse and the Acadian-Scottish burial ground (both view-only); whether the Belfast church pin (address point at a road junction) and the Green Gables pin (on the visitor centre) sit on the building itself; the Macphail pin was moved onto a house by the drive that is probably, not certainly, the 1856 house. The US public-land map behind `land:` has nothing in Canada, so every CHECK ACCESS line here is expected; owners are named from the Register and operators. There is no 1 m LiDAR in PEI.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Tryon United Church (National Historic Site, W. C. Harris, 1881) | Tryon or Crapaud, PE (46.24129, -63.50203 NHS list; 46.2397, -63.4994 Register list) | Register statement 12010 read: wooden High Victorian Gothic, almost freestanding tower | Both list points fall in Crapaud, about 3.5 km east of Tryon village, and the aerial shows no church at either; find the real spot and a service-times page |
| Hunter River grist mill and wood drying kiln | 4373 Route 13, Hunter River, PE (46.3585, -63.3474) | Register 13944 and 10363: Patterson mill of about 1880, rebuilt with a new water wheel after 2003 | Owner is private (rehabilitated by the current owners); no public page or visiting arrangement found |
| Emerald Junction railway station | 1929 Nodd Road, Emerald, PE (46.3613, -63.5485) | Register 20442: CNR standard station of 1923–24 on the Confederation Trail, community-owned since 1980 | Its present use and whether it opens; not read past the 1990s in the statement |
| Strathgartney Homestead (National Historic Site) | Bonshaw, PE (46.2009, -63.3547 NHS list) | On the NHS list | historicplaces.ca 7764 reset the connection three times |
| Old Princetown Road | New London area, PE (46.409, -63.4871) | A Register-listed old road (10672) | The Register page never opened |
| Glenaladale House, Victoria (Main Street) streetscape, Uigg school and church, St. Augustine's church Rustico, Covehead and North Rustico lights | Queens County list rows | On the Queens County list with Register ids | Not read this session; Victoria's Main Street has a dozen Register buildings that could make a `town` entry |

## Tips
- historicplaces.ca resets the connection (`ConnectionResetError 104`) when asked quickly; `page.py` then gives up. A loop with an 8-second sleep between pages and up to three tries read all but two of 31 statements.
- parks.canada.ca resets too on the first request of a run; `www.parks.canada.ca` with a retry worked. Parks Canada's Province House pages contradict each other (main page "closed", visit page "conservation concluded, Assembly back fall 2026"); read both.
- peimuseum.ca (the PEI Museum and Heritage Foundation's seven sites) and lgpei.ca answer 403 to `page.py`. Tourism PEI attraction pages (`tourismpei.com/attractions/<slug>`) read and give "Dates of operation" but never times; museumspei.ca (Community Museums Association) gives "Seasonal" or "Open year round".
- `choose.py --claim ... --state qc,nb,ns,pe,nl` refuses a comma list; give one key. Newfoundland and Labrador (nl) did not appear in `choose.py`'s list of thin regions.
- In PEI the HPC list's Register points are usually near the right building but land on road junctions for rural churches (the ArcGIS PointAddress gives the same point). OpenStreetMap (`nom.py`) had good points for most museums and lighthouses; the Point Prim Register point is 1 km off.
