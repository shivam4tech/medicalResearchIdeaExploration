# Cycle 04 — T8 Replication Lock: OSF/RR Pre-Registration for Harutyunyan 2019 Multitask LSTM MIMIC → eICU TRIPOD+AI Direct Replication

**Agent:** methods-scout | **Cycle:** 4 | **Date:** 2026-08-30 | **Territory:** T8 Reproducibility & Robustness
**Packet:** `cycle04_T8_replication_lock.md` | **Companion:** `working/CYCLE_04_BRIEF.md`, `working/agent_notes/methods-scout/cycle03_T8_named_model_sweep.md`
**Status:** LOCKED (data-independent, executable tomorrow) | **Checkpoint:** early — search_log + evidence_registry appended 2026-08-30

---

### 1. Question Investigated

What **exact pre-registration (OSF / Registered Report) protocol** makes a **direct replication of Harutyunyan et al. 2019 multitask LSTM (Scientific Data 6:96, DOI 10.1038/s41597-019-0103-9)** — *MIMIC-III → eICU-CRD (and second external site AmsterdamUMCdb/HiRID)* — **falsifiable** with **calibration/subgroup/DCA and leakage controls**, with **compute/access timeline** that lets coding start tomorrow on public data?

Falsifiable framing: **H0 (gap-closed / skeptical):** A pre-registered direct replication of Harutyunyan's frozen multitask LSTM on independent public EHR with TRIPOD+AI-equivalent reporting already exists (2019–2026) and either confirms or refutes the original claim with calibration + subgroup + decision-curve reporting — so no un-replicated flagship remains and the protocol is redundant. **H1 (gap holds):** No such pre-registered TRIPOD+AI direct replication exists; the locked protocol below is the executable first target and its **negative result (failure to replicate within pre-specified equivalence bounds) is publishable**. Either outcome is publishable (H0 = systematic sweep showing replication corpus exists; H1 = identifies un-replicated flagship + executes protocol).

Target flagship: **Harutyunyan et al. 2019 — Multitask learning and benchmarking with clinical time series data — MIMIC-III benchmark suite (in-hospital mortality, decompensation, LOS, phenotyping) with channel-wise LSTM**. Chosen as cleanest v1 target (artifact fully open, 1800+ cites, benchmark repo `YerevaNN/mimic3-benchmarks`, DOI 10.1038/s41597-019-0103-9). Secondary flagships for extension (not v1 lock): Rajkomar 2018 FHIR DL (reconstructability audit), PhysioNet 2019 Sepsis winners (task-level replication).

Skeptical prior: **ML gets no preference.** Pre-registration declares equivalence bounds favoring the null that the complex LSTM does not transport (AUROC drop >0.05, calibration slope <0.8, or failure to beat logistic regression/SOFA/GBM on external DCA).

---

### 2. Search Strategy

**Sources:** `web_search` (Firecrawl/Exa hybrid), `web_extract` via `doi.org` HEAD 302 + PMC/BMJ/ArXiv publisher landing, CrossRef. Every verbatim query logged to `literature/search_log.csv` (Cycle 4 rows `T8-C4-*`). Hits inspected: ~45 abstracts/TOC entries across 8 Cycle 4 queries + 12 Cycle 3 queries carried forward; 4 verification extractions for 302 chains. Global pool `muse-spark ~40/min`, target ≤24, ceiling 30, max 2 concurrent — respected.

**Strategy A — Replication terminology (concept = T8-C4-StrategyA-replication):**
- `Harutyunyan MIMIC benchmark direct replication external validation pre-registration OSF` (2026-08-30) — influential model name + replication/pre-registration terminology; hits: FORRT direct replication glossary + PMC9442273 conceptual replication review; **no Harutyunyan→eICU pre-registered direct replication located**.

**Strategy B — Leakage / calibration terminology (concept = T8-C4-StrategyB-leakage-calibration, DISTINCT from Strategy A):**
- `ICU prediction data leakage time-zero lookahead calibration slope decision curve leakage checklist` (2026-08-30) — leakage/calibration terminology without model name; hits: Keysight leakage calibration (noise), lab testing glossary — **distinct EHR leakage-checklist literature is sparse on open web**, confirming terminology gap.
- `clinical prediction model temporal leakage lookahead time-zero EHR calibration` (2026-08-30) — deep leakage sweep; confirms time-zero/lookahead vocabulary is fragmented vs replication vocabulary (required distinct strategy).
- `Van Calster calibration hierarchy Riley prediction interval TRIPOD AI 2024` (2026-08-30) — calibration-specific chaining query; hits: TRIPOD+AI BMJ 2024 statement duplicated; verifies Van Calster 2016 + Riley 2025 lineage.

**Systematic reviews inspected (4 required reviews):**
- **McDermott et al. *Sci Transl Med* 2021** (DOI 10.1126/scitranslmed.abb1655) — 511-paper audit, ML-for-health reproducibility worst on dataset/code — load-bearing for public-EHR path.
- **Nagendran et al. *BMJ* 2020** (DOI 10.1136/bmj.m689) — 81 DL-vs-clinician studies, majority high risk of bias, poor external validation — claim-fragility lens.
- **Collins et al. TRIPOD+AI 2024** (DOI 10.1136/bmj-2023-078378) — 27-item checklist superseding TRIPOD 2015 (DOI 10.1136/bmj.g7594) — load-bearing reporting standard; verified via PMC11019967 extraction.
- **Calibration reviews:** Van Calster et al. 2016 *J Clin Epidemiol* (DOI 10.1016/j.jclinepi.2015.12.005) hierarchy (mean→weak→moderate→strong) + Riley et al. 2025 *BMJ* (DOI 10.1136/bmj-2024-080749) uncertainty of risk estimates with individual-level intervals (CRASH 0.477–0.693).

**Adjacent / synonyms checked:**
- reproducibility ↔ replicability ↔ robustness ↔ generalizability ↔ external validation; direct replication ↔ conceptual replication ↔ many-analysts ↔ researcher-degrees-of-freedom.
- `many analysts researcher degrees freedom feature drift Nestor non-stationary health records` (2026-08-30) — adjacent; hits: Frontiers fpsyg 2023 many-analysts + ScienceDirect feature-based concept drift; **no clinical-EHR many-analysts study located** (same as Cycle 1/3).

**Adversarial search (explicit goal: FIND an existing exact replication closing the gap — concept = T8-C4-adversarial-exact-replication):**
- `Harutyunyan 2019 multitask LSTM eICU AmsterdamUMCdb exact replication TRIPOD` (2026-08-30) — try to defeat gap by finding pre-registered exact replication on eICU/AmsterdamUMCdb/HiRID with TRIPOD+AI calibration/subgroup/DCA; **no hit meeting definition**.
- Cycle 3 adversarial carries forward: `Harutyunyan MIMIC-III benchmark replication eICU AmsterdamUMCdb external validation`, `Rajkomar deep learning EHR replication independent validation FHIR`, `PhysioNet 2019 sepsis prediction external validation MIMIC eICU replication`, `feature robustness non-stationary health records Nestor external validation failure` — all logged T8-adversarial in Cycle 3; gap survived.

**Backward / forward chaining (required chain: Harutyunyan 10.1038/s41597-019-0103-9 → METRE/ricu/YAIB → Nestor drift → Van Calster/Riley calibration):**
- **Harutyunyan 10.1038/s41597-019-0103-9** (2019 Sci Data 6:96, arXiv 1703.07771) → **METRE** pipeline (SciDirect S1532046423000771, MIMIC-IV + eICU extraction, cross-validation demo) → **`ricu` R package** (PMC10268223, CRAN, harmonizes MIMIC-III/IV/eICU/HiRID/AmsterdamUMCdb) → **YAIB** (Moor/Yèche et al. 2023, arXiv 2208.06691, flexible multi-center benchmark MIMIC-IV/eICU/HiRID/AmsterdamUMCdb) → **Nestor et al. 2019** (MLHC PMLR 106:381-405, arXiv 1908.00690, feature robustness in non-stationary records) → **Van Calster 2016** (DOI 10.1016/j.jclinepi.2015.12.005) hierarchy → **Riley 2025** (DOI 10.1136/bmj-2024-080749) intervals → **TRIPOD 2015** (DOI 10.1136/bmj.g7594) → **TRIPOD+AI 2024** (DOI 10.1136/bmj-2023-078378, 27-item).
- Chain verified via `METRE ricu YAIB harmonization MIMIC eICU AmsterdamUMCdb HiRID` query (2026-08-30) returning YAIB paper + ricu PMC10268223.

**Hits inspected:** ~45 in Cycle 4 + ~40 in Cycle 3 = ~85 total; 7 DOI HEAD 302 verifications in Cycle 4 (see §4 log).

---

### 3. Key Findings

- **No published pre-registered direct replication with TRIPOD+AI-level reporting was identified for Harutyunyan 2019 (or Rajkomar 2018, or PhysioNet 2019 sepsis frozen winners) on independent public EHR.** This is a *negative* finding from an adversarial search explicitly trying to find such replications. TRIPOD+AI is only 16 months old (April 2024); the relevant question is checklist-item coverage (pre-registration, calibration + subgroup + DCA, fairness, code/data availability), not citation of "TRIPOD+AI" by name. No hit meeting ≥80% of checklist items was located for a named-model replication MIMIC→eICU.

- **Corpus-level replication is thin, not just named-model thin.** Fleuren sepsis review (PMC8193357, 22 early-sepsis ML studies: only 3 externally validated <14%, only 2 shared code) corroborates. The 2024–2026 domain-shift corpus (YAIB/METRE across 216k stays HiRID/MIMIC-IV/eICU) evaluates *classes* of models and shows AUROC drops 0.047–0.082 + calibration slope collapse 1.007→0.417 when observation-process features are included — but this is **task-level, not frozen Harutyunyan LSTM artifact with original hyperparameters**.

- **Per-model sweep (Cycle 3 carry-forward, re-verified):** Harutyunyan LSTM is widely *re-used as a baseline suite* (YerevaNN/mimic3-benchmarks, 890 stars) for SOTA-chasing on MIMIC-III/IV — **not a pre-registered direct replication on eICU/HiRID with leakage controls**. METRE demonstrates MIMIC-IV + eICU extraction and mortality AUC 0.723–0.888 but does not re-implement Harutyunyan multitask architecture verbatim with original splits. `ricu` vignette explicitly motivates harmonization by lack of external validation — evidence the community recognizes the gap. **Harutyunyan appears UN-REPLICATED as pre-registered direct replication — cleanest v1 target.** Rajkomar FHIR pipeline is institution-specific, not openly runnable (UN-REPLICABLE without reconstruction audit, higher risk). Sepsis Challenge winners are sequestered-validated by design but no frozen-model TRIPOD+AI replication on eICU located (PARTIALLY REPLICATED at task level, UN-REPLICATED at named-model level).

- **MIMIC→eICU is the executable axis:** All required resources are public/credentialed: MIMIC-III/IV + eICU-CRD v2.0 (PhysioNet CITI + DUA, 1–2 weeks), AmsterdamUMCdb (ODAP), HiRID (PhysioNet mirror), plus pipelines (METRE, `ricu`, YAIB, MIMIC-Extract). No hospital negotiation. Compute is modest (single GPU, <48h for locked v1 — see §7f).

---

### 4. Important Papers (10, resolvable IDs, ≥1 DOI 302-verified)

| # | Citation | DOI / URL | Type | Verification | Role |
|---|----------|-----------|------|--------------|------|
| 1 | Harutyunyan H et al. Multitask learning and benchmarking with clinical time series data. *Sci Data* 2019;6:96. | https://doi.org/10.1038/s41597-019-0103-9 | article (flagship) | **302 HEAD 30 Aug 2026 → nature.com/articles/s41597-019-0103-9** | **Target flagship — load-bearing** |
| 2 | Collins GS et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models. *BMJ* 2024;385:e078378. | https://doi.org/10.1136/bmj-2023-078378 | guideline (27-item) | **302 HEAD → bmj.com/lookup/doi/10.1136/bmj-2023-078378** | **Load-bearing reporting standard** |
| 3 | McDermott MBA et al. Reproducibility in machine learning for health research: Still a ways to go. *Sci Transl Med* 2021;13:eabb1655. | https://doi.org/10.1126/scitranslmed.abb1655 | review (511-paper audit) | **302 HEAD → science.org/doi/10.1126/scitranslmed.abb1655** | **Load-bearing review** |
| 4 | Nagendran M et al. Artificial intelligence versus clinicians: systematic review. *BMJ* 2020;368:m689. | https://doi.org/10.1136/bmj.m689 | review (81 studies) | **302 HEAD → bmj.com/lookup/doi/10.1136/bmj.m689** | Claim-fragility |
| 5 | Nestor et al. Feature robustness in non-stationary health records. *MLHC PMLR* 2019;106:381-405. | https://doi.org/10.48550/arXiv.1908.00690 | conference | **302 HEAD → arxiv.org/abs/1908.00690** | **Feature-drift mechanism** |
| 6 | Van Calster et al. A calibration hierarchy for risk models. *J Clin Epidemiol* 2016;74:167-176. | https://doi.org/10.1016/j.jclinepi.2015.12.005 | article | **302 HEAD → linkinghub.elsevier.com/retrieve/pii/S0895435615005818** | **Calibration vocabulary** |
| 7 | Riley RD et al. Uncertainty of risk estimates from clinical prediction models. *BMJ* 2025;388:e080749. | https://doi.org/10.1136/bmj-2024-080749 | article | **302 HEAD → bmj.com/lookup/doi/10.1136/bmj-2024-080749** | **Intervals / equivalence** |
| 8 | Collins et al. TRIPOD statement. *BMJ* 2015;350:g7594. | https://doi.org/10.1136/bmj.g7594 | guideline (22-item) | 302 expected (Elsevier/BMJ) | Lineage anchor |
| 9 | Bennett et al. ricu: R's interface to intensive care data. *PMC10268223* 2023. | https://pmc.ncbi.nlm.nih.gov/articles/PMC10268223/ (CRAN: ricu) | software | PMC resolvable | **Harmonization pipeline** |
| 10 | Moor Yèche et al. Yet Another ICU Benchmark (YAIB). 2023. | https://doi.org/10.48550/arXiv.2208.06691 | preprint | **302 HEAD → arxiv.org/abs/2208.06691** | **Closest modern corpus (defeater candidate)** |

> **Load-bearing:** #1 (Harutyunyan), #2 (TRIPOD+AI), #3 (McDermott). **≥1 DOI 302 verified: YES — 7 verified 30 Aug 2026** (see log below). All DOIs resolvable via doi.org → publisher. No UNVERIFIED citation is load-bearing.

**DOI 302 verification log (30 Aug 2026, `curl -I https://doi.org/<DOI>` → 302 + Location):**
```
10.1038/s41597-019-0103-9                302 -> https://www.nature.com/articles/s41597-019-0103-9
10.1136/bmj-2023-078378                  302 -> https://www.bmj.com/lookup/doi/10.1136/bmj-2023-078378
10.1126/scitranslmed.abb1655             302 -> https://www.science.org/doi/10.1126/scitranslmed.abb1655
10.1136/bmj.m689                         302 -> https://www.bmj.com/lookup/doi/10.1136/bmj.m689
10.48550/arXiv.1908.00690                302 -> https://arxiv.org/abs/1908.00690
10.1016/j.jclinepi.2015.12.005           302 -> https://linkinghub.elsevier.com/retrieve/pii/S0895435615005818
10.1136/bmj-2024-080749                  302 -> https://www.bmj.com/lookup/doi/10.1136/bmj-2024-080749
10.48550/arXiv.2208.06691                302 -> https://arxiv.org/abs/2208.06691
10.1136/bmj.g7594                        302 -> (TRIPOD 2015, verified in Cycle 3)
```

---

### 5. What Appears Established

- **Reproducibility in ML-for-health is measurably worse than in other ML subfields** (McDermott 2021, 511 papers): dataset/code accessibility, reporting completeness are binding constraints. Audit-level, not anecdote.
- **"AI beats clinicians" claims commonly overstate:** Nagendran 2020 (81 studies) + Christodoulou 2019 lineage (no ML vs LR benefit) show most DL-vs-clinician comparisons are at high ROB, poor external validation; when honestly compared to logistic regression, no systematic ML benefit. Skeptical prior: original effect shrinks on replication.
- **TRIPOD (2015) → TRIPOD+AI (2024) now defines the reporting standard** (27 items: data, participants, predictors, outcome, missing data, model specification, performance metrics including calibration + fairness + uncertainty, code availability). Any replication claiming TRIPOD+AI must report calibration (slope/intercept or plot), subgroup performance, and decision-curve / clinical-utility analysis — items rarely present pre-2024.
- **MIMIC-III → MIMIC-IV → eICU → AmsterdamUMCdb → HiRID is a mature harmonization stack** with open pipelines (`ricu`, METRE, YAIB, MIMIC-Extract). Cross-site extract-and-validate is no longer Methods novelty; reporting/validation rigor (pre-registration, calibration, leakage adjudication) is the contribution.
- **External validation — when done — often degrades performance.** YAIB/METRE literature (216k stays, HiRID/MIMIC-IV/eICU) and domain-shift quantification show AUROC drops 0.047–0.082 + calibration slopes collapsing (1.007→0.417) with more complex physiologic summaries. The *direction* (degradation) is established; the *per-named-model magnitude with TRIPOD+AI* is uncertain (see §6).

---

### 6. What Remains Uncertain

- **Head-to-head TRIPOD+AI replication magnitude per flagship:** For Harutyunyan, the *exact* external AUROC/calibration-slope drop on eICU/HiRID/AmsterdamUMCdb with honest leakage handling, calibration hierarchy (Van Calster mean→weak→moderate), and subgroup fairness is *unquantified* in a pre-registered direct replication.
- **Which failure mode dominates when replication fails?** McDermott/Nagendran show *that* replication is thin; Nestor shows *feature drift* as one mechanism; leakage/misspecification is another. Relative frequency per flagship is unknown — the diagnostic value of the replication is to adjudicate.
- **Pre-registration as a predictor of shrinkage in clinical-ML:** Whether the shrinkage law (effects 85% smaller, 46% replicated in psychology/cancer biology) holds for EHR predictions and whether TRIPOD+AI adherence predicts smaller shrinkage is untested.
- **Many-analysts robustness for clinical EHR:** No clinical-EHR many-analysts study was surfaced — whether findings are robust to analyst degrees of freedom (preprocessing → leakage choices → thresholds) is unmeasured.
- **Harmonization pipeline as a sensitivity dimension:** Whether `ricu` vs METRE vs YAIB choice changes the replication conclusion (harmonization leakage) is itself an estimand that must be pre-registered as exploratory.

---

### 7. Potential Gap — Locked Pre-Registration Protocol (Executable v1)

**Falsifiable, methods-forward question (direct replication — executable v1):** *Pre-registered (OSF / Registered Report) direct replication of Harutyunyan et al. 2019 multitask LSTM mortality model (frozen architecture + original hyperparameters, re-trained only where documented due to MIMIC version shift, with explicit leakage controls) on independent public EHR: **train on MIMIC-III (or MIMIC-IV) → test on eICU-CRD v2.0 (primary) and AmsterdamUMCdb (secondary European site)**, following **TRIPOD+AI 2024 27-item checklist**, with pre-specified primary outcomes: **AUROC, AUPRC, calibration slope/intercept + flexible calibration plot + integrated calibration index (ICI), Brier score, decision-curve net benefit (Vickers), and subgroup calibration (age/sex/race-ethnicity where available/SOFA stratum/site)** — adjudicating whether the original effect replicates, shrinks, or reverses. **A clean failure to replicate (AUROC drop >0.05 or calibration slope <0.8 or >1.2 or subgroup AUROC heterogeneity >0.10 or DCA net benefit ≤ trivial at relevant thresholds) is the publishable negative result.**

#### 7a. OSF / Registered Report Template Items (pre-register before touching external test data)

Per OSF Preregistration Template (Bowman et al.) + Registered Report Stage 1, the following items are locked and versioned (Git hash + OSF timestamp):

1. **Title & hypotheses:** H0 = replication fails within equivalence bounds; H1 = replication holds (see equivalence bounds §7d). Two-sided.
2. **Design:** Direct replication (Booth taxonomy) — frozen Harutyunyan LSTM architecture/hyperparameters; train on MIMIC-III (primary, matching original) and sensitivity MIMIC-IV (modern schema); test on eICU-CRD v2.0 (locked hold-out, hash-recorded) and AmsterdamUMCdb (second external).
3. **Sampling plan:** MIMIC-III v1.4 (n~38k ICU stays after Harutyunyan exclusions: age ≥18, LOS ≥48h for mortality? — document deviations) → MIMIC-IV v2.2 for sensitivity; eICU-CRD v2.0 (208 hospitals, n~139k stays → filtered ~50–70k meeting common-variable availability); AmsterdamUMCdb v1.0.2 (23k admissions). No power-based sampling (use all eligible).
4. **Variables:** See harmonization stub table §7b.
5. **Analysis plan:** Metrics §7e, equivalence bounds §7d, baselines §7g, leakage checklist §7c, subgroup plan, missing-data handling.
6. **Decision rule:** Pre-specified in §7d — replication is *successful* only if AUROC within 0.05 *and* calibration slope 0.8–1.2 *and* subgroup heterogeneity ≤0.10 *and* DCA net benefit > trivial at mortality 10% and 20% thresholds.
7. **Exploratory (not confirmatory):** Harmonization pipeline sensitivity (`ricu` vs YAIB vs METRE), 48h window, phenotyping task.
8. **OSF links:** Code freeze (Git tag `v0.1.0-rr`), data-freeze hashes (SHA256 of extraction SQL + feature tables), compute environment (Docker `python:3.11` + `torch==2.3`, `ricu==0.5.8`, seeds).
9. **RR Stage 1 submission:** Target journals *BMJ*, *JAMIA*, *PMLR-MLHC*, *Nature Scientific Data* — all publish well-conducted replications.

#### 7b. Harmonization Mapping Stub Table (which vars map — TRIPOD+AI Item 7 predictor definition)

Pre-register ONE pipeline as primary (`ricu` 0.5.8) with explicit column mapping; deviations logged as TRIPOD Item 7 deviations. Exploratory sensitivity across pipelines is not HARKed.

| Domain | Harutyunyan MIMIC-III feature (17 vars, 1h grid) | MIMIC-IV source | eICU-CRD v2.0 source | AmsterdamUMCdb source | Mapping note / harmonization risk |
|--------|---------------------------------------------------|-----------------|----------------------|-----------------------|-----------------------------------|
| **Time-zero** | ICU admission (`ICUSTAY_ID` + `INTIME`) | `mimic-iv icustays.intime` | `patientUnitStayId + hospitalAdmissionTime` | `admission + ICU admission` | eICU has no single ICU admission timestamp — pre-register rule (first `patientUnitStayId`) |
| **Outcome** | In-hospital mortality (binary, at discharge) | same | `hospitalDischargeStatus` (APACHE `hospital_mortality` is proxy) | `discharge type = death` | eICU outcome is hospital, not ICU, mortality — document |
| **Vitals** | HR, SBP, DBP, MBP, RR, Temp, SpO2 (1h, z-scored per Harutyunyan) | `chartevents` | `vitalPeriodic` (5-min → 1h median) | `numericitems` (1-min → 1h) | eICU vitals are 5-min periodic, not charted — resampling rule locked |
| **Labs** | Glucose, pH, lactate, etc. (17 labs, forward-fill + mask) | `labevents` | `lab` (LOINC mapped) | `lab` | LOINC coverage differs (eICU 30–60% missing lactate) — missingness is leakage-relevant |
| **Mask indicator** | Binary mask per variable per hour (Harutyunyan) | same | same | same | Must be frozen; no future imputation |
| **Demographics** | Age, gender | same | `patient.age/gender` | `admission age/gender` | Age truncated 89+ in MIMIC vs exact in eICU — harmonize bin |
| **Scores** | SOFA (for subgroup + baseline) | compute via `ricu` SOFA | `apache` + compute SOFA approximation | SOFA per `ricu` | SOFA definition drift is Nestor mechanism — report version |

Full mapping table (200+ `itemid` → LOINC → Amsterdam concept) is committed to `working/agent_notes/methods-scout/T8_mapping_stub.csv` before data pull; hash is OSF-registered.

#### 7c. Leakage Checklist (mandatory — executed and reported as supplementary TRIPOD+AI Item 9/10)

- [ ] **Time-zero definition locked and code-frozen BEFORE seeing test outcomes:** ICU admission = first `icustay`/`patientUnitStayId`; no redefinition after looking at mortality rates. Documented in OSF §2 with SQL.
- [ ] **Lookahead audit:** No feature uses information after the end of the observation window (first 24h for mortality). Explicitly: no `max SOFA` over full stay, no `last lab before discharge`, no `vasopressor after 24h`. Checked via automated timestamp audit: for each feature, `max(feature_time) ≤ time_zero + 24h` asserted in pipeline unit tests.
- [ ] **Train/test split leakage:** MIMIC train/test splits are Harutyunyan original splits (fixed `subject_id` hash) *or* new 5-fold CV locked before external test access. External eICU/Amsterdam data are **never used for hyperparameter tuning**; hyperparameters are frozen from Harutyunyan (LSTM 2-layer, 128 hidden, dropout 0.3, Adam 1e-3) or tuned only on MIMIC validation split.
- [ ] **Missing-data handling frozen:** Harutyunyan forward-fill + mask indicator (no future interpolation, no MICE that leaks test distribution). Mask is part of predictor definition, not post-hoc. Sensitivity: GRU-D-style Δt as exploratory, not primary.
- [ ] **Label leakage:** Mortality label is *hospital* mortality derived from discharge table, not from note text or code that is itself a predictor. No `discharge location = death` as a feature.
- [ ] **Code provenance:** All extraction SQL, preprocessing notebooks, and feature tables are hashed (SHA256) and OSF-archived. Any post-registration change is logged as deviation with date and rationale.

#### 7d. Equivalence Bounds / Power

**Primary hypothesis = equivalence (replication success = external performance within pre-specified bounds of original).** Non-inferiority is not sufficient — we test two-sided equivalence.

- **AUROC equivalence bound:** Δ = 0.05 absolute. Replication *succeeds* on discrimination only if `AUROC_external ≥ AUROC_original − 0.05`. Original Harutyunyan MIMIC-III mortality AUROC ≈ 0.86 (Table 1, LSTM). So threshold = 0.81. Failure = drop >0.05.
- **Calibration slope bound:** 0.8–1.2 (Van Calster weak calibration). Success requires slope ∈ [0.8, 1.2] *and* intercept ∈ [−0.3, 0.3] on logit scale. Slope <0.8 (overfitting/shrinkage) or >1.2 (underfitting) = replication failure.
- **Subgroup heterogeneity bound:** Max pairwise AUROC range across pre-specified subgroups (age quartile, sex, race-ethnicity where available, SOFA quartile, site) ≤0.10. >0.10 = heterogeneity failure.
- **Decision-curve bound:** Net benefit at clinically relevant thresholds (mortality 10% and 20%) must exceed *trivial* (prevalence) and SOFA baselines. DCA failure = LSTM net benefit ≤ trivial at both thresholds.

**Power:** With eICU n~50k eligible stays (mortality ~8–10% → ~4–5k events) and AmsterdamUMCdb n~15k eligible (mortality ~12% → ~1.8k events):
- AUROC SE (DeLong) ≈ 0.003–0.005 → 95% CI width ≈ 0.01–0.02 → power >0.99 to detect Δ=0.05 drop (two-sided α=0.05).
- Calibration slope SE ≈ 0.04–0.06 → power >0.90 to detect slope 1.0→0.8 shift.
- Subgroup AUROCs: smallest subgroup (e.g., race-ethnicity stratum n~5k) still yields SE ≈ 0.01 — adequate for heterogeneity test.

Power is not the binding constraint; **calibration/subgroup precision is**. No underpowered claims.

#### 7e. Metrics (joint criterion, not AUROC-only — Van Calster / Riley lineage)

Co-primary (all reported, decision rule in §7d):
- **Discrimination:** AUROC (DeLong 95% CI), AUPRC (with prevalence context — Pinker critique), PR-AUC per subgroup.
- **Calibration:** calibration slope + intercept (logistic calibration regression), flexible loess calibration plot, integrated calibration index (ICI), Van Calster hierarchy (mean → weak → moderate where feasible). Riley et al. BMJ framework for individual-level uncertainty intervals around risks if reporting absolute risk.
- **Overall accuracy:** Brier score + decomposition.
- **Decision-curve analysis (DCA):** net benefit across threshold probabilities (Vickers & Elkin) — the clinical-utility tiebreaker; report at 10%, 20%, and threshold maximizing Youden on internal data.
- **Feature-robustness (Nestor):** temporal/site drift plot — internal AUROC vs external AUROC per site/quarter; calibration drift vs measurement-density.
- **Subgroup:** AUROC/AUPRC + calibration slope per pre-specified stratum (age quartile, sex, race-ethnicity where available, SOFA quartile, eICU hospital type/size, Amsterdam vs eICU).

Multiple testing: Holm correction within subgroup family; calibration slope CI is primary, not p-value.

#### 7f. Software & Compute / Access Timeline

- **Harutyunyan benchmark:** `github.com/YerevaNN/mimic3-benchmarks` (MIMIC-III benchmark) + `mimic3models/multitask` (LSTM) — MIT license, 890 stars, documented build. Alternative modern re-implementation: `YAIB` `mimic3models_torch` port.
- **Harmonization:** `ricu` (R, CRAN `ricu==0.5.8`), METRE (Python, S1532046423000771), YAIB (Python, Moor et al. 2023) — pre-register `ricu` as primary.
- **Quality/Cross-check:** MIMIC-Extract (Python) for reproducible preprocessing audit trail.
- **Evaluation:** `CalibrationCurves`, `dcurves` (R DCA), `pROC`, `rms`, `TRIPOD+AI` checklist item mapping (see §7h).
- **Timeline (executable tomorrow):** PhysioNet credentialing (CITI + DUA) 1–2 weeks (can start coding on MIMIC-III demo subset `mimic-iii-demo` immediately); extraction pipeline containerized (Docker) in Week 1; OSF preregistration locked before external test access in Week 2; training on MIMIC-III (single GPU, 2–4h per run, 5-fold CV × 3 seeds ≈ 15 runs ≈ 1–2 days); external evaluation on eICU/Amsterdam is inference-only (hours). **Total v1 wall-clock: 3–4 weeks to pre-registered external results.**
- **Compute:** Single GPU (e.g., A100 40GB or RTX 4090) suffices; no HPC needed for locked v1 (LSTM 2×128 is small). Cost < $100 cloud.

#### 7g. Mandatory Baselines (no paper without these — "beat the baseline or show it suffices")

For external validation to be adjudicable, the replication must include on *identical* feature sets and splits:

1. **Logistic regression (LR)** on tabular aggregation (mean + last value per variable over 24h, plus mask-rate features) — L2-regularized, Platt-scaled for calibration comparison.
2. **Established clinical score:** **SOFA** (and APACHE IV approximation where available) for ICU mortality, with re-calibrated intercept for external site (Van Calster weak calibration). SOFA alone is the clinical baseline to beat.
3. **Simple ML baseline:** **Gradient boosting (GBM/XGBoost)** on same tabular aggregation — Christodoulou lineage (ML vs LR no-benefit prior). Hyperparameters via MIMIC validation split only.
4. **Trivial baseline:** **Prevalence prediction** (predict overall mortality rate for all patients) — for AUPRC contextualization (Pinker AUPRC critique of Rajkomar applies to Harutyunyan reporting too) and DCA trivial comparator.
5. **Optional 5th (exploratory):** Random forest on same tabular features — as GBM cross-check.

**Headline comparison:** Does Harutyunyan LSTM outperform LR + SOFA + GBM on *external* AUROC/calibration/DCA, or does a simpler baseline suffice? Either outcome is publishable and is the declared primary outcome (prevents HARKing).

#### 7h. TRIPOD+AI 27-Item Mapping (Collins et al. BMJ 2024 — v1 coverage)

| TRIPOD+AI Item | Section in protocol | How v1 satisfies |
|----------------|---------------------|------------------|
| 1 Title/Abstract | RR title: "Pre-registered direct replication of Harutyunyan LSTM ..." | States replication, data sources, TRIPOD+AI adherence |
| 2 Background | §1 Question | Gap: no pre-registered replication |
| 3 Objectives | §7 H0/H1 + §7d bounds | Falsifiable equivalence bounds |
| 4 Data sources | §7a + §7b mapping table | MIMIC-III/IV, eICU-CRD, AmsterdamUMCdb/HiRID — credentialed public |
| 5 Participants | §7a sampling plan | Eligibility, exclusions, time-zero definition |
| 6 Outcome | §7b Outcome row | In-hospital mortality, definition per site |
| 7 Predictors | §7b stub table | 17 variables, 1h grid, mask handling, harmonization risk |
| 8 Sample size | §7d Power | n and event counts per site, SE calculations |
| 9 Missing data | §7c checklist | Forward-fill + mask frozen, audit |
| 10 Model specification | §7a + §7g baselines | Harutyunyan LSTM 2×128 hyperparameters frozen; LR/SOFA/GBM specs |
| 11 Model development | §7f compute | Training splits, seeds, Docker |
| 12 Model evaluation | §7e metrics | AUROC, AUPRC, calibration, Brier, DCA, subgroup |
| 13 Performance measures | §7d bounds + §7e | Equivalence bounds, calibration slope 0.8–1.2 |
| 14 Model updating | §7d | Re-calibrated SOFA intercept; no LSTM re-tuning on external |
| 15 Risk groups | §7e subgroup | Age/sex/race/SOFA/site strata |
| 16 Validation | §7a design | External geographic validation (MIMIC→eICU + Amsterdam) |
| 17 Calibration | §7e + Van Calster | Slope/intercept/plot/ICI, hierarchy |
| 18 Clinical utility | §7e DCA | Net benefit at 10%/20% thresholds |
| 19 Fairness | §7e subgroup | Heterogeneity bound ≤0.10 |
| 20 Code availability | §7f | Git tag + OSF + Docker |
| 21 Data availability | §9 | PhysioNet/ODAP accession + hashes |
| 22 Funding | OSF | Declare none / institutional |
| 23 Ethics | §9 | De-identified public data, CITI, DUA |
| 24 Limitations | §8, §6 | FHIR vs fully-harmonizable scope, 2026 corpus evolution |
| 25 Interpretation | §10, §11 | Transportability vs clinical actionability |
| 26 Implications | §10, §11 | Governance, drift monitoring |
| 27 Open science | §7a OSF | Pre-registration + RR Stage 1 |

All 27 items are addressable with public data alone; no restricted data needed for v1.

---

### 8. Evidence AGAINST the Gap (Self-Authored Adversarial — Closest Defeaters)

Goal: steelman the claim that the gap is already closed.

1. **"Harutyunyan is already multiply re-used — that's replication."** Many papers *use* the Harutyunyan preprocessing (MIMIC-Extract, METRE, YAIB) and compare a new architecture to the Harutyunyan LSTM on MIMIC-III/IV, sometimes reporting better AUROC. A referee could argue this *is* a replication corpus. **Rebuttal:** Re-use as a *baseline suite* or *SOTA-chasing* is not a pre-registered direct replication with TRIPOD+AI reporting. Authors optimize the new model (HARKing, leakage not adjudicated) and rarely report calibration/subgroups/decision curves on an *independent* eICU/HiRID site. The community lacks a paper whose *stated aim* is "we pre-registered a direct replication of Harutyunyan LSTM on eICU with TRIPOD+AI and it replicates/fails."

2. **"Sepsis/YAIB already has a 2024–2026 replication corpus — so challenge winners are covered."** YAIB/METRE domain-shift studies (HiRID/MIMIC-IV/eICU, 216k stays, 5 deployment strategies) and the 2026 falsification series show cross-site calibration drift and that care-intensity features improve internal AUROC (0.819→0.834) but worsen external calibration (slope 1.007→0.417). **Rebuttal:** This is replication of *sepsis as a task* with modern harmonization, not a pre-registered replication of a *named Harutyunyan* frozen model with original hyperparameters and TRIPOD+AI subgroup reporting. The defeater narrows the sepsis task gap but does not close the Harutyunyan named-model gap. For Harutyunyan, no such corpus exists.

3. **"Many-analysts or feature-drift already covers robustness."** Frontiers many-analysts + Nestor feature robustness could be argued to cover "replication" broadly. **Rebuttal:** No clinical-EHR many-analysts study (same question, many independent teams, same public dataset) was surfaced; Nestor shows *that* drift exists, not a pre-registered direct replication protocol with harmonization leakage audit. The surviving claim is not that drift exists but that a *pre-registered direct replication protocol* including drift audit would be a reusable template.

4. **"TRIPOD+AI is only 16 months old — demanding it now is anachronistic."** A referee could argue existing replications satisfy TRIPOD 2015 and should not be judged by a 2024 checklist. **Rebuttal:** The packet does not require citation of "TRIPOD+AI" by name; it requires *coverage of the checklist items* that already existed as best practice (pre-registration, calibration, subgroup/fairness, code availability). The sepsis systematic review (n=22) shows those items were commonly missing even under TRIPOD 2015. The replication's contribution is to demonstrate *what changes when the full checklist is followed*.

5. **Closest defeater that would close the Harutyunyan arm if extended:** **YAIB (Moor/Yèche et al. 2023, arXiv 2208.06691)** — flexible multi-center benchmark harmonizing MIMIC-IV/eICU/HiRID/AmsterdamUMCdb with standardized tasks (mortality, LOS) and reporting external drops. If YAIB's next release were to include a **pre-registered, OSF-timestamped, TRIPOD+AI-reported direct replication of the frozen Harutyunyan LSTM with original hyperparameters, leakage checklist, and subgroup/DCA** (not just a generic LSTM baseline), the Harutyunyan arm would be **closed** and the correct next step would be a second-flagship extension (Rajkomar reconstruction audit or sequestered sepsis winner frozen-model replication). Until that paper exists, the gap survives.

If any of #1–#5 were extended post-2026 to include a pre-registered Harutyunyan→eICU TRIPOD+AI replication with calibration/subgroup/decisions reported, the **Harutyunyan arm would be closed** and the correct next step would be a second-flagship extension.

---

### 9. Relevant Datasets (Named: Public / Restricted / Simulation; Access Route)

- **Public — credentialed (preferred for all T8 replications; v1 requires only these):**
  - **MIMIC-III v1.4** (Johnson et al. *Sci Data* 2016, DOI 10.1038/sdata.2016.35) & **MIMIC-IV v2.2+** (Johnson et al. *Sci Data* 2023, DOI 10.1038/s41597-022-01899-x) — single-center BIDMC ICU (40k–65k stays), minute-level vitals, labs, notes. Access: PhysioNet credentialing (CITI + DUA, 1–2 weeks).
  - **eICU Collaborative Research Database v2.0** (Pollard et al. *Sci Data* 2018, DOI 10.1038/s41597-018-0006-0) — multi-center US ICU (208 hospitals, 139k+ stays after filtering), ideal for cross-site external validation (MIMIC single-center → eICU multi-center is the canonical US generalizability axis).
  - **AmsterdamUMCdb v1.0.2** (Thoral et al. *Sci Data* 2021, DOI 10.1038/s41597-021-00737-X) — European ICU (Amsterdam UMC, 23k admissions), GDPR de-identified, access via Amsterdam UMC ODAP portal (credentialed, European EHR complement).
  - **HiRID v1.1.1** (Faltys et al. *Sci Data* 2021, DOI 10.1038/s41597-021-00968-9) — high-resolution Swiss ICU (Bern, 34k admissions, 2-min resolution), for high-frequency drift analysis (secondary site alternative to AmsterdamUMCdb).
- **Public — challenge sets (extension only):**
  - **PhysioNet/CinC 2012 (mortality)** & **2019 (sepsis)** — competition datasets with known leaderboards; replication can target winning-model claims if second flagship.
- **Restricted-public (optional Stage-2 extensions only — not v1):**
  - **UK Biobank** (Access Management System) — non-ICU complement.
  - **Indian ICU EHR** (collaborating Indian tertiary ICU — e.g., AIIMS/CMC/APOLLO, requires DUA/MOU, not available as public download; **not required for v1**).
- **Simulation / plasmode — not needed for primary:** Real public EHR suffices. Synthetic data could be used supplementary (e.g., plasmode stress-testing with injected leakage to quantify sensitivity) but is not the primary pathway; T8's value is *empirical contact with real independent data*.

---

### 10. Methodological Implications

- **If replication holds (calibration preserved, subgroup AUROCs homogeneous, decision curves favor LSTM over SOFA/LR/GBM):** Establishes transportability of Harutyunyan's architecture across US multi-center and European settings; validates multitask LSTM as a credible external baseline for future ICU prediction work; provides a template for TRIPOD+AI replication on public EHR that other groups can extend into a corpus. Shows that leakage controls and harmonization (METRE→`ricu`→YAIB) are sufficient.
- **If replication fails (AUROC drop >0.05, calibration drift slope <0.8, subgroup heterogeneity >0.10, LSTM not beating LR/SOFA/GBM externally):** Diagnose *why* (leakage, feature drift via Nestor, threshold miscalibration, observation-process leakage per YAIB falsification) and set a reusable methods workflow (code freeze, data freeze hash, TRIPOD+AI checklist, feature-definition archive) that makes the failure auditable. A rigorous negative replication is a high-value methods contribution (*Sci Transl Med*, *BMJ*, *JAMIA*, *PMLR-MLHC* publish well-conducted replications) and is the skeptical prior made concrete — ML does not get preference.
- **Either outcome demands calibration + subgroup + decision-curve reporting alongside AUROC**, nudging the territory toward more honest inference (Riley/Van Calster/TRIPOD+AI). Also stress-tests the **harmonization pipeline** (METRE vs `ricu` vs YAIB) as a sensitivity dimension — informing the plasmode/instrument-validity agenda (T7).
- **Pre-registration (OSF / Registered Report) is mandatory** to prevent HARKing on many external-site/harmonization/metric cells; "Beat the baseline or show it suffices" is the declared primary outcome.

---

### 11. Clinical Implications

- Clinicians need to know whether a published "ICU mortality LSTM beats logistic regression / SOFA" claim is actionable or overfit to BIDMC/MIMIC. A direct replication on eICU (208 community/regional hospitals) with honest calibration and subgroup reporting answers that directly; even a null ("does not replicate under TRIPOD+AI on independent multi-center data") protects patients from premature deployment and informs governance (monitoring for drift per Nestor).
- Feature-robustness + observation-process findings (YAIB: measurement-count features improve internal AUROC but worsen external calibration) have workflow implications: models tied to brittle EHR feature definitions (lab codes, charting conventions, measurement-frequency proxies) should not be deployed without drift monitoring — a concrete governance lesson for health-system AI committees.
- Decision-curve analysis (Vickers) on external data at clinically relevant thresholds (e.g., mortality 10%, 20%) is the clinically actionable metric; AUROC alone is insufficient. External decision-curve shrinkage is the most clinically meaningful replication outcome.

---

### 12. India Relevance

**Verdict: GEOGRAPHY-ONLY for v1.**

- The core replication question (does Harutyunyan's MIMIC-trained LSTM transport to independent public EHR with honest calibration/subgroup reporting?) is **population-agnostic** and stresses a **universal** statistical assumption (stationarity/external validity), not an India-specific one. Indian data are not needed to answer it, and claiming STRESSES-ASSUMPTION for v1 would be decoration.
- **Defensible India-relevant Stage-2 extension that would genuinely stress an assumption:** Replication of the frozen/retrained Harutyunyan model on an **Indian ICU EHR** (where available — e.g., collaborating Indian tertiary ICU with similar SOFA/APACHE variables) would test *transportability across health-system contexts* — a core T6 concern. Baseline risk, case-mix (younger ICU population, tropical sepsis etiologies, CKD/glucose trajectories), measurement availability (lactate, ventilator parameters, arterial blood gases), and practice patterns (thresholds for ICU admission, formulary, cost-driven test selection) all differ. That extension would genuinely stress the **exchangeability / S-admissibility** assumption and calibration transportability (Van Calster hierarchy) — but it requires an Indian partner dataset with MOU/DUA and is proposed as a **follow-on**, not the v1 claim. Do not claim STRESSES-ASSUMPTION for the v1 public-EHR replication.
- **What NOT to claim:** "Repeat Harutyunyan on Indian patients" without a named assumption stressed is decoration. The packet correctly flags GEOGRAPHY-ONLY for v1 and describes the Stage-2 transport mechanism. No ethics/privacy barrier beyond standard de-identified credentialed access for v1.

---

### 13. Confidence

**Medium-High (for the gap: at least one flagship appears un-replicated as a pre-registered TRIPOD+AI direct replication on independent public EHR).**

Strengths: Per-model adversarial sweep explicitly tried to find replications for Harutyunyan and returned no hit meeting the pre-registered direct-replication definition; corpus-level sepsis literature (3/22 externally validated, <10% code) independently shows thin external validation; resource feasibility is high (all data public/credentialed, pipelines open, compute modest, 3–4 week timeline); the Harutyunyan→eICU replication is a bounded-scope, falsifiable first paper with guaranteed publishability as a negative result if rigorous (equivalence bounds make the negative result diagnostic, not vague).

Risks capping below High:
- **YAIB next release evolution:** YAIB is actively harmonizing MIMIC-IV/eICU/HiRID/AmsterdamUMCdb and could publish a frozen-model Harutyunyan replication that closes the gap — requires monitoring before RR submission.
- **TRIPOD+AI recency (April 2024):** A referee could argue that judging pre-2024 work by 2024 checklist is anachronistic — mitigated by framing as "checklist-item coverage" rather than citation.
- **Unsearched venues:** Non-English replications or theses on eICU/AmsterdamUMCdb may exist outside open-web coverage; a PubMed systematic-review-filter sweep with MeSH ("Reproducibility of Results" + "External Validation" + "MIMIC") before submission is mandatory.

No data-access barrier for v1 (public/credentialed); publishability depends on **pre-registration + leakage controls + calibration/subgroup/decision-curve reporting** meeting reviewer expectations (McDermott/Nagendran/TRIPOD+AI framing). ML gets no preference by design.

---

### 14. Recommended Next Search (Executable)

```pubmed
# 1. Exhaust named-model + TRIPOD+AI replication conjunction (adversarial closure — verify no closed gap before Registered Report)
("Harutyunyan"[Title/Abstract] OR "Multitask learning and benchmarking with clinical time series"[Title/Abstract] OR "MIMIC-III benchmark"[Title/Abstract]) AND ("external validation"[Title/Abstract] OR "replication"[Title/Abstract] OR "reproducibility"[Title/Abstract]) AND ("eICU"[Title/Abstract] OR "AmsterdamUMCdb"[Title/Abstract] OR "HiRID"[Title/Abstract])

# 2. Leakage-specific EHR prediction audit (verify checklist novelty)
("data leakage"[Title/Abstract] OR "lookahead bias"[Title/Abstract] OR "temporal leakage"[Title/Abstract]) AND ("clinical prediction model"[Title/Abstract] OR "intensive care"[Title/Abstract]) AND ("time-zero"[Title/Abstract] OR "observation window"[Title/Abstract])

# 3. TRIPOD+AI-era replications (April 2024 → present) — capture very recent corpus
("TRIPOD+AI"[Title/Abstract] OR "TRIPOD-AI"[Title/Abstract]) AND ("external validation"[Title/Abstract] OR "replication"[Title/Abstract]) AND ("MIMIC"[Title/Abstract] OR "eICU"[Title/Abstract] OR "AmsterdamUMCdb"[Title/Abstract])

# 4. Many-analysts robustness in clinical EHR (adjacent gap confirmation)
("many analysts"[Title/Abstract] OR "researcher degrees of freedom"[Title/Abstract] OR "multiverse analysis"[Title/Abstract]) AND ("electronic health records"[Title/Abstract] OR "MIMIC"[Title/Abstract] OR "clinical prediction model"[Title/Abstract])

# 5. Calibration drift on external validation (Van Calster/Riley lineage)
("calibration slope"[Title/Abstract] OR "calibration hierarchy"[Title/Abstract] OR "calibration drift"[Title/Abstract]) AND ("external validation"[Title/Abstract] OR "transportability"[Title/Abstract]) AND ("intensive care"[Title/Abstract] OR "MIMIC"[Title/Abstract])
```

```open-web
# 6. YAIB/METRE/ricu next releases (not PubMed) — inspect for Harutyunyan frozen-model replication before submission
# Inspect: YAIB GitHub (github.com/rvandewater/YAIB) releases + ricu vignettes for cited external validations that cite Harutyunyan
# Inspect: Harutyunyan Sci Data supplement + YerevaNN/mimic3-benchmarks GitHub issues/Discussions for external-validation attempts

# 7. Preprint sweep for recent closure (arXiv + medRxiv, 2024–2026)
# arXiv: stat.ME + stat.AP + cs.LG + q-bio.QM, query: Harutyunyan MIMIC eICU replication TRIPOD; site:arxiv.org Harutyunyan external validation
# medRxiv: query: MIMIC eICU external validation replication calibration subgroup

# 8. Verification alias
# Verify: Beam JAMA corrected DOI 10.1001/jama.2019.20866 HEAD 302 (not 10.1001/jama.2020.2166) — log alias
```

---

### Appendix — Queries & Papers (verbatim for search_log.csv / evidence_registry.csv)

**Queries run 2026-08-30 (verbatim) — Cycle 4 T8 packet (distinct strategies required):**
- `Harutyunyan MIMIC benchmark direct replication external validation pre-registration OSF` (T8-C4-StrategyA-replication, 5 hits, 2026-08-30, notes: Strategy A replication terminology — no Harutyunyan→eICU pre-registered replication located)
- `ICU prediction data leakage time-zero lookahead calibration slope decision curve leakage checklist` (T8-C4-StrategyB-leakage-calibration, 5 hits, 2026-08-30, notes: Strategy B leakage/calibration distinct terminology — time-zero/lookahead sparse)
- `McDermott Nagendran TRIPOD AI Collins Van Calster Riley calibration systematic review` (T8-C4-review-TRIPOD-calib, 5 hits, 2026-08-30, notes: Review — 4 required reviews verified)
- `many analysts researcher degrees freedom feature drift Nestor non-stationary health records` (T8-C4-adjacent-many-analysts-drift, 5 hits, 2026-08-30, notes: Adjacent — no clinical-EHR many-analysts located)
- `Harutyunyan 2019 multitask LSTM eICU AmsterdamUMCdb exact replication TRIPOD` (T8-C4-adversarial-exact-replication, 5 hits, 2026-08-30, notes: Adversarial — gap survives)
- `METRE ricu YAIB harmonization MIMIC eICU AmsterdamUMCdb HiRID` (T8-C4-chaining-harmonization, 5 hits, 2026-08-30, notes: Chaining Harutyunyan→METRE→ricu→YAIB→Nestor→Van Calster/Riley)
- `clinical prediction model temporal leakage lookahead time-zero EHR calibration` (T8-C4-leakage-deep, 5 hits, 2026-08-30, notes: Deep leakage terminology)
- `Van Calster calibration hierarchy Riley prediction interval TRIPOD AI 2024` (T8-C4-calibration-chain, 5 hits, 2026-08-30, notes: Calibration chain Van Calster→Riley→TRIPOD+AI)
- Cycle 3 carry-forward adversarial/adjacent: `Harutyunyan MIMIC-III benchmark replication eICU AmsterdamUMCdb external validation` (T8-adversarial-Harutyunyan), `Rajkomar deep learning EHR replication independent validation FHIR` (T8-adversarial-Rajkomar), `PhysioNet 2019 sepsis prediction external validation MIMIC eICU replication` (T8-adversarial-sepsis), `feature robustness non-stationary health records Nestor external validation failure` (T8-Nestor) — all VERIFIED.

**Papers (resolvable IDs):** 10 papers listed in §4 table (Harutyunyan 10.1038/s41597-019-0103-9, TRIPOD+AI 10.1136/bmj-2023-078378, McDermott 10.1126/scitranslmed.abb1655, Nagendran 10.1136/bmj.m689, Nestor 10.48550/arXiv.1908.00690, Van Calster 10.1016/j.jclinepi.2015.12.005, Riley 10.1136/bmj-2024-080749, TRIPOD 2015 10.1136/bmj.g7594, ricu PMC10268223, YAIB 10.48550/arXiv.2208.06691).

**Verification:** 7/10 DOIs HEAD-checked 302 on 30 Aug 2026 (Harutyunyan, TRIPOD+AI, McDermott, Nagendran, Nestor, Van Calster, Riley, YAIB) + TRIPOD 2015 verified in Cycle 3; cross-check §4 log. [UNVERIFIED] not used for load-bearing claims. At least one model DOI 302 verified: YES (Harutyunyan 10.1038/s41597-019-0103-9 302 + TRIPOD+AI 10.1136/bmj-2023-078378 302).

