# md_vdxv: Frederick County, Maryland: furnace, covered bridges, canal and battlefield
state: Maryland
region: md
date: 2026-11-18
places: 16
file: data_md_vdxv.py

## What this batch is
Sixteen places in Frederick County, Maryland, plus the Washington Monument just over the line in Washington County: the Catoctin Furnace stack, the Camp Misty Mount WPA cabins, the Roddy Road, Loys Station and Utica covered bridges, Graceham Moravian church, Schifferstadt, the Hessian Barracks, Rose Hill Manor, the Thomas Farm and Gambrill Mill at Monocacy battlefield, the Monocacy Aqueduct, the Point of Rocks station, St. Paul's at Point of Rocks, Gathland, and the Washington Monument. Wikipedia was read with `wiki_raw.py` (the county's Register list with `--rows`); Maryland DNR park pages (`dnr.maryland.gov/publiclands/Pages/western/...`), NPS pages for Catoctin Mountain Park, Monocacy and the C&O Canal, the Frederick County Landmarks Foundation visit page, the C&O Canal Trust parking page and one HMdb marker were read with `page.py`. Not checked: anything on the ground; hours for Rose Hill Manor (the county's recreater.com page answered 404 or reset), Loys Station Park, the C&O Canal at Monocacy, Hessian Barracks and the two churches; whether the Roddy Road and Utica bridges still carry cars; the parking at the Thomas Farm (no lot mapped). Pins moved from the Wikipedia coordinate onto OpenStreetMap features or with `pix.py` for the furnace, Roddy Road and Utica bridges, Schifferstadt, St. Paul's, Gathland arch and the Washington Monument; the Catoctin furnace stack and the Roddy Road bridge could not be made out for certain on the aerial (prec site). Sources disagree on the Monocacy Aqueduct's length (438 ft Wikipedia, 516 ft NPS), the Loys Station bridge's date (1848 vs about 1880) and Isabella furnace's date (1853 to 1867); both are given. Brick: four settled from pictures opened with `brick.py look`, three left '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Lewis Mill Complex | Jefferson, MD (39.372222, -77.559444) | Early 19th-century three-storey brick grist mill with the remains of an earlier race, a pottery shop since 1980 (Wikipedia) | Whether it is still a business open to visitors; owner and parking |
| Victor Cullen School Power House | Sabillasville, MD (39.7144, -77.4619) | On the National Register list for the county | Any source on what stands and whether the campus can be visited |
| Bowlus Mill House / Shafer's Mill | Spoolsville (39.4556, -77.5596) / Middletown (39.411111, -77.565), MD | Register list rows only | An opened source and the owner; probably private, view only |
| Brunswick B&O station | Brunswick, MD (39.31194, -77.62722) | 1891 Baldwin depot, frame on stone walls, still a MARC stop (Wikipedia) | Brick not settled; the Brunswick museum's hours (the C&O compendium points to brunswickmuseum.org) |
| Lock 28 and the Point of Rocks canal | Point of Rocks, MD (lot 39.27328, -77.54073) | C&O Canal lot mapped by parking.py | A source for the lock and what is left |

## Tips
- Maryland DNR park pages read well with `page.py`, at `dnr.maryland.gov/publiclands/Pages/western/<name>.aspx`; the guessed name is often wrong (Cunningham Falls is `Cunningham.aspx`, not `cunninghamfalls.aspx`); search the web for the exact address. Their history subpages (`.../CunninghamFalls/Catoctin-Furnace.aspx`, `.../Washington/History-Washington.aspx`) are the best source on what is left.
- Frederick County Parks and Recreation (`recreater.com`) pages answered 404 or a connection reset; the archived copies could not be read unattended.
- Several Wikipedia coordinates in Frederick County sat 50 to 550 m off the building (Catoctin Furnace's falls in woods south of the furnace); `osmnear.py <lat> <lon> 600 buildings -g '<name>'` found the right building every time.
- NPS Monocacy pages are at `nps.gov/mono/learn/historyculture/<name>.htm` with an underscore (`thomas_farm.htm`, `gambrill_mill.htm`).
