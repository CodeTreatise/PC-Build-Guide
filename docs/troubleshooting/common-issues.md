# Common PC Building Issues and Solutions

*Last updated: August 2025*

## Power Issues

### System Won't Turn On (No Lights, No Fans)

#### Symptoms
- No response when pressing power button
- No LED lights on motherboard
- No fan spinning
- Complete silence from system

#### Troubleshooting Steps
1. **Check PSU power switch**: Ensure switched to "I" (ON) position
2. **Verify wall outlet**: Test outlet with another device
3. **PSU cable connection**: Ensure PSU cable firmly connected to wall and PSU
4. **Front panel connectors**: Verify power button connected to correct pins
5. **24-pin ATX connector**: Ensure fully seated and clicked in place
6. **8-pin CPU power**: Check top-left motherboard connector

#### Advanced Diagnostics
**PSU Paperclip Test**:
1. Disconnect all PSU cables from components
2. Short green wire to any black wire on 24-pin connector
3. PSU fan should spin if PSU functional
4. If PSU works but system doesn't, motherboard issue likely

**Minimal Configuration Test**:
- Remove all components except CPU, one RAM stick, PSU
- Remove GPU, use integrated graphics if available
- Disconnect all drives and peripherals
- Try to POST with minimal setup

### System Powers On But Immediately Shuts Off

#### Symptoms
- Fans spin for 1-3 seconds then stop
- System cycles on/off repeatedly
- May see brief LED activity

#### Common Causes
1. **CPU overheating**: Cooler not properly mounted
2. **PSU insufficient**: Not enough wattage for components
3. **RAM issues**: Incompatible or faulty memory
4. **Short circuit**: Metal touching motherboard inappropriately
5. **CPU power**: 8-pin connector not connected

#### Solutions
1. **Check CPU cooler mounting**: Ensure even pressure, thermal paste applied
2. **Verify PSU wattage**: Calculate total system power draw
3. **Test single RAM stick**: Try different slots, different modules
4. **Remove standoff shorts**: Check no extra standoffs under motherboard
5. **Disconnect non-essential**: Remove all except basic components

### Random System Shutdowns During Use

#### Symptoms
- System shuts down without warning during operation
- May occur under load or idle
- Restarts automatically or requires manual power on

#### Troubleshooting
1. **Temperature monitoring**: Check CPU/GPU temperatures with HWiNFO64
2. **PSU stress test**: Run Prime95 + FurMark simultaneously
3. **Event Viewer**: Check Windows logs for shutdown causes
4. **RAM testing**: Run Windows Memory Diagnostic or MemTest86
5. **Power settings**: Disable fast startup, check power plan settings

## Display Issues

### No Display Output

#### Symptoms
- Monitor shows "No Signal" message
- Black screen but system appears to run
- Monitor stays in standby mode

#### Step-by-Step Diagnosis
1. **Monitor connection**: Ensure cable connected to GPU, not motherboard
2. **Monitor power**: Verify monitor powered on and functional
3. **Cable testing**: Try different cable (HDMI, DisplayPort)
4. **Input selection**: Check monitor input source selection
5. **GPU seating**: Reseat graphics card in PCIe slot
6. **GPU power**: Verify all PCIe power connectors attached

#### Advanced Solutions
**Integrated Graphics Test**:
- Remove dedicated GPU
- Connect monitor to motherboard output
- If display works, GPU or GPU power issue

**CMOS Clear**:
1. Power off system completely
2. Remove CMOS battery for 5 minutes
3. Or use CMOS clear jumper per motherboard manual
4. Reinstall battery, power on

**RAM Reseating**:
- Remove all RAM modules
- Clean contacts with isopropyl alcohol
- Install one stick in different slots
- Test each module individually

### Display Artifacts or Corruption

#### Symptoms
- Strange colors, lines, or patterns on screen
- Flickering or unstable image
- Partial display corruption

#### Causes and Solutions
1. **GPU overheating**: Check GPU temperatures, clean fans
2. **VRAM issues**: Run GPU memory test (VRAM test in FurMark)
3. **Driver corruption**: Uninstall GPU drivers with DDU, reinstall latest
4. **Cable issues**: Try different display cable
5. **Monitor issues**: Test with different monitor
6. **Overclocking**: Reset GPU to stock speeds

## Boot and BIOS Issues

### System POSTs But Won't Boot to Windows

#### Symptoms
- BIOS/UEFI screens appear normally
- Gets stuck at Windows loading screen
- Boot device not found errors

#### Solutions
1. **Boot device priority**: Set correct drive as first boot device
2. **SATA cable check**: Ensure storage drive connections secure
3. **Boot mode**: Verify UEFI vs Legacy boot mode matches installation
4. **Secure Boot**: Disable if causing compatibility issues
5. **Windows repair**: Boot from Windows installation media, try repair

### Stuck in BIOS Loop

#### Symptoms
- System boots to BIOS every time
- Can't exit BIOS to normal boot
- BIOS settings don't save

#### Troubleshooting
1. **CMOS battery**: Replace motherboard battery (CR2032)
2. **Load defaults**: Reset BIOS to factory defaults
3. **Boot device detection**: Ensure storage drives detected in BIOS
4. **Fast Boot**: Disable fast boot options
5. **CSM settings**: Enable/disable Compatibility Support Module

### BIOS Won't Load/Black Screen

#### Symptoms
- No BIOS splash screen
- Can't enter BIOS setup
- System appears dead but fans spin

#### Solutions
1. **Clear CMOS**: Reset BIOS settings to defaults
2. **CPU compatibility**: Verify CPU supported by motherboard
3. **BIOS version**: May need BIOS update for CPU compatibility
4. **Minimal hardware**: Remove all except CPU, RAM, PSU
5. **Motherboard inspection**: Check for damaged components

## Memory Issues

### System Doesn't Detect All Installed RAM

#### Symptoms
- BIOS shows less RAM than physically installed
- Windows reports incorrect memory amount
- Only some modules detected

#### Diagnosis Steps
1. **Module compatibility**: Check motherboard QVL (Qualified Vendor List)
2. **Slot population**: Use correct slots for dual channel (usually 2,4)
3. **Individual testing**: Test each module separately
4. **Slot testing**: Try working modules in different slots
5. **Clean contacts**: Remove modules, clean with isopropyl alcohol

### Blue Screen Errors Related to Memory

#### Common BSOD Codes
- MEMORY_MANAGEMENT
- IRQL_NOT_LESS_OR_EQUAL
- PAGE_FAULT_IN_NONPAGED_AREA
- SYSTEM_SERVICE_EXCEPTION

#### Solutions
1. **Memory testing**: Run Windows Memory Diagnostic (mdsched.exe)
2. **Extended testing**: Boot MemTest86, run for 8+ hours
3. **XMP/DOCP disable**: Turn off memory overclocking
4. **Voltage adjustment**: Slightly increase DRAM voltage (1.35V → 1.4V)
5. **Single module**: Test system stability with one RAM stick

### Slow Performance Despite Adequate RAM

#### Symptoms
- System sluggish despite sufficient RAM capacity
- Applications take long to load
- Frequent hard drive activity

#### Checks
1. **Memory speed**: Verify RAM running at rated speeds (XMP enabled)
2. **Dual channel**: Ensure modules installed in correct slots
3. **Background apps**: Check Task Manager for memory usage
4. **Virtual memory**: Verify page file settings appropriate
5. **Driver issues**: Update chipset and memory controller drivers

## Storage Issues

### SSD/HDD Not Detected

#### Symptoms
- Drive doesn't appear in BIOS
- Drive not visible in Windows Disk Management
- System can't find boot device

#### Troubleshooting
1. **Cable connections**: Check both SATA data and power cables
2. **Different cables**: Try different SATA data cable
3. **Different ports**: Try different motherboard SATA ports
4. **Power supply**: Verify sufficient PSU SATA power connectors
5. **Drive testing**: Test drive in different computer

### M.2 NVMe SSD Issues

#### Common Problems
- Drive not detected in BIOS
- Slower than expected performance
- System won't boot from M.2 drive

#### Solutions
1. **Slot compatibility**: Verify M.2 slot supports NVMe (not just SATA)
2. **PCIe lane conflicts**: Check if M.2 slot shares lanes with other slots
3. **BIOS settings**: Enable NVMe support, check boot priority
4. **Thermal throttling**: Ensure M.2 SSD has adequate cooling
5. **Firmware update**: Check for SSD firmware updates

### Slow Storage Performance

#### Symptoms
- Longer than expected boot times
- Slow file transfers
- Applications load slowly

#### Performance Checks
1. **Benchmark testing**: Use CrystalDiskMark or AS SSD Benchmark
2. **SATA mode**: Ensure SATA mode set to AHCI (not IDE)
3. **Drive health**: Check S.M.A.R.T. data with CrystalDiskInfo
4. **Free space**: Maintain 15-20% free space on SSDs
5. **TRIM status**: Verify TRIM enabled for SSDs

## Cooling and Temperature Issues

### High CPU Temperatures

#### Dangerous Temperature Ranges
- **Intel**: >85°C concerning, >100°C critical
- **AMD**: >85°C concerning, >95°C critical
- **Thermal throttling**: Performance reduces to prevent damage

#### Solutions
1. **Cooler mounting**: Check CPU cooler properly mounted with even pressure
2. **Thermal paste**: Reapply if old, dried, or improperly applied
3. **Case airflow**: Ensure adequate intake and exhaust fans
4. **Dust cleaning**: Clean CPU cooler fins and case fans
5. **Cooler adequacy**: Verify cooler rated for CPU TDP

### High GPU Temperatures

#### Temperature Guidelines
- **RTX 5060/5060 Ti**: <80°C good, >90°C concerning
- **RTX 5070/5070 Ti**: <85°C good, >95°C concerning
- **RTX 5080/5090**: <87°C good, >95°C concerning

#### Cooling Solutions
1. **Fan curves**: Adjust GPU fan curves for more aggressive cooling
2. **Case ventilation**: Improve case airflow, especially GPU intake
3. **Undervolting**: Reduce GPU voltage while maintaining performance
4. **Dust removal**: Clean GPU fans and heatsink
5. **Thermal pads**: Replace thermal pads if very old GPU

### System Overheating

#### Symptoms
- Multiple components running hot
- Frequent thermal throttling
- System instability under load

#### Comprehensive Solutions
1. **Case fan configuration**: Set up proper intake/exhaust airflow
2. **Positive pressure**: More intake than exhaust reduces dust
3. **Cable management**: Improve airflow by routing cables properly
4. **Component spacing**: Ensure adequate clearance around hot components
5. **Ambient temperature**: Consider room temperature and case location

## Performance Issues

### Lower Than Expected Gaming Performance

#### Symptoms
- FPS lower than benchmarks suggest
- Stuttering or frame drops
- Performance worse than similar builds

#### Diagnostic Steps
1. **GPU driver update**: Install latest graphics drivers
2. **Background processes**: Close unnecessary applications
3. **Windows updates**: Ensure Windows fully updated
4. **Power settings**: Set Windows power plan to "High Performance"
5. **Game settings**: Verify appropriate quality settings for hardware

#### Advanced Optimization
1. **RAM speed verification**: Ensure XMP/DOCP enabled for rated speeds
2. **GPU boost clocks**: Monitor actual vs advertised boost clocks
3. **CPU utilization**: Check for CPU bottlenecks in CPU-heavy games
4. **Storage performance**: Ensure games installed on fast storage
5. **Thermal throttling**: Monitor temperatures during gaming

### System Feels Slow Despite Good Specifications

#### Common Causes
1. **HDD as boot drive**: Upgrade to SSD for significant improvement
2. **Insufficient RAM**: 16GB minimum for modern systems
3. **Background software**: Bloatware or resource-heavy applications
4. **Windows indexing**: Search indexing using CPU resources
5. **Malware**: Run full system scan with Windows Defender

## Hardware Compatibility Issues

### Components Not Working Together

#### Symptoms
- System works with some components but not others
- Instability when all components installed
- Performance lower than individual component capabilities

#### Compatibility Checks
1. **CPU/Motherboard**: Verify socket and chipset compatibility
2. **RAM compatibility**: Check motherboard QVL for memory
3. **PSU adequacy**: Ensure sufficient wattage and connectors
4. **Physical clearance**: Check component sizes fit in case
5. **PCIe slot availability**: Verify adequate expansion slots

### New Component Causes Issues

#### Troubleshooting New Installs
1. **Driver installation**: Install appropriate drivers for new component
2. **BIOS update**: May need motherboard BIOS update for compatibility
3. **Power requirements**: Verify PSU can handle additional power draw
4. **Conflict resolution**: Check for resource conflicts with existing hardware
5. **Incremental testing**: Install one component at a time

## Getting Help

### When to Seek Professional Help
- Multiple troubleshooting attempts fail
- Potential hardware damage suspected
- Warranty concerns about self-repair
- Lack confidence in performing procedures
- System needs specialized tools or expertise

### Preparing for Tech Support
1. **Document symptoms**: Write down exact error messages
2. **List recent changes**: Note any new hardware or software
3. **Component list**: Prepare full system specifications
4. **Testing results**: Record what troubleshooting already attempted
5. **Warranty information**: Gather purchase receipts and warranty terms

### Online Resources
- **Manufacturer websites**: Official troubleshooting guides
- **Community forums**: Reddit r/buildapc, Tom's Hardware
- **Video guides**: YouTube channels for visual troubleshooting
- **Official support**: Manufacturer chat/phone support

---

## Prevention Tips

### Building Best Practices
- Read all manuals before starting
- Work in well-lit, static-free environment
- Take photos during disassembly for reference
- Keep components in anti-static bags until installation
- Test components before final assembly

### Maintenance Schedule
- **Monthly**: Check temperatures, clean dust filters
- **Quarterly**: Clean internal components with compressed air  
- **Annually**: Replace thermal paste, check connections
- **As needed**: Update drivers, monitor component health

---

*This troubleshooting guide covers the most common issues encountered when building and maintaining PCs in the Indian market. When in doubt, consult component manuals and manufacturer support resources.*
