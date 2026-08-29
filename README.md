# Medical Research Idea Exploration

An independent **clinical–computational methods research programme**: discovering and
adversarially verifying research gaps at the intersection of mathematical/computational
methods and clinical data, with attention to transportability of Western-derived methods
to Indian clinical populations.

**This is a methods-research project, not a medical app.** See `IDEA.md` (founding
document) and `docs/01_project_understanding.md` (charter).

## Structure

| Path | Purpose |
|---|---|
| `IDEA.md` | Foundational document — read first |
| `docs/` | Charter, protocol, evidence standards |
| `bots/` | Role specifications for the three specialist research bots |
| `journal/` | Chronological lab notebook (`research_log.md`, `cycles/`) |
| `literature/` | Search logs, evidence registry, topic notes |
| `ideas/` | Candidate research projects (strict template) |
| `rejected/` | Documented rejections — rejection reasons are data |
| `decisions/` | ADR-style decision records |
| `reports/` | Living landscape report, candidate matrix, figures |
| `working/agent_notes/` | Scratch space for specialist bots |
| `scripts/` | Reproducible chart generation |

## Rules of the house

1. **No patient data in this repo.** Ever. See `.gitignore`. Real clinical-data use is a
   separate governance decision for a later stage.
2. **No invented citations.** Every claim carries a resolvable identifier or is marked
   `[UNVERIFIED]`.
3. **Adversarial by design.** Ideas are promoted only after surviving a structured kill
   attempt. Rejected ideas are preserved, not deleted.
4. **Sole Git authority:** the Research Lead. Bots never commit or push.

## Rate-limit policy

Global shared pool ≈ 40 req/min (Kimi). Operating target ≤24/min, ceiling 30,
max 2 model-intensive bots concurrently. See `docs/02_research_protocol.md` §6.
