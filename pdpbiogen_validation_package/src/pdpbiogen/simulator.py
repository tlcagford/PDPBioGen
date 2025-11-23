import numpy as np
from scipy.signal import fftconvolve

def generate_phantom_pulse(fs, duration_ms=5, shape='bipolar', amplitude_pT=1.0):
    n = max(1, int(fs * duration_ms / 1000.0))
    t = np.linspace(0, duration_ms/1000.0, n, endpoint=False)
    if shape == 'bipolar':
        sig = amplitude_pT * (np.sin(2*np.pi*200*t) * np.exp(-50*t))
    else:
        sig = amplitude_pT * np.exp(-50*t)
    return t, sig

def generate_phantom_trials(fs=5000, amplitudes=[0.1,0.2,0.5,1.0,2.0], n_trials=60, pre_ms=50, post_ms=200):
    trials = []
    labels = []
    pre = int(fs*pre_ms/1000.0)
    post = int(fs*post_ms/1000.0)
    win_len = pre + post
    for A in amplitudes:
        for _ in range(n_trials):
            seg = np.zeros(win_len)
            t_sig, sig = generate_phantom_pulse(fs, duration_ms=5, amplitude_pT=A)
            seg[pre:pre+len(sig)] += sig
            t = np.linspace(0, (win_len-1)/fs, win_len)
            trials.append((t, seg))
            labels.append(1)
    # add null trials
    for _ in range(len(trials)//2):
        win_len = pre + post
        seg = np.zeros(win_len)
        t = np.linspace(0, (win_len-1)/fs, win_len)
        trials.append((t, seg))
        labels.append(0)
    idx = np.random.permutation(len(trials))
    trials = [trials[i] for i in idx]
    labels = [labels[i] for i in idx]
    return trials, np.array(labels)

def matched_filter_scores(windows, template):
    scores = []
    for w in windows:
        c = fftconvolve(w, template[::-1], mode='same')
        scores.append(np.max(np.abs(c)))
    return np.array(scores)
