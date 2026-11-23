# pueblo_wpln: Pueblo, Colorado: downtown and the Mesa Junction
state: Colorado
region: co
date: 2026-11-23
places: 16
file: data_pueblo_wpln.py

## What this batch is
Sixteen standing places in Pueblo, Colorado, which had only Rosemount. The names came from a video about the town (job 9 in PROMPTS.md; the record is `source/videos/20250307_E5-pXiAlw2s.md`). The video was used only as a list of names, and every fact comes from a source that was opened: Wikipedia as raw text, including the Pueblo County Register list; SAH Archipedia (Buildings of Colorado, 1997), which read well with `page.py --all`; the Trost Society and Wetmore Historical Society pages on Old Central High; History Colorado register pages; KOAA on the Columbus monument; and the managers' own pages for hours (the Pueblo Zoo, the Steelworks Center of the West, the Cathedral of the Sacred Heart). The places: the Orman–Adams House, the County Courthouse, the Federal Building (old post office), Union Depot, Old Central High School (the 1882 stone schoolhouse on Pitkin Avenue), the Vail Hotel, the Mechanics (Masonic) Building, the Tutt Building, the Thatcher Building (First National Bank), First Presbyterian, the Cathedral of the Sacred Heart, Temple Emanuel, the City Park Zoo, the CF&I office and dispensary (Steelworks Museum), City Hall with Memorial Hall, and the Columbus Monument. Pins are address points from the ArcGIS geocoder or Register list points; all were looked at on the aerial, and two were moved onto their buildings. Not checked: the present owner or use of the old Central High, the Federal Building and the Thatcher Building (Archipedia is from 1997); whether the courthouse, Memorial Hall, the Thatcher lobby or Union Depot can be visited inside; service times for First Presbyterian and Temple Emanuel (no page of their own was found); the Columbus statue's exact spot (the pin is the Register point on the Abriendo Avenue parkway, `prec='area'`). Nothing was checked on the ground. Red brick is `yes` only for the Tutt Building, whose Wikipedia article says its walls are red-faced brick.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| McClelland Orphanage | Pueblo, CO, 415 East Abriendo Avenue (38.256111, -104.616667, Register list point) | Register-listed 1992; built 1934–35, Colonial Revival (National Register search results); a USC project page says it is now a private school | A source opened on its present use and access |
| Colorado State Hospital Superintendent's House | Pueblo, CO (38.2806, -104.6239, Register list point) | Register-listed 1985, on the grounds of the state mental hospital, whose main building opened in 1883 (Wikipedia) | Whether anything early survives on the hospital grounds and what can be seen from a public way |
| Pueblo Union Avenue Historic Commercial District | Pueblo, CO (38.264167, -104.613333) | 69 contributing buildings, Register-listed 1983 (Wikipedia); Union Depot, the Vail Hotel and City Hall are in it | Could be added as one district place (cat town) |
| Quaker Flour Mill | Pueblo, CO (38.2625, -104.608889, Register list point) | Register-listed 1976; in the Union Avenue district | Any source opened on what stands and its use |

## Tips
- SAH Archipedia (`sah-archipedia.org/node/<n>`) reads in full with `page.py --all`, and each entry lists the nearby entries with their node numbers in the cached page: grep `href="/node/[0-9]*"` in `research/pages/` to get a whole downtown in one go. The `archipediavm.upress.virginia.edu` mirror reset the connection.
- historycolorado.org `/location/<slug>` pages are drawn by script for most places and give only a line or two; `steelworks.us` gives 403 to `page.py` but read with the web fetch tool.
- `shcathedral.org` is Knoxville, Tennessee; Pueblo's cathedral is `shcathedral.net`.
