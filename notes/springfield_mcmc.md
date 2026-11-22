# springfield_mcmc: Massachusetts: old Springfield, from Court Square to the Quadrangle
state: Massachusetts
region: pv
date: 2026-11-22
places: 12
file: data_springfield_mcmc.py

## What this batch is
Twelve standing buildings in Springfield and one in West Springfield, from a "videos" session (job 9) working one Old World Exploration video about Springfield (the record is `source/videos/20231217_bmx9lrgqaFQ.md`; 28 names: 12 places added, 1 already on the Atlas, 7 gone, 7 not checked). The Atlas had only the Armory within 6 km. Added: the Municipal Group (City Hall, Symphony Hall, Campanile), H. H. Richardson's Hampden County Courthouse, South Congregational Church, Trinity United Methodist Church (the 1929 church; the downtown one the video shows was razed in 1922), Union Station (1926), the Central Library, the Science Museum, the George Walter Vincent Smith Art Museum, the Hotel Kimball, the Paramount Theater, Classical High School, and the Eastern States Coliseum. Sources: Wikipedia read with `wiki_raw.py`; Lost New England and Historic Buildings of Massachusetts with `page.py`; Sacred Spaces of New England for Trinity; Cinema Treasures for the Capitol Theatre's fate. Hours from the city's page, the Springfield Museums, the City Library, Union Station's FAQ, and each church's own page (read November 22, 2026). Pins are OpenStreetMap or Wikipedia points, all looked at on the MassGIS aerial; Union Station was moved off the platforms onto the building, and South Congregational is `site` because the buildings at the bend of Maple Street could not be told apart. Not checked: any interior except as sources describe; whether work on the Paramount began in 2026; street parking and garage fees downtown; red brick for Union Station, the Kimball, Trinity and the Smith Art Museum (its picture shows orange-buff brick that could not be called red with confidence).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Mutual Life Insurance building | Springfield, MA | A video names it; probably Massachusetts Mutual Life's old building on Main Street | Which building, whether it stands, a source |
| Northwestern Mutual Life building | Springfield, MA | A video names it | Which building and whether it stands |
| Western Railroad offices (H. H. Richardson, late 1860s) | Springfield, MA, beside the old Union Station site on Main Street | Lost New England's old Union Station post describes it | Whether anything stands |
| Remaining Smith & Wesson building | Stockbridge Street area, Springfield, MA | Lost New England says one later Smith & Wesson building is part of an apartment complex near the old Milton Bradley factory | Which building, its date |

## Tips
- `videos.py check` reads everything after "added " as the place id: put any note about the row in the "Likely name" column, not after the id.
- Lost New England (lostnewengland.com) reads cleanly with `page.py --all` and gives demolition dates for Springfield buildings that Wikipedia lacks.
- The Springfield City Library's opening hours sit in a table that `hours.py page` misses; `page.py --all -n 200000` and a grep for "Hours" finds them.
