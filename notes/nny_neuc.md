# nny_neuc: Northern Oswego County: Sandy Creek, Lacona, Pulaski, Mexico
state: New York
region: cny, nny
date: 2026-11-22
places: 15
file: data_nny_neuc.py

## What this batch is
Fifteen places in northern Oswego County, drawn at random by `choose.py --state ny` (region `nny`, which offered Lacona and Sandy Creek); the Atlas had nothing in Oswego County north of Brewerton. Town of Sandy Creek and Richland (`nny`): Selkirk Lighthouse at Port Ontario (1838, private, let as lodging), the Pulaski courthouse (1817–1819, rebuilt 1859–1860), the Pulaski village district, the Lacona depot (1891), the Lacona clock tower (1925, with the 1922 bank noted beside it), and Sandy Creek's Methodist (1878) and octagonal First Baptist (1917) churches. Town of Mexico and Volney (`cny`): the Mexico Point Club ruins (burned 1952) and Casey's Cottage in Mexico Point State Park, the Starr Clark Tin Shop museum, the Mexico Stone Store, the Mexico depot, the Mexico Octagon Barn, the stone Arthur Tavern and Bristol Hill Church. Sources were read through `wiki_raw.py` and `page.py`: Wikipedia, HMdb marker pages and nearby lists, Visit Oswego County's historical guide PDF and directory, the Town of Mexico's parks page, the Friends of Mexico Point Park pages, the Salmon River Lighthouse & Marina page, courthouses.co (Pulaski courthouse) and the Town of Mexico Multiple Property form on NPGallery. Not checked: anything on the ground; service times for the three churches (no congregation pages found); the Starr Clark Tin Shop's hours (only the county tourism page, "free and open by appointment", so `hours='?'`); owners of the two depots, the Stone Store and the Lacona clock tower; whether non-customers may park at the Selkirk marina. Pins that mark only the general spot: the Mexico Octagon Barn (Wikipedia point on the road, no octagonal roof seen) and the Arthur Tavern (Register point in trees), both `prec='area'`; the Lacona clock tower and First Baptist are `site`. The Pulaski courthouse's red brick comes from courthouses.co's description; the Lacona depot's 'no' from its Commons photograph.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Syracuse Northern Railroad bridge remains | Salmon River, Pulaski, NY (43.56404, -76.13031) | Mapped as a ruin in OpenStreetMap beside the South Jefferson Street bridge; abandoned railway mapped either side | No written source; the leaf-off aerial shows only trees on the bank |
| Ard H. Stevens–George Washington Store | 31 Broad Street, Pulaski, NY (geocoder 43.56792, -76.12789) | Visit Oswego County historical guide: Stevens an abolitionist, later owned by George and Lucretia Bakeman Washington, African Americans | Whether the building stands (the guide's standing/gone symbols do not survive in its text) |
| Bethel Church | Lake Road Extension and NY 3, Richland, NY | Same guide: built by George Bragdon 1848–1849, abolitionist members, Luther Lee preached 1861; the federal names file has a "Bethel Church" old church site at 43.57222, -76.18611 | Whether the building stands |
| Mexico Point Inn / Twice-Told Tales | Mexico Point, east bank of the Little Salmon River | HMdb 280325: the second grand hotel at the river mouth | Whether anything is left |
| Pulaski Historical Society Museum | 3428 Maple Avenue, Pulaski, NY | Visit Oswego County guide lists it | Its own page (searches lead to Pulaski, Wisconsin and Indiana societies); what the building is |
| Orson Ames House | 3339 Main Street, Mexico, NY (Register 01001318) | Guide: about 1830, Jerry McHenry sheltered here one night in October 1851; Register form: of Arthur stone | Private house; owner and a picture not checked |
| Blount Lumber factory | 19 Demott Street, Lacona, NY (HMdb 132666) | Built 1894, closed 1992 | Whether the factory buildings stand |

## Tips
- Visit Oswego County's historical guide PDF (`visitoswegocounty.com/wp-content/uploads/2023/12/HistoricalGuideFNL_web.pdf`) reads with `page.py` and lists every museum and Underground Railroad site in the county with an address; its "existing / no longer exist" symbols are lost in the text.
- The Town of Mexico Multiple Property form (`npgallery.nps.gov/NRHP/GetAsset/NRHP/64500455_text`) has a text layer and gives the town's context (Arthur sandstone, the octagon barn, the depot); the single-property forms were not tried.
- Mexico Point Park's pages are at `mexicopointpark.com` (the address printed on HMdb signs, `mexicopoint-park.com`, does not connect).
- HMdb nearby lists run from four points at once gave markers as far as Sackets Harbor and Oneida Lake: the lists are "about the nearest hundred", so a 5-mile radius in thin country reaches far.
