# Cycle 7 — Pilot Execution (prove first wave runs)
Companion: docs/01..03, working/CYCLE_01..06_BRIEF.md, reports/shortlist_cycle_06.md, shortlist/SHORTLIST.md + REVISE_LOG.md, osf_prereg/*, ideas/candidate_*.md ×7 (all KEEP frozen), literature ledgers 320/217. Adversarial MONITOR.

Cycle 7 asks: EXECUTE small-scale pilots (code + data) that prove Tier 1 (no-DUA) and Tier 2 D-phase are runnable tomorrow on public/synthetic/literature data — so OSF pre-registrations can be timestamped with a working pipeline, not just a spec.

## Binding constraints (same pool)
- Global pool muse-spark-1.2-contributor-free ~40/min, target ≤24, ceiling 30, max 2 concurrent model-intensive bots. Active chat shares pool — respect cap.
- Pilots use ONLY public/synthetic/literature data: MIMIC-III demo (mimic-iii-demo on PhysioNet OR local mimic-iii-demo if credentialed, else synthetic rnorm fallback), synthEHRella (chenxran/synthEHRella open), CIMEHR CRAN simulator (fully synthetic mode), PubMed E-utilities + Europe PMC for corpus (no PHI). No restricted DUA required for Tier 1 D-phase; UKB-SA/CARRS DUAs remain staged.
- Every pilot must produce runnable code + execution log + pilot output table/figure + verification (unit test / checksum / kappa / calibration plot stub) — not just description. Checkpoint early.
- Write pilots to pilots/<candidate>/ with README + code + logs + outputs.

## Assignments this cycle (2 scouts, execution)

### methods-scout → 2 pilots (compute)
1. **pilot_002_synthEHRella_ladder** (002 A/D, synthEHRella S1–S5 + τ≥0.7): Clone synthEHRella (chenxran/synthEHRella), install deps, run inventory: `python run_preprocessing.py --help`, `python run_generation.py --help`, `evaluation/fidelity.py` + `evaluation/utility.py` on **tiny pilot** (MIMIC-III demo OR synthetic tabular fallback if no credential): generate S1 plasmode (bootstrap resample) vs S5 prevalence-random (trivial) 2-point pilot, compute MMD/correlation recovery/TSTR gap for 1 fidelity point, run logistic vs GRU-D (or logistic vs tree as GRU-D proxy if GPU not available) on synthetic-TRAIN vs real-TRAIN evaluated on held-out TEST_R, compute Kendall τ + Spearman + DCA stub at 10/20% thresholds. Deliver `pilots/candidate_002/README.md` + `run_pilot_002.sh` + `logs/pilot_002.log` + `outputs/pilot_002_fidelity_tau.csv` + calibration plot stub. Log any synthetic fallback honestly. 5-10 papers not needed — 2-3 new searches for synthEHRella API/tools if needed, logged verbatim.
2. **pilot_003_cimehr_plasmode** (003 D sim, CIMEHR engine): Install CIMEHR `install.packages(\"CIMEHR\")` + vignette `vignette(\"getting-started\")`, run simulator dry-run: N=200–500, 2 cells (low γ_v=0 vs high γ_v=0.8) × 20 reps, shared frailty b_i, visit+observation+longitudinal + outcome, fit LMM (lme4) vs GRU-D stub (torch or logistic proxy if GPU not available), compute AUC + calibration slope/intercept + coverage + DCA net benefit per cell, twin variant Generate-Treatment vs Generate-Outcome comparison. Deliver `pilots/candidate_003/README.md` + `run_pilot_003.R` + `logs/pilot_003.log` + `outputs/pilot_003_cell_calibration.csv` + decision rule stub (non-inferior calibration/coverage AND superior DCA). Log any R/Python dep install. Verify CIMEHR version 0.1.0 2026-06-08 via CRAN.

### clinical-evidence-scout → 2 pilots (literature + plasmode clinical framing)
3. **pilot_004_rayyan_corpus** (004 D lit, n=150 audit): Build PubMed E-utilities corpus: query `TRIPOD[Title/Abstract] AND validation[Title/Abstract]` (expect 570 hits), fetch 20-sample via `esearch`+`efetch`, deduplicate, random sample n=20 pilot (of 150 target), define extraction form CSV (interval-aware vs point: slope CI/plot band per Riley + TRIPOD+AI era split), dual-extraction pilot on n=5 overlap (simulate 2 reviewers with adjudication note), compute κ stub + Wilson CI stub for p(interval-aware subgroup calibration) with masking rate, generate PRISMA pilot flow. Deliver `pilots/candidate_004/README.md` + `run_pilot_004.py` + `logs/pilot_004.log` + `outputs/pilot_004_extraction_pilot.csv` + `outputs/pilot_004_prisma_pilot.txt` + eutils counts (570 vs 8188 vs RECORD 494 vs STROBE 18 already logged — re-verify). No PHI.
4. **pilot_005_006_plasmode_Dphase** (005+006 D+B staged, shared G0→G3, clinical): Build audit-anchored G0→G3 table CSV (BMI 28.3→22.8, MONO 0→56.7%, age 62→48, HbA1c observed 78%→15% selective P=0.20, generic 100→4.7%, AYUSH 0→96%, docs 100→8.5%) + tilting demo (entropy balancing or IPW resampling on synthetic MIMIC-like covariates N=5k), S_visit censoring demo (logit P(O) with γ_o), diagnostics SMD/S-score AUC/ESS/trimming per grade on synthetic cohort, B→R* titration contour stub (R*≈1.4–2.0 per RR_UD sweep, bounding factor B), 9-cell plasmode config CSV (3×P(U) 0.10/0.44/0.96 ×3×RR_UD 1.5/2.0/3.0). Deliver `pilots/candidate_005_006/README.md` + `run_pilot_005_006.py` + `logs/pilot_005_006.log` + `outputs/G0_G3_table.csv` + `outputs/pilot_005_006_diagnostics.csv` + `outputs/pilot_005_006_Rstar_contour.csv`. Link to candidate_005/006 dossiers + paired OSF `osf_prereg/candidate_005_006_OSF.md`.

## Output contract (all pilots)
- Each pilot dir `pilots/candidate_<NNN>/` with README.md (aim + data path + run command + outputs), runnable code (sh/py/R), execution log (full stdout/stderr), outputs (CSV/plot stub), verification (test pass / κ / calibration plot stub / checksum). Pilots may be small-scale dry-runs (N=200–500, n=20 corpus) — honesty about scale vs full 150/1500 fits.
- 2–3 new searches per pilot only if needed (tools/API/docs), logged verbatim to search_log; evidence_registry not needed for pilots (code outputs are pilots, not literature).
- No fabrication — pilot outputs must be real execution outputs (even if fallback synthetic). Log fallback honestly.

## Non-goals
Full RR execution (001 LSTM frozen replication on full eICU, full 16×200 CIMEHR, full n=150 screening) — pilots are dry-runs to prove pipeline + unblock OSF timestamp.

## Completion checklist per pilot
- [ ] Code is runnable (sh/py/R with pinned versions, help flag verified)
- [ ] Execution log exists with version + dep install + run output
- [ ] Outputs CSV/plot stub exists with real numbers (even if small-N)
- [ ] README with run command + data path + what full scale will add
- [ ] Searches logged verbatim if any tool/API lookups needed

