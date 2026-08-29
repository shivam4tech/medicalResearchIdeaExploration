# Research Log — append-only chronological summary

## 2026-08-28 — Foundation (Stage 1)
Read `IDEA.md`; scaffolded workspace; wrote `docs/01_project_understanding.md` (charter,
territories T1–T8, acceptance gate, record-keeping, multi-agent plan). No literature
review / topic selection / specialist bots at that stage (per directive).

## 2026-08-29 — Protocol & evidence standards
Wrote `docs/02_research_protocol.md`, `docs/03_evidence_standards.md`,
`docs/04_physician_intake_questions.md`.

## 2026-08-30 — Cycle 0 (Infrastructure)
Git verified (SSH `origin` OK, empty remote, `main`). Hygiene intact. Created three
persistent specialist profiles (`clinical-evidence-scout`, `methods-scout`,
`adversarial-reviewer`) sharing the Lead's Kimi model/quota. Roles documented in
`bots/*.md`. Ledgers (`search_log.csv`, `evidence_registry.csv`, `candidate_matrix.csv`)
and scaffold dirs in place. Chart script in `scripts/`. SOUL.md customisation deferred
(needs consent). Full detail: `journal/cycles/cycle_00.md`.

**Next cycle (Cycle 1 — Landscape):** deploy `clinical-evidence-scout` and
`methods-scout` on complementary bounded assignments (max 2 model-intensive bots
concurrently; adversarial reviewer stays dark).