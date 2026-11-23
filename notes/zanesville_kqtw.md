# zanesville_kqtw: Ohio: old Zanesville and the Y-Bridge
state: Ohio
region: oh
date: 2026-11-23
places: 12
file: data_zanesville_kqtw.py

## What this batch is
Twelve standing places in downtown Zanesville and Putnam, Ohio, where the Atlas had nothing within 15 km. Seven come from the names in one Old World Exploration video about the city (the record of every name is `source/videos/20231111_q9GZEtrU8O4.md`; the video is a tip and nothing rests on it): the Y-Bridge, St. Thomas Aquinas and St. Nicholas Catholic churches, the Muskingum County Courthouse, the 1904 post office and federal building, the John McIntire (Carnegie) Library and St. John's Lutheran Church. Five more stand within a kilometre and were taken from the Muskingum County Register list: St. James Episcopal Church, the 1926 YWCA (Bryan Place), the Black-Elliott Block, the Stone Academy museum in the Putnam Historic District, and Lock No. 10 and its canal on the Muskingum River. Facts are from Wikipedia (read with wiki_raw.py and page.py), the library's own history page, Muskingum County History, the St. Thomas Aquinas parish, St. James and St. John's own pages for service times, the county visitors' bureau pages, an ODNR river map PDF and a WHIZ news report. Every Register form tried at NPGallery was a placeholder. Pins are ArcGIS address points or Register list points, each looked at on the aerial; all fall on a building or, for the lock, on the lock canal. Red brick was settled from Commons photographs for nine places (the library, YWCA and St. John's are red brick; the rest stone or painted); St. Nicholas, the Stone Academy and the lock are '?'. Not checked: St. Nicholas's service times (its site refused), the library's opening hours (its hours page is drawn by script), the lock's season and hours (the ODNR park page was empty), the federal building's present use and owner, and every interior. The Stone Academy's own page and the visitors' bureau give different opening days: both are in the entry and it is marked mixed. The courthouse's date is given as both 1870 and 1874 by Wikipedia: both are in the entry.

## Leads
Places you read about and could not finish. One row each. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Putnam Presbyterian Church | Putnam, Zanesville, OH | Brick Gothic Revival, 1835, the oldest church building in Zanesville; first pastor William Beecher (Wikipedia, Putnam Historic District; WHIZ 2010) | Its address and pin, and its own page for service times (putnampresbyterian.org would not connect) |
| Pennsylvania (Pittsburg, Cincinnati and St. Louis) depot and the Belt Line freight house | Zanesville, OH (39.9428, -82.0100 and 39.9422, -82.0091, Register list) | On the National Register | Any source on what stands; both Register forms are placeholders at NPGallery |
| Clarendon Hotel | Main Street, Zanesville, OH | Built by Black and Elliott about 1878 (Wikipedia, Black-Elliott Block; a search result quoting the 1905 county history) | Whether any of it stands |
| Prospect Place | Trinway, north of Dresden, OH (40.1347, -82.0117) | 1856 abolitionist G. W. Adams mansion, Underground Railroad site, now an educational centre (Wikipedia) | Hours and access from its own page; outside this batch's town |

## Tips
- Every Muskingum County Register form tried at NPGallery (courthouse, post office, both Catholic churches, the Lutheran and Episcopal churches, the lock, the depot) is a placeholder: do not spend time on them.
- The Wikipedia redirect "St. Nicholas' Catholic Church (Zanesville, Ohio)" comes back empty from wiki_raw.py (it caches the redirect page); page.py on the article's new title read it.
- The ODNR Muskingum River Parkway page comes back with "No content found"; the park map PDF on dam.assets.ohio.gov reads, the water trail PDF answers 404.
- stnickparish.org and the library's hours page could not be read by page.py or the web fetch tool; stjameszanesville.org was refused by page.py but read by the web fetch tool.
- Cinema Treasures pages read well with page.py -g and settled which Zanesville theatres are gone.
