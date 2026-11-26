# Pictures batch thyb (2026-11-22)
tidied: 2026-11-26

## What this batch is

A pictures job (PROMPTS.md job 8): photographs for places already on the map that had none, chosen by looking at the candidate sheets from `tools/photo_find.py next 5`. No new places, no pins, no text about places. The choices are in `tools/pics_thyb.py`: 8 places got a picture, 6 got none chosen by looking, and 2 had nothing on Commons and were recorded as none by the tool. Every picture's address, credit and licence come from Wikimedia Commons through the tool.

Three rounds of five were looked at before the session stopped at its 40-minute limit. The third round's command ran out of time partway, but each place it had written was kept.

## Places that got a picture

Waterport trestle piers and bridge walls (Carlton), Glenaladale House (Tracadie Cross), Burke ghost town (the Hecla mine buildings), Fort Cobun (the earthworks), Poestenkill Gorge mill ruins (the falls), Whitesbog Village (the general store), Moffett Mill (Lincoln), Wasioja Seminary ruins.

## Places that got none

Miller, Hall & Hartwell collar factory (Troy): only a Cornell postcard. Hotel Balmoral (Wilton): a Bowmanville postcard, an Edinburgh hotel and a switch engine. Prospect Mountain incline (Lake George): a lake view only. Cedarvale Cemetery (White Oaks): a Bay City, Texas cemetery. Split Rock Park WPA structures (Garretson): nearby scenery and a different railroad bridge. Erie Canal Lock One (Albany): Albany river views and HABS photos of Lock 18 in Cohoes, a different lock.

Recorded as none by the tool itself: Barkhamsted Lighthouse village, Griffin ghost town.

## Hesitations

- Waterport: the candidates are mostly fishermen at the dam. The chosen view (Carlton, 60 m from the pin) shows large stone blocks in the river beside the falls, which may be the old bridge walls; people are incidental. A reviewer should check it against the pin.
- Fort Cobun: the candidate that names the place is 18 km from the pin, so it is marked LOOK TWICE. It shows an earthwork ridge, matching the description; the 30 m candidate showed only trees and lawn.
- Poestenkill Gorge: the picture is the falls in the gorge. The mill ruins are not clearly visible; it was chosen as the gorge the ruins stand in.
- Burke: the chosen Hecla mine picture is a name match, not at the pin; it shows red brick ruins above the canyon, which fits the description.
- Glenaladale: the chosen view names the house and is about 400 m from the pin, the nearest candidate that shows the whole house; a reviewer may want a closer one.

## Tips for the next session

Each `next 5` command can take more than two minutes when Commons is slow. Run it in the background with output to a file and poll it, rather than in the foreground, so a timeout does not cut a round short.
