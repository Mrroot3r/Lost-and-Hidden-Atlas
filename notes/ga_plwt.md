# ga_plwt: Georgia: Greensboro, Penfield, Crawfordville and the Oconee Piedmont
state: Georgia
region: ga
date: 2026-11-19
places: 17
file: data_ga_plwt.py

## What this batch is
Seventeen places in the Georgia Piedmont east of Athens, the first batch round here (the region had one place). Greene County: Scull Shoals mill village ruins (Oconee National Forest), the 1807 granite gaol and 1849 courthouse in Greensboro, the Church of the Redeemer, Springfield Baptist, Penfield and Old Mercer Chapel, Bethesda Baptist (1818 brick). Taliaferro: Liberty Hall in A. H. Stephens State Park, the 1901 courthouse, Crawfordville Baptist. Oglethorpe: Crawford's granite depot, Lexington's 1879 jail, Howard's Covered Bridge. Oconee: Elder Mill covered bridge, Eagle Tavern. Madison: Watson Mill bridge. Wilkes: Kettle Creek battlefield. Sources were Wikipedia (`wiki_raw.py`), Register forms (npgallery text layers, all of which read), HMdb marker pages (nearby lists at 5 miles round Greensboro, Scull Shoals, Penfield and Crawfordville), Georgia State Parks pages, recreation.gov and Vanishing Georgia. Not checked: anything on the ground; hours for the Old Gaol, Eagle Tavern, Kettle Creek, the courthouses and every church's services; whether Penfield's old college buildings stand or are ruins (the 1976 form and Wikipedia disagree); the Crawford depot's exact building on the aerial (pin is the Register point, prec=area); the Scull Shoals lot, which is under trees on the aerial. Springfield Baptist has two building stories (1907 form vs. the marker) and is conf=mixed. Brick was settled from photographs only for the Greene County courthouse and Old Mercer Chapel (both red brick); the Bethesda and Springfield churches are brick by their forms but the colour was not seen.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Church of the Purification and Locust Grove Cemetery | Sharon, GA (marker 33.56368, -82.79384) | HMdb 24896: first Catholic settlement in Georgia, log church 1792, church built in Sharon after 1860; Locust Grove Cemetery is on the Register (06001119) | Date and fabric of the Sharon church; the cemetery's position and access |
| Beth-Salem Presbyterian Church | Lexington, GA (33.87010, -83.10880) | HMdb 26059: organized 1785, moved to this site, chartered 1827 | When the present building was built (Register Lexington Historic District form not read) |
| Bethany Presbyterian Church | near Union Point, GA (33.5563, -83.0153) | HMdb 24619: organized 1786, first church in Greene County, Woodrow heresy trial 1886 | Whether an old building stands; the marker does not say |
| Union Manufacturing Company mill | Union Point, GA | On the Register (89000026), address restricted in the list | Its Wikipedia title (plain title goes to a Maryland company), position and state |
| Mary Leila Cotton Mill and Village | Greensboro, GA (33.579722, -83.187222) | On the Register (87001443) | Form not read; present use not checked |
| Park's Mill | near Buckhead, GA (33.52731, -83.30582) | HMdb 17274: mill about 1807; mill and dam collapsed by the 1930s; ruins said to be under Lake Oconee | Whether anything shows |

## Tips
- exploregeorgia.org (the state tourism listings, which carry hours for many small Georgia sites) answers 403 to `page.py`; the archived copies were not tried.
- Georgia State Parks pages read with `page.py --all`: the hours are in one run of text after "Hours." (park, office, historic site and last tour).
- Vanishing Georgia (vanishinggeorgia.com) posts read in full and carry a photograph per post; `brick.py look <id> <picture address>` takes the `wp-content/uploads/...jpg` found in the cached page. The Scull Shoals post's picture was the river, not the ruins.
- Wikimedia refused pictures (429) after the first in this run; two places left unset.
- The Watson Mill Bridge Register coordinate is 160 m east of the bridge in woods; the OpenStreetMap way named "Watson Mill Bridge" is on it.
