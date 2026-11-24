# pottsville_zxpw: Pottsville, Pennsylvania
state: Pennsylvania
region: pane
date: 2026-11-24
places: 12
file: data_pottsville_zxpw.py

## What this batch is
The first places in Pottsville, Schuylkill County (the Atlas had nothing within 15 km), taken as leads from one Old World Exploration video (record: `source/videos/20231015_aQCJ53ku1kQ.md`) and checked one by one. 12 standing places: the 1851 county jail (still the county prison), the 1892 courthouse, the 1913 armory (now the YMCA), the Yuengling brewery (free tours), the United Presbyterian Church (Tiffany windows sold, replicas in place), the Henry Clay Monument, the 1863 Female Grammar School (the county historical society), the North Centre Street business blocks, the Necho Allen Hotel, the 1922 library, Garfield Square and the 1932 high school. Sources: SAH Archipedia's Pottsville entries (`sah-archipedia.org/buildings/PA-02-SC1` to `SC24`, read with `page.py --all`), Wikipedia read with `wiki_raw.py`, Yuengling's own Pottsville page (tour hours), the historical society's May 2023 newsletter (its hours; the society's website gives none), the library's about page, the Synod of the Trinity's two articles on the Tiffany windows and the Tiffany census. Pins from the ArcGIS geocoder (PointAddress) or OpenStreetMap; all looked at on the state leaf-off aerial; the armory was moved onto the YMCA point. Not checked: the library's opening hours (its site gives none), the United Presbyterian church's service times, the courthouse's office hours, who owns the Henry Clay Monument ground and whether a path climbs to it, who owns Garfield Square, fees at the Mahantongo Street garage, and anything inside the buildings beyond what SAH Archipedia says. The National Register forms for the downtown district (82003819), the brewery (85000180) and the armory (91001701) are not on line at NPGallery.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Trinity Episcopal Church | Pottsville, PA (South Centre Street at West Howard Avenue) | Napoleon LeBrun, 1847; 1887 Lamb frescoes, 1920 parish house by Zantzinger, Borie and Medary, Samuel Yellin ironwork (SAH Archipedia PA-02-SC4) | Service times from the parish's own page, and a pin |
| Church of St. Patrick | Pottsville, PA (Mahantongo and South 4th streets) | Edwin Forrest Durang, 1891–1892 (SAH Archipedia PA-02-SC7) | Mass times from the parish page, and a pin |
| Reading Anthracite Company building | Pottsville, PA (200 Mahantongo Street) | 1905 terra-cotta Beaux-Arts office of the Philadelphia and Reading Coal and Iron Company; library and museum inside (SAH Archipedia PA-02-SC6) | Whether the museum opens to visitors, and when |
| Frank D. Yuengling Mansion | Pottsville, PA (1440 Mahantongo Street; 40.67861, -76.20833 from Wikipedia) | 1913 Tudor house, now the Schuylkill County Council for the Arts (Wikipedia; SAH Archipedia PA-02-SC10) | The council's visiting hours, and a pin check |
| Cloud Home (John Bannan House) | Pottsville, PA (351 South 2nd Street) | 1851 fieldstone house with Corinthian porticoes and two octagonal Gothic outbuildings (SAH Archipedia PA-02-SC3) | Who lives there and what can be seen from the street |
| Second Presbyterian Church building | Garfield Square, Pottsville, PA | Congregation merged into United Presbyterian in 1968 (Tiffany census) | Whether the building stands and what it is now |
| Charles Baber Cemetery gatehouse | Market Street at 14th Street, Pottsville, PA | 1867 Egyptian Revival gatehouse by Thomas Meehan (SAH Archipedia PA-02-SC11) | Cemetery hours and a pin |
| Majestic Theatre | 209 North Centre Street, Pottsville, PA | 1910, William H. Lee, restored (SAH Archipedia PA-02-SC15) | Its own page and show times |

## Tips
- SAH Archipedia's Pottsville and Schuylkill County entries are numbered `https://sah-archipedia.org/buildings/PA-02-SC1` to `SC24` (SC25 answers 404); `page.py --all` reads each, the title is in the cached page's `<title>`, and the text sits between "Print Source" and "Writing Credits".
- HMdb.org answered 403 to `page.py` again (November 24, 2026), so the PHMC marker texts for the courthouse, the jail and the Clay monument could not be read.
- The Schuylkill County Historical Society's website gives no hours; its newsletters (PDFs on `orca-marlin-583a.squarespace.com`) print them in the masthead.
- `videos.py check` reads "added <id>: remark" as an id with a colon on the end and reports no such place: put a remark after "added <id>" in brackets.
