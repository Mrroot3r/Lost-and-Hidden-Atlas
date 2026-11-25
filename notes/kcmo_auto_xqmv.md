# kcmo_auto_xqmv: Kansas City: Automobile Row and Midtown survivors
state: Missouri
region: kcmo
date: 2026-11-25
places: 10
file: data_kcmo_auto_xqmv.py

## What this batch is
Ten standing places in Kansas City, Missouri that the Atlas lacked: six on or near Automobile Row (the Buick building on Admiral Boulevard, the 1901 McGee and Kirkwood buildings, the Auto Coach Building, the McGee Street Automotive Historic District, the Greenlease Cadillac building), the Pickwick Plaza hotel and bus terminal, KCP&L Substation "A", Holy Rosary Church in Columbus Park and Linwood Presbyterian Church. The part worked was "Westport, Midtown and the Plaza" widened to the Crossroads and Columbus Park, because the Register lists for Platte, Clay and Cass counties and for the Kansas side turned out to be already fully on the Atlas (the Kansas State Register summaries for Wyandotte, Johnson and Leavenworth counties gave only a handful of house listings with no text). Sources: Wikipedia as raw text, the Kansas City Auto Museum, Clio, Flatland KC and KCUR pages, the National Park Service's record pages, and the full Register form for the substation (read). Not checked: any interior, current use of the Auto Coach, 1901 McGee, Kirkwood and Buick buildings, parking, Mass times for Holy Rosary, who now uses Linwood Presbyterian. Register forms before about 2018 are only placeholders on NPGallery, so builders and dates are given only where a page said so. Pins: all on the aerial and all on a building; Holy Rosary and Pickwick were moved from an address lookup to OpenStreetMap points after the aerial showed the lookup on a parking lot or across the block. The McGee district pin is at 1824 McGee and marks the area, not one building.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Kelley-Reppert Motor Company Building | 422 Admiral Blvd, Kansas City, MO (39.1055, -94.5777) | Register 2004, architects Keene and Simpson, three stories over a grade change (NPS record page) | No page with its history; form is a placeholder |
| Studna Garage Building | 415 Oak St, River Market, Kansas City, MO (39.1095, -94.5792) | Register 2006, period 1900 to 1924 (NPS record page) | Any narrative source |
| Bancroft School | 4300 Tracy Ave, Kansas City, MO (39.04835, -94.5706) | Register 2012, closed 1999, redeveloped as apartments in 2013 (BNIM, a search result); sources give 1904 and 1909 to 1922 | Rosin Preservation's page would not open; a firm build date |
| Joe Vaccaro Soda Water Manufacturing Company Building | Columbus Park, Kansas City, MO (39.11246, -94.57266) | Register 2003; red brick building in a Commons photograph | No source read |
| Wheatley-Provident Hospital | already on the Atlas | | Nothing; listed so nobody searches again |
| Claybrook House, Kearney | Clay County (39.388, -94.336) | Wikipedia: built about 1858, burned and demolished after a 2002 fire | Gone; no need to research again |
| Bannister Federal Complex (Pratt and Whitney plant, 1942) | south Kansas City, MO (38.958, -94.569) | Register 2013; Wikipedia calls it a former complex | Whether anything stands; large industrial site, secured |
| Abernathy/Lyle House; Hycrest (Charles Hyer House); Dr. Harkey House; George Hodges House | Leavenworth; Olathe; Gardner; Olathe, Kansas | Kansas State Register listings 1984 to 1990 with a style only | Any source with a date or description |
| Lamborn Farmstead | Leavenworth County, Kansas (39.24, -94.93) | National Register 2011; farm buildings of the late 1800s and early 1900s | Visiting rules (private farm) |

## Tips
- start.py counts only 15 km round a town and the Atlas already has 300 Kansas City places: before choosing, run build/sites.json against the Register lists. This session wrote that comparison in an hour (NPS points from tools/nrhp_state.py against the Atlas pins within 500 m) and it found the Platte, Clay, Cass and Kansas-side lists complete; Jackson County's Midtown, Crossroads and east side still had about 65 unlisted Register entries.
- tools/nrhp_state.py works from a cloud session and gives each listing's reference number and point; matching by name alone gave false results, so match by distance.
- NPGallery serves a real form only for some listings (the 2018 substation form did, through the GetAsset link on the AssetDetail/NRIS page); most earlier ones are a 22 KB placeholder.
- Kansas Historical Society register pages (kansashistory.gov/natreg/...) read well with a plain requests call; the name sits two lines above the county line.
- Clio, Flatland KC and the Kansas City Auto Museum read well with page.py; pendergastkc.org and rosinpreservation.com did not open.
