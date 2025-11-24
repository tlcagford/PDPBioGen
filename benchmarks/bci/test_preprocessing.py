# quick runner for bci smoke tests
import pytest, sys
sys.exit(pytest.main(["-q", "benchmarks/bci/test_preprocessing.py::test_preprocess_epoch_and_hash",
                      "benchmarks/bci/test_feature_extraction.py::test_feature_psd"]))

# benchmarks/bci/test_preprocessing.py (simplified)
import hashlib
import mne
import numpy as np
from pathlib import Path

SAMPLE = Path("benchmarks/bci/sample_data/eegmmidb_subject1.edf")
GOLD_HASH = "sha256:abcd1234..."  # set after generating once

def compute_file_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()

def test_preprocess_epoch_and_hash(tmp_path):
    raw = mne.io.read_raw_edf(SAMPLE, preload=True, verbose=False)
    # deterministic filter
    raw.filter(1.0, 40.0, method="fir", fir_design="firwin")
    raw.set_eeg_reference("average", projection=False)
    epochs = mne.make_fixed_length_epochs(raw, duration=2.0, preload=True)
    out = tmp_path / "features.npy"
    np.save(out, epochs.get_data())
    got = compute_file_hash(out)
    assert got == GOLD_HASH
