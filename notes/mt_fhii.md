# mt_fhii: Montana, a first scatter across the state: forts, missions, mansions, ghost towns and a coal mine
state: Montana
region: mt
date: 2026-11-20
places: 21
file: data_mt_fhii.py

## What this batch is
Twenty-one places spread across Montana, which had 14, all in the upper Clark Fork (region mt, taken with `choose.py --thinnest`): Elkhorn's two state-owned halls, Virginia City and Nevada City, the World Museum of Mining and the Copper King Mansion in Butte, the Cathedral of St. Helena, St. Mary's Mission and Fort Owen in the Bitterroot, Fort Missoula, the Conrad Mansion and Lake McDonald Lodge in the north-west, Old Fort Benton and the Grand Union Hotel on the Missouri, Fort Assinniboine near Havre, the Fort Peck Theatre, the Moss Mansion, Pompeys Pillar, the Livingston depot, the Smith Mine buildings at Bearcreek, and the Pierre Wibaux House and old St. Peter's church in Wibaux. Facts are from Wikipedia (wiki_raw.py), two National Register forms (Grand Union Hotel 76001121, Smith Mine Historic District 09000788), HMdb marker texts, and the managing bodies' pages read with page.py (FWP, BLM, Montana Heritage Commission, the cathedral parish, the Fort Missoula, Moss, Conrad and Copper King pages, the Fort Benton museums, the Glacier lodge concessioner). Not checked: hours for the World Museum of Mining (403), St. Mary's Mission (no hours on its site), the Grand Union Hotel and Fort Peck Theatre (sites drawn by script), the Livingston Depot Center, Fort Assinniboine (no page of the preservation association; Wikipedia's summer hours are quoted in the note only) and the Wibaux museum; the Conrad Mansion's regular season (only holiday hours were posted). The Smith Mine pin could not be checked: the aerial is under cloud at the pin and at the mapped mine area. The St. Peter's (Wibaux) pin is `area`: which nearby building is the 1895 church was not settled. Fort Owen gives both dates for the East Barracks (FWP 1857; Wikipedia's adobe of 1841-42); Fort Missoula's page gives two closing days. Nothing was checked on the ground. Eight Wikipedia coordinates were off their building (St. Mary's Mission's was on a Baptist church) and were moved to OpenStreetMap points.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort Keogh | Miles City, MT (Wikipedia 46.37556, -105.88333) | Wikipedia: 1876-78 army post, now a USDA livestock research station; parade ground, an 1883 wagon shed, the 1887 flag pole and seven other pre-1924 buildings remain | Whether the public may visit or see it from a public road; a page of the station |
| Bearcreek | Carbon County, MT (Wikipedia 45.16056, -109.1575) | Coal town of 1906; Wikipedia: only a few structures remain | What stands and is worth a visit; a source other than Wikipedia |
| Range Riders Museum | Miles City, MT | Wikipedia (Fort Keogh article): on the site of the first Fort Keogh cantonment | A page of the museum, what old buildings it holds |

## Tips
- In Montana the Wikipedia coordinates of standing buildings were often off by 75 to 400 m (8 of 21); `nom.py "<name>, <town>"` found most buildings, and `osmnear.py ... buildings -g 'church|mission'` found St. Mary's Mission when the name search did not.
- `fwp.mt.gov/stateparks/<name>` pages read well with `page.py`, but the hours sit in one line ("Seasons & Hours ... Open all year"): use `--all` and grep, as `-g` cuts the line at "9 a.m".
- miningmuseum.org answers 403; fortpecktheatre.org and fortbenton.com (Grand Union Hotel) are drawn by script; saintmarysmission.org/visit is 404.
- The Esri aerial is under cloud at Bearcreek (Smith Mine): `look.py` at 500 m was cloud too.
