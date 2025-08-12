# 🖥️ PC Build Guide - Complete Component Selection Guide

[![Deploy Status](https://github.com/shivprasad/pc-build-guide/actions/workflows/deploy.yml/badge.svg)](https://github.com/shivprasad/pc-build-guide/actions/workflows/deploy.yml)
[![Documentation](https://img.shields.io/badge/docs-mkdocs-blue.svg)](https://shivprasad.github.io/pc-build-guide/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Indian Market](https://img.shields.io/badge/market-India-orange.svg)](https://shivprasad.github.io/pc-build-guide/)

> 🇮🇳 **Comprehensive PC building guide tailored for the Indian hardware market with real-time pricing, compatibility checking, and detailed component analysis**

## 🌟 Project Overview

This project provides a comprehensive resource for PC building enthusiasts in India, covering everything from basic component understanding to advanced workstation builds including AI/ML systems, blockchain rigs, and embedded computing.

**🔗 Live Documentation**: [https://shivprasad.github.io/pc-build-guide/](https://shivprasad.github.io/pc-build-guide/)

## 🎯 What Makes This Special

- 🇮🇳 **Indian Market Focus**: Pricing from Amazon.in, Flipkart, MD Computers, PrimeABGB
- 📊 **Real-time Data**: Web scraping for current prices and availability
- 🔧 **Complete Coverage**: From basic desktop builds to specialized AI/ML workstations
- 🎓 **Educational**: Beginner-friendly explanations with expert-level details
- 🚀 **2025 Updated**: Latest hardware including RTX 50 series, Intel 15th Gen, AMD Ryzen 9000

## 📚 Complete Guide Coverage

### 🔧 **Core Components** (8 Guides)
| Component | Guide | Key Topics |
|-----------|-------|------------|
| 🔌 **Motherboard** | [Motherboard Guide](docs/guides/motherboard-guide.md) | Sockets, chipsets, PCIe lanes, VRM analysis, I/O connectivity |
| 🧠 **Processor** | [CPU Guide](docs/guides/cpu-guide.md) | Intel vs AMD, naming schemes, performance analysis |
| 🎮 **Graphics Card** | [GPU Guide](docs/guides/gpu-guide.md) | RTX 50/RX 9000 series, ray tracing, power requirements |
| 🧮 **Memory** | [RAM Guide](docs/guides/ram-guide.md) | DDR5 adoption, timings, capacity planning |
| 💾 **Storage** | [Storage Guide](docs/guides/storage-guide.md) | NVMe PCIe 5.0, capacity trends, endurance |
| ⚡ **Power Supply** | [PSU Guide](docs/guides/psu-guide.md) | ATX 3.1, PCIe 5.1, efficiency standards |
| 🏠 **PC Case** | [Case Guide](docs/guides/case-guide.md) | Airflow optimization, build quality |
| ❄️ **Cooling** | [Cooling Guide](docs/guides/cooling-guide.md) | AIO liquid cooling, TDP ratings |

### 🎯 **Specialized Computing** (5 Guides)
| Category | Guide | Focus |
|----------|-------|-------|
| 🖥️ **Monitors** | [Monitor Guide](docs/guides/monitor-guide.md) | Resolution, refresh rates, HDR |
| ⌨️ **Peripherals** | [Peripherals Guide](docs/guides/peripherals-guide.md) | Keyboards, mice, audio equipment |
| 🤖 **AI/ML Builds** | [AI/ML Guide](docs/guides/ai-ml-guide.md) | Local LLM inference, training workstations |
| ⛓️ **Blockchain** | [Blockchain Guide](docs/guides/blockchain-guide.md) | Mining rigs, validator nodes |
| 🔌 **Embedded** | [Embedded Guide](docs/guides/embedded-guide.md) | Raspberry Pi, IoT, industrial systems |

### 📖 **Learning Resources**
- 🏗️ **[Complete Build Guide](docs/assembly/build-guide.md)**: Step-by-step assembly
- 💰 **[Budget Builds](docs/builds/budget-builds.md)**: Pre-configured recommendations
- 🔄 **[Compatibility Matrix](docs/compatibility/compatibility-matrix.md)**: Component compatibility
- ❓ **[FAQ](docs/learning/faq.md)**: Common questions answered
- 🛠️ **[Troubleshooting](docs/troubleshooting/common-issues.md)**: Problem solving

### 🌐 **External References**
- 📺 **[Video Tutorials](docs/external/video-tutorials.md)**: 30+ YouTube/Twitch channels
- 📖 **[Technical Articles](docs/external/technical-articles.md)**: In-depth research
- 👥 **[Communities](docs/external/communities.md)**: Discord servers, forums
- 🔍 **[Review Sites](docs/external/review-sites.md)**: Professional benchmarks

## 🚀 Quick Start

### For Users (View Documentation)
Visit the live documentation: **[https://shivprasad.github.io/pc-build-guide/](https://shivprasad.github.io/pc-build-guide/)**

### For Developers (Run Locally)

1. **Clone the repository**
```bash
git clone https://github.com/shivprasad/pc-build-guide.git
cd pc-build-guide
```

2. **Set up Python environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Run the documentation server**
```bash
mkdocs serve
```

4. **Open in browser**
```
http://localhost:8000
```

## 🏗️ Project Structure

```
pc-build-guide/
├── docs/                          # Documentation source
│   ├── guides/                    # Component guides
│   │   ├── motherboard-guide.md   # Motherboard selection
│   │   ├── cpu-guide.md          # Processor guide
│   │   ├── gpu-guide.md          # Graphics card guide
│   │   └── ...                   # Other components
│   ├── builds/                   # Build recommendations
│   ├── assembly/                 # Assembly guides
│   ├── compatibility/            # Compatibility info
│   ├── learning/                 # Educational content
│   ├── troubleshooting/          # Problem solving
│   └── external/                 # External references
├── src/                          # Python source code
│   ├── scrapers/                 # Web scraping modules
│   ├── analyzers/                # Component analysis
│   └── utils/                    # Utility functions
├── data/                         # Data storage
├── mkdocs.yml                    # Documentation configuration
└── requirements.txt              # Python dependencies
```

## 💡 Key Features

### 🕷️ **Web Scraping Infrastructure**
- Real-time price collection from major Indian retailers
- Availability tracking and stock monitoring
- Automated data updates and caching

### 📊 **Component Analysis**
- Performance per dollar calculations
- Compatibility checking algorithms
- Comprehensive comparison matrices

### 🇮🇳 **Indian Market Focus**
- Major retailer integration (Amazon.in, Flipkart, MD Computers, PrimeABGB)
- Regional availability analysis
- Import duty and pricing considerations
- Local warranty information

### 📱 **Modern Documentation**
- Responsive Material Design theme
- Dark/light mode toggle
- Advanced search functionality
- Mobile-optimized browsing

## 🛠️ Technology Stack

- **Documentation**: MkDocs with Material theme
- **Web Scraping**: Python (requests, BeautifulSoup, Selenium)
- **Data Analysis**: Pandas, NumPy, Matplotlib
- **Deployment**: GitHub Pages with GitHub Actions
- **CI/CD**: Automated testing and deployment

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 📝 **Content Contributions**
- Update component specifications
- Add new hardware reviews
- Improve compatibility information
- Enhance build recommendations

### 💻 **Code Contributions**
- Improve web scrapers
- Add new analysis features
- Enhance data visualization
- Fix bugs and issues

### 📊 **Data Contributions**
- Submit price data
- Report availability changes
- Share build experiences
- Provide feedback

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Hardware manufacturers for detailed specifications
- Indian tech community for market insights
- Review sites and channels for performance data
- Open source community for tools and libraries

## 📞 Contact & Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/shivprasad/pc-build-guide/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/shivprasad/pc-build-guide/discussions)
- 📧 **Email**: [Contact via GitHub](https://github.com/shivprasad)

---

**⭐ Star this repository if you find it helpful!**

*Last Updated: August 2025 | Made with ❤️ for the Indian PC building community*
- Brand reliability and warranty

### 5. Storage Solutions
- SSD vs HDD comparison
- NVMe vs SATA interfaces
- Storage form factors (M.2, 2.5", 3.5")
- Speed ratings and real-world performance
- Endurance ratings (TBW, DWPD)
- Cache types and controllers
- Capacity vs performance trade-offs

### 6. Power Supply (PSU) Selection
- Wattage calculation and headroom
- Efficiency ratings (80+ Bronze, Gold, Platinum, Titanium)
- Modular vs non-modular cables
- Single vs multi-rail design
- Protection features (OVP, UVP, OCP, SCP)
- Brand reliability and warranty
- Connector types and quantities

### 7. PC Cases (Cabinets)
- Form factor compatibility
- Airflow design (positive vs negative pressure)
- Build quality and materials
- Expansion slots and drive bays
- Cable management features
- Tempered glass vs mesh panels
- Size constraints and clearances

### 8. Cooling Solutions
- Air cooling vs liquid cooling
- CPU cooler compatibility (socket, height clearance)
- TDP ratings and cooling capacity
- Noise levels and fan curves
- Case fans (static pressure vs airflow)
- Thermal paste application and types
- Custom loop considerations

### 9. Peripherals and Accessories
- Monitor types and technologies (TN, IPS, VA, OLED)
- Refresh rates and response times
- Keyboard switches and types
- Mouse sensors and DPI
- Audio solutions (headphones, speakers, DACs)
- Networking (Ethernet, WiFi standards)

## Market Research Components

### Indian Hardware Market Analysis
- **Major Retailers**: Amazon, Flipkart, MD Computers, Prime ABGB, Vedant Computers
- **Regional Availability**: Delhi, Mumbai, Bangalore, Chennai, Pune markets
- **Import Duties**: Impact on pricing compared to international markets
- **Warranty Considerations**: Local vs international warranty
- **Seasonal Pricing**: Festival sales and market trends

### Price Tracking and Comparison
- Real-time price monitoring across platforms
- Historical price trends and analysis
- Price per performance calculations
- Deal alerts and notifications
- Cryptocurrency impact on GPU pricing

## Technical Implementation

### Web Scraping Infrastructure
- **Target Sites**: 
  - E-commerce: Amazon, Flipkart, Newegg India
  - Tech Reviews: TechPowerUp, AnandTech, Tom's Hardware
  - Benchmarks: PassMark, 3DMark, Cinebench databases
  - Indian Tech: Tech Enclave, Digit forums

### Data Processing Pipeline
- Automated data collection and validation
- Price normalization across platforms
- Performance benchmarking database
- Compatibility matrix generation
- Market trend analysis

### User Interface
- Component selection wizard
- Compatibility checker tool
- Price comparison dashboard
- Build generator with recommendations
- Educational content management system

## Project Structure
```
pc-build-guide/
├── src/
│   ├── scrapers/          # Web scraping modules
│   ├── analysis/          # Data analysis tools
│   ├── compatibility/     # Component compatibility checker
│   ├── recommendations/   # Build recommendation engine
│   └── utils/            # Utility functions
├── data/
│   ├── components/       # Component databases
│   ├── benchmarks/       # Performance data
│   └── prices/          # Price tracking data
├── docs/
│   ├── guides/          # Component guides
│   ├── comparisons/     # Comparison charts
│   └── builds/          # Sample build guides
└── tests/               # Testing suite
```

## Getting Started
1. Install Python dependencies: `pip install -r requirements.txt`
2. Configure web scraping settings in `config.py`
3. Run initial data collection: `python src/scrapers/initial_setup.py`
4. Generate documentation: `mkdocs serve`

## Contributing
This project aims to be the most comprehensive PC building resource for Indian consumers, combining technical depth with practical market insights.
