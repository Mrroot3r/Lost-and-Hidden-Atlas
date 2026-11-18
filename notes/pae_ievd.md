# pae_ievd: Northern Chester County, Pennsylvania
state: Pennsylvania
region: pae
date: 2026-11-18
places: 13
file: data_pae_ievd.py

## What this batch is
The first places in region `pae` (drawn at random with `choose.py`): northern Chester County, the old iron country of the French Creek and Brandywine valleys, with Hopewell Furnace just over the line in Berks County. 13 places: Hopewell Furnace, the Warwick Furnace ruin (Bentley Preserve), Hibernia iron works and mansion, the Continental Powder Works site on French Creek, the Washington Hall hospital ruins at Yellow Springs, the Mill at Anselma, four covered bridges (Rapps, Kennedy, Hall's, Larkin), Uwchlan Meetinghouse, Old St. Mary's Warwick and the Coatesville High Bridge. Wikipedia read with `wiki_raw.py` (the northern, southern and eastern Chester County Register list pages with `--rows`); the NPS Hopewell visitor-center page, anselmamill.org, yellowsprings.org, WeConservePA, TrailLink, ironandsteelheritage.org and a West Chester University park plan PDF read with `page.py`. No Register nomination form was read. Not checked: Hibernia park hours (the county's park page was never found), who manages French Creek Heritage Park and its hours, whether Kennedy and Hall's bridges still carry cars, the interiors of Uwchlan Meetinghouse and St. Mary's, how much of the Warwick stack stands, when Washington Hall fell to ruin. The Warwick Furnace hours come from a WeConservePA report of the 2019 preserve opening, not the trust's own page. Pins for Hibernia (mansion) and the powder works (Rapps Dam Road) do not mark the ruins themselves; St. Mary's and Uwchlan are Register points kept as `site`. Nothing was checked on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Reading Furnace Historic District | Warwick Twp, Chester County, PA (40.14694, -75.76889) | Wikipedia: 1736 furnace foundation and an 18th-century dam remain beside a stone mansion; Washington camped here after Brandywine | Private; whether anything can be seen from a public road |
| Isabella Furnace | West Nantmeal Twp, Chester County, PA (40.11333, -75.82306) | Wikipedia: 1835 furnace, last in the county (out of blast 1894); stack largely demolished, foundations of orehouse and screenhouse remain | Owner and any public view; the Register form |
| Washington's Headquarters (Isaac Potts House) and the rest of Valley Forge | Valley Forge NHP, PA | Region `pae` has nothing at Valley Forge yet; nps.gov has a places page and a Potts House restoration news release | A whole session: NPS hours, which buildings are open during the restoration |
| National Iron & Steel Heritage Museum / Lukens Historic District | Coatesville, PA (39.98111, -75.8225) | steelmuseum.org: open Monday to Saturday 10 to 4; Wikipedia: Lukens NHL district of four properties on South First Street | Which buildings can be entered (tours page says one is under reconstruction); the pin |
| Snyder's Mill ruins and Jacob Rudy's Powder Mill site | French Creek Trail by Rapps Dam Road, East Pikeland Twp, PA (OSM Snyder's Mill 40.13773, -75.55364) | TrailLink names both as reachable from the Rapps Dam Road parking | A source on what they were and how they relate to the Continental Powder Works |

## Tips
- The Pennsylvania leaf-off server is slow: `pincheck.py --lidar` on 13 places with 5 trailheads took about 15 minutes, and the first run fell back to Esri imagery for several tiles before timing out at 10 minutes. Run it in the background from the start.
- Chester County's Register list is split into northern, southern and eastern pages; the plain county title has no rows.
- Chester County Parks pages (Hibernia, Warwick County Park) did not turn up in web search, even with `site:chesco.org`; ironandsteelheritage.org has short pages for most iron sites in the county.
- eastpikeland.org answers 403 to `page.py`; millpictures.com answers 409.
- mychesco.com's park features read like composites (unnamed "visitors" quoted); use them only for what other sources back up.
