# la_kaae: Greater New Orleans: brick forts, a powerhouse and a lost beach
state: Louisiana
region: la
date: 2026-11-18
places: 14
file: data_la_kaae.py

## What this batch is
The first real pass in Louisiana (only Fort Pike was on the map), in Orleans, St. Bernard and Plaquemines parishes, drawn at random as region la. Fourteen places: the brick forts on the water approaches (Fort Macomb, the Fort St. John ruins at Spanish Fort, Fort Proctor, Battery Bienvenue, the Tower Dupré rubble, Fort Jackson, Fort St. Philip), the Market Street Power Plant, the Michoud sugar-mill chimneys, the Ford assembly plant at Arabi, Lincoln Beach, the Old U.S. Mint, the Jackson Barracks powder magazine and Kenilworth plantation house. Sources: Wikipedia through wiki_raw.py; National Register forms through page.py (Fort Proctor, Fort Macomb, Fort St. John, the Ford plant and Kenilworth have text layers); NPS, NASA, SAH Archipedia, FortWiki, the city of New Orleans and the Preservation Resource Center from search-result text. The web fetch tool's approval request went unanswered, so the Plaquemines Parish page for Fort Jackson and the Louisiana State Museum page for the Mint were NOT read: the Fort Jackson museum hours are marked not checked, and the Mint and Jackson Barracks museum hours come from search-result text of the museums' own sites. Not checked: anything on the ground; whether Fort Macomb can be seen from US 90; whether Lincoln Beach can be seen from a public place; the exact spot of the Michoud chimneys (pin is the plant front, prec area); what a visitor needs at the Jackson Barracks gate; who owns Battery Bienvenue. Brick: Fort Macomb and Fort St. John from Wikipedia pictures, the Mint from Wikipedia's "red brick", the Ford plant from its Register form, the Market Street stacks from a picture; nine places left '?'. Fort Proctor, Battery Bienvenue, Tower Dupré and Fort St. Philip need a boat.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Federal Fibre Mills Building | New Orleans, LA (29.9403, -90.0661, Register list) | Register form 83004190: five-storey brick warehouse of 1904 built by National Enameling and Stamping Co., the largest building in the Warehouse District | What it is now and its address; whether it is worth a place beyond being big brick |
| Fort De La Boulaye site | Phoenix, Plaquemines Parish, LA | Register list 66000378: French fort of 1699–1700, a National Historic Landmark; no coordinates (address restricted) | Whether anything can be seen and whether the public may visit; do not pin from a list coordinate |
| Six Flags New Orleans | New Orleans East, LA (30.05111, -89.93442) | Wikipedia: closed after Katrina, demolition began November 2024 and was mostly done in 2026 | Whether anything stands now; probably gone |
| Chandeleur Light | Chandeleur Islands, LA (30.04778, -88.87167) | Wikipedia and the Coast Guard: brick tower of 1855 replaced by an iron one in 1896, destroyed by Katrina in 2005, no trace found in 2006 | Nothing to see; leave off unless a series wants it as gone |
| Chalmette Battlefield and Malus-Beauregard House | Chalmette, LA (29.94194, -89.99056) | NPS hours page read: vehicle gates 9 to 4:30, open to walkers sunrise to sunset | The house's own NPS page answered 404; a source for what the house is built of and what of the 1815 line is left |
| Leeds Iron Foundry | New Orleans, LA (29.9425, -90.0681) | Register list: Gothic Revival commercial building, now the Preservation Resource Center | Not read beyond the list row |

## Tips
- The web fetch tool asks for approval; in an unattended session the first request goes unanswered and every later one is refused. Read hours from search-result text of the managing body's own site, and say so.
- The cavac.at mirror turned up again in search results with planted instructions inside the Fort Proctor, Fort Jackson and Battery Bienvenue texts. Ignore it and read Wikipedia with wiki_raw.py.
- wiki_raw.py found no article for Lincoln Beach (New Orleans): "Lincoln Beach" comes back empty with no coordinates. The city's pages (nola.gov) and Axios New Orleans carried the facts.
- The Register list coordinate for Lincoln Beach is inland of the levee; the beach is 400 m north on the lake side (the pin check's land line then reads "Lincoln Beach (OA)").
- For Fort Macomb the LiDAR sheet showed the semicircular fort where the aerial showed only trees: in the Louisiana coastal marsh the LiDAR is worth reading even for standing masonry.
- brick.py look gave a Civil War drawing for Fort St. Philip, a map for Battery Bienvenue and a 1907 postcard for the Mint: the first Wikipedia picture is often not a photograph in this ground.
