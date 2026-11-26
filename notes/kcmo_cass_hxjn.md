# kcmo_cass_hxjn: Kansas City, Missouri
state: Kansas, Missouri
region: kcmo, ks
date: 2026-11-26
places: 3
file: data_kcmo_cass_hxjn.py

## What this batch is
Three places, short of the 15 to 20 aimed at: the Kansas City area's register lists are now almost all on the map. I looked at Lee's Summit, Raytown, Grandview, Belton and Cass County (Missouri) and Johnson County (Kansas), and compared the National Register lists for Jackson, Cass, Clay, Platte, Wyandotte, Leavenworth, Douglas and Johnson counties against every place list. What was missing was almost only modern-era or residential districts. Added: the Howard Schoolhouse in Independence (jchs.org pages), the Sharp-Hopper Log Cabin in Harrisonville (the Cass County Public Library's "Early Cass County" panel and Clio), and the Lake of the Forest Historic District at Bonner Springs (the National Park Service's full text of the 1996 form). Not checked: anything on the ground; the cabin's exact spot on its lot; where the Lake of the Forest clubhouse stands (the pin is in the lake, `prec='area'`); whether the schoolhouse has its own visiting times; the Cass County Historical Society's hours. No pictures exist on Commons for these, so all three have none.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Claybrook House | Kearney, MO | National Register 1981, a c. 1858 Federal-style frame house; Wikipedia says it was lost in a controlled burn on March 12, 2002 | Treat as gone unless a source shows something left |
| John and Adele Georgen House | 933 S. Main St, Independence, MO | National Register 2000, a Craftsman house; a search result gave the style and address | The nomination form is not on line (NPGallery placeholder; the Missouri state copy returns 404): no date, no description |
| Frank and Agnes Schmotz Farmstead (Schmotz-Knight) | 643 S. 138th St, Bonner Springs, KS | National Register June 17, 2024 | Nomination text not read; the Kansas Historical Society's search pages did not show it |
| Brown-Blachly House | Kansas City, KS | Listed in the Wyandotte County Register list | No page found |
| Friends' Place | Lawrence, KS | Listed in the Douglas County Register list | Not looked up |
| Biehler Barn | Easton, KS | Listed in the Leavenworth County Register list | Only the list entry seen |
| Shawnee Grade School | Shawnee, KS | Listed in Wikipedia's Johnson County list (reference 100013542) | No page found that describes it |
| Burnt District Museum (Cass County Historical Society) | 400 E. Mechanic St, Harrisonville, MO | Search results say it is in the society's office and open weekdays about 10 a.m. to 3:30 p.m. | A page of the society's own with hours; not opened |
| Greenwood Quarry and Mill | Greenwood, MO (38.840, -94.333) | USGS record only | Any source on what stands |

## Tips
- Johnson County, Kansas, and Jackson, Cass and Clay counties, Missouri, are close to finished for register listings: a matching test on place names alone gives false "missing" results (ids and names differ), so grep the data for a distinctive word before counting a place as missing.
- `page.py` with `-g` prints only sentences it likes; for a Register search page, strip the cached HTML in `research/pages/` instead.
- The Missouri state copies of National Register forms (`mostateparks.com/.../<name>.pdf`) returned 404 for every one tried; NPGallery gives full text only for older listings (Lake of the Forest, 1996, worked).
- HMdb nearby lists returned 403 from `page.py` this time.
- A better use of a Kansas City session now: Native American or Santa Fe Trail traces, mid-1800s Civil War sites in the border counties, and the remaining Lawrence districts, or picking another metro area.
