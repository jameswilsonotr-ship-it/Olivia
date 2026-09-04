# IP-WQ-123 — Agentify conversation boot

**Status:** OPEN
**Date:** 2026-09-04 10:58 EDT
**Priority:** critical
**Parent:** IP-WQ-094 / 118 / 128
**Owner:** agentify

## Done when

Any conversation that hits an Agentify trigger becomes coherent without babysitting.

## Trigger

`agentify` / `make an agent` / `menu b` / a roman+code (`I1cde`, `II BCD`) / `boot`.

## Resolution order (do not skip)

1. YouTube Short or watch URL in **this** message.
2. Else last `source.url` on the active registry row.
3. Else `menus/PLATE_BACKLOG.md` (what is not generated).
4. Else `menus/SERIALIZE_BACKLOG.md` (what exists locally and is not a Drive triple).
5. Else ask one question: plate or serialize. Never a wall.

## CLI contract (to wire into scripts/agentify.py)

```
python3 agentify.py boot [--text MSG] [--url URL]
python3 agentify.py menu plate
python3 agentify.py menu serialize
python3 agentify.py menu short --id YT_ID
```

`boot` prints: source, character id, next open token, picker card (118).
Does not plate unless the message also contains a plate code.

## Non-goals

- Not a live YouTube scraper of trending Shorts.
- Not a new engine. Still menu B under image-pipeline.
