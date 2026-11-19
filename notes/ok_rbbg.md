# ok_rbbg: Logan County, Oklahoma
state: Oklahoma
region: ok
date: 2026-11-19
places: 17
file: data_ok_rbbg.py

## What this batch is
Seventeen standing places in Logan County, Oklahoma, drawn at random by `choose.py` (region `ok`): in Guthrie, the territorial and first state capital, the Carnegie Library and Territorial Museum, Logan County Courthouse, Scottish Rite Temple, State Capital Publishing Company building, Santa Fe depot, Frontier Drugstore Museum (Gaffney Building), Pollard Theatre, Excelsior Library, Benedictine Heights Hospital, Guthrie Armory, Summit View Cemetery (Boot Hill) and the historic district itself; the Ozark Trails–Indian Meridian obelisk in Langston; Mulhall's 1894 Methodist church and 1908 sandstone bank; and Marshall's 1898 Methodist church and the Angie Debo House. Sources: the county's Register list (`wiki_raw.py --rows`), Wikipedia articles, Register forms read as text from NPGallery (`page.py -g`), the Oklahoma Historical Society's pages, the City of Guthrie's cemetery page, guthriescottishrite.org, drugmuseum.org, publishingmuseum.org, thepollard.org, one HMdb marker and two Waymarking pages. Not checked: nothing was seen on the ground; opening hours are recorded only for the Scottish Rite tours (the Territorial Museum, Drugstore Museum and Pollard pages read gave none, so `hours='?'`); present use and owner of the depot, the armory, the Mulhall bank and the Debo house; whether the Mulhall and Marshall churches still hold services (the forms are from 1984); where Boot Hill is inside Summit View (that pin is the cemetery office). Pins were checked on the Esri aerial; Oklahoma has no 1 m LiDAR in these tiles. The hospital pin was moved 55 m onto the building; the Mulhall church, Mulhall bank and Debo house pins are `area` because the building could not be picked out. Downtown places give street parking and no `th=` point. Red brick: four from a source or a 2006–2015 Wikimedia photograph (the Carnegie Library is tan brick, so `no`); four left `?`.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Langston University Cottage Row Historic District | Langston, OK (no coordinate on the Register list) | Five brick teacher cottages and three garages of 1930 and 1948 and 1947 stone and brick entry gates at the southwest corner of the campus, north of Highway 33; owned by the A&M regents (Register form 98001593) | A coordinate and the campus's visitor rules |
| Langston Jail | Langston, OK | Register listing 100011493 | The form is not on line at NPGallery (893 characters); no other source read |
| Melvin B. Tolson House | Langston, OK | Register listing 100012781, home of the poet | Same: the form is not on line; no coordinate |
| Victor Block and the other Foucart buildings | Guthrie, OK | Listed with addresses and years in the Wikipedia district article's table (from the 1998 NHL form) | Each could be its own place; only the district entry was written |
| Oklahoma Territorial Museum hours | 406 E Oklahoma Ave, Guthrie | The society's site page names a "Plan Your Visit" page | Its address: /sites/territorialmuseumvisit answered 404 and /sites/territorialmuseum/visit 500 |

## Tips
- Oklahoma Register forms on NPGallery read well as text (`page.py -g`), the 1984 ones included; 94001083 (Guthrie Armory) is a placeholder and 100011493 and 100012781 return 893 characters of nothing.
- `geo.py` PointAddress results put every Guthrie street address on its building; the Wikipedia point for the Carnegie Library is about 300 m off.
- Web searches for Guthrie museums returned link lists with no quoted text, so hours could not be taken from search results.
- guthriescottishrite.org reads with `page.py` (its home page gives the tour times); its `?p=` subpages answered 409 or reset the connection.
