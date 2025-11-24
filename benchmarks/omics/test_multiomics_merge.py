import pandas as pd
from pathlib import Path

GTEX = Path("benchmarks/omics/sample_data/gtex_sample_counts.tsv")
MET = Path("benchmarks/metabolomics/sample_data/metabolomics_small.tsv")

def test_merge_simple():
    g = pd.read_csv(GTEX, sep="\t", index_col=0)
    m = pd.read_csv(MET, sep="\t", index_col=0)
    # perform a deterministic merge by aligning on sample count columns
    # reduce to same number of columns (samples)
    min_cols = min(g.shape[1], m.shape[1])
    gm = g.iloc[:, :min_cols].copy()
    mm = m.iloc[:, :min_cols].copy()
    merged = pd.concat([gm, mm], axis=0)
    assert merged.shape[0] == g.shape[0] + m.shape[0] - 0
