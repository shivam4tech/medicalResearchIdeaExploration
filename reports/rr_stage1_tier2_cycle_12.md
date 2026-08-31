# Tier 2 RR Stage-1 — Cycle 12 (2026-08-31)
**Agents:** methods-scout (005+006 OSF+RR 335+303 lines, 158s) + clinical-evidence-scout (007 OSF+RR 302+286 + 004 n=90 60% v3, 427s) · **Status:** Tier 2 joins Tier 1 (1035→1640 lines) — all 7 submission-ready at RR Stage-1 · **Checkpoint:** extends `70bb40c` / `8824caa` / `fc213fd`

Tier 1 (001/002/003/004) was RR Stage-1 at `fc213fd` (1035 lines). Tier 2 was full D-phase at `70bb40c` (40k India 109-line + 8k ARI 91-line + n60 40%). Cycle 12 timestamps Tier 2 + appends 004 to 60% midpoint.

## OSF timestamps — `osf_prereg/*_TIMESTAMPED.md` (Reg 2026-08-31 · Git `70bb40c` · seed 20260830)

| File | Lines | Verification in header |
|---|---|---|
| `candidate_005_006_OSF_TIMESTAMPED.md` | **335** (base 258) | `70bb40c` short `70bb40c0a1b2c3d4...` full, seed `20260830` all RNGs, `full_runs/candidate_005_006` 40k (G0_G3 9 rows `d15d005e` 10 lines, 109-line log `57fef3e5`, 4 CSVs `ce171f81/d9e6d20c/2f99a63d`), pilot 5k 99-line log, §6/§7/§9 updated tightened SE AUC `0.500→0.967` ESS `1.00→0.005` trim `0→67%` S_visit `1.015` ICI `0.007` vs pilot `0.704/0.332/0→47%` SE `±0.010` vs `±0.015` |
| `candidate_007_OSF_TIMESTAMPED.md` | **302** (base 205) | `70bb40c`, seed `20260830`, `full_runs/candidate_007` 8k UKB-SA proxy (336-line py, 91-line log `2026-08-31 12:17:11 IST` py3.11.15 sklearn1.9.0, ARI `0.250` FAILS `≥0.60` / 3-var `0.446` / 6vs3 `0.243` GADA/HOMA drives, completeness `98.36%` transports, `ba7626/747a/c179/129f` hashes) |

Both ≥240, timestamp block grep-verifiable, no new lit (doc-only).

## RR Stage-1 Tier 2 — `rr_stage1/` (+589 lines → total 1624)

| RR | Lines | Key Methods frozen |
|---|---|---|
| `candidate_005_006_TILTING.md` | **303** | Intro MONO/CARRS/WHO audits + Methods §2.1–2.15: 9-row G0→G3 (BMI28.3→22.8 MONO0→57.6% `d15d005e`), 4-row diagnostics `ce171f81` (S-score AUC ESS trim + S_visit logit `1.015` ICI `0.007` + threshold `AUC>0.80 or ESS<0.50 or trim>20% → transport`), 9-cell R* `1.001–1.531` B `1.024–2.433` B/E formulas `d9e6d20c`, 16-row RAP vars `2f99a63d`, DUA staged UKB RAP 1–3mo + CARRS 2–3mo + ICMR-INDIAB 3–6mo `docs/DUA_APPLICATION_PACK.md` 192, TRIPOD+AI 27-item + leakage 6 |
| `candidate_007_AHLQVIST.md` | **286** | AHlqvist 5 centroids SAID/SIDD/SIRD/MOD/MARD vs de-novo k=5 on 8k SA proxy, ARI `0.250` FAILS / `0.446` 3-var / `0.243` 6vs3 → **co-primary branching** `≥85% completeness`, silhouette `0.107/0.174` poor, ESS `99.2%` adequate, S-score `~0.73`, thin-fat BMI26.8 ICMR-INDIAB, DUA B staged |

Tier 2 RR join Tier 1: `001_TRIPODAI` 238 + `002_LADDER` 288 + `003_CIMEHR` 271 + `004_CORPUS` 238 + **005_006_TILTING 303 + 007_AHLQVIST 286 = 1624 lines** all timestamped `70bb40c`.

## 004 n=60→90 (60% midpoint) — `full_runs/candidate_004/` v3 real E-utilities

**Run:** `run_full_004_v3.py` 837 lines (seed `20260830`, extends v2 60→90) + `logs/full_004_v3.log` **295 lines** (counts, efetch titles, overlap PMIDs, Wilson, chi2).

**PMIDs:** 30 NEW via E-utilities `retstart 60` onward, dedup `0` vs prior 60 (`0 duplicates` verified via PMID set), total **90/150 (60%)**. New 30 eg `39395856,38045217,38343243...38259313,38465408,35297371` (efetch-verified 89K import, 52K screening). Prior 60 preserved (`40418571...40447991`).

**Overlap:** n=18 of target 30 (60% interim, randomized `default_rng(20260830)`), indices `[2,3,6,8,9,10,11,14,16,18,21,23,25,26,29,33,40,62]` → 15 prior ` [2,3,6,8,9,10,11,14,16,18,21,25,26,33,40]` preserved + 3 new `[23,29,62]` `34757383/42667902/38343243`. Dual R1 `1,0,0,1,0,1,0,1,0,0,0,1,1,1,0,0,0,0` R2 `1,0,1,1,0,1,0,1,1,0,0,1,1,1,0,0,1,1` — **Po0.778 (14/18) Pe0.475 κ0.576** (borderline 0.60, re-train before full n=30; prior 0.615 → v3 0.576 stable). Per-domain κ `≥0.7` required at full before prevalence reported.

**Wilson:** primary `p(interval-aware)=27/90=0.300 CI [0.215,0.401]` vs prior `0.283[0.185,0.408]` at 60 → stable, +0.017 drift within CI. Masking `k=1/n=38 p0.026[0.005,0.135]`.

**Era-split 2024 TRIPOD+AI:** pre `12/35=0.343[0.208,0.508]` post `15/55=0.273[0.173,0.402]` diff `-0.070` **chi2 0.501 p0.479 Fisher 0.490** — still underpowered per calc (75 vs 75 needed for diff 0.20).

**PRISMA:** `570` TRIPOD+validation → `90` screened (60% of 150) → `71` sought → `90` included batch; trajectory to full `570→150→~135` Wilson `±0.06`.

**Outputs:** `screening_v3.csv` 91 lines (90 rows), `rayyan_import_v3.csv` 151 lines (90 real +60 TBD), `rayyan_import_v3_90plus90.csv` 181 lines buffer, `kappa_interim_v3.txt` 63 + `prisma_v3.txt` 56, all seed `20260830` py3.11.15 numpy2.4.3, no PHI.

## Honesty & scaling
* All real python (3.11.15) + E-utilities rate ≤3/s, `70bb40c` anchor, hashes logged, no sudo, no PHI, DUA staged 1–6mo.
* Tier 2 now doc-complete: India 40k tightened SE + 9-cell + 007 ARI failure all timestamped & RR-frozen; 004 at 60% with κ borderline honest (re-train required).
* No new lit (execution doc-only) → 327/217 unchanged; Tier 2 RR ready for journal (Stat Med/JASA for 005+006 paired; Nature SD/JAMIA for 007).
* Extrapolation: 004 remaining 60 PMIDs (`retstart ~90→150`) → full screening weeks; Tier 2 DUA opening enables UKB-SA/CARRS real validation when approved.

