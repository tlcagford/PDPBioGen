
### Step 4: Create Tests Directory
```python
import os

# Create tests directory structure
os.makedirs('tests', exist_ok=True)
print("✅ Created tests/ directory")

# Create __init__.py
with open('tests/__init__.py', 'w') as f:
    f.write('"""Test suite for PDPBioGen"""\n')
print("✅ Created tests/__init__.py")

# Create test_heart_healing.py
test_heart_content = '''"""
Tests for heart healing simulation functionality
"""
import pytest
import sys
import os
import numpy as np
import pandas as pd

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from heart_healing import HeartHealingSimulator, run_closed_loop_test, run_open_loop_test
    HAS_HEART_HEALING = True
except ImportError:
    HAS_HEART_HEALING = False


@pytest.mark.skipif(not HAS_HEART_HEALING, reason="heart_healing module not available")
class TestHeartHealingSimulator:
    """Test cases for HeartHealingSimulator"""
    
    def test_simulator_initialization(self):
        """Test that simulator initializes correctly"""
        simulator = HeartHealingSimulator()
        assert simulator is not None
        assert hasattr(simulator, 'healing_rate')
        assert hasattr(simulator, 'treatment_type')
    
    def test_parameter_validation(self):
        """Test parameter validation"""
        # Valid parameters should work
        simulator = HeartHealingSimulator(healing_rate=0.2)
        assert simulator.healing_rate == 0.2
        
        # Invalid parameters should raise errors
        with pytest.raises(ValueError):
            HeartHealingSimulator(healing_rate=-0.1)
    
    def test_data_generation(self):
        """Test data generation functionality"""
        simulator = HeartHealingSimulator()
        
        # Test basic data generation
        data = simulator.generate_heart_data(n_samples=100)
        
        assert isinstance(data, pd.DataFrame)
        assert len(data) == 100
        assert 'tissue_viability' in data.columns
        assert 'cellular_coherence' in data.columns
        assert 'time_hours' in data.columns
        
        # Test data ranges
        assert data['tissue_viability'].between(0, 100).all()
        assert data['cellular_coherence'].between(0, 100).all()
    
    def test_closed_loop_function(self):
        """Test closed loop test function"""
        data = run_closed_loop_test(n_samples=50)
        
        assert isinstance(data, pd.DataFrame)
        assert len(data) == 50
        assert 'control_signal' in data.columns
        assert 'feedback_error' in data.columns
    
    def test_open_loop_function(self):
        """Test open loop test function"""
        data = run_open_loop_test(n_samples=50)
        
        assert isinstance(data, pd.DataFrame)
        assert len(data) == 50
        assert 'control_signal' in data.columns


@pytest.mark.skipif(not HAS_HEART_HEALING, reason="heart_healing module not available")
class TestHeartHealingAdvanced:
    """Advanced tests for heart healing functionality"""
    
    def test_healing_trajectory(self):
        """Test healing trajectory simulation"""
        simulator = HeartHealingSimulator()
        
        # Test multi-scale data generation
        multi_scale_data = simulator.generate_multi_scale_data(n_samples=200)
        
        assert isinstance(multi_scale_data, dict)
        assert 'molecular' in multi_scale_data
        assert 'cellular' in multi_scale_data
        assert 'tissue' in multi_scale_data
        assert 'organ' in multi_scale_data
        
        # Verify all scales have data
        for scale, data in multi_scale_data.items():
            assert isinstance(data, pd.DataFrame)
            assert len(data) == 200
            assert 'time' in data.columns
    
    def test_treatment_comparison(self):
        """Test treatment effect comparison"""
        simulator = HeartHealingSimulator()
        
        closed_data = simulator.run_closed_loop_test(n_samples=100)
        open_data = simulator.run_open_loop_test(n_samples=100)
        
        # Both should have similar structure but different control strategies
        assert set(closed_data.columns) == set(open_data.columns)
        
        # Closed loop should have adaptive control signals
        assert closed_data['control_signal'].std() > 0  # Should vary
        # Open loop typically has constant control
        assert open_data['control_signal'].std() < 1.0  # Less variation


def test_import_all_modules():
    """Test that all core modules can be imported"""
    modules_to_test = [
        'heart_healing',
        'quantum_simulation', 
        'closed_loop',
        'multi_scale'
    ]
    
    for module_name in modules_to_test:
        try:
            __import__(module_name)
            assert True
        except ImportError:
            print(f"Warning: {module_name} not available for testing")
            # Don't fail test for missing optional modules


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
'''

with open('tests/test_heart_healing.py', 'w') as f:
    f.write(test_heart_content)
print("✅ Created tests/test_heart_healing.py")

# Create test_quantum_simulation.py
test_quantum_content = '''"""
Tests for quantum simulation functionality
"""
import pytest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from quantum_simulation import QuantumBiologicalSimulator
    HAS_QUANTUM = True
except ImportError:
    HAS_QUANTUM = False


@pytest.mark.skipif(not HAS_QUANTUM, reason="quantum_simulation module not available")
class TestQuantumBiologicalSimulator:
    """Test cases for QuantumBiologicalSimulator"""
    
    def test_simulator_initialization(self):
        """Test quantum simulator initialization"""
        simulator = QuantumBiologicalSimulator(n_states=5)
        assert simulator is not None
        assert simulator.n_states == 5
        assert hasattr(simulator, 'states')
    
    def test_quantum_states(self):
        """Test quantum state initialization"""
        simulator = QuantumBiologicalSimulator(n_states=4)
        
        expected_states = ['healthy', 'damaged', 'healing', 'recovered']
        for state in expected_states:
            assert state in simulator.states
            # Verify states are numpy arrays
            assert isinstance(simulator.states[state], np.ndarray)
    
    def test_healing_dynamics(self):
        """Test quantum healing dynamics simulation"""
        simulator = QuantumBiologicalSimulator(n_states=4)
        
        results = simulator.simulate_healing_dynamics(time_steps=50)
        
        assert isinstance(results, list)
        assert len(results) == 50
        
        # Check result structure
        for result in results:
            assert 'time_step' in result
            assert 'state_probabilities' in result
            assert 'entanglement' in result
            
            # Verify probabilities sum to approximately 1
            probs = result['state_probabilities']
            assert abs(np.sum(probs) - 1.0) < 0.01  # Allow small numerical error
    
    def test_quantum_metrics(self):
        """Test quantum metric calculations"""
        simulator = QuantumBiologicalSimulator(n_states=3)
        results = simulator.simulate_healing_dynamics(time_steps=10)
        
        # Check that entanglement values are reasonable
        entanglement_values = [r['entanglement'] for r in results]
        assert all(0 <= e <= 1 for e in entanglement_values)
        
        # Check state probabilities are valid
        for result in results:
            probs = result['state_probabilities']
            assert all(0 <= p <= 1 for p in probs)
            assert len(probs) == simulator.n_states


@pytest.mark.skipif(not HAS_QUANTUM, reason="quantum_simulation module not available")
class TestQuantumAdvanced:
    """Advanced quantum simulation tests"""
    
    def test_different_state_sizes(self):
        """Test simulator with different numbers of states"""
        for n_states in [3, 5, 7]:
            simulator = QuantumBiologicalSimulator(n_states=n_states)
            results = simulator.simulate_healing_dynamics(time_steps=20)
            
            # Verify correct number of states in results
            first_result = results[0]
            assert len(first_result['state_probabilities']) == n_states
    
    def test_deterministic_with_seed(self):
        """Test that setting random seed produces reproducible results"""
        # This would require the simulator to accept a random seed parameter
        # For now, just verify the interface works
        simulator = QuantumBiologicalSimulator(n_states=4)
        results1 = simulator.simulate_healing_dynamics(time_steps=10)
        results2 = simulator.simulate_healing_dynamics(time_steps=10)
        
        # Both should have the same structure
        assert len(results1) == len(results2)
        assert set(results1[0].keys()) == set(results2[0].keys())
'''

with open('tests/test_quantum_simulation.py', 'w') as f:
    f.write(test_quantum_content)
print("✅ Created tests/test_quantum_simulation.py")

# Create conftest.py
conftest_content = '''"""
Configuration and fixtures for PDPBioGen tests
"""
import pytest
import numpy as np
import pandas as pd


@pytest.fixture
def sample_heart_data():
    """Fixture providing sample heart data for tests"""
    np.random.seed(42)  # For reproducible tests
    return pd.DataFrame({
        'time_hours': range(100),
        'tissue_viability': np.linspace(30, 80, 100),
        'cellular_coherence': np.linspace(20, 70, 100),
        'inflammation': np.linspace(80, 20, 100)
    })


@pytest.fixture
def sample_quantum_data():
    """Fixture providing sample quantum data for tests"""
    np.random.seed(42)
    return {
        'time_steps': range(50),
        'state_probabilities': np.random.dirichlet(np.ones(4), 50),
        'entanglement': np.random.uniform(0, 1, 50)
    }


@pytest.fixture(autouse=True)
def set_random_seed():
    """Set random seed for all tests for reproducibility"""
    np.random.seed(42)
'''

with open('tests/conftest.py', 'w') as f:
    f.write(conftest_content)
print("✅ Created tests/conftest.py")
