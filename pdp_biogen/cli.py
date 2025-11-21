#!/usr/bin/env python3
import argparse
import sys
import json
from pathlib import Path
from .generator import BiographyGenerator

def main():
    parser = argparse.ArgumentParser(
        description='Generate professional biographies for profile pages',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  pdp-biogen --name "Dr. Jane Smith" --role "Professor" --institution "Stanford University" --expertise "machine learning and artificial intelligence"
  pdp-biogen --name "John Doe" --role "CTO" --institution "Tech Corp" --expertise "cloud infrastructure" --style corporate --output bio.md
  pdp-biogen --input researcher.json --output biography.txt
        """
    )
    
    # Input methods
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('--input', help='JSON file with biography parameters')
    input_group.add_argument('--name', help='Full name of the person')
    
    # Required if using individual args
    parser.add_argument('--role', help='Professional role or title')
    parser.add_argument('--institution', help='Company or academic institution')
    parser.add_argument('--expertise', help='Area of expertise or research interests')
    
    # Optional arguments
    parser.add_argument('--style', choices=['academic', 'corporate', 'short'], 
                       default='academic', help='Style of biography (default: academic)')
    parser.add_argument('--output', help='Output file path (optional)')
    parser.add_argument('--model', help='OpenAI model to use (default: gpt-3.5-turbo)')
    
    args = parser.parse_args()
    
    try:
        # Load parameters
        if args.input:
            with open(args.input, 'r') as f:
                params = json.load(f)
        else:
            if not all([args.role, args.institution, args.expertise]):
                parser.error("--role, --institution, and --expertise are required with --name")
            params = {
                'name': args.name,
                'role': args.role,
                'institution': args.institution,
                'expertise': args.expertise
            }
        
        # Generate biography
        generator = BiographyGenerator()
        print("Generating biography...")
        
        biography = generator.generate(style=args.style, **params)
        
        # Output results
        if args.output:
            Path(args.output).write_text(biography, encoding='utf-8')
            print(f"✓ Biography saved to: {args.output}")
        else:
            print("\n" + "="*60)
            print(biography)
            print("="*60)
            
    except FileNotFoundError:
        print(f"Error: Input file not found: {args.input}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in input file: {args.input}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
