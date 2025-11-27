import pytest
import tempfile
import os
import yaml
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
