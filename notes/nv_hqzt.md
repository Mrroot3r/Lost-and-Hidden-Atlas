# nv_hqzt: Nevada: depots, stone churches, a Pony Express inn and mining ruins
state: Nevada
region: nv
date: 2026-11-28
places: 11
file: data_nv_hqzt.py

## What this batch is
Eleven places spread over seven counties, taken from National Register listings the Atlas lacked (`tools/gaps.py nv`). Each was read from its Park Service record and nomination form (`tools/form.py`); access and hours come from web search results quoting museum, refuge and county pages, because those pages would not open from the shell. Pins were looked at on the aerial and LiDAR sheet; two were moved (Wabuska depot, Lund school). Not checked: whether anything stands today at Potosi, Bristol Wells or the Hidden Forest Cabin; owners and hours for the Tonopah, Lund, Wadsworth and Austin buildings; interiors. Friday's Station and the Wadsworth church pins are `area`: the Register point fell in an empty meadow and on a bare lot. Pictures: three places have one or an article picture; the rest have none on Commons.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Midas Schoolhouse | Midas, NV (41.24217, -116.79520) | Register-listed 1928 school; Wikipedia says it burned in 2005, Friends of Midas pages say visitors can only look through windows of other buildings | Whether the school stands; not added |
| Tonopah houses and Register district (Brown, Burdick, Curtis, Kendall and others, 82003xxx) | Tonopah, NV (38.065, -117.232) | About 25 listed stone and frame houses, a row house and the power substation | Per-building sources; a walking-tour page would settle them |
| Johnson Lake Mine Historic District | Great Basin National Park, NV (38.94262, -114.29466) | Tungsten mine 1910-1935 with log mill, cabins and tramway above 10,000 ft | NPS access page for the trail and season |
| Walking Box Ranch | Searchlight, NV (35.48884, -115.04071) | 1931-1958 ranch, Register-listed | Owner and whether visitors are allowed |

## Tips
- `form.py` text for newer (post-1990) listings often says "See continuation sheets" near the top; search the saved text in research/forms for built/constructed instead of reading the headings.
- `pincheck.py` shows Register points can be wrong by a block (Lund) or far off (Friday's Station), so check each.
- `smoke.js` (hosted build, `dist/` on port 8766) is the test that fits a places batch; `app_smoke.js` is for the Android build and needs a field-log button.
