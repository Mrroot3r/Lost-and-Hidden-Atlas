# ks_jflv_rkvm: Kansas: Jefferson and rural Leavenworth counties
state: Kansas
region: ks
date: 2026-11-25
places: 8
file: data_ks_jflv_rkvm.py

## What this batch is
Eight places 30 to 50 miles west and north-west of Kansas City, on ground the earlier Kansas City batches did not reach: two Delaware River truss bridges (Perry, 1926; Valley Falls, 1936), two country schools (Buck Creek, limestone of about 1878; Sunnyside, frame of about 1879), and four Register-listed farmsteads (Morris Harris, Maplecroft, Lyman Christy, and in Delaware Township the Lamborn and Holman farms). Fewer than the 15 to 20 aimed for: every other Kansas City part had been worked, and most of what is left in these two counties is a private farm or an archaeological site that the Register keeps unlocated. Sources: National Register forms read as text from NPGallery (Buck Creek, both bridges, Sunnyside, Maplecroft, Lamborn) and the Kansas Historical Society's register search for Jefferson and Leavenworth counties (the farmsteads whose forms would not open: Harris, Christy, Holman). Wikipedia had an article only for Buck Creek. Pins: address lookups and Register-list points, checked on the 2024 state aerial; the Buck Creek and Sunnyside pins were moved onto a building seen there, and Commons photographs of Sunnyside and the Harris farm were taken within 20 m of the final pins. Not checked: nothing was seen on the ground; present owners and whether any building is open; whether the two bridges still carry traffic (a 2019 photograph of the Perry bridge shows a bare deck with brush at both ends); the interiors; the Lamborn, Holman and Christy buildings, which only the Society's one-paragraph summaries and the Lamborn form describe. Pictures: five found on Wikimedia Commons (Perry bridge, Valley Falls bridge, Sunnyside, Harris, Maplecroft); none plausible for Christy, Lamborn or Holman (Commons has none). Buck Creek School keeps `brick='?'` because the form names only a brick chimney, with no colour.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Delaware Cemetery | 10388 222nd St, Linwood, KS (the address lookup gives 38.9636, -95.0934, which falls on a bare field crossing on the 2024 aerial) | Kansas Historical Society summary: Zeigler Family Burying Ground, first known burial a Delaware, Betsy Zeigler, October 1867, possibly burials from about 1860; National Register 2020 (100004927) | The nomination form would not open and the cemetery could not be seen on the aerial at the address; a web search turned up another Delaware Cemetery on K-5 south of Lansing, so the two may be mixed up |
| Cedar Creek Bridge | Valley Falls vicinity, Jefferson County, KS | State Register 1982 | No coordinate or description; the state form was not read |
| Meriden Rock Creek Bridge | 8725 K-4 Hwy, Meriden vicinity, KS | State Register 1989, a King Iron Bridge Company bowstring; "one of several listed bowstring bridges in the county" | Anything beyond that one line, and a pin |
| Benedict Meyer Log Cabin | Threshing Bee grounds on K-4, Meriden, KS | State Register 1986; a web search says it is a log cabin of 1854 moved to the Meriden threshers' grounds | A page of the association's own that says so, and its hours (the show is a few days in summer) |
| Methodist Episcopal Church of Oskaloosa | Oskaloosa, KS (39.2174, -95.3144) | Wikipedia's Register list gives it as listed in 2023 (100011579) | Web search could not confirm the listing and the form would not open as text |
| Senator William A. Harris House | near Linwood, KS | 1974 form read: an 1883 two-storey house on a rough limestone base, built for the Shorthorn cattle breeder (and later US senator) | A position and whether it is private; the Register keeps the address restricted |
| Biehler Barn | Easton, KS | National Register 1977 (77000585) | The form is a scan with no text layer and no other source was read |

## Tips
- `tools/page.py --all <npgallery text address>` stops after about 5,000 characters unless given `-n 120000`; redirect it to a file and search that, instead of reading page after page.
- The Kansas register search for Jefferson County (`county:JF`, two pages) lists 16 properties with summaries of the farmsteads whose forms do not open as text; the page text is in `research/pages/`, but printing it whole floods the screen (it has a long menu). Print only from "Records:".
- Web search could not confirm several Kansas listings (Oskaloosa church, Delaware Cemetery); do not count on it for small Register entries.
- Leavenworth and Jefferson counties are now nearly used up for Register-listed standing places; what remains is private farms, archaeological sites and unlocated bridges.
