# Vesper alignment items — DEFERRED
**Status**: DEFERRED (not in scope for Olivia/Eureka POC)  
**Date**: 2026-08-12  
**Reason**: Current work is repository structure + research coding surface + dual-SSoT (GitHub Olivia ↔ Drive) + GitHub Actions smoke. Hardware mesh / full agent bus / cluster telemetry are a **future conversation**.

---

## From Vesper’s “Alignment Requirements & Input Specification”

### 1. Repository Layout & Module Structure
| Item | Status |
|------|--------|
| Target directory tree for **initial** repo | **IN SCOPE** — answered by Eureka/Olivia layout (see live repo) |
| Primary build defs (`pyproject.toml`, `Cargo.toml`, Docker Compose) | **DEFERRED** for full stack; POC may add minimal Python reqs later only if research scripts need them |

### 2. Agent Communication Contracts & Interfaces
| Item | Status |
|------|--------|
| Shared schemas (Liv Id, Valerie logic, Rachel logistics) | **DEFERRED** |
| Zenoh mesh topic naming, event routing, payload formats | **DEFERRED** |

### 3. Telemetry & Hardware Target Specifications
| Item | Status |
|------|--------|
| Prometheus / Graphiti / HRV feedback hooks | **DEFERRED** |
| Jetson/G9 cluster, M.2 paths, air-gap simulation flags | **DEFERRED** |

### 4. Execution Scripts & CI/CD Pipeline
| Item | Status |
|------|--------|
| `rehydrate_state.py` / `PEARL_SYNC_V1` | **DEFERRED** |
| Ansible / Docker bootstrap for full system | **DEFERRED** |
| **CI smoke + reusable hygiene on GitHub Olivia** | **IN SCOPE** (already present) |

---

## POC that IS in scope (do not expand into deferred list)

1. Public GitHub **Olivia** structure correct and reviewable  
2. Drive mirror folder dual-SSoT with GitHub for **this coding surface**  
3. `research/` as shared coding root for research skill proof of concept  
4. Reusable workflow pattern (`uses:`) as the single hygiene gate  
5. Comments from Vesper on **that** structure only  

When POC is stable, reopen this file and promote individual deferred rows into real WQ items.

Signed: Olivia Mae Blackwell and her bunny 🐍🐰
