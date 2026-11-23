# fortworth_zbhn: Fort Worth, Texas: courthouse, stations, Art Deco towers, stockyards and banks
state: Texas
region: tx
date: 2026-11-23
places: 16
file: data_fortworth_zbhn.py

## What this batch is
Sixteen standing buildings in Fort Worth, taken from the names in one video about the city's old buildings (the record is `source/videos/20230802_kW1GIq_XnDg.md`; the video was a tip only, and nothing in the entries comes from it). The Atlas had nothing within 15 km before. Added: the Tarrant County Courthouse, the T&P Station, the Livestock Exchange Building (Stockyards Museum) and the Stockyards historic district, the Blackstone Hotel, the Flatiron Building, the Sinclair and Petroleum buildings, the Main Post Office, the Farmers and Mechanics and First National bank towers, the Will Rogers Memorial Center, North Fort Worth High School, the Fort Worth Union (Santa Fe) Depot, First United Methodist Church, and Fire Station No. 1 (not named in the video; found while looking for its "old Central fire station", which the postcards show was a different stone building). Sources: Wikipedia through `wiki_raw.py`; National Register forms from the THC atlas PDFs (Sinclair, Petroleum, North Fort Worth High School); THC marker texts; SAH Archipedia entries; the Stockyards' own museum page; Historic Fort Worth's page for the Methodist church (read with the web fetch tool) and the church's own worship page. Pins from `geo.py` PointAddress matches or OpenStreetMap building outlines, all looked at on the aerial; the T&P Station pin is on the plaza beside the station and is marked as the site. Not checked: any interior, hotel and post office hours (written `?`), the courthouse's public hours, what is inside Fire Station No. 1 now (an exhibit or a café: sources differ, so it is `conf='mixed'`), and the Union Depot's year (1899 or 1900: sources differ). 32 names from the video are left "not checked" in the record.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort Worth Hall, Southwestern Baptist Theological Seminary | Fort Worth, TX (Seminary Hill) | The seminary's first Fort Worth building, gift of the city, 1910 (THC marker 5439004991); a search result says it still stands as a dormitory | A position for the building (OpenStreetMap does not name it) and a source opened for its present state |
| Oneal-Sells Administration Building, Texas Wesleyan University | Fort Worth, TX (Polytechnic Heights) | Built 1902–1903 of Dublin, Texas stone as Polytechnic College's main building, remodelled 1909 and 1963–1966; Recorded Texas Historic Landmark 1966 (Wikipedia, Texas Wesleyan University) | A position for the building on the campus |
| Knights of Pythias Castle Hall | 315 Main Street, Fort Worth, TX | Red brick, 1901, Sanguinet & Staats; restored 1981 (Wikipedia) | Not named in the video; simply not written up |

## Tips
- In Fort Worth `geo.py` turns "W" into "E" on some streets (131 W for 131 E Exchange Avenue, 210 E for 210 W Sixth Street, 800 E for 800 W Fifth Street, 251 E Lancaster): check the matched address it prints; `osmnear.py ... buildings -g '<name>'` found the right building each time.
- NPGallery has only the placeholder for the Fort Worth Register forms tried; the THC atlas copies (`atlas.thc.state.tx.us/NR/pdfs/<ref>/<ref>.pdf`) read well with `page.py`.
- historicfortworth.org and hmdb.org answered 403 to `page.py`; the web fetch tool read historicfortworth.org.
- SAH Archipedia building pages (`sah-archipedia.org/buildings/TX-02-FW<n>`) read well with `page.py --all` and give address, date, architect and what the building is now.
