# kcmo_mtwn_tjwe: Kansas City: Midtown, Hyde Park and the Country Club District
state: Missouri
region: kcmo
date: 2026-11-26
places: 14
file: data_kcmo_mtwn_tjwe.py

## What this batch is
Fourteen standing buildings in Midtown, Hyde Park, Westport's edge, the Country Club District and the east side of Kansas City, Missouri, all National Register listings the Atlas lacked (found by matching the Park Service's Missouri points to the Atlas by distance): the Volker, Shelley, Knight, McIntire, Loose, Gary, Nicholson, Katz, Tromanhauser and Disney family houses, Vanderslice Hall (the August Meyer house), the Walnuts apartments, Christian Church Hospital and the Montgomery Ward warehouse at 19th Street. Facts come from Clio's "Historic Homes of Kansas City" tour and its Disney tour, the Midtown KC Post, the R. A. Long Historical Society, Kansas City Magazine, KC Yesterday, KCUR, Wikipedia and the Park Service record pages. No Register form could be read: the state's PDFs return 404, the Internet Archive is refused, and NPGallery serves a one-page stand-in. Not checked: interiors, who owns each house now, hours (Loose Mansion is open as an event venue and bed and breakfast; its own page was not read, so `hours='?'`), and the exact house for the Nicholson pin (pin is the junction its three neighbours face, `prec='area'`). The Register's points for Knight, Tension, Tromanhauser and Katz were 200 to 290 m off, so those four use address lookups. Pictures: 13 of 14 have a Commons photograph (all by one Commons photographer, 2015), the Walnuts none. Red brick: seen on the pictures for Shelley, Loose, the Montgomery Ward warehouse, Vanderslice Hall and the Gary house; some for Volker and Katz; none for the Disney house (Clio: wood cottage).

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Acme Brass and Machine Works Building | 609-611 East 17th Street, Kansas City, MO | Register 2004, small two-storey industrial building, architect S. W. Hitt (Park Service record) | No page with its history; the form is unreadable |
| Goodenow Textiles, Aines Farm Dairy, Hiland Telephone Exchange, Barclay and Kuehne-Schmidt buildings | Hyde Park, Hanover Place, Holmes Park, Kansas City, MO | Register listings 2003 to 2008 with no coordinates checked | A narrative source for each |
| Walter E. Bixby House | Kansas City, MO (39.0105, -94.6072) | Register 1978; the Magazine Antiques calls it Edward Tanner and Kem Weber's 1935-1937 modernist house | Left out as modernist (the owner's rule); do not add |
| Santa Fe Trail swales at 85th and Manchester, New Santa Fe and Minor Park | south Kansas City, MO | Three Register trail segments, 2012 and 1994 | A source for what can be seen and public access |
| Nettleton Home, Burnette-Berry House, Van Noy houses | south and east Kansas City, MO | Register listings with Park Service points | Any narrative source |
| Truitt House (1916, now a boutique hotel) | Oak Street, Westport, Kansas City, MO | Clio: brick colonial mansion built for realtor Elmore Truitt | An address for a pin and the hotel's hours |

## Tips
- The Wikipedia Register lists for Kansas City are titled "National Register of Historic Places listings in Jackson County, Missouri: Downtown Kansas City" and "...: Kansas City other"; the "Kansas City, Missouri:" titles do not exist.
- `tools/nrhp_state.py "MISSOURI" mo`, then a distance match against `build/sites.json`, gave 71 listings with no Atlas place within 300 m in eight counties; 53 are in Kansas City, and many are apartment blocks.
- Clio's tour page (`page.py --all -n 80000 https://theclio.com/tour/3153`) lists every stop with its text in one call, and each stop's own page (`/tour/3153/<n>`) adds a longer backstory.
- Register points for Kansas City houses can be 200 to 300 m off (Knight, Tension, Katz); `tools/geo.py` with the street address landed on the building every time.
- `photo_find.py` found a Commons photograph for 13 of 14 houses because one photographer photographed most of the city's Register houses in 2015; Midtown and Country Club houses are worth a pictures pass.
- The Kansas City Art Institute's Vanderslice Hall is the August Meyer house "Marburg"; Clio and Wikipedia use different names, so search both.
