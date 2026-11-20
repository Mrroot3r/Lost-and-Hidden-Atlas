# nc_qvkt: North Carolina: a first scatter from the Smokies to the Outer Banks
state: North Carolina
region: nc
date: 2026-11-20
places: 16
file: data_nc_qvkt.py

## What this batch is
Sixteen places spread across North Carolina, which had 13 (all round Winston-Salem, plus Brunswick Town): Mingus Mill and the Caldwell house at Cataloochee (Great Smoky Mountains), Henry River Mill Village, Reed Gold Mine, Gold Hill Mines Historic Park, Yates Mill, Stagville (Bennehan House and Horton Grove), the 1767 Chowan County Courthouse in Edenton, St. Thomas Church in Bath, Somerset Place, Hope Plantation, Fort Macon, Portsmouth Village, Bodie Island Lighthouse and Fort Fisher. Facts from Wikipedia (tools/wiki_raw.py) and the managing bodies' pages read with tools/page.py: historicsites.nc.gov (every state historic site page gave hours and fees), ncparks.gov, nps.gov (places pages for Mingus Mill and Caldwell Place, Cape Lookout visitor centers, Cape Hatteras lighthouse climbs), wake.gov, hopeplantation.org, historicgoldhill.org, stthomasparishnc.org and henryrivermillvillage.com. Nothing was checked on the ground. Not checked: Hope Plantation's hours (its site gave none), Yates Mill park hours, Cataloochee road conditions, Mingus Mill reopening (interior closed when read), whether every Edenton tour enters the courthouse, the Bennehan House pin (a building in the clearing at the address point, not confirmed as that house), and the Hope pin (address point on the lane, prec area; the Wikipedia coordinate is 16 km off). Red brick: Chowan courthouse yes, Fort Macon some, Bodie Island, Caldwell house and Fort Fisher no, from article photographs or sources; the rest '?'. Fort Dobbs was left out: what stands is the 2016-2019 reconstruction. West Point on the Eno was left out because Wikipedia says Durham closed the park for about six months from July 2026 for renovation.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Endor Iron Furnace | Cumnock, Lee County, NC (35.55018, -79.22447, Wikipedia) | Stone furnace about 32 ft square and 35 ft high; dates differ: 1861-64 and 1870-71 (Wikipedia), until 1874 (Lee County), ceased 1876 but ran small until 1896 (DNCR blog). Owner given as Triangle Land Conservancy (Wikipedia) or the state Department of Cultural Resources (Lee County) | A managing body's page saying the public may visit, and a parking spot; the Sanford greenway named for it does not reach it yet (sanfordnc.net) |
| West Point on the Eno | Durham, NC (36.06972, -78.90861) | City park with West Point Mill (mill shut 1942, NRHP 1985) | Whether the park has reopened after the renovation that began July 2026 |
| Palmer Chapel and Beech Grove School, Cataloochee | Haywood County, NC (Palmer Chapel 35.62663, -83.10931, OpenStreetMap) | Named by the NPS history page as standing; mentioned in the Caldwell house entry | A page with their dates and what is inside, for entries of their own |
| Old Burke County Courthouse | Morganton, NC (35.74556, -81.6875) | In use by 1837, restored 1984, houses the Heritage Museum and Historic Burke Foundation (Wikipedia) | The foundation's page for hours |

## Tips
- historicsites.nc.gov pages read cleanly with page.py --all and give hours, fees and tour times for every NC state historic site; ncparks.gov park pages do too.
- Hope Plantation's Wikipedia coordinate (36.1775, -77.01917) is about 16 km north of the house; geocoding the foundation's address (132 Hope House Road, Windsor) was closer. Check Wikipedia coordinates in eastern NC against an address.
- nps.gov/places/<name>.htm pages answer page.py where the older planyourvisit pages (Cataloochee, Portsmouth Village) now give 404.
- The public-land map puts Fort Fisher's earthworks in "Military Ocean Tml Sunny Point" (XA); the state historic site owns them.
