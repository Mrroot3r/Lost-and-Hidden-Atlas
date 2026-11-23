# on_pxkd: Ontario: a second scatter
state: Ontario
region: on
date: 2026-11-23
places: 11
file: data_on_pxkd.py

## What this batch is
Eleven places spread across Ontario away from the Kingston, Rideau and first-scatter batches: Her Majesty's Chapel of the Mohawks (Brantford), Eldon House (London), Gibraltar Point Lighthouse and Fort York (Toronto), Brock's Monument and the Laura Secord Homestead (Queenston), Bruce Mines (museum in the Church on the Rock), the Moose Factory HBC buildings, the Mill of Kintail, Silver Islet and the Cobalt mining district. Facts come from the Wikipedia article of each place, read with the web fetch tool, and from the page of whoever runs it where that opened (City of Toronto, Niagara Parks, Six Nations Tourism, Eldon House, Mississippi Valley Conservation, Town of Bruce Mines). parks.canada.ca and the Ontario Heritage Trust reset the connection from page.py, and cobaltmuseum.ca and the Silver Islet store's site did not resolve, so Brock's Monument hours, Cobalt, Silver Islet and Moose Factory hours are not checked (hours='?' or partial). Not checked on the ground: interiors, parking at most places, who owns the land at Silver Islet and Cobalt. The Moose Factory pin is area only (open field on the aerial). The Simpson shaft at Bruce Mines was not located. Pins looked at on the aerial only; the LiDAR sheet was not run (no woods). Brick: only Fort York ('some', brick officers' barracks and magazine, from Wikipedia) and the Gibraltar Point tower (stone, 'no') are settled.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Simpson Mine Shaft | Bruce Mines, ON | Restored copper shaft with replica whim; closed for repairs, no reopening date (town page) | A coordinate and its reopening |
| Moose Factory Staff House and blacksmith shop | Moose Factory, ON (51.2540, -80.6048 area) | Standing HBC buildings of 1847 to 1850 and 1849 (Wikipedia) | Exact positions and museum hours |
| Sainte-Marie among the Hurons | Midland, ON (44.73417, -79.84528) | Mission of 1639 to 1649, National Historic Site since 1920, now rebuilt (Wikipedia) | Which parts are original ground, hours |
| Old Fort Erie | Fort Erie, ON (42.89325, -78.92382) | Ruined 1764 fort rebuilt in 1937 to 1939 (Wikipedia) | Niagara Parks page, hours |

## Tips
- WebFetch read Wikipedia and city or town sites where page.py was reset on parks.canada.ca and ontarioheritagetrust.ca; ask it for specific facts (hours, address) in the prompt.
- Wikipedia coordinates were on the building for all but Moose Factory, where no Wikipedia point exists; use OpenStreetMap there.
- photo_find.py look takes seconds when logged in to Commons; Cobalt and Laura Secord had usable pictures, Bruce Mines had none.
