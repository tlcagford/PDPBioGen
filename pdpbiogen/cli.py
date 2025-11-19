#!/usr/bin/env python3
"""Command-line interface for PDPBioGen."""

import sys
import argparse
import logging

from .pdpbiogen import load_configuration, create_diagram, render_diagram
from .exceptions import PDPBioGenError, ConfigurationError, GraphvizError, ValidationError
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
        
        # Load configuration
        data = load_configuration(args.input_yaml)
        
        # Create diagram
        dot = create_diagram(data)
        
        # Render outputs
        render_diagram(dot, args.output_basename, formats)
        
        logger.info("PDPBioGen completed successfully")
        return 0
        
    except ConfigurationError as e:
        logger.error(f"Configuration error: {e}")
        return 1
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        return 1
    except GraphvizError as e:
        logger.error(f"Graphviz error: {e}")
        return 1
    except PDPBioGenError as e:
        logger.error(f"PDPBioGen error: {e}")
        return 1
    except KeyboardInterrupt:
        logger.info("Processing interrupted by user")
        return 130
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        if args.verbose:
            logger.exception("Detailed traceback:")
        return 2

if __name__ == '__main__':
    sys.exit(main())
