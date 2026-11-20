# renss_irek: Rensselaer County: Rensselaer city, Schodack, Nassau, Sand Lake and Stephentown
state: New York
region: renss
date: 2026-11-19
places: 16
file: data_renss_irek.py

## What this batch is
Sixteen places in southern and central Rensselaer County (region `renss`, drawn at random by `choose.py`), the ground the earlier `renss_osux` batch left: the City of Rensselaer, North Greenbush, Schodack, Nassau, Sand Lake, Poestenkill and Stephentown. City of Rensselaer: Crailo State Historic Site (a full entry that replaces the thin pin `lm-fort-crailo` with `was=`), the Aiken House, the Patroon Agent's House and Office, Beverwyck Manor and the W. P. Irwin Bank Building. North Greenbush: the DeFreest Homestead and Dutch barn. Schodack: District School No. 3 at Castleton, Muitzes Kill hamlet with the 1876 Reformed Church, and Schodack Landing (both area pins). Nassau village (Church Street, Chatham Street Row and the Academy, one area pin). Sand Lake: the 1805 Sand Lake Baptist Church, the former Presbyterian church that is now the Sand Lake Center for the Arts, the Faith Mills buildings on Burden Lake Road (now Arts Letters & Numbers) and the Fox Mansion. Stephentown Heritage Center (1871 Methodist church, open Fridays). The one ruin: the stonework of an unfinished mill at the foot of Barberville Falls (Rensselaer Plateau Alliance preserve). Sources: Wikipedia as raw text (`wiki_raw.py`, `--rows` for the county Register list), and through `page.py` the NYS Parks Crailo page, HMdb nearby lists and marker pages, the Sand Lake Historical Society marker and Faith Mills pages, the Town of Stephentown history page (Heritage Center hours), the Rensselaer Land Trust waterfall page and the Arts Letters & Numbers contact page. Every pin was looked at on the leaf-off aerial and LiDAR; Crailo, the Aiken House, the DeFreest house and Schodack Landing were moved. Red brick from Wikipedia photographs for the Irwin bank (yes), the Patroon Agent's House (some: the house is painted, the office wing bare) and District School No. 3 (painted, so no); the Aiken House picture was refused twice by Wikimedia and stays `'?'`. Not checked: anything on the ground; the mill remains at Muitzes Kill (Wikipedia says one can be seen; not located); the unfinished mill at Barberville (not seen on aerial or LiDAR; pin is the falls); Barberville's hours (the Alliance's pages answer 404; Wikipedia says dawn to dusk, an older Land Trust page says closed Memorial Day to Labor Day, both given); Beverwyck's present use and whether it can be seen from a road; the Sand Lake Baptist Church's and the Reformed churches' service times; the Sand Lake Center for the Arts' schedule; which house is the Fox Mansion (pin on the road beside it); the adult fee at Crailo.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Joachim Staats House and Gerrit Staats ruin | Papscanee Island, Schodack, NY (Wikipedia 42.57083, -73.74944) | Wikipedia: 1696 stone house, Staats family owned; the 1758 Gerrit Staats house burned in 1973 and nothing of it is visible | Whether the house can be seen from a public road or the county's Papscanee Island preserve |
| Evangelical Lutheran Church of West Berlin | Dutch Church Road at Bly Hollow Road, Berlin, NY (HMdb 135102, 42.65568, -73.40684) | HMdb has the marker but no inscription text | A source on the church's date and what stands |
| Glass Lake: Rensselaer Glass Factory village | Glass Lake, Sand Lake, NY (HMdb 65615, 42.63019, -73.53146) | Sand Lake Historical Society marker: glassworks and a village of 34 workers' houses, 1804–1852 | Whether anything of the works can be seen; owner of the shore |
| Hoags Corners mill hamlet | Hoags Corners, Nassau, NY (HMdb 135113, 42.5564, -73.5112) | State marker: many water-powered mills in the 1800s | Any mill ruin or building that can be seen |
| Arlington Hotel (Elkhorn) | West Sand Lake, NY (HMdb 284354, 42.64562, -73.59467) | Marker: stop 22 on the Troy & New England trolley, 1895–1925 | Whether the building stands and its use |
| Fred's Falls mill | Cropseyville, Brunswick, NY | Rensselaer Land Trust: a mill that still stands beside the falls on the Quacken Kill, with some original works inside; private | A coordinate, the owner, whether it can be seen from a road |
| Sharpe Homestead, Van Alen House, Elmbrook Farm, Blink Bonnie, John Carner Jr. House | Defreestville, Schodack and East Greenbush, NY (Register list points) | Wikipedia: farmhouses of about 1740 to 1850, all private | Whether each is worth a pin and can be seen from the road |

## Tips
- `start.py "Nassau, New York"` geocodes to Nassau County on Long Island; give a latitude and longitude for the Rensselaer County town.
- The Rensselaer Plateau Alliance's pages (`rensselaerplateau.org/barbervillefalls`, `/get-outside`) answer 404 and `/parking` is drawn by script; the site's title is now "Hudson Taconic Lands". No working page for Barberville's rules was found.
- The Sand Lake Historical Society's marker page (`sandlakehistory.org/historical-markers/index.html`) gives the full text of every town marker; `page.py -g` cuts it to fragments, so strip the tags from the cached copy in `research/pages/`.
- The Town of Stephentown's history page (`townofstephentown.org/history`) gives the Heritage Center's hours; `stephentown.gov/history/` returns the same page without them in what `-g` kept.
- NPGallery has only placeholders for the Muitzes Kill, Schodack Landing, Nassau Church Street and DeFreest forms (74001297, 77000976, 78001901, 77000978).
