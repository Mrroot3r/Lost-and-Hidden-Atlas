# ak_sitka_qvrb: Alaska: Sitka
state: Alaska
region: ak
date: 2026-11-24
places: 14
file: data_ak_sitka_qvrb.py
tidied: 2026-11-26

## What this batch is
Fourteen places in Sitka, Alaska, which had two (St. Michael's Cathedral and the Russian Bishop's House): Castle Hill, the Old Sitka redoubt site, the Second World War batteries of Fort Rousseau on Makhnati Island (the Sitka Naval Operating Base lead from ak_nwfc, now done), Sitka National Historical Park's Totem Trail and 1804 fort site, Russian-American Building No. 29, St. Peter's by-the-Sea, the Alaska Native Brotherhood Hall, the Sheldon Jackson Museum and the Sheldon Jackson School campus, the Pioneers' Home, the old Post Office and Court House (City Hall), Sitka National Cemetery, Princess Maksoutoff's grave in the Lutheran cemetery, and the Sitka Woman's Club cottage (Register 2024). Chosen from the Wikipedia Register list for Sitka (22 rows).

How the sources were read: this session's machine could not reach Wikipedia, Wikimedia Commons, the ArcGIS geocoder or image services, OpenStreetMap or any managing body's page from the shell (every host refused by the network proxy), so `wiki_raw.py`, `page.py`, `nom.py`, `geo.py`, `parking.py`, `pincheck.py` and `photo_find.py` could not run. Every page was read instead with the web fetch tool (Wikipedia articles, Alaska State Parks, the National Park Service, Alaska State Museums, the St. Peter's parish site, the VA, HMdb, Visit Sitka, SAH Archipedia, the Living New Deal, the Sitka Sentinel). Pins were looked at on the same Esri World Imagery the pin check uses, one 300 m square per pin (900 m for Makhnati Island, 600 m for the national park), opened in a cloud browser at the export address in `tools/ortho.py`, with the pin at the centre pixel; five were moved with `pix.py move` (Castle Hill, ANB Hall, Pioneers' Home, the national cemetery) or given a parking point (the national park). No LiDAR sheet, no `land:` line and no parking lots from OpenStreetMap.

Not checked: anything on the ground; every interior; the Sheldon Jackson Museum's current hours (the state page carries an undated closure notice and was last updated in 2020); City Hall's hours; whether the Sheldon Jackson campus grounds may be walked; who owns the Woman's Club cottage now; the exact spot of the batteries on Makhnati Island and of the 1804 battle field; which roof is Building No. 29 and which is St. Peter's church as against the See House. Red brick: 'no' from what the sources say each is built of (log, wood, stone, concrete, stucco); '?' for the two burial grounds. No pictures were chosen: Commons could not be reached, so there is no pics file; twelve places link a Wikipedia article whose picture the app may show by itself.

## Leads
Moved to `LEADS.md` on 2026-11-26 by the tidy job (4 rows). New leads for this ground go in the note of the batch that finds them.

| Place | Where | What is known | What is missing |
|---|---|---|---|

## Tips
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (5 tips).
