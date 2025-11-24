import numpy as np
import mne
from pathlib import Path

SAMPLE = Path("benchmarks/bci/sample_data/eegmmidb_subject1.edf")

def bandpower(data, sfreq, band=(8, 12)):
    # simple bandpower estimator using Welch (deterministic)
    from scipy.signal import welch
    f, Pxx = welch(data, fs=sfreq, nperseg=sfreq*2)
    mask = (f >= band[0]) & (f <= band[1])
    return Pxx[:, mask].mean(axis=1)

def test_feature_psd():
    assert SAMPLE.exists()
    raw = mne.io.read_raw_edf(str(SAMPLE), preload=True, verbose=False)
    raw.pick_types(eeg=True)
    data = raw.get_data()
    bp = bandpower(data, raw.info['sfreq'], band=(8,12))
    # sanity checks
    assert bp.ndim == 1
    assert bp.size == data.shape[0]
    # values should be finite
    assert np.isfinite(bp).all()
