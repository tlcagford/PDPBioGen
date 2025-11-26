import pandas as pd
import os
import pytest  # If using pytest; install if needed

# Base path (adjust if different)
BASE_DIR = 'validation/datasets/hepatic/gepliver'

# Sample files from GepLiver (download from https://springernature.figshare.com/collections/GepLiver_a_dynamic_integrative_liver_expression_atlas_spanning_developmental_stages_and_liver_disease_phases/6223739)
FILES = {
    'bulk_human': 'human_bulk_expression.tsv',  # TPM-normalized mRNA/lncRNA
    'bulk_mouse': 'mouse_bulk_expression.tsv',
    'single_cell_atlas': 'integrated_gepliver_single_cell_atlas.rds',  # Seurat object; requires R/Scanpy conversion
    'metadata': 'human_bulk_metadata.tsv',
    'cell_deconvolution': 'human_bulk_deconvolution_fractions.tsv'
}

def load_tsv(path):
    return pd.read_csv(path, sep='\t', low_memory=False)

@pytest.mark.parametrize("file_key", FILES.keys())
def test_gepliver_loading(file_key):
    path = os.path.join(BASE_DIR, FILES[file_key])
    assert os.path.exists(path), f"File missing: {path}"
    
    if file_key.endswith('.rds'):  # For RDS, suggest R conversion; skip detailed load here
        print(f"RDS file {path} exists. Convert to H5AD/CSV via R/Scanpy for Python testing.")
        return
    
    df = load_tsv(path)
    assert not df.empty, "DataFrame is empty"
    assert df.shape[0] > 100, f"Too few rows: {df.shape[0]}"
    assert df.shape[1] > 10, f"Too few columns: {df.shape[1]}"
    assert df.isnull().sum().sum() / df.size < 0.5, "Too many NaNs (>50%)"
    
    # Preview
    print(f"\n{file_key} Preview:\n{df.head()}\nShape: {df.shape}\nDtypes: {df.dtypes}")
    
    # Basic stats (e.g., mean expression for sample genes in regeneration context)
    if 'expression' in file_key:  # For expression matrices
        sample_genes = ['EGFR', 'HGF']  # Example regeneration factors
        for gene in sample_genes:
            if gene in df.index:
                mean_expr = df.loc[gene].mean()
                print(f"Mean expression for {gene}: {mean_expr}")
            else:
                print(f"Gene {gene} not found in matrix.")

# Run manually or via pytest
if __name__ == "__main__":
    for key in FILES:
        test_gepliver_loading(key)
    print("GepLiver tests complete. Integrate into PDPBioGen's HepaticHealingSimulator for simulation.")
