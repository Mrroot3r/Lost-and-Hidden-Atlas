# hud_niic: Livingston, Gallatin, Taghkanic and Stuyvesant, Columbia County
state: New York
region: hud
date: 2026-11-22
places: 13
file: data_hud_niic.py

## What this batch is
Thirteen places in southern and western Columbia County, New York (region `hud`, drawn at random by `choose.py --state ny`, which offered Livingston): the towns of Livingston, Gallatin, Taghkanic, Clermont and Stuyvesant, which the Atlas had nearly nothing in, plus three depots that were leads in `hud_pfit` and `hud_yfpe`. One ruin you walk to: the R. and W. Scott Ice Company ice house at Nutten Hook (DEC, open year-round; pin moved onto the foundation seen on LiDAR). Standing: the Linlithgo Reformed Church and the 1895 town hall with its markers in Livingston hamlet, the 1869 Glenco Mills Methodist Chapel (Register form describes original pews, harmonium and kerosene fixtures), the Gallatin Reformed Church and cemetery (congregation from 1748, meeting house 1823–24), the 1752 Stone Jug, the 1953 West Taghkanic Diner, and the Stuyvesant, Mellenville, Craryville and Copake (Rhinebeck & Connecticut, 1876) depots, the Snyderville one-room school, and the Livingston Manor house site marker (1699 house, gone). Sources: Wikipedia read raw (`wiki_raw.py`), HMdb marker pages, the Glenco Mills Register form (NPGallery PDF, text layer), DEC's Stockport Flats page, Scenic Hudson, The Millerton News (2021), the Governor's 2023 nominations release, roadsidefans.com and an 1878 county history on usgennet.org. Not checked: any interior, service times for the three churches (no parish pages found), the diner's hours (only directories found, so `hours='?'`), owners of the depots and the school, and whether the diner's Indian-head sign is still up. Pins: Mellenville, Copake depot and the Stone Jug could not be told apart from neighbouring buildings on the aerial (Mellenville and Copake are `prec='area'`; the Stone Jug pin is the road corner where its marker stands). Nothing was seen on the ground.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Teviotdale | Linlithgo, Livingston, NY (Wikipedia 42.15361, -73.84056) | Wikipedia: Walter Livingston's stone and brick Georgian/Federal house of about 1773, Robert Fulton's country home, abandoned by the 1920s and restored in the 1970s | Which of several houses near the Wikipedia point it is (not told on the aerial), and whether it shows from the road |
| Oak Hill | Linlithgo, Livingston, NY (Wikipedia 42.2, -73.84444) | Wikipedia: John Livingston's house of 1793, still in the family and used as a wedding venue | Whether visitors may come other than to events, and a pin seen on the aerial |
| Lynch Hotel and James Lynch House | Newton Hook, Stuyvesant, NY (42.3561, -73.7867; 42.3543, -73.7857) | On the Register; Scenic Hudson mentions Newton Hook's 19th-century buildings | Any source read; NPGallery has only the placeholder for both forms |
| Burroughs–Foland Farm | Livingston, NY (42.112799, -73.809239) | Register list: 1903 Mission Revival farmhouse; the form (NPGallery 14000205) has a text layer and was not read | Read the form; whether it shows from the road |
| West Taghkanic Diner hours | NY 82, Taghkanic | Added with hours='?' | The diner's own page with its days and hours |

## Tips
- NPGallery's text route gave placeholders for every older Columbia County form tried (1978 to 2009); the 2014 and 2019 forms had text. The Glenco Mills form came from a search result's `npgallery.nps.gov/GetAsset/<uuid>` address, which `page.py` read as a PDF.
- `photo_find.py look` on seven places ran well over the two-minute command limit; run it in the background from the start.
- `photo_find.py` offered pictures of the hamlet of Livingston Manor (Sullivan County) for the Livingston Manor house site in Columbia County.
- No parish page could be found for the Linlithgo, Glenco Mills or Gallatin churches by web search; `hours.py` will find nothing for them either.
