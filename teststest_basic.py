import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class TestBasicFunctionality(unittest.TestCase):
    def test_import(self):
        """Test that main modules can be imported"""
        try:
            from quantum_healing import QuantumCTHealingSystem
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Import failed: {e}")

if __name__ == '__main__':
    unittest.main()