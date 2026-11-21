# wny_rdxr: Chautauqua County, NY: Westfield, Mayville, Chautauqua, Lily Dale, Dunkirk and Jamestown
state: New York
region: wny
date: 2026-11-21
places: 19
file: data_wny_rdxr.py

## What this batch is
Nineteen places in Chautauqua County, drawn at random by `choose.py --state ny` (region `wny`, which offered Jamestown); the Atlas had no place within 40 km of Jamestown or Westfield. Almost all standing: the Barcelona and Dunkirk (Point Gratiot) lighthouses, the Busti and Fay-Usborne mills, Welch Factory No. 1, the Jamestown Erie, Mayville Pennsylvania and Westfield Lake Shore stations, Midway trolley park, the Chautauqua Institution, Point Chautauqua and Lily Dale (area pins), the Fenton Mansion, the Rorig truss bridge, the Brocton Arch, the Holland Land Company vault in Mayville, the 1869 skew arch at Silver Creek, the Clymer District No. 5 school and the Yorker Museum at Sherman. Sources: Wikipedia as raw text (`wiki_raw.py`, the county Register list with `--rows`), HMdb nearby lists round five towns, historypointer.com for Register addresses, and with `page.py` the pages of NY State Parks, chq.org, the Fenton History Center, dunkirklighthouse.com, the Village of Sherman, the Post-Journal, the Villager, WRFA and the county tourism office. Every NPGallery form tried (six) was the placeholder. Hours from the managing body's own page for Barcelona, Dunkirk, Midway, Chautauqua, Fenton and the Yorker Museum; Busti Mill's from the county tourism listing and the Mayville Depot Museum's from the Villager (both said so in the entry); Lily Dale's season from the Post-Journal. Red brick from Wikipedia/Commons photographs opened with `brick.py look` and `photo_find.py`. Not checked: anything on the ground; whether the Rorig Bridge is still open (OpenStreetMap shows no bridge between the two halves of South Water Street, and the aerial shows only trees); the present use of Welch Factory No. 1 (a Commons photo shows broken windows), the Fay-Usborne Mill and the Clymer school; whether the Holland Land vault still stands as more than its marker (an HMdb photo caption says so); the Clymer school's exact building (area pin on the road); Busti Mill's exact building (pin on a building by the Lawson Road bridge); the Westfield freight depot's position (Wikipedia calls it co-located but puts it 550 m away); Lily Dale off-season access.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Jamestown Armory | Jamestown, NY (42.0931, -79.255) | 1932 Tudor Revival armory by William Haugaard, Register 1995 (Wikipedia; 34 Porter Avenue, historypointer) | Present use and owner; whether anything can be seen beyond the street front |
| Lewis Miller Cottage | Chautauqua Institution, NY (42.210416, -79.464718, HMdb 117533) | National Historic Landmark inside the Institution grounds (Register list) | Folded into the district entry; a page saying whether it is ever shown |
| Celoron Park | Celoron, NY (42.10972, -79.28611, vanished-places layer) | A vanished amusement park on the federal names file | Any source on what is left; none read |
| Walnut Grove Archaeological Site | Jamestown, NY (42.09117, -79.23853, OpenStreetMap lead) | Mapped as an archaeological site beside the Fenton Mansion | A source saying the public may visit and what can be seen |
| Dunkirk Schooner Site | Dunkirk, NY (Register 09000285, address restricted) | Register-listed wreck | Public position and access; probably dive-only |
| Center and Pearl Streets Historic District | Forestville, NY (Register 100012812) | Listed recently; no coordinates on the list | A source and a position |

## Tips
- Chautauqua County Register forms on NPGallery are all the placeholder; historypointer.com gives each listing's street address in one line (`page.py --all`, second line), but it put the Jamestown Armory in "Albany".
- An HMdb nearby list with a 5-mile radius round Westfield, Mayville, Jamestown, Dunkirk and Chautauqua gave almost every marker in the county in five requests (grep the cached pages for `m.asp?m=`).
- `photo_find.py new` said three places whose Wikipedia articles have a photograph had "no picture the Atlas may show" (the Jamestown, Mayville and Westfield stations, whose articles were reached through a redirect); `look` then found good Commons pictures for all three.
- The Busti Historical Society and the Chautauqua Town Historical Society seem to have no web pages of their own; their hours come only from the county tourism office and local papers.
- publish.sh stopped twice in five minutes because picture and data batches were merging; resync.sh, a new batch time and a rebuild each time took about four minutes.
