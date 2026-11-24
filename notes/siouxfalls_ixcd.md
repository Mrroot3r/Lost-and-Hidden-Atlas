# siouxfalls_ixcd: Sioux Falls, South Dakota: quartzite churches, schools and civic buildings
state: South Dakota
region: sd
date: 2026-11-24
places: 14
file: data_siouxfalls_ixcd.py

## What this batch is
A video session (job 9): the names came from one walk-through video of Sioux Falls's old buildings, recorded in `source/videos/20240224_7HY3uH5SFGs.md` (43 names: 14 places added, 3 already on the map, 8 gone, 16 not checked). The 14 are standing buildings in and round downtown: the Carnegie library (now the council chambers), the Central Fire Station, the federal courthouse and old post office, the Phillips Block, the Odd Fellows (Pettigrew and Tate) Block, the Masonic Grand Lodge and library, the Coliseum, Washington High School (the Washington Pavilion), First Congregational Church, the Cathedral of Saint Joseph, Calvary Cathedral, the All Saints School main building, Old Main and East Hall at Augustana, and the Columbus College buildings on the VA medical centre campus. Sources: National Register nomination texts from NPGallery (read with `page.py --all -n 200000`), Wikipedia (`wiki_raw.py`), SAH Archipedia (VA campus, Augustana, Central Fire Station), the Washington Pavilion's hours page, the Episcopal Asset Map listing for Calvary's service times, and KELO and Dakota News Now pages for the Coliseum and the Phillips Block. Pins are from ArcGIS PointAddress hits and one OpenStreetMap point, each looked at on the aerial; First Congregational and All Saints were moved onto the buildings. Not checked: interiors today; St. Joseph's Mass and tour times (its own site answered 403); whether the Masonic library still opens to visitors; which wing at All Saints is the 1884 main building; the Coliseum's fate (in May 2026 the county put off a consultant's advice to raze it). All are seen from the street except the Pavilion and the two cathedrals.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| South Dakota School for the Deaf, Old Main (1883) | Sioux Falls, SD, 1800 East 10th Street (Register 81000576; 43.5475, -96.7028) | Register form: Wallace Dow's quartzite Old Main of 1883 and the 1884-85 boys' dormitory; the campus closed in 2011 and was sold, and a news item says the Center of Hope moved into a former school building on East 8th Street | Whether Old Main still stands, and who owns it now |
| Presentation Children's Home | Sioux Falls, SD (Register 92001852; 43.5397, -96.7511) | Register form text read (22 pages) but not used | Current use and owner, and a look at the aerial |
| First Baptist and First Methodist churches | Sioux Falls, SD | Named in the video only; a 2026 news item says First Baptist plans to sell its building and move | Building dates and materials from a source |
| Whittier School, the Elks Club, the Minnehaha Building, the YMCA | Sioux Falls, SD | Named in the video only | Any source saying they stand |

## Tips
- siouxfalls.gov, stjosephcathedral.net, episcopalchurchsd.org (a browser challenge) and HMdb.org all refused requests from the tools on November 24, 2026; the Episcopal Asset Map (`episcopalassetmap.org/node/5081`) read cleanly with `hours.py page`.
- SAH Archipedia pages (`sah-archipedia.org/node/<n>`) read fully with `page.py --all` and gave present-day detail that the 1970s Register forms lack.
- The Wikimedia Commons user w_lemay has 2023 photographs of most downtown Sioux Falls buildings; `photo_find.py` found them by position.
