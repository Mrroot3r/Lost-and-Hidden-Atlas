# portland_tdis: Portland, Oregon (old downtown)
state: Oregon
region: or
date: 2026-11-26
places: 17
file: data_portland_tdis.py

## What this batch is
Seventeen standing old buildings of central Portland, Oregon, taken as leads from the names in one walk-through video of the city's old buildings (the record is source/videos/20260814_obQPN1X1k_g.md; 72 names, 27 of them already torn down). Added: First Congregational, First Presbyterian and First Baptist (the White Temple) churches; City Hall; the 1914 Multnomah County Courthouse; the U.S. Custom House; the Benson, Multnomah and Imperial hotels; the Meier & Frank Building; the Central Library; Union Station; the Wells Fargo Building; the Hollywood Theatre; the Arlene Schnitzer Concert Hall (Portland Theatre); Lincoln Hall; and the St. Johns Bridge. Facts come from Wikipedia (tools/wiki_raw.py), the National Register list for South and Southwest Portland (--rows), Archiseek for the White Temple, and the pages of First Presbyterian, the City of Portland (2022 notice of City Hall hours), Amtrak's Great American Stations and First Baptist read with tools/page.py. The Central Library and Hollywood Theatre hours are from their own pages as web-search results quoted them (the pages drew by script or refused the tool). Not checked: service times for First Congregational and First Baptist (no page that surely belongs to the church gave them, so both are view with hours '?'); the hotels' and the concert hall's visiting hours ('?'); Union Station's waiting-room hours (Amtrak's page refused); red brick for nine places ('?'); nothing on the ground. Every pin was looked at on the aerial and sits on its building; the St. Johns Bridge has a parking point in Cathedral Park.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Neighborhood House | Portland, OR (45.5011, -122.6794) | On the National Register (79003737), 1910, by A. E. Doyle (Wikipedia stub) | A description of the building and its present use |
| Shanghai tunnels (Old Portland Underground) | Old Town Chinatown, Portland, OR | Wikipedia: passages under Old Town; the kidnapping stories are doubted by historians; tours have run since the 1970s | A tour operator's own page with hours and where the tour begins |
| Sunnyside Congregational Church | Portland, OR | Named in the video as built 1909 to 1910; a Wikipedia search suggests Staub Memorial Congregational Church | Whether it is the same building and still stands |

## Tips
- The Portland video named 72 buildings and 27 of them were already torn down; its standing ones are nearly all downtown on the National Register list for South and Southwest Portland, so `wiki_raw.py --rows -g` on that list settles most names in one call.
- OpenStreetMap's "Multnomah County Courthouse" is the new 2020 courthouse on SW 1st Avenue; the 1914 one needs the Register point.
- `tools/videos.py check` run with the clone as the working folder reports every added id as "no such place id"; run it from the workspace (it reads the built place list there).
