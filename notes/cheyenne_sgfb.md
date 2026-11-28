# cheyenne_sgfb: Cheyenne, Wyoming
state: Wyoming
region: wy
date: 2026-11-28
places: 13
file: data_cheyenne_sgfb.py

## What this batch is
Thirteen standing places in and near Cheyenne, worked from one walk-through video of the town's old buildings (the record is `source/videos/20230526_NsindAXmRv4.md`: 45 names, 13 added, 4 already on the map, 6 gone, 2 not found, the rest not checked). Downtown: the Plains Hotel, the Tivoli Building, the Hynds Building, the Capitol Avenue Theatre (Paramount) front, the Knights of Pythias Building, the Masonic Temple, the City and County Building and the Cathedral of St. Mary; on Carey Avenue the Idelman Mansion; F. E. Warren Air Force Base as Fort D. A. Russell, with its 1887 post hospital (now the base museum) as its own entry; the 1932 veterans' hospital; and Granite Springs Dam in Curt Gowdy State Park. Sources: the Register records and forms read with the form reader (the 1996 downtown boundary increase form is long and describes nearly every downtown building), the Fort D. A. Russell National Historic Landmark form, Wikipedia, SAH Archipedia, Cinema Treasures, Cowboy State Daily, KOWB, Wyoming State Parks and a Laramie County Library research guide. Not checked: any interior; the present use of the Tivoli (a brewpub as of 2012); whether the Idelman Mansion is still the Governor's Office; the dam's date beyond the national dam inventory as Snoflo gives it (1904; a state archives file name found in search mentions 1912); how near a visitor can get to the dam face; the hours of the City and County Building. The cathedral's Mass times and the base museum's hours and visiting rules were read as web searches quoted the owners' pages, which refused direct reading. Brick colour is recorded only where a source said it (Plains Hotel and Masonic Temple buff; the fort's red brick from the Landmark form).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Cheyenne Opera House site | Cheyenne, WY | Search results: opened 1882, burned inside 1901 or 1902, later apartments, torn down 1961 | The page that says so (wyomingtalesandtrails.com) refused; a marker or site to see |
| Convent and Academy of the Holy Child Jesus | Cheyenne, WY (21st Street and O'Neil Avenue, by a library record) | Founded 1884 (Laramie County Library record) | Whether any building stands |
| Nagle-Warren Mansion | Cheyenne, WY (Register list point 41.135, -104.8129) | Romanesque Revival house of 1886 to 1888, on the Register; a bed and breakfast with tours at times (its own pages read) | Present opening; not named in the video, so left for a places session |
| St. John's Hospital, Eagles aerie (1909), Elks Lodge, Stock Growers National Bank, the 1913 post office and courthouse | Cheyenne, WY | Named in the video only | Any source on what is left |

## Tips
- The Downtown Cheyenne Historic District boundary increase form (96000909) is about 930,000 characters with every line doubled; squeeze the spaces first (tr -s) and grep by building name: it gave dates, architects, materials and condition for most of downtown.
- SAH Archipedia has F. E. Warren Air Force Base buildings (nodes 23028 to 23034) with dates and materials; base pages on warren.af.mil refuse the page reader.
- stmarycathedral.com, warrenmuseum.com and wyomingtalesandtrails.com refused the page reader and the web fetch tool; web search with allowed_domains set to the site quoted the hours.
- The ArcGIS geocoder turned "301 W Lincolnway" and "312 W 17th St" into East addresses with an abbreviated W; spell out "West".
