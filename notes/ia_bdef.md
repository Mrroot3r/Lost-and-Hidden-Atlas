# ia_bdef: Iowa: a second scatter
state: Iowa
region: ia
date: 2026-11-21
places: 19
file: data_ia_bdef.py

## What this batch is
Nineteen places spread over Iowa, which had 17: in the northwest the Abbie Gardner Sharp Cabin (Arnolds Park), the Grotto of the Redemption (West Bend) and the Sergeant Floyd Monument (Sioux City); in the southwest the Hitchcock House (Lewis) and the Todd House (Tabor); in the middle Salisbury House (Des Moines) and the Scholte House (Pella); in the south the American Gothic House (Eldon), the Mars Hill log church (Ottumwa), Hotel Manning (Keosauqua), Liberty Hall (Lamoni) and Union Church (Davis City); in the east the Amana Colonies, Stone City, Anamosa State Penitentiary and Brucemore (Cedar Rapids); in the northeast the Painter-Bernatz Mill (Decorah) and the Little Brown Church (Nashua); in the north the Surf Ballroom (Clear Lake). All standing places. Facts from Wikipedia and Register list rows read with `wiki_raw.py`, and from the managing bodies' own pages read with `page.py` (State Historical Society of Iowa, westbendgrotto.com, hitchcockhouse.org, the Tabor Historical Society, salisburyhouse.org, pellahistorical.org, americangothichouse.org, villagesofvanburen.com, cofchrist.org, amanaheritage.org, doc.iowa.gov, the City of Decorah, littlebrownchurch.org, brucemore.org, surfballroom.com, the NPS page for the Floyd monument). Pins from ArcGIS PointAddress results or Wikipedia, all looked at on the aerial; the Floyd monument and the Scholte House were moved with `pix.py`. Not checked: hours for Hotel Manning, the Painter-Bernatz Mill (Vesterheim refuses `page.py` with 403), the Anamosa penitentiary museum (its site is gone, 404) and the Amana Heritage Museum (its page draws the hours by script); owner and access at Mars Hill and Union Church (both `view`); whether St. Joseph's at Stone City opens (thestonecityfoundation.org reset the connection); parking at Arnolds Park, West Bend, Lewis, Tabor, Mars Hill, Lamoni and Davis City; which building on the north side of Pella's square is the Scholte House; the Abbie Gardner cabin under the trees on the aerial. Red brick from pictures for Union Church and Hotel Manning (yes), the Scholte House (painted yellow, no) and Stone City (limestone); left '?' for Salisbury House, Liberty Hall, the Amanas, the mill, the Little Brown Church, Brucemore and the Surf. Nothing was seen on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Chicago, Rock Island and Pacific Railroad Stone Arch Viaduct | Shelby, Shelby County, IA (Register list 41.523889, -95.436389; ref 98000870) | Register-listed stone arch railway viaduct | Any source read about what stands and who owns it; a public place to see it from |
| Anamosa State Penitentiary Museum hours | Anamosa, IA | Wikipedia: in a former prison barn and cheese house outside the walls, open seasonally | A page of its own that opens (asp-museum.locable.com answers 404) |
| Painter-Bernatz Mill hours | Decorah, IA | Part of Vesterheim | Vesterheim's hours (vesterheim.org answers 403 to page.py); try the web fetch tool |
| Pella Historical Village and Vermeer Windmill | Pella, IA (507 Franklin Street) | pellahistorical.org gives hours for both | Which buildings are original and moved there; the windmill's date |
| Harlan, Atlantic and Corning courthouse squares | Southwest Iowa | Register rows with coordinates (wiki_raw.py --rows for Shelby, Cass and Adams counties) | Not read: candidates for the southwest, which is still thin |

## Tips
- Iowa Register list pages for small counties redirect to the whole-state list ("National Register of Historic Places listings in Iowa", 149 rows printed for Chickasaw): grep the `--rows` output for the town names.
- The ArcGIS street-address points (StreetAddress, not PointAddress) in Pella and Nashua fell 200 m and 500 m off the building; Wikipedia's point for the Little Brown Church was on it.
- The State Historical Society of Iowa's site pages print the Des Moines museum's own hours at the top before the site's hours: read the "Visiting Information" part with `page.py --all`.
- vesterheim.org answers 403 to `page.py`; pellahistorical.org and the Surf Ballroom's pages read fine.
