# south_tfzr: New Bedford, Fairhaven and Dartmouth: whaling port, Rogers buildings, a 1670s garrison
state: Massachusetts
region: south
date: 2026-11-19
places: 16
file: data_south_tfzr.py

## What this batch is
Sixteen places round New Bedford harbour, where the Atlas had only Fort Taber and Lincoln Park (region drawn at random by choose.py). New Bedford: the Seamen's Bethel, the U.S. Custom House, the Old Third District Courthouse (the national park's visitor center), the Rotch-Jones-Duff House, the Nathan and Polly Johnson House, Fire Station No. 4 (Fire Museum), the Wamsutta Mills (now apartments), and the Palmer Island and Butler Flats lights. Fairhaven: Fort Phoenix, the Millicent Library, Town Hall, the high school ("Castle on the Hill") with the 1798 Academy, and the Unitarian Memorial Church. Dartmouth: the Russell Garrison foundation (King Philip's War) and the 1791 Apponegansett Meeting House. Sources were Wikipedia read with wiki_raw.py, HMdb marker pages, and the managing bodies' pages read with page.py (nps.gov, rjdmuseum.org, millicentlibrary.org, uufairhaven.org, nbhistoricalsociety.org, savebuzzardsbay.org, lighthousefriends.com). Brick was settled from what sources say a place is built of, or from Wikipedia pictures opened with brick.py look (Millicent Library, Fairhaven Town Hall, the high school); the rest are '?'. Not checked: nothing on the ground; the Seamen's Bethel's daily times, the visitor center's hours and the Fire Museum's (Wikipedia only: July 4 to Labor Day), Fort Phoenix's DCR hours, Fairhaven Town Hall and visitor center hours (fairhaven-ma.gov 403), and the Apponegansett Meeting House's owner and summer meeting times. The Apponegansett pin is the one building in a clearing that fits the description (south of Russells Mills Road, just east of Fresh River Valley Road); the Register point was on houses west of the junction. Butler Flats could not be seen: the MassGIS aerial stops short of it. PAD-US marks the Russell Garrison parcel closed (XA) where Wikipedia and HMdb call it a town park.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Union Street Railway Carbarn and Repair Shop | New Bedford, MA (41.651944, -70.931111) | On the National Register (78000431) per the Wikipedia New Bedford Register list | No article; the Register form and the building's present use were not read |
| Paul Cuffe Farm | Westport, MA (41.5492, -71.0683) | National Historic Landmark, c. 1780 house; Wikipedia says the Cuffe attribution is now doubted | Reached by a long private drive; no public viewpoint found |
| Long Plain Friends Meetinghouse and Long Plain School (museum) | Acushnet, MA (41.7472, -70.9019 and 41.7375, -70.8965) | On the Register list; the school is now the Long Plain Museum | Not read; museum hours not looked for |
| Fairhaven Academy (Fairhaven visitors' center) | Fairhaven, MA (about 41.6428, -70.9068) | 1798 academy, visitors' center and historical society museum (Wikipedia, in the high school entry) | Its own hours: fairhaven-ma.gov answered 403 |

## Tips
- fairhaven-ma.gov answers 403 to page.py, and the archived copy page.py names could not be fetched either.
- rjdmuseum.org/hours-and-admission is drawn by script; rjdmuseum.org/visit/ reads cleanly and carries the hours and fees.
- The NPS hours page for New Bedford Whaling NHP (nps.gov/nebe/planyourvisit/hours.htm) read as "Page In-Progress" in November 2026; the visitor center page gives no times.
- wiki_raw.py on "Rotch–Jones–Duff House and Garden Museum" (and its redirect "William Rotch Jr. House") returned only a redirect to itself; the museum's own about page had the history.
- The ArcGIS geocoder (geo.py) gave PointAddress hits on the building for every downtown New Bedford and Fairhaven address tried; Register points were off at Wamsutta Mills (on Route 18) and the Apponegansett Meeting House.
- The MassGIS aerial does not reach Butler Flats in the outer harbour: the tile is blank.
