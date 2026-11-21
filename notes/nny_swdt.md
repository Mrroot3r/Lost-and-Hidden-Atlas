# nny_swdt: Northern Franklin County: Malone, Burke, Fort Covington and the Debar country
state: New York
region: nny
date: 2026-11-21
places: 15
file: data_nny_swdt.py

## What this batch is
Fifteen places in northern Franklin County, New York, drawn at random by `choose.py --state ny` (region `nny`, which offered Fort Covington); the Atlas had nothing within 30 km of Malone. Malone: the 1853 Horton Gristmill (a sandstone shell, owned in 2016 by the North Star of the Adirondacks Foundation), the 1892 Isaac Perry armory (vacated 2003), the 1852 Northern Railroad freight depot, the First Congregational Church (1883; an Underground Railroad tunnel said to survive in its basement), the 1830 Anselm Lincoln stone house and the 1934 post office. Burke: the Wilder Homestead (Farmer Boy farm, open by tour). Duane: the 1883–85 Methodist church (town-owned) and Debar Pond Lodge (DEC; removal proposed 2020 and again in 2025; finished from the LEADS.md row, pin moved onto the lodge roofs). Fire towers on Azure Mountain (cab open) and Loon Lake Mountain (closed, stairs removed). Border stations of 1931–33 at Trout River, Chateaugay and Fort Covington, the last with the 1820 hotel the line runs through (now the Halfway House parcel business). Mountain View's 1916 union church. Sources: Wikipedia through `wiki_raw.py`, HMdb lists and marker pages, the State Military Museum armory page, River City Malone and Spectrum News (Horton mill), the Almanzo Wilder Farm tours page and the Town of Burke, DEC's Debar Mountain Wild Forest page and the Debar Lodge day-use plan PDF, the Adirondack Explorer, Adirondack Council and Adirondack Wild (Debar), Protect the Adirondacks' Azure Mountain sheet, and QCNA (Halfway House), all through `page.py`. Not checked: any Register form; whether Debar Lodge still stands in November 2026 and whether its road is gated; the present use and owners of the armory, freight depot, Lincoln house and Horton mill (and whether its walls were capped); service times at the Congregational and Mountain View churches; whether the 1934 post office is still the post office. Pins: Horton mill, freight depot and Duane church are `area` (the building could not be picked out); Azure tower is `site` (summit under trees). The Fort Covington and Chateaugay pins draw `check.py`'s "just outside ny's outline" warning; on the aerial both are on the road at the United States station side.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Merrillsville Cure Cottage | Franklin, NY (44.52167, -74.01444) | Wikipedia: a cure cottage of about 1900, moved here in 1920 and used as the Town of Franklin's town hall; Register 1995 | The Register point is on the road with no building; the geocoder puts the Franklin town hall in Vermontville. Whether the cottage still stands and where |
| Catalan Forge site | Brainardsville, Franklin County, NY (44.84105, -74.03530, HMdb 57267) | 1940 state marker: the world's largest Catalan forge, built 1874, abandoned 1893 | Whether anything is left to see, and on whose land |
| Fort Covington Presbyterian Church | Fort Covington, NY (44.99097, -74.49285, HMdb 174921) | 1932 marker: organized about 1821, built 1828, rebuilt and enlarged 1866 | A source that it stands and what it is like; the fpccov.org site is Covington, Georgia |
| Union Church, Moira | Moira, NY (44.81801, -74.55625, HMdb 79115) | 1932 marker: first church in the county, about 1833; present church 1867 | Whether the 1867 church stands; any source |
| Franklin County House of History | Malone, NY | Franklin County Historical and Museum Society's house museum | Its own page with hours; adirondackscenicbyways.org would not connect |
| Hastings Farmstead, Brighton Town Hall, Beth Joseph Synagogue, St. Regis Mountain tower | Dickinson Center, Brighton, Tupper Lake, Santa Clara, NY | On the Franklin County Register list with Wikipedia articles | Not reached; the southern county (Tupper Lake, Paul Smiths, Saranac Inn camps) has nothing on the Atlas outside Saranac Lake |

## Tips
- Web searches here returned titles and links only, no quoted text; read pages with `page.py -g`.
- fpccov.org (top result for "Fort Covington Presbyterian Church") is First Presbyterian of Covington, Georgia.
- The Franklin County Register list point for the Fort Covington border station (44.9906, -74.7396) is 18 km west; Debar Pond Lodge's list point is 750 m off in forest; the lodge roofs show plainly on the leaf-off aerial at 44.62888, -74.19716.
- The DEC Debar Mountain Wild Forest page (dec.ny.gov/places/debar-mountain-wild-forest) gives trail lengths and the fire-tower status for Azure, Loon Lake and Debar mountains in one place.
