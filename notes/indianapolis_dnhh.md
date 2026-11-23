# indianapolis_dnhh: Indianapolis: Monument Circle, the War Memorial and the old north side
state: Indiana
region: in
date: 2026-11-23
places: 16
file: data_indianapolis_dnhh.py

## What this batch is
16 standing buildings in Indianapolis, the first Atlas places in the city beyond the Statehouse and the Medical History Museum: the Indiana World War Memorial, the Soldiers' and Sailors' Monument, the Scottish Rite Cathedral, Union Station, the Birch Bayh Federal Building, the Central Library, Old City Hall, the City Market, the Columbia Club, the Athenæum, the Old National Centre (Murat Shrine) and the Indiana Theatre downtown; Crown Hill Cemetery's Gothic Chapel, the Marott Hotel, St. Joan of Arc Church and Shortridge High School on the north side. The names came from one Old World Exploration video, worked as job 9 (record: `source/videos/20230707_l86-hE7_3Dc.md`); the video was a tip only. Sources: Wikipedia articles read with `wiki_raw.py`; the Indiana War Memorials' tours page (live) and home page (an archived copy of January 2026, because the live address answers 404); the Scottish Rite's tour page; the Indianapolis Public Library's Central Library page; the Crown Hill Heritage Foundation's visit and places pages; the City Market Corporation's release of May 28, 2026; WFYI's report of June 18, 2026 on Old City Hall; The Criterion's 2021 history of St. Joan of Arc (archived copy) and an archived copy of the parish's Mass-times page of October 2025 (the live site answers 403). Not checked: any interior; the Soldiers' and Sailors' Monument's inside hours (the commission's two pages disagree, both given, `conf='mixed'`); whether the War Memorial's Shrine Room has reopened; hours for the Athenæum, the Murat and the Indiana Theatre (performance venues, `hours='?'`); the Athenæum's tour dates; parking for nearly every place (downtown is described generally; Union Station's garage is the one `th=` point); which wing of Shortridge is the 1928 building. Red brick is `yes` only for the Marott (Wikipedia says red brick); limestone and terracotta fronts are `no`; the rest are `?` because no source gave the brick's colour and no picture was looked at with `brick.py`. `check.py` warns that "Scottish Rite Cathedral" reads as a church: it is a Masonic meeting house, so `civic` stands.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Indianapolis Masonic Temple | Indianapolis, IN (39.777222, -86.159167, Register list) | Register-listed (08000193), south of the Scottish Rite Cathedral | No article read; history, condition and access |
| The Ambassador | Indianapolis, IN (39.778889, -86.155833, Register list) | Register-listed apartment building (83000054) with a Wikipedia article | Not read; whether it is worth a stop beyond being an apartment block |
| Central State Hospital remains | Indianapolis, IN, west side | The Pathology Building is on the Atlas as the Indiana Medical History Museum | Which other hospital buildings still stand and who owns the grounds |

## Tips
- The Indiana War Memorials' home page `in.gov/iwm/index.html` answers 404; `page.py` falls back to a January 2026 copy. The tours page (`in.gov/iwm/visitor-information/tours-and-reservations/`) is live and gives the museum and monument hours, which disagree with the home page about the monument.
- `sjoa.org` (St. Joan of Arc, Indianapolis) and `archindy.org` answer 403 to `page.py`; archived copies read, and the `/mass-times` copy gave the Mass times even though `page.py` called it drawn by script.
- `crownhill.org` answers 403; the Crown Hill Heritage Foundation's `crownhillhf.org/visit/` gives the gate hours.
