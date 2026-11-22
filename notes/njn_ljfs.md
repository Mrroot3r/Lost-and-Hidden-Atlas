# njn_ljfs: Newark, New Jersey: cathedral, courthouse, theatres and the old downtown
state: New Jersey
region: njn
date: 2026-11-22
places: 17
file: data_njn_ljfs.py

## What this batch is
Seventeen standing buildings in Newark, the first places the Atlas has there, taken from the names in one video walk-through of the city (Old World Exploration, "Old World Newark New Jersey", 2025; the record is `source/videos/20251003_BcPu5HuXDj4.md`). The video was a tip only. Added: the Cathedral Basilica of the Sacred Heart, the Essex County Courthouse, the Hall of Records, City Hall, the Main Library, the American Insurance Company Building, the Krueger-Scott Mansion, First Baptist Peddie Memorial Church, the surviving front of South Park Presbyterian Church, Symphony Hall (Salaam Temple), Proctor's Palace and the Adams Theatre (both closed), the Essex Club (New Jersey Historical Society), the Bamberger's store (165 Halsey Street), the Central King Building (old Central High School), Broad Street station and the old Tiffany & Company silver works. Sources: Wikipedia with `wiki_raw.py`, the Essex County Register list (`--rows`), the Register form for the Mutual Benefit building, New Jersey Historic Trust pages, the library's Knowing Newark articles, Cinema Treasures, Jersey Digs, NewarkHistory.com, and the own pages of the cathedral, the library and the Historical Society (`page.py`). Pins are ArcGIS address points or OpenStreetMap buildings, every one looked at on the 2020 aerial; four were moved. Hours were read for the cathedral, the library (its page shows summer hours only) and the Historical Society; no own page with service times was found for Peddie Church, and Symphony Hall's box-office hours came only from a travel site, so both are `hours='?'`. Not checked: whether the public may walk into the courthouse rotunda, City Hall or the Krueger-Scott Mansion; parking for any of them; red brick for Proctor's, the Adams and the Central King Building. The Adams Theatre's state (lobby a shop, auditorium abandoned) rests on Cinema Treasures alone, and the Proctor's apartment plan on one undated Jersey Digs article.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Mutual Benefit Life building (later Essex Catholic High School) | 300 Broadway, Newark, NJ (Register 40.761111, -74.169444) | Completed April 1927 (Knowing Newark, 1999); on the Register (83004031), limestone fronts on Broadway and Second Avenue, buff brick elsewhere (the form); Essex Catholic until 1979 (Wikipedia) | A recent source saying it still stands and what it is used for |
| Wickliffe Presbyterian Church front | 111 13th Avenue, Newark, NJ (Register 40.738611, -74.184722) | Wikipedia: the 1889 church by William Halsey Wood was demolished for the University Heights Houses and only a front with two placards remains | A second source and a look at the spot |
| Paramount Theatre | Market Street, Newark, NJ | Jersey Digs: the auditorium, dating from 1886, collapsed | What is left of the front and when it collapsed |

## Tips
- The ArcGIS point for 465 Dr. Martin Luther King Jr. Boulevard (the Hall of Records) lands about 140 m west of the building, and for 1035 Broad Street (South Park Presbyterian) on the lawn of Lincoln Park; `nom.py` and `osmnear.py ... buildings -g` had both by name.
- `photo_find.py new` outruns a two-minute command and `look` on five places took about fifteen minutes: run both in the background.
- Newark's own Register list title ("National Register of Historic Places listings in Newark, New Jersey") does not exist; the Essex County list holds every Newark row.
