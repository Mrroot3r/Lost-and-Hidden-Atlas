#!/bin/bash
# Desk check of the "Near me" buzz logic in the Android app: bash tools/near_check.sh [repository]
# Compiles android-app/.../NearList.java (plain Java, nothing from Android) with tools/NearListCheck.java and runs it.
# Needs a JDK (javac). Run it after any change to NearList.java.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="${1:-$(cd "$HERE/../.." && pwd)}"
SRC="$REPO/android-app/android/app/src/main/java/com/losthiddenatlas/app/NearList.java"
[ -f "$SRC" ] || { echo "NearList.java not found under $REPO"; exit 1; }
OUT="$(mktemp -d)"
JAVA_TOOL_OPTIONS= javac -encoding UTF-8 -d "$OUT" "$SRC" "$HERE/NearListCheck.java"
JAVA_TOOL_OPTIONS= java -Dfile.encoding=UTF-8 -Dstdout.encoding=UTF-8 -cp "$OUT" com.losthiddenatlas.app.NearListCheck
rm -rf "$OUT"
