import pytest, sys
sys.exit(pytest.main(["-q", "benchmarks/reproducibility/test_random_seed_control.py::test_seed_smoke"]))
