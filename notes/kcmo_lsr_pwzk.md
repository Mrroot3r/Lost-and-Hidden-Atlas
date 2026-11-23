# kcmo_lsr_pwzk: Kansas City: south, Lee's Summit and Cass County
state: Missouri
region: kcmo
date: 2026-11-23
places: 10
file: data_kcmo_lsr_pwzk.py

## What this batch is
Ten places in south Kansas City, Raytown, Lee's Summit, Raymore, Belton, Pleasant Hill and the Harrisonville and Garden City country in Cass County, Missouri. Earlier sessions had already taken the big Register entries there (Lone Jack, Harrisonville square, Pleasant Hill depot, Unity Village), and Jackson County's own Register list outside Kansas City and Independence is mostly small residential districts, so this batch is smaller than the usual 15 to 20. Facts come from Wikipedia read as raw text, the National Park Service pages for the Raytown museum and the New Santa Fe cemetery ruts, the Great American Stations page for the Lee's Summit depot, VisitMO's page for the Lee's Summit museum and Clio's entry for the Belton society. Several operators' hours are only as web search results quote their own pages (Raytown, Lee's Summit); Belton, Pleasant Hill and the Belton railroad have no hours. National Register forms could not be read. Nothing was checked on the ground. Pins: the New Santa Fe pin has a Commons photograph taken at it showing the cemetery gate; the Robert A. Brown House pin falls in woods and is marked as the general area only; the Lee's Summit depot pin was moved 48 m off the tracks onto the building. The Brown House and O'Bannon Homestead and Watkins Farm are private and the owners were not found. Pictures: three places got one, the rest none.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Blenheim School | 2411 E 70th Terrace, Kansas City, MO | Register 2017 (Kansas City school district multiple listing); a school page says Kansas City bought the land in 1912 and the first school opened in fall 1913; turned into 52 senior apartments in December 2018 (search result quoting the district) | The building's architect, date of the present building and what original fabric survives; the pages were only seen in search results |
| Grandview Historical Depot Museum | 1205 Jones Street (Freedom Park), Grandview, MO | A listing calls it the Kansas City Southern depot of 1912 and gives a society formed in 1981 | The kcparent listing returned 403; no operator page or hours read; the depot's railroad is unclear |
| Bailey Family Farm Historic District | Southwest corner of Bailey and Ranson Roads, Lee's Summit, MO (38.8958, -94.3414) | Register 2006, Prairie School, part of the Lee's Summit multiple listing | The Missouri State Parks form answered 404; no source of what stands or who owns it |
| Vesper Hall | Fleming Park, Lee's Summit, MO | Searches found nothing for it | Any source for a hall at the park |
| Hours for Belton society, Pleasant Hill museum, Belton railroad | Belton and Pleasant Hill, MO | Clio gives March to December, Tuesday and Thursday 1 to 4 p.m., Saturday 10 a.m. to 1 p.m. for Belton | The operators' own pages |

## Tips
- `tools/photo_find.py look` for the Belton society returned the railroad's pictures, because both are in Belton: check each sheet's description, not the distance.
- VisitMO's page for a museum is readable by `page.py --all` and gives hours; the Lee's Summit museum's own pages were not opened.
- The Wikipedia Jackson County Register list (Kansas City excluded) is 52 rows, most of them small Lee's Summit house districts; for this ground the Cass County list (7 rows) and the Kansas City "other" list add more.
- `app_smoke.js` fails with a refused connection unless the Android www server is running; it is not needed for a data-only pull request.
