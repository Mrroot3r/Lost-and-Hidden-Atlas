# nyc_gudw: Long Island: Southold, Greenport, Orient and Shelter Island
state: New York
region: nyc
date: 2026-11-21
places: 17
file: data_nyc_gudw.py

## What this batch is
Seventeen places on the North Fork of Long Island and Shelter Island (region `nyc`, drawn by `choose.py --state ny`, which offered Orient and Southold; `start.py` showed no Atlas place in the Town of Southold or on Shelter Island). Nearly all standing. Cutchogue: the Old House and Village Green, the Old Cutchogue Burying Ground. Mattituck: the Gildersleeve octagon. Southold: Horton Point Lighthouse, the Southold Historical Museum's Maple Lane campus, First Presbyterian Church and its Old Burying Ground (1671 Wells tomb). Greenport: the station and Railroad Museum of Long Island, the antique carousel, Tifereth Israel synagogue, Brecknock Hall. Orient: the village and the Oysterponds Historical Society, Orient Point Light (boat/far view). Shelter Island: Havens House, Sylvester Manor, the Shelter Island Windmill, Union Chapel in the Grove. One ruin: "The Ruins" of Fort Tyler on Gardiners Point Island (boat only). Sources: the two town Register lists and Wikipedia via `wiki_raw.py`; the managing bodies' own pages via `page.py` (Cutchogue-New Suffolk Historical Council, southoldhistorical.org, the First Presbyterian Church's site, rmli.org, villageofgreenport.org, tiferethisraelgreenport.org, peconiclanding.org, oysterpondshistoricalsociety.org, shelterislandhistorical.org, sylvestermanor.org, unionchapelinthegrove.org, parks.ny.gov). Not checked: anything on the ground; parking except Horton Point's Park District lot; the Old House's tour days (the Council's pages give none: hours='?'); the carousel's maker and date; the Gildersleeve octagon's owner, use and exact corner (pin is the Love Lane/Main Road intersection, prec area; the Register point is 880 m east and wrong); the Union Chapel pin (trees hide it); the windmill pin was moved onto a small tower with a long shadow at the head of the Sylvester Manor fields and is likely but not certain. Brick was set from Wikipedia's pictures for six places, from source text for four, and left '?' for seven. The Old House's date is given both ways (1649 story; 1698/1699 tree rings).

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort Corchaug Archaeological Site (Downs Farm Preserve) | Cutchogue, NY (Wikipedia 41.00268, -72.49874) | National Historic Landmark, 17th-century Corchaug fort site; Wikipedia says the town-owned Downs Farm Preserve is open with trails; Peconic Land Trust says the Town runs a nature center and trails there | A Native American site: needs the Town of Southold's own page inviting visitors (southoldtownny.gov facility pages gave nothing readable) before it is written up |
| Fireboat Fire Fighter | Greenport, NY (Mitchell Marina) | National Historic Landmark fireboat (1938); Suffolk Times, May 2026: back at Mitchell Marina, free tours hourly on weekends from 10 a.m. Saturday, 11 Sunday | americasfireboat.org gives the boat's location as Mystic, CT: where she berths each season, before pinning |
| Shelter Island Heights Historic District, Manhanset Chapel, Camp Quinipet | Shelter Island Heights, NY (41.0844, -72.3572) | Register listings; Manhanset Chapel (1890, moved 1924) is now a private arts space (Wikipedia) | The district nomination for the best buildings; whether the chapel opens |
| Smith-Ransome Japanese Bridge | Shelter Island, NY (41.05063, -72.31930) | 1905 concrete bridge by Ernest Ransome for "Borax King" F. M. Smith's estate (Register list) | Owner and whether it can be seen from a public way |
| Greenport Village Historic District and Stirling | Greenport, NY (41.1047, -72.3647) | Register district of 254 buildings | Read the nomination for its best buildings |
| Terry-Mulford House, Joshua Wells House, David Tuthill Farmstead, Richard Cox House, New Suffolk School, Town Doctors' House | Orient, Cutchogue, Mattituck, New Suffolk, Southold | Register rows in the Southold town list | Owner and what can be seen from the road |
| Long Beach Bar ("Bug") Light and Plum Island Light | Orient, NY | NYS Parks says both can be seen from Orient Beach State Park | A source for each; Plum Island is closed federal land |

## Tips
- The Cutchogue-New Suffolk Historical Council's guessed pages (/visit/, /tours/, /the-old-house/) all return the home page; its real pages are under /timeline/<name>/ and /about-us/, found by grepping the cached home page in research/pages/.
- The First Presbyterian Church of Southold's site answers at jan-falkowski.squarespace.com (titled "FPC Southold"); it reads in full with page.py.
- southoldtownny.gov facility pages answer, but the Downs Farm address returned the Goose Creek beach page.
- The Register list point for the Andrew Gildersleeve Octagonal Building is about 880 m east of Love Lane.
- Web searches in this run returned titles and links only; every hour came from page.py on the managing body's page.
- publish.sh stopped once because main moved (app.js and others); resync.sh, all.sh and a second publish.sh to a new branch name worked as written.
