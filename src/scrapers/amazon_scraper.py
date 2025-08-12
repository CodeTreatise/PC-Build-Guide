"""
Amazon India Scraper for PC Components
Handles product search, price extraction, and specification gathering
"""

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from typing import Dict, List, Optional
import re
import logging
from urllib.parse import urljoin, quote

from ..utils.helpers import clean_text, extract_price, setup_logging

class AmazonIndiaScraper:
    def __init__(self, delay: float = 2.0):
        """
        Initialize Amazon India scraper
        
        Args:
            delay: Delay between requests in seconds
        """
        self.base_url = "https://www.amazon.in"
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
        self.logger = setup_logging('amazon_scraper')
    
    def search_products(self, query: str, max_pages: int = 5) -> List[Dict]:
        """
        Search for products on Amazon India
        
        Args:
            query: Search term
            max_pages: Maximum pages to scrape
            
        Returns:
            List of product dictionaries
        """
        products = []
        
        for page in range(1, max_pages + 1):
            try:
                search_url = f"{self.base_url}/s?k={quote(query)}&page={page}"
                self.logger.info(f"Scraping page {page} for query: {query}")
                
                response = self.session.get(search_url, timeout=30)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                page_products = self._extract_products_from_page(soup, query)
                products.extend(page_products)
                
                # Check if there are more pages
                if not self._has_next_page(soup):
                    break
                    
                time.sleep(self.delay)
                
            except Exception as e:
                self.logger.error(f"Error scraping page {page}: {str(e)}")
                continue
        
        return products
    
    def _extract_products_from_page(self, soup: BeautifulSoup, query: str) -> List[Dict]:
        """Extract product information from search results page"""
        products = []
        
        # Find all product containers
        product_containers = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        for container in product_containers:
            try:
                product_data = self._extract_product_data(container, query)
                if product_data:
                    products.append(product_data)
            except Exception as e:
                self.logger.warning(f"Error extracting product data: {str(e)}")
                continue
        
        return products
    
    def _extract_product_data(self, container, query: str) -> Optional[Dict]:
        """Extract individual product data from container"""
        try:
            # Product title and URL
            title_element = container.find('h2', class_='a-size-mini')
            if not title_element:
                return None
            
            title_link = title_element.find('a')
            if not title_link:
                return None
                
            title = clean_text(title_link.get_text())
            product_url = urljoin(self.base_url, title_link.get('href'))
            
            # Price extraction
            price_container = container.find('span', class_='a-price')
            price = None
            original_price = None
            
            if price_container:
                price_whole = price_container.find('span', class_='a-price-whole')
                price_fraction = price_container.find('span', class_='a-price-fraction')
                
                if price_whole:
                    price_text = price_whole.get_text() + (price_fraction.get_text() if price_fraction else '')
                    price = extract_price(price_text)
            
            # Original price (if on sale)
            original_price_element = container.find('span', class_='a-text-price')
            if original_price_element:
                original_price = extract_price(original_price_element.get_text())
            
            # Rating
            rating_element = container.find('span', class_='a-icon-alt')
            rating = None
            if rating_element:
                rating_text = rating_element.get_text()
                rating_match = re.search(r'(\d+\.?\d*) out of 5', rating_text)
                if rating_match:
                    rating = float(rating_match.group(1))
            
            # Number of reviews
            reviews_element = container.find('span', class_='a-size-base')
            reviews_count = None
            if reviews_element:
                reviews_text = reviews_element.get_text()
                reviews_match = re.search(r'([\d,]+)', reviews_text)
                if reviews_match:
                    reviews_count = int(reviews_match.group(1).replace(',', ''))
            
            # Prime availability
            prime_element = container.find('span', {'aria-label': 'Amazon Prime'})
            is_prime = prime_element is not None
            
            # Delivery info
            delivery_element = container.find('span', class_='a-color-base a-text-bold')
            delivery_info = delivery_element.get_text() if delivery_element else None
            
            # Image URL
            image_element = container.find('img', class_='s-image')
            image_url = image_element.get('src') if image_element else None
            
            product_data = {
                'title': title,
                'url': product_url,
                'price': price,
                'original_price': original_price,
                'rating': rating,
                'reviews_count': reviews_count,
                'is_prime': is_prime,
                'delivery_info': delivery_info,
                'image_url': image_url,
                'search_query': query,
                'source': 'amazon_in',
                'scraped_at': pd.Timestamp.now()
            }
            
            return product_data
            
        except Exception as e:
            self.logger.warning(f"Error extracting product data: {str(e)}")
            return None
    
    def get_product_details(self, product_url: str) -> Dict:
        """
        Get detailed product information from product page
        
        Args:
            product_url: URL of the product page
            
        Returns:
            Dictionary with detailed product information
        """
        try:
            response = self.session.get(product_url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            details = {
                'specifications': self._extract_specifications(soup),
                'features': self._extract_features(soup),
                'description': self._extract_description(soup),
                'images': self._extract_images(soup),
                'variants': self._extract_variants(soup)
            }
            
            return details
            
        except Exception as e:
            self.logger.error(f"Error getting product details: {str(e)}")
            return {}
    
    def _extract_specifications(self, soup: BeautifulSoup) -> Dict:
        """Extract technical specifications from product page"""
        specs = {}
        
        # Look for specification table
        spec_table = soup.find('table', {'id': 'productDetails_techSpec_section_1'})
        if spec_table:
            rows = spec_table.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                if len(cells) == 2:
                    key = clean_text(cells[0].get_text())
                    value = clean_text(cells[1].get_text())
                    specs[key] = value
        
        # Look for feature bullets
        feature_list = soup.find('div', {'id': 'feature-bullets'})
        if feature_list:
            features = []
            bullets = feature_list.find_all('span', class_='a-list-item')
            for bullet in bullets:
                feature_text = clean_text(bullet.get_text())
                if feature_text and len(feature_text) > 10:
                    features.append(feature_text)
            specs['features'] = features
        
        return specs
    
    def _extract_features(self, soup: BeautifulSoup) -> List[str]:
        """Extract product features"""
        features = []
        
        feature_bullets = soup.find('div', {'id': 'feature-bullets'})
        if feature_bullets:
            bullets = feature_bullets.find_all('span', class_='a-list-item')
            for bullet in bullets:
                feature_text = clean_text(bullet.get_text())
                if feature_text and len(feature_text) > 10:
                    features.append(feature_text)
        
        return features
    
    def _extract_description(self, soup: BeautifulSoup) -> str:
        """Extract product description"""
        description_elements = [
            soup.find('div', {'id': 'productDescription'}),
            soup.find('div', {'data-feature-name': 'productDescription'}),
            soup.find('div', class_='a-section a-spacing-medium a-spacing-top-small')
        ]
        
        for element in description_elements:
            if element:
                return clean_text(element.get_text())
        
        return ""
    
    def _extract_images(self, soup: BeautifulSoup) -> List[str]:
        """Extract product images"""
        images = []
        
        # Main product images
        image_elements = soup.find_all('img', {'data-old-hires': True})
        for img in image_elements:
            img_url = img.get('data-old-hires') or img.get('src')
            if img_url:
                images.append(img_url)
        
        return list(set(images))  # Remove duplicates
    
    def _extract_variants(self, soup: BeautifulSoup) -> List[Dict]:
        """Extract product variants (different sizes, colors, etc.)"""
        variants = []
        
        # Look for variation selection
        variation_elements = soup.find_all('div', class_='a-row a-spacing-small')
        
        return variants
    
    def _has_next_page(self, soup: BeautifulSoup) -> bool:
        """Check if there are more pages in search results"""
        next_button = soup.find('a', {'aria-label': 'Go to next page'})
        return next_button is not None
    
    def save_products_to_csv(self, products: List[Dict], filename: str):
        """Save products data to CSV file"""
        if products:
            df = pd.DataFrame(products)
            df.to_csv(filename, index=False)
            self.logger.info(f"Saved {len(products)} products to {filename}")
        else:
            self.logger.warning("No products to save")

# Example usage
if __name__ == "__main__":
    scraper = AmazonIndiaScraper()
    
    # Search for graphics cards
    products = scraper.search_products("RTX 4060 graphics card", max_pages=3)
    print(f"Found {len(products)} products")
    
    # Save to CSV
    scraper.save_products_to_csv(products, "amazon_rtx4060.csv")
