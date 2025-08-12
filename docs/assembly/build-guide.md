# Step-by-Step PC Build Assembly Guide

*Last updated: August 2025*

## Table of Contents
1. [Pre-Build Preparation](#pre-build-preparation)
2. [Component Installation Order](#component-installation-order)
3. [Detailed Assembly Steps](#detailed-assembly-steps)
4. [First Boot and Setup](#first-boot-and-setup)
5. [Common Issues and Solutions](#common-issues-and-solutions)

## Pre-Build Preparation

### Tools Required
**Essential Tools**:
- Phillips head screwdriver (magnetic tip recommended)
- Anti-static wrist strap (optional but recommended)
- Cable ties or velcro straps
- Thermal paste (if not included with cooler)

**Optional Tools**:
- Parts tray for screws
- Flashlight or headlamp
- Zip ties for cable management
- Compressed air for cleaning

### Workspace Setup
1. **Clean, static-free workspace**: Large desk or table
2. **Good lighting**: Adequate light to see small components
3. **Anti-static mat**: Or regularly touch grounded metal
4. **Component organization**: Keep boxes and accessories organized
5. **Manual access**: Have motherboard and case manuals ready

### Component Checklist
**Before opening anything**, verify you have:
- [ ] Motherboard with I/O shield
- [ ] CPU with cooler
- [ ] RAM modules
- [ ] Graphics card
- [ ] Power supply with all cables
- [ ] Storage drives
- [ ] PC case with screws and standoffs

### Important Safety Notes
⚠️ **Critical Safety Rules**:
- Never force components - they should fit easily
- Handle components by edges, avoid touching pins/contacts
- Keep components in anti-static bags until installation
- Power off and unplug PSU before any connections
- Work methodically - rushing leads to mistakes

## Component Installation Order

### Recommended Assembly Sequence
This order minimizes rework and provides easier access:

1. **Prepare the case** (install standoffs, I/O shield)
2. **Install PSU** (orient fan correctly, route basic cables)
3. **Prepare motherboard outside case** (CPU, RAM, M.2 drives)
4. **Install motherboard** (secure to standoffs)
5. **Install storage drives** (SATA drives in bays)
6. **Install CPU cooler** (air cooler or AIO radiator)
7. **Connect all power cables** (motherboard, CPU, drives)
8. **Install graphics card** (last, heaviest component)
9. **Connect all data cables** (SATA, front panel connectors)
10. **Cable management** (route and secure all cables)
11. **Final checks** (verify all connections)

### Why This Order Works
- **CPU installation outside case**: Easier access and no risk of dropping onto motherboard
- **PSU first**: Establishes cable routing paths early
- **GPU last**: Prevents interference during other installations
- **Cooling after motherboard**: Ensures proper mounting alignment

## Detailed Assembly Steps

### Step 1: Case Preparation

#### Install I/O Shield
1. **Locate I/O shield**: Comes with motherboard, not case
2. **Orient correctly**: Ports should align with motherboard layout
3. **Press firmly into case**: Should click into place all around
4. **Check sharp edges**: Be careful of metal tabs that may need bending

#### Install Motherboard Standoffs
1. **Identify form factor**: ATX, Micro-ATX, or Mini-ITX
2. **Install standoffs**: Screw into correct holes for your motherboard size
3. **Count standoffs**: Should match number of mounting holes on motherboard
4. **No extra standoffs**: Remove any that don't align with motherboard holes

#### Initial Cable Routing
1. **Route 24-pin ATX cable**: From PSU location to motherboard area
2. **Route 8-pin CPU cable**: Behind motherboard tray to top-left
3. **Keep cables loose**: Will tighten during final cable management

### Step 2: Power Supply Installation

#### Determine PSU Orientation
**Fan Down** (Recommended if case has bottom ventilation):
- PSU fan intakes cool air from outside case
- More efficient cooling for PSU
- Requires case bottom vent and clearance

**Fan Up** (If case has no bottom ventilation):
- PSU fan intakes air from inside case
- Less efficient but necessary in some cases
- Ensure adequate case ventilation

#### Installation Process
1. **Slide PSU into case**: Fan orientation as determined above
2. **Align with screw holes**: PSU should sit flush with case back
3. **Secure with 4 screws**: From outside back of case
4. **Don't overtighten**: Finger tight plus quarter turn

#### Initial Cable Connections (Modular PSUs)
Connect these cables before final PSU positioning:
- 24-pin ATX motherboard power
- 8-pin CPU power (sometimes 4+4 pin)
- PCIe power cables for graphics card
- SATA power cables for drives

### Step 3: Motherboard Preparation (Outside Case)

#### CPU Installation

**AMD AM5 Installation**:
1. **Open CPU socket**: Lift retention arm fully
2. **Remove plastic cover**: Keep for warranty purposes
3. **Orient CPU correctly**: Match triangle/arrow marks
4. **Place CPU gently**: Should drop in without force
5. **Close retention arm**: Will require moderate pressure

**Intel LGA 1851 Installation**:
1. **Open socket cover**: Lift load plate
2. **Remove plastic cover**: Keep for warranty
3. **Orient CPU correctly**: Match notches on CPU and socket
4. **Place CPU in socket**: Should sit flat without force
5. **Close load plate**: Push down and secure retention arm

⚠️ **Critical CPU Installation Notes**:
- Never force CPU into socket
- Bent pins (AMD) or damaged contacts (Intel) void warranty
- CPU should sit completely flat in socket
- Double-check orientation before closing retention mechanism

#### RAM Installation
1. **Open retention clips**: Pull tabs on sides of RAM slots
2. **Orient RAM correctly**: Match notch on module with slot
3. **Install in correct slots**: Usually slots 2 and 4 for dual-channel
4. **Press down firmly**: Should click into place with tabs closing
5. **Verify secure installation**: Modules should be level and fully seated

#### M.2 NVMe SSD Installation
1. **Locate M.2 slots**: Usually labeled M.2_1, M.2_2, etc.
2. **Remove mounting screw**: Keep track of tiny screw
3. **Insert SSD at angle**: About 30 degrees, pins should be mostly hidden
4. **Press down flat**: SSD should lie flat against motherboard
5. **Secure with screw**: Don't overtighten

### Step 4: Motherboard Installation

#### Prepare Motherboard for Installation
1. **Test fit first**: Lower motherboard to check alignment with standoffs
2. **I/O shield alignment**: Ensure ports align with I/O shield openings
3. **No interference**: Check for clearance around all edges

#### Secure Motherboard
1. **Start with corner screws**: Diagonal pattern for even pressure
2. **Hand tighten first**: Get all screws started before final tightening
3. **Tighten gradually**: Work in diagonal pattern
4. **Don't overtighten**: Motherboard should be secure but not stressed

#### Verify Installation
- All mounting holes have standoffs
- Motherboard sits flat against standoffs
- I/O ports align properly with shield
- No stress or bowing of motherboard

### Step 5: Storage Drive Installation

#### 2.5" SSD Installation
1. **Mount in drive bay**: Use provided screws
2. **Connect SATA data cable**: To motherboard SATA port
3. **Connect SATA power**: From PSU
4. **Secure cables**: Avoid stress on connectors

#### 3.5" HDD Installation
1. **Slide into drive bay**: Orient with connectors toward back
2. **Secure with screws**: Both sides typically
3. **Connect SATA data and power**: Same as SSD
4. **Check clearance**: Ensure no interference with other components

### Step 6: CPU Cooler Installation

#### Air Cooler Installation
1. **Apply thermal paste**: Pea-sized dot on CPU (if not pre-applied)
2. **Install mounting brackets**: According to socket type
3. **Mount cooler**: Even pressure, cross-pattern tightening
4. **Connect fan cable**: To CPU_FAN header on motherboard
5. **Check clearance**: RAM, case side panel, GPU clearance

#### AIO Cooler Installation
1. **Mount radiator**: Top or front of case with fans
2. **Apply thermal paste**: If not pre-applied on pump block
3. **Mount pump/block**: Even pressure, secure mounting
4. **Connect pump power**: CPU_FAN or AIO_PUMP header
5. **Connect fan cables**: For radiator fans

### Step 7: Power Cable Connections

#### Essential Power Connections
1. **24-pin ATX**: Main motherboard power (largest connector)
2. **8-pin CPU**: Top-left of motherboard (sometimes 4+4 pin)
3. **PCIe power**: For graphics card (when installed)
4. **SATA power**: For storage drives
5. **Case fans**: PWM headers on motherboard

#### Power Connection Tips
- **Fully seated**: All power connectors should click into place
- **Correct orientation**: Connectors only fit one way
- **No forcing**: If it doesn't fit easily, check orientation
- **Cable management**: Route cables neatly behind motherboard tray

### Step 8: Graphics Card Installation

#### Prepare for GPU Installation
1. **Remove slot covers**: From case back panel (usually 2-3 slots)
2. **Open PCIe retention clip**: On motherboard PCIe x16 slot
3. **Plan power cables**: Route PCIe power cables to GPU area

#### Install Graphics Card
1. **Align with PCIe slot**: GPU should be level with slot
2. **Insert firmly**: Press down until retention clip clicks
3. **Secure to case**: Screw GPU bracket to case back panel
4. **Connect power**: PCIe 8-pin, 6+2 pin, or 12V-2x6 connector
5. **Check clearance**: Case side panel, power cables, cooler

### Step 9: Front Panel and Data Connections

#### Front Panel Connectors
Small connectors from case to motherboard:
- **Power button**: PWR_BTN or similar
- **Reset button**: RESET or RST
- **Power LED**: PWR_LED (+ and - orientation matters)
- **HDD LED**: HDD_LED or similar
- **USB connectors**: USB 2.0 and USB 3.0/3.2 headers

#### Audio and USB Headers
- **Front panel audio**: HD_AUDIO header
- **USB 3.0**: Usually blue connector
- **USB 2.0**: Black connector, multiple ports possible
- **USB-C**: If case has front USB-C port

#### Reference Motherboard Manual
Front panel pinout varies by manufacturer - always check motherboard manual for correct pin layout.

### Step 10: Final Cable Management

#### Cable Routing Strategy
1. **Route behind motherboard tray**: Most cables should be hidden
2. **Use cable ties**: Secure cables to built-in tie points
3. **Group similar cables**: Route power and data cables separately when possible
4. **Maintain airflow**: Don't block case fans or ventilation

#### Common Cable Management Areas
- **24-pin ATX**: Route along right edge of motherboard
- **CPU 8-pin**: Route behind motherboard to top-left
- **GPU power**: Route cleanly to graphics card
- **SATA cables**: Bundle together, route to drives

## First Boot and Setup

### Pre-Boot Checklist
Before pressing power button:
- [ ] PSU power switch ON
- [ ] All power connections secure
- [ ] RAM properly seated
- [ ] GPU properly seated and powered
- [ ] Monitor connected to GPU (not motherboard)
- [ ] Keyboard/mouse connected

### Initial Power On
1. **Press power button**: Should see case fans spin, lights activate
2. **Check for POST**: Display should show BIOS/UEFI screen
3. **Enter BIOS**: Usually Delete, F2, or F12 key during boot
4. **Verify components**: Check CPU, RAM, storage detection

### BIOS/UEFI Initial Setup
1. **Enable XMP/DOCP**: For RAM to run at rated speeds
2. **Check temperatures**: CPU should be under 50°C at idle
3. **Set boot priority**: If installing OS from USB
4. **Update BIOS**: If newer version available
5. **Save and exit**: F10 typically saves and reboots

### OS Installation
1. **Create Windows 11 installation media**: On another computer
2. **Boot from USB**: Set USB as first boot device
3. **Follow installation wizard**: Choose custom installation
4. **Install on NVMe/SSD**: For best performance
5. **Complete initial Windows setup**

### Post-Installation Tasks
1. **Install motherboard chipset drivers**
2. **Install graphics card drivers**
3. **Update Windows**: Install all available updates
4. **Install essential software**: Browsers, utilities, games
5. **Run stress tests**: Verify system stability

## Common Issues and Solutions

### System Won't Turn On
**Symptoms**: No response when pressing power button

**Troubleshooting**:
1. Check PSU power switch (O = Off, I = On)
2. Verify PSU cable connection to wall outlet
3. Check 24-pin and 8-pin power connections
4. Verify front panel power button connection
5. Test PSU with paperclip test
6. Try single RAM stick in different slot

### No Display Output
**Symptoms**: System powers on but no display

**Troubleshooting**:
1. Check monitor cable connection (HDMI, DisplayPort)
2. Ensure monitor connected to GPU, not motherboard
3. Verify GPU power connections
4. Try different display cable
5. Test with single RAM stick
6. Clear CMOS (check motherboard manual)

### System Boots Then Shuts Down
**Symptoms**: Powers on for few seconds then shuts off

**Troubleshooting**:
1. Check CPU cooler installation and thermal paste
2. Verify CPU power (8-pin) connection
3. Check for short circuits (standoffs, loose screws)
4. Test with minimal components (CPU, one RAM stick, PSU)
5. Verify PSU wattage adequate for components

### BIOS Doesn't Detect RAM
**Symptoms**: BIOS shows less RAM than installed

**Troubleshooting**:
1. Verify RAM seated properly in slots
2. Try one stick at a time to identify faulty module
3. Check motherboard manual for correct slot population
4. Test RAM in different slots
5. Update BIOS to latest version

### High Temperatures
**Symptoms**: CPU/GPU running hot under load

**Troubleshooting**:
1. Check thermal paste application on CPU
2. Verify CPU cooler properly mounted
3. Check case fan configuration (intake vs exhaust)
4. Clean dust from components
5. Verify adequate PSU wattage (undervoltage can cause heat)

### Blue Screen or System Crashes
**Symptoms**: Random crashes, blue screen errors

**Troubleshooting**:
1. Run Windows Memory Diagnostic
2. Check for overheating components
3. Update all drivers (GPU, chipset, etc.)
4. Run system file checker (sfc /scannow)
5. Test with XMP/DOCP disabled
6. Check PSU stability under load

### Debugging Tools and Resources
- **HWiNFO64**: Comprehensive system monitoring
- **MemTest86**: RAM testing utility
- **Prime95**: CPU stress testing
- **FurMark**: GPU stress testing
- **CrystalDiskInfo**: Storage health monitoring

### When to Seek Help
Contact support or seek professional help if:
- Multiple components fail simultaneously
- Smoke or burning smell from any component
- Physical damage to components
- Repeated failures after following troubleshooting steps
- System works initially but degrades over time

---

## Final Tips for Success

### Best Practices
1. **Take your time**: Rushing leads to mistakes and damaged components
2. **Read manuals**: Motherboard and case manuals have crucial information
3. **Document as you go**: Take photos before disconnecting anything
4. **Test incrementally**: Power on after major steps to catch issues early
5. **Keep workspace organized**: Track screws and small parts carefully

### Maintenance Schedule
**Monthly**: Check temperatures, clean dust filters
**Quarterly**: Deep clean with compressed air
**Annually**: Replace thermal paste, check for loose connections

### Upgrade Considerations
Plan for future upgrades:
- Leave headroom in PSU wattage
- Choose motherboards with upgrade paths
- Ensure case has room for larger GPUs
- Document current configuration for future reference

---

*This guide reflects current best practices for PC assembly in August 2025, incorporating feedback from thousands of successful builds in the Indian PC building community.*
