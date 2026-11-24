# on_hvzt: Ontario: a third scatter
state: Ontario
region: on
date: 2026-11-24
places: 11
file: data_on_hvzt.py

## What this batch is
Eleven places across Ontario away from the Kingston/Rideau, first-scatter and second-scatter batches: Casa Loma and the Distillery District (Toronto), Old Fort Erie, Fort George and Navy Hall (Niagara), Sainte-Marie among the Hurons (Midland), Woodchester Villa (Bracebridge), Merrickville Blockhouse, Laurier House (Ottawa), the Bell Homestead (Brantford) and Old Hay Bay Church (Adolphustown). Claimed with `choose.py --thinnest` (Ontario, 48 places). Facts come from each place's Wikipedia article (`wiki_raw.py`) and, where a page opened, from whoever runs it (Casa Loma, Distillery District, Niagara Parks, Parks Canada, Merrickville-Wolford, Sainte-Marie, the federal designations directory). Fort George and Sainte-Marie are mostly reconstructions and are described as such. Pins were looked at on the aerial (no LiDAR: all are urban or open ground); Casa Loma's and Woodchester's parking points were dropped because the mapped lots did not look like lots. The Bell Homestead pin is on the road in front of the house, so it is `site`. Not checked: interiors and what is original; hours for Sainte-Marie, Woodchester, Bell Homestead and Hay Bay (no page opened or listings disagreed, so `hours='?'`); Navy Hall's visiting hours; who holds title to Old Hay Bay Church; fees at Sainte-Marie; brick for most places (`?`).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Sainte-Marie among the Hurons: street address and hours | Midland, ON (44.73417, -79.84528) | Its page names the site and cabins but gave no hours or address | Its visit page (try web fetch) |
| Navy Hall: hours | Niagara-on-the-Lake | Parks Canada lists it for rent | A Parks Canada visit page |
| Elora Mill, Inglis Falls mill remains, Cabot Head Lighthouse | Ontario | Looked for as candidates; no Wikipedia article under the title tried | A source for each |

## Tips
- `wiki_raw.py` has no article under "Hay Bay Methodist Church", "Hay Bay Church" or "Elora Mill"; the federal designations directory (`pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=...`) read well for Old Hay Bay Church.
- `page.py` read the Parks Canada hours pages for Fort George and Laurier House; brantford.ca and lennox-addington.on.ca gave 404/403.
- Wikipedia's coordinate for "Merrickville–Wolford" is the village, not the blockhouse: use `nom.py` (OpenStreetMap point was on the building).
- `photo_find.py new` took over two minutes (it moved to the background by itself); `look` then took seconds when logged in.
