# Sample check, November 21, 2026

A review, not a research batch: the daily sample check (GUIDE.md section 14). No place was added; no text, id or source was changed.

## What was looked at
- One pin drawn from each of 32 waiting batches, on the aerial (tools/pincheck.py). 28 were on their building, ruin or site and those batches are marked sample-checked.
- One row from each of 9 batches of looked-up hours, read against its page. All 9 pages bore the row out; those batches are marked.

## What was changed
- `garfield-county-courthouse-wa` (#333): the Wikipedia coordinate fell on flat-roofed shops. Moved 70 m east with tools/pix.py onto the dark hipped-roof building behind a lawn on the street, the only courthouse-like building in the tile. Not confirmed from a second source. Batch left unmarked.
- `barratts-chapel-frederica` (#279): the pin was on the parking lot (almost the same point as its parking point). Moved 36 m east with tools/pix.py onto the squarish building against the cemetery, taken to be the chapel. Not confirmed from a second source. Batch left unmarked.
- `tools/checked_ok.json`: two kind warnings recorded as standing, `powers-opera-house-site-lansingburgh` (civic: an opera house for its last forty years) and `fifth-avenue-1819-troy` (landmark: a house; "funeral chapel" is a firm's name).

## Left for a person
- `old-mulkey-meetinghouse` (#268), issue #347: leaf-on aerial, pin on canopy, one small roof 17 m away; could not tell which is the meetinghouse.
- `sage-estate-trails-menands` (#282), issue #348: the parking point is on a narrow paved strip between two houses; could not tell a trail entrance from a driveway.

## Not done
- The nine batches of pictures (#314, #318, #320, #324, #328, #332, #336, #339, #343) that `unchecked.py --sample` now lists were not looked at: this check's instructions cover pins and hours only.
- `check.py` still warns that `three-squares-glens-falls` is `public` though its name mentions a theatre. It is a downtown district of streets and a park, so the warning looks wrong, but it is an access warning, not a kind or state-line one, and was left alone.
- `hinton-historic-district` (#283): the pin is on the station and passed, but pincheck says the entry is `public` on land the public-land map calls private. Access was not this check's to change.
