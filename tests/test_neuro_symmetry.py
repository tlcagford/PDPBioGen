from dpbiogen.neuro.neuro_symmetry_mapper import NeuroSymmetryMapper
import numpy as np
import mne

def test_symmetry_imports():
    nsm = NeuroSymmetryMapper()
    assert hasattr(nsm, "compute")

def test_entropy():
    nsm = NeuroSymmetryMapper()
    fake = np.random.randn(8, 1000)
    ent = nsm.entropy(fake)
    assert ent > 0

def test_resonance():
    raw = mne.create_info(8, 256, ch_types="eeg")
    data = np.random.randn(8, 2048)
    raw = mne.io.RawArray(data, raw)

    nsm = NeuroSymmetryMapper()
    res = nsm.resonance(raw)
    assert "alpha" in res
