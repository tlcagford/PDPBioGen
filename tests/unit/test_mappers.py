from pdpbiogen.modules.neural.neural_mapper import NeuralMapper
from pdpbiogen.modules.genomic.genomic_mapper import GenomicMapper
from pdpbiogen.modules.metabolic.metabolic_mapper import MetabolicMapper

def test_neural_mapper():
    m = NeuralMapper()
    out = m.map({"signals": [[0],[1],[0,1]]})
    assert out["neural_count"] == 3

def test_genomic_mapper():
    m = GenomicMapper()
    out = m.map({"variants": [{"a":1}]})
    assert out["variant_count"] == 1

def test_metabolic_mapper():
    m = MetabolicMapper()
    out = m.map({"measures": {"x": 2, "y": 4}})
    assert out["measure_count"] == 2
    assert out["avg_value"] == 3
