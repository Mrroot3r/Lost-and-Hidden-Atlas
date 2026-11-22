# Pictures batch sgsk (2026-11-22)

## What this batch is

A pictures job (PROMPTS.md job 8): 19 places already on the map that had no picture. No new places, pins or text.
Three rounds of `photo_find.py next 5` were run, and each sheet was looked at before choosing. The run stopped at about 40 minutes, so about 30 places were not reached; the remaining places in the queue still wait.

## Counts

- Pictures chosen by looking: 6 (Most Holy Trinity church, Sleeping Giant quarry, Annapolis County Court House, Old Chain of Rocks Bridge, Duffields Depot, Vischer Ferry Lock 19).
- Said none by looking: 5 (Chester train station, Christ Episcopal Belvidere, Flynn's Lock Halfmoon, Idaho City Pioneer Cemetery, Kapa'eleele Koa Kahana).
- Recorded none by the tool itself (Commons has nothing for them): 8 (Batchellerville, Farmington Canal aqueduct, Hawley Middle Road cellar, Moss Street School, Repose of the Fallen, Sackville station, Voorheesville depot, Woodson suspension bridge).

## Where I hesitated

- Vischer Ferry Lock 19: the candidate is a view of the preserved Erie Canal channel, not the lock itself. Chosen because the canal section is the thing the pin marks.
- Old Chain of Rocks Bridge: the chosen picture is taken from the bridge deck, looking at the truss. It names the bridge and carries the Missouri name in its file, but the bridge crosses into Illinois; the description fits.
- Sleeping Giant quarry: the chosen picture is a stone structure with arched openings in the quarry area, with the caption naming the quarried area. Likely the crusher remains, not confirmed on the sheet.
- Pioneer Cemetery, Idaho City: candidates were single grave plots or a sign in the cemetery, all close-ups. None chosen, though a fenced grave plot was closest.
- Kapa'eleele Koa Kahana: the candidates are a park sign, a mountain ridge and geckos; none shows the sites.
- Christ Episcopal, Belvidere: the candidates are Christ Episcopal churches in Louisiana, Mississippi and Chicago. None chosen.
- Chester station: the only candidate is a 1925 Pennsylvania station clipping. None chosen.

## Not checked

- The rest of the queue (about 1000 places in all states) was not reached.
- The app smoke test (`tools/app_smoke.js`) was run against a local server of the build and failed at a field-log button; this pull request changes only `tools/pics_sgsk.py`, and the failure was not investigated further.

## Tips for the next session

- A `next 5` call that Commons answers slowly can run past ten minutes in the foreground and be cut off; the sheets and the record still get written. Run it with its output in a file and check the file afterwards.
