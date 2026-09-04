#!/usr/bin/env python3
"""IP-WQ-126 — folder-only ingest. No live scrapers.

Kinds: youtube-short | youtube-long | still | ig-export | fb-export | tt-export | dump

Usage:
  python3 ingest_source.py --kind still --path ./shot.jpg --url ""
  python3 ingest_source.py --kind tt-export --path ./Takeout/TikTok
  python3 ingest_source.py --kind youtube-short --url https://youtube.com/shorts/_CLrJZSn3Og
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ALLOWED = {
    "youtube-short",
    "youtube-long",
    "still",
    "ig-export",
    "fb-export",
    "tt-export",
    "dump",
}
SHORT_RE = re.compile(r"(?:youtube\.com/shorts/|youtu\.be/)([A-Za-z0-9_-]{6,})")
WATCH_RE = re.compile(r"(?:v=|/watch\?v=)([A-Za-z0-9_-]{6,})")


def parse_yt(url: str) -> tuple[str, str]:
    if not url:
        return "", ""
    m = SHORT_RE.search(url)
    if m:
        return m.group(1), "youtube-short"
    m = WATCH_RE.search(url)
    if m:
        return m.group(1), "youtube-long"
    return "", ""


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--kind", required=True)
    p.add_argument("--path", default="")
    p.add_argument("--url", default="")
    p.add_argument("--out", default="SET.json")
    args = p.parse_args()
    kind = args.kind.strip().lower()
    if kind not in ALLOWED:
        print(f"ingest: unknown kind {kind!r}", file=sys.stderr)
        return 2
    if kind in {"ig-export", "fb-export", "tt-export", "dump"}:
        folder = Path(args.path).expanduser()
        if not folder.is_dir():
            print("ingest: export/dump requires an existing folder (no live scraper)", file=sys.stderr)
            return 2
    if kind == "still":
        f = Path(args.path).expanduser()
        if not f.is_file():
            print("ingest: still requires a file", file=sys.stderr)
            return 2
    vid, detected = parse_yt(args.url)
    if kind.startswith("youtube") and not vid:
        print("ingest: youtube kind needs a watch or shorts URL", file=sys.stderr)
        return 2
    rec = {
        "schema": "agentify-ingest/v0.1",
        "ticket": "IP-WQ-126",
        "kind": kind,
        "url": args.url or None,
        "platform_id": vid or None,
        "path": str(Path(args.path).expanduser()) if args.path else None,
        "detected": detected or None,
        "scraper": False,
        "created": datetime.now(timezone.utc).isoformat(),
    }
    Path(args.out).write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "out": args.out, "kind": kind, "platform_id": rec["platform_id"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
