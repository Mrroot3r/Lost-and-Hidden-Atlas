# ms_rkvq: Mississippi: Jackson, Vicksburg, Natchez, Biloxi and more
state: Mississippi
region: ms
date: 2026-11-24
places: 8
file: data_ms_rkvq.py

## What this batch is
Eight places in Mississippi, claimed with `choose.py --thinnest` (52 places before, 60 after): the King Edward Hotel in Jackson, McRaven House in Vicksburg, Rosalie in Natchez, the Magnolia Hotel in Biloxi, the Old Fort House in Columbus, the old water and electric plant in Holly Springs, Brookhaven's Union Station and Brandon Hall at Washington. It is a short batch: the session read Wikipedia articles and National Register lists as raw text, one official page for Rowan Oak (dropped, already on the map) and the Natchez Pilgrimage page, and ran short on sources that say what survives. Not checked: interiors, ownership of the private houses, and hours for all eight (all `?`); McRaven's own page could not be read (search listings disagree). Parking was not looked up (no `th=`). Pins: five from the ArcGIS address lookup, two moved on the aerial, the Holly Springs plant is `area` because the building could not be told from its neighbours. Pictures: all eight have a Wikipedia article picture. Red brick: Brandon Hall `some` from the article, the King Edward and Magnolia Hotel `no` (beige brick; plastered wood), the rest `?` (Rosalie and Brookhaven are brick, colour not seen).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Old Noxubee County Jail of 1870 and the older jail | Macon, MS (33.1006, -88.5597; 33.1061, -88.5606) | Two National Register jail listings in the county list | A source that says what stands and who runs it |
| Monroe County Jail (Athens Jail) | Athens, MS (33.8714, -88.4425) | National Register listing | A source for its history and access |
| Old Tishomingo County Courthouse | Iuka, MS (34.8092, -88.1897) | National Register listing | The Wikipedia title was not found; a Register form or the town's page |
| Saenger Theatre | Hattiesburg, MS (31.3256, -89.2903) | National Register listing, Art Deco, c. 1929 | Article title not found; hours and history |
| Mobile and Ohio Railroad Depot | Aberdeen, MS (33.8261, -88.5514) | National Register listing | Article title not found |
| Casey Jones Railroad Museum State Park | Vaughan, MS | A state park; the depot was moved from Pickens | Coordinates, hours and a park page |
| Ricks Memorial Library | Yazoo City, MS (32.8486, -90.4119) | National Register listing | Source text |

## Tips
- Wikipedia titles for Mississippi Register listings often do not match the list's names (the Old Capitol is "Old Mississippi State Capitol"); the Register list rows show `article:` only for some.
- Check `grep -l <id> tools/data_*.py` for an id before writing it: Rowan Oak and the Old Capitol were already on the map under other batches and were found only at build.
- The ArcGIS address lookup put pins on the right building where the Wikipedia point was off by 50 m or more (McRaven, King Edward, Brookhaven).
- `page.py --all` on rowanoak.com gave the full hours sentence; the default filtered view cut it at the first full stop.
