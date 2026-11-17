# November 17, 2026: the Quabbin and North Quabbin country of central Massachusetts (region cmass), a second batch.
# Pull request 53 (data_quabbin.py) was opened by another session on the same ground while this one worked; this
# batch keeps only the three places that pull request does not have: the F-94 jet that lay undiscovered in the
# Quabbin woods near Dana, John Smith's Hermit's Castle in Erving State Forest, and the burned mill on the Ware River
# at Wheelwright. This session's own entries for the other nine places it shares with pull request 53 were set aside.
# Facts come from the linked sources only. The Erving State Forest draft resource management plan, the Erving State
# Forest and Quabbin pages and the state's 2021 dam-removal certificate were read through the web fetch tool or
# tools/page.py (mass.gov answers scripts with 403); the DVIDS article through the web fetch tool; the Athol Daily News,
# New England Trail, New England Aviation History and Mass Central Rail Trail pages through tools/page.py; Wikipedia's
# list of dam removals from a search result. Where sources disagree the text gives both; where a source is silent it
# says "not checked".
# Pins: an OpenStreetMap feature (tools/nom.py, tools/osmnear.py) or a spot read off the aerial with tools/look.py and
# tools/pix.py, as each pin note says. Every pin was looked at with tools/pincheck.py --lidar
# (research/pincheck_quabbin2_*.jpg), and ownership checked with tools/parcel.py.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'quabbin2','label':'North Quabbin extras: a lost jet, a hermit\'s cave and a burned mill','added':'2026-11-17 19:00'}
DCR_Q=L('DCR: Quabbin Reservoir (hours, parking, dogs)','https://www.mass.gov/locations/quabbin-reservoir')
ERV_RMP=L('DCR: Erving State Forest draft resource management plan (PDF)','https://www.mass.gov/doc/erving-state-forest-draft-rmp/download')
ERV_DCR=L('DCR: Erving State Forest (hours, dogs)','https://www.mass.gov/locations/erving-state-forest')
MCRT=L('Mass Central Rail Trail: Hardwick','https://www.masscentralrailtrail.org/hardwick')
PLACES=[
N('f94-crash-quabbin','F-94 Starfire crash site','Petersham','cmass','landmark','ruins',42.41144,-72.24006,'site','public','hike','','1955',
  'On April 3, 1955, Lt. Dewey Durrett of the Massachusetts Air National Guard was flying an F-94A Starfire jet back to Westfield in a snowstorm when he lost radar contact and ran low on fuel. Told to bail out, he came down safely in woods on Quabbin land and walked out; he assumed the jet had gone through the reservoir ice. Searches found nothing, and the wreck was found in the woods of Petersham nearly four years later.',
  'Pieces of the wreck still lie in the woods: New England Aviation History (2016) says the crash site can still be seen, and a 2025 Air National Guard article that it is still visible. Not checked on the ground.',
  'A jet the Air Force thought was under the ice, found four years later in the woods.',
  'DCR Quabbin Reservation (the state tax-parcel file shows the ground at the pin as state land), reached on foot from Gate 40 on Route 32A in Petersham by the old road past Dana Common; the Air National Guard article puts the round trip at about 7 miles. Federal and state law forbid removing any part of the wreckage. Open from one hour before sunrise to one hour after sunset. No dogs anywhere on Quabbin land.',
  [L('New England Aviation History: Quabbin Reservoir land, April 3, 1955','https://newenglandaviationhistory.com/tag/f-94a-49-2552/'),
   L('DVIDS: 104th Fighter Wing, forgotten history restored (March 2025)','https://dvidshub.net/news/494154/104th-fighter-wing-forgotten-history-restored'),DCR_Q],
  th=[42.44214,-72.20901],thn='Quabbin Gate 40'),
N('hermits-castle-erving','Hermit\'s Castle','Erving','cmass','landmark','ruins',42.61281,-72.42378,'site','public','hike','','1867–1899/1900',
  'John Smith, born in Perth, Scotland in 1823, came to Boston in 1866 and found a cave under the cliffs of Hermit Mountain while picking chestnuts that autumn; he moved in the next spring. DCR says he enlarged the natural cave. Once discovered he became a local attraction: the landowner let him stay, visitors brought food, and he grew vegetables, knitted socks to sell and sang for callers. A book about him, written for him by George W. Barber, came out in 1868. When he left is not agreed: the New England Trail gives 1899, a Northfield Mountain walk notice 1900.',
  'DCR lists a cellar hole, the cave and stone retaining walls just north of the cellar hole. DCR also says its interpretive panel is gone and its post is in disrepair. Not checked on the ground.',
  'A Scottish hermit\'s cave home that drew crowds of visitors.',
  'Erving State Forest (DCR), Hermit Mountain tract, open sunrise to sunset; dogs allowed. DCR owns no parking for it: the usual start is an informal lot on a FirstLight Power access road off Mountain Road, with no DCR sign, and the New England Trail (white blazes) leads to it, a loop of about 4.5 miles. DCR says a short stretch of the Hermit Mountain loop crosses private land: stay on the trail. Climbing bolts at the site were put in without permission. Steep.',
  [ERV_RMP,ERV_DCR,L('Athol Daily News: The Hermit of Erving Castle (2020)','https://atholdailynews.com/2020/03/23/recalling-the-hermit-of-erving-castle-33469026/'),
   L('New England Trail: Erving Ledges and Hermit Mountain','https://newenglandtrail.org/hike/erving-ledges-hermit-mountain'),
   L('Franklin County Chamber: Hike to Hermit Cave (Northfield Mountain walk)','https://chamber.franklincc.org/events/details/hike-to-hermit-cave-23890')],conf='mixed'),
N('wheelwright-mill-ruins','Wheelwright mill ruins','Hardwick','cmass','industry','ruins',42.35224,-72.13781,'site','view','drive','burned','to 2001',
  'Wheelwright, a village of Hardwick on the Ware River, has the site of a former mill beside the river. The rail trail page says it was a paper mill that later made tissue, and that many of its buildings burned in 2001. A timber dam built in the early 1900s fed the mill; the state\'s 2021 environmental certificate calls the mill complex abandoned and the dam privately owned. The dam was taken out in 2025 and 2026 to free the river.',
  'The rail trail page says brick ruins are still visible; the aerial shows rubble and open ground between the village and the river. What stands now, and what the dam removal changed, was not checked.',
  '',
  'PRIVATE LAND (the state tax-parcel file and the 2021 dam certificate both show the mill site privately owned): look from Maple Street or the Mass Central Rail Trail; do not enter the mill site. The rail trail page lists on-street parking on Maple Street.',
  [MCRT,L('MEPA certificate, Wheelwright Pond Dam removal (July 2021, PDF)','https://eeaonline.eea.state.ma.us/EEA/emepa/mepacerts/2021/sc/enf/16398%20EENF%20Wheelwright%20Pond%20Dam%20Removal%20Project%20HARDWICK%20NEW%20BRAINTREE.pdf'),
   W('List of dam removals in Massachusetts')],conf='mixed'),
]
OSM='OpenStreetMap feature (tools/nom.py / osmnear.py)'
PIN_NOTES={
 'f94-crash-quabbin':OSM+': "F-94 Starfire Crash Site" (tourism=attraction), beside the mapped Starfire Trail. Leaf-off aerial: unbroken conifers. LiDAR: old field walls and a faint dimple at the pin, nothing certain.',
 'hermits-castle-erving':OSM+': "Hermit\'s Castle" (tourism=attraction) at the end of the Hermits Castle Trail. LiDAR: a deep hollow under the ledges about 20 m north-west of the pin and a trail just south; the aerial shows only bare woods below the cliffs.',
 'wheelwright-mill-ruins':'Spot read off the aerial (tools/look.py + pix.py): the rubble field between Mill Street and the Ware River, beside the dam on the spring 2023 aerial; the LiDAR shows broken foundations there. The dam has since been removed.',
}
