# kcmo_dtc_wfqz: Kansas City, Missouri: downtown commercial buildings, the Paseo and Gillham Road
state: Missouri
region: kcmo
date: 2026-11-26
places: 12
file: data_kcmo_dtc_wfqz.py

## What this batch is
Twelve downtown Kansas City buildings (office blocks, a police station, a warehouse, a former Nabisco bakery, apartments on the Paseo, a church for the deaf, and Knuckleheads in the East Bottoms), all of them standing and view only except Knuckleheads. Every fact comes from Wikipedia read as raw text (`wiki_raw.py`), plus Knuckleheads' own history page and, for St. Mary's Episcopal church, the services page. Many Register listings here have only a one-paragraph Wikipedia stub and no readable nomination, so most entries are short and say so: materials, interiors and present use were mostly not checked. Pins are Wikipedia's coordinates, looked at on the aerial; Kessler Apartments' falls in the Paseo roadway and is marked area. Red brick is `yes` for Title and Trust (source says red brick), `some` for Palace Clothing and Safeway (sources say brick and terra cotta or brick and stone front), otherwise `?`. Hours were not checked for any new place; Knuckleheads' page is drawn by script. For the already-mapped St. Mary's Episcopal Church, Holmes Street, hours were recorded in `hours_npwt.py` (Sunday 8 and 10 a.m.; the page text lost the times, so they come from a web search result quoting the page). One picture search was run; Knuckleheads has only concert photographs on Commons, so none.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Maine Apartments | Paseo, Kansas City (39.0997, -94.5647) | National Register 2002, built 1901 (Wikipedia) | On the aerial the Wikipedia point is a cleared lot; whether the building stands is not known |
| Westminster Congregational Church | 3600 Walnut St | Wikipedia: demolished 2021 despite protest | Gone; not added |
| Imperial Brewing Company Brewery | 2825 Southwest Blvd | Wikipedia: demolished 2023 | Gone; not added |
| Benton Grammar School | Benton Blvd, Kansas City | Wikipedia: 1904 building, Walt Disney's school, later D.A. Holmes School | Whether the building stands |
| Kansas City Bolt and Nut Company plant | Northeast Industrial District (39.104, -94.499) | Wikipedia: 1888 to 2001 | What is left of it |
| Temple Block, Blackstone Hotel, Chicago Apartments, Tocoma, Aines Farm Dairy, Acme Brass, Vaccaro Soda Water building and other Register gaps in Jackson County | Kansas City | `tools/gaps.py mo "Jackson"` lists 70 | No Wikipedia article, and no nomination form readable (NPGallery gives a placeholder; mostateparks.com PDFs 404) |

## Tips
- Jackson County's remaining Register gaps have no Wikipedia article, so the quickest way to find a source is the Wikipedia category pages (curl `https://en.wikipedia.org/wiki/Category:Buildings_and_structures_in_Kansas_City,_Missouri` with any user agent works when `wiki_raw.py` cannot search) compared against the place lists by name.
- Grep the place lists for a church by a distinctive word, not the full name: St. Mary's was already on the map under an apostrophe spelling my first search missed.
- `resync.sh` kept two files that were not mine (`data_kcmo_wpt_dnvk.py`, `checked_ok.json`) as "session changes" after main had moved; check `git diff --cached --stat` after publish.sh and restore any file you did not touch from main.
- `page.py` drops lines of a page that begin with a day or a clock time when the times sit in separate elements; a web search result quoted them where the page text did not.
