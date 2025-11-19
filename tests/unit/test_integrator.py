import pytest
from pdpbiogen.core.integrator import Integrator

def test_integrator_runs_minimal():
    integrator = Integrator()
    inputs = {
        "neural": {"signals": [[1,0]]},
        "genomic": {"variants": []},
        "metabolic": {"measures": {"a": 1}}
    }
    result = integrator.run(inputs)
    assert "combined" in result and "agent" in result
    assert isinstance(result["agent"]["score"], (int, float))
