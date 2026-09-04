# IP-WQ-127 — Transcript → persona pack

**Status:** OPEN
**Date:** 2026-09-04 10:58 EDT
**Priority:** medium
**Parent:** IP-WQ-080 / 081

## Rule

If a source has speech, attach `verbal/<id>.persona.json` next to the registry row.
Flag `caption_source: auto | human | missing`.
Compilations (Sirens-style overlay text, no speaker) = `missing`. Do not invent a voice.

## Blocker

IP-WQ-081 cookies.txt. Track-2 YT inbound stays blocked without it.

## Done when

Boot prints persona-present or persona-missing. Never a fake bio for a compilation mouth.
