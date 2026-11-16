package com.losthiddenatlas.app;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.ServiceInfo;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.media.AudioAttributes;
import android.os.Build;
import android.os.Bundle;
import android.os.IBinder;
import android.os.Looper;
import android.os.PowerManager;
import android.os.VibrationEffect;
import android.os.Vibrator;
import android.widget.Toast;
import androidx.annotation.NonNull;
import androidx.core.app.NotificationCompat;
import java.util.List;
import java.util.Locale;

/**
 * Records a field log with the screen off or the app in the background.
 * It runs as a foreground service (Android shows a notification while it records), listens to GPS,
 * smooths the fixes, and appends accepted points to a file through TrackStore. It also does the "Near me" buzz:
 * the page hands it a list of places and leads (NearList), and it vibrates when the phone comes within range of one.
 * The page is not involved: it reads the file when it is next visible.
 */
public class TrackService extends Service implements LocationListener {

    static final String PREFS = "fieldlog";
    static final String ACTION_MARK = "com.losthiddenatlas.app.MARK"; // sent by the notification's "Mark here" button
    static volatile boolean running = false;
    // for the status readout in the app: how many GPS fixes arrived, how many were kept, and how good the last one was
    static volatile int fixes = 0;
    static volatile int kept = 0;
    static volatile float lastAccuracy = -1f;
    static volatile long lastFixAt = 0;
    static volatile String lastError = "";

    private static final String CHANNEL = "fieldlog";
    private static final int NOTE_ID = 4101;
    private static final float MAX_ACCURACY_M = 35f; // fixes worse than this are not recorded
    private double minStep = 4.0; // a new point is saved only this far from the last one (Settings, "Track detail")

    private LocationManager locations;
    private PowerManager.WakeLock wake;
    private String logId = "";
    private String activeId = ""; // the log the listener is currently writing to
    private String title = "Field log";

    // filter state: a one-number Kalman filter, the same one the page uses for its blue dot
    private boolean haveFix = false;
    private double fLat, fLon, fVar;
    private long fTime;
    private int badRun = 0;

    private boolean haveLast = false;
    private double lastLat, lastLon;
    private int count = 0;
    private int markCount = 0;
    private double meters = 0;
    private long lastNoteUpdate = 0;

    // "Near me": places and leads the page handed over (FieldLogPlugin.targets). The phone buzzes when one comes within range.
    private final NearList near = new NearList();
    private long nearStamp = -1; // which version of the list file is loaded
    private long nearLooked = 0;
    private String nearLine = ""; // what the notification says we are near
    private long nearUntil = 0;

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        SharedPreferences p = getSharedPreferences(PREFS, MODE_PRIVATE);
        logId = p.getString("logId", "");
        title = p.getString("title", "Field log");
        try {
            Notification n = note("Recording your route");
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
                startForeground(NOTE_ID, n, ServiceInfo.FOREGROUND_SERVICE_TYPE_LOCATION);
            } else {
                startForeground(NOTE_ID, n);
            }
        } catch (Exception e) {
            // Android refused, usually because it restarted us in the background without "allow all the time".
            // The page starts the recorder again the next time it is opened.
            lastError = "startForeground: " + e;
            running = false;
            stopSelf();
            return START_NOT_STICKY;
        }
        if (!p.getBoolean("rec", false) || !TrackStore.validId(logId)) {
            stopForegroundCompat();
            stopSelf();
            return START_NOT_STICKY;
        }
        if (running && !logId.equals(activeId)) halt(); // a different log was started without stopping the first
        if (!running) begin();
        if (running && intent != null && ACTION_MARK.equals(intent.getAction())) mark();
        return START_STICKY;
    }

    private void begin() {
        running = true;
        fixes = 0;
        kept = 0;
        lastError = "";
        activeId = logId;
        haveFix = false;
        haveLast = false;
        badRun = 0;
        near.forget();
        nearStamp = -1;
        nearLooked = 0;
        nearLine = "";
        List<double[]> have = TrackStore.read(this, logId, 0);
        count = have.size();
        markCount = TrackStore.readMarks(this, logId, 0).size();
        meters = 0;
        for (int i = 1; i < have.size(); i++) meters += dist(have.get(i - 1)[0], have.get(i - 1)[1], have.get(i)[0], have.get(i)[1]);
        if (count > 0) {
            lastLat = have.get(count - 1)[0];
            lastLon = have.get(count - 1)[1];
            haveLast = true;
        }
        locations = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
        try {
            SharedPreferences p = getSharedPreferences(PREFS, MODE_PRIVATE);
            minStep = Math.max(1f, Math.min(50f, p.getFloat("step", 4f)));
            long every = Math.max(1000L, Math.min(30000L, p.getLong("every", 2000L)));
            locations.requestLocationUpdates(LocationManager.GPS_PROVIDER, every, 0f, this, Looper.getMainLooper());
        } catch (SecurityException | IllegalArgumentException e) {
            lastError = "requestLocationUpdates: " + e;
            running = false;
            stopForegroundCompat();
            stopSelf();
            return;
        }
        try {
            PowerManager pm = (PowerManager) getSystemService(Context.POWER_SERVICE);
            wake = pm.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK, "atlas:fieldlog");
            wake.setReferenceCounted(false);
            wake.acquire(12L * 60L * 60L * 1000L); // released when recording stops; the limit is a safety net
        } catch (Exception ignored) {}
    }

    @Override
    public void onLocationChanged(@NonNull Location l) {
        float acc = l.hasAccuracy() ? Math.max(3f, l.getAccuracy()) : 50f;
        long t = l.getTime() > 0 ? l.getTime() : System.currentTimeMillis();
        fixes++;
        lastAccuracy = acc;
        lastFixAt = System.currentTimeMillis();
        double[] p = filter(l.getLatitude(), l.getLongitude(), acc, l.hasSpeed() ? l.getSpeed() : -1f, t);
        if (p == null || acc > MAX_ACCURACY_M) return;
        checkNear(p[0], p[1]); // before the "have we moved" test: a list the page has just sent must not wait for the next step
        if (haveLast) {
            double d = dist(lastLat, lastLon, p[0], p[1]);
            if (d < minStep) return;
            meters += d;
        }
        TrackStore.append(this, logId, p[0], p[1], t / 1000L);
        lastLat = p[0];
        lastLon = p[1];
        haveLast = true;
        count++;
        kept++;
        long now = System.currentTimeMillis();
        if (now - lastNoteUpdate > 20000L) {
            lastNoteUpdate = now;
            try {
                NotificationManager nm = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
                nm.notify(NOTE_ID, note(status()));
            } catch (Exception ignored) {}
        }
    }

    /**
     * "Near me": buzzes when a place or lead comes within range, and names it in the notification.
     * The list file is looked at again at most every 15 seconds, and re-read only when the page has rewritten it.
     */
    private void checkNear(double lat, double lon) {
        long now = System.currentTimeMillis();
        if (now - nearLooked >= 15000L) {
            nearLooked = now;
            long stamp = TrackStore.nearStamp(this);
            if (stamp != nearStamp) {
                nearStamp = stamp;
                try {
                    near.load(TrackStore.readNear(this));
                } catch (Exception e) {
                    lastError = "near-me list: " + e;
                }
            }
        }
        NearList.Hit hit = near.check(lat, lon);
        if (hit == null) return;
        nearLine = hit.line("km".equals(getSharedPreferences(PREFS, MODE_PRIVATE).getString("units", "mi")));
        nearUntil = now + 10L * 60L * 1000L;
        try {
            Vibrator v = (Vibrator) getSystemService(Context.VIBRATOR_SERVICE);
            if (v != null) {
                long[] pattern = { 0, 260, 140, 260 }; // two longer buzzes, unlike the single short one for "Mark here"
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
                    // sent as an alarm so that a silenced ringer does not swallow it: the walker asked for this buzz
                    AudioAttributes aa = new AudioAttributes.Builder().setUsage(AudioAttributes.USAGE_ALARM).setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION).build();
                    v.vibrate(VibrationEffect.createWaveform(pattern, -1), aa);
                } else v.vibrate(pattern, -1);
            }
        } catch (Exception ignored) {}
        try {
            NotificationManager nm = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
            nm.notify(NOTE_ID, note(status()));
        } catch (Exception ignored) {}
    }

    /** "Mark here": saves a timed pin where the phone is now. The page turns it into a note that can be named later. */
    private void mark() {
        double lat = Double.NaN, lon = Double.NaN;
        if (haveFix && System.currentTimeMillis() - lastFixAt < 30000L) {
            lat = fLat;
            lon = fLon;
        } else if (haveLast) { // standing still: the last saved point is where we are
            lat = lastLat;
            lon = lastLon;
        }
        TrackStore.appendMark(this, logId, lat, lon, System.currentTimeMillis() / 1000L);
        markCount++;
        try {
            NotificationManager nm = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
            nm.notify(NOTE_ID, note(status()));
        } catch (Exception ignored) {}
        try {
            if (getSharedPreferences(PREFS, MODE_PRIVATE).getBoolean("buzz", true)) {
                Vibrator v = (Vibrator) getSystemService(Context.VIBRATOR_SERVICE);
                if (v != null) {
                    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) v.vibrate(VibrationEffect.createOneShot(70, VibrationEffect.DEFAULT_AMPLITUDE));
                    else v.vibrate(70);
                }
            }
        } catch (Exception ignored) {}
        try {
            Toast.makeText(getApplicationContext(), "Marked (" + markCount + ")", Toast.LENGTH_SHORT).show();
        } catch (Exception ignored) {}
    }

    private String status() {
        boolean km = "km".equals(getSharedPreferences(PREFS, MODE_PRIVATE).getString("units", "mi"));
        String s = km ? String.format(Locale.US, "Recording · %.2f km", meters / 1000.0) : String.format(Locale.US, "Recording · %.2f mi", meters / 1609.34);
        return markCount > 0 ? s + " · " + markCount + (markCount == 1 ? " mark" : " marks") : s;
    }

    /** Trusts a fix by its stated accuracy and loosens up when the phone is really moving. Returns null for a fix to ignore. */
    private double[] filter(double lat, double lon, float acc, float speed, long t) {
        if (!haveFix) {
            haveFix = true;
            fLat = lat;
            fLon = lon;
            fVar = acc * acc;
            fTime = t;
            return new double[] { lat, lon };
        }
        double dts = Math.max(0, Math.min(60, (t - fTime) / 1000.0));
        if (acc > 80 && badRun < 4 && dts < 20) {
            badRun++;
            return null;
        }
        badRun = 0;
        double innov = dist(fLat, fLon, lat, lon);
        double q = speed >= 0 ? speed : 0;
        if (innov > 2.5 * acc) q = Math.max(q, innov / Math.max(1, dts));
        q = Math.max(1.5, Math.min(45, q));
        fVar += dts * q * q;
        fTime = t;
        double k = fVar / (fVar + acc * acc);
        fLat += k * (lat - fLat);
        fLon += k * (lon - fLon);
        fVar = (1 - k) * fVar;
        return new double[] { fLat, fLon };
    }

    private static double dist(double lat1, double lon1, double lat2, double lon2) {
        double r = 6371000, dLat = Math.toRadians(lat2 - lat1), dLon = Math.toRadians(lon2 - lon1);
        double a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
            Math.cos(Math.toRadians(lat1)) * Math.cos(Math.toRadians(lat2)) * Math.sin(dLon / 2) * Math.sin(dLon / 2);
        return 2 * r * Math.asin(Math.sqrt(a));
    }

    private Notification note(String text) {
        NotificationManager nm = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O && nm.getNotificationChannel(CHANNEL) == null) {
            NotificationChannel ch = new NotificationChannel(CHANNEL, "Field log recording", NotificationManager.IMPORTANCE_LOW);
            ch.setDescription("Shown while the Atlas is recording your route");
            ch.setShowBadge(false);
            nm.createNotificationChannel(ch);
        }
        Intent open = new Intent(this, MainActivity.class);
        open.setFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP | Intent.FLAG_ACTIVITY_CLEAR_TOP);
        PendingIntent pi = PendingIntent.getActivity(this, 0, open, PendingIntent.FLAG_IMMUTABLE | PendingIntent.FLAG_UPDATE_CURRENT);
        PendingIntent markIntent = PendingIntent.getService(this, 1, new Intent(this, TrackService.class).setAction(ACTION_MARK), PendingIntent.FLAG_IMMUTABLE | PendingIntent.FLAG_UPDATE_CURRENT);
        boolean nearNow = !nearLine.isEmpty() && System.currentTimeMillis() < nearUntil; // for ten minutes after a buzz, say what it was for
        NotificationCompat.Builder b = new NotificationCompat.Builder(this, CHANNEL);
        if (nearNow) b.setStyle(new NotificationCompat.BigTextStyle().bigText("Near " + nearLine + "\n" + text));
        return b
            .setSmallIcon(R.drawable.ic_stat_track)
            .setContentTitle(title)
            .setContentText(nearNow ? "Near " + nearLine : text)
            .setOngoing(true)
            .setOnlyAlertOnce(true)
            .setCategory(NotificationCompat.CATEGORY_SERVICE)
            .setPriority(NotificationCompat.PRIORITY_LOW)
            .setContentIntent(pi)
            .addAction(0, "Mark here", markIntent)
            .build();
    }

    private void stopForegroundCompat() {
        try {
            stopForeground(STOP_FOREGROUND_REMOVE);
        } catch (Exception ignored) {}
    }

    private void halt() {
        running = false;
        try {
            if (locations != null) locations.removeUpdates(this);
        } catch (Exception ignored) {}
        try {
            if (wake != null && wake.isHeld()) wake.release();
        } catch (Exception ignored) {}
    }

    @Override
    public void onDestroy() {
        halt();
        super.onDestroy();
    }

    // Older Android versions call these and have no default for them.
    @Override
    public void onStatusChanged(String provider, int status, Bundle extras) {}

    @Override
    public void onProviderEnabled(@NonNull String provider) {}

    @Override
    public void onProviderDisabled(@NonNull String provider) {}
}
