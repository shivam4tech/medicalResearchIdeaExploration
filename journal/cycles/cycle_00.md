# Cycle 0 — Infrastructure

**Date:** 2026-08-30 · **Agents:** Research Lead only (no scouting) · **Rate-limit incidents:** none

## Objective
Stand up everything needed to run disciplined multi-agent research: Git/hygiene, bot
definitions, schemas, ledgers, journal, scoring scaffold.

## Actions completed
1. **Git.** Confirmed `/home/shivam/Projects/medicalResearch` is a Git repo on `main`
   (no commits yet). `origin` already `git@github.com:shivam4tech/medicalResearchIdeaExploration.git`.
   SSH verified: `git ls-remote origin` exit 0 (empty remote — acceptably new/non-conflicting).
   No force operations; nothing to force.
2. **Repository hygiene.** `.gitignore` already covers secrets (`.env`, `*.pem`, `*.key`,
   `id_rsa*`, tokens), Hermes internals, and patient-data paths (`data/private/`,
   `data/raw_private/`, `data/phi/`, `**/patient_data/`, raw clinical exports). Left as-is;
   sufficient for the exploration phase. No patient data present (verified: only markdown/csv/py).
3. **Docs.** `docs/01_project_understanding.md` (charter, pre-existing), `02_research_protocol.md`
   (cycles/governance/rate-limit policy + rubric), `03_evidence_standards.md` (gap bar,
   packet format, verdicts, India test), `04_physician_intake_questions.md` — all present and complete.
4. **Specialist bots (3, persistent Hermes profiles).** Created via `hermes profile create`:
   `clinical-evidence-scout`, `methods-scout`, `adversarial-reviewer`. Verified they inherit the
   SAME model config as the Lead (`moonshotai/kimi-k3`, provider `nvidia`, same base_url),
   so all draw from one shared quota pool. Role specs written to `bots/*.md`.
   - NOTE: SOUL.md role prompts for the three profiles were NOT written (protected agent-instruction
     files; approval timed out). Deferred — the `bots/*.md` specs are the project-canonical
     form and are committed. Optional follow-up with user consent.
5. **Schemas / ledgers.** `literature/search_log.csv`, `literature/evidence_registry.csv`,
   `reports/candidate_matrix.csv` created with headers. Candidate template + evidence-packet
   + verdict formats live in `docs/03_evidence_standards.md`.
6. **Scaffold dirs.** `reports/figures/`, `scripts/`, `working/agent_notes/{3 bots}/`,
   `literature/topics/`, `journal/cycles/`.
7. **Chart script.** `scripts/generate_research_charts.py` (reads candidate_matrix.csv →
   novelty-vs-feasibility scatter + per-candidate score bars; matplotlib optional, graceful when absent).

## Open / deferred
- SOUL.md customisation for the three worker profiles (needs user consent; non-blocking).
- Adversarial Reviewer activation — correctly dark until ≥6 candidates exist.

## State
- Candidates: 0 · Rejections: 0 · Search log rows: 0
- Git: initial commit + push (this cycle's close-out).