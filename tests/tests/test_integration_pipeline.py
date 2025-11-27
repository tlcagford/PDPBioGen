import pytest

@pytest.mark.integration
def test_full_pipeline_runs():
    from pdpbiogen import full_pipeline_demo
    result = full_pipeline_demo()
    assert "status" in result
    assert result["status"] == "ok"
