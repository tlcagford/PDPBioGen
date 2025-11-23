import numpy as np
from sklearn.metrics import roc_auc_score

def compute_snr(windows, pre_samples):
    snrs = []
    for w in windows:
        baseline = np.mean(w[:pre_samples]**2) + 1e-12
        signal_energy = np.mean(w[pre_samples:]**2)
        snr = 10 * np.log10(signal_energy / baseline)
        snrs.append(snr)
    return np.array(snrs)

def compute_auc(scores, labels):
    return roc_auc_score(labels, scores)

def bootstrap_auc_diff(scores1, scores2, labels, nboot=2000, seed=1):
    rng = np.random.default_rng(seed)
    n = len(labels)
    diffs = []
    for _ in range(nboot):
        idx = rng.integers(0, n, n)
        a1 = roc_auc_score(labels[idx], scores1[idx])
        a2 = roc_auc_score(labels[idx], scores2[idx])
        diffs.append(a1 - a2)
    diffs = np.array(diffs)
    mean = diffs.mean()
    ci = np.percentile(diffs, [2.5, 97.5])
    p = np.mean(diffs <= 0)
    return mean, ci, p
