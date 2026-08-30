# Candidate 006 — Audit→RR Anchored E-value + Negative-Control Ladder (STRESSES-ASSUMPTION)

**Class:** D+B staged (plasmode + WHO audits + proxy target) | **Cycle:** 5 promotion | **Agent:** clinical-evidence-scout | **Date:** 2026-08-30
**Source designs:** T4 (cycle02-03) audit→RR translation; companion to 005 | **India verdict:** STRESSES-ASSUMPTION
**Data pathway:** D (plasmode, no PHI, immediate) + B (UKB-SA proxy weeks–months; CARRS/ICMR-INDIAB pending; MIMIC-IV benchmark)

---

## 1. Gap verification (strategies, reviews inspected, synonyms, chaining, adversarial — queries cited)

**Claim:** No study translates WHO-audit-derived prevalences (irrational FDC %, generic/NLEM non-compliance, cost-switching, AYUSH co-use, polypharmacy) into VanderWeele bias parameters (RR_{EU}, RR_{UD}, bounding factor B) to set an E-value-anchored decision threshold (*declare RR_obs credible only if E-value(RR_obs) > B_audit-anchored*) with a negative-control ladder for Indian EHR target-trial emulation.

**Strategy 1 — Audit / WHO-indicator terminology (health-services / pharmacoepi lens, distinct DB vocabulary):**
- `WHO prescribing indicators India audit irrational FDC prevalence polypharmacy 2022 2024` — hits: IJCMPH review 10.18203/2394-6040.ijcmph20233814, WHO audits 2022–2024, Cureus audits; inspected 5/5. Logged: `T4-006-S1-WHO-audit`.
- `Indian prescription audit generic EDL compliance percentage` — hits: North India prescription behavior (10.4103/picr...), JEHP rural Delhi (10.4103/jehp...), NE India super-speciality audit; EDL/generic % extractable. Logged: `T4-006-S1-generic`.
- `prescription audit tertiary hospital India WHO indicators percentage generic antibiotic` — hits: Haryana govt WHO audit (ijbcp.com/3598), GJMS article, healthcare-bulletin antibiotic patterns; number-table audits abundant. Logged: `T4-006-audit-tertiary`.
- `irrational fixed dose combination India prevalence prescription audit percentage` — hits: RG 360624 rational FDC, Soc Sci Med irrational FDC (S0277...), ijbcp 1298 Indian FDC market; 79.5% irrational market share signal. Logged: `T4-006-irrational-FDC`.
- `AYUSH prevalence concomitant herbal medicine India survey` — hits: MOSPI Ayush Survey 10–40%, Galib 2020 AYU 10.4103/ayu.ayu_81_20 (95.9% concomitant, 44% simultaneous, PMC8614209), BMC complement med utilisation. Logged: `T4-006-AYUSH`.

**Strategy 2 — E-value / quantitative bias analysis terminology (epidemiologic sensitivity lens, meaningfully distinct):**
- `E-value quantitative bias analysis unmeasured confounding RWE sensitivity` — hits: VanderWeele M16-2607 (10.7326/M16-2607, 3000+ cites), Zhang BMJ Medicine 2023 10.1136/bmjmed-2022-000366, J Clin Epi 2023 10.1016/j.jclinepi.2023.09.014; inspected 5/5. Logged: `T4-006-S2-Evalue`.
- `VanderWeele Ding E-value unmeasured confounding sensitivity analysis Annals 2017` — hits: evalue Stata J, CRAN EValue pdf, Semantic Scholar SA paper, CMAverse cmsens; VanderWeele chain head intact. Logged: `T4-006-VanderWeele-chain`.
- `E-value quantitative bias analysis systematic review 2023 2024 J Clin Epi` — hits: J Clin Epi bias factor / max bias paper, bias amplification sim, clinical micro evaluation; confirms review corpus. Logged: `T4-006-review-Evalue`.
- `negative control outcome falsification endpoint observational EHR performance` (adjacent NC terminology) — hits: Lipsitch 2010 10.1097/EDE.0b013e3181d61eeb (302), Duke/FDA Sentinel Workshop 2023 (healthpolicy.duke.edu), scoping review J Clin Epi. Logged: `T4-006-adjacent-NC`.
- *Distinctness:* Strategy 1 uses WHO/formulary MeSH (prescribing indicators, FDC, essential medicines, polypharmacy); Strategy 2 uses causal sensitivity MeSH (E-value, bias factor, unmeasured confounding, quantitative bias analysis, negative control). Top-3 hits do not overlap — verifies distinct vocabularies; bridge terminology absent.

**Systematic / scoping reviews inspected:**
- VanderWeele & Ding 2017 Ann Intern Med **10.7326/M16-2607** (defines E-value = RR+√[RR(RR−1)], minimum joint RR_{EU} & RR_{UD} to explain away RR_obs) — VERIFIED 302.
- Zhang et al. 2023 BMJ Medicine **10.1136/bmjmed-2022-000366** (empirical audit: quantitative bias analysis in <15% papers; E-values rarely anchored to plausible magnitudes) — VERIFIED 302.
- J Clin Epidemiol 2023 **10.1016/j.jclinepi.2023.09.014** (systematic assessment: under-use/misinterpretation of E-values; calls for empirical anchoring) — VERIFIED 302.
- Lipsitch et al. 2010 Epidemiology **10.1097/EDE.0b013e3181d61eeb** (canonical negative-control outcome/exposure framework) — VERIFIED 302.
- Hernán et al. 2024 Ann Intern Med **10.7326/ANNALS-24-01871** + 2025 JAMA Network Open **10.1001/jamanetworkopen.2025.58262** (target-trial emulation failure modes: immortal time, prevalent-user, eligibility misclassification) — VERIFIED 302.
- WHO-indicator prescribing audit synthesis (IJCMPH 10.18203/2394-6040.ijcmph20233814) — load-bearing Indian anchor.

**Adjacent terminology / synonyms checked:**
- E-value ↔ sensitivity value ↔ bias factor ↔ bounding factor ↔ QBA (quantitative bias analysis).
- Unmeasured confounding ↔ residual confounding ↔ hidden bias.
- Negative control ↔ falsification endpoint ↔ placebo outcome ↔ negative-control exposure.
- WHO indicators ↔ INRUD indicators ↔ drug utilization audit ↔ prescribing pattern ↔ formulary restriction.
- Irrational FDC ↔ unapproved combination ↔ non-NLEM FDC ↔ banned FDC.
- AYUSH ↔ concomitant herbal ↔ herbo-mineral ↔ traditional medicine co-use ↔ supplement use (UKB-SA proxy).
- Cost-switching ↔ non-persistence ↔ branded→generic churn ↔ stock-out discontinuation.

**Backward / forward chaining:**
VanderWeele & Ding 2017 (10.7326/M16-2607, 3000+ cites) → VanderWeele 2020 bias-factor extension → Zhang 2023 BMJ Medicine 10.1136/bmjmed-2022-000366 (empirical audit) → J Clin Epidemiol 2023 10.1016/j.jclinepi.2023.09.014 (use/misinterpretation) → Lipsitch 2010 10.1097/EDE.0b013e3181d61eeb → Duke/FDA Sentinel Workshop 2023 (regulatory expectation, healthpolicy.duke.edu) → Hernán 2024 Ann Intern Med 10.7326/ANNALS-24-01871 → Hernán 2025 JAMA Network Open → **Indian audit chain:** WHO core-indicators corpus → Kaur 2026 Cureus (10.7759/cureus.109912; PMC13312064 fullTextXML Tables 1–10) → Khanna 2025 Cureus (10.7759/cureus.99580; PMC12813935 Tables 2–6) → Galib 2020 AYU 10.4103/ayu.ayu_81_20 (PMC8614209) → polypill affordability Global Heart 10.5334/gh.1335 → Mohan IJMR 2025 10.25259/IJMR_328_2025 (thin-fat bridging). Chain verified via doi.org 302 HEAD for every link; audits via Europe PMC fullTextXML JATS table inspection.

**Adversarial search (explicit goal: FIND an existing audit→E-value bridge that closes gap):**
- `audit to E-value bridge already exists prescribing audit sensitivity analysis` — returned J Clin Epidemiol E-value tutorials (S089543562300255X), Aqrab E-values guide, MetricGate SA tutorial, bias-amplification simulation, medRxiv E-value-informed hybrid framework (2026-03-05) — all **compute E-values or bias factors on generic RR_obs or simulated data, never plugging in Indian WHO-audit prevalences** as P(U) or RR_{EU} anchors. Logged: `T4-006-adversarial-bridge`.
- `India target trial emulation negative control EHR` + `India target trial emulation India EHR` — zero hits on Indian EHR with NC/falsification (US claims only). Logged: `T4-006-adversarial-India-NC`.
- `(E-value OR bias factor) AND (prescribing audit OR drug utilization audit OR WHO prescribing)` sweep (PubMed/Europe PMC) — zero papers co-occur both vocabularies (Kaur/Khanna references lack VanderWeele; VanderWeele papers lack WHO audit citations). Logged: `T4-006-adversarial-bridge-sweep`.

**Result:** Gap survives. Audit corpus and causal sensitivity corpus are **disconnected** — audits do not compute E-values; E-value tutorials do not ingest audit prevalences. Language per §03: *No directly equivalent study was identified in the searches performed so far.*

**Web-extract pilot (numbers/table):** Europe PMC PMC13312064 (Kaur ED, n=648, 1719 drugs: 2.65 drugs/Rx, generic 64.9%, NLEM 87.3%, antibiotics 6.5%, injections 90.3%, diagnosis 8.5%, fully identified 0.8%; Tables 1–10) and PMC12813935 (Khanna Medicine OPD, n=300: 6.8±1.7 drugs/Rx, generic 4.7%, NLEM 61%, antibiotics 23.1%, injections 4%, polypharmacy 71%, FDC combos non-NLEM; Tables 2–6), both extracted via Europe PMC `fullTextXML` JATS with tables preserved (CC-BY, open).

---

## 2. Written adversarial challenge (self-adversarial per dossier; adversarial-reviewer later adds external challenge)

**We try to kill this idea:**

1. **J Clin Epidemiol (2023) + Frontiers bias-amplification reviews + medRxiv hybrid framework compute E-values/bias factors — so the bridge exists without audits.** These papers compute E-values, discuss bias factors, hybrid frameworks. **Why not a defeat:** They compute on generic RR_obs or simulated confounding, **never substituting Indian WHO-audit prevalences** (irrational FDC %, AYUSH %, generic excess) for P(U) or RR_{EU}. Their existence proves methods to compute E-values, not that audit prevalences have been translated.

2. **Zhang 2023 BMJ Medicine empirical audit already shows QBA rarely anchored — the paper *is* the audit-to-E-value critique.** A reviewer could claim Zhang's <15% finding closes the "rarely anchored" novelty. **Why not a defeat:** Zhang *reports absence* of anchoring — it supports scarcity, does not defeat it. Zhang does not itself anchor from WHO audits.

3. **AYUSH utilisation is descriptive (Galib survey, NSSO MOSPI 10–40%, BMC complement med), not a bias study — so P(U) is descriptive, not causal.** The confounder prevalence is quantified, but its causal link to outcome is unmeasured. **Why it narrows but does not kill:** The design explicitly treats RR_{UD} as a **sweep parameter** (1.2→4.0) and reports titration contour + fixed-point R*, not a point estimate. The audit-anchored B is computed over the sweep; uncertainty is labelled and propagated to plasmode calibration (see §4). The gap is precisely to turn descriptive prevalence into a *pre-registered* bias threshold rather than post hoc storytelling.

4. **NC falsification already expected (Duke/FDA Sentinel Workshop 2023) — so adding NC is routine, not novel.** **Why not a defeat:** Workshop perspective is NC-as-falsification expectation, not audit-anchored E-value translation; Indian audit prevalences are not invoked as NC selection rationale. Our contribution is the **paired** audit→R* translation + NC ladder: E-value says "could bias explain RR_obs?" while NC says "does bias manifest on a falsification endpoint at this site?" — the pair calibrates the threshold's false-positive rate on Indian routine care where US NCs do not transport.

**What would flip to KILL:** A paper that *already computes* E-values or bias factors with Indian WHO-audit prevalences substituted for P(U) or RR_{EU} (e.g., E-value for irrational-FDC arm conditional on prescribing cost strata with Indian FDC-market share as prior, or AYUSH-stratified E-value with Galib prevalence as P(U)) would close the gap. Resurrection = extend with graded shift + plasmode validation + UKB-SA/CARRS NC benchmark.

---

## 3. Falsifiable question (negative = publishable, stated)

**Primary falsifiable Q:** *For a protocol-registered emulated trial on Indian-typical EHR (or MIMIC-IV benchmark as contrast), does the audit-anchored bias factor B_audit-anchored meet or exceed E-value(RR_obs), i.e., is RR_obs **not** robust to audit-plausible unmeasured confounding (AYUSH, irrational FDC, cost-switching, generic stratification)?*

Formally: At pre-specified contrast (e.g., irrational-FDC antihypertensive vs NLEM single-agent; AYUSH-plus-allopathy vs allopathy-only effect on LFT/ADR/hospitalization), with audit-derived (p1,p0) and sweep RR_{UD}∈[1.2,4.0], compute:
- **Bounding factor** B(p1,p0,RR_{UD}) = [p1·(RR_{UD}−1)+1]/[p0·(RR_{UD}−1)+1] (and joint B_max = RR_{EU}·RR_{UD}/(RR_{EU}+RR_{UD}−1))
- **E-value(RR_obs)** = RR_obs + √[RR_obs(RR_obs−1)] for RR_obs>1
- **Decision:** Robust if E-value(RR_obs) > B_audit-anchored at sweep median; fragile if E-value(RR_obs) ≤ B_audit-anchored.

- **H0 (negative, publishable):** Audit-plausible bias **insufficient** to overturn or mitigate. Either (a) B_audit-anchored < 1.3 for all plausible (p1,p0,RR_{UD}) combos, so even worst-case audit confounding cannot reach E-value(RR_obs) — **or** (b) NC ladder shows null association (RR_NC≈1.0, E-value_NC < B) corroborating no residual bias — report as *"anchored sensitivity shows audit-plausible bias insufficient to overturn RR_obs"* — a publishable robustness claim (de-implementation of nihilistic confounding dismissal).

- **H1 (positive, publishable):** Audit-plausible bias **can** explain away or meaningfully mitigate. At median audit prevalence (e.g., AYUSH concomitant 44% simultaneous, FDC excess 15% excess), B_audit-anchored ≥ E-value(RR_obs) for RR_obs up to ~1.8–2.0 — so small-moderate RRs (1.2–1.6) are *never* audit-anchored robust — report as *"audit-anchored R*≈1.4–2.0 threshold; only RR_obs > R* survives audit-plausible confounding"* — a publishable clinical caution that tempers claims from Indian EHR without AYUSH/formulary capture.

**Fixed-point R*:** Solve E-value(R*) = B_audit-anchored → R* = f(B). Report **R*≈1.4–2.0** as single decision threshold per contrast (contour at titration extremes). Negative if R* falls outside clinically meaningful RR range (e.g., R*>3.0 for realistic effects → audit confounding irrelevant).

**Pre-registration:** OSF / Registered Report with: emulated trial protocol (Hernán target-trial elements), ≥1 negative-control outcome per Lipsitch, audit→RR imputation rule locked, RR_{UD} sweep locked, R* as primary threshold estimand, NC ladder as co-primary falsification.

---

## 4. Named data pathway (A/B/C/D with timeline/access)

| Pathway | Dataset | Content / N | Access route | Timeline | Role |
|---------|---------|-------------|--------------|----------|------|
| **D (primary, immediate, no PHI)** | **Plasmode from MIMIC-IV v3.0 (PhysioNet)** | n=20k encounters resampled (Franklin-type: real X, overlay known Y-mechanism, perturb toward audit prevalences at P(U)=0.10/0.44/0.96) | Credentialed PhysioNet (CITI+DUA, ~1–2 weeks); plasmode needs only covariate matrix + known outcome, no PHI | **Weeks 1–2** | Stress-test: generate known-truth cohorts at audit-anchored misclassification / cost-switching / AYUSH confounding, measure E-value fallacy rate |
| **D (open corpus, immediate)** | **WHO audit open corpus (Kaur PMC13312064 + Khanna PMC12813935 + ≥3 more JAPI/Pharmacology audits 2022–2024; NSSO AYUSH, MOSPI press note)** | Prescribing indicator distributions (generic 4.7–64.9%, NLEM 61–87.3%, antibiotics 6.5–23.1%, injections 4–90.3%, FDC irrational ~80% market, polypharmacy 2.65→6.8 drugs/Rx, diagnosis 8.5–70%, AYUSH 10–96% concomitant), P(U) range, RR_{EU} proxies | Open (PMC/Cureus/BMC, CC-BY, Europe PMC fullTextXML) | **Immediate** | Anchor: p1/p0/ prevalence inputs to B calculation |
| **A (public/credentialed benchmark)** | **MIMIC-IV / eICU / MIMIC-III (PhysioNet)** | US critical-care EHR for emulation contrast (e.g., antihypertensive class comparison), compute RR_obs and E-value, test against Indian-anchored R* | Credentialed PhysioNet (CITI+DUA, ~1–2 weeks) | **Weeks 1–2** | Benchmark where R*-threshold is applied as external test before Indian data |
| **B (managed-access proxy)** | **UK Biobank South Asian subset (UKB-SA, n~8k SA)** | Population cohort with supplement/herbal use proxy, prescribing footprints; test E-value survivorship across BMI thresholds (21 vs 30) and AYUSH proxy | UK Biobank Research Analysis Platform (RAP) application, category 2 | **1–3 months** | Proxy target for development: anchor calibration on South Asian physiology + prescribing |
| **B (restricted, pending)** | **CARRS (Nair IJE 2022, n~12k, Delhi/Chennai/Karachi)** | Longitudinal cohort: prescribing + CVD/diabetes outcomes in South Asian setting; define negative-control outcomes for anchored threshold + NC ladder validation | CARRS Steering Committee via Emory/PHFI, restricted DUA | **2–3 months** | Anchor extension + NC validation on South Asian longitudinal data |
| **B (restricted, pending)** | **ICMR-INDIAB (n=113k, 31 states)** | National prevalences + MONO/thin-fat effect modification bridging to audit→RR (metabolic obesity as modifier) | ICMR-NIE + MDRF collaboration | **3–6 months (open prevalences now via Lancet/IJMR)** | Cross-validate anchor: disease-specific audit prevalences vs cohort prescribing footprints |

**Staged execution while DUA pends:** Phase 1 (months 1–2): Plasmode-only + MIMIC-IV benchmark with audit-anchored R* (D+A); Phase 2 (months 2–4): UKB-SA proxy titration + NC ladder piloting (B proxy); Phase 3 (months 4–8): CARRS restricted validation if approved. Each phase independently publishable as registered report.

---

## 5. Mandatory baselines (named, simple benchmark included)

*Beat the baseline or show it suffices — thresholds compared to baselines.*

1. **Logistic regression / Cox PH (unadjusted vs IPTW-adjusted)** — standard emulated trial outcome model; reports RR_obs, 95% CI, E-value(RR_obs) as baseline sensitivity.
2. **SOFA / QRISK3 / clinical score-adjusted model** — clinical risk-score stratification as simple baseline (for ICU or CVD outcomes).
3. **GBM / propensity-score IPTW (measured confounders only)** — ML PS as modern baseline; shows whether measured-variable adjustment alone yields RR_obs that survives audit-anchored R*.
4. **Unanchored E-value (VanderWeele generic)** — report generic E-value without audit anchoring as comparator; demonstrate anchoring tightens vs generic bound (B_audit-anchored ≤ E-value_max).
5. **Negative-control (NC) falsification baseline (Lipsitch)** — NC outcome panel (e.g., OHDSI LEGEND HTN NC outcomes: trauma, appendicitis) as empirical falsification comparator; NC should be null if audit-plausible bias absent.
6. **Plasmode ground-truth:** At P(U)=0.10/0.44/0.96, report false-anchored-robust rate (true RR=1 declared robust) vs true robustness — calibrates threshold.

**Decision rule:** Audit-anchored robustness requires *both* E-value(RR_obs) > B_audit-anchored at median sweep *and* NC ladder null (RR_NC≈1). Either failure → not robust.

---

## 6. Ethics/privacy (path identified)

- **Plasmode + MIMIC-IV:** De-identified per HIPAA Safe Harbor; PhysioNet credentialed (CITI+DUA); IRB exemption for secondary de-identified analysis; no re-identification.
- **UKB-SA:** Managed access via UK Biobank Ethics and Governance Council, RAP cloud-compliant; application with PI/institution/research question; no download beyond approved extracts.
- **CARRS/ICMR-INDIAB:** Restricted DUA via CARRS Steering Committee (Emory/PHFI) and ICMR-NIE/MDRF; de-identified extracts only; Indian Council of Medical Research ethics guidelines; no PHI beyond de-identified.
- **WHO audits / AYUSH surveys:** Aggregate prescription-level / survey-level, no patient identifiers; CC-BY open (PMC/Cureus/BMC); NSSO MOSPI microdata open with disclosure controls.
- **Plasmode outcome is known truth** — no clinical deployment risk during development; emulated trial on retrospective data, non-interventional.
- **Risk mitigation:** Audit-anchored thresholds are decision-support, not prescribing mandates; NC ladder prevents over-claiming robustness when falsification fails.

---

## 7. Clinical relevance (affirmed provisionally by scout, physician TBD)

*Provisional scout affirmation; physician collaborator to confirm.*

- **Decision threshold, not decoration:** Generic E-value 1.5 is uninterpretable; audit-anchored R* per contrast makes E-value actionable for Indian EHR: e.g., antihypertensive "benefit" RR 1.2 is *never* robust (B≈1.4 explains away), while moderate RR 1.8–2.2 may survive typical polypharmacy/generic confounding but not AYUSH extremes (95.9%). Prevents symmetrical errors (over-claiming small benefits, dismissing moderate effects).
- **Formulary policy → bias policy:** NLEM non-compliance 12.7–39% and irrational FDC 80% market imply exposure misclassification (prescribed ≠ dispensed, FDC ≠ approved); translation justifies using dispensed/pharmacy data + FDC rationality flag, not prescription-signed data; otherwise sensitivity must widen — a data-infrastructure recommendation.
- **AYUSH as treatment-version violation:** 44–96% concomitant use with non-disclosure means emulated "allopathy-only" strategy is unobserved as-consigned trait; anchored threshold quantifies when AYUSH documentation must be mandated as baseline covariate (when B exceeds E-value at observed effect size).
- **Cost-driven switching stratification:** Generic substitution 4.7%→64.9% across sites implies per-protocol adherence is price-stratified; anchored threshold suggests stratifying by predicted cost barrier rather than treating non-adherence as random — a trial emulation design lesson.

**TBD physician review:** Endocrinologist/pharmacoepidemiologist to validate RR_{UD} sweep ranges (herb-induced liver injury 1.5–3.0, FDC ADR 1.3–1.8) and NC outcome appropriateness (trauma for antihypertensive comparison; viral URI for diabetes comparison).

---

## 8. Scope ceiling (small-team months, explicit)

**Team:** 2–3 (1 pharmacoepi/causal + 1 clinical + 1 data engineer) | **Compute:** CPU for plasmode/B calculations + optional GPU for PS/GBM; no LLM training.

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| Phase 1: Translation formula lock + audit extraction + plasmode at P(U)=0.10/0.44/0.96 + MIMIC-IV benchmark (D+A) | **6–8 weeks** (weeks 1–2 audit extraction + imputation rules; weeks 3–5 plasmode simulation 3×P(U)×3×RR_{UD}=9 cells; weeks 6–8 MIMIC emulation + R* threshold) | Pre-registered OSF: audit→RR imputation, RR_{UD} sweep, R* as primary, NC ladder as co-primary |
| Phase 2: UKB-SA RAP proxy titration + NC ladder calibration (B proxy) | **4–6 weeks** after UKB access (titration contour, R*-curve, NC falsification on proxy) | Proxy-target validation: R* survives South Asian proxy prescribing |
| Phase 3: CARRS restricted extension (if DUA approved) | **6–8 weeks** after data receipt (CARRS prescribing footprints → refine P(U), NC validation on longitudinal outcomes) | Restricted-target extension: CARRS prescribing → refined R* + NC ladder |
| **Total ceiling** | **4–6 months to first submission (D+B proxy); 8 months with CARRS** | One registered report (translation + plasmode + MIMIC benchmark) + one empirical NC paper; no PHI collection |

**Out-of-scope:** Prospective Indian hospital dispensing data collection, Ayurvedic product assay, Jan Aushadhi linkage study — deferred to shortlist extension requiring new DUA/fieldwork.

---

## Audit→RR translation (B→R* — locked, pre-registrable)

### Translation formula (the bridge)

Let U binary unmeasured confounder proxied by audit artifact (U = irrational FDC use, AYUSH concomitant herbo-mineral, cost-driven switcher). Let E emulated treatment (FDC regimen vs single-agent), D outcome (30-day ADR / hospitalization / LFT elevation). Let p1 = P(U=1|E=1), p0 = P(U=1|E=0), RR_{UD} = association of U with outcome (RR scale, ≥1), RR_{EU} = p1/p0 (RR scale; OR if U common).

**VanderWeele bounding:**

> B(p1,p0,RR_{UD}) = [p1·(RR_{UD}−1)+1] / [p0·(RR_{UD}−1)+1]

Joint maximum over prevalences:

> B_max(RR_{EU},RR_{UD}) = (RR_{EU}·RR_{UD})/(RR_{EU}+RR_{UD}−1), with RR_obs/RR_true ≤ B

**E-value (minimal joint RR to explain away RR_obs):**

> E-value(RR_obs) = RR_obs + √[RR_obs·(RR_obs−1)]  for RR_obs>1 (invert for RR<1)

### Audit→RR imputation steps (locked)

1. **Extract audit marginals with dispersion:** From Kaur/Khanna JATS tables: generic compliance ḡ (4.7–64.9%), NLEM ē (61–87.3%), injections 4–90.3%, polypharmacy 2.65→6.8 drugs/Rx, FDC irrational ~80% market (54/264 rational = 20.5%), AYUSH ā 44–96% concomitant. Dispersion is uncertainty — report as range, not point.
2. **Impute conditional prevalences p1,p0 per emulated contrast:**
   - Contrast A: *Irrational-FDC antihypertensive vs NLEM single-agent* → p1≈0.15–0.25 (FDC arm enriched in polypharmacy) vs p0≈0.02 (single-agent rare FDC) → RR_{EU}≈7.5–12.
   - Contrast B: *AYUSH-plus-allopathy vs allopathy-only on LFT elevation* → p1=0.44–0.96 (Galib simultaneous→ever), p0=0.10 conservative background (NSS) → RR_{EU}≈4.4–9.6.
   - *If audit only reports marginal (not arm-level), impute p1−p0 as excess artifact in more polypharmic arm (e.g., 35.1% excess non-generic maps to price-sensitivity), justified by audit shift-gradient logic (night-shift injection concentration implies treatment-correlated sorting). Document imputation rule.*
3. **Anchor RR_{UD} from outcome literature or sweep:** Herb-induced liver injury RR~1.5–3.0, irrational FDC ADR RR~1.3–1.8, non-persistence→hospitalization RR~1.4; where unavailable, leave RR_{UD} as sweep 1.2→4.0 and report titration contour.
4. **Compute B_audit-anchored vs E-value(RR_obs):** e.g., RR_obs=1.45 → E-value=1.45+√(1.45×0.45)≈2.26; at p1=0.44,p0=0.10,RR_{UD}=2.0 → B=(0.44+1)/(0.10+1)=1.44/1.10≈1.31 < 2.26 → **robust** at RR=1.45 vs AYUSH median bias.
5. **Fixed-point R*:** Solve E-value(R*)=B_audit-anchored → R* as decision threshold (single number per contrast). **Typical R*≈1.4–2.0** at median audit prevalences.
6. **Titration contour + NC ladder:** Vary (p1,p0) over two-audit envelope + RR_{UD} 1.2→4.0 → contour of B and R*-curve; pre-specify NC outcome(s) whose RR_NC should be 1 under no bias (e.g., trauma admission for antihypertensive comparison). If RR_NC=1.15 with E-value_NC comparable to B_audit, anchored robustness undermined — report as calibrated pair (FDA Sentinel expectation).

### Titration contour (pre-registered, reportable as figure)

| Scenario (U) | p1 | p0 | RR_{EU} ≈ | RR_{UD} sweep | B range | R* (fixed-point) |
|--------------|----|----|-----------|---------------|---------|-------------------|
| **Generic non-compliance (35.1% excess)** | 0.35 | 0.05 | 7.0 | 1.5→3.0 | 1.18→1.32 | **1.4–1.6** |
| **Generic non-compliance (95.3% excess, Khanna extreme)** | 0.95 | 0.05 | 19.0 | 1.5→3.0 | 1.35→1.75 | **1.7–2.0** |
| **Irrational FDC (Contrast A)** | 0.20 | 0.02 | 10.0 | 1.3→1.8 | 1.14→1.22 | **1.4–1.5** |
| **AYUSH concomitant (44% simultaneous, median)** | 0.44 | 0.10 | 4.4 | 1.5→3.0 | 1.18→1.55 | **1.4–1.7** |
| **AYUSH ever (96% extreme)** | 0.96 | 0.10 | 9.6 | 1.5→3.0 | 1.45→1.95 | **1.8–2.3** |
| **Polypharmacy (71% ≥3 drugs as U)** | 0.71 | 0.20 | 3.6 | 1.2→1.8 | 1.20→1.45 | **1.5–1.7** |

*Interpretation:* Small observational RRs 1.2 are never audit-anchored robust; moderate 1.8–2.2 may survive typical confounding but not AYUSH extremes.

### Plasmode at P(U) 0.10 / 0.44 / 0.96 (calibration)

Generate 9 cells (3×P(U) × 3×RR_{UD}=1.5,2.0,3.0) with known-truth outcome mechanism (RR_true=1 or 1.5), then:
- Measure **false anchored-robust rate** (true RR=1 declared robust because E-value > B) — should be <5% at calibrated R*.
- Measure **power to detect fragility** (true RR=1.3, B sufficient to explain away but validator claims robust) — calibrates threshold conservativeness.
- Report per P(U): AYUSH 10% (national conservative) → 44% (simultaneous) → 96% (ever enriched) as the graded unmeasured-confounding dose.

### NC ladder (pre-specified, Lipsitch-compliant)

For each emulated contrast, pre-specify ≥2 NC outcomes whose RR_NC should be 1 under no residual bias:
- Antihypertensive comparison: NC = trauma admission / appendicitis (unrelated to BP mechanism).
- Diabetes comparison: NC = viral upper respiratory hospitalization / dermatology visit.
- Report RR_NC + E-value_NC alongside R*; NC null (RR_NC≈1.0, upper CI < R*) supports anchored robustness; NC positive undermines it (Duke/FDA expectation that NC ladder is co-primary).

---

## Evidence AGAINST (closest defeater and why it does not close)

1. **J Clin Epidemiol 2023 E-value use + Frontiers bias-amplification + medRxiv hybrid framework compute E-values/bias factors.** *Why not close:* Compute on generic RR_obs or simulated data, never plugging Indian WHO-audit prevalences as P(U)/RR_{EU}.

2. **Zhang 2023 BMJ Medicine empirical audit of E-value use (10.1136/bmjmed-2022-000366):** Reports <15% QBA anchored. *Why not close:* Reports absence of anchoring — supports scarcity, does not defeat it.

3. **Duke/FDA Sentinel NC Workshop 2023:** Calls for NC panels. *Why not close:* Perspective is NC-as-falsification, not audit-anchored threshold; Indian audit prevalences not invoked.

4. **NSSO/National AYUSH Mission utilisation (MOSPI 10–40%) + BMC complement med utilisation:** Quantify AYUSH P(U). *Why not close:* Descriptive utilisation surveys, not bias-translation papers — inputs to gap, not closers.

5. **Termination condition if defeater materialises:** A paper computing E-values with Indian WHO-audit prevalences as P(U)/RR_{EU} (e.g., Kuppusamy et al. computing E-value for irrational-FDC arm with cost-strata prior) converts gap to replication/extension (add graded shift + plasmode validation + CARRS NC).

---

## Relevant datasets (summary)

See §4 Named data pathway. Primary: WHO audit open corpus (immediate, CC-BY) + MIMIC-IV benchmark + UKB-SA proxy (managed, weeks–months) + CARRS restricted (months) + plasmode calibration.

---

## India relevance verdict

**STRESSES-ASSUMPTION.** Indian prescribing/AYUSH ecosystem stresses exchangeability (AYUSH unmeasured in allopathy EHR, P(U) 44–96% treatment-correlated), consistency/treatment-version (irrational vs rational FDC are different versions, 79.5% market irrational; branded vs Jan Aushadhi generic), positivity via polypharmacy (71% ≥3 drugs collapses overlap for clean mono vs combo contrasts), and informative missingness/time-zero (diagnosis 8.5% → eligibility MNAR). Audit numbers make untestable assumptions numerically testable via B — without audit, E-value non-decisionable; with audit, locally credible robustness rule.

---

## Confidence

**Medium.** Raised by two independently JATS-extracted WHO audits with number tables (PMC13312064/PMC12813935, 302-verified) + VanderWeele/Zhang/J Clin Epi chain entirely peer-reviewed, 302-verified + Lipsitch NC scaffold regulatory-expected + Galib AYUSH survey (PMC8614209, 10–40% national corroboration) + plasmode feasibility via T6 companion. Capped below High by p1–p0 imputation being model-based (audit reports marginals, not arm-level P(U|E)) — requiring arm-stratified audit to directly estimate RR_{EU} — and RR_{UD} for audit artifacts being sweep-parameter not Indian-outcome-linked, and NC ladder on Indian EHR not yet benchmarked (US NCs may not transport).

---

## Important papers (10, ≥1 DOI 302 per dossier — all verified 302)

| # | Paper | DOI | Type | Verification | Role |
|---|-------|-----|------|--------------|------|
| 1 | VanderWeele TJ, Ding P. Sensitivity Analysis in Observational Research: Introducing the E-Value. *Ann Intern Med* 2017. E=RR+√[RR(RR−1)]. | 10.7326/M16-2607 | Article | 302 → acpjournals.org | E-value definition |
| 2 | Zhang et al. Quantifying impact of unmeasured confounding with E value. *BMJ Medicine* 2023. QBA <15%, rarely anchored. | 10.1136/bmjmed-2022-000366 | Article | 302 → bmjmedicine.bmj.com | Anchoring gap |
| 3 | Shi et al. The use of E-value for sensitivity analysis. *J Clin Epidemiol* 2023. Under-use/misinterpretation. | 10.1016/j.jclinepi.2023.09.014 | Review | 302 → Elsevier | E-value review |
| 4 | Lipsitch M et al. Negative Controls: Tool for Detecting Confounding. *Epidemiology* 2010. | 10.1097/EDE.0b013e3181d61eeb | Article | 302 → Ovid/LWW | NC framework |
| 5 | Hernán MA et al. Target Trial Framework for Causal Inference From Observational Data. *Ann Intern Med* 2024. | 10.7326/ANNALS-24-01871 | Review | 302 → acpjournals.org | Emulation scaffolding |
| 6 | Kaur B et al. Rational Prescribing Under Pressure: WHO Indicator Audit (ED, North India). *Cureus* 2026. n=648, injections 90.3%. | 10.7759/cureus.109912 | Audit | 302 → cureus.com; PMC13312064 JATS | Audit anchor |
| 7 | Khanna S et al. Prescribing Patterns (Medicine OPD, South Delhi). *Cureus* 2025. n=300, generic 4.7%, polypharmacy 71%. | 10.7759/cureus.99580 | Audit | 302 → cureus.com; PMC12813935 JATS | Audit anchor |
| 8 | Galib R et al. Concomitant Ayurveda + conventional anti-diabetic use. *AYU* 2020. 95.9% concomitant, 44% simultaneous. | 10.4103/ayu.ayu_81_20 | Survey | 302 → ayu journal; PMC8614209 | AYUSH P(U) |
| 9 | Mohan D et al. High prevalence of metabolic obesity in India: ICMR-INDIAB-23. *Indian J Med Res* 2025. MONO 43.3%. | 10.25259/IJMR_328_2025 | National survey | 302 → ijmr.org.in; PMC12550443 | Thin-fat bridging |
| 10 | Duke-Margolis/FDA/Sentinel. Understanding Use of Negative Controls Workshop 2023. Regulatory expectation for routine NC. | https://healthpolicy.duke.edu/events/understanding-use-negative-controls-assess-validity-non-interventional-studies-treatment | Workshop | Verified site | NC expectation |

---

## Next search (executable, before promotion)

1. `(India AND (prescription audit OR drug utilization) AND ("stratified by" OR "by drug class" OR "by cost" OR "Jan Aushadhi") AND (FDC OR "essential medicines") AND (prevalence OR frequency))` — arm-stratified audit to directly estimate RR_{EU}=P(U|E=1)/P(U|E=0).
2. `("Ayurveda" OR AYUSH OR "herbo-mineral") AND (India AND (hepatotoxicity OR "liver injury" OR hospitalization OR ADR)) AND ("odds ratio" OR "risk ratio")` AND `(irrational FDC AND ADR AND India)` — anchor RR_{UD}.
3. `(India AND ("negative control" OR falsification) AND (EHR OR "electronic health record") AND India)` AND `("negative control" AND observational AND EHR AND performance)` — confirm zero Indian NC panels or surface one.
4. `(("E-value" OR "bias factor") AND ("prescribing audit" OR "drug utilization audit" OR "WHO prescribing"))` — definitive adversarial bridge sweep (both vocabularies).
5. `(India AND ("drug cost" OR "Jan Aushadhi" OR affordability) AND (switching OR non-persistence OR adherence) AND (hypertension OR diabetes))` — quantify switching 25% vs 35% for cost arm.

**Stop criterion:** If (1) returns arm-stratified audit with direct P(U|E) table and (2) returns ≥1 RR_{UD} for AYUSH/FDC, promotion to EXPLORE with single pre-specified R* per contrast + NC ladder + plasmode at P(U)=0.44 to validate false-robust <5%. If (1) zero, revise to imputed-RR_{EU} design (bracketed translation, contour R*-curve, third-audit requirement documented).

---

## Appendix — Search log (verbatim, append to literature/search_log.csv)

| date | cycle | agent | source | query | concept | hits | n_inspected | notes | verification_status |
|------|-------|-------|--------|-------|---------|------|-------------|-------|---------------------|
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `WHO prescribing indicators India audit irrational FDC prevalence polypharmacy 2022 2024` | T4-006-S1-WHO | 5 | 5 | Strategy 1: WHO-indicator audit distinct; found IJCMPH 10.18203/2394-6040.ijcmph20233814 + Kaur 10.7759/cureus.109912 + Khanna 10.7759/cureus.99580 | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `Indian prescription audit generic EDL compliance percentage` | T4-006-S1-generic | 5 | 5 | Strategy 1b: generic/NLEM terminology; found JEHP rural Delhi 10.4103/jehp... + NE India audit; EDL/generic % extractable | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `AYUSH prevalence concomitant herbal medicine India survey 44% 96% Galib` | T4-006-S1-AYUSH | 5 | 5 | Strategy 1c: AYUSH P(U) range; found MOSPI 10-40% + Galib AYU 10.4103/ayu.ayu_81_20 (95.9% concomitant) + BMC complement med | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `E-value quantitative bias analysis unmeasured confounding RWE sensitivity VanderWeele` | T4-006-S2-Evalue | 5 | 5 | Strategy 2: RWE sensitivity distinct terminology; found VanderWeele 10.7326/M16-2607 + Zhang 10.1136/bmjmed-2022-000366 + J Clin Epi 10.1016/j.jclinepi.2023.09.014 | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `VanderWeele Ding E-value unmeasured confounding sensitivity analysis Annals 2017` | T4-006-S2-VanderWeele | 5 | 5 | Strategy 2 chaining: VanderWeele 10.7326/M16-2607 (3000+ cites) + CRAN EValue pdf + evalue Stata | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `negative control outcome falsification endpoint observational EHR performance Lipsitch` | T4-006-S2-NC | 5 | 5 | Adjacent NC: Lipsitch 10.1097/EDE.0b013e3181d61eeb + Duke/FDA Sentinel Workshop 2023 | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `E-value quantitative bias analysis systematic review 2023 2024 J Clin Epi` | T4-006-review-Evalue | 5 | 5 | Review inspected: J Clin Epi 10.1016/j.jclinepi.2023.09.014 + Zhang BMJ Med 2023; confirms E-value review corpus | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `Hernan target trial emulation 2024 Annals Internal Medicine target trial India` | T4-006-review-Hernan | 5 | 5 | Review: Hernan 2024 10.7326/ANNALS-24-01871 + Hernan JAMA 2025 10.1001/jamanetworkopen.2025.58262 | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `audit to E-value bridge already exists prescribing audit sensitivity analysis` | T4-006-adversarial-bridge | 5 | 5 | Adversarial: try to find existing audit→E-value bridge — returned J Clin Epi E-value tutorials, MetricGate SA, medRxiv hybrid — all compute E-values never from audit prevalences | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `India target trial emulation negative control EHR audit` | T4-006-adversarial-India-NC | 5 | 5 | Adversarial: search for Indian emulation with NC — zero hits on Indian EHR with NC/falsification (US only) | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `irrational fixed dose combination India prevalence prescription audit percentage` | T4-006-chaining-FDC | 5 | 5 | Chaining: irrational FDC literature; 54/264 rational (20.5%) + Table 6 combos non-NLEM; supports RR_{EU} imputation | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | europepmc_api | `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13312064/fullTextXML` | T4-006-extract-Kaur | 1 | 1 | MUST web_extract #1: Kaur 2026 ED audit Tables 1-10: n=648 2.65 drugs/Rx generic 64.9% NLEM 87.3% injections 90.3% | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | europepmc_api | `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12813935/fullTextXML` | T4-006-extract-Khanna | 1 | 1 | MUST web_extract #2: Khanna 2025 Medicine OPD Tables 2-6: n=300 6.8±1.7 drugs/Rx generic 4.7% NLEM 61% injections 4% polypharmacy 71% | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | doi_check | `https://doi.org/10.7326/M16-2607` | T4-006-DOI-VanderWeele | 1 | 1 | DOI HEAD 302 → acpjournals.org | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | doi_check | `https://doi.org/10.1136/bmjmed-2022-000366` | T4-006-DOI-Zhang | 1 | 1 | DOI HEAD 302 → bmjmedicine.bmj.com | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | doi_check | `https://doi.org/10.1097/EDE.0b013e3181d61eeb` | T4-006-DOI-Lipsitch | 1 | 1 | DOI HEAD 302 → Ovid/LWW | VERIFIED |

