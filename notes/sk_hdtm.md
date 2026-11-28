# sk_hdtm: Saskatchewan: convents, courthouses and a ruined Government House
state: Saskatchewan
region: sk
date: 2026-11-28
places: 13
file: data_sk_hdtm.py

## What this batch is
The fifth Saskatchewan batch: thirteen places spread over the east (Arcola, Vibank), the south (Willow Bunch, Val Marie, Ponteix), the centre and Regina (Watson, the RCMP Depot chapel), the northwest (Battleford: the ruins of Government House, the town hall and opera house, Gardiner Church; Cut Knife Hill) and the north (Duck Lake, Prince Albert). Picked from Wikipedia's lists of historic places in Saskatchewan, Regina, Battleford and Prince Albert, and each one read in its Canadian Register of Historic Places statement with `page.py`. Pins came from the register, the ArcGIS address lookup or OpenStreetMap and were looked at on the aerial; pictures through `photo_find.py` (four found, the rest none).
Not checked: owners (the register rarely gives them), opening times (no museum's own page was read, so the Willow Bunch, Val Marie, Watson and Prince Albert museums say `hours='?'`), parking, and the inside of any building. Pins that mark an area and not the building: the Battleford town hall, the Duck Lake jailhouse (small, not seen on the aerial) and the Prince Albert fire hall (a photograph 10 m from the address point showed another building). The Depot chapel's pin is a Commons photograph's position that lands on a small red-roofed building by the parade square. Brick was recorded only for Ponteix (a Commons photograph), the Val Marie and Battleford town hall (the register calls them red brick) and the buff Gardiner Church; the others are `?`, `no` for wooden or stucco buildings.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Kristiania Lutheran Church | Atwater, SK (about 50.78, -102.22) | Register id 6611: wooden church of 1920 with a bell-shaped spire, built over a church a tornado destroyed; services ended in the early 1980s | Its position: Atwater is not mapped in OpenStreetMap and no house number is given; the register's point lands in a field |
| Cattle Barn, Indian Head Research Farm | Valley Road at 18th Street, Indian Head, SK | Register id 18717: a large 1910s gambrel-roofed barn joined to a stable, a federal heritage building; one of the largest of its kind in the province | Which building on the farm it is (the register's point is a crossroads in the tree nursery), and whether visitors may come |
| Battleford Trail Wheel Rut Area | Swift Current, SK | Register id 4979: a fenced city lot with cart ruts of the 1883 to 1925 trail to Battleford | Its position: the register's point lands on a commercial lot; no address is given |
| Fleming Lake of the Woods grain elevator | Fleming, SK | Register id 12141: a national historic site from 1895; the register says it burned down in February 2010 | Nothing stands, so it was left out |
| Battle of Duck Lake site, Moose Jaw CPR station and others | Duck Lake, Moose Jaw | Register ids 12916 and 6639 were read; the battlefield has only a cairn and plaque | Not added for want of time |

## Tips
- `pincheck.py` marks Saskatchewan sheets with no LiDAR, as the guide says; the register's points were 200 to 600 m off at Arcola, Ponteix and Gardiner Church (Battleford) and in fields at Atwater and Indian Head. OpenStreetMap's `osmnear.py ... buildings` named the church at Ponteix and Gardiner when the address lookup did not.
- A Commons photograph's position (the API `prop=coordinates`) found the Depot chapel when the register's point landed in the open. Photographs that `photo_find.py` lists as "AWAY, names it" are a way to find where a building is.
- Wikipedia's Regina, Battleford, Moose Jaw and Prince Albert lists use the same `{{HPC row` form as the provincial list.
