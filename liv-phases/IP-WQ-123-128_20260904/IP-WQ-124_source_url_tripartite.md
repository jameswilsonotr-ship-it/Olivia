# IP-WQ-124 — source.url on every keep + same-turn triple

**Status:** OPEN
**Date:** 2026-09-04 10:58 EDT
**Priority:** critical
**Parent:** IPQ-078 / IP-WQ-115 / 122

## Rule

No emit without a source URL (or explicit `source.kind=still` + inbound path).

Every keep.json MUST contain:

```json
"source": {
  "kind": "youtube-short | youtube-long | still | ig-export | fb-export | tt-export | dump",
  "url": "https://youtube.com/shorts/ID",
  "platform_id": "_CLrJZSn3Og"
}
```

Same turn: write `.jpg` + `.prompt.md` + `.keep.json` same basename.
Do not say "on Drive" unless jpeg_id AND prompt_id AND keep_id are set (115 / 122).

## Named bug

Lane `E` vs intensity `e` collide in slugs. Stamp must include `lane-E` or `inten-e`.

## Done when

keep_path refuses to write a keep missing source.url (still-only rows use inbound path as url).
