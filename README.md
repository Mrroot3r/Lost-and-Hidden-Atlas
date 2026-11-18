# Lost & Hidden Atlas

A map tool for finding abandoned sites and ruins across upstate New York and Massachusetts, with a first pass at Rhode Island.

**Open it:** https://mrroot3r.github.io/Lost-and-Hidden-Atlas/

**Android app:** the newest build is at https://github.com/mrroot3r/Lost-and-Hidden-Atlas/releases/latest (download `lost-hidden-atlas.apk` on the phone and open it). The app opens with no signal, fetches new places from the site by itself, and records a field log with the screen off.

## What is in this repository

| Path | What it is |
|---|---|
| `index.html` | The page, with the place list built in |
| `app.js`, `leaflet.js` | The app and the map library |
| `sw.js` | Keeps the Atlas on the phone so it opens with no signal |
| `data/lines.json` | Every old railroad, trolley line and canal in one file; the Android app reads it |
| `data/lines/` | The same lines cut up by state, fetched by the page as the map goes there |
| `data/leads.json` | Unchecked leads from OpenStreetMap, loaded when the Leads layer is switched on |
| `topo/` | One old USGS survey map per place, loaded when that place is opened |
| `source/` | The files the site is built from |
| `boot.js`, `version.json` | Read by the Android app only |
| `android-app/` | The Android app |
| `GUIDE.md` | How the Atlas works and how to add places to it. Start here if you want to help |

Notes, progress, field logs and added places are saved in the visitor's own browser. Nothing is uploaded here.

## Helping out

New places, corrected pins and field reports are welcome. **You do not need to know GitHub:** in the Atlas, "I was here" on a place page and "+ Add" each end in a "Send to the Atlas" button, and the [Suggest a place](https://github.com/Mrroot3r/Lost-and-Hidden-Atlas/issues/new?template=lead.yml) and [Report a visit](https://github.com/Mrroot3r/Lost-and-Hidden-Atlas/issues/new?template=visit.yml) forms do the same from here. A name and a spot are enough; what you send is checked before the map changes, and it is public. `GUIDE.md` explains the place format and the research rules that keep the map trustworthy. Changes come in as pull requests; nothing is pushed straight to `main`, because merging publishes the site.

## Data credits

Imagery: New York State ITS Geospatial Services, MassGIS, Vermont Center for Geographic Information, RIGIS and the URI Environmental Data Center, New Jersey Office of GIS, CT ECO (University of Connecticut), NH GRANIT (University of New Hampshire), Pennsylvania Emergency Management Agency through PASDA, Maine GeoLibrary, Kansas NG911 through the Kansas Geological Survey, USGS (including the 3DEP elevation service), Esri.
Lines and leads: OpenStreetMap contributors, OpenHistoricalMap, MassGIS, U.S. DOT.
Public land: USGS PAD-US. Parcels: NYS tax parcel file, NYS DEC, MassGIS.
