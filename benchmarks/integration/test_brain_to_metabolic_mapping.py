import numpy as np
from pathlib import Path
import pandas as pd

EEG_SAMPLE = Path("benchmarks/bci/sample_data/eegmmidb_subject1.edf")
MET_SAMPLE = Path("benchmarks/metabolomics/sample_data/metabolomics_small.tsv")

def deterministic_feature_from_eeg(seed=42, nfeatures=32):
    rs = np.random.RandomState(seed)
    return rs.rand(nfeatures)

def brain_to_metabolic_model(eeg_features):
    # very small deterministic mapping used for smoke-tests
    W = np.arange(len(eeg_features)*2).reshape(len(eeg_features), 2) * 0.001
    return eeg_features.dot(W)

def test_brain_to_metabolic_mapping_smoke():
    assert EEG_SAMPLE.exists()
    eeg_features = deterministic_feature_from_eeg()
    meta_pred = brain_to_metabolic_model(eeg_features)
    assert meta_pred.shape[1] == 2
    # deterministic check
    meta_pred2 = brain_to_metabolic_model(deterministic_feature_from_eeg())
    assert np.allclose(meta_pred, meta_pred2)
