#!/usr/bin/env python3
"""Command-line interface for PDPBioGen."""

import sys
import argparse
import logging
import yaml
import graphviz
import os

# Import after basic imports to avoid circular dependencies
from .logger import setup_logger

def create_parser():
    """Create command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="PDPBioGen - Programmatic Diagram Pathway Biologist Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  pdpbiogen pathway.yaml output_name
  pdpbiogen --format svg pathway.yaml diagram
  pdpbiogen --verbose --format png pathway.yaml result
        """
    )
    
    parser.add_argument(
        'input_yaml',
        help='Input YAML file containing pathway configuration'
    )
    
    parser.add_argument(
        'output_basename',
        help='Base name for output files (without extension)'
    )
    
    parser.add_argument(
        '--format', '-f',
        nargs='+',
        choices=['png', 'svg', 'pdf', 'all'],
        default=['png', 'svg'],
        help='Output format(s) (default: png svg)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    
    parser.add_argument(
        '--version',
        action='store_true',
        help='Show version information'
    )
    
    return parser

def load_configuration(input_file):
    """Load YAML configuration with error handling."""
    try:
        with open(input_file, 'r') as f:
            data = yaml.safe_load(f)
        
        if data is None:
            raise ValueError(f"YAML file '{input_file}' is empty or invalid")
        
        return data
        
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML in {input_file}: {e}")
    except FileNotFoundError:
        raise ValueError(f"Input file not found: {input_file}")
    except PermissionError:
        raise ValueError(f"Permission denied reading: {input_file}")

def create_diagram(data):
    """Create diagram from configuration data."""
    # Import here to avoid circular imports
    from .pdpbiogen import create_diagram as _create_diagram
    return _create_diagram(data)

def main():
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    # Handle version flag
    if args.version:
        from . import __version__
        print(f"PDPBioGen version {__version__}")
        return 0
    
    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logger = setup_logger(log_level)
    
    try:
        # Determine output formats
        formats = args.format
        if 'all' in formats:
            formats = ['png', 'svg', 'pdf']
        
        logger.info(f"Starting PDPBioGen processing")
        logger.debug(f"Input: {args.input_yaml}, Output: {args.output_basename}, Formats: {formats}")
        
        # Load configuration using local function
        data = load_configuration(args.input_yaml)
        
        # Create diagram using the main module
        dot = create_diagram(data)
        
        # Render outputs
        output_dir = os.path.dirname(args.output_basename) or '.'
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        
        for format in formats:
            output_path = dot.render(
                filename=args.output_basename,
                format=format,
                cleanup=True
            )
            logger.info(f"Generated {format.upper()} output: {output_path}")
        
        logger.info("PDPBioGen completed successfully")
        return 0
        
    except Exception as e:
        logger.error(f"Error: {e}")
        if args.verbose:
            logger.exception("Detailed traceback:")
        return 1

if __name__ == '__main__':
    sys.exit(main())
