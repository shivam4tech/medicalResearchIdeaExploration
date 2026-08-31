# Cycle 11 — Tier 2 India Transport + 007 Ahlqvist + n=150 Completion Prep
**Date:** 2026-08-31 · **Agents:** Research Lead + clinical-evidence-scout + methods-scout (adversarial MONITOR light) · **Rate-limit incidents:** none

## Objective
Execute Tier 2 India D-phase at full granularity (G0->G3 10k/grade, 9-cell R*) + 007 centroids vs de-novo on UKB-SA synthetic proxy (ARI, ablation) + push 004 Rayyan 40→60 (of 150) + draft DUA application pack — so Tier 2 is submission-ready by Cycle 12.

## Questions for this cycle
1. Does India tilting full (40k synthetic, 4 grades) reproduce ESS collapse + R* 1.01-1.63 at scale with P(U)×RR_UD 9-cell?
2. Does 007 Ahlqvist centroids (European) vs de-novo on 8k SA proxy show ARI <0.60 (transport failure) and 6→3 ablation incompleteness?
3. Does 004 n=40→60 with n=15 overlap κ stabilize, and is DUA pack (UKB-SA RAP + CARRS) application-ready?

## Assignments
- **methods-scout:** 005+006 G0->G3 full India plasmode (N10k/grade) + 9-cell + diagnostics + RAP vars → `full_runs/candidate_005_006/` (122s, 13 api_calls)
- **clinical-evidence-scout:** 007 8k SA proxy centroids vs de-novo (ARI, ablation) + 004 n=40→60 (20 NEW PMIDs, κ+Wilson+PRISMA) + `docs/DUA_APPLICATION_PACK.md` → `full_runs/candidate_007/` + `full_runs/candidate_004/` append + docs (298s, 28 api_calls)
- Brief: `working/CYCLE_11_BRIEF.md` (India transport, no sudo, honest synthetic proxy, seeds 20260830).

## Findings
**Tier 2 India D-phase complete (40k diagnostics + 9-cell R*) + 007 ARI failure (GADA-driven) + n=60 midpoint, honest synthetic proxy.**

| Run | Dir | Log | Key numbers (N10k/grade or N8k SA) |
|---|---|---|---|
| 005+006 | `full_runs/candidate_005_006/` | 109 lines | 40k synthetic G0→G3 re-verified 9 rows (BMI 28.3→22.8 etc); S-score AUC 0.500→0.759→0.911→0.967 ESS/n 1.00→0.21→0.017→0.005 trim10 0→2.6%→37.7%→67% (tightened SE vs pilot 0.332→0.012); **R* 1.001–1.531** (9-cell 3×P(U)×3×RR): RR1.2 fragile at 96%/2+, RR1.5 robust except 96%/3.0 |
| 007 | `full_runs/candidate_007/` | 91 lines | 8k SA proxy age44.5 BMI26.8; k=5 transport vs de-novo **ARI 0.250 FAILS** (≥0.60 transports), 3-var ARI 0.446, **6vs3 ARI 0.243 → GADA/HOMA drives** (matches REVISE), completeness 98.36% transports (≥85%), silhouette 0.11/0.17 poor, ESS 99% |
| 004 | `full_runs/candidate_004/` append | 260+253 lines | 20 NEW PMIDs (0 duplicates) → **60 rows (40%)** of 150; dual n=15 (25% interim) **κ0.615 Po0.80 Pe0.48** (borderline <0.7, re-train required, stable vs pilot 0.615); Wilson **0.283 [0.185,0.408]** (k=17/60) vs 0.275 at 40 → stable; era χ²p0.430 |
| DUA | `docs/DUA_APPLICATION_PACK.md` | 192 lines | UKB RAP 1–3 mo SA n~8–10k + CARRS 2–3 mo PHFI/Emory + ICMR-INDIAB 3–6 mo 113k + CMC Vellore 2–4 mo; variables BMI/MONO/HbA1c/AYUSH/generic/docs, staged 1→3 mo proxy →2–6 mo restricted |

Honest synthetic proxy (DUA staged 1–6 mo), seeds 20260830, git rev 8824caa, no sudo, no PHI.

## Decisions
**Tier 2 D-phase executable now on synthetic, ready for real-SA validation when DUA opens:** India 40k proves dose-response ESS collapse + R* threshold; 007 ARI 0.25 failure + GADA 0.24 ablation proves **co-primary 3-var branching** (per REVISE 2026-08-30) is required; 004 κ borderline needs retraining before full n=30.

## Candidates created/weakened/killed
No dossier changes; 7 KEEP; Tier 2 India full D-phase evidence added under `full_runs/`; DUA pack new.

## Rate-limit incidents
_none_ (13+28=41 calls total, never hit ceiling)

## Ledgers updated
`search_log.csv` 327 unchanged (execution synthetic, DUA portal citations doc-only) · `evidence_registry.csv` 217 unchanged (India execution, synthetic proxy)

## State
- Candidates: 7 KEEP → Tier1 RR+full runs → Tier2 India full D-phase (40k+8k+60) → DUA staged · Search log 327 · Evidence 217
- Shortlist: FROZEN · India DUA 1–3 mo proxy →2–6 mo restricted

## Next cycle
Cycle 12 — Tier 2 OSF timestamp + Tier 2 RR Stage-1 (005+006 paired + 007) + n=150 completion (90→150) + journal submission Tier 2.

