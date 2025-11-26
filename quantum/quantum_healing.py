"""
pdpbiogen.quantum.quantum_healing
Deterministic, non-clinical simulation mapping EEG -> gene fold-changes + metabolite shifts.

NOT MEDICAL: purely for hypothesis generation and reproducibility testing.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import json
import hashlib
import logging

logger = logging.getLogger("pdpbiogen.quantum.quantum_healing")
logging.basicConfig(level=logging.INFO)

DEFAULT_SEED = 20251126  # pick a fixed seed for determinism

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def load_eeg_features(eeg_data: np.ndarray, sfreq: float, seed: int = DEFAULT_SEED):
    """
    Deterministic EEG feature
::contentReference[oaicite:0]{index=0}
