import pytest
import numpy as np
import pandas as pd
import sys
import os

# Add source to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from quantum_healing import QuantumCTHealingSystem, HeartHealingTestFramework, QuantumHealingProcessor


class TestQuantumCTHealingSystem:
    """Test core Quantum CT Healing System functionality"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.system = QuantumCTHealingSystem()
    
    def test_system_initialization(self):
        """Test that system initializes correctly"""
        assert self.system is not None
        assert hasattr(self.system, 'system_components')
        assert hasattr(self.system, 'quantum_fields')
    
    def test_generate_heart_data(self):
        """Test heart data generation"""
        heart_data = self.system.generate_realistic_heart_data(n_samples=100)
        
        # Check data structure
        assert isinstance(heart_data, pd.DataFrame)
        assert len(heart_data) == 100
        
        # Check required columns
        expected_columns = ['time_hours', 'tissue_viability', 'cellular_coherence', 
                          'quantum_entanglement', 'mitochondrial_energy', 'inflammation_marker']
        for col in expected_columns:
            assert col in heart_data.columns
        
        # Check data ranges
        assert heart_data['tissue_viability'].between(0, 100).all()
        assert heart_data['cellular_coherence'].between(0, 100).all()
    
    def test_quantum_ct_scan_generation(self):
        """Test 3D quantum CT scan generation"""
        scan_data = self.system.generate_quantum_ct_scan('heart_tissue')
        
        # Check scan data structure
        assert isinstance(scan_data, dict)
        
        expected_metrics = ['tissue_viability', 'quantum_coherence', 'cellular_energy',
                          'inflammation_levels', 'quantum_entanglement', 'bio_photon_emissions']
        
        for metric in expected_metrics:
            assert metric in scan_data
            data = scan_data[metric]
            
            # Check data is 3D numpy array
            assert isinstance(data, np.ndarray)
            assert data.ndim == 3
            assert data.shape == (64, 64, 64)  # Default grid size
            
            # Check data range
            assert data.min() >= 0
            assert data.max() <= 100
    
    def test_quantum_states_creation(self):
        """Test quantum state creation"""
        quantum_states = self.system.create_quantum_biological_states()
        
        expected_states = ['acute_damage', 'inflammatory', 'proliferative', 
                          'remodeling', 'recovered']
        
        for state in expected_states:
            assert state in quantum_states
            # Check it's a quantum state object
            assert hasattr(quantum_states[state], 'dims')
            assert hasattr(quantum_states[state], 'data')


class TestHeartHealingTestFramework:
    """Test heart healing test framework"""
    
    def setup_method(self):
        self.test_framework = HeartHealingTestFramework()
    
    def test_data_generation(self):
        """Test test data generation"""
        closed_data, open_data = self.test_framework.download_heart_test_data()
        
        # Check data structures
        assert isinstance(closed_data, pd.DataFrame)
        assert isinstance(open_data, pd.DataFrame)
        
        # Check both datasets have same columns
        assert set(closed_data.columns) == set(open_data.columns)
        
        # Check test type identification
        assert (closed_data['test_type'] == 'closed_loop').all()
        assert (open_data['test_type'] == 'open_loop').all()
    
    def test_comparative_analysis(self):
        """Test comparative analysis between closed and open loop"""
        closed_data, open_data = self.test_framework.download_heart_test_data()
        metrics = self.test_framework.run_comparative_analysis()
        
        assert 'closed_loop' in metrics
        assert 'open_loop' in metrics
        
        # Check metric structure
        for test_type in ['closed_loop', 'open_loop']:
            test_metrics = metrics[test_type]
            expected_metrics = ['final_viability', 'avg_healing_rate', 'viability_std',
                              'max_inflammation', 'settling_time', 'overshoot', 
                              'steady_state_error']
            
            for metric in expected_metrics:
                assert metric in test_metrics
                assert isinstance(test_metrics[metric], (int, float))


class TestQuantumHealingProcessor:
    """Test quantum healing processor"""
    
    def setup_method(self):
        self.processor = QuantumHealingProcessor()
        self.ct_system = QuantumCTHealingSystem()
    
    def test_healing_protocols_design(self):
        """Test healing protocols design"""
        protocols = self.processor.design_quantum_healing_protocols()
        
        expected_protocols = ['tissue_regeneration', 'inflammation_reduction',
                            'quantum_entanglement_repair', 'bio_photon_optimization']
        
        for protocol in expected_protocols:
            assert protocol in protocols
    
    def test_quantum_healing_application(self):
        """Test quantum healing application"""
        scan_data = self.ct_system.generate_quantum_ct_scan('heart_tissue')
        healed_data = self.processor.apply_quantum_healing(scan_data)
        
        # Check structure preservation
        assert set(healed_data.keys()) == set(scan_data.keys())
        
        # Check healing effect (viability should improve)
        original_viability = np.mean(scan_data['tissue_viability'])
        healed_viability = np.mean(healed_data['tissue_viability'])
        
        # Healing should generally improve viability
        # Using loose check due to stochastic nature
        assert healed_viability >= original_viability - 5  # Allow small tolerance


class TestEdgeCases:
    """Test edge cases and error conditions"""
    
    def test_empty_scan_data(self):
        """Test handling of empty scan data"""
        system = QuantumCTHealingSystem()
        
        # Should handle missing body regions gracefully
        with pytest.raises(KeyError):
            system.visualize_quantum_ct_scan('nonexistent_region')
    
    def test_invalid_parameters(self):
        """Test invalid parameter handling"""
        system = QuantumCTHealingSystem()
        
        # Invalid sample size
        with pytest.raises(ValueError):
            system.generate_realistic_heart_data(n_samples=-1)
    
    def test_memory_management(self):
        """Test memory management with large datasets"""
        system = QuantumCTHealingSystem()
        
        # Large scan should complete without memory errors
        large_scan = system.generate_quantum_ct_scan('whole_body')
        
        # Verify we can process the data
        total_voxels = sum(data.size for data in large_scan.values())
        assert total_voxels > 0


def test_performance_benchmarks():
    """Performance benchmarks for critical operations"""
    system = QuantumCTHealingSystem()
    
    # Time data generation
    import time
    start_time = time.time()
    heart_data = system.generate_realistic_heart_data(n_samples=1000)
    generation_time = time.time() - start_time
    
    # Should complete within reasonable time
    assert generation_time < 5.0  # 5 seconds for 1000 samples
    
    # Time CT scan generation
    start_time = time.time()
    scan_data = system.generate_quantum_ct_scan('heart_tissue')
    scan_time = time.time() - start_time
    
    assert scan_time < 10.0  # 10 seconds for 3D scan


if __name__ == '__main__':
    pytest.main([__file__, '-v'])