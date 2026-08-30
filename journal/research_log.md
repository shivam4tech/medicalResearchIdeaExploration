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

## 2026-08-30 — Cycle 1 (Landscape)
7 territories mapped by 2 scouts (clinical: T2/T4/T6; methods: T1/T5/T7/T8) — 7 packets (`working/agent_notes/*/`), 54 queries verbatim to `literature/search_log.csv` (52 VERIFIED / 2 UNVERIFIED-timeout), 49 papers to `literature/evidence_registry.csv` (48 VERIFIED / 1 UNVERIFIED correctly flagged T2-06). Spot-check 8 load-bearing DOIs 302 VERIFIED. All Medium confidence (terminology fragmentation + grey lit + 2024-25 preprints). 8 candidate seeds ranked for Cycle 2: T8-direct-replication (1, highest feasibility, public MIMIC→eICU), T7-instrument-validity, T1-irregularity benchmark, T5-aggregate-masking audit, T6-transportability-vs-recalibration, T4-emulation-falsification, T2-falsifiable-heterogeneity, T6/T2 India extension Stage-2. No candidates promoted yet (gate requires adversarial + named data + falsifiable negative). Synthesis: `reports/landscape_cycle_01.md`. Full detail: `journal/cycles/cycle_01.md`. Next: Cycle 2 — Methodological failure points (T1/T5/T7 pilots + T6/T4 assumption stress).