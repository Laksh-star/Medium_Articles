# 🧠 TRIBE Educational Demo

An educational implementation of Meta's TRIBE (Trimodal Brain Encoder) for understanding multimodal brain encoding concepts.

## Overview

This notebook provides a simplified, educational version of the TRIBE model that won first place in the Algonauts 2025 brain encoding competition. While the original research used real fMRI data and billion-parameter foundation models, this demo uses synthetic data to help you understand the core concepts and methodology.

## What You'll Learn

- **Multimodal Brain Encoding**: How to combine visual, audio, and text features to predict brain activity
- **Neural Architecture**: The structure of TRIBE's trimodal fusion approach
- **Attention Mechanisms**: How different modalities are weighted and combined
- **Brain Response Prediction**: Mapping external stimuli to internal neural patterns
- **Performance Evaluation**: Using correlation metrics to assess model quality

## Key Features

### 🎯 **Simplified TRIBE Architecture**
```python
# Educational version with ~1M parameters
class EducationalTRIBE(nn.Module):
    def __init__(self):
        self.visual_encoder = nn.Linear(1408, 256)    # V-JEPA 2 Gigantic dimension
        self.audio_encoder = nn.Linear(1024, 128)     # Wav2Vec2-BERT dimension  
        self.text_encoder = nn.Linear(3072, 256)      # Llama 3.2-3B dimension
        self.attention = nn.MultiheadAttention(...)
        self.brain_predictor = nn.Linear(192, 1000)   # 1000 brain regions
```

### 📊 **Synthetic Data Generation**
- Mathematically generated multimodal features
- Simulated brain responses with realistic noise patterns
- Cross-modal correlations that mirror real neural data

### 🔬 **Educational Experiments**
- Compare unimodal vs. multimodal performance
- Visualize attention weights across modalities
- Analyze regional brain response patterns
- Understand the importance of temporal dynamics

## Performance Comparison

| Metric | Educational Demo | Original TRIBE |
|--------|------------------|----------------|
| **Parameters** | ~1M | 1B |
| **Data** | Synthetic | Real fMRI (4 subjects) |
| **Performance** | Normalized corr = 0.10 | Normalized corr = 0.54 ± 0.1 |
| **Compute** | Google Colab (minutes) | HPC clusters (days) |
| **Purpose** | Learning concepts | Scientific discovery |

## Quick Start

1. **Open the notebook** in Google Colab or Jupyter
2. **Run all cells** to train the educational TRIBE model
3. **Explore the results** through interactive visualizations
4. **Experiment** with different architectural choices

## What Makes This Educational?

### ✅ **Conceptually Accurate**
- Same architectural principles as original TRIBE
- Identical evaluation metrics (Pearson correlation)
- Realistic multimodal fusion strategies

### 🎓 **Simplified for Learning**
- Synthetic data eliminates need for fMRI equipment
- Reduced model size for faster training
- Clear documentation and step-by-step explanations
- Interactive visualizations

### 🔬 **Research-Aligned**
- Based directly on Meta's TRIBE paper methodology
- Uses identical loss functions and optimization approaches
- Demonstrates key findings (multimodal > unimodal)

## Key Insights You'll Discover

1. **Multimodal Fusion Works**: Combining text, audio, and video consistently outperforms single modalities
2. **Attention Matters**: Learned attention weights improve cross-modal integration
3. **Regional Specialization**: Different brain areas respond to different modality combinations
4. **Temporal Dynamics**: Sequential processing enhances prediction accuracy

## Original Research Context

This educational demo is based on:
- **Paper**: "TRIBE: TRImodal Brain Encoder for whole-brain fMRI response prediction"
- **Authors**: Meta AI (Stéphane d'Ascoli, Jérémy Rapin, et al.)
- **Achievement**: 1st place out of 263 teams in Algonauts 2025
- **GitHub**: https://github.com/facebookresearch/algonauts-2025


## Requirements

```bash
pip install torch torchvision numpy matplotlib seaborn plotly
```

## Limitations & Next Steps

**Educational Demo Limitations:**
- Synthetic data doesn't capture real neural complexity
- Simplified architecture misses advanced optimization techniques
- No real-world validation or applications

**Next Steps for Serious Research:**
- Explore the original TRIBE implementation
- Work with real fMRI datasets (Courtois NeuroMod)
- Join the Algonauts community
- Consider computational neuroscience courses


## License

Educational use only. Original TRIBE research: Apache 2.0 License.
