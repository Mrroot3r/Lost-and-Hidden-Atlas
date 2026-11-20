# conf_edvk: Green Island, Cohoes markers and two Waterford churches
state: New York
region: conf
date: 2026-11-19
places: 10
file: data_conf_edvk.py

## What this batch is
Ten places in region `conf` (drawn at random by `choose.py --state ny`), the fourth pass there, aimed at Green Island and the corners of Cohoes and Waterford the earlier batches left. Green Island: St. Mark's Episcopal Church, settled as the town offices by a Times Union article (hours from the town's page; Wikipedia gives 1866–67 and the 2024 village marker 1886, both given; red brick 'some' from a 2010 Commons photograph), and the D&H Green Island branch's "black bridge", now on the Empire State Trail (Spindle City's "Forgotten Railroads of Cohoes" and two HMdb panels; parking point at the end of Cannon Street). Cohoes: the Troy & Schenectady's High Street station platform (HMdb), the William Moore House (Spindle City tour only, red brick), the Beattie Machine Works (Governor's 2022 nominations release and Go Historic's address; present use not checked), the Van Schaick burial plot with the Camp Van Schaick marker (HMdb; whether gravestones show not checked, so `view`), and the Cataract House site at Falls View Park (HMdb; park hours from Discover Albany, not the city). Watervliet: the Gibbonsville basin, dry dock and 14th Street bridge markers on Second Avenue. Waterford: St. Mary of the Assumption (The Evangelist, GCatholic; Mass times only from a directory, so `hours='?'`) and Grace Episcopal Church (diocese page against the museum's 2009 walking tour: 1841 or 1867, both given), which the village-district pin mentions but had no pin of their own. All pins were looked at on the leaf-off aerial (with the LiDAR sheet); both church pins were moved from the address point onto OpenStreetMap's church buildings. Nothing was seen on the ground. Three entries rest on one source each (William Moore House, High Street station, Beattie).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Godfrey Farmhouse | Cohoes, NY (Wikipedia 42.80778, -73.73472) | Wikipedia: Greek Revival temple-form farmhouse of about 1836 with a fluted-column portico, National Register 1979 | Whether it still stands: the point is among new housing beside Route 9/Columbia Street and no house of that form was seen on the aerial |
| Corporation Hall | Green Island, NY (George and Clinton Streets, 42.74202, -73.69243) | HMdb "Welcome to Green Island" and "Unique Urban Village" panels: the island's first public building, 1883 | Which corner building it is, and a second source |
| Rensselaer and Saratoga Railroad Green Island Shops (update to the LEADS.md row) | Green Island, NY (42.75056, -73.69278) | The leaf-off aerial shows cleared ground and fill at the Register point, no roundhouse or water tower | Probably nothing left; a source saying so |

## Tips
- Green Island's town page (villageofgreenisland.com/town/) gives office hours; the Times Union's "Sacred buildings' afterlives" (2013) is the source that St. Mark's is the town offices, which settles the earlier lead.
- The HMdb nearby list round Green Island and west Cohoes (2-mile radius) listed about 130 markers; the Watervliet Historical Society's small canal markers on Second Avenue (2024) are new there.
- The Mohawk-Hudson trail and the Empire State Trail at Green Island and Cohoes are not on the federal public-land map, so `pincheck.py` prints CHECK ACCESS for every trail place there.
- The NARA copies of older New York Register forms (s3.amazonaws.com/NARAprodstorage/...) answer 403 to `page.py`.
