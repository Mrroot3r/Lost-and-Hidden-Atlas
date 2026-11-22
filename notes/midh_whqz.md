# midh_whqz: Northern Westchester: Peekskill, Cortlandt, Croton, Yorktown and Ossining
state: New York
region: midh
date: 2026-11-22
places: 16
file: data_midh_whqz.py

## What this batch is
Sixteen places in northern Westchester County, the first pass there (region `midh`, drawn at random by `choose.py --claim --state ny`, which offered Peekskill, Tarrytown and Katonah; the Atlas had nothing east of the Hudson within 15 km of Peekskill), with the West Point Foundry Preserve just over the Putnam line at Cold Spring. Ruins: the West Point Foundry, the Mohegan granite quarries in Sylvan Glen Park Preserve (Yorktown) and the Underhill wine cellars at Croton Point. Water works: the New Croton Dam (Croton Gorge Park) and the Old Croton Aqueduct's Double Arch at Ossining. Standing: Old St. Peter's Church (1766 or 1767; sources disagree) and the Van Cortlandtville schoolhouse, the Van Cortlandt Upper Manor House, Van Cortlandt Manor at Croton, Croton North station, Yorktown Heights station, the Amawalk Friends Meeting House, the Peekskill freight depot (Lincoln Depot Museum), St. Peter's Episcopal and the Presbyterian church in Peekskill, and the Bear Mountain Bridge. Sources: Wikipedia through `wiki_raw.py` (and `--rows` for the northern Westchester and Peekskill Register lists), and through `page.py` Scenic Hudson's preserve brochure, Historic Hudson Valley, Westchester County Parks (Croton Gorge and Croton Point pages and history page), the Town of Yorktown, the NY-NJ Trail Conference, New York State Parks, the Friends of the Old Croton Aqueduct, crotonhistory.org, the Town of Cortlandt, St. Peter's Peekskill, the Van Cortlandtville Historical Society, Amawalk Friends Meeting and the Lincoln Depot Museum. Not checked: nothing on the ground. The Underhill wine cellar pin is an estimate (`prec='area'`, `conf='mixed'`) from the county's words "midway down the southern portion, on the east slope"; the vault did not show on the aerial or the LiDAR. The Old St. Peter's and schoolhouse pins could not be told apart on the aerial (both `site`). Van Cortlandt Manor is closed for tours during restoration (Historic Hudson Valley, read this day): `view`, `hours='?'`. The Lincoln Depot Museum's page gives a season but no days or times. The Upper Manor House's present owner and use, and service times at the Peekskill Presbyterian Church and the schoolhouse's open days, were not found. Red brick was left `?` wherever no picture or source settled the colour.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Underhill wine cellars, exact spot | Croton Point Park, Croton-on-Hudson, NY (estimate 41.17478, -73.89652) | Westchester County: vaults intact, built into the east slope midway down the southern part of the point; its 2026 historic-features map PDF lists wine cellar, wine cottage, fruit barn foundation and two brickyards | The map PDF itself (the county site returned an HTML page to a plain download); a coordinate for the vault entrance |
| Standard House | Peekskill, NY (Register list 41.285833, -73.930278) | Register list: 1855 Italianate commercial building, one of two hotels left from the industrial era, now the city's economic-development offices | A source beyond the list's one-line summary |
| Peekskill Downtown Historic District and US Post Office | Peekskill, NY (41.290556, -73.92; 41.289444, -73.923333) | Register list: core of 19th-century Peekskill with a Moorish Revival tower at Division and Park streets; a Colonial Revival post office with Palladian windows | Articles or the Register forms read; what stands |
| St. George's Church | Mohegan Lake, NY (41.3243, -73.8515) | On the Register (2012) | Its Wikipedia title (the guessed one does not exist) and a source |
| Asbury United Methodist Church and Bethel Chapel and Cemetery; St. Augustine's Episcopal Church Complex | Croton-on-Hudson, NY (41.207222, -73.880556; 41.2083, -73.8869) | On the Register | Any source read |
| Jug Tavern | Ossining, NY (41.144722, -73.864444) | Register list: 1760s stop on the old Albany Post Road, intact | Owner's page and opening times |
| Site of Old Croton Dam | Cortlandt, NY (41.227499, -73.852872) | Drowned by the New Croton Reservoir (Wikipedia, New Croton Dam) | Whether anything shows at low water; probably nothing to see |

## Tips
- `wiki_raw.py --rows` on "National Register of Historic Places listings in northern Westchester County, New York" leaves out Peekskill: the city has its own list page ("... listings in Peekskill, New York").
- Westchester County Parks pages read well with `page.py`; the county's PDF maps on parks.westchestercountyny.gov come back as an HTML page to a plain download, though `page.py` reads their text layer.
- Historic Hudson Valley's Van Cortlandt Manor page says the house is closed for tours during restoration (November 2026); look again before marking it open.
