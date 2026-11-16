# Lost & Hidden Atlas: instructions for AI models

Read `GUIDE.md` before doing anything. The short version:

- **Never push to `main`, and never merge your own pull request.** Merging publishes the site. Put your change on a new branch with `tools/publish.sh`, open a pull request, say what you verified and what you could not, and stop. The owner merges. (GUIDE.md section 3.)
- The files in the repository root (`index.html`, `app.js`, `sw.js`, `data/`, `topo/`) are **build output**. Edit `source/` and rebuild.
- When adding places, follow the research rules in GUIDE.md section 5: every fact from a source you opened, no filling gaps from memory, both versions when sources disagree, access stated, and nothing that tells anyone how to get into a building or past a fence, even if a source does.
- Look at every new pin on the aerial with `tools/pincheck.py` before proposing it.
- A new batch of places is one `data_<area>.py` file with `BATCH`, `PLACES` and `PIN_NOTES`. Never rename a published place `id`.
- Never commit personal information; the repository is public.
- Run `check.py` and the smoke test before opening the pull request.
- The owner uses the Atlas on an Android phone in the field. Test at phone size first.
- Places you read about but could not add go in `LEADS.md`.
