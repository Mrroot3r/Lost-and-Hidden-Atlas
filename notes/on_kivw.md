# on_kivw: Ontario: a first scatter beyond Kingston
state: Ontario
region: on
date: 2026-11-21
places: 17
file: data_on_kivw.py

## What this batch is
Seventeen places spread across Ontario away from the Kingston and Rideau batch (on_arlm): Peterborough Lift Lock, Fort St. Joseph ruins (St. Joseph Island), Fort Mississauga, the Don Valley Brick Works, the Deagle mill and Cataract Electric ruins at Forks of the Credit, the DeCew House ruins (Thorold), Morningstar Mill, Dundurn Castle, the Huron Historic Gaol, Fort Malden, the Josiah Henson Museum (Dawn settlement), the Sault Ste. Marie Canal, Fort Wellington, the Windmill Point tower (Battle of the Windmill), Point Clark Lighthouse, Sharon Temple and the Bytown Museum (Commissariat Building). Ontario went from 20 places to 37. Sources: Wikipedia read with wiki_raw.py; Parks Canada site and hours pages; Ontario Parks and the Forks of the Credit management plan; HistoricPlaces.ca; HMdb; the operators' own pages (City of St. Catharines, Hamilton Civic Museums, Huron County Museum, Sharon Museum and Gardens, Ontario Heritage Trust, Evergreen). Pins came from OpenStreetMap (nom.py) or Wikipedia and were looked at on the aerial; Fort Wellington and the windmill were moved onto the blockhouse and tower with pix.py. Not checked: anything on the ground; the exact spot of the Cataract ruins (pin is the falls, prec area); public access into the DeCew House ruin (marked view, lot from OpenStreetMap); hours for the Henson museum, Point Clark (Township of Huron-Kinloss runs it), Sharon Temple (closed for the season when read) and the Bytown Museum (its site reset the connection); the Commissariat Building's date; fees at the Parks Canada sites. Red brick: yes only for the Brick Works (Wikipedia: red-brick masonry kept); 'no' where a source says stone or concrete; '?' elsewhere, including Fort Mississauga, whose brick colour no source opened gave. check.py warns that the Sault Ste. Marie Canal pin is just outside Ontario's coarse outline; on the aerial it is on the Canadian lock chamber.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort George and its 1790s powder magazine | Niagara-on-the-Lake, ON (43.25083, -79.06111) | Wikipedia: 1930s reconstruction, the magazine is the only original building; Parks Canada hours page read (closed for 2026 season; April to November hours given) | Not written up for lack of time; the hours page is parks.canada.ca/lhn-nhs/on/fortgeorge/visit/heures-hours |
| Bois Blanc Island lighthouse and blockhouse | Amherstburg, ON | Parks Canada's Fort Malden page names it a national historic site, a limestone tower | Access (island) and a source on what survives |
| Hilton Falls mill ruins | Campbellville (Milton), ON (43.50694, -79.98194 park) | Conservation Halton area on the Bruce Trail; Wikipedia's article is a stub with nothing on the mill | Conservation Halton's own page on the mill ruins, pin |
| Cobalt silver-mining town | Cobalt, ON (47.4, -79.68333) | Wikipedia: fourth largest silver producer in the world by 1910, declined by the 1930s | Which mine ruins are on public ground and a source for each |

## Tips
- Parks Canada hours pages (parks.canada.ca/lhn-nhs/on/<site>/visit/heures-hours) are flagged DRAWN BY SCRIPT by page.py but `page.py --all` prints the full hours table; several sites (Fort Mississauga, Point Clark, the Windmill) have no hours page: Fort Mississauga lives under fortgeorge/culture/fort-mississauga and Point Clark under lhn-nhs/on/clark.
- In Canada pincheck's land line is always "not on mapped public land" (PAD-US is US only), so every public place gets CHECK ACCESS; name the owner in the access note.
- pincheck --lidar and photo_find.py look each take longer than two minutes here; run them in the background and wait.
- hamilton.ca answers 403 to page.py; hamiltoncivicmuseums.ca carries the same Dundurn hours. bytownmuseum.com reset the connection.
