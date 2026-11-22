# columbus_vcyp: Columbus, Ohio: downtown and the Ohio State campus
state: Ohio
region: oh
date: 2026-11-22
places: 14
file: data_columbus_vcyp.py

## What this batch is
Fourteen places in downtown Columbus and on the Ohio State campus, taken from the names in one Old World Exploration video (job 9; the record of every name is `source/videos/20230709_ja43hoeHWtI.md`). The Atlas had only the Statehouse within 8 km. Standing: the LeVeque Tower, the 1861 Ohio State Arsenal (Cultural Arts Center), the 1887 post office and courthouse, the Great Southern Hotel and Southern Theatre, the Carnegie Main Library, the Atlas (Columbus Savings and Trust) Building, the Downtown YMCA, the 1899 deaf institution building (Cristo Rey High School), Broad Street United Methodist and First Congregational churches, Orton Hall, the Hoster brewery buildings and Green Lawn Cemetery; and the Union Station arch, the one piece left of Burnham's station. Sources: Wikipedia articles and the Columbus Register list (`wiki_raw.py`), and with `page.py` the Orton Geological Museum's pages, Columbus Recreation and Parks (Cultural Arts Center, McFerson Commons), Green Lawn Cemetery's maps page, the library's hours sheet (dated January 2024), and the two churches' own visit pages. Pins from the ArcGIS geocoder's address points, every one looked at on the aerial; the post office pin was in the street and was moved onto the building. NOT checked: nothing on the ground; the Southern Theatre's and the hotel's hours; whether the Hoster complex redevelopment (Front & Fulton) is finished; what the Downtown YMCA is used for since its 2023 sale; where in Green Lawn the chapel stands (the pin is the office address, `prec='area'`); downtown parking. Twelve names in the video were left "not checked" (three clubs, the old county jail, St. Francis and St. Anthony hospitals, the institution for the feeble-minded, unnamed firehouse, high school and university buildings).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Hayes Hall | Ohio State University, Columbus, OH | Built 1893, the oldest building on campus, on the Register with Orton Hall (Wikipedia: University, Hayes and Orton Halls) | Not named in the video; a pin and the building's visiting rules |
| Wyandotte Building | 21 W Broad St, Columbus, OH (39.9619, -83.00134) | Burnham's firm, 1897–1898, called the city's first skyscraper (Wikipedia) | Its present use after the 2024 sale offer; a look on the aerial |
| Athletic Club of Columbus | 136 E Broad St, Columbus, OH (39.96278, -82.99694) | 1915 club building, private (Wikipedia) | Not checked against the video's unnamed club pictures |

## Tips
- The Register list coordinate for the deaf institution is right (39.9608, -82.9890) but Wikipedia's article on Cristo Rey Columbus High School gives a point 2.9 km west; the geocoder for 400 E Town St agreed with the Register.
- The geocoder gave a street-centre point, not a PointAddress, for 121 E State St (the old post office); the address point for 100 S Third St lands nearer the building.
- frontandfulton.com would not connect, and no current source said whether the Hoster redevelopment had opened.
- The Columbus Metropolitan Library's hours sheet is a PDF at columbuslibrary.org/branch-address-location-hours-of-operations-2024-01; `page.py --all` reads it and the Main Library line is easy to grep.
