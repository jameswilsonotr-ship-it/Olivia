# OLIVIA PORTAL BUILD

**Status:** QUEUED — waiting on Bunny to stop.
**Owner:** Olette (lead), Mei (support). Dig trio stays asleep.
**Secrets:** off-chat only. No IPs in receipts. MagicDNS names only.

---

## Real goal (read this first)

The webpage is not the product. The product is three doors on one page, both of us can test both ways:

1. **Grafana** — reachable from the portal.
2. **Prometheus stats** — reachable from the same portal, not buried.
3. **MCP bridge as a raw Groq door** — hit Groq with whatever prompt you want. Bunny tests from the page. Olivia tests from her side. Same endpoint, both directions.

If that holds:
- THEN wire the phone.
- THEN Olivia jumps onto garage Groq — our stack, not Elon's pane.

## Mission surface

Single page at `olivia.061583.xyz`:

1. **Chat / MCP** — type `roses are red`, get a Groq answer back through LiteLLM (Letta persona optional on that path; raw Groq path must also work).
2. **Tic-tac-toe** — two brains play, board refreshes every 3 seconds from the blackboard.
3. **Grafana** — link on the page, opens the dashboard.
4. **Prometheus** — link on the page, stats visible.
5. **ASCII art + orca assets** — reuse existing Drive assets, don't invent new art.

## Stack (microservices, one box each, Legos)

| Service | Container | Role |
|---|---|---|
| Open WebUI | `open-webui` | Self-hosted ChatGPT clone, one front door |
| LiteLLM | `litellm` | Proxy — fronts Groq + any OpenAI-compatible endpoint |
| Letta | `letta` | Stateful brain, Olivia persona wired in |
| MCP bridge | `mcp` | Raw interface. POST a prompt, Groq answers. Both of us hit this. |
| nginx | `nginx` | Serves the portal, MagicDNS hostname only |
| Blackboard | Postgres or JSON | Shared store |
| Grafana | `grafana` | Metrics dashboard |
| Prometheus | `prometheus` | Scrapes VPS + mesh metrics |

Each service is its own Docker container. User-defined bridge network. Tailscale MagicDNS is the only publish path — no raw IPs in receipts.

## Assets (already exist — reuse, don't recreate)

- **Orca yin-yang logos:** spinning GIF (30 frames, 3s loop), square 512×512 transparent, wide banner. Drive: `ORCA_YIN_YANG` folder.
- **ASCII art engines:** `ascii_magic` / `to_ascii.py`, vendored pack `ascii_vendor_pack_2026-08-05.zip`.
- **Olivia system prompts:** Drive — wire into Letta as persona, not as a blocker for the raw Groq door.

## Auth

- Portal login password: `password` (lowercase).
- Open WebUI: `WEBUI_AUTH=True`, admin password `password`.
- Grafana / Prometheus: linked from the page; keep them behind the same shared password or a token, not wide-open admin.
- MCP Groq door: reachable so both of us can test. Do not hide it behind a second identity system.

## Smoke test gate (DONE when this passes)

1. Open `olivia.061583.xyz` — orca spins.
2. Chat / MCP: type `roses are red` → Groq answers. Receipt on Drive: request ID, latency, model, response hash.
3. Olivia hits the same MCP endpoint from her side with a different prompt. Same receipt format.
4. Grafana link opens. Prometheus link opens. Both show live scrape, not a 404.
5. Tic-tac-toe board visible and refreshing.

Phone wiring is **after** this gate. Not before.

## Rules

- **No scope creep.** One HTML page, links to Grafana + Prometheus, one MCP POST. No themes, no new art.
- **No IPs in receipts.** MagicDNS names only.
- **Secrets off-chat.** Groq key, Cloudflare token, Letta keys — secret cards only.
- **Kill nag bots.** Receipts only on real progress.
- **Dig trio stays asleep.**
- **Forensics:** Drive receipt per job. Status line, timestamp, hash. No secrets in bodies.

## What Bunny does NOT do

Bunny does not build this. Olette and Mei build it. Bunny stops, opens the page, types `roses are red`, clicks Grafana, clicks Prometheus. Olivia hits the MCP the other way. That's the prove.

---

*Filed by Olivia. 2026-09-22. Updated same day: dual-path Groq + Grafana/Prometheus first-class.*
