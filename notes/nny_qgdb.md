# nny_qgdb: Jefferson County: Sackets Harbor, Cape Vincent and the Thousand Islands
state: New York
region: nny
date: 2026-11-18
places: 17
file: data_nny_qgdb.py

## What this batch is
The first close pass in region `nny` (drawn at random by `choose.py --state ny`), mostly Jefferson County. Sackets Harbor: the battlefield and 1850s Navy Yard (NYS Parks), the 1817 stone Union Hotel (Seaway Trail Discovery Center), the Fort Pike earthworks and Madison Barracks. Cape Vincent: Tibbetts Point Lighthouse, the 1856 Duvillard Mill (now the DEC fisheries aquarium) and the ruins of the British Fort Haldimand on Carleton Island (Thousand Islands Land Trust, no public access). Thousand Islands: Rock Island Lighthouse (boat only), Boldt Castle and Yacht House, and Singer Castle on Dark Island (Town of Hammond, St. Lawrence County). Inland: the 1837 Stone Mills Union Church and the Irwin Brothers Store (both the Northern NY Agricultural Historical Society's), the 1841 Dexter Universalist Church, the General Jacob Brown Mansion in Brownville, the 1850 Paddock Arcade in Watertown, the Chaumont railroad station, and the ruins of the New York Central's 1919 roundhouse in Watertown. Sources: Wikipedia through `wiki_raw.py`; NYS Parks, NYS DEC, TILT, boldtcastle.com, singercastle.com, the Tibbetts Point lighthouse society, HMdb, OABONNY and the Cape Vincent waterfront plan PDF through `page.py`. Not checked: anything on the ground; whether the Seaway Trail Discovery Center and the Dexter church museum still open (no current page found); hours at Stone Mills, the Brown Mansion and the Paddock Arcade; who owns the roundhouse ground (by working track) and the Fort Pike walkway; Boldt Castle's current hours (its page still shows 2018). Pins: Fort Haldimand and the roundhouse were placed from the LiDAR sheet (rampart enclosure; turntable pit with radial stall pits), Fort Pike's bastion shows on LiDAR too. The Jacob Brown Mansion and Paddock Arcade pins are `site` (not on a building that could be confirmed). Brick was left `?` wherever the sources say brick without a colour.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Bedford Creek Bridge | Hounsfield, NY (43.90889, -76.12) | 1825 stone arch, 18 ft 6 in span, National Register 1989 (Wikipedia) | NYSDOT has a project to replace the culvert carrying NY Route 3 over Bedford Creek; whether that is the listed arch, and whether it still stands, was not settled (the project page is drawn by script) |
| Grist mill built in 1805 | Philadelphia, NY (44.15919, -75.70885) | OpenStreetMap ruin point with that name | No source found that describes it or its owner |
| Talcott Falls Site | Adams, NY | National Register 74001244 (no coordinates in the list) | Falls are on private property (nnywaterfalls.com); what the site is was not read |
| LeRay Mansion | Fort Drum, NY (44.05, -75.76333) | LeRay de Chaumont estate, National Register district (Wikipedia) | Inside Fort Drum; public access rules not checked |
| Vincent LeRay House (Stone House) | Cape Vincent, NY (44.12598, -76.34202 from HMdb 75682) | Built 1815 by J. D. Le Ray de Chaumont; sheltered Canadian rebels in 1838 (1932 marker) | Private house; owner and whether it is worth a pin from the road not decided |

## Tips
- The NRHP form text for the Duvillard Mill (85002461) came back as a one-page scan with no text layer, like the Schenectady forms.
- The Cape Vincent Local Waterfront Revitalization Program section II (`docs.dos.ny.gov/opd-lwrp/...CapeVincentSII.pdf`) has a building-by-building historic inventory with dates and current uses; it tied the Duvillard Mill to the DEC Fisheries Station. Other NY villages' LWRP PDFs on that site may do the same.
- `boldtcastle.com/visitorinfo/hours-of-operation` still showed 2018 dates in November 2026; `www.boldtcastle.com/` itself reads as 75 characters.
- The Tibbetts Point lighthouse society's site is served from a `flugelhorn-pike-5nnj.squarespace.com` address; `capevincent.org/lighthouse/` returns almost nothing.
- In Watertown the `--lidar` pin sheet showed the buried roundhouse turntable and stall pits under woods that look like nothing on the aerial: worth running on every OpenStreetMap ruin lead in the North Country.
- `gh api .../pulls` printed nothing at the second check (no open PRs at that moment), and `publish.sh` then stopped because `data_hud_sgld.py` had been merged meanwhile; `resync.sh` fixed it in one step.
