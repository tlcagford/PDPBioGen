#!/usr/bin/env python3
"""
PDPBioGen - Protein Domain Plot Generator
Enhanced version with static exports, domain filtering, and better visualization
"""

import subprocess
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from Bio import SeqIO
import os
import argparse


def run_interproscan(fasta_file):
    """
    Run InterProScan on the input FASTA file
    """
    output_file = f"{fasta_file}.interproscan.tsv"
    
    if os.path.exists(output_file):
        print(f"Using existing InterProScan results: {output_file}")
        return output_file
    
    print("Running InterProScan...")
    cmd = [
        "interproscan.sh",
        "-i", fasta_file,
        "-f", "tsv",
        "-o", output_file,
        "--goterms",
        "--pathways"
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"InterProScan completed: {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error running InterProScan: {e}")
        raise
    except FileNotFoundError:
        print("InterProScan not found. Please install InterProScan and ensure it's in your PATH.")
        raise


def parse_interpro_output(interpro_output):
    """
    Parse InterProScan TSV output into a DataFrame
    """
    columns = [
        'protein', 'md5', 'length', 'database', 'domain_name', 
        'accession', 'start', 'end', 'evalue', 'date', 'description'
    ]
    
    df = pd.read_csv(interpro_output, sep='\t', header=None, names=columns)
    
    # Filter for domain entries (remove other feature types)
    domain_databases = ['Pfam', 'SMART', 'PROSITE', 'PANTHER', 'CDD', 'TIGRFAM']
    domains_df = df[df['database'].isin(domain_databases)].copy()
    
    # Convert positions to integers
    domains_df['start'] = domains_df['start'].astype(int)
    domains_df['end'] = domains_df['end'].astype(int)
    
    return domains_df


def filter_domains(domains_df, min_length=0, group_repeats=True):
    """
    Filter and group domains for better visualization
    """
    filtered_df = domains_df.copy()
    
    # Filter by minimum length
    if min_length > 0:
        initial_count = len(filtered_df)
        filtered_df = filtered_df[
            (filtered_df['end'] - filtered_df['start']) >= min_length
        ]
        removed = initial_count - len(filtered_df)
        if removed > 0:
            print(f"Filtered out {removed} domains shorter than {min_length} amino acids")
    
    # Group identical consecutive domains
    if group_repeats and len(filtered_df) > 1:
        filtered_df = filtered_df.sort_values('start').reset_index(drop=True)
        grouped_domains = []
        i = 0
        
        while i < len(filtered_df):
            current_domain = filtered_df.iloc[i]
            count = 1
            
            # Count consecutive identical domains
            while (i + count < len(filtered_df) and
                   filtered_df.iloc[i + count]['domain_name'] == current_domain['domain_name'] and
                   (filtered_df.iloc[i + count]['start'] - filtered_df.iloc[i + count - 1]['end']) < 50):
                count += 1
            
            if count > 1:
                # Merge consecutive domains
                merged_domain = current_domain.copy()
                merged_domain['end'] = filtered_df.iloc[i + count - 1]['end']
                merged_domain['domain_name'] = f"{current_domain['domain_name']} (x{count})"
                grouped_domains.append(merged_domain)
                print(f"Grouped {count} consecutive {current_domain['domain_name']} domains")
            else:
                grouped_domains.append(current_domain)
            
            i += count
        
        filtered_df = pd.DataFrame(grouped_domains)
    
    return filtered_df


def create_protein_domain_plot(domains_df, protein_length, width=1000, height=None):
    """
    Create an interactive protein domain architecture plot
    """
    # Auto-adjust height based on number of domains
    if height is None:
        height = max(400, len(domains_df) * 30 + 150)
    
    # Enhanced color scheme with 24 distinct colors
    expanded_colors = [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
        '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#393b79', '#637939',
        '#8c6d31', '#843c39', '#7b4173', '#5254a3', '#6b6ecf', '#9c9ede',
        '#3182bd', '#e6550d', '#31a354', '#756bb1', '#636363', '#bd9e39'
    ]
    
    # Create color mapping
    unique_domains = domains_df['domain_name'].unique()
    color_mapping = {}
    for i, domain in enumerate(unique_domains):
        color_mapping[domain] = expanded_colors[i % len(expanded_colors)]
    
    fig = go.Figure()
    
    # Add each domain as a shape
    for i, (idx, row) in enumerate(domains_df.iterrows()):
        fig.add_trace(go.Scatter(
            x=[row['start'], row['end'], row['end'], row['start'], row['start']],
            y=[i, i, i+0.8, i+0.8, i],
            fill="toself",
            fillcolor=color_mapping[row['domain_name']],
            line=dict(color='black', width=1),
            name=row['domain_name'],
            hoverinfo="text",
            hovertext=(
                f"<b>{row['domain_name']}</b><br>"
                f"Database: {row['database']}<br>"
                f"Position: {row['start']}-{row['end']}<br>"
                f"Length: {row['end'] - row['start'] + 1} aa<br>"
                f"Accession: {row.get('accession', 'N/A')}<br>"
                f"Description: {row.get('description', 'N/A')}"
            ),
            showlegend=False
        ))
    
    # Update layout
    fig.update_layout(
        width=width,
        height=height,
        title={
            'text': "Protein Domain Architecture",
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_title="Amino Acid Position",
        yaxis=dict(
            showticklabels=False,
            showgrid=False,
            zeroline=False
        ),
        hovermode="closest",
        plot_bgcolor='white'
    )
    
    # Add protein length scale
    fig.add_shape(
        type="line",
        x0=0, y0=-0.5, x1=protein_length, y1=-0.5,
        line=dict(color="black", width=2)
    )
    
    # Add scale annotations
    fig.add_annotation(
        x=0, y=-0.8,
        text="0",
        showarrow=False,
        font=dict(size=10)
    )
    
    fig.add_annotation(
        x=protein_length, y=-0.8,
        text=str(protein_length),
        showarrow=False,
        font=dict(size=10)
    )
    
    return fig


def export_static_plots(fig, base_name, width=1000, height=400):
    """
    Export plot to multiple static formats for publications
    """
    try:
        import plotly.io as pio
        
        export_formats = {
            'png': {'format': 'png', 'scale': 2},
            'pdf': {'format': 'pdf'},
            'svg': {'format': 'svg'},
            'jpeg': {'format': 'jpeg', 'scale': 2}
        }
        
        for fmt, params in export_formats.items():
            filename = f"{base_name}.{fmt}"
            pio.write_image(fig, filename, width=width, height=height, **params)
            print(f"✓ Static plot saved: {filename}")
            
    except ImportError:
        print("✗ Kaleido not installed. Install with: pip install kaleido")
    except Exception as e:
        print(f"✗ Error exporting static plots: {e}")


def generate_protein_domain_plot(fasta_file, output_html="protein_domains.html", 
                               output_static=None, min_domain_length=0, 
                               group_similar=True, width=1000, height=None):
    """
    Generate protein domain architecture plot with enhanced features
    
    Args:
        fasta_file: Input FASTA file
        output_html: Output HTML filename
        output_static: Base name for static exports
        min_domain_length: Minimum domain length to include
        group_similar: Group consecutive identical domains
        width: Figure width
        height: Figure height (auto-calculated if None)
    """
    try:
        # Parse FASTA file
        record = SeqIO.read(fasta_file, "fasta")
        protein_length = len(record.seq)
        print(f"Processing: {record.id}")
        print(f"Protein length: {protein_length} amino acids")
        
        # Run InterProScan
        interpro_output = run_interproscan(fasta_file)
        
        # Parse domains
        domains_df = parse_interpro_output(interpro_output)
        print(f"Found {len(domains_df)} domains")
        
        # Apply domain filtering and grouping
        if min_domain_length > 0 or group_similar:
            domains_df = filter_domains(
                domains_df, 
                min_length=min_domain_length,
                group_repeats=group_similar
            )
            print(f"Displaying {len(domains_df)} domains after processing")
        
        # Create visualization
        fig = create_protein_domain_plot(
            domains_df, 
            protein_length, 
            width=width, 
            height=height
        )
        
        # Save interactive HTML
        fig.write_html(output_html)
        print(f"✓ Interactive plot saved: {output_html}")
        
        # Export static formats if requested
        if output_static:
            plot_height = height if height else max(400, len(domains_df) * 30 + 150)
            export_static_plots(fig, output_static, width=width, height=plot_height)
        
        # Save domain data to CSV
        csv_file = output_html.replace('.html', '_domains.csv')
        domains_df.to_csv(csv_file, index=False)
        print(f"✓ Domain data saved: {csv_file}")
        
        return fig, domains_df
        
    except Exception as e:
        print(f"Error generating protein domain plot: {e}")
        raise


def main():
    """Command line interface"""
    parser = argparse.ArgumentParser(
        description='Generate enhanced protein domain architecture plots',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage
  python pdpbiogen.py protein.fasta
  
  # With static exports and filtering
  python pdpbiogen.py protein.fasta --static my_plot --min-length 50 --width 1200
  
  # Publication-ready with custom output
  python pdpbiogen.py protein.fasta -o domains.html --static publication --no-group
        """
    )
    
    parser.add_argument('fasta_file', help='Input FASTA file')
    
    parser.add_argument('--output', '-o', default='protein_domains.html',
                       help='Output HTML filename (default: protein_domains.html)')
    
    parser.add_argument('--static', 
                       help='Base name for static exports (PNG, PDF, SVG, JPEG)')
    
    parser.add_argument('--min-length', type=int, default=0,
                       help='Minimum domain length to display (default: 0)')
    
    parser.add_argument('--no-group', action='store_false', dest='group',
                       help='Disable grouping of consecutive identical domains')
    
    parser.add_argument('--width', type=int, default=1000,
                       help='Figure width in pixels (default: 1000)')
    
    parser.add_argument('--height', type=int,
                       help='Figure height in pixels (auto-calculated if not specified)')
    
    args = parser.parse_args()
    
    generate_protein_domain_plot(
        fasta_file=args.fasta_file,
        output_html=args.output,
        output_static=args.static,
        min_domain_length=args.min_length,
        group_similar=args.group,
        width=args.width,
        height=args.height
    )


if __name__ == "__main__":
    main()