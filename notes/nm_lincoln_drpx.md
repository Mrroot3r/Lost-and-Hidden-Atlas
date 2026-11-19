# nm_lincoln_drpx: New Mexico: Lincoln, Fort Stanton and White Oaks
state: New Mexico
region: nm
date: 2026-11-19
places: 15
file: data_nm_lincoln_drpx.py

## What this batch is
Fifteen standing places in Lincoln County, New Mexico, the first batch there: four in Lincoln (old courthouse, Tunstall store, Torreon, San Juan church), Fort Stanton, four in the gold camp of White Oaks (Hoyle House, schoolhouse museum, Cedarvale Cemetery, No Scum Allowed Saloon), the Jicarilla log schoolhouse, Monjeau Lookout, the Old Dowlin Mill in Ruidoso, the Carrizozo Woman's Club, Paden's Drug Store in Carrizozo and the Hurd house at San Patricio. Facts are from the National Register forms (NPGallery `_text`, read with `page.py`), Wikipedia (`wiki_raw.py`), HMdb marker pages (texts and positions), fortstanton.org, the Lincoln National Forest page for Monjeau, and a few secondary pages named in each entry. Not checked: nothing on the ground; Lincoln Historic Site's hours and fees from the state's own page (it would not open; hours are from Clio and an archived Los Alamos Daily Post notice, and they disagree on the opening time); the White Oaks schoolhouse museum's hours and who runs it; Cedarvale Cemetery's owner; the Hurd gallery's hours; whether Paden's and the Dowlin Mill are open inside. Red brick: no source opened gave a colour, so the brick buildings (Hoyle House, White Oaks school, the saloon, Paden's) are '?'; Hoyle House is stone in the 1970 nomination and brick in Legends of America (both given, conf='mixed'). The Jicarilla Schoolhouse pin is the Register coordinate, in a clearing by the road where no building could be seen on the aerial (prec='area'). Fort Stanton and the Dowlin Mill pins were moved (see PIN_NOTES).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Ancho Brick Plant and depot | Ancho, NM (33.9372, -105.7412, Wikipedia town point) | Wikipedia: brick plant from about 1901, 16 kilns, closed 1921; the school and depot restored by residents | Wikipedia says most of the land and buildings are private and not open; a source for what stands and a public view point |
| Exchange Bank shell | White Oaks, NM | The 1970 nomination names the shell of the Exchange Bank among the surviving buildings | A position and a current picture |
| Brown Store building | White Oaks, NM | 1893, later school, dance hall and offices (Legends of America); stone sides, brick front replaced by tin (New Mexico Ghost Towns) | A position and owner |
| Fort Stanton Cemetery and Merchant Marine cemetery | Fort Stanton, NM (33.48748, -105.52557, OpenStreetMap) | HMdb lists an "American Merchant Marine Monuments" marker (m=102809) | Who runs it, access, and a source for its history |
| El Paso and Southwestern Railway water supply system | near Nogal, NM (Register 79001540, no coordinates) | Listed on the National Register | The form (not opened) and a public way to see any of it |

## Tips
- nmhistoricsites.org (New Mexico Historic Sites) returns the same 3,525-character generic text to `page.py` for every address tried (`/lincoln`, `/fort-stanton`, `/lincoln/plan`, `/fort-stanton/plan`); Fort Stanton's hours came from fortstanton.org/information instead, which reads cleanly.
- The Monjeau Lookout Register form (87002483) is a scan with NO TEXT LAYER.
- The National Register list coordinate for the Old Dowlin Mill is on Sudderth Drive about 280 m east of the mill; OpenStreetMap's "Old Mill" point and the ArcGIS geocoder's point address for 641 Sudderth agree with each other.
- `publish.sh` stopped once because another batch merged while this session worked; `resync.sh` then a rebuild fixed it, as the guide says.
