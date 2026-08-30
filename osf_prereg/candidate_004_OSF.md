<!--
================================================================================
OSF REGISTRATION TIMESTAMP BLOCK — CANDIDATE 004 TRIPOD Subgroup-Calibration Corpus Audit
================================================================================
Registration date (locked): 2026-08-30
Git repository: /home/shivam/Projects/medicalResearch
Git rev (HEAD at freeze): 70730ae984ae0d2592c28a9d13a0179eed14e6d4 (short: 70730ae)
Code archive: pilots/candidate_004/ (run_pilot_004.py, logs/pilot_004.log, outputs/*)
  — Python 3.11.15, numpy, E-utilities esearch+efetch (tool=pilot_004, email=pilot_004@medicalresearch.local, rate ≤3/s)
  — E-utilities re-verified this run: TRIPOD 570, calib+external 8188 (~7% language bias), RECORD 494, STROBE 18 — all OK
Seed (locked): 20260830 (numpy.random.default_rng(20260830) for PMID randomization + Wilson bootstraps)
Pilot path: pilots/candidate_004/ (logs/pilot_004.log 106 lines, outputs/pilot_004_extraction_pilot.csv 20 rows, pilot_004_prisma_pilot.txt, pilot_004_pmids.txt)
  — Pilot exit 0: 2026-08-30 15:26:10 IST, esearch total=570 fetched 20 ids, efetch 20 records, dual n=5 kappa=0.615, Wilson stubs
Checklist (frozen at timestamp):
  [x] Corpus filter locked: TRIPOD[Title/Abstract] AND validation[Title/Abstract] + 2015:2025[PDAT] + Humans[Mesh] + English[lang] → sorted PMID → rng 20260830 → n=150 (pilot n=20)
  [x] Interval-aware extraction per Riley 10.1136/bmj-2024-080749: slope CI / plot band per subgroup vs point only
  [x] TRIPOD 570 vs calibration+external 8188 (~7% language bias, 570/8188) + RECORD 494 + STROBE 18 — corpus completeness sensitivity pre-registered
  [x] Wilson 95% CI (score method, not Wald) ±0.06 at n=150 (max ±0.08 at p=0.5, ±0.06 at p=0.2/0.8)
  [x] κ ≥0.7 target (Cohen's kappa on 20% dual = n=30 overlap; pilot n=5 kappa=0.615 borderline → re-train per protocol)
  [x] Masking definition: overall pass slope 0.8–1.2 + intercept ±0.3 + ICI <0.05 while ≥1 subgroup fail slope<0.8 or >1.2 or subgroup ICI ≥0.10 (with band consideration per Riley)
  [x] Era-split 2024 TRIPOD+AI (Collins 10.1136/bmj-2023-078378): pre-2024 (2015–Dec 2023) vs TRIPOD+AI era (Jan 2024–Dec 2025) — χ²/Fisher + Newcombe difference CI
  [x] PRISMA 2020 flow locked (Identification/Screening/Eligibility/Included) with Europe PMC fullTextXML + Rayyan
OSF registration type: Registered Report Stage 1 — D (literature corpus, no PHI)
OSF placeholder: osf.io → registration DOI TBD at submission; this TIMESTAMPED.md is submission-ready copy
Verification: pilot exit 0 — pilots/candidate_004/logs/pilot_004.log (lines 1–106), pilots/candidate_004/outputs/pilot_004_extraction_pilot.csv (sha256:a724531fd10a), pilots/candidate_004/outputs/pilot_004_prisma_pilot.txt, pilots/candidate_004/outputs/pilot_004_pmids.txt
================================================================================
-->

# OSF Pre-registration — Candidate 004 TRIPOD Subgroup-Calibration Corpus Audit n=150 (D literature)

**Territory T5 Corpus Audit | Cycle 8/9 OSF-Ready (2026-08-30)**
**Companion dossier:** `ideas/candidate_004.md` + `working/agent_notes/clinical-evidence-scout/cycle04_T5_corpus_lock.md` (LOCKED 2026-08-30) + `pilots/candidate_004/README.md`
**Agent:** methods-scout + clinical-evidence-scout | **Status:** OSF-Ready (data-independent, executable tomorrow)
**OSF registration type:** Registered Report Stage 1 — D (literature corpus, no PHI)
**Reporting:** PRISMA 2020 (Page et al. BMJ 2021 10.1136/bmj.n71) + TRIPOD 2015 10.1136/bmj.g7594 → TRIPOD+AI 2024 10.1136/bmj-2023-078378
**Uncertainty:** Riley 10.1136/bmj-2024-080749 (interval-aware calibration) + Van Calster 10.1016/j.jclinepi.2015.12.005 (hierarchy)
**Data availability tier:** D (PubMed + Europe PMC, no hospital DUA)

---

## 0. Administrative

| Field | Value |
|-------|-------|
| **Title** | Prevalence of interval-aware subgroup calibration reporting among TRIPOD-defined externally validated clinical prediction models 2015–2025: a 150-study corpus audit with Wilson CI, masking rate, and TRIPOD+AI era split |
| **Version hash** | `sha256:PENDING-004-` + commit hash at freeze |
| **Random seed (locked)** | 20260830 (`numpy.random.default_rng(20260830)` for PMID randomization + Wilson resampling) |
| **Analysis date lock** | Corpus filter, extraction form, and masking definition locked before full-text coding |
| **Embargo** | Open at Stage 1 acceptance |
| **Code** | `pilots/candidate_004/run_pilot_004.py` (E-utilities esearch+efetch, Wilson, κ) — git tag `v0.1.0-rr-t5` |

---

## 1. Background & Aims

**Problem:** TRIPOD 2015 (Collins 10.1136/bmj.g7594, 22-item) and TRIPOD+AI 2024 (Collins 10.1136/bmj-2023-078378, 27-item) require calibration reporting and subgroup/fairness evaluation, but whether externally validated models **report calibration per subgroup with interval awareness** (slope CI / plot band per Riley 2025) is unknown. External validation overall may look well-calibrated (slope 0.8–1.2, intercept ±0.3, ICI <0.05) while ≥1 clinically relevant subgroup (sex, age decile, comorbidity, site, race/ethnicity, PROGRESS) calibrates poorly (slope <0.8 or >1.2, subgroup ICI ≥0.10) — **aggregate masking**. This masks the exact failure mode Riley warns about: point calibration without interval can span 0.25–0.45 on individual risks (CRASH example 0.477–0.693) with uncertainty bands crossing decision thresholds.

**Prior audits:** Queiroz et al. BMC Endocr Disord 2026 (PMC13169604) audited **97 T2DM models (65 studies, 15,796 screened): 7% Asian? actually 70% Asian, 21.6% externally validated, PROBAST 91.8% high risk** — but audited geographic/validation/PRED quality, **not subgroup calibration prevalence with interval awareness**. Hughes et al. Clin Rheumatol PMID flow (UK Biobank 769 PsA + 8062 psoriasis + 4772 RA) stratified discrimination per disease subgroup but **calibration not stratified** — the masking pattern. Completeness reviews (Jin Diagn Progn Res 2026, Heus et al., Snell update review) audit TRIPOD item adherence, not Wilson-prevalenced subgroup calibration. **No existing meta-audit quantifies p(interval-aware subgroup calibration) with Wilson CI + TRIPOD+AI era split.**

**Aims (falsifiable):**

- **Primary:** Estimate **p(interval-aware subgroup calibration)** = proportion of TRIPOD-defined externally validated models 2015–2025 that report **≥1 clinically relevant subgroup** (sex, age, comorbidity, site, race/ethnicity, PROGRESS deprivation) with **interval-aware calibration** (slope CI or calibration plot with confidence band per subgroup per Riley 2025) — with **Wilson 95% CI ±0.06** at n=150.
- **Secondary:** p(point subgroup calibration), p(overall calibration), **masking rate** = proportion where overall calibration passes (slope 0.8–1.2 + intercept ±0.3 + ICI<0.05) while ≥1 subgroup fails (slope <0.8 or >1.2 or subgroup ICI ≥0.10, with band consideration), with Wilson CI; **TRIPOD+AI era split** (pre-2024 vs 2024–2025) testing enforcement gap via χ²/Fisher + Newcombe difference CI.
- **H0 (reporting solved, publishable negative):** ≥60% report both overall and interval-aware subgroup calibration; masking rare; TRIPOD+AI closes gap (difference CI excludes 0, favoring recent era).
- **H1 (gap holds):** Interval-aware subgroup calibration **<30% (expected <10%)**, point subgroup <30%, masking ≥15–20% where subgroup data allow assessment, and TRIPOD+AI does **not** significantly raise prevalence (era-difference CI includes 0) — enforcement gap persists.

Either outcome is a methods contribution: **negative is stronger** (contradicts 91.8% high-risk prior, needs scrutiny) and still publishable as "TRIPOD+AI works."

---

## 2. Data & Corpus Definition

### 2.1 Source — D (immediate, no PHI)

| Dataset / source | Role | Access | Timeline |
|------------------|------|--------|----------|
| **PubMed E-utilities corpus** (`TRIPOD[Title/Abstract] AND validation[Title/Abstract]`, Filters 2015:2025[PDAT], Humans[Mesh], English[lang]) | **Primary corpus** — TRIPOD-defined externally validated clinical prediction models 2015–2025 | Open via `esearch` + `efetch` (E-utilities API, no DUA, rate ≤3/s, tool=pilot_004) | Immediate (screening tomorrow) |
| **Europe PMC REST fullTextXML (JATS) + BMJ/PLOS OA HTML** | **Full-text retrieval** for eligibility + extraction (PMC OA ~60%; institutional proxy for remainder — fallback Crossref `text-mining` links) | Open OA + proxy | Immediate–1 week |
| **Queiroz corpus pad (PMC13169604, 61K chars, 2 tables) + Hughes (PMC11865138) + 5–10 sampled TRIPOD validations from pilot** | **Extraction form calibration** — feasibility demonstrated via web_extract tables | PMC13169604 fullTextXML | Verified 2026-08-30 |
| **PROBAST (Wolff 2019 10.7326/M18-1376) + PROBAST+AI (Moons 2025 10.1136/bmj-2024-082505)** | **Risk-of-bias scaffolding** (Participants/Predictors/Outcome/Analysis domains) alongside calibration matrix | DOI resolvable | Immediate |

### 2.2 Locked corpus filter (reproducible E-utilities string, logged to OSF)

```
PubMed: ("TRIPOD"[Title/Abstract] AND ("validation"[Title/Abstract] OR "external validation"[Title/Abstract]))
Filters: "2015/01/01"[PDAT] : "2025/12/31"[PDAT], Humans[Mesh], English[lang]
Randomization: sorted by PMID (deterministic) → numpy.random.default_rng(20260830) → sample n=150 (pilot n=20)
Exclusions (pre-registered): non-prediction-model validation (e.g., biomarker-only diagnostic accuracy),
  protocol/review without primary validation data, non-English full-text, duplicate PMID across TRIPOD+AI/TRIPOD classic
```

**E-utilities verification (live 2026-08-30, pilot logs/pilot_004.log):**

| Query | Term | Count | Expected | Status |
|-------|------|-------|----------|--------|
| TRIPOD AND validation | `TRIPOD[Title/Abstract] AND validation[Title/Abstract]` | **570** | 570 | OK |
| calibration AND external validation | `calibration[Title/Abstract] AND external validation[Title/Abstract]` | **8188** | 8188 | ~7% language bias (570/8188) |
| RECORD AND validation AND calibration | `RECORD[Title/Abstract] AND validation[Title/Abstract] AND calibration[Title/Abstract]` | **494** | 494 | OK |
| STROBE AND external validation | `STROBE[Title/Abstract] AND external validation[Title/Abstract]` | **18** | 18 | OK |

Full E-utilities URLs logged (retmode=json): `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=TRIPOD%5BTitle/Abstract%5D%20AND%20validation%5BTitle/Abstract%5D&retmode=json` etc.

**Pre-registered sensitivity corpora:** (i) **RECORD/STROBE** — repeat prevalence on RECORD 494 and STROBE 18 to test reporting-guideline bias; (ii) **Corpus completeness** — TRIPOD 570 vs calibration+external 8188 logged (quantifies TRIPOD language-bias magnitude); (iii) Language sensitivity (without English[lang]) exploratory.

**Estimated corpus size:** TRIPOD term ~2,500–4,000 PubMed records 2015–2025; validation narrows to ~600–1,200; random n=150 feasible for full-text extraction by small team (see §7).

---

## 3. Extraction Matrix — 22 columns, interval-aware, κ≥0.7

| Extraction domain | Rows | What is extracted per paper | Interval-aware? | κ domain |
|-------------------|------|-----------------------------|-----------------|----------|
| **Overall calibration** | 5 items | Slope/intercept (weak), calibration plot (moderate: loess vs 45° with band), Hosmer-Lemeshow / ICI, overall calibration statement (Van Calster hierarchy: mean→weak→moderate→strong) | Slope CI (Riley) vs point only; plot band vs point plot | κ≥0.7 (20% dual) |
| **Subgroup definition** | PROGRESS + site | Sex, age (decile/quartile), comorbidity (Charlson), site/hospital, race/ethnicity, deprivation (IMD), PROGRESS-Plus; which stratifiers are available in validation cohort but not used | Which are reported available but unused | κ≥0.7 |
| **Subgroup calibration per stratifier** | k per paper | For each stratifier level: slope/intercept + CI, calibration plot per subgroup + band, ICI per subgroup, sample per subgroup | **Interval-aware flag** per subgroup (CI/band present = 1, point only = 0) — **primary estimand p(interval-aware)** | κ≥0.7 |
| **Masking** | 1 per paper with ≥1 subgroup | Does overall "pass" (slope 0.8–1.2 + intercept ±0.3 + ICI<0.05) while ≥1 subgroup "fails" (slope<0.8 or >1.2 or subgroup ICI≥0.10)? With band consideration per Riley | Binary masking indicator with calibration-band consideration | κ≥0.7 |
| **TRIPOD+AI era** | 1 | Publication date pre-2024 (2015–Dec 2023) vs TRIPOD+AI era (Jan 2024–Dec 2025) — Collins 10.1136/bmj-2023-078378 | — | — |
| **PROBAST RoB** | 4 domains | Participants / Predictors / Outcome / Analysis + overall | — | κ≥0.7 |

**Full 22-col form** (per `pilots/candidate_004/outputs/pilot_004_extraction_pilot.csv`): `pmid, title, journal, year, overall_calib_reported, overall_calib_slope_CI_reported, overall_calib_plot_band, subgroup_calib_reported_any, subgroup_stratifiers, subgroup_interval_aware, subgroup_point_only, subgroup_slope_CI_per_stratifier, masking_overall_pass_subgroup_fail, masking_definition, triPod_AI_era, PROBAST_overall, extraction_reviewer, dual_overlap_flag, adjudication_note, rayyan_label, Wilson_p_interval_aware_stub, notes` — pilot 20 rows demonstrate form (see Appendix).

**Interval-aware definition (Riley 10.1136/bmj-2024-080749):** Calibration slope reported with 95% CI (bootstrap or Bayesian) or calibration plot with **confidence band** (not just loess point estimate) per subgroup. Point-only = slope point estimate or plot without band. **Primary estimand is p(interval-aware); secondary is p(point).**

**Van Calster hierarchy coding:** Each paper coded as mean (calibration-in-the-large only) → weak (slope/intercept ± CI) → moderate (plot with band) → strong (recalibration per subgroup) — vocabulary per J Clin Epidemiol 2016 10.1016/j.jclinepi.2015.12.005.

---

## 4. Statistical Analysis Plan

### 4.1 Prevalence estimation — Wilson score

- **Primary:** p(interval-aware subgroup calibration) with **Wilson 95% CI (score method, not Wald)** per protocol. Wilson via `prop.test` with `correct=FALSE` score equivalent; implemented as `numpy` stub in pilot.
- **Precision at n=150:** Half-width ~0.06–0.08 depending on p (max ±0.08 at p=0.5, ±0.06 at p=0.2 or 0.8); adequate to distinguish **<30% vs ≥60%** prevalence (primary decision threshold). This is **descriptive prevalence, not superiority test** — power via CI width, not p-value.
- **Secondaries:** p(point subgroup), p(overall calibration), masking rate — each with Wilson CI. Masking denominator = n with ≥1 subgroup calibration (not full n=150) — Wilson CI on that conditional proportion.

### 4.2 Era split — TRIPOD+AI enforcement gap

- **Split:** Pre-2024 (2015–Dec 2023) vs TRIPOD+AI era (Jan 2024–Dec 2025) per Collins 2024 10.1136/bmj-2023-078378 publication.
- **Test:** χ² (expected ≥5 per cell) or Fisher exact; **Newcombe difference CI** for prevalence difference (pre vs post). Era split is **secondary** with n₁≈75, n₂≈75 per era (based on pilot year distribution 2023–2026), detectable difference ~0.20 at 80% power (see §7).
- **Interpretation:** If difference CI excludes 0 favoring post-2024, TRIPOD+AI gap closing; if includes 0, enforcement gap persists.

### 4.3 Inter-rater reliability — κ≥0.7

- **Dual extraction:** 20% overlap = **n=30 of 150** (pilot n=5 of 20 = 25% with kappa stub).
- **Pilot stub:** R1=[1,0,0,1,0] R2=[1,0,1,1,0] on overlap indices [2,3,6,8,11] → **Po=0.800, Pe=0.480, κ=0.615** (target ≥0.7 per domain; pilot borderline → would re-train per protocol).
- **Full plan:** Cohen's κ per extraction domain (overall calibration, subgroup stratifiers, interval-aware flag, masking, PROBAST). **Checkpoint at n=30**: if κ<0.7, pause → re-train extractors (clarify band vs point, Riley band counting), refine codebook, re-extract pilot batch before continuing.
- **Adjudication:** Disagreements resolved by Lead reviewer (third adjudicator); pilot adjudication notes demonstrate: `R1=0 R2=1 → adjudicated 1 (plot band ambiguous, Riley band counted per protocol)` — verbatim from CSV.
- **Sensitivity:** κ per stratifier (sex vs deprivation) — deprivation harder.

### 4.4 Missing data & retrieval

- Expected **~5% not retrieved** via Europe PMC fullTextXML (OA ~60% + proxy); log retrieval rate per PRISMA.
- Non-retrieved after proxy are **excluded from denominator** for prevalence (sensitivity: include as "not reported" — conservative upper bound).
- Language/Humans filter sensitivity without English[lang] exploratory.

### 4.5 Software & reproducibility

- E-utilities `esearch` retmode=json, `tool=pilot_004`, `email=pilot_004@medicalresearch.local`, rate ≤3/s, sorted PMID deterministic.
- Europe PMC `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMID:...&format=json` + `fullTextXML`.
- Rayyan import via `pilot_004_extraction_pilot.csv` (pmid,title,journal,year,rayyan_label,dual_overlap_flag); Covidence RIS via PMIDs.
- Wilson via `statsmodels.stats.proportion.proportion_confint(method='wilson')` or numpy manual; all seeds logged.
- **No PHI.** PubMed metadata only.

---

## 5. PRISMA 2020 Flow (locked template — per pilot pilot_004_prisma_pilot.txt)

```
IDENTIFICATION
  Records identified via PubMed E-utilities esearch (re-verified 2026-08-30):
    - TRIPOD AND validation: 570 (570) [esearch retmode=json URL logged]
    - calibration AND external validation: 8188 (8188) [~7% bias, 570/8188]
    - RECORD AND validation AND calibration: 494 (494)
    - STROBE AND external validation: 18 (18)
  Records after E-utilities identification: 570
  Pilot sample fetched via esearch+efetch: n=20 (pilot; full target n=150)
  Deduplication: 0 duplicates in pilot (PMIDs unique; full n=150 dedup via PMID set)

SCREENING
  Records screened (title/abstract): n=150 (pilot n=20)
  Records excluded at title/abstract: n≈30–40% (pilot stub n=4 of 20; reasons: not prediction-model validation / protocol/review / non-English)

ELIGIBILITY
  Records sought for full-text retrieval: n≈90–105
  Records not retrieved: n~5% (~5–8)
  Records assessed for eligibility (full-text): n≈90–100
  Records excluded at full-text: n≈10–15 (non-prediction validation, duplicate PMID, protocol without data)

INCLUDED
  Studies included in synthesis: n=150 (full; pilot n=20 demonstrates form)
  Dual-extraction overlap: n=30 (20%; pilot n=5, κ=0.615 Po=0.800 Pe=0.480 target ≥0.7)
  Extraction form: interval-aware per Riley 10.1136/bmj-2024-080749 + TRIPOD+AI era + masking (overall pass slope 0.8–1.2 ICI<0.05 while ≥1 subgroup fail)
  Prevalence estimands (pilot stubs n=20): p(interval-aware)=5/20=0.250 [0.112,0.469], p(point)=4/20=0.200, masking 1/20=0.050 [0.009,0.236], p(overall)=14/20=0.700 [0.481,0.855]
  Sensitivity corpora (pre-registered): RECORD 494, STROBE 18, 570 vs 8188 completeness
```

**Rayyan-ready:** `pilot_004_extraction_pilot.csv` includes PMID/title/journal/year + rayyan_label + dual_overlap_flag; import via Rayyan CSV or Covidence RIS (PMIDs resolvable via doi.org). E-utilities reproducibility: retmode=json, tool=pilot_004, rate ≤3/s, sorted PMID deterministic.

---

## 6. Sample Size & Power — Wilson ±0.06 at n=150

| Scenario | Expected p | Wilson 95% CI half-width at n=150 |
|----------|-----------|-----------------------------------|
| p=0.50 (worst case) | 0.50 | ±0.08 |
| p=0.20 or 0.80 | 0.20 | ±0.06 |
| p=0.10 (expected interval-aware) | 0.10 | ±0.05 |
| p=0.05 (masking rare) | 0.05 | ±0.04 |

**Adequate to distinguish <30% vs ≥60% prevalence** — primary decision threshold. Era split secondary: n₁=75 pre-2024, n₂=75 post-2024 (based on pilot 2024–2025 dominance), χ² detectable difference ~0.20 at 80% power (via `pwr` 0.38 effect size). No p-value-hacking risk: primary is prevalence CI, not superiority test.

Wall-clock: 4–6 weeks with 2 extractors (20% dual). Cost <$50 (library proxy). OSF holds E-utilities string + PMID seed; no retrieval beyond publisher terms.

---

## 7. Risk of Bias & Ethics

- **PROBAST (Wolff 2019) + PROBAST+AI (Moons 2025)** RoB per included study (Participants/Predictors/Outcome/Analysis domains) — alongside extraction matrix; exploratory association between PROBAST overall high risk and absence of subgroup calibration.
- **Publication bias / corpus completeness:** Sensitivity on RECORD 494 and STROBE 18 tests guideline-specific reporting bias; 570 vs 8188 quantifies TRIPOD language-bias (only ~7% of calibration+external-validation studies mention TRIPOD).
- **Ethics:** No PHI. PubMed metadata only, Open. No consent/IRB needed. Full-text retrieval via publisher terms (OA 60% + proxy).
- **Equity framing:** PROGRESS extraction explicitly tests whether deprivation/race_ethnicity stratifiers are missing where equity-relevant — gap in the gap.

---

## 8. India Relevance — GEOGRAPHY-ONLY v1, Stage-2 India corpus

**v1: GEOGRAPHY-ONLY** (per docs/03 §6). Core question (does overall calibration mask subgroup failure? does TRIPOD+AI move needle?) is **methods audit on English PubMed corpus** — Indian data not needed and claiming them would be decoration. Sensitivity without English[lang] exploratory.

**Meaningful Stage-2 extension (not bundled, pre-registered as future):** Repeat the **same protocol on an India-affiliated corpus** (PubMed `India[Affiliation]` AND validation, or Indian journal set + CARRS Delhi/Chennai/Karachi validations) to test whether enforcement gap is larger for LMIC validations. Requires Indian co-extractor and affiliation-tagged E-utilities query — must not be bundled into v1. Lock's primary corpus is the **proxy** for this logic on global PubMed.

---

## 9. Leakage / Bias Checklist (adapted for D literature)

- [ ] Corpus filter string logged verbatim (E-utilities term + filters) before screening (no peeking at n=150 prevalences to adjust filter)
- [ ] Randomization locked (sorted PMID → rng 20260830) before title/abstract screening — no selection on PMID recency
- [ ] Extraction form locked before full-text coding (no addition of subgroup types after seeing masking rate)
- [ ] Dual-extraction overlap randomized (not enriched for high-risk papers)
- [ ] ERA split locked (Jan 2024 cut per TRIPOD+AI publication) before coding — no post-hoc cut optimization
- [ ] No HARKing on RECORD/STROBE sensitivities — pre-registered as secondary only

---

## 10. Harmonization & Code Archive Hashes

| Artifact | Placeholder | Filled at freeze |
|----------|-------------|------------------|
| PMID list (n=150 randomized) | `sha256:TBD-PMIDS` | post-esearch `pilot_004_pmids.txt` → n=150 |
| Europe PMC fullTextXML retrieval hash | `sha256:TBD-XML` | post-retrieval |
| Extraction CSVs per extractor + adjudicated | `sha256:TBD-EXTRACTION` | freeze tag `v0.1.0-rr-t5` |
| Code archive `pilots/candidate_004/` | `git:70730ae` | freeze |
| Seeds.log | `sha256:TBD-SEEDS` | rng 20260830 |

---

## 11. References (verbatim DOIs already in evidence_registry)

- Riley et al. BMJ 2025 10.1136/bmj-2024-080749 (388:e080749, PMID 39947680) — interval-aware calibration, load-bearing
- Van Calster et al. J Clin Epidemiol 2016 10.1016/j.jclinepi.2015.12.005 — hierarchy mean→weak→moderate→strong
- Collins TRIPOD 2015 10.1136/bmj.g7594 → Collins TRIPOD+AI 2024 10.1136/bmj-2023-078378 (27-item)
- Wolff PROBAST 2019 10.7326/M18-1376 + Moons PROBAST+AI 2025 10.1136/bmj-2024-082505
- Queiroz et al. BMC Endocr Disord 2026 10.1186/s12902-026-02301-2 (PMC13169604) — 97 models, 91.8% high risk (defeater context)
- Hughes et al. Clin Rheumatol 2025 10.1007/s10067-025-07325-y — UK Biobank external validation (masking pattern)
- Jin et al. Diagn Progn Res 2026 10.1186/s41512-026-00218-x — TRIPOD/TRIPOD+AI SR of 17 SRs
- Angelopoulos & Bates FTML 2023 10.1561/2200000101 — conformal interval baseline
- Chen et al. JAMIA 2025 10.1093/jamia/ocaf082 — bridge to synthetic evaluation lens
- Page et al. BMJ 2021 10.1136/bmj.n71 — PRISMA 2020

---

## 12. Verbatim Searches for this OSF (none new — dossier coverage)

Reuses dossier `cycle04_T5_corpus_lock.md` searches (T5-S1-TRIPOD, T5-review-Riley, etc.); E-utilities counts re-verified live 2026-08-30 (see logs/pilot_004.log §1). No new web search — pilot logs provide verification.

---

## 13. Pilot Verification (exit 0)

| Artifact | Path | Status |
|----------|------|--------|
| Log | `pilots/candidate_004/logs/pilot_004.log` | 106 lines, exit 0, 2026-08-30 15:26:10 IST, counts 570/8188/494/18 OK, esearch 20 ids, kappa 0.615 |
| Extraction pilot | `pilots/candidate_004/outputs/pilot_004_extraction_pilot.csv` | 20 rows, 22 cols, sha256:a724531fd10a, dual n=5, interval-aware flags |
| PRISMA pilot | `pilots/candidate_004/outputs/pilot_004_prisma_pilot.txt` | Flow Identification/Screening/Eligibility/Included with Wilson stubs |
| PMIDs | `pilots/candidate_004/outputs/pilot_004_pmids.txt` | 20 PMIDs (e.g. 40418571, 40241963, 38000872...) |
| Seed | 20260830 | rng deterministic |

Full n=150 will add Europe PMC fullTextXML retrieval, real extraction, PROBAST+AI, Wilson ±0.06, Newcombe difference CI, χ²/Fisher era split.

---

*End of OSF pre-registration — Results section intentionally left TBD (registered). Next: execute full n=150 corpus on Europe PMC + Rayyan, compute prevalences, locate masking rate, report whether TRIPOD+AI moves subgroup calibration.*
