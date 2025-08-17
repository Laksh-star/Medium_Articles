# Gemma 3 270M Medical Fine-tuning with Unsloth

This repository contains a Jupyter notebook for fine-tuning Google's Gemma 3 270M model on medical data using the Unsloth framework.
Colab notebook from Unsloth-->https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_(270M).ipynb


## Overview

Fine-tunes the compact Gemma 3 270M model on the MedMCQA dataset to create a specialized medical question-answering assistant. The notebook demonstrates how to adapt a general-purpose language model for domain-specific applications using efficient training techniques.

## Features

- **Efficient Training**: Uses LoRA (Low-Rank Adaptation) for parameter-efficient fine-tuning
- **Medical Dataset**: Trained on 15,000 questions from MedMCQA (Indian medical entrance exams)
- **Multiple Output Formats**: Generates LoRA adapters, merged models, and GGUF files
- **Edge Deployment Ready**: Optimized for local inference and offline use

## Requirements

```bash
# Install in Google Colab
!pip install unsloth
!pip install datasets transformers accelerate

# For local setup
pip install unsloth datasets transformers accelerate torch
```

## Quick Start

1. **Open in Google Colab**
   - Upload the notebook to Google Colab
   - Enable GPU runtime (Runtime → Change runtime type → GPU)

2. **Run the Notebook**
   - Execute cells sequentially
   - Training takes ~25 minutes on Colab free tier
   - No additional setup required

3. **Test the Model**
   - The notebook includes medical Q&A testing
   - Compare base vs fine-tuned model responses

## Training Configuration

- **Model**: `unsloth/gemma-3-270m-it`
- **Dataset**: MedMCQA (15,000 samples)
- **Training Steps**: 1,000 (less than 1 epoch)
- **LoRA Rank**: 128 (higher for medical complexity)
- **Learning Rate**: 3e-5
- **Training Time**: ~25 minutes

## Output Files

The notebook generates three model formats:

1. **LoRA Adapters** (`medical_qa_lora/`)
   - Lightweight adapters for development
   - Can be merged with base model

2. **Merged Model** (`medical_qa_merged/`)
   - Full 16-bit model for GPU inference
   - Ready for production deployment

3. **GGUF Model** (`medical_qa_gguf/`)
   - Quantized Q8_0 format (~270MB)
   - Optimized for CPU inference and LM Studio

## Usage Examples

### Testing Medical Questions

```python
question = """A 45-year-old presents with sudden chest pain radiating to the left arm. 
What is the most appropriate initial investigation?
Options:
A) Chest X-ray
B) Echocardiography  
C) 12-lead ECG
D) Cardiac enzymes"""

# Model should respond: "C) 12-lead ECG"
```

### LM Studio Deployment

1. Download the GGUF file from the notebook
2. Install [LM Studio](https://lmstudio.ai/)
3. Load the model file
4. Configure with medical system prompt

## Important Notes

⚠️ **For Educational Use Only**
- This model is for educational and research purposes
- Not suitable for clinical diagnosis or medical advice
- Always recommend consulting healthcare professionals

## Dataset

- **Source**: [MedMCQA](https://huggingface.co/datasets/medmcqa)
- **Size**: 194K+ medical multiple-choice questions
- **Coverage**: 21 medical subjects
- **Origin**: Indian medical entrance examinations

## Performance

- **Training Loss**: Converges within 1,000 steps
- **Memory Usage**: ~8GB GPU memory during training
- **Inference Speed**: 1-3 seconds on modern hardware
- **Model Size**: 270MB (GGUF), ~540MB (full model)

## File Structure

```
├── Gemma3-270-withmedical.ipynb    # Main training notebook
├── README.md                       # This file
└── outputs/                        # Generated models
    ├── medical_qa_lora/           # LoRA adapters
    ├── medical_qa_merged/         # Merged model
    └── medical_qa_gguf/           # GGUF quantized model
```

## Customization

To adapt for other domains:

1. **Replace Dataset**: Modify data loading section (Cell 5)
2. **Adjust Chat Format**: Update conversion function (Cell 6)
3. **Tune Hyperparameters**: Modify LoRA config (Cell 3)
4. **Change System Prompt**: Update medical assistant prompt


## License

This project is for educational use. Please check individual component licenses:
- Gemma 3 270M: [Gemma Terms of Use](https://ai.google.dev/gemma/terms)
- MedMCQA: Check dataset license
- Unsloth: Apache 2.0

## Acknowledgments

- Google DeepMind for Gemma 3 270M
- Unsloth team for the fine-tuning framework
- MedMCQA dataset creators
- Hugging Face for model hosting and tools
