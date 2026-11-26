# montreal_rrme: Montreal: old town and downtown
state: Quebec
region: qc
date: 2026-11-26
places: 19
file: data_montreal_rrme.py

## What this batch is
Nineteen standing buildings in Old Montreal, downtown and on the McGill campus, taken from the names in one walking-tour video (the record is `source/videos/20230721_6ySLSqEM0VQ.md`; the video was a tip only). Churches: Notre-Dame Basilica, Notre-Dame-de-Bon-Secours Chapel, Mary, Queen of the World Cathedral, St. James United, Saint Joseph's Oratory. Civic: City Hall, the 1856 courthouse (Édifice Lucien-Saulnier), the Old Custom House, Bonsecours Market, the Canadian Bank of Commerce on rue Saint-Jacques, the Sun Life Building, the old central fire station, the Macdonald Engineering Building and Redpath Hall. Also Place Viger and Windsor Station, the Redpath Museum, Royal Victoria College and the old Royal Victoria Hospital. Facts come from English Wikipedia (raw text), French Wikipedia for the courthouse, and McGill's building-history pages. Hours come from the pages of whoever runs each place, read on November 26, 2026. Pins are OpenStreetMap points, all checked on the aerial; the cathedral and the Oratory were moved onto their domes, and Place Viger, Windsor Station, the hospital and the fire station are marked `site`. Not checked: anything on the ground; what the old fire station and the Bank of Commerce are used for now; Pointe-à-Callière's hours apply to the museum as a whole; parking was not looked up building by building (they are downtown, by the metro). Red brick was set from Commons pictures for six places and left '?' for the rest.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Bell Telephone Building | Montreal, QC, Beaver Hall Hill | Named in the video as built 1927 to 1929 | A source; it is Art Deco, so check it is wanted |
| Macdonald-Stewart Library Building | Montreal, QC, McGill campus | Named in the video | A source and the pin |
| Mount Royal Hotel (Les Cours Mont-Royal) | Montreal, QC, rue Peel | Named in the video | A source on what is left of the hotel |
| Bonaventure Station, Saint-Henri station, Grand Union Hotel, Queen's Hotel, Queen's Hall, St. James's Club | Montreal, QC | Named in the video; likely gone | A source on when each went |

## Tips
- `wiki_raw.py` reads only English Wikipedia; a French article reads well with `page.py "https://fr.wikipedia.org/w/index.php?title=<Title>&action=raw"`.
- The Royal Victoria Hospital's Wikipedia coordinates are the new hospital at the Glen site; the old pavilions are on avenue des Pins (OpenStreetMap names them Pavillon A, H, M and so on).
- `hours.py page` read the basilica, the Oratory, the Marguerite Bourgeoys Museum, the archdiocese, Pointe-à-Callière and the City of Montreal pages at once; mcgill.ca/redpath answered 429, but mcgill.ca/redpath/visit read.
