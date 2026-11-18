# mohawk_qljt: Fulton County: Johnstown, Gloversville, Mayfield, Fish House
state: New York
region: adk, mohawk
date: 2026-11-18
places: 19
file: data_mohawk_qljt.py

## What this batch is
Nineteen places in Fulton County, the first close pass there (region `mohawk`, drawn at random by `choose.py --state ny`, which offered Broadalbin; the Atlas had nothing in Johnstown, Gloversville, Mayfield or Broadalbin). Johnstown: Johnson Hall (state historic site, with a parking point), the 1772 courthouse and the 1772 jail (Fort Johnstown), St. John's church with Sir William Johnson's grave, the Colonial Cemetery with the Drumm House, the 1781 battlefield markers and the Knox Mansion. Gloversville: the Glove Theatre, the Carnegie library, the armory, the downtown district (area pin) and the county museum in the Kingsboro school. Mayfield: the Rice Homestead museum and the 1937 Log Cabin Church. Broadalbin: the Hotel Broadalbin. Four on the Sacandaga side are filed under `adk`, like Batchellerville and Sacandaga Park: drowned Fish House (markers for Johnson's 1762 lodge, the 1818 covered bridge and the flooded road), the 1784 Shew house, the Caroga Historical Museum and Northville village (area pin). Wikipedia was read as raw text; parks.ny.gov, HMdb marker pages, 44lakes.com (county tourism), visitsacandaga.com, mohawkvalleymuseums.us, theglovetheatre.com and the Haunted History Trail page through `page.py`. Brick was set from Wikipedia photographs opened with `brick.py look` (courthouse and armory red brick; library and Glove Theatre pale; jail's brick wings painted; Knox Mansion frame) or from the article text; seven are left '?'. Not checked: anything on the ground; hours for the Drumm House, the county museum and the library (their pages would not open or gave no hours); whether the Hotel Broadalbin is still trading (a 2026 sale listing came up in search and could not be opened); whether the Log Cabin Church holds services; the adult fee at Johnson Hall. The Knox Mansion's date is 1898 in Wikipedia and 1889 on the Haunted History Trail page (both given, `conf='mixed'`); the D.A.R. battlefield tablet is 1909 on the tourism page and 1901 on the tablet as HMdb reads it. No ruins found worth adding: the unnamed OpenStreetMap "ruin" leads round Broadalbin and Johnstown are farm buildings on private land with no source. National Register forms for Fulton County on NPGallery are one-page placeholders and were not read.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Yanney woolen mill site | Ephratah, NY (Pomeroy marker at 43.000266, -74.545098, Yanney Road and County Highway 140) | Pomeroy Foundation marker page: a four-story stone woolen mill of 1865, closed a few years after Levi Yanney died in 1905; by 2019 only a dirt road to the site was left | Whether any stone is left (LiDAR not looked at), and who owns the road's end |
| Old stone dam at Lily Lake | Caroga, NY (west end of Lily Lake, toward Stewart's Landing) | Caroga Museum "Saw Mills of Caroga" page: remains of a stone dam of an early sawmill are still visible | A position and who owns the shore |
| Last water-powered sawmill site | Bowlers Mill Road, Bleecker, NY (across from Lilly Lake Road) | 44lakes.com: a 1976 marker for the Ernst family's sawmill on the West Branch of Stony Creek, run by water power until 1939 | Whether the dam or mill foundation can be seen; owner |
| Romeyn's Mill and the Sacandaga blockhouse | Mayfield, NY (off Van Den Burgh Road) | NY State Military Museum page: a 1777 blockhouse, attacked in 1778 or 1780 (accounts differ); a marker for Romeyn's Mill of 1773 | Position of the marker, and anything to see |
| Peck's Park schoolhouse | Pecks Lake Road and NY 29A, Town of Johnstown | carogalake.com (undated): an 1857 one-room schoolhouse museum, open summer Wednesdays and Saturdays | A current source and position |
| First United Methodist Church, Gloversville | 7 Elm Street, Gloversville | Wikipedia: 1869–70 red-brick Romanesque church, vacant since 2000; a byways page dates it 1909 | Its present state and which date is right |
| Western Montgomery County (region `mohw`) | Palatine Church, Stone Arabia churches, Fort Plain, Canajoharie, Nellis Tavern | The Atlas has nothing there; all on the county's Register list with coordinates | A session drawn to `mohw` |

## Tips
- `wiki_raw.py --rows` for Fulton County shows no "article:" for most rows, yet Log Cabin Church, Oliver Rice House, Godfrey Shew House, Hotel Broadalbin, Knox Mansion and others have articles under exactly the row names; try the row name before giving up.
- johnstownnyhistsoc.org resets the connection, and its archived copy is drawn by script; fultoncountyhistoricalsociety.org returns no text. 44lakes.com (Fulton County tourism) has plain pages for both museums and for every county marker.
- OpenStreetMap places the Fulton County courthouse's name on the county office building at 223 West Main Street; use the Register point.
