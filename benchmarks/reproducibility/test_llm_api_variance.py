# This test ensures that when LLMs are swapped, core logic can be tested using a mock.
from benchmarks.agents.mock_llm import respond

def test_llm_mock_integration():
    out = respond("unit-test-prompt")
    assert isinstance(out, str) and out.startswith("RESPONSE:")
