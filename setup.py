"""
Initial setup script for PC Build Guide project
Creates necessary directories and downloads initial data
"""

import os
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / 'src'))

from src.utils.helpers import setup_logging, ensure_data_dir, save_to_json
from src.scrapers.amazon_scraper import AmazonIndiaScraper
import config

def create_directory_structure():
    """Create the required directory structure"""
    logger = setup_logging('setup')
    logger.info("Creating directory structure...")
    
    directories = [
        'data/components',
        'data/benchmarks', 
        'data/prices',
        'data/compatibility',
        'logs',
        'docs/stylesheets',
        'docs/javascripts'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        logger.info(f"Created directory: {directory}")

def download_sample_data():
    """Download sample component data"""
    logger = setup_logging('setup')
    logger.info("Downloading sample component data...")
    
    scraper = AmazonIndiaScraper(delay=1.0)  # Faster for setup
    
    # Sample queries for different components
    sample_queries = {
        'gpu': ['RTX 4060 graphics card', 'RX 7600 graphics card'],
        'cpu': ['Ryzen 5 7600X processor', 'Intel Core i5 13400F'],
        'motherboard': ['B650 motherboard', 'B760 motherboard'],
        'ram': ['DDR5 32GB memory', 'DDR4 16GB memory'],
        'storage': ['1TB NVMe SSD', '2TB HDD'],
        'psu': ['650W power supply', '750W modular PSU']
    }
    
    for component, queries in sample_queries.items():
        logger.info(f"Scraping {component} data...")
        
        all_products = []
        for query in queries:
            try:
                products = scraper.search_products(query, max_pages=2)
                all_products.extend(products)
                logger.info(f"Found {len(products)} products for query: {query}")
            except Exception as e:
                logger.warning(f"Error scraping {query}: {str(e)}")
                continue
        
        if all_products:
            # Save to CSV
            output_file = f"data/components/{component}_sample.csv"
            scraper.save_products_to_csv(all_products, output_file)
            logger.info(f"Saved {len(all_products)} products to {output_file}")

def create_sample_configs():
    """Create sample configuration files"""
    logger = setup_logging('setup')
    logger.info("Creating sample configuration files...")
    
    # Sample build configurations
    build_configs = {
        'budget_gaming': {
            'budget': 60000,
            'use_case': 'budget_gaming',
            'target_resolution': '1080p',
            'target_fps': 60,
            'components': {
                'cpu': 'AMD Ryzen 5 5600',
                'gpu': 'NVIDIA RTX 4060',
                'motherboard': 'MSI B550M Pro-B',
                'ram': '16GB DDR4-3200',
                'storage': '500GB NVMe SSD',
                'psu': '650W 80+ Bronze',
                'case': 'Cooler Master MasterBox Q300L'
            }
        },
        'mid_range_gaming': {
            'budget': 120000,
            'use_case': 'mid_range_gaming',
            'target_resolution': '1440p',
            'target_fps': 60,
            'components': {
                'cpu': 'AMD Ryzen 7 7700X',
                'gpu': 'NVIDIA RTX 4070',
                'motherboard': 'ASUS TUF Gaming B650-Plus',
                'ram': '32GB DDR5-5600',
                'storage': '1TB NVMe SSD',
                'psu': '750W 80+ Gold Modular',
                'case': 'Fractal Design Core 1000'
            }
        }
    }
    
    save_to_json(build_configs, 'data/sample_builds.json')
    logger.info("Sample build configurations created")
    
    # Component compatibility matrix sample
    compatibility_matrix = {
        'intel_lga1700': {
            'compatible_cpus': ['12th Gen Intel', '13th Gen Intel', '14th Gen Intel'],
            'compatible_memory': ['DDR4', 'DDR5'],
            'compatible_coolers': ['LGA1700 mount required']
        },
        'amd_am5': {
            'compatible_cpus': ['Ryzen 7000 series', 'Ryzen 8000 series'],
            'compatible_memory': ['DDR5 only'],
            'compatible_coolers': ['AM5 mount or AM4 with adapter']
        }
    }
    
    save_to_json(compatibility_matrix, 'data/compatibility/socket_compatibility.json')
    logger.info("Sample compatibility matrix created")

def setup_development_environment():
    """Setup development environment"""
    logger = setup_logging('setup')
    logger.info("Setting up development environment...")
    
    # Create .env file template
    env_template = """# PC Build Guide Environment Configuration

# Web Scraping Settings
USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
REQUEST_DELAY=2
TIMEOUT=30

# API Keys (optional)
# AMAZON_API_KEY=your_amazon_api_key
# PRICE_TRACKING_API_KEY=your_price_api_key

# Database Settings
DATABASE_PATH=data/pc_components.db

# Logging Level
LOG_LEVEL=INFO

# Documentation Settings
DOCS_PORT=8000
"""
    
    with open('.env.template', 'w') as f:
        f.write(env_template)
    
    logger.info("Environment template created")

def main():
    """Main setup function"""
    print("🖥️  PC Build Guide - Initial Setup")
    print("=" * 50)
    
    try:
        # Create directory structure
        create_directory_structure()
        
        # Setup development environment
        setup_development_environment()
        
        # Create sample configurations
        create_sample_configs()
        
        # Ask user if they want to download sample data
        download_data = input("\nDownload sample component data? (y/n): ").lower().strip()
        
        if download_data == 'y':
            print("\n⚠️  This will make requests to e-commerce sites.")
            print("Please be respectful and don't run this frequently.")
            confirm = input("Continue? (y/n): ").lower().strip()
            
            if confirm == 'y':
                download_sample_data()
            else:
                print("Skipping sample data download.")
        
        print("\n✅ Setup completed successfully!")
        print("\nNext steps:")
        print("1. Copy .env.template to .env and configure settings")
        print("2. Run 'python main.py --help' to see available commands")
        print("3. Start documentation server: 'python main.py docs --serve'")
        print("4. Begin scraping: 'python main.py scrape gpu --query \"RTX 4060\"'")
        
    except KeyboardInterrupt:
        print("\n❌ Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
