# cny_yokj: New York: Seneca Falls, Waterloo and Seneca County
state: New York
region: cny
date: 2026-11-22
places: 18
file: data_cny_yokj.py

## What this batch is
Eighteen places in Seneca County, New York, the first pass there (region `cny`, drawn at random by `choose.py --state ny`, which offered Seneca Falls, Phelps and Webster; the county had only the Sampson Military Museum). Seneca Falls: the Wesleyan Chapel, the Elizabeth Cady Stanton House, the Seneca Knitting Mill (National Women's Hall of Fame), the Fall Street district, the Fourth Ward School, the Barge Canal locks 2 and 3, and the Flats, the industrial district drowned under Van Cleef Lake in 1915 (nothing to see but the lake and a panel). Waterloo: the M'Clintock and Hunt houses, the National Memorial Day Museum (Burton House), First Presbyterian and St. Paul's, and the Scythe Tree on US 20. Fayette: Rose Hill Mansion. Romulus and Varick: the Seneca Army Depot igloos, seen only on Deer Haven Park's tours (the lead row in `notes/wny_vtcb.md` was deleted). Ovid and Willard: the Three Bears courthouse group and the closed Willard asylum campus (state property, view only). Lodi: the 1880 Methodist church. Sources: Wikipedia via `wiki_raw.py` (the county Register list with `--rows`), HMdb nearby lists and marker pages via `page.py`, nps.gov/wori (FAQ, things-to-do and Hunt House pages; the hours page is drawn by script and empty), womenofthehall.org, deerhavenpark.org, senecacountyida.org and a FingerLakes1.com report of November 15, 2026 for Willard. Not checked: tour times of the park houses (only the visitor center's daily 9 to 5), Rose Hill and the Memorial Day Museum hours (`hours='?'`), the churches' service times, whether the Three Bears or Lodi church are in use, parking at Hunt House and Rose Hill, who owns the ground under the Scythe Tree. Wikipedia and NPS disagree on the day of the Hunt House tea (July 13 or 9, 1848); both are given. Pins were looked at on the aerial; the Memorial Day Museum, Rose Hill and Lodi church were moved onto the buildings, the Willard pin is in the campus grounds (`area`), Deer Haven's is its visitor center. Red brick from Wikimedia pictures for First Presbyterian, the Three Bears and Lodi; the Fourth Ward School looked painted red and was left `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Seneca Falls Historical Society (Mynderse-Partridge-Becker House) | Seneca Falls, NY | Museum in a Victorian house | sfhistoricalsociety.org answers 403 to `page.py`; date, hours |
| Seneca Museum of Waterways and Industry | Fall Street, Seneca Falls, NY | Canal and industry museum | senecamuseum.com answers 403; building and hours |
| Trinity Episcopal Church, Seneca Falls | Trinity Lane on Van Cleef Lake (Commons pictures near 42.9106, -76.7942) | Stone church on the lake shore | No Wikipedia article; a source for its date and services |
| Waterloo Woolen Mill bull wheel | 15 Church Street, Waterloo (HMdb 283940, 42.90583, -76.86044) | Mill's bull wheel set out with a marker | What else of the mill stands |
| Cobblestone farmhouses of Junius and Tyre | Stone Church Road and Birdsey Road, Junius; Hiram Lay house, Tyre (Register list) | Five listed cobblestone houses | All private; whether worth a view-only entry |
| Covert Historic District and First Baptist Church of Interlaken | Covert and Interlaken, NY (Register list) | Listed district and church | No article read; a source for what stands |

## Tips
- nps.gov/wori/planyourvisit/hours.htm is drawn by script and reads empty; the park FAQ (nps.gov/wori/faqs.htm) has the visitor center hours, and the house tour schedule was not found in any page that reads.
- historicgeneva.org (Rose Hill), sfhistoricalsociety.org, senecamuseum.com and waterloony.com answer 403 to `page.py`; waterloohistory.org would not connect.
- The Sampson Military Museum is already on the map under `wny` (data_wny_vtcb.py); `start.py "Seneca Falls"` at 20 km does not reach it, so run `nearby.py` on the county centre too.
- `photo_find.py` offered nothing for the Scythe Tree or the depot igloos; both need a photograph from someone who goes.
