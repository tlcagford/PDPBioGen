#!/usr/bin/env bash
set -euo pipefail

# Downloads small smoke-test sample data into benchmarks/*/sample_data/
# NOTE: if any URL is blocked, replace with your internal mirror.
# TODO: update these URLs if you host your own canonical samples.

BASE="$(cd "$(dirname "$0")" && pwd)"

echo "Creating sample_data folders..."
mkdir -p "$BASE/bci/sample_data" "$BASE/omics/sample_data" "$BASE/metabolomics/sample_data"

# 1) PhysioNet EEGMMIDB sample (small EDF)
# (If PhysioNet blocks bots, download manually and place at benchmarks/bci/sample_data/eegmmidb_subject1.edf)
PHYSIONET_URL="https://physionet.org/files/eegmmidb/1.0.0/S001/S001R03.edf"
PHYSIONET_TARGET="$BASE/bci/sample_data/eegmmidb_subject1.edf"

if [ ! -f "$PHYSIONET_TARGET" ]; then
  echo "Downloading PhysioNet sample (may require manual download if blocked)..."
  curl -L --fail -o "$PHYSIONET_TARGET" "$PHYSIONET_URL" || {
    echo "PhysioNet sample download failed — please download manually and save to $PHYSIONET_TARGET"
  }
else
  echo "PhysioNet sample already present."
fi

# 2) BNCI / BCI Competition sample (GDF)
BNCI_URL="https://bnci-horizon-2020.s3-eu-west-1.amazonaws.com/data-sets/001-2014/001-2014-01.gdf"
BNCI_TARGET="$BASE/bci/sample_data/bnci_subj1.gdf"

if [ ! -f "$BNCI_TARGET" ]; then
  echo "Downloading BNCI sample..."
  curl -L --fail -o "$BNCI_TARGET" "$BNCI_URL" || {
    echo "BNCI sample download failed — please download manually and save to $BNCI_TARGET"
  }
else
  echo "BNCI sample already present."
fi

# 3) GTEx sample expression matrix (small subset)
GTEX_TARGET="$BASE/omics/sample_data/gtex_sample_counts.tsv"
if [ ! -f "$GTEX_TARGET" ]; then
  echo "Generating small synthetic GTEx-style counts matrix for smoke tests..."
  python3 - <<PY
import pandas as pd, numpy as np
genes = [f"ENSG{100000+i}" for i in range(2000)]
samples = [f"GTEX-{i}" for i in range(6)]
df = pd.DataFrame(np.random.poisson(5, (len(genes), len(samples))), index=genes, columns=samples)
df.to_csv("$GTEX_TARGET", sep="\t")
print("Wrote $GTEX_TARGET")
PY
else
  echo "GTEx sample already present."
fi

# 4) Small metabolomics TSV (synthetic)
MET_TARGET="$BASE/metabolomics/sample_data/metabolomics_small.tsv"
if [ ! -f "$MET_TARGET" ]; then
  echo "Generating synthetic metabolomics small TSV..."
  python3 - <<PY
import pandas as pd, numpy as np
features = [f"M{1000+i}" for i in range(200)]
samples = [f"S{i}" for i in range(6)]
df = pd.DataFrame(np.random.rand(len(features), len(samples)), index=features, columns=samples)
df.to_csv("$MET_TARGET", sep="\t")
print("Wrote $MET_TARGET")
PY
else
  echo "Metabolomics sample already present."
fi

echo "Sample download/generation complete."
