# cosprings_ktkk: Colorado Springs, Colorado: downtown, the college and the Broadmoor
state: Colorado
region: co
date: 2026-11-27
places: 17
file: data_cosprings_ktkk.py

## What this batch is
Seventeen standing places in and round Colorado Springs, which had none (Miramont Castle in Manitou Springs was the only place within 15 km): the old El Paso County Courthouse (Pioneers Museum), the Mining Exchange, First Baptist Church, the City Auditorium, City Hall, the Carnegie library, St. Mary's Cathedral, Cutler, Palmer and Bemis halls at Colorado College, the School for the Deaf and the Blind, the Union Printers Home, the Broadmoor, the Will Rogers Shrine of the Sun, the Alamo Hotel, the YWCA building and the Manitou Cliff Dwellings. The names came from a video about the town (job 9 in PROMPTS.md; the record is `source/videos/20230819_PNhedFhd2TA.md`); the video was used only as a list of names. Facts come from Wikipedia read as raw text (and its El Paso County Register list), SAH Archipedia's Buildings of Colorado entries (nodes 8632 to 8696 cover El Paso County and read in full with `page.py --all`), and the own pages of the Pioneers Museum, St. Mary's Cathedral, First Baptist Church, the Pikes Peak Library District, the Cheyenne Mountain Zoo (for the Shrine), the Union Printers Home's owners and the Mining Exchange hotel. Not checked: interiors and visiting rules for the Mining Exchange, the Broadmoor, City Hall, the Auditorium and the college halls; hours of the Manitou Cliff Dwellings (its page came back unreadable); present use of the YWCA building; red brick for First Baptist, Bemis Hall and the YWCA. The zoo's page contradicts itself on whether the Shrine closes on Sundays as well as Mondays; both are given. Palmer Hall's pin is the Wikipedia coordinate on a lawn and is marked as the site only.

## Leads
Places you read about and could not finish. One row each. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| St. Francis Hospital (old building) | Colorado Springs, CO (Pikes Peak Avenue and Prospect Street; OpenStreetMap has a mapped ruin "St Francsis Health Center" at 38.83261, -104.80961) | Wikipedia's "Tuberculosis treatment in Colorado Springs": the city's first hospital, a three-building complex, one built in 1929 as a sanatorium | What stands today and who owns it |
| Ivywild School | Colorado Springs, CO | Named in the video with the year 1917 | Any source opened; no Wikipedia article under that title |
| Colorado City's old city hall | 2902 West Colorado Avenue, Old Colorado City (38.851197, -104.868478) | SAH Archipedia node 8696: built 1888, stone front, now commercial; on the National Register | Access and present use; not written up for lack of time |

## Tips
- SAH Archipedia's El Paso County entries are `https://sah-archipedia.org/node/8630` to `8700`; a loop over `page.py --all` printing the second line gives every title in a minute, and the text follows "Permissions and Terms of Use".
- The Manitou Cliff Dwellings' own pages (cliffdwellingsmuseum.com) came back as unreadable binary to `hours.py page` and `page.py`.
- Wikipedia's "The Broadmoor" has no coordinates (0, 0); the ArcGIS geocoder on 1 Lake Avenue lands on the main building.
