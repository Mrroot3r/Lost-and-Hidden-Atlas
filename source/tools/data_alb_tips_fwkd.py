# November 19, 2026: two places in Albany that readers sent in through the Atlas's form on November 18, 2026 (the first
# places to carry tip=, which the app shows as "Sent in by a reader"). The owner of the Atlas sent both himself, from a
# walk, and said so in the maintainer chat, so what he saw on the ground is taken as a field report (GUIDE.md sections 6
# and 15). Everything else is from sources opened in this session: Historic Albany Foundation's "Places in Peril" page for
# 759 Madison Avenue (read whole with tools/page.py --all), and Wikipedia's article on the Washington Park Historic
# District as raw text (tools/wiki_raw.py) for the Taylor grounds. Not checked: who owns 759 Madison Avenue now, what
# state it is in beyond the reader's report, any city demolition record, and what the brick walk in the park is.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'alb_tips_fwkd','label':'Albany: two places readers sent in','added':'2026-11-19 06:01'}
HAF=L('Historic Albany Foundation: Places in Peril (759 Madison Avenue)','https://www.historic-albany.org/places-in-peril-2024')
PLACES=[
N('759-madison-avenue-albany','759 Madison Avenue: Queen Anne mansion, empty since the 1980s','Albany','alb','landmark','standing',42.65911,-73.77867,'exact','view','drive','now','1889',
  'A freestanding Queen Anne mansion of 1889 in Pine Hills, its design attributed to the architect Albert Fuller. Historic Albany Foundation, which lists it among its "Places in Peril", says it was last occupied in the 1980s, is also known as 755 Madison Avenue, and in 2024 was being renovated by its owner. A reader who walks past it often reported on November 18, 2026 that only a shell is left and that it may be demolished.',
  'From the Madison Avenue sidewalk: a detached house standing back from the street between its neighbours on the north side, west of Ontario Street. Look for what is left of the Queen Anne detail the foundation praises. The reader\'s report of a shell has not been checked against a photograph or a city record. Interior not checked.',
  'An 1889 mansion, forty years empty, that a passer-by says is down to a shell.',
  'Private property (the foundation speaks of "the current owner" and does not name one). See it from the public sidewalk only; do not go onto the lot. Park on the street where the signs allow.',
  [HAF],conf='mixed',brick='?',tip='2026-11-18'),
N('washington-park-buried-brick-walk','Buried brick walk, Washington Park','Albany','alb','inst','traces',42.65814,-73.77545,'exact','public','walk','','',
  'A reader walking in Washington Park on November 18, 2026 found a brick walkway, mostly buried, on the wooded rise just north of the tennis courts at the west end of the lake. Nothing in print about it has been found yet. The ground it lies in was the house and landscaped grounds of John Taylor, the last part of the park to be bought, in 1882; tennis courts have stood on that ground since 1889. Whether the brick belongs to the Taylor grounds or to an early park path is not known.',
  'Brick showing through soil and leaves near where a paved path from the Madison Avenue side ends in a strip of trees, north of the tennis courts. Easiest to find when the leaves are down. Leave it as it lies.',
  'A brick path nobody has written down, under the leaves beside the tennis courts.',
  'A public city park (the city maintains the courts beside it, Wikipedia says). Walk in from Madison Avenue past the tennis courts. Park hours were not checked. Park on the street where the signs allow.',
  [W('Washington Park Historic District (Albany, New York)')],conf='lead',brick='?',tip='2026-11-18'),
]
PIN_NOTES={
 '759-madison-avenue-albany':'OpenStreetMap\'s address point for 759 Madison Avenue is 42.65906, -73.77861; moved 7 m onto the roof of the house on the leaf-off aerial (tools/pix.py). The reader\'s own point, 42.65901, -73.77886, is 20 m west, by the next house.',
 'washington-park-buried-brick-walk':'The reader\'s own position, from a field-log note (phone GPS): 42.65814, -73.77545. On the leaf-off aerial that is where a paved path ends in a strip of trees north of the tennis courts; no brick can be seen from the air.',
}
