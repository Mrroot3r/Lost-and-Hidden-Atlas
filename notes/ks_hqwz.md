# ks_hqwz: Johnson County, Kansas, second pass
state: Kansas
region: ks
date: 2026-11-23
places: 14
file: data_ks_hqwz.py

## What this batch is
Fourteen places in Johnson County, Kansas, round Olathe, Shawnee, Merriam, Gardner, Edgerton, Stilwell and De Soto (Kansas City area, Kansas side), added on top of the earlier Johnson County batch (ks_dvmh). The Atlas had 7 places within 15 km of Olathe and 19 round Shawnee before. They come from the Kansas Historical Society's Johnson County register search (46 listings, read with page.py and from the cached HTML), National Register forms read as text from NPGallery (Ott, Parker, Pickering, Olathe Cemetery, McCarthy, Redel, Turner barn, Sunflower Village), Wikipedia articles (wiki_raw.py), and a news story for the Walker School. Pins are address lookups checked on the Kansas 2024 aerial; Sunflower Village was moved onto the houses. Not checked: anything on the ground, interiors, hours of Olathe Cemetery, present use of Clement's Market, and the nomination text of the 2021 to 2024 listings (Downtown Gardner, Voigts, Wolcott are from the register summary and Wikipedia only). Left out on purpose: the Shawnee Indian Cemetery (a tribal-owned sacred burial ground, no invitation to visit found). The Walker School pin is the church that holds services in it, from OpenStreetMap.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Hodges House and Hyer House (Hycrest) | Olathe, KS (425 S. Harrison; 505 E. Cedar) | State Register houses of 1990 and 1984 (Tudor Revival; Bungalow) | Any source beyond the register summary |
| Shawnee Grade School; Edgerton Grange Hall; Dr. Harkey House | Shawnee, Edgerton, Gardner, KS | Register listings | Sources beyond the register summary; Shawnee Grade School (2023 listing) has no page I could find |

## Tips
- NPGallery text for listings numbered 100000000 and up returns a picture, not text (page.py shows `PNG`): those forms cannot be read this way; the Kansas register summary is all there is.
- The Kansas register search page cut by page.py: the whole page is in research/pages/*.html; text can be pulled from it with a few lines of Python.
- Johnson County Post (johnsoncountypost.com) pages read well with page.py --all and had the Walker School story; hmdb.org gave 403.
