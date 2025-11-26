"""
dpbiogen.quantum.healing_sim
Deterministic prototype pipeline:
EEG (EDF) -> deterministic EEG features -> surrogate gene-expression delta ->
apply to a COBRA model and run FBA -> return flux deltas.

Requirements (add to environment.yml / Docker):
  - mne
  - numpy, pandas
  - cobra (COBRApy)
  - scipy
"""

from pathlib import Path
import json, hashlib, os
import numpy as np
import pandas as pd

# External libs (import lazily to avoid failing if not installed)
def import_mne():
    import mne
    return mne

def import_cobra():
    import cobra
    return cobra

# ---------------------
# Utility functions
# ---------------------
def sha256_file(path: Path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def save_json(obj, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as fh:
        json.dump(obj, fh, indent=2)

# ---------------------
# EEG loader + deterministic preprocessing
# ---------------------
def load_eeg_edf(edf_path: str, picks=None):
    """
    Load EDF via MNE with deterministic processing.
    Returns raw object.
    """
    mne = import_mne()
    raw = mne.io.read_raw_edf(edf_path, preload=True, verbose=False)
    # deterministic filter and referencing
    raw.filter(1.0, 40.0, method='fir', fir_design='firwin')
    raw.set_eeg_reference('average', projection=False)
    return raw

def eeg_to_features(raw, sfreq_target=128, n_features=64, seed=42):
    """
    Deterministic feature extraction:
      - downsample to sfreq_target
      - compute bandpower in canonical bands per channel and flatten
      - reduce to n_features with deterministic PCA-like projection (SVD with fixed seed)
    """
    # get data
    data = raw.get_data(picks='eeg')  # (n_channels, n_times)
    # resample deterministically
    raw_res = raw.copy().resample(sfreq_target)
    data = raw_res.get_data()
    # compute simple bandpowers per channel for delta/theta/alpha/beta/gamma
    bands = [(1,4),(4,8),(8,12),(12,30),(30,45)]
    bp = []
    from scipy.signal import welch
    for ch in range(data.shape[0]):
        f, Pxx = welch(data[ch], fs=raw_res.info['sfreq'], nperseg=int(raw_res.info['sfreq']*2))
        for (lo,hi) in bands:
            mask = (f>=lo)&(f<=hi)
            bp.append(Pxx[mask].mean())
    bp = np.array(bp)  # shape (n_channels * n_bands,)
    # deterministic projection to n_features via randomized SVD with fixed seed
    rs = np.random.RandomState(seed)
    # create deterministic projection matrix via seeded normal
    proj = rs.normal(size=(bp.size, n_features))
    feats = bp.dot(proj)  # shape (n_features,)
    # normalize
    feats = (feats - feats.mean()) / (feats.std() + 1e-12)
    return feats

# ---------------------
# Surrogate mapping: EEG features -> gene expression delta
# ---------------------
def features_to_gene_delta(feats, ngenes=200, seed=0):
    """
    Deterministic mapping: linear projection + tanh nonlinear to keep values bounded.
    """
    rs = np.random.RandomState(seed)
    W = rs.normal(scale=0.01, size=(feats.size, ngenes))
    delta = np.tanh(feats.dot(W))  # between -1 and 1
    # scale to plausible fold-change-like values (log2 scale small)
    # interpret as small log2 fold changes
    log2fc = delta * 0.5  # up to +/-0.5 log2 fold-change
    return log2fc  # length ngenes

# ---------------------
# Apply gene delta to COBRA model (simple deterministic mapping)
# ---------------------
def apply_gene_delta_to_model(cobra_model, gene_list, log2fc, base_expression=None):
    """
    gene_list: list of gene IDs aligned with log2fc
    base_expression: optional baseline expression dict {gene: value}
    We implement a naive mapping: low expression reduces upper bounds of reactions associated with that gene.
    For real models use GPR parsing; here we use a lightweight approach for prototyping.
    """
    # Build gene->score mapping
    gene_score = {g: float(fc) for g, fc in zip(gene_list, log2fc)}
    # Apply: for every reaction, if it has genes, compute min gene score and scale flux bounds.
    for rxn in cobra_model.reactions:
        genes = [g.id for g in rxn.genes] if hasattr(rxn, 'genes') else []
        if not genes:
            continue
        # compute a factor in (0.2, 1.5) from gene scores
        vals = [gene_score.get(g, 0.0) for g in genes]
        mean_fc = float(np.mean(vals)) if vals else 0.0
        factor = 1.0 + (mean_fc)  # mean_fc is in -0.5..0.5 -> factor in 0.5..1.5
        # Clip factor to avoid runaway
        factor = max(0.2, min(2.0, factor))
        # apply to bounds deterministically (scale upper and lower)
        # skip blocked/unbounded reactions
        if rxn.upper_bound is not None and np.isfinite(rxn.upper_bound):
            rxn.upper_bound = rxn.upper_bound * factor
        if rxn.lower_bound is not None and np.isfinite(rxn.lower_bound):
            rxn.lower_bound = rxn.lower_bound * factor
    return cobra_model

# ---------------------
# Run flux-balance analysis & return key flux changes
# ---------------------
def run_fba_and_report(cobra_model, baseline_solution=None):
    cobra = import_cobra()
    # get baseline if not provided
    if baseline_solution is None:
        baseline_solution = cobra_model.optimize()
    # run FBA on current model
    sol = cobra_model.optimize()
    # compare objective and a few reaction fluxes
    report = {
        "objective_baseline": float(baseline_solution.objective_value) if baseline_solution is not None else None,
        "objective_changed": float(sol.objective_value),
    }
    # pick top N reactions by absolute change
    diffs = {}
    for rxn in cobra_model.reactions:
        r_id = rxn.id
        v_before = float(baseline_solution.fluxes.get(r_id, 0.0)) if baseline_solution is not None else 0.0
        v_after = float(sol.fluxes.get(r_id, 0.0))
        diffs[r_id] = v_after - v_before
    # sort by absolute change
    top = sorted(diffs.items(), key=lambda kv: abs(kv[1]), reverse=True)[:20]
    report['top_flux_changes'] = top
    return report

# ---------------------
# Orchestration function
# ---------------------
def run_healing_sim(eeg_path: str,
                    cobra_sbml_path: str,
                    gene_list: list = None,
                    outdir: str = "results/healing_sim",
                    seed: int = 42):
    """
    Run the full deterministic pipeline:
      - load EEG
      - extract features
      - map to gene delta
      - load COBRA model and apply delta
      - run FBA
      - save artifacts and manifest
    Returns manifest dictionary.
    """
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    # Step 1: EEG -> features
    raw = load_eeg_edf(eeg_path)
    feats = eeg_to_features(raw, seed=seed, n_features=64)
    feats_path = outdir / "eeg_features.npy"
    np.save(feats_path, feats)
    feats_hash = sha256_file(feats_path)

    # Step 2: mapping -> gene delta
    if gene_list is None:
        # generate synthetic gene list
        ng = 200
        gene_list = [f"GENE{i:05d}" for i in range(ng)]
    log2fc = features_to_gene_delta(feats, ngenes=len(gene_list), seed=seed+1)
    gene_delta_df = pd.DataFrame({"gene": gene_list, "log2fc": log2fc})
    gene_delta_path = outdir / "gene_delta.tsv"
    gene_delta_df.to_csv(gene_delta_path, sep="\t", index=False)
    gene_hash = sha256_file(gene_delta_path)

    # Step 3: load COBRA model
    cobra = import_cobra()
    model = cobra.io.read_sbml_model(cobra_sbml_path)

    # Step 4: baseline solution
    baseline = model.optimize()

    # Step 5: apply delta
    model_mod = apply_gene_delta_to_model(model, gene_list, log2fc)

    # Step 6: run FBA & report
    report = run_fba_and_report(model_mod, baseline_solution=baseline)
    manifest = {
        "feats_path": str(feats_path),
        "feats_hash": feats_hash,
        "gene_delta_path": str(gene_delta_path),
        "gene_delta_hash": gene_hash,
        "fba_report": report
    }
    save_json(manifest, outdir / "manifest.json")
    return manifest
