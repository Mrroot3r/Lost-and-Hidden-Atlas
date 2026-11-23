# hud_futy: Central Dutchess: Millbrook, Clinton Corners, Pleasant Valley and Dover Plains
state: New York
region: hud
date: 2026-11-23
places: 11
file: data_hud_futy.py

## What this batch is
Eleven places in central and eastern Dutchess County, drawn at random by `choose.py --state ny` (region `hud`); the Atlas had only the Nine Partners meeting house and the Bennett College site round Millbrook. Millbrook: the Thorne Memorial School (a lead from `hud_gfhh`, now added), Grace Episcopal Church (services from the parish site), the 1908 Hayes Memorial Library (hours from the library's own page), and one `town` entry for the 1869 railroad village centre and its Museum in the Streets panels (the 1870 railroad office now the Bank of Millbrook, the 1910 firehouse, the 1913 red-brick school now the town hall, the Ciferri stone building, St. Joseph's, the 1952 Millbrook Diner). Salt Point: the Bloomvale mill ruins, dam and Bloom house (private, view only). Clinton Corners: the 1777–82 Creek Meeting House with the 1890/1916 Friends Church across the road in the same entry. Stanfordville: the Campbell House. Pleasant Valley: the Mill Site Memorial Park and restored mill office. Dover Plains: the Second Baptist Church and the Tabor-Wing House. Wassaic: the Harlem Valley Rail Trail's south end on the old Harlem main line (hours from Dutchess County Parks). Sources: Wikipedia through `wiki_raw.py`, HMdb marker pages and the Pomeroy Foundation, Town of Clinton, Dutchess County, gracemillbrook.org and millbrooklibrary.org through `page.py`/`hours.py`. Not checked: anything on the ground; the Clinton Historical Society's open days (its site answered 403); the Tabor-Wing House museum hours (hours='?'); Pleasant Valley park hours; which building is the Campbell House on the aerial (pin `area`); whether the Thorne building is now in use; interiors throughout. Pins were all looked at on the leaf-off aerial and LiDAR; the Tabor-Wing pin was moved 22 m onto the house.

## Leads
Places you read about and could not finish. One row each. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Beekman Meeting House and Friends' Cemetery | LaGrangeville, NY (Register 41.633333, -73.767222) | Register list: ruins of an 1809 Quaker meeting house, one of two in the county to go Orthodox after 1828 | A source on what stands, the owner and whether it can be seen from a road (outside region `hud`) |
| Site of Beekman Furnace | Beekman / Union Vale, NY (HMdb 168689 at 41.63489, -73.69202) | HMdb marker | Whether anything of the furnace is left, and the owner |
| Carman Mill site | Pine Plains, NY (HMdb 144591 at 41.94321, -73.60889) | Pomeroy marker: a mill by 1784, burned 1936 | Whether any dam or foundation shows from County Route 83 |
| Millbrook Diner hours | Franklin Avenue, Millbrook, NY | In the village-centre entry; Dinerville lists it open | A page of its own with days and hours, if a separate entry is wanted |
| Creek Meeting House open days | Clinton Corners, NY | clintonhistoricalsociety.org answered 403 (archived copy of 2026-11-16 not fetched) | The society's exhibit days, to make the entry acc='open' |

## Tips
- Web search returned titles and links only, no quoted text, all session: read every page with `page.py` or `hours.py page`.
- HMdb's nearby list round Millbrook found the 2014 Museum in the Streets panels (English and Italian); their text runs from "Inscription." to "This historical marker", and the position is under "Location." on panels that have one.
- `nyym.org/node/168` (offered for Clinton Corners) is the Bulls Head-Oswego meeting, not the Clinton Corners Friends Church, which closed in 1986.
- The Tabor-Wing House's Town of Dover page in Wikipedia's links is struck out; no town page for the museum was found.
