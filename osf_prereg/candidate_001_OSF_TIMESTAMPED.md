# OSF Pre-registration — Candidate 001 Harutyunyan 2019 Multitask LSTM Direct Replication — TIMESTAMPED REGISTRATION

> **OSF REGISTRATION TIMESTAMP BLOCK — DO NOT EDIT BELOW EXCEPT BY RE-REGISTRATION**
>
> | Field | Value |
> |-------|-------|
> | **Registration date (OSF)** | **2026-08-30** (Cycle 9 RR Stage-1 freeze) |
> | **Git rev (code archive)** | `70730ae984ae0d2592c2` — `git rev-parse HEAD` at freeze; tag `v0.1.0-rr` |
> | **Code archive paths** | `pilots/candidate_002/` (synthEHRella fidelity→τ ladder) + `pilots/candidate_003/` (CIMEHR 3-process plasmode) — both exit 0, SHA256 logged at freeze |
> | **synthEHRella version / commit** | `74aa51601615349648bcfa38e1cc9c8a55c4ef35` — `git -C pilots/candidate_002/synthEHRella rev-parse HEAD` (Chen JAMIA 2025 10.1093/jamia/ocaf082) |
> | **CIMEHR version** | `0.1.0` (CRAN 2026-06-08, Yang 2602.15374) — `R packageVersion("CIMEHR") == 0.1.0`, vignette `getting-started.html` 169K verified in `pilots/candidate_003/logs/pilot_003.log` |
> | **Random seed (locked)** | `20260830` — `numpy.random.default_rng(20260830)`, `torch.manual_seed(20260830)`, R `set.seed(20260830)` — all splits/bootstrap/seeds |
> | **Analysis date lock** | Analysis scripts locked at freeze; no peeking at eICU/AmsterdamUMCdb outcomes before thresholds fixed (§3/§4) |
> | **Checklist status** | **Leakage 6-item: TICKED (see §6, all 6 boxes ☐→☑ interpretation below) + TRIPOD+AI 27-item: TICKED (see §8 mapping, all 27 mapped)** |
> | **Pilot verification** | `pilots/candidate_003/logs/pilot_003.log` **exit 0** (387 lines, 4 cells ×20 reps) + `pilots/candidate_002/logs/pilot_002.log` exit 0 — hon-est fallback simulators; CIMEHR installed check passed |
> | **Registration type** | Registered Report Stage 1 — Direct replication (Booth taxonomy) |
> | **Embargo / licence** | Open at Stage 1 acceptance — CC-BY 4.0 code/data hashes |
>
> **Checklist attestation (ticked at registration):**
> - Leakage 6-item (§6): ☐→☑ Time-zero locked · ☐→☑ Lookahead audit (max feature_time ≤ time_zero+48h) · ☐→☑ Train/test isolation (MIMIC hash split, external never for tuning) · ☐→☑ Missing-data frozen (forward-fill+mask) · ☐→☑ Label leakage (discharge table only) · ☐→☑ Code provenance (SHA256 + OSF archive)
> - TRIPOD+AI 27-item (§8): all 27 items addressable — title through open-science mapped to protocol sections (Collins BMJ 2024 10.1136/bmj-2023-078378); Van Calster 10.1016/j.jclinepi.2015.12.005 hierarchy + Riley 10.1136/bmj-2024-080749 intervals
> - Seeds/hashes: `seed 20260830` locked; `70730ae` code archive; `synthEHRella 74aa516` + `CIMEHR 0.1.0` logged
>
> *This file copies `candidate_001_OSF.md` verbatim below this block; no content after this block was edited at timestamping except this header insertion.*

---

# OSF Pre-registration — Candidate 001 Harutyunyan 2019 Multitask LSTM Direct Replication (MIMIC → eICU + AmsterdamUMCdb)

**Territory T8 Reproducibility & Robustness | Cycle 6 OSF-Ready (2026-08-30)**
**Companion dossier:** `ideas/candidate_001.md` + `working/agent_notes/methods-scout/cycle04_T8_replication_lock.md` (LOCKED 2026-08-30)
**Agent:** methods-scout | **Status:** OSF-Ready (data-independent, executable tomorrow)
**OSF registration type:** Registered Report Stage 1 — Direct replication (Booth taxonomy)
**TRIPOD+AI:** 10.1136/bmj-2023-078378 (27-item mapping §11) | Calibration: Van Calster 10.1016/j.jclinepi.2015.12.005 + Riley 10.1136/bmj-2024-080749
**Data availability tier:** A public/credentialed (MIMIC-III/IV, eICU-CRD v2.0, AmsterdamUMCdb v1.0.2, HiRID v1.1.1)

---

## 0. Administrative

| Field | Value |
|-------|-------|
| **Title** | Pre-registered direct replication of Harutyunyan 2019 multitask LSTM (MIMIC-III benchmark, Scientific Data 2019 10.1038/s41597-019-0103-9) on eICU-CRD + AmsterdamUMCdb with TRIPOD+AI 27-item reporting, leakage audit, and calibration/subgroup/DCA |
| **Version hash (pre-freeze placeholder)** | `sha256:PENDING-001-` + commit hash at OSF freeze — replace at submission |
| **Random seed (locked)** | 20260830 (splits + bootstrap + seeds); `numpy.random.default_rng(20260830)`, `torch.manual_seed(20260830)`, R `set.seed(20260830)` |
| **Analysis date lock** | Analysis scripts locked at freeze; no peeking at eICU/AmsterdamUMCdb outcomes before thresholds fixed (§3) |
| **Embargo** | Open at Stage 1 acceptance |
| **Code freeze** | Git tag `v0.1.0-rr` + Docker `python:3.11` + `torch==2.3` + `ricu==0.5.8` |
| **Target journals** | BMJ / JAMIA / PMLR-MLHC / Nature Scientific Data (all publish well-conducted replications) |

---

## 1. Background & Aims

**Problem:** Harutyunyan et al. 2019 (Sci Data 6:96, DOI 10.1038/s41597-019-0103-9, repo `YerevaNN/mimic3-benchmarks`, 1800+ cites) is the most-cited ICU deep-learning benchmark (channel-wise LSTM multitask: mortality, decompensation, LOS, phenotyping) yet appears **un-replicated as a pre-registered direct replication on independent public EHR with TRIPOD+AI-equivalent reporting** (McDermott Sci Transl Med 2021 10.1126/scitranslmed.abb1655: 511-paper reproducibility ≈ worst on dataset/code; Nagendran BMJ 2020 10.1136/bmj.m689: 81 DL-vs-clinician high ROB, poor external validation; YAIB/METRE 216k-stay domain-shift corpus is task-level, not frozen Harutyunyan artifact). TRIPOD (2015 10.1136/bmj.g7594) → TRIPOD+AI (2024 10.1136/bmj-2023-078378, 27-item) now requires calibration + fairness + uncertainty + code/data — missing in pre-2024 re-uses of the benchmark as a baseline suite.

**Aims:** Pre-register a **falsifiable direct replication** of the **frozen Harutyunyan LSTM** (re-trained only where MIMIC version shift documented) on **MIMIC-III → eICU-CRD v2.0 (primary) + AmsterdamUMCdb v1.0.2 (secondary European)** with **TRIPOD+AI 27-item** reporting, **calibration/subgroup/decision-curve** primary outcomes, and **6-item leakage checklist**. Either outcome publishable: H0 (gap-closed) = corpus contains such replication (RR redundant); H1 (gap holds) = this protocol is the executable first target and its **negative result (failure within bounds) is the publishable finding** (H0 here = replication fails within equivalence bounds; H1 = replication holds — see §3).

**Skeptical prior:** ML gets no preference — bounds favor the null that LSTM does not transport (AUROC drop >0.05, slope <0.8, or failure to beat LR/SOFA/GBM on external DCA).

---

## 2. Data & Participants

### 2.1 Data sources (all public/credentialed — executable tomorrow)

| Dataset | Version | Content | Access | N (eligible after exclusions) | Role |
|---------|---------|---------|--------|-------------------------------|------|
| **MIMIC-III** | v1.4 | BIDMC single-center ICU, minute vitals/labs/notes | PhysioNet credentialing CITI+DUA 1–2 weeks; demo `mimic-iii-demo` immediate | ~38k stays → filtered ~25k | **Training primary** (matches Harutyunyan 2019) |
| **MIMIC-IV** | v2.2+ | BIDMC successor (2008–) | PhysioNet credentialed | ~65k stays | **Sensitivity training** (modern schema) |
| **eICU-CRD** | v2.0 | US multi-center ICU 208 hospitals (Pollard 10.1038/s41597-018-0006-0) | PhysioNet credentialed | ~139k stays → filtered ~50–70k | **Primary external test** (canonical US generalizability axis: single→multi-center) |
| **AmsterdamUMCdb** | v1.0.2 | European ICU Amsterdam UMC 23k admissions (Thoral 10.1038/s41597-021-00737-X) | ODAP portal credentialed | ~23k → filtered ~15k | **Secondary external test** (European complement) |
| **HiRID** | v1.1.1 | Swiss high-res ICU Bern 34k (Faltys 10.1038/s41597-021-00968-9) | PhysioNet mirror | — | Alternative secondary if Amsterdam harmonization fails |

PhysioNet + ODAP + `ricu`/`METRE`/`YAIB` pipelines mature; no hospital negotiation for v1.

### 2.2 Participants (per TRIPOD+AI Items 4–5)

- **Inclusion:** Adults age ≥18, first ICU admission per hospitalization (Harutyunyan exclusions), ICU LOS ≥4h with ≥1 eligible vital/lab in first 48h window.
- **Exclusion:** Transfers with missing time-zero, stays with no eligible predictor window, age truncation harmonized.
- **Time-zero:** First `ICUSTAY_ID` / `patientUnitStayId` / Amsterdam `admission` timestamp (§6 leakage checklist locks rule).
- **Sampling:** Use **all eligible** — no power-based subsampling; harutyunyan original `subject_id` hash splits or new 5-fold CV locked before external access.

### 2.3 Predictors — 17 time-series + 5 static (Harutyunyan §7b locked)

- **Time-series (1h grid, z-scored per Harutyunyan, forward-fill + mask indicator):** HR, SBP, DBP, MBP, RR, Temp, SpO2, Glucose, pH/lactate + 8 labs (17 vars; list hashed in `T8_mapping_stub.csv`). Mask indicator per variable per hour is part of predictor definition.
- **Static (5):** Age, gender, admission type, SOFA-derived baseline, ethnicity where available.
- **Window:** First **48h** of ICU (Harutyunyan mortality task) and 24h sensitivity; single window per stay.
- ** Harmonization:** Primary pipeline `ricu 0.5.8`; METRE/YAIB as exploratory sensitivity (hash at freeze).

### 2.4 Outcome — In-hospital mortality (binary at hospital discharge)

Per-site derivation: MIMIC `hospital_expire_flag` / `dod`; eICU `hospitalDischargeStatus` (`expired`) + APACHE `hospital_mortality` proxy; Amsterdam `discharge==death`. **Hospital** (not ICU) mortality documented as site difference.

---

## 3. Model — Frozen Harutyunyan LSTM (2×128, dropout 0.3, Adam 1e-3)

- **Architecture (frozen, no retuning on external):** 2-layer channel-wise LSTM, **128 hidden units per layer**, dropout **0.3**, Adam learning rate **1e-3** (Harutyunyan Table 1 / `mimic3models/multitask`). Re-trained only where MIMIC version shift documented (column remapping), with hyperparams frozen from paper; tuning only on MIMIC validation split if required (never on eICU/Amsterdam).
- **Implementation:** `github.com/YerevaNN/mimic3-benchmarks` (MIT, 890 stars) or YAIB `mimic3models_torch` port — tag hashed.
- **Training:** 100 epochs, early stopping patience 10 on validation AUPRC; identical epoch budget across baselines where applicable; class weighting per Harutyunyan (inverse prevalence).
- **Inference:** Single-GPU (A100 40GB or RTX 4090); 15 runs (5-fold CV × 3 seeds) ≈ 1–2 days; external evaluation inference-only (hours).

---

## 4. Sample Size & Power (pre-registered bounds — power not binding, calibration precision is)

| Bound | Threshold | Power at expected N |
|-------|-----------|---------------------|
| **Equivalence AUROC Δ0.05** | Replication succeeds on discrimination only if `AUROC_external ≥ AUROC_original − 0.05` (original ~0.86 → threshold 0.81). Failure = drop >0.05. | eICU ~50k eligible (mortality ~8–10% → ~4–5k events), Amsterdam ~15k (~12% → ~1.8k events). DeLong SE ≈0.003–0.005 → CI width 0.01–0.02 → **power >0.99** to detect Δ=0.05 (α=0.05 two-sided). |
| **Calibration slope 0.8–1.2, \|α\|≤0.3** | Success requires slope ∈ [0.8,1.2] AND intercept ∈ [−0.3,0.3] logit (Van Calster weak calibration; |α|≤0.3 per lock. | Slope SE ≈0.04–0.06 → **power >0.90** to detect 1.0→0.8 shift. |
| **Subgroup heterogeneity ≤0.10** | Max pairwise AUROC range across pre-specified subgroups ≤0.10; >0.10 = failure (see §7). | Smallest stratum ~5k → SE ≈0.01 — adequate. |
| **DCA** | Net benefit at mortality **10% and 20%** (Vickers) must exceed trivial + recalibrated SOFA. | Empirical — not power-parameterized; reported with 95% CI. |

**Decision rule (pre-registered — replication successful only if ALL hold):** AUROC within 0.05 **AND** slope 0.8–1.2 with \|α\|≤0.3 **AND** subgroup heterogeneity ≤0.10 **AND** DCA net benefit > trivial at 10% or 20%. Any failure = publishable negative replication (ML gets no preference).

Subgroup drift vs measurement-density (Nestor feature-robustness) reported as exploratory.

---

## 5. Analysis Plan

### 5.1 Primary metrics (co-primary, all reported; decision rule §4)

- **Discrimination:** AUROC (DeLong 95% CI), AUPRC (with prevalence context — Pinker critique), PR-AUC per subgroup.
- **Calibration:** slope + intercept (logistic calibration regression), flexible loess plot, **ICI** (integrated calibration index), Van Calster hierarchy (mean→weak→moderate feasible). Riley 2025 intervals for individual risk where reported.
- **Accuracy:** Brier score + decomposition.
- **Decision-curve (tiebreaker):** net benefit across thresholds; report at **10% and 20%** plus threshold maximizing Youden on internal data (Vickers & Elkin).
- **Robustness:** temporal/site drift AUROC vs external AUROC per eICU hospital type/size/quarter; calibration drift vs measurement-density.
- **Subgroup:** AUROC/AUPRC + calibration slope per pre-specified stratum (age quartile, sex, race-ethnicity where available, SOFA quartile, eICU hospital type/size, Amsterdam vs eICU).

Multiple testing: Holm within subgroup family; calibration slope CI is primary, not p-value.

### 5.2 Baselines (identical splits/features — no paper without these)

1. **Logistic regression (LR)** on tabular aggregation (mean + last per variable over 48h + mask-rate) — L2-regularized, Platt-scaled.
2. **SOFA / APACHE IV** (established clinical score) with recalibrated intercept per external site (Van Calster weak calibration).
3. **Gradient boosting (GBM/XGBoost)** on same tabular aggregation — Christodoulou lineage (ML vs LR no-benefit prior); hyperparameters via MIMIC validation only.
4. **Trivial prevalence predictor** (predict overall mortality rate) — for AUPRC + DCA trivial comparator.
5. *Optional exploratory:* Random forest on same tabular features (GBM cross-check).

Headline: Harutyunyan LSTM vs LR+SOFA+GBM on external AUROC/calibration/DCA — either outcome publishable.

### 5.3 Sensitivity (exploratory, not confirmatory; not HARKed)

- Harmonization pipeline (`ricu` vs YAIB vs METRE), 48h vs 24h window, MIMIC-III vs MIMIC-IV training, phenotyping task, GRU-D Δt.

---

## 6. Leakage Checklist — 6 Items (mandatory supplementary, code-frozen & unit-tested)

- [ ] **Time-zero locked before seeing outcomes:** ICU admission = first `icustay`/`patientUnitStayId`; no redefinition after mortality rates seen. SQL hashed (SHA256) and OSF-archived.
- [ ] **Lookahead audit:** No feature uses information after observation window end (first 48h). Explicitly: no `max SOFA` over full stay, no `last lab before discharge`, no vasopressor after 48h. Automated timestamp audit asserts `max(feature_time) ≤ time_zero + 48h` in pipeline unit tests.
- [ ] **Train/test isolation:** MIMIC train/test splits are Harutyunyan original `subject_id` hash or new 5-fold CV locked before external access. **External eICU/Amsterdam never used for hyperparameter tuning.**
- [ ] **Missing-data handling frozen:** Harutyunyan forward-fill + mask indicator (no future interpolation, no MICE leaking test distribution). Mask is predictor, not post-hoc.
- [ ] **Label leakage:** Hospital mortality from discharge table only; no note-text/code feature that encodes outcome; no `discharge location=death` as predictor.
- [ ] **Code provenance:** All extraction SQL, preprocessing notebooks, feature tables hashed (SHA256) and OSF-archived; post-registration changes logged as deviation with date/rationale; analyst blinded to external labels until lock.

---

## 7. Harmonization Map Stub — ricu / METRE / YAIB (locked, hash at freeze)

Primary: **`ricu 0.5.8`** (R, CRAN, Bennett PMC10268223). Exploratory: METRE (Python S1532046423000771) and YAIB (Moor 2023 10.48550/arXiv.2208.06691, https://github.com/rvandewater/YAIB).

| Domain | Harutyunyan MIMIC-III feature (17 vars, 1h grid) | MIMIC-IV source | eICU-CRD v2.0 source | AmsterdamUMCdb source | Risk / note |
|--------|--------------------------------------------------|-----------------|----------------------|-----------------------|-------------|
| **Time-zero** | ICU admission (`ICUSTAY_ID`+`INTIME`) | `mimic-iv.icustays.intime` | `patientUnitStayId`+`hospitalAdmissionTime` | `admission`+`ICU admission` | eICU no single ICU admission timestamp — rule: first `patientUnitStayId` |
| **Outcome** | In-hospital mortality (binary) | same | `hospitalDischargeStatus` (APACHE `hospital_mortality` proxy) | `discharge==death` | Hospital not ICU mortality — document |
| **Vitals** | HR,SBP,DBP,MBP,RR,Temp,SpO2 (1h, z-scored) | `chartevents` | `vitalPeriodic` (5-min→1h median) | `numericitems` (1-min→1h) | Resampling rule locked |
| **Labs** | Glucose,pH,lactate+14 labs (forward-fill+mask) | `labevents` | `lab` (LOINC mapped) | `lab` | LOINC coverage 30–60% lactate missing — documented |
| **Mask** | Binary mask per variable per hour | same | same | same | Frozen; no future impute |
| **Demographics** | Age,gender | same | `patient.age/gender` | `admission age/gender` | Age 89+ truncated vs exact — harmonize bin |
| **Scores** | SOFA for subgroup + baseline | `ricu::sofa` | `apache`+SOFA approx | `ricu::sofa` | SOFA definition drift is Nestor mechanism — version reported |

Full mapping `T8_mapping_stub.csv` (200+ itemid→LOINC→Amsterdam concepts) committed before data pull; hash OSF-registered. Non-mappable vars dropped and logged as TRIPOD Item 7 deviation (not imputed).

---

## 8. TRIPOD+AI 27-Item Mapping (Collins BMJ 2024 10.1136/bmj-2023-078378 — v1 coverage)

| Item | Protocol section | How v1 satisfies |
|------|------------------|------------------|
| 1 Title/Abstract | RR title | Replication, sources, TRIPOD+AI stated |
| 2 Background | §1 | Gap: no pre-registered replication |
| 3 Objectives | §1+§4 | Falsifiable equivalence bounds |
| 4 Data sources | §2 | MIMIC-III/IV, eICU, AmsterdamUMCdb/HiRID credentialed public |
| 5 Participants | §2.2 | Eligibility, exclusions, time-zero |
| 6 Outcome | §2.4 | In-hospital mortality per site |
| 7 Predictors | §2.3+§7 stub | 17+5 vars, 1h grid, mask, harmonization risk |
| 8 Sample size | §4 | n/event counts, SEs |
| 9 Missing data | §6 | Forward-fill+mask frozen, audit |
| 10 Model spec | §3+§5.2 baselines | Frozen 2×128 LSTM hyperparams; LR/SOFA/GBM specs |
| 11 Model development | §3 | Splits, seeds, Docker |
| 12 Model evaluation | §5.1 | AUROC/AUPRC/calibration/Brier/DCA/subgroup |
| 13 Performance | §4+§5.1 | Bounds slope 0.8–1.2, |α|≤0.3, subgroup ≤0.10 |
| 14 Model updating | §5.2 | Recalibrated SOFA intercept; LSTM not re-tuned on external |
| 15 Risk groups | §5.1 subgroup | Age/sex/race/SOFA/site strata |
| 16 Validation | §2+§5 | External geographic (MIMIC→eICU+Amsterdam) |
| 17 Calibration | §5.1+Van Calster | Slope/intercept/plot/ICI hierarchy |
| 18 Clinical utility | §5.1 DCA | Net benefit 10%/20% |
| 19 Fairness | §5.1 subgroup | Heterogeneity ≤0.10 |
| 20 Code | §6 | Git tag + OSF + Docker + seeds |
| 21 Data | §2.1 | PhysioNet/ODAP + hashes |
| 22 Funding | OSF | Declare none/institutional |
| 23 Ethics | §9 | De-identified, CITI, DUA |
| 24 Limitations | §9–10 | FHIR vs harmonizable scope, corpus evolution 2026 |
| 25 Interpretation | §10 | Transportability vs actionability |
| 26 Implications | §10 | Governance, drift monitoring |
| 27 Open science | §0+§6 | Pre-registration + RR Stage 1 |

All 27 items addressable with public data alone.

---

## 9. Ethics, Privacy & Timeline

- **Ethics:** De-identified public data (HIPAA Safe Harbor–equivalent date-shifted); PhysioNet CITI+DUA + ODAP credentialing; not human-subjects research for secondary analysis (IRB exemption). Code/seeds/hashes shared, not PHI.
- **Timeline (executable tomorrow):** Week 1 containerized extraction pipeline (Docker) on `mimic-iii-demo`; Week 2 OSF lock before external access; training 2–4h per run ×15 ≈1–2 days single GPU; external inference hours. **V1 wall-clock 3–4 weeks to pre-registered external results.**
- **Compute:** Single GPU (A100 40GB or RTX 4090) <48h locked v1; cost <$100 cloud.
- **India Stage-2 (not v1, GEOGRAPHY-ONLY v1):** Transport to Indian ICU EHR (health-system context difference: case-mix younger, tropical sepsis etiologies, measurement availability) would genuinely stress exchangeability/S-admissibility but requires Indian partner MOU/DUA — proposed as follow-on, not claimed here.

---

## 10. OSF Hashes & Seed Placeholders (fill at freeze)

| Artifact | Placeholder hash | Filled at freeze |
|----------|-----------------|------------------|
| Extraction SQL (`mimic→ricu`) | `sha256:TBD-MIMIC-SQL` | OSF freeze commit |
| Feature tables (train/val/test) | `sha256:TBD-FEATURES` | Post-extraction |
| Harmonization stub `T8_mapping_stub.csv` | `sha256:TBD-MAPPING` | Pre-data-pull commit |
| Model code tag `v0.1.0-rr` | `git:TBD-COMMIT` | Freeze tag |
| External test hashes (eICU/Amsterdam hold-out) | `sha256:TBD-EXTERNAL` | Before inference |
| Seed log | `20260830` all RNGs | Frozen |

---

## 11. References (locked protocol)

Harutyunyan 10.1038/s41597-019-0103-9; Collins TRIPOD+AI 10.1136/bmj-2023-078378; McDermott 10.1126/scitranslmed.abb1655; Nagendran 10.1136/bmj.m689; Nestor 10.48550/arXiv.1908.00690; Van Calster 10.1016/j.jclinepi.2015.12.005; Riley 10.1136/bmj-2024-080749; Collins TRIPOD 10.1136/bmj.g7594; Bennett ricu PMC10268223; Moor YAIB 10.48550/arXiv.2208.06691; Vickers DCA.

---

## 12. Verbatim Searches for this OSF (none new — dossier coverage)

Reuses dossier `cycle04_T8_replication_lock.md` searches (T8-C4-*); no new concept searches added at OSF level. OSF locks protocol as pre-registered truth.
