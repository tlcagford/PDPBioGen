import json
import numpy as np

def test_pdpbiogen_import():
    """Basic import sanity check."""
    import pdpbiogen
    assert hasattr(pdpbiogen, "__version__")


def test_minimal_domain_map():
    """Test a simple transformation using a synthetic dataset."""
    from pdpbiogen.core.integrator import DomainIntegrator

    integrator = DomainIntegrator()

    sample_input = {
        "neural": {"activity": 0.82},
        "genomic": {"expression": 12.4},
        "metabolic": {"atp": 6.8},
    }

    result = integrator.integrate(sample_input)

    assert isinstance(result, dict)
    assert "neural" in result
    assert "genomic" in result
    assert "metabolic" in result
    assert result["neural"]["activity"] > 0  # staying positive


def test_cross_domain_signal_flow():
    """Verifies cross-domain communication."""
    from pdpbiogen.core.agent_system import AgentSystem

    agents = AgentSystem()

    # Synthetic test event
    event = {
        "source": "neural",
        "target": "genomic",
        "payload": {"signal_strength": 0.55}
    }

    response = agents.route(event)

    assert response is not None
    assert "status" in response
    assert response["status"] in ["delivered", "queued"]


def test_validation_pipeline():
    """Runs a simple consistency check on synthetic data."""
    from pdpbiogen.validation.validators import check_consistency

    synthetic = {
        "neural": {"activity": 0.9},
        "genomic": {"expression": 13.1},
        "metabolic": {"atp": 7.2},
    }

    result = check_consistency(synthetic)

    assert result["valid"] is True
    assert "score" in result
    assert 0 <= result["score"] <= 1
