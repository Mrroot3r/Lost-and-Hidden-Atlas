# Lost & Hidden Atlas

A map tool for finding abandoned sites and ruins across upstate New York and Massachusetts.

**Open it:** https://mrroot3r.github.io/Lost-and-Hidden-Atlas/

## What is in this repository

| Path | What it is |
|---|---|
| `index.html` | The page, with the place list built in |
| `app.js`, `leaflet.js` | The app and the map library |
| `sw.js` | Keeps the Atlas on the phone so it opens with no signal |
| `data/lines.json` | Old railroads, trolley lines and canals, loaded after the page opens |
| `data/leads.json` | Unchecked leads from OpenStreetMap, loaded when the Leads layer is switched on |
| `topo/` | One old USGS survey map per place, loaded when that place is opened |
| `source/` | The files the site is built from |

Notes, progress, field logs and added places are saved in the visitor's own browser. Nothing is uploaded here.

## Data credits

Imagery: New York State ITS Geospatial Services, MassGIS, Vermont Center for Geographic Information, USGS, Esri.
Lines and leads: OpenStreetMap contributors, OpenHistoricalMap, MassGIS, U.S. DOT.
Public land: USGS PAD-US. Parcels: NYS tax parcel file, NYS DEC, MassGIS.
