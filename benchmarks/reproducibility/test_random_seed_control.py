import numpy as np

def test_seed_smoke():
    # demonstrate deterministic RNG control
    np.random.seed(42)
    a = np.random.rand(10)
    np.random.seed(42)
    b = np.random.rand(10)
    assert (a == b).all()
