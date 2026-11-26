# Pictures batch pics_ndng (2026-11-22)
tidied: 2026-11-26

What this batch is: a pictures job (job 8). No new places, no pins, no text. It chose photographs for places already on the map that had none, using `tools/photo_find.py next 5` and looking at each sheet. The pictures file is `tools/pics_ndng.py`.

Counts for this batch:
- 23 places had a look, in total.
- 8 got a picture chosen by looking.
- 7 were given none by the session, because no candidate plausibly showed the place.
- 8 were recorded as none by the tool itself, because Commons had nothing near the pin, under the name, or in a named category.

How the pictures were chosen: one candidate per place, from the sheets. Chosen by looking:
- capitol-theatre-rome: a Commons marquee photo at 16 m from the pin. Mostly marquee, so a weaker choice than a full facade.
- farmington-canal-lock-13-hamden: the lock wall at the pin.
- first-methodist-church-nebraska-city: the 1855 wall, named in its caption. Small brick front, shown from outside.
- high-rock-park-spring: a 19th-century stereo view of the spring rock, by McDonnald & Sterry.
- kyburz-flat-mores-station: a view across the flat, from a category named for the place.
- pecos-mission-church-nm: a wide view of the church ruin, named in full.
- potsdam-civic-center-museum: the museum front of the complex. The photo shows brick, while the place text says sandstone for the 1876 church. The complex's 1934 brick front matches its Wikipedia description, but this is the one choice a person should look at.
- stafford-flint-furnace: the furnace itself, from a category named for it.

Where I hesitated (one line each):
- capitol-theatre-rome: the chosen marquee photo is mostly sign. Kept, because it is the building's front at the pin.
- potsdam-civic-center-museum: brick photo for a place whose text says sandstone. See above.
- high-rock-park-spring: the chosen view is a 19th-century stereo card; it is the spring rock itself, not the later pavilion.
- first-methodist-church-nebraska-city: the 1855 wall photo is a partial view of the small building; the nearby later church (by name only) was not chosen.
- troy-steel-iron-furnace-site-menands: a 395 m photo of a masonry tower yard labelled "old King Fuels" was passed over. It is not this furnace.
- kyburz-flat-mores-station: the chosen picture shows the meadow, not any building. The site has no standing structure, so this is the flat as a visitor sees it.

Not checked: a fourth round of `next 5` was cut off by a timeout before it printed its sheets. The places it had not reached still wait in the tool, and no sheet from it was used. Two places that the tool recorded as none by itself during that run are counted in the eight above.

Tips for the next session:
- `tools/photo_find.py next 5` can take more than two minutes. Run it with a long timeout (about ten minutes), one command at a time, and write its output to a file so a timeout does not lose it.
- Several Commons results come back as "LOOK TWICE" for the same subject across different states or towns (Erie Canal locks, Capitol theatres, Steelers players named Troy). Most were wrong. Choose from the description, not the name alone.
