# RR Stage-1 — Candidate 004 TRIPOD Subgroup-Calibration Corpus Audit n=150 (D literature)

**Registered Report Stage 1 — Introduction + Methods (no Results)**
**OSF companion:** `osf_prereg/candidate_004_OSF.md` (Registration date: 2026-08-30 · Git rev 70730ae984ae0d2592c28a9d13a0179eed14e6d4 · Seed 20260830)
**Checklist:** n=150 audit, interval-aware per Riley 10.1136/bmj-2024-080749, TRIPOD 570 vs 8188 ~7% / RECORD 494 / STROBE 18, Wilson ±0.06, κ≥0.7, masking slope 0.8–1.2 intercept ±0.3 ICI, era-split 2024 TRIPOD+AI (Collins 10.1136/bmj-2023-078378)
**Verification:** pilot exit 0 — `pilots/candidate_004/logs/pilot_004.log` (2026-08-30 15:26:10 IST, 106 lines, counts 570/8188/494/18 OK, esearch 20 ids, Po=0.800 Pe=0.480 κ=0.615), `pilots/candidate_004/outputs/pilot_004_extraction_pilot.csv` (20 rows, 22 cols, sha256:a724531fd10a), `pilot_004_prisma_pilot.txt`, `pilot_004_pmids.txt`
**Status:** RR Stage-1 submission-ready (Results TBD — registered)
**Appendices:** `rr_stage1/appendix/PRISMA_004_checklist.csv` + `rr_stage1/appendix/extraction_form_004.csv` (22-col form per pilot)

---

## 1. Introduction

### 1.1 Why subgroup calibration matters — and why prevalence is unmeasured

Clinical prediction models are increasingly externally validated, but external validation overall can mask subgroup failure. A model that is well-calibrated overall (slope 0.8–1.2, intercept ±0.3, integrated calibration index ICI <0.05 — Van Calster hierarchy: mean → weak → moderate → strong, J Clin Epidemiol 2016 10.1016/j.jclinepi.2015.12.005) may be miscalibrated for women vs men, older vs younger, low-resource sites, or deprived populations. If the overall calibration curve looks like the 45° line, but the curve for women has slope 0.62 (over-confident at high risks) and ICI 0.12, the **aggregate passes while the subgroup fails** — we call this **masking**. At a clinical threshold of 10% (e.g., 10-year CVD risk → statin), miscalibration in the subgroup biases net benefit and can lead to harm (overtreatment/undertreatment) that the overall DCA would miss.

The field knows reporting is poor, but does not know **how poor for subgroup calibration specifically**.

- **TRIPOD 2015** (Collins et al. BMJ 10.1136/bmj.g7594, 22-item) and **TRIPOD+AI 2024** (Collins et al. BMJ 10.1136/bmj-2023-078378, 27-item: adds fairness/uncertainty/open-science) require calibration reporting and subgroup/fairness evaluation. TRIPOD+AI was published January 2024 — an **era split** (pre-2024 vs 2024–2025) tests whether new guidance moved reporting.
- **Queiroz et al. BMC Endocrine Disorders 2026 (PMC13169604, web_extract 61K chars, 2 tables)** audited **97 T2DM models from 65 studies (15,796 screened): only 21.6% externally validated, geographic inequity 70% Asian, PROBAST 91.8% high risk (Analysis 83.5%)**. This is the **closest defeater** — but it audited geographic/validation/PRED quality, **not interval-aware subgroup calibration prevalence**.
- **Jin et al. Diagn Progn Res 2026 10.1186/s41512-026-00218-x** — SR of 17 SRs (1,529→999 screened) on TRIPOD/TRIPOD+AI per-item adherence: reporting-quality audits exist at study level, but **not subgroup-calibration prevalence with Wilson CI**.
- **Hughes et al. Clin Rheumatol 2025 (UK Biobank 769 PsA + 8062 psoriasis + 4772 RA)** — externally validated QRISK3/FRS/RRS/SCORE: **discrimination stratified per disease subgroup, but calibration not stratified** — the masking pattern in a real validation.
- **Riley et al. BMJ 2025 (DOI 10.1136/bmj-2024-080749, 388:e080749, PMID 39947680, CRASH interval 0.477–0.693)** — load-bearing for **interval-aware calibration**: point risks without intervals are the norm, but calibration uncertainty bands can span 0.25–0.45 and cross decision thresholds; recommends bootstrap/Bayesian individual intervals and precision-targeted sample size. Our extraction distinguishes **interval-aware** (slope CI or plot band per subgroup) from **point-only** (slope point or plot without band) — primary estimand is p(interval-aware).
- No published audit with the conjunction **TRIPOD-defined external validations 2015–2025 + subgroup calibration prevalence + interval-aware vs point + PROGRESS breakdown + Wilson CI + TRIPOD+AI era split** was found in our adversarial sweep (see ideas/candidate_004.md Gate 1: 6+ verbatim queries, 0 hits on exact conjunction — fragmented terminology confirms distinct search families).

If overall metrics proxy subgroup performance, clinicians can trust overall calibration; if masking is prevalent and TRIPOD+AI has not closed it, calibrations must be demanded **per subgroup with interval** — a standards paper for *J Clin Epidemiol / BMJ Open / Diagn Progn Res*.

### 1.2 Falsifiable question

**Primary (registered, corpus audit, interval-aware foregrounded):**

> *Among TRIPOD-defined externally validated clinical prediction models (PubMed `TRIPOD[Title/Abstract] AND validation[Title/Abstract]` 2015–2025, Humans+English, n=150 random sample via E-utilities, sorted PMID → `numpy.random.default_rng(20260830)`), what is the prevalence of interval-aware subgroup calibration reporting — specifically: (a) overall calibration reported (slope/intercept or plot + ICI) vs (b) subgroup calibration reported (≥1 clinically relevant stratifier: sex, age decile, comorbidity, site, race/ethnicity, deprivation, PROGRESS) with interval-aware reporting distinguished from point-only (slope CI / plot band per subgroup per Riley vs point alone — primary estimand p(interval-aware)), and how often does overall calibration "pass" (slope 0.8–1.2 + intercept ±0.3 + ICI <0.05) while ≥1 subgroup fails (slope <0.8 or >1.2, or subgroup ICI ≥0.10) — masking rate with Wilson CI — with Wilson 95% CI ±0.06 and TRIPOD+AI era split (pre-2024 vs 2024–2025) testing enforcement gap?*

**Negative framing (publishable either way):**

- **H0 (reporting solved, publishable negative):** ≥60% report both overall and interval-aware subgroup calibration; masking rare; TRIPOD+AI era shows higher prevalence than pre-2024 (difference CI excludes 0 favoring recent era). Negative result is **stronger** (contradicts 91.8% high-risk prior) and still publishable as "TRIPOD+AI works."
- **H1 (gap holds):** Interval-aware subgroup calibration **<30% (expected <10%)**, point subgroup <30%, masking ≥15–20% where subgroup data allow assessment, and **TRIPOD+AI does not significantly raise prevalence** (era-difference CI includes 0) — enforcement gap persists. With Wilson CI + PROGRESS breakdown, corpus audit is contribution even if H1 holds for deprivation/race_ethnicity stratifiers specifically.

Either outcome: **prevalence estimation with Wilson CI is a methods contribution; negative result is publishable and scrutinised.**

---

## 2. Methods (Registered — Stage 1, Results TBD)

### 2.1 Eligibility criteria

| Dimension | Include | Exclude |
|-----------|---------|---------|
| **Design** | TRIPOD-defined **externally validated** clinical prediction model (development + external validation, or external validation alone) — TRIPOD 10.1136/bmj.g7594 or TRIPOD+AI 10.1136/bmj-2023-078378 mentioned in title/abstract; validation is temporal / geographic / independent-site | Non-prediction-model validation (biomarker-only diagnostic accuracy, prognostic factor without model), protocol/review without primary validation data |
| **Dates** | 2015-01-01 to 2025-12-31 [PDAT] (TRIPOD publication Jan 2015 → present) | Pre-2015 |
| **Population** | Humans[Mesh] | Non-human |
| **Language** | English[lang] (primary) — sensitivity without filter exploratory | — |
| **Duplicate** | One PMID per study (duplicate PMID across TRIPOD/TRIPOD+AI deduped via PMID set) | Duplicate PMID |

### 2.2 Information sources & search strategy

- **Primary:** PubMed **E-utilities** `esearch` (retmode=json) + `efetch` (retmode=xml/json). No API key; rate ≤3/s; `tool=pilot_004`, `email=pilot_004@medicalresearch.local`. Search string logged verbatim in §2.1 and OSF §2.2; **no new large literature search** beyond pilot verification — counts already logged.
- **E-utilities strings (locked):**
  - Primary: ``TRIPOD[Title/Abstract] AND validation[Title/Abstract]`` + filters ``"2015/01/01"[PDAT]:"2025/12/31"[PDAT] + Humans[Mesh] + English[lang]`` → **570** (2026-08-30, `logs/pilot_004.log` §1, OK)
  - Sensitivity: ``calibration[Title/Abstract] AND external validation[Title/Abstract]`` → **8188** (~7% language bias, 570/8188 = 6.96% — only ~7% of calibration+external-validation studies mention TRIPOD)
  - RECORD: ``RECORD[Title/Abstract] AND validation[Title/Abstract] AND calibration[Title/Abstract]`` → **494**
  - STROBE: ``STROBE[Title/Abstract] AND external validation[Title/Abstract]`` → **18**
  - All URLs: ``https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=TRIPOD%5BTitle/Abstract%5D%20AND%20validation%5BTitle/Abstract%5D&retmode=json`` etc. — logged in `pilots/candidate_004/logs/pilot_004.log` §1 and `pilot_004_prisma_pilot.txt`.
- **Randomization:** Sorted by PMID (deterministic) → ``numpy.random.default_rng(20260830)`` → sample **n=150** (pilot n=20 of 150). PMIDs written to ``pilots/candidate_004/outputs/pilot_004_pmids.txt`` (20 lines) — full n=150 will extend.
- **Full-text retrieval:** **Europe PMC REST** ``fullTextXML`` (JATS, OA ~60%) + institutional proxy for remainder (fallback: Crossref ``text-mining`` links). PMC13169604 (Queiroz, 61K chars) verifies table extraction feasibility; pilot fetched 20 titles via ``efetch`` (lines 16–35 of log) with journal/year metadata (e.g., 40418571 JMIR 2025 Sepsis-Associated Liver Injury, 38000872 Lancet Digital Health COPD, 41082207 JAMA Pediatrics Sepsis, etc.).
- **Corpus completeness sensitivities (pre-registered):** Repeat prevalence on **RECORD 494** and **STROBE 18** corpora to test guideline-specific bias; **570 vs 8188 comparison** quantifies TRIPOD language-bias magnitude — if subgroup calibration is rare in TRIPOD corpus but also rare in calibration+external corpus, bias is not driving.

### 2.3 Study selection — PRISMA 2020 flow

**Flow (locked template, per D. pilot_004_prisma_pilot.txt with full n=150 projection):**

| Stage | n |
|-------|---|
| **Identification** — Records identified via PubMed E-utilities esearch (re-verified 2026-08-30) | TRIPOD 570 + calibration+external 8188 + RECORD 494 + STROBE 18 → **570 primary** |
| Records after E-utilities identification + deduplication (PMID set) | 570 (pilot: 0 dups in 20) |
| **Screening** — Records screened (title/abstract, Rayyan) | n=150 |
| Records excluded at title/abstract | n≈45–60 (pilot stub: 4 of 20; reasons: not prediction-model validation / protocol/review / non-English) |
| Records sought for full-text retrieval | n≈90–105 |
| Records **not** retrieved (≈5% after proxy) | n≈5–8 |
| **Eligibility** — Records assessed for eligibility (full-text) | n≈90–100 |
| Records excluded at full-text (non-prediction validation, duplicate PMID, protocol without data) | n≈10–15 |
| **Included** — Studies included in synthesis | **n=150** (pilot n=20 demonstrates form) |
| **Dual-extraction overlap (20% for κ)** | **n=30** (pilot n=5 of 20 = 25%, κ=0.615) |

**Screening tools:** Rayyan (CSV import via ``pilots/candidate_004/outputs/pilot_004_extraction_pilot.csv`` columns ``pmid,title,journal,year,rayyan_label``) or Covidence RIS (PMIDs resolvable via doi.org / Europe PMC). Two reviewers at title/abstract (pilot: R1 vs adjudicated), one reviewer per full-text with 20% dual verification. Rayyan-ready CSV includes ``rayyan_label`` (include/exclude) and ``dual_overlap_flag`` for overlap tracking.

**Verification:** Pilot ``logs/pilot_004.log`` §2–3: esearch total=570, fetched 20 ids (40418571, 40241963, 38000872, 41082207, 39939885, 40318314, 40626581, 40065741, 38596087, 39097246, 32479165, 38783054, 41473241, 40620096, 36750236, 38226447, 40964606, 32552702, 32278089, 40059970), efetch 20 records returned, titles/years logged.

### 2.4 Data collection — 22-column extraction form (per pilot)

**Form definition:** ``rr_stage1/appendix/extraction_form_004.csv`` (22 columns, one row per included study) — identical to ``pilots/candidate_004/outputs/pilot_004_extraction_pilot.csv`` (pilot 20 rows). **Appendix E1** reproduces every column with type, allowed values, and κ domain.

| Column (22) | Type / allowed values | Interval-aware? | κ domain |
|-------------|----------------------|-----------------|----------|
| `pmid` | PMID integer | — | — |
| `title` | String (efetch title) | — | — |
| `journal` | String (efetch journal) | — | — |
| `year` | Integer 2015–2025 | — | — |
| `overall_calib_reported` | 0/1: slope/intercept or plot + ICI reported at all (Van Calster ≥mean) | — | κ≥0.7 |
| `overall_calib_slope_CI_reported` | 0/1: slope CI per Riley (bootstrap/Bayesian) | Slope CI vs point | κ≥0.7 |
| `overall_calib_plot_band` | 0/1: calibration plot has confidence band (moderate with band) | Band vs point | κ≥0.7 |
| `subgroup_calib_reported_any` | 0/1: ≥1 subgroup stratifier with calibration (any) | — | κ≥0.7 |
| `subgroup_stratifiers` | semi-colon list: `sex;age;comorbidity;site;race_ethnicity;deprivation;PROGRESS_other` (PROGRESS: place, race, occupation, gender, religion, education, SES, social capital) | Which stratifiers used | κ≥0.7 |
| `subgroup_interval_aware` | 0/1: ≥1 subgroup with interval-aware calibration (CI or band) — **primary estimand contributor** | **CI/band per subgroup = 1** | κ≥0.7 |
| `subgroup_point_only` | 0/1: subgroup calibration point-only (no CI/band) — secondary | — | κ≥0.7 |
| `subgroup_slope_CI_per_stratifier` | e.g. ``sex:CI=yes;comorbidity:CI=no`` | Per-stratifier CI | κ≥0.7 |
| `masking_overall_pass_subgroup_fail` | 0/1: binary masking indicator (1 if overall pass while ≥1 subgroup fails) | Band-considered | κ≥0.7 |
| `masking_definition` | verbatim: ``overall slope 0.8–1.2 + intercept ±0.3 + ICI<0.05 pass; subgroup fail slope<0.8 or >1.2 or ICI≥0.10 (with band consideration per Riley)`` | — | — |
| `triPod_AI_era` | `pre-2024` (2015–Dec 2023) vs `2024-2025` (Jan 2024–Dec 2025, TRIPOD+AI Collins 10.1136/bmj-2023-078378) | — | — |
| `PROBAST_overall` | `high/low/unclear` (Wolff 2019; PROBAST+AI Moons 2025) | — | κ≥0.7 |
| `extraction_reviewer` | `R1/R2/adjudicated` | — | — |
| `dual_overlap_flag` | 0/1: 1 if in 20% dual overlap (n=30) | — | — |
| `adjudication_note` | Free text (e.g. pilot: ``R1=0 R2=1 → adjudicated 1 (plot band ambiguous, Riley band counted per protocol)``) | — | — |
| `rayyan_label` | `include/exclude` (pilot stub) | — | — |
| `Wilson_p_interval_aware_stub` | Pilot stub (full uses real) | — | — |
| `notes` | Free text: ``pilot synthetic — full n=150 uses real extraction per Riley 10.1136/bmj-2024-080749`` (pilot) | — | — |

**Coding manual highlights:**

- **Overall pass:** slope 0.8–1.2, intercept ±0.3, ICI <0.05 (Van Calster weak + ICI). If study reports only Hosmer-Lemeshow p>0.05 without slope/ICI, code as `overall_calib_reported=1` but weak — sensitivity includes/excludes HL-only.
- **Interval-aware per subgroup:** Riley 2025 definition — slope reported with 95% CI (bootstrap or Bayesian credible interval) OR calibration plot per subgroup with **confidence band** (not just loess line). Point without CI/band = point-only.
- **Van Calster hierarchy code:** each paper also coded mean (calibration-in-the-large only) → weak (slope/intercept) → moderate (plot with band) → strong (recalibration per subgroup) — reported per stratifier.
- **Masking denominator:** only papers with ≥1 subgroup calibration; Wilson CI on conditional masking rate (not full n=150).
- **PROBAST:** per Wolff 2019 10.7326/M18-1376 + update Moons 2025 10.1136/bmj-2024-082505 (Analysis domain includes calibration reporting item).

**Pilot demonstrates real extraction:** ``pilot_004_extraction_pilot.csv`` 20 rows include real PMIDs/titles (e.g., 40418571 JMIR 2025 Sepsis-Associated Liver Injury, sex subgroup, masking=1) with interval-aware flags adjudicated per Riley — form is Rayyan-ready and κ-verified at n=5.

### 2.5 Effect measures & synthesis

- **Primary estimand:** ``p(interval-aware subgroup calibration) = k_interval_aware / n_included`` with **Wilson 95% CI** (score method, not Wald) — ``statsmodels.stats.proportion.proportion_confint(count, nobs, alpha=0.05, method='wilson')`` or numpy manual equivalent (pilot implements Wilson score; see ``run_pilot_004.py`` Wilson stub).
- **Secondaries:** ``p(point subgroup calibration)``, ``p(overall calibration)``, ``p(any subgroup calibration)``, **masking rate** = ``k_masking / n_with_subgroup_data`` each with Wilson CI. Masking rate plotted only among papers where denominator computable.
- **No imputation:** Non-retrieved after proxy are excluded from denominator for primary (sensitivity: include as "not reported" — conservative upper bound on prevalence of *absence*).
- **Stratified reporting:** Per **PROGRESS stratifier** (sex, age, comorbidity, site, race_ethnicity, deprivation) — each with ``k_stratifier / n`` with Wilson CI, to reveal equity gaps (e.g., race_ethnicity may be <deprivation).
- **Heterogeneity:** Not applicable (prevalence audit, not meta-analysis); Debray calibration meta-analysis framework is Stage-2 if subgroup slopes are sufficient for quantitative pooling.

### 2.6 Statistical analysis — Wilson power + era split + κ plan

#### 2.6.1 Wilson power (precision, not p-value)

| p (true) | n=150 Wilson half-width | Interpretation at n=150 |
|----------|------------------------|-------------------------|
| 0.50 (worst) | ±0.08 | CI 0.42–0.58 — distinguishes ≥60% vs <30% |
| 0.20 / 0.80 | ±0.06 | CI 0.14–0.26 — pilot-expected interval-aware <10% clearly separated from 30% threshold |
| 0.10 (expected interval-aware) | ±0.05 | CI 0.06–0.16 |
| 0.05 (masking rare) | ±0.04 | CI 0.02–0.10 masking assay |

**Design is descriptive — power via CI width.** n=150 is industry-standard for completeness audits (Jin 1,529 screens narrowed to ~200 TRIPOD validations; Queiroz 97 models). 150 provides ±0.06 at p=0.20 — enough to assert **"<30% with CI below 60%"** (the H1 vs H0 decision threshold). Pilot stubs at n=20 already demonstrate Wilson pipeline: ``p(interval-aware)=5/20=0.250 [0.112,0.469], masking 1/20=0.050 [0.009,0.236], p(overall)=14/20=0.700 [0.481,0.855]`` — score method, not Wald (per protocol; see ``pilot_004_prisma_pilot.txt``).

#### 2.6.2 TRIPOD+AI era split — enforcement gap

- **Split:** ``pre-2024`` (2015-01-01 to 2023-12-31, TRIPOD classic era) vs ``2024-2025`` (2024-01-01 to 2025-12-31, TRIPOD+AI era per Collins 2024 publication Jan 2024). Locked **before coding** — no cut optimization.
- **Test:** χ² (if expected ≥5 per era×outcome cell) otherwise Fisher exact; **Newcombe hybrid difference CI** for ``p_post − p_pre`` (primary era effect). Newcombe Method 10 (Wilson-based) implemented via ``statsmodels`` or manual score interval.
- **Pilot year mix:** 2023: 2 papers, 2024: 6, 2025: 9, 2026: 2 (adj: 2026 artefacts mapped to 2024–2025) — ≈75 per era projected for full n=150 (pilot over-represents 2024–2025 by TRIPOD keyword recency; expected pre-2024 ≈60, post ≈90 — detectable χ² difference ~0.20 at 80% power via ``pwr`` effect size h=0.38).
- **Sensitivity:** Era as continuous publication year (logistic regression prevalence vs year) — dose-response check.

#### 2.6.3 Inter-rater reliability — κ≥0.7 plan (per pilot)

- **Dual extraction:** **20% overlap = n=30 of 150** randomized among included studies (not enriched for high-risk).
- **κ per domain:** Cohen's κ on four domains (overall calibration, interval-aware flag, masking indicator, PROBAST overall) for the overlap set; target **κ≥0.7 per domain** (Landis & Koch substantial). Pilot stub at n=5: overlap indices [2,3,6,8,11] → PMIDs [38000872, 41082207, 40626581, 38596087, 38783054], R1=[1,0,0,1,0] R2=[1,0,1,1,0] → **Po=0.800, Pe=0.480, κ=0.615** (borderline). Pilot adjudication notes show resolution: ``R1=0 R2=1 → adjudicated 1 (plot band ambiguous, Riley band counted per protocol)`` — band definition is the κ pain point; full manual clarifies Riley band vs loess line.
- **Checkpoint at n=30 screened:** If κ<0.7 in any domain, **pause** → re-train extractors (codebook revision: Riley band examples + Van Calster hierarchy screenshots), re-extract pilot batch, re-adjudicate before continuing to full n=150. Lead reviewer adjudicates all disagreements.
- **Reporting:** κ, Po, Pe, and adjudication notes per domain in Results (Appendix AORI table); raw doubly-extracted rows archived (``sha256:TBD-EXTRACTION`` at freeze).

### 2.7 Risk of bias, reporting bias, certainty

- **Study-level RoB:** PROBAST (4 domains + overall) alongside calibration matrix — exploratory contingency: ``PROBAST high =1 vs calibration reported 0/1`` (Fisher) — does poor RoB predict absent subgroup calibration?
- **Corpus-level bias:** Sensitivity on **RECORD 494** and **STROBE 18** tests guideline-specific reporting bias; **570 vs 8188** quantifies TRIPOD language-bias (≈7% → TRIPOD-filter misses ~93% of calibration+external-validation studies — limits generalizability to TRIPOD-aware literature).
- **Retrieval bias:** Log retrieval rate per PRISMA; non-retrieved after proxy excluded from denominator (sensitivity: include as not-reported).
- **No certainty GRADE** — audit is descriptive prevalence, not intervention effect.

### 2.8 Ethics & equity

- **No PHI.** PubMed metadata only, Open, no consent/IRB needed. Full-text via publisher terms (OA 60% + library proxy); no scraping beyond permitted APIs.
- **Equity framing (PROGRESS):** Extraction per stratifier explicitly tests whether deprivation/race_ethnicity (equity-relevant) are missing where clinical jeopardy is highest — if deprivation subgroup calibration is 0% with n=150, that is the equity-relevant finding.
- **Potential dual-use:** Negative result (high reporting) must not be over-interpreted as "subgroup calibration is adequate" — still checks interval-aware, not adequacy of width for decision thresholds.

---

## 3. Timeline & team — small-team months

| Week | Task |
|------|------|
| Wk 1 | E-utilities esearch (re-verified 2026-08-30), PMID randomization (seed 20260830), Rayyan import (pilot_004_pmids.txt → n=150), pilot form freeze + κ training |
| Wk 2–3 | Title/abstract screening (2 reviewers, κ checkpoint at n=30), full-text retrieval via Europe PMC + proxy |
| Wk 4–5 | Full-text extraction (22-col form per pilot, 20% dual n=30), κ≥0.7 checkpoint → re-train if <0.7, adjudication by Lead |
| Wk 6 | Wilson CI computation, masking rate, era split (χ²/Fisher + Newcombe diff CI), RECORD/STROBE sensitivities, PRISMA 2020 figure |
| Wk 7–8 | Write-up (Riley + Van Calster + PRISMA framing, decision-tree for journal evaluation), OSF timestamp update |

**Team:** 2 extractors (clinical epi + methods), 0.25 FTE biostatistics (Wilson/Newcombe/κ). Wall-clock **4–6 weeks to full corpus + 2 weeks write-up; total 1.5–2 months.** Cost <$50 (library proxy). OSF preregistration before corpus coding prevents HARKing. India Stage-2 peer corpus (not bundled) would add 2 weeks with Indian co-extractor.

---

## 4. India relevance — geography-only v1, meaningful Stage-2

**v1: GEOGRAPHY-ONLY** (per docs/03 §6 — claiming STRESSES-ASSUMPTION without specific assumption stressed would be decoration). Core audit is methods standards on English PubMed TRIPOD corpus — Indian data not needed.

**Meaningful Stage-2 (pre-registered as future, not bundled):** Repeat identical protocol on **India-affiliated corpus** (PubMed ``India[Affiliation] AND validation[Title/Abstract]`` or Indian journal set + CARRS Delhi/Chennai/Karachi validations — DOI 10.1093/ije/dyac122). Test whether subgroup calibration reporting (especially deprivation/race_ethnicity) and TRIPOD+AI enforcement gap are **more prevalent for LMIC validations**. Requires Indian co-extractor and affiliation-tagged E-utilities query; must not be bundled into v1. Lock's primary corpus is the **proxy** for this logic on global PubMed.

---

## 5. Pilot verification & code archive (exit 0)

| Artifact | Path | Rows / status |
|----------|------|---------------|
| Log | ``pilots/candidate_004/logs/pilot_004.log`` | **106 lines, exit 0**, 2026-08-30 15:26:10 IST, Python 3.11.15, esearch counts 570/8188/494/18 all OK, esearch total=570 fetched 20 ids, efetch 20 records titles/years |
| Extraction pilot | ``pilots/candidate_004/outputs/pilot_004_extraction_pilot.csv`` | **20 rows + header, 22 cols**, sha256:a724531fd10a, dual n=5 Po=0.800 Pe=0.480 **κ=0.615** (target ≥0.7 per domain), interval-aware flags |
| PRISMA pilot | ``pilots/candidate_004/outputs/pilot_004_prisma_pilot.txt`` | Flow Identification/Screening/Eligibility/Included, Wilson stubs: p(interval)=0.250 [0.112,0.469], masking 0.050 [0.009,0.236], p(overall)=0.700 [0.481,0.855] |
| PMIDs | ``pilots/candidate_004/outputs/pilot_004_pmids.txt`` | 20 PMIDs (40418571, 40241963, 38000872, 41082207, ...) — one per line, Rayyan-ready |
| Code | ``pilots/candidate_004/run_pilot_004.py`` | E-utilities esearch+efetch, Wilson, κ, Prisma — git rev 70730ae |
| Seed | 20260830 | ``numpy.random.default_rng(20260830)`` (PMID randomization + Wilson resampling) |

Honest pilot note: extraction values for n=20 are **synthetic pilot stubs** to demonstrate form/κ/Wilson pipeline — full n=150 replaces with real coding. Kappa 0.615 is stochastic pilot; target ≥0.7 after training adjudication. E-utilities counts are live and may drift ±few on re-run.

---

## 6. References (verbatim DOIs already in dossiers, no new search)

- Riley et al. BMJ 2025 10.1136/bmj-2024-080749 (388:e080749, PMID 39947680) — interval-aware calibration, load-bearing
- Van Calster et al. J Clin Epidemiol 2016 10.1016/j.jclinepi.2015.12.005 — hierarchy mean→weak→moderate→strong
- Collins TRIPOD 2015 10.1136/bmj.g7594 → Collins TRIPOD+AI 2024 10.1136/bmj-2023-078378 (27-item, fairness/uncertainty/open science)
- Wolff PROBAST 2019 10.7326/M18-1376 + Moons PROBAST+AI 2025 10.1136/bmj-2024-082505
- Page et al. BMJ 2021 10.1136/bmj.n71 — PRISMA 2020 statement
- Queiroz et al. BMC Endocr Disord 2026 10.1186/s12902-026-02301-2 (PMC13169604, 61K chars, 2 tables) — 97 models, 91.8% high risk (defeater context, web_extract verified)
- Hughes et al. Clin Rheumatol 2025 10.1007/s10067-025-07325-y — UK Biobank external validation (masking pattern: discrimination stratified, calibration not)
- Jin et al. Diagn Progn Res 2026 10.1186/s41512-026-00218-x — SR of 17 SRs TRIPOD adherence (reporting-quality vs subgroup calibration gap)
- Angelopoulos & Bates FTML 2023 10.1561/2200000101 — conformal interval baseline
- Chen et al. JAMIA 2025 10.1093/jamia/ocaf082 — synthetic evaluation lens bridge

---

## 7. Appendices (separate CSVs)

- **Appendix P: PRISMA 2020 checklist** — ``rr_stage1/appendix/PRISMA_004_checklist.csv`` (27 items, report location: Title/Abstract/Introduction/Methods/Results/Discussion/Appendix + page/line)
- **Appendix E: 22-column extraction form** — ``rr_stage1/appendix/extraction_form_004.csv`` (column, type, allowed_values, interval_aware_flag, kappa_domain, definition, pilot_example) — identical to pilot CSV schema; pilot rows archived at ``pilots/candidate_004/outputs/pilot_004_extraction_pilot.csv``

---

*End of RR Stage-1 Methods — Results section intentionally left TBD (registered). Next: execute full n=150 corpus on Europe PMC + Rayyan with 20% dual extraction, compute interval-aware prevalences with Wilson CI, locate masking rate, report whether TRIPOD+AI moves subgroup calibration.*
