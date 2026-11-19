# nyc_faqy: North Shore of Nassau County & Fort Totten
state: New York
region: nyc
date: 2026-11-19
places: 17
file: data_nyc_faqy.py

## What this batch is
Seventeen places on the North Shore of Nassau County, with two just over the line in Queens, drawn at random by `choose.py --state ny` (region `nyc`, which offered Roslyn); `start.py` found no Atlas place within 20 km of Roslyn. Ruins: the Knollwood estate ruins (King Zog's mansion) in Muttontown Preserve, and the unfinished granite fort at Fort Totten. Standing: the Roslyn Grist Mill (under restoration), Roslyn's Main Street with the 1895 clock tower (one area pin), Cedarmere, Trinity Church Roslyn, the Mackay (Harbor Hill) water tower, the Saddle Rock tide mill, Castle Gould and Hempstead House at Sands Point Preserve, Raynham Hall, the Oyster Bay depot and turntable, the Planting Fields Main House, Sagamore Hill, the Matinecock (1725) and Jericho (1788) Friends meeting houses, Westbury House at Old Westbury Gardens, and the 1964 New York State Pavilion. Facts from Wikipedia (`wiki_raw.py`, the town Register lists with `--rows`), Nassau County's Muttontown and Saddle Rock pages, the Roslyn Landmark Society, the Friends of Cedarmere, the Sands Point Preserve Conservancy, Raynham Hall Museum, the Planting Fields Foundation and NYS Parks, NPS (Sagamore Hill), Old Westbury Gardens, NYC Parks and Long Island Press / Herald articles. Every pin was looked at on the aerial and LiDAR sheets; two were moved with `pix.py` (the Pavilion onto the Tent of Tomorrow, the Sagamore Hill lot point onto the lot). Not checked: anything on the ground; hours for Muttontown Preserve, Fort Totten Park, Flushing Meadows, the Oyster Bay Railroad Museum (its site answers 403; Wikipedia's "weekends April to November" is used), Saddle Rock, Trinity Church and both meeting houses; whether the New York State Pavilion towers reopened when the restoration was due to end in October 2026; the exact spot of the Knollwood staircase (the pin is on the OSM ruin point, where the LiDAR shows a terraced platform); who owns the ground at the Mackay water tower; the Fort Totten pin's land (the federal map calls it Coast Guard land, NYC Parks runs tours of the fortress). Red brick is `?` for nine places: no source or picture opened said.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Falaise (Harry Guggenheim house) | Sands Point Preserve, Sands Point, NY | Shown on guided tours only (Sands Point Preserve Conservancy hours page) | Its own source for dates and fabric; the Wikipedia title "Falaise (Sands Point, New York)" redirects to Hempstead House |
| Execution Rocks and Stepping Stones lights | Long Island Sound off Port Washington and Kings Point, NY (40.878056, -73.738056; 40.824167, -73.775) | Both on the Register (Wikipedia list of North Hempstead) | Access by boat only; a source for what can be seen and from where |
| Christeen, oyster sloop (1883) | Oyster Bay WaterFront Center, NY (40.87774, -73.5397) | Oldest oyster sloop in the US, NHL 1992, restored 1999, sails from the WaterFront Center (Wikipedia) | The WaterFront Center's own page for sailings and where to see her |
| Mackay Estate Gate Lodge and Dairyman's Cottage | East Hills, NY (40.793056, -73.641667; 40.800556, -73.625556) | The other two Harbor Hill survivors (Roslyn Landmark Society) | Whether they can be seen from a public road; both likely private houses |
| Walled Garden, Muttontown Preserve | Muttontown, NY (OSM ruin lead 40.82762, -73.53612) | OSM maps it 250 m north of the Knollwood ruin point; the county page says the Hammond parcel holds traces of the pre-Revolutionary Duryea farm | A source tying the walled garden to Knollwood or to the Duryea farm |
| Huguenot Yacht Club ruins | New Rochelle, NY (OSM lead 40.87757, -73.76264) | OSM ruin lead seen in the Roslyn briefing | Westchester, so region midh, not nyc; no source opened |

## Tips
- `wiki_raw.py --rows` needs the Register sub-list's exact title: in Nassau County they are "... in North Hempstead (town), New York" and "... in Oyster Bay (town), New York" (grep the county list's raw text for "National Register of Historic Places listings in" to get them).
- The Register point for the Oyster Bay LIRR depot (40.8869, -73.5286) is 1.3 km off; `nom.py "Oyster Bay Railroad Museum"` gives the depot and the turntable yard.
- obrm.org answers 403 to `page.py`; NYC Parks' fort-totten-park/history page and Nassau County's Cedarmere page gave 500 and 404. Old Westbury Gardens' /visit is drawn by script, but `oldwestburygardens.org/?p=4879` reads in full; the Sands Point Preserve hours are at `sandspointpreserveconservancy.org/?p=6519`.
- The federal land map puts the Fort Totten water battery inside a Coast Guard station while NYC Parks tours it: say so in the access note.
