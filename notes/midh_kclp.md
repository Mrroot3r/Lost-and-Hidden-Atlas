# midh_kclp: Central Orange County: Montgomery, Walden, Goshen, Vails Gate and Newburgh
state: New York
region: midh
date: 2026-11-19
places: 20
file: data_midh_kclp.py

## What this batch is
Twenty places in central Orange County, New York, the first pass there (region `midh` drawn at random by `choose.py --state ny`, which offered Montgomery; the Atlas had nothing within 20 km of it). Ruins: the Orange Mills gunpowder works in Algonquin Park (Town of Newburgh, roofless stone mill buildings in a county park) and the Colden Mansion ruins at Coldenham (view only from NY 17K; town-owned, a park planned in 2022). Revolutionary sites: Knox's Headquarters with the Ellison mill remains, the New Windsor Cantonment (a reconstruction), the Edmonston House, and Washington's Headquarters in Newburgh (house closed for restoration). Standing: the Nathaniel Hill Brick House and Hill-Hold (county museums), the Bull Stone House and Dutch barn (private, tours by appointment), the Jacob T. Walden Stone House and St. Andrew's church in Walden, the Montgomery Worsted Mills (now City Winery), Montgomery village's two Register districts (area pin), the Harrison Meeting House site and Germantown cemetery, Goshen's 1841 courthouse with Church Park, the Historic Track with the Harness Racing Museum, the Old Stone Schoolhouse (District 9) on Route 17A, Hopewell Presbyterian Church at Thompson Ridge, the Brotherhood Winery cellars and the Moodna Viaduct. Sources: Wikipedia through `wiki_raw.py` (Register list rows and articles), NYS Parks pages, HMdb marker pages and nearby lists, pickocny.com (county tourism), the Times Hudson Valley, The Clio, harnessmuseum.com, brotherhood-winery.com, bullstonehouse.org, thewaldenhouse.org, the Town of New Windsor and Chronogram, all through `page.py`. Not checked: anything on the ground; hours for the Brick House and Hill-Hold (their own and the county's pages answered 403), the Walden House, the Edmonston House, the Old Stone Schoolhouse and City Winery today; whether the Colden park has been built; where exactly the Orange Mills ruins and the Ellison mill ruins are (the Orange Mills pin is an area pin in the park); the Germantown cemetery could not be seen on the aerial. Brick: set from a Wikipedia photograph for the Brick House (red brick) and the Goshen courthouse (yellow stucco, red brick chimneys: some), from Wikipedia's description for St. Andrew's (reddish-brown brick), from sources calling the building stone for the stone houses; left `?` where no picture was settled (Wikimedia refused the Worsted Mills picture twice; Brotherhood's only picture is a sign).

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Maybrook Yard offices | Maybrook, NY (OpenStreetMap ruin lead 41.50056, -74.20408) | Wikipedia (Maybrook Yard): the New Haven's western gateway yard, three miles long after 1912, closed before the Poughkeepsie Bridge burned in 1974; much of it is now a truck terminal; a caboose display in the village | A source for what the mapped ruin is, and who owns it |
| Colden Family Cemetery | Town of Montgomery (HMdb 136094, 41.52188, -74.14710) | Register: burial place of Cadwallader Colden Jr.'s family, about a mile southwest of the mansion ruins | Owner and a public way in |
| Gidney Grist Mill site | Town of Newburgh, Gidney Avenue (HMdb 57429, 41.52510, -74.03412) | State marker: flour mill of the early 1800s, rebuilt 1880 after a fire | Whether anything stands |
| Denniston–Steidle House | New Windsor (Register 41.46194, -74.10649) | Register summary: 1875 farmhouse of unreinforced lime concrete, rare in the region | A second source; private |
| Bodine's Tavern | Town of Montgomery, NY 211 (HMdb 285265, 41.50151, -74.26506) | Register: 1809 turnpike tavern expanded 1835 | Owner and condition; probably private |
| John Tears Inn | Town of Wallkill (HMdb 136700, 41.49935, -74.37294) | Register: 1770s inn on the Goshen Turnpike | Owner and condition |

## Tips
- orangecountygov.com answers HTTP 403 to `page.py` for every page (Algonquin Park, Hill-Hold); pickocny.com (county tourism) reads and gives park hours. hillholdandbrickhouse.org also answers 403.
- `start.py "Montgomery, New York"` geocodes to Montgomery County, not the village in Orange County; give the coordinate (`start.py 41.527,-74.238 20`).
- HMdb nearby lists round Montgomery, Goshen, Maybrook and Walden (3-mile radius) gave positions for most of the batch in four requests.
- The geocoder put "150 Route 17A, Goshen" 4 km away in Florida village; the HMdb marker position was right.
