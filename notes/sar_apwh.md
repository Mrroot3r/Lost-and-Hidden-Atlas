# sar_apwh: Saratoga County: Ballston Spa, Malta, Crescent and Day
state: New York
region: sar
date: 2026-11-19
places: 11
file: data_sar_apwh.py

## What this batch is
Eleven places in region `sar` (drawn by `choose.py --state ny`), mostly standing buildings in towns the Atlas was thin in. Ballston Spa: Christ Church (1860–62, Upjohn office; the 1858 armory it owns is in its text), the marble First Baptist Church (1896), the National Bottle Museum, the 1936 post office and the Verbeck House. Malta: the Wiggins-Collamer House (now a shop). Crescent: the 1842 Noxon Bank. Saratoga Springs: Bethesda Episcopal Church (1842–44) and the 1832 Bryan house on Maple Avenue. Milton: the Rose Hill stone water tower. Day: the WPA old town hall at Day Center (the lead row in `sar_defo` and `sar_wqmx` notes, deleted). Sources: Wikipedia raw text (`wiki_raw.py`), HMdb markers (`page.py`), the Diocese of Albany's parish page, the State Military Museum's armory page, Bethesda's own history and home pages, the Baptist church's own history article in Saratoga TODAY, the Bottle Museum's page, the Collamer house shop's page. Brick from Wikipedia photos opened in the session (post office and Noxon Bank red brick; Verbeck and Collamer houses clapboard with red-brick chimneys); the rest are '?'. Not checked: the post office's hours (hours='?'); present use of the Noxon Bank, the Bryan house and the Day town hall; where exactly the Rose Hill tower stands (pin is the marker, on the road; the aerial did not show it plainly) and who owns it; which building at the Day Center corner is the town hall; which house on Church Street is the Verbeck House (pin moved 18 m off the road onto the likeliest house, not confirmed). The Bryan house, the Rose Hill tower and the Day town hall rest on one marker each (`conf='mixed'`). Interiors not checked anywhere.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Ballston Spa National Bank building | Ballston Spa, NY (Register 100012106, 43.0024, -73.8518) | Listed on the National Register 2025 | The form: NPGallery's text route returns a PNG for it and the parks.ny.gov PDF is 404 |
| First Presbyterian Church of Ballston Spa | Ballston Spa, NY (Register 100013325) | Listed on the National Register | Any source on the building; the village's church pages are 404 |
| Seabury Mills | Galway, NY (HMdb 127167, 43.02724, -73.98947) | 1850 carding mill, vinegar works, saw and feed mill, run 60 years by the Seabury family | Whether anything is left on the ground; owner |
| Mosher plow factory | Mosherville, NY (HMdb 131062, 43.06182, -74.01901) | Mosher Plow made here 1847–1926, waterwheel-powered | Whether anything is left; owner |
| Royal Blockhouse site | Moreau, NY (Register 11001062) | 1758 blockhouse site of the Fort Edward complex; Archaeological Conservancy bought it 2011 | Whether the Conservancy lets visitors in, and a location; form is an NPGallery placeholder |
| Rensselaer & Saratoga Railroad at Shenantaha Creek Park | Malta, NY (HMdb 151597, 42.96422, -73.82491) | Marker at the park lot: third railroad chartered in New York, 1832 | What of the grade is left in the park |

## Tips
- NPGallery's `_text` route for New York listings numbered 100xxxxxx (2017 on) returned an 893-byte PNG, not a form or a placeholder, for six Saratoga County listings; `page.py` does not say so.
- ballstonspa.gov moved: every `/churches/pages/...` and `/plaques-dates/...` address that search results give is 404 (archived copies exist but need the web fetch tool). saratogacountyny.gov `?p=` addresses are 404 too.
- historypointer.com NRIS pages are drawn by script; the 307 characters `page.py` gets still give the address and whether the listing was removed (the old county courthouse complex was delisted in 1974).
- Wikimedia refused the Bottle Museum picture twice after four in a row.
