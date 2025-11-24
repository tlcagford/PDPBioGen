from benchmarks.agents.mock_llm import respond

def simple_agent_loop(prompt, steps=3):
    history = []
    for i in range(steps):
        r = respond(prompt + f"|step{i}")
        history.append(r)
    return history

def test_agent_determinism_smoke():
    h1 = simple_agent_loop("test-prompt", steps=3)
    h2 = simple_agent_loop("test-prompt", steps=3)
    assert h1 == h2
