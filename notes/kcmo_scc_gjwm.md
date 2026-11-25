# kcmo_scc_gjwm: Kansas City: Country Club District, Sunset Hill and Midtown houses
state: Missouri
region: kcmo
date: 2026-11-25
places: 11
file: data_kcmo_scc_gjwm.py

## What this batch is
Eleven standing houses in Kansas City, Missouri, none of which the Atlas had: the Epperson House (UMKC), the Dr. Generous Henderson House on The Paseo, the Keith (J. C. Nichols), Mack B. Nelson and Tom Pendergast houses on or near Ward Parkway, and six houses by the architect Mary Rockwell Hook on Sunset Hill (her own house, 5011 Sunset Drive, and the Bertrand Rockwell, Emily Rockwell Love, Floyd Jacobs and Robert Ostertag houses). Chosen by comparing the National Park Service Register points (`nrhp_state.py`) with the Atlas pins: the Midtown and Country Club listings still held about 30 gaps. All text comes from Wikipedia read as raw text; the state's Register PDFs answer 404 and archive copies cannot be fetched, so no nomination form was read. Every house is private or a closed building, so all are view-only and hours are blank. Pins: six from OpenStreetMap street-address lookups that name the house, checked on the aerial; Love and Ostertag are the Register point only (house nearest the point, not confirmed by address). Pictures: nine from Commons chosen by looking at the sheets (Epperson and Nelson: none fit; Tom Pendergast: nothing on Commons). Brick: Keith yes (picture), Henderson some (Wikipedia: brick and stone; the picture looks pale), 5011 Sunset some (picture); the rest '?'. Not checked: interiors, current owners, whether any house is open.

The Lee's Summit, Raytown and Grandview ground was the first choice but earlier notes had worked it out; Cass, Ray and Lafayette county Register lists are mostly on the Atlas already.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Pilgrim Lutheran Church for the Deaf and Parsonage | 3801-3807 Gilham Road, Kansas City, MO | Wikipedia: 1941, Frederick Roth Webber, Register 2001, Missouri Synod church for the deaf | Wikipedia's point fell on Pennsylvania Avenue houses and OpenStreetMap shows no church on Gilham Road near it; needs a correct address and pin |
| Michael H. and Rose Katz House, George H. Nettleton Home (5125 Swope Parkway), Norman Tromanhauser House, Hiland Telephone Exchange, Seven Oaks School, Bancroft School, Wheatley-Provident, colonnade apartments | Midtown and east side, Kansas City, MO | On the Register list (Kansas City other), no Wikipedia article or none under the title tried | A readable narrative source (Register forms unavailable) |
| Reverend Nathan Scarritt Home | Westport, Kansas City, MO | Wikipedia: built 1847-1853, cared for by James B. Nutter & Company | No address or coordinate in any source opened |
| Westminster Congregational Church | 3600 Walnut, Kansas City, MO | Wikipedia: demolished in 2021 | Nothing to see; listed so it is not searched again |
| Sondern House (Frank Lloyd Wright, 1940) | 3600 Belleview, Kansas City, MO | Wikipedia | Usonian modernist: left out under the style rule |

## Tips
- `nrhp_state.py` plus the Atlas's `build/sites.json` (match by distance, over 500 m) found the gaps quickly; Wikipedia's "Historic Houses of Kansas City, Missouri" navbox (`wiki_raw.py "Template:..."` then read research/wikiraw) lists houses by neighbourhood.
- `nom.py "<number> <street>, Kansas City, MO"` returns OpenStreetMap buildings named for the house; better than Wikipedia's point (Keith, 5011 Sunset were far off).
- `photo_find.py look` renumbers candidates on each run: look at the sheet of the same run before `set` (the 5011 house first got another house's picture and was corrected).
- Wikipedia category API answers 429 if asked in a row; leave about 8 s between requests.
- `tools/app_smoke.js` could not load its page in this cloud session; `tools/smoke.js` against dist/web passed for a new place.
