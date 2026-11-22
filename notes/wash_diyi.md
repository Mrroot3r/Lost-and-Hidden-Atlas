# wash_diyi: Washington County, NY: Whitehall, Fort Ann, Kingsbury, Argyle and Battenville
state: New York
region: wash
date: 2026-11-21
places: 13
file: data_wash_diyi.py

## What this batch is
Thirteen places in western and northern Washington County (region `wash`, drawn at random by `choose.py --state ny`), taken from the county's Register list and the state and town markers that the Atlas still lacked: in Whitehall the Skenesborough Museum (1917 Barge Canal terminal), the 1913 fire station that horses hauled to Main Street in 1932, and the 1937–38 post office with Axel Horn's mural; the 1935–36 Hudson Falls post office with George Picken's murals; the Wing-Northup House in Fort Edward (Washington County Historical Society, Tuesday and Wednesday hours from its own page); three Kingsbury burying grounds (Moss Street, Kingsbury, Patten's Mills); the 1870 stone arch bridge at the Kilmer Mill site in Argyle; the Fort Anne wayside with the Battle Hill tablet; the Stoops Hotel with the Thomas McLean House at Battenville; and two eighteenth-century brick houses, the DeRidder Homestead in Easton (c. 1735) and the Alexander McNish House in Salem (c. 1794). Sources: Wikipedia read with `wiki_raw.py`, HMdb marker pages (an HMdb nearby list round five points, 250 markers), the NPGallery text of the Whitehall Fire Station and Moss Street Cemetery nominations, the historical society's house page, the Skenesborough Museum friends' page (its hours are 2021's, and the site says it does not speak for the museum), the Glens Falls Business Journal's 2020 article on the Anthony house, and OpenStreetMap or the ArcGIS geocoder for building points. Not checked: anything on the ground; post office hours (`hours='?'`); who owns the three cemeteries and the Fort Anne wayside; parking everywhere except as noted; interiors. The Kingsbury Cemetery pin fell on US 4 at the Kingsbury Road junction and is an area pin. The Kingsbury Cemetery's first year is given both ways (1788 on the Pomeroy marker, 1777 in the Moss Street nomination). Whether the "former tavern" the state agreed to buy in 2020 beside the Anthony house is the Stoops Hotel is not confirmed, though the federal land map puts the Stoops pin inside the state's unit. The DeRidder pin is Wikipedia's point, on a farmhouse in fields, not confirmed as the right house. Brick: the two post offices (Wikipedia: red brick) and the fire station (nomination and a Commons photo) are `yes`; the museum (concrete) and the stone bridge `no`; the rest `?`. Pictures: two found (fire station, Moss Street gate), eleven none.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Former D&H shops and boiler house, Whitehall | Whitehall, NY (OpenStreetMap ruin, building marked abandoned, 43.54494, -73.40582) | Mapped in OpenStreetMap only; Wikipedia's Whitehall station article covers the 1850 and 1892–93 stations, not the shops | Any written source for the shops, their dates and the owner |
| Old Champlain Canal Lock 19 (Parish) | Comstock, Town of Fort Ann, NY (43.44548, -73.44666; canal society and OpenStreetMap agree) | American Canal Society index (2011): "submerged by Barge Canal" | Whether any stone shows above water, and from where |
| Old Powder House, Fort Ann | Fort Ann, NY (HMdb 58088, 43.41438, -73.49403, NY 149) | 1935 state marker: used in the French and Indian and Revolutionary wars | No source says the building still stands; not tried on the aerial |
| Granville Friends Meeting House | Quaker Street, Granville, NY (HMdb 131742, 43.40596, -73.26566) | 1932 marker: built 1806 beside the site of a log school, later a district school | Whether the building stands and what it is now |
| South Argyle United Presbyterian Church | County Route 49 at Lohret Road, Argyle, NY (HMdb 58529, 43.19063, -73.46145) | 1935 marker: first pastor Thomas Beveridge, church on the 160-acre glebe from the Argyle Patent | When the present building was put up, and service times from the church's own page |
| First Church and Manse of Argyle | NY 40 south of Brennan Road, Argyle, NY (HMdb 306094, 43.22424, -73.48911) | 2022 town historian's marker: built 1792 a short way east | Whether anything is left; probably a site only |
| Maxwell Farm | Jackson, NY (Wikipedia 43.10528, -73.40361) | Register 2012: house c. 1815, main barn c. 1790, corn crib c. 1815 | Whether the barns can be seen from a public road; position not checked |
| Hiram Congdon House | Putnam, NY (Wikipedia 43.69944, -73.43111) | Register 1997: house of about 1848 | Left out as an ordinary private house unless a source gives more |

## Tips
- `photo_find.py look` on five places took more than two minutes and hit the shell's limit; run it in the background with its output sent to a file, then read the file.
- The NPGallery text route (`npgallery.nps.gov/NRHP/GetAsset/NRHP/<ref>_text`) read the 2017–2018 New York forms in full (Whitehall Fire Station 100002367, Moss Street Cemetery 100000650).
- The Washington County Historical Society's site (`wchs-ny.org/the-wing-northup-house/`) reads with `page.py` and gives its research hours; `skenesborough.com` reads too but is a friends' site whose hours were for 2021.
- Web searches in this session returned titles and links only, with no quoted text.
