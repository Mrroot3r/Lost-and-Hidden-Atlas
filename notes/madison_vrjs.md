# madison_vrjs: Madison, Wisconsin: the old campus, theatres and a sugar factory
state: Wisconsin
region: wi
date: 2026-11-28
places: 14
file: data_madison_vrjs.py

## What this batch is
Fourteen standing buildings in Madison, Wisconsin, a city the Atlas had only four places in, taken as leads from the names in one walk-through video (the record is `source/videos/20250815_aUjmQeRhBx0.md`) and each checked in sources: the old University of Wisconsin campus (Bascom Hall, Music Hall, Science Hall, the Red Gym, the Carillon Tower, Memorial Union, Agriculture Hall, Hiram Smith Hall, the Field House), the Wisconsin Historical Society headquarters, the Masonic Temple, the Orpheum and Barrymore theatres, and the Garver Feed Mill (the 1905-06 U.S. Sugar Company beet factory). Sources: Wikipedia read as raw text with `wiki_raw.py` (the Bascom Hill article covers most of the campus), the Park Service records and three Register forms through `form.py` (Orpheum, Masonic Temple, Garver), and the operators' own pages for hours (Wisconsin Union, Wisconsin Historical Society library, Garver Feed Mill, UW School of Music, UW news). Pins are OpenStreetMap buildings, all on the right roof on the aerial. Not checked: interiors; parking except at Garver; theatre show times (hours `?`); the Carillon's present access (the newest page read was 2017); Hiram Smith Hall's architect and year, where the Register record (Ferry & Clas, 1892) and Wikipedia's list (George B. Ferry, 1891) differ, and the Carillon's year (1934, 1935 or 1936 by source).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| St. James Catholic Church | 1128-1130 St. James Court, Madison, WI | Historic Madison Inc.'s page: parish incorporated 1905, a combination church and school built 1905-06, a new church within seven years | The year and builder of the present church, and the parish's own page for Mass times |
| Capitol Theater (in the Overture Center) | State Street, Madison, WI | The Orpheum's Register form: the 1928 auditorium was cut down inside the Overture Center and only its Moorish tower survives outside | Whether the tower is worth a pin of its own, and a source on what can be seen |
| Madison East High School | 2222 East Washington Avenue, Madison, WI | Wikipedia: Collegiate Gothic, Frank Riley, 1922, additions 1925 to 1963 | A Register or city landmark source; a working school, seen from the street only |

## Tips
- The Wisconsin Historical Society's "Records/Article" pages answer 404 to `page.py` but the web fetch tool reads them (the library page is `Records/Article/CS68`).
- carillon.wisc.edu would not connect from the shell; music.wisc.edu event pages and news.wisc.edu carry the carillon's recitals.
- `garverfeedmill.com` reads with the web fetch tool; `/visit` is 404.
