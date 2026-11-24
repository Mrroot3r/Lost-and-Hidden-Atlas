# superior_pnqa: Superior, Wisconsin: boom-era blocks, library and mansion
state: Wisconsin
region: wi
date: 2026-11-24
places: 12
file: data_superior_pnqa.py

## What this batch is
Twelve standing buildings in Superior, Wisconsin, a city the Atlas had nothing in but the SS Meteor. Seven come from the names in one walk-through video (the record is `source/videos/20231104_jqCNC8DOM0k.md`): the New Jersey Building, the New York and Empire blocks, the 1908 federal building at 1401 Tower Avenue, the 1901 Carnegie library, Old Main at UW-Superior and the old Franklin School. Five more are the boom-period buildings round them on the Register: the Minnesota Block (Board of Trade), the Washington and Berkshire blocks, the Trade and Commerce Building and Fairlawn. Facts come from the National Register forms read as text from NPGallery (`page.py`), the Wisconsin Historical Society's property records (later surveys and demolitions: the Massachusetts Block and the Wemyss Building on the Register list are demolished), the Douglas County Historical Society's school pages, Wikipedia read raw, the Library History Buff page quoting a 1999 state survey of the Carnegie library, WPR and B105 news. Nothing from the video went into an entry. Pins: OpenStreetMap building points, checked on the aerial; the 1401 Tower Avenue address point fell in the street and was moved to the three-storey building on the west side of Tower at 14th (Commons has a photograph of the federal building taken about 60 m away; not matched by name). Not checked: nothing was seen on the ground; Fairlawn's hours (the museum's site refused connections and its archived copy could not be fetched); who owns the Carnegie library now; the present use of the federal building and the Trade and Commerce Building; the Franklin School pin is the OpenStreetMap "Franklin Courts" apartment building on the block the historical society gives. check.py warns that five pins are just outside the Wisconsin outline: they are in Superior, on the Wisconsin side of the bay, on the aerial.

## Leads
Places you read about and could not finish. One row each. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Maryland Block (Badger Building) | Superior, WI, Tower Avenue (46.723333, -92.104167, Register list) | 1892 Neoclassical block by the Land and River Improvement Company (Register list) | Its Register form and whether it still stands |
| Roosevelt Terrace | Superior, WI (46.715278, -92.102778, Register list) | 1890 Richardsonian Romanesque apartments by Carl Wirth, owned by James Roosevelt Sr. (Register list) | Its form, current state, a pin on the building |
| Hammond Avenue Presbyterian Church (Harrington Arts Center) | Superior, WI, 1401 Belknap Street | 1911 Neo-Gothic church by Earl W. Barber, cream brick, highly intact in a 2012 state survey (state property record HI17546) | The arts centre's own page and hours |
| Douglas County Courthouse | Superior, WI, 1313 Belknap Street (46.721111, -92.096944) | 1918-1919 Classical Revival courthouse of Bedford limestone by Royer and Radcliff (Wikipedia, Register list) | The county's opening hours |
| Second Nelson Dewey School (1934) | Superior, WI, between 24th and 25th avenues East and East 6th and 7th streets | Alternative school 1995-2002 (Douglas County Historical Society) | Whether it stands and what it is now |
| Superior YMCA | Superior, WI, Ogden Avenue at 14th Street | Four-storey pressed brick and stone building by E. W. Barber on an old postcard (Perfect Duluth Day, search result only) | Whether it stands |

## Tips
- The Wisconsin Historical Society property records (`page.py --all`) gave the later surveys the 1985 Register forms lack, including two Register blocks now demolished; the record numbers for downtown Superior run in order along Tower Avenue (HI17825 to HI17864), so one can read a street block by block.
- superiorpublicmuseums.org refused connections from `page.py` and the web fetch tool (503), and the web fetch tool cannot reach web.archive.org; Fairlawn's hours stay unchecked.
- zenithcity.com's Superior pages that search results list answered 404.
