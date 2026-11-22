# conf_zmqk: Mechanicville churches, Colonie farmhouses, Clifton Park burying grounds
state: New York
region: albco, conf, sar
date: 2026-11-22
places: 10
file: data_conf_zmqk.py

## What this batch is
Ten places round the edges of region `conf` (drawn at random by `choose.py --state ny`). Cohoes, Waterford village, Watervliet, Green Island, Crescent and Newtonville were already worked closely, so this takes what was still missing a little further out. Mechanicville: St. Paul the Apostle Church (1912–1917, sandstone, Wikipedia) and the old St. Luke's Episcopal Church (1897–98, the city historian's article "Seeing the Light"; OpenStreetMap now calls the building the Arts Center on the Hudson, present use not checked). Waterford: the Isaac Eddy House (1826, HMdb). Colonie (filed `albco`): the Martin Dunsbach, Isaac M. Haswell and Friend Humphrey houses from the 1985 Colonie survey (Wikipedia, addresses from historypointer.com's copies of the Register entries). Rexford: the Cyrus Rexford House (Wikipedia, Register 2011). Halfmoon and Clifton Park: three small burying grounds known from markers (Millious Cemetery with the North Church site, the Moe family cemetery, the Newtown Baptist burying ground). Sources were read with `wiki_raw.py` and `page.py`; pins came from the ArcGIS geocoder (PointAddress matches except Haswell, which is interpolated), OpenStreetMap or HMdb, and were all looked at on the aerial and LiDAR. Not checked: Mass times at St. Paul's (the parish site allsaintsny.us answered 403), whether the old St. Luke's opens to anyone, whether the Colonie houses still look as the 1985 listing describes, and where exactly the Millious and Moe cemeteries lie (no gravestones show near their markers on the leaf-off aerial). Nothing was visited.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Halfmoon Academy building | Halfmoon, NY (HMdb 128389, Church Hill Road, 42.82722, -73.71935) | HMdb: private school chartered 1851–1877, then District No. 1 common school until 1951 | Whether the building stands; the town's "Early Halfmoon Schools" page (townofhalfmoon-ny.gov/node/18581) answered 403 |
| Anthony spice factory site | Halfmoon, NY (HMdb 125354, Anthony Road at Farm to Market Road, 42.88565, -73.76350) | HMdb: Joshua Anthony's baking-powder and spice works, 1859 to 1920 | Whether anything is left to see |
| Clifton Park Village general store | Clifton Park, NY (HMdb 198016, 1716 US 9, 42.86509, -73.77043) | HMdb: store and post office of about 1850 beside the Clifton Park Hotel; HMdb's 136089 page says the buildings were condemned | Whether it stands; could be folded into clifton-park-hotel |
| First Methodist Church, Mechanicville | 7 North Main Street (OpenStreetMap, 42.90333, -73.68697) | City historian: its bell on North Main Street was rung as the fire alarm; Wikipedia: one of two active churches in the city | Its building date and a source on the building |
| Brookwood (Widow Peebles Tavern site) | Halfmoon, NY (HMdb 129189, US 4 at Brookwood Road, 42.83870, -73.67361) | HMdb: Thomas Peebles bought the site in 1760; the Widow Peebles Tavern is on a 1779 map | Whether any old building stands |

## Tips
- historypointer.com's Register pages (`historypointer.com/nris/resource/<ref>`) give the street address for the Colonie survey houses, whose Wikipedia list rows have no coordinates; `page.py --all` reads it even when it says DRAWN BY SCRIPT.
- NPGallery's text route gave placeholders for all four Register forms tried here (1985 Colonie survey and the 2011 Cyrus Rexford House).
- The City of Mechanicville's historian articles (`mechanicvilleny.gov/<Title>`) read with `page.py --all`; several `node/<n>` addresses search results give answer 404.
- HMdb answered 429 after about twenty marker pages in a row; a few seconds' wait between pages was enough.
