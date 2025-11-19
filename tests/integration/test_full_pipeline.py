from pdpbiogen.core.integrator import Integrator

def test_full_pipeline_with_sample_data():
    inputs = {
        "neural": {"signals": [[0,1],[1,1]]},
        "genomic": {"variants": [{"chr":"1", "pos":1}]},
        "metabolic": {"measures": {"a": 1.0}}
    }
    integrator = Integrator()
    out = integrator.run(inputs)
    assert "agent" in out
    assert out["agent"]["score"] >= 0
