#!/usr/bin/env bash
# WAVE3 Spark-safe fetch. Curl official pins. Do not use Drive for binaries.
set -euo pipefail
DEST="${1:-$PWD/wave_fetch}"
mkdir -p "$DEST"
cd "$DEST"
fetch() {
  local url="$1" out="$2" expect="${3:-}"
  echo "+ $out"
  curl -fL --retry 3 -o "$out" "$url"
  if [[ -n "$expect" ]]; then
    got=$(sha256sum "$out" | awk '{print $1}')
    if [[ "$got" != "$expect" ]]; then
      echo "HASH MISMATCH $out expected $expect got $got" >&2
      exit 1
    fi
  fi
}
fetch "https://github.com/eclipse-zenoh/zenoh/releases/download/1.10.0/zenoh-1.10.0-x86_64-unknown-linux-gnu-standalone.zip" zenoh-standalone.zip 43de097382e3db4f95903cbadbbf472a21fbea53d6a3193606ae12b034a20881
fetch "https://github.com/eclipse-zenoh/zenoh/releases/download/1.10.0/zenoh-1.10.0-x86_64-unknown-linux-gnu-debian.zip" zenoh-debian.zip 0025546d81164a2c0747642e28f031bd237289d0c1bdb1ccc0d262c06376ecf5
fetch "https://nodejs.org/dist/v20.20.0/node-v20.20.0-linux-x64.tar.xz" node-v20.20.0-linux-x64.tar.xz
fetch "https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-gnu/rustup-init" rustup-init
chmod +x rustup-init
fetch "https://github.com/junegunn/fzf/releases/download/v0.74.3/fzf-0.74.3-linux_amd64.tar.gz" fzf-0.74.3-linux_amd64.tar.gz
fetch "https://github.com/BurntSushi/ripgrep/releases/download/15.2.0/ripgrep-15.2.0-x86_64-unknown-linux-musl.tar.gz" ripgrep-15.2.0-x86_64-unknown-linux-musl.tar.gz
fetch "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl-shared.tar.xz" ffmpeg-shared.tar.xz
python3 -m pip download -d wheels "eclipse-zenoh==1.10.0" "textual==8.2.8" "prompt_toolkit==3.0.53" "questionary==2.1.0" "duckdb==1.1.0" "cowsay==6.1" "polars==1.21.0" "yt-dlp==2026.8.19" "loguru" "bleak" "vaderSentiment" || true
echo "WAVE3 fetch complete in $DEST"
