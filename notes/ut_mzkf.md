# ut_mzkf: Utah: a third scatter, from Bryce Canyon to Randolph and Wendover
state: Utah
region: ut
date: 2026-11-24
places: 11
file: data_ut_mzkf.py

## What this batch is
Eleven places spread across Utah, which had 53: Camp Floyd and its Stagecoach Inn, Hole-in-the-Rock, the Dalton Wells camp near Moab, Bryce Canyon Lodge, the Wendover airfield, Parry Lodge in Kanab, Goulding's Trading Post, the Manti Temple, the Randolph meetinghouse, the Buckhorn Flat lime kiln and the Elsinore sugar factory. Facts are from Wikipedia (wiki_raw.py), four National Register forms read as text from NPGallery (lime kiln, Elsinore, Randolph, Goulding's), the National Park Service pages for Hole-in-the-Rock and Bryce Canyon Lodge, the Utah State Parks pages for Camp Floyd and Utahraptor, Parry Lodge's and Goulding's own sites and the church's Manti temple page. Not checked: the entrance fee at Camp Floyd; where the Dalton Wells remains are signed; the Bryce Lodge season; Goulding's museum hours; Wendover museum hours (its site gave 403 and the archive copy could not be opened, so the hours come from a search result and are recorded `?`); who owns the Elsinore buildings now; whether the Buckhorn Flat kiln is still BLM land and what the road is like (the BLM page refused). Pins were looked at on the aerial and LiDAR sheets; Elsinore's is on the old building cluster, not on a known building. Wikipedia's and the Register's coordinates for Camp Floyd (700 m off in a field) and for the Wendover base (on a runway) were replaced. Pictures: four places had none and got a Commons picture (pics_swhz.py).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Devil's Gate-Weber Hydroelectric Power Plant | Weber Canyon, Morgan and Weber counties (41.13833, -111.86722) | Built 1909 to 1910 for the Utah Light and Railway Company; 1989 Register form read (27 pages), private owner | Whether it can be seen from any public road; present owner |
| Hans Peter Nielson Gristmill (Bicknell Gristmill) | south-east of Bicknell, Wayne County (38.30806, -111.51056) | About 1890; Register 1975 | Owner, whether it stands, any public access |
| Jens Larson Jenson Lime Kiln | north of Richfield, Sevier County (38.79333, -112.08556) | 1903; Register 1978 | Owner and access |
| Black Rock resort ruins | Great Salt Lake, Tooele and Salt Lake counties (40.72503, -112.22774) | Register 2020s listing of the rock and the resort's foundations | A source on the park's access; no Wikipedia article found |
| Echo Canyon Breastworks and Mormon Flat Breastworks | Echo, Summit County; Porterville, Morgan County | Register 1988 listings of the 1857 defences | No source opened; coordinates absent |
| Kimball Stage Stop | Kimball Junction, Summit County (40.72346, -111.51726) | Register 1971 | Not opened |
| Moab Cabin, Elk Mountain Mission Fort site | Moab (38.57278, -109.54611; 38.58861, -109.5625) | Register listings | Not opened |

## Tips
- `choose.py --thinnest` took Utah (53); it is the thinnest state but the sixth batch there, so many Register rows are done: the Sanpete, Summit, Utah and Carbon county lists still have plenty of towns' worth of buildings.
- Register coordinates for camps and airfields are often a field or runway: use `osmnear.py ... -g 'hangar|museum'` first; for Wendover it found the Enola Gay hangar and the museum at once.
- The Utah State Parks page for Camp Floyd prints "Wallsburg" in its address block: ignore it.
- historicwendoverairfield.com does not exist; the real site is wendoverairfield.org and it answers 403 to page.py.
- The NPS "places" pages sit under `/places/000/<name>.htm` for Bryce Canyon Lodge, not `/places/<name>.htm`.
- The 1980 Register forms give the owner and "accessible" lines, which is the quickest source of land ownership for a ruin when the BLM site refuses page.py.
