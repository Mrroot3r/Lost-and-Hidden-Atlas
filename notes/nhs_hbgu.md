# nhs_hbgu: Monadnock region: stone arches, covered bridges, meeting houses, a mill village and cellar holes
state: New Hampshire
region: nhs
date: 2026-11-18
places: 19
file: data_nhs_hbgu.py

## What this batch is
First close pass in region `nhs`, drawn at random by `choose.py`: 19 places in Cheshire County (Keene, Swanzey, Winchester, Hinsdale, Westmoreland, Walpole, Gilsum, Harrisville, Jaffrey, Fitzwilliam, Rindge, Stoddard, Sullivan). Ruins and traces: the Otter Brook Preserve cellar hole and 1818 mill site (The Nature Conservancy), the Halfway House hotel site on Mount Monadnock, the McGoldrick dam remnant and canal head-gate in Hinsdale, and the Stoddard glassworks state marker. Standing: the Cheshire Railroad and Gilsum stone arch bridges, four covered bridges (Ashuelot, Coombs, Sawyers Crossing, Carlton), the Park Hill, Fitzwilliam, Rindge and Jaffrey Center meeting houses, the Hinsdale post office, Harrisville mill village, Beaver Mills, the Wyman Tavern and Walpole Academy. Sources were read with `wiki_raw.py` (Register list rows and articles), `page.py` (HMdb markers, NH State Parks, TNC, the Historical Society of Cheshire County, Historic Harrisville, jcvis.org, rs41.org, Waymarking) and web search. Not checked: anything on the ground; opening times of the Park Hill, Rindge and Fitzwilliam buildings and the Hinsdale post office; Walpole Academy's hours come from a Waymarking listing, not the society; whether the covered bridges are open to cars; who owns the Keene section of the rail trail, and parking there. Pins that mark only an area: Otter Brook (TNC's map point; the cellar hole and the Bowlder Road lot were not found) and the Halfway House site (no source coordinate). Red brick: Beaver Mills `yes` and the Wyman Tavern `some` from Wikipedia pictures opened with `brick.py look`; Harrisville `some` from the article (Cheshire Mill No. 2 is red brick); bridges and clapboard meeting houses `no` from the articles; the rest `?`.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Eli Morse Sawmill Foundations | Dublin, NH (42.899167, -72.091944, Register list) | Register 83004056: stone foundations astride a stream near an old logging road south of Old Marlborough Road; walls about 10 and 23 feet (historypointer.com summary) | Owner and any public way in; the nomination form was not read |
| Moore Farm and Twitchell Mill Site | Dublin, NH (42.866111, -72.034444) | Register 83004052 | What is left of the mill, owner, access |
| Mosquitobush mill sites | Harrisville, NH, between Lake Nubanusit and Harrisville Pond | Historic Harrisville bought the seven acres in 2004; woodworking mills ran there until the late 1930s (historicharrisville.org/conservation) | What remains to be seen, a pin, whether it is open to walkers |
| Pisgah State Park sawmill and box-shop sites | Chesterfield/Winchester/Hinsdale, NH | NH Magazine (2018): eight sawmills and four box shops in 1885, a massive stone dam and old graveyards survive in the park | Which dam, where; a source for each site |
| Stoddard Mill Village glassworks site | Stoddard, NH, two miles north of the state marker | HMdb marker 77059 and Wikipedia: the Granite Glass Company works stood at Mill Village from 1846 | Any trace on the ground, owner |
| Troy Railroad Depot | Troy, NH (42.82455, -72.18438, OSM lead) | NH State Parks: limited parking on Water Street next to the depot, on the Cheshire Rail Trail | A source on the building and its date |

## Tips
- NH State Parks' Cheshire Recreational Rail Trail page gives a Troy parking coordinate of 42.724676, -72.184249, which is in Massachusetts; Troy village is near 42.82. Do not copy it.
- The Nature Conservancy's preserve pages read in full with `page.py --all`; the trail map PDF and a directions coordinate (`maps/search/?api=1&query=`) are in the cached HTML in `research/pages/`.
- `parking.py` near the Keene stone arch bridge returned a "lot" that is a point on Marlboro Street; check every lot on the aerial before using it.
- The Historical Society of Cheshire County's "Monadnock Moments" pages (hsccnh.org/education/...) answer 404 and the archived copy needs the web fetch tool.
- `gh api .../pulls` printed nothing at all here too; `start.py` showed 0 open pull requests.
