# ks_kcm_xqnv: Kansas: Leavenworth districts and Kansas City, Kansas
state: Kansas
region: ks
date: 2026-11-24
places: 7
file: data_ks_kcm_xqnv.py

## What this batch is
Seven places, far fewer than the 15 to 20 aimed for, because the Kansas City area is already worked to the depth that the Register lists allow. This run first looked at Lee's Summit, Raytown and Grandview (claim released), then Olathe, Shawnee and Lenexa; every National Register row in Jackson, Cass, Platte, Clay, Johnson, Wyandotte, Leavenworth and most of Douglas County was already a place. What was added: four Leavenworth districts or houses that the earlier Leavenworth batches skipped (the Downtown, South Esplanade, North Broadway with St. Joseph Catholic Church, and Union Park districts, and the 1864 Albert Doege House), White Feather Spring in Argentine, Kansas City, Kansas (where the Shawnee Prophet died), and the Hanover Heights district in Kansas City, Kansas. Sources: the City of Leavenworth's own district pages, read with page.py; the Kansas Historical Society's register search; Wikipedia read with wiki_raw.py. Not checked: the ground, owners, parking, the church's service times, and where the White Feather Spring marker stands. Photographs: four places got a Commons picture; Commons has none for the Doege House, and White Feather Spring and Hanover Heights show their Wikipedia picture. North Broadway is not on the Register list the Kansas Historical Society's search returned, so the entry calls it a historic district on the city's authority only.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Leavenworth Landing Historic District | 201-221 Delaware St, Leavenworth, KS | State Register 1981 (Kansas Historical Society); the city's downtown page mentions the Landing area on Delaware | The state listing's own description; the 2023 Leavenworth resurvey report (kansashistory.gov/preserve/pdfs/Leavenworth Resurvey Report 9-23-2023.pdf) was found but not read |
| Hycrest (Charles Hyer House) | 505 E Cedar, Olathe, KS | State Register 1984, Bungalow/Craftsman; a Hyer boot factory family of Olathe | A source for the house itself, not the family |
| George Hodges House | 425 S Harrison, Olathe, KS | State Register 1990 | Any description |
| Dutton-Thomas-Soule Farm, Edgerton Grange Hall, Graham Rogers House | De Soto, Edgerton, Overland Park | State Register summaries only | Sources and public views |
| Kansas School for the Deaf | Olathe, KS (38.8825, -94.8128) | Founded 1861, in Olathe from about 1866 (Wikipedia) | Which older buildings stand on the campus, from the school's or a survey page |

## Tips
- The City of Leavenworth's district pages (leavenworthks.gov/cd/page/<name>-historic-district) read cleanly with page.py --all and describe buildings one by one with dates; the Downtown, Third Avenue, Arch Street, North Broadway, South Esplanade and Union Park pages are all there. Save the output to a file (> research/lv/x.txt): the page cache is keyed by hash.
- pix.py pin takes only the target pixel (x y) in the sheet, not the old tile pixel.
- This ground is saturated at the Register level: a next pass needs non-Register sources (Clio tour pages, city survey PDFs such as the Johnson County 2009 survey report on kansashistory.gov, local histories), not the Wikipedia lists.
- olatheks.gov pages return HTTP 403 from page.py.
