# asheville_wypl: Asheville, North Carolina: Biltmore, the Grove Park Inn, Art Deco downtown and a castle on Sunset Mountain
state: North Carolina
region: nc
date: 2026-11-23
places: 9
file: data_asheville_wypl.py

## What this batch is
Nine standing buildings in Asheville named in an Old World Exploration video (record: `source/videos/20250110_96VFYAP18QI.md`): Biltmore House, Asheville City Hall, the First Baptist Church, the Grove Park Inn, Overlook (Seely's Castle), the Basilica of St. Lawrence, the Grove Arcade, Asheville High School and the Asheville Masonic Temple. Facts from Wikipedia (`wiki_raw.py`), the Buncombe County National Register list (`wiki_raw.py --rows`), and the owners' pages read with `hours.py page`/`page.py`: biltmore.com (open every day, hours vary; no times given), fbca.net (worship and office hours), the Diocese of Charlotte's parish page (Sunday Masses), grovearcade.com (building hours). Pins from OpenStreetMap (`nom.py`) and the Wikipedia point for the Masonic Temple; all nine were on their buildings on the aerial. Not checked: the Grove Park Inn's own page (Omni, HTTP 403) so its hours are '?'; whether City Hall and the Masonic Temple open to visitors; whether Overlook can be seen from a public road; red brick on every place (Wikimedia refused pictures, HTTP 429), so all but the granite Grove Park Inn are brick='?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| George Vanderbilt Hotel (Vanderbilt Apartments) | Asheville, NC, Haywood Street | Opened July 24, 1924; apartments for older people since 1969 (as a web search result quoted Mountain Xpress) | An opened source, the address and a pin |
| Glen Rock Hotel | Asheville, NC, Depot Street | A 1930 building by Henry Irven Gaines (as a search result quoted a housing nonprofit); an earlier Glen Rock Hotel stood in the 1890s | Which one stands, an opened source, a pin |
| Central Methodist Church | Asheville, NC, downtown | Listed in the Downtown Asheville Historic District with dates 1902–1905, 1924, 1968 (Wikipedia) | How much of the 1902 building survives |
| Battery Park Hotel (1924) | Asheville, NC, Battle Square | Built 1924 by Edwin W. Grove, National Register 77000990 (Wikipedia) | Its present use and access |

## Tips
- In this cloud container `pip install` of Pillow left the Debian PIL first on the path; `python3 -m pip install --break-system-packages --ignore-installed Pillow` fixed the pin check. `pypdf` needed `cffi` before it would import.
- saintlawrencebasilica.org answers 403 to `page.py`; the Diocese of Charlotte's parish page gives the Sunday Masses. omnihotels.com answers 403 too.
- biltmore.com's hours page says only "open every day", with no times in the text `page.py` reads (the times are drawn by script).
