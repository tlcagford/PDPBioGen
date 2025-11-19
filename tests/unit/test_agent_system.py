from pdpbiogen.core.agent_system import AgentSystem

def test_agent_step_returns_score():
    agent = AgentSystem()
    out = agent.step({"domains": {"a": {"x": 1}, "b": {"y": 2}}})
    assert "score" in out
    assert out["score"] >= 0
