package com.losthiddenatlas.app;

import java.util.HashSet;
import java.util.Locale;

/**
 * "Near me": the places and leads the page handed over, and the test for "has one just come within range".
 * Plain Java with nothing from Android in it, so it can be run on a desk: see source/tools/near_check.sh.
 *
 * The list is text. The first line is the alert distance in metres (0 = off); every other line is one target,
 * "lat TAB lon TAB id TAB name". FieldLogPlugin.targets writes it, TrackService reads it.
 */
final class NearList {

    /** What to tell the walker when something has come within range. */
    static final class Hit {
        final String name;
        final double metres;
        final String compass;
        final int others; // how many more came within range on the same fix

        Hit(String name, double metres, String compass, int others) {
            this.name = name;
            this.metres = metres;
            this.compass = compass;
            this.others = others;
        }

        /** "Cole Hill farmstead · 270 ft N · and 1 more" */
        String line(boolean km) {
            String far = km ? Math.max(10, Math.round(metres / 10.0) * 10) + " m" : Math.max(10, Math.round(metres * 3.28084 / 10.0) * 10) + " ft";
            return (name.isEmpty() ? "a place on the map" : name) + " · " + far + " " + compass + (others > 0 ? " · and " + others + " more" : "");
        }
    }

    private double range = 0; // metres; 0 = off
    private double[] lat = new double[0];
    private double[] lon = new double[0];
    private String[] id = new String[0];
    private String[] name = new String[0];
    private final HashSet<String> inside = new HashSet<>(); // the ones we are standing near now, so each buzzes once

    int size() {
        return lat.length;
    }

    double range() {
        return range;
    }

    /** Start of a recording: nothing counts as "already near". */
    void forget() {
        inside.clear();
    }

    /** Replaces the list. Lines that do not parse are skipped; null or empty text switches the alert off. */
    void load(String text) {
        range = 0;
        lat = new double[0];
        lon = new double[0];
        id = new String[0];
        name = new String[0];
        if (text == null) return;
        String[] lines = text.split("\n");
        if (lines.length == 0) return;
        try {
            double r = Double.parseDouble(lines[0].trim());
            range = Double.isNaN(r) ? 0 : Math.max(0, Math.min(1000, r));
        } catch (NumberFormatException e) {
            return;
        }
        int n = lines.length - 1, k = 0;
        double[] la = new double[n], lo = new double[n];
        String[] ids = new String[n], names = new String[n];
        for (int i = 1; i < lines.length; i++) {
            String[] f = lines[i].split("\t", 4);
            if (f.length < 3 || f[2].isEmpty()) continue;
            try {
                double y = Double.parseDouble(f[0]), x = Double.parseDouble(f[1]);
                if (Double.isNaN(y) || Double.isNaN(x) || Math.abs(y) > 90 || Math.abs(x) > 180) continue;
                la[k] = y;
                lo[k] = x;
            } catch (NumberFormatException e) {
                continue;
            }
            ids[k] = f[2];
            names[k] = f.length > 3 ? f[3].trim() : "";
            k++;
        }
        lat = java.util.Arrays.copyOf(la, k);
        lon = java.util.Arrays.copyOf(lo, k);
        id = java.util.Arrays.copyOf(ids, k);
        name = java.util.Arrays.copyOf(names, k);
    }

    /**
     * Call with every good fix. Returns the nearest target that has just come within range, or null.
     * A target is reported once; it can be reported again only after the phone has gone more than
     * twice the range (plus 30 m of GPS wobble) away from it.
     */
    Hit check(double atLat, double atLon) {
        if (range <= 0 || lat.length == 0) return null;
        double out = range * 2 + 30;
        int best = -1, others = 0;
        double bestD = 0;
        for (int i = 0; i < lat.length; i++) {
            if (Math.abs(lat[i] - atLat) > 0.02) { // more than 2 km north or south: no need for the full sum
                if (!inside.isEmpty()) inside.remove(id[i]);
                continue;
            }
            double d = dist(atLat, atLon, lat[i], lon[i]);
            if (d <= range) {
                if (inside.add(id[i])) {
                    if (best < 0 || d < bestD) {
                        if (best >= 0) others++;
                        best = i;
                        bestD = d;
                    } else others++;
                }
            } else if (d > out) inside.remove(id[i]);
        }
        if (best < 0) return null;
        return new Hit(name[best], bestD, compass(atLat, atLon, lat[best], lon[best]), others);
    }

    /** One line of the list file. Tabs and line breaks in a name would break the format, so they become spaces. */
    static String row(double lat, double lon, String id, String name) {
        String clean = name == null ? "" : name.replace('\t', ' ').replace('\n', ' ').replace('\r', ' ');
        String key = id == null ? "" : id.replace('\t', ' ').replace('\n', ' ').replace('\r', ' ');
        return String.format(Locale.US, "%.5f\t%.5f\t%s\t%s", lat, lon, key, clean);
    }

    static double dist(double lat1, double lon1, double lat2, double lon2) {
        double r = 6371000, dLat = Math.toRadians(lat2 - lat1), dLon = Math.toRadians(lon2 - lon1);
        double a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
            Math.cos(Math.toRadians(lat1)) * Math.cos(Math.toRadians(lat2)) * Math.sin(dLon / 2) * Math.sin(dLon / 2);
        return 2 * r * Math.asin(Math.sqrt(a));
    }

    /** N, NE, E ... from the first point towards the second. */
    static String compass(double lat1, double lon1, double lat2, double lon2) {
        double y = Math.sin(Math.toRadians(lon2 - lon1)) * Math.cos(Math.toRadians(lat2));
        double x = Math.cos(Math.toRadians(lat1)) * Math.sin(Math.toRadians(lat2)) -
            Math.sin(Math.toRadians(lat1)) * Math.cos(Math.toRadians(lat2)) * Math.cos(Math.toRadians(lon2 - lon1));
        double b = (Math.toDegrees(Math.atan2(y, x)) + 360.0) % 360.0;
        String[] names = { "N", "NE", "E", "SE", "S", "SW", "W", "NW" };
        return names[(int) Math.round(b / 45.0) % 8];
    }
}
