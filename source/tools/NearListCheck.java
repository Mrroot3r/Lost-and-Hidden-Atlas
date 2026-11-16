package com.losthiddenatlas.app;

/**
 * Desk check of the "Near me" buzz logic the Android recorder uses (NearList.java). Run it with tools/near_check.sh.
 * It cannot prove the phone vibrates; it proves the list parses and that each target is reported once, at the right time.
 */
public class NearListCheck {
    static int fails = 0;

    static void ok(String what, boolean cond, Object got) {
        System.out.println((cond ? "ok   " : "FAIL ") + what + (got == null ? "" : "  [" + got + "]"));
        if (!cond) fails++;
    }

    public static void main(String[] args) {
        double lat = 42.6, lon = -74.1, m = 1.0 / 111320.0; // one metre of latitude
        String list = "100.0\n" +
            NearList.row(lat, lon, "p:cellar", "Cole Hill farmstead") + "\n" +
            NearList.row(lat + 60 * m, lon, "l:42.60054,-74.1", "fallen\tchimney") + "\n" +
            NearList.row(lat + 5000 * m, lon, "m:10071234", "Old quarry") + "\n" +
            "not a row\n" + "91.5\t0\tbad\tout of range\n" + "42.6\t-74.1\t\tno id\n";
        NearList n = new NearList();
        n.load(list);
        ok("three good rows kept, three bad ones dropped", n.size() == 3 && n.range() == 100.0, n.size() + " rows, range " + n.range());
        ok("400 m south: nothing", n.check(lat - 400 * m, lon) == null, null);
        ok("150 m south: nothing yet", n.check(lat - 150 * m, lon) == null, null);
        NearList.Hit h = n.check(lat - 90 * m, lon);
        ok("90 m south: the farmstead, to the north", h != null && h.name.equals("Cole Hill farmstead") && h.compass.equals("N") && h.others == 0 && Math.abs(h.metres - 90) < 1, h == null ? "null" : h.line(false));
        ok("feet and metres wording", h != null && h.line(false).matches("Cole Hill farmstead · (290|300) ft N") && h.line(true).equals("Cole Hill farmstead · 90 m N"), h == null ? "null" : h.line(false) + " / " + h.line(true));
        ok("still 90 m south: silent", n.check(lat - 90 * m, lon) == null, null);
        h = n.check(lat - 30 * m, lon);
        ok("30 m south: the second target comes into range, tab in its name made a space", h != null && h.name.equals("fallen chimney"), h == null ? "null" : h.line(false));
        ok("standing on it: silent", n.check(lat, lon) == null, null);
        ok("180 m away (inside twice the range): no re-arm", n.check(lat - 180 * m, lon) == null && n.check(lat - 80 * m, lon) == null, null);
        ok("300 m away, then back: buzzes again, and counts the other one", n.check(lat - 300 * m, lon) == null && (h = n.check(lat + 30 * m, lon)) != null && h.others == 1, h == null ? "null" : h.line(false));
        n.check(lat + 30 * m, lon);
        n.forget();
        ok("a new recording forgets what was near", n.check(lat + 30 * m, lon) != null, null);
        ok("far target 5 km north is found from the east", (h = n.check(lat + 5000 * m, lon + 0.0005)) != null && h.name.equals("Old quarry") && h.compass.equals("W"), h == null ? "null" : h.line(false));
        n.load("0\n" + NearList.row(lat, lon, "p:cellar", "x"));
        ok("range 0 switches it off", n.check(lat, lon) == null, null);
        n.load(null);
        ok("no file: off, no crash", n.size() == 0 && n.check(lat, lon) == null, null);
        n.load("rubbish");
        ok("a damaged file: off, no crash", n.size() == 0 && n.check(lat, lon) == null, null);
        StringBuilder big = new StringBuilder("200\n");
        for (int i = 0; i < 4000; i++) big.append(NearList.row(lat + (i % 200) * 0.002, lon + (i / 200) * 0.002, "v:" + i, "n" + i)).append('\n');
        n.load(big.toString());
        long t0 = System.nanoTime();
        int hits = 0;
        for (int i = 0; i < 1000; i++) if (n.check(lat + i * 0.0001, lon + i * 0.00005) != null) hits++;
        double ms = (System.nanoTime() - t0) / 1e6 / 1000.0;
        ok("4,000 targets: a check takes well under a millisecond", n.size() == 4000 && ms < 1.0 && hits > 5, String.format("%.3f ms each, %d alerts on a 15 km walk", ms, hits));
        System.out.println(fails == 0 ? "near list check passed" : fails + " FAILED");
        System.exit(fails == 0 ? 0 : 1);
    }
}
