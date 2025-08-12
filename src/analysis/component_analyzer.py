"""
Component Analysis Module
Detailed analysis tools for different PC components
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple
import re
from dataclasses import dataclass
from ..utils.helpers import extract_numeric_value, parse_memory_capacity, parse_clock_speed

@dataclass
class CPUSpecs:
    """CPU specifications data class"""
    name: str
    brand: str
    series: str
    cores: int
    threads: int
    base_clock: float  # GHz
    boost_clock: float  # GHz
    tdp: int  # Watts
    socket: str
    cache_l3: int  # MB
    integrated_graphics: bool
    process_node: int  # nm
    price: float

@dataclass
class GPUSpecs:
    """GPU specifications data class"""
    name: str
    brand: str
    series: str
    memory_size: int  # GB
    memory_type: str
    memory_bus: int  # bit
    base_clock: int  # MHz
    boost_clock: int  # MHz
    cuda_cores: Optional[int]
    stream_processors: Optional[int]
    tdp: int  # Watts
    outputs: List[str]
    ray_tracing: bool
    dlss_fsr: bool
    price: float

@dataclass
class MotherboardSpecs:
    """Motherboard specifications data class"""
    name: str
    brand: str
    socket: str
    chipset: str
    form_factor: str
    memory_slots: int
    max_memory: int  # GB
    memory_type: str
    pcie_slots: Dict[str, int]
    sata_ports: int
    m2_slots: int
    usb_ports: Dict[str, int]
    ethernet: str
    wifi: bool
    bluetooth: bool
    price: float

class ComponentAnalyzer:
    """Main component analysis class"""
    
    def __init__(self):
        self.cpu_data = []
        self.gpu_data = []
        self.motherboard_data = []
    
    def analyze_cpu(self, cpu_name: str, specs: Dict) -> CPUSpecs:
        """
        Analyze CPU specifications
        
        Args:
            cpu_name: CPU name
            specs: Raw specifications dictionary
            
        Returns:
            CPUSpecs object with parsed data
        """
        # Extract brand
        brand = self._extract_cpu_brand(cpu_name)
        
        # Extract series
        series = self._extract_cpu_series(cpu_name, brand)
        
        # Parse specifications
        cores = self._extract_cores(specs)
        threads = self._extract_threads(specs)
        base_clock = self._extract_base_clock(specs)
        boost_clock = self._extract_boost_clock(specs)
        tdp = self._extract_tdp(specs)
        socket = self._extract_socket(specs)
        cache_l3 = self._extract_cache(specs)
        integrated_graphics = self._has_integrated_graphics(cpu_name, specs)
        process_node = self._extract_process_node(specs, brand, series)
        price = self._extract_price(specs)
        
        return CPUSpecs(
            name=cpu_name,
            brand=brand,
            series=series,
            cores=cores,
            threads=threads,
            base_clock=base_clock,
            boost_clock=boost_clock,
            tdp=tdp,
            socket=socket,
            cache_l3=cache_l3,
            integrated_graphics=integrated_graphics,
            process_node=process_node,
            price=price
        )
    
    def analyze_gpu(self, gpu_name: str, specs: Dict) -> GPUSpecs:
        """
        Analyze GPU specifications
        
        Args:
            gpu_name: GPU name
            specs: Raw specifications dictionary
            
        Returns:
            GPUSpecs object with parsed data
        """
        # Extract brand
        brand = self._extract_gpu_brand(gpu_name)
        
        # Extract series
        series = self._extract_gpu_series(gpu_name, brand)
        
        # Parse specifications
        memory_size = self._extract_gpu_memory(specs)
        memory_type = self._extract_memory_type(specs)
        memory_bus = self._extract_memory_bus(specs)
        base_clock = self._extract_gpu_base_clock(specs)
        boost_clock = self._extract_gpu_boost_clock(specs)
        cuda_cores = self._extract_cuda_cores(specs) if brand.lower() == 'nvidia' else None
        stream_processors = self._extract_stream_processors(specs) if brand.lower() == 'amd' else None
        tdp = self._extract_tdp(specs)
        outputs = self._extract_outputs(specs)
        ray_tracing = self._has_ray_tracing(gpu_name, specs)
        dlss_fsr = self._has_dlss_fsr(gpu_name, brand)
        price = self._extract_price(specs)
        
        return GPUSpecs(
            name=gpu_name,
            brand=brand,
            series=series,
            memory_size=memory_size,
            memory_type=memory_type,
            memory_bus=memory_bus,
            base_clock=base_clock,
            boost_clock=boost_clock,
            cuda_cores=cuda_cores,
            stream_processors=stream_processors,
            tdp=tdp,
            outputs=outputs,
            ray_tracing=ray_tracing,
            dlss_fsr=dlss_fsr,
            price=price
        )
    
    def analyze_motherboard(self, mb_name: str, specs: Dict) -> MotherboardSpecs:
        """
        Analyze motherboard specifications
        
        Args:
            mb_name: Motherboard name
            specs: Raw specifications dictionary
            
        Returns:
            MotherboardSpecs object with parsed data
        """
        brand = self._extract_motherboard_brand(mb_name)
        socket = self._extract_socket(specs)
        chipset = self._extract_chipset(specs)
        form_factor = self._extract_form_factor(specs)
        memory_slots = self._extract_memory_slots(specs)
        max_memory = self._extract_max_memory(specs)
        memory_type = self._extract_supported_memory_type(specs)
        pcie_slots = self._extract_pcie_slots(specs)
        sata_ports = self._extract_sata_ports(specs)
        m2_slots = self._extract_m2_slots(specs)
        usb_ports = self._extract_usb_ports(specs)
        ethernet = self._extract_ethernet(specs)
        wifi = self._has_wifi(specs)
        bluetooth = self._has_bluetooth(specs)
        price = self._extract_price(specs)
        
        return MotherboardSpecs(
            name=mb_name,
            brand=brand,
            socket=socket,
            chipset=chipset,
            form_factor=form_factor,
            memory_slots=memory_slots,
            max_memory=max_memory,
            memory_type=memory_type,
            pcie_slots=pcie_slots,
            sata_ports=sata_ports,
            m2_slots=m2_slots,
            usb_ports=usb_ports,
            ethernet=ethernet,
            wifi=wifi,
            bluetooth=bluetooth,
            price=price
        )
    
    # CPU Analysis Helper Methods
    def _extract_cpu_brand(self, cpu_name: str) -> str:
        """Extract CPU brand from name"""
        name_lower = cpu_name.lower()
        if 'intel' in name_lower or 'core' in name_lower:
            return 'Intel'
        elif 'amd' in name_lower or 'ryzen' in name_lower:
            return 'AMD'
        return 'Unknown'
    
    def _extract_cpu_series(self, cpu_name: str, brand: str) -> str:
        """Extract CPU series from name"""
        name_lower = cpu_name.lower()
        
        if brand == 'Intel':
            if 'core i9' in name_lower:
                return 'Core i9'
            elif 'core i7' in name_lower:
                return 'Core i7'
            elif 'core i5' in name_lower:
                return 'Core i5'
            elif 'core i3' in name_lower:
                return 'Core i3'
        elif brand == 'AMD':
            if 'ryzen 9' in name_lower:
                return 'Ryzen 9'
            elif 'ryzen 7' in name_lower:
                return 'Ryzen 7'
            elif 'ryzen 5' in name_lower:
                return 'Ryzen 5'
            elif 'ryzen 3' in name_lower:
                return 'Ryzen 3'
        
        return 'Unknown'
    
    def _extract_cores(self, specs: Dict) -> int:
        """Extract number of cores"""
        for key, value in specs.items():
            if 'core' in key.lower() and 'thread' not in key.lower():
                cores = extract_numeric_value(str(value))
                if cores:
                    return int(cores)
        return 0
    
    def _extract_threads(self, specs: Dict) -> int:
        """Extract number of threads"""
        for key, value in specs.items():
            if 'thread' in key.lower():
                threads = extract_numeric_value(str(value))
                if threads:
                    return int(threads)
        return 0
    
    def _extract_base_clock(self, specs: Dict) -> float:
        """Extract base clock speed"""
        for key, value in specs.items():
            if 'base' in key.lower() and 'clock' in key.lower():
                return parse_clock_speed(str(value)) or 0.0
        return 0.0
    
    def _extract_boost_clock(self, specs: Dict) -> float:
        """Extract boost clock speed"""
        for key, value in specs.items():
            if any(term in key.lower() for term in ['boost', 'turbo', 'max']):
                if 'clock' in key.lower():
                    return parse_clock_speed(str(value)) or 0.0
        return 0.0
    
    def _extract_tdp(self, specs: Dict) -> int:
        """Extract TDP (Thermal Design Power)"""
        for key, value in specs.items():
            if 'tdp' in key.lower() or 'power' in key.lower():
                tdp = extract_numeric_value(str(value), 'W')
                if tdp:
                    return int(tdp)
        return 0
    
    def _extract_socket(self, specs: Dict) -> str:
        """Extract CPU socket type"""
        for key, value in specs.items():
            if 'socket' in key.lower():
                return str(value)
        return 'Unknown'
    
    def _extract_cache(self, specs: Dict) -> int:
        """Extract L3 cache size in MB"""
        for key, value in specs.items():
            if 'cache' in key.lower() and 'l3' in key.lower():
                cache = extract_numeric_value(str(value), 'MB')
                if cache:
                    return int(cache)
        return 0
    
    def _has_integrated_graphics(self, cpu_name: str, specs: Dict) -> bool:
        """Check if CPU has integrated graphics"""
        name_lower = cpu_name.lower()
        
        # Intel naming conventions
        if any(term in name_lower for term in ['uhd', 'iris', 'xe']):
            return True
        
        # AMD naming conventions
        if 'g' in name_lower and 'amd' in name_lower:
            return True
        
        # Check specs
        for key, value in specs.items():
            if 'graphics' in key.lower():
                return 'yes' in str(value).lower() or 'integrated' in str(value).lower()
        
        return False
    
    def _extract_process_node(self, specs: Dict, brand: str, series: str) -> int:
        """Extract manufacturing process node"""
        for key, value in specs.items():
            if 'process' in key.lower() or 'node' in key.lower():
                node = extract_numeric_value(str(value), 'nm')
                if node:
                    return int(node)
        
        # Fallback to known architectures
        if brand == 'AMD':
            if 'ryzen 7000' in series.lower() or 'ryzen 9000' in series.lower():
                return 5
            elif 'ryzen 5000' in series.lower():
                return 7
        elif brand == 'Intel':
            if '13th' in series.lower() or '12th' in series.lower():
                return 10
        
        return 0
    
    # GPU Analysis Helper Methods
    def _extract_gpu_brand(self, gpu_name: str) -> str:
        """Extract GPU brand from name"""
        name_lower = gpu_name.lower()
        if 'nvidia' in name_lower or 'rtx' in name_lower or 'gtx' in name_lower:
            return 'NVIDIA'
        elif 'amd' in name_lower or 'radeon' in name_lower or 'rx' in name_lower:
            return 'AMD'
        return 'Unknown'
    
    def _extract_gpu_series(self, gpu_name: str, brand: str) -> str:
        """Extract GPU series from name"""
        name_lower = gpu_name.lower()
        
        if brand == 'NVIDIA':
            if 'rtx 40' in name_lower:
                return 'RTX 40 Series'
            elif 'rtx 30' in name_lower:
                return 'RTX 30 Series'
            elif 'rtx 20' in name_lower:
                return 'RTX 20 Series'
            elif 'gtx 16' in name_lower:
                return 'GTX 16 Series'
        elif brand == 'AMD':
            if 'rx 7000' in name_lower:
                return 'RX 7000 Series'
            elif 'rx 6000' in name_lower:
                return 'RX 6000 Series'
            elif 'rx 5000' in name_lower:
                return 'RX 5000 Series'
        
        return 'Unknown'
    
    def _extract_gpu_memory(self, specs: Dict) -> int:
        """Extract GPU memory size in GB"""
        for key, value in specs.items():
            if 'memory' in key.lower() and 'size' in key.lower():
                memory = parse_memory_capacity(str(value))
                if memory:
                    return memory
        return 0
    
    def _extract_memory_type(self, specs: Dict) -> str:
        """Extract memory type (GDDR6, GDDR6X, etc.)"""
        for key, value in specs.items():
            if 'memory' in key.lower() and 'type' in key.lower():
                return str(value)
        return 'Unknown'
    
    def _extract_memory_bus(self, specs: Dict) -> int:
        """Extract memory bus width"""
        for key, value in specs.items():
            if 'bus' in key.lower():
                bus = extract_numeric_value(str(value), 'bit')
                if bus:
                    return int(bus)
        return 0
    
    def _extract_gpu_base_clock(self, specs: Dict) -> int:
        """Extract GPU base clock in MHz"""
        for key, value in specs.items():
            if 'base' in key.lower() and 'clock' in key.lower():
                clock = extract_numeric_value(str(value), 'MHz')
                if clock:
                    return int(clock)
        return 0
    
    def _extract_gpu_boost_clock(self, specs: Dict) -> int:
        """Extract GPU boost clock in MHz"""
        for key, value in specs.items():
            if 'boost' in key.lower() and 'clock' in key.lower():
                clock = extract_numeric_value(str(value), 'MHz')
                if clock:
                    return int(clock)
        return 0
    
    def _extract_cuda_cores(self, specs: Dict) -> Optional[int]:
        """Extract CUDA cores count"""
        for key, value in specs.items():
            if 'cuda' in key.lower():
                cores = extract_numeric_value(str(value))
                if cores:
                    return int(cores)
        return None
    
    def _extract_stream_processors(self, specs: Dict) -> Optional[int]:
        """Extract stream processors count"""
        for key, value in specs.items():
            if 'stream' in key.lower() or 'compute' in key.lower():
                processors = extract_numeric_value(str(value))
                if processors:
                    return int(processors)
        return None
    
    def _extract_outputs(self, specs: Dict) -> List[str]:
        """Extract display outputs"""
        outputs = []
        for key, value in specs.items():
            if 'output' in key.lower() or 'display' in key.lower():
                output_text = str(value).lower()
                if 'hdmi' in output_text:
                    outputs.append('HDMI')
                if 'displayport' in output_text or 'dp' in output_text:
                    outputs.append('DisplayPort')
                if 'usb-c' in output_text:
                    outputs.append('USB-C')
        return list(set(outputs))
    
    def _has_ray_tracing(self, gpu_name: str, specs: Dict) -> bool:
        """Check if GPU supports ray tracing"""
        name_lower = gpu_name.lower()
        
        # NVIDIA RTX series have ray tracing
        if 'rtx' in name_lower:
            return True
        
        # AMD RX 6000+ series have ray tracing
        if 'rx' in name_lower:
            rx_match = re.search(r'rx\s*(\d+)', name_lower)
            if rx_match and int(rx_match.group(1)) >= 6000:
                return True
        
        # Check specs
        for key, value in specs.items():
            if 'ray' in key.lower() and 'tracing' in key.lower():
                return 'yes' in str(value).lower()
        
        return False
    
    def _has_dlss_fsr(self, gpu_name: str, brand: str) -> bool:
        """Check if GPU supports DLSS or FSR"""
        name_lower = gpu_name.lower()
        
        if brand == 'NVIDIA' and 'rtx' in name_lower:
            return True  # RTX cards support DLSS
        elif brand == 'AMD':
            return True  # Most modern AMD cards support FSR
        
        return False
    
    # Motherboard Analysis Helper Methods
    def _extract_motherboard_brand(self, mb_name: str) -> str:
        """Extract motherboard brand"""
        name_lower = mb_name.lower()
        brands = ['asus', 'msi', 'gigabyte', 'asrock', 'evga', 'biostar']
        
        for brand in brands:
            if brand in name_lower:
                return brand.title()
        
        return 'Unknown'
    
    def _extract_chipset(self, specs: Dict) -> str:
        """Extract chipset"""
        for key, value in specs.items():
            if 'chipset' in key.lower():
                return str(value)
        return 'Unknown'
    
    def _extract_form_factor(self, specs: Dict) -> str:
        """Extract form factor"""
        for key, value in specs.items():
            if 'form' in key.lower() and 'factor' in key.lower():
                return str(value)
        return 'Unknown'
    
    def _extract_memory_slots(self, specs: Dict) -> int:
        """Extract number of memory slots"""
        for key, value in specs.items():
            if 'memory' in key.lower() and 'slot' in key.lower():
                slots = extract_numeric_value(str(value))
                if slots:
                    return int(slots)
        return 0
    
    def _extract_max_memory(self, specs: Dict) -> int:
        """Extract maximum memory capacity"""
        for key, value in specs.items():
            if 'max' in key.lower() and 'memory' in key.lower():
                memory = parse_memory_capacity(str(value))
                if memory:
                    return memory
        return 0
    
    def _extract_supported_memory_type(self, specs: Dict) -> str:
        """Extract supported memory type"""
        for key, value in specs.items():
            if 'memory' in key.lower() and 'type' in key.lower():
                return str(value)
        return 'Unknown'
    
    def _extract_pcie_slots(self, specs: Dict) -> Dict[str, int]:
        """Extract PCIe slot configuration"""
        pcie_slots = {}
        for key, value in specs.items():
            if 'pcie' in key.lower():
                # Extract slot type and count
                if 'x16' in str(value):
                    pcie_slots['x16'] = extract_numeric_value(str(value)) or 1
                elif 'x8' in str(value):
                    pcie_slots['x8'] = extract_numeric_value(str(value)) or 1
                elif 'x4' in str(value):
                    pcie_slots['x4'] = extract_numeric_value(str(value)) or 1
                elif 'x1' in str(value):
                    pcie_slots['x1'] = extract_numeric_value(str(value)) or 1
        return pcie_slots
    
    def _extract_sata_ports(self, specs: Dict) -> int:
        """Extract number of SATA ports"""
        for key, value in specs.items():
            if 'sata' in key.lower():
                ports = extract_numeric_value(str(value))
                if ports:
                    return int(ports)
        return 0
    
    def _extract_m2_slots(self, specs: Dict) -> int:
        """Extract number of M.2 slots"""
        for key, value in specs.items():
            if 'm.2' in key.lower() or 'm2' in key.lower():
                slots = extract_numeric_value(str(value))
                if slots:
                    return int(slots)
        return 0
    
    def _extract_usb_ports(self, specs: Dict) -> Dict[str, int]:
        """Extract USB port configuration"""
        usb_ports = {}
        for key, value in specs.items():
            if 'usb' in key.lower():
                if '3.0' in str(value) or '3.1' in str(value) or '3.2' in str(value):
                    usb_ports['USB 3.x'] = extract_numeric_value(str(value)) or 0
                elif '2.0' in str(value):
                    usb_ports['USB 2.0'] = extract_numeric_value(str(value)) or 0
                elif 'usb-c' in str(value).lower():
                    usb_ports['USB-C'] = extract_numeric_value(str(value)) or 0
        return usb_ports
    
    def _extract_ethernet(self, specs: Dict) -> str:
        """Extract ethernet specification"""
        for key, value in specs.items():
            if 'ethernet' in key.lower() or 'lan' in key.lower():
                return str(value)
        return 'Unknown'
    
    def _has_wifi(self, specs: Dict) -> bool:
        """Check if motherboard has WiFi"""
        for key, value in specs.items():
            if 'wifi' in key.lower() or 'wireless' in key.lower():
                return 'yes' in str(value).lower() or 'built-in' in str(value).lower()
        return False
    
    def _has_bluetooth(self, specs: Dict) -> bool:
        """Check if motherboard has Bluetooth"""
        for key, value in specs.items():
            if 'bluetooth' in key.lower() or 'bt' in key.lower():
                return 'yes' in str(value).lower() or 'built-in' in str(value).lower()
        return False
    
    def _extract_price(self, specs: Dict) -> float:
        """Extract price from specifications"""
        for key, value in specs.items():
            if 'price' in key.lower():
                from ..utils.helpers import extract_price
                price = extract_price(str(value))
                if price:
                    return price
        return 0.0
