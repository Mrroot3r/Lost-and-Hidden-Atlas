# dc_xywf: Washington, D.C.: a third scatter, firehouse to pumping station
state: District of Columbia
region: dc
date: 2026-11-23
places: 12
file: data_dc_xywf.py

## What this batch is
A third scatter of 12 places over the District (taken with `choose.py --thinnest`; it had 38): the Adas Israel Synagogue inside the Capital Jewish Museum, the Georgetown Car Barn, Dumbarton House, the Vigilant Firehouse, the Georgetown observatory, the Navy Yard's Latrobe Gate, the Main Pumping Station, Boulder Bridge, the Thomas Law House, Franklin School (Planet Word), the Glenwood cemetery chapel and the Conduit Road Schoolhouse. They were chosen from Wikipedia's Register lists for the District (`wiki_raw.py --rows`) and each place's article, read as raw text; the only managing body's page that opened with hours was the Capital Jewish Museum's. Not checked: hours for Dumbarton House and Planet Word (their sites would not open), Glenwood Cemetery (page had no hours), the Navy's visitor rules (403), what each building is used for today (Vigilant Firehouse, Conduit Road Schoolhouse, Thomas Law House), and the pins beyond the aerial. The Adas Israel pin is a point on a roof placed from the street grid; Franklin School's was moved 13 m off the street. Brick is `?` for most places: no source or picture opened settled it (only the synagogue, from its photograph, and the pumping station, from its article).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Pierce Springhouse and Barn ("Art Barn") | Tilden Street and Beach Drive NW, beside Peirce Mill (38.94, -77.0522) | Wikipedia: springhouse of 1801 in the Tilden Street median, barn built for Isaac Peirce, used as an art gallery in 1971 | Its position apart from the mill, and present use |
| Duncanson-Cranch House, Edward Simon Lewis House | Southwest Waterfront, near 6th and N Streets SW | Register rows of 1973 beside the Thomas Law House | A source on each house |
| Union Station, Howard Theatre, Lincoln Theatre | Northeast and U Street | Register rows | Not read |

## Tips
- Wikipedia's coordinate for the Franklin School fell in the middle of 13th Street; the Adas Israel article has no coordinate (the building was moved in 2019, so the Register row's old position is wrong).
- `photo_find.py look` on a place named in a news event brings back dozens of photographs of the event; the one of the building was candidate 1.
- Dumbarton House's and Planet Word's own sites reset the connection from `page.py`.
