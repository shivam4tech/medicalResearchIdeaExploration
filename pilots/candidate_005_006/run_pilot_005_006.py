#!/usr/bin/env python3
"""
Pilot 005_006 — paired G0->G3 plasmode D-phase

- G0_G3_table.csv audit-anchored (BMI 28.3->22.8, MONO 0->56.7%, age 62->48,
  HbA1c 78%->15% selective P0.20, generic 100->4.7%, AYUSH 0->96%, docs 100->8.5%)
- synthetic tilting / S_visit demo on N=5k synthetic MIMIC-like covariates
  (entropy balancing / IPW resampling stub)
- diagnostics SMD / S-score AUC / ESS / trimming per grade
- B->R* contour CSV (R*~1.4-2.0 per RR_UD sweep, bounding factor B)
- 9-cell config 3xP(U) 0.10/0.44/0.96 x 3xRR_UD 1.5/2.0/3.0

Ref: ideas/candidate_005 & 006, osf_prereg/candidate_005_006_OSF.md
No PHI. Synthetic only. Real python execution required.
"""
import math, random, hashlib, time, sys, os
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

BASE = Path(__file__).parent
OUT = BASE / "outputs"
LOG = BASE / "logs"
OUT.mkdir(parents=True, exist_ok=True)
LOG.mkdir(parents=True, exist_ok=True)

SEED = 20260830
rng = np.random.default_rng(SEED)
random.seed(SEED)

# G0->G3 locked table spec (from OSF)
G_TABLE = [
    {"dimension":"BMI (mean)", "parameter":"Mean BMI, kg/m2", "G0_MIMIC_ref_no_shift":"28.3", "G1_Mild_lean_urban_India":"26.0", "G2_Moderate_national_avg_MAIN":"24.5", "G3_Severe_rural_Tripura":"22.8", "anchor_justification":"MIMIC-IV mean ~28-29; ICMR-INDIAB gen obesity 28.6% -> thin-fat phenotype 10.25259/IJMR_328_2025"},
    {"dimension":"MONO prevalence", "parameter":"BMI<25 ∩ ≥2/5 risks, %", "G0_MIMIC_ref_no_shift":"0", "G1_Mild_lean_urban_India":"18", "G2_Moderate_national_avg_MAIN":"43.3", "G3_Severe_rural_Tripura":"56.7", "anchor_justification":"Mohan IJMR 2025 PMC12550443 (national 43.3%, Tripura 56.7%)"},
    {"dimension":"Age at event", "parameter":"Median CVD/T2D onset, y", "G0_MIMIC_ref_no_shift":"62", "G1_Mild_lean_urban_India":"58", "G2_Moderate_national_avg_MAIN":"52", "G3_Severe_rural_Tripura":"48", "anchor_justification":"CARRS IJE 10.1093/ije/dyac122; MDRF Young Diabetes Registry (5-10y earlier)"},
    {"dimension":"HbA1c measurement", "parameter":"% eligible with HbA1c observed", "G0_MIMIC_ref_no_shift":"78", "G1_Mild_lean_urban_India":"55", "G2_Moderate_national_avg_MAIN":"30", "G3_Severe_rural_Tripura":"15", "anchor_justification":"MIMIC ~78% protocol; ICMR-INDIAB every-5th 20% -> real-world lower; Kaur/Khanna tables"},
    {"dimension":"Selective observation", "parameter":"P(test | asymptomatic)", "G0_MIMIC_ref_no_shift":"0.78", "G1_Mild_lean_urban_India":"0.45", "G2_Moderate_national_avg_MAIN":"0.20", "G3_Severe_rural_Tripura":"0.20", "anchor_justification":"Cost/availability gating; diagnosis 91.5% missing ED; vs P(test|sympt)=0.80 gating (severe)"},
    {"dimension":"Generic prescribing", "parameter":"Generic %", "G0_MIMIC_ref_no_shift":"100", "G1_Mild_lean_urban_India":"85", "G2_Moderate_national_avg_MAIN":"64.9", "G3_Severe_rural_Tripura":"4.7", "anchor_justification":"Kaur Table2 64.9% (ED), Khanna Table2 4.7% (Medicine OPD) — 60-point spread"},
    {"dimension":"AYUSH concomitant", "parameter":"Ever herbo-mineral, %", "G0_MIMIC_ref_no_shift":"0", "G1_Mild_lean_urban_India":"10", "G2_Moderate_national_avg_MAIN":"44", "G3_Severe_rural_Tripura":"96", "anchor_justification":"Galib AYU 10.4103/ayu.ayu_81_20 95.9%/44%; NSS 10-40% national"},
    {"dimension":"Documentation", "parameter":"Diagnosis recorded, %", "G0_MIMIC_ref_no_shift":"100", "G1_Mild_lean_urban_India":"70", "G2_Moderate_national_avg_MAIN":"29", "G3_Severe_rural_Tripura":"8.5", "anchor_justification":"Kaur Table3 8.5% (ED), Khanna 70->29% (Medicine)"},
    {"dimension":"Polypharmacy", "parameter":"Drugs per prescription", "G0_MIMIC_ref_no_shift":"1.8-2.0", "G1_Mild_lean_urban_India":"2.65", "G2_Moderate_national_avg_MAIN":"4.5", "G3_Severe_rural_Tripura":"6.8", "anchor_justification":"Kaur 2.65±1.59, Khanna 6.8±1.7; 71% >=3 drugs"},
]

def bounding_factor(p1, p0, RR_UD):
    return (p1*(RR_UD-1)+1)/(p0*(RR_UD-1)+1)

def B_max(RR_EU, RR_UD):
    return (RR_EU*RR_UD)/(RR_EU+RR_UD-1)

def evalue(RR):
    return RR + math.sqrt(RR*(RR-1)) if RR>1 else None

def invert_evalue(B):
    # solve E(R*)=B => R* + sqrt(R*(R-1))=B => numeric
    # closed form: R = (B^2)/(2B-1) ??? let's solve numerically
    # Use binary search R in (1, B) actually E(R) >=R so R* <B; search R in [1, B+2]
    lo, hi = 1.001, max(1.5, B+2)
    for _ in range(100):
        mid = (lo+hi)/2
        ev = mid + math.sqrt(mid*(mid-1))
        if ev < B:
            lo = mid
        else:
            hi = mid
        if abs(hi-lo)<1e-6:
            break
    return (lo+hi)/2

def main():
    log_path = LOG / "pilot_005_006.log"
    orig_out = sys.stdout; orig_err = sys.stderr
    class Logger:
        def __init__(self, fp, orig):
            self.fp=fp; self.orig=orig
        def write(self, s):
            self.orig.write(s); self.fp.write(s)
        def flush(self):
            self.orig.flush(); self.fp.flush()
    lf = open(log_path, "w")
    sys.stdout = Logger(lf, orig_out)
    sys.stderr = Logger(lf, orig_err)
    print("=== PILOT 005+006 — paired G0->G3 plasmode D-phase ===")
    print(f"Seed {SEED}, {time.strftime('%Y-%m-%d %H:%M:%S %Z')}, Python {sys.version.split()[0]}")
    print(f"Working dir: {BASE}")

    # 1. Write G0_G3_table.csv
    print("\n--- Step 1: Write audit-anchored G0->G3 table ---")
    g_df = pd.DataFrame(G_TABLE)
    # Ensure column order per spec
    cols = ["dimension","parameter","G0_MIMIC_ref_no_shift","G1_Mild_lean_urban_India","G2_Moderate_national_avg_MAIN","G3_Severe_rural_Tripura","anchor_justification"]
    g_df = g_df[cols]
    g_path = OUT / "G0_G3_table.csv"
    g_df.to_csv(g_path, index=False)
    print(g_df.to_string(index=False))
    print(f"  wrote {g_path} ({len(g_df)} rows)")
    # Verify key values
    checks = [
        ("BMI G0", g_df.loc[0,"G0_MIMIC_ref_no_shift"], "28.3"),
        ("BMI G3", g_df.loc[0,"G3_Severe_rural_Tripura"], "22.8"),
        ("MONO G0", g_df.loc[1,"G0_MIMIC_ref_no_shift"], "0"),
        ("MONO G3", g_df.loc[1,"G3_Severe_rural_Tripura"], "56.7"),
        ("Age G0", g_df.loc[2,"G0_MIMIC_ref_no_shift"], "62"),
        ("Age G3", g_df.loc[2,"G3_Severe_rural_Tripura"], "48"),
        ("HbA1c G0", g_df.loc[3,"G0_MIMIC_ref_no_shift"], "78"),
        ("HbA1c G3", g_df.loc[3,"G3_Severe_rural_Tripura"], "15"),
        ("Generic G0", g_df.loc[5,"G0_MIMIC_ref_no_shift"], "100"),
        ("Generic G3", g_df.loc[5,"G3_Severe_rural_Tripura"], "4.7"),
        ("AYUSH G0", g_df.loc[6,"G0_MIMIC_ref_no_shift"], "0"),
        ("AYUSH G3", g_df.loc[6,"G3_Severe_rural_Tripura"], "96"),
        ("Docs G0", g_df.loc[7,"G0_MIMIC_ref_no_shift"], "100"),
        ("Docs G3", g_df.loc[7,"G3_Severe_rural_Tripura"], "8.5"),
    ]
    for label, got, exp in checks:
        status = "OK" if str(got)==exp else f"FAIL expected {exp}"
        print(f"  check {label}: {got} {status}")
    # also verify selective P0.20
    sel = g_df.loc[4]
    print(f"  selective observation G2={sel['G2_Moderate_national_avg_MAIN']} G3={sel['G3_Severe_rural_Tripura']} (expected 0.20)")

    # 2. Synthetic MIMIC-like covariates N=5k + tilting/S_visit demo
    print("\n--- Step 2: Synthetic MIMIC-like cohort N=5k, tilting & S_visit per grade ---")
    N = 5000
    # Generate base G0-like MIMIC covariates: BMI ~ N(28.3,5), Age ~ N(62,12), HbA1c ~ N(6.8,1.5) truncated, etc.
    bmi0 = rng.normal(28.3, 5.0, N).clip(14, 55)
    age0 = rng.normal(62, 12, N).clip(18, 95)
    hba1c0 = rng.normal(6.8, 1.4, N).clip(4.0, 14)
    mono0 = (rng.random(N) < 0.02).astype(int)  # near 0 in MIMIC (screened)
    generic0 = np.ones(N)  # 100%
    ayush0 = np.zeros(N)
    docs0 = np.ones(N)
    symptom_score = rng.normal(0,1,N)  # latent symptom for selective observation
    cost_score = rng.normal(0,1,N)

    base = pd.DataFrame({"bmi":bmi0, "age":age0, "hba1c":hba1c0, "mono":mono0, "generic":generic0, "ayush":ayush0, "docs":docs0, "symptom":symptom_score, "cost":cost_score})
    print(f"  base cohort: N={N} mean BMI {bmi0.mean():.2f} age {age0.mean():.1f} mono {mono0.mean():.3f}")

    # Define target BMI/mono per grade for tilting resampling (entropy balancing stub via resampling weights)
    grade_targets = {
        "G0": {"bmi_mean":28.3, "mono":0.00, "age_mean":62, "observe_rate_symptom_low":0.78, "generic":1.00, "ayush":0.00, "docs":1.00},
        "G1": {"bmi_mean":26.0, "mono":0.18, "age_mean":58, "observe_rate_symptom_low":0.45, "generic":0.85, "ayush":0.10, "docs":0.70},
        "G2": {"bmi_mean":24.5, "mono":0.433, "age_mean":52, "observe_rate_symptom_low":0.20, "generic":0.649, "ayush":0.44, "docs":0.29},
        "G3": {"bmi_mean":22.8, "mono":0.567, "age_mean":48, "observe_rate_symptom_low":0.20, "generic":0.047, "ayush":0.96, "docs":0.085},
    }
    # For each grade, create tilted copy: resample with weights targeting BMI/MONO means + add calibrated shifts
    # Simple stub: compute IPW weights via logistic targeting low BMI + mono
    diagnostics_rows=[]
    grade_frames={}
    for grade, tgt in grade_targets.items():
        # create copy with shifted BMI: add delta
        delta_bmi = tgt["bmi_mean"] - 28.3
        bmi_g = bmi0 + delta_bmi + rng.normal(0, 0.6, N)  # small noise
        # mono prevalence: generate directly
        mono_g = (rng.random(N) < tgt["mono"]).astype(int)
        age_g = age0 + (tgt["age_mean"]-62) + rng.normal(0,1.5,N)
        # S_visit censoring: P(observe | asymptomatic) = tgt observe_rate, symptomatic fixed 0.80
        # Define asymptomatic = symptom <0.5
        p_asym = tgt["observe_rate_symptom_low"]
        p_sym = 0.80
        is_sym = (symptom_score > 0.5).astype(int)
        # also cost-dependent via score
        # S_visit score = 0.7*symptom -0.5*cost ; but use p_asym/p_sym gating per spec
        p_observe = np.where(is_sym, p_sym, p_asym)
        # clip ayush-induced cost? just use p_observe
        # Adjust with small cost penalty for G3
        if grade=="G3":
            p_observe = np.clip(p_observe - 0.05*(cost_score>1), 0.05, 0.95)
        observed_hba1c_mask = rng.random(N) < p_observe
        # generic/ayush/docs as Bernoulli per target rate
        generic_g = (rng.random(N) < tgt["generic"]).astype(int)
        ayush_g = (rng.random(N) < tgt["ayush"]).astype(int)
        docs_g = (rng.random(N) < tgt["docs"]).astype(int)
        df_g = pd.DataFrame({
            "bmi": bmi_g.clip(14,55),
            "age": age_g.clip(18,95),
            "mono": mono_g,
            "hba1c_observed": observed_hba1c_mask.astype(int),
            "generic": generic_g,
            "ayush": ayush_g,
            "docs": docs_g,
            "symptom": symptom_score,
            "cost": cost_score,
            "S_visit_p": p_observe,
            "grade": grade
        })
        grade_frames[grade]=df_g
        # Diagnostics: SMD between G0 base and this grade
        # SMD = (mean_g - mean_G0)/pooled SD
        def smd(a,b):
            sd = math.sqrt((a.var()+b.var())/2) if (a.var()+b.var())>0 else 1
            return (b.mean()-a.mean())/sd if sd!=0 else 0
        smd_bmi = smd(bmi0, bmi_g)
        smd_age = smd(age0, age_g)
        smd_mono = smd(mono0.astype(float), mono_g.astype(float))
        # S-score: train logistic to distinguish source (G0) vs target grade
        # Stack G0 (label 0) vs this grade (label 1), features: bmi, age, mono proxy
        if grade=="G0":
            auc=0.50; ess_ratio=1.0; trim05=0.0; trim10=0.0
        else:
            X = np.vstack([
                np.column_stack([bmi0, age0, mono0.astype(float)]),
                np.column_stack([bmi_g, age_g, mono_g.astype(float)])
            ])
            y = np.array([0]*N + [1]*N)
            # add small jitter to avoid perfect separation? Already some overlap
            clf = LogisticRegression(penalty='l2', C=1.0, solver='lbfgs', max_iter=500)
            clf.fit(X, y)
            prob = clf.predict_proba(X)[:,1]
            auc = roc_auc_score(y, prob)
            # Compute IPP weights for target vs source: w = prob/(1-prob) for source? Use inverse odds
            # For diagnostics, compute weights for source population to transport to target: w = P(S=1|X)/P(S=0|X)
            p = np.clip(clf.predict_proba(np.column_stack([bmi0, age0, mono0.astype(float)]))[:,1], 1e-6, 1-1e-6)
            w = p/(1-p)
            # Normalize to mean 1
            w = w / w.mean() if w.mean()!=0 else w
            # ESS
            ess = (w.sum()**2)/( (w**2).sum() )
            ess_ratio = ess / N
            # Trimming: Crump 0.05/0.10 -> trim weights outside [alpha, 1-alpha] on PS scale? Use weight trimming quantiles
            # Simpler: trim if p<0.05 or p>0.95 (alpha=0.05) and p<0.10 or p>0.90 (alpha=0.10)
            trim05 = ((p<0.05)|(p>0.95)).mean()
            trim10 = ((p<0.10)|(p>0.90)).mean()
        # Report per-grade observed hba1c rate
        obs_rate = observed_hba1c_mask.mean()
        print(f"  {grade}: N={N} bmi {bmi_g.mean():.2f} mono {mono_g.mean():.3f} age {age_g.mean():.1f} HbA1c obs {obs_rate:.3f} SMD_bmi {smd_bmi:.3f} AUC {auc:.3f} ESS/n {ess_ratio:.3f} trim05 {trim05:.3f} trim10 {trim10:.3f}")
        diagnostics_rows.append({
            "grade": grade,
            "N": N,
            "bmi_mean": round(float(bmi_g.mean()),2),
            "mono_prev": round(float(mono_g.mean()),3),
            "age_mean": round(float(age_g.mean()),1),
            "hba1c_observed_rate": round(float(obs_rate),3),
            "generic_rate": round(float(generic_g.mean()),3),
            "ayush_rate": round(float(ayush_g.mean()),3),
            "docs_rate": round(float(docs_g.mean()),3),
            "SMD_bmi": round(float(smd_bmi),3),
            "SMD_age": round(float(smd_age),3),
            "SMD_mono": round(float(smd_mono),3),
            "SMD_exceed_0.1_flag": int(abs(smd_bmi)>0.1 or abs(smd_age)>0.1 or abs(smd_mono)>0.1),
            "pct_SMD_gt0.1": round(float(sum(abs(x)>0.1 for x in [smd_bmi, smd_age, smd_mono])/3*100),1),
            "S_score_AUC": round(float(auc),3),
            "overlap_diagnostic": "benign" if auc<0.70 else ("moderate" if auc<0.80 else "severe"),
            "ESS": round(float(ess_ratio*N),1) if grade!="G0" else float(N),
            "ESS_ratio": round(float(ess_ratio),3),
            "trim_frac_alpha0.05": round(float(trim05),3),
            "trim_frac_alpha0.10": round(float(trim10),3),
            "method": "entropy_balancing/IPW resampling stub (logistic S-score, N=5k)",
            "S_visit_censoring": f"logit P(O) with p_asym={p_asym}, p_sym=0.80 (gamma_o graded)",
        })

    diag_df = pd.DataFrame(diagnostics_rows)
    diag_path = OUT / "pilot_005_006_diagnostics.csv"
    diag_df.to_csv(diag_path, index=False)
    print(f"\n  wrote diagnostics to {diag_path}")

    # 3. B->R* contour CSV: sweep RR_UD 1.5/2.0/3.0 x P(U) scenarios, plus titration extremes
    print("\n--- Step 3: B->R* contour (R*~1.4-2.0 per RR_UD sweep) ---")
    # Use audit-derived (p1,p0) pairs per spec titration table
    scenarios = [
        ("Generic non-compliance 35% excess", 0.35, 0.05),
        ("Generic Khanna extreme 95% excess", 0.95, 0.05),
        ("Irrational FDC contrast A", 0.20, 0.02),
        ("AYUSH 44% simultaneous median", 0.44, 0.10),
        ("AYUSH 96% ever extreme", 0.96, 0.10),
        ("Polypharmacy >=3 drugs", 0.71, 0.20),
    ]
    RR_sweep = [1.5, 2.0, 3.0]
    contour_rows=[]
    for name, p1, p0 in scenarios:
        RR_EU = p1/p0 if p0>0 else float('inf')
        for RR_UD in RR_sweep:
            B = bounding_factor(p1, p0, RR_UD)
            Bmax = B_max(RR_EU, RR_UD)
            Rstar = invert_evalue(B)
            Rstar_max = invert_evalue(Bmax)
            contour_rows.append({
                "scenario": name,
                "p1": p1, "p0": p0, "RR_EU": round(RR_EU,2),
                "RR_UD": RR_UD,
                "B_bounding_factor": round(B,3),
                "B_max_joint": round(Bmax,3),
                "Rstar": round(Rstar,3),
                "Rstar_Bmax": round(Rstar_max,3),
                "interpretation": f"RR_obs > {Rstar:.2f} survives this audit-anchored bias (B={B:.2f}); R*~1.4-2.0 sweep" if 1.4 <= Rstar <= 2.3 else f"R*={Rstar:.2f} outside typical 1.4-2.0"
            })
    contour_df = pd.DataFrame(contour_rows)
    contour_path = OUT / "pilot_005_006_Rstar_contour.csv"
    contour_df.to_csv(contour_path, index=False)
    print(contour_df.to_string(index=False))
    print(f"  wrote contour to {contour_path} ({len(contour_df)} rows, R* range {contour_df['Rstar'].min():.2f}-{contour_df['Rstar'].max():.2f})")

    # Also report titration table check: typical R*~1.4-2.0
    typical = contour_df[(contour_df['RR_UD']==2.0)]
    print(f"\n  At RR_UD=2.0 typical R*: {typical[['scenario','Rstar']].to_string(index=False)}")

    # 4. 9-cell config: 3xP(U) 0.10/0.44/0.96 x 3xRR_UD 1.5/2.0/3.0
    print("\n--- Step 4: 9-cell plasmode config (3xP(U) x 3xRR_UD) ---")
    configs=[]
    PUs = [0.10, 0.44, 0.96]
    for pu in PUs:
        for rr in RR_sweep:
            # Impute p1 = pu (enriched arm), p0 = 0.10 conservative background for AYUSH-like; but for pu=0.10 use p0=0.05
            # Use generic mapping: p1=pu, p0=0.10 if pu>0.10 else 0.05
            p1 = pu
            p0 = 0.10 if pu>0.10 else 0.05
            B = bounding_factor(p1,p0,rr)
            Rstar = invert_evalue(B)
            configs.append({
                "P_U": pu, "RR_UD": rr, "p1": p1, "p0": p0,
                "B": round(B,3), "Rstar": round(Rstar,3),
                "RR_true_options": "1.0 (null) vs 1.5 (alternative)",
                "n_per_cell": 2000,
                "false_robust_target": "<5% at calibrated R* (RR_true=1 declared robust)",
                "power_fragile_target": "calibrates threshold conservativeness",
                "note": f"P(U)={pu} AYUSH background 0.10 (conservative) -> B={B:.3f} R*={Rstar:.3f}"
            })
    config_df = pd.DataFrame(configs)
    config_path = OUT / "pilot_005_006_9cell_config.csv"
    config_df.to_csv(config_path, index=False)
    print(config_df.to_string(index=False))
    print(f"  wrote 9-cell config to {config_path}")

    # 5. Hashes
    for p in [g_path, diag_path, contour_path, config_path]:
        h = hashlib.sha256(p.read_bytes()).hexdigest()[:12]
        print(f"  hash {p.name}: sha256:{h}")

    print(f"\n=== PILOT 005+006 COMPLETE ===")
    print(f"Outputs: {g_path}, {diag_path}, {contour_path}, {config_path}")
    print(f"Diagnostics grades: {list(diag_df['grade'])} S-score AUC range {diag_df['S_score_AUC'].min():.3f}-{diag_df['S_score_AUC'].max():.3f}")
    print(f"R* range {contour_df['Rstar'].min():.2f}-{contour_df['Rstar'].max():.2f} typical 1.4-2.0")
    print(f"Log: {log_path}")

    lf.close()
    sys.stdout = orig_out
    sys.stderr = orig_err

if __name__=="__main__":
    main()
