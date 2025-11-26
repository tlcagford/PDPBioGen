# Add to the if __name__ == "__main__" section:
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate protein domain plots with enhanced features')
    parser.add_argument('fasta_file', help='Input FASTA file')
    parser.add_argument('--output', '-o', default='protein_domains.html', help='Output HTML file')
    parser.add_argument('--static', '-s', help='Base name for static exports (PNG, PDF, SVG)')
    parser.add_argument('--min-length', '-m', type=int, default=0, help='Minimum domain length to include')
    parser.add_argument('--no-group', action='store_false', dest='group', help='Disable domain grouping')
    parser.add_argument('--width', type=int, default=1000, help='Figure width')
    
    args = parser.parse_args()
    
    generate_protein_domain_plot(
        args.fasta_file,
        output_html=args.output,
        output_static=args.static,
        min_domain_length=args.min_length,
        group_similar=args.group,
        figure_width=args.width
    )
