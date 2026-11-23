# Pictures batch pics_vagq (2026-11-23)

## What this batch is

A pictures-only batch: no new places, no pins, no text about places. The tool
(`photo_find.py next 5`) took waiting places six rounds running, 30 places in all
had a look, and 10 more the tool recorded as "none" by itself (Commons had nothing
for them). Every picture is taken from Wikimedia Commons by the tool; nothing was
typed by hand and nothing came from anywhere else.

Totals in `tools/pics_vagq.py` (here `source/tools/pics_vagq.py`): 40 entries.

- **16 places got a picture** (chosen by looking at the sheet).
- **14 places said none** (chosen by looking at the sheet; the candidates did not show the place).
- **10 places the tool recorded as none by itself** (no candidates on Commons).

## Places where I hesitated

Each is a picture chosen, unless marked "none".

- coleman-main-street: one corner commercial building at the pin in Coleman, Alberta. The place is the whole company town and its main street; no picture shows the street itself. The 1910 Main Street postcard is Coleman, Michigan, so it was not used.
- bernat-mill: the Bernat gate and brick ruins (Uxbridge, MA). Commons puts the file 3 km from the pin, but its name and what it shows fit the 2007 burned mill. The other candidate (Elmdale Mill) is a different, intact building.
- st-marys-waterford: the church is partly blocked by a tree in the front. The file name matches the place exactly and the village is right.
- brownville-historic-district: one brick building in the district (the Masonic lodge), not the whole district.
- fort-plain-village: one brick church in the village, not the canal village as a whole.
- split-rock-furnace: a near view of the main furnace front, not a distant view of the stack.
- elliston-twin-root-cellars: one stone-walled root cellar in Elliston, Newfoundland (Maberly Road). The place is one of a pair of cellars; the picture shows one.
- brandywine-battlefield-park: the Brandywine Baptist Church, inside the park. The marker at the entrance and the Benjamin Ring House (2 km off) were not used.
- bell-inn-dorchester: named as the Bell Inn. Its lower wall is stone, its upper part clapboard with dormers; the register says a one-storey stone house. Name and place fit; the look is not a clean match.
- elmira-railway-station: a grey station building in the PEI Railway Museum. Not certain it is the 1912 station and not the freight shed.
- david-conklin-farmhouse: the white house and barn, 338 m from the pin. A close-up of the Conklin marker was also among the candidates and was not used.

## Places said none, and why

- shelving-rock-knapp-carriage-roads: a fungus and a waterfall.
- peebles-island-bleachery: a cannon and river views; a brick building behind the cannon could not be confirmed as the bleachery.
- cotton-ice-cream-parlor-sand-lake: road views and road signs of the crossroads; none shows the parlour.
- engine-hill: Pittsburgh fire houses (not Schenectady).
- cuba-lake-dam: reservoirs in Cuba the country (not Cuba, New York).
- liberty-theatre-fresno: Hotel Californian and other Fresno buildings; not the Liberty Theatre.
- black-bridge-green-island: a newspaper page from 1862.
- riley-tavern-piseco: a tavern in Texas and a Seattle band.
- hudson-river-mill: parks in Michigan and New York, a parkway sign and an 1800s print.
- crockett-gallant-building-summerside: City Hall and an information centre; not the block.
- white-elephant-saloon-albany: Albany, Texas and Lincoln, New Mexico.
- becker-leicester: Leicester buildings that name only the town; none is identified as Becker.
- montmorency-1856-bridge-towers: a concrete weir and intake at the falls; no bridge towers.
- eglise-sainte-famille-io: interiors, altars, statues, paintings and graveyard views only; no view of the outside.

## Tips

- The first publish stopped because two photo-finder files (`source/tools/photo_find.py` and `source/tools/photo_find_test.py`) changed on `main` after the workspace was set up. The resync ran cleanly, the rebuild passed and the second publish went through. A pictures session started from fresh `main` should not hit this.
- The smoke test (`tools/app_smoke.js`) was not run: it tests the Android app's page at `localhost:8772`, not the built site, and the job says it is not needed for a pictures-only change.
