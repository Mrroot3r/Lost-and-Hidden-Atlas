# Pictures batch fgdw (23 November 2026, scheduled run)
tidied: 2026-11-26

What this batch is: photographs for places already on the map that had none. No new places, no pins, no text. The file is tools/pics_fgdw.py, written by tools/photo_find.py. Seven rounds of `next 5`, 35 places looked at.

Counts:
- 20 places got a picture chosen by looking at the sheet.
- 15 places said none after looking.
- 69 places were recorded as none by the tool itself (nothing on Commons, or nothing new since an earlier look).
- The tool was logged in to Commons in every round.

Where I hesitated:
- frankfort-mineral-springs: the only candidate is a generic waterfall 64 m from the pin; the place is springs opposite a waterfall, so it plausibly shows the site, but it is not a building.
- union-bridge: the picture is the present Troy-Waterford Bridge, which stands on the old stone piers; chosen as the nearest view of the crossing.
- village-historique-acadien: an aerial view of the village 109 m from the pin, chosen over single buildings because the place is the whole open-air museum.
- lm-oakwood-cemetery-and-earl-chapel: the chapel photograph is 1.5 km from the pin by position but is named for the chapel and matches it.
- yankee-hill-lock-28: the lock chamber photograph taken 31 m from the pin; the HAER pictures named for it are 4 km off.
- empire-lock-29: an old HAER survey photograph of the lock, the clearest view of those listed.
- spanish-coquina-quarries: the quarry floor from the category named for it, 1.4 km off by position.
- forest-park: the dining hall of the old park, the only candidate.
- tannery-prattsville: only Pratt Rock and a postcard of it, no tannery; said none.
- myrna-loy-old-county-jail-helena: only street views and other buildings; said none.

Tips for the next session: publish.sh stopped once because main had moved (resync.sh fixed it); it then also staged two older LiDAR unit files from the workspace, which I removed from the pull request by hand before committing.
