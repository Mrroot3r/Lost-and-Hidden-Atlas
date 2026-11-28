# hi_kbvq: Hilo, Honokaʻa and Kona
state: Hawaii
region: hi
date: 2026-11-28
places: 8
file: data_hi_kbvq.py

## What this batch is
Eight standing buildings on Hawaiʻi Island, chosen from the National Register listings the Atlas lacked (`tools/gaps.py hi "Hawaii"`): the Greenwell Store (Kealakekua), Daifukuji Soto Mission (Honalo), the Honokaʻa People's Theatre and the Hotel Honokaʻa Club, in Hilo the Federal Building, the Masonic Temple (Bishop Trust Building), the Naha Stone and Kamehameha Hall at Keaukaha. Facts come from the Park Service records and forms (`tools/form.py`), Wikipedia (`wiki_raw.py`) and the temple's and Kona Historical Society's pages (`page.py`). Not checked: interiors, who owns what today, and hours for the store, the theatre and Kamehameha Hall (none found; entries say so). The Kona Historical Society says it must raise $200,000 by December 31, 2026 to stay open, so the Greenwell Store's opening is uncertain. A cloud covers the Greenwell Store on the aerial. Pictures: three found on Commons (theatre, hotel, Masonic Temple); none fit the Federal Building and none exist for Kamehameha Hall. Old Volcano House was dropped because the Atlas already has it as `old-volcano-house-42`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Tong Wo Society Building | Halaula, North Kohala (Register point 20.2278, -155.7694) | Register 78001011: 1886 Chinese society house, two-storey, best preserved on the island; only the main building of six is left | The Register and Wikipedia points are in empty pasture on the aerial; no street address found. The form's tax parcel is 5-3-08:20. Needs a point on the building |
| W. H. Shipman House | Reed's Island, Hilo | Register 78001013: 1899 house, architect Henry Livingston Kerr (Wikipedia), guest cottage of 1910 still takes guests (shipmanhouse.com) | Both the Register point (19.72557, -155.09446) and Wikipedia's (19.7242, -155.0994) fall in water or an orchard on the aerial; needs an address point. Private |
| James M. Hind House | Hawi, North Kohala | Register 93001557: 1900 prefabricated house of a sugar manager | The Register point (20.113, -155.578) is nowhere near Hawi; the form gives only "Skilled Camp, House J"; private |
| Waimea Elementary School Building N | Kamuela | Register 05000541: 1915 school building moved to the Hawaii Preparatory Academy lower school, now an art centre | Only the headings of the form were read; a school campus |
| Honokaʻa's other Register stores (Ferreira, Botelho, Teiji Yamatsuka and about ten more on Māmane Street) | Honokaʻa | Register listings of 2015 to 2023; commons has pictures of several | Not read; the town could be written up as one entry |
| Hilo downtown: District Courthouse, S. Hata Building, Volcano Block | Hilo | LEADS.md rows (the Federal Building row is now done here) | Forms not read |

## Tips
- `tools/form.py` for listing 74000708 (Hilo Federal Building) returned a form headed "Honolulu"; its description is the Hilo building's (Whitfield, 1915-17), but check names before trusting a header.
- Register points are the least reliable thing in Hawaii: Daifukuji's was 6 km out, Shipman's and Tong Wo's missed the building, Hind's is in the wrong district. `nom.py "<name>, <town>, Hawaii"` found the temple and the Federal Building; Wikipedia's Register list rows (`wiki_raw.py --rows`) gave the right town spelling (Halaula, not Halawa).
- `tools/app_smoke.js` is for the Android app only; for a place-list batch run `tools/smoke.js` against `dist/` (the guide's wording sends you to the first).
