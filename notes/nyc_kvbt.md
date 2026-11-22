# nyc_kvbt: The Bronx
state: New York
region: nyc
date: 2026-11-22
places: 22
file: data_nyc_kvbt.py

## What this batch is
The first 22 places in the Bronx (region `nyc` drawn at random by `choose.py --state ny`; `start.py` found no Atlas place in the borough). Standing: the Van Cortlandt House (1748–49), the Valentine–Varian House (1758), Poe Cottage, the Bartow–Pell Mansion, Fort Schuyler, the Lorillard Snuff Mill in the Botanical Garden, Wave Hill, Fonthill Castle, the Keeper's House at Williamsbridge, the High Bridge, the Hall of Fame for Great Americans, the Rainey Memorial Gates, the New York, Westchester and Boston station house at East 180th Street, St. Ann's Church of Morrisania, St. Peter's at Westchester Square, Grace Church on City Island and Woodlawn Cemetery; empty and closed: the Old Bronx Borough Courthouse and the Kingsbridge Armory. Ruins: North Brother Island (view only, from Barretto Point Park), the Seton Hospital ruins and grotto (Raoul Wallenberg Forest / Seton Park) and the Putnam Division station skeleton in Van Cortlandt Park. Sources: Wikipedia read with `wiki_raw.py`; hours from the Historic House Trust pages, Wave Hill, the Botanical Garden, Woodlawn, SUNY Maritime, Bronx Community College and Grace Church's own page; NYC Parks pages for Seton Park, North Brother Island and the 2006 Van Cortlandt railroad article; Riverdale Press (2021) for the grotto; Welcome2TheBronx (2024) and the Governor's office (2025) for the courthouse and armory. Not checked: anything on the ground; the interiors of the churches, Fonthill and the station; service times at St. Ann's and St. Peter's (`hours='?'`); park hours for Seton Park, Van Cortlandt Park and the High Bridge; what stands at the Seton Hospital ruin pin (only NYC Parks' trail-map label and the LiDAR); whether the Hall of Fame has reopened after construction. Pins: all on Wikipedia or OpenStreetMap points, looked at on the aerial; the Keeper's House was moved to its OpenStreetMap building. North Brother Island's pin is the island itself (no landing); Woodlawn's is one point in 400 acres. Red brick was settled from sources or a Commons picture where possible; eight places are `'?'`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Seton Hospital grotto (exact spot) | Bronx, NY, behind the Seton Park tennis courts (about 40.8860, -73.9160) | Riverdale Press, August 2021: a small rock grotto, the last piece of Seton Hospital, behind the tennis courts | A coordinate seen on the aerial; whether it was restored |
| Bronx General Post Office | Bronx, NY (address not checked) | Welcome2TheBronx (2024) says the landmark post office was for sale for $75 million | Wikipedia article not read; murals, present use, hours |
| Hunts Point station (NYW&B) | Bronx, NY (40.8197, -73.8899) | On the Register list (100007684) as Hunts Point Rail Station | Article not read; whether the station house is open or restored |
| Old Croton Aqueduct in the Bronx (Van Cortlandt Park, Aqueduct Walk) | Bronx, NY | The aqueduct runs through Riverdale, Van Cortlandt Park, Kingsbridge and University Heights (Register list) | A point and a source for what can be seen (weirs, vent towers) on the Bronx stretch |
| St. Ann's and St. Peter's service times | Bronx, NY | Both active Episcopal parishes (added in this batch) | Their own pages' service times for `tools/hours.py` |

## Tips
- `wiki_raw.py` caches "Bartow-Pell Mansion" (hyphen, a redirect) and "Bartow–Pell Mansion" (en dash) under the same file name, so the second returns the redirect text; delete `research/wikiraw/Bartow_Pell_Mansion.txt` and ask again.
- The Historic House Trust pages gave owner, operator and hours for all four Bronx house museums in one `page.py -g` each.
- NYC Parks' Raoul Wallenberg Forest trail-guide PDF has no text layer except its map labels, which do include "Ruins of Seton Hospital".
- `photo_find.py look` took about a minute per candidate this time (Commons slow); run it in the background for three places or more.
