# Multi-Agent Content Generation System

A sophisticated content generation system that leverages multiple AI agents and web research capabilities to create high-quality articles.

## 🌟 Features

- **Multi-Agent Architecture**: Employs three specialized agents:
  - Research Agent: Conducts web research using Tavily API
  - Writer Agent: Creates content based on research findings
  - Editor Agent: Polishes and optimizes the final content

- **Web Research Integration**: Utilizes Tavily API for accurate and up-to-date information
- **Automated Pipeline**: Seamless flow from research to writing to editing
- **File Management**: Saves all outputs including research data, drafts, and final content
- **Error Handling**: Robust error management and logging system

## 🚀 Getting Started

### Prerequisites

```bash
pip install llama-stack==0.0.36 llama-stack-client==0.0.35 nest_asyncio tavily-python
```

### API Keys Required

- Together AI API key (for LlamaStack)
- Tavily API key (for web research)

### Configuration

1. Replace the API keys in the code:
```python
os.environ["TOGETHER_API_KEY"] = "your-together-api-key"
# In ResearchAgent class:
self.tavily_client = TavilyClient(api_key="your-tavily-api-key")
```

### Running the System

```python
python main.py
```

## 📂 Output Structure

The system generates several files in the `article_outputs` directory:

- `raw_search_results_{timestamp}.md`: Raw search results from Tavily
- `processed_research_data_{timestamp}.md`: Formatted research findings
- `writer_draft_{timestamp}.md`: Initial article draft
- `editor_revision_{timestamp}.md`: Final edited article
- `generation_report_{timestamp}.md`: Overview of the generation process

## 🔄 Pipeline Process

1. **Research Phase**
   - Extracts search query from topic
   - Conducts web search via Tavily API
   - Processes and saves research findings

2. **Writing Phase**
   - Creates article based on research data
   - Incorporates key insights and examples
   - Maintains consistent structure and style

3. **Editing Phase**
   - Reviews and improves content
   - Optimizes for SEO and readability
   - Provides improvement suggestions

## 🛠️ Customization

You can customize various aspects:
- Modify agent instructions in each agent class
- Adjust the number of search results used
- Change the output format and structure
- Add new agents or modify the pipeline

## 📝 Error Handling

The system includes comprehensive error handling:
- Saves error logs with timestamps
- Graceful fallbacks for search failures
- Detailed error reporting in the generation report

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Llama Stack
- Uses Tavily API for web research
- Inspired by multi-agent AI systems

## 📮 Contact

For questions and support, please open an issue in the GitHub repository.