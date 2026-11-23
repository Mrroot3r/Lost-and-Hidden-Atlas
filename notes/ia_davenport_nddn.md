# ia_davenport_nddn: Davenport, Iowa
state: Iowa
region: ia
date: 2026-11-23
places: 17
file: data_ia_davenport_nddn.py

## What this batch is
Seventeen standing buildings in Davenport, Iowa, which had no place on the Atlas, taken from the buildings named in one video of old postcards of the town (the record is source/videos/20230809_eJ_Of8bmHDA.md); the video was a tip only and nothing in the entries comes from it. Added: the First National Bank Building, the Davenport Bank and Trust Building, the Kahl Building with the Capitol Theatre, City Hall (1895), the Old City Hall (1857, now Oxford Flats), the Central Fire Station, the Hotel Blackhawk, the Hotel Mississippi with the Adler Theatre, the Burtis Opera House remnant, the Col Ballroom (Saengerfest Halle), Trinity Episcopal Cathedral (Grace Cathedral), Sacred Heart Cathedral, First Presbyterian Church, St. John's United Methodist Church, Ambrose Hall at St. Ambrose, Central High School and the J. Monroe Parker–Ficke House. Facts are from Wikipedia read as raw text (`wiki_raw.py`) and the Register list rows for Downtown, East and West Davenport; service times from the four congregations' own pages (`hours.py page`); pins from OpenStreetMap buildings (`osmnear.py ... buildings`) or point-address lookups, every one looked at on the aerial. Not checked: anything on the ground; parking for every place; whether the banking halls of the two banks can be visited; the Capitol Theatre's box office (its site answered 406); City Hall's office hours (not on the city's home page); the Col Ballroom's use since it closed in 2018; the present user of the Burtis Opera House building. Red brick is '?' for seven places whose sources say brick without a colour. The Burtis Opera House's Wikipedia picture is an old view of the opera house and hotel before the fire, not the building as it stands. Eight names in the video are gone (the 1886 courthouse, the Davenport Hotel collapsed and demolished in 2023, the Kimball House, the first Burtis House, the Carnegie library, St. Luke's Hospital, St. Margaret's Cathedral, the macaroni factory's first building).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| St. Mary's Roman Catholic Church Complex | Davenport, IA (41.525436, -90.594739) | Register list: church, rectory, school and convent of St. Mary's parish, Romanesque and Colonial Revival | Its article and Mass times not read |
| St. Katharine's Historic District | Davenport, IA (41.528611, -90.56) | Register list: girls' school buildings by Cochrane and Hammatt | Article and present use not read |
| Clarissa C. Cook Library | Davenport, IA (41.525270, -90.574389) | Register list: Davenport's first library building, 1878, later the Blue Ribbon News Building | Whether it stands as it was; not read beyond the list row |
| Marycrest College Historic District | Davenport, IA (41.531049, -90.598555) | Wikipedia: college closed 2002, campus now senior housing | Which building is worth a pin; access |
| Vander Veer Park conservatory | Davenport, IA (41.5438, -90.5752) | Wikipedia: Central Park renamed Vander Veer; a conservatory added after World War I | The conservatory's age and hours from the city's page |
| Northwest Davenport Turner Society Hall | Davenport, IA (41.535989, -90.596701) | Register list: built 1882, one of three Davenport Turnvereine | Whether the video's downtown Turner Hall is this or another; present use |
| Saint Ambrose: Lewis Hall | Davenport, IA | Named in the video only | A source |

## Tips
- `wiki_raw.py --rows "National Register of Historic Places listings in Davenport, Iowa"` finds no rows: the city list is split into "Downtown Davenport", "east Davenport" and "west Davenport" (lowercase east and west in the titles).
- `wiki_raw.py "German Free School"` returns the one in Austin, Texas; Davenport's was not found under that name.
- The Capitol Theatre's site (capitoltheatreqc.com) answered HTTP 406 to `hours.py page`.
- `videos.py check` takes `added <id>;` but not `added <id>:` (the colon is read as part of the id), and "on the atlas" fails for a place added in the same batch.
