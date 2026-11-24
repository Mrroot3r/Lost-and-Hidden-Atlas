# southbridge_hjsb: Massachusetts: old Southbridge, from Elm Street to the mills
state: Massachusetts
region: worc
date: 2026-11-24
places: 10
file: data_southbridge_hjsb.py

## What this batch is
Ten places in Southbridge (Worcester County), where the Atlas had nothing within 8 km, from a "videos" session (job 9) working one Old World Exploration video about Southbridge (the record is `source/videos/20261002_AzXuV8WNDEM.md`; 31 names: 10 places added, 7 gone, 3 not found, 9 not checked). Added: Notre Dame Catholic Church (1912 to 1916), Southbridge Town Hall (1888), Elm Street Congregational Church (1885), the Elm Street (1899) and Globe Village (1894) fire houses, the American Optical main plant (now the Wellsworth Hotel), the Hamilton Woolen Company Big Mill and Brick Square, Central Mills, the Sacred Heart Church group (closed, sold in 2018) and Centre Village on Main Street. Facts are from Wikipedia (read with `wiki_raw.py`), the Worcester Business Journal and Global Traveler on the hotel, and search-result quotations of the diocese's paper (Notre Dame's loose marble facing) and the Associated Press (the 2018 Sacred Heart sale); the parish site (stjp2parish.org and its news pages on ecatholic.com) answered 403 to `page.py` and the web fetch tool, so no church hours were taken and both active churches are `view`. Red brick was settled for nine places from the Wikipedia article's photograph; Centre Village is `?`. Not checked: anything on the ground, interiors, the town hall's office hours, the hotel's present trading after a mortgagee-sale listing, what has become of Sacred Heart since 2018, and the Globe Village Fire House's present use (its pin marks only the corner of West and Main streets, `prec='area'`). Every place had a picture from its article, so there is no pics file.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| St. Mary Church | Southbridge, MA (247 Hamilton Street, at Marcy Street; OpenStreetMap 42.08032, -72.03648) | Notre Dame's Wikipedia article: one of the two churches of the Parish of Saint John Paul II, with the parish center and rectory | Any source on the building's date and design; the parish site refuses requests |
| Southbridge National Bank | Southbridge, MA (south side of Main Street between Elm and Everett streets) | Digital Commonwealth photo records: built 1930 by F. X. Laliberte & Co., 1929 over the door, four columns at the entrance | Whether it still stands, and a pin |
| Strand Theatre site | Southbridge, MA (18 Elm Street; the alley Strand Place) | Cinema Treasures pages: opened 1926 in the old Hippodrome, last show 1965; commenters disagree on when it was pulled down | A source better than commenters; likely nothing left to see |
| Civil War monument | Southbridge, MA, in front of the town hall | Seen beside the town hall in the Wikipedia photograph | Its date and maker from a source (HMdb or the town) |
| Central Street bridge | Southbridge, MA, over the Quinebaug | Old postcards call it the Central bridge, a stone arch bridge | Whether the stone bridge stands, its date |

## Tips
- stjp2parish.org and 18271.sites.ecatholic.com (the Worcester diocese's paper) answer 403 to both `page.py` and the web fetch tool; search-result text is the only way in.
- The Massachusetts Historical Commission town report address that searches give (sec.state.ma.us/.../town-reports/sbd.pdf) is 404 with no archived copy.
- Southbridge's Register list rows have Commons photographs for nearly every building, so `brick.py look` settles brick quickly here.
