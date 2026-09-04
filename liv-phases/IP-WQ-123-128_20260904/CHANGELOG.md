# Changelog — image-pipeline / agentify surface (Olivia publish)

Versioning convention: skill-tree uses semver on SKILL.md frontmatter when the bunker is present.
This file is the **publish-side** log for hops that cannot touch `/home/workdir/.grok/skills/`.

## [1.4.0-olivia-publish] — 2026-09-04

### Added
- IP-WQ-123 conversation boot contract (`agentify boot`).
- IP-WQ-124 `source.url` required on keep.json + same-turn tripartite rule.
- IP-WQ-125 two-tier menus: plate backlog vs serialize backlog; per-short trees.
- IP-WQ-126 inbound source classes (short, long-form, still, IG/FB/TT export).
- IP-WQ-127 transcript → persona pack (auto-caption flagged; compilations often have none).
- IP-WQ-128 `registry/characters.json` seed (Bunny + compilation I–VIII + Park Mouse).

### Changed
- 115–122 statuses promoted honestly (PARTIAL / IN_PROGRESS / OPEN). None falsely DONE.
- Noun in heat grammar remains **outfit**, never dress.

### Known gaps
- Live `scripts/agentify.py` on Drive does not yet have `boot` / `menu` / `registry` subcommands.
- Drive connector for binary keeps is missing on this host.
- Frozen Drive WORK_QUEUE.md dated 2026-08-29 is stale vs 115+.

### Prior live code (already on Drive agentify.py 2026-09-04)
- `parse_code`, `hop_plan`, `picker_card`, INTENSITY c/d/e, LANES A–E.
