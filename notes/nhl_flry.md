# nhl_flry: Rockingham County, New Hampshire: Seacoast forts, meetinghouses and depots
state: New Hampshire
region: nhl
date: 2026-11-19
places: 21
file: data_nhl_flry.py

## What this batch is
First pass at Rockingham County, which had only Fort Dearborn on the map: 21 places, drawn by `choose.py` (region `nhl`). Forts and harbour: Fort Constitution (currently closed for repairs, view only), Portsmouth Harbor Light, Fort Stark, Pulpit Rock Tower. Portsmouth: the Wentworth-Coolidge Mansion, the Warner House, the Richard Jackson House (1664), Strawbery Banke, Old North Cemetery, the Rockingham Hotel. Inland: the Weeks House, the Newington depot at Bloody Point (vacant, NHDOT is selling it), the Gilman Garrison House, Newmarket's stone mills and Stone School, the Square Schoolhouse, the Sandown, Danville and Fremont meetinghouses, and the Sandown and Raymond depots. Sources: the county's Register list and the Wikipedia articles read with `wiki_raw.py` (and `page.py` for the Wentworth-Coolidge article, which `wiki_raw.py` could not read); NH State Parks pages for the three state sites; the Warner House, Strawbery Banke and Friends of Portsmouth Harbor Lighthouses pages; colonialmeetinghouses.com for Sandown and Danville; the Sandown Historical Society page; NHDOT's 2026 surplus-land package for the Newington depot. Not checked: anything on the ground; hours for the Jackson and Gilman houses (Historic New England answers 403; Jackson's are Wikipedia's), the Raymond depot, Stone School, Old North Cemetery and the three meetinghouses (when their interiors open); Pulpit Rock Tower's tour dates and where to park; Fremont Meeting House's owner. Pins: the Danville, Sandown and Fremont meetinghouses were moved off the Wikipedia points onto buildings by reading the aerial against Wikipedia's descriptions, not a photograph; the Weeks House (area), Square Schoolhouse and Jackson House (site) pins are not on an identified building. Red brick: yes for the Warner House, Weeks House and Rockingham Hotel, some for Fort Constitution (brick walls in the sources), '?' for Fort Stark, Strawbery Banke, Old North Cemetery and the Newmarket mills; the rest are wood, stone, concrete or cast iron by their articles.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Isles of Shoals | Rye, NH (42.9760, -70.6206, Register list) | Register district 80000419, extends into Kittery, Maine | Not read: which islands and ruins can be reached by boat, and who owns them |
| Richman Margeson Estate | Newington, NH (43.0792, -70.8581) | Register list: in the Great Bay National Wildlife Refuge, no public access as of 2012 | Whether the refuge now allows any view of it |
| Battery 204, Odiorne Point | Rye, NH (43.04476, -70.71487, OpenStreetMap ruin) | Mapped ruin in Odiorne Point State Park, near the Fort Dearborn pin | A source; could be added to the Fort Dearborn entry |
| Kensington Town House and Union Meetinghouse | Kensington, NH (42.9316, -70.9452; 42.9313, -70.9453) | Register list only (13000155, 13000008); `choose.py` named Kensington as an old centre with no place | No Wikipedia article; Register forms not read |
| Dudley House and Exeter waterfront | Exeter, NH (42.9803, -70.9469) | Register listings 71000051 and 80000299 | Not read this session |

## Tips
- `wiki_raw.py "Wentworth-Coolidge Mansion"` writes the redirect into `Wentworth_Coolidge_Mansion.txt`, and the en-dash title it redirects to maps to the same file name, so the article comes back empty; `page.py` on the en.wikipedia.org address read it.
- Historic New England's property pages answered 403 again, and the archived copies could not be fetched by `page.py`.
- `friendsofpulpitrocktower.org` now redirects to a Facebook login; `weekshouse.org`, `newingtonnh.org` and `raymondnhhistoricalsociety.org` would not connect.
- The NH State Parks page for the Wentworth-Coolidge site is `/find-parks-trails/wentworth-coolidge-mansion`, not `...-historic-site` (404).
- `pincheck.py --lidar` on 21 pins took about four minutes; run it in the background.
