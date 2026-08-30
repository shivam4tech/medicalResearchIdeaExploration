#!/usr/bin/env python3
"""
Pilot 002: synthEHRella S1–S5 2-point ladder (synthetic fallback)
- Synthetic 5k rows 10 numeric + 5 categorical + binary outcome
- S1 bootstrap resample vs S5 prevalence-random (trivial)
- Fidelity: MMD (max prevalence gap), correlation Frobenius, discriminative AUC
- Utility: logistic vs tree TSTR vs TRTR on held-out real TEST_R
- Kendall tau + Spearman over methods, DCA net benefit at 10/20%
"""
import numpy as np
import pandas as pd
from scipy.stats import kendalltau, spearmanr
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.model_selection import train_test_split

SEED = 20260830
rng = np.random.default_rng(SEED)
N = 5000
print(f"[Pilot002] SEED={SEED} N={N} fallback=SYNTHETIC (MIMIC-III demo not credentialed - honest fallback)")

# --- synthetic tabular fallback ---
# 10 numeric
num_names = [f"num{i}" for i in range(10)]
cat_names = [f"cat{i}" for i in range(5)]
# correlated numeric block
mean = np.zeros(10)
cov = 0.3*np.ones((10,10)) + 0.7*np.eye(10)
X_num = rng.multivariate_normal(mean, cov, size=N)
# shift/scale to plausible
X_num = X_num*2 + rng.normal(0,0.5,size=(N,10))
# 5 categorical: 3 levels each
X_cat = np.column_stack([rng.integers(0,3,size=N) for _ in range(5)])
# outcome: logistic of linear combo
logit = 0.8*X_num[:,0] -0.5*X_num[:,1] +0.6*X_num[:,2] + 0.4*(X_cat[:,0]==1) -0.3*(X_cat[:,1]==2) + rng.normal(0,0.8,N)
prob = 1/(1+np.exp(-logit))
y = (rng.random(N) < prob).astype(int)
print(f"[Data] outcome prevalence={y.mean():.3f}")
# assemble full matrix for fidelity (binary encoded cats one-hot-ish -> just use ints scaled + y as column)
# For fidelity: use normalized numeric + cat dummies + y
X_cat_oh = np.eye(3)[X_cat.reshape(-1)].reshape(N, -1)  # N x 15
full_real = np.hstack([X_num, X_cat_oh, y[:,None]])
print(f"[Data] full_real shape {full_real.shape}")

# train/test split 80/20 stratified
idx = np.arange(N)
train_idx, test_idx = train_test_split(idx, test_size=0.2, random_state=SEED, stratify=y)
real_train = full_real[train_idx]
real_test = full_real[test_idx]
# for utility: features vs label
# reconstruct feature matrix for modeling: use X_num + X_cat_oh as X, y as label
def split_Xy(full):
    X = full[:,:-1]
    y_ = full[:,-1].astype(int)
    return X, y_
X_real_train, y_real_train = split_Xy(real_train)
X_real_test, y_real_test = split_Xy(real_test)
print(f"[Split] train {len(train_idx)} test {len(test_idx)}")

# --- S1 bootstrap (plasmode resample) ---
np.random.seed(SEED)
S1 = real_train[rng.integers(0, len(real_train), size=len(real_train))]
print(f"[S1] bootstrap shape {S1.shape}")

# --- S5 prevalence-random (independent Bernoulli per column with p=col mean) ---
p_ones = real_train.mean(axis=0)  # prevalence per column
# clip for binary-like columns; for continuous numeric this is weird but we follow spec: prevalence-random = independent per dim
# For fallback: treat every column as continuous? We'll do Bernoulli for binarized version, else Gaussian approx
# Simpler: for each column sample Bernoulli(p) then scale? But numeric cols mean not in [0,1]. Use Gaussian sampling per col mean/sd instead for numeric, Bernoulli for binary cols
# Heuristic: first 10 cols are numeric (continuous) -> sample N(mean, sd); remaining are binary 0/1 -> Bernoulli
numeric_means = real_train[:,:10].mean(axis=0)
numeric_stds = real_train[:,:10].std(axis=0) + 1e-6
binary_ps = real_train[:,10:].mean(axis=0)
S5_numeric = rng.normal(numeric_means, numeric_stds, size=(len(real_train),10))
S5_binary = np.column_stack([rng.binomial(1, p, size=len(real_train)) for p in binary_ps])
S5 = np.hstack([S5_numeric, S5_binary])
print(f"[S5] prevalence-random shape {S5.shape} (numeric Gaussian + binary Bernoulli)")

# --- fidelity metrics ---
def compute_prevalence(data): return data.mean(axis=0)
def compute_correlation(data):
    d = data.astype(float).copy()
    for i in range(d.shape[1]):
        if len(np.unique(d[:,i]))==1:
            d[:,i]+= rng.normal(0,1e-6,d.shape[0])
    return np.corrcoef(d, rowvar=False)

def mmd_prevalence(real, synth):
    return np.abs(compute_prevalence(real)-compute_prevalence(synth)).max()

def rmspe(real, synth):
    rp = compute_prevalence(real); sp = compute_prevalence(synth)
    # avoid div by zero
    mask = np.abs(rp)>1e-9
    return np.sqrt(np.mean(((rp[mask]-sp[mask])/rp[mask])**2))

def corr_fro(real, synth):
    return np.linalg.norm(compute_correlation(real)-compute_correlation(synth), 'fro')

def discriminative_auc(real, synth):
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import KFold
    data = np.vstack((real, synth))
    labels = np.hstack((np.ones(len(real)), np.zeros(len(synth))))
    kf = KFold(n_splits=5, shuffle=True, random_state=SEED)
    aucs=[]
    for tr, te in kf.split(data):
        m=LogisticRegression(max_iter=1000); m.fit(data[tr], labels[tr]); prob=m.predict_proba(data[te])[:,1]; aucs.append(roc_auc_score(labels[te], prob))
    return np.mean(aucs)

fidelity_rows=[]
for name, synth in [("S1_bootstrap", S1), ("S5_prevalence_random", S5)]:
    mmd = mmd_prevalence(real_train, synth)
    cfro = corr_fro(real_train, synth)
    disc_auc = discriminative_auc(real_train, synth)
    rmsp = rmspe(real_train, synth)
    fidelity_rows.append({"method":name,"mmd_max_gap":mmd,"rmspe":rmsp,"corr_fro":cfro,"discriminative_auc":disc_auc})
    print(f"[Fidelity {name}] mmd={mmd:.4f} rmspe={rmsp:.4f} corr_fro={cfro:.4f} disc_auc={disc_auc:.4f}")

# --- utility: TSTR vs TRTR ---
def train_eval(Xtr, ytr, Xte, yte, model_type="logistic"):
    if model_type=="logistic":
        m=LogisticRegression(max_iter=1000)
    elif model_type=="tree":
        m=DecisionTreeClassifier(max_depth=5, random_state=SEED)
    elif model_type=="rf":
        m=RandomForestClassifier(n_estimators=100, random_state=SEED)
    else: raise ValueError(model_type)
    # flip if single class
    if len(np.unique(ytr))==1:
        ytr = ytr.copy(); ytr[0]=1-ytr[0]
    m.fit(Xtr, ytr)
    prob=m.predict_proba(Xte)[:,1]
    return {"auc": roc_auc_score(yte, prob), "acc": accuracy_score(yte, (prob>0.5).astype(int)), "prob": prob}

# TRTR (real->real)
trtr_log = train_eval(X_real_train, y_real_train, X_real_test, y_real_test, "logistic")
trtr_tree = train_eval(X_real_train, y_real_train, X_real_test, y_real_test, "tree")
print(f"[TRTR] logistic auc={trtr_log['auc']:.4f} tree auc={trtr_tree['auc']:.4f}")

# TSTR S1
X_S1, y_S1 = split_Xy(S1)
tstr_S1_log = train_eval(X_S1, y_S1, X_real_test, y_real_test, "logistic")
tstr_S1_tree = train_eval(X_S1, y_S1, X_real_test, y_real_test, "tree")
print(f"[TSTR S1] logistic auc={tstr_S1_log['auc']:.4f} tree auc={tstr_S1_tree['auc']:.4f}")

# TSTR S5
X_S5, y_S5 = split_Xy(S5)
tstr_S5_log = train_eval(X_S5, y_S5, X_real_test, y_real_test, "logistic")
tstr_S5_tree = train_eval(X_S5, y_S5, X_real_test, y_real_test, "tree")
print(f"[TSTR S5] logistic auc={tstr_S5_log['auc']:.4f} tree auc={tstr_S5_tree['auc']:.4f}")

# --- Kendall tau over methods ranking ---
# Real ranking: sort methods by TRTR auc
# Synthetic ranking: sort by TSTR auc per synthetic method
# We have 2 methods -> tau is 1 if concordant, -1 if discordant
def ranking_tau(real_scores, synth_scores):
    # real_scores, synth_scores dict method->auc
    methods = list(real_scores.keys())
    real_rank = np.argsort([-real_scores[m] for m in methods])
    synth_rank = np.argsort([-synth_scores[m] for m in methods])
    # map to rank positions
    real_order = [methods[i] for i in real_rank]
    synth_order = [methods[i] for i in synth_rank]
    # For 2 methods, kendall tau
    # Convert to rank vectors
    r_real = [real_order.index(m) for m in methods]
    r_synth = [synth_order.index(m) for m in methods]
    tau, p = kendalltau(r_real, r_synth)
    rho, _ = spearmanr(r_real, r_synth)
    # handle tau nan when n=2 and tied?
    return tau, rho, real_order, synth_order

real_scores = {"logistic": trtr_log["auc"], "tree": trtr_tree["auc"]}
s1_scores = {"logistic": tstr_S1_log["auc"], "tree": tstr_S1_tree["auc"]}
s5_scores = {"logistic": tstr_S5_log["auc"], "tree": tstr_S5_tree["auc"]}
tau_S1, rho_S1, ro_S1, so_S1 = ranking_tau(real_scores, s1_scores)
tau_S5, rho_S5, ro_S5, so_S5 = ranking_tau(real_scores, s5_scores)
print(f"[Tau S1] tau={tau_S1:.4f} rho={rho_S1:.4f} real_order={ro_S1} synth_order={so_S1}")
print(f"[Tau S5] tau={tau_S5:.4f} rho={rho_S5:.4f} real_order={ro_S5} synth_order={so_S5}")

# --- DCA net benefit at 10%,20% ---
def net_benefit(y_true, y_prob, pt):
    # NB = TP/N - FP/N * pt/(1-pt)
    y_pred = (y_prob >= pt).astype(int)
    TP = ((y_pred==1)&(y_true==1)).sum()
    FP = ((y_pred==1)&(y_true==0)).sum()
    N_ = len(y_true)
    return TP/N_ - FP/N_ * (pt/(1-pt))

def dca_row(probs_dict, label):
    rows=[]
    for pt in [0.10, 0.20]:
        for m, prob in probs_dict.items():
            nb = net_benefit(y_real_test, prob, pt)
            # also treat-all, treat-none
            rows.append({"label":label, "method":m, "pt":pt, "net_benefit":nb})
        # treat-all NB
        # treat_all: predict everyone positive
        nb_all_10 = y_real_test.mean() - (1-y_real_test.mean())*(0.10/0.90) if 0.10!=1 else 0
        # computed via formula using all positive: TP = prevalence, FP=1-prevalence
        # We'll compute directly but also add rows for reference
    return rows

# collect probs for DCA
probs_trtr = {"logistic": trtr_log["prob"], "tree": trtr_tree["prob"]}
probs_S1 = {"logistic": tstr_S1_log["prob"], "tree": tstr_S1_tree["prob"]}
probs_S5 = {"logistic": tstr_S5_log["prob"], "tree": tstr_S5_tree["prob"]}
dca_rows=[]
for label, probs in [("TRTR", probs_trtr), ("TSTR_S1", probs_S1), ("TSTR_S5", probs_S5)]:
    for pt in [0.10, 0.20]:
        for m, prob in probs.items():
            nb = net_benefit(y_real_test, prob, pt)
            dca_rows.append({"train":label, "method":m, "pt":pt, "net_benefit":nb})
# add treat-all/none reference
prev = y_real_test.mean()
for pt in [0.10, 0.20]:
    nb_all = prev - (1-prev)*(pt/(1-pt))
    dca_rows.append({"train":"treat_all", "method":"all", "pt":pt, "net_benefit":nb_all})
    dca_rows.append({"train":"treat_none", "method":"none", "pt":pt, "net_benefit":0.0})
for r in dca_rows: print(f"[DCA] {r}")

# --- Save outputs ---
fid_df = pd.DataFrame(fidelity_rows)
# add tau
tau_df = pd.DataFrame([
    {"synth_method":"S1_bootstrap","kendall_tau":tau_S1,"spearman_rho":rho_S1,"concordant":int(tau_S1==1),"real_order":">".join(ro_S1),"synth_order":">".join(so_S1)},
    {"synth_method":"S5_prevalence_random","kendall_tau":tau_S5,"spearman_rho":rho_S5,"concordant":int(tau_S5==1),"real_order":">".join(ro_S5),"synth_order":">".join(so_S5)},
])
# DCA
dca_df = pd.DataFrame(dca_rows)
# utility gaps
util_rows=[]
for name, auc_log, auc_tree in [("TRTR",trtr_log["auc"],trtr_tree["auc"]),("TSTR_S1",tstr_S1_log["auc"],tstr_S1_tree["auc"]),("TSTR_S5",tstr_S5_log["auc"],tstr_S5_tree["auc"])]:
    util_rows.append({"train":name,"logistic_auc":auc_log,"tree_auc":auc_tree,"winner":"logistic" if auc_log>auc_tree else "tree","delta_auc":abs(auc_log-auc_tree)})
util_df = pd.DataFrame(util_rows)

# Merge fidelity+tau into one pilot file per spec
out = fid_df.merge(tau_df, left_on="method", right_on="synth_method", how="outer")
out["mmd"] = out["mmd_max_gap"]
out["fidelity_composite"] = 1/(1+out["corr_fro"])  # simple
# Save
out.to_csv("outputs/pilot_002_fidelity_tau.csv", index=False)
print(out.to_string(index=False))
dca_df.to_csv("outputs/pilot_002_dca.csv", index=False)
util_df.to_csv("outputs/pilot_002_utility.csv", index=False)
print("[Saved] outputs/pilot_002_fidelity_tau.csv")
print("[Saved] outputs/pilot_002_dca.csv")
print("[Saved] outputs/pilot_002_utility.csv")

# --- calibration plot stub (data for plot) ---
# bin predictions and compute observed rate
def calibration_bins(y_true, y_prob, n_bins=10):
    bins = np.linspace(0,1,n_bins+1)
    rows=[]
    for i in range(n_bins):
        mask = (y_prob>=bins[i])&(y_prob<bins[i+1]) if i<n_bins-1 else (y_prob>=bins[i])&(y_prob<=bins[i+1])
        if mask.sum()==0: continue
        rows.append({"bin":i,"bin_low":bins[i],"bin_high":bins[i+1],"mean_pred":y_prob[mask].mean(),"obs_rate":y_true[mask].mean(),"n":int(mask.sum())})
    return pd.DataFrame(rows)

for name, probs in [("TRTR_logistic",trtr_log["prob"]),("TSTR_S1_logistic",tstr_S1_log["prob"]),("TSTR_S5_logistic",tstr_S5_log["prob"])]:
    df = calibration_bins(y_real_test, probs, 10)
    df.to_csv(f"outputs/pilot_002_calibration_{name}.csv", index=False)
    print(f"[Calibration {name}] {df.head(3).to_dict(orient='records')}")

print("[Done] Pilot002 complete - honest synthetic fallback, 5k rows, S1 vs S5 2-point ladder")
