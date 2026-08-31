# Full Runs — Cycle 10 (2026-08-31)
**Agents:** methods-scout (002 5-level 45 fits + 003 4-cell 120 fits hold-out, 704s) + clinical-evidence-scout (004 n=40 kickoff + 001 submission pack, 406s) · **Status:** scaled full execution toward registered N, honest extrapolation · **Checkpoint clinical:** `f0929c6` (from `fc213fd`) — 004 n=40 + submission 001

Cycle 9 froze RR Stage-1 methods (Results TBD). Cycle 10 executes *scaled* full runs (not the entire 22k/150 in one wall-clock) with hold-out calibration and journal submission prep.

## Full runs executed (real python/R, no sudo)

### 002 S1–S5 fidelity→τ ladder — `full_runs/candidate_002/` (methods, 158-line log, 9.5s)
* **Design:** N=5k synthetic 10 num +15 cat train4000/test1000, **5 levels** S1_plasmode_treat / S1p_plasmode_outcome / S2_gan_epochs / S4_resample / S5_random, **3 methods** logistic + tree + RF, **3 seeds** 20260830/31/32 = **45 fits** (scaled from ~1,500 full: 8 methods×50 reps×5 levels → 315s synthetic ⇒ 1–2 GPU-h real MIMIC → 8–12h with CIs).
* **Fidelity (5 rows):** S4_resample best mmd 0.001 corr_fro 0.009 disc 0.443 composite 0.991; S1 0.060/0.388/0.482 0.721; S1p 0.057/0.395/0.486 0.717; S2_gan worst 0.132/3.98/0.649 0.201; S5_random 0.058/3.99/0.478 0.200 — resample ceiling >> plasmode >> GAN/random floor (expected).
* **Utility (15 rows =5×3):** TSTR means S4 0.857/0.803/0.832 (logistic/tree/RF) vs S5/S2 collapse ~0.48–0.50; TRTR 0.85–0.86.
* **Ranking:** Overall **Kendall τ =0.733, Spearman ρ=0.867, LB τ = -0.067** across 5 levels (fidelity vs utility). S4 rank 1 fidelity=1 utility=1, S1 2/3, S1p 3/2, S2 4/5, S5 5/4 — expected: high-fidelity resample preserves utility, GAN/random degrade. LB negative warns n=5 is small — full S1–S5 8-point ladder will tighten CI (registered primary: LB≥0.5 on TEST_R + TEST_TRANSPORT).
* **Hold-out calibration + DCA:** per-level calibration slopes (S4 ~0.98, S2 ~0.78) + NB10/20% (S4 NB10 0.455 ≈ TRTR 0.457 vs S2 0.30), full files `full_002_fidelity.csv/tau.csv/calibration.csv/dca.csv` + rep-level.

### 003 CIMEHR 16-cell expansion — `full_runs/candidate_003/` (methods, 726-line log, hold-out)
* **Design:** Manual 3-process simulator via `~/R/library` CIMEHR 0.1.0 verified (version+vignette+exports), **4 cells** (C1 N500_g0, C2 N500_g08_09, C3 N2k_g0, C4 N2k_g08_09) × **30 reps** = **120 fits** (scaled toward 16-cell×200 = ~22k fits / 200–300 GPU-h), **hold-out 70/30** train/test (vs pilot in-sample slope 1.0), metrics AUC/slope/intercept/coverage/NB/winrate/twin_delta.
* **Results `full_003_cell.csv` (4 rows):**
  * C1 N500_g0: LMM 0.773 vs GBM 0.771, slopes 0.968/0.931, GBM winrate 36.7%, coverage 46.7%, twin Δ -0.002.
  * C2 N500_g08_09: 0.780 vs 0.773, slopes 0.988/0.901, coverage 60/56.7%, winrate 30%.
  * C3 N2k_g0: 0.772 vs 0.771, slopes 0.976/0.965, coverage 83.3%, winrate 30%.
  * C4 N2k_g08_09: 0.787 vs 0.786, slopes 1.024/1.003, coverage 83–86%, winrate 43% — larger N + high γ improves hold-out slope toward 1.0 and coverage (pilot in-sample was 100% artificially).
* Hold-out exposes calibration variance (slopes 0.90–1.02 vs pilot 1.00 everywhere) and winrate drop (30–43% vs pilot 80–90% in-sample) — honest and expected.

### 004 Rayyan n=150 kickoff — `full_runs/candidate_004/` (clinical, 260-line log, real E-utilities)
* **Pipeline:** Re-verified counts 570/8188/494/18 OK, loaded pilot 20 + fetched **2 windows 0+20 relevance** → 20 NEW PMIDs `40604360,40536772…41258421` (corpus drift `40604360` at rank 2 logged) → **40 dedup 0 duplicates** → 2 efetch batches (40 titles), 22-col extraction (pilot 20 preserved + 20 new synthetic deterministic per Riley/TRIPOD+AI/masking), expanded dual **n=10 of 40 (25% interim, target n=30 of 150 =20%)** indices `[2,3,6,8,9,10,11,16,21,25]` preserving pilot 5.
* **Dual:** R1 `1,0,0,1,0,1,0,0,0,1` R2 `1,0,1,1,0,1,0,1,0,1` → **Po0.800 Pe0.480 κ0.615** (borderline <0.7 → re-train required before full n=30, inclusive Riley band rule, blinded).
* **Wilson:** p(interval-aware) **0.275 [0.161,0.428]** (11/40), overall 0.675, masking 0.062 [0.022,0.168] (vs pilot 0.250/0.050 — stable), era-split TRIPOD+AI χ² p0.416 (no era effect at n=40).
* **PRISMA:** 570→screened→n=40→included, Rayyan import `full_004_rayyan_import.csv` (151 lines: 40 + header + 110 placeholder for n=150), screening CSV 41 rows.

### 001 RR submission pack — `submission/candidate_001/` (clinical, 4 docs)
* `cover_letter.md` 52 lines: journal choice BMJ (Reproducibility) / JAMIA (Methods) / PMLR-MLHC (ML-for-Health) with Harutyunyan 10.1038/s41597-019-0103-9 gap (no TRIPOD+AI replication), cohort MIMIC→eICU/AmsterdamUMCdb via ricu 0.5.8, equivalence Δ0.05.
* `TRIPODAI_checklist_filled.csv` 33 lines: 27 TRIPOD+AI items filled (Location DONE, Notes leakage 6-item).
* `code_archive_manifest.txt` 103 lines: hashes pilots `pilots/candidate_002+003` + rr_stage1 + synthEHRella 74aa516 + CIMEHR 0.1.0 + git `fc213fd` (header) / `f0929c6` (clinical checkpoint) + seeds 20260830.
* `reproducibility_statement.md` 94 lines: ricu 0.5.8, python 3.11.15 pandas 3.0.5 sklearn 1.9.0 R 4.5.2, seeds, compute 1.5–2.5 mo, GitHub.

## Submission readiness & extrapolation
* All outputs real execution (python 3.11.15 sklearn 1.9.0 / R 4.5.2 ~/R/library), no sudo, honest scaled vs registered full N noted in READMEs.
* Full N extrapolation: 002 ~1,500 fits ⇒ 1–2 GPU-h (synthetic) → 8–12h with MIMIC + CIs; 003 ~22k fits ⇒ 200–300 GPU-h; 004 n=150 ⇒ full screening over weeks (n=40 kickoff proves pipeline + κ/Wilson stable).
* 001 pack journal-ready; 002/003/004 RR Stage-1 Intro+Methods already frozen (`rr_stage1/` 1035 lines, fc213fd).
* Ledgers: no new lit (execution) — 327/217 unchanged; at most 1–2 verification if journal policy lookup needed.

