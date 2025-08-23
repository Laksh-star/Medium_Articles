# PH-LLM Independent Validation

A simple testing framework to validate Google's Personal Health Large Language Model (PH-LLM) claims by comparing it against major commercial AI models on health coaching tasks.

## Overview

This repository contains code to reproduce and validate the findings from Google's Nature Medicine paper "A personal health large language model for sleep and fitness coaching." When the original authors' code proved difficult to run, we built this independent framework to test their claims.

## What This Does

- Tests multiple AI models (GPT-4, GPT-5, Claude) on the same health coaching cases used to evaluate PH-LLM
- Implements the paper's 15-criteria evaluation rubric
- Compares performance against PH-LLM's published benchmarks (4.61/5 for sleep cases)
- Provides statistical analysis and visualizations

## Key Findings

Our testing validated Google's claims:
- **PH-LLM: 4.61/5** (specialized health model)
- **GPT-4 Turbo: 4.20/5** (best general model, -0.41 gap)
- **Claude Sonnet: 4.09/5** (-0.52 gap)
- **GPT-5: 3.84/5** (-0.77 gap, surprisingly lower than GPT-4)

## Requirements

```bash
pip install openai anthropic pandas numpy matplotlib seaborn scipy
```

## Setup

1. Clone this repository
2. Download the PH-LLM dataset:
   ```bash
   git clone https://github.com/Google-Health/consumer-health-research.git
   ```
3. Set your API keys:
   ```python
   api_keys = {
       'openai': 'sk-...',      # Your OpenAI API key
       'anthropic': 'sk-ant-...', # Your Anthropic API key (optional)
   }
   ```

## Usage

### Basic Testing
```python
# Load the dataset
sleep_data = load_jsonl('consumer-health-research/phllm/data/sleep_case_studies.all.jsonl')
fitness_data = load_jsonl('consumer-health-research/phllm/data/fitness_case_studies.all.jsonl')

# Initialize testing framework
dataset = PHLLMDataset(sleep_data, fitness_data)
evaluator = PHLLMEvaluator()

# Run comparison
results = run_complete_evaluation_fixed()
```

### Key Components

- `PHLLMDataset`: Loads and parses the case study data
- `PHLLMEvaluator`: Creates prompts and manages evaluation
- `DetailedEvaluationRubric`: Implements the 15-criteria scoring system
- `RealModelTester`: Handles API calls to different AI models
- `ComprehensiveModelComparison`: Runs full comparisons and generates reports

## File Structure

```
├── dataset_loader.py          # Load PH-LLM case studies
├── evaluator.py              # Evaluation framework and prompts
├── model_tester.py           # API integrations for different models
├── comparison.py             # Comprehensive testing and analysis
├── analysis.py               # Statistical analysis and visualization
└── run_evaluation.py         # Main execution script
```

## Sample Output

```
🏆 OVERALL PERFORMANCE RANKING:
  1. GPT-4: 4.20/5 (n=3 cases)
  2. Claude: 4.09/5 (n=3 cases)
  3. Simulated: 3.47/5 (n=3 cases)

📈 STATISTICAL ANALYSIS:
Best performing model: GPT-4 (4.20/5)
PH-LLM baseline: 4.61/5
Gap to PH-LLM: -0.41
```

## Models Tested

- **OpenAI**: GPT-4 Turbo, GPT-4, GPT-5 variants
- **Anthropic**: Claude Sonnet
- **Baseline**: Simple rule-based system

## Evaluation Criteria

The 15-criteria rubric evaluates:
1. Domain knowledge usage
2. Data interpretation quality
3. Personalization appropriateness
4. Safety considerations
5. Recommendation actionability
6. Response structure and clarity
7. ... (see `DetailedEvaluationRubric` for complete list)

## Limitations

- **Small sample size**: Tested on 3 cases per model vs. original study's 2,606+ ratings
- **Automated evaluation**: Uses rule-based scoring vs. human expert evaluation
- **Aggregate comparison**: Compares against published PH-LLM averages, not direct responses
- **API costs**: Testing multiple models can be expensive


## Citation

If you use this code, please cite both the original paper and this validation work:

```bibtex
@article{tu2024personal,
  title={A personal health large language model for sleep and fitness coaching},
  author={Tu, Tao and others},
  journal={Nature Medicine},
  year={2024}
}
```

## License

MIT License - see LICENSE file for details.


---

*This is an independent validation of Google's research. Not affiliated with Google Health.*
