# renss_rgvs: Rensselaer County: the Town of Hoosick, with Glass Lake, Hoags Corners and North Schodack
state: New York
region: renss
date: 2026-11-21
places: 12
file: data_renss_rgvs.py

## What this batch is
Twelve places in Rensselaer County (region `renss`, drawn at random by `choose.py --state ny`). Town of Hoosick, outside what `renss_osux` already had: the 1899 NY 67 bridge at Eagle Bridge, Captain John Potter's tavern at Potter Hill, West Hoosick hamlet, the Wilcox tavern corner at Hoosick, and in Hoosick Falls the Old Maple Grove Cemetery, the Louis Miller Museum, the Cheney Library, and the First Meeting House / Nathaniel Shipman ("Natty Bumppo") burial ground markers; the Brimmer Farm grave of 1755 on Indian Massacre Road. Further south, three leads left by `renss_irek` and `renss_acet`: the Rensselaer Glassworks site at Glass Lake, Hoags Corners (mill hamlet and the 1844 Anti-Rent rally), and the Log Meeting House Cemetery at North Schodack. Sources: HMdb marker pages and nearby lists through `page.py` (mostly the 2025 Hoosick "Eye on History" panels and state markers of the 1930s), the Pomeroy Foundation's Old Maple Grove page, the Hoosick Township Historical Society's home page, the Sand Lake Historical Society's marker page, the FOHBC 2021 glassworks article (PDF), the Rensselaer County GenWeb page on the Particular Baptist Church of Schodack, and one Commons photograph for the Hoag's Tavern marker text. Not checked: nothing was seen on the ground; no opening hours could be read for the museum or the library (`hours='?'`); whether the Eagle Bridge eagles and the Memorial M.E. church with the Pitney mail window survive; which building is Potter's tavern, the Wilcox tavern or Hoag's tavern (pins are the road corners, `prec='area'`); the cemeteries' owners and rules (Log Meeting House is `view`). Red brick is `?` everywhere: no picture opened settled it. Several entries rest on markers alone (`conf='mixed'` where a detail is open). Pins were checked on the leaf-off aerial and LiDAR; one was moved off a building onto Main Street. One picture chosen (Hoosick corner); the rest none.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Captain John Potter monument | Gully by a creek near the NY 7 / NY 22 junction, Hoosick, NY (junction 42.8519, -73.3472) | Potter Hill Eye on History panel (HMdb 290218): three-sided monument to Potter, killed 1806 | Its exact place and whether it is on public ground |
| Tibbits stone schoolhouse | NY 7 and NY 22, Hoosick, NY (42.8519, -73.3472) | Potter Hill panel (HMdb 290218): stone schoolhouse built by the Tibbits family for their tenants' children | Which building, its date, a second source |
| Memorial M.E. church and Pitney mail window | Eagle Bridge, NY | Eagle Bridge panel (HMdb 290171): church formed 1878, cornerstone 1881, stained-glass window about railway mail designed by John H. Pitney | Whether church and window survive; where it is |
| Ball Seminary | Classic Street, Hoosick Falls, NY (HMdb 124805) | State marker: built 1842, given to the town in 1863 for a free union school | Whether the building stands |
| Gilead Lutheran Church | Center Brunswick, NY (marker HMdb 97561 on NY 7 at Mickelhill Road) | State marker: congregation organized about 1746, moved 2.5 miles south to its present site in 1817 | The present church's position, date and page |
| Hoag's Tavern | Hoags Corners, Nassau, NY (42.5564, -73.5112) | Marker seen in a 2010 Commons photo: built about 1820, meeting place of the Anti-Rent War | Which building, whether it stands |
| Smith Boughton (Big Thunder) house | 2093 NY 43, Averill Park, NY (42.59562, -73.50950) | HMdb 315226: Boughton lived here 1838–1888 | Whether his house is the one standing |
| Van Alen Home | 1745 Washington Avenue, Defreestville, NY (HMdb 145274) | 1932 state marker: 400-acre tract bought 1778 by Congressman John Evert Van Alen | Whether the house stands |
| Hoosick Falls Louis Miller Museum hours | 166 Main Street | The society's site gives no hours; a 2014 town item on second-Saturday openings (townofhoosick.org/news2014/013.php) was not read | Current hours |

## Tips
- The Hoosick "Eye on History" panels (2025, HMdb, by the Hoosick Township Historical Society and Hoosick Rising) give a hamlet history each with what still stands; read the whole inscription, `page.py -g` cuts them up.
- cheneylibrary.org is drawn by script and its `?p=` posts answer 404; villageofhoosickfalls.com would not connect; townofhoosick.org/historical.php is 404.
- `photo_find.py` showed a grey tile twice for a by-name candidate with no position (Cheneylibrary.jpg); it may be a file it cannot download.
- Dougtone's 2009–2010 Commons photographs along NY 7 and NY 66 show the text of several markers HMdb lacks (Hoag's Tavern).
