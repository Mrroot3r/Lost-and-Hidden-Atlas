# nhw_bzpl: North Country New Hampshire: iron furnace, covered bridges, ski jump and old hotels
state: New Hampshire
region: nhw
date: 2026-11-18
places: 20
file: data_nhw_bzpl.py

## What this batch is
First close pass at region `nhw` beyond the two woods ruins already there: 20 places in northern Grafton County (Bath, Woodsville, Haverhill Corner, Littleton, Franconia, Bethlehem) and Coös County (Lancaster, Stark, Berlin, Milan, Crawford Notch, Mount Washington). Ruins and traces: the Franconia stone iron furnace (view only, from the interpretive park; the furnace is on private land), the Bedell Bridge pier and abutments, and the Nansen Ski Jump. Standing: five covered bridges, the Brick Store, Haverhill Corner, the Woodsville Opera Building, Thayer's Hotel, the Littleton Town Building, the Frost Place, The Rocks, the Weeks Estate, Garland Mill (a working water-powered sawmill), the Russian Orthodox church in Berlin, the Tip-Top House and Crawford Depot. Sources were read in this session: Wikipedia with `wiki_raw.py` (including the Grafton and Coös Register lists with `--rows`), HMdb marker pages, NH State Parks pages, the Forest Society, the Frost Place, Northern Woodlands, Yankee and a local radio station through `page.py`. Not checked: anything on the ground; interiors of most standing buildings; hours for the Brick Store (its site would not open), Crawford Depot, the Tip-Top House (the state page gives only the summit building's season), the iron furnace park, Littleton offices and the Berlin church. Brick is `?` for Haverhill Corner, the Frost Place, The Rocks and the Weeks Estate; Woodsville Opera (yes) and the Berlin church (no) were set from the Wikipedia photographs. Pins are on the structures except: the iron furnace (pin on the viewing park across the river; `area`), the Frost Place (geocoder point, house not picked out; `area`), Thayer's Hotel and the Berlin church (`site`), and the Bedell Bridge and Mount Orne bridge, whose real spots lie on the Vermont side of the state outline `check.py` uses, so the pins sit on the New Hampshire bank or approach. Sources disagree on Garland Mill's date (1856 or about 1860) and on the Stark bridge's date and flood year; both versions are given.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| East Branch and Lincoln Logging Railroad Historic District | Lincoln, NH (Register 100012568, address restricted) | Listed 2025; the Lincoln Woods Trail follows part of the grade | The Forest Service closed the Lincoln Woods Trail from June 15, 2026 to January 1, 2027; a source for what is visible and where |
| Willey House site, Crawford Notch State Park | Hart's Location, NH (44.18222, -71.39944, Wikipedia) | The 1826 slide; the site is an interpretive area in the state park (Wikipedia, NH State Parks page) | What is left of the house, if anything; the article did not say |
| Tripoli mill ruins, Little East Pond Trail | Livermore, NH | Wikipedia (Livermore article): diatomaceous-earth mill ruins a short way into the woods off the old railroad grade the trail follows | A coordinate and a second source |
| Mount Jasper Lithic Source | Berlin, NH (44.485556, -71.194444, Register list) | A prehistoric stone quarry on the Register | Access (city land? trail?) and what can be seen |
| Gale River CCC camp | Bethlehem/Franconia, NH (44.26784, -71.61758, federal names file) | Named in the vanished-places layer | Any source for remains |

## Tips
- The White Mountain National Forest road status page (`fs.usda.gov/r09/whitemountain/alerts/forest-roads-status`) reads cleanly with `page.py` and lists every forest road open or closed with a date; Sawyer River Road (the way to Livermore) has been closed to vehicles since a December 2023 washout.
- NH State Parks addresses are now `nhstateparks.org/find-parks-trails/<name>` (Mount Washington is `mt-washington-state-park`); the older `/visit/state-parks/...` form answers 404 except for Weeks State Park.
- `check.py`'s state outline puts the whole Connecticut River in Vermont at Bedell Bridge and the Mount Orne bridge, although the legal line is the Vermont low-water mark; a New Hampshire place on that river needs its pin on the New Hampshire bank.
- `whitemountainhistory.org` (Google Sites) reads in full with `page.py --all` and has a page on each abandoned logging town.
- `gh api .../pulls` printed nothing at all in this session (not even an empty list); `start.py` showed 0 open pull requests.
