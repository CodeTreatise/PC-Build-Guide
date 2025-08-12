# Component Compatibility Matrix

*Last updated: August 2025*

## CPU and Motherboard Compatibility

### Intel Socket Compatibility (2025)

| CPU Generation | Socket | Chipsets | DDR Support | PCIe |
|---------------|--------|----------|-------------|------|
| 15th Gen (Arrow Lake) | LGA 1851 | Z890, B860, H810 | DDR5-5600+ | PCIe 5.0 |
| 14th Gen (Raptor Lake-S) | LGA 1700 | Z790, B760, H770 | DDR4/DDR5 | PCIe 5.0/4.0 |
| 13th Gen (Raptor Lake) | LGA 1700 | Z790, Z690, B760, B660 | DDR4/DDR5 | PCIe 5.0/4.0 |
| 12th Gen (Alder Lake) | LGA 1700 | Z690, B660, H670, H610 | DDR4/DDR5 | PCIe 5.0/4.0 |

**Key Notes**:
- **LGA 1851**: New socket for 15th Gen, NOT compatible with LGA 1700
- **LGA 1700**: Supports 12th, 13th, and 14th Gen with BIOS update
- **DDR4/DDR5**: Cannot mix on same motherboard - choose one type

### AMD Socket Compatibility (2025)

| CPU Generation | Socket | Chipsets | DDR Support | PCIe |
|---------------|--------|----------|-------------|------|
| Ryzen 9000 (Zen 5) | AM5 | X870E, X870, B850 | DDR5-5600+ | PCIe 5.0 |
| Ryzen 8000 (APUs) | AM5 | X670E, X670, B650E, B650 | DDR5-5200+ | PCIe 5.0/4.0 |
| Ryzen 7000 (Zen 4) | AM5 | X670E, X670, B650E, B650 | DDR5-5200+ | PCIe 5.0/4.0 |
| Ryzen 5000 (Zen 3) | AM4 | X570, B550, A520 | DDR4-3200+ | PCIe 4.0 |

**Key Notes**:
- **AM5**: All Ryzen 7000+ series, DDR5 only, PCIe 5.0 support
- **AM4**: Legacy socket, DDR4 only, still viable for budget builds
- **Chipset features**: Higher-end chipsets offer more USB, SATA, PCIe lanes

## Memory Compatibility

### DDR4 vs DDR5 Motherboard Support

| Platform | DDR4 Support | DDR5 Support | Notes |
|----------|-------------|-------------|-------|
| Intel LGA 1851 | ❌ No | ✅ Yes | DDR5 only |
| Intel LGA 1700 | ✅ Yes* | ✅ Yes* | Choose one type |
| AMD AM5 | ❌ No | ✅ Yes | DDR5 only |
| AMD AM4 | ✅ Yes | ❌ No | DDR4 only |

*Individual motherboards support either DDR4 OR DDR5, not both

### RAM Speed Compatibility by Platform

#### Intel Memory Support (2025)
| CPU Series | JEDEC Standard | XMP/Overclocked |
|------------|---------------|-----------------|
| 15th Gen | DDR5-5600 | DDR5-8000+ |
| 14th Gen | DDR5-5600 | DDR5-7200+ |
| 13th Gen | DDR5-4800 | DDR5-6400+ |
| 12th Gen | DDR5-4800 | DDR5-6000+ |

#### AMD Memory Support (2025)
| CPU Series | JEDEC Standard | EXPO/Overclocked |
|------------|---------------|------------------|
| Ryzen 9000 | DDR5-5600 | DDR5-8000+ |
| Ryzen 8000 | DDR5-5200 | DDR5-6400+ |
| Ryzen 7000 | DDR5-5200 | DDR5-6000+ |
| Ryzen 5000 | DDR4-3200 | DDR4-4000+ |

### Memory Configuration Guidelines

#### Channel Configuration
| Motherboard Slots | Recommended Population | Performance |
|------------------|----------------------|-------------|
| 2 slots | Slot 1 + Slot 2 | Dual Channel |
| 4 slots | Slot 2 + Slot 4 | Dual Channel |
| 4 slots | All 4 slots | Dual Channel |

**Key Rules**:
- Always populate slots of same color first
- Use identical memory modules for best compatibility
- Check motherboard QVL (Qualified Vendor List) for guaranteed compatibility

## Graphics Card Compatibility

### PCIe Slot Compatibility

| GPU Generation | PCIe Required | Backward Compatible |
|---------------|---------------|-------------------|
| RTX 50 Series | PCIe 4.0 x16 | PCIe 3.0 x16 |
| RTX 40 Series | PCIe 4.0 x16 | PCIe 3.0 x16 |
| RX 9000 Series | PCIe 4.0 x16 | PCIe 3.0 x16 |

**Performance Impact**:
- **PCIe 3.0 vs 4.0**: <5% performance difference in most games
- **PCIe x8 vs x16**: <3% performance difference for gaming
- **Future proofing**: PCIe 4.0 recommended for RTX 5080/5090

### Power Supply Requirements for RTX 50 Series

| GPU Model | TGP | 12V-2x6 | Legacy Connectors | Min PSU |
|-----------|-----|---------|------------------|---------|
| RTX 5060 | 115W | Optional | 1x 8-pin | 500W |
| RTX 5060 Ti | 165W | Optional | 1x 8-pin | 600W |
| RTX 5070 | 220W | Recommended | 1x 12+4pin | 700W |
| RTX 5070 Ti | 285W | Required | 2x 8-pin | 800W |
| RTX 5080 | 400W | Required | 3x 8-pin | 850W |
| RTX 5090 | 575W | Required | 4x 8-pin | 1000W |

### GPU Physical Clearance

#### Length Clearance by Case Type
| Case Type | Typical Max Length | RTX 50 Compatibility |
|-----------|------------------|-------------------|
| Mini-ITX | 280-320mm | RTX 5060/5060 Ti |
| Micro-ATX | 320-350mm | Up to RTX 5070 Ti |
| Mid-Tower | 350-400mm | All RTX 50 series |
| Full-Tower | 400mm+ | All RTX 50 series |

#### Height Clearance (Slot Width)
| GPU Model | Slot Width | Case Requirement |
|-----------|------------|-----------------|
| RTX 5060 | 2.0 slots | Standard |
| RTX 5060 Ti | 2.5 slots | Standard |
| RTX 5070 | 2.75 slots | Check clearance |
| RTX 5070 Ti | 3.0 slots | Verify fit |
| RTX 5080 | 3.0 slots | Verify fit |
| RTX 5090 | 3.5 slots | Large case needed |

## CPU Cooler Compatibility

### Socket Mounting Compatibility

#### Intel Cooler Compatibility
| Socket | Compatible Coolers | Notes |
|--------|------------------|-------|
| LGA 1851 | LGA 1851 specific | New mounting mechanism |
| LGA 1700 | LGA 1700, some 115x* | Check manufacturer |
| LGA 1200 | LGA 115x series | Wide compatibility |

*Some LGA 115x coolers compatible with adapter

#### AMD Cooler Compatibility  
| Socket | Compatible Coolers | Notes |
|--------|------------------|-------|
| AM5 | AM5, AM4 (most) | Check manufacturer |
| AM4 | AM4, AM3/AM3+ | Wide compatibility |

### CPU Cooler Height Clearance

| Case Type | Typical Max Height | Compatible Coolers |
|-----------|------------------|------------------|
| Mini-ITX | 70mm | Low profile only |
| Micro-ATX | 155mm | Most tower coolers |
| Mid-Tower | 165mm | All tower coolers |
| Full-Tower | 170mm+ | All coolers |

### AIO Radiator Compatibility

| Radiator Size | Case Support | Performance Level |
|--------------|-------------|------------------|
| 120mm | Most cases | Entry level |
| 240mm | Mid-tower+ | Good performance |
| 280mm | Mid-tower+ | Better performance |
| 360mm | Full-tower | High performance |
| 420mm | Full-tower | Maximum performance |

## Storage Compatibility

### M.2 Slot Types and Speeds

| Interface | Max Speed | Compatible Drives |
|-----------|-----------|------------------|
| M.2 SATA | 600 MB/s | SATA M.2 SSDs |
| M.2 PCIe 3.0 x4 | ~3,500 MB/s | NVMe SSDs |
| M.2 PCIe 4.0 x4 | ~7,000 MB/s | PCIe 4.0 NVMe |
| M.2 PCIe 5.0 x4 | ~12,000 MB/s | PCIe 5.0 NVMe |

### M.2 Slot Configuration by Platform

#### Intel Motherboards
| Chipset | CPU M.2 Slots | Chipset M.2 Slots | Total Slots |
|---------|---------------|------------------|-------------|
| Z890 | 1x PCIe 5.0 | 2-4x PCIe 4.0 | 3-5 |
| B860 | 1x PCIe 4.0 | 1-2x PCIe 4.0 | 2-3 |
| H810 | 1x PCIe 4.0 | 1x PCIe 4.0 | 2 |

#### AMD Motherboards  
| Chipset | CPU M.2 Slots | Chipset M.2 Slots | Total Slots |
|---------|---------------|------------------|-------------|
| X870E | 1x PCIe 5.0 | 2-4x PCIe 4.0 | 3-5 |
| X870 | 1x PCIe 5.0 | 2-3x PCIe 4.0 | 3-4 |
| B850 | 1x PCIe 4.0 | 1-2x PCIe 4.0 | 2-3 |

### PCIe Lane Sharing Considerations

**Common Conflicts**:
- Some M.2 slots share lanes with SATA ports
- Using M.2_2 may disable SATA 5-6 ports
- PCIe slots may share lanes with M.2 slots
- Check motherboard manual for specific limitations

## Power Supply Compatibility

### ATX Form Factor Compatibility

| PSU Type | Motherboard Support | Case Requirement |
|----------|------------------|-----------------|
| ATX | ATX, Micro-ATX | Mid-tower+ |
| SFX | Mini-ITX, Micro-ATX | Compact cases |
| SFX-L | Mini-ITX, Micro-ATX | Some compact cases |

### Connector Compatibility

#### Essential Connectors (All PSUs)
- 24-pin ATX motherboard power
- 8-pin (4+4) CPU power  
- 6-pin/8-pin PCIe for graphics cards
- SATA power for drives

#### Modern Connectors (2025)
- **12V-2x6**: RTX 50 series native connector
- **12VHPWR**: Previous generation (still compatible)
- **Multiple PCIe 8-pin**: For high-end GPUs without native connector

### PSU Length Compatibility

| Case Type | Max PSU Length | Standard ATX |
|-----------|---------------|-------------|
| Mini-ITX | 140-160mm | Check case specs |
| Micro-ATX | 160-180mm | Most ATX PSUs |
| Mid-Tower | 180mm+ | All ATX PSUs |
| Full-Tower | 200mm+ | All PSU types |

## Case and Component Compatibility

### Motherboard Form Factor Support

| Case Type | Supported Motherboards |
|-----------|----------------------|
| Mini-ITX | Mini-ITX only |
| Micro-ATX | Mini-ITX, Micro-ATX |
| Mid-Tower | Mini-ITX, Micro-ATX, ATX |
| Full-Tower | All form factors |

### Drive Bay Compatibility

| Drive Type | Bay Size | Modern Support |
|------------|----------|---------------|
| 3.5" HDD | 3.5" bay | Most cases |
| 2.5" SSD | 2.5" bay | Universal |
| M.2 NVMe | Motherboard | No case space needed |

### Clearance Checklist

**Before Building**:
- ✅ GPU length vs case clearance
- ✅ CPU cooler height vs case clearance  
- ✅ PSU length vs case space
- ✅ RAM height vs CPU cooler clearance
- ✅ Cable routing space
- ✅ Radiator mounting positions

## Troubleshooting Compatibility Issues

### Common Compatibility Problems

#### Boot Issues
**Symptoms**: No POST, black screen
**Common causes**:
- Incompatible RAM speed/voltage
- Insufficient PSU wattage
- CPU/motherboard mismatch
- Loose connections

#### Performance Issues  
**Symptoms**: Lower than expected performance
**Common causes**:
- RAM not running at XMP speeds
- GPU in wrong PCIe slot (x8 instead of x16)
- Thermal throttling from inadequate cooling
- PCIe version limitations

#### Stability Issues
**Symptoms**: Random crashes, BSODs
**Common causes**:
- Overclocked RAM unstable
- Insufficient PSU power delivery
- Thermal throttling
- Incompatible component combinations

### Verification Tools

**Before Purchase**:
- Check motherboard QVL for RAM
- Verify CPU socket compatibility
- Confirm PSU wattage requirements
- Measure case clearances

**After Assembly**:
- Run CPU-Z to verify specifications
- Check RAM speed in BIOS
- Monitor temperatures with HWiNFO64
- Stress test with Prime95 + FurMark

### When to Seek Help

**Contact manufacturer support if**:
- Components are listed as compatible but don't work
- Performance significantly below specifications
- Repeated stability issues after troubleshooting
- Physical compatibility issues despite meeting requirements

---

## Quick Reference Tables

### Socket Quick Reference
- **Intel 15th Gen**: LGA 1851 only
- **Intel 12-14th Gen**: LGA 1700 only  
- **AMD Ryzen 7000+**: AM5 only
- **AMD Ryzen 5000**: AM4 only

### Memory Quick Reference
- **AM5 + LGA 1851**: DDR5 only
- **LGA 1700**: DDR4 OR DDR5 (choose one)
- **AM4**: DDR4 only

### GPU Power Quick Reference
- **RTX 5060/5060 Ti**: 500-600W PSU
- **RTX 5070/5070 Ti**: 700-800W PSU  
- **RTX 5080**: 850W PSU minimum
- **RTX 5090**: 1000W PSU minimum

---

*This compatibility matrix reflects August 2025 hardware standards and verified component interactions. Always consult individual manufacturer specifications for definitive compatibility confirmation.*
