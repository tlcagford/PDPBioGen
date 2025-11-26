import os
import ftplib
import gzip
import shutil
import tarfile
import pandas as pd

# Function to download from FTP
def download_ftp_file(host, file_path, dest_folder='datasets'):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    filename = file_path.split('/')[-1]
    local_path = os.path.join(dest_folder, filename)
    
    try:
        ftp = ftplib.FTP(host)
        ftp.login('anonymous', 'guest@example.com')
        with open(local_path, 'wb') as local_file:
            ftp.retrbinary(f'RETR {file_path}', local_file.write)
        ftp.quit()
        print(f"Downloaded: {filename} to {local_path}")
        return local_path
    except Exception as e:
        print(f"Failed to download ftp://{host}{file_path}: {e}")
        return None

# Function to extract file if needed
def extract_file(local_path):
    extracted_path = local_path
    if local_path.endswith('.gz'):
        extracted_path = local_path[:-3]
        with gzip.open(local_path, 'rb') as f_in:
            with open(extracted_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        os.remove(local_path)
        print(f"Extracted: {extracted_path}")
    elif local_path.endswith('.tar') or local_path.endswith('.tgz'):
        extract_dir = os.path.dirname(local_path)
        with tarfile.open(local_path, 'r') as tar:
            tar.extractall(extract_dir)
        os.remove(local_path)
        print(f"Extracted tar to: {extract_dir}")
        extracted_path = extract_dir  # Return dir since multiple files
    return extracted_path

# Function to test dataset (load sample and print summary)
def test_dataset(file_path):
    if os.path.isdir(file_path):
        print(f"Directory extracted: {file_path}. Skipping detailed test (manual inspection recommended for multiple files).")
        return
    try:
        if file_path.endswith(('.txt', '.tsv')):
            df = pd.read_csv(file_path, sep='\t', nrows=20, on_bad_lines='skip')
        elif file_path.endswith('.csv'):
            df = pd.read_csv(file_path, nrows=20)
        elif file_path.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file_path, nrows=20)
        else:
            print(f"Unsupported file type for testing: {file_path}")
            return
        print(f"\nTesting: {file_path}")
        print(f"Sample shape: {df.shape}")
        print("Head:\n", df.head())
    except Exception as e:
        print(f"Error testing {file_path}: {e}. May need custom parsing (e.g., for GEO SOFT format).")

# List of datasets with FTP paths (host is always 'ftp.ncbi.nlm.nih.gov')
host = 'ftp.ncbi.nlm.nih.gov'
datasets = [
    # Neural
    {'name': 'GSE183591_matrix', 'path': '/geo/series/GSE183nnn/GSE183591/matrix/GSE183591_series_matrix.txt.gz'},
    {'name': 'GSE183591_raw', 'path': '/geo/series/GSE183nnn/GSE183591/suppl/GSE183591_RAW.tar'},
    {'name': 'GSE246714_matrix', 'path': '/geo/series/GSE246nnn/GSE246714/matrix/GSE246714_series_matrix.txt.gz'},
    {'name': 'GSE29488_matrix', 'path': '/geo/series/GSE29nnn/GSE29488/matrix/GSE29488_series_matrix.txt.gz'},
    {'name': 'GSE29488_raw', 'path': '/geo/series/GSE29nnn/GSE29488/suppl/GSE29488_RAW.tar'},
    
    # Hepatic
    {'name': 'GSE39791_matrix', 'path': '/geo/series/GSE39nnn/GSE39791/matrix/GSE39791_series_matrix.txt.gz'},
    {'name': 'GSE39791_raw', 'path': '/geo/series/GSE39nnn/GSE39791/suppl/GSE39791_RAW.tar'},
    {'name': 'GSE77045_matrix', 'path': '/geo/series/GSE77nnn/GSE77045/matrix/GSE77045_series_matrix.txt.gz'},
    {'name': 'GSE63742_matrix', 'path': '/geo/series/GSE63nnn/GSE63742/matrix/GSE63742_series_matrix.txt.gz'},
    {'name': 'GSE63742_raw', 'path': '/geo/series/GSE63nnn/GSE63742/suppl/GSE63742_RAW.tar'},
    # For GSE63742 XLS ratios (specific suppl file; adjust if name differs)
    {'name': 'GSE63742_ratios', 'path': '/geo/series/GSE63nnn/GSE63742/suppl/GSE63742_ratios.xls.gz'},  # Check exact name on GEO page if fails
    
    # Pulmonary
    {'name': 'GSE245721_matrix', 'path': '/geo/series/GSE245nnn/GSE245721/matrix/GSE245721_series_matrix.txt.gz'},
    {'name': 'GSE136831_matrix', 'path': '/geo/series/GSE136nnn/GSE136831/matrix/GSE136831_series_matrix.txt.gz'},
    {'name': 'GSE168191_matrix', 'path': '/geo/series/GSE168nnn/GSE168191/matrix/GSE168191_series_matrix.txt.gz'},
    # For GSE168191 H5 (specific suppl; check exact if fails)
    {'name': 'GSE168191_h5', 'path': '/geo/series/GSE168nnn/GSE168191/suppl/GSE168191_filtered_feature_bc_matrix.h5'},  # Example; verify on GEO
    
    # Disease-Specific
    {'name': 'GSE241124_matrix', 'path': '/geo/series/GSE241nnn/GSE241124/matrix/GSE241124_series_matrix.txt.gz'},
    {'name': 'GSE265972_matrix', 'path': '/geo/series/GSE265nnn/GSE265972/matrix/GSE265972_series_matrix.txt.gz'},
    {'name': 'GSE8056_matrix', 'path': '/geo/series/GSE8nnn/GSE8056/matrix/GSE8056_series_matrix.txt.gz'},
    {'name': 'GSE8056_raw', 'path': '/geo/series/GSE8nnn/GSE8056/suppl/GSE8056_RAW.tar'},
    
    # Age-Related
    {'name': 'GSE226907_matrix', 'path': '/geo/series/GSE226nnn/GSE226907/matrix/GSE226907_series_matrix.txt.gz'},
    {'name': 'GSE240017_matrix', 'path': '/geo/series/GSE240nnn/GSE240017/matrix/GSE240017_series_matrix.txt.gz'},
    {'name': 'GSE202664_matrix', 'path': '/geo/series/GSE202nnn/GSE202664/matrix/GSE202664_series_matrix.txt.gz'},
]

# Download, extract, and test
for ds in datasets:
    local_path = download_ftp_file(host, ds['path'])
    if local_path:
        extracted_path = extract_file(local_path)
        test_dataset(extracted_path)

print("All downloads and tests complete. Check 'datasets' folder and add to your GitHub repo.")
