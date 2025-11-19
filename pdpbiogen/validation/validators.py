def validate_combined_output(obj: dict):
    """Basic validation: ensure keys exist and scores are numeric."""
    if "combined" not in obj or "agent" not in obj:
        raise ValueError("Malformed pipeline output: missing keys")
    agent = obj["agent"]
    if "score" not in agent or not isinstance(agent["score"], (int, float)):
        raise ValueError("Invalid agent score")
    # More domain-specific checks could go here
    return True
