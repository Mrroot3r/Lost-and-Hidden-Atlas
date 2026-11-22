# evansville_paxj: Evansville, Indiana: courthouse square and old downtown
state: Indiana
region: in
date: 2026-11-22
places: 11
file: data_evansville_paxj.py

## What this batch is
The first Atlas places in Evansville: 11 standing buildings, ten round the Old Vanderburgh County Courthouse in downtown Evansville and one (Olmsted Hall) on the University of Evansville campus. The names came from one Old World Exploration video, worked as job 9 (record: `source/videos/20230705_3moLJ91HyLA.md`); the video was a tip only. Sources: Wikipedia articles read with `wiki_raw.py`; National Register forms and the 1981–82 Indiana state inventory sheets on NPGallery (`page.py`); the Old Courthouse Foundation's history page; Willard Library's own page (hours); the Coliseum's own page; Clio entries for the courthouse and YMCA; Discover Indiana for Evansville College. Red brick was settled from Wikipedia photographs (`brick.py look`) or a source naming the material; the Coliseum is `?` after two refusals from Wikimedia. Not checked: interiors (none visited by any source except the courthouse's marble and the Coliseum's rooms, from their own pages), today's owners of the brewery block and the Indiana Bell building, and who may use the downtown lots. Only Willard Library has opening hours; the courthouse, post office and Coliseum are event venues with no visiting hours found, so they are `view`. The courthouse's start date and cost differ between Wikipedia and its Foundation and both are given (`conf='mixed'`). The jail's pin marks its block: the castle front could not be picked out on the aerial.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| St. Boniface Church | Evansville, IN, 418 N. Wabash Avenue | GCatholic lists the church at that address in the Diocese of Evansville with "1881" | A parish or diocese page with its history and Mass times; none could be opened |
| YMCA building | Evansville, IN, Fifth/Sixth and Court/Vine streets | Register-listed (82000128). Wikipedia says built 1924, five-storey yellow brick Tudor Revival; Clio says begun 1912 at Fifth and Vine and dedicated 1914; WEHT (2025) says Indiana Landmarks bought the old YMCA at Sixth and Court in 2023 | Which building is the listed one; its Register form is not digitized on NPGallery |
| Washington Avenue Presbyterian Church | Evansville, IN, 641 Washington Avenue | The Evansville library's photo record gives the address and names God's Way Church as a later user | A history and whether it stands as built |
| Delaware School | Evansville, IN | Dated 1896 on its front in old photos (video); a Delaware Elementary School exists today | Whether the 1896 building stands |

## Tips
- NPGallery's Indiana listings from 1982 (a downtown Evansville multiple listing) are two-page state inventory sheets, mostly handwriting; the typed "Historical Information" paragraph at the end is the readable part and gives the address, architect and year.
- The Diocese of Evansville directory found by search (`dio-bell.solutiosoftware.com`) is the Diocese of Belleville's, for Evansville, Illinois: check the state before taking Mass times.
- The SHAARD nomination PDFs that Wikipedia cites (`secure.in.gov/apps/dnr/shaard/...`) return only the database's front page to `page.py`; use the NPGallery `_text` form instead.
- `brick.py look` takes one id per call; giving several reads the second as a picture address.
- `tools/videos.py check` must be run from the working folder: run from the clone it reports every added id as "no such place id".
