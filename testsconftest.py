import pytest
import numpy as np
import tempfile
import os
# conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--reruns", action="store", default="2",
        help="Number of times to rerun failing tests."
    )

@pytest.fixture(scope="session", autouse=True)
def set_default_reruns(pytestconfig):
    # Default: rerun flaky tests twice
    pytestconfig.option.reruns = int(pytestconfig.getoption("--reruns"))


@pytest.fixture
def sample_heart_data():
    """Fixture providing sample heart data for tests"""
    import pandas as pd
    return pd.DataFrame({
        'time_hours': range(100),
        'tissue_viability': np.linspace(30, 80, 100),
        'cellular_coherence': np.linspace(20, 70, 100),
        'quantum_entanglement': np.random.normal(50, 10, 100),
        'mitochondrial_energy': np.linspace(25, 75, 100),
        'inflammation_marker': np.linspace(80, 20, 100)
    })


@pytest.fixture
def temp_data_dir():
    """Fixture providing temporary directory for test data"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield tmp_dir


@pytest.fixture
def quantum_system():
    """Fixture providing initialized quantum system"""
    from quantum_healing import QuantumCTHealingSystem
    return QuantumCTHealingSystem()


@pytest.fixture(autouse=True)
def set_random_seed():
    """Set random seed for reproducible tests"""
    np.random.seed(42)
