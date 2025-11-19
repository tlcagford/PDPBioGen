#!/usr/bin/env python3
"""Test the fixed PDPBioGen structure."""

import os
import sys
import tempfile
import yaml
import pytest

# Add the parent directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_imports():
    """Test that all modules can be imported without circular imports."""
    print("Testing imports...")
    
    # Test basic imports
    from pdpbiogen import __version__, PDPBioGenError
    assert __version__ == "0.1.0"
    
    # Test module imports
    from pdpbiogen.exceptions import ConfigurationError, GraphvizError, ValidationError
    from pdpbiogen.validator import PathwayValidator
    from pdpbiogen.logger import setup_logger, logger
    
    print("✓ All imports successful")

def test_configuration_validation():
    """Test configuration validation."""
    from pdpbiogen.validator import PathwayValidator
    
    # Valid configuration
    valid_config = {
        'molecules': {
            'ProteinA': {'color': 'blue'},
            'ProteinB': {'type': 'output'}
        },
        'interactions': [
            {'from': 'ProteinA', 'to': 'ProteinB', 'label': 'Activates'}
        ]
    }
    
    # Should not raise
    PathwayValidator.validate_configuration(valid_config)
    print("✓ Configuration validation working")

def test_diagram_creation():
    """Test diagram creation with sample data."""
    from pdpbiogen.pdpbiogen import create_diagram
    
    sample_data = {
        'molecules': {
            'Ligand': {'type': 'input', 'color': 'lightblue'},
            'Receptor': {'color': 'lightgreen'},
            'Response': {'type': 'output', 'color': 'lightcoral'}
        },
        'interactions': [
            {'from': 'Ligand', 'to': 'Receptor', 'label': 'Binds'},
            {'from': 'Receptor', 'to': 'Response', 'label': 'Activates'}
        ]
    }
    
    dot = create_diagram(sample_data)
    assert dot is not None
    print("✓ Diagram creation working")

def test_cli_interface():
    """Test CLI interface."""
    from pdpbiogen.cli import create_parser, load_configuration
    
    # Test parser
    parser = create_parser()
    args = parser.parse_args(['test.yaml', 'output'])
    assert args.input_yaml == 'test.yaml'
    assert args.output_basename == 'output'
    
    print("✓ CLI interface working")

def test_integration():
    """Test full integration with temporary files."""
    from pdpbiogen.pdpbiogen import load_configuration, create_diagram
    
    # Create temporary YAML file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump({
            'molecules': {
                'Gene': {'type': 'input', 'color': 'lightblue'},
                'mRNA': {'color': 'lightyellow'},
                'Protein': {'type': 'output', 'color': 'lightgreen'}
            },
            'interactions': [
                {'from': 'Gene', 'to': 'mRNA', 'label': 'Transcribed'},
                {'from': 'mRNA', 'to': 'Protein', 'label': 'Translated'}
            ]
        }, f)
        temp_yaml = f.name
    
    try:
        # Test loading
        data = load_configuration(temp_yaml)
        assert 'molecules' in data
        assert 'interactions' in data
        
        # Test diagram creation
        dot = create_diagram(data)
        assert dot is not None
        
        # Test rendering (just SVG for speed)
        with tempfile.NamedTemporaryFile(delete=False) as f:
            output_base = f.name
        
        try:
            dot.render(output_base, format='svg', cleanup=True)
            assert os.path.exists(output_base + '.svg')
            print("✓ Full integration test passed")
        finally:
            if os.path.exists(output_base + '.svg'):
                os.unlink(output_base + '.svg')
    
    finally:
        if os.path.exists(temp_yaml):
            os.unlink(temp_yaml)

if __name__ == '__main__':
    print("Testing fixed PDPBioGen structure...")
    
    try:
        test_imports()
        test_configuration_validation()
        test_diagram_creation()
        test_cli_interface()
        test_integration()
        
        print("\n🎉 All tests passed! The structure is working correctly.")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
