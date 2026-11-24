# nd_bvtq: North Dakota: opera houses, depots, mill, churches and a lift bridge across the state
state: North Dakota
region: nd
date: 2026-11-24
places: 11
file: data_nd_bvtq.py

## What this batch is
Eleven standing buildings across North Dakota, which had 49 places before; claimed with `choose.py --thinnest`. They are the Carson Roller Mill, the Lisbon, Ray and Ellendale opera houses, the Wilton and Rugby depots, the Fairview Lift Bridge with its tunnel at Cartwright, Vang Lutheran Church at Manfred, Saints Peter and Paul at New Hradec, the Billings County Courthouse museum at Medora and Old Main at Bottineau. The state's National Register list was read with `wiki_raw.py --rows -g`, each article with `wiki_raw.py`, and the nomination forms from NPGallery with `page.py --all`. Hours came from the Medora tourism page, the Epping town page (for Ray), the Lisbon Opera House Foundation page and Prairie Public; the Wilton, Rugby, Carson, Ellendale and Bottineau entries have no hours because no page of the owner gave any (Wilton is `hours='?'`). Not checked: anything on the ground, every interior as it is today (the forms are from 1978 to 2001 and say so), ownership of the Carson mill, Ellendale block and Fairview bridge, and the Fairview parking lot. The two Wikipedia coordinates for the Lisbon Opera House and Old Main fell in a parking lot and on a ball field; both were moved (Old Main to the OpenStreetMap building of that name), and the pins for Lisbon, Vang, Ray, Wilton, Ellendale, Billings and Old Main are `site`, since the aerial did not pick out the building. Sources disagree on whether the Fairview bridge and tunnel are open as a path and on who owns them (conf mixed); the entry is view-only. Brick is `?` for Lisbon, Rugby, Ellendale, Billings and Old Main (the forms say brick but not its colour, or were not read). The picture for Wilton came from `photo_find.py` (choice 2).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Urbain Cote Round Barn | near Dunseith, ND (Wikipedia gives 47.64444, -100.05833) | 1943 round dairy barn, NRHP 1986; Rolette County Historical Society is buying it (KFYR, 2025) | The Wikipedia coordinate falls in empty field (nothing within 600 m on the aerial); a true position and whether the public may visit |
| Bradford Hotel and Ransom County Courthouse | Lisbon, ND (46.442778, -97.682222) | Hotel built 1909, NRHP 1987 (Wikipedia, one paragraph) | Anything beyond the date; the courthouse was not read |
| Hotel Brown | Flasher, ND (46.4543, -101.2321) | NRHP 2014 | No article; nothing read |
| Old Mandan High School, Fort Lincoln, Assumption Abbey, Grand Forks County Courthouse | Mandan, Bismarck, Richardton, Grand Forks | Already named in the notes nd_cumj and nd_ssxv | Still unworked here |

## Tips
- NPGallery nomination forms read well with `page.py --all <url>` piped through `tr '\n' ' '`; the Ray Opera House form's header is the Williams County Courthouse's, but its text is the opera house's.
- Wikipedia coordinates for North Dakota Register entries can be well off (Cote barn, Old Main); `nom.py "<name>, <town>, North Dakota"` found Old Main at once.
- `pgrep -f` inside a Monitor matches the monitor's own command line and never ends; wait on a file instead.
- hmdb.org and ndtourism.com gave HTTP 403 from `page.py`; a web search result that quotes the page was the only way to read the Lisbon tourism listing.
