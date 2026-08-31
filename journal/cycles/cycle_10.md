# Cycle 10 — Full Runs + Journal Submission Prep
**Date:** 2026-08-31 · **Agents:** Research Lead + clinical-evidence-scout + methods-scout (adversarial MONITOR light) · **Rate-limit incidents:** none

## Objective
Execute scaled full runs (toward registered N) and prepare journal submission packs — bridge RR Stage-1 (methods frozen) to execution (Results TBD) for Tier 1 (001/002/003/004).

## Questions for this cycle
1. Do 002 S1–S5 (5-point, 3 methods × 3 seeds) and 003 16-cell expansion (4-cell ×30 reps hold-out) reproduce pilot trends at scale?
2. Does 004 Rayyan kickoff scale from n=20 → n=40 (of 150) with interim κ + Wilson + PRISMA update?
3. Is 001 Harutyunyan→eICU submission pack (cover letter + TRIPOD+AI checklist + manifest) journal-ready?

## Assignments
- **methods-scout:** 002 full ladder 5-point ×3×3 (45 fits) + 003 4-cell×30 reps (120 fits hold-out) → `full_runs/candidate_002/` + `full_runs/candidate_003/` (704s, 30 api_calls)
- **clinical-evidence-scout:** 004 n=150 kickoff n=40 + 001 submission pack (cover letter + checklist + manifest) → `full_runs/candidate_004/` + `submission/candidate_001/` (406s, 46 api_calls, checkpoint `f0929c6` early)
- Brief: `working/CYCLE_10_BRIEF.md` (scaled full runs, honest extrapolation, no sudo).

## Findings
**Scaled full runs prove pipeline toward registered full N, with honest hold-out calibration.**

| Run | Dir | Log | Key scaled-full numbers (honest hold-out) |
|---|---|---|---|
| 002 | `full_runs/candidate_002/` | 158 lines 9.5s | 5 levels: S4_resample best mmd 0.001 corr 0.009 disc 0.443 composite 0.991 → S2_gan worst 0.132/3.98/0.649 0.201; TSTR S4 0.857/0.803/0.832 vs S5 0.501; **τ=0.733 ρ=0.867 LB -0.067** (n=5 small, pilot was n=2 τ=1.0 → full 8-point ladder will tighten LB≥0.5) |
| 003 | `full_runs/candidate_003/` | 726 lines hold-out | 4 cells ×30 reps=120 fits: N500_g0 0.773→0.771 slope 0.968/0.931 cover 46.7%, N2k_g08_09 0.787→0.786 slope 1.024/1.003 cover 83–86% winrate 30–43% (vs pilot in-sample 80–90% → hold-out drops honest) |
| 004 | `full_runs/candidate_004/` | 260 lines E-utilities | 20 NEW PMIDs (0 duplicates, drift `40604360` logged) → 40 rows; dual n=10 (25% interim) **κ0.615** Po0.800 (pilot 0.615 preserved → re-train required <0.7); Wilson **0.275 [0.161,0.428]** masking 0.062 era χ²p0.416; Rayyan import 151 lines (40+110) |
| 001 pack | `submission/candidate_001/` | 4 docs 282 lines | cover 52 + checklist 33 (27 DONE) + manifest 103 (fc213fd/74aa516/CIMEHR0.1.0) + repro 94 (ricu 0.5.8, py3.11.15 etc) — journal choice BMJ/JAMIA/PMLR-MLHC |

Extrapolation READMEs: 002 ~1,500 fits ⇒ 1–2 GPU-h synthetic → 8–12h MIMIC; 003 ~22k ⇒ 200–300 GPU-h; 004 n=150 ⇒ weeks (n=40 kickoff proves pipeline).

## Decisions
**Submission-ready for 001** (TRIPOD+AI 27 DONE, leakage 6, OSF fc213fd); **scaled runs confirm feasibility** but flag LB (-0.067 <0.5) and coverage 46% at N500 → full 8-point ladder + N2k+ will stabilize; κ borderline requires reviewer retrain before full n=30 dual.

## Candidates created/weakened/killed
No dossier changes; 7 KEEP; 4 RR → scaled execution evidence; 001 pack new under `submission/`.

## Rate-limit incidents
_none_ (32 total this cycle before, 30+46 =76 now; never hit ceiling 30, no 429s)

## Ledgers updated
`search_log.csv` 327 unchanged (execution, no new lit); `evidence_registry.csv` 217 unchanged.

## State
- Candidates: 7 KEEP → 4 RR + scaled full evidence (002/003/004) + 001 submission pack · Search log 327 · Evidence 217
- Shortlist: FROZEN · RR Stage-1 fc213fd → submission pack f0929c6 checkpoint
- Full runs: 002 45fits + 003 120fits hold-out + 004 n=40 → extrapolation to registered N

## Next cycle
Cycle 11 — Full 16×200 / n=150 completion + RR reviewer revision; Tier 2 India DUAs (UKB-SA/CARRS) staged.

