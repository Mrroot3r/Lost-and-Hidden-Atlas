# kcmo_ls2_ydhk: Kansas City: Raytown and Vale
state: Missouri
region: kcmo
date: 2026-11-26
places: 3
file: data_kcmo_ls2_ydhk.py

## What this batch is
Three places in south-east Kansas City and Raytown, from the Lee's Summit, Raytown and Grandview part of the Kansas City ground (the Atlas had 20 places within 15 km of Lee's Summit before and 23 after; Lee's Summit's own Register listings were already on the map). Far fewer than the 15 to 20 aimed for: that ground is nearly worked out. Four Gates Farm, Vale Tunnel and Richards Field come from Wikipedia read as raw text, Clio entries, the Historical Marker Database and Missouri State Parks. A fourth, St. Peter's Episcopal Church in Harrisonville, was dropped because it is already on the map. Not checked: the National Register forms (the state's copies return 404 and the National Park Service copies are placeholders), who owns Four Gates Farm, which body manages the Vale Tunnel stretch of the trail, where exactly the Richards Field marker stands, and anything on the ground. No picture was chosen for the tunnel or the airfield (the only near picture of the tunnel area shows a small stone culvert).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Bailey Family Farm Historic District | SW corner of Bailey and Ranson roads, Lee's Summit (38.8958, -94.3414) | Register 2006; NPS record lists Prairie School style | Nomination form (state copy 404, NPS copy a placeholder): what buildings stand, and whether anything can be seen from the road |
| Howard Neighborhood Historic District | SE 5th, Green, 7th and Miller streets, Lee's Summit (38.9085, -94.3734) | Register 2007, community planning and architecture | A readable form, and a best building to pin |
| Bayles Addition and four other Lee's Summit house districts | Lee's Summit (38.909, -94.382) | Register districts 2008 to 2013 per Wikidata and Wikipedia | Forms; mostly ordinary houses, so likely not worth a pin |
| Hickman Mills town site and Hickman's mill | Hickman Mills, Kansas City (38.919, -94.519) | Wikipedia: mill built 1854, closed 1859; exact site not known | Anything that stands |
| Cooper & Black (Poos) Building | 11 SE 3rd St, Lee's Summit | Marker by the Lee's Summit Historic Preservation Commission, built about the 1890s (HMdb) | A source read in full; may be inside the downtown district pin |
| Kansas City Register and the Kansas City part of the Register list | Kansas City, MO | The Wikipedia list is split into sub-pages whose titles I could not find (wiki_raw.py found NO SUCH ARTICLE for six guesses) | The right titles; Wikidata (wd_nrhp.py mo) lists south Kansas City entries instead |

## Tips
- tools/wd_nrhp.py mo gives a quick list of Register listings with coordinates; compare it with build/sites.json by distance to find listings the Atlas lacks. Check the id with grep before writing: my gap check missed an existing Harrisonville entry because the Wikidata coordinate was 30 m off the Atlas pin.
- mostateparks.com's old Register PDFs (Bailey Farm, Four Gates, the Lee's Summit and Grandview surveys) all return 404 and the web fetch tool refuses web.archive.org, so those forms cannot be read unattended.
- HMdb.org's nearby list returns 403 from here.
- Wikipedia's geosearch API (curl with a plain user agent) works but is throttled; run it in the background.
