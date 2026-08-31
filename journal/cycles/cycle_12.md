# Cycle 12 — Tier 2 RR Stage-1 + n=150 60% Midpoint
**Date:** 2026-08-31 · **Agents:** Research Lead + clinical-evidence-scout + methods-scout (adversarial MONITOR light) · **Rate-limit incidents:** none

## Objective
Cut Tier 2 RR Stage-1 (005+006 paired G0→G3 40k tilting + 007 Ahlqvist 8k SA ARI) with OSF timestamp `70bb40c` + push 004 Rayyan 60→90 (of 150, 60% midpoint).

## Questions for this cycle
1. Are 005+006 and 007 timestamped OSFs verifiable (Reg date · Git `70bb40c` · seed 20260830 · 40k/8k hashes) and RR Intro+Methods complete (≥250 lines each)?
2. Does 004 n=60→90 with 30 NEW PMIDs preserve κ and tighten Wilson at 60% midpoint?
3. Is Tier 2 journal submission prep aligned (DUA staged, no PHI)?

## Assignments
- **methods-scout:** 005+006 OSF timestamp + RR TILTING → `osf_prereg/candidate_005_006_OSF_TIMESTAMPED.md` 335 + `rr_stage1/candidate_005_006_TILTING.md` 303 (158s, 16 api_calls)
- **clinical-evidence-scout:** 007 OSF timestamp + RR AHLQVIST + 004 n=60→90 append → `osf_prereg/candidate_007_OSF_TIMESTAMPED.md` 302 + `rr_stage1/candidate_007_AHLQVIST.md` 286 + `full_runs/candidate_004/` v3 90/150 (427s, 25 api_calls)
- Brief: `working/CYCLE_12_BRIEF.md` (no sudo, honest synthetic proxy, seeds 20260830).

## Findings
**Tier 2 joins Tier 1 — 6/6 RR Stage-1 frozen (1624 lines total) + n=90 60% midpoint, honest execution.**

| File / Dir | Lines/Log | Key numbers |
|---|---|---|
| `osf_prereg/candidate_005_006_OSF_TIMESTAMPED.md` | 335 | `70bb40c` · `d15d005e` 9 rows G0→G3, `ce171f81` 4-row diagnostics, `d9e6d20c` 9-cell R*, `2f99a63d` 16 RAP vars |
| `rr_stage1/candidate_005_006_TILTING.md` | 303 | AUC0.500→0.967 ESS1.00→0.005 trim0→67% S_visit1.015 ICI0.007 + R*1.001–1.531 B/E + DUA staged |
| `osf_prereg/candidate_007_OSF_TIMESTAMPED.md` | 302 | `70bb40c` 8k SA ARI0.250 FAILS 3-var0.446 6vs30.243 GADA/HOMA drives completeness98.36% |
| `rr_stage1/candidate_007_AHLQVIST.md` | 286 | 5 centroids vs de-novo ARI co-primary ≥85% silhouette0.11/0.17 DUA B staged |
| `full_runs/candidate_004/` v3 | 295-line log | 30 NEW PMIDs dedup0 → **90/150 (60%)** n=18 overlap **κ0.576 Po0.778 Pe0.475** Wilson **0.300[0.215,0.401]** era p0.479 |
| `rr_stage1/` total | 1624 | 001 238 +002 288 +003 271 +004 238 +005_006 303 +007 286 all `70bb40c` |

Honest synthetic proxy (DUA staged 1–6mo), seeds 20260830, no sudo, no PHI, 41 calls total (16+25).

## Decisions
**Tier 2 RR Stage-1 submission-ready now on synthetic, ready for real-SA validation when DUA opens:** India 40k tightened SE + 9-cell + 007 ARI failure all registered `2026-08-31`; 004 κ borderline needs retraining before full n=30 (stable 0.615→0.576).

## Candidates created/weakened/killed
No dossier changes; 7 KEEP; Tier 2 RR + n=90 evidence added; DUA pack at `70bb40c`.

## Rate-limit incidents
_none_ (16+25=41 calls total, never hit ceiling)

## Ledgers updated
`search_log.csv` 327 unchanged (execution doc-only) · `evidence_registry.csv` 217 unchanged

## State
- Candidates: 7 KEEP → Tier1 RR1035 + Tier2 RR589 → **1624 total + n=90** · Search log 327 · Evidence 217
- Shortlist: FROZEN · Tier2 RR frozen 2026-08-31

## Next cycle
Cycle 13 — Tier 2 journal submission + n=90→150 completion + Tier 2 full runs scaling (CARRS/ICMR-INDIAB when DUA opens).

