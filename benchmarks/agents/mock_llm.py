# benchmarks/agents/mock_llm.py
# Simple deterministic LLM response provider for tests.
def respond(prompt):
    # deterministic function of prompt
    return "RESPONSE:" + str(hash(prompt) % 100000)
