# albco_lydm: Albany County: Menands cemeteries, Bethlehem, New Scotland, Guilderland Center, Berne
state: New York
region: albco
date: 2026-11-19
places: 13
file: data_albco_lydm.py

## What this batch is
Thirteen standing places in Albany County outside the city, a third pass after `albco_kaom` and `albco_ktfd` (region `albco` drawn by `choose.py --state ny`). Menands: a full entry for the Albany Rural Cemetery (replaces `lm-albany-rural-cemetery`), St. Agnes Cemetery, and the red-brick Albany Felt Company mill (Lofts at One Broadway). Bethlehem: Bethlehem House (about 1735) with the Nicoll-Sill burying ground, the First Reformed Church of Bethlehem (about 1890, congregation 1763) and the Van Der Zee manor house marker (1754). New Scotland: the Onesquethaw Reformed Church (1825, said by its marker to be built of stone rejected for the Erie Canal) and the Wemp Barn marker. Guilderland: the Freeman House (about 1734), St. Mark's Lutheran Church in Guilderland Center (1872, now Centerpointe Community Church), the 1863 cobblestone vault in Prospect Hill Cemetery and the Lainhart farm with its Dutch barn. Berne: the First Reformed Church (1832, congregation 1763). Sources: Wikipedia raw text (`wiki_raw.py`), HMdb marker pages and nearby lists (`page.py`), the Albany Rural Cemetery's hours and rules pages, the Hudson River Valley heritage area and Discover Albany listings, and albanyhilltowns.com's Berne church pages (web fetch tool). Not checked: anything on the ground; St. Agnes's hours (operator's page 404); owners of the Freeman House, Prospect Hill Cemetery, the Onesquethaw church and Bethlehem House's burial ground; parking everywhere except the cemeteries. Five pins are markers or Register points, not the building: Wemp Barn, Van Der Zee (both `conf='mixed'`, survival not confirmed), Freeman House (falls on Route 146), Prospect Hill vault (falls on Western Avenue; vault not seen), Berne church (marker on NY 443; church building not picked out). The Lainhart pin was moved 87 m from a field to the nearest farm buildings on the road, not confirmed as Lainhart's.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Becker Homestead | Selkirk, NY (42.54678, -73.81290), NY 396 at Beckers Corners | HMdb 305289, 1932 state marker | Whether a homestead building survives |
| Bennett Hill House and Preserve | Feura Bush, NY (42.57089, -73.96047) | HMdb 276308: house built 1821, Bennett sheep and apple farm, boarding house 1890s–1920s; preserve is MHLC land (mohawkhudson.org) | Whether the house is on the preserve or private; any farm traces on the trails |
| Coeymans Creek gunboat encampment | Selkirk, NY (42.50251, -73.79223), NY 144 | HMdb 308875 (Pomeroy 2025): Continental troops built gunboats nearby 1777–78 | Anything to see; access to the creek mouth |
| Five Rivers CCC camp and game farm | Delmar, NY (42.60864, -73.89029) | HMdb 263982: CCC camp S-72 1933–36, Delmar Experimental Game Farm 1933–70; DEC centre, trails sunrise to sunset (dec.ny.gov) | Whether any camp or game-farm building survives |

## Tips
- The Albany County Historical Association's New Scotland tour PDFs (albanycountyhistory.org, "Tour40thAnni-NewScotland-...") are scans with no text layer.
- albanyhilltowns.com refused `page.py` again; the web fetch tool read three pages in about 15 seconds.
- Albany Rural Cemetery's hours are at `albanyruralcemetery.org/about/for-visitors/hours-of-operation/` and read with `page.py -g`.
- `capitaldistrictcemeteries.org/locations/st-agnes-cemetery` is 404 with no archived copy.
