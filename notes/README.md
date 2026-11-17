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
wrote about that state, and their tips. From time to time the tips that have proved true are folded into `GUIDE.md` and
the leads into `LEADS.md` by one session working alone, and those lines are then taken out of the notes.

Batches added before November 18, 2026 have no note: their lines are in `GUIDE.md` sections 8 and 10 and in `LEADS.md`.
