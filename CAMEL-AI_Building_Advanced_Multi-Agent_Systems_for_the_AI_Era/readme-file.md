# Multi-perspective News Analysis System

A collaborative AI system that analyzes news topics from multiple perspectives using the CAMEL framework.

## Overview

This project implements a multi-agent news analysis system that examines current events from different political, historical, and media perspectives. It uses the CAMEL (Communicative Agents for Mind Exploration of Large Language Model Society) framework to coordinate specialized AI agents working together to create comprehensive, balanced analyses.

## Features

- **Multi-perspective Analysis**: Examines topics from progressive, conservative, and centrist political viewpoints
- **Factual Research**: Includes a research agent with search capabilities to gather verifiable facts
- **Historical Context**: Connects current events to historical patterns and precedents
- **Media Literacy**: Analyzes how different media outlets frame and cover the topic
- **Comprehensive Synthesis**: Integrates all perspectives into a balanced overview

## System Architecture

The system consists of seven specialized agents:

1. **Fact Gatherer**: Researches and compiles factual information about the topic
2. **Progressive Analyst**: Examines the topic from a progressive/left-leaning perspective
3. **Conservative Analyst**: Analyzes the topic from a conservative/right-leaning viewpoint
4. **Centrist Analyst**: Provides a moderate/centrist perspective
5. **Historical Context Analyst**: Connects the topic to relevant historical patterns
6. **Media Bias Analyst**: Examines how different media outlets cover the topic
7. **Synthesis Specialist**: Integrates all perspectives into a cohesive analysis

## Setup

### Requirements

- Python 3.8+
- CAMEL AI library
- OpenAI API key
- Google API key
- Google Custom Search Engine ID

### Installation

1. Install the CAMEL AI library:
```bash
pip install "camel-ai[all]==0.2.16"
```

2. Install other dependencies:
```bash
pip install nest_asyncio
```

3. Set up your API keys:
```python
os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"
os.environ["GOOGLE_API_KEY"] = "your_google_api_key_here"
os.environ["SEARCH_ENGINE_ID"] = "your_search_engine_id_here"
```

## Usage

```python
# Import the main function
from news_analysis import analyze_news_topic

# Analyze a topic
result = analyze_news_topic("Recent Supreme Court ruling on social media regulation")

# View the analysis
print(result["summary"])
print("Full analysis saved to:", result["full_analysis_file"])
```

## Output

The system generates a comprehensive markdown file with the following sections:

- Executive Summary
- Factual Background
- Progressive Perspective
- Conservative Perspective
- Centrist Perspective
- Historical Context
- Media Coverage Analysis

## Acknowledgments

This project is built upon the CAMEL (Communicative Agents for Mind Exploration of Large Language Model Society) framework developed by the CAMEL AI team. The implementation was inspired by their "Create A Hackathon Judge Committee with Workforce" notebook example.

For more information about CAMEL:
- [CAMEL GitHub Repository](https://github.com/camel-ai/camel)
- [CAMEL Documentation](https://docs.camel-ai.org/)

## License

[MIT License](LICENSE)
