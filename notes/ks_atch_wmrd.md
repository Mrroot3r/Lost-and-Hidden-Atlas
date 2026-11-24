# ks_atch_wmrd: Atchison, Kansas
state: Kansas
region: ks
date: 2026-11-24
places: 18
file: data_ks_atch_wmrd.py

## What this batch is
Eighteen places in Atchison, Kansas (about 44 miles north-west of Kansas City, on the Missouri River), where the Atlas had none. The Kansas City ground itself (downtown, Independence, the Northland, Lee's Summit, Johnson County) was already worked by earlier batches: every National Register row checked there was either on the map or a house with no source beyond the list, so this run moved out to Atchison, which `start.py` showed with 26 listed places and nothing on the Atlas. Facts come from the Kansas Historical Society's register summaries for Atchison County, the one Register form read in full (the Burlington freight depot), Wikipedia read as raw text, and the pages of the museums, the church and the monastery for hours. Brick colour comes from the Register text or a Commons photograph opened in the session (Earhart birthplace is white wood: `no`; Campbell Chapel is red brick under white paint: `no`). Pins were looked at on the Kansas 2024 aerial and all sit on the buildings (or the bridge).

Not checked: any interior; who owns the Memorial Hall, the post office, the Howe house, Lincoln School and the rural church; whether the post office is still a post office; whether Campbell Chapel, Ebenezer Baptist and St. Patrick's still hold services; whether the Stranger Creek bridge still carries traffic. The Burlington depot's Register form (2023) says vacant, but a 2024 Commons photo is captioned as Servaes Brewery in it; the text says so and gives no hours. The Muchnic House start year disagrees (Register 1887–88, gallery's page 1885) and says so. Parking: the mapped lots near downtown have no known owner, so no `th` points were given; the notes say to park on the street. Hours were read from the pages of the Earhart museum, the historical society, the Art Association and Trinity Episcopal; the Earhart days (closed Sunday and Monday) are on the museum's page. Pictures: `photo_find.py` was run on the nine places with no Wikipedia article picture. Commons pictures were chosen for eight (Memorial Hall, post office, Santa Fe depot, Burlington depot, Harwi building, Price Villa, the convent, Lincoln School); the Stranger Creek bridge has nothing on Commons. The others show their Wikipedia article's picture.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Atchison's Black Business District | Atchison, KS | Register listing 2024 (100012099), also covered on the Atchison County Historical Society site | The Register text; which buildings stand |
| Benedictine College North Campus Historic Complex (St. Benedict's Abbey) | Atchison, KS (39.5725, -95.1144) | Register 1982, architects Francis Himpler and Alfred Meier, Romanesque | Any source on the buildings; visitor access |
| Central School (1938) | 215 N 8th St, Atchison, KS | Register 2022; PWA-funded Moderne school, now apartments per a Commons caption | Left out as a Moderne building (style rule); revisit if the owner wants it |
| Atchison Rail Museum | 200 S 10th St, Atchison, KS | Run by North East Kansas Railroaders beside the depot; search results gave weekend hours | Hours from its own page |
| Houses: Glick-Orr, Pease, Edmiston, Hetherington, Waggener, Jansen, Hausner, Stein, Lanphear-Mitchell, Bolman, Braun, Schmitt, Horan, Baker, Brown, Harwi, Howard | Atchison, KS | All on the Register with Commons photographs; Atchison has a large stock of 1870s–1900 mansions | A source on each beyond the list; owners; which are worth a page |
| Amelia Earhart Hangar Museum | Atchison airport, KS | Named by search results | Not read |
| Mount Vernon Cemetery | 6920 Rawlins Rd, Atchison, KS | Register 2024 | The form; access |
| Julius Kuhn Block, Wherrett-Mize Drug Building, Atchison YMCA, Atchison First Presbyterian | Downtown Atchison, KS | Register listings 2010–2023 | Sources beyond the list |
| Edgar W. Howe's Potato Hill house | 20045 266th Rd, Atchison County, KS | Register 2021, Bungalow by William H. Sayler | Not read; private |

## Tips
- For Kansas counties the Kansas Historical Society's register search (`natreg_listings/search/page:N/county:XX/records:all`) gives a real summary for every listing, and many nomination PDFs open with `page.py` at `kansashistory.gov/resource/national_register/nominationsNRDB/...`; Wikipedia's county list often has no article behind a row.
- The Kansas City area is saturated by Register listings: check `start.py` counts at 8 km for the smaller towns before choosing, and consider ground 40 to 50 miles out (Atchison had 0; Plattsburg, Odessa, Louisburg and Tonganoxie had 0 to 1).
- A museum page that hides its days in a script (the Earhart museum) still has them in the raw HTML; `page.py -g` showed only some lines, a plain `requests` fetch showed all.
- `photo_find.py look` on five places took about four minutes and wrote sheets only as each finished; wait for the process to end before looking.
