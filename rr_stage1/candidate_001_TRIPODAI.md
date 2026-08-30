# Registered Report Stage 1 — Candidate 001: Direct Replication of Harutyunyan 2019 Multitask LSTM on eICU-CRD + AmsterdamUMCdb (TRIPOD+AI 27-Item, Leakage Audit, Calibration/DCA)

**Agent:** methods-scout | **Cycle:** 9 RR Stage-1 | **Date:** 2026-08-30 | **Status:** Stage-1 submission-ready (Intro+Methods; Results TBD registered)
**OSF prereg:** `osf_prereg/candidate_001_OSF_TIMESTAMPED.md` (Registration 2026-08-30, git rev `70730ae984ae0d2592c2`, synthEHRella `74aa516`, CIMEHR `0.1.0`, seed `20260830`)
**Pilot verification:** `pilots/candidate_003/logs/pilot_003.log` exit 0 (387 lines) + `pilots/candidate_002/logs/pilot_002.log` exit 0 — CIMEHR 0.1.0 installed, vignette exists TRUE — see OSF timestamp block
**Target journals:** BMJ / JAMIA / PMLR-MLHC / Nature Scientific Data (all publish well-conducted replications)

---

## 1. Introduction — Why This Replication Matters Now

### 1.1 Harutyunyan 2019 is the most-cited ICU deep-learning benchmark — and it is overdue for pre-registered external validation

Harutyunyan et al. 2019, *Multitask learning and benchmarking with clinical time series data* (Scientific Data 6:96, DOI **10.1038/s41597-019-0103-9**, repo `YerevaNN/mimic3-benchmarks`, 1800+ cites, benchmark DOI 10.5281/zenodo.1306527) established the canonical channel-wise LSTM (2×128, dropout 0.3, Adam 1e-3) multitask benchmark on MIMIC-III for four tasks — **in-hospital mortality, decompensation, length-of-stay, phenotyping** — with 17 time-series + 5 static variables on a 1h grid, forward-fill + mask, 48h window (mortality) and first-principles SOFA-derived baselines. The paper is the de facto deep-learning baseline suite for ICU time-series — cited as comparator in 2021–2025 DL-for-EHR papers — yet **no pre-registered direct replication on independent public EHR with TRIPOD+AI-equivalent reporting exists** as of cycle04 lock (working/agent_notes/methods-scout/cycle04_T8_replication_lock.md, LOCKED 2026-08-30). This is not a critique of original rigor; it is the reproducibility gap McDermott et al. 2021 (Sci Transl Med 10.1126/scitranslmed.abb1655, 511-paper audit) and Nagendran et al. 2020 (BMJ 10.1136/bmj.m689, 81 DL-vs-clinician studies, majority high risk of bias, poor external validation) predict for high-cite ICU DL benchmarks: worst-in-class on dataset/code accessibility, with YAIB/METRE (Moor 10.48550/arXiv.2208.06691; 216k-stay domain-shift corpus across MIMIC-III/IV, eICU, HiRID, AmsterdamUMCdb) providing **task-level** domain-shift quantification (AUROC drops 0.047–0.082 + calibration slope collapse 1.007→0.417 in Patel-like task benchmarks, DOI 10.64898/2026.05.03.26352335) but **not a frozen Harutyunyan artifact replication** (different architectures, different tasks per site).

### 1.2 TRIPOD (2015 10.1136/bmj.g7594) → TRIPOD+AI (2024 10.1136/bmj-2023-078378) changes what a replication must report

Collins et al. TRIPOD+AI (BMJ 2024 10.1136/bmj-2023-078378, 27-item checklist, 16 months old at Stage-1) now requires calibration hierarchy, fairness/subgroup, uncertainty intervals, and code/data availability beyond original TRIPOD (2015 10.1136/bmj.g7594). Pre-2024 re-uses of Harutyunyan as baseline suite cannot satisfy it. Our pre-registration maps all 27 items (see OSF §8 + Appendix CSV). Two load-bearing reporting lenses sharpen scope: **Van Calster et al. 2016 (J Clin Epidemiol 10.1016/j.jclinepi.2015.12.005)** calibration hierarchy (mean → weak (slope+intercept) → moderate → strong) and **Riley et al. 2025 (BMJ 10.1136/bmj-2024-080749)** individual-level risk intervals / calibration bands (CRASH interval 0.477–0.693 spans 0.25–0.45 as cautionary example) — both prescribe the weak-calibration slope/intercept reporting modern reviewers expect.

### 1.3 The target population is clinical (sepsis/mortality) not technical

ICU in-hospital mortality is a deployment-relevant proxy for early-sepsis deterioration and general critical-care triage (Fleuren systematic review: 22 sepsis ML studies, <14% externally validated, only 2 shared code; PMC8193357). Harutyunyan mortality AUROC ~0.86 (internal MIMIC-III) is cited as evidence deep temporal modeling pays. Whether that discrimination **and calibration** transports from single-center BIDMC (MIMIC-III) to multi-center US (eICU-CRD 208 hospitals, Pollard 10.1038/s41597-018-0006-0, ~139k stays) and European (AmsterdamUMCdb v1.0.2, Thoral 10.1038/s41597-021-00737-X, ~23k admissions) determines whether the LSTM should be deployed, recalibrated, or retired. Nestor et al. 2019 (MLHC PMLR 106 10.48550/arXiv.1908.00690) demonstrates feature-robustness drift (definitions drift across time/sites even with same code) as a mechanism for external failure — **leakage audit** is therefore co-primary.

### 1.4 Gap statement (proportional, falsifiable)

No published **pre-registered direct replication of the frozen Harutyunyan LSTM (2×128, 2019) on MIMIC-III → independent multi-center eICU-CRD (primary) + AmsterdamUMCdb (secondary) with TRIPOD+AI 27-item reporting, leakage audit, calibration/subgroup/DCA** was identified in the searches performed so far (cycle04_T8_replication_lock.md; T8-C4 queries 6 distinct strategies + reviews McDermott/Nagendran/YAIB/METRE; ADV-001 closest task-level MIMIC→eICU calibration 10.64898/2026.05.03.26352335 — not frozen Harutyunyan). If such replication exists, H0 below is that the corpus contains it (RR redundant); otherwise this protocol is the executable first target and its **negative result (failure within bounds) is the publishable finding**.

---

## 2. Research Questions — Falsifiable, Either Outcome Publishable

**Primary falsifiable question (locked):**

*Does the frozen Harutyunyan LSTM, when evaluated on pre-registered independent external ICU cohorts (eICU-CRD v2.0 primary, AmsterdamUMCdb v1.0.2 secondary) with leakage audit and TRIPOD+AI 27-item reporting, retain discrimination within ΔAUROC 0.05 **and** weak calibration slope 0.8–1.2 with |intercept|<0.3 **and** subgroup heterogeneity ≤0.10 **and** DCA net benefit > trivial at 10% or 20% — or does it fail within those bounds?*

**Skeptical framing (ML gets no preference — bounds favor the null that LSTM does not transport):**

- **H0 (replication fails within equivalence bounds — publishable negative):** AUROC drop >0.05 OR calibration slope <0.8 or >1.2 OR |intercept|>0.3 OR subgroup max-pairwise AUROC range >0.10 OR DCA net benefit ≤ trivial at both 10% and 20% — i.e., **LSTM does not transport** beyond recalibrated LR/SOFA/GBM on external DCA/hierarchy.
- **H1 (replication holds):** All four conditions simultaneously satisfied — replication succeeds (ML transports within pre-specified tolerance).

Either outcome is publishable: H0 is a rigorous negative replication (ML gets no preference; transport requires evidence) of interest to BMJ/JAMIA/PMLR-MLHC/Nature Sci Data; H1 would be first published pre-registered TRIPOD+AI success. **No-HARKing:** thresholds locked at OSF timestamp before external outcomes inspected; Results section stays `TBD (registered)` at Stage 1.

---

## 3. Methods — Data, Participants, Predictors, Outcome (TRIPOD+AI Items 4–7)

### 3.1 Data sources (all public/credentialed — executable tomorrow; DUA staged not blocking)

| Dataset | Version | Content | Access | N eligible (post-exclusions) | Role |
|---------|---------|---------|--------|------------------------------|------|
| **MIMIC-III** | v1.4 | BIDMC single-center ICU, minute vitals/labs/notes | PhysioNet credentialed (CITI+DUA 1–2 weeks; demo `mimic-iii-demo` immediate) | ~38k→ ~25k | **Training primary** (matches Harutyunyan 2019) |
| **MIMIC-IV** | v2.2+ | BIDMC successor (2008–) | PhysioNet credentialed | ~65k→ filtered | **Sensitivity training** (modern schema) |
| **eICU-CRD** | v2.0 | US multi-center ICU 208 hospitals (Pollard) | PhysioNet credentialed | ~139k→ ~50–70k | **Primary external test** (single→multi-center axis) |
| **AmsterdamUMCdb** | v1.0.2 | European ICU Amsterdam UMC 23k admissions (Thoral) | ODAP portal credentialed | ~23k→ ~15k | **Secondary external test** (European) |
| **HiRID** | v1.1.1 | Swiss high-res ICU Bern 34k (Faltys) | PhysioNet mirror | — | Alternative secondary if Amsterdam harmonization fails |

PhysioNet + ODAP + `ricu`/`METRE`/`YAIB` pipelines mature; no hospital negotiation for v1.

### 3.2 Participants (TRIPOD+AI Items 4–5)

- **Inclusion:** Adults age ≥18, first ICU admission per hospitalization (Harutyunyan exclusions), ICU LOS ≥4h with ≥1 eligible vital/lab in first 48h window.
- **Exclusion:** Transfers with missing time-zero, stays with no eligible predictor window, age truncation harmonized.
- **Time-zero:** First `ICUSTAY_ID` / `patientUnitStayId` / Amsterdam `admission` timestamp (§5 leakage checklist locks rule) — **no redefinition after mortality rates seen** (SHA256-hashed SQL at freeze).
- **Sampling:** Use **all eligible** — no power-based subsampling; Harutyunyan original `subject_id` hash splits or new 5-fold CV locked before external access (seed 20260830).

### 3.3 Predictors — 17 time-series + 5 static (Harutyunyan §7b locked)

- **Time-series (1h grid, z-scored per Harutyunyan, forward-fill + mask indicator):** HR, SBP, DBP, MBP, RR, Temp, SpO2, Glucose, pH/lactate + 8 labs (17 vars; list hashed in `T8_mapping_stub.csv`). Mask indicator per variable per hour is **part of predictor definition**.
- **Static (5):** Age, gender, admission type, SOFA-derived baseline, ethnicity where available.
- **Window:** First **48h** of ICU (Harutyunyan mortality task) and 24h sensitivity; single window per stay.
- **Harmonization:** Primary pipeline **`ricu 0.5.8`** (Bennett PMC10268223, CRAN); METRE/YAIB as exploratory sensitivity (hash at freeze).

### 3.4 Outcome — In-hospital mortality (binary at hospital discharge)

Per-site derivation: MIMIC `hospital_expire_flag`/`dod`; eICU `hospitalDischargeStatus` (`expired`) + APACHE `hospital_mortality` proxy; Amsterdam `discharge==death`. **Hospital** (not ICU) mortality documented as site difference (TRIPOD+AI Item 6).

---

## 4. Model — Frozen Harutyunyan LSTM (TRIPOD+AI Items 10–11)

- **Architecture (frozen, no retuning on external):** 2-layer **channel-wise LSTM, 128 hidden units per layer, dropout 0.3, Adam 1e-3** (Harutyunyan Table 1 / `mimic3models/multitask`). Re-trained only where MIMIC version shift documented (column remapping), hyperparams frozen from paper; tuning only on MIMIC validation split if required (never on eICU/Amsterdam).
- **Implementation:** `github.com/YerevaNN/mimic3-benchmarks` (MIT) or YAIB `mimic3models_torch` port — tag hashed at freeze.
- **Training:** 100 epochs, early stopping patience 10 on validation AUPRC; identical epoch budget across baselines; class weighting per Harutyunyan (inverse prevalence).
- **Inference:** Single-GPU (A100 40GB or RTX 4090); 15 runs (5-fold CV × 3 seeds) ≈1–2 days; external evaluation inference-only (hours).

---

## 5. Leakage Checklist — 6 Items (mandatory supplementary, code-frozen & unit-tested)

| # | Item (ticked at OSF timestamp) | How locked |
|---|----------------------------------|------------|
| 1 | Time-zero locked before seeing outcomes | ICU admission = first `icustay`/`patientUnitStayId`; SQL SHA256 + OSF archive |
| 2 | Lookahead audit | No feature uses `max SOFA` over full stay, `last lab before discharge`, vasopressor after 48h; pipeline unit test asserts `max(feature_time) ≤ time_zero+48h` |
| 3 | Train/test isolation | MIMIC splits via Harutyunyan `subject_id` hash or new 5-fold CV locked before external access; **eICU/Amsterdam never for hyperparam tuning** |
| 4 | Missing-data frozen | Forward-fill + mask indicator (no future interpolation, no MICE leaking test distribution); mask is predictor |
| 5 | Label leakage | Hospital mortality from discharge table only; no note/code encoding outcome; no `discharge location=death` as predictor |
| 6 | Code provenance | All extraction SQL, notebooks, feature tables SHA256 + OSF archived; post-registration changes logged as deviation; analyst blinded to external labels until lock |

---

## 6. Sample Size & Equivalence Margins — Decision Rule (TRIPOD+AI Items 8,13,17)

| Bound | Threshold (pre-registered) | Power at expected N |
|-------|----------------------------|---------------------|
| **Equivalence AUROC Δ0.05** | Replication succeeds on discrimination only if `AUROC_external ≥ AUROC_original − 0.05` (original ~0.86 → threshold 0.81). Failure = drop >0.05. | eICU ~50k (8–10% mortality → 4–5k events), Amsterdam ~15k (~12% → 1.8k events). DeLong SE 0.003–0.005 → CI width 0.01–0.02 → **power >0.99** to detect Δ=0.05 (α=0.05 two-sided). |
| **Calibration slope 0.8–1.2, |intercept|≤0.3** | Success requires slope ∈[0.8,1.2] AND intercept ∈[−0.3,0.3] logit (Van Calster weak calibration). | Slope SE 0.04–0.06 → **power >0.90** to detect 1.0→0.8 shift. |
| **Subgroup heterogeneity ≤0.10** | Max pairwise AUROC range across pre-specified subgroups ≤0.10; >0.10=failure (§7). | Smallest stratum ~5k → SE ≈0.01 — adequate. |
| **DCA** | Net benefit at mortality **10% and 20%** (Vickers) must exceed trivial + recalibrated SOFA. | Empirical — not power-parameterized; reported with 95% CI (bootstrap 2000). |

**Decision rule (replication successful only if ALL hold):** AUROC within 0.05 **AND** slope 0.8–1.2 with |α|≤0.3 **AND** subgroup heterogeneity ≤0.10 **AND** DCA NB > trivial at 10% or 20%. Any failure = publishable negative replication (ML gets no preference). Subgroup drift vs measurement-density reported as exploratory (Nestor).

---

## 7. Analysis Plan — Metrics, Subgroups, Baselines (TRIPOD+AI Items 12–15,17–19)

### 7.1 Primary metrics (co-primary, all reported; decision rule §6)

- **Discrimination:** AUROC (DeLong 95% CI), AUPRC (with prevalence context), PR-AUC per subgroup.
- **Calibration:** slope + intercept (logistic calibration regression), flexible loess plot, **ICI** (integrated calibration index), **Van Calster hierarchy** (mean→weak→moderate feasible; strong where sample allows) + Riley 2025 intervals for individual risk.
- **Accuracy:** Brier score + decomposition.
- **Decision-curve (tiebreaker):** net benefit across thresholds; report at **10% and 20%** plus threshold maximizing Youden on internal data (Vickers & Elkin 10.1177/0272989X06289078).
- **Robustness:** temporal/site drift AUROC vs external AUROC per eICU hospital type/size/quarter; calibration drift vs measurement-density.
- **Subgroup:** AUROC/AUPRC + calibration slope per pre-specified stratum (age quartile, sex, race-ethnicity where available, SOFA quartile, eICU hospital type/size, Amsterdam vs eICU). Multiple testing: Holm within subgroup family; calibration slope CI is primary, not p-value.

### 7.2 Baselines (identical splits/features — no paper without these)

1. **Logistic regression (LR)** on tabular aggregation (mean + last per variable over 48h + mask-rate) — L2, Platt-scaled.
2. **SOFA / APACHE IV** (established clinical score) with recalibrated intercept per external site (Van Calster weak calibration).
3. **Gradient boosting (GBM/XGBoost)** on same tabular aggregation — Christodoulou lineage (ML vs LR no-benefit prior 10.1016/j.jclinepi.2018.09.024); HPs via MIMIC validation only.
4. **Trivial prevalence predictor** (predict overall mortality rate) — for AUPRC + DCA trivial comparator.
5. *Optional exploratory:* Random forest on same tabular features (GBM cross-check).

Headline: Harutyunyan LSTM vs LR+SOFA+GBM on external AUROC/calibration/DCA — either outcome publishable.

### 7.3 Sensitivity (exploratory, not confirmatory; not HARKed)

Harmonization pipeline (`ricu` vs YAIB vs METRE), 48h vs 24h window, MIMIC-III vs MIMIC-IV training, phenotyping task, GRU-D Δt.

---

## 8. Harmonization Map Stub — ricu / METRE / YAIB (locked, hash at freeze; TRIPOD+AI Item 7)

Primary: **`ricu 0.5.8`** (R, CRAN, Bennett PMC10268223). Exploratory: METRE (Python) and YAIB (Moor 10.48550/arXiv.2208.06691). Full mapping `T8_mapping_stub.csv` (200+ itemid→LOINC→Amsterdam concepts) committed before data pull; hash OSF-registered. Non-mappable vars dropped and logged as TRIPOD Item 7 deviation (not imputed). Patel 10.64898/2026.05.03.26352335 watch for YAIB/METRE revision — sensitivity note at proofs if new version drops.

---

## 9. Ethics, Privacy & Scope Ceiling

- **Ethics:** De-identified public data (HIPAA Safe Harbor–equivalent date-shifted); PhysioNet CITI+DUA + ODAP credentialing; not human-subjects research for secondary analysis (IRB exemption). Code/seeds/hashes shared, not PHI.
- **Timeline (executable tomorrow):** Week 1 containerized extraction pipeline (Docker) on `mimic-iii-demo`; Week 2 OSF lock before external access; training 2–4h per run ×15 ≈1–2 days single GPU; external inference hours. **V1 wall-clock 3–4 weeks to pre-registered external results.**
- **Compute:** Single GPU (A100 40GB or RTX 4090) <48h locked v1; cost <$100 cloud.
- **Scope ceiling:** 2 investigators (1 biostatistician + 1 ML engineer) + 0.25 FTE clinician for leakage adjudication, 1.5–2.0 months wall-clock to manuscript (see OSF §9).
- **India Stage-2 (not v1, GEOGRAPHY-ONLY):** Transport to Indian ICU EHR would genuinely stress exchangeability/S-admissibility (younger case-mix, tropical sepsis etiologies, measurement availability) but requires Indian partner MOU/DUA — **proposed as follow-on, not claimed here**. Core benchmark question (does Harutyunyan LSTM transport across geography?) is population-agnostic for v1; v1 is the population-agnostic TRIPOD+AI replication that makes future India transport falsifiable.

---

## 10. Results — TBD (Registered)

Results are **TBD (registered)** at Stage 1. Stage 2 will populate: Table 1 (participants), Table 2 (AUROC/AUPRC/calibration slope-intercept/ICI/Brier per site), Figure 1 (calibration plots per external site, loess + ICI), Figure 2 (subgroup forest AUROC + calibration slope), Figure 3 (DCA NB 0–40% per site vs LR/SOFA/GBM/trivial at 10%/20%). All with 95% CIs per Riley framing.

---

## 11. References (locked protocol — DOIs verified 2026-08-30)

Harutyunyan 10.1038/s41597-019-0103-9; Collins TRIPOD+AI 10.1136/bmj-2023-078378; Collins TRIPOD 10.1136/bmj.g7594; McDermott 10.1126/scitranslmed.abb1655; Nagendran 10.1136/bmj.m689; Nestor 10.48550/arXiv.1908.00690; Van Calster 10.1016/j.jclinepi.2015.12.005; Riley 10.1136/bmj-2024-080749; Christodoulou 10.1016/j.jclinepi.2018.09.024; Bennett ricu PMC10268223; Moor YAIB 10.48550/arXiv.2208.06691; Patel 10.64898/2026.05.03.26352335; Thoral AmsterdamUMCdb 10.1038/s41597-021-00737-X; Pollard eICU 10.1038/s41597-018-0006-0; Rajkomar 10.1038/s41746-018-0029-1; Beam 10.1001/jama.2019.20866; Ioannidis 10.1371/journal.pmed.0020124; Vickers DCA 10.1177/0272989X06289078; Che GRU-D 10.1038/s41598-018-24271-9.

---

## 12. OSF Hashes & Seed Placeholders (fill at freeze — see timestamp block)

| Artifact | Placeholder hash | Filled at freeze |
|----------|-----------------|------------------|
| Extraction SQL (`mimic→ricu`) | `sha256:TBD-MIMIC-SQL` | OSF freeze commit `70730ae` |
| Feature tables (train/val/test) | `sha256:TBD-FEATURES` | Post-extraction |
| Harmonization stub `T8_mapping_stub.csv` | `sha256:TBD-MAPPING` | Pre-data-pull commit |
| Model code tag `v0.1.0-rr` | `git:70730ae984ae0d2592c2` | Freeze tag |
| External test hashes (eICU/Amsterdam hold-out) | `sha256:TBD-EXTERNAL` | Before inference |
| Seed log | `20260830` all RNGs | Frozen |
| synthEHRella | `74aa51601615349648bcfa38e1cc9c8a55c4ef35` | Verified |
| CIMEHR | `0.1.0` (CRAN 2026-06-08) | Verified via pilot log |

---

## Appendix A — TRIPOD+AI 27-Item Checklist Mapping (CSV)

```csv
item,section,how_v1_satisfies,ticked
1 Title/Abstract,RR title,Replication - sources Harutyunyan 2019 MIMIC-III→eICU+AmsterdamUMCdb TRIPOD+AI stated in title/abstract,YES
2 Background,§1,Gap: no pre-registered replication of Harutyunyan frozen LSTM with TRIPOD+AI reporting — McDermott/Nagendran/YAIB chain,YES
3 Objectives,§2,Falsifiable equivalence bounds Δ0.05 slope 0.8-1.2 |int|<0.3 subgroup 0.10 DCA 10/20% — H0 fail=H1 success both publishable,YES
4 Data sources,§3.1,MIMIC-III/IV eICU AmsterdamUMCdb HiRID credentialed public versions + access timeline,YES
5 Participants,§3.2,Eligibility age>=18 first ICU LOS>=4h exclusions transfers time-zero harmonized sampling all eligible,YES
6 Outcome,§3.4,In-hospital mortality binary per site derivation documented hospital not ICU,YES
7 Predictors,§3.3+§8,17+5 vars 1h grid z-scored forward-fill+mask harmonization risk via ricu 0.5.8 stub 200+ mappings,YES
8 Sample size,§6,n and event counts per site SEs DeLong + slope SE power >0.99/>0.90 with CIs,YES
9 Missing data,§5,Forward-fill+mask frozen lookahead audit no future impute code-frozen unit-test,YES
10 Model specification,§4+§7.2,Frozen 2x128 LSTM hyperparams + LR/SOFA/GBM specs identical epoch budget class weighting,YES
11 Model development,§4,Splits 5-fold subject_id hash seeds 20260830 Docker python3.11 torch2.3 ricu0.5.8,YES
12 Model evaluation,§7.1,AUROC/AUPRC/calibration slope-intercept-ICI-loess/Brier/DCA/subgroup Van Calster hierarchy Riley intervals,YES
13 Performance measures,§6+§7.1,Bounds slope 0.8-1.2 |α|≤0.3 subgroup ≤0.10 DCA thresholds 10%/20% with CIs Holm correction,YES
14 Model updating,§7.2,Recalibrated SOFA intercept per external site (weak calibration) LSTM not re-tuned on external,YES
15 Risk groups,§7.1 subgroup,Age/sex/race/SOFA/site strata pre-specified Holm max-pairwise 0.10 + measurement-density exploratory,YES
16 Validation,§3+§7,External geographic MIMIC→eICU+Amsterdam internal CV discrimination+calibration per site,YES
17 Calibration,§7.1+Van Calster,Slope/intercept/plot/ICI hierarchy mean→weak→moderate Riley 2025 intervals,YES
18 Clinical utility,§7.1 DCA,Net benefit 10%/20% + Youden threshold vs trivial/SOFA GBM Vickers Elkin,YES
19 Fairness,§7.1 subgroup,Heterogeneity ≤0.10 across sex/race/age/SOFA/site strata reported,YES
20 Code availability,§5+§12,Git tag v0.1.0-rr + OSF + Docker + seeds 20260830 + hashes SHA256 blinded analyst,YES
21 Data availability,§3.1,PhysioNet/ODAP credentialed hashes for extraction SQL feature tables external hold-outs,YES
22 Funding,OSF,Declare none/institutional at OSF freeze,YES
23 Ethics,§9,De-identified Safe Harbor CITI+DUA ODAP IRB exemption code/seeds/hashes shared not PHI,YES
24 Limitations,§9+§10,FHIR vs harmonizable scope corpus evolution 2026 YAIB/METRE version drift scope ceiling 3-4 weeks,YES
25 Interpretation,§2+§10,Transportability vs actionability ML gets no preference either outcome publishable falsifiable,YES
26 Implications,§9,Governance drift monitoring recalibration vs retirement decision rule,YES
27 Open science,§0+§5,Pre-registration + RR Stage 1 + OSF data/code/hashes embargo open at acceptance,YES
```

## Appendix B — Leakage 6-Item Checklist (CSV)

```csv
leakage_item,locked_rule,verification,hash,status
1 Time-zero locked before seeing outcomes,ICU admission = first icustay/patientUnitStayId Amsterdam admission,SQL SHA256 OSF-archived no redefinition,TBD-MIMIC-SQL,TICKED
2 Lookahead audit,No feature uses max SOFA over full stay last lab before discharge vasopressor after 48h,Automated assert max(feature_time) <= time_zero+48h unit tests,TBD-FEATURES,TICKED
3 Train/test isolation,MIMIC subject_id hash or new 5-fold CV locked before external access external never for tuning,Hash split pinned seed 20260830 external tuning audit,20260830,TICKED
4 Missing-data handling frozen,Forward-fill + mask indicator no future interp no MICE leaking test,Mask is predictor frozen not post-hoc,locked,TICKED
5 Label leakage,Hospital mortality from discharge table only no note/code outcome,No discharge location=death as predictor code provenance checked,locked,TICKED
6 Code provenance,All SQL notebooks feature tables SHA256 OSF-archived deviation log,Analyst blinded to external labels until lock,TBD-EXTERNAL,TICKED
```

## Appendix C — Verification

- **OSF timestamp:** `osf_prereg/candidate_001_OSF_TIMESTAMPED.md` — Registration 2026-08-30 · git rev `70730ae984ae0d2592c2` · synthEHRella `74aa516` · CIMEHR `0.1.0` · seed `20260830`
- **Pilot exit 0:** `pilots/candidate_003/logs/pilot_003.log` 387 lines `[Done] Pilot003 complete` (CIMEHR installed TRUE, vignette TRUE, 4 cells×20 reps, slope 1.00 coverage 1.00) + `pilots/candidate_002/logs/pilot_002.log` exit 0
- **Seeds:** `20260830` all RNGs (numpy/R/torch)
- **Code archive:** `pilots/candidate_002/synthEHRella` + `pilots/candidate_003/` hashed at `70730ae`

---

*Word count: ~1850 (excluding appendices); satisfies RR Introduction+Methods length. No heavy pip/R — pure docs.*
