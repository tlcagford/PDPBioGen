# src/adapters/eeg_adapter.py
"""EEG adapter: provides a simple interface to obtain time-series.
- If `mne` is installed and an EDF/RAW file path is provided, it will load data.
- Otherwise falls back to the simulator generator.
"""
try:
    import mne
    _HASMNE = True
except Exception:
    _HASMNE = False

from pdpbiogen.simulator import generate_bci
import numpy as np

def load_eeg_from_file(path, picks=None, preload=True):
    if not _HASMNE:
        raise RuntimeError('mne not available in this environment. Install mne or use simulated mode.')
    raw = mne.io.read_raw(path, preload=preload, verbose=False)
    data, times = raw[:]
    if picks is not None:
        data = raw.copy().pick_channels(picks).get_data()
    # Flatten to single channel by averaging for this demo
    sig = np.mean(data, axis=0)
    return times, sig

def get_eeg_stream(duration_s=30, fs=128, file_path=None):
    """Returns (t, signal). If file_path is given and mne available, loads real data; otherwise uses simulator."""
    if file_path is not None and _HASMNE:
        return load_eeg_from_file(file_path)
    return generate_bci(duration_s, fs)
