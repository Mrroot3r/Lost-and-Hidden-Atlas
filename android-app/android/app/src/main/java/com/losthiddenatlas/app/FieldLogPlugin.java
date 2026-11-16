package com.losthiddenatlas.app;

import android.Manifest;
import android.content.ClipData;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.location.LocationManager;
import android.net.Uri;
import android.os.Build;
import android.os.PowerManager;
import android.provider.Settings;
import androidx.core.content.ContextCompat;
import androidx.core.content.FileProvider;
import com.getcapacitor.JSArray;
import com.getcapacitor.JSObject;
import com.getcapacitor.PermissionState;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.CapacitorPlugin;
import com.getcapacitor.annotation.Permission;
import com.getcapacitor.annotation.PermissionCallback;
import java.io.File;
import java.io.FileOutputStream;
import java.nio.charset.StandardCharsets;
import java.util.List;

/**
 * What the page can ask the phone to do for a field log:
 * start and stop the background recorder, read the points it has saved, share a file, and open the two
 * Android settings that keep recording reliable. The page calls these as FieldLog.<method>.
 */
@CapacitorPlugin(
    name = "FieldLog",
    permissions = {
        @Permission(alias = "location", strings = { Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION }),
        @Permission(alias = "notifications", strings = { Manifest.permission.POST_NOTIFICATIONS }),
        @Permission(alias = "background", strings = { Manifest.permission.ACCESS_BACKGROUND_LOCATION })
    }
)
public class FieldLogPlugin extends Plugin {

    private SharedPreferences prefs() {
        return getContext().getSharedPreferences(TrackService.PREFS, Context.MODE_PRIVATE);
    }

    private boolean has(String permission) {
        return ContextCompat.checkSelfPermission(getContext(), permission) == PackageManager.PERMISSION_GRANTED;
    }

    private JSObject state() {
        Context c = getContext();
        SharedPreferences p = prefs();
        String id = p.getString("logId", "");
        JSObject o = new JSObject();
        o.put("recording", p.getBoolean("rec", false));
        o.put("running", TrackService.running);
        o.put("logId", id);
        o.put("started", p.getLong("started", 0));
        o.put("count", TrackStore.validId(id) ? TrackStore.count(c, id) : 0);
        o.put("fine", has(Manifest.permission.ACCESS_FINE_LOCATION));
        o.put("background", Build.VERSION.SDK_INT < Build.VERSION_CODES.Q || has(Manifest.permission.ACCESS_BACKGROUND_LOCATION));
        boolean gps = false;
        try {
            LocationManager lm = (LocationManager) c.getSystemService(Context.LOCATION_SERVICE);
            gps = lm != null && lm.isProviderEnabled(LocationManager.GPS_PROVIDER);
        } catch (Exception ignored) {}
        o.put("gps", gps);
        boolean unrestricted = true;
        try {
            PowerManager pm = (PowerManager) c.getSystemService(Context.POWER_SERVICE);
            unrestricted = pm == null || pm.isIgnoringBatteryOptimizations(c.getPackageName());
        } catch (Exception ignored) {}
        o.put("battery", unrestricted);
        o.put("fixes", TrackService.fixes);
        o.put("kept", TrackService.kept);
        o.put("lastAccuracy", TrackService.lastAccuracy);
        o.put("lastFixAgo", TrackService.lastFixAt > 0 ? (System.currentTimeMillis() - TrackService.lastFixAt) / 1000 : -1);
        o.put("error", TrackService.lastError);
        o.put("android", Build.VERSION.SDK_INT);
        o.put("phone", Build.MANUFACTURER + " " + Build.MODEL);
        try {
            o.put("version", c.getPackageManager().getPackageInfo(c.getPackageName(), 0).versionName);
        } catch (Exception ignored) {}
        return o;
    }

    @PluginMethod
    public void status(PluginCall call) {
        call.resolve(state());
    }

    /** start({logId, title}): asks for location (and, on newer phones, notification) permission, then starts recording. */
    @PluginMethod
    public void start(PluginCall call) {
        if (!TrackStore.validId(call.getString("logId"))) {
            call.reject("That log has no usable id.");
            return;
        }
        if (!has(Manifest.permission.ACCESS_FINE_LOCATION)) {
            requestPermissionForAlias("location", call, "afterLocation");
            return;
        }
        afterLocation(call);
    }

    @PermissionCallback
    private void afterLocation(PluginCall call) {
        if (!has(Manifest.permission.ACCESS_FINE_LOCATION)) {
            call.reject("Precise location was not allowed. Allow it for the Atlas in Android settings, then try again.");
            return;
        }
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU && getPermissionState("notifications") == PermissionState.PROMPT) {
            requestPermissionForAlias("notifications", call, "afterNotifications");
            return;
        }
        begin(call);
    }

    @PermissionCallback
    private void afterNotifications(PluginCall call) {
        begin(call); // recording works without the notification being visible, so a refusal does not stop it
    }

    private void begin(PluginCall call) {
        String id = call.getString("logId");
        SharedPreferences p = prefs();
        boolean same = p.getBoolean("rec", false) && id.equals(p.getString("logId", ""));
        SharedPreferences.Editor e = p.edit().putBoolean("rec", true).putString("logId", id).putString("title", call.getString("title", "Field log"));
        if (!same || p.getLong("started", 0) == 0) e.putLong("started", System.currentTimeMillis());
        e.apply();
        try {
            ContextCompat.startForegroundService(getContext(), new Intent(getContext(), TrackService.class));
        } catch (Exception ex) {
            p.edit().putBoolean("rec", false).apply();
            call.reject("Android would not start the recorder: " + ex.getMessage());
            return;
        }
        call.resolve(state());
    }

    @PluginMethod
    public void stop(PluginCall call) {
        prefs().edit().putBoolean("rec", false).apply();
        try {
            getContext().stopService(new Intent(getContext(), TrackService.class));
        } catch (Exception ignored) {}
        call.resolve(state());
    }

    /** points({logId, from}) -> {points: [[lat, lon, seconds], ...], count} */
    @PluginMethod
    public void points(PluginCall call) {
        String id = call.getString("logId");
        if (!TrackStore.validId(id)) {
            call.reject("That log has no usable id.");
            return;
        }
        Integer from = call.getInt("from", 0);
        List<double[]> pts = TrackStore.read(getContext(), id, from == null ? 0 : Math.max(0, from));
        JSArray arr = new JSArray();
        try {
            for (double[] p : pts) {
                JSArray one = new JSArray();
                one.put(p[0]);
                one.put(p[1]);
                one.put((long) p[2]);
                arr.put(one);
            }
        } catch (Exception ignored) {}
        JSObject o = new JSObject();
        o.put("points", arr);
        o.put("count", (from == null ? 0 : Math.max(0, from)) + pts.size());
        call.resolve(o);
    }

    @PluginMethod
    public void remove(PluginCall call) {
        String id = call.getString("logId");
        SharedPreferences p = prefs();
        boolean active = p.getBoolean("rec", false) && id != null && id.equals(p.getString("logId", ""));
        if (TrackStore.validId(id) && !active) TrackStore.delete(getContext(), id);
        call.resolve();
    }

    /** Asks Android to stop pausing the app to save battery, which is what usually ends a background recording. */
    @PluginMethod
    public void battery(PluginCall call) {
        Context c = getContext();
        try {
            Intent i = new Intent(Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS, Uri.parse("package:" + c.getPackageName()));
            getActivity().startActivity(i);
        } catch (Exception e) {
            try {
                getActivity().startActivity(new Intent(Settings.ACTION_IGNORE_BATTERY_OPTIMIZATION_SETTINGS));
            } catch (Exception ignored) {}
        }
        call.resolve();
    }

    /** Opens this app's page in Android settings, where location can be set to "Allow all the time". */
    @PluginMethod
    public void appSettings(PluginCall call) {
        try {
            Intent i = new Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS, Uri.parse("package:" + getContext().getPackageName()));
            getActivity().startActivity(i);
        } catch (Exception ignored) {}
        call.resolve();
    }

    /** share({name, text, mime}): hands a file to Android's share sheet (GPX tracks, note lists). */
    @PluginMethod
    public void share(PluginCall call) {
        String name = call.getString("name", "atlas.txt").replaceAll("[^A-Za-z0-9._-]", "_");
        String text = call.getString("text", "");
        String mime = call.getString("mime", "text/plain");
        try {
            File dir = new File(getContext().getCacheDir(), "share");
            if (!dir.exists()) dir.mkdirs();
            File f = new File(dir, name);
            try (FileOutputStream out = new FileOutputStream(f)) {
                out.write(text.getBytes(StandardCharsets.UTF_8));
            }
            Uri uri = FileProvider.getUriForFile(getContext(), getContext().getPackageName() + ".fileprovider", f);
            Intent send = new Intent(Intent.ACTION_SEND);
            send.setType(mime);
            send.putExtra(Intent.EXTRA_STREAM, uri);
            send.putExtra(Intent.EXTRA_SUBJECT, name);
            send.setClipData(ClipData.newRawUri(name, uri));
            send.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
            getActivity().startActivity(Intent.createChooser(send, name));
            call.resolve();
        } catch (Exception e) {
            call.reject("Could not share the file: " + e.getMessage());
        }
    }
}
