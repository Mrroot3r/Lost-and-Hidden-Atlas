# Pictures run, November 23, 2026 (pics_yhnx)
tidied: 2026-11-26

Scheduled pictures job (job 8). About 30 places were meant to get a look. The run reached 40 minutes after 20 places had been looked at by eye, and the last round was cut short by a background timeout, so it stopped there.

- Pictures chosen: 15 (ashokan-overlook, mount-beacon-fire-tower, binghamton-dlw-station, baker-city-hall-or, altamont-maple-avenue, laurel-dale-cemetery-rugby, fitzgerald-bottling-works-troy, charlottetown-cnr-station, lockport-locks-raceway, great-swamp-fight-monument, coldbrook-springs, historic-speedwell, white-horse-inn-chatsworth, lake-katharine-reynolda, minnewaska-hotels).
- Said none after looking: 5 (sixteen-to-one-mine-alleghany, st-laurent-shrine, hewetts-lock-halfmoon, coketon-coke-ovens-thomas, montague-railway-station).
- Recorded none by the tool itself: 14 (pioneer-oil-museum-bolivar, lidar-chapel-road-field-corner-pit, cupids-cove-plantation, hugh-moore-park-lehigh-canal, lidar-reit-road-walled-yard, lidar-coye-hill-road-house-site, doukhobor-dugout-house, international-paper-office-corinth, yeo-house-green-park, bishops-machine-shop-summerside, caroga-museum, genesee-valley-canal-oakland-locks, maynard-school-bovina, yorker-museum-sherman).

Places where I hesitated:
- ashokan-overlook: the chosen picture is the reservoir with the Burroughs Range, 116 m from the pin. The drowned hamlets are under the water, so this shows the site as it stands now, not a building.
- altamont-maple-avenue: chosen the Pangburn Building (completed 1886, built by the drug store owner after the fire); it is 229 m from the pin and not on the burned Lockwood block itself. Other candidates were a station and a house.
- charlottetown-cnr-station: the name matches exactly, but the marker says Island sandstone and the photograph's stone looks brick-like. Chosen on the name.
- fitzgerald-bottling-works-troy: the uploader was unsure what the building across from St Peter's Church is. Chosen as the nearest plausible red brick building; the place's full description was not read in this run, so a person may want to check it against the bottling works.
- laurel-dale-cemetery-rugby: chosen from the name (the file is in Rugby, Tennessee, the same colony), 858 m away; it shows a single cross monument in a cemetery.
- historic-speedwell: chosen the stone dam and building in Speedwell Park (named in the file, no position); the ironworks ruins are not clearly visible in it.
- coldbrook-springs: chosen the village marker (46 m from the pin); it names the village but is a memorial, not a building.
- lockport-locks-raceway: chosen Lockport 3 (the locks with the bridge), 10 m from the pin, over the other locks shown.
- lake-katharine-reynolda: chosen a 1919 photograph of the boathouse on the lake; the lake is now a wetland, so the picture is historic.
- minnewaska-hotels: chosen a wide view of the Cliff House ruins (a colour transparency from the Library of Congress set). The Wildmere site is not shown.
- sixteen-to-one-mine-alleghany: the only candidates were three aerial tiles of forest; none.
- montague-railway-station: the candidates showed the harbour, a bridge, and a painting of a waiting room; none shows the station site.

Checks: the workspace site was built (tools/all.sh) and the picture test (tools/photo_find_test.py) passed. The phone-size smoke test (tools/app_smoke.js) passed on a web folder built with android-app/scripts/make-www.js from the clone's main build; it was not run on the workspace build. The pull request was not merged by this session. Not checked: how the pictures look on a phone.

Tips for the next session:
- On this machine `python3` lacked `requests`. /usr/bin/python3 has requests and PIL, and tools/all.sh works when a python3 shim pointing at it comes first on PATH.
- tools/app_smoke.js expects the Android web folder (android-app/www), not dist/web; the first run against dist/web failed on the field-log checks for that reason.
- One `next 5` round took about 10 minutes when Commons was slow; a background command with a 600-second limit was cut off mid-list. Run the rounds in the background with a longer limit.
