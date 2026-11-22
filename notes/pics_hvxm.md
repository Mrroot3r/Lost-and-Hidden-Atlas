# Pictures batch pics_hvxm (2026-11-22)

What this batch is: a pictures run (job 8). No new places, no pins, no text. It chooses freely licensed Wikimedia Commons photographs for places already on the map that had none, one answer per place by looking at its candidate sheet.

Counts, 19 places looked at in three rounds of `photo_find.py next 5`:
- 7 places got a picture (cape-bear-lighthouse, saratoga-spa-bathhouses, larkin-administration-building, drinkhall-saratoga-springs, brown-hopkins-country-store-chepachet, roque-house-natchitoches, prison-brickyard-deer-lodge).
- 7 places were set to none after looking (west-troy-weighlock, faith-mills-averill-park, martindale-boat-basin, knox-school-5-thompsons-lake, old-holy-trinity-middleton, jay-cooke-river-inn-swinging-bridge, doe-farm-cellar-hole-durham).
- 5 places were recorded as none by the tool itself, with nothing on Commons (lidar-scutt-road-house-site, stonewall-quarry-park-kilns, maxon-mills-wassaic, canyon-round-station-pony-express, cohotate-ice-house).

Where I hesitated:
- west-troy-weighlock: the only candidates were a park sign and canal-wall ruins; the weighlock building is not in any picture. Set none.
- cape-bear-lighthouse: chosen picture is 107 m from the pin but names the lighthouse and matches its 1881 tower. A nearer view at 29 m (the lighthouse with picnic tables) was also a fair choice; the 107 m one was taken for its wide framing of the whole tower.
- saratoga-spa-bathhouses: chosen picture is the Roosevelt Baths, matched by name only (no position). It is one of the park's bathhouses, so it was accepted; the Hall of Springs is not shown.
- larkin-administration-building: chosen picture is the surviving brick wall, 61 m from the pin, named by its file name. Its description matches the remaining wall.
- drinkhall-saratoga-springs: chosen picture is the front of the building, matched by name at 39 m from the pin.
- roque-house-natchitoches: chosen picture is a HABS survey view named Roque House, 267 m from the pin, matched by name only. Candidates named Badin-Roque House 10 to 21 km away were not chosen.
- prison-brickyard-deer-lodge: chosen picture is a category photograph of the historic district looking north, 119 m from the pin; it shows the grassy hill and pit-like hollows, not clearly the kilns or yard buildings.
- martindale-boat-basin: only a trail photograph of a canal bank 107 m away; the stone basin cannot be told in it. Set none.
- jay-cooke-river-inn-swinging-bridge: the candidates were falls, river views, bridge-closed signs and an inn dining room; no view of the inn or the bridge. Set none.
- faith-mills-averill-park and doe-farm-cellar-hole-durham: candidates were unrelated (a protest photograph, burial grounds elsewhere). Set none.
- knox-school-5-thompsons-lake and old-holy-trinity-middleton: candidates were unrelated (Philippine church, Staffordshire war memorial, Northumberland church). Set none.

Not checked: the rounds stopped at about 19 places (not 30) because the tool takes about eight to ten minutes per round on Commons' request limit, and the 40-minute limit of the run was reached. Picture credits and licences were taken from Commons by the tool and not typed.

Tips for the next session: a `next 5` round can run longer than the shell's two-minute default; run it with a long timeout, one at a time. Commons rounds with many "none by the tool" places return quickly; rounds with candidates take about eight minutes.
