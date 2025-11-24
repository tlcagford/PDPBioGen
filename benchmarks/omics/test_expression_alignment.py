import pandas as pd
from pathlib import Path

SAMPLE = Path("benchmarks/omics/sample_data/gtex_sample_counts.tsv")

def test_expression_matrix_read():
    assert SAMPLE.exists()
    df = pd.read_csv(SAMPLE, sep="\t", index_col=0)
    # basic shape checks
    assert df.shape[0] >= 100
    assert df.shape[1] >= 2
    # entries non-negative ints
    assert (df.values >= 0).all()
