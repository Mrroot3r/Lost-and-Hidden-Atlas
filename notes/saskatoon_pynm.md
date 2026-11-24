# saskatoon_pynm: Saskatoon: downtown, Riversdale and the mills
state: Saskatchewan
region: sk
date: 2026-11-24
places: 10
file: data_saskatoon_pynm.py

## What this batch is
Ten standing places in Saskatoon, from a video's list of names (record: source/videos/20221222_5v0LGyc0q9I.md) and, where the video named too little, from the City of Saskatoon heritage register. From the video's names: the King George Hotel, the Albany Hotel, the Robin Hood mill (now Ardent Mills), King George School and the 19th Street Subway. Added from the register to fill out downtown (the video shows unnamed churches, a bank and a brewery, and these are not claimed to be the ones shown): the Great Western brewery, the Royal Bank building, Knox United Church, St. John's Anglican Cathedral and Third Avenue United Church. Every fact is from the City's heritage-register page for each place (read with page.py; the slug is the place name, saskatoon.ca/heritage-register/<name>) or its printed register PDF, Wikipedia raw text, the two churches' own pages for service times, Ardent Mills' list of mills, the province's June 2025 news release on the new city-centre school, and a CBC timeline for the YMCA. Pins are the ArcGIS geocoder's address points or OpenStreetMap points, each looked at on the aerial; the Robin Hood mill's address point fell on a bare lot and was moved onto the mill, St. John's moved 20 m onto the church. Not checked: anything on the ground, parking (downtown street parking, said "not checked"), brick colour on seven places (left '?'), whether Great Western runs tours or a shop (its site reset the connection), service times at Third Avenue United / St. Vincent of Lerins (no page of its own found), and what happens to King George School when the new school opens in 2027–28.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Empire Hotel | 2nd Avenue South at 20th Street, Saskatoon, SK | A University of Saskatchewan archive photo puts it there; a user-made model page says it opened 1906 and is now part of the Lighthouse supported living building | A reliable source that the building stands and which one it is |
| Quaker Oats mill | Saskatoon, SK | The Encyclopedia of Saskatchewan (search result only, not opened) says Quaker Oats took over the A.P. McNab mill in 1912 and left Saskatoon in 1972 | Where it stood and whether anything is left |
| Saskatoon Masonic temple | Saskatoon, SK | Named in a video; not on the City heritage register | Any source |

## Tips
- City of Saskatoon heritage-register pages open with page.py --all at saskatoon.ca/heritage-register/<slug> (slug = name in lower case with hyphens); the listing page itself answers 404 to a script, but the printed register PDF (heritageregistry_final.pdf, linked from search results) lists every entry with a summary.
- The ArcGIS geocoder gave PointAddress matches for every Saskatoon street address tried; nom.py found only buildings with their own OpenStreetMap names.
- greatwesternbrewing.com reset the connection and its Internet Archive copy could not be fetched either.
