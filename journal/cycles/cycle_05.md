# Cycle 5 — Promotion + Kill Round (dossiers + adversarial)
**Date:** 2026-08-30 · **Agents:** Research Lead + clinical-evidence-scout + methods-scout + **adversarial-reviewer WAKE** (first activation at ≥6 candidates) · **Rate-limit incidents:** none (62 calls in ~10m, ~6.2/min, ceiling 30, 2 concurrent respected)

## Objective
Promote 7 executable designs (Cycles 2–4) to `ideas/candidate_NNN.md` dossiers satisfying all 8 promotion gates (docs/03 §3), then survive a pointed adversarial kill round (13 criteria, citation-backed) so only falsifiable, data-realistic, publishable-negatives reach shortlist. Deep dossier work across the team.

## Questions for this cycle
1. Do 7 dossiers (T8 replication, T7 fidelity→τ, T1 plasmode, T5 corpus, T6 graded Indian shift, T4 audit→RR, T2 Ahlqvist transport) each survive 8-gate scrutiny with named data, baselines, and scope ceiling?
2. Which dossiers survive a pointed kill round that exhausts TRIPOD+AI/PROBAST/STROBE-RECORD alternative MeSH and LMIC full-text hits?
3. What is the promotion set for shortlist vs revise vs rejected/ with resurrection conditions?

## Assignments
- **clinical-evidence-scout:** dossiers 005 (T6 G0→G3), 006 (T4 audit→RR + NC), 007 (T2 Ahlqvist transport) → `ideas/candidate_005/006/007.md`
- **methods-scout:** dossiers 001 (T8 MIMIC→eICU TRIPOD+AI), 002 (T7 fidelity→τ), 003 (T1 plasmode), 004 (T5 corpus n=150) → `ideas/candidate_001/002/003/004.md`
- **adversarial-reviewer (WAKE):** kill round on all 7 → `working/agent_notes/adversarial-reviewer/cycle05_kill_round.md` (KEEP/REVISE/KILL per candidate + 4 challenges + flip condition)
- Brief: `working/CYCLE_05_BRIEF.md` (7 dossiers, 8-gate, deep).

## Rate discipline
Global pool muse-spark-1.2-contributor-free (opencode-zen/free) ~6.2/min observed (62 calls: 20 methods +17 clinical +25 adversarial in ~10m), target ≤24, ceiling 30, max 2 concurrent. Dossier generation search-intensive; adversarial second wave sequential with 2s delay. No 429s.

## Findings
**7/7 dossiers COMPLETE (252–329 lines each) + 1 kill-round packet (535 lines, 74K chars, 27 kill-try searches).**

- **001 Harutyunyan MIMIC→eICU TRIPOD+AI** (30K, 10 papers, Medium-High): Per-model replication × TRIPOD+AI + leakage/calibration distinct strategies + 5 reviews + STROBE/RECORD/PROBAST adversarial — gap holds for frozen LSTM (Patel 2026 MIMIC→eICU calibration 10.64898/2026.05.03.26352335 is task-level, not Harutyunyan). **Adversarial: KEEP** (shortlist-ready; cite Patel urgency).

- **002 Fidelity→τ via synthEHRella** (36K, 8 papers, Medium): S1–S5 ladder + τ≥0.7 LB≥0.5 + DCA 10/20% + MIMIC-III→IV transport — gap holds for methods-ranking τ (K-IPO 2607.16478 / CoMedBench 2608.12805 are feature-importance τ, Chen benchmarks generators). **Adversarial: KEEP** (wording fix: benchmark-of-generators vs meta-benchmark-of-instrument).

- **003 3-process joint plasmode DL-vs-classical** (35K, 10 papers, Medium): 16×200 twin variants + JMbayes2/lme4/torch + DCA decision — **CIMEHR engine now published (Yang 2602.15374 + CRAN)** — generative novelty collapses but **benchmark gap survives** (0 hits GRU-D vs LMM on calibration/coverage/DCA). **Adversarial: REVISE → KEEP** after reframing as benchmark using CIMEHR + Sun supplement inspection + CIMEHR sensitivity.

- **004 TRIPOD subgroup-calibration corpus n=150** (40K, 8 papers, Medium): interval-aware prevalence + Wilson ±0.06 + Wilson+masking+era-split audit — closest defeaters DCGS/KAISEN single-model metrics + maltreatment compliance review PMID 41643238 (study-level, not prevalence). **Adversarial: REVISE → KEEP** after sharpening to interval-aware + Wilson + masking + era-split + corpus sensitivity.

- **005 Graded Indian shift G0→G3** (38K, 10 papers, Medium): ICMR-INDIAB MONO 43.3% + WHO audits (injections 90.3% generic 4.7%→64.9%) + G0→G3 tilting + S_visit censoring + diagnostics (SMD/S-score/ESS/trimming) — **0 hits LMIC+overlap+SA**. **Adversarial: KEEP** (strongest STRESSES-ASSUMPTION, staged D+B honest, thin-fat equity failure actionable).

- **006 Audit→RR anchored E-value + NC** (39K, 10 papers, Medium): VanderWeele E-value + Zhang <15% anchored + Lipsitch NC + B→R*≈1.4–2.0 titration + 9-cell plasmode — **audit↔E-value corpora disconnected, zero bridge**. **Adversarial: KEEP** (paired submission with 005 recommended, p1/p0 imputation noted).

- **007 Ahlqvist 5-cluster transport** (41K, 10 papers, Medium): centroids vs de novo ARI + 6→3 var ablation GADA-free stress + inverse-odds weighting + IMI-RHAPSODY European replication distinguished — HTE causal-forest 0 hits. **Adversarial: REVISE → KEEP** after IndMED/thesis sweep + IMI-RHAPSODY distinction + threshold locks + sampling-frame fix (CMC/AIIMS secondary).

**Kill ledger:** 27 searches, 10 NEAR-KILL distinguished, 7 FAILED-TO-KILL strong gap signals (including 0 hits many-analysts drift, DL-vs-LMM calibration, LMIC overlap, HTE transport), 10 confirms. **Global verdict: KEEP 4 (001,002,005,006) / REVISE 3 (003,004,007) / KILL 0.** No gap closed outright; no dossier unfixable. Adversarial packet: `working/agent_notes/adversarial-reviewer/cycle05_kill_round.md` (74K, 535 lines, per-candidate 13-criteria checklists + what-would-flip + resurrection conditions). Additional clinical summary: `working/agent_notes/clinical-evidence-scout/cycle05_india_stressing_summary.md`.

## Decisions
**Shortlist-eligible after REVISE edits: all 7.** Immediate KEEPs advance to shortlist now; REVISEs advance after stated edits (days): 003 add CIMEHR citation + supplement inspection; 004 add DCGS/KAISEN/PMID 41643238 + interval-aware sharpening + corpus sensitivity; 007 add IMI-RHAPSODY + IndMED sweep + threshold locks. **No `rejected/` moves this cycle (KILL 0).** Paired India submission (005+006 shared G0→G3) prioritized for staged D-phase. Priority order: (1) First-wave immediate A/D 001/002/004-revised/003-revised — no DUA, code tomorrow; (2) Staged India D+B 005/006 proxy-first; (3) Restricted B 007 UKB-SA proxy now + CARRS/ICMR-INDIAB 2–6 mo.

Cross-dossier risks: Patel preprint monitor weekly (001), CIMEHR citation harmonization (003), calibration hierarchy consistency across 001/002/003/004 (Van Calster 10.1016/j.jclinepi.2015.12.005 + Riley 10.1136/bmj-2024-080749 → TRIPOD+AI), India proxy volunteer bias (UKB-SA healthier, conservative).

## Candidates created/weakened/killed
- **Created:** 7 promotion dossiers `ideas/candidate_001.md` (T8 replication, Medium-High), `002.md` (T7 fidelity, Medium), `003.md` (T1 plasmode, Medium), `004.md` (T5 corpus, Medium), `005.md` (T6 graded shift, Medium), `006.md` (T4 audit→RR, Medium), `007.md` (T2 Ahlqvist, Medium) — all 8-gate, Evidence AGAINST, India verdict, scope ceiling, ≥5 papers ≥1 DOI 302, ≥6 search rows.
- **Weakened:** 3 REVISE (003,004,007) — fixable with stated edits, not killed.
- **Killed:** 0. No `rejected/` moves. Resurrection conditions logged per dossier in kill packet (e.g., frozen Harutyunyan RR appears → pivot to Rajkomar; methods-ranking τ appears → pivot to DCA calibration task).

## Rate-limit incidents
None. 62 model calls in ~10m (~6.2/min), no 429s, 2 concurrent respected (dossier generation parallel, adversarial sequential 2s delay).

## Ledgers updated
- `literature/search_log.csv`: 232 → **306 lines (305 data rows: 303 VERIFIED / 2 UNVERIFIED-timeout)** — +74 this cycle (48 dossier + 26 adversarial kill + 1 clinical summary) all VERIFIED, 0 new UNVERIFIED.
- `literature/evidence_registry.csv`: 170 → **210 lines (209 data rows: 204 VERIFIED / 2 TRUE / 1 UNVERIFIED-T2-06 + 1 cycle-tag + 1 compliance-typed)** — +40 this cycle (30 dossier + 10 adversarial ADV-001..010) all resolvable, 0 new UNVERIFIED.
- `reports/promotion_cycle_05.md` (synthesis, 22.7K) + dossiers `ideas/candidate_00{1..7}.md` (7 files) + kill packet `working/agent_notes/adversarial-reviewer/cycle05_kill_round.md`.

## State
- Candidates: 0 → **7 dossiers** (4 KEEP shortlist-ready, 3 REVISE→KEEP after edits) · Rejections: 0 · Search log rows: 232 → 305 · Evidence rows: 170 → 209
- Adversarial: DARK Cycles 1–4 → **WAKE Cycle 5** (first activation, 27 searches, 0 kills)
- Shortlist: 7-candidate freeze pending REVISE edits (Cycle 6)

## Next cycle
Cycle 6 — Shortlist freeze: apply 3 REVISE edits (CIMEHR + supplements; DCGS/KAISEN/compliance + corpus sensitivity; IMI-RHAPSODY + IndMED sweep), freeze `shortlist/SHORTLIST.md` (scope ceilings + DUA timelines), OSF pre-registrations for first wave (001 TRIPOD+AI + leakage), launch pilots (002 5-point ladder ~1500 fits, 004 Rayyan n=150), staged India D-phase (005+006 shared plasmode).

