---
title: Persistence contract C
updated: 2026-08-25
claim: Absolute Liv HUB
---

# Persistence C — Drive publish, Git history

Locked 2026-08-25.

| Plane | Role | What lives there |
|-------|------|------------------|
| **Git** (`jameswilsonotr-ship-it/Olivia`, branch/tag `wq038-hygiene-2026-08-25`) | History, diffs, Actions | Scripts, schema, MANIFEST, NORMALIZED, receipts, CURRENT prompt pointer |
| **Drive** `Liv-HUB / Work-Queues / YYYY-MM-DD_full` | Publish target Vesper can see | Zips + MANIFEST.md + NORMALIZED.md |
| **Drive** `Liv-HUB / Work-Queues / _receipts` | Audit | PUBLISH_RECEIPT_*.md with Drive file IDs |
| **Preview / published app** | Exposed face | Hygiene Console; not SSOT |

## Restore
1. Clone/checkout the Git branch for code.
2. Pull the matching Drive `YYYY-MM-DD_full` zip if the blob is needed.
3. Run `python3 skill-orchestrator/scripts/wq_hygiene.py --export-app`.

Do **not** mint another `work_queues` folder. Canonical Drive path is `Liv-HUB / Work-Queues /` only.
