# cleveland_lnbb: Ohio: old Cleveland, from Public Square to University Circle
state: Ohio
region: oh
date: 2026-11-22
places: 15
file: data_cleveland_lnbb.py

## What this batch is
Fifteen standing places in Cleveland, from the names in one Old World Exploration video about the city (the record is source/videos/20221203_hvRfITuDjbs.md; the video is a tip and nothing rests on it). The Atlas had nothing within 6 km of downtown before. Downtown: the Soldiers' and Sailors' Monument on Public Square, the Arcade, Hotel Cleveland, the Cuyahoga County Courthouse, City Hall, the Main Library, the Tiffany Glass (Citizens) Building, the Rose Building and Trinity Cathedral; further out the Cleveland Masonic Temple, the West Side Market in Ohio City, the Shrine Church of St. Stanislaus in Slavic Village, and in University Circle and Lake View Cemetery the Cleveland Museum of Art, Severance Hall and the James A. Garfield Memorial. Facts are from Wikipedia (read with wiki_raw.py) and the National Register list for Cleveland; hours from the owners' own pages read with page.py: Lake View Cemetery (memorial and gates), the museum's visit page, the library's Main Library page, westsidemarket.org/hours (drawn by script, but --all read the hours), the St. Stanislaus parish page (address 3649 E 65th St checked), Trinity's services calendar (only the 9 a.m. time is given; the other services are named without times), the Cleveland Orchestra's guest-services page. Pins are ArcGIS PointAddress results, or the Wikipedia point for the monument and the Garfield Memorial; all looked at on the aerial, and the monument pin was moved about 60 m from the roadway onto the monument. Not checked: opening hours of the monument (its commission's page lists only events), the Arcade, Hotel Cleveland and City Hall; whether courthouse and City Hall interiors may be visited; Severance Hall's public tour dates (the orchestra's tour page is drawn by script); downtown garage hours and fees. Red brick: St. Stanislaus 'yes' from Wikipedia ("locally made warm red brick"); West Side Market 'some' (the clock tower reads red-brown, the hall buff, from the article's Commons photo); Trinity, the Rose Building and the library 'no' from their Commons photos; granite, sandstone or marble from the articles for the courthouse, monument, Garfield Memorial and museum; the rest '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Grays Armory | 1234 Bolivar Rd, Cleveland, OH (41.49889, -81.68222, Register list) | Wikipedia: built by the Cleveland Grays from 1893, sandstone and scarlet brick, a theatre organ from Erie; open houses and organ concerts | Its own page for visiting times; the video's "armory" could not be tied to it |
| Old Stone Church | Public Square, Cleveland, OH (41.500278, -81.695, Register list) | On the Register list | Not read; not named in the video |
| Cleveland Police Headquarters (old Central Police Station) | Payne Ave, Cleveland, OH | Named in the video only | Which building was shown, and a source |
| Gordon Park stone bridge | Gordon Park, Cleveland, OH | Named in the video only | Whether it still stands, and a source |

## Tips
- In Cleveland the Wikipedia Register list is one page, "National Register of Historic Places listings in Cleveland, Ohio" (293 rows), with --rows and -g working.
- The ArcGIS geocoder gave PointAddress results on the buildings for every downtown and University Circle address tried.
- lakeviewcemetery.com moved its Garfield page to /visit/james-a-garfield-memorial; the old /visit/garfield-monument/ answers 404.
- photo_find.py candidates at the Cleveland Museum of Art pin are all artworks inside; Wikipedia's article picture is also not one the Atlas may use.
