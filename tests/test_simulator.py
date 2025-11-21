import os
from pdpbiogen.simulator import generate_bci, extract_feature_rms, run_simulation
from pdpbiogen.bio_model import TwoStateModel
import numpy as np

def test_generate_bci():
    t, sig = generate_bci(5.0, fs=128)
    assert len(t) == len(sig)
    assert len(t) > 0

def test_extract_feature():
    t, sig = generate_bci(5.0, fs=128)
    feats = extract_feature_rms(sig, fs=128, window_s=1.0)
    assert feats.shape[0] >= 4  # 5s / 1s window -> at least 4 windows

def test_bio_model_step():
    m = TwoStateModel()
    s0 = m.state.copy()
    s1 = m.step(0.1, dt=1.0)
    assert len(s1) == 2
    assert s1 != s0

def test_run_simulation_smoke(tmp_path):
    # Run a short simulation and ensure results file is generated
    cwd = os.getcwd()
    try:
        os.chdir(tmp_path)
        run_simulation(duration_s=6.0, fs=64, window_s=1.0)
        assert os.path.exists('results/simulation.npz')
    finally:
        os.chdir(cwd)
