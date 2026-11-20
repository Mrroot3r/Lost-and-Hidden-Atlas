# conf_fvsv: The Boght, Loudonville and Menands
state: New York
region: albco
date: 2026-11-20
places: 8
file: data_conf_fvsv.py

## What this batch is
Eight places in the Town of Colonie just west and south of Cohoes and Watervliet. Region `conf` was drawn at random by `choose.py --state ny`, but Cohoes, Waterford, Watervliet and Green Island had five batches already and the HMdb nearby list for Waterford gave nothing new (the village entry already names the Eddy house, the bank robbery and the concrete Smith house), so the batch took the Colonie ground round them, where `start.py` showed no Atlas place in Loudonville or Menands. All are filed under `albco`, as earlier conf batches filed Colonie. The Boght: the Van Denbergh-Simmons House (Dutch part about 1720–60), the Simmons Stone House (1847–49) and the Boght church site and settlement markers, as one place. Loudonville: Bryan's Store with the Loudon Road Historic District, and the D. D. T. Moore Farmhouse. Latham: the Goodrich School. Menands: Hedge Lawn (1870), Menands Manor (the 1877 Home for Aged Men), the Louis Menand House with the Menand Park bungalow district, and the Sage Estate Trails on the Fern Brook estate (village land, dawn to dusk, with a parking point). Sources were Wikipedia read raw with `wiki_raw.py`, historypointer.com copies of the Register entries for street addresses, the Colonie multiple resource nomination text (NPGallery 64000545), HMdb marker pages, and the Village of Menands' three Sage Estate Trails pages and trail map (read through the web fetch tool; `page.py` got 403). Not checked: present use and owner of Bryan's Store, the Goodrich School, Hedge Lawn and Menands Manor; whether the Sage mansion stands; any interior; any ruin on the Sage trails (the village names none). Brick from Wikipedia photographs for three (Goodrich red brick; Bryan's Store and the Moore house frame); the other five are `?`. All pins are address points that land on a building on the leaf-off aerial except the Sage trails (middle of the trail map) and the Goodrich School (`area`, the Wikipedia point on a building by the school lot). Nothing was seen on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Godfrey Farmhouse (update to the conf_edvk and conf_fmbb rows) | Cohoes, NY, 1313 Loudon Road (historypointer); geocoder 42.80848, -73.73321 (interpolated) | Register 79003240: Greek Revival temple-form farmhouse of about 1836 | The geocoded address lands on Route 9 beside a large earthworks site and no house of that form shows on the leaf-off aerial; probably gone, a source saying so |
| Henry M. Sage mansion (Fern Brook) | Menands, NY (1 Sage Rd., Register 80004398; Wikipedia 42.69389, -73.73389) | Wikipedia: limestone Georgian Revival mansion of the 1890s, remodelled 1920, sold to Albany International in 1973; now among the private Sage Estates houses | Whether it stands and what it is now |
| Whitney Mansion, Springwood Manor, Gorham House | Loudonville, NY (Register 79003242, 79003243, 79003239) | Wikipedia: about 1840 house given Georgian Revival wings; 1890 mansard house remodelled 1912; 1926 house built partly of the 1806 Hegeman house from Vischer Ferry | Private houses; worth a pin only with a picture or more story |
| Urger (canal tugboat) | was at Waterford, NY | Wikipedia: retired to drydock at Waterford in 2018, towed to the Canal Corporation shops at Lysander in September 2021 | Where it is now; it is no longer at Waterford |

## Tips
- The village of Menands' pages (menandsny.gov) answer 403 to `page.py` but read with the web fetch tool; the Sage trail map is a plain JPEG (`/wp-content/uploads/2020/11/trail-map-main.jpg`) with entrances and the parking lot marked.
- historypointer.com gives the Register street address for every Colonie multiple resource house that the Wikipedia list shows as "address restricted"; they are ordinary addresses, not restricted sites.
- The OpenStreetMap "Sage Estate Preserve Main Entrance Lot" point falls on the road; the entrance stub is about 70 m west.
- museumships.us and newyorkalmanack.com answer 403 to `page.py`.
