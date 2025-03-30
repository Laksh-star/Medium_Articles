# Poetry Planning Experiment

This repository contains code to explore how Claude approaches poetry writing, specifically whether it plans ahead when crafting rhyming couplets. This experiment was inspired by findings in Anthropic's research paper ["On the Biology of a Large Language Model"](https://transformer-circuits.pub/2025/attribution-graphs/biology.html).

## Overview

Out of curiosity, I decided to run a simple experiment to explore how Claude approaches poetry writing, specifically whether it plans ahead when crafting rhyming couplets. This was inspired by some interesting findings in Anthropic's research about language model interpretability.

## Contents

- `poetry_planning_experiment.py`: Script to collect data from Claude about rhyming couplets with various constraints
- `poetry_planning_analysis.py`: Script to analyze and visualize the results
- `poetry_planning_results.csv`: Generated CSV file containing the experiment results

## Requirements

- Python 3.7+
- Anthropic API key
- Required packages: `anthropic`, `pandas`, `matplotlib`, `seaborn`, `numpy`

## Installation

```bash
pip install anthropic pandas matplotlib seaborn numpy
```

## Usage

1. Replace the placeholder API key in `poetry_planning_experiment.py` with your actual Anthropic API key:

```python
client = anthropic.Anthropic(
    api_key="YOUR_API_KEY_HERE",
)
```

2. Run the data collection script:

```bash
python poetry_planning_experiment.py
```

3. Run the analysis script to generate visualizations and see the results:

```bash
python poetry_planning_analysis.py
```

## Experiment Design

The experiment tests four aspects of Claude's rhyming capabilities:

1. **Base Rhyming**: Establishes baselines for how Claude writes rhyming couplets on different themes without constraints.
2. **Constrained Rhymes**: Tests whether Claude changes its first line when given a specific ending word that must appear at the end of the second line.
3. **Mid-Generation Steering**: Tests Claude's ability to adapt after the first line has already been written.
4. **Planning Hints**: Directly asks Claude to describe its process for creating rhyming couplets.

## Interpreting Results

The analysis calculates the percentage of first lines that differ when Claude is given second-line constraints. A high percentage suggests that Claude is planning ahead—changing how it writes the first line based on knowledge of the required ending for the second line.

The analysis produces two main visualizations:
- **First Line Similarities**: Shows Jaccard similarity between constrained and unconstrained first lines
- **Unique Words**: Shows new words that appear in the first line under different constraints

## License

MIT
