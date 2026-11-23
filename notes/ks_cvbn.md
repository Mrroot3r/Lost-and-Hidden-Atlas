# ks_cvbn: Kansas: Miami County
state: Kansas
region: ks
date: 2026-11-23
places: 17
file: data_ks_miami_cvbn.py

## What this batch is
Seventeen places in Miami County, Kansas (Paola, Osawatomie, New Lancaster), 45 to 55 miles south of Kansas City, where the Atlas had nothing. I meant to work Johnson County (Olathe, Shawnee, Lenexa) but two batches from earlier today had already taken its Register listings, so I moved south. Sources: the Kansas Historical Society's county register search, National Register forms for the bridges and the Mills House (NPGallery text), Wikipedia one article at a time, the Kansas Historical Society's John Brown Museum page (hours), the Ursuline Sisters' page, and the descriptions on Wikimedia Commons photographs, which quote the newer forms. Pins were checked on the 2024 Kansas aerial: the Ursuline pin was moved 44 m onto the building; the two New Lancaster pins and the hospital pin mark the hamlet or campus (`prec='area'`). Not checked: interiors, who owns the Osawatomie and New Lancaster buildings, whether the two Marsh arch bridges and the Creamery road are open to cars, the courthouse, library, community center and church hours (no page of the body that runs them could be read), and the age of the Ursuline auditorium's listing. The Creamery Bridge date differs between sources (1931 on the National Register form, 1930 in a Commons caption). Red brick was set from the Commons photographs for the courthouse, city hall, Mercantile building and auditorium, from the register summary for the Jackson Hotel, and left '?' for the library, the grange hall's neighbour and the hospital. 11 places have a picture (the six with Wikipedia pictures show them by themselves).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Judge D.B. Wilson Homestead | Plum Creek Road, Paola vicinity, KS | State Register 2023: a two-storey limestone ruin built into a hillside with terraces and a large chimney, 1857 to 1917; on private farmland with no access road | A coordinate (the form has none that was read) and the owner's permission to visit |
| First Presbyterian Church of Paola | Paola, KS | Register listing 2023 to 2025; Commons photographs show a red brick church with a 1904 cornerstone | Any text about it: the nomination was not readable |
| Fowler and Baehr Buildings | 118 and 120 S. Silver Street, Paola, KS | Two brick commercial buildings, the south one built 1907 (Commons caption) | A source for the north building's date and use |
| West Elementary School | 1009 Pacific Avenue, Osawatomie, KS | National Register 2024, part of the Public Schools of Kansas listing | Date and description |
| Jake's Branch of Middle Creek Bridge | southwest of Louisburg, KS | 1985 form: reinforced concrete arch, 47 ft long, 13.5 ft wide, 14 ft above the stream | A reliable coordinate and a date |
| Martin Farmstead | 31943 and 31860 W 247th St, Paola vicinity, KS | Register 2019: sixteen farm resources, 1879 to 1964, windmill and silos | Access (private farm) |
| Johnson County leftovers | Johnson County, KS | Not yet on the map: Horn-Vincent-Russell Estate (Mission Hills), Loomis Historic District (Merriam), Blackfeather Farm (Stilwell), Campbell Dome House (Overland Park), Shawnee Indian Cemetery, Virginia School (Shawnee), Westwood Hills, Hammer and Morrow barns, Spring Hill district | Sources beyond the register summaries; most are private houses |

## Tips
- Johnson, Douglas, Wyandotte and Leavenworth counties in Kansas were all worked earlier today; Miami County (Paola, Osawatomie) was empty, and so are Franklin (Ottawa) and Linn counties.
- The Kansas register search saves its pages in research/pages/ as HTML; pages with the county code MI list Miami County, but its fifth page would not come through page.py.
- Wikimedia Commons file descriptions for 2026 photographs of newer Kansas listings (Dcomputerman12, SharonPapierdreams) quote the nomination text, so `photo_find.py look` doubles as a way to read a form that NPGallery serves only as an image; it cuts each description short, though.
- WebSearch returned no hours for the Jackson Hotel or the Paola library from their own pages; the Kansas Historical Society's John Brown Museum page gave its hours directly, though `page.py -g` missed the hours line and the saved HTML had it.
