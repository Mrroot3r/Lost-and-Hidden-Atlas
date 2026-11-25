# kcmo_lex2_pdrb: Lexington, Higginsville and Lee's Summit, Missouri: second pass
state: Missouri
region: kcmo
date: 2026-11-25
places: 12
file: data_kcmo_lex2_pdrb.py

## What this batch is
Twelve places: nine round Lexington and Higginsville (Lafayette County, about 40 miles east of Kansas City) and three nearer the city (Blue Mills, the Sibley railroad bridge, the Lee's Summit historical cemetery). Eight of the twelve were leads left by earlier notes (the Madonna of the Trail, Machpelah and Forest Grove cemeteries, the Houx-Hoefer-Rehkop and Dinwiddie houses, Blue Mills); those rows are deleted. I started with Lee's Summit, Raytown and Grandview as the ground and found the earlier passes had left nothing there that a readable source could back, so I went on to Lexington.
Sources: Wikipedia read as raw text; the Lexington city and chamber of commerce pages (`page.py`); Missouri Preservation pages; the University of New Mexico Santa Fe Trail page on Blue Mills; the parish page of Christ Church; Waymarking pages that copy historical-marker and Register text (Christ Church, the Madonna). Web search results were used only to find pages, and what is written comes from pages opened. Not checked: Register forms (not readable, see Tips), the owner and opening hours of both Lexington cemeteries, the Lee's Summit cemetery and Heritage Park, whether anything of Blue Mills can be seen, the insides of every building. The pins for Forest Grove Cemetery, the Zion AME Church and the Saluda memorial mark only the area: the aerial did not show them clearly. The Madonna's exact corner follows a coordinate on Waymarking and was not settled against a second source. Pictures: only the Madonna has one; Commons offered nothing for the others that fits.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Englewood Theatre | 10917 E. Winner Road, Independence, MO | Opened July 1949; closed 2007; Register listing; a nonprofit bought it in 2025 (KSHB, Kansas City magazine, Jackson County Historical Society pages) | Streamline Moderne of 1949, so left out as possibly a style the Atlas does not want; the owner can decide |
| Georgen House, Smallwood Noland House, Woodson-Sawyer House | Independence, MO | Register list only: a Craftsman house (Georgen), a Greek Revival house at 1024 S. Forest (Noland), a house at 1604 W. Lexington | A source that says what each is and what is left |
| Bailey Family Farm Historic District | Lee's Summit, MO (38.8958, -94.3414) | Register 2006, Prairie School farm | Nothing readable beyond the Register list |
| Lexington Municipal Auditorium (1939 WPA) | Courthouse Square, Lexington, MO | Buff brick Art Deco Streamline Moderne, Register-listed, 99-year lease to a nonprofit (Missouri Preservation) | Left out as a modernist style; owner may overrule |
| Lexington Masonic College earthworks, Old Catholic Cemetery, Zion AME's later owners | Lexington, MO | Named on the chamber's points-of-interest list | A source for each |

## Tips
- Plain `mostateparks.com` Register PDFs answer 404, NPGallery `_text` files are placeholders, `dnr.mo.gov` answers 503 and the web fetch tool refuses archive.org: no Missouri Register form is readable from a session. Chamber-of-commerce, city, Missouri Preservation and Waymarking pages were readable and often quote the form.
- Lee's Summit, Raytown, Grandview and Independence are done as far as Wikipedia, Clio and the city pages allow (also said in `kcmo_ind2_qfhm`); the next gain in the Kansas City area is in the counties round it (Lafayette, Ray, Cass) or needs a person with the Register forms.
- `historiclexington.com` pages read well with `page.py --all`; `?p=` numbers lead to per-place pages.
- Wikipedia's category listing "Buildings and structures in Kansas City, Missouri" through the API (`curl` with a plain user agent) lists articles the Register list lacks.
