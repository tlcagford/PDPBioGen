from benchmarks.agents.mock_llm import respond

def test_agent_replay():
    prompt = "replay-prompt"
    log = []
    for i in range(4):
        out = respond(prompt + f"|{i}")
        log.append(out)
    # replay by re-calling respond with same sequence
    replay = [respond(prompt + f"|{i}") for i in range(4)]
    assert log == replay
