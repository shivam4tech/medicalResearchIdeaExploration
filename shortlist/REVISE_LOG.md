# REVISE LOG — Cycle 6 (2026-08-30) — Methods Half p190 / p268

**Source:** `working/agent_notes/adversarial-reviewer/cycle05_kill_round.md` kill packets p190 (003 T1 plasmode) + p268 (004 T5 corpus)
**Agents:** methods-scout + clinical-evidence-scout
**Date:** 2026-08-30 | **Status:** Both REVISE→KEEP after edits

---

## 003 — T1 3-Process Joint Plasmode DL-vs-Classical — REVISE p190 (methods-scout)

| Field | Entry |
|-------|-------|
| **Verdict** | REVISE→KEEP (not KILL) |
| **Kill packet** | p190 — CIMEHR engine now published (Yang 2026 10.48550/arXiv.2602.15374) — "we propose 3-process spec" is generative novelty claim defeated; CIMEHR provides load-bearing shared random effects engine |
| **Required edits (5)** | (1) Add Yang 2026 CIMEHR 10.48550/arXiv.2602.15374 + CRAN https://cran.r-project.org/web/packages/CIMEHR + GitHub https://github.com/ysph-dsde/CIMEHR as load-bearing engine (Important Papers + Evidence AGAINST, replace 'we propose 3-process spec' with 'we use CIMEHR as engine'); (2) Add CIMEHR vs Liang 2410.13113 sensitivity; (3) Inspect Sun supplement github.com/SCXsunchenxi/ISMTS-Review + Frontiers LMM + CIMEHR vignettes logged verbatim (queries+finding); (4) Keep 16-cell core + Schneider 10.1186/s13040-025-00450-z; (5) State compute via CIMEHR pipeline. Need ≥2 new searches + ≥1 new DOI 302. Append REVISE Addendum 2026-08-30. |
| **Edits applied** | All 5: (1) Important Papers new row 4a CIMEHR (DOI+CRAN+GitHub 302/200 2026-08-30) + row 4b Liang retained as sensitivity; generative spec intro reframed to "we use CIMEHR as engine"; (2) Gate 4 twin-variants updated: primary CIMEHR `simData`+`cimehr()` all 16 cells + Liang 4-cell sensitivity subset (engine fragility, Liu 2504.11740); (3) 3 inspection queries logged (Sun supplement: README datasets no LMM/joint-vs-DL calibration/coverage/DCA table 200; Frontiers FAMS 10.3389/fams.2026.1849703: LMM vs BSM/GEE no DL comparator 2026-07-01 full text; CIMEHR vignette: CRAN 301→200 HTML 169K + GitHub 200 no GRU-D/SeFT head-to-head) + terminal vignette inspect; (4) 16-cell core preserved (γ_v{0,0.8}×sparsity low/high×SNR noisy/clean×N2k/10k=16×200 MC + one-at-a-time γ_o/censoring/D sweeps; Schneider 10.1186/s13040-025-00450-z load-bearing template retained); (5) Gate 4 "Compute via CIMEHR pipeline" + Gate 8 cost via CIMEHR pipeline + GPU (~1–3 sec simData). |
| **New searches (≥2)** | 2026-08-30 T1-REVISE-Sun-supplement (5 hits), T1-REVISE-Frontiers-LMM (5 hits, 1 inspected full text), T1-REVISE-CIMEHR-vignette (5 hits), T1-REVISE-CIMEHR-vignette-inspect (terminal curl) — **4 searches** |
| **New DOI 302 (≥1)** | 10.48550/arXiv.2602.15374 302→arxiv.org/abs/2602.15374 + 10.3389/fams.2026.1849703 (Frontiers) verified + CRAN 301→200 + GitHub 200 — **≥2 DOIs** |
| **Citations added** | Yang 2026 CIMEHR 10.48550/arXiv.2602.15374 + CRAN + GitHub (load-bearing engine); Mashishi 2026 Frontiers 10.3389/fams.2026.1849703 (adjacent no-DL); Liang 2410.13113 retained as sensitivity |
| **Evidence registry** | `literature/search_log.csv` +10 rows (entries 188+: T1/T5 REVISE) + `literature/evidence_registry.csv` 6 rows (T1-C6-001/002/003) — VERIFIED |
| **Gate preservation** | 8 gates preserved — gap type D simulation, Schneider template, twin variants, baselines, decision rule (calibration |slope−1|≤0.1 + coverage 2pp + DCA), scope ceiling |
| **Confidence** | Medium (post-REVISE): benchmark-poor strengthened (T1-KILL2 0 hits + Sun no table + Frontiers no DL + CIMEHR no head-to-head), 16-cell core unchanged, compute via pipeline explicit |
| **Contingency** | If any inspected source later adds GRU-D/SeFT vs LMM/joint on joint criterion across γ_v/γ_o with known truth, pivot to replication/extension of that phase diagram |

---

## 004 — T5 TRIPOD Subgroup-Calibration Corpus Audit n=150 (D literature) — REVISE p268 (methods-scout + clinical-evidence-scout)

| Field | Entry |
|-------|-------|
| **Verdict** | REVISE→KEEP (not KILL) |
| **Kill packet** | p268 — DCGS 2026.06.17.26355900 + KAISEN 10.48550/arXiv.2607.28608 + maltreatment review PMID 41643238 near-equivalents are compliance study-level — gap sharpening required |
| **Required edits (4)** | (1) Add PMID 41643238 + DCGS 2026.06.17.26355900 + KAISEN 10.48550/arXiv.2607.28608 to Important Papers + Evidence AGAINST with rebuttal (compliance study-level vs prevalence with Wilson + interval-aware per subgroup slope CI/plot band per Riley 10.1136/bmj-2024-080749 + masking rate + era split); (2) Run corpus completeness sensitivity count TRIPOD filter vs calibration AND external validation logged verbatim; (3) Foreground interval-aware vs point in Falsifiable Q; (4) Add RECORD/STROBE sensitivity. Need ≥2 searches + ≥1 DOI/PMID 302. Append REVISE Addendum. |
| **Edits applied** | All 4: (1) Important Papers new rows 9–11: Ahmed 2026 Child Abuse Negl PMID 41643238 10.1016/j.chiabu.2026.107923 (study-level compliance vs prevalence+Wilson+interval-aware+masking+era-split 302→linkinghub verified 2026-08-30), DCGS medRxiv 10.64898/2026.06.17.26355900 (single-model Demographic Calibration Gap Score MIMIC-IV 302), KAISEN arXiv 2607.28608 (single-model audit tool 302); Evidence AGAINST updated with full Wilson+interval-aware-per-subgroup+masking+era-split rebuttal + corpus completeness magnitude + interval-aware foregrounded; (2) Eutils counts logged verbatim: TRIPOD[Title/Abstract] AND validation 570 hits vs calibration AND external validation 8188 hits (~7% — language bias quantified) + RECORD calibration 494 + STROBE external validation 18; (3) Gate 3 Falsifiable Q reworded: primary estimand p(interval-aware subgroup calibration) slope CI/plot band per Riley vs secondary p(point) with Wilson±0.06 + masking definition slope 0.8–1.2 intercept±0.3 ICI thresholds + era split χ²/Fisher Newcombe; (4) Gate 4 Locked corpus filter updated with pre-registered RECORD/STROBE sensitivities (494/18 corpora + completeness magnitude + language exploratory). |
| **New searches (≥2)** | 2026-08-30 T5-REVISE-PMID41643238 (5 hits), T5-REVISE-DCGS-KAISEN (5 hits), T5-REVISE-corpus-TRIPOD eutils 570, T5-REVISE-corpus-calib-external eutils 8188, T5-REVISE-RECORD 494, T5-REVISE-STROBE 18 — **6 searches** |
| **New DOI/PMID 302 (≥1)** | PMID 41643238 DOI 10.1016/j.chiabu.2026.107923 302→linkinghub + 10.64898/2026.06.17.26355900 302→medrxiv.org + 10.48550/arXiv.2607.28608 302→arxiv.org + Riley 10.1136/bmj-2024-080749 carry-forward — **≥3 new DOIs** |
| **Citations added** | Ahmed 2026 10.1016/j.chiabu.2026.107923 PMID 41643238; DCGS 10.64898/2026.06.17.26355900; KAISEN 10.48550/arXiv.2607.28608; Riley 10.1136/bmj-2024-080749 anchor for interval-aware |
| **Evidence registry** | search_log +10 rows + evidence_registry 6 rows (T5-C6-001/002/003) — VERIFIED |
| **Gate preservation** | 8 gates preserved — gap type D literature, corpus filter n=150 Wilson±0.06, extraction matrix with interval-aware per subgroup + Van Calster hierarchy + κ≥0.7 + PROBAST, Wilson score (not Wald), still no Indian corpus pivot unless new prevalence audit closes gap |
| **Confidence** | Medium (post-REVISE): MUST web_extract 61k + Hughes masking pattern + interval-aware sharpened (Riley band) + prevalence+Wilson+masking+era-split framing quantified vs study-level compliance |
| **Contingency** | If maltreatment review extended to interval-aware prevalence+Wilson+era-split, pivot to Debray quantitative pooling or Indian-corpus extension (pre-registered) |

---

## Machine-validated counts (Cycle 6 delta)

- search_log: +10 rows (T1-REVISE 4 + T5-REVISE 6), all VERIFIED, ≥2 per dossier
- evidence_registry: +6 rows (T1-C6 3 + T5-C6 3), all VERIFIED, ≥1 new DOI 302 per dossier (003: 10.48550/arXiv.2602.15374; 004: 10.1016/j.chiabu.2026.107923 / 10.64898/2026.06.17.26355900)
- DOIs 302 batch: Harutyunyan, TRIPOD+AI, Sun, Schneider, Franklin, Liang, CIMEHR, Frontiers, maltreatment, DCGS, KAISEN — spot-check verified 2026-08-30
- OSF preregs created: candidate_001_OSF.md (17+5 vars, 2×128 LSTM, 6 leakage items, ricu/METRE/YAIB stub, 27-item TRIPOD+AI, equivalence Δ0.05 slope 0.8–1.2 |α|≤0.3 subgroup ≤0.10, LR/SOFA/GBM/trivial, hashes/seeds) + candidate_002_OSF.md (S1–S5 ladder τ≥0.7 LB≥0.5 DCA 10/20% MIMIC-III→IV 1500 fits pilot)

---

## What was NOT changed (8-gate preserved, not HARKed)

- 003: 16-cell core unchanged; Schneider load-bearing template unchanged; twin variants preserved as sensitivity (now CIMEHR vs Liang engine fragility); decision rule (non-inferior calibration+coverage AND superior DCA) unchanged; scope ceiling preserved (via CIMEHR pipeline clarified).
- 004: Corpus filter (TRIPOD n=150 Wilson±0.06) unchanged — sensitivities added as secondary not replacement; extraction matrix interval-aware already planned, now foregrounded not retrofitted; masking rate definition quantified not changed.
