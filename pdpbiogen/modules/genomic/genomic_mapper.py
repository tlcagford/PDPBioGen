class GenomicMapper:
    """Simple genomic mapper: counts variants and returns a summary."""

    def map(self, payload):
        variants = payload.get("variants", [])
        return {"variant_count": len(variants), "top_variant": variants[0] if variants else None
