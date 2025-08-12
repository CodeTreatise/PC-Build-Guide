"""
Utility functions for the PC Build Guide project
Common helper functions used across different modules
"""

import re
import logging
import os
from typing import Optional, Dict, List, Union
import pandas as pd
from datetime import datetime

def clean_text(text: str) -> str:
    """
    Clean and normalize text data
    
    Args:
        text: Raw text to clean
        
    Returns:
        Cleaned text string
    """
    if not text:
        return ""
    
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text.strip())
    
    # Remove special characters that might cause issues
    text = re.sub(r'[^\w\s\-\.\,\(\)\[\]\%\+\=\:\;]', '', text)
    
    return text

def extract_price(price_text: str) -> Optional[float]:
    """
    Extract numeric price from text
    
    Args:
        price_text: Text containing price information
        
    Returns:
        Price as float or None if not found
    """
    if not price_text:
        return None
    
    # Remove currency symbols and commas
    price_clean = re.sub(r'[₹,\$\€\£]', '', price_text)
    
    # Find price pattern
    price_match = re.search(r'([\d,]+\.?\d*)', price_clean)
    
    if price_match:
        try:
            price_str = price_match.group(1).replace(',', '')
            return float(price_str)
        except ValueError:
            return None
    
    return None

def extract_numeric_value(text: str, unit: str = None) -> Optional[float]:
    """
    Extract numeric values from text (e.g., "8GB" -> 8.0)
    
    Args:
        text: Text containing numeric value
        unit: Optional unit to look for
        
    Returns:
        Numeric value as float
    """
    if not text:
        return None
    
    # Create pattern based on unit
    if unit:
        pattern = rf'(\d+\.?\d*)\s*{re.escape(unit)}'
    else:
        pattern = r'(\d+\.?\d*)'
    
    match = re.search(pattern, text, re.IGNORECASE)
    
    if match:
        try:
            return float(match.group(1))
        except ValueError:
            return None
    
    return None

def normalize_component_name(name: str, component_type: str) -> str:
    """
    Normalize component names for better matching
    
    Args:
        name: Component name
        component_type: Type of component (cpu, gpu, etc.)
        
    Returns:
        Normalized name
    """
    if not name:
        return ""
    
    name = name.lower().strip()
    
    # Remove common prefixes/suffixes
    removals = [
        'nvidia', 'amd', 'intel', 'asus', 'msi', 'gigabyte', 'evga',
        'graphics card', 'processor', 'motherboard'
    ]
    
    for removal in removals:
        name = re.sub(rf'\b{removal}\b', '', name, flags=re.IGNORECASE)
    
    # Clean up spacing
    name = re.sub(r'\s+', ' ', name).strip()
    
    return name

def setup_logging(name: str, level: str = 'INFO') -> logging.Logger:
    """
    Set up logging for modules
    
    Args:
        name: Logger name
        level: Logging level
        
    Returns:
        Configured logger
    """
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        # Create logs directory if it doesn't exist
        log_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'logs')
        os.makedirs(log_dir, exist_ok=True)
        
        # File handler
        file_handler = logging.FileHandler(
            os.path.join(log_dir, f'{name}.log'),
            encoding='utf-8'
        )
        file_handler.setLevel(getattr(logging, level))
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(getattr(logging, level))
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        logger.setLevel(getattr(logging, level))
    
    return logger

def parse_memory_capacity(capacity_str: str) -> Optional[int]:
    """
    Parse memory capacity from string (e.g., "16GB" -> 16)
    
    Args:
        capacity_str: Memory capacity string
        
    Returns:
        Capacity in GB as integer
    """
    if not capacity_str:
        return None
    
    # Look for patterns like "16GB", "32 GB", "1TB"
    pattern = r'(\d+)\s*(GB|TB|MB)'
    match = re.search(pattern, capacity_str, re.IGNORECASE)
    
    if match:
        value = int(match.group(1))
        unit = match.group(2).upper()
        
        if unit == 'TB':
            return value * 1024
        elif unit == 'MB':
            return value // 1024 if value >= 1024 else 1
        else:  # GB
            return value
    
    return None

def parse_clock_speed(speed_str: str) -> Optional[float]:
    """
    Parse clock speed from string (e.g., "3.5GHz" -> 3.5)
    
    Args:
        speed_str: Clock speed string
        
    Returns:
        Clock speed in GHz as float
    """
    if not speed_str:
        return None
    
    pattern = r'(\d+\.?\d*)\s*(GHz|MHz)'
    match = re.search(pattern, speed_str, re.IGNORECASE)
    
    if match:
        value = float(match.group(1))
        unit = match.group(2).upper()
        
        if unit == 'MHZ':
            return value / 1000
        else:  # GHz
            return value
    
    return None

def calculate_price_per_performance(price: float, performance_score: float) -> Optional[float]:
    """
    Calculate price per performance ratio
    
    Args:
        price: Component price
        performance_score: Performance benchmark score
        
    Returns:
        Price per performance ratio
    """
    if not price or not performance_score or performance_score <= 0:
        return None
    
    return price / performance_score

def detect_component_type(product_name: str) -> str:
    """
    Detect component type from product name
    
    Args:
        product_name: Product name/title
        
    Returns:
        Component type string
    """
    name_lower = product_name.lower()
    
    # Component type keywords
    type_keywords = {
        'cpu': ['processor', 'cpu', 'ryzen', 'core i3', 'core i5', 'core i7', 'core i9'],
        'gpu': ['graphics card', 'gpu', 'rtx', 'gtx', 'radeon', 'rx', 'geforce'],
        'motherboard': ['motherboard', 'mobo', 'mainboard'],
        'ram': ['memory', 'ram', 'ddr4', 'ddr5'],
        'storage': ['ssd', 'hdd', 'nvme', 'hard drive', 'solid state'],
        'psu': ['power supply', 'psu', 'smps'],
        'case': ['cabinet', 'case', 'chassis', 'tower'],
        'cooling': ['cooler', 'cooling', 'fan', 'aio', 'liquid cooling']
    }
    
    for component_type, keywords in type_keywords.items():
        for keyword in keywords:
            if keyword in name_lower:
                return component_type
    
    return 'unknown'

def format_currency(amount: float, currency: str = 'INR') -> str:
    """
    Format currency amount
    
    Args:
        amount: Amount to format
        currency: Currency code
        
    Returns:
        Formatted currency string
    """
    if currency == 'INR':
        if amount >= 100000:
            return f"₹{amount/100000:.1f}L"
        elif amount >= 1000:
            return f"₹{amount/1000:.1f}K"
        else:
            return f"₹{amount:.0f}"
    else:
        return f"{currency} {amount:.2f}"

def validate_product_data(product: Dict) -> bool:
    """
    Validate product data dictionary
    
    Args:
        product: Product data dictionary
        
    Returns:
        True if valid, False otherwise
    """
    required_fields = ['title', 'price', 'url']
    
    for field in required_fields:
        if field not in product or not product[field]:
            return False
    
    # Validate price is numeric
    try:
        float(product['price'])
    except (ValueError, TypeError):
        return False
    
    return True

def create_product_id(product: Dict) -> str:
    """
    Create unique product ID from product data
    
    Args:
        product: Product data dictionary
        
    Returns:
        Unique product ID string
    """
    # Use combination of title and source
    title = product.get('title', '').lower()
    source = product.get('source', '')
    
    # Remove special characters and create hash-like ID
    clean_title = re.sub(r'[^\w\s]', '', title)
    clean_title = re.sub(r'\s+', '_', clean_title)
    
    return f"{source}_{clean_title}_{hash(product.get('url', '')) % 100000}"

def save_to_json(data: Union[Dict, List], filename: str):
    """
    Save data to JSON file
    
    Args:
        data: Data to save
        filename: Output filename
    """
    import json
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)

def load_from_json(filename: str) -> Union[Dict, List, None]:
    """
    Load data from JSON file
    
    Args:
        filename: Input filename
        
    Returns:
        Loaded data or None if file doesn't exist
    """
    import json
    
    if not os.path.exists(filename):
        return None
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return None

def get_data_dir() -> str:
    """Get the data directory path"""
    return os.path.join(os.path.dirname(__file__), '..', '..', 'data')

def ensure_data_dir():
    """Ensure data directory exists"""
    data_dir = get_data_dir()
    os.makedirs(data_dir, exist_ok=True)
    
    # Create subdirectories
    subdirs = ['components', 'benchmarks', 'prices', 'compatibility']
    for subdir in subdirs:
        os.makedirs(os.path.join(data_dir, subdir), exist_ok=True)
