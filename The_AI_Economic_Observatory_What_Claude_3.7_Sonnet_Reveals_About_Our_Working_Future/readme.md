# Claude AI Economic Analysis Tool

This repository contains a Python tool for analyzing Claude AI conversations following the methodology established in Anthropic's Economic Index research reports. The tool allows you to visualize and understand your personal Claude AI usage patterns through the lens of occupational categories, interaction modes, and augmentation vs. automation patterns.

## Overview

Anthropic's Economic Index provides valuable insights into how AI is being used across different occupations and tasks. This tool brings similar analysis capabilities to individual users, allowing you to:

- Categorize your Claude conversations by occupational categories
- Analyze interaction modes (Learning, Task Iteration, Validation, Directive, Feedback Loop)
- Measure augmentation vs. automation patterns in your AI usage
- Track extended thinking mode usage across different task types
- Visualize results through comprehensive dashboards

## Features

- **Occupation Category Classification**: Maps conversations to categories like Computer & Mathematical, Education & Training, Healthcare, etc., following Anthropic's taxonomy
- **Interaction Mode Analysis**: Classifies conversations into five interaction modes (Learning, Task Iteration, Validation, Directive, Feedback Loop)
- **Augmentation/Automation Detection**: Determines whether conversations reflect augmentative or automative patterns
- **Extended Thinking Analysis**: Tracks usage of Claude 3.7 Sonnet's extended thinking mode across different tasks
- **Privacy-Focused**: All analysis happens locally on your machine with no data shared externally
- **Comprehensive Visualization**: Creates detailed dashboards showing your AI usage patterns
- **Exportable Datasets**: Generates datasets similar to those released by Anthropic for further analysis

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/claude-economic-analysis.git
cd claude-economic-analysis

# Install required dependencies
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
import pandas as pd
from claude_analysis import load_user_data, load_and_process_chats, analyze_chats_streamlined

# Load your Claude exports
users_df = load_user_data('users.json')
df = load_and_process_chats('conversations.json', users_df)

# Run the analysis
results, processed_df = analyze_chats_streamlined(df)

# Display visualization dashboard
plt.show()
```

### Creating Datasets

```python
from claude_analysis import create_task_occupation_dataset, save_validation_samples

# Create datasets for further analysis
task_occ_df = create_task_occupation_dataset(processed_df)

# Save sample conversations for validation
save_validation_samples(processed_df)
```

## Input Data

The tool expects Claude conversation exports in the following format:

- `users.json`: Contains user information
- `conversations.json`: Contains Claude conversation history

You can export these files from Claude.ai in your account settings.

## Output

The tool produces several outputs:

1. **Interactive visualization dashboard**: Shows occupation distribution, interaction modes, augmentation vs. automation, extended thinking usage, etc.
2. **Statistics summary**: Provides key metrics about your Claude usage
3. **Datasets**:
   - `task_occupation_analysis.csv`: Maps tasks to occupations with usage metrics
   - `validation_samples.json`: Sample conversations for each category

## Research Methodology

This tool implements the methodology described in Anthropic's Economic Index research:

- [The Anthropic Economic Index](https://www.anthropic.com/news/the-anthropic-economic-index)
- [Economic Tasks AI Paper](https://assets.anthropic.com/m/2e23255f1e84ca97/original/Economic_Tasks_AI_Paper.pdf)

Key concepts from the research:

- **Occupational Categories**: Based on O*NET categories adapted by Anthropic
- **Interaction Modes**:
  - **Learning**: Information gathering and explanation
  - **Task Iteration**: Collaborative refinement of work
  - **Validation**: Verifying or checking work
  - **Directive**: Complete task delegation
  - **Feedback Loop**: More interactive automation scenarios
- **Augmentation vs. Automation**: Whether AI is used to enhance human capabilities (augmentation) or replace human tasks (automation)

## Example Analysis

Here's an example of what the analysis dashboard looks like:

![Claude Analysis Dashboard](dashboard_example.png)

## Limitations

While this tool provides valuable insights, it has some limitations:

- Classification accuracy depends on pattern recognition rather than deep semantic understanding
- Limited to the conversations in your export (no visibility into how outputs are used beyond the conversation)
- Cannot track external factors that might influence usage patterns
- Uses simplified classification compared to Anthropic's more sophisticated Clio platform

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Anthropic for their groundbreaking research on AI's economic impact
- The Claude AI team for creating an API that enables this kind of analysis
