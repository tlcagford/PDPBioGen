class MetabolicMapper:
    """Simple metabolic mapper."""

    def map(self, payload):
        measures = payload.get("measures", {})
        avg = sum(measures.values())/len(measures) if measures else 0
        return {"measure_count": len(measures), "avg_value": avg}
