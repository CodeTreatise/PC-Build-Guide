#!/usr/bin/env python3
"""
PC Build Guide - Main Application
Entry point for the PC component analysis and guide generation system
"""

import argparse
import sys
import os
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / 'src'))

from src.scrapers.amazon_scraper import AmazonIndiaScraper
from src.analysis.component_analyzer import ComponentAnalyzer
from src.utils.helpers import setup_logging, ensure_data_dir
import config

def main():
    """Main application entry point"""
    parser = argparse.ArgumentParser(description="PC Build Guide - Component Analysis Tool")
    
    # Add subcommands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Scrape command
    scrape_parser = subparsers.add_parser('scrape', help='Scrape component data')
    scrape_parser.add_argument('component', choices=['cpu', 'gpu', 'motherboard', 'ram', 'storage', 'psu', 'case', 'cooling'], 
                              help='Component type to scrape')
    scrape_parser.add_argument('--query', required=True, help='Search query')
    scrape_parser.add_argument('--pages', type=int, default=3, help='Number of pages to scrape')
    scrape_parser.add_argument('--output', help='Output CSV file')
    
    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze component data')
    analyze_parser.add_argument('input_file', help='Input CSV file with component data')
    analyze_parser.add_argument('--component-type', required=True, 
                               choices=['cpu', 'gpu', 'motherboard', 'ram', 'storage', 'psu', 'case', 'cooling'])
    
    # Generate docs command
    docs_parser = subparsers.add_parser('docs', help='Generate documentation')
    docs_parser.add_argument('--serve', action='store_true', help='Serve documentation locally')
    docs_parser.add_argument('--build', action='store_true', help='Build static documentation')
    
    # Price tracking command
    price_parser = subparsers.add_parser('track', help='Track component prices')
    price_parser.add_argument('--component', required=True, help='Component to track')
    price_parser.add_argument('--alert-threshold', type=float, default=10.0, 
                             help='Price change percentage to trigger alert')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Setup logging and data directory
    logger = setup_logging('main')
    ensure_data_dir()
    
    try:
        if args.command == 'scrape':
            run_scraping(args, logger)
        elif args.command == 'analyze':
            run_analysis(args, logger)
        elif args.command == 'docs':
            run_docs(args, logger)
        elif args.command == 'track':
            run_price_tracking(args, logger)
    except KeyboardInterrupt:
        logger.info("Operation cancelled by user")
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        sys.exit(1)

def run_scraping(args, logger):
    """Run component scraping"""
    logger.info(f"Starting scraping for {args.component} with query: {args.query}")
    
    # Initialize scraper
    scraper = AmazonIndiaScraper()
    
    # Perform search
    products = scraper.search_products(args.query, max_pages=args.pages)
    
    if not products:
        logger.warning("No products found")
        return
    
    logger.info(f"Found {len(products)} products")
    
    # Save results
    output_file = args.output or f"data/components/{args.component}_{args.query.replace(' ', '_')}.csv"
    scraper.save_products_to_csv(products, output_file)
    
    logger.info(f"Results saved to {output_file}")

def run_analysis(args, logger):
    """Run component analysis"""
    logger.info(f"Analyzing {args.component_type} data from {args.input_file}")
    
    if not os.path.exists(args.input_file):
        logger.error(f"Input file not found: {args.input_file}")
        return
    
    # Initialize analyzer
    analyzer = ComponentAnalyzer()
    
    # Load and analyze data
    import pandas as pd
    df = pd.read_csv(args.input_file)
    
    logger.info(f"Loaded {len(df)} products for analysis")
    
    # Perform analysis based on component type
    analyzed_data = []
    
    for _, row in df.iterrows():
        try:
            if args.component_type == 'cpu':
                specs = analyzer.analyze_cpu(row['title'], row.to_dict())
                analyzed_data.append(specs)
            elif args.component_type == 'gpu':
                specs = analyzer.analyze_gpu(row['title'], row.to_dict())
                analyzed_data.append(specs)
            elif args.component_type == 'motherboard':
                specs = analyzer.analyze_motherboard(row['title'], row.to_dict())
                analyzed_data.append(specs)
        except Exception as e:
            logger.warning(f"Error analyzing product {row['title']}: {str(e)}")
            continue
    
    logger.info(f"Successfully analyzed {len(analyzed_data)} products")
    
    # Save analyzed data
    output_file = args.input_file.replace('.csv', '_analyzed.csv')
    analyzed_df = pd.DataFrame([vars(item) for item in analyzed_data])
    analyzed_df.to_csv(output_file, index=False)
    
    logger.info(f"Analysis results saved to {output_file}")

def run_docs(args, logger):
    """Run documentation generation"""
    if args.serve:
        logger.info("Starting documentation server...")
        os.system("cd docs && python -m mkdocs serve")
    elif args.build:
        logger.info("Building documentation...")
        os.system("cd docs && python -m mkdocs build")
    else:
        logger.info("Use --serve to start server or --build to build docs")

def run_price_tracking(args, logger):
    """Run price tracking"""
    logger.info(f"Starting price tracking for {args.component}")
    
    # This would implement the price tracking logic
    # For now, just a placeholder
    logger.info("Price tracking feature coming soon!")

def quick_start():
    """Quick start function for common tasks"""
    print("🖥️  PC Build Guide - Quick Start")
    print("=" * 50)
    print()
    print("Common commands:")
    print("1. Scrape GPU prices:")
    print("   python main.py scrape gpu --query 'RTX 4060 graphics card'")
    print()
    print("2. Scrape CPU data:")
    print("   python main.py scrape cpu --query 'Ryzen 5 7600X processor'")
    print()
    print("3. Analyze scraped data:")
    print("   python main.py analyze data/components/gpu_data.csv --component-type gpu")
    print()
    print("4. Start documentation server:")
    print("   python main.py docs --serve")
    print()
    print("For full help: python main.py --help")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        quick_start()
    else:
        main()
