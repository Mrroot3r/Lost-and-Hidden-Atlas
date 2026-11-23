# elgin_abst: Elgin, Illinois
state: Illinois
region: il
date: 2026-11-23
places: 9
file: data_elgin_abst.py

## What this batch is
Nine places in Elgin, Illinois, taken from the names in one walk-through video of the town's old buildings (the record is source/videos/20251024_8vwH_2uaeis.md; the video was a list of names only, never a source). Added: Old Main of the Elgin Academy (now the Elgin History Museum, with hours from the museum's own page), Fire Barn No. 5, the watch-shaped First Universalist Church, the Elgin Tower Building, the Lords Park Pavilion, the old Gail Borden Public Library, the David C. Cook Mansion, the Congdon Avenue (Selz, Schwab) shoe factory, and the Elgin National Watch Company Observatory, the one building of the razed watch works the video's last section was about. Facts come from Wikipedia read as raw text, the Elgin Heritage Commission's plaque pages (historicelgin.com), the museum's visit page, the Unitarian Universalist Church of Elgin's history page (read with the web fetch tool after page.py got 403) and the 2014 Register form for the Elgin Downtown Commercial District (NPGallery text route). Pins are OpenStreetMap points; three address points fall on the street in front and are marked site; the shoe factory was moved onto the building. Not checked: anything on the ground; the Fire Barn museum's opening days (its old weebly address now points to an unrelated site, so no hours); who owns and uses the First Universalist Church since 1979 and the old library since 1985; park hours and parking for Lords Park; whether the observatory opens to the public; red brick for most places (only the fire barn, from Wikipedia, and the Cook mansion, from a photograph, are settled).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| First Congregational Church | Elgin, IL, 256 E. Chicago Street at Center Street | Search-result text quoting the Daily Herald gives a third building of 1889 costing $35,000; an 1894-95 city directory (ilkane.whalen-family.org) puts it at Chicago and Center | A page that opens: the church's own site was not found, HMdb answered 403 |
| St. Mary Catholic Church | Elgin, IL, Fulton Street | Named in the video as built 1896 to 1899 | stmaryelgin.org and the Rockford diocese page both answered 403; no building date read |
| St. John's Lutheran Church | Elgin, IL, 115 N. Spring Street | Congregation founded 1859; services Saturday 5:30 p.m., Sunday 9 a.m. (stjohnselgin.org) | The building's date |
| Holy Trinity Lutheran Church | Elgin, IL, 357 Division Street | Search results quote a consecration in 1907 | A page that opens |
| Elgin Turners hall | Elgin, IL, 112 Villa Street | A club listing says the building dates from the early 1870s | Any source that opens |

## Tips
- historicelgin.com (the Elgin Heritage Commission's plaque site) reads cleanly with page.py; its pages are named by street address (105-n-gifford-street) and the list of all of them is in https://historicelgin.com/scripts/maps.js.
- HMdb answered 403 to page.py and to the web fetch tool; the marker titles and positions for Elgin were in data/pock/il.json, as GUIDE.md section 16 says.
- elginfiremuseum.weebly.com, the link on Wikipedia's Fire Barn 5 article, now redirects to an unrelated site: do not take hours from it.
