# pe_tpau: Prince County, Prince Edward Island
state: Prince Edward Island
region: pe
date: 2026-11-19
places: 20
file: data_pe_tpau.py
tidied: 2026-11-26

## What this batch is
The first places in Prince County, Prince Edward Island (outside Summerside); the two earlier PEI batches hold only Queens County. Twenty places: the Alberton Courthouse (1878, now the Alberton Museum) and the granite Alberton station (1904–05); Yeo House and the Green Park Shipbuilding Museum (1865), Old St. James Anglican Church at Port Hill (1841, box pews, never wired) and the Bideford Parsonage Museum (1878, L. M. Montgomery boarded there); Kensington's fieldstone station (1905, now a pub) and O'Leary's wooden station (1913–14); four churches (St. Simon and St. Jude, Tignish, 1859–60 red brick by P. C. Keely; Notre-Dame-du-Mont-Carmel, 1898 red brick; St. John the Baptist, Miscouche, 1890–92; St. Mary's, Indian River, 1900–02 by W. C. Harris, now a concert hall) and the Keir Memorial Museum (1927 Presbyterian church); five lighthouses (North Cape 1865–66, Seacow Head 1863, West Point 1875–76 with its inn and museum, Indian Head 1881, Cape Egmont 1883–84); the Lower Bedeque school (1886, where Montgomery taught), the Ramsay Stone House (1850s sandstone, private) and the Moase Blacksmith Shop (1842, private). Every place has its Canadian Register statement, read in full with `page.py --all -n 60000` (ids from the `{{HPC row}}` templates of the Wikipedia "List of historic places in Prince County, Prince Edward Island", split from `research/wikiraw/`). Hours: Tourism PEI operator pages (dates of operation only, marked "times not checked"), the Diocese of Charlottetown's February 2026 Mass-times PDF (only Tignish's Saturday vigil could be read), the Indian River Festival's page, and the Anglican Parish of Port Hill's history page plus a 2016 news item (Old St. James deconsecrated 2009, a heritage and genealogy centre). Brick: yes for Tignish and Mont-Carmel from the Register's own photographs (`brick.py look <id> <historicplaces.ca thumbnail>`); no for wooden and stone buildings whose Register text says what they are built of; ? where a brick chimney or foundation's colour was not stated. **Not checked:** anything on the ground; opening times for every museum (peimuseum.ca answers 403); who owns and whether visitors may walk to the Cape Egmont, Seacow Head and Indian Head lights; current use of the Alberton and O'Leary stations; Mass times at Mont-Carmel and Miscouche; when Old St. James opens. **Pins that mark only an area:** Keir Memorial Museum (Register and address point in a yard; the museum and the Princetown United Church stand close together and were not told apart), Lower Bedeque school (in a belt of trees, no building seen), Ramsay Stone House and Moase Blacksmith Shop (pins on the public road in front of the farms). Pins moved with `pix.py`: Mont-Carmel (54 m) and Tignish (83 m) off road junctions and lawns onto the churches, North Cape (24 m) and Cape Egmont (20 m) onto the towers. Kensington's Register list point is about 600 m off; the OpenStreetMap point at 62 Broadway Street North was used. There is no 1 m LiDAR in PEI and the US land map knows nothing here, so every `land:` line reads "not on mapped public land".

## Leads
Moved to `LEADS.md` on 2026-11-26 by the tidy job (3 rows). New leads for this ground go in the note of the batch that finds them.

| Place | Where | What is known | What is missing |
|---|---|---|---|

## Tips
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (4 tips).
