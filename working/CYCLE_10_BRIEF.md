# Cycle 10 — Full Runs + Journal Submission Prep (execution after RR Stage-1)
Companion: shortlist/SHORTLIST.md FROZEN (7 KEEP), rr_stage1/* (4 RR Intro+Methods 1035 lines timestamped 70730ae), osf_prereg/*TIMESTAMPED* (001 245 + 002 238 + 003 262 + 004 291), pilots 4 exit 0, git rev fc213fd. Adversarial MONITOR light.

**Why Cycle 10 now:** RR Stage-1 (Cycle 9) froze methods. Cycle 10 executes the *registered* analyses at feasible scale and prepares journal submission packs (cover letter + checklist + code archive). This is the execution counterpart to the 8–12 mo Tier-1 timeline in SHORTLIST (1.5–2.5 mo per project ×2 persons + agents).

## Binding constraints (same pool — no new heavy installs)
- Pool muse-spark-1.2-contributor-free ~40/min target ≤24 ceiling 30 max 2 concurrent. This cycle is **compute + docs**, but bounded: full runs are still large (002 ~1,500 fits, 003 ~22k fits) — scouts run *scaled full pilots* (not the entire 22k in one delegate wall-clock). Honest logging: report scaled N vs registered full N, with extrapolation.
- No sudo/pkexec (Cycle 7 rule persists). R via ~/R/library, Python via hermes venv. No PHI.
- Every run must produce real python/R execution (logs + CSVs + version hashes), not just docs. Checkpoint writes early. Log at most 1–2 verification searches verbatim if a journal policy DOI needed.

## Assignments (2 scouts, execution + submission docs)

### methods-scout → 002 full ladder + 003 16-cell expansion (compute)
1. **002 S1–S5 full ladder expansion:** Extend pilot `pilots/candidate_002/` (2-point pilot mmd 0.088/0.070 τ=1.0 n=2) to **5-point full ladder** (S1 plasmode Generate-Treatment, S1' Generate-Outcome, S2 GAN epochs 10/50/200, S3 Synthea, S4 resample, S5 random) on N=5k synthetic 10+15cat (MIMIC-III demo still uncredentialed, honest). Run 3 methods (logistic, tree/GBM, RF) × 3 seeds (20260830, 20260831, 20260832) × 5 synthetic levels = 45 fits (scaled from ~1500 full via 8 methods×50 reps), compute full τ (Kendall + Spearman + LB) + DCA 10/20% + calibration slopes. Deliver `full_runs/candidate_002/` with `run_full_002.py` + `logs/full_002.log` (real python) + `outputs/full_002_tau.csv` (5 rows) + `outputs/full_002_utility.csv` + calibration stubs. README with extrapolation to ~1500 fits.
2. **003 CIMEHR 16-cell expansion:** Extend `pilots/candidate_003/` (80 fits, 2γ×2 variants) to **4-cell × 30 reps = 120 fits** scaling toward 16×200 register (N 500/2k, visits 2/6, SNR 0.5/1.5, γ_v 0/0.8, γ_o 0/0.9, variants 2) via R `--libPaths ~/R/library`, CIMEHR 0.1.0 verification repeated. Compute AUC + slope/intercept + coverage + NB hold-out (train/test split, not in-sample), winrate ladder, twin delta. Deliver `full_runs/candidate_003/` with `run_full_003.R` + `logs/full_003.log` + `outputs/full_003_cell.csv` + `outputs/full_003_rep.csv` + extrapolation note to 16×200 (200–300 GPU-h).

### clinical-evidence-scout → 004 n=150 kickoff + 001 submission pack (literature + docs)
3. **004 n=150 Rayyan kickoff:** From pilot `pilots/candidate_004/` (20 fetched, κ 0.615 pilot), run expanded **n=40 screening** (of 150 target) via E-utilities fetch 20 new PMIDs + de-duplicate, apply 22-col extraction form, pilot dual extraction expanded to n=10 overlap (of n=30 target 20%), compute interim κ + Wilson for p(interval-aware) + masking + era-split contingency, generate updated PRISMA flow counts (Identification n=570→Screening→n=40→...), Rayyan import CSV for n=150. Deliver `full_runs/candidate_004/` with `run_full_004.py` + `logs/full_004.log` + `outputs/full_004_screening.csv` (40 rows) + `outputs/full_004_kappa_interim.txt` + `outputs/full_004_rayyan_import.csv`.
4. **001 RR submission pack:** Prepare journal submission for `rr_stage1/candidate_001_TRIPODAI.md` — auto-generate `submission/candidate_001/cover_letter.md` (journal choice BMJ/JAMIA/PMLR-MLHC with Harutyunyan 10.1038/s41597-019-0103-9 gap), checklist `submission/candidate_001/TRIPODAI_checklist_filled.csv` (27-item filled), `submission/candidate_001/code_archive_manifest.txt` (hashes of pilots + rr_stage1 + git rev fc213fd), `submission/candidate_001/reproducibility_statement.md` (ricu 0.5.8, R/python versions, seeds, compute). Re-use OSF timestamp fc213fd block. Deliver `submission/candidate_001/` with 4 docs + verification that rr_stage1 file is submission-ready.

## Output contract
- Each `full_runs/candidate_*` has README + runnable code (py/R) + execution log (real) + outputs CSVs (real numbers) + extrapolation to registered full N.
- Each `submission/candidate_001/` has cover letter + checklist + manifest + statement (≥30 lines each), referencing git rev fc213fd + OSF timestamp + pilot logs.
- Log any journal policy lookup verbatim to search_log (≤2 rows). Evidence registry unchanged (execution, not lit).
- Checkpoint early; honest about scaled vs full N; no sudo.

## Non-goals
Full 22k CIMEHR or full 150 full-text screening in one wall-clock — scaled runs prove pipeline + extrapolate; full 150 completes over weeks per RR.

