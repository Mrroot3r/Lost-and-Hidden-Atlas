# Session notes

One file for each batch of places, named after its batch key (`notes/<batch key>.md`). A research session writes its
note here and nowhere else: it does not edit `GUIDE.md`, `LEADS.md` or `PROMPTS.md`. Several sessions often run at the
same time, and when each added its lines to the same spots in those files, every pull request after the first had to be
untangled by hand. A file of one's own cannot collide.

`python3 tools/note.py <batch key> <clone>` makes the file (so does `publish.sh`, for a new batch). It has three parts:

- **What this batch is**: what was added, how the sources were read, and what was not checked.
- **Leads**: places read about and not finished, as table rows in the same four columns as `LEADS.md`.
- **Tips**: anything about a tool, a source or the guide that the next session should know.

`tools/start.py` reads every note: for a piece of ground it prints the leads that fall there, what earlier sessions
wrote about that state, and their tips.

**The tidy job.** `start.py` prints at most fourteen tips, the newest first, so a tip in an old note is soon never read
again. From time to time one session, working alone and asked for by name (the prompt is in `PROMPTS.md`), runs
`python3 tools/tidy.py <clone>` and follows its steps: the lead rows move into `LEADS.md`; each tip worth keeping is
written into `GUIDE.md` (section 16, by state; or the table of sites that will not open in section 3) or fixed in the tool
it was about; the table in `GUIDE.md` section 8 is brought up to date; and the tips are then taken out of the notes.
A tidied note has a `tidied:` line at its head, an empty leads table and a line where its tips were. "What this batch is"
stays for good: it is the record of the batch, and `start.py` shows it to the next session in that state.

Batches added before November 18, 2026 have no note: their lines are in `GUIDE.md` sections 8 and 10 and in `LEADS.md`.
