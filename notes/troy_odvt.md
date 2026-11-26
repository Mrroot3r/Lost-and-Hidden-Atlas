# troy_odvt: Troy: Oakwood Cemetery, downtown and Lansingburgh
state: New York
region: renss, troy
date: 2026-11-21
places: 17
file: data_troy_odvt.py
tidied: 2026-11-26

## What this batch is
Seventeen places in Troy (region `troy`, drawn at random by `choose.py --state ny`), filling gaps on well-worked ground, with one just over the line in North Greenbush (`renss`). Oakwood Cemetery as a full entry, with separate pins for the Gardner Earl Memorial Chapel and Crematorium (inside shown only on Friends of Oakwood tour days) and the 1861 Warren Family Mortuary Chapel. Downtown: the Rensselaer County Courthouse with the 1793 first-courthouse marker, St. John's Episcopal Church (service times from the Diocese of Albany's parish page), the Rice Building, the John Paine Mansion, the National State Bank Building, 1819 Fifth Avenue (Mayor Murphy's house, later the Burns funeral chapel), the Pumpkin House and the Northern River Street collar-factory block. Further out: Glenwood (Troy Housing Authority offices), the Henry Koon House, the Powers Home in Lansingburgh, the former St. Barnabas Episcopal Church (New Hope Missionary Baptist), the Église Saint Jean Baptiste marker (church demolished 2021), and the 1861 Little Red Schoolhouse on US 4. Sources: Wikipedia read with `wiki_raw.py`; HMdb marker pages found from three HMdb nearby lists and read with `page.py`; the Oakwood Cemetery Association's about, policies, facilities and event pages; historypointer.com for Register street addresses; the Lansingburgh Historical Society page on the Powers Home; the North Greenbush town historian's 2008 column and a 2020 Q105.7 news item. Pins from the ArcGIS PointAddress, HMdb positions or `nom.py`, all looked at on the leaf-off aerial and LiDAR sheets; the courthouse was moved onto its OpenStreetMap building and the schoolhouse with `pix.py` off the road onto the building. Not checked: anything on the ground; present uses of the National State Bank, 1819 Fifth Avenue, the Powers Home, the Northern River Street buildings and the Paine Mansion (the Paine's year, architect and fraternity use come only from Wikimedia Commons photo descriptions); courthouse visiting rules; whether the Little Red Schoolhouse addition voted on in 2020 was built; New Hope Missionary Baptist's service times (no page of its own found). **The thin pin `lm-oakwood-cemetery-and-earl-chapel` is still on the map**: it sits at 42.74287, -73.67788, about 1.3 km south of the Oakwood Avenue gate, and `build_sites.py` refuses `was=` beyond 600 m, so this batch could not replace it. Someone allowed to change `src/landmarks.json` should move or drop that pin and give `oakwood-cemetery-troy` `was='lm-oakwood-cemetery-and-earl-chapel'`.

## Leads
Moved to `LEADS.md` on 2026-11-26 by the tidy job (3 rows). New leads for this ground go in the note of the batch that finds them.

| Place | Where | What is known | What is missing |
|---|---|---|---|

## Tips
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (5 tips).
