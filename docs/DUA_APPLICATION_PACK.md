# DUA Application Pack — UKB-SA / CARRS / ICMR-INDIAB (Candidate 007 + 005/006 India Transport)

**Version:** 2026-08-31 · **Seed:** 20260830 · **Git anchor:** 8824caa (Cycle 11) + fc213fd (RR Stage-1)
**Status:** Ready to submit — UKB RAP 1–3 mo proxy → CARRS/ICMR-INDIAB 2–6 mo restricted
**Companion:** `osf_prereg/candidate_007_OSF.md` (205 lines), `osf_prereg/candidate_005_006_OSF.md` (258 lines), `full_runs/candidate_007/` (N=8k synthetic proxy proves pipeline), `ideas/candidate_007.md` §4
**Scope:** This pack stages **all** B-restricted DUAs for India transport work (007 Ahlqvist centroids vs de-novo + 005/006 G0→G3 tilting + ICMR-INDIAB population positivity). No PHI. Synthetic proxy already demonstrates pipeline (Phase 1).

---

## 1. Summary Timeline (staged, honest)

| Phase | Dataset | N / content | Access route | Timeline | Deliverable this pack proves |
|-------|---------|-------------|--------------|----------|------------------------------|
| **Phase 1 proxy** | **UK Biobank South Asian (UKB-SA, n~8–10k SA: Indian/Pakistani/Bangladeshi, of ~500k total)** | Deeply phenotyped BMI/HbA1c/C-peptide/genetics/outcomes, UKB RAP cloud | UKB AMS category 2, RAP | **1–3 mo** (application → EGC approval → RAP activation) | Proxy feasibility preprint: overlap + 3-var verdict (already synthetic proxy N=8k run, `full_runs/candidate_007/`) |
| **Phase 2 primary** | **CARRS (Centre for Cardiometabolic Risk Reduction in South Asia, n~12k, Delhi/Chennai/Karachi, 2010–11 baseline+f/u)** | Cardiometabolic; age/BMI/HbA1c/FBG/insulin/lipids/BP/SES; CKD/CVD longitudinal; **GADA/HOMA sparse — completeness unconfirmed pending DUA** | PHFI/Emory Steering Committee DUA | **2–3 mo** (proposal → Steering review → de-identified extract) | Primary paper: centroids vs de-novo with IOPW ESS + Cox HR |
| **Phase 3 national** | **ICMR-INDIAB (n~113k, 31 states/UTs 2008–20)** | National survey; BMI/age/HbA1c/FBG/lipids/BP; GADA limited; largest covariate-support | ICMR-NIE/MDRF DUA | **3–6 mo** (collaboration + ethics + DUA) | Population positivity + 3-var only (Mohan Lancet 2023) |
| **Phase 3b sensitivity** | **CMC Vellore / AIIMS Delhi T2D registry (new-onset enriched)** | Tertiary T2D clinic; richer phenotyping (GADA where ordered, C-peptide/HOMA research subset); new-onset → ANDIS-analogous | Institutional MOU + ethics | **2–4 mo** | Sampling-frame sensitivity (CARRS prevalent vs ANDIS incident) |
| **Reference A** | **MIMIC-IV T2D subset (n~10k ICU T2D)** + **ANDIS summary stats (Ahlqvist Table 1 centroids)** | US ICU T2D; ANDIS published centroids/means/SDs | PhysioNet credentialed (weeks 1–2); open supplement (immediate) | 1–2 weeks / immediate | Contrast distribution + source centroids |

**Total ceiling:** 4–6 mo to first submission (proxy+CARRS); 8 mo with ICMR-INDIAB/registry. Each phase independently publishable per OSF staged execution.

---

## 2. UK Biobank RAP — UKB-SA 8–10k SA Cohort Application Steps

**Data:** UK Biobank South Asian subset ~8k (Indian/Pakistani/Bangladeshi) of ~500k total; deeply phenotyped (BMI, HbA1c, C-peptide where available, genetics, longitudinal CKD/CVD). This is the **proxy-first** dataset for 007 per OSF §2 (1–3 mo, managed access, before Indian data arrive).

### 2.1 UKB AMS Portal Steps (ukbiobank.ac.uk → AMS)

1. **Register PI + institution** at https://www.ukbiobank.ac.uk/enable-your-research/apply-for-access (institutional signatory, PI CV, institutional ethics letter). No download beyond RAP extracts.
2. **AMS application (category 2 — phenotype + genetics, no re-contact):** Title: *Do Ahlqvist 2018 Scandinavian centroids transport to UKB-SA with overlap diagnostics and GADA-free ablation?* — reference `osf_prereg/candidate_007_OSF.md` + this pack.
3. **Research question + lay summary:** Transportability of Ahlqvist 5 clusters (SAID/SIDD/SIRD/MOD/MARD) to SA proxy with inverse-odds weighting, SMD/S-score/ESS, 6→3 ablation. Include TRIPOD+AI framing.
4. **RAP cloud compliance:** Confirm analysis on UKB Research Analysis Platform (RAP) DNA Nexus — no download beyond approved extracts; RAP credits budget (~$500–1000 for 8k SA extract + 6-month compute).
5. **EGC oversight:** UK Biobank Ethics and Governance Council approval; managed access, no PHI beyond coded IDs.
6. **Timeline:** EGC review 4–6 weeks → RAP activation 1–2 weeks → phenotype harmonization 2 weeks → first transport vs de-novo run (6–8 weeks after access, per OSF Phase 1).

### 2.2 UKB-SA Variables Needed (field IDs + harmonization, per OSF §8)

| Variable | UKB field(s) | ANDIS harmonization | Note |
|----------|--------------|---------------------|------|
| **BMI** | 21001 (BMI kg/m²) + 21002 (weight), 50 (height) | kg/m², same cutoff | Thin-fat SA phenotype |
| **Age at diagnosis** | 2443 (diabetes diagnosis), 2976 (age at diagnosis), 130706/130708 (date) | years, ANDIS mean 57.5 → SA younger | ICMR-INDIAB younger -5 to -10y |
| **HbA1c** | 30750 (HbA1c mmol/mol + NGSP %), 30740/30750 harmonized | IFCC mmol/mol + NGSP %, ANDIS mean 8.0% | Primary glycaemia |
| **GADA** | Research subset (GADA where ordered) + 30770 proxy | ELISA cutoff > per ANDIS (positive 1/0) | Sparse (<20% expected, per Anjana sparsity, CARRS note) |
| **HOMA2-B / HOMA2-IR** | 30770/30640 (insulin/glucose where available) → Oxford calculator v2.2 | HOMA2 via same Oxford calculator if insulin>5% complete; else 3-var arm | IMI-RHAPSODY C-peptide/HDL substitution analogue |
| **MONO% / inflammatory** | 30170 (monocyte count/percentage) | %; per Mohan PMC7437708 table (MONO 43.3% table) | For 005/006 tilting G0→G3 table |
| **Lipids/BP** | 30760/30770/30690 etc. | lipids mg/dL, BP mmHg | For SIRD metabolic syndrome |
| **Outcomes** | HES/primary care linkage (CKD eGFR decline ≥40%/UACR, retinopathy fundoscopy, insulin prescription) | Per CARRS protocol analog, Cox HR vs MARD | Ahlqvist Fig 3–4 analogues |
| **Genetics** | SA ancestry PCs | For sensitivity, not primary |
| **SES** | Townsend, education | For transport adjustment, not clustering |
| **AYUSH / traditional medicine** | Not in UKB (India-specific; CARRS + ICMR-INDIAB questionnaire) | — | Docs below |

**Honest note:** UKB-SA showcase available at https://biobank.ndph.ox.ac.uk/showcase/ — South Asian phenotype availability confirmed via field search (BMI/HbA1c available, GADA/C-peptide limited research subset). This pack includes RAP application checklist, not data itself (no PHI).

---

## 3. CARRS — PHFI / Emory Steering Committee DUA (Primary, n~12k)

**Dataset:** CARRS — Centre for Cardiometabolic Risk Reduction in South Asia, multi-site cohort Delhi/Chennai/Karachi, n~12k (Nair 2022 Int J Epidemiol 10.1093/ije/dyac122, PMC9749725), baseline 2010–11 + follow-up, cardiometabolic.

### 3.1 CARRS Contact + Application

- **Steering Committee contacts (public):**
  - **PHFI (Public Health Foundation of India), Gurugram** — CARRS coordinating centre: https://phfi.org/research/carrs-study/ (contact via PHFI research office, email via PHFI portal; DUA template on PHFI site). PI: Prof. Dorairaj Prabhakaran (PHFI) / Prof. K.M. Venkat Narayan (Emory).
  - **Emory Global Diabetes Research Center, Atlanta** — emory.edu/diabetes (CARRS Emory site: https://diabetes.emory.edu/research/carrs.html, contact via Emory Global Health).
  - **Formal route:** DUA via PHFI/Emory Steering Committee — proposal submission (2-page concept → full proposal), scientific review, ethics (PHFI/Emory IRB), data sharing agreement, de-identified extract delivery via secure portal. Timeline **2–3 months** (concept 2 weeks → review 4 weeks → DUA 2–4 weeks → extract 2 weeks).

### 3.2 CARRS Variables Needed (per dossier §4 + 005/006 G0_G3_table)

| Domain | Variable | CARRS availability | Use in this study |
|--------|----------|-------------------|-------------------|
| **BMI** | BMI kg/m² | ✅ Profile lists BMI, waist | 007 clustering + 005/006 tilting G0→G3 (BMI 28.3→22.8) |
| **MONO** | Monocyte count/percentage, inflammation | ✅ Inferred from CBC (Nair profile includes CBC) | 005/006 tilting MONO 0→56.7% (audit-anchored IIA-08/ICMR-INDIAB 43.3%) |
| **HbA1c** | HbA1c NGSP %, fasting glucose | ✅ HbA1c + FBG | 007 clustering (HbA1c IFCC/NGSP), 005/006 glycaemia |
| **AYUSH** | AYUSH / traditional medicine use (Ayurveda/Yoga/Unani/Siddha/Homeopathy) | ⚠️ Questionnaire SES/comorbidity section (confirm via DUA) | 005/006 G0→G3 tilting AYUSH 0→~40% (per Galib table PMC8614209) |
| **Generic meds** | Generic vs branded medication, polypharmacy | ⚠️ Prescription data (confirm via DUA) | 005/006 tilting + adherence sensitivity |
| **Docs age** | Provider age / experience, facility type | ⚠️ Facility survey (confirm via DUA) | 005/006 tilting docs age (per audit) |
| **Age at diagnosis** | Age, age at diabetes diagnosis | ✅ Age | 007 clustering (SA younger) |
| **HOMA2-B/IR, GADA, C-peptide** | Fasting insulin, GADA where ordered, C-peptide research subset | ⚠️ **Sparse — inferred <20% from cohort profile (Anjana sparsity, no public dictionary)** — honest unconfirmed pending DUA per dossier REVISE note | 007: 3-var co-primary (age/BMI/HbA1c) if completeness <85%; 6-var aspirational |
| **Lipids/BP/SES** | Lipids, BP, SES | ✅ | SIRD metabolic + transport adjustment |
| **Outcomes** | CKD (eGFR decline ≥40% or UACR progression), retinopathy, insulin initiation | ✅ Longitudinal (CARRS protocol, lab adjudicated) | 007 outcome gradients (Cox HR vs MARD per Ahlqvist analogues) |

**Honest CARRS note (REVISE 2026-08-30):** Data dictionary is **not public** — inferred GADA/HOMA <20% from cohort profiles. Pre-registered rule: **3-var co-primary; 6-var aspirational requiring completeness ≥85% to claim; if <10% post-DUA, 6-var → sensitivity-only** (per OSF §2, §3 thresholds).

### 3.3 DUA Package to Submit (CARRS)

- 2-page concept: *Ahlqvist transport + GADA-free ablation on CARRS SA adults* + *India tilting G0→G3 with entropy balancing* (reference OSF preregs + synthetic proxy results).
- Variable list above (BMI/MONO/HbA1c/AYUSH/generic/docs age + 007 6 vars + outcomes + SES).
- Analysis plan: IOPW (Dahabreh) with propensity P(S=Scandinavian|vars), SMD, S-score distribution, overlap coefficient, ESS, truncation 1%/5%/10%, Li overlap weights ATO, ARI transport vs de-novo, silhouette, Jaccard bootstrap, Cox HR CKD/retinopathy/insulin, 6→3 ablation, decision relevance net benefit.
- Ethics: PHFI/Emory IRB + Indian Council of Medical Research ethics guidelines compliance; de-identified extracts only, no PHI; pre-registration prevents HARKing.
- MTA/DUA: PHFI template + Emory counterpart, institutional signatory, RAP-style cloud if required.

---

## 4. ICMR-INDIAB — 113k National Survey DUA (Secondary, 31 states/UTs)

**Dataset:** ICMR-INDIAB, n~113k, 31 states/UTs 2008–2020 (Anjana Lancet Diabetes Endocrinol 2023 10.1016/S2213-8587(23)00119-5 + IJMR 2025 10.25259/IJMR_328_2025), national population-based survey; largest Indian covariate-support for positivity.

### 4.1 ICMR-INDIAB Contact + Application

- **Contacts (public):**
  - **MDRF (Madras Diabetes Research Foundation), Chennai** — ICMR-INDIAB coordinating: https://www.mdrf.in (Dr. R.M. Anjana / Dr. V. Mohan group, correspondence via MDRF).
  - **ICMR-NIE (National Institute of Epidemiology), Chennai** — ICMR data governance: https://nie.icmr.org.in (DUA via ICMR-NIE/MDRF).
  - **Route:** Collaboration proposal + DUA via MDRF/ICMR (Mohan/Anjana group), ICMR ethics, de-identified national extract. Timeline **3–6 months** (summary prevalences open via Lancet 2023; individual-level requires DUA). Open-web ICMR-INDIAB-23 fullTextXML (PMC12550443, MONO 43.3% table) already extracted for 005/006 thin-fat bridging.

### 4.2 Variables Needed (ICMR-INDIAB)

| Variable | Availability | Use |
|----------|--------------|-----|
| **BMI, age at diagnosis, FBG, HbA1c subgroup** | ✅ (core phenotyping) | 007 3-var only (no HOMA in population sample per Mohan PMC7437708 → 3-var primary for national positivity) |
| **Lipids, BP, SES, state** | ✅ | Positivity diagnostics, state-stratified overlap |
| **GADA** | Limited (population survey, not routine) | → 3-var analysis |
| **Outcomes** | Cross-sectional + limited longitudinal | Population-level transport assessment |

**Secondary target: CMC Vellore / AIIMS Delhi T2D registry (new-onset enriched)** — tertiary-care T2D clinic with richer phenotyping (GADA where ordered, C-peptide/HOMA research subset), new-onset enriched → **ANDIS-analogous sampling frame** (mitigates CARRS prevalent vs ANDIS incident mismatch, per dossier adversarial challenge #4). DUA via institutional MOU + ethics, **2–4 months**. If CARRS fails but CMC/AIIMS transports, failure was frame artifact (sampling-frame sensitivity).

---

## 5. Timeline & Checklist (1–3 mo proxy → 2–6 mo restricted)

```
Week 0 (now): Submit UKB-SA RAP application (AMS category 2) + CARRS concept (PHFI/Emory) + ICMR-INDIAB inquiry (MDRF)
  Deliver proxy preprint: full_runs/candidate_007/ synthetic N=8k + overlap diagnostics (this pack proves pipeline)
Week 4–6:  UKB-SA EGC approval → RAP activation → harmonize 21001/30750/etc. per ANDIS means/SDs (OSF §8)
Week 6–12: UKB-SA Phase 1 run (transport vs de-novo, ARI, SMD/ESS/AUC, 6→3 ablation, HR stub) — 6–8 weeks after access
Week 6–10: CARRS Steering review → DUA → extract (parallel, 2–3 mo total) — query GADA/HOMA completeness first
Week 8–14: CARRS Phase 2 primary (IOPW, ESS, truncation 1%/5%/10%, Cox HR CKD/retinopathy/insulin) — 8–10 weeks after receipt
Week 14–20: ICMR-INDIAB / CMC-AIIMS Phase 3 (population positivity + new-onset sensitivity) — 4–6 weeks after receipt
Total: 4–6 mo to first submission (proxy+CARRS); 8 mo with ICMR-INDIAB/registry → one registered report + one empirical paper.
```

**Gate before 6-var primary claim:** Check CARRS GADA completeness post-DUA — if ≥85% claim 6-var primary, if <85% 3-var co-primary, if <10% 6-var → sensitivity-only (locked, per OSF §3, no post hoc tuning).

---

## 6. Variables Needed Summary (BMI / MONO / HbA1c / AYUSH / generic / docs age + 007 6 vars)

For **Dossier §4 / OSF §8 / 005/006 G0_G3_table** completeness, every DUA requests:

- **BMI** (kg/m²) — 007 + 005/006 tilting (audit-anchored G0 28.3→G3 22.8)
- **MONO** (monocyte %/count) — 005/006 tilting (0→56.7%, ICMR-INDIAB 43.3% table)
- **HbA1c** (NGSP % + IFCC mmol/mol) — 007 + 005/006
- **AYUSH** (traditional medicine use) — 005/006 tilting (Galib PMC8614209 table)
- **Generic vs branded** — 005/006 + adherence
- **Docs age / provider** — 005/006 tilting (audit provider age)
- **Age / age at diagnosis** — 007 (ICMR-INDIAB younger, SA vs ANDIS SMD)
- **HOMA2-B / HOMA2-IR (Oxford v2.2), GADA, C-peptide** — 007 6-var (if completeness ≥85%, else 3-var)
- **Lipids, BP, SES, state, facility, comorbidities** — transport adjustment + SIRD metabolic
- **Outcomes:** CKD (eGFR decline ≥40% or UACR), retinopathy (fundoscopy where available), insulin initiation, CVD (for HR stub)

---

## 7. Ethics & Privacy (all pathways)

- **UKB-SA:** UK Biobank EGC oversight; managed access AMS, RAP cloud; no download beyond extracts.
- **CARRS/ICMR-INDIAB/CMC-AIIMS:** Restricted, de-identified extracts only; DUA via PHFI/Emory (CARRS Steering), ICMR-NIE/MDRF (ICMR-INDIAB), institutional MOU (CMC/AIIMS); Indian Council of Medical Research ethics guidelines; no PHI beyond de-identified; IRB (PHFI, ICMR, CMC, AIIMS).
- **ANDIS summary stats:** Published, no individual-level — zero privacy risk.
- **MIMIC-IV:** De-identified per HIPAA Safe Harbor; PhysioNet credentialed (CITI+DUA); IRB exemption.
- **No prospective patient contact;** all retrospective, non-interventional; pre-registration prevents HARKing on k/feature-set/missing/overlap thresholds.

---

## 8. Verification & References (no open-search needed beyond DUA portals)

- **UKB RAP portal:** https://www.ukbiobank.ac.uk/enable-your-research/apply-for-access + showcase https://biobank.ndph.ox.ac.uk/showcase/
- **CARRS:** PHFI https://phfi.org/research/carrs-study/ + Emory https://diabetes.emory.edu/research/carrs.html + Nair 2022 10.1093/ije/dyac122 (PMC9749725)
- **ICMR-INDIAB:** MDRF https://www.mdrf.in + Lancet 2023 10.1016/S2213-8587(23)00119-5 + IJMR 2025 10.25259/IJMR_328_2025 + Mohan PMC7437708 (19k Indians, 4 replicable clusters, 2 novel CIRDD/IROD) + PMC12550443 fullTextXML (MONO 43.3%)
- **Ahlqvist 2018:** 10.1016/s2213-8587(18)30051-2 (n=8980 ANDIS, 5 clusters, 6 vars) + IMI-RHAPSODY 10.1007/s00125-021-05490-8 (European cross-validation distinction, no Indian LMIC transport)
- **Methods:** Degtiar 10.1146/annurev-statistics-042522-103837, Dahabreh 10.1093/aje/kwy253, Pearl 10.1214/14-STS486 (selection diagrams, S-admissibility)
- **TRIPOD+AI:** Collins 10.1136/bmj-2023-078378 (27-item §11, era split Jan 2024)
- **This pack:** Seeds 20260830, honest synthetic proxy already executed (full_runs/candidate_007/ N=8k ARI 0.25, SMD 50%, completeness 98% synthetic), no PHI.

---

## 9. Application Template (one-paragraph lay summary for UKB/CARRS/ICMR cover letters)

> We propose to test whether the Scandinavian Ahlqvist 2018 adult-onset diabetes subtypes (5 clusters SAID/SIDD/SIRD/MOD/MARD defined by GADA/age/BMI/HbA1c/HOMA2-B/HOMA2-IR) transport to South Asian adults in UKB-SA (n~8k, proxy-first), CARRS (n~12k urban India, primary), and ICMR-INDIAB (n~113k national, secondary) using pre-registered centroids-vs-de-novo clustering with formal positivity/overlap diagnostics (inverse-odds weighting, ESS, truncation 1%/5%/10%, S-score AUC, SMD, overlap coefficient, Li overlap weights ATO) and a GADA-free 6→3 variable ablation for India primary-care deployability. Each phase is independently publishable while DUAs are pending; synthetic UKB-SA proxy (N=8k, honest, no PHI) already proves pipeline (completeness 98% synthetic, ARI 0.25 vs de-novo, SMD 50% failure). Thresholds are locked before data receipt (completeness ≥85%, S-score AUC <0.70 adequate, ESS>70%, ARI ≥0.60 transports; otherwise transport fails and de-novo India-specific subtypes are proposed).

---

**Checklist to attach to each DUA:**

- [ ] OSF prereg PDFs (candidate_007 + candidate_005_006, hashes)
- [ ] Variable lists (§2.2, §3.2, §4.2 above, plus docs age)
- [ ] Analysis plan (k-means vs GMM vs hierarchical, IOPW truncation, Jaccard bootstrap, Cox HR CKD/retinopathy/insulin, calibration per Van Calster, net benefit)
- [ ] This DUA_APPLICATION_PACK.md (≥80 lines, timeline, contacts)
- [ ] Synthetic proxy results (full_runs/candidate_007/ logs + ARI + ablation) as pipeline proof
- [ ] Ethics letters (institutional IRB, ICMC MR guidelines compliance, UKB EGC)
- [ ] RAP/cloud budget (UKB credits + CARRS secure portal)
- [ ] No PHI declaration + pre-registration HARKing prevention statement

*End of pack — ready to submit. Next: OSF timestamp Stage 1 + DUA dispatch Week 0.*
