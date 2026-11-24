# sandiego_mgjl: San Diego: Gaslamp Quarter blocks, downtown hotels and theatres, Balboa Park
state: California
region: ca
date: 2026-11-24
places: 16
file: data_sandiego_mgjl.py

## What this batch is
A "videos" session (PROMPTS.md job 9). The names came from one video, "Old World San Diego" by Old World Exploration (https://www.youtube.com/watch?v=dGmazYWabS8); the record of all 48 names is source/videos/20230908_dGmazYWabS8.md. The video was a tip only: no fact here rests on it. Added 16 standing places, the first in San Diego: in the Gaslamp Quarter the district itself, the Louis Bank of Commerce, the Nesmith-Greely Building, the Cole Block and the Odd Fellows Building; downtown the Balboa Theatre, the Spreckels Theatre, the U.S. Grant Hotel, the San Diego Trust and Savings Bank Building, the San Diego Athletic Club and the Santa Fe Depot; on Cortez Hill El Cortez and St. Joseph Cathedral; in Bankers Hill the Park Place Methodist church (The Abbey); in Balboa Park the California Quadrangle and the Spreckels Organ Pavilion. Facts come from Wikipedia (`wiki_raw.py`), the county's National Register list (`--rows`) and Wikipedia's "List of Gaslamp Quarter historic buildings" for addresses and dates. Hours: the Museum of Us and the Spreckels Organ Society's own pages (web fetch tool). Not checked: the cathedral's service times and the Balboa Theatre's box office (their pages answered 403 or 406), hotel and station hours, who owns the depot, and most interiors. Most pins were moved from the Register point to the ArcGIS street-address point (PointAddress) and looked at on the aerial; the Trust and Savings Bank pin stays on the Register point, marked site. Red brick was settled for four places only (Nesmith-Greely yes from a Commons picture; Louis Bank granite, Spreckels Theatre and the Athletic Club concrete); the rest are '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Marston Building | 809 Fifth Avenue, San Diego, CA (32.71381, -117.16002) | 1881; San Diego Historic Landmark (Wikipedia, List of Gaslamp Quarter historic buildings); no article of its own | A source for its story; look at the pin |
| Old City Hall (Commercial Bank Building) | 664 Fifth Avenue, San Diego, CA (32.71246, -117.16028) | 1874 (same list) | A source beyond the list row |
| First National Bank Building | 904 Fifth Avenue, San Diego, CA (32.71485, -117.16030) | 1884, San Diego Historic Landmark (same list) | A source beyond the list row |
| Sweetwater Dam | Bonita / La Presa, San Diego County, CA (32.69139, -117.00806) | Masonry arch dam of 1888, raised later, still in use (Wikipedia) | Where the public may see it from, and the owner's page |
| Lomaland buildings, Point Loma Nazarene University | Point Loma, San Diego, CA (32.71685, -117.25069) | Theosophical community 1900 to 1942; the campus keeps many of its buildings (Wikipedia, Lomaland) | Which buildings stand, and whether visitors may walk the campus |
| California Theatre | Third Avenue and C Street, San Diego, CA | 1927 theatre, derelict; news reports say it was bought in 2026 and demolition was expected from mid-December 2026 | Whether it still stands; probably gone soon |

## Tips
- The San Diego NRHP rows are in "National Register of Historic Places listings in San Diego County, California"; there is no city list title.
- Wikipedia's "List of Gaslamp Quarter historic buildings" gives each Gaslamp building's address, year and a coordinate (`wiki_raw.py` saves the raw table in research/wikiraw/).
- `geo.py "<number street>, San Diego, CA 92101"` gave a PointAddress for every downtown address tried; the Register point for the Park Place church fell in Balboa Park, 110 m from the building.
- sdcathedral.org, sdcatholic.org, gaslampfoundation.org and sandiegotheatres.org answered 403 or 406 to both `page.py` and the web fetch tool; the web fetch tool cannot open web.archive.org here.
