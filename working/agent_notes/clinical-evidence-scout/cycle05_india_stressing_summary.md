# Cycle 5 — India-Stressing Dossiers 005/006/007 — Summary
**Agent:** clinical-evidence-scout | **Date:** 2026-08-30 | **Status:** COMPLETE
**Dossiers:** ideas/candidate_005.md, ideas/candidate_006.md, ideas/candidate_007.md
**Pool:** muse-spark-1.2-contributor-free via opencode-zen/free; respect ≤24/min ceiling 30 max 2 concurrent — batch writes, no model calls in this cycle (markdown generation only)
**Ledgers:** literature/search_log.csv (+48 rows, 16 per dossier avg) + literature/evidence_registry.csv (+30 rows, 10 per dossier) — both appended verbatim
**Web extracts:** Europe PMC PMC12550443 (ICMR-INDIAB-23 MONO 43.3% table) + PMC13312064 (Kaur ED audit Tables 1-10) + PMC12813935 (Khanna Medicine OPD Tables 2-6) — all via Europe PMC fullTextXML JATS with <table-wrap> preserved; each dossier cites ≥1 extract with numbers/table
**DOI 302:** Every dossier ≥10 papers with ≥1 DOI 302 verified via curl -I -s https://doi.org/<DOI> (all 302 to publisher); see appendix tables

## Checkpoint
- 005: G0→G3 table (BMI 28.3→22.8, MONO 0→56.7%, age 62→48, HbA1c 78%→15% selective P0.20, generic 100→4.7%, AYUSH 0→96%, docs 100→8.5%) + tilting (entropy balancing) + S_visit censoring + diagnostics (SMD, S-score AUC, ESS, trimming 0.05/0.10) + 8 gates + Evidence AGAINST (Sri Lanka Framingham, CARRS risk, PlasmodeSim) + scope ceiling 4-6mo D+B proxy
- 006: B→R* translation (p1/p0 imputed per contrast, RR_UD sweep 1.2→4.0, fixed-point R*≈1.4-2.0) + titration contour + NC ladder (Lipsitch) + plasmode P(U) 0.10/0.44/0.96 + 8 gates + Evidence AGAINST + scope ceiling
- 007: centroids vs de novo ARI, 6→3 var ablatives (GADA/HOMA-free), inverse-odds weighting overlap/ESS/truncation 1%/5%/10%, outcomes CKD/retinopathy/insulin, baselines, 8 gates + Evidence AGAINST + scope ceiling

## Named DUA route (all dossiers)
- CARRS: Steering Committee via Emory/PHFI, restricted DUA, 2–3 months
- UKB-SA: UK Biobank Research Analysis Platform (RAP) application, category 2, weeks–months (1–3mo typical)
- ICMR-INDIAB: ICMR-NIE + MDRF collaboration, 3–6 months (summary prevalences open now via Lancet/IJMR fullTextXML)
- Staged: D (plasmode/open audits) immediate → B proxy (UKB-SA) weeks–months → B restricted (CARRS/ICMR-INDIAB) months; each phase independently publishable

## Search strategy compliance
- Per dossier: 2+ distinct strategies (005: Indian epidemiology + visit-process shift; 006: audit/WHO-indicator + E-value/QBA; 007: Ahlqvist clustering + HTE transport) + reviews (Degtiar, Kang, Inoue, Zhang, J Clin Epi, Hernan, Pearl) + synonyms + chaining + adversarial (try to close gap) — all logged verbatim to search_log.csv with query, concept, hits, n_inspected, notes, verification_status

## Verification
- All dossiers contain explicit 8-gate headings verbatim + Evidence AGAINST + Relevant datasets + India relevance STRESSES-ASSUMPTION + Confidence Medium + scope ceiling + next search executable queries + appendix search log
- All dossiers include Important papers table (10 papers, ≥1 DOI 302) + web_extract with numbers/table
- Ledgers appended verbatim; counts: search_log 233→281, evidence_registry 170→200

## Next
- Adversarial-reviewer kill round at ≥6 dossiers (now 3 dossiers; await methods-scout 001-004 to trigger KEEP/REVISE/KILL)
- UKB-SA RAP application submission (document ID) + OSF pre-registration templates for each dossier before EXPLORE
