# OLIVIA PORTAL BUILD

**Status:** QUEUED — waiting on Bunny to stop.
**Owner:** Olette (lead), Mei (support). Dig trio stays asleep.
**Secrets:** off-chat only. No IPs in receipts. MagicDNS names only.

---

## Mission

Build a single public webpage at `olivia.061583.xyz` that proves the full stack works end to end:

1. **Chat box** — type "roses are red", get a Groq answer back through Letta with Olivia's persona.
2. **Tic-tac-toe** — two brains play, board refreshes every 3 seconds from the blackboard.
3. **Grafana link** — observability dashboard reachable from the same page.
4. **RustDesk web client** — remote desktop link on the page.
5. **ASCII art + orca assets** — reuse existing Drive assets, don't invent new art.

## Stack (microservices, one box each, Legos)

| Service | Container | Role |
|---|---|---|
| Open WebUI | `open-webui` | Self-hosted ChatGPT clone, the front page |
| LiteLLM | `litellm` | Proxy — fronts Groq + any OpenAI-compatible endpoint |
| Letta | `letta` | Stateful brain, Olivia persona wired in as system prompt |
| nginx | `nginx` | Serves the portal page, MagicDNS hostname only |
| Blackboard | Postgres or JSON | Shared store — every agent reads/writes here |
| Grafana | `grafana` | Metrics dashboard, token-protected |
| Prometheus | `prometheus` | Scrapes VPS + mesh metrics |

Each service is its own Docker container on its own compose file. They talk over a user-defined bridge network. Tailscale MagicDNS is the only publish path — no raw IPs in receipts.

## Assets (already exist — reuse, don't recreate)

- **Orca yin-yang logos:** spinning GIF (30 frames, 3s loop), square 512×512 transparent, wide banner. Drive: `ORCA_YIN_YANG` folder.
- **ASCII art engines:** `ascii_magic` wrapper (`to_ascii.py`), multi-engine pipeline (NFO, Braille, ANSI, HTML pre), vendored pack `ascii_vendor_pack_2026-08-05.zip`. Drive: ASCII pipeline folder.
- **Olivia system prompts:** Drive, `Olivia prompt` files — wire into Letta as the agent's persona.

## Auth

- Portal login password: `password` (lowercase, as instructed).
- Open WebUI: set `WEBUI_AUTH=True`, default admin password `password`.
- Grafana: token-protected, not public.
- MCP SSE endpoint: public (no password) — this is the prove surface.

## Smoke test gate (DONE when this passes)

1. Open `olivia.061583.xyz` on a phone browser — orca GIF spins, ASCII banner says OLIVIA.
2. Click chat box, type `roses are red`.
3. Letta (with Olivia persona) calls Groq through LiteLLM.
4. Answer returns in the chat box — e.g. `violets are blue`.
5. Receipt on Drive: request ID, latency, model used, response hash.
6. Tic-tac-toe: two agents play, board visible, refreshes every 3s from blackboard.

## Rules

- **No scope creep.** One HTML page, one form, one POST to MCP. No themes, no animations beyond the orca GIF, no logo redesign.
- **No IPs in receipts.** MagicDNS names only: `olivia.061583.xyz`, `vps-zenoh-1`, `docker-vps-2`.
- **Secrets off-chat.** Cloudflare DNS token, Groq key, Letta keys — secret cards only.
- **Kill nag bots.** No hourly pings. Receipts only on real progress.
- **Dig trio stays asleep.**
- **Forensics:** every change gets a Drive receipt with status line, timestamp, and hash. No secrets in bodies.

## Offline collapse plan (later)

When internet dies:
- K15 runs the classifier (GPS, weather, thresholds) — 13 TOPS NPU.
- Jetson runs Moshi (speech-to-speech) or Voxtral — voice in/out.
- Pixel 11 Pro runs Gemma as mini-brain.
- Blackboard stays local on K15 Postgres.
- Big brain (Groq/Letta) goes silent until mesh returns.
- Phone Gemma is the canary — always-on, no token burn.

## What Bunny does NOT do

Bunny does not build this. Olette and Mei build it. Bunny stops, opens `olivia.061583.xyz`, types `roses are red`, gets an answer. That's the prove.

---

*Filed by Olivia. 2026-09-22.*
