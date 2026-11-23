# mb_pdbq: Manitoba: third scatter
state: Manitoba
region: mb
date: 2026-11-23
places: 15
file: data_mb_pdbq.py

## What this batch is
Fifteen places across Manitoba (37 before, 52 after): Winnipeg (Ross House, the Forks lift bridge, Johnston Terminal), Camp Hughes near Carberry, the Brandon House No. 1 site, Asessippi townsite, the Sargenia Terraces, Arnold Cement Quarry, Emerson's first customs office, the Pointe du Bois and Slave Falls power stations, the Grand Rapids Tramway, Port Nelson, and at Churchill the HMCS Churchill station and the Sayisi Dene village. Each rests on its Manitoba Historical Society page (read with page.py; coordinates are theirs), plus the Province's heritage page, Parks Canada and the Town of Carberry for Camp Hughes, and Manitoba Parks' guide for Asessippi. Pins were looked at on the aerial and moved nowhere; Arnold, Grand Rapids and Sayisi Dene are `area`. Not checked: owners and parking for most places (several marked ask-first or view-only for that reason), hours for Ross House and Johnston Terminal (`hours='?'`), whether the Grand Rapids tramcars and rails survive where the Historical Society put them, and anything on the ground. No Manitoba public-land layer exists, so the pin check's "not on mapped public land" lines mean nothing here. Brick is `?` unless the Historical Society's text says: Slave Falls has a small brick tramway station (`some`).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Valley River Suspension Bridge | RM of Dauphin (51.24270, -100.09844) | Removed in 2017; concrete abutments of a c.1920 bridge remain (MHS) | Nothing left worth a pin |
| Dauphin CNR engine house and turntable | Jackson Street, Dauphin (51.15381, -100.06224) | 1906, still standing in 2021 photographs (MHS) | Owner, access, history beyond one line |
| Transcona Cordite Plant | Transcona, Winnipeg (49.89394, -96.92578) | MHS page long but not read in full | What survives and where |
| Pine Falls Paper Mill | Pine Falls (50.56854, -96.22705) | MHS page read only in part | Current state |
| Manitoba House | Kinosota (50.92929, -98.86517) | 1810s-1911 post; only a degraded 1970s replica seen in 2018 | A source that shows anything old |
| Kanuchuan Generating Station | northern Manitoba (54.36022, -94.84307) | 1934-35, powerhouse intact in 2001/2022 (MHS) | Any way a visitor can reach it |
| Trump Oil Refinery | Trump, RM of Morris (49.40298, -97.36811) | 1934 farmers' refinery (MHS) | What stands |

## Tips
- The Historical Society's pages end in "Site Coordinates (lat/long): N.., W.." and `grep -o` on the saved text pulls them out for a dozen pages at once; `page.py <url> --all -n 6000` mistakes `-n` for an address, so give the address first and filter the output with head.
- `photo_find.py look` finds nothing on Commons for most small Manitoba sites; only the Forks, Camp Hughes, Johnston Terminal and Pointe du Bois had pictures.
- The Ross House operator's own page (sevenoakshouse.ca) answered 404 to page.py; a web search gave only directory hours.
