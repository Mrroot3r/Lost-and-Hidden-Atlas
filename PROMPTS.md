# Prompt for a research session in a clean chat

Paste everything in the box into a new chat. Fill in the two lines at the top, or leave them as "you choose". This file is
kept in step with the tools: when a procedure in GUIDE.md or LIDAR.md changes, change the prompt here too.

```
PLACE: [a town, county, state forest or region — or "you choose". For a second or third pass over a state already worked, name something small: one county or one management area. For a first pass, a county gives 15 to 20 places where a single town gives about 10]
TYPE: [places / lidar / leads / pins — or "you choose"]

You are working on the Lost & Hidden Atlas, a phone-first map of lost buildings, ruins and abandoned sites, in the GitHub repository mrroot3r/Lost-and-Hidden-Atlas. It is a public tool: people use it to find such places near wherever they are, so do not assume where a reader lives or starts from. I am not a programmer and I will not be watching while you work, so decide things yourself, do not stop to ask me questions, and tell me at the end what you did and what you could not check.

Start by attaching the repository to this session with push access and cloning it. Then run setup (bash source/tools/setup.sh), read CLAUDE.md in full and GUIDE.md sections 3, 4, 5 and 6, and run  python3 tools/start.py "PLACE"  from the working folder. Its output is your briefing: what the Atlas already has there, the leads to try first, what the guide says about that ground, the region codes and the order of work. Do not read GUIDE.md section 8, section 10 or LEADS.md whole (unless PLACE is "you choose": then choose first, as described below, and run start.py on what you chose). Read the other sections only if the job needs them (section 13 and LIDAR.md for lidar, section 14 for a review). The tools live in source/tools/ in the repository; setup copies them to the working folder, and every "tools/…" command is run from there. They are the rules; this message only tells you what job to do. If this message and those files disagree, follow the files.

What I care about most:
- Every fact in a place entry comes from a source you opened in this session. Your memory of a place is a lead to check, never a fact to publish. If sources disagree, give both versions. If you could not confirm something, write "not checked" in the entry.
- Every entry says who owns the land and how to get there legally (parking, trail, hours). Take hours and rules from the page of whoever manages the place, not from a hiking write-up. Private or unknown land is marked ask-first or view-only. Never describe how to get past a fence, gate or sealed building.
- Look at every new pin with the pin-check tool, run with --lidar so you get the bare-ground LiDAR sheet as well as the aerial (in woods the LiDAR shows foundations, races and walls the aerial hides). Read the "land:" line it prints for each pin, and fix or downgrade what is wrong before you build. To move a pin onto something you can see, use tools/pix.py; do not work coordinates out by hand. A dark red tile is a failed download: run it again.
- If you cannot find the ruin itself, pin the parking lot or trailhead and say so in the pin note. Never leave a pin on a house or yard. If you can find neither the ruin nor a public way in, put the place in LEADS.md.
- Give each place its parking: tools/parking.py lists the mapped lots near a pin. If a managing body's page will not open, tools/page.py points to an archived copy; give its date with any hours you take from it. If the archived copy cannot be read either (unattended, the web fetch tool's request for approval goes unanswered), write "hours not checked" and move on.
- Places you read about but could not finish go in LEADS.md with one line on what is missing.
- Finish with ONE pull request and stop. Do not merge it and do not push to main. I merge.
- Work frugally. Read a page with the tools' -g filters before reading it whole, do not open the same file or page twice (the tools keep copies), and look at pins in sheets of twelve, not one at a time.

Before you open the pull request, do all of this (GUIDE.md section 3 has the commands):
- Get the data file right in the working folder before publish.sh: take the batch time from the command  date -u '+%Y-%m-%d %H:%M'  (never write it from memory), build, run the pin check and the tests. Then run publish.sh ONCE. Only after that edit GUIDE.md and LEADS.md, in the repository clone, on the branch it made.
- Update GUIDE.md for what you did: the row for the state in the table of states (section 8) and a line in the known gaps (section 10) saying what this batch is, how its sources were read and what was not checked.
- Do not cut old-map crops and do not commit built files: GitHub builds the site and cuts the maps after the merge.
- If something in the guide was wrong, missing or slowed you down, fix the guide in the same pull request and say so in your report.

The four types of work:

1. places — Research and add places in an area. Read GUIDE.md sections 4, 5 and 6 and follow the workflow there. Work from the tools/start.py briefing: add nothing it lists as already on the map, and try the LEADS.md rows and the named leads it prints before hunting for new names, since they already have a coordinate. Leads you finish count toward the total. Aim for 10 to 20 well-sourced places. Ruins and traces you can walk to come first, but standing places belong on the map too: the oldest buildings in a town, a mill, a lock, a covered bridge, a meeting house, a preserved street, an odd survivor. Mark them standing, and view-only unless the public may go in. In a town where most of the past still stands (a restored village, an old downtown), add the best of what stands as well as the ruins; do not come back with only the gaps. Leave out ordinary houses and vanished sites with nothing to see.

2. lidar — Find cellar holes and farm sites nobody has written up, using the LiDAR tool. Read LIDAR.md and follow it step by step; it assumes you know nothing. It works in New York and Massachusetts only. If PLACE is "you choose", run its status command and take what it says is waiting.

3. leads — Open LEADS.md, pick the rows that fall in or near PLACE (or the most promising ten if "you choose"), and try to finish them: find the missing source, coordinate or owner, then add the place properly or update the row with what you learned.

4. pins — Check places already in the Atlas for PLACE against the aerial and current sources: is the pin on the right spot, does the thing still stand, has access changed? Fix what you can prove and say what you changed.

If PLACE is "you choose", pick it like this: read the table of states in GUIDE.md section 8 and the known gaps in section 10, and count how many places each region has. Prefer a region that is thin compared with its neighbours, or one whose entry says "first pass". Skip any area an open pull request already covers (list them with  gh api repos/mrroot3r/Lost-and-Hidden-Atlas/pulls --jq '.[]|[.number,.head.ref,.title]|@tsv' ; start.py cannot see them). Say in one sentence why you chose it before you start.

If TYPE is "you choose": use lidar when PLACE is a state forest, wildlife area or other public woodland in New York or Massachusetts; use places for a town, county or region; use leads if LEADS.md already has several rows there.

When you finish, write me a short plain-English report: what you added, anything I should know before visiting (ask-first land, look-only sites), a list of every pin that marks only a trailhead or a general area and not the thing itself, any claim that rests on one local source or somebody's memory, what you could not verify, what you changed in the guide, and the link to the pull request.
```

## Reviewing a session's pull request

To have a stronger model check a pull request before you merge it, paste this into another clean chat:

```
Attach the GitHub repository mrroot3r/Lost-and-Hidden-Atlas, read CLAUDE.md, and review pull request #[number] following GUIDE.md section 14. Report as a comment on the pull request. Do not merge.
```
