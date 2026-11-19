# pane_jmkq: Nazareth, Bethlehem and Easton (Lehigh Valley), Pennsylvania
state: Pennsylvania
region: pane
date: 2026-11-19
places: 14
file: data_pane_jmkq.py

## What this batch is
The first places in the Lehigh Valley (region `pane`, drawn at random with `choose.py`; the Atlas had nothing within 25 km of Bethlehem). Northampton County round Nazareth, Bethlehem and Easton, with the Coplay cement kilns just over the line in Lehigh County. 14 places, mostly standing. Moravian: Whitefield House and Gray Cottage, Nazareth Hall with the Single Sisters' House, the 1741 Gemeinhaus (Moravian Museum of Bethlehem), the Colonial Industrial Quarter (1762 Waterworks, 1761 Tannery, the Pottery and mill ruins), the 1758 Sun Inn. Industry and transport: the Boulton gun works estate (Pennsylvania Longrifle Museum) in Jacobsburg, the Bethlehem Steel blast furnaces and the Hoover-Mason Trestle, the Coplay Schoefer kilns, the Lehigh Canal at Hugh Moore Park, the Chain Bridge piers in the Lehigh, the Lehigh Gap chain-bridge toll house. Also the Weona Park Dentzel carousel, the Kreidersville Covered Bridge and the Parsons-Taylor House in Easton. Wikipedia was read with `wiki_raw.py`; the managing bodies' pages (Moravian Historical Society, DCNR, Historic Bethlehem Museums & Sites, Sun Inn, ArtsQuest, National Canal Museum, Pen Argyl Borough, the covered-bridge association), HMdb markers, SAH Archipedia and the toll-house survey on ctevans.net with `page.py`. Not checked: anything on the ground; hours for the Boulton site and the Parsons-Taylor House (only the Lehigh Valley Passport to History pages give them, so `hours='?'`); Saylor Park's hours (Lehigh County's page would not connect); Waterworks and Tannery tour times (Historic Bethlehem's quarter page answers 404); who owns the Lehigh Gap toll house and Nazareth Hall; whether the Kreidersville bridge still carries cars; whether Hugh Moore Park and the Chain Bridge viewpoints can be reached while the Glendon Hill Road bridge is closed (2026). The Weona Park pin marks the park, not the carousel pavilion (`prec='area'`). Brick is '?' for Boulton, Kreidersville, the steel furnaces and Hugh Moore Park.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Jacobsburg village and Henry's Forge foundations | Jacobsburg Environmental Education Center, Bushkill Township, PA (district point 40.7825, -75.2928) | DCNR's history page says only foundations remain at the colonial village of Jacobsburg and the Henry's Forge site | Their positions and the trail that reaches them (the park map PDF); look on the LiDAR |
| Mary Immaculate Seminary | Lehigh Township, Northampton County, PA (40.7355, -75.5223) | Vincentian seminary 1939–1990, then an archdiocesan retreat centre; Register 2022; Hildreth Meiere apse mosaic (Wikipedia). CatholicPhilly (October 2014) says the property was sold | Who owns it now, its state, and whether it can be seen from a public road |
| Old Mill (Ruins) | Near Nazareth, PA (40.75137, -75.2566), OpenStreetMap ruin | Name only | Any source, the owner |
| Lime Kilns | Near Bethlehem, PA (40.6727, -75.35542), OpenStreetMap kiln point | Name only | Any source, the owner |
| Coffeetown Grist Mill | Williams Township, PA (40.619444, -75.205833) | Register-listed (77001179) | Not researched |
| Lehigh Canal: Glendon and Abbott Street industrial sites | Easton, PA (40.6567, -75.2947) | Register district (78002437); HMdb panels at Hugh Moore Park ("Men of Iron", "Birthplace of the American Industrial Revolution") speak of iron-works ruins | Which ruins can be seen, and from where |
| Edelman Schoolhouse | Moore Township, PA (40.7506, -75.3675) | Register-listed (100003520) | Not researched |

## Tips
- lvhistory.org (Lehigh Valley Passport to History) has a page for almost every museum and historic house in the Lehigh Valley, with address, hours and fees, and reads cleanly with `page.py --all`; but it is a consortium's listing, not the site's own page, so hours from it were not put in `hours=`.
- historicbethlehem.org's page for each museum (`/visit-us/museums-sites/<name>/`) gives full weekly and seasonal hours; its older addresses (`/the-colonial-industrial-quarter`, `/site-category/...`) answer 404.
- lehighcounty.org did not connect at all from here (park pages); jacobsburghistory.com's home page gives no hours.
- The Pennsylvania leaf-off pin check took about 15 minutes for 20 tiles; start it in the background as soon as the data file builds.
- `publish.sh` stopped once because another batch merged while the pin check ran; `resync.sh` caught up cleanly in about five minutes.
