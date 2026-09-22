# Gift-horse compare — 2026-09-22

Constraint: attach, do not rebuild. Existing stack stays: MCP+Groq, Zenoh, RustDesk, Tailscale/MagicDNS, Ansible-per-compose, blackboard, olivia.061583.xyz.

## Already ours (do not recode)
- jameswilsonotr-ship-it/Olivia — portal brief already here
- grok-build-cli — sovereign 7-phase orchestrator stub
- kokoro-speaker-cloner.apk — Android clone pipeline started
- zenoh.apk — mesh experiment
- sovereign-skills, visuals-mining-git

## Compatible attach list

| Piece | Repo | Why attach | Why not replace stack |
|---|---|---|---|
| Truck dashboard ideas | vonhex/delamain (4★, PolyForm NC) | proactive silence, telemetry, phrase cache, OpenAI-compat LLM_URL | Comma/sunnypilot tied; NC license; tiny |
| Jetson offline voice | ShayneP/local-voice-ai (MIT, Jetson profile) | Kokoro + llama.cpp + LiveKit, compose, maps to our Kokoro APK | LiveKit not Pipecat; attach later not now |
| Groq voice MCP | glebis/pipecat-mcp-server | Groq Whisper+Orpheus default | audio still needs a transport |
| Official Groq MCP | groq/groq-mcp-server | chat/STT/TTS/vision tools | not a portal |
| Pipecat+Groq example | daily-co/pcc-groq-llama | STT+LLM+TTS all Groq | example only |
| Memory harness | letta-ai/letta-code | persistent agent, model-agnostic, Groq via OpenAI-compat | do not also run LangGraph |
| Cheap coder | Aider | OPENAI_API_BASE=https://api.groq.com/openai/v1 | not a swarm |
| Official coder | Grok Build (`grok -p`) | headless, ACP, MCP, custom models | still xAI auth unless custom model points at Groq |
| Heavy coder | OpenHands / Agent Canvas | Docker sandbox | heavier than we need first |
| Fleet UI light | louislam/dockge | edits compose on disk | single-host |
| Fleet UI multi | moghtech/komodo ~12k | GitOps stacks + periphery per host | wait until 2nd host |
| Portal pattern | openwebui + litellm compose examples | already our plan | no single Letta+OWUI+LiteLLM monorepo |

## Do not attach now
- OpenClaw / girlfriend-monsters — replace-the-stack
- LangGraph as control plane — fragments offline
- 160-agent swarms — token burn
- Fish/CosyVoice cloning until a rented GPU or Jetson is on

## 4 staged plans
A Prove door — current MCP/Groq/blackboard/hostname + OWUI/LiteLLM/Letta compose. Smoke: roses are red.
B See the fleet — Dockge + Prometheus/Grafana extra compose. Komodo only on host #2.
C Voice attach — Pipecat Groq preset on VPS; ShayneP jetson-realtime later; steal Delamain events not repo.
D Swarm without Olette — Groq-backed Aider or `grok -p` or Letta Code writes Ansible; Dockge/Komodo applies; max_concurrent=1.

## Compatibility rule
Every new service = its own compose + Ansible + MagicDNS name. Groq is the cheap brain until steel is on. Blackboard (Postgres/JSON) not LangGraph.
