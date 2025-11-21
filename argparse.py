def main():
    parser = argparse.ArgumentParser(description='Generate academic biography')
    parser.add_argument('--name', required=True, help='Researcher name')
    parser.add_argument('--role', required=True, help='Academic role')
    parser.add_argument('--institution', required=True, help='Institution name')
    parser.add_argument('--research', required=True, help='Research interests')
    parser.add_argument('--output', help='Output file (optional)')
    
    args = parser.parse_args()
    
    # Your existing logic here using args.name, args.role, etc.

if __name__ == "__main__":
    main()
