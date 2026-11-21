# oh_cmhg: Ohio: a first scatter from Lake Erie to the Ohio River
state: Ohio
region: oh
date: 2026-11-21
places: 14
file: data_oh_cmhg.py

## What this batch is
Fourteen places spread across Ohio, which had 20 (18 of them in Licking County). Ground taken with `choose.py --thinnest`. Northeast and the lake: Squire's Castle (ruined gatehouse, North Chagrin Reservation), the Ohio State Reformatory at Mansfield, Zoar Village, Marblehead Lighthouse. Northwest and west: Lock 44 and the Isaac Ludwig Mill at Providence Metropark, the Miami and Erie Canal Deep Cut near Spencerville, Bear's Mill near Greenville, Piatt Castle Mac-A-Cheek at West Liberty. Southwest: the Golden Lamb at Lebanon, Fort Ancient. Southeast: the Rufus Putnam House (Campus Martius Museum) and Mound Cemetery in Marietta, Hope Furnace at Lake Hope, Buckeye Furnace. Sources: Wikipedia with `wiki_raw.py`; hours from the runners' own pages with `page.py` (Cleveland Metroparks FAQ, mrps.org FAQ, historiczoarvillage.com, marbleheadlighthouseohio.org, piattcastles.org, mariettamuseums.org, metroparkstoledo.com, hopewellearthworks.org). Not checked: anything on the ground; hours of the Golden Lamb, Bear's Mill, Buckeye Furnace (ohiohistory.org 403), Hope Furnace and the Deep Cut park, Mound Cemetery; owner of Mound Cemetery beyond Wikipedia's "city cemetery". Pins: the Reformatory (moved onto the old building's centre tower) and Zoar (moved off a house onto the central garden) were moved with `pix.py`; Zoar, the Deep Cut and Fort Ancient are prec area. Brick: Piatt 'some' from a Commons photo (red brick chimneys); Reformatory, Golden Lamb, Zoar, Putnam House, Providence and Buckeye Furnace left '?'. Zoar got no picture (only a 1936 photo of one house).

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Lanterman's Mill | Mill Creek Park, Youngstown, OH | Wikipedia (Mill Creek Park): built 1845–46 by German Lanterman and Samuel Kimberly, restored 1982–85 | Mill Creek MetroParks' site would not connect; hours, pin and parking |
| Ohio and Erie Canal locks 26–30 at Lockbourne | Lockbourne, OH (OSM ruins 39.819, -82.961 to 39.810, -82.972) | Wikipedia: the village is named for the canal locks; a photo caption names Lock 30 in Lock Meadows Park | A source on what is left of each lock and who owns the ground |
| Everett Road Covered Bridge | Cuyahoga Valley National Park, OH | Not read: no Wikipedia article under that title and the NPS page answered 404 | A readable NPS page |
| Mac-O-Chee (Donn Piatt's castle) | West Liberty, OH | Wikipedia: finished 1879, sold by the family in 2019 to local residents | Whether it can be seen from the road or visited |

## Tips
- ohiohistory.org still answers HTTP 403 to `page.py`; hopewellearthworks.org carries Fort Ancient's hours, and mariettamuseums.org (the Northwest Territory Museum Society) carries Campus Martius's.
- The ODNR park pages (ohiodnr.gov/.../parks/<name>) come back as an empty portal shell ("No content found"); the Marblehead Lighthouse Historical Society's own site has the tower hours.
- bearsmill.com resets the connection and jampd.com (Johnny Appleseed Metroparks) is drawn by script; millcreekmetroparks.org would not connect.
- The Ohio State Reformatory's Wikipedia coordinate is in the field west of the building, about 200 m off.
