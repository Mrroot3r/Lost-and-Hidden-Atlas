# alb_inbox_ugzq: Albany: two buildings readers marked
state: New York
region: alb
date: 2026-11-21
places: 2
file: data_alb_inbox_ugzq.py

## What this batch is
The daily inbox run of November 21, 2026: three marks readers sent through the form on November 20 and 21, all in Albany round the west end of Washington Park. Two are added with `tip=`: the Woman's Club of Albany at 725 Madison Avenue (the 1895 Joseph Steefel house, by Nolan, Nolan and Stern; the club's own history page, read whole with `page.py --all`, and Wikipedia's Washington Park Historic District article with `wiki_raw.py`), and the former Albany High School on Western Avenue at North Lake Avenue, now the University at Albany's engineering building (the university's May 2024 news release, read whole, and its facilities project page, node 98251; the older facilities address is 404). The reader's "School" point fell on the federal names file's "Philip Schuyler Elementary School" vanished-place lead, which is this same building, still standing. Both pins are on OpenStreetMap buildings checked on the leaf-off aerial; the school's was moved 31 m onto the roof with `pix.py`. Not checked: brick (no picture opened plainly shows either building; `photo_find.py` found none, so both are `brick='?'`), either interior beyond what the university's release describes, whether the club ever opens its house to visitors, and which of the club's neighbours is Barnard Steefel's twin (OpenStreetMap names 727 as the Albany Friends Meeting House).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Reader's tip: "Red brick house" | Albany, NY (42.65789, -73.77781), south side of Madison Avenue just west of South Lake Avenue, between 710 and 718 Madison | Sent November 21, 2026 through the form, marked "Ruins"; the point is on an unaddressed OpenStreetMap building, a house on the leaf-off aerial. No source opened names it | A source naming the house and why it matters (the Washington Park Historic District nomination, if it covers the south side, or Historic Albany Foundation); whether it is a ruin at all |

## Tips
- For a bare reader's mark in a city, `osmnear.py <lat> <lon> 60 buildings` named two of three buildings at once (OpenStreetMap carries old names, `old_name=Albany High School`).
- `start.py`'s vanished-places list can hold a building that still stands under another use: "Philip Schuyler Elementary School" in the federal names file is the 1913 Albany High School building.
- `photo_find.py` on Madison Avenue and Western Avenue in Albany offered only one Mapillary driver's street views; none showed either building plainly.
