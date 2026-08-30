# Pilot 004 — Rayyan-ready corpus pilot (TRIPOD validation, interval-aware subgroup calibration)

**Candidate 004 dossier:** `ideas/candidate_004.md` (TRIPOD corpus audit n=150, interval-aware subgroup calibration per Riley + TRIPOD+AI era split).  
**Cycle:** 7 — clinical-evidence-scout pilot 3 (Rayyan-ready).  
**Status:** Pilot dry-run n=20 of target n=150 (Wilson ±0.06). Real E-utilities execution, synthetic extraction stub for form validation.

## Aim
Prove Tier-1 D-literature pipeline: PubMed E-utilities `esearch`+`efetch` for `TRIPOD[Title/Abstract] AND validation[Title/Abstract]` (expect 570), fetch n=20, define interval-aware extraction form (slope CI/plot band per Riley `10.1136/bmj-2024-080749` + TRIPOD+AI era split + masking rate), demonstrate dual-extraction on n=5 overlap with kappa stub, Wilson CI stub for p(interval-aware subgroup calibration) + masking rate, generate PRISMA pilot flow, re-verify eutils counts (570 vs 8188 vs RECORD 494 vs STROBE 18).

## Data path
- **Primary:** PubMed E-utilities (`https://eutils.ncbi.nlm.nih.gov/entrez/eutils`) — open, no PHI, rate ≤3/s, `tool=pilot_004`.
- **Locked corpus filter (pre-registered):** `TRIPOD[Title/Abstract] AND validation[Title/Abstract]` + `2015:2025[PDAT]` + `Humans[Mesh]` + `English[lang]` → sorted PMID → `numpy.random.default_rng(20260830)` → n=150 (pilot n=20).
- **Full-text (full scale):** Europe PMC `fullTextXML` (OA ~60%) + institutional proxy for remainder.
- **Sensitivity corpora:** `calibration AND external validation` (8188), `RECORD AND validation AND calibration` (494), `STROBE AND external validation` (18) — all re-verified this run.

## Run command
```bash
python3 pilots/candidate_004/run_pilot_004.py
# logs: pilots/candidate_004/logs/pilot_004.log
# outputs: pilots/candidate_004/outputs/pilot_004_extraction_pilot.csv
#          pilots/candidate_004/outputs/pilot_004_prisma_pilot.txt
#          pilots/candidate_004/outputs/pilot_004_pmids.txt
```
Dependencies: `python3` stdlib + `numpy` (Wilson + RNG). No API key; respects E-utilities rate.

**Pinned versions:** Python 3.11.15, numpy (any), E-utilities retmode=json.

## Outputs
| File | Rows | Description |
|------|------|-------------|
| `outputs/pilot_004_extraction_pilot.csv` | 21 (20+header) | Pilot extraction form: 22 columns — interval-aware flags (slope CI/plot band per Riley), subgroup stratifiers (PROGRESS), masking indicator (overall pass slope 0.8–1.2 + intercept ±0.3 + ICI<0.05 while ≥1 subgroup fail), TRIPOD+AI era, PROBAST, dual_overlap_flag, adjudication_note, rayyan_label. Random pilot n=5 overlap resolved via adjudication. |
| `outputs/pilot_004_prisma_pilot.txt` | — | PRISMA 2020 pilot flow (Identification/Screening/Eligibility/Included) with counts re-verified this run, Wilson stubs, kappa, sensitivity corpora. |
| `outputs/pilot_004_pmids.txt` | 20 | Fetched PMIDs (one per line) for Rayyan/Covidence import. |
| `logs/pilot_004.log` | 106 lines | Full stdout with E-utilities counts, efetch titles, overlap PMIDs, kappa 0.615, Wilson CIs. |

**Rayyan-ready:** CSV includes `pmid,title,journal,year,rayyan_label,dual_overlap_flag,subgroup_interval_aware` — import via Rayyan CSV or resolve PMIDs to RIS via `https://doi.org` / Europe PMC. Pilot `rayyan_label` is stub (full n=150 uses real title/abstract screening via Rayyan with 20% dual).

## Verification (real execution 2026-08-30)
- **E-utilities re-verification (this run):** TRIPOD 570, calibration+external-valid 8188 (~7% language bias), RECORD 494, STROBE 18 — all `OK` vs expected per `ideas/candidate_004.md` REVISE addendum.
- **Sample fetch:** esearch total 570, fetched 20 IDs (e.g. 40418571, 40241963, …), efetch 20 records returned with titles/years (log lines 16–35).
- **Dual-extraction simulation:** n=5 overlap indices [2,3,6,8,11] PMIDs [38000872,41082207,40626581,38596087,38783054]; R1=[1,0,0,1,0] R2=[1,0,1,1,0]; Po=0.800 Pe=0.480 **kappa=0.615** (target ≥0.7; pilot borderline → would re-train per protocol; full n=30 overlap).
- **Wilson CI stubs (pilot n=20):** p(interval-aware subgroup)=5/20=0.250 **[0.112,0.469]** (full expected <0.10); masking 1/20=0.050 [0.009,0.236]; p(overall calibration) 14/20=0.700 [0.481,0.855]. Wilson via score method (not Wald) per protocol.
- **Hash:** `pilot_004_extraction_pilot.csv` sha256:a724531fd10a (logged).

Full n=150 will add: Europe PMC fullTextXML retrieval, real extraction per Van Calster hierarchy + Riley intervals, PROBAST+AI, Wilson ±0.06, Newcombe difference CI, χ²/Fisher era split, SMD/κ≥0.7 checkpoint at n=30.

## Scaling to full
Wall-clock: pilot seconds → full n=150 ~4–6 weeks with 2 extractors (20% dual). Cost <$50 (library proxy). OSF pre-reg holds E-utilities string + PMID seed; no retrieval of PDFs beyond publisher terms.

## Limitations (pilot honesty)
Extraction values for n=20 are synthetic pilot stubs to demonstrate form/κ/Wilson pipeline — full n=150 replaces with real coding. Kappa 0.615 is stochastic pilot; target ≥0.7 after training adjudication. E-utilities counts are live and may drift ±few.

## Links
- Dossier: `ideas/candidate_004.md` (Gates 4–8, extraction matrix, PRISMA, REVISE 570/8188/494/18).
- Shortlist: `reports/shortlist_cycle_06.md`, `shortlist/SHORTLIST.md`.
- Europe PMC example: PMC13169604 (Queiroz, 61K chars, 2 tables) — form feasibility.

## No PHI
PubMed metadata only; no patient-level data.
