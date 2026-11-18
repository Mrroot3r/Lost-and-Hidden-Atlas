# Red brick, first pass (November 17, 2026): read off each place's own Atlas text, where the text says brick.
# Nobody looked at a picture for these, and the text rarely gives the colour: brick is taken as red unless the text says
# otherwise (Cranston Street Armory is yellow brick and is left out; Barree's brick mansion is painted white and is left out).
# 'yes' = brick is the main thing to see; 'some' = part of it (a chimney, an arch, brick with stone).
_T='its own Atlas text says so; no picture was looked at'
BRICK={k:('yes',_T) for k in '''scott-ice-house empire-stove-works shultz-brickyard valley-paper-mill-chimney troy-gasholder mohasco-power-house
 buffalo-smelting-works mechanicville-hydro herkimer-home remington-ilion wyndcliffe harlem-valley laugh-o-gram-studio wornall-house
 baldwin-city-santa-fe-depot washburn-moen monson-developmental medfield-state-hospital fort-andrews cocheco-mills-dover
 salmon-falls-mill-rollinsford woonsocket-rubber-mill new-manchester-mill fort-pike susan-b-anthony-childhood-house crompton-loom-works
 whittall-mills worcester-corset ashworth-jones lancaster-mills heywood-wakefield'''.split()}
BRICK.update({k:('some',_T) for k in '''the-hill burden-wheel poestenkill-gorge hutton-brickyards beaver-kill kelloggs-dam-amsterdam
 kamananui-valley-road queensbury-mill-somersworth idols-dam-yadkin juniata-iron-works wheelwright-mill-ruins high-cliff-lime-kilns
 mariscal-mine eureka-historic-district-ut mammoth-historic-district-ut richardson-olmsted-campus browns-race cornish-estate-northgate
 wcsr-remains'''.split()})
