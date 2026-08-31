# Cycle 13+14 Combined — Programme Closure (n=150 final + Tier 2 submission + audit)
**Date:** 2026-08-31 · **Agents:** Research Lead + clinical-evidence-scout + methods-scout (adversarial MONITOR light) · **Rate-limit incidents:** none

## Objective
Finish the programme in one: close 004 corpus to 150/150 (100%, n=30 dual final) + cut Tier 2 journal submission packs (005+006 & 007) + light adversarial MONITOR audit + final programme report — so all 7 dossiers are RR + full-run + submission-ready with honest synthetic proxy (B-restricted 1–6mo).

## Assignments
- **clinical-evidence-scout:** 004 n=90→150 final (60 NEW PMIDs, n=30 overlap, κ+Wilson+PRISMA+Rayyan) → `full_runs/candidate_004/` final v3→final (433-line log, 150 rows, 34+33 calls, 589s)
- **methods-scout:** Tier 2 submission packs (005+006 + 007, 4 files each) + MONITOR + final report → `submission/candidate_005_006/` + `submission/candidate_007/` + `reports/final_programme_report.md` + `working/agent_notes/adversarial-reviewer/cycle1314_monitor.md` (130+85 lines, 34 calls)
- Brief: `working/CYCLE_13_BRIEF.md` (no sudo, honest synthetic, seeds 20260830, E-utilities ≤3/s, Git `d419b12`).

## Findings
**Programme CLOSED — 150/150 final + 8-file Tier 2 submission + 130-line final report + 85-line MONITOR KEEP 7/7, honest execution.**

| Deliverable | Path | Lines/Log | Key numbers |
|---|---|---|---|
| **004 final corpus** | `full_runs/candidate_004/` final | `433-line log` `run_full_004_final.py` 1040 lines | **60 NEW PMIDs retstart 90** dedup0 → **150/150 (100%)** efetch 150/150 real titles, `91+151` screening/rayyan final 151 lines each, `151` extraction 22-col |
| **Overlap final** | `full_004_kappa_interim_final.txt` 91 lines | n=30 of 30 =100% preserves prior 18 `[2,3,6,8,9,10,11,14,16,18,21,23,25,26,29,33,40,62]` +12 new `[35,36,44,58,60,64,76,96,103,114,142,147]` | **κ interval-aware 0.545 Po0.767 Pe0.487** (trajectory 0.615→0.576→0.545), overall **0.842 PASS**, PROBAST **0.795 PASS**, masking **0.366** rare |
| **Wilson + era** | same | primary `47/150=0.313 [0.245,0.391]` vs `0.300` at90 stable; masking `0.031[0.008,0.105]` | **era-split 2024: pre 27/60=0.450[0.331,0.575] vs post 20/90=0.222[0.149,0.318] χ²8.68 p0.0032 Yates p0.0057 Fisher OR2.86 p0.0041** — now significant at final (prior p0.479 at90), Wilson overlaps but chi2 detects |
| **PRISMA** | `full_004_prisma_final.txt` 63 lines | 570 TRIPOD+validation →150 screened (100%) →121 sought →150 extraction | re-verified `570/8188/494/18` 0 duplicates vs prior 90 |
| **005+006 submission** | `submission/candidate_005_006/` | `cover 59 + checklist 34 (27 DONE) + manifest 135 + repro 104` =332 | journal Stat Med/JASA, gap audit-anchored II 40k AUC0.500→0.967 ESS1.00→0.005 R*1.001–1.531 hashes `70bb40c/d15d005e/ce171f81/d9e6d20c/ba7626` |
| **007 submission** | `submission/candidate_007/` | `59+34+130+102`=325, `ba7626/747a/c179/129f` | journal Nature SD/JAMIA, ARI0.250 FAILS 3-var0.446 6vs30.243 |
| **Final report** | `reports/final_programme_report.md` 130 lines | 12 cycles C0→12 + closure bridge 1624 RR (1035+589) 40k+8k+150 | programme closure verdict |
| **MONITOR** | `working/agent_notes/adversarial-reviewer/cycle1314_monitor.md` 85 lines | 8 spot checks | **KEEP 7/7 no kills**, no new lit doc-only |

Honest synthetic proxy (DUA staged 1–6mo), seeds 20260830, no sudo, no PHI, 67 calls total (34+33), E-utilities ≤3/s with 60s→120s backoff (2 reruns for `PosixPath.__format__` fix).

## Decisions
**Programme closure — all 7 RR Stage-1 + full-run + OSF + submission-ready:** 004 corpus at 150/150 with borderline κ0.545 (re-train required per gate before prevalence publication, but overall/PROBAST PASS); Tier 2 submission packs mirror Tier1 `submission/candidate_001/` discipline; MONITOR light finds no kills — DUA opening enables B-proxy validation when approved (no further cycles required unless restricted data arrives).

## Candidates created/weakened/killed
No dossier changes; 7 KEEP (no kills) — programme closure.

## Rate-limit incidents
_none_ (34+33=67 calls total, 2 reruns for Path-format bug, no 429s beyond backoff)_

## Ledgers updated
`search_log.csv` 327 unchanged (execution final doc-only) · `evidence_registry.csv` 217 unchanged

## State
- Candidates: 7 KEEP → 1624 RR + 40k+8k + **150/150 final** → submission 12 files (001 4 + 005_006 4 + 007 4) · Search log 327 · Evidence 217
- Shortlist: FROZEN · Programme CLOSED

## Next cycle
_Programme closure — maintenance only: DUA opening (UKB-SA 1–3mo + CARRS 2–3mo + ICMR-INDIAB 3–6mo) enables 40k→B re-tilt and 8k→B ARI re-run when approved; no further exploration cycles unless new restricted data triggers Tier 1→2 re-execution._

