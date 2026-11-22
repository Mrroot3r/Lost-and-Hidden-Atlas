# troy_iqwc: Troy and Lansingburgh: St. Joseph's, St. Augustine's, Frear's, the armory
state: New York
region: troy
date: 2026-11-22
places: 7
file: data_troy_iqwc.py

## What this batch is
Seven places in Troy and Lansingburgh (region `troy`, drawn by `choose.py --state ny`), filling gaps in a city that already had about ninety: St. Joseph's Church in South Troy (1847 parish, Tiffany windows, Carmelite Latin rite), St. Augustine's Church in Lansingburgh (1864–66), Frear's Troy Cash Bazaar (1897 department store), the 1918–20 armory on Fifteenth Street that RPI bought in 1971, the Soldiers and Sailors Monument in Monument Square (1891), the Theta Xi chapter house (1931) and the Chapel + Cultural Center at RPI (1968, National Register 2011). Sources were read with `wiki_raw.py` and `page.py`: The Evangelist (Diocese of Albany), the diocese's parish pages on rcda.org (Mass times for St. Joseph's), St. Augustine's own site (Mass times), the Lansingburgh Historical Society's pages, Brownstoner's 2013 history of Frear's, the state military museum's armory page, RPI's archives, the Rensselaer Newman worship page. Every pin was looked at on the leaf-off aerial; none is a trailhead. Not checked: any interior (the Frear stair and atrium today, St. Augustine's interior), which shops are now open in the Frear building (the account is from 2013), parking and permit rules on the RPI hill, and red brick for four places (only St. Joseph's was settled, from a Commons photograph). The armory's build year differs between sources (1918–19 against 1920); the entry gives both.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Troy waterworks pumping station remains | Lansingburgh, Troy, NY (849 Second Avenue, 42.78457, -73.67329) | Lansingburgh Historical Society, quoting Waite's 1976 Architecture of Lansingburgh: 1880 pumping station by Sherman and McDonough; pump house gone, river intake and superintendent's house remained in 1976 | The leaf-off aerial shows a large modern commercial building with a parking lot at 849; the house looks gone. Whether the intake is visible from the river bank |
| St. Peter's Church (Troy) | North Troy, NY (lot at Hutton Street and Fifth Avenue per The Evangelist; Commons photos near 500 River Street) | The Evangelist: parish 1824, first church 1830, rebuilt after a fire about 1846–49, Meneely ten-bell chime 1896; closed 2009 with St. Paul the Apostle | Whether the church still stands and who owns it; abandonedonline.net has a page (403 to page.py) |
| St. Paul the Apostle Church (Troy) | Troy, NY | The Evangelist: founded 1890, designed by Edward Loth, Munich glass windows; closed 2009 | The address and whether the building and its glass survive |
| J. J. Child Steamer Co. No. 11 firehouse | Lansingburgh, Troy, NY (Fifth Avenue and 106th Street, geocoder 42.76280, -73.67871) | Lansingburgh Historical Society, quoting Waite 1973: firehouse occupied 1902, last used 1971 | No firehouse is mapped at the corner on OpenStreetMap and the aerial does not settle it; whether it still stands |
| Our Lady of Victory Church and its 1832 rectory | Sycaway, Troy, NY (55 North Lake Avenue) | Parish history (olvols.org): parish 1922, rector in Dr. Marsh's Gothic farmhouse of 1832, still the rectory; first church February 1923 | When the present church was built; the history page is long and was only searched |
| Sacred Heart Church (Troy) | Troy, NY (310 Spring Avenue) | Diocese of Albany page gives Mass times; parish 1913 (Wikipedia parish list) | Any source on the building |

## Tips
- `photo_find.py new` counts a place as having its own Wikipedia article when its only Wikipedia link is a list page (here "List of parishes in the Diocese of Albany"), so it skips it; `wikiTitle()` in the app already ignores list pages. Run `photo_find.py look <id>` by hand for such a place.
- `photo_find.py look` on a downtown store (Frear's) pulled sixteen nineteenth-century trade cards one by one and took about ten minutes; start it in the background early.
- The Diocese of Albany's parish pages follow `https://www.rcda.org/parishes/parish/<name>-<town>-ny` (for example `st-josephs-church-troy-ny`) and give current Mass times when the parish's own site is gone.
- The Lansingburgh Historical Society site has a page for almost every old building and business in Lansingburgh; list them from the links on its archives-am and archives-nz pages.
