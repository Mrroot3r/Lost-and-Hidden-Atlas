# wichita_vbjq: Wichita, Kansas: old downtown
state: Kansas
region: ks
date: 2026-11-23
places: 12
file: data_wichita_vbjq.py

## What this batch is
Twelve standing buildings in Wichita, Kansas, worked from the names in one video (Old World Exploration, "Old World Wichita, Kansas", record in source/videos/20230606_BJ7eEE6XPFQ.md; the video is a tip only): the 1868 Munger house at Old Cowtown, the 1887 YMCA building that is now the Scottish Rite Temple, Eagles Lodge No. 132, the Soldiers and Sailors Monument by the old courthouse, the Carnegie library, the Catholic cathedral, Fiske Hall at Wichita State, the Davis Administration Building at Friends University, Carey House (Eaton Hotel), the Lassen and Broadview hotels, and Union Station. Sources: the Kansas Historical Society register search for Sedgwick County (county code SG, 16 pages, read with page.py --all -n 40000), Wikipedia (wiki_raw.py), the cathedral's own page (Mass times and the weekday closure for dome work), Drury Hotels' history page, KMUW and The Sunflower for Fiske Hall, and the Kansas Preservation Alliance for the Eagles lodge. Pins: ArcGIS street-address points and OpenStreetMap points, all looked at on the 2024 Kansas aerial; the cathedral and Davis building pins were moved to OpenStreetMap points, Carey House was moved onto the building beside the park by sight, and the Munger house pin is the register point at the edge of Old Cowtown (prec area). Not checked: anything on the ground; Old Cowtown's hours (oldcowtown.org answered 403 to both tools); whether the Scottish Rite Center gives tours; what the Eagles lodge and Carnegie library hold now; whether the Lassen conversion has been done; campus parking at both universities. Red brick: Lassen from the register summary; Eagles lodge, Broadview and Davis building from Commons photographs; the stone buildings from their sources; the rest left "?".

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| First Presbyterian Church | Wichita, KS (525 N Broadway) | Stone Gothic church completed 1911–1912 by Badgley and Nicklas (Waymarking, read); register listing claimed but not in the Sedgwick County register search | The church's own page (firstpreswichita.org did not answer) for services and a source for the building |
| Wichita Veterans Administration Hospital | Wichita, KS (5500 E Kellogg; 37.6812, -97.2740) | National Register 2012, Classical and Colonial Revival, second-generation VA hospital (Kansas Historical Society search, page 15) | A description of the original buildings and which of them stand; access to an active VA campus |
| Fairmount College buildings | Wichita State University | Fairmount's Carnegie library (1908–1910) and other early buildings (Wikipedia) | Whether any stands; wichita.edu history pages return a block page to both tools |
| Kansas Masonic Home | Wichita, KS (Delano) | Search results say the 1896 home burned in 1916 and a new building rose in its place | A page opened that describes the present building |

## Tips
- Kansas register search for Sedgwick County is county code SG, 16 pages of ten; page.py --all -n 40000 reads each page whole, and splitting the text on "National Register Nomination" gives one listing a line.
- oldcowtown.org answers 403 to page.py and to the web fetch tool; wichita.edu pages return an Incapsula block page.
- The ArcGIS address point for 430 N Broadway (the cathedral) and 2100 W University (Friends) fell on the wrong building; the OpenStreetMap points were right.
