# nny_tughill_bmwh: Northern Lewis County & Tug Hill: Lowville, Croghan, Beaver Falls, Pinckney
state: New York
region: nny
date: 2026-11-24
places: 14
file: data_nny_tughill_bmwh.py

## What this batch is
Fourteen little-known places in northern Lewis County, chosen because they are obscure: the remains of the Lowville & Beaver River Railroad (Croghan depot and turntable, the Lowville yard, the Black River bridges at New Bremen, the Beaver Falls trestle and depot), the Croghan island mill, the Adirondack Mennonite Heritage Farm, the Beaver Falls Grange hall, the Lewis house at Beaver Falls, Pinckney Corners Cemetery on Tug Hill, and four Lowville buildings (the stone church, the Franklin B. Hough house, the Masonic temple that holds the county historical society, the Bateman Hotel) with the soldiers' monument. Sources were read through a web reader: the 2024 L&BR Register nomination (parks.ny.gov), NPGallery nominations, historypointer.com, Pomeroy Foundation marker pages, Wikipedia, the county rail-trail page, historicallylewis.org and the museums' own pages. Pins were set from nomination UTM references, ArcGIS address points and OpenStreetMap buildings, and looked at on the New York leaf-off aerial and LiDAR. Not checked: anything on the ground; the Croghan depot museum's hours (the only hours found carry no date, so hours='?'); present owners and use of the Grange hall, the Lewis house and the Hough house; the colour of the Lowville yard dining house and the Hough house (brick='?'). The L&BR bridge figures differ between the nomination and Wikipedia; both are given.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Osceola Town Hall (1882 church) | Osceola, NY; Register point 43.50306, -75.7225 falls in a field | Register lists an 1882 church used as town hall | No source ties it to the town building at 1426 Osceola Rd; pin |
| Hooker, Parker sawmill, Sears Pond sawmill, Montague churches | Town of Montague, NY | historicallylewis.org/?p=221 describes the vanished hamlet and mills | No source says anything is left; sites unpinned |
| Dannatburg | Town of Watson/Greig, NY | historicallylewis.org/?p=1887: vanished settlement, washed-out bridge abutment | Pin for the abutment; whether it can be reached |
| Pinckney Corners M.E. church | Pinckney Corners, NY, across from the cemetery | Gone; named in an 1873 gazetteer | Whether a foundation shows |
| Deer River Station ruin | 43.93425, -75.57639 (OpenStreetMap ruin) | Mapped ruin beside the working MA&N track | What it was; any source |
| Barnes Corners, Petries Mill | Tug Hill, NY | Vanished hamlets on the old names list | Any source with remains |
| Old Lowville Cemetery, Basselin House, Stoddard–O'Connor House, Lewis County Fairgrounds | Lowville, NY | Register rows | Not read |

## Tips
- page.py failed (refused or no connection) for parks.ny.gov, npgallery, nps.gov, hmdb.org, historicallylewis.org and historypointer.com here; a web-reader agent read them all.
- The 2024 L&BR nomination gives UTM references for every resource along the line: the quickest way to pin all of it.
- HMdb 158327 is a Ticonderoga marker, not Croghan; nps.gov "industry in the Beaver Valley" is about Delaware.
- The geocoder put 7707 N State St and 7574 S State St, Lowville, on the wrong streets; check address points against the aerial.
- maplemuseum.com (American Maple Museum, Croghan) now redirects to another domain, so it was left out.
- The Pomeroy marker page for the Beaver Falls Grange gives a point 300 m from the hall.
