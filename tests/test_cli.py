import pytest
import tempfile
import os
import sys
from unittest.mock import patch

from pdpbiogen.cli import main, create_parser

class TestCLI:
    
    def test_parser_creation(self):
        """Test argument parser creation."""
        parser = create_parser()
        assert parser is not None
    
    def test_parser_help(self):
        """Test help argument."""
        parser = create_parser()
        
        with pytest.raises(SystemExit):
            parser.parse_args(['--help'])
    
    def test_parser_version(self):
        """Test version argument."""
        parser = create_parser()
        args = parser.parse_args(['--version'])
        assert args.version is True
    
    def test_parser_defaults(self):
        """Test parser default values."""
        parser = create_parser()
        args = parser.parse_args(['input.yaml', 'output'])
        
        assert args.input_yaml == 'input.yaml'
        assert args.output_basename == 'output'
        assert args.format == ['png', 'svg']
        assert args.verbose is False
    
    def test_parser_custom_format(self):
        """Test custom format argument."""
        parser = create_parser()
        args = parser.parse_args(['--format', 'pdf', 'input.yaml', 'output'])
        
        assert args.format == ['pdf']
    
    def test_parser_verbose(self):
        """Test verbose argument."""
        parser = create_parser()
        args = parser.parse_args(['--verbose', 'input.yaml', 'output'])
        
        assert args.verbose is True
    
    @patch('pdpbiogen.cli.load_configuration')
    @patch('pdpbiogen.cli.create_diagram')
    @patch('pdpbiogen.cli.render_diagram')
    def test_cli_success(self, mock_render, mock_create, mock_load, temp_yaml_file, sample_config):
        """Test successful CLI execution."""
        yaml_file = temp_yaml_file(sample_config)
        
        try:
            # Mock the processing functions
            mock_dot = mock_create.return_value
            mock_load.return_value = sample_config
            
            # Run CLI with test arguments
            with patch('sys.argv', ['pdpbiogen', yaml_file, 'test_output']):
                exit_code = main()
            
            assert exit_code == 0
            mock_load.assert_called_once_with(yaml_file)
            mock_create.assert_called_once_with(sample_config)
            mock_render.assert_called_once()
            
        finally:
            os.unlink(yaml_file)
    
    @patch('pdpbiogen.cli.load_configuration')
    def test_cli_configuration_error(self, mock_load, temp_yaml_file):
        """Test CLI handling of configuration errors."""
        yaml_file = temp_yaml_file({'molecules': {'A': {}}})
        
        try:
            from pdpbiogen.exceptions import ConfigurationError
            
            # Mock configuration error
            mock_load.side_effect = ConfigurationError("Test error")
            
            with patch('sys.argv', ['pdpbiogen', yaml_file, 'test_output']):
                exit_code = main()
            
            assert exit_code == 1
            
        finally:
            os.unlink(yaml_file)
    
    def test_cli_missing_arguments(self):
        """Test CLI with missing arguments."""
        with patch('sys.argv', ['pdpbiogen']):
            exit_code = main()
        
        assert exit_code != 0  # Should return error code
