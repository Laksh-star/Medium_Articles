# Six Thinking Hats with CrewAI Flows

This repository contains an implementation of Edward de Bono's Six Thinking Hats methodology using CrewAI Flows. The system creates an AI-powered decision-making pipeline that analyzes problems from multiple perspectives.

## Features

- Implementation of all six thinking perspectives (White, Red, Black, Yellow, Green, Blue)
- Additional synthesis and implementation planning agents
- YAML-based configuration for easy customization
- Structured decision output in markdown format

## Prerequisites

- Python 3.10+
- CrewAI 0.80.0+
- OpenAI API key or compatible LLM setup

## Installation

```bash
pip install torch matplotlib crewai crewai_tools
```

## Configuration

The system uses two YAML files:
- `config/six_hats_agents.yaml`: Agent definitions
- `config/six_hats_tasks.yaml`: Task specifications

## Usage

1. Set up your environment variables:
```python
import os
os.environ['OPENAI_MODEL_NAME'] = 'your-model-name'
os.environ['OPENAI_API_KEY'] = 'your-api-key'
```

2. Run the decision-making pipeline:
```python
flow = DecisionMakingPipeline()
result = flow.kickoff()
```

3. Save the analysis results:
```python
save_decision_results(result)
```

## Output

The system generates a comprehensive decision analysis including:
- Factual information (White Hat)
- Emotional considerations (Red Hat)
- Risk assessment (Black Hat)
- Benefits analysis (Yellow Hat)
- Creative solutions (Green Hat)
- Process management (Blue Hat)

## License

MIT

## Acknowledgments

- Edward de Bono's Six Thinking Hats methodology
- CrewAI team for their framework
- DeepLearning.AI for their course on practical multi-agent systems
