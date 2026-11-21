# sch_pxpt: Esperance, Eatons Corners and downtown Schenectady
state: New York
region: mohawk, sch
date: 2026-11-21
places: 10
file: data_sch_pxpt.py

## What this batch is
Ten places on the western edge of region `sch` (drawn at random by `choose.py --state ny`, which offered Esperance) and in downtown Schenectady. Esperance village (Schoharie County, filed under `mohawk` like the Schoharie places): the Esperance Historical Museum in the 1878 village school, the Old Stone Presbyterian Church (1824), the 1868 Methodist Episcopal church, and the Landis Arboretum's Oak Nose Farm (farmhouse and English barn of 1820 or 1830). Burtonville (Montgomery County): Judah Burton's mill site with the town's millstones and the 1834 Burton House (marker pin, area). Duanesburg: the Eatons Corners hamlet (area pin) and the Duanesburg-Florida Baptist Church at Braman Corners. Schenectady: Proctors in full (replaces the thin `lm-proctors` pin with `was=`), the Wedgeway Building (the first Proctor's, 1912–1926, being made into apartments in 2024) and Vale Cemetery (1857). Sources: Wikipedia as raw text (`wiki_raw.py`, including the Schenectady and Schoharie County Register lists), HMdb marker pages, the Esperance town historian's page on theoldstonefort.org, Landis Arboretum pages (timeline, barn history, FAQ for hours), the State Archives photograph record, valecemetery.org (history and contact page for gate hours), the Proctors Collaborative guest page (box office hours) and WAMC, all through `page.py`. No Register form was read. Not checked: any interior except Proctors (from Wikipedia's summary of the Register form); whether the Esperance churches and the Braman Corners Baptist church still hold services (no congregation page was found; hours='?'); the Esperance museum's season for this year (two pages agree on summer weekends 1 to 4, one of them from 2017); whether anything of the Burtonville mill or dam survives; which Eatons Corners house is which; whether the Wedgeway work is finished. Pins were looked at on the leaf-off aerial and LiDAR sheets; the two village churches were moved onto the building beside their markers with `pix.py`. Nothing was checked on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Macomber Stone House | Duanesburg, NY (Register point 42.72139, -74.21444) | Wikipedia: Federal farmhouse of about 1836 in local limestone, five bays, three 19th-century barns; NRHP 1984; private | The Register point is in an open field with no house within 300 m on the aerial (looked at again at 900 m); an address |
| Esperance covered bridge site | Esperance, NY, US 20 at the Schoharie Creek | Town historian (theoldstonefort.org): Theodore Burr's 300-foot two-lane covered toll bridge of 1812 on the Great Western Turnpike, after the 1793 State Bridge washed out in 1798 | Whether any abutment or toll house is left; New York Almanack's 2024 article on the Esperance bridges answers 403 |
| Sherburne Tannery site | Duanesburg, NY, Batter Street near North Road (42.82048, -74.17499) | HMdb 66740: 1932 marker (reported missing) for John Sherburne's tannery of about 1790 | Anything left to see; marker gone |
| Schoharie Creek Preserve | Charleston, NY (lot at 42.81722, -74.26590) | `parking.py`: a mapped lot on the Blue Trail 1.5 km north of Burtonville, on land the federal map lists as Schoharie Creek Preserve | Owner's page, and whether any mill or farm remains are on it |

## Tips
- HMdb nearby lists round Esperance (5 miles) gave every marker in this batch; a short Python regex over `page.py --all` output, between "Inscription." and "Topics", pulls each marker's text and location line in one call.
- The Esperance town historian's page is on the Old Stone Fort's site (`theoldstonefort.org/?p=4690`) and gives the museum's season, address and phone.
- `photo_find.py look` on four places took over two minutes: give it a long timeout (the 2-minute default cut it off once).
- `geo.py` and `start.py` read "Glenville, New York" as Glenville, Connecticut (Greenwich): give Schenectady County's Glenville as a latitude and longitude.
- `unyumc.org` church pages answer 404 (archived copy only); `newyorkalmanack.com` answers 403.
