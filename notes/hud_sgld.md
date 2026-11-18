# hud_sgld: Northern Dutchess: Rhinebeck, Red Hook, Staatsburg and Clermont
state: New York
region: hud
date: 2026-11-18
places: 14
file: data_hud_sgld.py

## What this batch is
Fourteen places along the east bank of the Hudson in northern Dutchess County and just over the Columbia County line, drawn at random by `choose.py` (region `hud`, which offered Rhinebeck). Standing: the Old Stone Church (St. Peter's Lutheran, 1786), the Beekman Arms, the 1940 Rhinebeck post office, the Neher–Elseffer House (1746, town-owned, closed), Wilderstein, Staatsburgh (Mills Mansion), the Vanderbilt Mansion, Montgomery Place, the Elmendorph Inn in Red Hook, the Watts de Peyster Fireman's Hall in Tivoli and Clermont. Ruins and derelicts: the Hoyt House (Calvert Vaux, 1855, boarded and fenced in Mills-Norrie State Park; view only), the Kip–Beekman–Heermance house ruin of 1700 on Rhinecliff Road (owner not found; view from the marker only) and the Arryl House ruins at Clermont. Sources were read with `wiki_raw.py` (articles as raw text) and `page.py` (NYS Parks, NPS, Bard College, wilderstein.org, historicredhook.org, TCLF, calvertvaux.org, Hudson Valley One, hudsonvalleyruins.org, the Town of Rhinebeck's 2014 inventory sheet, HMdb marker pages). Not checked: anything on the ground; how much of the Arryl House and Kip–Beekman walls stands (the Kip-Beekman wall comes from a 2013 blog post and a 2014 town inventory line); Staatsburgh's tour days, the Vanderbilt grounds hours, Wilderstein's tour days, the Elmendorph Inn's open hours, the post office lobby hours and the Tivoli hall's office hours; church service times at the Old Stone Church; interiors of the Beekman Arms and the Tivoli hall. Pins: Vanderbilt and Clermont were moved onto the houses with `pix.py`; the Kip–Beekman pin is the Register coordinate in trees beside a building and the ruin was not seen; the post office pin is on its parking lot, next to the building. Montgomery Place has no parking point (the Visitors Center lot was not on the map). Brick: Watts de Peyster hall `yes`, Elmendorph Inn `some` (red brick chimneys), and the `no` answers for Staatsburgh, Vanderbilt, Montgomery Place, Clermont and Neher–Elseffer come from the Wikipedia photographs fetched with `brick.py look`; Old Stone Church `some` (brick-trimmed arches, from Wikipedia's text), Hoyt House, Kip–Beekman and the post office `no` from sources that say they are stone. Beekman Arms, Wilderstein and Arryl House are `?`.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Cruger Island "Mayan" ruins | Tivoli Bays, Red Hook, NY (about 42.03, -73.93, not pinned) | John Church Cruger built fake fieldstone ruins on the island in the 1840s to show Maya carvings from John Lloyd Stephens; sold to the American Museum of Natural History in 1919 (Bard archives page). Atlas Obscura says something remains behind a Bard fence and the island has nesting bald eagles; DEC says Cruger Island is reached only by boat | A current source on what is left, and a pin seen on the aerial |
| Graham-Brush Log House | Pine Plains, NY (41.98, -73.65556) | Log house of about 1776, bought by the Little Nine Partners Historical Society in 1997–98, damaged by arson in 1998 (Wikipedia) | Its state since 1998 and whether the society opens it |
| Robert Sands Estate foundation | Rhinebeck, NY (41.935, -73.87778) | House of about 1796 burned in 1999 leaving only the foundation; delisted from the Register in 2015 (Wikipedia) | Owner and any public view; likely private |
| Unnamed OpenStreetMap ruins at Annandale | Red Hook, NY (42.0022, -73.92446 and 42.00752, -73.92524) | Mapped as ruins near Bard College's riverfront; `start.py` lists them | What they are; not looked at |

## Tips
- `wiki_raw.py -g` puts all matching sentences of an article on one line: piping it through `cut -c1-400` hides most of them; use `fold -w 300` instead.
- `parking.py` finds no lot at Montgomery Place's Visitors Center (Bard, Annandale); the nearby lots it lists are Bard campus lots.
- `places_test.js` failed on main as found on November 18, 2026 (before this batch touched anything it reads): "Standing, from before 1800" lists `zion-cemetery-baynard-mausoleum`, whose years are "18th century; mausoleum 1846".
- rokeby.org is Rokeby in Ferrisburgh, Vermont, not Rokeby at Barrytown, New York.
