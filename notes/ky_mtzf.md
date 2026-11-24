# ky_mtzf: Kentucky: a second statewide scatter
state: Kentucky
region: ky
date: 2026-11-24
places: 10
file: data_ky_mtzf.py

## What this batch is
Ten places across Kentucky, where earlier batches sit round Harrodsburg, Danville, Frankfort and Louisville: the Roebling bridge and the Cathedral Basilica in Covington, Waveland (Lexington), Fort Duffield (West Point), the Lincoln Birthplace Memorial Building (Hodgenville), Wickliffe Mounds (far west), Blue Heron mining camp (McCreary County), Nada Tunnel (Powell County), Pine Mountain Settlement School (Harlan County) and the Mayo Mansion (Paintsville). Facts come from Wikipedia (`wiki_raw.py`, raw text), NPS pages, fortduffield.com, covcathedral.com and pinemountainsettlementschool.com (`page.py`). Not checked: interiors, parking at most places, the school and tunnel on the ground. Kentucky State Parks pages (parks.ky.gov and its static mirror) answered 404 or 403, so Waveland and Wickliffe have `hours='?'` and the access note says so; search listings gave tour times for both but are not a source. Blue Heron's Wikipedia point fell in woods 200 m east of the camp; the OpenStreetMap point named for it is on the depot and store frames, and a mapped lot by the tipple bridge is its parking. Nada Tunnel's pin is on its road, `prec='site'`. Two pictures came from Commons (Roebling, Wickliffe); the other eight have Wikipedia pictures.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Old Taylor Distillery (Castle & Key) | Millville, Woodford County KY | A castle-style distillery; no Wikipedia article under that title | A source read and a pin |
| Lynch coal town and Portal 31 mine tour | Lynch, Harlan County KY (36.965, -82.917) | Wikipedia: planned 1917 by U.S. Coal and Coke as a company town, 10,000 people by the 1940s | Which standing buildings and tour hours, from a page of its own |
| Shelbyville historic district | Shelbyville, Shelby County KY (38.211, -85.221) | `start.py`: 6 listed places, 3 districts, 205 buildings, no Atlas place | Register entries read and a best building chosen |
| Paducah Market House | Paducah KY | No Wikipedia article under that title | The right title or an operator page |

## Tips
- `https://www.nps.gov/biso/...` pages for Blue Heron 404 on guessed names; `home.nps.gov/biso/learn/historyculture/blueheron.htm` reads cleanly with `page.py --all`.
- `wiki_raw.py` leaves raw wikitext in `research/wikiraw/`; a few lines of Python to strip `<ref>` and `{{...}}` made it readable.
- Kentucky State Parks pages cannot be read by `page.py` (404 on the guessed address, 403 on the static mirror); a session that needs their hours will have to use another route.
- A Wikipedia point for a mining camp can sit in woods: check `osmnear.py ... buildings` for a mapped building of the same name.
