# cat_qhid: Southwestern Otsego County, NY: Unadilla, Gilbertsville, Morris and Oneonta
state: New York
region: cat, scho
date: 2026-11-19
places: 18
file: data_cat_qhid.py

## What this batch is
Eighteen places in southwestern Otsego County, New York, with Sidney over the line in Delaware County, drawn at random by `choose.py --state ny` (region `cat`, which offered Windsor, Tannersville and Unadilla); the Atlas had seven places within 20 km of Unadilla and only the roundhouse lead in Oneonta. Unadilla and Sidney (reg `cat`): the Unadilla village district (area pin on St. Matthew's), the Andrew Mann Inn (1787, private), the Old Unadilla marker (the town burned in 1778) and the Sidney covered bridge replica, with the 1852 bridge's abutment at the end of Bridge Street (pin is the replica; the abutment was not found on the aerial). Farther north (reg `scho`, like the Oneonta roundhouse): Major's Inn and the Gilbert Block and the Old Village Cemetery in Gilbertsville; Zion Episcopal (1818 stone) and All Saints Chapel with the Morris family burial ground in Morris; Otsdawa Baptist Church (1840); in Oneonta the Swart-Wilcox House museum (1807), the D&H passenger station (1892), the 1905 armory, the Oneonta Theatre (1897, closed), the Fairchild Mansion, Huntington Memorial Library, the Wilber House (CANO) and the Old Post Office (city hall); and the Colliersville dam (1906 or 1907; sources differ). All standing except the marker and the abutment. Sources: Wikipedia through `wiki_raw.py` (with the county Register list), HMdb markers and Pomeroy Foundation pages, the Diocese of Albany's parish pages (service times for the Morris churches), the Swart-Wilcox House's own site, Huntington Memorial Library's site, All Otsego and WZOZ/CNY News articles, the Friends of the Oneonta Theatre history page and Michigan Tech's IA archive. Every NPGallery form tried was a placeholder, so no Register form was read. Not checked: anything on the ground; the cemetery's owner and the Otsdawa church's current use; whether the Fairchild Mansion is still the Masonic lodge; current use of the D&H station; full library and CANO hours; parking for most of the village places. Red brick was settled from Wikimedia photographs for Major's Inn (some), the armory, the theatre and the Fairchild Mansion (yes); four stay `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| DeVillers-Cope Mills Historic District | Mount Vision, Town of Laurens, NY | Register listing 100013037 (recent; Wikipedia list row only, no article) | Any source on what stands; NPGallery returns 893 characters of nothing |
| Gilbertsville Water Works | Near Gilbertsville, NY (Wikipedia 42.49361, -75.38972) | 1896, enlarged 1914–18: three dams, pond, gate house, control house, filter beds, NRHP 2011 (Wikipedia) | Owner and whether any of it can be seen; form is a placeholder |
| Unadilla Waterworks | Unadilla, NY (Wikipedia 42.33944, -75.3175) | Two sites built 1880–1891, one building and 11 structures, NRHP 1992 (Wikipedia) | Owner, access, what is visible; form is a placeholder |
| Sidney covered bridge abutment, exact spot | End of Bridge Street, Sidney, NY | HMdb 220631 says the 1852 bridge's stone abutment is still visible there | The abutment on the aerial or a photograph, to pin it apart from the replica |
| Tianderah | Gilbertsville, NY (Wikipedia 42.46389, -75.315) | 1887 stone and shingle house by William Ralph Emerson with stable, NRHP 1978 (Wikipedia) | Whether it can be seen from a public road |
| John Sleeper's log house and grist mill marker | 56 Main Street, Laurens, NY (HMdb 148884, 42.53092, -75.08888) | Log house of 1774 pillaged in 1778; grist mill of 1775–78 stood 200 yards NNE (marker) | Anything to see beyond the stone |

## Tips
- Every Register form tried in Otsego County (92001079, 92001080, 11000290, 97001455, 97001456, 02000143) is an NPGallery placeholder; 100013037 returns 893 characters of nothing.
- The Diocese of Albany's parish pages (`albanyepiscopaldiocese.org/<name>-<town>-ny/`) read with `page.py` and give service arrangements and building dates; All Saints Chapel near Morris opens only for 10 a.m. services on the last Sunday of June, July and August.
- The Pomeroy Foundation's marker pages (`wgpfoundation.org/historic-markers/<slug>`) carry a researched paragraph, the address and a coordinate, more than the HMdb page for the same marker.
- `pix.py pin` on a contact sheet: my first reading of the All Saints chapel was off by about 40 px vertically; re-running the pin check after a move and checking the ring was what caught it.
- Web search returned links with no quoted text throughout this session, so every hour came from a page read with `page.py`.
