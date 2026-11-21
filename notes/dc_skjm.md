# dc_skjm: Washington, D.C.: east of the river, Northeast and a second Northwest pass
state: District of Columbia
region: dc
date: 2026-11-21
places: 19
file: data_dc_skjm.py

## What this batch is
A second scatter of 19 places over the District (taken with `choose.py --thinnest`; it had 19, all from dc_uzsg), aimed at the wards the first batch missed: the National Capitol Columns and the New York Avenue brick kilns at the National Arboretum, Kenilworth Aquatic Gardens, the Franciscan Monastery, Cedar Hill (Frederick Douglass), Fort Stanton and Fort Davis, Woodlawn Cemetery, Eastern Market, the Old Naval Hospital (Hill Center), the Navy Yard car barn ("Blue Castle"), St. Paul's Rock Creek, Lincoln's Cottage, the McMillan sand-filter site (now Reservoir Park), Rosedale, the Castle Gatehouse at the Georgetown Reservoir, the Mason house ruins on Theodore Roosevelt Island, the Octagon and the Oak Hill Cemetery chapel. Sources: the four DC Register list pages and the articles, read with `wiki_raw.py`; NPS `places/`, history, tours and directions pages read with `page.py`; the parks' `<code>_linked_data.json` files for NPS opening hours; the pages of Lincoln's Cottage, the Franciscan Monastery, Oak Hill Cemetery, St. Paul's, the Rosedale Conservancy, Eastern Market and a DC Parks and Recreation release. Not checked: hours at the National Arboretum (its site would not answer), the Octagon (visiting page 404), Eastern Market (no hours on its page), Hill Center, Woodlawn, Fort Stanton and Fort Davis; whether the brick kilns still stand (the Esri aerial shows bare, disturbed earth at the Register point); which McMillan sand bins and regulator houses survive; the colour of the car barn now. Pins that mark only an area: Fort Stanton and Fort Davis (woods of the parks; no earthwork could be picked out on the LiDAR), the Mason house (pin is the island's memorial plaza), McMillan (the new park). The St. Paul's pin is on the cross-plan building in Rock Creek Cemetery taken to be the church, not confirmed by a source. Red brick was set only where a source says what a place is built of; most are '?'. Nobody has been on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Glenwood Cemetery Mortuary Chapel | 2219 Lincoln Road NE, Washington, DC (38.92194, -77.00611) | Glenn Brown chapel of 1892, Register 1988 (Wikipedia) | Cemetery's own hours: search results for "Glenwood Cemetery" lead to Houston's glenwoodcemetery.org |
| Boundary markers of the original District | SE No. 2 at Fort Davis (38.8722, -76.9358) and others on the 1791–92 line | Register list rows | Whether `check.py` accepts a pin on the District line; each stone's setting and access |
| Fort Mahan | Benning Road NE area, Washington, DC | NPS places page gives the history but says nothing of what remains | Whether any earthwork shows (try the LiDAR sheet) |
| U.S. Capitol Gatehouses and Gateposts | Constitution Avenue at 15th and 17th Streets NW (Register 38.890833, -77.032222) | Register row only; no Wikipedia article under the list's name | A source opened in a session |
| Latrobe Gate, Washington Navy Yard | 8th and M Streets SE (38.8764, -76.9953) | Register row | Whether the public may see it from outside the base |

## Tips
- NPS parks' hours pages draw the hours by script, but `https://www.nps.gov/<code>/<code>_linked_data.json` holds them as `openingHoursSpecification` (opens, closes, a description): it gave Kenilworth, Theodore Roosevelt Island and Frederick Douglass hours when `page.py` gave none.
- The DC Register lists are four pages: "... in Northeast Quadrant, Washington, D.C.", "... in Southeast Quadrant, Washington, D.C.", "... in central Washington, D.C.", "... in the upper NW Quadrant of Washington, D.C." and "... in western Washington, D.C."; the plain DC title has no rows.
- `photo_find.py set <id> none` does not stop a Wikipedia article's picture: Fort Stanton's article picture is a Battery Rodgers magazine, which the place page will still show.
- Wikipedia's coordinate for Fort Davis Park lands on houses in the Fort Davis neighbourhood, and for St. Paul's Rock Creek on the road; the Castle Gatehouse's falls in the reservoir.
