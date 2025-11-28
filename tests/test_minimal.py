#!/usr/bin/env python3
"""
Minimal test for PDPBioGen components
"""
import sys
import os

def test_imports():
    """Test that required packages can be imported"""
    try:
        import pandas as pd
        import networkx as nx
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

if __name__ == "__main__":
    print("Running PDPBioGen minimal tests...")
    success = test_imports()
    sys.exit(0 if success else 1)
