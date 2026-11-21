# Pictures batch xcze (2026-11-21)

## What this batch is
A scheduled pictures run (job 8). It looked at the first 30 places from `photo_find.py list` that had no picture, and recorded one answer for each in `tools/pics_xcze.py`. No places, pins or text were added.

## Result
- 11 places got a picture: convicts-bread-oven, crown-king-saloon, father-lacombe-chapel, fort-selden-nm, holyoke-canals, lm-cherry-hill, lm-proctors, north-pemberton-station, place-eglise-chateau-richer, praha-painted-church, summerside-city-hall.
- 19 places got none.

## Hesitations
- crown-king-saloon: two candidates carry the name (one 14 m from the pin). Both show a two-storey saloon with a SALOON sign and a balcony, so they look like the same building. Took the one nearer the pin.
- lm-proctors: the picture is the theatre's street front with the marquee, 46 m from the pin. A second named picture shows the same theatre from the street. Took the nearer one.
- praha-painted-church: several candidates show the same church. Took the clear frontal view with the spire (80 m from the pin, the nearest full exterior). Interior views were not used.
- holyoke-canals: many canal views. Took a wide view of the second-level canal with a mill; the place is a system of canals, so any view of them fits.
- father-lacombe-chapel: the chosen picture is black and white, of the small log chapel itself (16 m from the pin). The two colour photographs nearer the pin are of the later brick church next door and were not used.
- american-cemetery-natchitoches: the only candidate that carries the name shows a man standing on a grassy mound as the subject. Set to none under the person rule; the other candidates are downtown street views 137 m away.
- roque-house-natchitoches: candidates are downtown Natchitoches streetscapes and a parade photograph, none of the Roque House 22 miles south. Possibly the pin is far from the house; not checked here.
- tunnicliff-inn-cooperstown: the candidates show the bank next door and the Hall of Fame. None.
- sierra-silver-mine-tour-wallace: the only name-only candidate shows miners at a mine entrance, not the surface building. None.
- powerhouse-park-port-henry: the 212-217 m candidates are a lakeshore and a flower by a wall. None.
- old-military-crossing-cohoes: the nearby pictures are the Cohoes dam and power station, not a crossing site. None.

## Not finished
- Places with no Commons picture within the search radius (none found): windswept-carriage-house-black-point, adirondac, new-manchester-mill, lidar-cook-hill-crossroads-cellar, old-santee-canal-park, dibbles-quarry, benton-stone-water-tower, fisk-quarry-isle-la-motte, old-unadilla-marker-sidney, keillor-house-dorchester, henry-lloyd-manor, bradt-house-rotterdam.
- The first attempt to look at one batch of five timed out and was run again with a longer limit; no place was skipped.

## Tips
- `photo_find.py look` on five places can take more than two minutes when Commons is slow. Running it with a longer timeout, and writing the output to a file, worked.
- `publish.sh` stopped once because main had moved; `resync.sh` kept the pics file and the rebuild passed.
- `tools/app_smoke.js` expects the Android build (its page has a "Start a field log" button), so it cannot be pointed at `dist/web`. This batch changes no app code, so it was not run against the web build.
