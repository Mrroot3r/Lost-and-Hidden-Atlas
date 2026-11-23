# canton_pknj: Ohio: old Canton, McKinley's town
state: Ohio
region: oh
date: 2026-11-23
places: 10
file: data_canton_pknj.py

## What this batch is
Ten standing places in downtown Canton, Ohio, where the Atlas had nothing within 15 km. Six come from the names in one Old World Exploration video about the city (the record of every name is `source/videos/20250117_ky7yvCYNKx8.md`; the video is a tip and nothing rests on it): the Stark County Courthouse, the McKinley National Memorial, the First Methodist Episcopal Church (Crossroads United Methodist), the 1903 Carnegie library, the Canton Masonic Temple and the surviving entrance of the Hotel Courtland. Four more stand within a few blocks and were added from the Stark County Register list: the Basilica of St. John the Baptist, the First Ladies National Historic Site (Saxton McKinley House), the Palace Theatre and the former Trinity Lutheran Church. Facts are from Wikipedia (each article linked), the National Register form for Guy Tilden's Canton buildings (64000606), the Clio walking-tour page for the Courtland, and a Repository article on the Masonic Temple's centenary. Hours are from the First Ladies museum's own page, the Basilica parish's page (the diocese's page gives a seasonal swap of Saturday and Sunday Masses with St. Peter's, which the access note says), and the Palace Theatre's page. Not checked: the McKinley Memorial's hours (the Stark County Historical Society's site asks for a browser check), Crossroads United Methodist's service times (its site would not connect), the courthouse's public hours, the present state of the Courtland entrance and which of the small buildings at 331 Market Avenue South is the Saxton House on the aerial. Red brick is unset ('?') for most: no source or picture opened settled it. Nothing here was seen on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Old McKinley High School | Canton, OH (40.80361, -81.37222) | Built 1916, named for Anna McKinley; on the National Register 1982; now a health care centre (Wikipedia) | Owner's page and a look at the pin |
| First Reformed and First Lutheran Churches | 901 and 909 E. Tuscarawas St., Canton, OH (40.7975, -81.3675) | On the National Register together (1982); First Reformed's sanctuary finished 1862, now First Church of the Resurrection (search results only) | An article or form opened, service times |
| Molly Stark Sanatorium | Louisville, OH (Nimishillen Township, Stark Parks) | 1929 tuberculosis hospital, closed 1995; Stark Parks began demolishing it in autumn 2025 (News 5 Cleveland, search results only) | Whether anything was kept; whether the park is open |

## Tips
- `page.py` could not read PDFs at first: pypdf died on a broken `cryptography` binding (`_cffi_backend` missing). `python3 -m pip install --break-system-packages cffi` fixed it.
- `videos.py check` reads everything after "added " as the place id: write `added <id>` with nothing after it and put any remark in the "Likely name" column.
- In Canton the ArcGIS geocoder gave PointAddress results on the buildings for every downtown address tried.
- mckinleymuseum.org answers page.py and the web fetch tool with a browser check; its hours could not be read.
- crossroadsumc.org is a Pittsburgh church, not Canton's Crossroads United Methodist (crossroads120.org, which would not connect).
- The Basilica parish's old address stjohncanton.com now redirects to sjbspcanton.org.
