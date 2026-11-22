# chattanooga_vkqr: Chattanooga: domes, churches and Lookout Mountain
state: Georgia, Tennessee
region: ga, tn
date: 2026-11-22
places: 16
file: data_chattanooga_vkqr.py

## What this batch is
Sixteen places in and around Chattanooga, Tennessee, taken from the buildings named in one video of old architecture (Old World Exploration, "Old World Chattanooga"; the record of every name and its outcome is source/videos/20261016_2s5yh0Xm9ls.md). The video was used only as a list of names. Added downtown: the Dome Building (old Chattanooga Times), the Hamilton County Courthouse, the Fireman's Memorial Fountain, the Carnegie library, the Basilica of Saints Peter and Paul, the lone First Methodist Church tower in Phillips Park, Second Presbyterian, the Municipal Building, the 1893 Old Post Office, the Maclellan Building, the Read House and Terminal Station (Chattanooga Choo-Choo). On Lookout Mountain: the Incline Railway, Ruby Falls and Cavern Castle, and the Point Park entrance gate; and the Wilder Brigade Monument on the Chickamauga battlefield in Georgia. Sources: National Register forms read as NPGallery text layers, the 2020 Downtown Chattanooga Historic District form on tn.gov, Wikipedia through wiki_raw.py, HMdb markers, National Park Service pages, the Incline's and Ruby Falls' own pages, Second Presbyterian's own page and a 2025 WUTC report on the fountain. Not checked: the present use of the Dome Building, the Old Library and the Old Post Office (the forms are from the 1970s); Mass times at the basilica (the parish site, an ecatholic.com site, answered 403); opening hours of the Read House and the Choo-Choo complex; whether the courthouse may be walked into; red brick for Second Presbyterian, the Municipal Building, the Read House and the Incline stations. The Incline's own page contradicts itself on Mondays (closed Mondays, and open Monday to Sunday); the entry gives both. The Incline pin is on the building taken for the lower station on the aerial (prec site). Every pin was looked at on the aerial; the fountain was moved onto the basin seen there.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| News-Pound Building | Chattanooga, TN | On the Register list (80003819), with no coordinates; possibly the "News building" of the video | The Register form had no text layer; a source for what and where it is |
| Park Hotel (Newell Towers) | Chattanooga, TN | The 2020 downtown district form describes a nine-storey brick hotel of 1915, altered 1981, counted as not contributing; separately on the Register (80003821) | Its own Register form had no text layer; whether it is the 1880s Park Hotel the video showed |
| First Baptist Church education building | 317 Oak Street, Chattanooga, TN | The Fountain Square form says part of the 1888 First Baptist church complex survives as the education wing; separately listed (80003811) | Its own form, and what of the 1888 work is in it |
| Lookout Mountain Hotel | Lookout Mountain, GA | Named in the video | A source saying what stands |

## Tips
- NPGallery text forms for Hamilton County read well; Park Hotel (80003821) and News-Pound Building (80003819) return a picture, not text.
- The 2020 Downtown Chattanooga Historic District form (tn.gov PDF, 75 pages) reads with page.py --all -n 900000 and covers most downtown blocks.
- wiki_raw.py answered NO SUCH ARTICLE for several titles the Register list row names as the article (Ochs Building, Municipal Building, Fountain Square, Park Hotel, Read House, Old Post Office); "The Read House Hotel" and "Basilica of Sts. Peter and Paul (Chattanooga)" worked.
- photo_find.py look on seven places took about fifteen minutes and outran a ten-minute command limit: run it in the background from the start.
