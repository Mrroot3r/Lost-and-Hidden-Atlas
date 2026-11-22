# sk_qvtr: Saskatchewan: the Battlefords to the Cypress Hills, Regina and the north
state: Saskatchewan
region: sk
date: 2026-11-22
places: 18
file: data_sk_qvtr.py

## What this batch is
The third Saskatchewan batch, a first scatter over the parts of the province the first two left empty. Northwest: Fort Battleford, Fort Pitt, the Frenchman Butte rifle pits, Steele Narrows. Southwest: Fort Walsh, the Cypress Hills Massacre site with its rebuilt trading posts, Wood Mountain Post. South and centre: the Gravelbourg co-cathedral group, the Moose Jaw Court House, Government House and the Legislative Building in Regina, Last Mountain House. East and north: the Humboldt Post Office (now the museum), Keyhole Castle in Prince Albert, the Doukhobor prayer home at Veregin, Fort Livingstone, Cumberland House and Holy Trinity Church at Stanley Mission (the oldest building in the province, reached by boat). Sources: the Canadian Register (historicplaces.ca) statement for 15 places, read with `page.py --all`; Wikipedia raw text for all; the Museums Association of Saskatchewan listings (Fort Walsh, Veregin); Parks Canada's Fort Battleford hours and fees pages (read with the web fetch tool); governmenthousesk.ca (web fetch tool); the Legislative Assembly's tour and access pages; humboldtmuseum.ca; the Town of Gravelbourg's pages; Tourism Saskatchewan; HMdb for the Steele Narrows marker. Not checked: nothing on the ground; no Sask Parks page could be read, so season and hours are missing for Fort Pitt, Steele Narrows, Wood Mountain Post, Last Mountain House, Cumberland House and Holy Trinity; whether Holy Trinity opens inside; parking for all but Fort Walsh and Steele Narrows. Access to the Frenchman Butte battlefield and Fort Livingstone could not be confirmed from any page: both are `view`, `conf='mixed'`, and their pins mark the area only (Frenchman Butte is the Wikipedia coordinate, in woods). Cumberland House marks the park, not the powder magazine. Wood Mountain Post was moved onto a building that is probably the reconstructed barracks (not confirmed). Disagreements kept in the text: Steele Narrows date (June 3 or June 2, 1885), Government House vacated 1944 or 1945, Fort Livingstone as capital 1874–76 or 1876–77, Keyhole Castle private house or bed and breakfast.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Battleford Court House | Battleford, SK (52.73685, -108.31143, Wikipedia) | National historic site; Wikipedia article is thin | Its register statement (the CRHP id in the Wikipedia list is wrong: 7384 is Biggar station), build date and what survives |
| Old Government House / Saint-Charles Scholasticate | Battleford, SK, 52 7th Street West | Seat of the territorial government 1878–83; burned 2003; grassy plateau with buried remains (register id 7644) | Whether there is a marker or anything to see, and public access |
| Former Prince Albert City Hall | Prince Albert, SK | National historic site, register id 7536 | Register page refused connection; read it and add |
| Biggar railway station, Melville railway station, Canadian Bank of Commerce (Watson), Addison Sod House (Kindersley) | Saskatchewan | All national historic sites on Wikipedia's list | Not opened this session; Addison Sod House is on a farm, check access |
| St. Victor Petroglyphs Provincial Park | St. Victor, SK (49.4118, -105.8712) | Over 360 carvings in a provincial park | Left out: Indigenous rock art; read GUIDE.md on the native category and the park's own invitation to visit first |

## Tips
- `pincheck.py --lidar` in Saskatchewan prints NO 1 m LiDAR HERE on every tile: run it without `--lidar` there and save the minutes.
- historicplaces.ca answered "connection reset" for about one page in four (ids 12545, 11599, 7627, 7536); asking again a few minutes later worked for three of them.
- The Wikipedia national-historic-site list's CRHP id for Battleford Court House is wrong (7384, the Biggar station's).
- Parks Canada's Cypress Hills Massacre page gives a latitude of 51.78, which is wrong; Wikipedia's 49.549 is in the valley south of Fort Walsh.
- Tourism Saskatchewan listing pages are mostly menu: Steele Narrows read in full, Holy Trinity and Wood Mountain Post came back empty.
