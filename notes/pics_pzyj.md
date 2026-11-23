# Pictures batch pzyj (November 23, 2026)

**What this batch is.** A pictures run (PROMPTS.md job 8): photographs chosen for places already on the map that had none. No new places, no pins, no text about places. The batch's file is tools/pics_pzyj.py, written by tools/photo_find.py.

**How it was done.** Five rounds of `photo_find.py next 5` were started. Each place's sheet was looked at and one answer recorded per place with `set`. Wikimedia Commons answered slowly (its request limit waits), so the 40-minute limit was reached after 14 places had been looked at by hand, short of the 30 aimed for.

**Counts.**
- 8 places got a picture chosen by looking.
- 6 places were judged `none` by hand (no candidate plausibly shows the place).
- 8 places were recorded as `none` by the tool itself (Commons had nothing near the pin, under the names or in a category).
- 14 places were looked at by hand in all, 22 in all with the tool's own none.

**Hesitations, one line each.**
- first-presbyterian-lansingburgh: chose candidate 3 (the brick church with towers, 57 m from the pin, named by its later name, Cornerstone Community Church). Candidate 2 shows the same building; 3 is the wider view.
- rexford-aqueduct: chose candidate 8, flagged LOOK TWICE; its description names the Rexford Aqueduct and it shows a stone pier beside the modern bridge. The historic survey photographs of the arches were the other option.
- whale-rock-light: chose a scanned 1900 album page that carries photographs of the light; the lighthouse is the subject, but the picture is a scan of a page, not a single photograph.
- big-fill-promontory: chose a viewpoint 532 m off that names the site, with stone masonry and an interpretive sign; the fill itself is grass and rock ridge and is not clearly in view.
- jacob-patten-house-lansingburgh: chose candidate 1, the house 22 m from the pin.
- centrale-saint-narcisse: chose the stone annexe of the old plant, 32 m from the pin; the view is outside the building.
- kent-tavern-calais: chose a Historic American Buildings Survey photograph found by name; the caption places it in Kents Corners, Washington County, Vermont, which matches Calais, Vermont.
- old-austerlitz: chose a wide view of the village houses found by name only; the place is a village rather than one building.
- louis-miller-museum-hoosick-falls: none; portraits, a letter and a painting under the Miller name.
- bailey-house-brownville: none; a letter by Benedict Arnold to Captain McNeill, not the house.
- reformed-presbyterian-churchyard-duanesburg: none; the only candidate is a cemetery named for a church in another state.
- crandall-library-glens-falls: none; Civil War monument photographs.
- idaho-territorial-penitentiary-idaho-city: none; downtown buildings and plaques, and a courthouse of another building.
- split-rock-quarry: none; a rock sample of volcanic tuff.

**Not checked.** The Commons pages of the chosen pictures were not opened beyond the sheet and the tool's own address, credit and licence. The pictures were not checked against the places on the ground.
