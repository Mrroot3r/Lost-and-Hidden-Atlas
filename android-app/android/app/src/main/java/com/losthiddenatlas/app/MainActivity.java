package com.losthiddenatlas.app;

import android.os.Bundle;
import androidx.activity.OnBackPressedCallback;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {

    @Override
    public void onCreate(Bundle savedInstanceState) {
        registerPlugin(FieldLogPlugin.class);
        super.onCreate(savedInstanceState);

        // The page is never magnified, only the map (GUIDE.md section 9): once the whole screen came up a quarter bigger with
        // its edges cut off and there was no way back. The page refuses zoom too; this is the same rule on the WebView's side.
        try {
            android.webkit.WebSettings ws = bridge.getWebView().getSettings();
            ws.setSupportZoom(false);
            ws.setBuiltInZoomControls(false);
            ws.setDisplayZoomControls(false);
        } catch (Exception e) {}

        // Back closes whatever is open in the page (a sheet, a place, a popup). When nothing is open the app goes to the
        // background instead of closing, so the map and a running field log are still there when it is reopened.
        getOnBackPressedDispatcher().addCallback(
            this,
            new OnBackPressedCallback(true) {
                @Override
                public void handleOnBackPressed() {
                    try {
                        bridge
                            .getWebView()
                            .evaluateJavascript(
                                "(window.atlasBack&&window.atlasBack())?1:0",
                                value -> {
                                    if (!"1".equals(value)) moveTaskToBack(true);
                                }
                            );
                    } catch (Exception e) {
                        moveTaskToBack(true);
                    }
                }
            }
        );
    }
}
