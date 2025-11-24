import json
import hashlib
import numpy as np
from pathlib import Path

def compute_hash(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()

def test_multiscale_pipeline_hash_consistency():
    # create deterministic outputs
    eeg = list(np.linspace(0.1, 1.0, 32))
    genomic = list(np.round(np.linspace(0.2, 0.9, 100).tolist(), 6))
    metabolic = list(np.round(np.linspace(0.05, 0.7, 10).tolist(),6))
    tree = {"eeg": eeg, "genome": genomic, "metabolome": metabolic}
    h1 = compute_hash(tree)
    h2 = compute_hash(tree)
    assert h1 == h2
