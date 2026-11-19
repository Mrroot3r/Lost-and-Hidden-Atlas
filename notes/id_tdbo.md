# id_tdbo: Idaho: Boise, the Boise Basin and the Owyhee country
state: Idaho
region: id
date: 2026-11-19
places: 19
file: data_id_tdbo.py

## What this batch is
The first full batch for Idaho (region drawn at random by `choose.py`): 19 places in southwestern Idaho. The Boise Basin gold camps (Idaho City's district, St. Joseph's church, the Boise Basin Museum, the territorial jail building, the Masonic and Odd Fellows halls, the courthouse, the pioneer cemetery; Placerville and its two museums), Arrowrock Dam, Boise (Old Idaho Penitentiary, the Assay Office, the O'Farrell Cabin, the Union Pacific depot), and the Snake River and Owyhee country (Swan Falls Dam powerhouse, the Guffey Railroad Bridge, Silver City, the lava-rock church at Oreana, the Wickahoney stage station ruin). Sources: Register forms read as NPGallery text PDFs with `page.py` (Idaho City 75000626, Assay Office NHL 66000305, Oreana 80001333, Wickahoney 82002514), Wikipedia with `wiki_raw.py`, HMdb marker pages (an HMdb nearby list round Idaho City gave positions for most of the town), and the managers' pages for the Old Pen (ISHS), the Boise Depot (City of Boise), Swan Falls (Idaho Power, BLM), Celebration Park and Silver City (BLM). Not checked: anything on the ground; hours for the Boise Basin Museum (the foundation's site is drawn by script), Placerville's museums (from Wikipedia only), Celebration Park (Canyon County's page answers 404) and Arrowrock Road; owners of the Idaho City jail building, the pioneer cemetery, the Oreana church and the Wickahoney ruin (the 1982 form called Wickahoney private, so it is look-only); winter road conditions to Silver City. The Boise Depot is closed for restoration until about August 2027. Two dates disagree and are given both ways: the I.O.O.F. Hall (form 1855, marker 1875) and the courthouse (form 1870 as a hotel, marker 1871 as a store). Pins that mark a general area: Idaho City (town centre), Silver City (town centre); the Old Pen has no checked lot.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| De Lamar ghost town | Owyhee County, ID (43.02444, -116.83139) | Mining camp of 1888, Register district 1976 with four contributing buildings (Wikipedia) | Who owns the land now (mining claims round it) and whether anything can be seen from a public road |
| Pon Yam House | Idaho City, ID | 1867 store of a Chinese merchant, one of the few survivals of the Chinese town (Wikipedia; HMdb marker 119061 nearby) | Its position, owner and whether it opens |
| Fort Boise (1863 army post) | Boise, ID (43.61980, -116.19426, HMdb 267460) | HMdb says many original buildings of 1863 on are still in use | Which buildings survive and who lets the public see them (the VA grounds) |
| Ada Odd Fellows Temple | Boise, ID (43.616111, -116.204167) | Register list says only parts of the facade still stand | A source on what is left and where |
| Poison Creek Stage Station | Homedale, ID (43.502201, -116.938278) | Register 78001089 | Form not read; owner and access |
| Bruneau Episcopal Church | Bruneau, ID (42.880603, -115.800945) | Register 82000356 | Form not read; brick and access |
| Barber Dam and Lumber Mill | Boise, ID (43.562222, -116.121111) | 1904–06 timber-crib dam, still working (Wikipedia) | Whether anything of the 1906 mill survives |

## Tips
- Idaho Register forms tried (1974 to 1982) all had text layers that `page.py` read; HMdb coverage is dense round Idaho City and Boise's North End, and one nearby list gave positions for most of Idaho City.
- `idahocityhistoricalfoundation.org` is drawn by script and `idahocitychamber.org` resets the connection; museum hours for Idaho City were found only quoted on Clio.
- `canyoncounty.id.gov` park pages answer 404 with no usable archived copy; the BLM's Celebration Park page covers the Guffey bridge.
- `parking.py` lists nothing near Arrowrock Dam or Silver City.
