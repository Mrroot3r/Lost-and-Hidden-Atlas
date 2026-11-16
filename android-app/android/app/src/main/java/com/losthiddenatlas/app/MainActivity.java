package com.losthiddenatlas.app;

import android.os.Bundle;
import androidx.activity.OnBackPressedCallback;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {

    @Override
    public void onCreate(Bundle savedInstanceState) {
        registerPlugin(FieldLogPlugin.class);
        super.onCreate(savedInstanceState);

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
