# ca_lavd: Los Angeles: downtown theatres, hotels, banks, City Hall and Wilshire landmarks
state: California
region: ca
date: 2026-11-23
places: 16
file: data_ca_lavd.py

## What this batch is
Sixteen standing places in Los Angeles, worked from the names in one Old World Exploration video (the record is `source/videos/20230616_yVI5L9ATai8.md`; 83 rows, 16 places added, 13 names not identified, 49 not checked, 3 elsewhere; nothing within 15 km was on the Atlas before). Added: the Natural History Museum's 1913 Building, the Fine Arts Building, Hotel Alexandria, Bullocks Wilshire, the Biltmore, City Hall, the Herald Examiner Building, the Farmers and Merchants Bank, the Million Dollar Theatre, Angels Flight, the Pacific Electric Building, the Central Library, St. Vincent de Paul Church, the Tower Theatre, the United Artists Theatre and Immanuel Presbyterian Church. Facts are from Wikipedia (wiki_raw.py) and, for hours, the museum's, the library's, Apple's and the archdiocese's own pages. Pins are ArcGIS PointAddress lookups (Angels Flight: the Wikipedia point), each looked at on the aerial; all sit on their buildings, Angels Flight and the museum at site precision. Not checked: City Hall observation deck hours (only travel sites gave them, and they disagree), Angels Flight hours and fare (angelsflight.org answered 403), the Biltmore's public rooms, Immanuel Presbyterian's service times (its page gives none), lobby access at the Fine Arts Building, and red brick for every place (all `?`).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Shrine Auditorium | Los Angeles, CA, Exposition Park area | Named in the video as standing | Sources, pin, access |
| Elks Lodge No. 99 (Park Plaza Hotel) | Los Angeles, CA, Westlake | Named in the video, 1923–24 | Sources, pin, current use |
| Powell Library and Royce Hall, UCLA | Los Angeles, CA, UCLA campus (34.0717, -118.44218 for Powell, Wikipedia) | Wikipedia: Powell Library 1926–1929, Romanesque Revival, modelled with Royce Hall on Sant'Ambrogio in Milan | UCLA visitor rules and library hours |
| Doheny Memorial Library, USC | Los Angeles, CA (34.0201, -118.2838, Wikipedia) | Wikipedia: given by Edward L. Doheny in 1932, Ralph Adams Cram exterior, Samuel Lunden interiors, pale brick and limestone | USC visitor rules and hours |
| Orpheum and Pantages theatres, Hollywood First National Bank, Hayward Hotel, Los Angeles Memorial Coliseum | Los Angeles, CA | Named in the video; standing buildings of these names exist | Sources and pins (49 rows of the record are "not checked") |

## Tips
- The Los Angeles Archdiocese's parish pages (`lacatholics.org/venue/<parish>/`) give each parish's Mass times by day and language and read well with `page.py --all`.
- Apple's store page for the Tower Theatre (`apple.com/retail/towertheatre/`) gives the coming week's hours with `page.py --all`; the plain run shows only one line.
- angelsflight.org answers 403 to `page.py` and the web fetch tool sees an empty page.
