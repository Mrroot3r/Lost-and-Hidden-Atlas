# hi_rwke: Honolulu, Waipahu, Hilo, Waimea, Maui and Molokaʻi
state: Hawaii
region: hi
date: 2026-11-28
places: 12
file: data_hi_rwke.py

## What this batch is
Twelve standing places, mostly downtown Honolulu (Aloha Tower, Hawaii Theatre, Royal Brewery, Kamehameha V Post Office, Kakaʻako Pumping Station, Hānaiakamalama), plus Wakamiya Inari Shrine (Waipahu), the W. H. Shipman House (Hilo), Anna Ranch (Waimea), Waihee Church and ʻIao Theater (Maui) and Molokaʻi Light. Facts come from Wikipedia (tools/wiki_raw.py) and the National Register record; the National Register forms for the Hawaii listings are thin (Tong Wo's form is for a Honolulu building). Hours come from search results quoting the managers' pages (Daughters of Hawaiʻi, Hawaii Theatre, Anna Ranch via a travel guide) and were not read on the pages themselves; Aloha Tower, ʻIao Theater, Royal Brewery, Post Office, Wakamiya, Waihee, Shipman and Molokaʻi Light have no hours or access checked beyond what the entries say. Nothing was seen on the ground. Three Wikipedia or Register points fell in water, an orchard or on an airstrip and were moved by eye on the aerial (Kakaʻako, Shipman House, Molokaʻi Light); the Royal Brewery pin is on the corner building by eye and could be a few metres off.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Ainahou Ranch | Hawaiʻi Volcanoes NP (19.3436, -155.2289) | 1941 Shipman refuge ranch house, nēnē pens; Register listing 94001619 | Whether the public may visit; the Register form's description is blank |
| Bond District | Kapaau (20.2258, -155.7925) | Bond homestead, Kohala Seminary; Kalahikiola Church already on the map | Access and hours for the homestead |
| Wo Hing Society Hall | Lahaina (20.8764, -156.6804) | Destroyed in the August 2023 fire, per Wikipedia | Whether anything is left; a source on the site now |
| Chee Kung Tong, Ket Hing, Maui Jinsha Mission, Hana Wananalua Church | Maui | Register listings with no Wikipedia article | An opened source for each |
| Many Honolulu Register listings (fire stations, Kalakaua Ave houses, Battery Hasebrouck, Our Lady of Peace Cathedral) | Honolulu County | Listed in tools/gaps.py | Sources; 126 listings remain |

## Tips
- tools/gaps.py "nearest Atlas place" can be 0.3 to 1 km away for a place that is not on the map (Aloha Tower, Royal Brewery); check the name list, not the distance. Daifukuji and Holy Ghost Church were already on the map under other coordinates.
- Wikipedia coordinates in Honolulu harbour and Hilo were off by 100 m or more; look at the aerial before keeping them.
- tools/start.py --prs printed "Open pull requests: 0" with no gh available; the claim step still kept sessions apart.
