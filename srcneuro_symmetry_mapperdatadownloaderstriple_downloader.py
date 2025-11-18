#!/usr/bin/env python3
"""
Triple Domain Data Downloader
Downloads neural, genomic, and metabolic data in parallel
"""

import os
import argparse
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from ..processors.data_normalizer import CrossDomainNormalizer

class TripleDomainDownloader:
    def __init__(self, data_dir="./data", download_all=True):
        self.data_dir = data_dir
        self.download_all = download_all
        self.setup_directories()
        
    def setup_directories(self):
        """Create organized directory structure"""
        dirs = ['neural', 'genomic', 'metabolic', 'processed', 'tmp']
        for domain in dirs:
            os.makedirs(os.path.join(self.data_dir, domain), exist_ok=True)
    
    def download_neural_data(self):
        """Download neural datasets"""
        from .neural_downloader import NeuralDownloadAgent
        agent = NeuralDownloadAgent(self.data_dir)
        return agent.download()
    
    def download_genomic_data(self):
        """Download genomic/proteomic datasets"""
        from .genomic_downloader import GenomicDownloadAgent
        agent = GenomicDownloadAgent(self.data_dir)
        return agent.download()
    
    def download_metabolic_data(self):
        """Download metabolic datasets"""
        from .metabolic_downloader import MetabolicDownloadAgent
        agent = MetabolicDownloadAgent(self.data_dir)
        return agent.download()
    
    def download_all_domains(self):
        """Download all three domains in parallel"""
        print("🚀 Starting triple-domain data download...")
        
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = {
                'neural': executor.submit(self.download_neural_data),
                'genomic': executor.submit(self.download_genomic_data),
                'metabolic': executor.submit(self.download_metabolic_data)
            }
            
            results = {}
            for domain, future in tqdm(futures.items(), desc="Downloading domains"):
                results[domain] = future.result()
                print(f"✅ {domain.capitalize()} data downloaded")
        
        return results
    
    def normalize_and_integrate(self, raw_data):
        """Normalize data across domains"""
        normalizer = CrossDomainNormalizer()
        normalized_data = normalizer.process(raw_data)
        return normalized_data

def main():
    parser = argparse.ArgumentParser(description='Download triple-domain biological data')
    parser.add_argument('--data-dir', default='./data', help='Data directory')
    parser.add_argument('--domains', nargs='+', choices=['neural', 'genomic', 'metabolic', 'all'],
                       default=['all'], help='Domains to download')
    args = parser.parse_args()
    
    downloader = TripleDomainDownloader(args.data_dir)
    
    if 'all' in args.domains:
        raw_data = downloader.download_all_domains()
    else:
        raw_data = {}
        if 'neural' in args.domains:
            raw_data['neural'] = downloader.download_neural_data()
        if 'genomic' in args.domains:
            raw_data['genomic'] = downloader.download_genomic_data()
        if 'metabolic' in args.domains:
            raw_data['metabolic'] = downloader.download_metabolic_data()
    
    # Normalize and integrate
    normalized_data = downloader.normalize_and_integrate(raw_data)
    print("🎉 Data download and normalization complete!")
    print(f"📁 Data saved to: {args.data_dir}")

if __name__ == "__main__":
    main()