# springfield_esac: Ohio: old Springfield, the Champion City
state: Ohio
region: oh
date: 2026-11-26
places: 9
file: data_springfield_esac.py

## What this batch is
Nine standing places in Springfield, Ohio (Clark County), where the Atlas had nothing within 15 km, taken from the names in one Old World Exploration video about the city (the record of every name is `source/videos/20240320_HZot3PrV83M.md`; the video is a tip and nothing rests on it). Downtown: the Clark County Courthouse (rebuilt 1918 to 1924 inside the walls of the second courthouse), the 1890 City Hall and Market (now the Clark County Heritage Center, a free museum), St. Raphael's and St. John's Lutheran churches, the Bushnell Building and the Warder Public Library; on East High Street the Bushnell House (a funeral home); north of downtown the 1898 Odd Fellows' Home and Wittenberg's Recitation Hall. Facts are from Wikipedia (read with `wiki_raw.py`), the Clark County Historical Society's own pages, SAH Archipedia, the Westcott House audio-tour page, Wittenberg University's pages and, for the Odd Fellows' Home's later demolitions and present use, the herr2ck architecture blog (marked conf='mixed'). Hours: the Heritage Center from its own plan-your-visit page; St. Raphael's from the St. Rose Family of Parishes bulletin of October 18, 2026. Not checked: St. John's service times (no page of its own was found), the Warder library's (literacy centre's) hours, who runs the Odd Fellows' Home now, visitor parking at Wittenberg, and red brick for five places. Pins are ArcGIS address points, each looked at on the aerial; the Wikipedia point for the courthouse is about 400 m east of it. The narrator said the library was gone; Wikipedia and the Register list show it standing, so it was added.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Ohio Masonic Home, first building (Bushnell Hall) | Springfield, OH, West National Road | Grand Lodge pages: first residents 1895; the cornerstone year is given as 1882 on freemason.com and 1892 elsewhere | A page that says which early buildings stand and whether visitors may look; Springfield News-Sun articles answered 429 |
| Knights of Pythias Orphans Home | Springfield, OH, West McCreight Avenue | Greater Hilltop historical society page: opened 1895, closed 1944, mostly demolished, some buildings reused as Mercycrest | Which building stands, and its owner |
| Old downtown post office | Springfield, OH | The Clark County Historical Society names Charles A. Cregar as its architect | Whether it stands, and where |
| Crowell Publishing works (Farm and Fireside) | Springfield, OH | Wikipedia: the company closed its Springfield plant | Whether any building stands |

## Tips
- `videos.py check` reads the place id after "added" with a trailing colon as part of the id: write "added <id> (remark)", not "added <id>: remark".
- The St. Rose Family of Parishes bulletins (irp.cdn-website.com PDFs) give Mass times for all the Springfield Catholic churches; `page.py` on them prints pages of fontTools warnings to stderr, so add `2>/dev/null`.
- herr2ck.blogspot.com has detailed 2025 posts on most of downtown Springfield's old buildings, with present use; good for a follow-up batch (Lagonda Club, Shawnee Hotel, Masonic Temple, Third Presbyterian, Westcott House).
- Springfield News-Sun pages answer 429 to `page.py`.
