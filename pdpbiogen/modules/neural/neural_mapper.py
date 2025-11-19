class NeuralMapper:
    """Simple neural domain mapper: counts channels and returns summary."""

    def map(self, payload):
        # Expect dict with "signals": list
        signals = payload.get("signals", [])
        return {"neural_count": len(signals), "mean_length": (sum(len(s) for s in signals)/len(signals)) if signals else 0}
