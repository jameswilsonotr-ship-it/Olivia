# IP-WQ-122 — Serialization backorder drain

**Status:** OPEN · **Parent:** IP-WQ-115 · **Date:** 2026-09-04

This is the named queue the user asked for.

## Cohorts (audit 2026-09-04)

1. KEEP_INDEX 2026-08-28: 15 queued + 6 polish uploaded.
2. KEEP_INDEX 2026-08-29: 6 Crepax queued.
3. Jpeg-only orphans already in Drive keep folder (NCO khaki, some Agentify parents).
4. Local-only last-night set: skater I-1-cde, I-2-cde, I-E; bunny-phg A/C; PHG bunker plates. Not in Drive.

## Acceptance

- One ledger row per `keep.json` with `drive.status != uploaded` OR jpeg on Drive without prompt+keep.
- Each row tagged: `flush` | `orphan-repair` | `local-only` | `skip`.
- Drain does not invent file ids.
- Last-night Agentify set is the first `local-only` cohort — flush when upload tool returns, not before.
