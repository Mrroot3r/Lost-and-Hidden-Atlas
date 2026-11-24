# ks_kckb_pwzn: Kansas City, Kansas (second pass)
state: Kansas
region: ks
date: 2026-11-24
places: 16
file: data_ks_kckb_pwzn.py

## What this batch is
Sixteen standing places in Kansas City, Kansas and Edwardsville that the Atlas lacked: downtown (Brotherhood Block, the 8th Street YMCA, the Town House Hotel, the Horace Mann school and the old high school gymnasium), schools (Lowell, Franklin, Whittier, Vernon, Northeast Junior High, Sumner), Welborn church, two funeral homes, Saint Margaret's Hospital and the Roy Williamson stone house. The facts come from the Kansas Historical Society's register summaries for Wyandotte County (read with page.py), and Sumner's 1939 building from Wikipedia. Most Register forms were not opened, so each entry says only what the short summary gives. Not checked: interiors, hours, present owners and uses. Pins are Register list coordinates looked at on the 2024 aerial; the YMCA and Vernon School pins mark the block or street only (Vernon had no coordinate; the aerial at its address showed a park and houses). Pictures came from Commons by photo_find.py; Vernon School has none. Brick is '?' except Franklin (stone, from a photograph), Saint Margaret's (buff brick, from the register) and the Williamson house (stone).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| St. Augustine Hall | 3301 Parallel Ave, Kansas City, KS (39.1275, -94.6689) | Register 1971, college building, Late Victorian; no article read | A source saying what it is and what stands |
| Judge Louis Gates House | Kansas City, KS (39.0522, -94.6087) | Register 1980 | A summary of it |
| Immanuel Baptist Church; First AME Church; Huron Building | Kansas City, KS | Register listings, no coordinates in the list | Sources and addresses |
| St. John's Orphanage; St. Mary's Church; White Church Memorial Church | Kansas City, KS | State Register only, with no summary on the Society's list | Sources read |
| Vernon School | 2700 Sewell Ave, Kansas City, KS | In the Atlas with an area pin | The school's true spot on the aerial |

## Tips
- The `--rows` list for Wyandotte County shows "article:" for pages that do not exist (red links): wiki_raw.py then says NO SUCH ARTICLE. The Kansas Historical Society's county pages (page:1 to page:6, county:WY) were the source.
- Run the Society's pages through page.py without a cut-off, then keep the text between "starting on record" and "New Search"; the rest is menus.
- A Commons photograph that sits 0 to 6 m from the pin is a good check that a Register coordinate is on the building (it settled Franklin School, which the aerial alone left unclear).
