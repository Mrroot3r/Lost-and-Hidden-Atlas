# kcmo_xtrd: Kansas City: Crossroads and downtown (second pass)
state: Missouri
region: kcmo
date: 2026-11-24
places: 8
file: data_kcmo_xtrd_hwqn.py

## What this batch is
Eight places in downtown Kansas City, the Crossroads and the West Side: the Mainstreet Theater, the TWA headquarters, the Jenkins Music Company building, the Midwest and Monroe hotels, Webster School, the Guadalupe Center and Our Lady of Guadalupe Shrine. This is fewer than the 15 to 20 asked for. I looked first at Johnson County, Leavenworth, Lawrence, Cass, Clay, Ray and Lafayette Counties, found each already worked by earlier batches, and settled on the Register list "Downtown Kansas City" (about 160 rows), where roughly 120 listings still had no place. Most of those have no Wikipedia article, and NPGallery has only placeholders for them, so only the ones with an article or a Clio entry could be written up. Facts come from Wikipedia as raw text (Mainstreet, TWA, Jenkins, Monroe, Midwest) and Clio entries and a KCUR story read with page.py (Midwest, Monroe, Webster, Guadalupe Centers, the shrine). Not checked: hours for anything, interiors, whether the Symphony took over Webster School, current tenants of the Jenkins and TWA buildings, the date of the present Guadalupe Center building (the Register form could not be read), and the Midwest and Monroe hotels' ownership today. The Jenkins and Monroe pins mark the block (prec area): the aerial could not pick the building out. Red brick: Webster yes (a Commons photograph), Guadalupe Center no (white stucco, photograph), TWA no (aluminium and concrete panels, Wikipedia), shrine no (gray stone, KCUR), Midwest and Monroe some (Clio: brick with terra cotta), the others unchecked. Photographs: Webster and the Guadalupe Center got one; the shrine has none on Commons; the other five have Wikipedia pictures.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Imperial Brewing Company Brewery | 2825 Southwest Boulevard, Kansas City, MO | Built 1901 to 1902, a flour mill from 1919 to 1985, on the Register in 2011; web search results say it was demolished in 2023 | The pages (Wikipedia, Clio) were not opened; a gone site with nothing to see |
| Switzer School Buildings | West Side, Kansas City, MO (39.0903, -94.5940) | Register list: listed December 2009; a library record says the main building is from 1899, by Charles A. Smith, with a Depression-era addition | Pages that open; the Register form is not on line |
| Helping Hand Institute Building | 523 Grand Boulevard, River Market, Kansas City, MO | Register 2000, social history, 1915 to 1950 | Pages that open |
| Liquid Carbonic Company Building | 1900 block of Wyandotte, Crossroads, Kansas City, MO (39.0892, -94.5844) | Wikipedia: built 1913, a soda fountain maker, Register 1994 | A fuller source |
| Gumbel, Bunker, Baker-Vawter, Columbia and Studna buildings, Westminster Congregational Church | Downtown, Crossroads, Hyde Park, Kansas City, MO | Register listings with Commons categories but no Wikipedia article | Any page that describes them |
| Houx-Hoefer-Rehkop House and James M. Dinwiddie House | Higginsville and Dover, MO | Register listings of 1983 and 1997 | Their forms are not digitized and Wikipedia has one line on Dover |

## Tips
- Greater Kansas City is nearly all taken: Johnson, Leavenworth, Lawrence, Cass, Clay, Ray and Lafayette Counties already have batches. What is still open is the Wikipedia Register list "Jackson County, Missouri: Downtown Kansas City" (about 120 listings with no Atlas place) and its "Kansas City other" list (Hyde Park, Valentine, Westport apartments and houses). A script that matches the first two words of each name against `tools/data_*.py` finds them.
- NPGallery's `_text` files for 1970s to 2010s Kansas City listings are mostly the "not yet digitized" placeholder, and the NARA S3 copies answer 403. A web search for the building name followed by `theclio.com` finds a Clio entry for many of them, and page.py reads it whole; the search tool's own summary is not a source until the page is opened.
- `tools/start.py` for a town counts only places within the radius, so Lafayette and Ray Counties looked empty (Waverly: 0) when earlier batches had in fact worked Lexington, Higginsville and Richmond; checking the notes folder for the town names is quicker than trusting the count.
- The Commons photograph of Webster School settled red brick at once; for other places on the list a photograph by the user Mwkruse of each Register listing is often on Commons.
