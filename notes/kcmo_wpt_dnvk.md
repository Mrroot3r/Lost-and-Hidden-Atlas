# kcmo_wpt_dnvk: Kansas City: Westport and Midtown
state: Missouri
region: kcmo
date: 2026-11-23
places: 16
file: data_kcmo_wpt_dnvk.py

## What this batch is
Sixteen standing places in Westport, Midtown and the Country Club Plaza area of Kansas City, Missouri, from the Wikipedia list of Register listings outside downtown (Jackson County): Kelly's Westport Inn, the Harris-Kearney House, the Alexander Majors House, the Benton home, Mineral Hall, the Ward Homestead, the Corrigan House, the Uptown Theater, the Athenaeum, Loretto Academy, Westport High School, the Newbern Hotel, Sophian Plaza, the Raphael, Community Christian Church and the Pink House. The Atlas had about nine places in this ground before (Wornall House, Waldo tower, Electric Park and a few more). Facts come from Wikipedia raw text; hours for the Benton site and the Majors house are from their operators' own pages (read in full); the Harris-Kearney hours are quoted in a search result from the society's page and are pandemic-era. Not checked: Register forms (not read), interiors, parking (pins are on buildings, street parking assumed but not confirmed), any operator page for the theater, hotels, church, Athenaeum and Loretto. Pins were looked at on the aerial; Loretto's was moved onto the school building (the geocoded address fell on the street). Two pictures were chosen: the Westport High School one is a red-brick photo (brick = yes from it); none fits the Pink House.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Mabry Hall | 4112 Pennsylvania Avenue, Kansas City, MO | Wikipedia's Kelly's article says it is seven years older than Kelly's (about 1843) | An article or operator page; not found under that title |
| Westminster Congregational Church | 3600 Walnut Street, Kansas City, MO | Register 1980, demolished 2021 per Wikipedia | Nothing to see; add only as gone |
| Mutual Ice Company Building | Westport, Kansas City, MO (39.0511, -94.5905) | Register 2004, built 1907; Wikipedia has only a stub | A source on what it is now |
| Masonic Temple, Beth Shalom Synagogue, Newbern-era Hyde Park apartment districts, Janssen Place | Midtown, Kansas City, MO | On the Register list; Masonic Temple has a Wikipedia article (1911, Tiffany ballroom, restoration from 2017) | Operator pages and hours; Janssen Place and Beth Shalom have no article under the titles tried |

## Tips
- Wikipedia's Kansas City Register list is split in two: "National Register of Historic Places listings in Jackson County, Missouri: Downtown Kansas City" and "...: Kansas City other" (191 rows); `wiki_raw.py --rows` reads both.
- `mostateparks.com/hours/<id>/...` pages read well with `page.py --all` and give tour times; the park's main page answers 404. `wornallmajors.org` also reads well.
- `parking.py` lists street names, not lots, in dense Kansas City; it gave nothing useful for these pins, so no `th=` points were given.
- The Commons finder's "NAMES IT" candidates for the Pink House were other Hook houses with similar file names: check the house name, not the architect.
