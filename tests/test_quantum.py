tests/test_quantum.pyimport pytest

@pytest.mark.quantum
@pytest.mark.flaky
def test_quantum_module_imports():
    import pdpbiogen.quantum as q
    assert callable(q.quantum_healing_estimator)
