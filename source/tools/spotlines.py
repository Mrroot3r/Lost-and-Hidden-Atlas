#!/usr/bin/env python3
"""Spots sent through the form. The app's "Send spots to the public Atlas" fills the form's Place with "Spots: N marked for
research" and its text with one line a spot: "1. 42.65852, -73.77767 a few words". tools/inbox.py shows each as its own
lead to research. Like everything in the inbox, each is a stranger's tip."""
import re
def spots(place,text):
    """[(number, lat, lon, note)] when the submission says it is spots, else []"""
    if not re.match(r'\s*spots:\s*\d+',place or '',re.I): return []
    out=[]
    for l in (text or '').replace('\r','').split('\n'):
        m=re.match(r'\s*(\d{1,3})[.)]\s*(-?\d{1,2}\.\d{4,})\s*,\s*(-?\d{1,3}\.\d{4,})\s*(.*)$',l)
        if not m: continue
        la,lo=float(m.group(2)),float(m.group(3))
        if abs(la)>90 or abs(lo)>180: continue
        out.append((int(m.group(1)),la,lo,m.group(4).strip()[:140]))
    return out
