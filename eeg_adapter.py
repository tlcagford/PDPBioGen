import numpy as np
import mne

def load_real_eeg(path):
    raw = mne.io.read_raw_edf(path, preload=True)
    raw.filter(1, 40)
    data = raw.get_data()[0]
    return data

def extract_eeg_features(data, fs=250):
    # alpha/beta + entropy
    fft = np.abs(np.fft.rfft(data))
    alpha = np.mean(fft[10:14])
    beta = np.mean(fft[20:25])
    ratio = alpha / (beta + 1e-6)
    entropy = -np.sum((data**2) * np.log(data**2 + 1e-6))
    return np.array([ratio, entropy])
