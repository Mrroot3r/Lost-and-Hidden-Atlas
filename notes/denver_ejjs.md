# denver_ejjs: Denver, Colorado: downtown and Capitol Hill
state: Colorado
region: co
date: 2026-11-24
places: 19
file: data_denver_ejjs.py

## What this batch is
Nineteen places in and round Denver, Colorado, which had only the State Capitol: the Daniels & Fisher Tower, the Boston, Kittredge, Equitable and Gas & Electric buildings, the Denver Dry Goods building, the Brown Palace Hotel, Union Station, the Paramount Theatre, the old post office (Byron White U.S. Courthouse), Fire Station No. 1 (the Denver Firefighters Museum), the Mosque of the El Jebel Shrine, the Cathedral Basilica of the Immaculate Conception, Saint John's Cathedral, Central Presbyterian, Trinity United Methodist and St. Mark's (now a nightclub); and outside the city the Castlewood Canyon dam ruins (Franktown) and Westminster Castle (Westminster). The names came from a video about the city (job 9 in PROMPTS.md; the record is `source/videos/20230311_kodpvuBcZMQ.md`). The video was used only as a list of names: every fact comes from Wikipedia read as raw text (and the downtown Denver Register list), Register nomination forms from NPGallery (Boston, Kittredge, St. Mark's, El Jebel), Westword (May 6, 2024) on the El Jebel building, and the pages of Colorado Parks and Wildlife, Denver Union Station and the churches. Hours were read from the cathedral's, Saint John's, Central Presbyterian's and Trinity's own pages and from Colorado Parks and Wildlife; the Brown Palace, Union Station and the Paramount gave none (`hours='?'`), and the Firefighters Museum's site reset the connection, so its hours are not checked. Not checked: any interior on the ground; present owners and uses of the Boston, Kittredge and Equitable buildings (the forms are from 1977 and 1978); whether the Brown Palace lobby welcomes people who are not guests; visiting rules at the federal courthouse; which trail reaches the Castlewood dam (the parking point is the nearest mapped lot, about a kilometre away). Five pins were moved onto OpenStreetMap buildings after the aerial showed the Wikipedia or first point in a street crossing, on a train hall or on the next roof; Union Station, St. Mark's and the courthouse are marked as the site, not exact.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Tivoli Brewery (Tivoli Student Union) | Auraria campus, Denver | Named in the video; no Wikipedia article under "Tivoli Brewery" | A source (try the Auraria campus page or the Register form) and a pin |
| Denver Public Library of 1910 (McNichols Civic Center Building) | Civic Center Park, Denver | Named in the video; part of the Civic Center Historic District | Its own source and hours |
| Denver City and County Building | Civic Center, Denver | Named in the video ("new city hall") | Source, hours, pin |
| Mary Reed Library | University of Denver | Named in the video | Source and access |
| Cheesman Park pavilion | Cheesman Park, Denver | Named in the video | Source and pin |
| Temple Emanuel (two: Curtis Street, 78000853; Pearl Street, 87001554) | Denver | Both on the downtown Register list with Wikipedia articles; the video does not say which | Read both articles |

## Tips
- The Denver Register list is titled "National Register of Historic Places listings in downtown Denver"; "...in Denver" and "...in Denver County, Colorado" come back with no rows.
- `wiki_raw.py` takes `-g` only before the titles: `wiki_raw.py "Title" -g x` reads "-g" and "x" as titles.
- denverfirefightersmuseum.org reset the connection from `page.py` and gave 503 to the web fetch tool.
- `osmnear.py <lat> <lon> 200 buildings` put the Byron White courthouse, the Gas & Electric building (mapped as the Insurance Exchange Building) and Union Station's station house on their buildings when the Wikipedia points fell in street crossings.
