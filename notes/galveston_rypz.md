# galveston_rypz: Galveston, Texas: mansions, cathedral, customhouse, orphans' home, seawall and a gun battery
state: Texas
region: tx
date: 2026-11-23
places: 16
file: data_galveston_rypz.py

## What this batch is
Sixteen places in Galveston (fifteen standing buildings and structures and one World War II gun battery), taken from the names in one walking-tour video about the city's old buildings (the record is `source/videos/20220815_WksFgkilQqg.md`; the video was a tip only, and nothing in the entries comes from it). The Atlas had nothing within 8 km before. Added: the Bishop's Palace, Ashton Villa, the Moody Mansion, the Grand 1894 Opera House, the Galveston Orphans Home (Bryan Museum), the Scottish Rite Cathedral, the 1861 Old Galveston Customhouse, the City National Bank building, the Rosenberg Library, St. Mary Cathedral Basilica, the Ashbel Smith Building (Old Red), Santa Fe Union Station (Galveston Railroad Museum), Old Central High School, the Broadway Cemeteries, the Galveston Seawall and Battery Hoskins of Fort Crockett. Sources: Wikipedia read with `wiki_raw.py` (the Galveston County Register list with `--rows`), the owners' pages with `page.py` and `hours.py page` (Galveston Historical Foundation, Moody Mansion, the Bryan Museum, the railroad museum, the Old Central Cultural Center), a Texas Historical Commission marker text (Santa Fe Union Station), FortWiki and NOAA Fisheries for Battery Hoskins, and the Holy Family Parish Mass page as archived on 2025-10-11. Pins are ArcGIS PointAddress or OpenStreetMap points, all looked at on the aerial; the seawall and battery pins were moved. Not checked: anything on the ground; hours for the Grand (box office) and the Rosenberg Library (its pages are drawn by script); who owns the Broadway Cemeteries and their gate hours (so the entry is view-only); whether the battery pin is on the emplacements (the aerial shows two low terraces, one with a pool, between the resort tower and the boulevard, matching Wikipedia's description, but nothing proves it); Old Central's build date (the centre says 1893, Wikipedia about 1900: both given, conf mixed). `check.py` warns that "Scottish Rite Cathedral" reads as a church: it is a Masonic hall, so `civic` stands.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Galveston City Hall (1916) | Galveston, TX, 823 Rosenberg Avenue (Register point 29.3003, -94.7953) | Wikipedia: C. D. Hill and Company's Italian palazzo city hall, in use since 1916; the 1888 city hall was torn down in 1966 | Not written for lack of time; a source on what is to see and whether the public may walk in |
| Galveston Causeway (1912) | Galveston, TX (Register point 29.2975, -94.8867) | On the Register list and a State Antiquities Landmark | Wikipedia article and what is left of the 1912 causeway beside the newer bridges |
| Galveston US Post Office, Custom House and Courthouse (1937) | Galveston, TX (Register point 29.3022, -94.7958) | On the Register list | Any source opened |
| Garten Verein Pavilion, Grace Episcopal, Trinity Episcopal, Reedy Chapel AME, First Presbyterian, Congregation Beth Jacob | Galveston, TX (points on the Galveston County Register list) | Register listings, several with Wikipedia articles | Not named in the video; not read |
| Falstaff Brewery | Galveston, TX (29.3007, -94.8061) | The Register list says the structure is abandoned | Its article and who owns it now |

## Tips
- In Galveston `geo.py` with ", TX 77550" put every address on the building; the Register point for the Grand 1894 Opera House is about 1 km off.
- `stmcathedral.com`, which a search offers for St. Mary Cathedral Basilica, is St. Mary's in Halifax, Nova Scotia; the Galveston cathedral's Mass times are on `holyfamilygb.com/mass-times`, which did not answer live (the archived copy read).
- `rosenberg-library.org` pages come back nearly empty (drawn by script); no hours found.
- The Texas Historical Commission's `atlas.thc.texas.gov/Details/<number>` pages read with `page.py --all`; the marker text follows "Marker Text".
- 27 names from the video are left "not checked" in the record: mostly bathhouses, schools and hospitals shown in old photographs; whether any of them stands was not looked up.
