# Cycle 6 — Shortlist Freeze + REVISE Edits + OSF Pre-registrations
**Date:** 2026-08-30 · **Agents:** Research Lead + clinical-evidence-scout + methods-scout (adversarial-reviewer MONITOR until REVISE lands) · **Rate-limit incidents:** none (73 calls in ~9m, ~8.1/min, ceiling 30, 2 concurrent respected)

## Objective
Freeze the 7-candidate shortlist by applying the 3 REVISE edits (003 CIMEHR reframing, 004 interval-aware+Wilson+masking+era-split, 007 IMI-RHAPSODY+IndMED+sampling-frame fix) and cut OSF pre-registration templates for the first wave — so pilots start with no open REVISE and no HARKing risk.

## Questions for this cycle
1. Do 003/004/007 dossiers survive after CIMEHR engine reframing, interval-aware sharpening, and IndMED sweep with corrected near-equivalent rebuttals?
2. Is the 7-candidate SHORTLIST frozen with tiers, scope ceilings, DUA timelines, and paired 005+006 shared plasmode?
3. Are OSF templates for 001 (TRIPOD+AI + leakage), 002 (synthEHRella ladder + τ), 005+006 (G0→G3 paired), 007 (Ahlqvist transport) ready to timestamp?

## Assignments
- **methods-scout:** REVISE 003 (CIMEHR) + REVISE 004 (interval-aware) + OSF 001/002 + shortlist tech half
- **clinical-evidence-scout:** REVISE 007 (IndMED/IMI-RHAPSODY) + OSF 005+006/007 + shortlist clinical half + DUA timelines
- Brief: `working/CYCLE_06_BRIEF.md` (REVISE addenda, 2+ searches per REVISE, OSF templates, freeze).

## Rate discipline
Global pool muse-spark-1.2-contributor-free (opencode-zen/free) ~8.1/min observed (73 calls: 36 methods +37 clinical in ~9m), target ≤24, ceiling 30, max 2 concurrent. Dossier patches are search-intensive; OSF is second wave. No 429s. Active chat shares pool — respected via 2-concurrent cap.

## Findings
**3/3 REVISE patched 2026-08-30 + 4 OSF templates cut + SHORTLIST frozen — no open REVISE.**

- **REVISE 003 T1 plasmode DL-vs-classical → KEEP** (`ideas/candidate_003.md` 35K→46K, 10→11 papers, Medium): Reframed from "we propose 3-process spec" to **"we benchmark using CIMEHR as engine"** — Added Yang 2026 **10.48550/arXiv.2602.15374** + CRAN **cran.r-project.org/web/packages/CIMEHR** + GitHub **ysph-dsde/CIMEHR** as load-bearing (Important Papers + Evidence AGAINST, Liang 2410.13113 retained as sensitivity CIMEHR vs Liang engine fragility). **Inspections logged verbatim 2026-08-30:** Sun supplement **github.com/SCXsunchenxi/ISMTS-Review** — datasets+code, no LMM/joint-vs-DL calibration/coverage/DCA table in README/main text; **Frontiers 10.3389/fams.2026.1849703** (Mashishi et al. LMM vs BSM vs GEE vs weighted GEE on extreme irregular visits, ARB/coverage/MSE, missingness 10/20/40% — **no DL comparator**) ; **CIMEHR vignettes** CRAN 0.1.0 (2026-06-08) `Getting Started` 169K — three-stage semiparametric joint + simulator + benchmark methods — **no DL-vs-joint head-to-head on joint criterion**. Gap survives as benchmark with decision rule (non-inferior calibration/coverage AND superior DCA else classical suffices). 16-cell core + Schneider **10.1186/s13040-025-00450-z** retained; compute restated via CIMEHR pipeline (~22k fits naive, locked core 3,200–6,400 per N). REVISE Addendum appended (lines 340–391) + inline patches; 3 new searches + DOI 302 CIMEHR. **Post-REVISE confidence: Medium (engine now published but benchmark gap survives, now explicitly using CIMEHR).**

- **REVISE 004 T5 corpus n=150 → KEEP** (`ideas/candidate_004.md` 40K→50K, 8→11 papers, Medium): Sharpened from "subgroup calibration" to **interval-aware prevalence + Wilson + masking + era-split**. Added **PMID 41643238 Ahmed Child Abuse Negl 2026 (DOI 10.1016/j.chiabu.2026.107923)** + **DCGS 10.64898/2026.06.17.26355900** + **KAISEN 10.48550/arXiv.2607.28608** to Important Papers + Evidence AGAINST with rebuttal — **compliance study-level vs prevalence with Wilson CI + interval-aware per subgroup slope CI/plot band per Riley + masking rate (overall pass while ≥1 subgroup fails) + era split TRIPOD+AI 2024**. **Eutils counts logged verbatim 2026-08-30: TRIPOD[Title/Abstract] AND validation = 570 hits vs calibration[Title/Abstract] AND external validation = 8,188 hits (~7% language bias, quantified) + RECORD calibration 494 + STROBE external validation 18.** Gate 3 Falsifiable Q reworded: primary p(interval-aware subgroup calibration) slope CI/plot band per Riley vs secondary p(point) with Wilson ±0.06 + masking definition slope 0.8–1.2 intercept±0.3 ICI + era split χ²/Fisher Newcombe; Gate 4 filter updated with pre-registered RECORD/STROBE sensitivities. REVISE Addendum appended (lines 298–350) + inline patches; 4 new searches + DOI 302 Ahmed. **Post-REVISE confidence: Medium (near-equivalents now distinguished).**

- **REVISE 007 T2 Ahlqvist transport → KEEP** (`ideas/candidate_007.md` 41K→54K, 10→11 papers, Medium-High core / Medium data): Added **IMI-RHAPSODY 10.1007/s00125-021-05490-8** (Wesolowska-Andersen Diabetologia 2021 64:1982–1989 n=15,940 3 European cohorts, C-peptide/HDL) distinction — **proves HOMA→C-peptide transport *within Europe*, no Indian LMIC transport, no overlap diagnostics (SMD/ESS/S-score), no GADA-free ablation**. **IndMED/thesis sweep logged verbatim 2026-08-30: `Ahlqvist diabetes clusters India IndMED thesis` 0 closing hits** — gap survives (Anjana descriptive, IMI-RHAPSODY European only). **CARRS GADA/HOMA completeness: data dictionary not publicly available; inferred sparse (<20%) from Nair 2022 IJE and Anjana 2020; honest status "unconfirmed pending DUA" with co-primary 3-var (age/BMI/HbA1c) if completeness <10%, threshold ≥85% for 6-var primary pre-registered.** Added CMC/AIIMS new-onset enriched secondary target for ANDIS-vs-CARRS sampling mismatch; thresholds locked (completeness≥85% S-score AUC<0.70 ESS>70% ARI≥0.60). REVISE Addendum appended (lines 292–356) + inline patches; 4 new searches + DOI 302 IMI-RHAPSODY. **Post-REVISE confidence: Medium-High (core gap) / Medium (data assumption — honest pending DUA).**

- **OSF Pre-registrations (4 templates, OSF-ready with hashes/seed placeholders):** `osf_prereg/candidate_001_OSF.md` 218 lines (Harutyunyan TRIPOD+AI 27-item mapping, leakage checklist 6 items, harmonization ricu 0.5.8 primary + METRE/YAIB sensitivity, equivalence AUROC Δ0.05 slope 0.8–1.2 |α|≤0.3 subgroup ≤0.10, baselines LR/SOFA/GBM/trivial); `candidate_002_OSF.md` 208 lines (synthEHRella S1–S5 ladder + τ≥0.7 LB≥0.5 + DCA 10/20% + MIMIC-III→IV transport + 1500 fits pilot); `candidate_005_006_OSF.md` 258 lines (paired G0→G3 audit-anchored table + tilting + S_visit censoring + staged D+B 005 transport vs recalibration + 006 B→R* 9-cell + SMD/S-score/ESS/trimming); `candidate_007_OSF.md` 205 lines (centroids vs de novo IOPW + 6→3 ablation + thresholds). All with Van Calster 10.1016/j.jclinepi.2015.12.005 + Riley 10.1136/bmj-2024-080749 → TRIPOD+AI 10.1136/bmj-2023-078378 mapping where relevant.

- **SHORTLIST Freeze:** `shortlist/SHORTLIST.md` 209 lines — **FROZEN 2026-08-30, no open REVISE**. Tiers: **Tier 1 immediate A/D** 001/002/004-revised/003-revised (no DUA, single GPU, 1.5–2.5 mo each); **Tier 2 staged India D+B** 005+006 (shared plasmode+MIMIC+UKB-SA 1–3 mo → CARRS/ICMR-INDIAB 2–6 mo, paired submission 2 papers one sprint, 2.0–2.5 mo effective each); **Tier 3 restricted B** 007 (UKB-SA proxy 1–3 mo → CARRS 2–3 mo + ICMR-INDIAB 3–6 mo + CMC/AIIMS 2–4 mo). Scope ceilings, personnel (2 persons per dossier), compute (<$100–300 GPU-h), calibration hierarchy reuse, preprint watch (Patel 10.64898/2026.05.03.26352335 + YAIB/METRE), cross-dossier risks, outcome definitions TDD physician, ethics/privacy per dataset. `shortlist/REVISE_LOG.md` 57 lines logs 3 addenda + search_log IDs + DOI verifications.

All 7 dossiers now KEEP (4 original KEEP + 3 REVISE→KEEP); KILL 0 remains.

## Decisions
**Shortlist frozen: 7 candidates, no open REVISE, 4 OSF templates ready to timestamp tomorrow.**

- **REVISE verdicts closed:** 003 REVISE→KEEP (CIMEHR reframing + 3 inspections logged), 004 REVISE→KEEP (interval-aware sharpening + 4 searches + counts + RECORD/STROBE), 007 REVISE→KEEP (IMI-RHAPSODY distinction + IndMED 0 hits + honest CARRS GADA unconfirmed + thresholds locked). All 3 now KEEP; original KILL 0 stands. No `rejected/` moves.
- **OSF ready:** 4 templates cut with hashes/seed placeholders (001/002/005+006/007); 004 corpus OSF embedded in 004 dossier + shortlist; all TRIPOD+AI mapped, leakage checklists, equivalence bounds, harmonization stubs where relevant.
- **Execution tiers frozen:** Tier 1 (4 dossiers) code tomorrow; Tier 2 (2 dossiers paired, shared sprint) D-phase immediate while UKB-SA/CARRS DUA pends; Tier 3 (1 dossier) proxy now. Not a search problem anymore — next cycle is **pilot execution**, not dossier work.
- **Global verdict post-freeze:** KEEP 7 / REVISE 0 / KILL 0. Programme transitions from discovery (Cycles 1–5: 8 territories → 7 dossiers → 27 kill-try searches) to execution (Cycle 7+ pilots + RR Stage-1). Adversarial-reviewer returns to MONITOR until pilot PRs need second kill sweep.

## Candidates created/weakened/killed
- **Patched:** 3 REVISE dossiers `ideas/candidate_003.md` (46K lines 391, + CIMEHR engine), `004.md` (50K lines 350, + DCGS/KAISEN/PMID 41643238 + counts), `007.md` (54K lines 356, + IMI-RHAPSODY + IndMED + CARRS threshold locks) — all now KEEP, no open REVISE.
- **Created:** 4 OSF templates `osf_prereg/candidate_001_OSF.md` (218), `002_OSF.md` (208), `005_006_OSF.md` (258), `007_OSF.md` (205) + frozen `shortlist/SHORTLIST.md` (209) + `shortlist/REVISE_LOG.md` (57).
- **Weakened/killed:** 0. KILL 0 persists (7/7 gaps survive pointed kill round + REVISE re-argument).

## Rate-limit incidents
None. 73 model calls in ~9m (~8.1/min), no 429s, 2 concurrent respected (patches parallel, OSF second wave). Active chat shares pool — respected via cap.

## Ledgers updated
- `literature/search_log.csv`: 305 → **320 lines (319 data rows: 317 VERIFIED / 2 UNVERIFIED-timeout)** — +14 this cycle (003: Sun suppl + Frontiers + CIMEHR vignette 3; 004: Ahmed/DCGS/KAISEN/eutils/RECORD+STROBE 4; 007: IMI-RHAPSODY + IndMED + CARRS phenotyping + CMC/AIIMS 4; +3 OSF-linked) all VERIFIED, 0 new UNVERIFIED.
- `literature/evidence_registry.csv`: 209 → **217 lines (216 data rows: 211 VERIFIED / 2 TRUE / 1 UNVERIFIED-T2-06 + 1 cycle-tag + 1 compliance-typed)** — +7 this cycle (Yang CIMEHR, Ahmed PMID 41643238, DCGS, KAISEN, IMI-RHAPSODY, CIMEHR software, Frontiers) all VERIFIED/PMID resolvable.
- `reports/shortlist_cycle_06.md` (synthesis, 16.8K) + `shortlist/SHORTLIST.md` + `shortlist/REVISE_LOG.md` + 4 OSF templates + 3 patched dossiers.

## State
- Candidates: 7 dossiers → **7 KEEP frozen** (4+3 REVISE→KEEP) · Rejections: 0 · Search log rows: 305 → 319 · Evidence rows: 209 → 216
- Shortlist: **FROZEN** 2026-08-30 — no open REVISE, 3 tiers, scope ceilings 1.5–2.5 mo per dossier, DUA timelines honest, paired 005+006.
- OSF: 4 templates ready to timestamp (001/002/005+006/007)

## Next cycle
Cycle 7 — Pilot launches (execution, not search): methods-scout 002 synthEHRella 5-point ladder (~1500 fits, 30–50 replicates + 3–5 GAN seeds, Kendall τ curve, DCA, MIMIC-III→IV transport) + 003 CIMEHR pipeline 16-cell dry-run (synthetic rnorm fallback → MIMIC extraction when credentialed); clinical-evidence-scout 004 Rayyan n=150 screening (dual 20% κ≥0.7, Wilson CI, masking+era-split) + 005+006 D-phase plasmode on MIMIC (G0→G3 tilting + S_visit censoring, SMD/S-score/ESS, B→R* contour) → UKB-SA RAP.

