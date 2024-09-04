# Multi-Strategy Business Analysis

## Overview

This project implements a **Multi-Strategy Business Analysis** framework to analyze business data and generate actionable insights using AI-driven natural language processing techniques. The framework covers multiple dimensions, including customer feedback, competitor profiles, market research, and innovation roadmaps, with a focus on the AI and IoT industries.

The project leverages **LLM-based models** (GPT-4) to analyze unstructured data from company records, market reports, and customer feedback, providing strategic recommendations. It also supports **Blue Ocean Strategy** by identifying untapped market opportunities and value innovation.

## Disclaimer

The company name **InnoWave Inc.** used in this project is fictitious and created for illustrative purposes. InnoWave is the name of an actual company, but this project is in no way affiliated with or related to the real InnoWave. All content, data, and scenarios presented in this project are purely fictional.

## Features

- **Automated Query Refinement**: Refines vague strategy queries into actionable insights.
- **Company History Analysis**: Extracts strategic insights based on historical performance.
- **Market and Competitive Analysis**: Compares the company with competitors and analyzes market conditions.
- **Blue Ocean Strategy**: Identifies opportunities for differentiation and value innovation using the Four Actions Framework.
- **Customizable Workflow**: Adaptable for any company by inputting relevant reports and market data.
- **Partial Generation Strategy**: Generates recommendations even if partial data is available.

## Dependencies

- **Python 3.x**
- **LlamaIndex**: A package for managing data indexing.
- **OpenAI API**: For GPT-based model usage in query analysis and text generation.
- **Asyncio**: For handling asynchronous operations.
- **Nest Asyncio**: To run asyncio in Jupyter environments.

Install dependencies:

```bash
pip install llama_index openai asyncio nest_asyncio
```

## Setup

### OpenAI API Key
Set up your OpenAI API key:

```bash
export OPENAI_API_KEY="your-api-key"
```

### Directory Setup
Create a `data/` directory to store company history, market reports, and documents for analysis.

```bash
mkdir data
```

### Running the Workflow

Run the following code to execute the workflow:

```python
import asyncio
from your_script import BusinessStrategyWorkflow  # Ensure correct import

async def run_workflow():
    workflow = BusinessStrategyWorkflow(timeout=600, verbose=True)
    result = await workflow.run(query="How can InnoWave create new demand in the IoT market?", company_id="innowave")
    print(result)

# Running the workflow
asyncio.get_event_loop().run_until_complete(run_workflow())
```

## Customization

To adapt this framework for any company, update the company-specific files (e.g., annual reports, market research) in the `data/` folder, and adjust the queries and workflow steps as needed.

## Sample Queries

- "What new market opportunities can [Company Name] explore in AI-driven healthcare?"
- "Analyze the competitive landscape for [Company Name] and identify value innovation opportunities."
- "How can [Company Name] apply the Four Actions Framework to create a Blue Ocean?"

## License

This project is licensed under the MIT License.

