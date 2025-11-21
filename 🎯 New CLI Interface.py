# New powerful CLI
@click.group()
def cli():
    """PDPBioGen 2.0 - Production Phylogenetic Pipelines"""
    pass

@cli.command()
@click.option('--config', '-c', help='Pipeline configuration file')
@click.option('--preset', '-p', type=click.Choice(['standard', 'orthology', 'custom']))
@click.option('--output-dir', '-o', default='./results')
def run_pipeline(config, preset, output_dir):
    """Execute complete phylogenetic pipeline"""
    pipeline_config = load_config(config, preset)
    pipeline = PhylogeneticPipeline(pipeline_config, output_dir)
    result = pipeline.execute()
    
    if result.success:
        click.echo(f"✅ Pipeline completed successfully!")
        click.echo(f"📁 Results in: {output_dir}")
        click.echo(f"🌳 Tree file: {result.tree_file}")
        click.echo(f"📊 Alignment: {result.alignment_file}")
    else:
        click.echo(f"❌ Pipeline failed: {result.error}")

@cli.command()
def setup_database():
    """Setup local BLAST databases"""
    # Interactive local DB setup
    # Download and format common databases