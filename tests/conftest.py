import pytest
import tempfile
import os
import yaml
# conftest.py
import pytest
import os
import random
import hashlib
import pytest

# If numpy/pytorch present, seed them for reproducibility
try:
    import numpy as _np
except Exception:
    _np = None

try:
    import torch as _torch
except Exception:
    _torch = None

DEFAULT_SEED = int(os.environ.get("PDPBIOGEN_TEST_SEED", "20251127"))

@pytest.fixture(autouse=True)
def deterministic_seed():
    """
    Sets deterministic seeds for python, numpy and torch (if available).
    Ensures runs are repeatable unless PDPBIOGEN_TEST_SEED env var is set.
    """
    seed = DEFAULT_SEED
    random.seed(seed)
    if _np is not None:
        _np.random.seed(seed)
    if _torch is not None:
        _torch.manual_seed(seed)
        # for CUDA (if used)
        if _torch.cuda.is_available():
            _torch.cuda.manual_seed_all(seed)
    yield
    # no teardown needed

def pytest_collection_modifyitems(config, items):
    """
    By default, skip integration/slow tests unless explicitly requested.
    Use: pytest -m "not integration and not slow"  (default behavior here)
    """
    run_slow = config.getoption("-m")  # if user specified markers, don't skip
    if run_slow:
        return

    skip_slow = pytest.mark.skip(reason="skipped slow/integration tests (default). Use -m to run.")
    for item in items:
        if "integration" in item.keywords or "slow" in item.keywords:
            item.add_marker(skip_slow)

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
def temp_yaml_file():
    """Create a temporary YAML file for testing."""
    def _create_yaml(content):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(content, f)
            return f.name
    return _create_yaml

@pytest.fixture
def sample_config():
    """Sample valid configuration."""
    return {
        'molecules': {
            'Ligand': {'type': 'input', 'color': 'lightblue'},
            'Receptor': {'color': 'lightgreen'},
            'Complex': {'color': 'gold'},
            'Response': {'type': 'output', 'color': 'lightcoral'}
        },
        'interactions': [
            {'from': 'Ligand', 'to': 'Receptor', 'label': 'Binds'},
            {'from': 'Receptor', 'to': 'Complex', 'label': 'Forms'},
            {'from': 'Complex', 'to': 'Response', 'label': 'Activates'}
        ]
    }

@pytest.fixture
def cleanup_files():
    """Clean up generated files after tests."""
    generated_files = []
    
    def _add_file(filepath):
        generated_files.append(filepath)
    
    yield _add_file
    
    # Cleanup
    for filepath in generated_files:
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
        except OSError:
            pass  # Ignore cleanup errors
