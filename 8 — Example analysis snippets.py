import numpy as np
from scipy import signal, stats
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# Assume windows_nv: (n_trials, n_samples) and windows_classical same shape
def compute_snr(windows, pre_samples):
    # baseline = mean energy in pre-stim region
    n_trials = windows.shape[0]
    snrs = []
    for i in range(n_trials):
        sig = windows[i]
        baseline = np.mean(sig[:pre_samples]**2)
        signal_energy = np.mean(sig[pre_samples:]**2)
        snr = 10*np.log10(signal_energy / baseline)
        snrs.append(snr)
    return np.array(snrs)

# matched-filter detection scores:
def matched_filter_score(windows, template):
    scores = [np.max(np.abs(np.convolve(win, template[::-1], mode='same'))) for win in windows]
    return np.array(scores)

# Compute ROC/AUC
scores_nv = matched_filter_score(windows_nv, template)
labels = np.array([...])  # 1 for signal trials, 0 for null
auc_nv = roc_auc_score(labels, scores_nv)

# Compare AUC across sensors (bootstrap)
def bootstrap_auc(scores1, scores2, labels, nboot=2000):
    diffs = []
    n = len(labels)
    for _ in range(nboot):
        idx = np.random.choice(n, n, replace=True)
        a1 = roc_auc_score(labels[idx], scores1[idx])
        a2 = roc_auc_score(labels[idx], scores2[idx])
        diffs.append(a1 - a2)
    diffs = np.array(diffs)
    p = np.mean(diffs <= 0)  # one-sided test NV > classical
    return np.mean(diffs), np.percentile(diffs, [2.5,97.5]), p

mean_diff, ci, pval = bootstrap_auc(scores_nv, scores_classical, labels)
print("AUC diff", mean_diff, ci, "p", pval)
