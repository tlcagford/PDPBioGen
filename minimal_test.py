#!/usr/bin/env python3
import sys
import os

print("🔍 System Information:")
print(f"Python: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Current dir: {os.getcwd()}")

try:
    print("\n📦 Testing basic imports...")
    import yaml
    print("✅ PyYAML imported")
    
    import graphviz
    print("✅ graphviz imported")
    
    # Test Graphviz functionality
    dot = graphviz.Digraph()
    dot.node('test')
    dot.render('/tmp/minimal_test', format='png', cleanup=True)
    print("✅ Graphviz working")
    
    print("\n🎉 All basic dependencies working!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Try: pip install pyyaml graphviz")
    
except Exception as e:
    print(f"❌ Error: {e}")
