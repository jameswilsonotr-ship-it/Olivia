# Skill patch notes — merge into image-pipeline when bunker is present

Target skill: image-pipeline (agentify is a subscale module, not a top-level skill).
Suggested SKILL.md version after merge: **1.4.0** (Heat-aware work was 1.2.0 / IPQ-077).

## README bullets to add

- Agentify boot order (123).
- Two menus: plate vs serialize (125).
- source.url required on keeps (124).
- Outfit noun. Lane E ≠ intensity e.

## scripts/agentify.py hooks (current Drive file already has)

- `parse_code`, `hop_plan`, `picker_card`, `route`, `plan`, `card`, `set`, `scrape`
- CLI today: route, veto, plan, card, set, scrape
- Missing CLI: boot, menu, registry

## Do not edit YouTube tape for b/c heat. No reverse-c.
