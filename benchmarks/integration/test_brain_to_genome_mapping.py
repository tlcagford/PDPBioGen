import numpy as np

def simple_brain_to_genome(eeg_features):
    # map to 'gene expression' vector deterministically
    rs = np.random.RandomState(int(sum(eeg_features)*1e6) % 2**31)
    return rs.rand(100)

def test_brain_to_genome_consistency():
    f = np.linspace(0.1, 1.0, 32)
    g1 = simple_brain_to_genome(f)
    g2 = simple_brain_to_genome(f)
    assert (g1 == g2).all()
    assert g1.size == 100
