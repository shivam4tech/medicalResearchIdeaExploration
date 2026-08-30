# Cycle 7 — Pilot Execution (prove first wave runs)
**Date:** 2026-08-30 · **Agents:** Research Lead + clinical-evidence-scout + methods-scout (adversarial-reviewer MONITOR) · **Rate-limit incidents:** none

## Objective
Execute small-scale pilots (code + data) that prove Tier 1 (no-DUA) and Tier 2 D-phase are runnable tomorrow on public/synthetic/literature data — so OSF pre-registrations can be timestamped with a working pipeline, not just a spec.

## Questions for this cycle
1. Do synthEHRella (002) and CIMEHR (003) pipelines run end-to-end on a tiny pilot (2-point fidelity, 2-cell γ_v) with real outputs (τ, calibration, coverage, DCA)?
2. Does Rayyan-ready corpus pilot (004) fetch PubMed, sample n=20/150, define interval-aware extraction form, and produce pilot κ + Wilson CI + PRISMA pilot?
3. Does paired G0→G3 plasmode D-phase (005+006) build the audit-anchored table, tilting/S_visit demo, and B→R* contour on synthetic MIMIC-like data?

## Assignments
- **methods-scout:** pilot_002_synthEHRella_ladder (S1–S5 2-point pilot + τ/DCA) + pilot_003_cimehr_plasmode (2-cell ×20 reps CIMEHR dry-run + calibration/coverage/DCA)
- **clinical-evidence-scout:** pilot_004_rayyan_corpus (PubMed fetch n=20 + κ/Wilson/PRISMA) + pilot_005_006_plasmode_Dphase (G0→G3 table + tilting/S_visit + diagnostics + R* contour)
- Brief: `working/CYCLE_07_BRIEF.md` (4 pilots, runnable code + logs + outputs).

## Findings
**4/4 pilots executed, real python/R, logs 99–387 lines, outputs 3–81 rows, READMEs 50–79 lines, all exit 0, no sudo/pkexec.**

| Pilot | Dir | Log | Key pilot numbers (honest small-N) |
|---|---|---|---|
| 002 synthEHRella | `pilots/candidate_002/` | 152 lines | cloned `chenxran/synthEHRella` 74aa516 + `pip install .` hermes venv; S1 mmd 0.088 corr_fro 0.40 disc_auc 0.500 vs S5 0.070/4.06/0.508; TRTR 0.852/0.798 → TSTR_S1 0.850/0.793 → TSTR_S5 0.553/0.536; **τ=1.0** (n=2 trivial, winner preserved); NB10 0.457→0.456 vs treat_all 0.451; synthetic fallback (MIMIC-III demo not credentialed) logged |
| 003 CIMEHR | `pilots/candidate_003/` | 387 lines | R 4.5.2 `.libPaths~/R/library` CIMEHR 0.1.0 2026-06-08 vignette verified; 80 fits N=300×2×2×20; visits γ0 6.0 → γ0.8 7.6; AUC 0.776→0.788 GBM winrate 80–90%; slope ~1.0 in-sample (hold-out needed for full); manual 3-process fallback mirroring CIMEHR spec logged |
| 004 Rayyan | `pilots/candidate_004/` | 106 lines | esearch 570/8188/494/18 re-verified; fetched 20 IDs `40418571…` + n=5 overlap `[2,3,6,8,11]`; dual sim R1=[1,0,0,1,0] R2=[1,0,1,1,0] Po0.80 Pe0.48 **κ=0.615** (<0.7 → retrain); Wilson p-interval-aware 0.250 [0.112,0.469] masking 0.050 [0.009,0.236]; PRISMA 45 lines; 22-col interval-aware form per Riley `10.1136/bmj-2024-080749` |
| 005+006 G0→G3 | `pilots/candidate_005_006/` | 99 lines | G0_G3_table 9 rows verified (BMI 28.3→22.8 MONO 0→56.7% etc); N=5k tilting demo ESS/n 0.332→0.048→0.012 trim10 0.166→0.472 (transport collapse at G2/G3); R* 1.01–1.63 (spec ~1.4–2.0 at RR 4–5); 9-cell config 3×P×3RR |

Honest fallbacks: synthetic tabular for 002/005+006 (no MIMIC-IV credential), manual CIMEHR-sim for 003 runtime — all logged. Clock: 1235s methods + 319s clinical (parallel, 20m34s wall, ~80 calls, never hit ceiling 30).

## Decisions
Pilots **pass dry-run** — Tier 1 + D-phase runnable tomorrow: `pilots/candidate_*/run_pilot_*.{py,R}` with seeds `20260830` + versions pinned (python 3.11.15 pandas 3.0.5 sklearn 1.9.0 R 4.5.2 CIMEHR 0.1.0). Retrain needed for 004 κ <0.7 before full n=30; recalibration needed for 005+006 G2/G3 high trimming; hold-out calibration for 002/003.

## Candidates created/weakened/killed
No new dossiers; 7 KEEP frozen unchanged; 4 pilots added under `pilots/` (code outputs, not evidence rows).

## Rate-limit incidents
_none_

## Ledgers updated
`search_log.csv`: 320→**327** (+7 VERIFIED: synthEHRella API + CIMEHR API+CRAN + eutils 570/8188 + docs + entropy-balancing) · `evidence_registry.csv`: **217** unchanged (pilots are code, not literature).

## State
- Candidates: 7 KEEP frozen → 4 pilots (002/003/004/005+006) · Rejections: 0 · Search log rows: 327 · Evidence rows: 217
- Shortlist: FROZEN Cycle 6 — no open REVISE, 4 OSF templates ready → unblocked for timestamp
- Pilots: 0→4 runnable; next: 001 Harutyunyan→eICU TRIPOD+AI + full S1–S5 / 16×200 / n=150 / tilting hold-out

## Next cycle
Cycle 8 — RR Stage-1 submissions: 001 frozen LSTM replication on eICU + full runs for 002/003/004/005+006; India DUAs (UKB-SA RAP 1–3 mo, CARRS 2–3 mo).

