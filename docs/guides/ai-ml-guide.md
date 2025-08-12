# AI/ML PC Build Guide

## 🧠 AI & Machine Learning Workloads

### **What is AI/ML Computing?**
Artificial Intelligence and Machine Learning workloads require specialized hardware for:
- **Training**: Teaching AI models with large datasets
- **Inference**: Running trained models to make predictions
- **Data Processing**: Handling large datasets efficiently

### **Key AI/ML Applications**
- **Local LLM Inference**: Running ChatGPT-like models locally (Llama, Mistral, Phi)
- **Image Generation**: Stable Diffusion, DALL-E alternatives
- **Video Processing**: AI upscaling, frame interpolation
- **Code Assistance**: Local coding AI assistants
- **Research**: Personal ML experimentation
- **Professional Development**: AI/ML software development

---

## 🎮 GPU Requirements for AI/ML

### **NVIDIA Advantages**
- **CUDA Ecosystem**: Mature software stack
- **Tensor Cores**: Specialized AI acceleration
- **NVENC/NVDEC**: Hardware encoding/decoding
- **Software Support**: PyTorch, TensorFlow optimization

#### **RTX 50 Series (Blackwell) - Best for AI/ML (2025)**
| Model | VRAM | Tensor Cores | AI Performance | Price (₹) | Best For |
|-------|------|--------------|----------------|-----------|----------|
| RTX 5090 | 32GB GDDR7 | 5th Gen | Excellent | 2,50,000+ | Professional ML, Large LLMs |
| RTX 5080 | 16GB GDDR7 | 5th Gen | Very Good | 1,50,000+ | Advanced AI, Medium LLMs |
| RTX 5070 Ti | 16GB GDDR7 | 5th Gen | Good | 90,000+ | AI Development, Stable Diffusion |
| RTX 5070 | 12GB GDDR7 | 5th Gen | Good | 70,000+ | Entry AI/ML, Local inference |

#### **RTX 40 Series (Ada Lovelace) - Current Value**
| Model | VRAM | Tensor Cores | AI Performance | Price (₹) | Best For |
|-------|------|--------------|----------------|-----------|----------|
| RTX 4090 | 24GB GDDR6X | 4th Gen | Excellent | 1,80,000+ | Professional ML, Training |
| RTX 4080 Super | 16GB GDDR6X | 4th Gen | Very Good | 1,20,000+ | Advanced AI projects |
| RTX 4070 Ti Super | 16GB GDDR6X | 4th Gen | Good | 85,000+ | AI development |
| RTX 4060 Ti 16GB | 16GB GDDR6 | 4th Gen | Entry | 55,000+ | Basic AI/ML, learning |

### **AMD Considerations**
- **ROCm Support**: Limited but improving
- **OpenCL**: Alternative to CUDA
- **Better Value**: More VRAM per dollar
- **Linux Focus**: Better ROCm support on Linux

#### **RX 7000 Series (RDNA 3)**
| Model | VRAM | AI Support | Performance | Price (₹) | Notes |
|-------|------|------------|-------------|-----------|-------|
| RX 7900 XTX | 24GB GDDR6 | ROCm | Good | 85,000+ | Excellent VRAM/price |
| RX 7900 XT | 20GB GDDR6 | ROCm | Good | 75,000+ | Good value for VRAM |
| RX 7800 XT | 16GB GDDR6 | ROCm | Moderate | 60,000+ | Budget AI option |

---

## 🧮 CPU Considerations for AI/ML

### **High Core Count Priority**
- **Data Preprocessing**: CPU-intensive operations
- **Parallel Training**: Multi-threaded workloads
- **Model Serving**: Multiple inference requests

#### **Intel Options**
| Processor | Cores/Threads | AI Features | Price (₹) | Best For |
|-----------|---------------|-------------|-----------|----------|
| i9-15900K | 24C/32T | Intel AI Boost | 65,000+ | Professional ML |
| i7-15700K | 20C/28T | Intel AI Boost | 45,000+ | AI Development |
| i5-15600K | 14C/20T | Basic AI | 30,000+ | Entry AI/ML |

#### **AMD Options**
| Processor | Cores/Threads | AI Features | Price (₹) | Best For |
|-----------|---------------|-------------|-----------|----------|
| Ryzen 9 9950X | 16C/32T | Ryzen AI | 75,000+ | High-performance ML |
| Ryzen 9 9900X | 12C/24T | Ryzen AI | 55,000+ | AI Development |
| Ryzen 7 9700X | 8C/16T | Ryzen AI | 40,000+ | Entry AI/ML |

---

## 🧠 Memory Requirements

### **System RAM for AI/ML**
- **Minimum**: 32GB DDR5 for serious AI/ML work
- **Recommended**: 64GB DDR5 for large datasets
- **Professional**: 128GB+ for enterprise workloads

#### **Memory Configuration**
```
Entry AI/ML Build:    32GB (2x16GB) DDR5-5600
Advanced AI/ML:       64GB (2x32GB) DDR5-5600  
Professional ML:      128GB (4x32GB) DDR5-5600
```

### **VRAM vs System RAM**
- **VRAM**: Direct GPU processing (model weights)
- **System RAM**: Dataset storage, preprocessing
- **Balance**: Both are important for different tasks

---

## 💾 Storage for AI/ML

### **Dataset Storage Requirements**
- **Fast Access**: NVMe SSDs for active datasets
- **Large Capacity**: HDDs for dataset archives
- **Backup**: Multiple copies of training data

#### **Storage Configuration**
```
AI/ML Storage Setup:
├── 2TB NVMe SSD (Primary) - Models, active datasets
├── 4TB SATA SSD (Secondary) - Processed data, checkpoints  
└── 8TB HDD (Archive) - Raw datasets, backups
```

### **Recommended Storage**
| Component | Capacity | Type | Purpose | Price (₹) |
|-----------|----------|------|---------|-----------|
| Primary SSD | 2TB | NVMe PCIe 4.0 | OS, models, active data | 15,000+ |
| Secondary SSD | 4TB | SATA III | Processed datasets | 25,000+ |
| Archive HDD | 8TB | 7200 RPM | Raw data, backups | 12,000+ |

---

## 🔌 Power Supply for AI/ML

### **High Power Requirements**
AI/ML workloads often run GPUs at 100% utilization for hours.

#### **Power Calculations**
```
Example AI/ML Build:
RTX 4090:           450W
i9-13900K:          150W  
System Components:  100W
Safety Margin:      200W
Total Required:     900W
Recommended PSU:    1000W 80+ Gold
```

#### **PSU Recommendations**
| GPU Configuration | Minimum PSU | Recommended | Price (₹) |
|-------------------|-------------|-------------|-----------|
| Single RTX 4090 | 850W | 1000W Gold | 15,000+ |
| RTX 4080 Super | 750W | 850W Gold | 12,000+ |
| RTX 4070 Ti Super | 650W | 750W Gold | 10,000+ |

---

## 🌡️ Cooling for AI/ML

### **Thermal Management**
- **Extended Load**: AI/ML runs hardware at high load for hours
- **Consistent Performance**: Thermal throttling hurts training
- **Quiet Operation**: Long training sessions need quiet cooling

#### **CPU Cooling**
| Cooler Type | TDP Rating | Noise Level | Price (₹) | Best For |
|-------------|------------|-------------|-----------|----------|
| AIO 360mm | 250W+ | Low | 15,000+ | High-end CPUs |
| AIO 240mm | 200W+ | Moderate | 10,000+ | Mid-range builds |
| Air Tower | 180W+ | Moderate | 5,000+ | Budget builds |

#### **Case Airflow**
```
AI/ML Airflow Setup:
Front: 3x 120mm Intake fans
Top: 2x 140mm Exhaust fans  
Rear: 1x 120mm Exhaust fan
GPU: Custom fan curve for sustained load
```

---

## 🏗️ AI/ML Build Examples

### **Entry AI/ML Build (₹1,50,000)**
```
CPU: AMD Ryzen 7 9700X - ₹40,000
GPU: RTX 4060 Ti 16GB - ₹55,000  
RAM: 32GB DDR5-5600 - ₹15,000
Storage: 1TB NVMe + 2TB HDD - ₹10,000
PSU: 750W 80+ Gold - ₹10,000
Motherboard: B650 - ₹15,000
Case: Mid-tower - ₹5,000
```

### **Professional AI/ML Build (₹3,50,000)**
```
CPU: Intel i9-15900K - ₹65,000
GPU: RTX 4090 24GB - ₹1,80,000
RAM: 64GB DDR5-5600 - ₹40,000
Storage: 2TB NVMe + 4TB SSD - ₹40,000
PSU: 1000W 80+ Platinum - ₹18,000
Motherboard: Z890 - ₹25,000
Case: Full tower - ₹8,000
Cooling: 360mm AIO - ₹15,000
```

### **Extreme AI/ML Workstation (₹6,00,000+)**
```
CPU: Intel i9-15900K - ₹65,000
GPU: RTX 5090 32GB - ₹2,50,000  
RAM: 128GB DDR5-5600 - ₹80,000
Storage: 4TB NVMe + 8TB SSD - ₹80,000
PSU: 1200W 80+ Titanium - ₹25,000
Motherboard: Z890 Extreme - ₹40,000
Case: Workstation case - ₹15,000
Cooling: Custom loop - ₹35,000
```

---

## 🛠️ Software Ecosystem

### **Development Environment**
- **Python**: Primary language for AI/ML
- **CUDA Toolkit**: NVIDIA GPU programming
- **PyTorch**: Popular ML framework
- **TensorFlow**: Google's ML platform
- **Jupyter**: Interactive development

### **Popular AI/ML Applications**
- **Ollama**: Local LLM inference
- **Stable Diffusion**: Image generation  
- **ComfyUI**: Node-based AI workflows
- **Automatic1111**: Stable Diffusion WebUI
- **LM Studio**: Local language model GUI

### **Performance Monitoring**
- **GPU-Z**: GPU monitoring
- **HWiNFO64**: System monitoring  
- **MSI Afterburner**: GPU overclocking
- **Process Monitor**: Resource usage tracking

---

## 📊 Performance Expectations

### **Local LLM Inference**
| Model Size | Required VRAM | Tokens/Second | GPU Recommendation |
|------------|---------------|---------------|-------------------|
| 7B (Llama2) | 8GB+ | 50-100 | RTX 4060 Ti 16GB |
| 13B (Llama2) | 12GB+ | 30-70 | RTX 4070 Ti Super |
| 30B+ | 24GB+ | 10-40 | RTX 4090/5090 |

### **Image Generation (Stable Diffusion)**
| Resolution | Model | Generation Time | GPU Recommendation |
|------------|-------|-----------------|-------------------|
| 512x512 | SD 1.5 | 3-8 seconds | RTX 4060 Ti |
| 768x768 | SDXL | 8-15 seconds | RTX 4070 Ti |
| 1024x1024 | SDXL | 15-30 seconds | RTX 4080/4090 |

---

## 🛒 Where to Buy AI/ML Hardware in India

### **Online Retailers**
- **Amazon.in**: Wide selection, good return policy
- **Flipkart**: Competitive pricing, sales events
- **PrimeABGB**: PC specialist, latest hardware
- **MD Computers**: Good for bulk/professional orders

### **Offline Markets**  
- **Delhi**: Nehru Place - AI/ML specialist vendors
- **Mumbai**: Lamington Road - Custom AI workstations
- **Bangalore**: SP Road - Good for developers
- **Pune**: Computer market near FC Road

### **Professional Vendors**
- **Ant PC**: Custom AI workstations
- **SMC International**: Enterprise AI solutions
- **Supertron**: Professional workstation builder

---

## ⚠️ Common Mistakes

### **Hardware Mistakes**
1. **Insufficient VRAM**: Don't underestimate memory requirements
2. **Poor Cooling**: AI workloads generate significant heat
3. **Inadequate PSU**: High-end GPUs need clean, stable power
4. **Limited Storage**: AI datasets can be massive

### **Software Mistakes**
1. **Wrong CUDA Version**: Ensure framework compatibility
2. **Poor Environment Management**: Use virtual environments
3. **Insufficient Monitoring**: Track resource usage during training
4. **No Backup Strategy**: Always backup training data and models

---

## 🎯 Future Considerations

### **Emerging Technologies**
- **NPUs**: Dedicated Neural Processing Units
- **HBM Memory**: Higher bandwidth for AI workloads
- **PCIe 5.0**: Better GPU-CPU communication
- **DDR5**: Essential for large dataset processing

### **Market Trends**
- **Local AI**: Growing demand for on-device inference
- **Open Source Models**: More accessible AI development
- **Hardware Efficiency**: Better performance per watt
- **Indian AI Ecosystem**: Growing local development community

---

*AI/ML workloads require different hardware considerations than traditional computing. Focus on VRAM, sustained performance, and adequate cooling for optimal results.*
