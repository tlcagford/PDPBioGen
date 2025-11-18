"""
Tests for quick start demo
"""

import pytest
import tempfile
from pathlib import Path
from examples.quick_start import QuickStartDemo
from neuro_symmetry_mapper.data.sample_data import create_sample_data

class TestQuickStart:
    def test_sample_data_creation(self):
        """Test that sample data is created correctly"""
        data = create_sample_data(n_subjects=3)
        
        assert 'neural' in data
        assert 'genomic' in data
        assert 'metabolic' in data
        assert len(data['neural']['regions']) > 0
        assert len(data['genomic']['genes']) > 0
        assert len(data['metabolic']['metabolites']) > 0
    
    def test_quick_start_demo(self):
        """Test that quick start demo runs without errors"""
        with tempfile.TemporaryDirectory() as temp_dir:
            demo = QuickStartDemo(test_mode=True)
            demo.results_dir = Path(temp_dir)
            
            # Test individual steps
            sample_data = demo.step1_load_sample_data()
            frameworks = demo.step2_initialize_frameworks()
            
            assert sample_data is not None
            assert 'critic' in frameworks
            assert 'collaboration' in frameworks
            assert 'evolver' in frameworks
    
    def test_demo_integration(self):
        """Test the complete demo integration"""
        demo = QuickStartDemo(test_mode=True)
        success = demo.run_demo()
        
        # Check that results were created
        assert demo.results_dir.exists()
        assert (demo.results_dir / 'sample_data_info.json').exists()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])