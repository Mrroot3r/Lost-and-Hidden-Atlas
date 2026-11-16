package com.losthiddenatlas.app;

import android.content.Context;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

/**
 * Track points on disk: one text file per field log, one "lat,lon,unixSeconds" line per point.
 * The recording service appends; the page reads. Nothing here depends on the page being alive.
 */
final class TrackStore {

    private TrackStore() {}

    static boolean validId(String id) {
        return id != null && id.matches("[A-Za-z0-9_-]{1,64}");
    }

    private static File file(Context c, String id) {
        File dir = new File(c.getFilesDir(), "tracks");
        if (!dir.exists()) dir.mkdirs();
        return new File(dir, id + ".csv");
    }

    static synchronized void append(Context c, String id, double lat, double lon, long seconds) {
        try (FileWriter w = new FileWriter(file(c, id), true)) {
            w.write(String.format(Locale.US, "%.5f,%.5f,%d\n", lat, lon, seconds));
        } catch (Exception ignored) {}
    }

    /** Every point from index "from" on, as {lat, lon, seconds}. */
    static synchronized List<double[]> read(Context c, String id, int from) {
        List<double[]> out = new ArrayList<>();
        File f = file(c, id);
        if (!f.exists()) return out;
        try (BufferedReader r = new BufferedReader(new FileReader(f))) {
            String line;
            int i = 0;
            while ((line = r.readLine()) != null) {
                if (i++ < from) continue;
                String[] p = line.split(",");
                if (p.length < 3) continue;
                try {
                    out.add(new double[] { Double.parseDouble(p[0]), Double.parseDouble(p[1]), Double.parseDouble(p[2]) });
                } catch (NumberFormatException ignored) {}
            }
        } catch (Exception ignored) {}
        return out;
    }

    static synchronized int count(Context c, String id) {
        File f = file(c, id);
        if (!f.exists()) return 0;
        int n = 0;
        try (BufferedReader r = new BufferedReader(new FileReader(f))) {
            while (r.readLine() != null) n++;
        } catch (Exception ignored) {}
        return n;
    }

    static synchronized void delete(Context c, String id) {
        File f = file(c, id);
        if (f.exists()) f.delete();
    }
}
