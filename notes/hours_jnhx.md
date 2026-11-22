# hours_jnhx: the daily sample check of November 22, 2026 (one hours row corrected, ten warnings recorded as standing)
state: several
region: several
date: 2026-11-22
places: 0
file: hours_jnhx.py

## What this batch is
A review, not research: the daily sample check (GUIDE.md section 14). No new places, no pins moved, no place text or sources changed. It carries two files: `hours_jnhx.py` (one corrected hours row) and `checked_ok.json` (ten warnings looked at and recorded as standing).

**The hours row corrected.** Old Narragansett Church, Wickford (`old-narragansett-church`, first recorded in `hours_aedp.py`, pull request #358). The row said St. Paul's "often holds its Sunday 9 a.m. Eucharist here in August". The page it cites, St. Paul's "Our campus" page, says the church "is open for docent-led tours during the summer and hosts St. Paul's Saturday evening services in the month of August". The row now says that. No time is given on the page for the tours or the Saturday service. Pull request #358 is left "not double-checked" because its drawn row was wrong.

**Warnings recorded as standing** (each looked at; reasons are in `checked_ok.json`):
- Pins just outside a coarse state outline, each seen on a wide aerial to be on its own side: `hotel-metropole-cincinnati` and `doctors-building-cincinnati` (north of the Ohio River), `nauvoo-historic-district` (east bank of the Mississippi), `gadsbys-tavern-alexandria` (west of the Potomac), `ss-meteor-superior` (the island in Superior Bay), `sault-ste-marie-canal` (north shore of the St. Marys River), `fort-covington-border-station` and `chateaugay-border-station` (on the New York side of the Canadian border; a land line, not a river).
- Kinds: `olana-greenport` (Frederic Church's estate, kind `inst`; the name trips the check because of his surname) and `germantown-parsonage` (a minister's house, kind `landmark`).

## What the sample found
- 58 pins were drawn and looked at on the aerial. 55 passed and their batches are marked "sample-checked".
- Eleven of twelve drawn hours rows were borne out by their pages and those batches are marked. The Charlottetown diocese's table is a PDF whose column headings are lost in plain text; read with its layout kept, All Saints, Cardigan has 9:30 a.m. under Thursday and 10:30 a.m. under Sunday, as recorded.

## Not settled (left "not double-checked")
| Batch | Place | What was seen |
|---|---|---|
| #268 | `old-mulkey-meetinghouse` | Already waiting for a person (issue #347). On a closer aerial the only roof in the clearing is about 17 m south-south-west of the pin; not moved, because the issue is open |
| #392 | `dyea-townsite` | Pin and parking point both under unbroken spruce canopy; the bare-ground LiDAR there is too coarse to show a road or lot. Filed as issue #447 |
| #403 | `rocky-mount-piney-flats` | Marked exact, but the pin is on the large modern museum building; which of the small roofs 40 to 60 m away is the old house could not be told. Filed as issue #448 |
| #358 | `old-narragansett-church` | The hours row corrected above |

## Not checked
- The 25 batches of pictures and the two batches with no places in the working folder (#307, #312) were not part of this check.
- `three-squares-glens-falls` still draws a warning that its name reads as a place you go into (`acc='public'`). It is a downtown historic district, so `public` looks right, but that kind of warning cannot be recorded as standing and the entry was not changed.
- `amsterdam-post-office-murals` passed, but its pin sits on the pavement about 5 m off the west wall of the building rather than on the roof.

## Tips for the next session
- `tools/hours.py page` prints only lines with clock times. For a row with no clock time ("tours in summer", "closed for the season") read the same page with `tools/page.py --all` and search it.
- Running `tools/pincheck.py <id> --lidar` after the main run overwrites `research/pincheck_picked_1.jpg`; look at the sheets first.
