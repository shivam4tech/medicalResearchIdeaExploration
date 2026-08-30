# Cycle 8/9 — OSF Timestamp + RR Stage-1 Submission Packages (Cycle 9 per operator)
Companion: docs/01..03, shortlist/SHORTLIST.md FROZEN (7 KEEP, 3 patched), osf_prereg/* (4 templates 889 lines), pilots/candidate_002+003+004+005_006 (all exit 0), ideas/candidate_00*.md (7 dossiers), literature 327/217. Adversarial MONITOR (light check, no kill unless gate fails).

Cycle 7 proved Tier 1 + D-phase runnable tomorrow (synthetic fallbacks honest, CIMEHR 0.1.0 + synthEHRella verified). Cycle 8/9 asks: **timestamp OSFs + turn 4 Tier-1 pilots into RR Stage-1 submission-ready packages** — so a journal sees Introduction + Methods + full pre-reg, not just a pilot stub.

## Binding constraints (same pool)
- Pool muse-spark-1.2-contributor-free ~40/min target ≤24 ceiling 30 max 2 concurrent. Active chat shares pool.
- No new large literature search — pilots already logged 5 new tools; only 1–2 *verification* searches allowed if a checklist item needs DOI (e.g., TRIPOD+AI 2024 10.1136/bmj-2024-080749 already logged, Van Calster hierarchy already logged). Log verbatim if any.
- All outputs are **documents, not field work**: MD + PDF-ready. No PHI/DATA fetch — reuse pilot code + OSF templates + dossier evidence. DUA-track (UKB-SA/CARRS/ICMR-INDIAB) stays staged, mentioned as future Stage-2.
- Each RR package must pass its **checklist**: 001 TRIPOD+AI 27-item + leakage 6-item + Van Calster levels; 002 τ≥0.7 + DCA + held-out calibration plan; 003 CIMEHR decision rule (slope/intercept/coverage/DCA) + twin variants + 16-cell spec; 004 PRISMA 2020 + Wilson + κ≥0.7 plan + masking definition per Riley. Provide code archive hash (git rev 70730ae) + random seed.

## Assignments (2 scouts, docs)

### methods-scout → 001 + 003 RR Stage-1
1. **RR_001_Harutyunyan_eICU** (TRIPOD+AI): Promote `osf_prereg/candidate_001_OSF.md` to timestamp-ready `osf_prereg/candidate_001_OSF_TIMESTAMPED.md` (add OSF registration placeholder + `git rev 70730ae` + code hash for `pilots/candidate_002/synthEHRella` + seed + leakage checklist copy with 6 items + TRIPOD+AI 27-item ticked). Then draft `rr_stage1/candidate_001_TRIPODAI.md` (RR Stage-1 Intro + Methods: sepsis/mortality per Harutyunyan 10.1038/s41597-019-0103-9 + Shin 10.1038/s41467-023- ... [use Harutyunyan DOI already logged], cohort MIMIC→eICU/AmsterdamUMCdb via ricu 0.5.8, leakage audit, equivalence margin Δ0.05 slope 0.8–1.2 intercept |·|<0.3, hierarchical Van Calster 10.1016/j.jclinepi.2015.12.005, baselines LR/SOFA/GBM/trivial). Deliver `rr_stage1/candidate_001_TRIPODAI.md` + checklist appendix CSV.
2. **RR_003_CIMEHR_plasmode** (DL vs classical): Promote `ideas/candidate_003.md` + pilot `pilots/candidate_003/` + OSF (no template yet — create `osf_prereg/candidate_003_OSF.md` 200+ lines mirroring 001 style: 3-process joint λ_V/logitP(O)/Y + 16-cell core + twin variants + decision rule non-inferior slope/coverage AND superior DCA). Then draft `rr_stage1/candidate_003_CIMEHR.md` (Intro: Liang 2410.13113 + Yang CIMEHR 2602.15374 + Sun supplement gap) + Methods + code archive hash. Deliver both files + pilot cell table reference.

### clinical-evidence-scout → 002 + 004 RR Stage-1
3. **RR_002_synthEHRella_ladder** (fidelity→τ): Promote `osf_prereg/candidate_002_OSF.md` → `osf_prereg/candidate_002_OSF_TIMESTAMPED.md` (add git rev + synthEHRella 74aa516 + seed 20260830 + S1–S5 6 methods from Chen 10.1093/jamia/ocaf082 vs Liu 2504.11740, fidelity points MMD/corr/discriminative, τ≥0.7, DCA 10/20%, MIMIC-III→IV transport). Then draft `rr_stage1/candidate_002_LADDER.md` (Intro + Methods) + pilot fidelity/τ table. Deliver both + DCA stub plot note.
4. **RR_004_corpus_audit** (TRIPOD subgroup calibration): Timestamp `osf_prereg/candidate_004_OSF.md` if exists else create from `ideas/candidate_004.md` + pilot `pilots/candidate_004/` (n=150 audit, interval-aware per Riley 10.1136/bmj-2024-080749, TRIPOD 570 vs 8188 ~7% bias, RECORD/STROBE sensitivities, Wilson ±0.06 CI, κ≥0.7, masking rate, era-split 2024 TRIPOD+AI). Then draft `rr_stage1/candidate_004_CORPUS.md` (PRISMA 2020 flow + extraction form 22 cols + Wilson power + adjudication). Deliver both + PRISMA checklist CSV + extraction form CSV.

## Output contract
- `osf_prereg/candidate_*_OSF_TIMESTAMPED.md` or `_OSF.md` (timestamp-ready: add `Registration date: 2026-08-30 · Git rev 70730ae · Code archive pilots/candidate_*/ sha256 + seed + checklist ticked` at top, preserve original OSF body).
- `rr_stage1/candidate_*_*.md` (RR Stage-1 Intro+Methods, 150+ lines each, with falsifiable Q + publishable negative framing + ethics + scope ceiling + India Stage-2 note where relevant, citations already in dossiers).
- Each RR must include: git rev, code hash/seed, checklist appendix (TRIPOD+AI/PRISMA/Wilson/CIMEHR decision rule), and a `Verification: pilot exit 0` line linking to `pilots/candidate_*/logs/pilot_*.log` row counts.
- No fabrication — cite only DOIs already in `literature/evidence_registry.csv` (or log 1 new verification if truly needed).
- Checkpoint writes early; keep diffs small.

## Non-goals
Field execution of full 16×200 / n=150 screening / UKB-SA DUA — RR Stage-1 methods-only, pilots are feasibility proof. Results section stays `TBD (registered)`.

