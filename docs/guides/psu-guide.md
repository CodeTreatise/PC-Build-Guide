# Power Supply (PSU) Selection Guide

*Last updated: August 2025*

## Table of Contents
1. [PSU Basics](#psu-basics)
2. [Wattage Calculation](#wattage-calculation)
3. [Efficiency Standards](#efficiency-standards)
4. [Modular vs Non-Modular](#modular-vs-non-modular)
5. [ATX 3.1 and PCIe 5.1](#atx-31-and-pcie-51)
6. [Indian Market Analysis](#indian-market-analysis)
7. [Recommended PSUs by Budget](#recommended-psus-by-budget)
8. [Installation Tips](#installation-tips)

## PSU Basics

### What is a Power Supply Unit?
The PSU converts AC power from your wall outlet into DC power that your PC components can use. It's one of the most critical components as it powers everything in your system.

### Key Specifications to Understand

**Wattage**: Total power output capacity (measured in Watts)
- Entry Level: 450-550W
- Mid-Range: 650-750W  
- High-End: 850-1000W
- Enthusiast: 1200W+

**Voltage Rails**:
- +12V: Powers CPU, GPU, and fans (most important)
- +5V: Powers storage drives and some peripherals
- +3.3V: Powers motherboard and memory

## Wattage Calculation

### RTX 50 Series Power Requirements (2025)
Based on verified specifications:

| GPU Model | Recommended PSU | Minimum PSU |
|-----------|-----------------|-------------|
| RTX 5060 | 550W | 500W |
| RTX 5060 Ti | 650W | 600W |
| RTX 5070 | 750W | 700W |
| RTX 5070 Ti | 850W | 800W |
| RTX 5080 | 850W | 800W |
| RTX 5090 | 1000W | 950W |

### Component Power Consumption (Estimated)

**CPUs (2025)**:
- Intel Core i5-14400F: 65W base, 148W max
- AMD Ryzen 5 9600X: 65W base, 105W max
- Intel Core Ultra 7 265KF: 125W base, 250W max
- AMD Ryzen 9 9950X: 170W base, 230W max

**Other Components**:
- Motherboard: 20-50W
- RAM (32GB DDR5): 10-20W
- NVMe SSD: 5-8W each
- Case Fans: 2-5W each
- AIO Cooler: 15-25W

### PSU Calculator Formula
```
Total Wattage = (CPU Max + GPU Max + Motherboard + RAM + Storage + Cooling) × 1.2 (20% headroom)
```

**Example Build (RTX 5080 + Ryzen 9 9600X)**:
- CPU: 105W
- GPU: 320W
- Motherboard: 30W
- RAM (32GB): 15W
- Storage (2x NVMe): 16W
- Cooling (AIO): 20W
- Fans (6x): 18W
- **Total**: 524W × 1.2 = **629W minimum**
- **Recommended**: 750-850W PSU

## Efficiency Standards

### 80 PLUS Certification Levels

| Certification | 20% Load | 50% Load | 100% Load |
|---------------|----------|----------|-----------|
| 80 PLUS | 80% | 80% | 80% |
| 80 PLUS Bronze | 82% | 85% | 82% |
| 80 PLUS Silver | 85% | 88% | 85% |
| 80 PLUS Gold | 87% | 90% | 87% |
| 80 PLUS Platinum | 90% | 92% | 89% |
| 80 PLUS Titanium | 92% | 94% | 90% |

### Why Efficiency Matters
- **Lower electricity bills**: Higher efficiency = less power waste
- **Less heat generation**: More efficient PSUs run cooler
- **Environmental impact**: Reduced power consumption
- **Component longevity**: Less heat stress on PSU components

### Sweet Spot for Indian Market
**80 PLUS Gold** offers the best price-to-efficiency ratio for most users.

## Modular vs Non-Modular

### Non-Modular PSUs
**Pros**:
- Lower cost (₹2,000-₹5,000 savings)
- All cables permanently attached
- No connection points to fail

**Cons**:
- Cable management challenges
- Unused cables clutter case
- Restricted airflow

### Semi-Modular PSUs
**Pros**:
- Essential cables (24-pin, CPU) permanently attached
- Optional cables removable
- Good balance of cost and flexibility

**Cons**:
- Still some cable clutter
- Limited customization

### Fully Modular PSUs
**Pros**:
- Use only needed cables
- Excellent cable management
- Custom cable options available
- Better airflow

**Cons**:
- Higher cost (₹3,000-₹8,000 premium)
- Additional connection points
- Risk of losing cables

### Recommendation
- **Budget builds**: Non-modular 80 PLUS Bronze
- **Mid-range builds**: Semi-modular 80 PLUS Gold
- **High-end builds**: Fully modular 80 PLUS Gold/Platinum

## ATX 3.1 and PCIe 5.1

### ATX 3.1 Standard (2025)
New standard designed for RTX 50 series and modern GPUs:

**Key Features**:
- **12V-2x6 connector**: Replaces 12VHPWR
- **Improved power delivery**: Better power regulation
- **Enhanced safety**: Reduced connector issues
- **Future compatibility**: Ready for next-gen GPUs

### PCIe 5.1 Benefits
- **Higher power delivery**: Up to 600W through single connector
- **Simplified cabling**: One cable instead of multiple 8-pin
- **Better power efficiency**: Direct 12V delivery to GPU
- **Reduced cable clutter**: Cleaner builds

### Backward Compatibility
- ATX 3.1 PSUs work with older GPUs
- Adapters available for 12V-2x6 to legacy connectors
- No performance penalty with older components

---

## 🔌 Power Connectors & Cables

### **Motherboard Power Connectors**

#### **Primary Power (ATX)**
| Connector | Pin Count | Purpose | Voltage Rails | Usage |
|-----------|-----------|---------|---------------|-------|
| 24-pin ATX | 20+4 pin | Main motherboard power | +12V, +5V, +3.3V, -12V | All modern motherboards |
| 20-pin ATX | 20 pin | Legacy motherboard | +12V, +5V, +3.3V, -12V | Older systems only |

#### **CPU Power (EPS)**
| Connector | Pin Count | Power Rating | CPU Support | Notes |
|-----------|-----------|--------------|-------------|-------|
| 8-pin EPS | 4+4 pin | 235W | Mid-range CPUs | Standard configuration |
| 8+4 pin EPS | 12 pin | 350W+ | High-end CPUs | i9/Ryzen 9 series |
| 8+8 pin EPS | 16 pin | 500W+ | Extreme CPUs | Overclocking, Threadripper |

### **GPU Power Connectors**

#### **PCIe Power Standards**
| Connector Type | Pin Count | Power Rating | GPU Support | Availability |
|----------------|-----------|--------------|-------------|--------------|
| PCIe 6-pin | 6 pin | 75W | Entry GPUs | Legacy standard |
| PCIe 8-pin (6+2) | 8 pin | 150W | Mid-range GPUs | Most common |
| 12VHPWR | 16 pin | 600W | RTX 4090 | ATX 3.0 standard |
| 12V-2x6 | 12 pin | 600W | RTX 5090, future | ATX 3.1 standard |

#### **GPU Power Requirements (2025)**
| GPU Series | Power Connectors | Total Power | PSU Recommendation |
|------------|------------------|-------------|-------------------|
| RTX 5090 | 1x 12V-2x6 | 575W | 1000W+ ATX 3.1 |
| RTX 4090 | 1x 12VHPWR | 450W | 850W+ ATX 3.0 |
| RTX 4080 Super | 2x 8-pin | 320W | 750W+ |
| RTX 4070 Ti | 2x 8-pin | 285W | 650W+ |
| RX 7900 XTX | 2x 8-pin | 355W | 750W+ |

### **Storage Power Connectors**

#### **SATA Power**
| Connector | Pin Count | Power Rating | Device Support | Cable Type |
|-----------|-----------|--------------|----------------|------------|
| SATA Power | 15 pin | 54W (12V: 54W, 5V: 25W) | SATA drives | Flat cable |
| SATA Slimline | 13 pin | 25W | Slim optical drives | Compact design |

#### **Legacy Storage Connectors**
| Connector | Pin Count | Power Rating | Device Support | Status |
|-----------|-----------|--------------|----------------|--------|
| Molex 4-pin | 4 pin | 54W | IDE drives, fans | Legacy/adapters |
| Floppy 4-pin | 4 pin | 25W | Floppy drives | Obsolete |

### **Peripheral Power Connectors**

#### **Fan and RGB Connectors**
| Connector | Pin Count | Power Rating | Device Support | Control |
|-----------|-----------|--------------|----------------|---------|
| 3-pin Fan | 3 pin | 12W | Basic fans | Voltage control |
| 4-pin PWM | 4 pin | 12W | PWM fans | Digital control |
| RGB 4-pin | 4 pin | 36W | RGB strips | Basic RGB |
| ARGB 3-pin | 3 pin | 60W | Addressable RGB | Digital RGB |

### **Modular vs Non-Modular Cables**

#### **Cable Types**
| Cable Type | Modularity | Advantages | Disadvantages | Best For |
|------------|------------|------------|---------------|----------|
| Hardwired | Fixed | Lower cost, reliable | Cable clutter | Budget builds |
| Semi-Modular | ATX+EPS fixed, others detachable | Balance of cost/flexibility | Some unused cables | Mid-range builds |
| Fully Modular | All cables detachable | Clean builds, custom cables | Higher cost | High-end builds |

#### **Cable Length Standards**
| Cable Type | Standard Length | Extended Length | Use Case |
|------------|-----------------|-----------------|----------|
| 24-pin ATX | 60cm | 75cm+ | Large cases |
| 8-pin EPS | 65cm | 80cm+ | Top-mount PSU |
| PCIe 8-pin | 60cm | 75cm+ | Multi-GPU setups |
| SATA Power | 50cm + 15cm between | Custom lengths | Storage arrays |

### **Power Distribution Examples**

#### **Gaming PC Power Layout**
```
Standard Gaming Build (750W PSU):
├── 24-pin ATX → Motherboard (250W capacity)
├── 8-pin EPS → CPU (235W capacity)
├── 2x 8-pin PCIe → GPU (300W capacity)
├── 4x SATA Power → Storage drives
└── Molex adapters → Case fans, RGB
```

#### **High-End Workstation**
```
Professional Workstation (1200W PSU):
├── 24-pin ATX → Motherboard
├── 8+4 pin EPS → High-end CPU (350W)
├── 3x 8-pin PCIe → Dual GPUs (600W total)
├── 8x SATA Power → Storage array
└── Multiple 4-pin → Extensive cooling
```

#### **Mining Rig Configuration**
```
6-GPU Mining Rig (Dual 1200W PSUs):
PSU 1 (Primary):
├── 24-pin ATX → Motherboard
├── 8-pin EPS → CPU
└── 6x 8-pin PCIe → 3 GPUs

PSU 2 (Secondary):
├── Add2PSU sync cable
└── 6x 8-pin PCIe → 3 GPUs
```

### **Cable Management Best Practices**

#### **Routing Guidelines**
| Cable Type | Routing Path | Management Tips | Common Mistakes |
|------------|--------------|-----------------|------------------|
| 24-pin ATX | Behind motherboard | Secure with velcro | Tight bends |
| 8-pin EPS | Top of case | Plan route early | Cable too short |
| PCIe Power | Side routing | Avoid GPU fans | Blocking airflow |
| SATA Power | Drive bays | Daisy-chain efficiently | Overloading single rail |

#### **Cable Extensions and Sleeving**
| Solution | Cost | Difficulty | Visual Impact | Use Case |
|----------|------|------------|---------------|----------|
| Extension cables | Low | Easy | Medium | Quick color matching |
| Sleeved extensions | Medium | Easy | High | Show builds |
| Custom sleeving | High | Hard | Maximum | Enthusiast builds |
| Replace PSU cables | Medium | Medium | High | Modular PSUs only |

### **Power Connector Compatibility**

#### **Backward Compatibility**
| New Standard | Old Standard | Adapter Required | Performance Impact |
|--------------|--------------|------------------|-------------------|
| ATX 3.1 PSU | ATX 2.x motherboard | No | None |
| 12V-2x6 PSU | 12VHPWR GPU | No (included cable) | None |
| ATX 3.1 PSU | 8-pin GPU | Adapter cable | None |
| Modular cables | Different PSU brand | ⚠️ NEVER | Damage risk |

#### **Safety Warnings**
⚠️ **CRITICAL SAFETY RULES:**
1. **Never mix modular cables** between different PSU brands/models
2. **Check pin layouts** before using adapters
3. **Verify power ratings** don't exceed connector limits
4. **Secure all connections** to prevent arcing
5. **Test system** before final cable management

---

## Indian Market Analysis

### Major PSU Brands Available

**Tier 1 (Premium)**:
- **Seasonic**: PRIME TX 3.1, FOCUS GX 3.1
- **Corsair**: RM1000x, HX1200i
- **EVGA**: SuperNOVA G7, P6 series
- **Cooler Master**: V Gold, MWE Gold

**Tier 2 (Value)**:
- **Antec**: NeoECO Gold, HCG series
- **Thermaltake**: Toughpower GF3, Smart series
- **ADATA**: XPG Core Reactor, PYLON series

**Tier 3 (Budget)**:
- **Gigabyte**: P-B series, GP-P series
- **MSI**: MAG A-GF, MPG A-GF series
- **Local brands**: Zebronics, Circle, iBall

### Current Pricing (August 2025)

**500-600W Range**:
- **Budget** (₹3,500-₹5,500): Gigabyte P550B, MSI MAG A550BN
- **Mid-range** (₹6,000-₹9,000): Antec NeoECO Gold 550W, Cooler Master MWE Gold 650W
- **Premium** (₹10,000-₹14,000): Seasonic FOCUS GX-650, Corsair RM650x

**750-850W Range**:
- **Budget** (₹6,500-₹9,000): Gigabyte P750GM, Thermaltake Smart BX1 750W
- **Mid-range** (₹10,000-₹15,000): Antec HCG750 Gold, Cooler Master V Gold 750W
- **Premium** (₹16,000-₹22,000): Seasonic FOCUS GX-850, Corsair RM850x

**1000W+ Range**:
- **Mid-range** (₹15,000-₹25,000): Cooler Master V1000 Gold, Thermaltake Toughpower GF3 1000W
- **Premium** (₹25,000-₹40,000): Seasonic PRIME TX-1300 3.1, Corsair HX1200i

### Where to Buy in India
- **Online**: Amazon.in, Flipkart, MDComputers, PrimeABGB
- **Offline**: Nehru Place (Delhi), Lamington Road (Mumbai), SP Road (Bangalore)
- **Authorized dealers**: Check manufacturer websites for local dealers

## Recommended PSUs by Budget

### Budget Gaming (₹50,000-₹80,000 build)
**Target**: RTX 5060/5060 Ti + Ryzen 5 9600X

**Primary Choice**: Antec NeoECO Gold 650W (₹7,500)
- 80 PLUS Gold efficiency
- Semi-modular design
- 5-year warranty
- Good voltage regulation

**Alternative**: Cooler Master MWE Gold 650W V2 (₹8,500)
- Fully modular
- 80 PLUS Gold
- Quiet operation
- DC-DC converter design

### Mid-Range Gaming (₹1,00,000-₹1,50,000 build)
**Target**: RTX 5070/5070 Ti + Ryzen 7 9700X

**Primary Choice**: Seasonic FOCUS GX-750 ATX 3.1 (₹13,500)
- ATX 3.1 compliant
- 12V-2x6 connector
- 80 PLUS Gold
- 10-year warranty

**Alternative**: Corsair RM750x (₹15,000)
- Fully modular
- Zero RPM fan mode
- Premium Japanese capacitors
- 10-year warranty

### High-End Gaming (₹2,00,000+ build)
**Target**: RTX 5080/5090 + Ryzen 9 9950X

**Primary Choice**: Seasonic PRIME TX-1300 ATX 3.1 (₹32,000)
- 1300W capacity
- ATX 3.1 standard
- 80 PLUS Titanium
- 12-year warranty

**Alternative**: Corsair HX1000i (₹28,000)
- 1000W capacity
- Digital monitoring
- 80 PLUS Platinum
- Fully modular

### Content Creator/Workstation
**Target**: High-end CPU + RTX 5090 + Multiple drives

**Recommended**: Seasonic PRIME TX-1600 ATX 3.1 (₹45,000)
- 1600W capacity
- Multiple 12V-2x6 connectors
- 80 PLUS Titanium
- Premium components

## Installation Tips

### Pre-Installation
1. **Verify compatibility**: Check case PSU clearance
2. **Cable planning**: Identify required connectors
3. **Tools needed**: Phillips head screwdriver, anti-static wrist strap

### Installation Steps
1. **Mount PSU**: Install in case with fan facing down (if case has bottom ventilation)
2. **Connect motherboard**: 24-pin ATX and 8-pin CPU connectors first
3. **GPU power**: Use dedicated PCIe cables (avoid daisy-chaining for high-end GPUs)
4. **Storage/peripherals**: SATA power for drives
5. **Cable management**: Route cables behind motherboard tray

### Post-Installation Checks
1. **Power on test**: System should boot to BIOS
2. **Voltage monitoring**: Use HWiNFO64 to check rail voltages
3. **Stress testing**: Run FurMark + Prime95 to test stability
4. **Temperature monitoring**: PSU should remain cool under load

### Common Issues and Solutions

**PSU Won't Turn On**:
- Check power switch position
- Verify all connections are secure
- Test with paperclip test (shorting green and black wires)

**System Randomly Shuts Down**:
- Insufficient wattage for components
- Overheating PSU (check ventilation)
- Failing PSU (RMA if under warranty)

**Coil Whine**:
- Common with high-efficiency PSUs
- Usually not harmful
- Can be reduced with quality PSUs

### Maintenance
- **Dust cleaning**: Every 6 months using compressed air
- **Fan replacement**: If PSU fan fails (professional repair recommended)
- **Warranty**: Keep purchase receipts for RMA claims

## Future Considerations

### Upcoming Standards
- **ATX 3.2**: Expected 2026 with further power delivery improvements
- **PCIe 6.0**: Higher bandwidth and power delivery
- **12V-only PSUs**: Simplified designs removing +5V and +3.3V rails

### Capacity Planning
When choosing PSU wattage, consider:
- **GPU upgrades**: Next 2-3 generations
- **Efficiency curve**: PSUs most efficient at 50-80% load
- **Age degradation**: PSUs lose ~5% capacity over 5-7 years

### Investment Perspective
A quality PSU is a long-term investment:
- **Lifespan**: 7-10 years with quality units
- **Efficiency savings**: ₹2,000-₹5,000 annually on electricity
- **Component protection**: Good PSUs protect other components
- **Upgrade compatibility**: Quality PSUs support multiple system upgrades

---

*This guide reflects August 2025 market conditions and verified product specifications from leading PSU manufacturers including Seasonic, Corsair, and other major brands available in the Indian market.*
