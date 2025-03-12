# Building Observable AI Agents with Arize Phoenix

This repository contains code and resources for building observable AI agents using Arize Phoenix, as described in the accompanying Medium article.

## Overview

AI agents are becoming increasingly complex, combining LLMs with tools, memory, and planning capabilities. However, traditional testing methods fall short for these systems. This project demonstrates how to implement comprehensive observability and evaluation for an AI agent using Arize Phoenix.

The repository contains a movie recommendation agent implementation that showcases:

1. Agent architecture with router and specialized tools
2. OpenTelemetry instrumentation for tracing
3. Multiple evaluation methods (LLM-as-judge, code-based)
4. Structured experiments for agent improvement

## Repository Contents

- `Medium_Phoenix_test_movieagent.ipynb`: Jupyter notebook with the complete implementation of a movie recommendation agent with Phoenix observability
- Supporting documentation and design files for the Medium article

## Agent Architecture

The movie recommendation agent consists of:

- **Router**: Uses GPT-4o-mini to decide which tool to call based on the user query
- **Tools**:
  - `lookup_movie_data`: Simulates database queries for movie information
  - `analyze_movie_trends`: Analyzes patterns in movie data
  - `generate_visualization`: Creates Python code for data visualization

## Observability Implementation

The implementation uses Arize Phoenix with OpenTelemetry to trace agent execution:

```python
from phoenix.otel import register
tracer_provider = register()
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)
```

## Evaluation Framework

Five evaluators are implemented to assess different aspects of agent performance:

1. **Function Calling**: Evaluates if the router selected the appropriate tool
2. **SQL Result**: Verifies if database queries produce expected results
3. **Clarity**: Assesses if responses are clear and well-structured
4. **Entity Correctness**: Checks if entities in responses match the query
5. **Code Runnability**: Tests if generated Python visualization code is executable

## Running Experiments

The notebook demonstrates how to:

1. Create a test dataset with expected outputs
2. Run the agent on test queries
3. Apply multiple evaluators to assess performance
4. Implement improvements (e.g., enhanced prompts)
5. Compare experiment results

## Getting Started

To run this code:

1. Clone the repository
2. Install the required dependencies:
   ```
   pip install arize-phoenix arize-phoenix-otel openinference-instrumentation-openai openai pandas matplotlib
   ```
3. Set up environment variables for your API keys
4. Run the Jupyter notebook

## Requirements

- Python 3.8+
- OpenAI API key
- Jupyter notebook environment

## Related Resources

- [Evaluating AI Agents](https://learn.deeplearning.ai/courses/evaluating-ai-agents/) - deeplearning.ai course
- [Arize Phoenix Documentation](https://docs.arize.com/phoenix/)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Arize AI for developing Phoenix
- deeplearning.ai for the "Evaluating AI Agents" course
