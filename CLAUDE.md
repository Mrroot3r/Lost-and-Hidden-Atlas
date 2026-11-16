# Lost & Hidden Atlas: instructions for AI models

Read `GUIDE.md` before doing anything. The short version:

- **Never push to `main`, and never merge your own pull request.** Merging publishes the site. Put your change on a new branch with `tools/publish.sh`, open a pull request, say what you verified and what you could not, and stop. The owner merges. (GUIDE.md section 3.)
- The files in the repository root (`index.html`, `app.js`, `sw.js`, `data/`, `topo/`) are **build output**. Edit `source/` and rebuild.
- When adding places, follow the research rules in GUIDE.md section 5: every fact from a source you opened, no filling gaps from memory, both versions when sources disagree, and legal access detail stated (owner, parking, trail, hours). The one thing left out is how to get past a barrier into somewhere closed.
- Look at every new pin on the aerial with `tools/pincheck.py` before proposing it.
- Every US state, the District of Columbia and the ten Canadian provinces already have an outline, a region, a start city and map coverage (`tools/states.py`, `tools/outlines.py`), and 40 states and 7 provinces have one worked example each in `tools/data_states.py`. To work in any of them you only add a batch of places: one `data_<area>.py` file with `BATCH`, `PLACES` and `PIN_NOTES`. Never rename a published place `id`.
- Old rail, trolley and canal lines and the leads layer exist for New York and Massachusetts only. To add them for another state follow GUIDE.md section 8, "Lines and leads for a new state" (`tools/osm_layers.py`, `tools/ohm_state.py`, then `lines.py` and `leads.py`).
- Never commit personal information; the repository is public.
- Run `check.py` and the smoke test before opening the pull request.
- If `git push` is refused, attach the repository to the session with push access, then push again (GUIDE.md section 3). Do not retry or look for another login.
- A state's trespass-law note is optional and done only when the owner asks. The access line on each place is not optional.
- The owner uses the Atlas on an Android phone in the field. Test at phone size first.
- Places you read about but could not add go in `LEADS.md`.
- Places found on LiDAR that nobody has written up go in the `lidar` category as unverified leads, with a parcel check for every one (GUIDE.md section 13). Never write a private landowner's name or address into the repository.
- Asked to review a pull request? Follow GUIDE.md section 14: `tools/review.py`, open the sources, look at the pins, report as a comment, do not merge.
- The Android app is in `android-app/` (GUIDE.md section 12). It runs the same `source/src/app.js`. You cannot run it on a phone from here: after any change to the field log, data loading or the app's Java, run `tools/app_smoke.js`, and say in the pull request what only the owner can test. Never commit a signing key.
