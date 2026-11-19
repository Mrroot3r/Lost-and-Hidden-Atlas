# az_qhns: Cochise County, Arizona
state: Arizona
region: az
date: 2026-11-19
places: 17
file: data_az_qhns.py

## What this batch is
Seventeen places in Cochise County, Arizona, the first county batch in the state (only Fairbank was on the map). Ruins: Presidio Santa Cruz de Terrenate (1775), Fort Bowie, the Millville mills and Charleston, Dragoon Springs stage station, Courtland jail. Standing: Tombstone Courthouse, St. Paul's Episcopal, Sacred Heart and the Bird Cage Theatre in Tombstone; Gleeson jail; Pearce General Store and Our Lady of Victory church; the Cochise Hotel; the Gadsden Hotel in Douglas; the Phelps Dodge office (Bisbee Mining and Historical Museum); Slaughter Ranch; Faraway Ranch. Sources: Wikipedia read with `wiki_raw.py` (the Cochise County Register list with `--rows`), the managing bodies' pages read with `page.py` (BLM's Terrenate and San Pedro pages, NPS Fort Bowie and Chiricahua pages, Arizona State Parks' Tombstone Courthouse page), HMdb (Dragoon Springs, Phelps Dodge office), Arizona Highways' Ghost Town Trail page, a Friends of the San Pedro River event listing (Millville trailhead). Not checked: hours for the Bird Cage, Gleeson jail (only a travel guide's), Bisbee museum, Slaughter Ranch (visitarizona.com gave 403), the churches, the hotels and Faraway Ranch tours; who owns the Courtland townsite, the Pearce store and the Cochise Hotel; whether the Arizona State Land Department permit HMdb mentions is really needed for the Dragoon Springs road. Nothing was seen on the ground. Pins that mark an area and not the thing: Courtland (townsite coordinate, the jail not identified on the aerial), Millville (a trail point; the mill walls not identified). The Pearce General Store pin was put on the corner building from the aerial and the Register summary's description alone. Brick: Cochise Hotel set from Wikipedia's 2013 photo (stucco and clapboard); courthouse and Phelps Dodge office from the articles' text (red brick); adobe, stone and concrete places 'no' from the sources' materials; five left '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Contention City | Cochise County, AZ (31.76889, -110.20194) | Wikipedia: 1879 mill town on the San Pedro, now scattered adobe walls, cellar holes and a small cemetery in BLM's San Pedro Riparian NCA, reached by paths along the river | A BLM page naming the trailhead; the walls not looked for on the aerial |
| Brunckow cabin | near Tombstone, AZ | Known adobe ruin on the San Pedro (memory only) | No source opened |
| Benson Railroad Historic District, Hi Wo grocery, Max Treu meat company | Benson, AZ (31.9694, -110.2947) | Register rows in Cochise County list | No article or description read |
| Douglas Grand Theatre, El Paso and Southwestern depot and YMCA | Douglas, AZ | Register rows; Grand Theatre has an article | Not read |
| Barfoot and Silver Peak lookouts, Portal ranger station | Chiricahua Mountains, AZ | Register rows (CCC lookouts, 1930s) | Coronado NF access and condition |
| Tombstone City Hall | Tombstone, AZ (31.713333, -110.066667) | Register row | No article read |

## Tips
- `page.py` read blm.gov and nps.gov pages in full; on nps.gov the `/places/<name>.htm` quick facts gave "open to public: no" for the Faraway Ranch house, which the history pages do not say.
- Wikipedia coordinates for the Cochise Hotel (1 km off, in a field), Our Lady of Victory (75 m) and Pearce General Store (on the road) were wrong; `nom.py` had the hotel and the church right.
- In the desert the `--lidar` sheet showed what the aerial did not: the square enclosure of the Terrenate presidio and the building outlines at Fort Bowie.
- `parking.py` gave the Tombstone courthouse an empty dirt field as the nearest "lot"; it was dropped.
- `brick.py look` waits out Wikimedia's refusals for a long time: a loop over three places ran past a two-minute shell limit.
