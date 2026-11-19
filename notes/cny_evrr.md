# cny_evrr: New York: Auburn, Moravia and the Cayuga County lake towns
state: New York
region: cny
date: 2026-11-19
places: 23
file: data_cny_evrr.py

## What this batch is
Twenty-three places in Cayuga County, New York, plus one just over the line in Skaneateles. The region (`cny`) was drawn at random by `choose.py --state ny`, which offered Moravia; the Atlas had nothing within 20 km of Moravia and nothing in Auburn but the canal places to the north. Nearly all standing. Auburn: the Seward House Museum, the Harriet Tubman Home on South Street and the Thompson A.M.E. Zion Church (Harriet Tubman National Historical Park), the Willard Memorial Chapel (Tiffany interior), Fort Hill Cemetery (Logan obelisk, Tubman's grave), Auburn Prison seen from State Street, the closed Schine's Auburn Theatre, and the Cayuga Museum with the Case Research Lab. Owasco and Fleming: the Lakeside Park trolley-park pavilion and carousel shelter in Emerson Park, the Owasco Reformed Church, the Sand Beach Church. Lake shore: the Howland Stone Store Museum at Sherwood, the Jethro Wood House, Aurora village with the closed Wells College campus (area pin), the Almeron Durkee stone house in Union Springs. North: the 1825 Mentz Church. South: New Hope Mills, St. Matthew's in Moravia (Oberammergau carvings), the Cady Tavern, the Morse Farm, Moravia Union Cemetery, the East Genoa Methodist church. Skaneateles: the 1903 Auburn & Syracuse trolley substation. Sources: Wikipedia through `wiki_raw.py` (the county's Register list with `--rows`), HMdb nearby lists and marker pages through `page.py`, sewardhouse.org, nps.gov/hart, cayugamuseum.org, howlandstonestore.org, parks.ny.gov, TourCayuga listings (read through `tourcayuga.com/wp-json/wp/v2/listing/<id>`), the Pomeroy Foundation's Mentz Church page, WAMC on the Wells College sale (November 2026), and a 2016 Waymarking page quoting St. Matthew's own description. Brick: 16 settled (12 from Wikipedia pictures opened with `brick.py look`, 4 from sources that name stone, cobble or carved stones), 7 left '?'. Not checked: anything on the ground; Willard Chapel tour hours; the Cayuga Museum's open days; Fort Hill grounds hours; Emerson Park hours (county page 403); Mentz Church open days; whether the Owasco Reformed, East Genoa and St. Matthew's churches open; whether New Hope Mills has become a museum; whether the trolley substation building at the marker is the 1903 one; which house is the Cady Tavern (pin on the street at the marker); the Schine's current state since 2024 (fingerlakes1.com 2026 article answered 403). St. Matthew's rests on one source (the church's words quoted on Waymarking). Area pins: Aurora village (marker on Main Street), East Genoa church (crossroads; church not picked out), Moravia Union Cemetery (Register point in woods; park lot as parking). The Mentz Church pin was moved 230 m onto the building in the road triangle.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| North Street Friends Meetinghouse | Brick Church Road, Ledyard, NY (Register point 42.76333, -76.65111 is in a field) | Brick Quaker meeting house of 1836 tied to abolition and women's rights (Wikipedia) | The building could not be found on the aerial at the Register point or along Brick Church Road; owner not checked |
| Aurora Steam Grist Mill | Aurora, NY (42.754167, -76.704167) | 1817 stone steam mill, roof fell 1974, Wells College began demolishing it in 1992 (Wikipedia) | Whether anything is left behind the Aurora Inn |
| Old Quarries, Union Springs | Route 90 at Paradise Hill Road (42.82573, -76.69733) | Worked 1836 to late 1800s for paving blocks shipped by canal to Manhattan (Pomeroy marker, HMdb 145832) | Where the quarry faces are and who owns them |
| Genoa Mill site | Route 90, Genoa (42.66817, -76.53725) | Flour mill about 1859–1942 on a mill pond dammed about 1835 (HMdb 133156) | Whether the dam or foundations remain |
| Millard Fillmore boyhood site | Carver Road, Niles (42.80021, -76.33436) | Town of Niles marker, 1976 (HMdb 206829) | Anything to see beyond the marker |

## Tips
- TourCayuga listing pages are drawn by script, but `page.py --all https://tourcayuga.com/wp-json/wp/v2/listing/<id>` reads the listing's text (the id is the `?p=` number in search results; `?search=<word>` lists matches).
- cayugacounty.us facility pages and fingerlakes1.com's 2026 articles answer 403 to `page.py`; fingerlakes1.com's 2025 articles read.
- `wiki_raw.py` saves raw wikitext in `research/wikiraw/`, not plain text, so read more of an article with `-g` rather than from the file.
- `data_b` has no `W`; import it with `from data_ma import W`.
- `publish.sh` stopped twice in five minutes as other batches merged; after `resync.sh`, take the batch time, run `all.sh` and publish straight away.
