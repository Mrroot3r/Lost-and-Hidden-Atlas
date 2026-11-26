# milwaukee_ijfn: Milwaukee, Wisconsin: breweries, churches and downtown landmarks
state: Wisconsin
region: wi
date: 2026-11-26
places: 18
file: data_milwaukee_ijfn.py

## What this batch is
Eighteen standing buildings in Milwaukee, a city the Atlas had only one place in, taken as leads from the names in one walk-through video (the record is `source/videos/20230517_wmryOpy1Wys.md`) and each checked in sources: the Pabst, Blatz and Schlitz brewery complexes, the Basilica of St. Josaphat, the Cathedral of St. John the Evangelist, St. Stanislaus, the Tripoli Shrine Temple, the Mayer Boot and Shoe factory, the Central Library, the Federal Building, the Mitchell and Mackie buildings, City Hall, the Germania Building, the Pabst Theater, the North Point Water Tower, Old Main at the Soldiers Home and the Pfister Hotel. Facts come from Wikipedia raw text and the Register list for Milwaukee, the Wisconsin Historical Society property records, the Encyclopedia of Milwaukee, SAH Archipedia, Urban Milwaukee and the VA's Milwaukee pages. Hours come from the owners' own pages (Milwaukee Public Library, the cathedral, the Institute of Christ the King, Best Place); the basilica's visit page answered 403 and its hours are from what a web search quoted from it; City Hall's and the Pabst Theater's pages could not be read, so their hours are '?'. Pins are address points or OpenStreetMap points, all on the building on the aerial; the basilica was moved onto its dome. Not checked: interiors of the private buildings, whether visitors may walk the VA grounds round Old Main, whether the Tripoli temple opens to the public, red brick on the Blatz stock houses, Germania Building, Tripoli and the Pabst Theater, parking (downtown street parking only).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Milwaukee County Courthouse | Milwaukee, WI (43.0414, -87.9239, Register list) | Classical Revival courthouse by Albert Randolph Ross, finished 1931 (Register list) | Not read; access and pin |
| Johnston Hall, Marquette University | Milwaukee, WI (43.038333, -87.926944, Register list) | 1907 hall that held all of Marquette College (Register list) | Not read |
| Wisconsin Club (Alexander Mitchell House) | Milwaukee, WI (43.0397, -87.9237, Register list) | Mitchell's house, begun 1848; the old Deutscher Club (Register list) | Not read; private club access |
| Ward Memorial Hall, Soldiers Home | Milwaukee, WI (43.0256, -87.9764, Register list) | 1881 to 1882 theatre by H. C. Koch, to be restored (VA) | Visitor access to the VA grounds |
| Milwaukee-Downer Quad | Milwaukee, WI (43.0783, -87.8786, Register list) | Four college buildings of 1897 to 1905, now UW-Milwaukee (Register list) | Not read |
| Milwaukee Normal School / Girls Trade and Technical High School | Milwaukee, WI (43.0408, -87.9358, Register list) | 1885 Queen Anne normal school by E. Townsend Mix (Register list) | Not read |
| Pabst Brewery Saloon and Schlitz saloons | Milwaukee, WI (43.046111, -87.93; 43.0003, -87.8931, Register list) | Brewery-built corner taverns of 1896 and 1897 (Register list) | Not read |

## Tips
- The Wisconsin Historical Society property records (`page.py --all -n 12000 https://www.wisconsinhistory.org/Records/Property/HI<n>`) read well; their own search page answers 404, so find the HI number with a web search.
- The Wikipedia coordinate for the Mackie Building is in Lake Michigan; the address point is right.
- thebasilica.org, city.milwaukee.gov and pabsttheatergroup.com refused `page.py` (403 and 406).
- `tools/geo.py` with a full street address and ZIP gave PointAddress hits on every downtown Milwaukee building.
