# mo_wbkr: Johnson County, Missouri: Warrensburg, Knob Noster, Chilhowee
state: Missouri
region: mo
date: 2026-11-25
places: 14
file: data_mo_wbkr.py

## What this batch is
Fourteen standing places in Johnson County, Missouri, about 50 miles south-east of Kansas City: the two Warrensburg courthouses (the 1838–41 Old Courthouse run as a museum, and McDonald's 1898 sandstone one), the Masonic Temple, the Jones Brothers Mule Barn, the Holden and Pine Streets district, the 1890 depot, the Warren Street Methodist church, the Grover Street houses, the Cress and Griebel houses (one entry), the Garden of Eden filling station, Pleasant View School, the Chilhowee business street, the Adams (Cedarcroft) farmstead, and the Montserrat Recreation Demonstration Area works in Knob Noster State Park (one entry). The Atlas had nothing in the county but the Holden mausoleum. The other Kansas City-side Register lists (Cass, Ray, Platte, Jackson, most of Lafayette) were compared by coordinate with the map first and had almost nothing missing.
Sources: Wikipedia raw text; the Johnson County Historical Society's own tour page (jocomohistory.org), which says what is open, closed or gone; the Missouri State Parks Register list; three Register forms that opened (courthouse, Chilhowee, the Holden and Pine district); Cedarcroft's own history page; Clio; web search results that quote other pages. Hours of the Old Courthouse differ on three pages and are written as a disagreement. Not checked on the ground: everything. Not read: the forms for the other places. Knob Noster's pin is the visitor centre and marks the park only, because the Register points for the bath house, dam and bridge fall 1 to 2 km east of the park's two dams.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Howard School | 400 W. Culton St., Warrensburg (38.7642, -93.7256) | Built 1888 for the town's Black pupils on a lot bought in 1867; the historical society's tour page says the building collapsed and was removed about 2016 | Gone as far as one page says; a marker or the site |
| Magnolia Mills | 200 W. Pine St., Warrensburg (38.7631, -93.7431) | Wikipedia: only the concrete elevator of the 1879 mill is left; the society's tour page says the wooden mill and elevator were torn down in the early 2000s; a Commons photograph of 2018 shows a tall concrete elevator | Which is right; a source for what stands now |
| Theodore Gosewisch House | near Lexington, Lafayette County (39.1578, -93.8917) | Wikipedia: about 1847 Greek Revival brick I-house, on the Register since 1997 | Any page on access or its present state; pin check |
| Montserrat dam, bath house and bridge | Knob Noster State Park | Commons photographs of all three exist and give positions: the bath house is about 680 m and the dam about 870 m from the visitor centre | The photographs' exact points, then separate pins; the park's hours |
| Camp Shawnee Historic District | Knob Noster State Park | 30 frame buildings of 1936–41 | A coordinate |
| Adams Farmstead tours | 431 SE County Road Y | The society says tours by appointment; the owners' page says the bed and breakfast closed | Whether tours still run |

## Tips
- Missouri State Parks Register forms now answer at `https://mostateparks.com/sites/g/files/zuston361/files/media/pdf/2025/02/<name>.pdf` (courthouse, Chilhowee and the Holden and Pine district read well; others are scans or 404). The older tips saying every Missouri form was unreadable are out of date.
- `jocomohistory.org/national-register-sites-in-johnson-county/` reads with `page.py --all`: the county society's tour says which places are closed, gone or by appointment, which Wikipedia does not.
- Wikipedia's Register coordinates were off by 100 to 200 m in four of fourteen cases (Old Courthouse, Mule Barn, Chilhowee, Adams farmstead); `geo.py` on the street address landed on the building each time.
- `photo_find.py look` is a good way to find where a Register point is wrong: Commons photographs named for the place come with positions (Knob Noster).
- A Columbia Missourian page prints part of its text scrambled (looks like paywall obfuscation); it was not decoded.
