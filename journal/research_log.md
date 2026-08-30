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

## 2026-08-30 — Cycle 2 (Deepening: Failure Points)
5 deepening packets (clinical: T6 positivity diagnostics, T4 prescribing audit; methods: T1 plasmode design, T5 corpus pilot, T7 threshold pilot) → `working/agent_notes/cycle02_*.md`, 118 queries (116 VERIFIED/2 UNVERIFIED), 94 evidence (93 VERIFIED/1 UNVERIFIED). Designs delivered: T6 graded-shift plasmode + 5-diagnostic reporting set (SMD 10.1002/sim.3697, Li 10.1080/01621459.2018.1448823, Inoue 10.1016/j.annepidem.2025.03.001); T4 audit-anchored E-value + NC panel (VanderWeele 10.7326/M16-2607, Lipsitch 10.1097/EDE.0b013e3181d61eeb, WHO audits 10.18203/2394-6040.ijcmph20233814 + polypill 10.5334/gh.1335); T1 3-process joint plasmode with 16-cell core + decision rule (Sun 10.34133/hds.0456, Schneider 10.1186/s13040-025-00450-z, Liang 10.48550/arXiv.2410.13113); T5 TRIPOD corpus + pilot (Hughes 10.1007/s10067-025-07325-y, 10.1186/s41512-026-00218-x) GO for n=150; T7 synthEHRella threshold pilot (Chen 10.1093/jamia/ocaf082, Liu 10.48550/arXiv.2504.11740). All GEOGRAPHY-ONLY except T6/T4 STRESSES-ASSUMPTION. Refined seeds unchanged; 6 designs ready for promotion, gate requires Lead next-searches + adversarial activation. Synthesis: `reports/failure_points_cycle_02.md`. Full detail: `journal/cycles/cycle_02.md`. Next: Cycle 3 — India/transportability opportunities.