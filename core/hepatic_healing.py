import pandas as pd
import numpy as np
import scanpy as sc
from .quantum_simulation import QuantumSimulator  # Existing import

class HepaticHealingSimulator:
    def __init__(self, data_path='validation/datasets/hepatic/gepliver/integrated_gepliver_single_cell_atlas.h5ad',
                 age_data_path=None, disease_data_path=None):
        # Load single-cell data (Anndata format; convert RDS if needed)
        self.adata = sc.read_h5ad(data_path)  # Assumes H5AD; use sc.read_10x_mtx for MTX
        sc.pp.normalize_total(self.adata, target_sum=1e4)  # Basic preprocessing if not done
        sc.pp.log1p(self.adata)
        sc.pp.highly_variable_genes(self.adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
        sc.tl.pca(self.adata, svd_solver='arpack')
        sc.pp.neighbors(self.adata, n_neighbors=10, n_pcs=40)
        
        # Compute or load UMAP (links high-dim data to 2D for visualization/clustering)
        if 'X_umap' not in self.adata.obsm:  # If not pre-computed in atlas
            sc.tl.umap(self.adata)
        self.umap_coords = self.adata.obsm['X_umap']  # UMAP embeddings
        
        # Extract time points or regeneration stages from metadata (e.g., from GepLiver phenotypes)
        self.time_points = np.unique(self.adata.obs.get('time_point', np.arange(len(self.adata))))  # Adjust key
        
        self.age_factor = 1.0
        self.disease_factor = 1.0
        if age_data_path:
            age_adata = sc.read_h5ad(age_data_path)
            self.age_factor = np.mean(age_adata.X) / np.mean(self.adata.X)  # Proxy
        if disease_data_path:
            disease_adata = sc.read_h5ad(disease_data_path)
            self.disease_factor = np.mean(disease_adata.X) / np.mean(self.adata.X)

    def simulate_regeneration(self, initial_viability=50, regeneration_genes=['EGFR', 'HGF']):
        # Use UMAP clusters to model regeneration: Mean expression in clusters as viability proxy
        sc.tl.leiden(self.adata)  # Cluster on UMAP neighbors
        cluster_expr = self.adata.to_df().groupby(self.adata.obs['leiden']).mean()
        viability = cluster_expr[regeneration_genes].mean(axis=1).values * (initial_viability / 100)
        viability *= self.age_factor * self.disease_factor
        
        quantum_sim = QuantumSimulator()
        entanglement = quantum_sim.compute_entanglement(viability)
        
        return {
            'umap_coords': self.umap_coords,  # For visualization
            'cluster_viability': viability,
            'time_points': self.time_points,
            'entanglement_strength': entanglement
        }

    def visualize_umap(self):
        # Plot UMAP with regeneration viability colored
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        sc.pl.umap(self.adata, color='leiden', show=False, ax=ax)  # Base UMAP
        plt.savefig('hepatic_regeneration_umap.png')  # Save for repo/docs
        print("UMAP plot saved: hepatic_regeneration_umap.png")

    def run_closed_loop_test(self, target_viability=90, max_iters=10, kp=0.1, ki=0.01, kd=0.05):
        sim_data = self.simulate_regeneration()
        viability = sim_data['cluster_viability']
        error_prev = target_viability - np.mean(viability)
        integral = 0
        for i in range(max_iters):
            error = target_viability - np.mean(viability)
            integral += error
            derivative = error - error_prev
            adjustment = kp * error + ki * integral + kd * derivative
            viability += adjustment
            viability = np.clip(viability, 0, 100)
            if abs(error) < 1:
                break
            error_prev = error
            # Re-run with adjusted (e.g., filter adata for optimized clusters)
        self.visualize_umap()  # Visualize post-optimization
        return {
            'optimized_viability': viability,
            'iterations': i + 1,
            'final_error': error
        }
