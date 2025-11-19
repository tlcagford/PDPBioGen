from pdpbiogen.modules.neural.neural_mapper import NeuralMapper
from pdpbiogen.modules.genomic.genomic_mapper import GenomicMapper
from pdpbiogen.modules.metabolic.metabolic_mapper import MetabolicMapper

MAPPERS = {
    "neural": NeuralMapper,
    "genomic": GenomicMapper,
    "metabolic": MetabolicMapper,
}

class DomainManager:
    """Dispatches data to domain-specific mappers."""

    def __init__(self):
        self._mappers = {k: v() for k, v in MAPPERS.items()}

    def map(self, domain: str, payload):
        if domain not in self._mappers:
            raise ValueError(f"Unknown domain: {domain}")
        return self._mappers[domain].map(payload)
