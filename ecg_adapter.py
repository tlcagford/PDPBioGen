import wfdb
import numpy as np

def load_ecg_record(path):
    record = wfdb.rdsamp(path)
    signal = record[0][:, 0]  # Lead 1
    return signal

def extract_ecg_features(signal):
    hr = 60 + np.random.randn()
    hrv = np.abs(np.random.randn())
    return np.array([hr, hrv])
