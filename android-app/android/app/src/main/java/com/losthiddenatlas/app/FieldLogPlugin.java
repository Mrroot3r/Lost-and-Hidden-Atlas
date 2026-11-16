package com.losthiddenatlas.app;

import android.Manifest;
import android.content.ClipData;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.location.LocationManager;
import android.content.ContentResolver;
import android.content.ContentUris;
import android.database.Cursor;
import android.graphics.Bitmap;
import android.net.Uri;
import android.provider.MediaStore;
import android.util.Base64;
import android.util.Size;
import java.io.ByteArrayOutputStream;
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
        @Permission(alias = "background", strings = { Manifest.permission.ACCESS_BACKGROUND_LOCATION }),
        @Permission(alias = "media", strings = { Manifest.permission.READ_MEDIA_IMAGES, Manifest.permission.READ_MEDIA_VIDEO }),
        @Permission(alias = "mediaOld", strings = { Manifest.permission.READ_EXTERNAL_STORAGE })
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
        o.put("media", mediaAccess());
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

    // ---- photos and video taken during a log ----

    /** "all", "some" (Android 14+: the user picked individual photos) or "none". */
    private String mediaAccess() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
            if (has(Manifest.permission.READ_MEDIA_IMAGES) && has(Manifest.permission.READ_MEDIA_VIDEO)) return "all";
            if (Build.VERSION.SDK_INT >= 34 && has("android.permission.READ_MEDIA_VISUAL_USER_SELECTED")) return "some";
            return has(Manifest.permission.READ_MEDIA_IMAGES) || has(Manifest.permission.READ_MEDIA_VIDEO) ? "some" : "none";
        }
        return has(Manifest.permission.READ_EXTERNAL_STORAGE) ? "all" : "none";
    }

    /**
     * media({from, to, ask}): the photos and videos the phone's camera saved between two times (unix seconds).
     * Only their details are read (name, times, length); the files stay where they are.
     * With ask=false it never shows a permission prompt and rejects if access has not been given.
     */
    @PluginMethod
    public void media(PluginCall call) {
        if ("none".equals(mediaAccess())) {
            if (!Boolean.TRUE.equals(call.getBoolean("ask", false))) {
                call.reject("Photo access has not been allowed.");
                return;
            }
            requestPermissionForAlias(Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU ? "media" : "mediaOld", call, "afterMedia");
            return;
        }
        afterMedia(call);
    }

    @PermissionCallback
    private void afterMedia(PluginCall call) {
        String access = mediaAccess();
        if ("none".equals(access)) {
            call.reject("Photo access was not allowed. Allow Photos and videos for the Atlas in Android settings, then try again.");
            return;
        }
        Double fromD = call.getDouble("from"), toD = call.getDouble("to");
        if (fromD == null || toD == null) {
            call.reject("No time range was given.");
            return;
        }
        long from = fromD.longValue(), to = toD.longValue();
        JSArray items = new JSArray();
        try {
            readMedia(items, false, from, to);
            readMedia(items, true, from, to);
        } catch (Exception e) {
            call.reject("The phone's photo list could not be read: " + e.getMessage());
            return;
        }
        JSObject o = new JSObject();
        o.put("items", items);
        o.put("access", access);
        call.resolve(o);
    }

    private void readMedia(JSArray out, boolean video, long from, long to) throws Exception {
        ContentResolver cr = getContext().getContentResolver();
        Uri table = video ? MediaStore.Video.Media.EXTERNAL_CONTENT_URI : MediaStore.Images.Media.EXTERNAL_CONTENT_URI;
        String[] cols = video
            ? new String[] { "_id", "_display_name", "datetaken", "date_modified", "bucket_display_name", "duration" }
            : new String[] { "_id", "_display_name", "datetaken", "date_modified", "bucket_display_name" };
        // A video is stamped when it ends, and a long one may end well after the log does, so look a little wider for those.
        long pad = video ? 4 * 3600 : 0;
        String where = "(datetaken>=? AND datetaken<=?) OR (date_modified>=? AND date_modified<=?)";
        String[] args = { String.valueOf((from - pad) * 1000L), String.valueOf((to + pad) * 1000L), String.valueOf(from), String.valueOf(to + pad) };
        try (Cursor c = cr.query(table, cols, where, args, "date_modified ASC")) {
            if (c == null) return;
            int n = 0;
            while (c.moveToNext() && n++ < 2000) {
                JSObject m = new JSObject();
                m.put("kind", video ? "video" : "image");
                m.put("id", c.getLong(0));
                m.put("name", c.isNull(1) ? "" : c.getString(1));
                m.put("taken", c.isNull(2) ? 0 : c.getLong(2)); // milliseconds
                m.put("modified", c.isNull(3) ? 0 : c.getLong(3)); // seconds
                m.put("bucket", c.isNull(4) ? "" : c.getString(4));
                if (video) m.put("duration", c.isNull(5) ? 0 : c.getLong(5)); // milliseconds
                out.put(m);
            }
        }
    }

    private Uri mediaUri(PluginCall call) {
        Double id = call.getDouble("id");
        if (id == null) return null;
        boolean video = "video".equals(call.getString("kind"));
        return ContentUris.withAppendedId(video ? MediaStore.Video.Media.EXTERNAL_CONTENT_URI : MediaStore.Images.Media.EXTERNAL_CONTENT_URI, id.longValue());
    }

    /** thumb({id, kind, size}) -> {data: "data:image/jpeg;base64,..."}: a small preview of one photo or video. */
    @PluginMethod
    public void thumb(PluginCall call) {
        Uri uri = mediaUri(call);
        if (uri == null || "none".equals(mediaAccess())) {
            call.reject("No preview.");
            return;
        }
        Integer want = call.getInt("size", 256);
        int size = Math.max(96, Math.min(1024, want == null ? 256 : want));
        try {
            Bitmap b;
            ContentResolver cr = getContext().getContentResolver();
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
                b = cr.loadThumbnail(uri, new Size(size, size), null);
            } else {
                long id = ContentUris.parseId(uri);
                b = "video".equals(call.getString("kind"))
                    ? MediaStore.Video.Thumbnails.getThumbnail(cr, id, MediaStore.Video.Thumbnails.MINI_KIND, null)
                    : MediaStore.Images.Thumbnails.getThumbnail(cr, id, MediaStore.Images.Thumbnails.MINI_KIND, null);
            }
            if (b == null) {
                call.reject("No preview.");
                return;
            }
            ByteArrayOutputStream bytes = new ByteArrayOutputStream();
            b.compress(Bitmap.CompressFormat.JPEG, 82, bytes);
            JSObject o = new JSObject();
            o.put("data", "data:image/jpeg;base64," + Base64.encodeToString(bytes.toByteArray(), Base64.NO_WRAP));
            call.resolve(o);
        } catch (Exception e) {
            call.reject("No preview: " + e.getMessage());
        }
    }

    /** openMedia({id, kind}): opens the photo or video in the phone's gallery or player. */
    @PluginMethod
    public void openMedia(PluginCall call) {
        Uri uri = mediaUri(call);
        if (uri == null) {
            call.reject("Nothing to open.");
            return;
        }
        try {
            Intent view = new Intent(Intent.ACTION_VIEW);
            view.setDataAndType(uri, "video".equals(call.getString("kind")) ? "video/*" : "image/*");
            view.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
            getActivity().startActivity(view);
            call.resolve();
        } catch (Exception e) {
            call.reject("No app on this phone could open it.");
        }
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
