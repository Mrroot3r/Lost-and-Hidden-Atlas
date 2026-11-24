# nb_mdvp: Saint Andrews to Caraquet: churches, courthouses and museums of New Brunswick
state: New Brunswick
region: nb
date: 2026-11-24
places: 16
file: data_nb_mdvp.py

## What this batch is
Sixteen places across New Brunswick (53 before, 69 after), picked from the National Historic Site list and the county lists of the Canadian Register of Historic Places: Greenock Church and the Charlotte County court house and gaol (Saint Andrews), Connell House (Woodstock), Belmont House (Lincoln), the Fredericton Military Compound, Tilley House (Gagetown), Rothesay station, Hammond House (Sackville), the Free Meeting House (Moncton), the Kent Museum convent (Bouctouche), the Saint John County Court House and Mechanics' Engine House, Bonar Law House (Rexton), the church at Caraquet, the Richibucto ballast heaps and Kedgwick station. Every Register statement was read with page.py --all. Pins came from the ArcGIS address geocoder and were looked at on the Esri aerial; Greenock's and Hammond's were moved to OpenStreetMap's building. Belmont House and Bonar Law House could not be picked out on the aerial and are marked prec='area'; Rothesay's pin is Wikipedia's coordinate (on a building by the tracks). Opening times came only from web search results that quote the managing bodies' pages (the pages themselves were not opened), and several sources disagree, so each says to confirm. Not checked: interiors, parking (no th= points given), whether Belmont, Rothesay, Hammond and Kedgwick are open, services at the two churches, and no on-the-ground look at anything. Commons pictures were chosen for 12 places; Connell House, Belmont, Tilley House, Hammond House, Kedgwick and the ballast heaps have none.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort Jemseg site | Jemseg, NB (45.7685, -66.1322) | National Historic Site; 1659 trading post | Anything to see above ground; public access |
| Fort Nerepis | Grand Bay-Westfield, NB | National Historic Site (1659 fort) | Site, what is left, access |
| Denys Fort / Habitation | Shippagan, NB (47.8813, -64.5895) | National Historic Site, 17th-century trading post remains | What is visible, access |
| Burns Mill Site | Five Rivers, NB (46.6414, -64.8781) | Register-listed mill site | Register statement not read |
| Fredericton City Hall, York County Court House, St. Anne's Chapel of Ease, Arts Building (UNB) | Fredericton, NB | All National Historic Sites | Not researched |
| Greenwich-area and northern towns: Bathurst, Campbellton, Dalhousie | NB | County Register lists carry many entries | Not researched |

## Tips
- historicplaces.ca search (results-resultats.aspx?m=2&Keyword=...&Province=NB) reads with page.py --all, and the place ids are in the cached copy in research/pages/ as place-lieu.aspx?id=N, but the order of the ids does not always match the order of the titles: open each id and check its title.
- Wikipedia's county lists of historic places give a Register number that is the place id on historicplaces.ca (id=2147 etc.).
- ArcGIS PointAddress results sat on the building for most New Brunswick addresses but not for Greenock Church or Hammond House; OpenStreetMap's place_of_worship / named building point was right for both.
- Web search returned quoted hours from official pages (Kent Museum, Charlotte County Archives, Fredericton) while the pages themselves were not fetched.
- photo_find.py look took about four minutes per place on the first places; it sped up later.
