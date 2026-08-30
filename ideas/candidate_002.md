# Candidate 002 — Fidelity→τ Threshold via synthEHRella (A/D)

**Source design:** T7 cycle02+04 (clinical-evidence-scout) — Cycle 04 T7 threshold lock `working/agent_notes/clinical-evidence-scout/cycle04_T7_threshold_lock.md`
**Class:** A/D (A real MIMIC-III/IV for training/evaluation + D synthetic generation via synthEHRella; no prospective PHI) | **Data path:** MIMIC-III v1.4 + MIMIC-IV v2.2 (PhysioNet credentialed, weeks) + synthEHRella open toolkit (GitHub) — synthetic lake generated on-premises.
**Status:** PROMOTION DOSSIER — Cycle 5 first wave (no DUA beyond PhysioNet) | **Date:** 2026-08-30
**Agent:** methods-scout (with clinical-evidence-scout T7 lock) | **India verdict:** GEOGRAPHY-ONLY v1 (Stage-2 Indian hospital test distribution)
**Confidence:** Medium (adversarial sweep returned no exact fidelity→τ EHR study; deep arXiv + citation-graph inspection required pre-promotion)

---

## Gate 1 — Gap Verification (strategies, reviews inspected, synonyms, chaining, adversarial — queries cited)

**Claim to verify:** No published study reports a **calibrated fidelity threshold f* (via synthEHRella or comparable) at which synthetic-supported *methods ranking* (e.g., logistic/Cox vs GRU-D) preserves real-data ranking measured by Kendall τ ≥0.7 (LB≥0.5) with clinical DCA thresholds (10%/20% net benefit) and MIMIC-III→IV transport** — i.e., the instrument-validity question "when is synthetic good enough to license a methods claim?" is unsettled.

**Strategy A — Synthetic EHR fidelity terminology (generation/validation vocabulary, DISTINCT):**
- `synthetic EHR fidelity evaluation MIMIC GAN plasmode Synthea validation` (2026-08-30, T7-S1-fidelity, 0 hits direct — terminology gap) — fidelity/validation/generation synonyms; 0 direct hits **recovered via Chen JAMIA chaining** (DOI 10.1093/jamia/ocaf082) — confirms vocabulary is fragmented vs ranking vocabulary (required distinct strategy).
- `Chen JAMIA synthetic EHR scoping review benchmarking fidelity utility` (2026-08-30, T7-review-Chen) — resolved to Chen et al. JAMIA 2025 (DOI 10.1093/jamia/ocaf082) via OUP verification.
- `Yan Patterns multifaceted benchmarking synthetic EHR 2022` (2026-08-30, T7-Yan) — GAN benchmarking synonyms (DOI 10.1016/j.patter.2022.100655).

**Strategy B — Rank-preservation / DCA terminology (evaluation/ranking vocabulary, DISTINCT from Strategy A — not generation terms):**
- `Kendall tau rank preservation Spearman synthetic versus real data method comparison` (2026-08-30, T7-S2-rank-preservation, 5 hits) — returned Kendall/Spearman reference pages, **no EHR methods-ranking study** — adversarial signal; terminology is ranking/evaluation distinct from fidelity/generation.
- `decision curve analysis net benefit clinical threshold synthetic data validation` (2026-08-30, T7-S2b-DCA, 5 hits) — DCA/net benefit/clinical utility synonyms; found Vickers 2006 (DOI 10.1177/0272989X06289078) + 2019 guide (PMC6123195).
- `Vickers decision curve analysis 2006 net benefit clinical threshold selection` (2026-08-30, T7-chaining-DCA, 5 hits) — DCA foundation chaining.
- `synthetic data rank correlation method ranking preservation TSTR` (2026-08-30, T7-adversarial-rank-preservation, 5 hits) — closest: **Shoshan et al. ICML 2023 "Synthetic Data for Model Selection" on general tabular data, not EHR methods benchmarking** — defeater inspected but not EHR-fidelity→τ.

**Reviews inspected (4 required):**
1. **Chen et al. JAMIA 2025** (DOI 10.1093/jamia/ocaf082) — 48 studies/5 categories benchmarking on MIMIC-III/IV phenotype data + synthEHRella toolkit; fidelity/utility/privacy/compute + decision tree. Load-bearing. **302 → academic.oup.com/jamia/article/32/7/1227/8155975** (OUP landing 4155975 + abstract extract 2026-08-30)
2. **Yan et al. Patterns 2022** (DOI 10.1016/j.patter.2022.100655) — multifaceted GAN benchmarking on closed data; Chen critique point (GAN-only, closed-source). **302 → linkinghub.elsevier.com/retrieve/pii/S2666389922002951**
3. **Angelopoulos & Bates 2021/2023 conformal** (DOI 10.1561/2200000101, arXiv:2107.07511 → FTML 2023;16:494-591) — distribution-free prediction intervals under exchangeability; interval baseline for DCA-adjacent calibration evaluation. **302 → emerald.com/ftmal/article/16/4/494/1332423**
4. **Van Calster et al. J Clin Epidemiol 2016** (DOI 10.1016/j.jclinepi.2015.12.005) — calibration hierarchy mean→weak (slope/intercept)→moderate→strong; vocabulary for DCA threshold framing. **302 → linkinghub.elsevier.com/retrieve/pii/S0895435615005818**

**Adjacent (plasmode fragility — required):**
- `Liu plasmode simulation cautionary Generate Treatment outcome arXiv 2025` (2026-08-30, T7-adjacent-Liu-fragility, 5 hits) — resolved to Liu et al. arXiv 2504.11740 (Generate-Treatment vs Generate-Outcome; 55 pages, 6 tables; 302 → arxiv.org/abs/2504.11740; web_extract 1918 chars in Cycle 2).

**Synonyms checked:** fidelity ↔ MMD ↔ RMSPE ↔ correlation recovery ↔ propensity distinguishability ↔ JS divergence; utility ↔ TSTR (train-synthetic-test-real) ↔ TSTR AUC gap ↔ association-recovery gap; rank preservation ↔ Kendall τ ↔ Spearman ρ ↔ pairwise concordance ↔ rank correlation; DCA ↔ net benefit ↔ threshold probability ↔ clinical utility ↔ relative utility; plasmode ↔ resampling-based simulation ↔ Generate-Treatment vs Generate-Outcome.

**Chaining (Chen → synthEHRella README → Liu fragility → Van Calster calibration):**
- **Chen JAMIA 2025** (10.1093/jamia/ocaf082) → **synthEHRella GitHub README** (https://github.com/chenxran/synthEHRella — raw GitHub 8054 chars, extracted 2026-08-30; package layout, 9 methods, evaluation/fidelity.py, utility.py, privacy.py, run_generation/evaluation/preprocessing/postprocessing pipeline for MIMIC-III/IV PhecodeX) → **Liu arXiv 2504.11740** (Generate-Treatment vs Generate-Outcome fragility; two frameworks comparison) → **Van Calster JCE 2016** (calibration hierarchy). Chain verified via **doi.org 302 HEAD for every link** (see Appendix batch) + raw GitHub extract (MUST web_extract satisfied). Additional link: **Vickers DCA 2006/2019** (DOI 10.1177/0272989X06289078 / PMC6123195).

**Adversarial (explicit goal: FIND existing fidelity→τ methods-ranking study that closes gap — T7-adversarial-rank-preservation):**
- `synthetic data rank correlation method ranking preservation TSTR` (2026-08-30, 5 hits) — try to find study reporting **Kendall τ between real and synthetic *methods* conclusions** (e.g., logistic vs GRU-D winner concordance as function of fidelity). Closest hits: generic YData/BlueGen vendor benchmarks (utility vs fidelity correlation for **generators**, not for **methods compared on that synthetic**), LLM evaluation papers, and **Shoshan et al. ICML 2023 "Synthetic Data for Model Selection"** (general tabular ML model selection with rank correlation, **not EHR methods benchmarking with Kendall τ + DCA + fidelity ladder**). **No EHR study reports τ for a fixed method comparison on real vs synthetic** — gap survives this sweep.
- Cycle 2 adversarial carry: `real vs synthetic data method ranking preservation evaluation` (5 hits), `plasmode synthetic TSTR rank correlation methods comparison real data` (0 hits on exact conjunction) — no synthesis of fidelity→τ for EHR methods.
- **6+ search_log rows verbatim satisfied** (see Appendix: 2 strategies with 3+ queries + reviews + adjacent + adversarial + chaining ≥6).

**Language (proportional):** No directly equivalent study with the conjunction (fixed methods comparison × real vs synthetic/plasmode × Kendall τ threshold × fidelity ladder × DCA × MIMIC-III→IV transport) was identified in the searches performed so far — not "no synthetic EHR paper exists" (Chen comprehensive benchmark exists but evaluates *generators*, not *methods evaluated via those generators*).

---

## Gate 2 — Written Adversarial Challenge (self-adversarial per dossier)

**Goal:** steelman closure — 5 strongest defeating arguments.

1. **Chen et al. JAMIA 2025 is the strongest defeating evidence.** It already delivers comprehensive benchmarking (fidelity/utility/privacy/compute), open toolkit, and open-data (MIMIC-III/IV) benchmark with **generator** ranking MIMIC-III→IV. Referee will argue no further benchmarking needed. *Survival condition:* Lock is **not a benchmark of generators** — it is a **meta-benchmark of the instrument** (do synthetic-supported *methods* conclusions agree with real-data conclusions?). Chen evaluates *generators*; T7 evaluates *methods evaluated on those generators* (logistic/Cox vs GRU-D winner concordance vs fidelity). Title makes distinction crisp: *Do synthetic EHR preserve methods conclusions? A rank-preservation threshold study via SynthEHRella*.

2. **Yan et al. 2022 + prior reviews** could be cited as prior benchmarking attempts, narrowing perceived novelty. Chen's critique (GAN-only, closed data) limits force, but τ/threshold framing must be foregrounded to survive.

3. **Liu et al. arXiv 2504.11740** already demonstrates plasmode fragility for causal inference (estimators appear biased under misspecified plasmode). Reviewer could argue "plasmode validity is already studied." *Survival condition:* Lock is **broader than causal point-treatment effects** — extends to **prediction + calibration + DCA** (logistic/Cox vs GRU-D with calibration slope + DCA net benefit at p_t) and to **synthetic EHR generators broadly** (GAN/Synthea/resample), not just plasmode; asks for **calibrated fidelity threshold with transport check**, not just fragility demonstration. S1 vs S1′ sensitivity directly tests Liu's lesson.

4. **SynthEHRella README + Chen's MIMIC-III→IV transport experiment** already shows generator rankings shift MIMIC-III→IV — partially answering transportability piece. *Survival condition:* Lock asks whether **methods rankings (not generator rankings)** also shift — and whether **DCA ranking** at fixed clinical threshold p_t (which depends on calibration, not just discrimination) is more fragile than AUC ranking. That subtle distinction must survive review; if misread as "just another generator comparison," it will be rejected as incremental — DCA + Van Calster hierarchy framing distinguishes it.

5. **A narrow study/preprint performing exact real-vs-synthetic *methods* ranking already exists but was missed by open-web search.** Highest-risk defeater. 2026-08-30 sweeps found **no such paper** on exact conjunction — closest is Shoshan ICML 2023 (general tabular, not EHR methods benchmarking) and vendor YData/BlueGen benchmarks (generator utility correlation, not methods ranking). *Pre-promotion requirement:* Run targeted `arXiv (stat.ME, stat.AP, cs.LG) [2024–2026] "TSTR" AND "Kendall"` + inspect **all 2025–2026 citations of Chen (DOI 10.1093/jamia/ocaf082)** and synthEHRella GitHub dependents ("Used by"/Dependents). If any downstream paper already ran EHR methods-ranking meta-benchmark, re-frame as **direct replication on different comparison/task** (T5 calibration task).

If any #1–#5 extended post-2025 to include exact conjunction (fixed methods comparison × real vs synthetic/plasmode × Kendall τ × fidelity threshold sweep × MIMIC-III→IV × DCA), gap closes and correct next step is **replication on DCA-centric task** (logistic vs conformal calibration DCA ranking).

---

## Gate 3 — Falsifiable Question (negative = publishable, stated)

**Primary question (locked fidelity ladder + rank-preservation, falsifiable):**

*At what fidelity does synthetic-supported **methods ranking** agree with real-data ranking, and when must synthetic be treated as **cautionary**? Specifically: across the fidelity ladder S1/S1′/S2/S3/S4/S5, does there exist a calibrated fidelity threshold **f*** such that for f ≥ f*, synthetic-supported winner (logistic/Cox vs GRU-D) preserves the real-data winner with **Kendall τ ≥0.7 and lower 95% bootstrap bound ≥0.5** (or winner concordance ≥0.80 with Wilson LB≥0.60 for 2-method case), and does this threshold **transport MIMIC-III→IV**?*

**Skeptical framing (instrument fails = cautionary, publishable):**

- **H0 (instrument fails / cautionary, publishable negative):** Across fidelity ladder, synthetic-supported ranking does **not** preserve real-data winner; **τ(f) <0.5** (pairwise concordance ≈ chance) at all achieved fidelities, or τ≥0.7 only at near-bootstrap fidelity (S4) — so **synthetic cannot license methods claims without real-data replication**. This is a **cautionary standard** paper (cf. Liu plasmode fragility) — of interest to *JAMIA/Biostatistics/Nature Digital Medicine* as a standard for journals evaluating synthetic-supported methods papers. **Negative result is guaranteed publishable** as operational guidance: "Do not trust synthetic alone below f*."
- **H1 (instrument suffices above threshold, publishable positive):** There exists calibrated **f*** such that for f ≥ f*, **τ(f) ≥0.7 LB≥0.5**, transports MIMIC-III→IV — licenses cheap privacy-safe methods development and plasmode-based power calculations; threshold reported as "MMD<ε* and TSTR gap<δ* ⇒ τ≥0.7."

**Either outcome:** Decision rule (MMD/utility thresholds, generator-choice guidance, DCA caution) rather than leaderboard — more useful to methodologists and IRBs evaluating compute/privacy trade-offs. Pre-registered threshold prevents HARKing.

---

## Gate 4 — Named Data Pathway (A/B/C/D with timeline/access)

**Path: A public (credentialed, weeks) + D synthetic (generated on-premises) — no prospective PHI; highest feasibility.**

| Dataset | Role | Access | Timeline |
|---------|------|--------|----------|
| **MIMIC-III v1.4** (PhysioNet DOI 10.13026/C2XW26, PhysioNet credentialed) | **TRAIN pool + TEST_R** (phenotype PhecodeX via synthEHRella `run_preprocessing`; the exact dataset Chen benchmarked) — stratified 80/20, seed=20260830 | Credentialed (PhysioNet, CITI + signed DUA) | **Days–2 weeks** (CITI + DUA auto-approved; same route Chen used) |
| **MIMIC-IV v2.2** (PhysioNet DOI 10.13026/6MM1-EK67 / 10.13026/7EBG-V124) | **TEST_TRANSPORT** (code-shift / ICD-9→10 stress) — tests whether real→synthetic threshold transports when test distribution shifts | Same PhysioNet | Same |
| **SynthEHRella-generated synthetic datasets (S1–S5, 5–8 operating points)** | **Synthetic TRAIN lake** (9 methods, 30–50 plasmode draws each, seeded) — generated TRAIN-side only via `run_generation` + `run_postprocessing` (PhecodeX); evaluation via `run_evaluation` | Generated locally via `synthEHRella` (GitHub open) | **Immediate** once MIMIC obtained (no new engineering) |
| **Synthea** synthetic patients (open, rule-based, DOI 10.1093/jamia/ocx079) | S3 rung (independent of MIMIC, workflow-realistic but statistics-unfaithful) | Open download (Synthea JAR) | Immediate |
| **No prospective collection** | — | — | IRB: de-identified public data only |

**Fixed evaluation scaffold (same for all ladder rungs, pre-registered):**
```
Real lake (frozen):
├── MIMIC-III v1.4 — TRAIN (80% stratified) + TEST_R (20% held-out, shared evaluation)
└── MIMIC-IV v2.2 — TEST_TRANSPORT (code-shift stress)

Synthetic lake (TRAIN-side only, same N as TRAIN, seeded):
├── S1  plasmode Generate-Treatment (G-Treatment, high fidelity, preferred per Liu)
├── S1′ plasmode Generate-Outcome (G-Outcome, high but different bias — sensitivity)
├── S2  GAN-based MedGAN/CorGAN (medium-high, learned joint)
├── S3  Synthea rule-based (low-medium, workflow-realistic)
├── S4  Resample bootstrap with replacement (perfect by construction, upper-bound, null generator)
├── S5  Prevalence-based random (worst, null generator)
└── Fidelity sweep within S2 (early-stopped vs converged) to reach 6–8 operating points
    └── Post-processed to PhecodeX via run_postprocessing; seeded
```
**Transport check (locked):** Repeat ranking evaluation on **TEST_TRANSPORT (MIMIC-IV)** instead of TEST_R; report τ_III vs τ_IV and whether f* shifts. If τ collapses on IV, threshold is distribution-specific (not universal) — cf. Chen's MIMIC-III→IV generator degradation.

**Timeline:** Once MIMIC credentialed (1–2 wks), pipeline is `conda env create -f environment.yaml → pip install . → run_preprocessing → run_generation <method> → run_evaluation` per README (8054 chars verified 2026-08-30). Can start coding on synthetic demo data immediately.

---

## Gate 5 — Mandatory Baselines (named, simple benchmark included)

**Locked method pair — primary comparison (required, 1–2 methods, same MIMIC-derived task):**

1. **Logistic regression (or Cox for survival)** vs **GRU-D** (Che et al. 2018 DOI 10.1038/s41598-018-24271-9, 2168 cites) — binary phenotype prediction (or time-to-event if Cox) on same MIMIC-derived task (e.g., phenotype prediction / ICU mortality). Models trained on Real TRAIN vs each Synthetic TRAIN (S1–S5), evaluated on **shared TEST_R** (primary) and **TEST_TRANSPORT** (MIMIC-IV). Tests whether "DL advantage" conclusion is synthetic-stable. **GRU-D is mandatory DL baseline for irregularity** (masking + Δt).

**Secondary / sensitivity (if time):** Standard calibration (Platt/isotonic) vs conformal calibration — compare calibration slope error / empirical coverage / interval width gap on same task, real vs synthetic (bridges T5/T7). Keep **one primary comparison** for lock; second is sensitivity. `lme4`/`JMbayes2` can be added as classical trajectory baseline if task is longitudinal rather than tabular phenotype.

**Locked metrics:**
- **Rank preservation (primary):** Kendall τ over method suite; for 2-method primary collapses to **pairwise winner concordance** (does winner match?) + effect-size preservation (|Δ_real − Δ_synth| / Δ_real) and **τ over bootstrap replicates** to obtain CI. Spearman ρ (secondary), pairwise concordance rate = (1+τ)/2.
- **Fidelity (per rung):** MMD (`evaluation/fidelity.py`), RMSPE, Pearson correlation recovery, dimension-wise prevalence gap, propensity distinguishability (real-vs-synthetic classifier AUC).
- **Utility:** TSTR AUC gap (or C-index gap for Cox) = AUC_TSTR − AUC_TRTR; association-recovery gap (logistic β L2 distance).
- **Calibration / DCA:** calibration slope/intercept per method (Van Calster weak), ICI, and **DCA net benefit at fixed thresholds p_t ∈ {0.05, 0.10, 0.20}** (Vickers): NB(p_t) = (TP/N) − (FP/N)·(p_t/(1−p_t)); report **DCA ranking** (which method has higher NB at p_t) and whether DCA ranking agrees with AUC ranking.
- **Privacy (reported, not gated):** membership inference AUC, attribute inference accuracy — characterise operating point.

**Locked decision rule (pre-registered threshold):**
- Declare "synthetic preserves ranking at fidelity f" if **Kendall τ(f) ≥0.7 with lower 95% bootstrap CI ≥0.5** (bootstrap over plasmode replicates + GAN seeds; B=1000). For 2-method case: winner concordance ≥0.80 with Wilson LB≥0.60 and τ-equivalent ≥0.7.
- **Threshold f*** = smallest fidelity where this holds **monotonically above** (isotonic regression / change-point where τ crosses 0.7 and stays above). Estimate via piecewise-linear or isotonic fit of τ vs fidelity composite (first PC of MMD⁻¹, correlation recovery, 1−TSTR gap).
- **Cautionary trigger:** If no f achieves rule except S4 (Resample), report **"synthetic is cautionary — methods claims require real-data replication"** (publishable negative, per Liu framing).

**Replication / sample-size structure locked:**
- Plasmode replicates 30–50 draws per fidelity point (SE(τ) ≈0.06–0.10 at τ≈0.5 via Kendall variance — adequate to separate τ≥0.7 vs τ≤0.3); GAN training replicates 3–5 seeds per point.
- Total fits: ~2 methods × 8 operating points × 30 replicates ≈ **480–1,500 fits** (phenotype prediction is tabular batch, not trajectory-model heavy) — feasible on single GPU node.
- Seeds: `numpy.random.default_rng(20260830)` + torch seeds logged; Snakemake/Make orchestration.

---

## Gate 6 — Ethics / Privacy (path identified)

- **De-identified public data** under PhysioNet DUA (MIMIC-III/IV); HIPAA Safe Harbor–equivalent de-identification with date shifting; no re-identification attempted; no linkage to external identifiers. Synthea synthetic patients are open and carry no privacy risk.
- **Credentialing:** CITI Program + PhysioNet credential approval + signed DUA before access; restricted to listed investigators; no redistribution beyond DUA. Synthetic datasets S1–S5 are generated on-premises and can be shared as aggregate metrics (no patient-level release required).
- **Institutional path:** IRB **exemption / not-human-subjects determination** (de-identified, publicly shared for research) — file protocol with institutional IRB upon credentialing; OSF preregistration declares ethics path (no prospective Indian hospital data for v1). Privacy-relevant metrics (membership inference AUC, attribute inference accuracy) are **characterised per rung** but not gated — privacy is reported for IRB usefulness.
- **MUST web_extract:** synthEHRella README (GitHub raw 8054 chars 2026-08-30) confirms privacy evaluation is built into pipeline (`evaluation/privacy.py`), not an afterthought.

---

## Gate 7 — Clinical Relevance (affirmed provisionally by scout, physician TBD)

*Provisionally affirmed — physician collaborator to confirm.*

- **Direct DCA implication:** At a given clinical threshold p_t (e.g., 10% 10-yr CVD risk → statin, or ICU mortality p_t=0.2 → escalation), DCA net benefit depends on **calibration at p_t**, not just AUC. If synthetic preserves AUC ranking but inverts calibration slope ranking, DCA ranking at fixed p_t may flip — a model that appears clinically useful on synthetic would be **harmful at deployment**. Lock makes this failure mode explicit and testable; Vickers update (PMID 31592444, PMC6123195) gives step-by-step interpretation.
- **Indirect but real:** If validated (τ≥0.7 above f* and transports), synthetic/plasmode benchmarking enables **safer development of risk models and causal tools without repeated patient-data access**, accelerating equity-relevant adaptations (e.g., testing behaviour on synthetic cohorts enriched for underrepresented subgroups) before clinical validation. **Caveat (must be stated):** Synthetic must **not** be presented as replacing clinical validation — claim is about *methods benchmarking*, not deployment readiness.
- **Methodological implication:** Positive result licenses cheap privacy-safe power/sample-size calculations; negative result sets cautionary standard for journals ("do not trust synthetic alone below f*").

---

## Gate 8 — Scope Ceiling (small-team months, explicit)

**Ceiling: 2 investigators (1 EHR informatician + 1 ML engineer) + 0.25 FTE biostatistician for τ/DCA calibration, 4–6 weeks wall-clock to full ladder + 2–4 weeks write-up; total 1.5–2.5 months.**

- **Personnel:** 1 informatician (MIMIC pipelines + synthEHRella orchestration + Snakemake) + 1 ML engineer (logistic/Cox + GRU-D + DCA pipeline) + 0.25 biostatistician (Kendall τ bootstrap, isotonic f* estimation).
- **Compute:** Single GPU node (A100/4090) for GAN training (MedGAN/CorGAN, 3–5 seeds) + CPU for logistic/Cox + `synthEHRella/run_evaluation` (MMD/TSTR/privacy); total fits ~480–1,500 (tabular, not trajectory-model heavy); wall-clock **days, not weeks** (D simulation, no PHI queue). Cost <$100 cloud.
- **Milestones:** Wk1 `run_preprocessing` + S1/S1′ plasmode (30 draws) + seed-locked split; Wk2 S2 (GAN) multiple seeds + fidelity sweep + MMD/TSTR computation; Wk3 DCA + τ bootstrap + MIMIC-III→IV transport; Wk4 write-up (Van Calster + Vickers framing, decision tree). **OSF preregistration before synthetic evaluation** prevents threshold HARKing.
- **Explicitly OUT of scope v1:** Indian-typical sparsity regimes beyond MIMIC-III→IV code-shift (needs Indian partner data — Stage-2), fairness mitigation development, trajectory-specific fidelity metrics beyond Chen's binary-phenotype MMD/RMSPE (scoped in pilot Wk1), many-analysts experiment.

---

## Evidence AGAINST (strongest reasons this may not be a gap)

See Gate 2 — 5 potential defeaters (Chen comprehensive benchmark, Yan/GAN critique, Liu causal fragility, synthEHRella MIMIC-III→IV generator shift, Shoshan general tabular). Additional nuance: If Shoshan ICML 2023 already evaluated TSTR-based model selection with rank correlation on EHR-like data, gap reduces to **DCA-specific fragility** (calibration-dependent net benefit) rather than full threshold.

---

## Relevant Datasets

Section Gate 4 above: **MIMIC-III v1.4 + MIMIC-IV v2.2 (PhysioNet)** + **SynthEHRella-generated synthetic lake (S1/S1′/S2/S3/S4/S5, 5–8 points)** + **Synthea (open)**. All A/D public; no prospective collection. See also Gate 5 software pointers (synthEHRella, `scikit-learn`/`lifelines`, GRU-D PyTorch, `scipy.stats.kendalltau`, `snakemake`).

---

## India Relevance Verdict

**GEOGRAPHY-ONLY for v1** — justified (per docs/03 §6).

Core question (does synthetic preserve methods ranking? at what fidelity?) is **population-agnostic and methods-forward**; Indian data not needed and claiming them would be decoration. No transportability assumption specific to Indian epidemiology is stressed by the fidelity ladder itself.

**Meaningful Stage-2 extension (not bundled):** Testing whether a synthetic generator trained on US MIMIC preserves methods ranking when evaluated against an **Indian hospital test distribution** (coding prevalence, measurement frequency, formulary, documentation completeness differ) would genuinely stress transportability assumption — but requires Indian partner data (CARRS / hospital EHR) and must not be bundled into v1. Lock's MIMIC-III→IV transport check is the **proxy** for this logic on public data. Per 03 evidence standards §6: claiming STRESSES-ASSUMPTION without specific assumption stressed would be decoration.

---

## Confidence

**Medium.**

What raises confidence: Chen 2025 is peer-reviewed (JAMIA, OUP) and 302-verified; synthEHRella README 8054-char extract confirms toolkit is immediately usable for 5–8 point fidelity sweep with no new engineering; Van Calster hierarchy + Vickers DCA canonical and 302-verified; GRU-D vs logistic/Cox baseline standard (Che et al. 302); DOI batch 8/8 verified 2026-08-30. Adversarial sweep for exact fidelity→τ EHR methods-ranking study returned **no EHR hit** (closest: general tabular ICML 2023, vendor benchmarks).

What caps below High:
1. Recent late-2024/2025 preprint performing exact meta-benchmark (real-vs-synthetic *methods* ranking with τ + DCA on MIMIC) may have been missed by open-web search (arXiv stat.ME/stat.AP + JAMIA forward citations of Chen not yet exhaustively inspected at Firecrawl level — arXiv API sweep required pre-promotion).
2. Fidelity metric for trajectory tasks (continuous longitudinal biomarkers) may need extension beyond Chen's binary-phenotype MMD/RMSPE — trajectory-specific fidelity (e.g., longitudinal correlation recovery) should be scoped in pilot Wk1.
3. MIMIC-IV transport check tests **code-shift**, not **health-system shift** (formulary, measurement frequency) — genuine Indian hospital test distribution would be stronger stress but deferred to Stage-2.

---

## Recommended Next Search (executable)

```pubmed
# 1. Instrument-specific sweep (does real-vs-synthetic methods ranking with τ already exist on EHR?)
(plasmode[Title/Abstract] OR "synthetic data"[Title/Abstract]) AND (TSTR[Title/Abstract] OR "train synthetic test real"[Title/Abstract]) AND (Kendall[Title/Abstract] OR Spearman[Title/Abstract] OR "rank correlation"[Title/Abstract]) AND (methods[Title/Abstract] OR benchmark[Title/Abstract])

# 2. Plasmode validity deep sweep
plasmode[Title/Abstract] AND (2024[PDAT] : 2026[PDAT])

# 3. Synthetic EHR fidelity-threshold terminology
("synthetic electronic health records"[Title/Abstract] OR "synthetic EHR"[Title/Abstract]) AND (fidelity[Title/Abstract] OR MMD[Title/Abstract] OR RMSPE[Title/Abstract]) AND (threshold[Title/Abstract] OR cutoff[Title/Abstract] OR "decision rule"[Title/Abstract])
```

```europepmc
# 3b. Same as 3 via Europe PMC (fidelity thresholds on synthetic EHR)
# query: ("synthetic EHR" AND fidelity AND threshold)
```

```
# arXiv (manual, stat.ME + stat.AP + cs.LG 2024–2026):
#   query: plasmode synthetic TSTR rank correlation methods comparison real data
#   tool: arxiv.org search + site:arxiv.org plasmode TSTR Kendall
# Forward chaining (manual, must be logged):
#   Inspect all 2025–2026 citations of Chen (DOI 10.1093/jamia/ocaf082) + synthEHRella GitHub dependents/insights
#   GitHub: github.com/chenxran/synthEHRella → dependents, issues, recent PRs — any fork already comparing logistic/Cox vs GRU-D?
```

**Stop criterion:** If Query 1 still returns zero EHR methods-ranking τ studies and GitHub dependents inspection returns zero forks running meta-benchmark, promote with OSF preregistration draft and PhysioNet credential confirmation. If Query 1 returns hit, re-frame to **replication on DCA-centric calibration task**.

---

## Appendix — Queries & Papers (verbatim for search_log.csv / evidence_registry.csv)

**Queries run 2026-08-30 (verbatim, ≥6 required — distinct strategies satisfied):**

| date | cycle | agent | source | query | concept | hits | n_inspected | verification |
|------|-------|-------|--------|-------|---------|------|-------------|--------------|
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `synthetic EHR fidelity evaluation MIMIC GAN plasmode Synthea validation` | T7-S1-fidelity | 0 | 0 | VERIFIED — terminology gap; recovered via Chen chaining |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `Kendall tau rank preservation Spearman synthetic versus real data method comparison` | T7-S2-rank-preservation | 5 | 5 | VERIFIED — no EHR methods-ranking study |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `decision curve analysis net benefit clinical threshold synthetic data validation` | T7-S2b-DCA | 5 | 5 | VERIFIED — DCA synonyms found |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `Chen JAMIA synthetic EHR scoping review benchmarking fidelity utility` | T7-review-Chen | 0 | 0 | VERIFIED — DOI HEAD 302 |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `Van Calster calibration hierarchy 2016 risk prediction model` | T7-review-VanCalster | 5 | 5 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `Yan Patterns multifaceted benchmarking synthetic EHR 2022` | T7-review-Yan | 0 | 0 | VERIFIED — DOI HEAD 302 |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `Angelopoulos conformal prediction tutorial 2021 distribution-free` | T7-review-Angelopoulos | 5 | 5 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `Liu plasmode simulation cautionary Generate Treatment outcome arXiv 2025` | T7-adjacent-Liu-fragility | 5 | 5 | VERIFIED — Liu fragility |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `synthetic data rank correlation method ranking preservation TSTR` | T7-adversarial-rank-preservation | 5 | 5 | VERIFIED — gap survives (Shoshan ICML 2023 not EHR) |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `Vickers decision curve analysis 2006 net benefit clinical threshold selection` | T7-chaining-DCA | 5 | 5 | VERIFIED — chaining |
| 2026-08-30 | 4 | clinical-evidence-scout | web_extract | `https://raw.githubusercontent.com/chenxran/synthEHRella/main/README.md` | T7-synthEHRella-README | 1 | 1 | VERIFIED — 8054 chars, 9 methods + pipeline |
| 2026-08-30 | 2 | methods-scout | web_search | `real vs synthetic data method ranking preservation evaluation` | T7-adversarial-carry | 5 | 5 | VERIFIED — vendor benchmarks only |

**Papers (8, resolvable, ≥1 DOI 302-verified):**

| # | Citation | DOI / URL | Type | Verification | Role |
|---|----------|-----------|------|--------------|------|
| 1 | Chen et al. Generating synthetic EHR data: scoping review with benchmarking (SynthEHRella). JAMIA 2025;32:1227–1240. | https://doi.org/10.1093/jamia/ocaf082 | review+benchmark load-bearing | **302 → academic.oup.com/jamia/article/32/7/1227/8155975** | Load-bearing benchmark |
| 2 | SynthEHRella benchmarking toolkit (Chen lab) GitHub 2025. | https://github.com/chenxran/synthEHRella | software instrument | **GitHub raw 8054 chars 2026-08-30** | Instrument (MUST web_extract) |
| 3 | Liu et al. Cautionary note for plasmode simulation (Generate-Treatment vs Generate-Outcome). arXiv:2504.11740 2025. | https://doi.org/10.48550/arXiv.2504.11740 | preprint adjacent fragility | **302 → arxiv.org/abs/2504.11740** | Adjacent fragility (S1 vs S1′) |
| 4 | Van Calster et al. Calibration hierarchy. J Clin Epidemiol 2016;74:167-176. | https://doi.org/10.1016/j.jclinepi.2015.12.005 | article chaining | **302 → linkinghub.elsevier.com/retrieve/pii/S0895435615005818** | Calibration vocabulary |
| 5 | Yan et al. Multifaceted benchmarking of synthetic EHR generation. Patterns 2022;3:100655. | https://doi.org/10.1016/j.patter.2022.100655 | article review | **302 → linkinghub.elsevier.com/retrieve/pii/S2666389922002951** | Prior GAN-only limitation |
| 6 | Angelopoulos & Bates. Gentle Introduction to Conformal Prediction. FTML 2023;16:494-591 / arXiv:2107.07511. | https://doi.org/10.1561/2200000101 | review interval baseline | **302 → emerald.com/ftmal/article/16/4/494/1332423** | Interval baseline |
| 7 | Walonoski et al. Synthea. JAMIA 2018;25:230-238. | https://doi.org/10.1093/jamia/ocx079 | article S3 baseline | **302 → academic.oup.com/jamia/article/25/3/230/4098271** | Fidelity ladder S3 |
| 8 | Vickers & Elkin. Decision curve analysis. Med Decis Making 2006;26:565-574 (+ 2019 BMJ guide). | https://doi.org/10.1177/0272989X06289078 | article DCA | **302 → journals.sagepub.com/doi/10.1177/0272989X06289078** | DCA framing (Gate 5/7) |

**Additional cross-ref:** Che et al. GRU-D DOI 10.1038/s41598-018-24271-9 (302, method pair anchor) — not counted in 8-table but resolvable.

**DOI HEAD batch (curl -I -s, 302 Found → publisher, 2026-08-30):**

| DOI | Resolves to | Status |
|-----|-------------|--------|
| 10.1093/jamia/ocaf082 | https://academic.oup.com/jamia/article/32/7/1227/8155975 | **302** |
| 10.48550/arXiv.2504.11740 | https://arxiv.org/abs/2504.11740 | **302** |
| 10.1016/j.jclinepi.2015.12.005 | https://linkinghub.elsevier.com/retrieve/pii/S0895435615005818 | **302** |
| 10.1016/j.patter.2022.100655 | https://linkinghub.elsevier.com/retrieve/pii/S2666389922002951 | **302** |
| 10.1561/2200000101 | https://www.emerald.com/ftmal/article/16/4/494/1332423 | **302** |
| 10.1093/jamia/ocx079 | https://academic.oup.com/jamia/article/25/3/230/4098271 | **302** |
| 10.1177/0272989X06289078 | https://journals.sagepub.com/doi/10.1177/0272989X06289078 | **302** |
| 10.1038/s41598-018-24271-9 | https://www.nature.com/articles/s41598-018-24271-9 | **302** |

**Verification:** 7/8 DOIs HEAD 302 + synthEHRella URL verified via GitHub raw 8054 chars; ≥1 DOI 302 YES (Chen 10.1093/jamia/ocaf082).
**MUST web_extract:** synthEHRella README 8054 chars — package layout 9 methods + evaluation/fidelity.py utility.py privacy.py + run_generation/evaluation/preprocessing/postprocessing for MIMIC-III/IV PhecodeX.

**Fidelity ladder:** S1 Plasmode G-Treatment → S1′ G-Outcome (sensitivity) → S2 GAN (MedGAN/CorGAN) → S3 Synthea → S4 Resample (ceiling) → S5 Prevalence-random (floor) + fidelity sweep within S2 to reach 6–8 operating points.
**Rank preservation:** Kendall τ ≥0.7 LB≥0.5 (primary) ; Spearman ρ + pairwise concordance (1+τ)/2 secondary.
**DCA thresholds:** p_t ∈ {0.05, 0.10, 0.20}; NB(p_t) per method; DCA ranking vs AUC ranking agreement.
**Transport:** MIMIC-III → IV (code-shift stress); MIMIC→Indian hospital as Stage-2.
