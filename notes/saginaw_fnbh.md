# saginaw_fnbh: Michigan: old Saginaw
state: Michigan
region: mi
date: 2026-11-27
places: 10
file: data_saginaw_fnbh.py

## What this batch is
Ten places in Saginaw from one walk-through video of old Saginaw buildings (Old World Exploration, "Old World Saginaw Michigan"; the record of every name it gave is source/videos/20250314_zoxXyf3DM4o.md). Standing buildings: the Bearinger Building, the Saginaw Armory, the Potter Street (Flint and Pere Marquette) depot, Hoyt Public Library, the Temple Theatre, the Forest Lawn Cemetery chapel and receiving vault, the Saginaw Water Works, First Congregational Church and the Schuch Hotel; and the Jeffers Memorial Fountain of 1906. Sources were Wikipedia (read with wiki_raw.py), SAH Archipedia's Saginaw entries (MI-01-SA1 to SA22 exist; SA23 and up answer 404), the Castle Museum of Saginaw County History's own articles, and the Michigan Stained Glass Census. Hours are from the library's own branch page only; the Temple Theatre's and First Congregational's own sites refused every fetch (403), so their hours are "?". Not checked: anything on the ground; whether the Potter Street depot's tower still stands (the video says it is gone; the 1996 Register description has it); whether the Forest Lawn chapel is still used (one undated blog says it is not; the entry carries conf='mixed'); whether the Schuch Hotel's restaurant is still open. Pins: the Potter Street depot is an address point marked 'site' (the summer aerial did not show the depot's roofs clearly); the Forest Lawn chapel pin is the cemetery's address point by its entrance, marked 'area' (the chapel was not picked out under the trees). Red brick: yes for the Bearinger Building and the depot (Wikipedia says red brick); no for Hoyt (limestone, with a beige brick wing) and the limestone chapel; '?' for the rest.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Warren Avenue Presbyterian Church | Saginaw, MI | Named in the video as standing and run down; a Detroit Public Library postcard shows it | Any source on the building's date, address and state |
| First Presbyterian Church | Saginaw, MI (121 South Harrison Street, as a search result quotes its state marker) | Congregation founded 1838, as quoted from the marker | The marker text itself (the state's marker PDFs answered 404) and the present building's date |
| Michigan Employment Institution for the Blind | Saginaw west side, MI | Postcards of its administration building exist | Whether any building stands |
| Heavenrich Brothers and Company building | Saginaw, MI | Named in the video, a men's and boys' outfitter | Address, date, whether it stands |
| Michigan Central depots | Saginaw, MI | Search results name a Court Street station replaced about 1909 and a depot on West Genesee demolished after 1976 | A source read in full; which, if any, stands |

## Tips
- SAH Archipedia's Saginaw County entries are `https://sah-archipedia.org/buildings/MI-01-SA<n>` for n = 1 to 22 (Saginaw, Frankenmuth, Montrose, Birch Run); they read in full with `page.py --all`.
- The Castle Museum (castlemuseum.org/post/...) has long researched articles on single Saginaw buildings that read in full with `page.py --all`; its tour page answers 404.
- The Michigan state marker PDFs on dnr.state.mi.us and www2.dnr.state.mi.us answered 404 for every Saginaw marker tried (MHC731998013, MHC732012019, MHC731981026); hmdb.org answered 403.
- templetheatre.com and fccsaginaw.org answer 403 to `page.py` and the web fetch tool.
