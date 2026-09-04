# IP-WQ-115 — Tripod repair + flush gate 0

**Status:** OPEN · **Priority:** CRITICAL · **Date:** 2026-09-04

## Why

KEEP_INDEX EIO and a lying Drive flush are why plates are rumors. IP-WQ-082 already named it: Python cannot call Drive. This host still has no `google_drive_upload_artifact`. Keep claiming "saved to Drive" without gate 0 is forbidden.

## Contract (IPQ-078)

One keep is three files, same basename:
- `<slug>_<stamp>.jpg`
- `<slug>_<stamp>.prompt.md`
- `<slug>_<stamp>.keep.json` schema `ipq-078-keep/v1`

Lake = `artifacts/rendered/` + skill-tree `references/visuals/keeps/YYYY/MM/` + Drive folder `1_1xhWdBagAlUi-_g1MaksTE36fewmU1-` **only after gate 0**.

## Acceptance

1. KEEP_INDEX is append-only **jsonl** plus a generated markdown view. Flock or atomic rename. EIO cannot truncate the ledger.
2. `step6_drive_flush.py --gate` exits **0** only if `drive.jpeg_id` AND `drive.prompt_id` AND `drive.keep_id` are all set. Else nonzero.
3. Missing upload tool → exit **2**, print `UPLOAD_TOOL_MISSING`. Never write `drive.status=uploaded`.
4. Agent prose may not say "on Drive" unless gate 0.
5. Child ticket **IP-WQ-122** is the backorder ledger drain.
6. Smoke: dry-run keep with fake ids fails gate; three real ids pass.

## Do not

- Do not treat stream `render_file` as a keep.
- Do not mark queued rows uploaded by hand.
