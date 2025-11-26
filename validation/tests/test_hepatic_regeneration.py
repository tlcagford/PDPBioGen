import pytest
import scanpy as sc
import matplotlib.pyplot as plt
import os
from pdpbiogen.core.hepatic_healing import HepaticHealingSimulator  # Assume added from prior guide

# Paths (link datasets and UMAP files)
DATA_PATH = 'validation/datasets/hepatic/gepliver/integrated_gepliver_single_cell_atlas.h5ad'  # Main dataset (expression matrix)
UMAP_DIR = 'validation/datasets/hepatic/gepliver/umap_by_dataset/'  # Dir for UMAP_by_dataset plots (e.g., PNGs split by dataset)
AGE_PATH = 'validation/datasets/age_related/GSE226907_series_matrix.txt'  # Example cross-link
DISEASE_PATH = 'validation/datasets/disease_specific/GSE241124_series_matrix.txt'  # Example

# Helper to load and link UMAP image (e.g., for visualization in test)
def load_umap_image(dataset_name='example_dataset'):
    image_path = os.path.join(UMAP_DIR, f'umap_{dataset_name}.png')  # Assume naming like umap_SC01.png for dataset SC01
    if os.path.exists(image_path):
        img = plt.imread(image_path)
        return img
    else:
        raise FileNotFoundError(f"UMAP image for {dataset_name} not found. Download from GepLiver Figshare.")

@pytest.fixture
def hepatic_simulator():
    return HepaticHealingSimulator(data_path=DATA_PATH, age_data_path=AGE_PATH, disease_data_path=DISEASE_PATH)

def test_data_loading(hepatic_simulator):
    assert hepatic_simulator.adata is not None, "Failed to load GepLiver dataset"
    assert 'X_umap' in hepatic_simulator.adata.obsm, "UMAP embeddings not present or linked"
    assert hepatic_simulator.adata.shape[0] > 400000, "Unexpected cell count in atlas"  # ~409k cells

def test_umap_visualization():
    # Link and display a sample UMAP_by_dataset image
    img = load_umap_image(dataset_name='SC01')  # Example dataset from GepLiver (adjust based on downloads)
    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.axis('off')
    plt.savefig('test_umap_visualization.png')
    assert os.path.exists('test_umap_visualization.png'), "Failed to link and save UMAP image"

def test_simulate_regeneration(hepatic_simulator):
    results = hepatic_simulator.simulate_regeneration()
    assert 'umap_coords' in results, "UMAP linkage missing in simulation"
    assert len(results['cluster_viability']) > 0, "No viability data generated"
    assert results['umap_coords'].shape[1] == 2, "Invalid UMAP dimensions"

def test_closed_loop(hepatic_simulator):
    results = hepatic_simulator.run_closed_loop_test()
    assert 'optimized_viability' in results, "Closed-loop results missing"
    assert abs(results['final_error']) < 5, "Closed-loop did not converge sufficiently (tune PID if needed)"
    assert results['iterations'] <= 10, "Exceeded max iterations"
    print("Closed-Loop Results:")
    print(f"Optimized Viability: {results['optimized_viability']}")
    print(f"Iterations: {results['iterations']}")
    print(f"Final Error: {results['final_error']}")

if __name__ == "__main__":
    pytest.main()

