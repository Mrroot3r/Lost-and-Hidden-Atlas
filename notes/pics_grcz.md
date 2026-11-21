# Pictures batch grcz (2026-11-21)

## What this batch is

A pictures job (PROMPTS.md job 8), run unattended as a scheduled task. No new places, no pins, no text. It looked at the first 30 places from `photo_find.py list --n 30` that had no picture and chose a photograph from Wikimedia Commons for each one by looking at the candidate sheets. The pull request holds only `tools/pics_grcz.py` and this note.

Result: 9 places got a picture, 21 got none. Every picture's address, credit and licence came from the tool, which reads them from Commons.

Sources read: the candidate sheets (`research/photofind_<id>.jpg`) for every place, each candidate's name, description and distance from the pin as the tool printed them. Wikimedia Commons answered 429 at the start; it was retried after a pause and answered 200 after about four minutes.

## Chosen pictures

- rm-brooks-store-rugby: candidate 2 (roadside view of the store with its false front; "by name" only, Tennessee).
- excelsior-library-guthrie: candidate 1 (brick front with the "EXCELSIOR LIBRARY" sign; "by name" only).
- nine-mens-misery: candidate 1 (the cairn and bronze plaque). Hesitation: the picture is 447 m from the area pin. The cairn is the marked site itself, so it was taken as the place.
- walkers-mill: candidate 1 (white mill building seen across the Brandywine, 37 m from pin).
- waterford-historical-museum: candidate 1, "White Homestead" (by name; its description says it is where the museum is). Hesitation: a second Commons picture, 15 m from the pin, shows what looks like the same white Greek Revival house. Only candidate 1 carries the name, so it was chosen.
- port-henry-dh-depot: candidate 4 (station building from the corner). Candidates 1 to 5 are all 46 m from the pin and show the same station; the clearest, widest view was chosen.
- nazareth-hall: candidate 3 (Nazareth Hall, mansard roof, from the side). Hesitation: all candidates are 163 m from the pin (the tract's centre). The building shown is the large Nazareth Hall, not the Schenk House or a monument.
- livingston-depot: candidate 5 (2025 photograph of the red-brick arcaded depot, 21 m from the pin). The 1894 historic photograph was not used because the depot still stands.
- government-house-pei: candidate 1 (white Georgian front with portico, 50 m from the pin). Several "by name" pictures show the same house from other sides; the one nearest the pin was chosen.

## Places with no picture, and why

- croswell-parsons-paper-mill: the only candidate is a close view of a rubble pile in woods; it does not plainly show a mill. (Close call; the caption names it as the mill ruin.)
- sand-lake-center-for-the-arts: candidates show the post office, a Cumberland Farms, the crossroads and the town sign; none shows the former church.
- bailey-house-brownville, union-church-indian-point, kent-iron-furnace, criddle-vane-homestead, schenectady-central-fire-station, scull-shoals-mill-village, chenango-museum-ward-school-2, webster-road-enfield, fort-griffin-town-flat, first-reformed-church-fishkill, columbia-turnpike-east-gate, piedmont-quarry-winston-salem, cable-building-bay-roberts: nothing on Commons within the search distance.
- fossil-cabin-medicine-bow: candidates show the Virginian Hotel and a yard of tanks; not the cabin.
- canonchet-stable-ruins: the only candidate shows the South County Museum.
- old-mount-ida-cemetery-troy: the only candidate is a close-up of the state marker.
- lambert-street-school-alloway: candidates are street views 182 to 184 m away; none shows the school.
- tivoli-lakes: the only candidate is Empire Plaza, a different place.
- wcsr-remains: candidates are downtown Worcester views and a sidewalk star; no former streetcar building is shown.

## Tips for the next session

- Commons answered 429 at the start of this run. Waiting a few minutes and then retrying worked.
- `photo_find.py look` with five places ran past a two-minute foreground limit in this environment. Running it in the background with output to a file, then reading the file and the sheets, worked well.
- `publish.sh` stopped once because `main` moved. `resync.sh` kept the new pics file, and the rebuild and publish then went through.
