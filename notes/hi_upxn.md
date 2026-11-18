# hi_upxn: Kona and Kohala, Hawaiʻi Island
state: Hawaii
region: hi
date: 2026-11-18
places: 17
file: data_hi_upxn.py

## What this batch is
The first batch on Hawaiʻi Island (the Big Island), in the West Hawaiʻi districts of Kohala, Waimea and Kona (region `hi` drawn by `choose.py`). Seventeen places, ruins and standing buildings together: the heiau Puʻukoholā (with Mailekini), Moʻokini (with the Kamehameha I birthplace), Ahuʻena at Kamakahonu and Hikiau at Kealakekua Bay; the Lapakahi fishing village; Puʻuhonua o Hōnaunau; Kaloko fishpond and the Honokōhau settlement; the Kāneaka (Keauhou) hōlua slide; the mission churches Mokuʻaikaua, Kalahikiola, ʻImiola, Kahikolu and Hale Hālāwai O Hōlualoa; St. Benedict's Painted Church; Huliheʻe Palace; the Kohala District Courthouse; and the Kona Coffee Living History Farm. Facts come from Wikipedia (`wiki_raw.py`, the full text in `research/wikiraw/`), the Hawaii State Parks pages for Lapakahi, Kohala Historical Sites and Kealakekua Bay (`page.py --all`), the NPS hours and fee pages for Puʻukoholā, Puʻuhonua o Hōnaunau and Kaloko-Honokōhau, the Daughters of Hawaii (Huliheʻe Palace hours, fees and parking), the Kona Historical Society (coffee farm hours, fees, address) and the Mokuʻaikaua congregation's home page. Pins from OpenStreetMap (`nom.py`) or the ArcGIS geocoder, all looked at on the aerial and LiDAR sheets; Kaloko was moved onto its seawall and Hale Hālāwai onto Aliʻi Drive with `pix.py`. Not checked: anything on the ground; visiting hours for every church (Kalahikiola, ʻImiola, Kahikolu, Hale Hālāwai, St. Benedict's, and Mokuʻaikaua's tours); what the Kohala courthouse is used for now and which building on the aerial it is; who owns the land around the hōlua slide; where Moʻokini's visitors park. Pins that are not on the thing itself: `lapakahi-village` (the park's entrance lot), `hale-halawai-holualoa` (Aliʻi Drive in front of the church grounds), `kahikolu-church` (Wikipedia's point, beside a building that may be the church), `kohala-district-courthouse` (the Kamehameha statue in front). Red brick: none seen or described; the coffee farm and St. Benedict's are `?` (wood is likely but no source said).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Bond homestead and Kohala Girls' Seminary | Kapaʻau, HI (Bond District, about 20.2258, -155.7925) | Wikipedia "Bond District": missionary house of 1841 with stone additions of the 1840s–50s, seminary building of 1874; family-owned retreat | Whether anyone may visit, and who owns it now |
| Greenwell Store | Kealakekua, HI (19.515278, -155.923333, Register list) | 1870 store, Kona Historical Society museum (Register list summary) | Current hours: the society says it needs $200,000 by December 31, 2026 to stay open; no Wikipedia article |
| Tong Wo Society Building | Halaula, HI (20.2278, -155.7694, Register list) | Chinese society hall on the National Register (1978) | No article under that title; a source and an owner |
| Hilo downtown (Lyman House, Palace Theater, Hata Building, Federal Building, Haili Church) | Hilo, HI | All on the Register list with points | East Hawaiʻi was not worked in this batch |
| Whitney Seismograph Vault No. 29, Old Volcano House No. 42 | Hawaiʻi Volcanoes National Park | Register list: 1912 first home of the volcano observatory; 1877 Volcano House, now the Volcano Art Center | NPS pages for access |
| Star of the Sea Painted Church | Kaimu, HI (19.3761, -154.9669, Register list) | Painted by Father Evarist Gielen, a pupil of Velghe (Wikipedia, St. Benedict's article) | Its own article and access |

## Tips
- The Painted Church's old web address (`thepaintedchurch.org`) now holds an unrelated Spanish-language blog; do not take hours from it.
- `imiolachurch.com` did not answer, and `page.py` could not fetch its archived copy.
- The Kona Historical Society said in November 2026 it must raise $200,000 by December 31, 2026 to stay open; check its places' hours again in 2027.
- `nom.py` found most heiau and churches in Kona by name; Huliheʻe Palace, Kahikolu Church and the Kohala courthouse it did not, and the ArcGIS geocoder's POI for "Kohala District Courthouse" was the South Kohala court in Waimea. The Kamehameha statue in Kapaʻau (`nom.py "Kamehameha statue, Kapaau"`) marks the old courthouse.
- The Hawaii State Parks pages' closure notices at the bottom are the same on every page and name other parks (the Kealakekua page carried Lapakahi's reopening date); read them for the whole island, not only the page's park.
- `publish.sh` stopped once because another batch merged while the pin check ran; `resync.sh` and a fresh batch time fixed it in one go.
