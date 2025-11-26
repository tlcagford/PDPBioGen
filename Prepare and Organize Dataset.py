import os
import pandas as pd
import h5py
import shutil

# Source dir from downloads
source_dir = 'datasets'  # From previous script
target_base = 'validation/datasets'

# Categories and example files (update with your actual downloaded file names)
categories = {
    'neural': ['GSE183591_series_matrix.txt', 'GSE246714_series_matrix.txt', 'GSE29488_series_matrix.txt'],
    'hepatic': ['GSE39791_series_matrix.txt', 'GSE77045_series_matrix.txt', 'GSE63742_series_matrix.txt', 'GSE63742_ratios.xls'],
    'pulmonary': ['GSE245721_series_matrix.txt', 'GSE136831_series_matrix.txt', 'GSE168191_series_matrix.txt', 'GSE168191_filtered_feature_bc_matrix.h5'],
    'disease_specific': ['GSE241124_series_matrix.txt', 'GSE265972_series_matrix.txt', 'GSE8056_series_matrix.txt'],
    'age_related': ['GSE226907_series_matrix.txt', 'GSE240017_series_matrix.txt', 'GSE202664_series_matrix.txt']
}

# Create subdirs and copy/convert
for cat, files in categories.items():
    target_dir = os.path.join(target_base, cat)
    os.makedirs(target_dir, exist_ok=True)
    for file in files:
        src = os.path.join(source_dir, file)
        if os.path.exists(src):
            if file.endswith('.xls') or file.endswith('.xlsx'):
                # Convert XLS to CSV
                df = pd.read_excel(src)
                csv_path = os.path.join(target_dir, file.replace('.xls', '.csv'))
                df.to_csv(csv_path, index=False)
                print(f"Converted and moved: {file} to {csv_path}")
            elif file.endswith('.h5'):
                # Convert H5 (e.g., filtered_feature_bc_matrix.h5) to CSV (sparse matrix example)
                with h5py.File(src, 'r') as f:
                    # Assuming 10x Genomics format; adjust keys as needed
                    barcodes = f['matrix/barcodes'][:]
                    features = f['matrix/features/id'][:]
                    data = f['matrix/data'][:]
                    indices = f['matrix/indices'][:]
                    indptr = f['matrix/indptr'][:]
                    shape = f['matrix/shape'][:]
                # Reconstruct sparse matrix and save as CSV (dense for simplicity, but large!)
                from scipy.sparse import csr_matrix
                mat = csr_matrix((data, indices, indptr), shape=shape)
                df = pd.DataFrame(mat.toarray(), index=features, columns=barcodes)
                csv_path = os.path.join(target_dir, file.replace('.h5', '_matrix.csv'))
                df.to_csv(csv_path)
                print(f"Converted and moved: {file} to {csv_path}")
            else:
                # Copy TXT/TSV as-is
                dest = os.path.join(target_dir, file)
                shutil.copy(src, dest)
                print(f"Moved: {file} to {dest}")
        else:
            print(f"File not found: {src} – ensure downloads completed.")

# For raw TAR (e.g., CEL files), extract and normalize if needed (example for GSE29488_RAW.tar)
# Use affy/bioconductor in R or Biopython, but for now, leave as-is or add processing later.

print("Datasets organized. Add/commit to git.")
