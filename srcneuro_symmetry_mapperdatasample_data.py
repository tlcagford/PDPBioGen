"""
Sample data generator for quick start demo
Provides synthetic but biologically plausible data for testing
"""

import numpy as np
import pandas as pd
from datetime import datetime

def create_sample_data(n_subjects=5):
    """Create synthetic sample data for three domains"""
    
    return {
        'neural': _create_neural_data(n_subjects),
        'genomic': _create_genomic_data(n_subjects), 
        'metabolic': _create_metabolic_data(n_subjects),
        'metadata': {
            'creation_date': datetime.now().isoformat(),
            'n_subjects': n_subjects,
            'data_type': 'synthetic_demo'
        }
    }

def _create_neural_data(n_subjects):
    """Create synthetic neural data"""
    brain_regions = ['prefrontal_cortex', 'hippocampus', 'amygdala', 
                    'striatum', 'cerebellum', 'brainstem']
    
    return {
        'regions': {region: np.random.normal(0, 1, n_subjects) for region in brain_regions},
        'connectivity': np.random.random((len(brain_regions), len(brain_regions))),
        'eeg_power': {
            'delta': np.random.gamma(2, 2, n_subjects),
            'theta': np.random.gamma(1.5, 1.5, n_subjects),
            'alpha': np.random.gamma(1, 1, n_subjects),
            'beta': np.random.gamma(0.5, 0.5, n_subjects)
        },
        'subject_ids': [f'SUBJ_{i:03d}' for i in range(n_subjects)]
    }

def _create_genomic_data(n_subjects):
    """Create synthetic genomic data"""
    genes = ['BDNF', 'COMT', 'SLC6A4', 'DRD2', 'HTR2A', 'MAOA', 
            'GRIN2B', 'FTO', 'APOE', 'MTHFR']
    
    return {
        'genes': genes,
        'expression': pd.DataFrame(
            np.random.lognormal(0, 1, (n_subjects, len(genes))),
            columns=genes,
            index=[f'SUBJ_{i:03d}' for i in range(n_subjects)]
        ),
        'pathways': {
            'neurotransmitter_synthesis': ['COMT', 'SLC6A4', 'DRD2', 'HTR2A', 'MAOA'],
            'neuroplasticity': ['BDNF', 'GRIN2B'],
            'metabolic': ['FTO', 'MTHFR'],
            'risk_factors': ['APOE']
        }
    }

def _create_metabolic_data(n_subjects):
    """Create synthetic metabolic data"""
    metabolites = ['glucose', 'lactate', 'pyruvate', 'glutamate', 'gaba',
                  'atp', 'nad', 'acetyl_coa', 'citrate', 'alanine']
    
    return {
        'metabolites': metabolites,
        'concentrations': pd.DataFrame(
            np.random.lognormal(2, 0.5, (n_subjects, len(metabolites))),
            columns=metabolites,
            index=[f'SUBJ_{i:03d}' for i in range(n_subjects)]
        ),
        'pathways': ['glycolysis', 'tca_cycle', 'oxidative_phosphorylation', 
                    'neurotransmitter_synthesis', 'fatty_acid_metabolism'],
        'flux_rates': {
            'glycolysis': np.random.normal(100, 10, n_subjects),
            'tca_cycle': np.random.normal(50, 5, n_subjects),
            'atp_production': np.random.normal(200, 20, n_subjects)
        }
    }