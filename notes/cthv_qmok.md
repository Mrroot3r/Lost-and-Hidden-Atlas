# cthv_qmok: Hartford County, Connecticut: Wethersfield to New-Gate
state: Connecticut
region: cthv
date: 2026-11-18
places: 16
file: data_cthv_qmok.py

## What this batch is
First pass over region `cthv` (Hartford & the Connecticut Valley), drawn at random by `choose.py`; sixteen places across Hartford County. Old Wethersfield: the Webb and Deane houses (Webb-Deane-Stevens Museum), the 1711 Buttolph-Williams House, the 1761 brick First Church meetinghouse and the c.1690 Cove Warehouse. Rocky Hill and South Glastonbury: the Dividend Pond mill ruins (state archaeological preserve with HMdb-filed markers), the 1655 Rocky Hill–Glastonbury Ferry and the Cotton Hollow mill walls. Hartford: the Old State House and the Ancient Burying Ground. Manchester: the Pitkin Glassworks ruin and the Cheney Brothers silk mills. Simsbury: Heublein Tower, the Drake Hill Flower Bridge and the CCC Massacoe Forest Pavilion. East Granby: Old New-Gate Prison and Copper Mine. Windsor Locks: the Enfield Falls Canal and its towpath trail. Sources: Wikipedia with `wiki_raw.py` (the Hartford County Register rows), CT DEEP park pages (Talcott Mountain, Stratton Brook, Windsor Locks Canal Trail), CT DECD for New-Gate, CTDOT for the ferry, the Old State House, Webb-Deane-Stevens and Connecticut Landmarks pages, Simsbury Parks, the Pitkin Glass Works and Manchester Historical Society sites, HMdb marker pages for Dividend Pond, the Save Cotton Hollow Mill coalition and Patch, and Historic Buildings of Connecticut for the Cove Warehouse (the one source for its c.1700 flood story). Not checked: anything on the ground; the Cotton Hollow walls' spot (area pin on the preserve) and its parking and hours (glastonburyct.gov answers 403); Dividend Pond parking and hours; the Cove Warehouse museum's season; the Ancient Burying Ground's owner and gate hours (left `view`); who may walk onto the Pitkin ruin (left `view`, pin at the street corner, the building not picked out on the aerial); where the Enfield canal locks are (area pin on the canal); the Massacoe pavilion was not seen on the aerial; admission prices at Webb-Deane-Stevens and the Old State House; Heublein Tower's closing hour (DEEP's two pages give 4 and 5 p.m.). Shade Swamp Shelter (Farmington, CCC) was left out: Wikipedia says it collapsed in 2021–22. Red brick: yes for the Wethersfield meetinghouse, Old State House and Cheney mills; some for New-Gate; no where sources give stone, wood or iron; `?` for the rest.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Enfield Falls Canal locks | Windsor Locks, CT (south end of the canal) | The locks still exist, unused since the 1970s (Wikipedia, Enfield Falls Canal) | Where they are, and whether the towpath trail passes them |
| Windsor Locks Passenger Station (1875) | 225 Main Street, Windsor Locks, CT (41.93187, -72.62748) | Register 1975; the town got money from 2020 to restore it as a welcome centre and café; a new station beside it opened October 18, 2026 (Wikipedia) | What state the 1875 building is in now and whether it is open |
| Simeon North Factory Site | Berlin, CT | Register 1990; no coordinates in the list | A source on what is left and a public way in |
| Enfield Shakers Historic District | Enfield, CT | Register district in the Hartford County list | A source on which buildings stand and whether any can be seen (much of the land is a prison) |
| Slocomb Mill | South Glastonbury, CT (41.66367, -72.58025) | OpenStreetMap ruin point near Hopewell Pond open space | Any written source |

## Tips
- `glastonburyct.gov` answers HTTP 403 to `page.py` (the Cotton Hollow facility page and fundraiser page), and `ctmq.org` resets the connection; `savecottonhollowmill.org` and Patch carried the Cotton Hollow history.
- HMdb's marker pages for the Dividend Pond Archaeological District (Rocky Hill) give each mill's story and what is left, with a position; start at `https://www.hmdb.org/m.asp?m=301402`.
- Wikipedia "Hopewell Mills District" is in Taunton, Massachusetts, not Glastonbury's Hopewell.
- The ArcGIS geocoder put "Pine Street & Elm Street, Manchester, CT" in Manchester, England; give a house number and ZIP (230 Pine Street, Manchester, CT 06040) to keep it in Connecticut.
- Several Wikipedia infobox points in Old Wethersfield fell 60 m off the houses; the geocoder's PointAddress hits were on them.
