# ns_spvy: Lunenburg County, Nova Scotia
state: Nova Scotia
region: ns
date: 2026-11-20
places: 21
file: data_ns_spvy.py

## What this batch is
Twenty-one places in Lunenburg County, the first in the county. Old Town Lunenburg (the 1753 model town, one entry for the district), St. John's Anglican (1754–1763, burned 2001 and rebuilt), the Knaut-Rhuland House Museum (1793), the Lunenburg Academy (1895), Zion Lutheran (1890) and St. Andrew's Presbyterian (1828), the Walters Blacksmith Shop (Bluenose ironwork) and the Fisheries Museum of the Atlantic; Mahone Bay's Three Churches on Edgewater Street; the Chester train station (c. 1905) and the Old Methodist Church (now a house, view only); Ross Farm Museum with Rosebank Cottage (1817) and Christ Anglican (1876) at New Ross; the Wile Carding Mill (1860) in Bridgewater; Fort Sainte-Marie-de-Grâce (1632, site eroded, cairn) with Fort Point Museum at LaHave; the two marine-access churches of the LaHave Islands (1903 and 1913, one now the marine museum); St. Barnabas' at Blue Rocks and the Union Church at Indian Point. Every place's history is from its Canadian Register statement (historicplaces.ca, read with `page.py --all -n 60000`, about 4 seconds between pages); hours from the museums' own pages (Lunenburg Heritage Society, Fisheries Museum, Ross Farm, LaHave Islands Marine Museum) and the Town of Bridgewater (Wile mill hours are the 2025 reopening hours). Not checked: service times for any of the churches (all `view`), whether St. John's Lunenburg opens for visitors, Fort Point Museum and the Chester visitor centre hours (`hours='?'`), the Lunenburg Academy's present owner and whether visitors may go in (`conf='mixed'`), road-side parking at the country churches and the LaHave Islands. No 1 m LiDAR in Canada for the pin check; all pins checked on the Esri aerial. Christ Anglican, New Ross, is `prec='area'` (the Register point is on the road junction). Red brick: `no` for the wooden buildings the Register describes as clapboard or shingle; `?` where a chimney or several buildings left it open.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| The Ovens gold-rush remains | Ovens Natural Park, 326 Ovens Park Rd, Riverport, NS | The park's own page: 1861 gold rush, a town of over a thousand miners; the Cunards dredged the beach; "remnants of the gold mining efforts" in many parts of the park; a small Gold Rush Museum | Where the remnants are, a pin (nom.py and geo.py found no point), the park's hours and fees (its rates page is gone) |
| East Ironbound lighthouse | East Ironbound Island, Mahone Bay (Register id 13073; 44.4395, -64.0832) | 1870 combined light and dwelling, still a working light (Register) | Who owns the island and whether anyone may land; boat access |
| St. Matthew's Lutheran Church | Rose Bay, NS (Register id 5684; 44.2984, -64.3062) | 1897 Gothic Revival church by H. F. Busch, built by Boehner Bros. (Register) | Not written up for time; pin not checked |
| St. Stephen's Anglican Church | Chester, NS (Register id 11326; 44.5415, -64.2423) | Register page read, not written up | Write-up and pin |
| Bayview Cemetery (Mush-a-Mush burying ground) | Mahone Bay (Register id 12008; 44.4534, -64.3812) | The Three Churches statements name it as the old burying ground, site of the first Anglican and Presbyterian churches | Its own Register statement not read |
| Lunenburg Town Hall and Old New Town School | Lunenburg (Register ids 1611 and 2688) | Town Hall 1891–1893 by H. F. Busch (per the St. Matthew's statement) | Their own statements not read |

## Tips
- In the Wikipedia "List of historic places in Lunenburg County, Nova Scotia", most rows carry only a municipal id (`idm=`); those are historicplaces.ca ids too, as the Annapolis note says. `wiki_raw.py --rows` reads none of them (it looks for NRHP rows): split the raw file on `{{HPC row`.
- historicplaces.ca reset the connection on 3 of 22 pages at a 4-second pace; a second try 6 seconds later read all three.
- The Register list point for St. Andrew's Presbyterian, Lunenburg, fell on another house; `osmnear.py ... buildings -g Andrew` found the church. OpenStreetMap had most Lunenburg County churches and museums by name (`nom.py`).
- `parking.py` gave a "lot" on Victoria Road, Bridgewater, that is the road itself on the aerial; not used.
- The pin check has no 1 m LiDAR for Nova Scotia: every tile says NO 1 m LiDAR HERE.
- cardingmill.novascotia.ca serves the Nova Scotia Museum's general pages (its /node/89 was a Parrsboro event); the Wile mill's hours were on the Town of Bridgewater's page. fortpointmuseum.com gives no hours on any page read.
