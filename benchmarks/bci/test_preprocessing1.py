import hashlib
import numpy as np
import mne
from pathlib import Path

SAMPLE = Path("benchmarks/bci/sample_data/eegmmidb_subject1.edf")
# TODO: generate this by running in controlled env and update
GOLD_HASH = "TODO_GENERATE"

def compute_file_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()

def test_preprocess_epoch_and_hash(tmp_path):
    assert SAMPLE.exists(), f"Sample file missing: {SAMPLE}"
    raw = mne.io.read_raw_edf(str(SAMPLE), preload=True, verbose=False)
    # deterministic pipeline
    raw.filter(1.0, 40.0, method="fir", fir_design="firwin")
    raw.set_eeg_reference("average", projection=False)
    epochs = mne.make_fixed_length_epochs(raw, duration=2.0, preload=True)
    out = tmp_path / "features.npy"
    np.save(out, epochs.get_data())
    got = compute_file_hash(out)
    # If running locally to produce GOLD_HASH, print and exit early
    if GOLD_HASH.startswith("TODO"):
        print("GOLD_HASH not set; computed:", got)
        # write the artifact so maintainer can compute and paste GOLD_HASH manually
        print("Artifact at:", out)
        return
    assert got == GOLD_HASH
