# pe_rhhz: More of Charlottetown and Queens County, Prince Edward Island
state: Prince Edward Island
region: pe
date: 2026-11-19
places: 10
file: data_pe_rhhz.py

## What this batch is
Ten places in Queens County that the batch pe_bhrt lacks. This session drew region pe at random and wrote twenty places; pe_bhrt (same ground, from a run limited to the eastern provinces) merged while it worked, so sixteen duplicates were dropped and six new places added. Charlottetown: City Hall (1888, red brick), Apothecaries Hall (1900, red and buff brick), the Great George Street Historic District, Dundas Terrace (1889 wooden apartment house by W. C. Harris), and Fairholm (1839 red brick villa, now an inn). Rural: St. Augustine's Church, Rustico (1838, oldest parish church in the diocese), North Rustico Lighthouse (1876), Uigg Baptist Church (1874, closed, pews and organ inside), Glenaladale House (1883–1884 brick, private), and the Victoria Community Hall (1915, now the Victoria Playhouse). Sources: the Canadian Register of Historic Places statement for each (historicplaces.ca with `page.py --all -n 60000`, ids from the `{{HPC row}}` templates of the Wikipedia lists for Charlottetown and Queens County); Wikipedia's list of national historic sites in the province (for Apothecaries Hall's brick colour); the Diocese of Charlottetown's February 2026 Mass-times PDF; OpenStreetMap (`nom.py`) and the ArcGIS geocoder for positions. **Not checked:** anything on the ground; hours for St. Augustine's (the diocese table lists 7 p.m., 9 a.m. and 10:30 a.m. but its day columns could not be read), Fairholm and the Victoria Playhouse (hours='?'); who owns the North Rustico Lighthouse and whether it opens; whether the public may go inside City Hall; whether Glenaladale House shows from the road; who owns the closed Uigg church. Pins that mark only an area: Glenaladale House (Register point on a road junction; house not picked out) and the Great George Street district (middle of the street). Pin moved: Uigg Baptist Church, 21 m onto the building in the cemetery. Brick: yes for City Hall, Apothecaries Hall and Fairholm (Register or Wikipedia caption), ? for the lighthouse, Glenaladale (Island brick, colour not stated) and the district. No 1 m LiDAR in Canada; `CHECK ACCESS` lines mean nothing here.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Victoria village Register buildings | Victoria, PE (Main, Howard, Nelson, Russell streets; Register ids 5677 Orient Hotel, 5717–6044 Main Street, 6230–6261) | The Orient Hotel statement read: c. 1900, third storey added about 1930, still a hotel | A `town` entry for the village needs the other statements read |
| Tryon United Church | Tryon, PE | Register 12010 read: 1881 W. C. Harris church; the Register's "current function" lists a library as well as worship | Present use and the right spot (pe_bhrt found the list points wrong) |

## Tips
- Before writing up a region `choose.py` gave you, run `python3 tools/start.py --prs` and `git fetch` again after the first hour: a batch for the same region (pe_bhrt) was started by a session limited with `--state`, merged within 20 minutes of this one's claim, and was not visible at the start. `choose.py --claim` did not stop it.
- historicplaces.ca answered all but two of 40 requests with a 1-second pause; the two that reset worked on a retry after 3 to 8 seconds.
- The Diocese of Charlottetown's Mass-times PDF (`dioceseofcharlottetown.com/wp-content/uploads/2026/02/Masstimesfec2426.pdf`) reads with `page.py`, but the day columns run together; only parishes with a full row of times can be read with confidence.
- `pix.py pin` worked on the sheet pixel straight from the contact sheet; `look.py` at 200 m half-width settled which building a rural church is.
