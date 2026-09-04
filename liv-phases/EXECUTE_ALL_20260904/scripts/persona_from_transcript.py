#!/usr/bin/env python3
"""IP-WQ-127 — attach persona pack or mark missing. Never invent a voice.

Usage:
  python3 persona_from_transcript.py --id _CLrJZSn3Og --kind compilation
  python3 persona_from_transcript.py --id tswoGPiNAV8 --transcript captions.vtt
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--id", required=True)
    p.add_argument("--kind", default="youtube-short")
    p.add_argument("--transcript", default="")
    p.add_argument("--out", default="")
    args = p.parse_args()
    out = Path(args.out or f"verbal/{args.id}.persona.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    text = ""
    caption_source = "missing"
    if args.transcript:
        tpath = Path(args.transcript)
        if tpath.is_file():
            text = tpath.read_text(encoding="utf-8", errors="replace")[:8000]
            caption_source = "human" if tpath.suffix.lower() in {".txt", ".md"} else "auto"
    if args.kind == "compilation" or not text.strip():
        rec = {
            "schema": "agentify-persona/v0.1",
            "ticket": "IP-WQ-127",
            "id": args.id,
            "available": False,
            "caption_source": "missing" if args.kind == "compilation" else caption_source,
            "reason": "compilation overlay / no speaker" if args.kind == "compilation" else "no transcript file",
            "do_not_invent": True,
            "updated": datetime.now(timezone.utc).isoformat(),
        }
    else:
        rec = {
            "schema": "agentify-persona/v0.1",
            "ticket": "IP-WQ-127",
            "id": args.id,
            "available": True,
            "caption_source": caption_source,
            "excerpt": text[:1200],
            "do_not_invent": True,
            "updated": datetime.now(timezone.utc).isoformat(),
        }
    out.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "out": str(out), "available": rec["available"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
