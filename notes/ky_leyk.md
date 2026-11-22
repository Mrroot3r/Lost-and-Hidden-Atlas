# ky_leyk: Kentucky: old downtown Louisville, the Water Tower and Churchill Downs
state: Kentucky
region: ky
date: 2026-11-22
places: 15
file: data_ky_leyk.py

## What this batch is
A "videos" batch (job 9): the names came from one video's tour of old Louisville (the record is `source/videos/20230703_o0OVZh9H_JM.md`, 52 names). Fifteen standing places were added: City Hall, the Louisville Trust Building, the Cathedral of the Assumption, the Seelbach and Brown hotels, the Louisville Palace (Loew's), the Carnegie main library, the Gene Snyder Courthouse, Louisville Gardens (the 1905 armory), Union Station, St. Boniface and St. Joseph (Butchertown) churches, the Water Tower and pumping station, Churchill Downs with its twin spires, and Cherokee Park. Sources read: Wikipedia with `wiki_raw.py`, the Kentucky Historical Society's marker pages (City Hall, St. Joseph, St. Boniface), the 1977 Register form for the Louisville Trust Building (NPGallery text), Louisville Public Media (June 2025) on Louisville Gardens, and for hours the pages of Louisville Water, the Kentucky Derby Museum and St. Boniface parish. Not checked: hours for the cathedral, St. Joseph, the main library and the Palace (their own pages and the archdiocese's refused the reader), whether the public may go into City Hall, Union Station and the federal courthouse, present use of the Louisville Trust Building, downtown parking, and red brick on most places (left `?`). Pins are ArcGIS address points looked at on the aerial; St. Boniface is `site` because the point falls by the street front rather than on the church roof. No interior was visited by any source read unless the entry says so.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Masonic Widows and Orphans Home (1927 campus) | Louisville, KY, Frankfort Avenue (Wikipedia point 38.25444, -85.6675) | Wikipedia: home moved to a 176-acre campus in 1927 and most of its buildings still stand; it now takes any senior citizen | An owner page for visiting rules and which building to pin |
| Walnut Street Theater | Louisville, KY (Register list point 38.251111, -85.758611) | On the downtown Register list (78001370) | Not read; check whether it stands |
| "Theater Building" on Fourth Street | Louisville, KY (Register list point 38.247778, -85.757778, 82002726) | On the downtown Register list; may be the Mary Anderson Theatre the video names | The Register form, to name it |
| Chestnut Street Methodist Church | Louisville, KY (Register list point 38.25, -85.765278) | On the downtown Register list (79001000) | Not read |

## Tips
- archlou.org (every parish page and the Louisville Mass schedule), cathedraloftheassumption.org and lfpl.org answer HTTP 403 to `page.py`; search results for Mass times lead only to directories. St. Boniface's own site (`stbonifaceparish.com`) reads cleanly.
- Louisville Water's visit page (`louisvillewater.com/louisville-water-tower/visit-us/`) reads in full with `page.py --all`; the older `louisvillewater.com/waterworks-museum/` address is 404.
- The Kentucky Derby Museum's hours are on `derbymuseum.org/visit-guide`; `plan-a-visit` holds only menu text.
- The downtown Louisville Register list is "National Register of Historic Places listings in Downtown Louisville, Kentucky"; Union Station and the Water Tower are not on it.
