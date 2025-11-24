# quick runner for bci smoke tests
import pytest, sys
sys.exit(pytest.main(["-q", "benchmarks/bci/test_preprocessing.py::test_preprocess_epoch_and_hash",
                      "benchmarks/bci/test_feature_extraction.py::test_feature_psd"]))
