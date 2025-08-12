"""
PC Build Guide - Main Configuration File
Centralized configuration for web scraping, data sources, and project settings
"""

import os
from typing import Dict, List

# Project Settings
PROJECT_NAME = "PC Build Guide"
VERSION = "1.0.0"
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
DOCS_DIR = os.path.join(os.path.dirname(__file__), "docs")

# Web Scraping Settings
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
REQUEST_DELAY = 2  # Seconds between requests
TIMEOUT = 30  # Request timeout in seconds

# Indian E-commerce Sites
ECOMMERCE_SITES = {
    "amazon_in": {
        "base_url": "https://www.amazon.in",
        "search_url": "https://www.amazon.in/s?k={query}",
        "selectors": {
            "product_title": "[data-component-type='s-search-result'] h2 a span",
            "price": ".a-price-whole",
            "rating": ".a-icon-alt",
            "availability": ".a-color-success"
        }
    },
    "flipkart": {
        "base_url": "https://www.flipkart.com",
        "search_url": "https://www.flipkart.com/search?q={query}",
        "selectors": {
            "product_title": "._4rR01T",
            "price": "._30jeq3._1_WHN1",
            "rating": "._3LWZlK",
            "availability": "._24B_AU"
        }
    },
    "mdcomputers": {
        "base_url": "https://mdcomputers.in",
        "search_url": "https://mdcomputers.in/index.php?route=product/search&search={query}",
    },
    "primeabgb": {
        "base_url": "https://www.primeabgb.com",
        "search_url": "https://www.primeabgb.com/online-price-list/",
    }
}

# Tech Review and Benchmark Sites
TECH_SITES = {
    "techpowerup": {
        "base_url": "https://www.techpowerup.com",
        "gpu_db": "https://www.techpowerup.com/gpu-specs/",
        "cpu_db": "https://www.techpowerup.com/cpu-specs/"
    },
    "anandtech": {
        "base_url": "https://www.anandtech.com",
        "bench_url": "https://www.anandtech.com/bench/"
    },
    "passmark": {
        "base_url": "https://www.cpubenchmark.net",
        "cpu_chart": "https://www.cpubenchmark.net/cpu_list.php",
        "gpu_chart": "https://www.videocardbenchmark.net/gpu_list.php"
    }
}

# Component Categories
COMPONENT_CATEGORIES = {
    "motherboard": {
        "keywords": ["motherboard", "mobo", "mainboard"],
        "key_specs": ["socket", "chipset", "form_factor", "memory_slots", "pcie_slots", "vrm"]
    },
    "cpu": {
        "keywords": ["processor", "cpu", "intel", "amd", "ryzen", "core"],
        "key_specs": ["cores", "threads", "base_clock", "boost_clock", "tdp", "socket", "cache"]
    },
    "gpu": {
        "keywords": ["graphics card", "gpu", "nvidia", "amd", "rtx", "radeon"],
        "key_specs": ["memory", "memory_type", "core_clock", "memory_clock", "tdp", "outputs"]
    },
    "ram": {
        "keywords": ["memory", "ram", "ddr4", "ddr5"],
        "key_specs": ["capacity", "speed", "timings", "voltage", "modules"]
    },
    "storage": {
        "keywords": ["ssd", "hdd", "nvme", "storage"],
        "key_specs": ["capacity", "interface", "form_factor", "read_speed", "write_speed"]
    },
    "psu": {
        "keywords": ["power supply", "psu", "smps"],
        "key_specs": ["wattage", "efficiency", "modular", "certification", "rails"]
    },
    "case": {
        "keywords": ["cabinet", "case", "chassis"],
        "key_specs": ["form_factor", "materials", "fans", "clearance", "expansion_slots"]
    },
    "cooling": {
        "keywords": ["cooler", "cooling", "fan", "aio", "liquid cooling"],
        "key_specs": ["type", "socket_support", "tdp_rating", "noise_level", "dimensions"]
    }
}

# Indian Market Specific Settings
INDIAN_MARKET = {
    "major_cities": ["Mumbai", "Delhi", "Bangalore", "Chennai", "Pune", "Hyderabad", "Kolkata"],
    "gst_rate": 18,  # GST percentage
    "import_duty_electronics": 10,  # Import duty percentage
    "currency": "INR",
    "warranty_types": ["Indian", "International", "Local Distributor"]
}

# Price Tracking Settings
PRICE_TRACKING = {
    "update_frequency": 24,  # Hours
    "price_change_threshold": 5,  # Percentage change to trigger alert
    "historical_data_days": 365,
    "deal_threshold": 15  # Percentage discount to consider as deal
}

# Build Recommendation Categories
BUILD_CATEGORIES = {
    "budget": {
        "max_price": 50000,  # INR
        "use_cases": ["basic computing", "office work", "light gaming"]
    },
    "mid_range": {
        "max_price": 100000,
        "use_cases": ["1080p gaming", "content creation", "streaming"]
    },
    "high_end": {
        "max_price": 200000,
        "use_cases": ["1440p gaming", "professional work", "heavy multitasking"]
    },
    "enthusiast": {
        "max_price": 300000,
        "use_cases": ["4K gaming", "workstation", "extreme overclocking"]
    }
}

# Database Settings
DATABASE = {
    "name": "pc_components.db",
    "tables": {
        "components": "components",
        "prices": "price_history",
        "benchmarks": "benchmark_data",
        "compatibility": "compatibility_matrix"
    }
}
