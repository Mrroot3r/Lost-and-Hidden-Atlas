# bc_ftpi: British Columbia: a second scatter, Vancouver Island to Atlin
state: British Columbia
region: bc
date: 2026-11-23
places: 16
file: data_bc_ftpi.py

## What this batch is
Sixteen places spread across British Columbia, claimed with `choose.py --thinnest` (BC had 36 places): in Victoria Craigdarroch Castle and Point Ellice House (closed to the public since August 21, 2026); the Sheringham Point Lighthouse at Shirley; the Point Atkinson Lighthouse in West Vancouver's Lighthouse Park; Britannia Shipyards in Steveston; the old Stave Falls powerhouse (BC Hydro's visitor centre); the Kilby store at Harrison Mills; Christ Church at Hope (1861); the Grist Mill at Keremeos (1877); the Myra Canyon trestles of the Kettle Valley Railway near Kelowna; the O'Keefe Ranch north of Vernon (buildings closed since October 2026); the BC Copper Company smelter stack and slag at Greenwood; the Rossland Court House; the Doukhobor Suspension Bridge at Castlegar; the Twin Falls Tea House in Yoho; and the M.V. Tarahne at Atlin.

Sources: Wikipedia (`wiki_raw.py`), the Canadian Register (only three pages opened: Christ Church, Doukhobor bridge, Rossland Court House), the Parks Canada federal designations directory, and the managers' own pages where they opened (BC Parks, BC Hydro, Kilby, the Sheringham society, the Rossland Museum, the Greenwood Museum and city, the O'Keefe Ranch, the province's release on Point Ellice House, the Anglican diocese). Hours for Craigdarroch Castle and Lighthouse Park are as web search results quote the castle's and the district's pages (one drawn by script, the other HTTP 403). Britannia Shipyards, the Grist Mill, Christ Church, Myra Canyon, the Doukhobor bridge, the Twin Falls Tea House and the Tarahne have `hours='?'`. Red brick was settled from the Register text or from Commons photographs for eleven places; Stave Falls, Britannia, Point Ellice, O'Keefe and the Greenwood stack (a brick stack, colour not seen) are `?`. Nothing was checked on the ground. Othello Tunnels was written and then dropped: it is already on the map in `data_states.py`.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Emily Carr House | 207 Government Street, Victoria, BC (Wikipedia 48.4138, -123.37) | National Historic Site, built 1863 for the Carr family; Register id 10705 | Current opening days: listings disagree and the house's own page was not read |
| Esquimalt and Nanaimo Railway Roundhouse | Victoria West, BC | National Historic Site, 1913; Register id 7416 | Register page would not open; who owns it now and whether it can be seen |
| Greenwood Courthouse | Greenwood, BC | City of Greenwood page: a 1903 wooden courthouse with stained-glass windows, guided visits through the Greenwood Museum | Pin, a register entry and visiting times |
| Walhachin flumes | Walhachin, BC, south shore of the Thompson (Wikipedia 50.74972, -120.98444) | Wikipedia describes the 1910s orchard flumes and their abandonment | A source on what is left today and where to see it |
| Atlin Courthouse | Atlin, BC | Wikipedia photo caption: built 1900, now an art gallery; kept by the Atlin Historical Society | Pin and a page of the gallery's own |
| Powell River Townsite | Powell River, BC | National Historic Site district, 1911 | Register page; pick its best buildings |
| Twin Falls Tea House season | Yoho National Park | Entry added with `hours='?'` and the pin at area precision | Parks Canada's page refused; the season and a pin on the building |

## Tips
- historicplaces.ca answered the first request or two and then reset every connection for the rest of the session (proxy "ws_closed_mid_exchange"), whether through `requests`, `curl` or `page.py`, with or without 15-second gaps. Fetch the Register pages you need most first, one at a time. The Parks Canada directory (`pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=N`) still answered and carries the plaque text and dates, but its keyword search ignores the keyword.
- Wikipedia's "List of National Historic Sites of Canada in British Columbia" gives each site's Register id in a `{{CRHP|id|name}}` template; grep the cached raw text for `CRHP|` to get them all in one go.
- `start.py` lists only the places within its radius of the town given: a province-wide batch should grep `tools/data_*.py` (including `data_states.py`) for each name before writing. The Othello Tunnels were in `data_states.py`.
- `nom.py` found most BC buildings by name; it found nothing for the Keremeos Grist Mill or the Twin Falls Tea House. The ArcGIS geocoder found 2691 Upper Bench Road.
