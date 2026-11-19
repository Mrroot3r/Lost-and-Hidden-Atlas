# wny_odvw: New York: Allegany County
state: New York
region: wny
date: 2026-11-19
places: 21
file: data_wny_odvw.py

## What this batch is
Twenty-one places in Allegany County, New York, the first pass there (region `wny`, drawn at random by `choose.py --state ny`, which offered Wellsville, Angelica and Fairport; the Atlas had nothing within 30 km of Angelica). Standing: the 1819 Old Allegany County Courthouse on Angelica's eight-sided green, Belvidere (John Barker Church's 1804 mansion, private), Christ Episcopal Church at Belvidere (1860 Carpenter Gothic), the Moses Van Campen House, the Caneadea camelback truss bridge (closed to vehicles since 2012), the Rail and Titsworth canal warehouse in Belfast, Muldoon's training barns (Belfast), the Allen Steinheim Museum, the Terra Cotta Building, Fireman's Hall and Alumni Hall in Alfred, the Wellsville Erie depot (for sale and fenced, April 2026), the Pink House (Wellsville, private), the Belmont Hotel (now the Fountain Arts Center), Centerville Town Hall and Cuba's Main Street. Oil and canal: the Seneca Oil Spring (Seneca Nation land, county historical society park), the Cuba Lake dam (Genesee Valley Canal summit feeder), the Pioneer Oil Museum in Bolivar, and two markers for first wells (Triangle No. 1 at Petrolia, the 1860 Bopp Farm well at Rushford). Sources: Wikipedia through `wiki_raw.py` (the county Register list with `--rows`), HMdb nearby lists round five towns and the marker pages, alleganyhistory.org, the Belfast bicentennial audio tour, pioneeroilmuseum.com (the only hours taken), parks.ny.gov for the Greenway, angelicany.org, wellsvillepinkhouse.com, WLEA and the Wellsville Sun. Not checked: anything on the ground; office hours for the Angelica and Alfred town buildings and the Fountain Arts Center (`hours='?'`); whether the Caneadea bridge may be walked; the Terra Cotta Building's open-house dates; owners of Belvidere, the canal warehouse and the training barns (treated as private); parking at most places (only the Angelica Park Circle lot is given). Pins that mark a marker and not the thing: Triangle No. 1 and the Rushford well. Four red-brick answers come from the Wikipedia photographs (Fireman's Hall, Van Campen House, Belmont Hotel yes; Terra Cotta Building some); the depot's from a 1911 newspaper account. The canal warehouse's date and the 1910 murder story differ between sources (`conf='mixed'`).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| McKinney Stables of Empire City Farms | Cuba, NY (Register 42.2097, -78.2711) | On the Register (99001000), county list | No article read; what stands and who owns it |
| Ceres School | Ceres, NY (HMdb 88289, 41.9995, -78.27272) | 1855 two-room school remodelled 1893, served pupils from both states, later community centre (Wikipedia) | Owner and whether it opens; not added for lack of time |
| West Almond Churches | West Almond, NY | On the Register (00000876) | No article; no coordinate in the list |
| Belmont Literary and Historical Society Free Library | Belmont, NY (OSM 42.22353, -78.03568) | Register 03000599; OpenStreetMap marks it heritage | Building date and hours from the library's own page |
| Genesee Valley Canal remains in Allegany County | Belfast to Cuba along the Greenway | The canal bed shows on LiDAR beside the Belfast warehouse | The American Canal Society sheet for this canal is a blank form (635 characters); the NYS Parks Greenway existing-conditions PDF is 404 |
| Hanging Bog CCC pond | New Hudson, NY (HMdb 86561, 42.30554, -78.24997) | CCC pond of the 1930s in a 4,571-acre wildlife management area | Whether any CCC work beyond the pond is left |

## Tips
- The American Canal Society's Genesee Valley Canal sheet (`americancanalsociety.org/wp-content/uploads/2019/08/Genesee-Valley-Canal.pdf`) is an empty form: no lock list.
- alleganyhistory.org (Allegany County Historical Society) reads well with `page.py -g` and has articles on single buildings (the Belfast warehouse, the Wellsville depot's 1911 opening, the oil museum).
- `parking.py`'s "East Pearl Street" lot in Wellsville (42.12480, -77.94785) is houses on the aerial.
- `check.py` warns that "Belvidere (John Barker Church mansion)" and "Alumni Hall (Chapel Hall)" read as places of worship; both are kept as they are (a house, an academy hall).
