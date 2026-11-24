# lacrosse_dcyv: La Crosse, Wisconsin: churches, breweries and downtown blocks
state: Wisconsin
region: wi
date: 2026-11-24
places: 15
file: data_lacrosse_dcyv.py

## What this batch is
Fifteen standing places in the city of La Crosse, taken as leads from the names in one Old World Exploration video (the record is `source/videos/20251226_RHorO5frMnw.md`) and each checked in sources: seven churches and church buildings (St. James and St. Clara's Convent, Christ Episcopal, Mary of the Angels Chapel, First Methodist/Wesley, Emmanuel Lutheran, First Evangelical Lutheran), two downtown blocks (McMillan, Solberg), Oak Grove Cemetery and the Losey Memorial Arch, Main Hall of the old normal school, the Gund bottling works, the old stone section of the Heileman brewery and the Exchange State Bank on Rose Street. Facts come from the Wisconsin Historical Society's property records (`page.py --all` on `wisconsinhistory.org/Records/Property/HI...`, which read in full), Wikipedia raw text and the La Crosse County Register rows, the La Crosse Public Library Archives' architecture blog, the Oak Grove Cemetery's tour page, WIZM news, and the pages of the Franciscan Sisters (chapel hours) and Christ Episcopal (service time). Pins are address points or OpenStreetMap points, each looked at on the aerial. Not checked: service times of St. James, Wesley and the two Lutheran churches (no page of their own was read; `hours='?'`), who now uses the First Evangelical Lutheran building, the Oak Grove visiting hours, parking for any place (the lots mapped near the cemetery, chapel and campus are permit lots), and how much of the Masonic part of the Exchange State Bank still stands. Red brick for six places is from Commons photographs or the state records' wall material; the rest are `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Salzer Memorial Methodist Church | 525 Seventh Street South, La Crosse, WI | On the city's local register (2006); the library archives say German Baptists bought "the Old Salzer Methodist Church" here in 1949 | A building date, and to settle a library record that says a fire destroyed the Salzer church before the 1945 merger |
| William W. Cargill House | La Crosse, WI | On the Register list (74002337) with no coordinate or description | Whether it still stands (the list row is blank) |
| Gund brewery office and malt house | 2104 and 2111 South Avenue, La Crosse, WI | Named as related Gund buildings in the state record for the racking house (1827 Sims Place) | Their own records and pictures; the racking house itself could be its own entry |

## Tips
- The Wisconsin Historical Society property records (`page.py --all -n 60000`) give year built, wall material, "Demolished" yes or no, and a long description: they settled most of this batch, including that the Michel brewery was torn down.
- The ArcGIS geocoder returned the same point for "400 West Ave N" and "400 West Ave S" in La Crosse, about 800 m from the church: the picture finder's Commons photos, placed far from the pin, gave the mistake away.
- `photo_find.py` found Michael Barera's August 2026 La Crosse photographs for downtown and campus buildings; they are worth checking for any later La Crosse batch.
