from dpbiogen.quantum.healing_sim import run_healing_sim
from pathlib import Path

def test_healing_sim_smoke(tmp_path):
    # Using small sample files (ensure these are in benchmarks/sample_data)
    eeg = "benchmarks/bci/sample_data/eegmmidb_subject1.edf"
    sbml = "benchmarks/metabolomics/sample_model_small.xml"
    outdir = tmp_path / "healing_out"
    # If SBML not present, the test should skip (maintainers should provide a small SBML)
    if not Path(eeg).exists() or not Path(sbml).exists():
        # soft skip so CI doesn't fail until SBML is provided
        import pytest
        pytest.skip("Smoke samples missing (place eeg and sbml samples in benchmarks/sample_data)")
    manifest = run_healing_sim(eeg, sbml, outdir=str(outdir))
    assert "feats_hash" in manifest
    assert "gene_delta_hash" in manifest
    assert "fba_report" in manifest
