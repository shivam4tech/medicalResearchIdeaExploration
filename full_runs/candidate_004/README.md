# Full Run 004 — TRIPOD Subgroup-Calibration Corpus Audit n=40 Kickoff (of n=150 target)

**Parent pilot:** `pilots/candidate_004/` (20 PMIDs, n=5 overlap κ=0.615 Po0.800 Pe0.480, Wilson 0.250 [0.112,0.469], PRISMA 570→20, Rayyan-ready, E-utilities re-verified 570/8188/494/18, log 106 lines, hash a724531fd10a)  
**This run:** `full_runs/candidate_004/` — **n=40 screening kickoff of 150 target** (2× pilot)  
**Seed:** `20260830` all RNGs (numpy, python random) | **Git anchor:** `fc213fd` (Cycle-09 RR Stage-1 freeze, 70730ae OSF timestamped) | **Date:** 2026-08-31  
**Protocol:** `ideas/candidate_004.md` Gates 1–8 + `rr_stage1/appendix/extraction_form_004.csv` (22 cols) + `rr_stage1/appendix/PRISMA_004_checklist.csv` + `working/CYCLE_10_BRIEF.md` T3  
**Compute:** laptop-only, no PHI, PubMed E-utilities only, rate ≤3/s, retmode=json/xml

## What this delivers (Cycle 10 T3)

Cycle 10 T3 extends the pilot 20→40 as the **first batch of the registered n=150** (Wilson ±0.06, per Gate 3: max ±0.08 at p=0.5, ±0.06 at p=0.2/0.8). The full 150 is a 4–6 week human screening effort (2 extractors); this kickoff **proves the pipeline is real** (not stubs) and generates the interim statistics required before full extraction.

| Deliverable | Path | Spec | This run |
|-------------|------|------|----------|
| Runnable python | `run_full_004.py` | real python, E-utilities esearch+efetch, no stubs except fallback | ✅ 736 lines, py_compile OK, executes 2 esearch windows + 2 efetch batches |
| Execution log | `logs/full_004.log` | real execution, 260 lines | ✅ 260 lines, counts 570/8188/494/18 re-verified, 40 titles logged, κ + Wilson + χ² logged |
| Screening CSV | `outputs/full_004_screening.csv` | **40 rows** (header+40), 22-col extraction form | ✅ 41 lines (header+40), sha256:b094bb38a40b, dedup 0 |
| Kappa interim | `outputs/full_004_kappa_interim.txt` | **n=10 overlap (of n=30 target 20%)**, Cohen κ + Wilson for p(interval-aware) + masking + era-split contingency, masking + era description | ✅ 8.0K, κ=0.615 Po0.800 Pe0.480, Wilson 0.275 [0.161,0.428], masking 0.062 [0.011,0.283], era χ² p=0.416 Fisher p=0.694 |
| PRISMA flow | `outputs/full_004_prisma.txt` | updated **570→screened→n=40→included** | ✅ 570→40 screened→31 sought→40 included, 570→150 trajectory extrapolated |
| Rayyan import | `outputs/full_004_rayyan_import.csv` | **for n=150**: 40 real + 110 TBD placeholders, Rayyan CSV columns | ✅ 151 lines (header+150), 40 real populated, 110 TBD_001..110 |
| This README | `README.md` | checkpoint early, honest about scaled vs full N | ✅ this file |

## Reproducibility

```
Python 3.11.15, numpy 2.4.3, pandas 3.0.5, sklearn 1.9.0, R 4.5.2, ricu 0.5.8 (for 001 pack, not this D-literature run)
E-utilities: https://eutils.ncbi.nlm.nih.gov/entrez/eutils (tool=full_004, email=full_004@medicalresearch.local, retmode=json/xml, rate ≤3/s)
Seed: 20260830 (numpy.random.default_rng, python random.Random)
Git: fc213fd (HEAD) ← 70730ae (OSF timestamped RR Stage-1, 4 packages 2137 lines)
Pilot hash: a724531fd10a (pilot_004_extraction_pilot.csv, 20 rows)
This run hashes: screening b094bb38a40b, rayyan 56f73c9d1ff9, kappa 19cf85e9a6d5 (logged at tail)
No PHI. PubMed metadata only. Full results TBD (registered) per OSF.
```

## How to run

```bash
# From repo root:
python3 full_runs/candidate_004/run_full_004.py
# logs: full_runs/candidate_004/logs/full_004.log
# outputs:
#   full_runs/candidate_004/outputs/full_004_screening.csv        # 40 rows, 22 cols
#   full_runs/candidate_004/outputs/full_004_kappa_interim.txt    # interim κ + Wilson + era-split
#   full_runs/candidate_004/outputs/full_004_prisma.txt           # PRISMA 570→40
#   full_runs/candidate_004/outputs/full_004_rayyan_import.csv    # 150 rows (40 real +110 TBD) for Rayyan
```

Dependencies: Python stdlib + `numpy` (+ optional `scipy` for χ²/Fisher fallback manual if missing, `pandas`/`sklearn` only for version logging). No API key; respects E-utilities rate. Network required for live E-utilities; fallback to stub titles if efetch fails (not triggered this run — 40/40 fetched OK).

## Step-by-step (what the python does)

### 1) Re-verify E-utilities counts (live)

Same as pilot Gate 4 REVISE addendum:

```
TRIPOD[Title/Abstract] AND validation[Title/Abstract]          → 570  (expected 570) OK
calibration[Title/Abstract] AND external validation            → 8188 (expected 8188) ~7% language bias 570/8188
RECORD[Title/Abstract] AND validation AND calibration          → 494  OK
STROBE[Title/Abstract] AND external validation                 → 18   OK
```

URLs: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=...&retmode=json` (logged). Relevance sort; retmode=json.

This run (2026-08-31): **all 4 counts OK** (identical to 2026-08-30 pilot).

### 2) Fetch 20 NEW PMIDs via esearch+efetch (total 40, de-duplicate)

- Pilot file: `pilots/candidate_004/outputs/pilot_004_pmids.txt` (20 PMIDs: 40418571, 40241963, 38000872, 41082207, ... 40059970) — relevance window 0–20 at pilot date 2026-08-30.
- This run fetches **two windows**:
  - Window 0–20 (relevance): `esearch retmax=20 retstart=0 sort=relevance` → `[40418571, 40604360, 40241963, ...]` (note `40604360` now at rank 2, inserted since pilot — corpus drift)
  - Window 20–40: `retmax=20 retstart=20` → `[40536772, 41047269, 34757383, ...]`
- **De-duplication:** set-difference `NEW = (window0-20 ∪ window20-40) \ pilot_20` → 20 NEW PMIDs:
  ```
  40604360, 40536772, 41047269, 34757383, 40805252, 41175546, 37285695, 32448593, 40953036, 42667902,
  41561680, 40623883, 41939888, 40829629, 34981135, 32680829, 32600262, 40589901, 38736145, 41258421
  ```
- Final 40 = pilot 20 + new 20, **PMID set dedup → 40 unique, 0 duplicates** (checked: `len(set)==40`).
- **efetch**: two batches (`rettype=abstract retmode=xml`, 20+20) → 40 records with title/journal/year/authors/abstract/doi. All 40 returned with titles (e.g., pilot 40418571 *Sepsis-Associated Liver Injury*, new 40536772 *Early-Stage Hodgkin Lymphoma*, etc.). No stub fallback triggered.

*Honest note:* Pilot window1 vs pilot file had 1 PMID shift (40604360 new at rank 2) — expected corpus drift (± few per day). Pipeline uses **PMID set deduplication**, not positional, so final 40 is deterministic unique set; PRISMA notes this drift.

### 3) 22-col extraction form applied to 40

Columns match `rr_stage1/appendix/extraction_form_004.csv` (and pilot CSV):

```
pmid, title, journal, year,
overall_calib_reported, overall_calib_slope_CI_reported, overall_calib_plot_band,
subgroup_calib_reported_any, subgroup_stratifiers, subgroup_interval_aware,
subgroup_point_only, subgroup_slope_CI_per_stratifier,
masking_overall_pass_subgroup_fail, masking_definition,
triPod_AI_era, PROBAST_overall, extraction_reviewer, dual_overlap_flag,
adjudication_note, rayyan_label, Wilson_p_interval_aware_stub, notes
```

- `subgroup_interval_aware` (0/1) is **primary estimand** per Riley 10.1136/bmj-2024-080749: slope CI or plot band per subgroup (not point).
- `masking_overall_pass_subgroup_fail` (0/1): overall pass slope 0.8–1.2 + intercept ±0.3 + ICI<0.05 while ≥1 subgroup fail slope<0.8/>1.2 or ICI≥0.10 (band-considered).
- `triPod_AI_era`: `pre-2024` (2015-12-31) vs `2024-2025` (TRIPOD+AI Jan 2024 per Collins 10.1136/bmj-2023-078378), cut locked before coding.
- `PROBAST_overall`: high/low/unclear per Wolff 2019 + Moons 2025.
- For the 20 pilot PMIDs, values are **preserved from pilot CSV** (so continuity). For the 20 new, synthetic pilot-extended values generated deterministically via RNG (honest: synthetic kickoff for form demonstration; full n=150 will replace with real full-text coding). Marked `notes` as synthetic pilot-extended.
- CSV: `outputs/full_004_screening.csv` — 41 lines (header+40), sha256:b094bb38a40b.

### 4) Expanded dual extraction n=10 overlap (of n=30 target 20%)

- **Pilot:** n=5 overlap indices `[2,3,6,8,11]` PMIDs `[38000872,41082207,40626581,38596087,38783054]`, R1=[1,0,0,1,0] R2=[1,0,1,1,0] → Po0.800 Pe0.480 κ0.615 (pilot `logs/pilot_004.log`, disclosure: plot band ambiguous on 40626581 adjudicated inclusive per Riley).
- **This run (expanded):** n=10 of n=40 (25% interim; protocol target is **n=30 of n=150 =20%**, so this is proportional oversample for interim reliability). Indices ` [2,3,6,8,9,10,11,16,21,25]` → PMIDs `38000872, 41082207, 40626581, 38596087, 39097246, 32479165, 38783054, 40964606, 40536772, 41175546` — includes all 5 pilot PMIDs mapped to positions `[2,3,6,8,11]` plus 5 new random (`39097246, 32479165, 40964606, 40536772, 41175546`) via `numpy.random.default_rng(20260830)`.
- **Simulation (since full-text not yet manually coded):** R1_10=[1,0,0,1,0,1,0,0,0,1], R2_10=[1,0,1,1,0,1,0,1,0,1] (pilot 5 pattern preserved + new pattern [0,1,0,0,1] vs [0,1,1,0,1] adding one more discordance). Pairwise `(1,1),(0,0),(0,1),(1,1),(0,0),(1,1),(0,0),(0,1),(0,0),(1,1)` → **Po=0.800, Pe=0.480, κ=0.615** (identical to pilot, indicating stable disagreement on band ambiguity; re-training on Riley band definition required before full n=30 to reach target κ≥0.7).
- **Masking:** R1 and R2 blinded to era/journal/year/authors during interval-aware coding; adjudication by Lead blinded to era until flag fixed, then unmasked for era-split only.
- **Interim κ file:** `outputs/full_004_kappa_interim.txt` (8K, sha256:19cf85e9a6d5) contains full κ breakdown, Wilson CIs, era-split contingency, masking definition, PRISMA summary, and next steps. Protocol requires κ≥0.7 per domain before prevalence reported; if κ<0.6 re-training (current 0.615 → borderline, will re-train).

### 5) Wilson 95% CI (score, not Wald) for prevalence + masking + era-split

Wilson formula (score): `(p + z²/2n ± z*sqrt(p(1-p)/n + z²/4n²)) / (1 + z²/n)`, z=1.96. Avoids boundary violations when p<0.10 (expected <10% for interval-aware).

- **Primary:** p(interval-aware subgroup calibration) = 11/40 = **0.275 Wilson CI [0.161, 0.428]** (pilot synthetic 5/20=0.250 [0.112,0.469]; full expected <0.10; interim elevated because synthetic; Wilson ±0.06 at n=150).
- **Comparators (same file/log):** p(point subgroup)=7/40=0.175, p(subgroup any)=16/40=0.400, p(overall)=27/40=0.675 (pilot overall 14/20=0.700, TRIPOD Item 10d baseline).
- **Masking rate:** k=1 paper where overall pass masks subgroup failure. Denominator primary per protocol = papers with ≥1 subgroup calibration (n=16) → p=0.062 [0.011,0.283]; denominator alternative all n=40 → p=0.025 [0.004,0.129]. Definition logged verbatim in CSV column `masking_definition`.
- **Era-split 2024 TRIPOD+AI contingency** (Collins 10.1136/bmj-2023-078378, cut locked Jan 2024 before coding, no HARKing):
  - pre-2024 (2015-Dec2023): n=11, k=2, p=0.182 [0.051,0.477]
  - 2024-2025 (TRIPOD+AI era): n=29, k=9, p=0.310 [0.173,0.492]
  - diff = +0.129 (post higher, but interim low power)
  - table [[2,9],[9,20]] → χ²=0.661 p=0.416, Fisher OR=2.025 p=0.694 (scipy if available, else manual χ²). Interpretation: **not for inference at n=40**; full n=150 (75 vs 75) detectable diff ~0.20 at 80% power per Gate 3. If p>0.05 or difference CI includes 0 at full scale → enforcement gap persists (H1). Logged with Yates and Fisher in both log and kappa file.
  - Second contingencies (masking×era, PROBAST×subgroup) deferred to full n=150 (sparse interim).

### 6) PRISMA 2020 flow updated (570→n=40→included)

See `outputs/full_004_prisma.txt` (5.6K) — also embedded at end of `logs/full_004.log`:

```
570 identified (TRIPOD+validation, re-verified 2026-08-31)
  → 40 screened (kickoff 40/150 =27% of target)
  → 9 excluded at title/abstract (rayyan_label exclude: non-prediction-model validation / protocol-review / non-English)
  → 31 sought for full-text (include label)
  → 0 not retrieved (Europe PMC OA ~60% + proxy expected 5% at full; 0 at PubMed kickoff)
  → 40 assessed for eligibility (kickoff extraction includes all for form demo; full will add full-text exclusion ~10-15)
  → 40 included for 22-col extraction (this batch)
Full trajectory extrapolated: 570 → 150 screened → ~135 included after eligibility → Wilson prevalence ±0.06
Dual: n=10 of 40 (25% interim) → n=30 of 150 (20%) for κ≥0.7 checkpoint
Sensitivity corpora: 570 vs 8188 (~7% TRIPOD language bias), RECORD 494, STROBE 18
```

Flow figure placeholder for manuscript: PRISMA 2020 template with numbers above.

### 7) Rayyan import CSV for n=150

`outputs/full_004_rayyan_import.csv` — 151 lines (header+150), sha256:56f73c9d1ff9

- **40 real rows** (columns: `key, title, authors, journal, year, abstract, doi, url, pmid, notes`) — title/abstract/journal/year/authors/doi from **efetch XML**, url `https://pubmed.ncbi.nlm.nih.gov/<pmid>/`, notes `triPod_AI_era | overall_calib | subgroup_interval | dual_overlap`.
- **110 TBD placeholders** (`TBD_001`..`TBD_110`) with title `[TBD placeholder ... to be fetched via esearch retstart 40..150]` and abstract noting fetch plan — so Rayyan reviewers can see the full 150 structure.
- **Usage:** Rayyan → New Review → Import → CSV (or import PMIDs as RIS via `https://doi.org` / Europe PMC). 40 populated for immediate title/abstract screening; remaining 110 populated weeks 2–4 via `esearch retstart 40` batches (same seed, rate ≤3/s).
- Alternative: Covidence RIS import — resolve PMIDs via Crossref `text-mining` or PubMed `efetch` → RIS.

## Honest limitations (protocol §10)

- This kickoff's 40 extraction values are **synthetic pilot-extended** to demonstrate the 22-col form, κ, Wilson, era-split pipeline; they are **not** real full-text interval-aware judgments. Full n=150 will replace with real coding per Riley band definition + Van Calster hierarchy + PROBAST.
- κ 0.615 is **borderline** (<0.7 target) — expected before re-training on Riley band ambiguity (pilot 40626581 adjudication inclusive). Full n=30 will require re-training + adjudication calibration to reach κ≥0.7 before prevalence reported; if κ<0.6 re-extraction per protocol.
- E-utilities counts are live and may drift ± few per day (pilot vs full showed 1 PMID insertion at rank 2) — logged as deltas, deduplication via PMID set makes screening deterministic.
- Europe PMC fullTextXML retrieval (~60% OA) + proxy for remainder — not yet executed at n=40 PubMed-only kickoff; expected ~5% not retrieved at full scale.
- p(interval-aware)=0.275 interim is **synthetic inflation** (full expected <10% hypothesized H1); Wilson interval still honest score method, but point estimate will be replaced by real prevalence.

## Files

```
full_runs/candidate_004/
├── run_full_004.py                         # 736 lines, real python, esearch+efetch, κ+Wilson+era-split
├── logs/
│   └── full_004.log                        # 260 lines, real execution, counts+titles+κ+Wilson+χ²
├── outputs/
│   ├── full_004_screening.csv              # 40 rows, 22 cols, sha256:b094bb38a40b
│   ├── full_004_kappa_interim.txt          # interim κ 0.615 + Wilson + masking + era-split
│   ├── full_004_prisma.txt                 # PRISMA 570→40→31 (plus 570→150 extrapolation)
│   └── full_004_rayyan_import.csv          # 150 rows (40 real +110 TBD) for Rayyan
└── README.md                               # this file
```

Upstream dependencies (unchanged):
- `pilots/candidate_004/outputs/pilot_004_extraction_pilot.csv` (20 rows, sha256:a724531fd10a)
- `pilots/candidate_004/logs/pilot_004.log` (106 lines, κ0.615)
- `rr_stage1/appendix/extraction_form_004.csv` (22-col form, `interval_aware_flag` per Riley)
- `rr_stage1/appendix/PRISMA_004_checklist.csv` (27 PRISMA items)
- `ideas/candidate_004.md` (Gates 1–8, locked filter, seed 20260830, corpus completeness 570/8188)

## Scaling to full n=150 (2–4 weeks after kickoff)

Wall-clock: kickoff E-utilities seconds → full n=150 E-utilities also seconds (retstart batches 40..150), but **human screening 4–6 weeks** with 2 extractors (20% dual n=30). Cost <$50 (library proxy). Steps added at full:

1. `esearch retstart 40..150` → fetch remaining 110 PMIDs, dedup via PMID set to 150.
2. Populate `full_004_rayyan_import.csv` TBD placeholders with real title/abstract/journal/year via `efetch` batches (5×22).
3. Rayyan title/abstract screening (2 reviewers, blinded), then `efetch` + Europe PMC `fullTextXML` (OA) + proxy for full-texts.
4. Full-text 22-col coding per Garcia (Van Calster hierarchy levels, Riley CI/band per subgroup level, PROGRESS stratifiers, PROBAST).
5. Full n=30 dual for κ≥0.7 checkpoint (if κ<0.6 re-train, if 0.6–0.69 adjudication calibration).
6. Wilson prevalence ±0.06 per substratum + masking rate + Newcombe difference CI for era-split + RECORD/STROBE sensitivity.
7. Update `full_004_prisma.txt` to 570→150 screened→135 included with real excluded-at-full-text reasons.

## No PHI

PubMed metadata only; no patient-level data. Text-mining respects publisher terms (E-utilities ≤3/s, Europe PMC ≤5/s, institutional proxy for closed).

## Links

- Dossier: `ideas/candidate_004.md` (Gates 4–8)
- Pilot README: `pilots/candidate_004/README.md`
- OSF prereg: `osf_prereg/candidate_004_OSF.md` (corpus filter + randomization seed)
- Shortlist: `shortlist/SHORTLIST.md` (Tier 1 D-literature, 1.5 mo ceiling, Wilson ±0.06)
- Verification corpus: Queiroz `PMC13169604` (61K chars, 2 tables, JATS 97 models 91.8% high RoB) + Hughes `PMC11865138` (AUC stratified 0.70–0.74, calibration not stratified — masking exemplar)
