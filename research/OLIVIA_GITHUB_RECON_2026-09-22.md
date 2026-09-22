# Olivia GitHub recon — 2026-09-22

Goal: attach gift-horses to the EXISTING stack. Do not rebuild. Stage bit by bit so Groq-alive can later spawn extra VPS services without burning Olette/Mei/Cursor tokens.

## Already ours — do not recode
- Live: MCP + Groq on olivia.061583.xyz, Zenoh, RustDesk, Tailscale MagicDNS, Ansible-per-compose, blackboard, nginx page
- Repos: jameswilsonotr-ship-it/Olivia (OLIVIA_PORTAL_BUILD.md), grok-build-cli, kokoro-speaker-cloner.apk, zenoh.apk, sovereign-skills, visuals-mining-git, Groxxporter
- Chosen: Letta memory, Pipecat voice, Open WebUI + LiteLLM, Prometheus/Grafana, Headscale later, K15/Jetson/Pixels

## Compatibility matrix
| Piece | Groq | LiteLLM | Letta | Compose | MagicDNS | Notes |
|---|---|---|---|---|---|---|
| Pipecat | native Whisper/LLM/Orpheus | via OpenAI base URL | sidecar | yes | yes | headset path |
| Open WebUI | via LiteLLM | native | pipe exists | yes | yes | portal chat |
| Aider | official Groq docs | yes | n/a | process | yes | cheapest coder |
| Grok Build CLI | native | yes | n/a | process | yes | we already wrote one |
| harness-dispatch | grok_dispatch MCP | n/a | n/a | MCP server | yes | queue + concurrency cap |
| Delamain | LLM_URL OpenAI-compat | yes | no | yes | yes | PolyForm NC; Comma for events |
| ShayneP/local-voice-ai | swap LLM URL | yes | no | yes | yes | Jetson profile + Kokoro |
| Dockge | n/a | n/a | n/a | yes | yes | files stay on disk |
| Komodo | n/a | n/a | n/a | git deploy | yes | multi-host spawn |

## Gift horses (verified)
1. vonhex/delamain — 4 stars, 2026-06-16, PolyForm Noncommercial, docker-compose, FastAPI+React, LLM_URL OpenAI-compat, F5-TTS. Steal dashboard + proactive silence alerts. Do NOT take sunnypilot/Comma.
2. ShayneP/local-voice-ai — 715 stars MIT, Jetson Orin Nano realtime profile, LiveKit + llama.cpp + Kokoro. Offline collapse.
3. letta-ai/letta-voice — Letta + LiveKit. Keep Letta; voice glue is Pipecat.
4. chrispangg/openwebui-litellm + mhajder/openwebui-stack — compose we want; mhajder already has Grafana.
5. louislam/dockge ~24k stars — file-based compose manager.
6. moghtech/komodo ~12k stars GPL — Git-driven multi-host deploy = swarm spawn later.
7. andrewcooke89/harness-dispatch MIT — MCP dispatch for Grok/Codex/Claude with queue.
8. writeitai/team-harness, berenddeboer/ready-for-agent, chaitanyagiri/munder-difflin — wrap existing CLIs.

## Do not attach now
- OpenClaw / ZeroClaw — replace-the-stack, token furnace
- LangGraph 160-agent office
- VAOS Talker-Reasoner as day-one (needs ~20GB VRAM)
- Full Delamain as product (no Comma, NC license)

## Four staged plans (do not pick one winner)
### A — Prove the door (now)
Keep current MCP/Groq/blackboard/hostname. Add Open WebUI + LiteLLM + Letta as separate compose files behind nginx. Smoke: roses are red. Password=password. Both headset and phone hit same MCP.

### B — See the fleet
Dockge on the VPS so compose files stay on disk (Ansible-friendly). Prometheus + Grafana as their own compose. Komodo only when a second host (K15 or Jetson) is actually on.

### C — Voice attach (after text is green)
Pipecat Groq preset (Whisper + LLM + Orpheus) as its own compose. Phone = official Pipecat Android client, not a custom APK yet. Jetson = ShayneP jetson-realtime + our Kokoro APK as offline fallback. Steal Delamain dashboard events; feed GPS/weather from phone MCP + blackboard.

### D — Swarm without Olette tokens
harness-dispatch MCP in front of grok-build-cli (already ours) and/or Aider pointed at Groq. max_concurrent=1. Groq writes Ansible/compose. Dockge or Komodo applies. New VPS = new periphery, not a new 160-agent roster.

## Token-lean rule
One service per compose. Hostnames only. Receipts on Drive. Dig trio asleep. No chatter between agents. Classifier/heartbeat stays on phone/K15 NPU. Big brain only on change.
